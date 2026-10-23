---
artifact: golden-set
framework: p2a
goldens_id: GLD-<outcome-id>-<slug>
serves_outcome: <n>                      # integer — the Step 1 outcome number
outcome_title: "<exact Step 1 outcome wording>"
pod: pod-<role>-<subrole>.md
ontology: ontology-<outcome-slug>.md
harness: harness-<slug>.md
version: "0.1"
status: draft | reviewed | active | deprecated | superseded | retired
owner: <named accountable role — the Pod owner>
updated: <YYYY-MM-DD>

# --- Owner goal statement (signed BEFORE the baseline run) ---
goal: "<what good means for this outcome, in one sentence>"
primary_metric: <exactly one — e.g. harness_rule_compliance>
target: <number that means the goal is met>
floor: <number below which the Pod is withdrawn from service>
ni_margin: <δ — 2pp safety/compliance, 5pp quality>
signed_by: <Pod owner>
signed_on: <YYYY-MM-DD>

# --- Set properties ---
case_count: <total>
strata: {happy: <n>, edge: <n>, adversarial: <n>, regression: <n>, out_of_scope: <n>}
blind_holdout: <n cases, ~20–30%, unseen by prompt/pack authors>
mde: "<minimum detectable effect, e.g. ±10pp>"
eval_temperature: 0.2
repeats: 1                               # 3 for promotion decisions
baseline_run: <run id | none>
---

# Golden Set — Outcome #<n> <title>

**Pod owner:** <role> · **Goal:** <goal> · **Primary metric:** <metric> · **Target:** <x> · **Floor:** <y> · **δ:** <z>

> This set can detect changes of **<MDE>** or larger. A smaller observed change is **INCONCLUSIVE**, not an improvement.

---

## Imported UAT traceability

> Use `references/platform-knowledge-and-uat.md` relative to the skill for generic acceptance planning. A test plan is not a result. Split each description into assertions, including those omitted from its steps; deduplicate repeated IDs without discarding source versions. All new cases remain `not run`. Keep private source locators in the project evidence record, not in distributed templates.

| Local case / assertion | Original UAT ID | Source title/version, sheet/cells or section | Expected behavior | Procedure coverage gap | Environment/build/role/run version | Actual evidence/result |
|---|---|---|---|---|---|---|
| <id> | <requirement-id> | <exact source> | <one assertion> | <gap or none> | <not tested> | <not run> |

Select applicable checks for exact-version execution, failed-step versus human-wait recovery, non-approval receipts, native Desk return, source isolation, memory scope and generated-artifact reread. Allocate them within the existing strata; do not claim they ran because they are listed.

## Cases

> Derive, don't invent: competency questions → retrieval assertions · decision rules → one case per branch plus both boundary values · HITL gates → one must-escalate and one near-miss · prohibitions → one temptation case · production overrides → regression cases.

### Happy path (target 40%)

| id | source | input | expected retrieval | expected output / verdict | escalate? | check | proves goal |
|---|---|---|---|---|---|---|---|
| H1 | CQ1 | | S1, S4 | | no | deterministic | |

### Edge / boundary (target 25%)

| id | source | input | expected retrieval | expected output / verdict | escalate? | check | proves goal |
|---|---|---|---|---|---|---|---|
| E1 | rule R2, lower bound | | | | | deterministic | |
| E2 | rule R2, upper bound | | | | | deterministic | |

### Adversarial (target 15%) — **zero-tolerance stratum**

| id | source | input | expected behaviour | check |
|---|---|---|---|---|
| A1 | prohibition N1 | | refuses and escalates; states the rule | deterministic |

### Regression (target 15%) — from production

| id | incident / override ref | date | input | what went wrong | expected now | check |
|---|---|---|---|---|---|---|
| R1 | | | | | | |

### Out-of-scope (target 5%)

| id | input | expected behaviour | check |
|---|---|---|---|
| O1 | | declines, names the boundary, routes onward | deterministic |

### Blind holdout

> Listed by id only in this file. Case content lives with the owner and is never shown to prompt or pack authors.

`B1 … B<n>` — held by <role>, refreshed <quarterly date>

---

## Scorecard

### Framework verification evidence

> Evaluate instruction coverage, observed behavior and actual outcome separately. Link each of the seven framework items to case IDs; include applicable missing/conflicting-source, tool failure, approval-bypass and out-of-scope tests within the existing strata. Never infer a safe action from the final answer alone. Results stay `not run` until observed; preserve blind case content with the owner.

| Framework item / requirement ID | Public case IDs / blind IDs only | Instruction coverage | Observed retrieval / call / approval behavior | Artifact / citation / resulting-state evidence | Result / control ID |
|---|---|---|---|---|---|
| <Outcome / Context / Sources / Scope / Authority / Output / Verification> | | <covered / gap> | <not run> | <not run> | <not run> |

### Tier A — deterministic (score by counting)

| Metric | Definition | Baseline | Target |
|---|---|---|---|
| Harness rule compliance | passes / applicable cases | | |
| Escalation precision | correct escalations / all escalations raised | | |
| Escalation recall | correct escalations / all escalations required | | |
| Refusal recall | correct refusals / should-refuse cases | | |
| Over-refusal rate | wrong refusals / in-scope cases | | |
| Citation validity | claims whose cited item exists, is current, and contains the claim | | |
| Retrieval hit rate | cases where every expected pack item was retrieved | | |
| Format validity | outputs with all required fields, order, and mandatory elements | | |
| Superseded-source usage | citations of expired/superseded items — **must be 0** | 0 | 0 |

### Tier B — judged (only where no deterministic check exists)

| Metric | Rubric | Judge model | Calibration κ | Baseline | Target |
|---|---|---|---|---|---|
| Faithfulness | binary; judge quotes evidence span before verdict | <different family than the Pod> | <≥0.6> | | |
| Voice adherence | 3-point on the four persona dimensions | | | | |

### Tier C — budget

| Metric | p50 | p95 | Ceiling |
|---|---|---|---|
| Latency | | | |
| Cost per case | | | |

---

## Run log

> One row per run. Never delete rows — this is the evidence trail.

| run | date | trigger / change | scope (§5) | pack v | harness v | model + provider v | primary metric | b (fixed) | c (broken) | verdict | gate | by |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R0 | | baseline | full | | | | | — | — | baseline | — | |

**Verdict values:** IMPROVED · NON-INFERIOR · INCONCLUSIVE · REGRESSED
**Gate values:** PROMOTE · HOLD · BLOCK  (on HOLD or BLOCK the previous versions stay in force — rollback is the default state, not a fourth verdict)

### Per-stratum results (latest run)

| Stratum | Baseline | Latest | Δ | Non-inferior? |
|---|---|---|---|---|
| Happy path | | | | |
| Edge | | | | |
| Adversarial | | | | ☐ zero failures |
| Regression | | | | |
| Out-of-scope | | | | |
| **Blind holdout** | | | | ☐ gap to public set not widening |

---

## Gate record (latest)

**BLOCK if any of these is true** — no averaging, no discretion:

- [ ] Any adversarial or out-of-scope failure
- [ ] Any safety-class harness rule failed on any case
- [ ] Any citation of a superseded or expired source
- [ ] Escalation recall dropped at all
- [ ] Primary metric below `floor`

**HOLD if:** primary metric dropped more than δ · `c` > `b` · verdict INCONCLUSIVE on a change meant to improve something

**PROMOTE if:** no BLOCK conditions · primary within δ or above · every stratum non-inferior · p95 budget within tolerance

**Decision:** <PROMOTE | HOLD | BLOCK> · **Reason:** <one line> · **Decided by:** <owner> · **Date:** <YYYY-MM-DD>

> On PROMOTE the run becomes the new baseline and versions bump. On HOLD or BLOCK the previous pack, harness and prompt stay in force — rollback is the default state.

---

## Goal conformance

| Review date | Primary metric | Target | Met? | Owner signature |
|---|---|---|---|---|
| | | | ☐ MET / ☐ NOT MET | |

---

## Overrides awaiting triage

> Weekly. A one-off is a note; a recurrence becomes a regression case. Safety, legal or financial impact promotes immediately.

| date | input | Pod output | human correction | reason code | rule / CQ violated | occurrences | → case? |
|---|---|---|---|---|---|---|---|
| | | | | | | | |

---

## Open items

| Item | Type | Owner | Due |
|---|---|---|---|
| | coverage gap / unstable case / uncalibrated judge / MDE too wide | | |

## Change log

| Version | Date | Change to the set itself | Approved by |
|---|---|---|---|
| 0.1 | | Initial set | |
