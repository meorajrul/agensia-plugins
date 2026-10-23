# Converse copy-and-paste prompt playbook

**Production prohibition:** never create or push changes to Agensia production, including uploads, submissions, publication, edits, deletions, runs, schedules or connected production writes. Verify the platform and downstream resources are non-production before operations; unknown targets block operations. No approval or delegated tool/agent can waive this rule.

Use with [the operating process](converse-operating-process.md). These are reusable templates, not evidence that a run occurred. Replace every bracketed value using the approved Pod design. Do not paste unresolved placeholders into an execution request. G0–G8 still apply; the builder prepares local drafts; authorised platform operations require verified non-production targets. No prompt grants missing access. Run each step, inspect its result, then continue only when its prerequisites are satisfied.

## Bind once

Record: [VERIFIED NON-PRODUCTION ENVIRONMENT], [WORKSPACE], [POD AND VERSION], [CASE ID], [REVISION], [APPROVED RESOURCE IDS], [SYSTEM OF RECORD], [ALLOWED WRITE FIELDS], [SOURCE VERSIONS], [ASSIGNED REVIEWER], [APPROVAL POLICY], [TIMEZONE], [OUTPUT DESTINATION], [WORKFLOW IDS/VERSIONS], [TEMPLATE VERSIONS]. Use exact resource identifiers, not broad Drive search. Never place credentials in prompts.

## 1. Preflight — selected Pod chat

```text
In [VERIFIED NON-PRODUCTION ENVIRONMENT] / [WORKSPACE], verify that [POD AND VERSION] is selected and available. Read only [APPROVED RESOURCE IDS] through the required integration. Confirm exact source versions, record schema, allowed status values, current case [CASE ID] revision [REVISION], assignments and connector capabilities. Distinguish observed identity/access from labels or assumptions. Do not write or approve. Report pass, blocked or not exposed for each prerequisite, with evidence and the next owner/action. Stop dependent work if required integration or approval verification is unavailable.
```

Proceed when the necessary reads and access are verified. A read-only preflight does not verify writes.

## 2. Route intake and assessment — selected Pod chat

```text
Process [CASE ID], revision [REVISION], from [SOURCE VERSIONS] using [POD AND VERSION]. Read current records and governed vocabulary in [SYSTEM OF RECORD]. Access only [APPROVED RESOURCE IDS]. Invoke verified saved [INTAKE WORKFLOW ID/VERSION], then [ASSESSMENT WORKFLOW ID/VERSION], for their named outputs. Verify current reads, native gates and receipts before dependent progression. If a required Workflow/capability is unavailable, report the blocker; do not silently perform its writes directly in chat. Distinguish source claims, independent evidence and missing mandatory information. I authorise this case's operational writes only to [ALLOWED WRITE FIELDS]; preserve all other data, formulas, validations, assignments and permissions. Deduplicate by case/submission/revision, preserve before-values, append actual events and read back each write. Stop at the review gate assigned to [ASSIGNED REVIEWER]. This message grants no review or approval decision. Show the active case tracker in Composer with every governed stage, current stage, next actor, Unverified decision history, source and last successful read time; use an explicitly labelled text fallback if unavailable.
```

Expected: persisted operational records or a precise partial/blocked result; no invented business decision.

### Minimal-input acceptance after configuration

Once the deployment profile, source route, authority and actual Converse write/read-back are verified, attach the current submissions and use:

```text
Assess these submissions.
```

Expected: the selected Pod resolves its approved profile and sources, routes verified saved Workflows, reuses or allocates case identities correctly, and stops at the human gate. Operational changes occur only in authorised action tasks with receipts. Internal locators and stable rules belong in configuration. A guided diagnostic recovery does not pass this minimal-prompt check. See [case operations contract](case-operations-contract.md).

If a write times out, reconcile before resuming:

```text
Reconcile the last attempted operation for this case. Read its existing receipt and actual target values before retrying. Preserve any partial changes, formulas and validation. Reuse the same intent key; return a verified existing receipt or the precise discrepancy and next owner. Do not append a duplicate or invent a human decision.
```

## 3. Dashboard — selected Pod chat

```text
Read [APPROVED RESOURCE IDS] and build a Composer work dashboard for [WORKSPACE]. Show my assigned work, case stage, next actor, evidence gaps, latest decision provenance and integration/run failures. Include the active case's complete governed stage tracker, current-stage emphasis and Unverified labels where needed. Show source and exact last successful read time. Describe whether this is a snapshot and how to refresh it. Show actions only where identity, assignment and the action handler are verified; otherwise show the next action as text. Do not write decisions or claim real-time refresh or working controls without evidence.
```

Expected: rendered dashboard checked against the same source records. Refresh after a real state change to test freshness.

## 4. Optional Collection and Blueprint — chat plus visible save controls

```text
Prepare a concise reusable case brief for [CASE ID]/[REVISION]: source links, findings, unresolved evidence, current stage and next actor. Exclude unnecessary personal data. Propose a Blueprint showing steps, responsible roles, inputs, outputs and human gates for [PROCESS]. Treat it as a plan, not an executed workflow. Do not claim it was saved or added to a Collection without verifying the actual saved item.
```

Use the response's available Pin/Move to collection controls, explicitly select the destination and reopen the saved item. Creating a Collection alone may leave it empty. Test retrieval of a known non-sensitive fact in a Collection-scoped chat; memory preview alone is insufficient.

## 5. Reusable output Workflow — dedicated Workflows builder

Use [Workflow execution contract](workflow-execution-contract.md). Map the process/human responsibilities first. Create one reusable Workflow per repeatable output or decision-bearing operation.

```text
Draft [WORKFLOW NAME] for the single output [NAMED OUTPUT] in [WORKSPACE], triggered manually with [CASE ID]/[REVISION]/[SOURCE VERSIONS]. Bind [POD AND VERSION] and independently bind [PROCEDURE AND TEMPLATE VERSIONS] to relevant tasks. Use short linear single-purpose native tasks: read/extract, human_request, classification, document_template_output, and one erp_action/integration_action per authorised write followed by read-back. Read before every human question. Each task states purpose, exact inputs, output/cardinality, source and exact human reply when relevant. Set concrete classification values. Put shared constraints once in the procedure/description; no if/then scripts inside tasks. Show required native preconditions/gates and recovery owner. Save Draft; report unsupported kinds or controls.
```

Reopen each task; compare count/order, body, actual kind where exposed, selected Pod, Sources, labels and decision flags. Builder chat is not saved configuration. Independently verify source text and bounded live reads before dependent execution.

Publication and execution are separate approvals. A failed run does not by itself invalidate a verified definition. Use only the authority granted for each action:

```text
Publish [VERIFIED WORKFLOW ID/VERSION] with [AUTHORISED VISIBILITY] in [WORKSPACE]. Verify exact version row and retained access. Do not run, send or schedule. Report actual publication or the supported next UI action.
```

```text
Run published [WORKFLOW ID/VERSION] once for [AUTHORISED CASE/REVISION] within [ALLOWED WRITE FIELDS]. Verify executable workspace attachment, task bindings and content/live-read capabilities. Stop at the assigned human gate or failed prerequisite; do not infer a business pass from green ticks. Report actual run/step references, result, connector receipts and independent read-back. Preserve valid prior decisions and do not repeat notifications.
```

For a failed read, compare the same approved resource/action in native chat and Workflow. Record identity, version/task, actual content or handle, consent state and error. Do not widen access, add dummy writes or substitute external-assistant reads. Keep failed/intervened runs distinct from clean reruns.

## 6. Suggested schedule — start with a one-time read-only digest

Candidates: assigned-work digest, stale-case report, evidence-expiry report. Choose one; define thresholds from owner policy.

```text
Create one one-time test schedule for [LOCAL DATE AND TIME] in [TIMEZONE], delivering to [SUPPORTED OUTPUT DESTINATION]. At that time, read only [APPROVED RESOURCE IDS] and report cases needing action under [APPROVED THRESHOLD RULES], their assigned actors, evidence gaps and source read time. No approval, case progression, external messages or other writes. Confirm the saved schedule's time, timezone, scope and destination. If scheduling is unavailable, state it; do not claim a reminder was created.
```

At the scheduled time inspect actual prompt arrival and output. A model saying it ran is insufficient. Check whether the one-time entry remains or disappears; keep available execution evidence.

Only after delivery is verified and recurring execution is authorised:

```text
Configure the verified digest for [EXACT FREQUENCY AND LOCAL TIME] in [TIMEZONE], ending [END CONDITION], owned by [OWNER], delivered to [SUPPORTED OUTPUT DESTINATION]. Reuse the approved read-only scope. Apply [NOTIFICATION POLICY] only if supported; explain limitations. Check existing schedules to avoid duplicates. Confirm the saved configuration, next occurrence and how to pause or remove it. Never treat a timer as approval or automatic case progression.
```

## 7. Decision Desk — calculated gate and originating Workflow

```text
From [ORIGINATING WORKFLOW RUN/TASK], prepare the required native Decision Desk calculation for [CASE ID]/[REVISION], evidence snapshot [SNAPSHOT] and policy [POLICY VERSION], concerning [EXACT DECISION]. Options: [OPTIONS WITH SOURCE-CITED FACTS]. Hard constraints: [RULES AND EFFECTIVE VALUES]. Comparison criteria: [APPROVED CRITERIA OR NONE]. Decision type: [CLASSIFY EACH / COMPARE OPTIONS, AS SUPPORTED]. Assigned approver: [PERSON/ROLE]. Ask for essential missing facts; do not invent weights, thresholds or a winner. Separate unknown evidence from a failed rule. Show original versus current rule values if they differ. Create/solve the model only; do not accept options, record human approval or execute downstream actions. Report actual model/solve/result references and return bound to the originating run/task and evidence revision, or the missing capability. A standalone solve does not prove the round trip.
```

Use a supported decision entry route in the verified non-production environment; do not assume a Collection is a prerequisite. Inspect model, parameter values and computed outputs. Multiple feasible options with no ranking criteria may correctly remain undetermined. In an authorised test, vary one threshold, verify recalculation and displayed wording, then restore it. Per-option acceptance, final acceptance and external action remain separate milestones.

If framing repeats despite prose confirmation, inspect the available structured decision-kind choices and their Submit action. Use only the decision-kind controls actually available for the required calculation. Verify the persisted model and actual result against the current case/evidence revision; this is not a universal UI recipe or backend fix. A hold-only diagnostic model does not satisfy a required weighted comparison. Do not replace a required native gate with chat arithmetic or click Accept merely to clear a blocker.

## 8. Human review or approval in chat — assigned human only

Use only after the approved identity/receipt mechanism is verified. The human completes and sends this message after examining the evidence; an agent must not generate and submit it as the person's decision.

```text
For case [CASE ID], revision [REVISION], gate [GATE], my decision is [EXACT ALLOWED DECISION]. Reason: [MY REASON AND CONDITIONS]. Before recording it, verify my authenticated connector account as acting identity (CONNECTOR_OWNER), connector authority, live assignment and prerequisite gates under [APPROVAL POLICY]. Record only this decision through [DECISION RECORDING WORKFLOW ID/VERSION] and its authorised linked status, with a durable receipt and before-values; read back and refresh the tracker. Preserve valid unchanged receipts; reconcile retrieval failures without asking for that decision again. Stop if identity, assignment, revision, access or receipt verification fails. This decision does not authorise any additional disclosure, payment, signature or downstream execution.
```

Use separate decisions for review and final approval unless the approved policy explicitly permits combining them. Preserve any/all approver rules and rejection precedence. A human decision in chat is not a substitute for missing connector or enforcement access.

## 9. Reconcile and improve — selected Pod chat

```text
Reconcile [CASE ID]/[REVISION] across the source records, chat, workflow, schedule and Decision Desk items that actually exist. Report observed state, versions, actor, source/read time, requested versus executed actions, decision receipts, partial failures and next owner. Mark unavailable telemetry Not exposed. Do not manufacture cross-object links. Add findings to [PROJECT EVIDENCE LOG] with expectation, actual result, evidence, confidence and next test. Propose changes to the existing Pod/harness and golden set; do not change authority or claim improvement without the required review and regression evidence.
```
