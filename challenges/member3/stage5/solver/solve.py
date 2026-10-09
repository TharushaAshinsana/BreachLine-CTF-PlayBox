from pathlib import Path
import gzip
import hashlib
import re
import shutil
import subprocess

STAGE = Path(__file__).resolve().parents[1]
IMAGE = STAGE / "player" / "server_image.dd"
OUTPUT = STAGE / "solver" / "recovered"


def run(*args):
    return subprocess.run(
        args, check=True, capture_output=True
    ).stdout


def main():
    for tool in ("debugfs", "fls", "icat"):
        if shutil.which(tool) is None:
            raise SystemExit(f"Missing tool: {tool}")

    before = hashlib.sha256(IMAGE.read_bytes()).hexdigest()

    logs = run(
        "debugfs", "-R", "cat /var/log/auth.log", str(IMAGE)
    ).decode("utf-8")

    history = run(
        "debugfs", "-R",
        "cat /home/analyst/.bash_history", str(IMAGE)
    ).decode("utf-8")

    print("=== Authentication logs ===")
    print(logs)
    print("=== Shell history ===")
    print(history)

    names = re.findall(
        r"^rm\s+([A-Za-z0-9_.-]+\.gz)\s*$",
        history, re.MULTILINE
    )
    if len(names) != 1:
        raise SystemExit("Expected one deleted gzip archive in history.")

    filename = names[0]
    deleted = run("fls", "-r", "-d", str(IMAGE)).decode("utf-8")

    print("=== Deleted entries ===")
    print(deleted)

    candidates = []
    for line in deleted.splitlines():
        match = re.match(r"^\S+\s+\*\s+(\d+):\s+(.+)$", line)
        if match and Path(match.group(2)).name == filename:
            candidates.append(match.groups())

    if len(candidates) != 1:
        raise SystemExit("Could not uniquely identify the deleted archive.")

    inode, evidence_path = candidates[0]
    print(f"Recovering {evidence_path}, inode {inode}")

    archive = run("icat", "-r", str(IMAGE), inode)
    plaintext = gzip.decompress(archive).decode("utf-8")

    OUTPUT.mkdir(parents=True, exist_ok=True)
    (OUTPUT / filename).write_bytes(archive)
    (OUTPUT / "transfer_notes.txt").write_text(
        plaintext, encoding="utf-8"
    )

    print("\n=== Recovered message ===")
    print(plaintext)

    flag = re.search(r"NOVATECH\{[^}\r\n]+\}", plaintext)
    if flag is None:
        raise SystemExit("No flag found in recovered content.")

    after = hashlib.sha256(IMAGE.read_bytes()).hexdigest()
    if before != after:
        raise SystemExit("ERROR: Evidence image changed.")

    print("Recovered flag:", flag.group())
    print("Evidence unchanged: SHA256 verified.")


if __name__ == "__main__":
    main()
