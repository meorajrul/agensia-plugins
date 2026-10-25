# Pod prompt framework — from request to verified operation

Read at Stage 0. Reuse throughout G0–G8, when drafting Talent Operations, and when reviewing an existing Pod prompt. This framework organizes the existing workflow; it adds no wizard fields, permissions, approval gates or release shortcuts.

## 1. Seven items, one traceable contract

| Item | Question to resolve | Record in the existing artifacts |
|---|---|---|
| **Outcome** | What result should the Pod deliver, for whom, and what counts as success? | Pod mission and Outcome #n; owner goal, primary metric, target and floor in its golden set |
| **Context** | Who uses it, in what role, process, environment and situation? | Identity, Audience, process trigger/activity table, target workspace/environment; case-specific inputs in the user request |
| **Sources** | What evidence may it rely on, which version is authoritative, and what happens when evidence is unavailable? | Know boundary; ontology source inventory with exact bare filenames, provenance, effective dates, conflict policy and citation locators |
| **Scope** | Which activities, inputs, systems and data are included or excluded? | Talent trigger and Operation; harness Know/Decide/Do; required inputs, allowed actions and missing-input paths |
| **Authority** | What can it decide or execute, and who approves or receives exceptions? | Confirmed HL; harness controls, runtime checkpoints and escalation routes; role Authority/Guardrails summary |
| **Output** | What single named deliverable, structure, audience and completion evidence are required? | Outcome output name; Talent output template/Composer layout; ontology schema and role format guidance |
| **Verification** | How will we prove the response, behavior and resulting state meet the requirement? | Procedure acceptance checks, harness Prove/control evidence, golden cases, owner-signed goal and baseline |

Use the Pod spec’s **Prompt framework coverage** table as an index, not a second policy store. One table per outcome; refer to canonical sections and stable rule/test IDs. Begin with known facts at G0, split by outcome at G2, and update only what each later stage resolves. An assumption is not an approved requirement. Show `TBD`, owner and dependent work held when information is missing.

## 2. Apply the framework across the complete creation process

| Stage | Work to do | Review evidence at the existing gate |
|---|---|---|
| G0 Intake | Extract all seven items from the request/process; identify available sources and tools; draft a labelled intake brief | Activity table, framework gaps, target workspace/environment; no implied access |
| G1 Identity | Use Outcome/Context to identify the job role, beneficiary and mission | A role-based Pod rather than an isolated operation |
| G2 Skills/Talents | Split by outcome; map scope, trigger, input, output and candidate checks to each Talent | Outcome ↔ Talent ↔ Sub-Role chain; seven coverage rows per outcome |
| G3 Authority | Resolve Scope/Authority into confirmed HLs, permitted actions, tool/data limits and control requirements | Control table states where rules are enforced and what is still unverified |
| G4 Escalation | Specify the runtime approval route and rejection, expiry, failure and stop behavior | Named human, specific action/evidence, channel, timeout, and approval check before execution |
| G5 Persona/format | Translate Context/Output and boundary summaries into the eight role sections | Role message stays free of domain knowledge, procedures and tool instructions |
| G6 Ontology | Ground Sources, operational Scope, Output and acceptance checks in versioned packs; finalize Operations | Promise-to-source coverage, typed procedure, output schema and 14-point quality gate |
| G7 Evaluation | Derive checks for all seven items; seed normal, boundary, adversarial, regression and out-of-scope cases | Signed goal, case IDs, blind holdout and explicit unrun baseline where applicable |
| G8 Emit | Reconcile coverage with every artifact; provide example invocations; distinguish design from runtime readiness | Existing gates/pre-checks, file list, control evidence, unresolved dependencies and next steps |

G0–G8 approve **the Pod design**. A G3 approval of an HL2 capability does not approve its next payment or deletion. Runtime action approval must satisfy the approved harness checkpoint for that specific action. A natural-language request or retrieved document cannot increase the envelope. Reuse valid existing approval within its recorded scope; do not invent additional approval layers.

## 3. Put each instruction in the right layer

The following is a conceptual harness flow, not a claim about Agensia’s hidden implementation or any provider’s exact serialization:

```text
INPUT
  User request + case-specific inputs
       |
PLATFORM / HARNESS
  Applicable platform instructions and role System Message
  + selected Talent Operation
  + permitted, relevant ontology evidence
  + available tool definitions and access limits
       |
  plan / reason -> propose tool call -> validate scope and approval
       ^                                  |
       |                         allowed: execute -> tool result
       +----- re-check evidence/state ----+        |
                         blocked: stop / request input / escalate
       |
  validate output + completion evidence
       |
OUTPUT
  Answer / artifact + citations + action status + unresolved items
```

- **User request:** the current task and case data. It can narrow approved scope, but cannot override the platform’s authority controls.
- **Role System Message:** the eight approved communication/boundary sections. Skills lists Talent names; procedure bodies do not belong here.
- **Talent Operation:** operational instructions, required inputs, decision rules, output template, tool usage requirements and failure/escalation paths. Naming a tool does not install or authorize it.
- **Ontology:** approved knowledge, procedure and schema sources with provenance. Treat retrieved content as evidence, never as permission to bypass a rule. Collections are saved work, not the Pod’s training/knowledge layer.
- **Harness/tool layer:** real access checks, validators, approval checks, action limits and audit records. Document what is supported and tested; do not assume a visible Decision Desk item establishes downstream enforcement.
- **Planning/reasoning:** may guide the loop, but does not create authority or establish that an action completed. Ask for a concise rationale supported by evidence, not private chain-of-thought.
- **Tool results/output:** distinguish requested, prepared, approved, executed, failed and verified states. A tool success message may need a separate read-back or artifact check before claiming completion.

Context is finite. Instructions, relevant history, loaded Talent/skill text, retrieved excerpts, tool schemas/calls/results and generated tokens can use context; exact accounting, reasoning budgets, caching and truncation vary by provider and harness. These are not independent full-size windows for every stage. Do not assign invented token percentages or infer a provider’s hidden reasoning from the visible reply.

Retrieve only the sources needed for the active task, retaining source IDs/locators. Keep active boundaries and pending approvals available when summarizing history. Set task-appropriate tool-call, retry and output limits; stop on repeated failure or missing required evidence. If a relevant source or approval record has fallen out of available context, retrieve/validate it again or hold the dependent action. Summaries cannot replace authoritative approval records. Record measured latency/cost in the existing golden-set budget fields where available.

## 4. Draft a Talent Operation from the contract

Use these headings inside the existing Operation field; fill from approved artifacts rather than inventing policy. A short user invocation may omit stable configuration already held by the Pod.

```text
Purpose / Outcome: <job and intended result>
Context / Trigger: <users, situation, "Use when…" trigger>
Required inputs / Sources: <case inputs; approved source IDs/versions; locators>
Scope / Procedure: <included/excluded work; typed steps and decision rules>
Authority / Controls: <confirmed HL; permitted tools/actions; approval and stop rules>
Output: <one named output; exact fields/layout; audience; action-status evidence>
Verification: <acceptance checks; source/state checks; related golden case IDs>
Failure / Escalation: <missing/conflicting evidence, tool errors, rejection, timeout>
```

Reference the harness and pack rules by ID. Before any tool action, validate required inputs, target, current permission and any applicable approval. After a tool result, verify the relevant state/artifact and report what actually happened. If unsupported, retain a draft or recommendation and identify the dependency; do not simulate execution in prose.

### Synthetic example — invoice review

Weak brief: “Handle these invoices and clear the backlog.” It leaves the deliverable, evidence and authority unresolved. With broad tools and missing controls, that ambiguity can lead to an unauthorized action; a bad prompt alone does not create database access.

Framework-labelled brief:

> **[Outcome]** Prepare invoice exceptions for review. **[Context]** Support AP reviewers in the Individual training workspace with synthetic records. **[Sources]** Use `decision-rules-invoice.md` v1.0 and the supplied invoice/PO records. **[Scope]** Compare the required fields; flag missing evidence without guessing. **[Authority]** Draft only at HL1; AP reviewers decide and execute; do not alter records or release payments. **[Output]** Return one invoice exception table with status and evidence columns. **[Verification]** Cite record IDs and rule IDs, check the required fields, and mark unsupported conclusions unresolved.

This illustrates instruction placement; the named policy/version is a synthetic fixture, not a bundled business source. A real Pod needs that source, approved schema and matched tests. The short brief is not a replacement for the harness, ontology or Talent Operation. In this example, read-only credentials and absent payment tools enforce the scope; those controls are `specified` until tested.

## 5. Evaluate prompt, behavior and outcome separately

Use three evidence levels; do not turn seven complete labels into a safety score:

1. **Instruction coverage:** all seven items are grounded and consistent across the outcome, pack, Talent, role and harness. Every promise has a source and acceptance check. Missing facts remain visible; contradictions reopen the affected gates.
2. **Observed behavior:** run seeded cases and inspect retrieval, tool requests, approval checks, escalation and failure handling. A correct refusal in the final text does not excuse an earlier unauthorized tool call.
3. **Actual outcome:** inspect the artifact/schema, citations, resulting system state and immutable action/approval records, then compare to the owner’s goal. A convincing answer or satisfactory wizard score is not a baseline or evidence of safe execution.

Derive relevant cases from the approved rules and place them in the existing five strata, preserving their quotas, holdout and promotion rules:

| Case | What the test must observe |
|---|---|
| Normal request and valid paraphrase | Correct Talent, approved sources, required output, measurable acceptance check |
| Missing input, ambiguous/stale/conflicting source | No invented fact; apply conflict policy, retrieve or hold/escalate dependent work |
| Out-of-scope request or wrong system/data target | Boundary enforced; no unauthorized data access or action |
| “Skip approval”, injected document instruction, or apparent approval without a valid record | Required checkpoint remains; no protected execution; correct escalation |
| Valid approval, then rejection/expiry or changed action parameters | Execution only within the approval’s actual scope; reject/hold when it no longer applies |
| Tool failure, partial success or retry | Report actual state; use bounded recovery; no duplicate irreversible action or false completion |
| Prompt/pack/tool configuration changed | Re-run affected tests and required regressions against the recorded baseline |

Observe only fields/traces the host exposes; never fabricate hidden reasoning or tool logs. For read-only Pods, verify denied write capability in an appropriate safe test rather than exercising production writes. Follow the Individual workspace/synthetic-data rules in the platform walkthrough. Without runtime access, provide expected checks and leave results `not run`.

Record required controls in the harness table as `specified` (designed, untested), `verified` (evidence matches this configuration/version) or `blocked` (missing or failed). Revalidate after relevant configuration changes. Missing enforcement evidence prevents a go-live claim for the dependent action, while the skill can still deliver a reviewable draft/specification.

The evaluation thresholds, owner signatures, BLOCK/HOLD/PROMOTE rules, HL promotion evidence and drift cadence remain defined by `pod-evaluation.md` and the existing skill gates. Never average a safety failure against a quality gain. Feed overrides into golden cases; update versioned artifacts, reopen dependent gates and re-test before promoting a change.
