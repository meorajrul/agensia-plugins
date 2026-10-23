# Harness Levels (HL0–HL4) — Full Rubric

The harness level is a per-skill (and per-Pod) declaration of how much authority the agent holds. Assigned at design time, enforced at runtime by the control envelope, changed only through governed review.

## The five levels

| Level | Name | The agent may… | A human… | Typical BPMN anchor |
|---|---|---|---|---|
| **HL0** | Observer | Read, retrieve, summarize, classify, monitor, alert | Consumes output; no action implied | Receive tasks, timer watches, event-based gateways |
| **HL1** | Advisor | Draft, recommend, score, pre-fill, explain — nothing leaves the agent's sandbox | Executes every action | User tasks (assisted), businessRule tasks (advisory) |
| **HL2** | Preparer | Prepare complete transactions/actions with evidence attached | Approves each action before execution (checkpoint / Decision Desk) | Service tasks behind an approval gateway |
| **HL3** | Bounded Executor | Execute **reversible, in-policy, within-budget** actions autonomously; log everything; stop on any rule breach | Reviews samples + exceptions after the fact | Service tasks on the happy path with explicit decision rules |
| **HL4** | Delegated Operator | Execute high-impact workflows end-to-end within the envelope | Owns risk acceptance, monitors continuously, can kill-switch; rollback plan mandatory | Whole lanes/subprocesses — rare, earned, never default |

## Two hard rules

1. **Design-time ceiling: HL2.** New Pods launch at HL0–HL2. **HL3 requires all four:** ≥30 days of HL2 operating evidence with an agreed error budget · a reviewed override rate · a PROMOTE run on a 120+ case golden set at 3 repeats, with superiority on the declared primary metric and zero adversarial or out-of-scope failures · harness spec version bump with owner sign-off. HL4 additionally requires written risk acceptance from the accountable executive and a tested rollback. Evaluation detail: `pod-evaluation.md`.
2. **Irreversible + consequential = never above HL2.** Payments release, contract execution, clinical actions, regulatory filings, personnel actions, permanent deletion: a human clicks the final button, whatever the level elsewhere in the process.

## Control envelope by level

| Verb | HL0 | HL1 | HL2 | HL3 | HL4 |
|---|---|---|---|---|---|
| **Know** | Assigned KB, read-only source data | + case data | + transaction context | + system state it acts on | + cross-process context |
| **Decide** | Nothing | Recommendations only | Selects the proposed action | Deterministic gateway decisions per written rules | Rule + bounded-judgment decisions in envelope |
| **Do** | Alert, report | Produce drafts | Stage actions for approval | Execute reversible actions | Execute per delegation contract |
| **Prove** | Source citations | Citations + reasoning summary | + evidence bundle per staged action | + full action log, before/after state | + continuous telemetry, periodic attestation |
| **Escalate** | On anomaly detected | On low confidence / missing data | On approval rejection or timeout | On any rule breach, threshold hit, or novelty | On envelope-edge conditions + heartbeat loss |
| **Learn** | Usage feedback | Accepted/rejected drafts | Approval outcomes | Exception reviews | Post-incident + periodic audit findings |

## Assignment decision tree

```
Is the action irreversible OR legally/clinically/financially consequential?
├── yes → HL2 max (human approves each instance)
└── no → Is the decision rule fully written & testable?
    ├── no  → HL1 (agent advises; human decides)
    └── yes → Is the action reversible with a known rollback?
        ├── yes → HL3 eligible (after HL2 evidence period)
        └── no  → HL2
Activity only reads/watches? → HL0 regardless of the above.
```

## Pod-level aggregation

- A Pod's **headline level** = the highest HL among its skills — this is what governance reviews.
- Each **skill keeps its own HL** — a Pod can hold HL0 monitoring, HL1 drafting, and HL2 preparation skills simultaneously.
- **Escalation must exist at every level ≥ HL1** and must name a role, a trigger, and a channel. "Escalate to manager" without a trigger fails review.

## Level changes

| Change | Requires |
|---|---|
| Raise HL of a skill | Operating evidence + reviewed override rate + a PROMOTE golden-set run (120+ cases, 3 repeats, superiority, zero adversarial failures) + harness spec version bump + owner sign-off. A HOLD or BLOCK verdict on the latest run bars the increase outright. |
| Lower HL | Immediate, no ceremony — safety changes are never blocked |
| Emergency freeze (any → HL0) | Anyone on the escalation chain may trigger; review within 48h |

System-side caps compose by minimum: if a target system declares `write_allowed_hl: HL2`, an HL3 skill writing to it still gets a human checkpoint.
