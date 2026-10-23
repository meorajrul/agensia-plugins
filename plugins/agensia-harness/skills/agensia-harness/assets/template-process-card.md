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

## Narrative

<3–6 sentences: trigger to outcome, plain language a new hire would understand.>

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
