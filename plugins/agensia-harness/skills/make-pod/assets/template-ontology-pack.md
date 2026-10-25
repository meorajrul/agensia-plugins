---
artifact: ontology-pack
framework: p2a
ontology_id: ONT-<outcome-id>-<slug>
serves_outcome: <n>                      # integer — the Step 1 outcome number
outcome_title: "<exact Step 1 outcome wording>"
pod: pod-<role>-<subrole>.md
harness: harness-<slug>.md
tier: bronze | silver | gold
version: "0.1"
status: draft | reviewed | active | deprecated | superseded | retired
owner: <named accountable role>
effective_from: <YYYY-MM-DD>
effective_to: <YYYY-MM-DD | open>
supersedes: <ontology_id | none>
superseded_by: <ontology_id | none>
jurisdiction: <country / entity / sector scope>
volatility: stable | evolving | volatile | live
ttl: <e.g. 12 months>
review_due: <YYYY-MM-DD>
review_cadence: <e.g. semi-annual>
conflict_policy: prefer-higher-authority | prefer-more-recent-within-rank | escalate-to-owner | refuse-and-flag
retention: <gold only — e.g. 10 years>
updated: <YYYY-MM-DD>
---

# Ontology Pack — <name>

**Serves:** Outcome #<n> — <one line>
**Tier:** <bronze | silver | gold> · required by harness level HL<?>
**Owner:** <named role> · **Review due:** <date>

---

## Part 1 — Domain knowledge & standards

### 1A Competency questions

> 8–15 questions this pack must be able to answer. Each maps to ≥1 source item. Unmapped = coverage gap.

| # | Competency question | Answered by (source id) | Status |
|---|---|---|---|
| CQ1 | | | covered / **GAP** |
| CQ2 | | | |

### 1B Controlled vocabulary

> One term, one meaning. Pin the words that carry three meanings in most SOPs: review · validate · verify · check · approve · confirm · sign off.

| Term | Single definition | Banned synonyms | Authority |
|---|---|---|---|
| | | | |

### 1C Standards & governance instruments

| Scope | Instrument | Clause / Article | What it requires | What it constrains here |
|---|---|---|---|---|
| Global | | | | HL cap / evidence type / retention |
| Country | | | | |
| Industry | | | | |

> Constraints listed here flow into the harness spec `policy_constraints`. Note any that cap the harness level.

### 1D Reuse record

| Reused from | Type | What was taken |
|---|---|---|
| | existing pack / overlay / standard / client doc | |

**Authored from scratch:** <list — keep this short>

### 1E Source inventory (the upload set)

> **Flat filenames only** — bare name, same directory. No `./`, no folder segments, no paths. Standards use the instrument's short name (`as9100.md`, `iso-9001.md`, `pdpa-my.md`); pack-local sources are suffixed with the outcome slug so they don't collide with other packs.

| id | Source file / link | What it helps determine | Authority rank (1–5) | Version | Effective from–to | Volatility / TTL | Owner |
|---|---|---|---|---|---|---|---|
| S1 | decision-rules-<outcome-slug>.md | | 3 | | | | |
| S2 | glossary-<outcome-slug>.md | | 3 | | | | |
| S3 | <standard-short-name>.md | | 1 | | | | |

**Conflict policy:** <prefer higher authority · prefer more recent within rank · escalate to owner · refuse and flag>

---

## Part 2 — Procedure & human checkpoints

> ASD-STE100: one instruction per sentence · imperative verb first · active voice · ≤20 words · vocabulary from 1B.

| step | precondition | actor | action (STE) | inputs | acceptance criteria | evidence produced | on-failure | next |
|---|---|---|---|---|---|---|---|---|
| P1 | | agent / human / system | | | | | | P2 |
| P2 | | | | | | | | |

**Terminal states:** <list — every branch must reach one>

### Human-in-the-loop gates

| gate | guards step | accountable role (+competence) | what the reviewer sees (incl. disconfirming evidence) | discriminating input required | timebox | timeout behaviour | rejection path | automation level |
|---|---|---|---|---|---|---|---|---|
| G1 | | | | | 60–90s | fail-closed: halt | returns to agent with reason code | |

**Checkpoint budget:** <max gates per run / per reviewer per day>
**Override-rate target:** <non-zero — near-zero means rubber-stamping>
**Sample audit:** <% of approved items re-checked, by whom, how often>
**Manual drill (gold):** <cadence for humans executing the procedure unaided>

### Visualisation

- [ ] Diagram rendered for human reference: `<filename>.drawio`
- [ ] Stamped **`DO NOT UPLOAD — human reference only`**
- [ ] Excluded from the Step 2 upload set

---

## Part 3 — Harness: do / do-not

### Do (write this first, make it complete)

| # | Rule (single binary proposition) | Class: prompt / enforcement | Enforcement mechanism |
|---|---|---|---|
| D1 | | | tool scope / validator / schema / approval gate |

### Do not (max 5, each paired)

| # | Prohibition | Positive replacement — "INSTEAD OF X, DO Y" | Enforcement mechanism |
|---|---|---|---|
| N1 | | | |

> Every rule protecting something irreversible, financial, legal or personal must appear in **both** classes. A prompt is a nudge; the tool scope is the control.

### Decision table(s)

> Use where ≥2 rules can fire on one case. Hit policy is mandatory.

**Table:** <name> · **Hit policy:** Unique | First | Priority | Any | Collect

| input 1 | input 2 | → output | → action |
|---|---|---|---|
| | | | |

### Evidence contract

Recorded per step: <inputs · tool calls with arguments · human decision + reason code · timestamp · **pack version and procedure version in force**>
Retention: <from Part 0>

---

## Part 4 — Language, persona & output format

### Language

- **Working language(s):** · **Code-switching rule:**
- **Reading level ceiling:** · **Max sentence length:**
- **Plain-language commitment:** <ISO 24495-1 — tested by reader task success>

### Persona (scored)

| Dimension | Position | Why |
|---|---|---|
| funny ↔ serious | | |
| formal ↔ casual | | |
| respectful ↔ irreverent | | |
| enthusiastic ↔ matter-of-fact | | |

**Lexicon file:** `lexicon-<outcome-slug>.md` — approved terms · banned terms · never-say list · canonical spellings · forbidden clichés

**Worked exemplars:** 3 positive, 3 negative — each demonstrating exactly one thing.

| # | Type | Demonstrates | Example |
|---|---|---|---|
| E1 | positive | | |
| E4 | negative | | |

**Voice adherence scoring (1–5):** personality match · tone-for-scenario · vocabulary · structural consistency · compliance flags

### Output format

- **Default structure:** <headline-first, depth ceiling>
- **Schema:** <name> — **reasoning fields ordered before conclusion fields**; field names semantic
- **Validation:** <schema validator + repair loop; track rejection rate>
- **Citation policy:** <HL2+: every claim cites item id + version + retrieval timestamp>
- **Mandatory on every output:** <disclaimers · confidence statement · "what I could not verify">

---

## Pre-upload quality gate

> Score `x/14`. Mark out-of-scope checks `n/a — <tier>`, not passed. Any failed in-scope check goes to Open items with an owner and a due date.

| # | Check | Scope | Result |
|---|---|---|---|
| 1 | Every outcome has ≥1 pack; this pack names one primary outcome | all | ☐ |
| 2 | Every CQ maps to ≥1 source; gaps in Open items (bronze ≥5 CQs, silver/gold ≥8) | all | ☐ |
| 3 | Every term in Parts 2–3 defined once in 1B | all | ☐ |
| 4 | Conflict policy stated; every source item authority-ranked 1–5 | policy: all · ranking: silver+ | ☐ |
| 5 | Nothing expired or superseded in the upload set; owner + review date present (gold: per item) | all | ☐ |
| 6 | Every item jurisdiction-scoped; no cross-jurisdiction leakage | gold | ☐ |
| 7 | Every step has precondition and on-failure path; all branches terminate (silver+: acceptance criteria) | all | ☐ |
| 8 | Every HL1+ gate names role, discriminating input, timeout, rejection path | all | ☐ |
| 9 | Do-list complete; ≤5 prohibitions, each paired; irreversible actions have enforcement-class rules | all | ☐ |
| 10 | Every harness rule is a single binary proposition | all | ☐ |
| 11 | Output structure defined, reasoning before conclusion, lexicon present (silver+: citations + exemplars) | all | ☐ |
| 12 | Sources small and single-purpose; no monolith | all | ☐ |
| 13 | Pack tier ≥ tier required by harness level | all | ☐ |
| 14 | Diagrams stamped DO NOT UPLOAD; every filename flat and unique across the upload set | all | ☐ |

---

## Open items

| Item | Type | Owner | Due |
|---|---|---|---|
| | TBD / coverage gap / assumption | | |

## Change log

| Version | Date | Change | Approved by |
|---|---|---|---|
| 0.1 | | Initial draft | |
