from pathlib import Path
import gzip
import hashlib
import shutil
import subprocess
import tempfile

STAGE = Path(__file__).resolve().parents[1]
PLAYER = STAGE / "player"
IMAGE = PLAYER / "server_image.dd"

def run(*args):
    return subprocess.run(
        args, check=True, capture_output=True, text=True
    )

def main():
    for tool in ("mkfs.ext4", "debugfs"):
        if shutil.which(tool) is None:
            raise SystemExit(f"Missing tool: {tool}")

    PLAYER.mkdir(parents=True, exist_ok=True)

    # Create only the challenge image file; no physical disks are used.
    with IMAGE.open("wb") as image:
        image.truncate(32 * 1024 * 1024)

    run(
        "mkfs.ext4", "-q", "-F",
        "-E", "lazy_itable_init=0,lazy_journal_init=0",
        str(IMAGE),
    )

    with tempfile.TemporaryDirectory(prefix="novatech-s5-") as temp:
        work = Path(temp)

        (work / "auth.log").write_text(
            "Oct 09 02:10:01 server-core sshd[2100]: "
            "Failed password for backup from 192.0.2.44 port 44010 ssh2\n"
            "Oct 09 02:12:08 server-core sshd[2110]: "
            "Accepted publickey for analyst from 192.0.2.44 port 44012 ssh2\n"
            "Oct 09 02:12:09 server-core sshd[2110]: "
            "session opened for user analyst\n"
            "Oct 09 02:18:40 server-core sshd[2110]: "
            "session closed for user analyst\n",
            encoding="utf-8",
        )

        (work / "history").write_text(
            "whoami\n"
            "hostname\n"
            "cd /var/tmp\n"
            "ls -l\n"
            "gzip -k transfer_notes.txt\n"
            "rm transfer_notes.txt\n"
            "sha256sum transfer_notes.txt.gz\n"
            "rm transfer_notes.txt.gz\n"
            "exit\n",
            encoding="utf-8",
        )

        recovered_message = (
            "NOVATECH INCIDENT - TRANSFER NOTES\n"
            "Correlate the analyst SSH session with the shell history.\n"
            "This archive was removed from /var/tmp after the session.\n"
            "Flag: NOVATECH{deleted_transfer_recovered}\n"
            "Next stage: inspect exfil_tool.elf and reconstruct its "
            "input-validation logic.\n"
        )

        (work / "notes.gz").write_bytes(
            gzip.compress(
                recovered_message.encode("utf-8"), mtime=0
            )
        )

        commands = [
            "mkdir /var",
            "mkdir /var/log",
            "mkdir /var/tmp",
            "mkdir /home",
            "mkdir /home/analyst",
            f"write {work / 'auth.log'} /var/log/auth.log",
            f"write {work / 'history'} /home/analyst/.bash_history",
            f"write {work / 'notes.gz'} /var/tmp/transfer_notes.txt.gz",
            "rm /var/tmp/transfer_notes.txt.gz",
        ]

        batch = work / "commands.txt"
        batch.write_text("\n".join(commands) + "\n", encoding="utf-8")

        result = run("debugfs", "-w", "-f", str(batch), str(IMAGE))
        print(result.stdout)
        print(result.stderr)

    (PLAYER / "clue.txt").write_text(
        "NovaTech Incident Evidence - Server Image\n\n"
        "Analyse this synthetic filesystem image without modifying it.\n"
        "Correlate authentication logs and shell history.\n"
        "Locate and recover the deleted compressed artifact.\n"
        "Recover the flag and the clue for the next stage.\n",
        encoding="utf-8",
    )

    digest = hashlib.sha256(IMAGE.read_bytes()).hexdigest()
    (PLAYER / "server_image.dd.sha256").write_text(
        f"{digest}  server_image.dd\n", encoding="utf-8"
    )

    print(f"Created: {IMAGE}")
    print(f"Size: {IMAGE.stat().st_size} bytes")
    print(f"SHA256: {digest}")
    print("Generation finished; recovery verification is still required.")

if __name__ == "__main__":
    main()
