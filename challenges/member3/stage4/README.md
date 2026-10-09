# S4 — Intercepted Comms

Owner: Member 3 — IT24100054
Domain: Cryptography
Target difficulty: Moderate
Status: Standalone prototype; platform integration pending.

## Challenge

Recover an intercepted English communication encrypted with
repeating-key XOR and exported as hexadecimal.

Players receive:
- player/intercepted_ciphertext.hex
- player/clue.txt

Admin and solver files must not be distributed to players.

## Requirements

Python 3. No third-party Python packages are required.

Run commands from the NovaTech-Member3 project root.

## Generate / Reset — Windows

    py stage4/admin/generate.py

## Solve — Windows

    py stage4/solver/solve.py

## Generate / Reset — Ubuntu

    python3 stage4/admin/generate.py

## Solve — Ubuntu

    python3 stage4/solver/solve.py

## Intended Solution

1. Decode hexadecimal into ciphertext bytes.
2. Use the known communication header from the clue.
3. XOR the header with the corresponding ciphertext bytes.
4. Identify the shortest repeating key-stream pattern.
5. Repeat the recovered key to decrypt the complete message.
6. Extract the flag and the clue for S5.

The solver does not import or read the generator.

## Reset Behaviour

Running the generator overwrites the player ciphertext with the
baseline version defined in the generator. It does not reset CTFd
accounts, submissions, scores or challenge unlocks.

## Current Manual Verification

- Generator completed successfully.
- Plaintext size: 311 bytes.
- Ciphertext size: 311 bytes.
- Solver recovered a key length of 5.
- Solver recovered the key and displayed the original message.

## Pending Integration

- Confirm the group's final flag format and replace the development flag.
- Agree how S3 leads to or unlocks S4.
- Align the decrypted S5 clue with the actual forensic challenge.
- Configure flag validation and hints in CTFd.
- Test the final player package and complete stage progression.

## Attribution

Record assistance and external resources used during development.
Development guidance and initial code were provided with ChatGPT assistance.