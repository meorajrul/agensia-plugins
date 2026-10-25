---
artifact: pod-contract
framework: p2a
version: "0.1"
status: draft   # draft → signed at G8 ; superseded by the next signed version
owner: <accountable process owner role>
builder: <builder role>
updated: <YYYY-MM-DD>
pod: pod-<role>-<subrole>.md
togaf_phase: "G (Implementation Governance)"
---

> **Design agreement only.** Signing this contract does not approve runtime actions, publication or production release.

# Pod Contract and playback log — <Pod name>

The Pod Contract is the agreement between the builder and the process owner on what the Pod will and will not do. It works like a TOGAF Architecture Contract. The playback log shows that every fact the builder inferred was read back to the owner.

## 1. Playback log

Run before G1, G3, G6 and G8. Show only `INF`, `ASM` and `SME` values that need the owner. See `references/elicitation-cards.md` §4.

| Date | Gate | Component | Statement read back | Owner answer (correct / change / don't know) | New value | New tag |
|---|---|---|---|---|---|---|
| | G1 | Role | | | | OWN |

## 2. What the owner agrees the Pod will do

| Outcome # | Single named output | Talent | HL | Human gate | Workflow |
|---|---|---|---|---|---|
| 1 | | | | | |

## 3. What the Pod will never do

| # | Prohibition | Positive replacement | Enforcement (tool scope / validator / gate) | Status |
|---|---|---|---|---|
| 1 | | | | specified |

## 4. Acceptance criteria

| Requirement ID | Acceptance check | Golden case IDs | Owner goal (target / floor) |
|---|---|---|---|
| R1 | | | |

## 5. Open items accepted at signature

| ID | Item | Owner | Due | Blocks |
|---|---|---|---|---|
| | | | | |

## 6. Change rule

Any change to an outcome, HL, approver, prohibition or source authority reopens the matching gate and requires a new signed version of this contract.

## 7. Signature (Gate G8)

| Role | Name | Version | Decision | Date |
|---|---|---|---|---|
| Process owner | | | sign / change | |
| Builder | | | | |
