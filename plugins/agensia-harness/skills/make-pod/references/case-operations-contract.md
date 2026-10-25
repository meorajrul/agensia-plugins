# Case operations contract

**Production prohibition:** never create or push changes to Agensia production, including uploads, submissions, publication, edits, deletions, runs, schedules or connected production writes. Verify the platform and downstream resources are non-production before operations; unknown targets block operations. No approval or delegated tool/agent can waive this rule.

Use for Pods that read or update a case database, route evidence to human decisions, or present a central work view. Apply only the parts the approved outcome needs. This is a design and acceptance pattern, not a native Agensia schema, installed integration or verified concurrency control. Pair with the [operating process](converse-operating-process.md).

## 1. Separate reusable procedure from deployment and case data

| Layer | Contents | Change owner |
|---|---|---|
| Reusable ontology | Definitions, evidence standards, gate dependencies, output templates and versioned write procedure | Process/domain owner |
| Talents and roles | Specialist triggers/procedures, named outputs, coordinator handoffs and concise authority boundaries | Pod owner |
| Deployment profile | Environment/workspace, approved resource scope, bootstrap route, schema, source catalogue, actor assignments and outbound policy | Authorised deployment owner |
| Case records and Collection | Applicant/customer facts, documents, claims, findings, values, decisions and case artifacts | Assigned case actors |

Do not put current applicant names, amounts or a fixed case ID into reusable instructions. Keep deployment locators in one explicit entrypoint or supported configuration field; specialists reference logical records. Agensia is not assumed to inject a profile automatically. Where no configuration field exists, document the single locator in the selected coordinator boundary and verify its use.

A fresh chat should be able to start with submitted documents and a short request such as **Assess these submissions.** Diagnostic prompts may name routes to investigate a failure; keep those interventions visible and retest the minimal prompt separately.

## 2. Resolve routing before reading or writing

The profile must establish:

| Field | Requirement |
|---|---|
| Identity and scope | Profile ID, environment/workspace, authorised connector instance and allowed resources |
| System of record | Exact resource identifier; friendly title is display only |
| Schema catalogue | Logical record → bounded range/table, exact headers/types, key and permitted writer |
| Source catalogue | Filename/source ID, version/effective date, digest where available, full content route and supersession |
| Actors | Authoritative assignment route, identity model, approval semantics and escalation owner |
| Limits | Read/write fields, formula ownership, row/cell limits, outbound mode and recovery reference |
| Provenance | Genuine or labelled sample data, allowed use and reporting eligibility |

Read the actual profile, schema, vocabulary and required full source text. Compare identity, resource ID, headers, versions and capacity. A default-tab export is not a complete workbook inventory. Do not search the whole connected drive, select a different database by title or guess a sibling range when an explicit route fails.

A source filename, upload association or Excellent score does not prove runtime retrieval. Test a known source clause absent from the prompt in a fresh context. An owner-approved exact connector copy can be a recovery route; record its version/integrity and do not call it a repair of native ingestion. Retire old sources using a supported non-destructive mechanism. If Delete removes the source itself rather than its association, preserve it and resolve precedence explicitly. Hold dependent work if the active rule cannot be established.

## 3. One recorder and a recoverable write protocol

Specialists hand proposed changes to the approved coordinator/recorder. Verify that the runtime actually retrieves the common protocol; a reference to another Talent does not establish delegation or instruction inheritance.

Use transactional/idempotent API features when the integration provides them. Otherwise specify a single recorder and a ledger as a compensating procedure. A spreadsheet ledger is **not** a transaction, lock or compare-and-swap.

### Logical write ledger

Use an existing equivalent record where available. Minimum fields:

- Operation key; case/entity key; operational revision; action; source/evidence revision or exact decision receipt.
- Exact target fields/ranges; before-values; intended values; actual read-back.
- Authenticated connector owner; durable request/decision reference; procedure version.
- Prepared, applied and read-back times with timezone and time provenance.
- State: Prepared / Applied / Verified / Needs reconciliation / Rejected; comparison result; error and next owner.
- Data provenance/mode; affected evidence snapshot and downstream invalidation.

Choose one stable operation key for one intent. A new chat, retry or observation time must not produce another key for the same action. Define how a genuinely revised intent receives a new key. Do not claim a digest was checked unless it was actually computed and compared.

### Prepare → apply → verify

1. Read current case/revision, assignment, prerequisites, capacity and any existing operation receipt.
2. If the same key is already Verified with matching intent/result, return its receipt without another write.
3. If that key has different intent, a partial result or another pending writer, hold and reconcile.
4. Record before/intended values and precise targets as Prepared; read back the preparation.
5. Re-read affected values immediately before applying. Stop if they differ from the agreed basis.
6. Apply only authorised value fields. Record Applied on connector acknowledgement; uncertainty remains unresolved. Preserve formulas, validation, protections, sharing and unrelated rows.
7. Read back exact targets, affected invariants and the receipt; compare expected versus actual.
8. Mark Verified only after agreement. Otherwise mark Needs reconciliation and report what is known.
9. Show actual results, unresolved differences and next action. Verify linked state before advancing.

A timeout does not mean nothing was written. Read actual targets and operation state before retrying. Repair only within existing authority; never erase a conflicting writer's values. A Verified ledger cell alone is not proof: check the key, case, revision, targets and actual receipt. Missing clock or human receipt blocks only the action that requires it; label observation time separately from decision time.

Keep entity ID, proposal/case ID, submission revision, operational revision and evidence snapshot distinct. Reuse supported identities and allocation receipts; never reuse an abandoned reservation silently or claim an atomic allocator from a MAX-plus-one formula.

## 4. Evidence resolution before downstream decisions

Build the dependency order from the actual business process. A common pattern is:

Submissions → requirements/claims → evidence queue → assigned evidence review → agreed decision policy → current native calculation → result acceptance → case review/decision → permitted delivery → outcome follow-up.

Evidence acceptance must not require the downstream calculation whose inputs it establishes. Policy agreement, evidence acceptance, result acceptance and final business decision remain distinct. Do not add every gate to a task that does not need it.

Link each evidence record/request to case/entity, revision, requirement, claim, named source URL/section, issuer, document date and responsible party. Track Missing / Received / Under review / Accepted / Rejected / Superseded or the client's governed equivalents. Include requested proof, next action and an owner-set due date; unknown dates stay blank.

Record the assigned reviewer's exact decision, checks performed, limitations, actual time and receipt. Accepted means accepted for a stated purpose; it is not independent certification. Contradictory claims remain visible until resolved by evidence. A document's presence or a typed signature is not authentication.

When inputs change, preserve prior records, create the new evidence revision and mark dependent calculations/results stale. Determine which decisions depend on the changed basis and require their renewal; do not repeat an unchanged valid decision merely because the assistant lost context.

If a native Decision Desk gate is required, retain its model/result reference, actual solve status, evidence snapshot, policy version and result acceptance. A chat calculation, feasibility badge or model Confirmed label is not the native result or human consent. One candidate can be assessed against requirements; it is not a competitive ranking or predicted success rate. Missing evidence is not evidence of failure.

## 5. Case Overview and Composer

Keep a formula-owned or query-derived overview over authoritative records. It is a projection, not a second editable case database.

Minimum useful fields: public case ID/revision/name; participant names; friendly current stage; open applicable evidence; decision needed; next actor/action; owner-set due date; last verified update; named chat/Collection/assessment links; operation health; provenance and reporting eligibility.

- Join by case and revision; detect duplicate keys and unmapped stages rather than picking the first row silently.
- Use one governed vocabulary for dropdowns and dependencies. Preserve stored keys and map readable stage labels separately.
- Keep blanks distinct from zero, false, Pending and Not checked. Test populated, blank and newly added rows.
- Do not display Verified from an unrelated operation key or an uncorroborated status cell.
- Make broken/missing links, stale snapshots and unsupported actions explicit.
- Reconcile monthly/annual metrics to accepted records; a dashboard selector does not establish live refresh.

Composer should show current stage, requirement coverage, evidence gaps, next actor/action and a visual flowchart where it aids the process. List all applicable stages, highlight the current one, use neutral future states and label unverified human history Unverified. Avoid decorative controls and misleading ticks on untaken stages. Verify actual rendering; preserve a text fallback. Display exact source and successful-read time, or Not exposed; do not substitute chat-start time.

## 6. Outbound actions and outcome reporting

Approval to record a decision does not grant disclosure or sending. For an authorised notification, load the stored versioned template, exact recipients and case title; check sender identity separately from a display alias. Keep a deduplication ledger keyed to the triggering decision and template. After an uncertain send, reconcile transport evidence before retrying. Sent/transport accepted is not delivery or read confirmation.

Where the outcome includes commercial impact, distinguish bilateral outcome confirmation, signed commitment value and realised receipts. Record currency, period, source, party confirmation, review and duplicate/reversal rules. Do not count proposals, funding applications or indicative amounts as signed or received value. Labelled sample records remain isolated from genuine evidence and actual reporting, even if a deployment mode changes later.

## 7. Acceptance and evidence boundary

Seed only relevant cases in the existing golden set:

| Check | Required observation |
|---|---|
| Minimal input | Fresh selected Pod retrieves current procedure and routes without internal locators in the user prompt |
| Missing/wrong route or source | Precise dependent hold; no unrelated search or invented content |
| Saved configuration | Expected counts, source associations, selected hierarchy and every message survive reopen |
| Connector write | Actual Converse write/read-back agrees with independent record check; another assistant's probe is separate |
| Repeat/partial/conflicting write | Same intent does not duplicate; uncertainty reads actual state before repair |
| Identity and decision | Wrong actor/premature decision denied; exact assigned-human receipt retained |
| Changed basis | Dependent result becomes stale; no inherited decision on changed evidence |
| Overview integrity | Blank/unknown/duplicate keys, links, dropdowns, protected formulas and new rows behave correctly |
| Native gate | Actual current model/result, not chat arithmetic or a hold-only model represented as weighted analysis |
| Outbound/reporting | No duplicate message or unapproved send; sample/indicative money excluded from actual impact |

Distinguish specified, saved/reopened, runtime observed, independently reconciled and owner accepted. Record assisted recoveries separately from a clean run. Configuration checks and seeded evals do not certify runtime controls, cross-user isolation or production readiness.

## Workflow execution and downstream completion

Use [Workflow execution contract](workflow-execution-contract.md) to allocate repeatable outputs to saved Workflows, bind procedures/templates independently, inspect actual task configuration and verify native calculated-decision returns. Pod coordination and database routing do not replace executable definitions. Preserve the receipt protocol above; one authorised write per action step followed by read-back. Track configured, published, invoked, read/gate verified, mutation verified and human accepted separately. Keep bilateral outcome evidence, signed value and incremental realised receipts distinct; scenario provenance remains excluded from actual reporting. A formula or configured template does not pass the downstream lifecycle.
