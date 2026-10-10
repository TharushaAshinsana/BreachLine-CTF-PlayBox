# Member 4 – Test Results

## Project
BreachLine-CTF-PlayBox

## Tester
Member 4

## Test Environment
- Platform: CTFd
- Repository: BreachLine-CTF-PlayBox
- Test date: To be recorded during testing

## Test Results

| Test ID | Test | Expected Result | Actual Result | Status | Evidence |
|---|---|---|---|---|---|
| TC-01 | Open available challenge | Challenge page loads correctly | Not tested yet | NOT TESTED | Pending |
| TC-02 | Submit correct flag | Challenge is marked solved | Not tested yet | NOT TESTED | Pending |
| TC-03 | Submit incorrect flag | Submission is rejected | Not tested yet | NOT TESTED | Pending |
| TC-04 | Check challenge prerequisites | Locked challenge stays unavailable until requirements are met | Not tested yet | NOT TESTED | Pending |
| TC-05 | Complete stage progression | Stages unlock in the intended order | Not tested yet | NOT TESTED | Pending |
| TC-06 | Check for unintended shortcuts | Flags are not exposed through unintended paths | Not tested yet | NOT TESTED | Pending |
| TC-07 | Test reset and recovery | Environment returns to the documented initial state | Not tested yet | Pending | Pending |
| TC-08 | Test complete S1–S6 integration | All implemented stages work together as intended | Not tested yet | NOT TESTED | Pending |

## Defects
No test results recorded yet.

## Summary
Testing has not started. Results will be updated after the challenges are implemented and tested.
---

## Member 3 - S4-S6 Component Verification

Tester: Member 3 - IT24100054
Test dates: 2026-10-09 to 2026-10-10
Environment: Windows 11, Ubuntu WSL 2, Docker Compose and CTFd

These are Member 3 component tests, separate from Member 4 testing.

| Test | Result | Status |
|---|---|---|
| S4 authenticated evidence download | Ciphertext and clue downloaded successfully | PASS |
| S4 solver | Key, plaintext and flag recovered | PASS |
| S4 flag validation and hints | Correct accepted, incorrect rejected, hints accessible | PASS |
| S5 forensic recovery | Logs/history led to recoverable deleted gzip archive and flag | PASS |
| S5 integrity | Image hash unchanged after analysis | PASS |
| S5 reset | Regeneration followed by solving and checksum verification succeeded | PASS |
| S5 CTFd | Hints and flag validation reported successful | PASS |
| S6 binary | Static stripped Linux x86-64 ELF built | PASS |
| S6 validation | Incorrect short and 17-byte inputs rejected | PASS |
| S6 solver | Token reconstructed and flag printed | PASS |
| S6 strings check | Targeted search found no plaintext flag or token | PASS - LIMITED |
| S6 player download | Downloaded ELF checksum and execution verified | PASS |
| S6 rebuild | Rebuilt binary remained solvable | PASS |
| S6 CTFd | Hints and flag validation reported successful | PASS |
| Prerequisite configuration | Export confirms S5 requires S4; S6 requires S5 | PASS |
| S4-S6 scoring | Test team received 575 points | PASS |
| Player lock/unlock enforcement | Explicit before/after observations needed | PENDING |
| Full S1-S6 integration | Remaining stages must be integrated | PENDING |

### Evidence
Terminal outputs, player screenshots, CTFd exports and repository commits:
9946535, e3846e0, 99340a8, d381e45.

### Remaining Work
- Record fresh-team lock/unlock behaviour.
- Verify downloaded S5 image checksum.
- Broaden shortcut testing and review difficulty.
- Align final points and hint costs with the group design.
- Complete S3-to-S4 gating and full progression.
- Test backup restoration in a separate environment.
