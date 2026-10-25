---
artifact: process-card
framework: p2a
version: "0.1"
status: draft
owner: <accountable role>
updated: <YYYY-MM-DD>
apqc_id: "<n.n.n>"
name: <Process name, verb-first>
capability: capability-<apqc>-<slug>.md
bpmn_file: process-<apqc>-<slug>.bpmn   # optional; delete if none
trigger: <start event in plain language>
outcome: <end event(s) / what success looks like>
sla: <end-to-end target>
lanes:
  - {lane: <Lane name>, owner_role: <Accountable role>}
agent_assignment: []   # e.g. [{pod: pod-<role>-<subrole>.md, skills: [A2, A3]}]
---

# Process — <name> (APQC <apqc_id>)

> Tag captured values `[OWN]` `[DOC]` `[SME]` `[OBS]` `[INF]` `[ASM]` (see `references/elicitation-cards.md`). Charter: `pod-charter-<slug>.md`. SIPOC and RACI: `sipoc-raci-<slug>.md`.

## Narrative

<3–6 sentences: trigger to outcome, plain language a new hire would understand.>

## As-is (baseline) — how the work runs today

<Walk through the last real case. Name who did each step, the wait points and the rework.>

| Baseline measure | Value | Date / sample | Tag |
|---|---|---|---|
| Volume per period | | | |
| Cycle time (median / p90) | | | |
| Rework or rejection rate | | | |
| Main pain points | | | |

## To-be (target) — what changes when the Pod arrives

| As-is step | To-be step | Changed by (Talent / Workflow / human) | HL | Expected effect | Tag |
|---|---|---|---|---|---|
| | | | | | |

## Activity table (normative)

| id | name | bpmn_type | lane | systems | data | decision_rule | hl | escalate_to | evidence |
|---|---|---|---|---|---|---|---|---|---|
| A1 | | | | | | | | | |

## Gateways

| id | Type | Condition (plain language, policy-grade) |
|---|---|---|
| G1 | XOR | IF <condition> THEN <path A> ELSE <path B> |

## Unhappy paths & escalation events

| Event | Trigger | Handled by | Target |
|---|---|---|---|
| | | | |

## Volumes & timing

| Metric | Value |
|---|---|
| Instances per <day/week/month> | |
| Current cycle time | |

## Open questions

- <Must be empty before status: reviewed.>
