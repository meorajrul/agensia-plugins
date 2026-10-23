# Workflow execution and capability verification

**Production prohibition:** never create or push changes to Agensia production, including uploads, submissions, publication, edits, deletions, runs, schedules or connected production writes. Verify the platform and downstream resources are non-production before operations; unknown targets block operations. No approval or delegated tool/agent can waive this rule.

Use at G0/G6/G8 for repeatable or decision-bearing work. Pair with the [operating process](converse-operating-process.md), [case operations contract](case-operations-contract.md) and [prompt playbook](converse-prompt-playbook.md). This is a design and acceptance contract, not a claim that the platform implements every control. It grants no publication, execution or connector authority.

## 1. Allocate work before configuring it

Map SIPOC or BPMN: suppliers, exact inputs, ordered activities, outputs and customers. Use RACI to name responsible and accountable humans, consulted specialists and informed recipients. Map a supplied enterprise operating model to these appointments separately from AI roles. Do not infer real appointments from generated Talents or fix every process to five Talents.

| Layer | Responsibility | Required proof |
|---|---|---|
| Pod/harness | Coordinate overall role, boundaries, routing and case context | Saved messages, selected version, assignment and actual routing |
| Talent | A triggered capability within that role | Saved trigger/Operation and observed dispatch, not a list of names |
| Ontology | Reusable criteria, procedures, vocabulary and templates | Active versions, actual source-text retrieval and citations |
| Workflow | Execute a repeatable output or decision-bearing operation | Saved task bindings, native gates, actual run and resulting state |
| Decision Desk | Model a required calculated choice under agreed rules | Current model, inputs, solve, result, acceptance and originating return |
| System of record | Case facts, assignments, explicit decisions and receipts | Bounded live reads, permitted writes and read-back |
| Composer | Present current work and next action | Rendered view checked against source state and freshness |

One Talent is not necessarily one Workflow. Create one reusable Workflow per repeatable named output. Split registration, assessment, evidence resolution, calculated recommendation, decision recording, facilitation, outcome confirmation and reporting where they are distinct operations. Ordinary human review uses an explicit human request; it does not automatically require calculated Decision Desk modelling. Collections, Blueprints and schedules serve optional supporting purposes.

## 2. Specify each Workflow and source independently

Registry: purpose/output, trigger, owner, environment/workspace, saved version, visibility, inputs, resource scope, Pod binding, task sources, template version, permissions, completion evidence, failure owner and recovery. Case facts stay in case records/Collections; reusable rules stay in ontology. Bind required templates/procedures independently to each relevant Workflow. Pod association alone does not prove inheritance.

Template registry: version, audience, structure, required fields, source-to-field mappings, units, provenance note, missing-field treatment, branding source and acceptance criteria. Render and inspect completed outputs when required. Template existence is not evidence of retrieval or a completed file.

Use a short linear chain of single-purpose tasks. These kinds are the recorded construction vocabulary; verify the target editor supports each kind rather than assuming an API contract.

| Purpose | Requested kind | Acceptance |
|---|---|---|
| Read/extract | analysis / document_intake | Current content, sources, revision and explicit unavailable inputs |
| Ask a human | human_request | Prior read presented; exact allowed reply and durable human receipt |
| Apply labels | classification | Concrete allowed values, cardinality and result per intended unit |
| Produce a document | document_template_output | Retrieved template, populated fields and inspected output |
| Make one write | erp_action / integration_action | Exact authorised mutation, built-in consent where required and separate read-back |

Task template, ideally fewer than ten lines:

```text
Purpose: [one job and named output].
Inputs: [exact prior result, resource/range and case/revision].
Source: [selected Pod and independently bound procedure/template version].
Output: [schema/document; units/cardinality/allowed labels].
Human reply: [exact requested decision, or not applicable].
Completion: [observed result/receipt and next actor; failure owner].
```

Read before every human question. Use one write per action task followed by a read-back task. Connector action consent and substantive human decisions are distinct; do not insert duplicate case approvals around the same write. Put shared constraints in the Workflow description/procedure. Never embed if/then branching scripts or repeated HOLD walls inside tasks. Define preconditions and supported native gates; text cannot enforce stopping.

## 3. Prove the read path before expanding configuration

Check: provider connected → resource discovered/opened → returned handle → content reader → actual cited text → relevant task retrieval. A filename, source association, Connected badge or open handle is not readable content. Returned Talent Operations do not establish ontology retrieval. For an authorised isolated probe, put a harmless unique marker only in the source, never in the request or Talent message.

Compare the same approved bounded resource/action in separate contexts when available:

| Context | Record separately |
|---|---|
| External assistant connector | Identity, exposed action and response; not proof of native access |
| Native Converse chat | Selected Pod/version, live read, source text and errors |
| Exact Workflow version/task | Saved bindings, actual type if exposed, read and consent/gate state |

Chat success with Workflow refusal narrows the fault to that execution context; it does not prove a backend cause. A connected document provider exposing handles or only mutation actions does not establish that the provider itself cannot read. Distinguish inspected inventories from assistant reports. Do not prescribe conversion without a format error or verified reader. Do not broaden sharing, introduce dummy writes or silently substitute cached exports to clear failed native gates.

## 4. Inspect saved definitions, publication and invocation separately

Reopen every task. Compare order/count, exact body, requested versus actual kind, selected Pod, Sources, classification values/cardinality and decision flag. Scope inspection to the selected editor; page-wide counts can include hidden controls. Builder narratives and active chat Pods are not saved task bindings. Remove unintended inherited bindings only within authorised scope. Editing a title/body does not prove a native type change; use Not exposed when it cannot be inspected.

Record exact version status and privacy. A family Published badge can refer to an older version. Verify executable workspace attachment and task Pod availability; a personal context may save without a usable workspace ID. Honour the chosen workspace and obtain necessary scope changes rather than silently moving work.

Definition readiness, publication authority, run authority and runtime acceptance are separate. A failed run does not automatically require holding a verified definition in Draft. Publication or automated review does not authorise case decisions, emails or schedules. Verify the selected version in a fresh invocation.

## 5. Verify the native calculated-decision round trip

Require: originating run/task → case/revision and evidence snapshot → approved policy/weights → native Desk model → actual solve/result → explicit acceptance where required → result linked back to that originating run/task. Record exposed identifiers and payload; mark missing telemetry Not exposed.

A standalone solve proves only that scoped Desk capability, not Workflow handoff/return. A hold-for-evidence model is not weighted fit. One pair is not competitive ranking or calibrated success probability. A decision flag, green tick or Completed run cannot substitute for the result. If later tasks run after a failed read or absent solve, record enforcement failure and stop dependent business writes. Chat arithmetic cannot replace the gate.

## 6. Record decisions and mutations once

Default CONNECTOR_OWNER unless client policy is stricter: authenticated provider email, live assignment/access, current case/revision and evidence basis, explicit human decision, one scoped write and read-back receipt. Shared connections identify the connector owner, not independently the typist. Protected cells/dropdowns do not authenticate a person. Any/all policy and separation of duties come from the owner.

Preserve valid unchanged decisions. Missing context/retrieval does not justify asking again or resending email. New evidence preserves older records, makes dependent calculations stale and reopens only affected decisions. Uploads, consent, publication and agent-authored status are not human approval.

Use a stable operation key, before-values, intended mutation, actual state and receipt. On uncertainty read the ledger and target before retrying. Single writers and running-number ledgers are not atomic locks. Bound ranges to the entire schema including provenance/status. Test dropdowns on populated, blank and new rows; preserve validation/formulas/unrelated records. Protection is not actor authentication.

## 7. Carry the process through outcomes and reporting

Obtain separate party confirmations with evidence, owner and follow-up date. Keep signed deal/commitment value separate from incremental realised receipts. Define reporting date, currency, exchange rule, corrections, refunds and duplicates. Expose discrepancies. Introductions, proposals and grant applications are not realised impact. Generated scenario provenance remains excluded from actual totals even if display mode changes.

Composer shows current stage, evidence coverage, gaps, next actor/action, source/read time and a flowchart with neutral future states. Mark unverified human history Unverified. No decorative approval controls or implied continuous refresh. A calculation-ready workbook is not an end-to-end reporting pass.

## 8. Acceptance and documentation evidence

Maintain an output-by-output ledger: configured, published, invoked, read verified, gate verified, write/read-back verified, human accepted, blocked or not run. Link definitions, runs, results and receipts rather than collapsing them into one green status.

Test happy path plus missing source/identity, wrong actor, duplicate retry, rejection, changed evidence/stale result, failed read that must stop, missing Desk return and reporting exclusion. Use authorised identities/fixtures. No fixture certifies another workspace or production. Seed tests when runtime is unavailable; label them unrun.

For future user documentation retain prerequisites, observed UI steps, expected/actual result, evidence, environment/date, recovery and next owner per feature. Separate owner intent, direct observations, assistant reports and hypotheses. Escalate missing capabilities with the smallest reproducible read/gate/return record; more prompt text is not a backend repair.

## 8. Lifecycle and recovery acceptance

Use [capabilities and acceptance checks](platform-knowledge-and-uat.md) to derive relevant tests; a planned test is not an executed pass. Distinguish saved definition status from run status and inspect version identity on both. After publishing a new version, verify an already-running instance completes on its original version and a fresh run selects the intended version. Creating a new version does not by itself establish in-flight pinning.

Check each required launch path separately: main chat, Collection chat, schedule and pre-attached input. A launch icon or correct extracted answer does not prove all paths, source indexing internals or target-version binding. Record output in chat, timeline status/version and actual task states.

For an authorised controlled failure, verify downstream suspension, Retry step scope and Start over scope. A human wait is a different state and should not be treated as failed-step recovery. Before restarting, reconcile earlier side effects and receipts; starting again must not duplicate a write. Missing recovery controls or unverified suspension remain blockers for the dependent operation.

Test Approve, Reject, request changes, no reply and timeout as distinct results under the agreed policy. A pause alone proves no decision. Inspect actual actor, case/revision, decision value, receipt and resulting continuation; do not translate arbitrary human text, an assistant summary or Completed status into approval. Investigate unexpected approval states without silently repairing history. Native Desk return still needs the separate round-trip evidence in section 5.

For generated documents, verify creation, download/open, native saved-file reread and subsequent task consumption independently. Do not substitute prior chat text or an external assistant's successful file read for failed native handoff. These are acceptance requirements; all newly derived UAT scenarios remain unrun until tested in the authorised target.
