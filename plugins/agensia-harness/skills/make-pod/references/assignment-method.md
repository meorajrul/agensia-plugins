# Agent Assignment Method

Which activities become agent skills, at what harness level, grouped into which Pod.

## Step 1 — Score each activity (AAS: Agent Aptitude Score, 0–10)

Score 0–2 on five factors; sum = AAS:

| Factor | 0 | 1 | 2 |
|---|---|---|---|
| **Frequency** | < weekly | weekly–daily | many times daily |
| **Rule clarity** | Tacit judgment | Partly written | Fully written, testable rules |
| **Data availability** | Paper/tribal | Partly digital | Fully digital, API-accessible |
| **Reversibility** | Irreversible | Compensable with effort | Trivially reversible |
| **Risk if wrong** *(inverted)* | Severe (legal/safety/financial) | Moderate | Negligible |

| AAS | Disposition |
|---|---|
| 8–10 | Automate: HL3 **candidate** — still launches at HL2 and reaches HL3 only through the evidence bar, never through the score |
| 5–7 | Assist: HL1–HL2 |
| 3–4 | Watch only: HL0 |
| 0–2 | Leave human; revisit when data or rules improve |

The AAS caps but never overrides the decision tree in `harness-levels.md` — irreversible/consequential actions stay ≤HL2 even at AAS 10.

**A high AAS is a hypothesis, not a promotion.** The score says a skill *could* earn HL3; only the evidence bar in `harness-levels.md` grants it — ≥30 days of HL2 operating evidence, a reviewed override rate, and a PROMOTE run on a 120+ case golden set at 3 repeats with superiority and zero adversarial failures (`pod-evaluation.md`). Scoring 9 on day one changes nothing about the launch level.

## Step 2 — Four disqualifiers (exclude from HL ≥ 1 if ANY hold)

1. **No accountable owner** — nobody in the lane owns escalations.
2. **No evidence definition** — the team cannot state what "done correctly" looks like.
3. **Prohibited by policy/regulation** — check the industry overlay and local law (e.g., decisions requiring licensed professionals).
4. **Rule source is one person's head** — capture the rule first (interview → decision_rule column), then rescore.

## Step 3 — Group skills into Pods (priority order)

1. **One lane → one Pod.** Role = lane's function; Subrole = the process context.
2. **Shared escalation target.** Skills escalating to different owners belong in different Pods.
3. **Shared knowledge scope.** Skills needing disjoint KBs split.
4. **≤7 skills per Pod** at launch; beyond that, split into a coordinated Pack.
5. **Uniform audience.** External-customer-facing and internal-auditor-facing = two Pods.

## Step 4 — Name the human checkpoints (every HL2 skill)

| Field | Example |
|---|---|
| Approver role | AP Supervisor |
| What they see | Case, evidence, exception flags, agent recommendation + confidence |
| Timeout | 24h → escalate to next level |
| Rejection path | Returns to agent with reason; agent revises once, then routes to human queue |

Checkpoints without timeouts stall processes; checkpoints without rejection paths teach the agent nothing.

## Anti-patterns

- **Automating the exception path first.** Happy path automates; exceptions go to humans — that's where judgment lives.
- **HL creep via prompt edits.** Authority changes ride harness-spec versions, never silent prompt edits.
- **The do-everything Pod.** Spanning lanes, audiences, and escalation chains = unauditable by construction.
- **Scoring by enthusiasm.** AAS factors are evidence-based; seniority of the requester is not a factor.
