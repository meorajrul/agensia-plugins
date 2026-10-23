# BPMN 2.0 Capture (Agent-Ready Subset)

How to capture a process so it can drive an AI agent. P2A uses a small BPMN 2.0 subset — enough for governance, small enough for non-modelers.

## Element subset and agent meaning

| BPMN element | Use | Agent meaning |
|---|---|---|
| Pool | Process/organization boundary | Deployment boundary |
| Lane | A role (human or agent) | Candidate Pod role/subrole; lane owner = escalation target |
| User Task | Human work | Stays human, or HL1/HL2 agent-assisted |
| Service Task | Automated system call | Prime agent candidate (any HL) |
| Business Rule Task | Decision against policy | Agent `decide` boundary; rules must be citable |
| Manual Task | Offline physical work | Out of agent scope; agent may track |
| Send/Receive Task | Message in/out | Agent communication skills |
| Exclusive Gateway (XOR) | Either/or decision | Deterministic branch — agent may take at its HL |
| Parallel Gateway (AND) | Concurrent work | Agent may fan out; join needs completion checks |
| Event-Based Gateway | Wait for external event | Agent monitoring/signal skill |
| Start/End Events | Triggers and outcomes | Pod activation conditions; success criteria |
| Timer Event | Deadline / SLA | Escalation trigger |
| Error / Escalation Event | Failure or handoff | **Mandatory** — becomes the Pod's escalation path |
| Message Event | Cross-pool communication | Inter-Pod or Pod-to-human message |

Excluded in v1: complex gateways, compensation, transactions, choreography/conversation diagrams. If a process needs them, agent authority in those regions defaults to HL1.

## Capture rules

1. **One pool per process card.** Cross-organization flows = separate cards linked by message events.
2. **Verb-first activity names**: "Validate invoice against PO", not "Invoice validation".
3. **Every lane names an accountable owner** (role title, not a person).
4. **Every gateway states its condition in plain, policy-grade language**: "IF amount ≤ RM10,000 AND 3-way match passes THEN auto-approve path". This text becomes the agent's decision rule.
5. **Every unhappy path gets an error or escalation event.** Zero escalation events = failed review; real processes fail somewhere.
6. **Attach data objects** to activities that read/write them.
7. **Timers on anything with an SLA** — agents are excellent at watching timers.

## The activity table (normative artifact)

Diagrams help humans; the activity table is what drives everything downstream:

| Column | Content |
|---|---|
| `id` | `A1`, `A2`, … stable within the card |
| `name` | Verb-first activity name |
| `bpmn_type` | user / service / businessRule / manual / send / receive |
| `lane` | Role that owns it |
| `systems` | Systems touched |
| `data` | Data objects read/written |
| `decision_rule` | For rule tasks/gateways: the plain-language rule |
| `hl` | Harness level HL0–HL4 |
| `escalate_to` | Role receiving escalation + trigger |
| `evidence` | What proves the step ran correctly |

## BPMN XML twin

Optionally store the diagram as standard BPMN 2.0 XML (Camunda Modeler, bpmn.io, Signavio all export it). The markdown card wins on conflict — it carries the harness annotations.

## From lanes to Pod roles

- Lane ≥80% service/businessRule tasks at HL2+ → dedicated Pod (lane = Role, process = Subrole context).
- Lane dominated by user tasks with a few HL1 service tasks → human role with an assistant-style Pod.
- Never merge two lanes into one Pod if their escalation targets differ — it blurs accountability.
