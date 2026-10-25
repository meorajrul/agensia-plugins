# Agensia platform guide

Use this guide to map a business process to Pod configuration. It describes component responsibilities and design checks, not guaranteed UI controls or an installed capability. Confirm supported fields and permissions in the user's authorised **non-production** environment. Never infer an environment from its name, appearance or available credentials. No environment URLs are supplied by this skill.

## Production boundary

**Never create or push changes to Agensia production.** Do not create, edit, upload, submit, publish, deploy, delete, run or schedule production assets, or write through production-connected integrations. The same prohibition applies through UI, APIs, scripts, connectors and delegated agents. A design approval, account role or publication request cannot waive this skill's boundary. If the target or downstream resource is production or unverified, stop the dependent operation and provide a local draft or non-production test plan.

## Component responsibilities

| Component | Job | Boundary |
|---|---|---|
| Pod | Represent an accountable job role with a mission and capabilities | A single operation is usually a Talent, not a new Pod |
| Pack | Combine complementary Pods | Composition does not prove routing or shared permissions |
| Outcome | Define the result, audience and one named output | Every promise needs a source and an acceptance check |
| Ontology / knowledge source | Supply reusable knowledge, rules, procedures and templates | Source association is not proof of content retrieval |
| Talent | Define a capability, trigger and operation | Naming a tool does not install it or grant access |
| Role hierarchy | Define role/sub-role responsibilities and communication boundaries | Prompt wording is not permission enforcement |
| Converse | Provide the user interaction surface | Generated narrative is not an execution receipt |
| User Collection | Organise saved work and contextual material | Saving work does not modify the Pod's reusable ontology |
| Blueprint | Plan stages, responsibilities and dependencies | A plan is not a saved or executed Workflow |
| Workflow | Execute a governed task sequence for a named output | Saved definition, version, run and business acceptance are separate |
| Schedule | Trigger authorised work at a specified time | A timer cannot supply human approval |
| Decision Desk | Model a calculated choice under agreed rules | Solving, human acceptance and resulting action need separate evidence |
| Composer | Present outputs and current work | Rendering does not prove persistence, freshness or a working action |
| Connector | Access explicitly permitted resources and operations | A connected account is not evidence of every read/write capability |

Distinguish reusable knowledge stores from user-saved Collections wherever the interface uses similar terms. Inspect the selected object's purpose and access scope rather than assuming that its label determines behavior.

## Four-part Pod configuration

### 1. Overview

Prepare a Pod name and clear outcomes. Each outcome states who it serves, the task or decision, exclusions and one named deliverable. Keep outcomes distinct and grounded in the process.

Where evaluation is available, inspect the actual criteria, scores and improvement feedback. Use completeness, uniqueness and usability as design checks; do not predict a fixed numeric score or assume scoring enforces safety. An output schema, chart, audience or standard promised in an outcome needs a source that defines it.

### 2. Ontology

Group sources by the outcome they support. Explain what each group helps determine. Use exact, unique bare filenames and provenance: owner, version, effective dates, authority rank and conflict policy. Keep diagrams for human review outside the upload set.

Verify the available source-entry types in the target environment. A listed file, link, knowledge base or connected record must still pass a content-read and citation check. After adding or removing a source, inspect dependent outcomes, Talents, role messages and evaluations; do not assume automatic recomputation or reset.

### 3. Talent

Each Talent has a capability name, a Description beginning **Use when…**, and an Operation. Specify required inputs, source/procedure versions, bounded steps, exact output, exclusions, escalation and completion evidence. Use [the Talent framework](talent-operation-framework.md) for specialist and coordinator responsibilities.

Inspect generated instructions before use. Compare count, names and full Operations after saving. Request a Composer output only when its layout is defined and its renderer is available; do not assume an implementation-specific tool name.

### 4. Role hierarchy

Use a job role and appropriate sub-roles. Draft eight sections: Identity, Audience, Voice and Tone, Response Format and Depth, Authority and Boundaries, Escalation, Guardrails, and Skills. Keep domain content and procedures in ontology/Talent Operations.

The P2A outcome–Talent–sub-role mapping is a design convention, not a claimed platform restriction. Verify the selected hierarchy and each saved message. Preserve traceability if the approved design uses a different mapping.

## Save, review and availability

Record exact version and separate evidence for draft persistence, submission, review, publication, assignment and invocation. A family-level status can differ from the selected version. Do not infer availability from submission or acceptance from a score. Required actor roles and review transitions must be established for the selected environment.

All platform operations described here are limited to verified non-production targets and separately authorised actions. This skill produces local designs by default. Help or support controls require their own check of booking, notification and handover; a visible button proves none of those completed.

## Runtime checks

1. Verify the selected non-production workspace, Pod/version, user role and permitted resources.
2. Test source text and citations independently of saved source bindings.
3. Check selected Talents, task inputs and required tool capabilities.
4. Save and reopen outputs; separately test fresh-context recall and next-task file reading.
5. Verify actual run/step identifiers, output and resulting state.
6. Test approval, rejection, request changes, timeout and restricted-actor paths.
7. For calculated decisions, verify native result and return to the originating run.

Use [capabilities and acceptance](platform-knowledge-and-uat.md), [onboarding verification](platform-evidence-and-onboarding.md) and [Workflow execution](workflow-execution-contract.md) for the detailed checks. Leave unsupported or untested capabilities explicit.
