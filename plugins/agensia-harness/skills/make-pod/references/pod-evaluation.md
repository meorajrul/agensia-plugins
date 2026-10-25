# Pod Lifecycle Feedback Loop — golden sets and evaluation

An outcome that cannot be re-tested is an outcome nobody can safely change. This is the loop that lets a Pod owner edit a decision rule, add a document to an ontology pack, or tighten a prompt — and *know* whether the Pod got better, got worse, or moved inside the noise.

**One golden set per outcome.** It lives in its own artifact, `goldens-<outcome-slug>.md`, and is versioned independently of the knowledge it tests.

Platform configuration scores are a separate diagnostic, not results from this golden-set loop. Before score-guided edits, use [configuration verification](configuration-verification.md) to confirm committed fields, current source bindings and feedback provenance. Do not infer a score for unscored sections or claim runtime improvement from a higher wizard rating.

---

## The loop

```
Outcome + owner goal
        ↓
Golden set  ←──────────── competency questions (Part 1A)
        ↓                 SOP clauses, harness rules
Baseline run ─→ scorecard ─→ owner signs the goal as MET / NOT MET
        ↓
   [ change ]  knowledge added · rule edited · prompt tweaked · model moved
        ↓
Change classification ─→ re-test scope
        ↓
Re-run (paired, same cases) ─→ Δ vs baseline
        ↓
Promotion gate ─→ PROMOTE / HOLD / BLOCK
        ↓
New baseline ────┐
        ↓        │
Production ──→ overrides, escalations, corrections
        ↓        │
New golden cases ┘
```

The loop never terminates. A Pod that has stopped being evaluated has stopped being governed.

---

## 1 · The outcome goal statement

This is the governance object the whole loop exists to serve, and it is the Pod owner's to write — not the builder's. One per outcome, in the golden set frontmatter:

| Field | Meaning |
|---|---|
| `goal` | What "good" means for this outcome, in one sentence the owner would defend to their own manager |
| `primary_metric` | **One** metric — the one the owner would accept as the verdict. Not three. |
| `target` | The number that means the goal is met |
| `floor` | The number below which the Pod is withdrawn from service, not merely held |
| `ni_margin` (δ) | How far the primary metric may drop before a change is blocked. Default 2pp for safety and compliance metrics, 5pp for quality metrics. |
| `signed_by` / `signed_on` | The owner accepts these numbers before the baseline is run, not after |

**Declare the target before the first run.** A target chosen after seeing the score is not a target, it is a description.

---

## 2 · Building the golden set

### Derive, don't invent

| Source | Becomes |
|---|---|
| Each competency question (ontology Part 1A) | 1 retrieval assertion + 2–3 phrasing variants |
| Each decision rule / DMN row (Part 3) | 1 case per branch, including the boundary values on both sides |
| Each HITL gate (Part 2) | 1 case that must escalate, 1 near-miss that must not |
| Each harness prohibition (Part 3) | 1 case that tempts the Pod to violate it |
| Each acceptance criterion (Part 2) | 1 case checking the criterion is stated in the output |
| Each production override or correction | 1 regression case (see §7) |

If a competency question cannot become a test case, the CQ is too vague — fix the CQ.

### Strata and quotas

Fix the mix, then hold it constant. A shifting mix can manufacture an improvement without anything improving.

| Stratum | Share | Contains |
|---|---|---|
| Happy path | 40% | The ordinary case, in the ordinary phrasing |
| Edge / boundary | 25% | Values either side of every threshold; missing fields; ambiguity |
| Adversarial | 15% | Attempts to talk the Pod past its harness; injected instructions in input documents |
| Regression | 15% | Real past failures, overrides, and corrections |
| Out-of-scope | 5% | Must be refused or escalated, not answered |

**Score every stratum separately and report them separately.** A headline mean is exactly the place an adversarial regression hides under happy-path gains.

### Size, honestly

Markdown golden sets are hand-run, so they are small, and small sets detect only large effects. State the limit rather than pretending otherwise.

| Set size | Honest use |
|---|---|
| 20–40 | Smoke test. Detects only gross breakage. Never sufficient for an HL increase. |
| 40–80 | Working default for a Bronze/Silver Pod. Detects roughly ≥10pp swings. |
| 120+ | Required before any HL2 → HL3 promotion (at 3 repeats), and for any Gold-tier Pod. |

Publish the set's **minimum detectable effect** in the frontmatter. If an observed change is smaller than the MDE, the verdict is **INCONCLUSIVE** — which is a legitimate, expected, and frequently correct answer. A loop that never returns "inconclusive" is a loop that is fooling itself.

### Blind holdout

Hold back 20–30% of cases that whoever writes the prompts and packs never sees. Compare the public score to the blind score at every run. **A widening gap between them is the overfitting alarm** — the Pod is learning the test, not the job. Refresh the blind set quarterly; rotate ~10% of the public set each month.

### Case metadata

Every case carries: `id · stratum · source (CQ / rule / gate / incident) · input · expected retrieval (which pack items) · expected output or verdict · expected escalation flag · check type (deterministic / judge) · which owner goal it proves · date added · last reviewed`.

---

## 3 · The metric ladder — deterministic first

**Use a judge only where no deterministic check exists.** Most of what matters here is countable, and counting does not drift, cost tokens, or need calibration.

### Tier A — deterministic, count these by hand

| Metric | How to score |
|---|---|
| **Harness rule compliance** | Each rule is already a single binary proposition. Pass rate = passes / applicable cases. |
| **Escalation correctness** | Confusion matrix against the expected escalation flag. Report **precision and recall separately** — a Pod that escalates everything scores perfectly on recall and is useless. |
| **Refusal correctness** | Should-refuse recall, *and* over-refusal rate on the in-scope strata. Both, always. |
| **Citation validity** | Does each cited item exist, is it the current version, and does the cited passage actually contain the claim? |
| **Retrieval hit** | Did the expected pack items appear? Miss = the ontology's problem, not the prompt's. |
| **Format validity** | Required fields present, order correct, mandatory elements (disclaimer, confidence, "could not verify") included. |
| **Superseded-source usage** | Any citation of an expired or superseded item. **This is a zero-tolerance count.** |

### Tier B — judged, and only under discipline

Faithfulness, completeness, tone/voice adherence, reasoning quality.

Rules if you use a judge:
1. Binary or 3-point verdicts. Never 1–10 — the middle of a 10-point scale carries no shared meaning.
2. One criterion per judgement. Do not ask for an overall score.
3. Require the judge to quote the evidence span *before* giving a verdict.
4. Swap the presentation order and keep only order-consistent verdicts. Position bias is large and free to eliminate.
5. Use a different model family than the one being tested. Self-preference is measurable and real.
6. Calibrate against 30–50 human-labelled cases before a judge is allowed to gate anything, and re-calibrate whenever the judge model changes.
7. Normalise for length. Judges reward verbosity far more than humans do.

### Tier C — budget

p50 and p95 latency, tokens, cost per case. **Gate on p95, not the mean** — the mean hides exactly the tail the user will complain about.

---

## 4 · Statistics you can actually do by hand

The trap is treating "78% → 81%" as evidence. On 40 cases that is one or two cases and it is noise.

### Rule 1 — always compare paired, on the identical case set

Never re-sample. Run the same cases before and after. Pairing is what makes a small set usable at all.

### Rule 2 — count the discordant cases, not the totals

For every case, record whether it flipped:

- **b** = cases that were **wrong before, right after** (fixed)
- **c** = cases that were **right before, wrong after** (broken)
- Cases that did not change carry no information about the change and are excluded.

Let n = b + c.

### Rule 3 — the sign test table

Exact one-sided sign test at α = 0.05. You may claim **improvement** only if `c` (the count of newly broken cases) is at or below the threshold for your n:

| n = b + c | Max `c` for a claim of improvement |
|---|---|
| ≤ 4 | no claim possible at any value |
| 5, 6, 7 | 0 |
| 8, 9, 10 | 1 |
| 11, 12 | 2 |
| 13, 14, 15 | 3 |
| 16, 17 | 4 |
| 18, 19, 20 | 5 |
| 21, 22 | 6 |
| 23, 24, 25 | 7 |
| 30 | 10 |
| 35 | 12 |
| 40 | 14 |
| 45 | 16 |
| 50 | 18 |
| 60 | 23 |
| 80 | 32 |
| 100 | 41 |

For an n not listed, use the next lower row — that is conservative and safe.

Read it as: *8 cases flipped in total; if 1 or fewer of them got worse, the improvement is real at the 5% level. If 2 or more got worse, it isn't — regardless of what the headline percentage did.*

If n ≤ 4, the honest verdict is **INCONCLUSIVE**. Add cases or accept that you cannot tell.

### Rule 4 — non-inferiority is the default question

For a knowledge addition or a minor workflow edit, the owner's real question is almost never "is it better?" — it is **"am I confident it isn't worse?"** Test that instead:

> **Pass non-inferiority if** the primary metric has not dropped by more than δ, **and** `c` (newly broken cases) ≤ `b` (newly fixed cases) **and** zero safety-stratum failures.

Superiority is a stronger, separate claim requiring the sign-test threshold above. Most healthy changes are non-inferior, not superior, and that is fine.

### Rule 5 — designate one primary metric

Tracking ten metrics at α = 0.05 gives roughly a 40% chance that one of them moves "significantly" by luck alone. Name the owner's primary metric in advance; everything else is descriptive context, reported but not celebrated.

### Rule 6 — repeat the run if the Pod is non-deterministic

Set the eval temperature to ≤ 0.3. For a promotion decision, run each case 3 times and take the majority verdict; a case whose verdict is unstable across 3 runs is itself a finding and belongs in Open items. Once repeats are stable, **more cases beat more repeats.**

### Rule 7 — record the environment

Every run logs: golden-set version, ontology pack versions, harness version, model and provider version, date, and who ran it. Without this you cannot tell a regression from a provider update.

---

## 5 · Change classification — what to re-test

Not every change deserves the full suite. Not every change may skip it.

| Change | Re-test scope | Statistical bar |
|---|---|---|
| Typo, formatting, comment | Smoke set (20 cases) | None — deterministic checks only |
| **Add** a source to an ontology pack | Full set; retrieval + citation metrics closely | Non-inferiority on everything else |
| **Edit or remove** a source, term, or decision rule | Full set + every case tracing to the touched item + all CQ assertions for it | Non-inferiority mandatory; zero safety failures |
| Persona, format, or lexicon change | Full set, format + voice metrics primary | Non-inferiority on task metrics |
| New or changed HITL gate | Full set + escalation stratum oversampled | Escalation precision **and** recall both non-inferior |
| Harness rule added or relaxed | Full set + adversarial stratum | Zero tolerance: any adversarial failure blocks |
| **Harness level increase** (e.g. HL2 → HL3) | Full set at 120+ cases, 3 repeats, plus ≥30 days of HL2 operating evidence with an agreed error budget and a reviewed override rate | PROMOTE with verdict IMPROVED — superiority on the primary metric, zero adversarial or out-of-scope failures |
| Model or provider version change | Full set + adversarial + refusal strata | Non-inferiority; pin the old version until it passes |
| **Nothing changed** (scheduled drift run) | Full set, frozen cases | Any significant move = provider drift, not your edit |

---

## 6 · The promotion gate

Run the gate after every re-test and record the verdict in the golden set's run log. Three outcomes only.

**BLOCK — no averaging, no discretion:**

- Any failure in the adversarial or out-of-scope stratum.
- Any harness rule marked safety-class failing on any case.
- Any citation of a superseded or expired source.
- Escalation recall dropped at all.
- Primary metric below the owner's declared `floor`.

These are gates, not scores. **A compliance violation cannot be offset by a quality gain**, and any design that lets it be averaged away is not a control.

**HOLD:**

- Primary metric dropped by more than δ.
- `c` > `b` — the change broke more than it fixed.
- Verdict INCONCLUSIVE on a change that was supposed to improve something. Not a failure; an instruction to add cases or accept the change on other grounds, explicitly.

**PROMOTE:**

- No BLOCK conditions.
- Primary metric within δ of baseline (non-inferior), or above it.
- Every stratum non-inferior — not just the mean.
- Budget within tolerance at p95.

On PROMOTE, the new run becomes the baseline and the version bumps. On BLOCK or HOLD, the previous versions of the pack, harness and prompt remain in force — **rollback is the default state, not an intervention.**

---

## 7 · Closing the loop

The golden set's most valuable cases are the ones production gave you.

1. **Capture** every human override, rejected output, escalation the Pod missed, and correction: input, what the Pod produced, what the human changed it to, the reason code, and which rule or CQ it violated.
2. **Triage weekly.** A one-off is a note; a recurrence is a case.
3. **Promote to the regression stratum** on the second occurrence, or immediately for anything with safety, legal or financial impact.
4. **Fix the cause, not the case.** An override usually means a missing decision rule, an ambiguous term, or a coverage gap in the ontology — not a prompt that needs more adjectives. Patch the pack, then re-run.
5. **Retire** cases that have passed for six consecutive months, to keep the set fast and the regression stratum near 15%.
6. **Watch the override rate by category.** A rising override rate is the earliest regression signal you have, and it arrives before any metric moves.

This is also the evidence trail. Repeated related corrections should trigger a governed review of the pack or process card under the owner's change policy. And the golden set plus its gate records are what an ISO/IEC 42001 continual-improvement clause, a NIST AI RMF MEASURE/MANAGE claim, or an EU AI Act post-market monitoring plan actually wants to see: a declared accuracy target, a versioned test set, dated runs, and recorded decisions.

---

## 8 · Cadence

| Trigger | Run |
|---|---|
| Any change | Scope per §5, before promotion |
| Weekly | Drift run on frozen cases, unchanged config |
| Monthly | Rotate 10% of public cases; review override log |
| Quarterly | Refresh blind holdout; owner re-signs the goal statement; retire stale cases |
| Before any HL increase | Full suite at 120+ cases, 3 repeats, plus ≥30 days HL2 evidence and a reviewed override rate |

---

## Anti-patterns

- **"The number went up."** On 40 cases, three points is one case. Count the discordant cases and use the table.
- **Comparing against a different sample.** Unpaired comparison throws away the only statistical advantage a small set has.
- **One headline score.** It hides the stratum that regressed. Report all five.
- **The author writes the tests.** With no blind holdout, you will optimise the test and call it progress.
- **Averaging a safety failure away.** A 3% gain in quality does not buy one adversarial breach.
- **Judging what you could count.** Schema validity, citation existence and escalation flags are deterministic. A judge on those adds cost, noise and nothing else.
- **An uncalibrated judge with a gate.** Agreement with humans is an assumption until measured. Get κ ≥ 0.6 first.
- **No drift baseline.** The provider updates the model, the suite is never re-run on the unchanged config, and the regression gets blamed on last week's prompt edit.
- **A target set after the run.** That is a description wearing a target's clothes.
- **Never returning INCONCLUSIVE.** If every run finds a result, the loop is generating confidence rather than measuring it.
