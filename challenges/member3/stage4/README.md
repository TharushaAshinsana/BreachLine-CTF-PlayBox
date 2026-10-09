# S4 — Intercepted Comms

Owner: Member 3 — IT24100054
Domain: Cryptography
Target difficulty: Moderate
Status: Prototype integrated with S3 evidence delivery and CTFd.
Final group flag and S5 clue alignment pending.

## Challenge

Recover an intercepted English communication encrypted with
repeating-key XOR and exported as hexadecimal.

Players receive:
- player/intercepted_ciphertext.hex
- player/clue.txt

Players download these files through the Stage 3 admin portal.

Admin and solver files must not be distributed to players.

## Requirements

Python 3. No third-party Python packages are required.

Run commands from the BreachLine-CTF-PlayBox project root.

## Generate / Reset — Windows

    py challenges/member3/stage4/admin/generate.py

## Solve — Windows

    py challenges/member3/stage4/solver/solve.py

## Generate / Reset — Ubuntu

    python3 challenges/member3/stage4/admin/generate.py

## Solve — Ubuntu

    python3 challenges/member3/stage4/solver/solve.py

## Intended Solution

1. Decode hexadecimal into ciphertext bytes.
2. Use the known communication header from the clue.
3. XOR the header with the corresponding ciphertext bytes.
4. Identify the shortest repeating key-stream pattern.
5. Repeat the recovered key to decrypt the complete message.
6. Extract the flag and the clue for S5.

The solver does not import or read the generator.

## S3 Evidence Delivery

Docker Compose mounts the player directory read-only into s3-web:

    ./challenges/member3/stage4/player:/app/s4-evidence:ro

Evidence routes:
- /evidence/s4/intercepted_ciphertext.hex
- /evidence/s4/clue.txt

An unauthenticated ciphertext request redirected to the login page.
Both files returned HTTP 200 during authenticated testing.

## CTFd Configuration

- Name: S4 — Intercepted Comms
- Category: Cryptography
- Type: Standard
- Points: 100 for prototype testing
- State: Visible
- Flag type: Static, case sensitive
- Development flag: NOVATECH{xor_key_reuse}

Files are delivered through the S3 portal rather than attached
directly to the CTFd challenge.

Two hints were saved with a cost of 0 for prototype testing:

1. Convert the hexadecimal text into bytes. Compare the beginning
   with the known communication header in clue.txt.
2. For XOR, ciphertext XOR known plaintext reveals the key stream.
   Look for its shortest repeating pattern.

## Reset Behaviour

Running the generator overwrites the player ciphertext with the
baseline version defined in the generator.

It does not reset CTFd accounts, submissions, scores or challenge
unlocks.

If the flag changes, regenerate the ciphertext and update the
CTFd static flag to match.

## Current Manual Verification

- Generator completed successfully during standalone testing.
- S4 ciphertext and clue downloaded successfully through S3.
- Project solver recovered key length 5 and key ORBIT.
- Solver recovered the English message and development flag.
- CTFd accepted the correct flag during submission testing.
- The test team received 100 points on the scoreboard.
- Two hints saved in CTFd; player visibility check pending.

## Pending Integration

- Confirm the group's final flag format and replace the development flag.
- Align the decrypted S5 clue with the actual forensic challenge.
- Verify both hints are accessible from a player account.
- Verify an incorrect flag is rejected, if not already tested.
- Decide whether CTFd should enforce an S3 solve prerequisite.
- Test the final player package and complete stage progression.

## Attribution

Record assistance and external resources used during development.
Development guidance, initial code, integration guidance and
verification support were provided with ChatGPT assistance.

## Current Manual Verification

- Generator completed successfully during standalone testing.
- S4 ciphertext and clue downloaded successfully through S3.
- Project solver recovered key length 5 and key ORBIT.
- Solver recovered the English message and development flag.
- CTFd accepted the correct flag during submission testing.
- The test team received 100 points on the scoreboard.
- Both CTFd hints opened successfully from the test player account.
- CTFd rejected an incorrect flag during player testing.

## Pending Integration

- Confirm the group's final flag format and replace the development flag.
- Align the decrypted S5 clue with the actual forensic challenge.
- Verify an incorrect flag is rejected, if not already tested.
- Decide whether CTFd should enforce an S3 solve prerequisite.
- Test the final player package and complete stage progression.
- Verify an incorrect flag is rejected, if not already tested.