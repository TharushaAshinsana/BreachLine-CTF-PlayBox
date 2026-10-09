from pathlib import Path

STAGE_DIR = Path(__file__).resolve().parents[1]
cipher_path = STAGE_DIR / "player" / "intercepted_ciphertext.hex"

ciphertext = bytes.fromhex(
    cipher_path.read_text(encoding="utf-8").strip()
)

# Taken from the player-facing clue, not from the generator.
known_header = b"NOVATECH INTERNAL COMMUNICATION"

if len(ciphertext) < len(known_header):
    raise SystemExit("Ciphertext is shorter than the known header.")

# C XOR P reveals the corresponding key-stream bytes.
key_stream = bytes(
    ciphertext[i] ^ known_header[i]
    for i in range(len(known_header))
)

# Search for a short period, with at least three observed repeats.
key = None

for length in range(1, len(key_stream) // 3 + 1):
    candidate = key_stream[:length]

    if all(
        value == candidate[i % length]
        for i, value in enumerate(key_stream)
    ):
        key = candidate
        break

if key is None:
    raise SystemExit("No short repeating key found using this header.")

plaintext = bytes(
    value ^ key[i % len(key)]
    for i, value in enumerate(ciphertext)
)

try:
    message = plaintext.decode("utf-8")
except UnicodeDecodeError:
    raise SystemExit("Recovered candidate did not produce valid UTF-8.")

print(f"Recovered key length: {len(key)}")
print(f"Recovered key: {key!r}")
print("\nDecrypted message:\n")
print(message)