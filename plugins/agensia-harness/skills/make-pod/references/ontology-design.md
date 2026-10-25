# Ontology Design — the four-part knowledge pack

An **ontology** in P2A is not a folder of documents. It is a governed knowledge pack that makes one outcome achievable and auditable. **Every outcome carries at least one ontology pack. No orphan outcomes, no orphan packs.**

Each pack has exactly four parts plus a provenance header:

| Part | Name | Answers |
|---|---|---|
| **0** | Provenance & lifecycle header | Who owns it, what version, valid when, superseding what, in which jurisdiction |
| **1** | Domain knowledge & standards | *What must be known* to reach this outcome — including the ISO / regulatory / governance instruments that bind it |
| **2** | Procedure & human checkpoints | *How* the outcome is reached, step by step, with typed human-in-the-loop gates |
| **3** | Harness — do / do-not | *What is allowed and forbidden* inside this workflow |
| **4** | Language, persona & output format | *How the result is expressed* |

Parts 1–4 map to what gets uploaded at Platform Step 2 (Ontology). Part 0 lives in the pack file's frontmatter and in the harness spec — it governs, it does not get retrieved.

---

## Tiering — do not over-engineer a read-only Pod

Tier is set by the pack's **highest harness level**, not by ambition. Confirm the tier with the user before authoring.

| Tier | Applies to | Mandatory | Deferred |
|---|---|---|---|
| **Bronze** | HL0–HL1, internal audience, no regulated client | Part 0: owner, version, effective_from, review_due, conflict_policy · Part 1 §A (≥5 CQs), §B, §E · Part 2 steps + gates · Part 3 do-list + ≤5 paired prohibitions · Part 4 lexicon + format | CQ suite ≥8 · authority ranking · decision tables · jurisdiction scoping · per-item TTL · exemplars · retention |
| **Silver** | HL2, external client, non-regulated | Bronze + CQ suite ≥8 · source-authority rank on every item · §C standards · acceptance criteria per step · decision table where ≥2 rules interact · 3 positive + 3 negative exemplars · citation policy | Jurisdiction scoping · per-item TTL · retention schedule · manual drill |
| **Gold** | HL3+, or any regulated / public-sector / EU / NSRF client | Silver + all Part 0 fields · jurisdiction scoping on every item · TTL per item · §D reuse record · exception + rollback paths · evidence contract · review cadence · retention schedule · manual drill | — |

**Escalate the tier, never the other way.** If a Pod moves HL2 → HL3, its packs move Silver → Gold *before* the level change is signed off.

---

## Part 0 — Provenance & lifecycle header

Naive packs fail here first: undated documents, three versions of the same policy, no named owner. Every pack and every source item inside it carries:

| Field | Notes |
|---|---|
| `ontology_id` | `ONT-<outcome-id>-<slug>` |
| `serves_outcome` | The Step 1 Outcome this pack exists for (exactly one primary) |
| `version` / `status` | semver · `draft \| active \| superseded \| retired` |
| `owner` | **Named accountable role**, not a team. This person approves changes. |
| `effective_from` / `effective_to` | Retrieval must hard-filter outside this window, not down-rank |
| `supersedes` / `superseded_by` | The supersession chain — an agent must never cite a superseded item |
| `jurisdiction` | Country / entity / sector scope. A Malaysian PDPA clause must not surface on an EU query. |
| `volatility` / `ttl` | `stable` (~12 mo) · `evolving` (~6 mo) · `volatile` (days) · `live` (query the system, do not cache) |
| `review_due` | Date + the owner's review cadence |
| `conflict_policy` | What the Pod does when two in-scope sources disagree — see below |
| `retention` | Gold only — e.g. 10 years for EU AI Act Annex IV technical documentation |

Authority rank (1–5) is carried **per source item** in the Part 1E inventory, not on the pack as a whole.

**Source-authority ladder** — every item gets a rank; the agent resolves conflicts by rank, then by recency:

1. Binding law / regulation / licence condition
2. Certified management-system document (ISO 9001 controlled procedure, QMS work instruction)
3. Approved internal SOP or policy, signed and dated
4. Reference standard or industry good practice (non-binding)
5. Internal wiki, note, prior correspondence, tribal knowledge

**Conflict policy is mandatory and explicit.** State which of these the Pod does when two in-scope sources disagree: *prefer higher authority* · *prefer more recent within same rank* · *escalate to owner* · *refuse and flag*. Silence here produces confident wrong answers — inter-context conflict is a measured failure class in current RAG research, not a theoretical worry.

---

## Part 1 — Domain knowledge & standards

### §A Competency questions (the completeness test)

Before writing a single source file, write **8–15 competency questions** the pack must be able to answer. These are the scope test and the acceptance test at once (Grüninger & Fox). Format: a question a competent practitioner would ask, phrased so the answer is checkable.

> *"Given an invoice with a 3-way match failure on quantity only, and a supplier on the watchlist, what is the approval route and who signs?"*

Rules: each CQ maps to at least one source item; any CQ with no source is a **coverage gap** and goes in Open items. A pack with no CQ suite has no definition of "complete" — and the platform's Completeness score becomes guesswork.

**CQs are also the seed of the golden set.** Each one becomes a retrieval assertion plus two or three phrasing variants in `goldens-<outcome-slug>.md`, which is how a change to this pack later gets proved harmless or beneficial. Write them so the answer is checkable by someone who is not you — a CQ that cannot become a test case is too vague to be a CQ. See `references/pod-evaluation.md`.

### §B Controlled vocabulary

One term, one meaning, one authority (the ISO/IEC 11179 discipline). List every term the procedure and harness rely on, with its single definition and any banned synonyms. The words that most often carry three meanings in the same SOP: *review · validate · verify · check · approve · confirm · sign off*. Pin each one.

### §C Standards & governance instruments

List the instruments that bind this outcome, each with **why it applies** and **what it constrains** — not a bibliography. Cover three scopes:

| Scope | Ask |
|---|---|
| **Global** | ISO/IEC 42001 (AI management system), ISO/IEC 23894 (AI risk), ISO 9001 §8.5.1 (controlled conditions, results to be achieved), ISO 30401 (knowledge lifecycle), ISO/IEC 25012 (data quality), NIST AI RMF, GHG Protocol, IFRS/ISSB where financial or sustainability data is touched |
| **Country / regional** | EU AI Act (Art. 10 data governance, Art. 11 + Annex IV technical documentation, Art. 12 record-keeping, Art. 14 human oversight) · Malaysia: PDPA, NSRF / Bursa PN9A, MFRS, sector licences · sector regulators wherever the client operates |
| **Industry** | The overlay from `references/standards-registry.md` — BIAN, ACORD, eTOM, SCOR-DS, ISA-95, ITIL 4, GS1, HR Open, APQC PCF — plus certification schemes in play (AS9100, ISO 27001, ISO 13485, HACCP…) |

For each: `instrument · clause/article · what it requires · what it constrains in this Pod (HL cap, evidence type, retention, disclosure)`. Constraints found here flow straight into the harness spec's `policy_constraints` and can cap the harness level.

### §D Reuse before authoring

Check in this order before writing anything new: existing P2A packs in the repo → the industry overlay's reference model → published standards and taxonomies → client's own controlled documents → author from scratch. Authoring from zero is the expensive failure mode; record what you reused and from where.

### §E Source inventory

**Flat filenames, always.** Every file reference — in a pack, between packs, in the pod spec, in the upload set — is a **bare filename in the same directory**. No `./`, no folder segments, no absolute paths, no nesting.

| Write | Never write |
|---|---|
| `as9100.md` | `./ontology/as9100.md` · `standards/as9100.md` · `/repo/ontology/as9100.md` |
| `decision-rules-invoice.md` | `invoice/decision-rules.md` |
| `ontology-invoice-validation.md` | `packs/ontology-invoice-validation.md` |

The reason is mechanical: the platform ingests an upload set as a flat group, so folder structure does not survive the upload. A path that only resolves in your repo is a path that breaks on the platform.

**Naming convention.** Lowercase, hyphenated, `.md`.

- **Standards** — the instrument's common short name, not its full title: `as9100.md` · `iso-9001.md` · `iso-42001.md` · `iso-27001.md` · `ghg-protocol.md` · `ifrs-s2.md` · `pdpa-my.md` · `eu-ai-act.md` · `bursa-pn9a.md`. One file per instrument, reusable across packs — a standard is shared, not copied.
- **Pack-local sources** — `<concern>-<outcome-slug>.md`: `decision-rules-invoice.md` · `glossary-invoice.md` · `lexicon-invoice.md` · `report-layout-invoice.md`.
- **Packs** — `ontology-<outcome-slug>.md`.

**Collisions are resolved by suffix, never by folder.** With one pack per outcome, three packs each wanting `decision-rules.md` is the normal case, not the edge case. Suffix them with the outcome slug. If a source is genuinely shared by several packs, keep one copy under a neutral name (`authority-matrix.md`) and reference it from each pack's inventory — do not duplicate it.

### Inventory table

The actual files/links to upload, each with its Part 0 fields, plus a one-line "what this source helps determine". Package the harness `Know` boundary as **small, single-purpose files** — `decision-rules-<outcome-slug>.md`, `report-layout-<outcome-slug>.md`, `disclaimers-<outcome-slug>.md`, `glossary-<outcome-slug>.md` — not one 80-page PDF. Chunking quality dominates retrieval quality; a monolith retrieves badly no matter how good the content.

---

## Part 2 — Procedure & human checkpoints

### Form

Write the procedure as an **ordered, typed sequence** — not prose. Each step is a row:

`step_id | precondition | actor (agent \| human \| system) | action (STE imperative) | inputs | acceptance criteria | evidence produced | on-failure path | next`

Three things naive procedures omit, all three mandatory here:

1. **Preconditions** — what must be true, present and authorised before the step may start; safety and policy warnings surface *before* the step body (the S1000D discipline).
2. **Acceptance criteria** — the result to be achieved, stated so pass/fail is unambiguous. ISO 9001 §8.5.1 requires documented information defining results, not just actions.
3. **Exception & rollback path** — what happens on failure, partial completion, timeout or novel case. Default on no-response is **fail-closed: halt, do not proceed.**

### Writing rules (ASD-STE100)

One instruction per sentence · imperative verb first · active voice · ≤20 words per procedural sentence · one meaning per word, using the Part 1 §B vocabulary · no pronouns referring across steps. This is the highest-leverage single rule in the whole pack — it is what makes step text machine-followable rather than machine-interpretable.

### Human-in-the-loop gates

Every gate is typed and named. A gate is **not** "a human checks this."

| Gate field | Requirement |
|---|---|
| `gate_id` / step it guards | |
| `accountable_role` | A named role with a competence requirement. Never "a human". |
| `what the reviewer sees` | Including the **disconfirming evidence**: assumptions made, conflicting sources, low-support claims |
| `discriminating input required` | A typed value, a chosen branch, or a named exception — **never a bare Approve button** |
| `timebox` | 60–90s typical; if the item set can't be checked in the box, it's the wrong item set |
| `timeout behaviour` | Fail-closed |
| `rejection path` | Returns to the agent with a **reason code**, logged |
| `automation level` | Per step, not one global flag — say what the agent acquires, analyses, decides and does at this step |

**Anti-rubber-stamp mechanics** (a rubber-stamped gate is worse than no gate — it manufactures the appearance of control):

- Cap the checkpoint budget. Past roughly 30 approvals a day, reviewers stop reading.
- Group items at natural pause points, ≤5–9 per pause — the surgical-checklist scale, not one prompt per step.
- Use challenge-response: the agent states the item, the human states the verified value back.
- Measure the override rate. An override rate near zero is a **failure signal**, not success.
- Sample-audit approved items and rotate reviewers.
- Gold tier: schedule periodic manual execution of the procedure so the supervising humans keep the skill to intervene.

**Gate on irreversibility and blast radius, not on model confidence.** Confidence is a self-report; irreversibility is a property of the tool.

### Visualisation — human reference only, never uploaded

The STE step text **is** an uploadable ontology source. Any diagram of it is not.

- On request, render the procedure as BPMN or a flowchart via `the host’s available draw.io capability` (ISO 5807 symbols; use the manual-operation symbol for HITL gates).
- Save it beside the pack and stamp it: **`DO NOT UPLOAD — human reference only`**.
- State this to the user every time you produce one. The Agensia platform ingests the text; the picture is for the people who have to sign off on it.

---

## Part 3 — Harness: do / do-not

### Positive first, negative second — and short

Negatively framed rules are unreliable in isolation: models attend to the concept you named, and adherence variance rises with every added prohibition. Current evidence is consistent that positively framed directives achieve near-perfect adherence where the matching prohibition does not.

So: **write the do-list first and make it complete. Then add at most 3–5 sharp prohibitions, each paired with the positive behaviour that replaces it.**

Pattern: `INSTEAD OF <forbidden>, DO <required>.`

Cap the whole harness at ~10–15 rules. Beyond that, the rules belong in a decision table, not a list.

### Two rule classes — never conflate them

| Class | Where it lives | Strength |
|---|---|---|
| **Prompt rule** | The pack / system prompt | A nudge. Assume it can be talked around. |
| **Enforcement rule** | Tool scope, permission, validator, schema, approval gate | A control. This is what actually stops the action. |

Every rule protecting something irreversible, financial, legal or personal **must exist in both classes**. A prompt is not a control. Instruction hierarchies — "the system prompt wins" — are not robust enough to carry a security-relevant rule alone.

### Decision tables

Where two or more rules can fire on the same case, express them as a **DMN-style decision table** with inputs, outputs and an explicit **hit policy** (Unique / First / Priority / Any / Collect). The hit policy is the machine-checkable contract for what happens on overlap. Prose lists silently contradict; tables cannot.

### Make every rule scoreable

Decompose each rule into a **single binary proposition** a reviewer or an LLM judge can mark yes/no. "Be professional" is not a rule. "Every figure quoted carries a citation to a system record" is. This decomposition is what makes the harness evaluable later.

### Evidence contract

State what is recorded per step, for audit: inputs, tool calls with arguments, the human decision and its reason code, timestamp, and **the version of the pack and procedure that was in force**. Gold tier ties this to the retention schedule in Part 0.

---

## Part 4 — Language, persona & output format

Decorative persona specs are worthless. Everything here must be testable.

### Language

Working language(s) and the rule for code-switching · reading level ceiling and max sentence length · plain-language commitment (ISO 24495-1: findable, understandable, actionable, consistent — tested by whether the reader can act, not by a readability score) · translation and terminology rules where the audience is multilingual.

### Persona — scored, not described

Place the Pod on four bipolar dimensions, each with a chosen point and a one-line justification: *funny ↔ serious · formal ↔ casual · respectful ↔ irreverent · enthusiastic ↔ matter-of-fact*. Then:

- **Lexicon files**: approved terms · banned terms · never-say list · canonical spellings · forbidden clichés. Machine-checkable, and a source file in its own right.
- **Worked exemplars**: 3 positive and 3 negative, each demonstrating exactly one thing.
- **Voice adherence check**: how the reviewer scores it (1–5 on personality match, tone-for-scenario, vocabulary, structural consistency, compliance flags).

### Output format

- **Default structure**, headline-first, with a stated depth ceiling.
- **Where the output is structured, define the schema — and order reasoning fields before conclusion fields.** Field order measurably affects quality under constrained decoding; a schema that demands the conclusion first degrades the reasoning behind it. Name fields semantically (`evidence_citation`, not `f3`) — the key names are an instruction channel.
- **Validation**: schema validation plus a repair loop; track the rejection rate. Structured-output mode is not a contract.
- **Citation policy**: at HL2+, every claim cites a source record — item ID + version + retrieval timestamp. This is also what satisfies record-keeping obligations.
- **Mandatory elements** on every output (disclaimers, confidence statement, "what I could not verify").

---

## Pre-upload quality gate

Do not hand a pack to the platform until every check **in scope for its tier** passes. Report the result to the user as a table, scored `x/14`, with out-of-scope checks marked `n/a — <tier>` rather than passed. A failed in-scope check goes to Open items with an owner and a due date.

| # | Check | Pass condition | Scope |
|---|---|---|---|
| 1 | Outcome coverage | Every outcome has ≥1 pack; every pack names exactly one primary outcome | all |
| 2 | CQ coverage | Every competency question maps to ≥1 source item; gaps listed as Open items. Bronze ≥5 CQs, Silver/Gold ≥8 | all |
| 3 | Vocabulary | Every term used in Parts 2–3 is defined in Part 1 §B, once | all |
| 4 | Authority & conflict | Conflict policy stated (all tiers); every source item ranked 1–5 | conflict policy: all · ranking: silver+ |
| 5 | Currency | No item past `effective_to`; no superseded item in the upload set; pack has an owner and a review date (Gold: every item does) | all |
| 6 | Jurisdiction | Every item scoped; no cross-jurisdiction leakage | gold |
| 7 | Procedure integrity | Every step has a precondition and an on-failure path; procedure reaches a terminal state from every branch. Silver+: acceptance criteria on every step | all |
| 8 | Gates | Every HL1+ step's gate names an accountable role, a discriminating input, a timeout and a rejection path | all |
| 9 | Harness balance | Do-list complete; ≤5 prohibitions, each paired with a positive replacement; every irreversible action has an enforcement-class rule, not just a prompt rule | all |
| 10 | Scoreability | Every harness rule is a single binary proposition | all |
| 11 | Format | Output structure defined, reasoning before conclusion, lexicon present. Silver+: citation policy and exemplars | all |
| 12 | Granularity | Sources are small and single-purpose; no monolithic PDF carrying more than one concern | all |
| 13 | Tier | Pack tier ≥ the tier required by its harness level | all |
| 14 | Upload hygiene | Every diagram stamped `DO NOT UPLOAD`; nothing in the upload set that shouldn't leave the client. Every filename flat and unique across the whole upload set — no paths, no collisions | all |

**After the gate passes, the pack is testable but not yet proven.** Any edit to it from here — a document added, a term changed, a rule amended — is a change that must be re-tested against the outcome's golden set before it goes live. See `references/pod-evaluation.md` for the change-classification table and the promotion gate.

Checks 4 (ranking), 6, 7 (acceptance criteria) and 11 (citations, exemplars) are the ones that tier off. Everything else is mandatory at every tier, including Bronze — a pack with no owner, no conflict policy and no terminating procedure is not shippable at any level of authority.

The platform separately scores Outcome–Ontology alignment and each group on Completeness / Uniqueness / Usability (x/5). Checks 1–2 drive Completeness, 3–4 and 12 drive Uniqueness, 7–11 drive Usability.

---

## Anti-patterns

- **The document dump.** Sixty files, no CQs, no ranking. The platform will score it, the agent will retrieve the wrong version, and nobody will know why.
- **One ontology for the whole Pod.** Outcomes get their own packs. Shared material goes in a named shared pack, referenced — not copied into each.
- **The prohibition wall.** Twenty "do not" rules and no do-list. Measurably worse output *and* no actual control.
- **Prose procedure.** A paragraph the model re-derives every run instead of a typed sequence it follows.
- **Undated everything.** No version, no owner, no review date — the pack rots in place and nobody notices for a year.
- **The decorative persona.** "Professional and friendly." Untestable, so untested, so it drifts.
- **Uploading the diagram.** The picture is for the humans. The platform gets the text.
- **Foldered references.** `./ontology/as9100.md` resolves in your repo and nowhere else. The upload set is flat; write `as9100.md`.
- **Three packs, three files called `decision-rules.md`.** They collide the moment they're uploaded together. Suffix by outcome slug.
- **Gold-plating an HL0 Pod.** A read-only monitoring Pod does not need a retention schedule. Tier honestly; over-specification is how the whole spec gets abandoned.
