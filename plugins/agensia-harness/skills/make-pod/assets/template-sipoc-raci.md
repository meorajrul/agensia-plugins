---
artifact: sipoc-raci
framework: p2a
version: "0.1"
status: draft
owner: <accountable process owner role>
updated: <YYYY-MM-DD>
process: process-<apqc>-<slug>.md
togaf_phase: "B (Business Architecture)"
---

# SIPOC and RACI — <process name>

Map the process before configuring anything. SIPOC fixes inputs and outputs. RACI fixes who answers each question and who approves each write. Tag values `[OWN]` `[DOC]` `[SME]` `[OBS]` `[INF]` `[ASM]`.

## 1. SIPOC

| Supplier | Input (exact, with format) | Process step (from activity table) | Output (named) | Customer | Tag |
|---|---|---|---|---|---|
| | | A1 | | | |

## 2. RACI — humans and agents

One **A** per row. Agents (Talents) may be **R** only. An agent is never **A**.

| Activity / decision | Process owner | Performer | Approver | Data owner | Compliance | Talent (agent) | Tag |
|---|---|---|---|---|---|---|---|
| A1 | A | R | | C | | | |
| A2 — prepare | A | C | | | | R (S1, HL2) | |
| A2 — approve | | | A/R | | C | | |

## 3. Decision rights

| Decision | Decides (A) | Delegate when absent | Evidence the decider sees | Receipt location | Tag |
|---|---|---|---|---|---|
| | | | | | |

## 4. Handoffs between lanes

| From lane | To lane | What is handed over | Acceptance condition | Clock / timeout | Tag |
|---|---|---|---|---|---|
| | | | | | |

## 5. Checks before G1

- [ ] Every activity has exactly one **A**.
- [ ] No Talent is **A**.
- [ ] Every write or external send has a human **A** and a receipt location.
- [ ] Every handoff has an acceptance condition.
- [ ] Columns name roles, not people; a `role-binding-<pod>.md` source maps roles to current holders and cover.
- [ ] No *must* value remains `INF` or `ASM` without an Open item.
