---
artifact: harness-spec
framework: p2a
version: "0.1"
status: draft
owner: <accountable role>
updated: <YYYY-MM-DD>
name: <e.g. "AP Invoice Processing Agent Harness">
processes: [process-<apqc>-<slug>.md]
headline_hl: HL2
policy_constraints:
  - <e.g. "Payment release is human-only regardless of HL">
evidence_store: <where prove-records land>
review_cadence: monthly
kill_switch_roles: [<role 1>, <role 2>]
---

> **Non-production only.** Verify the platform and downstream resources before operations. Never create or push changes to Agensia production; no production uploads, publication, edits, deletions, runs, schedules or connector writes. Unknown targets block operations. No design approval waives this rule.

# Harness Spec — <name>

## Skills covered

| Skill | From activity | Name | HL |
|---|---|---|---|
| S1 | A2 | | HL2 |

## Know — knowledge & data access

| Skill | KB / knowledge sources | Data objects (read) | Explicitly excluded |
|---|---|---|---|
| S1 | | | |

## Decide — autonomous decision scope

| Skill | May decide alone | Rule source | May NOT decide |
|---|---|---|---|
| S1 | | | |

## Do — permitted actions

| Skill | Action | Target system | System write cap | Mode at HL |
|---|---|---|---|---|
| S1 | | | HL2 | prepared, human approves |

## Prove — evidence requirements

| Skill | Evidence captured | Where | Retention |
|---|---|---|---|
| S1 | | | |

### Control verification

> One row per required enforcing control. A prompt instruction is not enforcement. Status: `specified` = designed but untested; `verified` = evidence for this configuration/version; `blocked` = unavailable or failed. Revalidate on relevant changes. G0–G8 approve the design; runtime approval authorizes only the recorded action within its scope.

| Control ID / skill | Rule + action / target | Preconditions / approval evidence | Enforcement location + owner | Denial / rejection / expiry / failure behavior | Test ID + observed call/state evidence + config/version/date | Status |
|---|---|---|---|---|---|---|
| C1 / S1 | <read/write/action limits> | <inputs, permission, approver, specific action parameters> | <tool scope / validator / approval gate; not prompt-only> | <hold / escalate / bounded recovery> | <not run until observed> | specified |

**Context and tool-loop limits:** <relevant source retrieval; source locators retained; tool-call/retry/output budgets; recover authoritative evidence/approval after context loss or hold the action>

## Escalate — triggers, targets, channels

| Trigger | From skill | Escalate to | Channel | Timeout behavior |
|---|---|---|---|---|
| | S1 | | | |
| rule breach / novel case | any | | | freeze skill to HL0 |

## Learn — feedback loop

| Signal | Captured how | Feeds into |
|---|---|---|
| Approval/rejection outcomes | checkpoint records | KB update proposals (human-reviewed) |
| Corrections (≥3 similar) | corrections log | process card version bump |

## HL change history

| Date | Skill | From → To | Evidence / approver |
|---|---|---|---|
| | | | |
