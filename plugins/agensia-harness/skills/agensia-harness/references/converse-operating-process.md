# Repeatable Converse operating process

**Production prohibition:** never create or push changes to Agensia production, including uploads, submissions, publication, edits, deletions, runs, schedules or connected production writes. Verify the platform and downstream resources are non-production before operations; unknown targets block operations. No approval or delegated tool/agent can waive this rule.

Use at G0 to identify dependencies, G3–G6 to define controls and data, and G8 to prepare the operating handoff. This is a client-neutral design and acceptance procedure. It adds no permissions and does not replace G0–G8. Pair with [copy-and-paste prompts](converse-prompt-playbook.md).

## 1. Define the process before the Pod

Map SIPOC or BPMN first; use RACI and the supplied enterprise operating model to distinguish human appointments from AI responsibilities. Record beneficiary, accountable owner, trigger, named output, success criteria, stages, exceptions, evidence and next actor. Select the smallest useful end-to-end case. Separate the normal path from missing evidence, rejected, changes requested, expired and integration failure paths. Define precedence: missing mandatory evidence cannot be disguised by a favourable recommendation.

## 2. Establish the data contract

Bind exact approved resources; never assume a workbook or folder name uniquely identifies one. A spreadsheet is optional: use the client's authorised system of record.

| Logical record | Minimum purpose |
|---|---|
| Cases | Stable case ID, revision, current stage, next actor, source links, last update |
| Submissions | Submission ID, case/revision, source version and intake provenance |
| Assessments | Criterion, actual evidence, finding, gap, assessor/run reference |
| Decisions | Case/revision/gate, assigned actor, decision, reason, timestamp, provenance method |
| Events | Action, before/after values, actor, result, receipt and verification |
| Vocabulary | Allowed stages, decisions, roles, transition rules and field types |
| Assignments | Authoritative person/role-to-case/gate mapping |

Define required fields, keys, units, null meanings, source priority, freshness and revision invalidation. Link dropdowns to governed vocabulary; test populated and blank rows, dependencies and invalid values. Dropdowns do not enforce identity or approval. Preserve formulas, validation, permissions and unrelated records. Before an authorised reset, preserve recoverable evidence; clear only specified case data, retain vocabulary and initialise the new revision explicitly. Never carry old approvals forward silently.

For case databases, use [case operations contract](case-operations-contract.md): separate reusable procedure, one deployment profile and case facts. Define a bounded logical-table catalogue, complete versioned source route, one recorder and a write ledger where the integration lacks equivalent transaction receipts. Derive Case Overview from authoritative records; do not create another editable source of case state. These are optional design patterns where appropriate, not mandatory native Agensia tables.

## 3. Verify access before dependent work

Record environment, company/workspace, user role, Pod version/assignment, connector instance, exact resource scope and permitted actions. Verify actual scoped reads and an authorised reversible write/read-back when writes are required. A Connected label or another assistant's connector access is insufficient. Stop the dependent request if required integration, access or approval verification is missing; record who must resolve it. Never replace a required real integration with a mock without an explicitly revised simulation scope.

## 4. Construct and persist consistently

Map outcome → ontology pack → Talent → role boundary → output → acceptance test. Treat one-to-one mapping as the P2A design convention, not a proven platform restriction. Put domain rules in ontology, operations in Talents and concise identity/authority summaries in the eight role sections. Retire superseded sources non-destructively where supported. Do not assume Delete detaches an association; inspect its consequence and preserve history. Where history remains attached, specify and verify active-source precedence before dependent runtime use.

After generation and after every save, reopen and compare all outcomes, source associations, Talent count/names/operations and coordinator/sub-role messages. Check identity and content of the selected editor before saving. Record expected versus actual values. A failed read-back blocks submission; do not submit and hope to repair afterward. Check for duplicate or missing Talents on new-version saves rather than trusting a summary count. If correction is available, save/reopen the corrected draft and verify again. Submitted/read-only states require a supported return-to-edit or subsequent editable version; never overwrite an approved version invisibly.

Configuration scoring, publication, workspace assignment and runtime success are separate. Establish the actual review process without assuming automatic approval or a fixed completion time. Observe actual status and Pod selectability. Do not repeatedly demand manual approval where an automatic process applies, or call submission activation.

Read the exact version's history row. A family-level Published badge may describe an older version while the new version is Draft or Submitted. Generation can propose duplicate Talents or a different hierarchy; verify the selected option and all messages after saving. Preserve failed attempts and distinguish the supported draft correction from an unverified backend fix.

## 5. Human decisions within chat


Default identity model: CONNECTOR_OWNER. Obtain the authenticated account email from the connector profile/tool, and use it as the acting identity. Require that email to match the live assigned reviewer/approver and verify resource/write access. A separate Agensia session email is not required. Typed email or display name is not identity evidence. Shared connections attribute actions to the connector owner; do not claim independent chat-person verification. Record this limitation and the identity model in the harness and receipt. Preserve explicit human decisions, gate order, case/revision checks, scoped writes and read-back. A client policy may require a stricter identity model; document it explicitly.

Offer this pattern only when owner-approved authority and supported identity/receipt controls exist. The human decides; the agent records the explicit decision through the approved integration. Do not grant blanket execution or disclosure because someone is an approver.

1. Resolve the exact case, revision, gate and proposed action.
2. Read live assignment and earlier gate state. Obtain authenticated connector account identity and authority; user-typed email is not identity evidence.
3. Enforce the approved identity model. Default to CONNECTOR_OWNER: authenticated connector email = assigned actor. Separate Agensia session email is not required. Attribute shared-connection activity to the connector owner and disclose that limitation. A client-required service-account/delegation or stricter session model needs its own explicit policy and tested attribution.
4. Present evidence, gaps, consequences and available decisions. Obtain the human's explicit case-specific decision and reason. Silence, configuration approval and connector consent are not business approval.
5. Re-read revision, assignment and gate state immediately before writing. Stop on conflict, rejection, expiry or changed evidence. Define single/any/all approval semantics and separation-of-duties rules from owner policy, never assume them.
6. Save only authorised decision/status fields and append the receipt. Deduplicate by case/revision/gate/decision request; preserve previous values. A partial failure remains partial; reconcile before retrying.
7. Read back the decision and linked state. Advance only to the authorised next stage; approval recording does not authorise downstream sends, payment, signatures or disclosure.
8. Refresh the dashboard and show the next actor. If trusted identity, durable receipt or required write access is unavailable, hold the action and identify the missing prerequisite.

Receipt: case/revision/gate, assigned and acting human, trusted identity references, connector identity, decision/reason, decision time and timezone, durable chat message/event reference, prior values, write result, read-back time/result, Pod/procedure version and verification method. Never invent IDs or timestamps; label observation time separately. A durable chat link plus exact decision quote and observed time is acceptable only if the owner-approved verification policy accepts it. Agent-written cells under owner OAuth do not by themselves prove a human decision or enforce agent/human separation. Preserve manual-history checks separately; never mark them complete from a chat receipt. Consequential final actions retain existing HL2/human-final-action limits.

Order gates by dependency: evidence acceptance can establish inputs for a calculation; do not make it depend on that calculation. Keep evidence acceptance, scoring-policy agreement, native-result acceptance and final case decision distinct. A changed decision basis makes dependent results stale; preserve earlier receipts and renew only affected decisions. Do not ask for an unchanged valid decision again because context or receipt retrieval failed; resolve the retrieval/policy issue without inventing verification.

## 6. Central workspace and dashboard contract

Converse is the interaction surface; the authorised system of record remains authoritative. Composer rendering is separate from persistence, refresh and action execution.

Provide: My work; case stage and next actor; evidence and gaps; permitted next actions; decision/activity history; integration/run health. For the active case, list every governed stage, highlight current stage and label any stage with unverified human decision history **Unverified**. Display case/revision, source, exact last successful read time and freshness/refresh limitation. If Composer is unavailable, provide a text fallback and record that limitation. Never render a working approval button unless its authorised handler and enforcement have been tested.

Use effective rule values in titles, summaries and calculations. If original rule wording is retained, label original versus current values clearly. A generated summary must not contradict the live parameter or execution result. Do not claim continuous monitoring from a snapshot or a prompt instruction to refresh. Test interim/error responses separately when every-response tracking is required.

For a case view, include requirement coverage, next actor/action, owner-set due date, actual verified update and write health. Join by case/revision; expose duplicate or unknown keys, preserve blanks and link to source records. Use friendly stage labels mapped to stored keys. Prefer an explicit flowchart with neutral future states when generic widgets add misleading ticks. Read-back proves data; rendered pixels, working links and action handlers need their own checks.

## 7. Allocate work to platform components

| Component | Good candidate | Boundary and verification |
|---|---|---|
| Collection | Reusable case evidence or reviewed outputs | Explicitly save/move; reopen item; test recall separately from memory preview |
| Blueprint | Discussing stages and responsibilities | Plan only; inspect roles and dependencies; do not claim executable workflow creation |
| Workflow | Required for repeatable outputs and decision-bearing operations in this operating model | One output per Workflow; short single-purpose tasks; inspect saved kinds, bindings, categories, native gates and resulting records |
| Scheduler | Read-only daily queue digest, stale-case report, evidence expiry check | Exact timezone, frequency, destination, scope and owner; first test one-time delivery; no inferred approval or automatic progression |
| Decision Desk | Required calculated comparison or classification under approved rules | Verify model/solve/result and return to the originating Workflow; ordinary human review needs no calculation |

Suggest only components justified by the user's process; mark others not applicable with reason. Provide purpose, trigger, inputs, expected output, authority, failure route and acceptance check for each suggestion. Use the prompt playbook to emit a tailored sequence after design approval; placeholders remain drafts until bound.

## 8. Diagnostics and repeatable acceptance

Maintain a run record with case/revision/chat reference, exposed run ID, Pod/workflow version, requested versus actual action, actor, connector result, before/after state, source/read time, blocker and next owner. Mark unavailable telemetry **Not exposed**. Prefer platform execution events over generated prose. A native permission-controlled diagnostic timeline/export is a product recommendation, not an assumed feature; exclude credentials, unnecessary payloads and unrelated tenant data.

Test: successful intake/write/read-back; missing evidence; wrong actor; identity mismatch; duplicate decision; changed revision; rejection/expiry; conflicting decisions; unavailable connector; partial write; stale dashboard; rule-label/effective-value divergence; multi-record output cardinality; saved configuration drift. Test restricted access with an authorised test identity, not impersonation. Add relevant cases to the existing golden set. Keep design scores, configuration checks, runtime checks and owner acceptance separate. Compare generated/reviewed variants on the same fixture and settings before claiming improvement.

Record findings in the existing Kanban: ID, lane, expectation, observation, environment/version, evidence, confidence, impact, owner and next check. Suggested lanes: Backlog, Investigating, Blocked, Ready for review, Verified within scope. Preserve intervened/failed runs. No baseline or required verified controls means no go-live claim.

## Workflow acceptance

Use the [Workflow execution contract](workflow-execution-contract.md) before expanding configuration. Prove actual content reading separately from Connected/source-association/open-handle states. Compare the same bounded action in native chat and the exact Workflow; a chat read pass does not pass Workflow authorisation. Inspect each saved task's Sources and Pods independently; builder narrative does not establish bindings, type or enforced stopping. Definition publication, run authority and runtime acceptance remain separate. Preserve valid decisions while resolving retrieval failures. Unresolved read gates and Desk returns are blocked, not completed business stages.
