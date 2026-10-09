# Member 4 – Integration and Testing Plan

## 1. Objective

The objective is to verify that the BreachLine CTF challenges work correctly, integrate properly with the CTFd platform, and provide the intended challenge-solving experience.

## 2. Testing Scope

Testing will cover:

- Challenge availability and instructions
- Correct and incorrect flag submissions
- Challenge prerequisites and progression
- Intended solution paths
- Unintended shortcuts and flag exposure
- Reset and recovery behaviour
- Integration of all six stages (S1–S6)

## 3. Test Cases

| Test ID | Test Description | Expected Result |
|---|---|---|
| TC-01 | Open each available challenge | Challenge page and instructions display correctly |
| TC-02 | Submit the correct flag | Challenge is marked as solved |
| TC-03 | Submit an incorrect flag | Incorrect submission is rejected |
| TC-04 | Attempt to access a locked challenge | Prerequisite restrictions work as configured |
| TC-05 | Complete challenges in the intended order | Stage progression works correctly |
| TC-06 | Check for exposed flags or unintended shortcuts | Flags cannot be obtained through unintended methods |
| TC-07 | Reset the challenge environment | The environment returns to the documented initial state |
| TC-08 | Test the complete S1–S6 workflow | All stages integrate and progress as intended |

## 4. Test Execution Status

All test cases are initially marked as NOT TESTED. Results will be recorded after testing the implemented challenges.

## 5. Defect Handling

For each defect, record its ID, description, steps to reproduce, expected result, actual result, severity, responsible team member, fix status, and retest result.

## 6. Evidence

Evidence may include screenshots, test logs, defect reports, and permitted video demonstration footage.

## 7. Final Evaluation

The final report will summarise passed tests, failed tests, unresolved defects, retest outcomes, and integration limitations.