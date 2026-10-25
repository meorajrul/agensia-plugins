---
artifact: pod-spec
framework: p2a
version: "0.1"
status: draft  # draft → reviewed only after Gate G8; active only once published and baselined
gates: {G0: open, G1: open, G2: open, G3: open, G4: open, G5: open, G6: open, G7: open, G8: open}
workspace: <authorised workspace>
environment: <verified non-production target; unknown blocks operations>
production_changes: prohibited  # no creation, push, upload, publish, execution or mutation
owner: <accountable role>
updated: <YYYY-MM-DD>
role: <Pod Hierarchy Role, e.g. "Finance Operations">
subrole: <Pod Hierarchy Subrole, e.g. "AP Invoice Processing Specialist">
harness: harness-<slug>.md
ontologies:
  - {id: ONT-O1-<slug>, file: ontology-<outcome-slug>.md, serves_outcome: 1, tier: bronze}
goldens:
  - {id: GLD-O1-<slug>, file: goldens-<outcome-slug>.md, serves_outcome: 1, baseline_run: none}
platform: agensia
headline_hl: HL2
skills:
  - {id: S1, name: <skill name>, from_activity: A2, hl: HL2}
---

> **Non-production only.** Verify the platform and downstream resources before operations. Never create or push changes to Agensia production; no production uploads, publication, edits, deletions, runs, schedules or connector writes. Unknown targets block operations. No design approval waives this rule.

# Pod Spec — <role> / <subrole>

## Identity (Role → Subrole)

- **Role:** <organizational function — from the BPMN lane>
- **Subrole:** <specialist identity within that role — from the process context>
- **Mission (one sentence):** <what outcome this Pod exists to deliver>

## Prompt framework coverage

> Start at G0; repeat this table per outcome from G2. Index canonical artifact sections/rule IDs rather than duplicating policy. Keep gaps explicit and update at each gate. Spec: `references/prompt-framework.md`.

### Outcome #<n> — <title>

| Item | Agreed requirement | Canonical artifact / section or rule ID | Gate | Open item / owner |
|---|---|---|---|---|
| Outcome | <result, beneficiary and success measure> | <outcome + owner goal> | G2 / G7 | |
| Context | <role, trigger, users, environment> | <identity / process card> | G0 / G1 / G5 | |
| Sources | <approved evidence, version and freshness/conflict rule> | <pack source inventory / Know> | G6 | |
| Scope | <included/excluded work, inputs, tools/data limits> | <Talent / Know, Decide, Do> | G2 / G3 / G6 | |
| Authority | <HL, approver, checkpoint, escalation/stop> | <harness rule / control ID> | G3 / G4 | |
| Output | <single named artifact, schema/layout and audience> | <outcome / Talent / schema> | G2 / G5 / G6 | |
| Verification | <acceptance checks, test IDs and state evidence> | <Prove / golden-set case IDs> | G6 / G7 / G8 | |

**Example invocation:** <short prompt labelled Outcome / Context / Sources / Scope / Authority / Output / Verification, consistent with this approved design>

**Readiness:** design <draft / reviewed> · baseline <not run / run ID> · required controls <specified / verified / blocked — see harness control IDs>. Design-gate approval does not approve individual runtime actions. Unrun baselines and unverified required controls prevent a go-live claim for the dependent capability.

## Persona & Voice

- **Persona:** <one-sentence professional character>
- **Voice attributes:** <3–5 adjectives>
- **Never:** <tones to avoid>

## Audience

| Audience | Relationship | Adjustment |
|---|---|---|
| | | |

## Response Format & Depth

- **Default format:** <e.g. structured summary + evidence table>
- **Depth:** <e.g. headline first, one screen max unless asked>
- **Citations:** <e.g. every claim links to a source record>

## Authority Boundaries (from harness spec)

- **Headline harness level:** HL<?> — <one-line meaning>
- **May:** <from harness Do/Decide at this HL>
- **Must not:** <policy_constraints + excluded scope>
- **Stop rules:** <conditions that freeze the Pod to observe-only>

## Escalation

| Trigger | Escalate to | Channel | Timeout |
|---|---|---|---|
| | | | |

## Skills

| id | Skill (Talent) | HL | Description (verb-first) | Trigger |
|---|---|---|---|---|
| S1 | | HL2 | | |

## Knowledge (KB scope)

> What this Pod is permitted to know, inherited from the harness `Know` boundary. This is the *permission* layer. The ontology packs below are what make that knowledge usable.

| KB item | Content | In scope / excluded | Update owner |
|---|---|---|---|
| | | | |

## Outcomes (Platform Step 1 — Overview)

> One outcome per skill/skill cluster. Each: what it does, what it does NOT do, single named output. No overlaps.

| # | Outcome definition (paragraph) | Single output |
|---|---|---|
| 1 | | |

## Ontology packs (Platform Step 2)

> One pack per outcome, minimum. Each pack is a separate file (`ontology-<outcome-slug>.md`) built from `assets/template-ontology-pack.md`. This table is the index; the packs hold the detail. Spec: `references/ontology-design.md`.

| # | Pack file | Serves outcome | Tier | Owner | Version | Review due | Quality gate |
|---|---|---|---|---|---|---|---|
| 1 | `ontology-<outcome-slug>.md` | Outcome #1 | bronze/silver/gold | | 0.1 | | ☐ 14/14 |

### Upload set (what actually goes into Platform Step 2)

> From each pack's Part 1E source inventory. Small single-purpose files only. **No diagrams.**

| Group | What these sources help determine | Source files | Authority rank | Version | Effective from–to | Jurisdiction |
|---|---|---|---|---|---|---|
| Ontology #1 | | decision-rules.md · glossary.md · lexicon.md | | | | |

**Conflict policy:** <prefer higher authority · prefer more recent within rank · escalate to owner · refuse and flag>

**Excluded from upload (human reference only):** `<procedure>.drawio` — stamped DO NOT UPLOAD

## Outcome goals & evidence (the feedback loop)

> Signed by the Pod owner **before** the baseline run. One primary metric per outcome — not three. Detail lives in each `goldens-<outcome-slug>.md`.

| # | Owner goal (one sentence) | Primary metric | Target | Floor | δ | Golden set | Cases | Baseline | Latest verdict | Goal met? | Signed |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | | | | | | `goldens-<outcome-slug>.md` | | | | ☐ | |

**Re-test triggers:** any change per the classification table in `references/pod-evaluation.md` · weekly drift run on frozen cases · quarterly goal re-signature · full 120+ case suite before any HL increase.

**Gate:** non-inferiority plus zero safety regressions. BLOCK on any adversarial or out-of-scope failure, safety-class rule breach, superseded-source citation, drop in escalation recall, or primary metric below floor. On HOLD or BLOCK the previous versions stay in force.

## Talents (Platform Step 3)

> One talent per outcome (Outcome #n ↔ Talent #n ↔ Sub-Role #n).

| # | Name | Description ("Use when…" + trigger phrases) | Operation spec covers |
|---|---|---|---|
| 1 | | | purpose · required inputs · rule tables · exact output layout · what it does NOT do · edge cases |

## Behavioral Guardrails

- <absolute never-do rules>
- <mandatory elements on every output>

## Platform Field Mapping (paste-ready, in platform step order)

| Step | Platform field | Value |
|---|---|---|
| 1 Overview | Pod Name | |
| 1 Overview | Outcome #1…#n | |
| 2 Ontology | Ontology groups + sources (upload set only) | |
| 3 Talent | Talent #1…#n (Name/Description/Operation) | |
| 4 Pod Hierarchy | Role | |
| 4 Pod Hierarchy | Sub-Roles (one per talent) | |
| 4 Pod Hierarchy | Identity | |
| 4 Pod Hierarchy | Audience | |
| 4 Pod Hierarchy | Voice and Tone | |
| 4 Pod Hierarchy | Response Format and Depth | |
| 4 Pod Hierarchy | Authority and Boundaries | |
| 4 Pod Hierarchy | Escalation (incl. Decision Desk route for HL2 choices) | |
| 4 Pod Hierarchy | Guardrails | |
| 4 Pod Hierarchy | Skills (talent names) | |

> Scorer note: the platform rates Outcome–Ontology alignment and each Ontology group on Completeness / Uniqueness / Usability (x/5); all sections must reach satisfactory level to proceed. Every promise in an outcome needs a source that covers it. The platform auto-generates the System Message per role/sub-role in the eight sections above. Talent Descriptions start "Use when…". The user uploads sources by drag and drop and clicks Submit; this spec is paste-ready only after Gate G8.

## Platform pre-checks

| # | Check | Result (pass / fail / waived) | Note |
|---|---|---|---|
| 1 | Promise-to-source: every outcome promise covered by a source | | |
| 2 | Outcome form: user, task, exclusions, one output, no overlap | | |
| 3 | Each ontology group answers "What do these sources help determine?" | | |
| 4 | Talent form: capability name, "Use when…" description, full Operation | | |
| 5 | Hierarchy covers the eight System Message sections | | |
| 6 | Human decision routes/receipts; required calculated Desk gate with policy, options, constraints, approver and originating return | | |

## Deployment handoff

> Prepare at G0 and reconcile at G8 using `references/platform-evidence-and-onboarding.md`. This records operational dependencies; it does not execute deployment or establish client acceptance. Keep G0–G8 design approvals separate from runtime approvals and release evidence.

| Item | Requirement / target | Status | Evidence / date / configuration | Next owner / action |
|---|---|---|---|---|
| Target and actors | <environment/build/workspace, identity/access dimensions, responsible roles> | specified | <not verified> | <TBD> |
| Knowledge | <source owner/version, KB/group, admissibility and known-answer checks> | specified | <not verified> | <TBD> |
| Connectors | <approved instance/company/module, read/write scope and reconciliation> | specified | <not verified> | <TBD> |
| Configuration | <saved/reopened fields and correct evaluations> | specified | <not verified> | <TBD> |
| Availability | <reviewed/published/assigned/activated/invoked with actor evidence> | specified | <not verified> | <TBD> |
| User acceptance | <intended-user success, restricted-user denial and output checks> | specified | <not verified> | <TBD> |
| Action controls | <approval-to-action linkage, baseline, rejection/expiry and resulting state> | specified | <not verified> | <TBD> |
| Training and operations | <repeatable task, limits, escalation, transfer and revalidation> | specified | <not verified> | <TBD> |

Allowed statuses: **specified**, **verified**, **blocked**, or **not applicable with reason**. Link unresolved rows to Open items and framework coverage; do not fill missing evidence with a score, generated claim or account-attribution label. Publication/client acceptance remain pending until separately evidenced.


## Operating playbook

Use `references/converse-operating-process.md` and `references/converse-prompt-playbook.md` relative to the builder skill. Bind exact resources and versions; no credentials or unresolved execution placeholders.

| Component | Purpose / trigger | Inputs / scope | Output / destination | Authority / human gate | Status / evidence | Stop / recovery / owner |
|---|---|---|---|---|---|---|
| Preflight and intake | | | | | specified | |
| Dashboard and tracker | | | | | specified | |
| Collection / Blueprint | | | | | specified or not applicable with reason | |
| Workflow per repeatable output / decision-bearing operation | | | | | specified; not applicable only for a process without these operations | |
| Schedule | | | | | specified or not applicable with reason | |
| Decision Desk | | | | | specified or not applicable with reason | |
| Chat decision recording | | | | | blocked until required identity/receipt controls verified | |

For database-backed cases, complete the applicable rows below using `references/case-operations-contract.md`. Logical labels are examples; bind them to the client's existing system. Mark unused rows not applicable with reason.

| Case operation | Approved design / binding | Verification and remaining check |
|---|---|---|
| Deployment profile | <one bootstrap; resource scope; connector; schema/source catalogue; provenance mode> | <fresh-context retrieval; exact versions; no global search> |
| Recorder and ledger | <writer; stable intent key; before/intended/actual values; prepare/apply/read-back> | <actual Converse probe; timeout/conflict reconciliation; no atomic-lock claim> |
| Evidence dependency | <requirements/claims; requests; purpose-scoped review; policy/calculation/business gates> | <no circular gate; changed-basis stale results; retained decisions> |
| Case Overview | <authoritative joins; stages; actor/action/due; source links; receipt health; freshness> | <blank/duplicate/unmapped/new-row checks; rendered view separately> |
| Notifications and impact | <template/trigger; recipient/sender; dedup; signed/realised units/periods> | <transport evidence; no repeat sends; sample exclusion; actual reporting review> |

Include: data contract and vocabulary; case/revision keys; transition and rejection precedence; identity/assignment/approval policy; write/read-back and duplicate handling; stage tracker/freshness/fallback; diagnostics and acceptance case IDs. Attach tailored sequential prompts with expected results and stop conditions. Design approval, platform availability and runtime acceptance remain separate. Do not invent automatic links between components.

## Workflow execution manifest and acceptance ledger

Use `references/workflow-execution-contract.md`. Keep one row per repeatable output; bind templates/procedures independently. Native kinds and enforcement remain unverified until observed.

| Output / Workflow | Trigger / case inputs | Exact version / workspace / privacy | Task kinds / Pod / Sources / template version | Human gate / permitted write | Read / gate / result / receipt evidence | State / blocker / next owner |
|---|---|---|---|---|---|---|
| <named output> | <case/revision/snapshot> | <saved definition> | <per-task read-back> | <explicit policy> | <actual links or not run> | <configured/published/invoked/verified/blocked/not run> |

Record source-text access separately from associations; compare native chat and Workflow reads when diagnosing. For required calculations, link model/solve/result/acceptance and the originating return. Preserve unchanged decisions; no approval inferred from green ticks. Include bilateral outcome and separate signed/realised reporting evidence where relevant.

## Approval log

| Gate | Stage | Date | Approver | Approved content / version | Reopened by |
|---|---|---|---|---|---|
| G0 | Intake | | | | |
| G1 | Identity | | | | |
| G2 | Skills → Talents and Outcomes | | | | |
| G3 | Authority | | | | |
| G4 | Escalation | | | | |
| G5 | Persona, audience, format | | | | |
| G6 | Ontology packs | | | | |
| G7 | Golden set | | | | |
| G8 | Emit and submission readiness | | | | |

Gate values in frontmatter: `open` or `approved <YYYY-MM-DD>`. A change to an approved gate reopens it and every later gate that depends on it.
