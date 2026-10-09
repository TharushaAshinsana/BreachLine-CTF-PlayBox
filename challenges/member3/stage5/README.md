# S5 — Lateral Movement

Owner: Member 3 — IT24100054
Domain: Digital Forensics
Target difficulty: Moderate–Hard
Status: Working prototype integrated with CTFd.

## Challenge

Investigate a synthetic NovaTech server filesystem image.
Correlate authentication logs and shell history, identify a
deleted gzip archive, and recover its contents.

The recovered content contains the flag and a clue for S6.

## Player Files

- player/server_image.dd
- player/server_image.dd.sha256
- player/clue.txt

The image is a 32 MiB ext4 filesystem image, without a partition
table. It contains fictional evidence, not a real server capture.

Distribute only player files. Admin code, solver code and
recovered output must not be distributed to players.

## Requirements

Build and solve using Ubuntu or Ubuntu on WSL 2.

    sudo apt install python3 e2fsprogs sleuthkit gzip

Run commands from the BreachLine-CTF-PlayBox project root.

## Generate / Reset

    python3 challenges/member3/stage5/admin/generate.py

The generator replaces the challenge image and writes a new
SHA256 checksum. It operates on the image file, not a physical disk.

Filesystem metadata may cause the image hash to change between
generations.

## Solve

    python3 challenges/member3/stage5/solver/solve.py

The solver reads authentication logs and shell history, finds the
deleted archive name, discovers its inode using fls, recovers it
using icat -r, and decompresses it.

The inode is discovered dynamically rather than hardcoded.
The solver does not import or read the generator.

Recovered files are written to solver/recovered/.

## Intended Evidence Path

1. Verify the image checksum.
2. Read /var/log/auth.log.
3. Identify the successful analyst login.
4. Read /home/analyst/.bash_history.
5. Identify the deleted transfer_notes.txt.gz archive.
6. Find its deleted entry using fls.
7. Recover its contents using icat -r.
8. Decompress the archive and locate the flag and S6 clue.

The tested method uses filesystem metadata recovery.
A separate file-carving workflow has not yet been verified.

## Integrity Verification

    (cd challenges/member3/stage5/player && sha256sum -c server_image.dd.sha256)

Perform analysis without modifying the image.
The solver compares the image SHA256 before and after recovery.

## CTFd Configuration

- Name: S5 — Lateral Movement
- Category: Digital Forensics
- Type: Standard
- Points: 200
- Flag type: Static, case sensitive
- Flag: NOVATECH{deleted_transfer_recovered}
- Player files: image, checksum and clue

The flag shown here is administrator documentation.

## Hints

Prototype hint cost: 0.

1. Start with /var/log/auth.log. Identify the successful login
   and inspect that user's shell history.
2. The shell history identifies a deleted gzip archive.
   Use fls to locate its deleted filesystem entry.
3. Recover the deleted entry using icat -r with its inode number,
   then decompress the recovered gzip archive.

## Verified Tests

- Image generation completed successfully.
- Authentication logs and shell history were readable.
- fls identified the deleted archive.
- icat recovered a valid gzip archive.
- Manual decompression recovered the flag and S6 clue.
- Solver recovered the archive and flag successfully.
- Image SHA256 remained unchanged after analysis.
- Regeneration followed by solving succeeded.
- Regenerated image matched its generated checksum.
- CTFd player view showed S5 as solved.

## Remaining Checks

- Record the scoreboard total after S5.
- Record incorrect-flag rejection and player hint access.
- Verify the downloaded CTFd image against its checksum.
- Test that simple plaintext searches do not expose the flag.
- Configure and test the S4 prerequisite during final integration.
- Review challenge difficulty with a peer.
- Preserve a known-good image for re-upload recovery.

## Platform Reset

Regenerating the local image does not update CTFd attachments.
After regeneration, replace both the uploaded image and checksum.

To restore the existing published challenge, re-upload its
matching known-good image and checksum.

This does not reset CTFd submissions, scores or accounts.

## Attribution

Development and debugging assistance was provided by ChatGPT.
The member must review, understand and verify the implementation.
