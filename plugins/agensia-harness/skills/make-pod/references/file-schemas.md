# P2A File Schemas & Repository Layout

All artifacts: UTF-8 markdown + YAML frontmatter. Frontmatter = machine contract; body = human contract. `snake_case` fields, ISO dates, IDs never reused.

## Repository layout (flat — no subfolders)

```
<company-process-repo>/
├── README.md                     # company header: legal name, industry, overlay standard
├── capability-map.md             # whole capability map, one file
├── value-streams.md              # all value streams, one file
├── capability-<apqc>-<slug>.md
├── process-<apqc>-<slug>.md      (+ optional .bpmn XML twin)
├── harness-<slug>.md
├── ontology-<outcome-slug>.md
├── goldens-<outcome-slug>.md
├── decision-rules-<outcome-slug>.md   # pack-local source
├── glossary-<outcome-slug>.md         # pack-local source
├── lexicon-<outcome-slug>.md          # pack-local source
├── <standard-short-name>.md           # as9100.md, iso-9001.md, pdpa-my.md — shared
├── <process-slug>.drawio              # human reference, never uploaded
├── pod-<role>-<subrole>.md
├── pod-charter-<slug>.md         # consultant mode: drivers, goals, stakeholders (TOGAF A)
├── sipoc-raci-<slug>.md          # consultant mode: SIPOC, RACI, decision rights (TOGAF B)
├── data-connector-<slug>.md      # data objects, connectors, environments (TOGAF C/D)
├── role-binding-<slug>.md        # role → current holder and cover; uploaded as a source
├── pod-contract-<slug>.md        # playback log + signed design agreement (TOGAF G)
├── data-object-<slug>.md
├── system-<slug>.md
└── decisions-log.md              # append-only ADRs
```

**Flat means flat.** Every cross-reference between artifacts is a bare filename in this directory — `as9100.md`, never `./ontology/as9100.md` or `standards/as9100.md`. Names must be unique repo-wide: standards take the instrument's short name and are shared across packs; pack-local sources are suffixed with the outcome slug.

Link chain: `capability ─contains→ process ─governed-by→ harness ─deployed-as→ pod ─knows-via→ ontology ─proven-by→ golden-set`.

## Common frontmatter (all artifacts)

```yaml
artifact:        # capability | process-card | harness-spec | pod-spec | ontology-pack | golden-set | data-object | system
framework: p2a
version: "1.0"
status: draft    # draft | reviewed | active | deprecated | superseded | retired
owner:           # accountable role, not a person's name
updated:         # YYYY-MM-DD
```

## Per-artifact fields

**capability**: `apqc_id`, `name`, `value_streams[]`, `processes[]`, `overlay`

**process-card**: `apqc_id`, `name`, `capability`, `bpmn_file?`, `trigger`, `outcome`, `sla`, `lanes[{lane, owner_role}]`, `agent_assignment[{pod, skills[]}]`. Body: activity table (`id|name|bpmn_type|lane|systems|data|decision_rule|hl|escalate_to|evidence`) + `## Gateways` with plain-language conditions.

**harness-spec**: `name`, `processes[]`, `headline_hl`, `policy_constraints[]`, `evidence_store`, `review_cadence`, `kill_switch_roles[]`. Body sections (all mandatory): `## Know`, `## Decide`, `## Do`, `## Prove`, `## Escalate`, `## Learn` — scoped per skill. Under Prove, include `### Control verification`: control ID, action/target, preconditions/approval evidence, enforcement location/owner, failure behavior, test/state evidence with configuration/version/date, and `specified|verified|blocked` status. Include context/tool-loop limits; unobserved controls remain `specified`, not `verified`.

**pod-spec**: `role`, `subrole`, `harness`, `ontologies[{id, file, serves_outcome, tier}]`, `goldens[{id, file, serves_outcome, baseline_run}]`, `platform`, `headline_hl`, `skills[{id, name, from_activity, hl}]`, `gates{G0…G8: open | approved <date>}`, `workspace`, `environment`, `production_changes: prohibited`. Body: `## Identity`, `## Prompt framework coverage`, `## Persona & Voice`, `## Audience`, `## Response Format & Depth`, `## Authority Boundaries`, `## Escalation`, `## Skills`, `## Knowledge (KB scope)`, `## Outcomes`, `## Ontology packs`, `## Outcome goals & evidence`, `## Talents`, `## Behavioral Guardrails`, `## Platform Field Mapping`, `## Platform pre-checks`, `## Deployment handoff`, `## Operating playbook`, `## Approval log`. Framework coverage has seven rows per outcome (Outcome, Context, Sources, Scope, Authority, Output, Verification), each recording the agreed requirement, canonical artifact/section or rule ID, gate and unresolved item/owner; also a labelled example invocation and separate design/baseline/control readiness.

The Pod Deployment handoff records target/actors, knowledge, connectors, configuration read-back, availability, user acceptance, action controls and training/operations. Each row contains requirement/target, specified|verified|blocked|not applicable with reason, dated configuration-bound evidence and next owner/action. Link gaps to Open items; design approval does not establish deployment acceptance.

**ontology-pack**: `ontology_id`, `serves_outcome` (integer — the Step 1 outcome number), `outcome_title`, `pod`, `harness`, `tier` (bronze|silver|gold), `effective_from`, `effective_to`, `supersedes`, `superseded_by`, `jurisdiction`, `volatility`, `ttl`, `review_due`, `review_cadence`, `conflict_policy`, `retention?`. Authority rank is per source item in the Part 1E table, not a pack-level field. Body sections (all mandatory): `## Part 1 — Domain knowledge & standards` (1A competency questions · 1B controlled vocabulary · 1C standards & governance instruments · 1D reuse record · 1E source inventory), `## Part 2 — Procedure & human checkpoints` (typed step table + gate table + visualisation record), `## Part 3 — Harness: do / do-not` (do-list · ≤5 paired prohibitions · decision tables with hit policy · evidence contract), `## Part 4 — Language, persona & output format`, `## Pre-upload quality gate`, `## Open items`, `## Change log`. Spec: `references/ontology-design.md`.

**golden-set**: `goldens_id`, `serves_outcome` (integer), `outcome_title`, `pod`, `ontology`, `harness`, `goal`, `primary_metric`, `target`, `floor`, `ni_margin`, `signed_by`, `signed_on`, `case_count`, `strata{happy,edge,adversarial,regression,out_of_scope}`, `blind_holdout`, `mde`, `eval_temperature`, `repeats`, `baseline_run`. Body sections (all mandatory): `## Cases` (five stratum tables + blind holdout), `## Scorecard` (Tier A deterministic · Tier B judged · Tier C budget), `## Run log` (append-only) + per-stratum results, `## Gate record`, `## Goal conformance`, `## Overrides awaiting triage`, `## Open items`, `## Change log`. Spec: `references/pod-evaluation.md`.

**data-object**: `name`, `standard_mapping`, `systems[]`, `sensitivity`, `residency`, `retention`

**system**: `name`, `system_type`, `api_style`, `auth_model`, `write_allowed_hl` (system-side HL cap; caps compose by minimum)

The golden-set Scorecard also includes a **Framework verification evidence** table linking each framework item/requirement to case IDs, instruction coverage, observed behavior, artifact/citation/state evidence and control IDs. Keep blind cases ID-only and unobserved results `not run`. This adds evidence detail without changing existing metric thresholds or verdicts.

## Runtime trace records (P2A execution trace triad)

```yaml
# work-request
request_id: ""
definition: process-<…>.md#A3
requested_by: ""
state: requested   # requested|accepted|in-progress|completed|failed|cancelled|escalated
hl_at_execution: HL2
# work-event (immutable)
event_id: ""
request_id: ""
actor: pod-<…>.md#S2
action: ""
evidence_ref: ""
timestamp: ""
```

## Validation rules (lintable)

1. Every process-card references an existing capability; every harness-spec references `active`/`reviewed` process cards; every pod-spec references exactly one harness-spec.
2. `headline_hl` in pod-spec == max skill `hl` == harness `headline_hl`.
3. Every skill at HL1+ has a non-empty escalation row.
4. No pod-spec may be `active` while its harness is `draft`.
5. Any HL increase requires a major version bump on the harness spec.
6. Every outcome in a pod-spec has ≥1 ontology pack; every ontology pack names exactly one primary `serves_outcome`.
7. Ontology `tier` ≥ the tier required by the pod's `headline_hl` (HL0–HL1 → bronze · HL2 or external client → silver · HL3+ or regulated client → gold). An HL increase forces the tier upgrade *before* sign-off.
8. No ontology pack may be in an upload set while `status: superseded`/`retired`, or past `effective_to`.
9. Every ontology pack has a named `owner` and a `review_due` date; every source item in Part 1E has an authority rank 1–5.
10. Every competency question in Part 1A maps to ≥1 source item, or is listed as a coverage gap in Open items.
11. No `.drawio`/diagram file appears in an upload set.
12. Every file reference in any artifact is a bare filename — no `./`, no folder segment, no absolute path. Filenames are unique repo-wide.
13. Every outcome has exactly one golden set; every golden set names one `serves_outcome` and references an existing ontology pack for that same outcome.
14. No pod-spec may be `active` while any of its golden sets has `baseline_run: none`, an unsigned goal (`signed_by` empty), or no `target` and `floor`.
15. Run-log rows are append-only. Every row records golden-set version, pack version, harness version, model + provider version, `b`, `c`, verdict and gate decision.
16. A gate decision of BLOCK or HOLD may not be followed by a version bump on the pack, harness or pod-spec — rollback is the default state.
17. Any HL increase requires the latest run to be `PROMOTE` with verdict `IMPROVED`, `case_count` ≥ 120, `repeats` ≥ 3, and zero adversarial or out-of-scope failures.
18. `strata` counts sum to `case_count`; the adversarial and out-of-scope strata are non-empty for any Pod above HL0.
19. No pod-spec may be `reviewed` or `active` while any gate G0–G8 is `open`, or while any platform pre-check is `fail` without a written waiver in the Approval log.
20. A pod-spec changed after G8 returns to `draft`, and the gates its change touches reopen.
21. Every outcome has all seven framework coverage rows, linked to canonical requirements and verification cases or explicit Open items; no framework label implies an approval or permission.
22. A required control is `verified` only with observed enforcement/state evidence for the relevant configuration/version. Unverified required controls and unrun baselines prevent claiming the dependent capability is ready for go-live; a draft or reviewed design may record them as pending.

The Operating playbook records each applicable component, trigger, scoped inputs, output/destination, authority, status/evidence, stop/recovery owner and bound sequential prompts. Include data/transition contracts, dashboard freshness, diagnostics and acceptance checks; unverified controls remain blocked.

## Target boundary

Pod specifications must identify a verified non-production environment before operations; unresolved targets remain blocked. Harnesses retain the non-waivable prohibition on Agensia production creation, push, publication, execution and mutation, including connected production resources. A design approval cannot remove this boundary.
