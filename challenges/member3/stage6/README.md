# S6 — The Exfiltration Tool

Owner: Member 3 — IT24100054
Domain: Reverse Engineering
Target difficulty: Hard (capstone), pending peer review.
Status: Working prototype integrated with CTFd.

## Challenge

Analyse a synthetic offline Linux executable, reconstruct its
input-validation logic, and recover the required token.

The executable prints the final flag for the correct token.
It performs no network communication or actual exfiltration.

## Player Files

- player/exfil_tool.elf
- player/exfil_tool.elf.sha256
- player/clue.txt

Distribute only player files.
Do not distribute admin source, solver code or analysis outputs.

## Requirements

Build environment: Ubuntu Linux x86-64 or Ubuntu on WSL 2.

    sudo apt install build-essential binutils python3 file

Optional analysis tools: Ghidra and gdb.

The player binary is statically linked and stripped.
Windows users can run it through Ubuntu on WSL 2.

Run project commands from the BreachLine-CTF-PlayBox root.

## Build / Rebuild

    bash challenges/member3/stage6/admin/build.sh

The script compiles the C source, strips symbols and generates
the SHA256 checksum.

Compiler and library versions may affect the rebuilt binary
and its addresses.

## Solve

    python3 challenges/member3/stage6/solver/solve.py

The solver reads target bytes from the ELF LOAD segment,
reverses the validation transformation and runs the executable
with the recovered token.

It does not read or import the admin source.

The target virtual address, 0x487020, was identified by
disassembly of the tested build. If a different build changes
the address, locate the table again and update TARGET_ADDRESS.

## Intended Solution

1. Verify the downloaded executable checksum.
2. Identify the file format and architecture.
3. Inspect strings and disassembly.
4. Locate the input-length check and validation loop.
5. Identify the target table and transformation.
6. Reverse the transformation to reconstruct the token.
7. Run the executable with the token and obtain the flag.

## Validation Logic — Administrator Notes

- Required token length: 17 bytes.
- Input position: (i * 5) % 17.
- Transform: rotate left by 3 bits.
- Add 17*i + 0x29 modulo 256.
- Compare against the target table.
- The correct input also decodes the encrypted flag bytes.

Recovered token: N0vaTech-R3c0very
Flag: NOVATECH{binary_logic_recovered}

These answers are administrator documentation.

## CTFd Configuration

- Name: S6 — The Exfiltration Tool
- Category: Reverse Engineering
- Type: Standard
- Points: 275
- Flag type: Static, case sensitive
- Attachments: ELF executable, checksum and clue

## Hints

Prototype hint cost: 0.

1. Find the input-length check and follow the validation loop.
   The required token has 17 bytes.
2. The loop reads input positions in a permuted order:
   (i * 5) % 17. Identify the rotation and index-dependent addition.
3. Subtract 17*i + 0x29 from each target byte modulo 256,
   rotate right by 3 bits, and place the result at
   position (i*5)%17.

## Verified Tests

- Compiled successfully as a static x86-64 ELF executable.
- Symbols stripped successfully.
- Incorrect short input rejected.
- Incorrect 17-byte input rejected.
- Target table and validation logic inspected using objdump.
- Solver recovered the token and flag.
- Targeted strings search did not reveal the plaintext flag or token.
- Downloaded CTFd executable matched its supplied checksum.
- Downloaded executable accepted the correct token and printed the flag.
- Rebuild followed by solving succeeded.
- CTFd hints and flag submission tests reported successful.

## Reset / Recovery

The executable is stateless; rerun or redownload it for another
attempt. Keep a known-good binary and matching checksum.

For rebuilding, use admin/build.sh and rerun the solver.
If the published binary changes, replace both the ELF and
checksum attachments in CTFd.

Rebuilding does not reset CTFd submissions, scores or accounts.

## Remaining Integration

- Confirm the scoreboard total for the test team.
- Configure and test the S5 prerequisite.
- Review capstone difficulty with a peer.
- Test full S1–S6 progression.
- Preserve CTFd configuration through export or setup instructions.

## Attribution

Development and debugging assistance was provided by ChatGPT.
The member must review, understand and verify the implementation.
