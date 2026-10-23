# Talent operation framework

**Production prohibition:** never create or push changes to Agensia production, including uploads, submissions, publication, edits, deletions, runs, schedules or connected production writes. Verify the platform and downstream resources are non-production before operations; unknown targets block operations. No approval or delegated tool/agent can waive this rule.

Use at G2, G5, G6 and whenever editing a deployed Talent. This framework implements the seven-part prompt contract; it does not replace the eight Role System Message sections, owner authority, G0–G8 or evaluation gates.

## One specialist job, one shared coordinator

A Talent has a capability name, a Description beginning **Use when…**, and an Operation. The Description routes requests; the Operation defines execution. Give each specialist one outcome, one bounded procedure and one named output. Do not repeat every other specialist's job in its procedure.

Author shared sections 3, 4, 5 and 7 once in a versioned common protocol. The coordinator Talent owns executing shared decisions, receipts, state transitions and the closing tracker. Specialists reference the same exact protocol/version and hand off; they do not maintain divergent copies or duplicate writes. Sections 1, 2 and 6 are specific to each Talent.

This is a design pattern, not proof that the runtime automatically loads another Talent. Put the shared protocol in the required ontology sources for every participating outcome. Verify retrieval and coordinator routing. If delegation is unsupported, use the approved single recorder with the protocol loaded, or hold; never assume instruction inheritance. Keep a concise boundary and handoff reference in every specialist.

For database-backed work, use [case operations contract](case-operations-contract.md) for the single deployment entrypoint, logical-record routing and prepare/apply/read-back/reconcile protocol. Specialists submit one proposed change set; the recorder alone applies it. Reusable ontology carries procedures/templates, the profile carries resource/actor bindings, and case records/Collections carry applicant facts. Do not copy a client's names, amounts or fixed case IDs into the reusable framework.

## Operation template

Description: Use when <event or user intent>; include natural trigger phrases and relevant missing-input cases.

```text
TALENT: <capability>
VERSION: <version>
PURPOSE: <one specialist job>
OUTPUT: <one named deliverable>

1. SCOPE AND SOURCES — specific
Required: <domain pack, shared protocol, exact versions and bare filenames>.
Context: <approved environment, cases and resource bindings>.
Inputs: <required evidence; missing/conflict handling>.
Checklist: <field | Present / Gap / Missing permission | evidence locator>.
A present assertion is not independently verified evidence.

2. PROCEDURE — specific
<Numbered steps for this Talent only, domain rules, acceptance and failure paths>.
<Hand off other specialist work and shared recording to named coordinator>.

3. HUMAN DECISION PROTOCOL — shared reference
Apply <protocol filename/version, step IDs>, owned by <coordinator>.
<Specialist: pass request and evidence; do not create a second decision write>.

4. AUTHORITY AND BOUNDARIES — shared reference
Apply <protocol boundary IDs>; retain the approved harness level.
The human decides. Recording is allowed only under the approved verification model.
Role membership alone grants no unrelated execution or disclosure.

5. ESCALATION AND HOLDS — shared reference
Apply <protocol failure IDs, accountable role, channel, timeout>.
Missing required integration, identity or receipt holds dependent work.

6. OUTPUT FORMAT — specific
<Exact field order, evidence before finding, named output, source locators>.
<Actual actions versus proposals, gaps, handoff and completion evidence>.

7. CLOSING ELEMENT — shared reference
Apply <protocol tracker IDs>. Coordinator assembles the final response.
All governed stages, current stage, next actor, evidence freshness and Unverified history.
Text fallback if rendering is unavailable; never pretend a snapshot is a live control.
```

Use stable rule IDs in the shared protocol. Store domain knowledge in the outcome pack, with a short operational field checklist in the Talent. Do not substitute a long repeated policy wall for the actual specialist procedure.

## Shared protocol checklist

- Resolve case, revision, gate and action. Read live assignment and prerequisites.
- Default CONNECTOR_OWNER: authenticated connector email equals live assigned actor; no separate Agensia email is required. Record shared-connection attribution limits. Typed email is not authentication.
- Present evidence, gaps, consequences and valid decisions. Obtain an explicit human decision and reason.
- Recheck revision, assignment and previous decisions immediately before recording. Respect any/all/sequential semantics and separation of duties.
- Write only permitted fields. Preserve source links, formulas, validation, protections, assignments and unrelated values. Use value-only updates where supported; verify validation after writes.
- Keep one durable receipt: actor/connector evidence, case/revision/gate, exact quote, reason, chat reference, prior values, actual time and timezone, procedure version and read-back result.
- Use trusted source or observation timestamps, labelled distinctly. Never invent missing times. Correct bad timestamps through an auditable correction retaining the original value; do not reconstruct event time without evidence.
- Read back the decision and event before advancing state. Deduplicate repeat requests and reconcile partial writes before retrying.
- A timeout is uncertain, not proof of no write. Re-read the stable operation key and exact targets; reuse an existing verified receipt. A ledger or single recorder is not an atomic lock.
- Keep manual editor-history verification separate from chat-receipt verification. No claimed verification without its evidence.
- Rejection, changes, stale evidence or missing access holds. Changed evidence invalidates decisions that depend on its changed basis. Approval does not authorise unrelated sends, signatures, payments or publication.

Evidence review may precede calculation. Require renewed decisions only where the changed evidence affects their basis; retain unchanged valid decisions and their receipts. An accepted evidence record is purpose-scoped review, not independent issuer certification. Native calculation and business acceptance remain separate.

## Consistency and release check

Compare outcomes, ontology, every Talent, every role/sub-role, system-of-record instructions and dashboard wording. Check one current protocol version, one decision writer, exact role terminology, no obsolete manual-only prohibition where chat recording is authorised, no broader authority than approved, and no duplicate Talent entries. Save, reopen and compare before submission; compare again after submission/activation.

Run the existing evaluation scope for changed rules. Minimum relevant cases: two-document minimal intake; specialist scope isolation; missing shared protocol; missing identity; wrong assigned actor; explicit review then final approval; premature final approval; rejection; duplicate/partial write; stale revision; preserved dropdowns; missing source link; unavailable clock; tracker on error responses. Record actual results separately from seeded tests. No baseline or enforcement evidence means no production-readiness claim.

A simple user prompt can be: “Please start the process for these two submissions.” Stable resource bindings, procedure, actors and decision rules belong in the approved configuration, not in a long onboarding prompt.
