from pathlib import Path

# Find stage4 regardless of the terminal's current directory.
STAGE_DIR = Path(__file__).resolve().parents[1]
PLAYER_DIR = STAGE_DIR / "player"
PLAYER_DIR.mkdir(parents=True, exist_ok=True)

# Development values: confirm the final flag format with your group.
KEY = b"ORBIT"

MESSAGE = """NOVATECH INTERNAL COMMUNICATION
The portal access has been confirmed.
We reused the same short key throughout this transmission.
The server evidence contains authentication logs and shell history.
Investigate the deleted artifact in the next stage.
Development flag: NOVATECH{xor_key_reuse}
END OF TRANSMISSION
"""

plaintext = MESSAGE.encode("utf-8")

# Repeat the key and XOR each plaintext byte with its matching key byte.
ciphertext = bytes(
    value ^ KEY[index % len(KEY)]
    for index, value in enumerate(plaintext)
)

output_path = PLAYER_DIR / "intercepted_ciphertext.hex"
output_path.write_text(ciphertext.hex() + "\n", encoding="utf-8")

print(f"Created: {output_path}")
print(f"Plaintext size: {len(plaintext)} bytes")
print(f"Ciphertext size: {len(ciphertext)} bytes")