# Elicitation cards — building a Pod when you are not the process owner

Use this reference whenever the Pod builder is a consultant, architect or analyst rather than the accountable process owner. That is the normal case. The templates say *what* to fill in. These cards say **what to ask, who must answer, what evidence confirms the answer, and what safe default applies until it is confirmed**.

A card does not grant authority. Answers from the wrong role stay `Inferred` or `Assumed` until the accountable role confirms them.

## 1. Provenance tags — every captured fact carries one

| Tag | Meaning | May it pass a gate? |
|---|---|---|
| `OWN` | Stated or confirmed by the accountable process owner (A in RACI) | Yes |
| `DOC` | Taken from a named, versioned, approved document | Yes, if the document is current and owned |
| `SME` | Stated by a Responsible or Consulted subject-matter expert | Yes for facts; no for authority, targets or HLs |
| `OBS` | Observed by the builder (system read, shadowing, sample record) | Yes for as-is facts; record date and sample |
| `INF` | Inferred by the builder or an agent from other facts | No. Playback to the owner first |
| `ASM` | Assumed so work can continue | No. Must appear in Open items with an owner |

Write the tag in brackets after the value, for example `Weekly volume: 40 [OBS <YYYY-MM-DD>, 4-week sample]`. A gate may not pass while a **must-confirm** field is `INF` or `ASM`.

## 2. Who answers what (default RACI for elicitation)

| Role | Typical answers | Never the source of |
|---|---|---|
| Sponsor | Drivers, business goal, budget, priority, success measure | Procedure detail |
| Process owner (A) | Outcomes, scope, decision rules, HLs, approvers, targets and floors, golden goal signature | — |
| Performer / SME (R) | Steps, exceptions, volumes, inputs, tools, real examples | Authority, HL, approval rights |
| Approver / reviewer | What they need to see, timebox, rejection reasons | Scope |
| Data or system owner | Data objects, classification, connector scope, identity model | Business rules |
| Risk / compliance | Binding instruments, prohibitions, retention, regulated limits | Throughput targets |
| Downstream customer | Output format, audience, acceptance criteria | Upstream procedure |
| Builder (you) | Proposals, drafts, inferences, test design | Any `OWN` field |

## 3. Cards by Agensia component

Each card lists the fields that must be confirmed, the question that usually gets the answer, the role that answers, the evidence accepted and the default used until confirmation. *Must-confirm* fields block their gate while `INF` or `ASM`.

### 3.1 Pod Charter (G0) — why this Pod exists

| Field | Ask | Who | Evidence | Default until confirmed |
|---|---|---|---|---|
| Business driver *(must)* | "What problem costs you most today if nothing changes?" | Sponsor | Strategy note, KPI report, incident | Charter stays `draft`; no G0 |
| Goal and KPI baseline *(must)* | "How do you measure this today, and what is the current number?" | Sponsor + owner | Report extract with date | Baseline `TBD`; no benefit claims |
| Process owner *(must)* | "Who is accountable if the output is wrong?" | Sponsor | Org chart, appointment, RACI | Block G1 |
| In / out of scope | "Which requests should this Pod refuse?" | Owner | Owner statement | Narrowest reading |
| Constraints and principles | "Which rules can never be bent?" | Risk / compliance | Policy, regulation | Treat as HL ≤1 |

### 3.2 Process as-is / to-be and SIPOC (G0)

| Field | Ask | Who | Evidence | Default |
|---|---|---|---|---|
| Trigger and end state *(must)* | "What starts this and how do you know it is finished?" | Owner | SOP or 2 real cases | Ask; do not invent |
| Activities and lanes | "Walk me through the last real case, step by step." | Performer | Walkthrough of a real case | Mark steps `SME` |
| Inputs / suppliers | "What do you need in hand before you start?" | Performer | Sample input | `TBD` |
| Volumes and cycle time | "How many per week, and how long does each take?" | Performer / data owner | System extract | `TBD`; no SLA |
| Exceptions | "What goes wrong most often? What did you do last time?" | Performer | Exception log, tickets | Route to human |
| Pain points (to-be driver) | "Where do you wait, rework or chase?" | Performer | Observation | Record as `SME` |

### 3.3 Outcome (G2 → Platform Step 1)

| Field | Ask | Who | Evidence | Default |
|---|---|---|---|---|
| Beneficiary and job *(must)* | "Who uses the result and for what decision?" | Owner + downstream customer | Owner statement | Block G2 |
| Single named output *(must)* | "Show me a good example of the finished output." | Downstream customer | Real exemplar | Draft a layout, mark `INF` |
| What it does NOT do *(must)* | "What would be dangerous for it to do?" | Owner | Owner statement | Exclude all writes |
| Success measure | "What makes this output acceptable or rejected?" | Approver | Rejection reasons | Seed from rejections |

### 3.4 Ontology group (G6 → Platform Step 2)

| Field | Ask | Who | Evidence | Default |
|---|---|---|---|---|
| Authoritative sources *(must)* | "Which document wins when two disagree?" | Owner + compliance | Source list with versions | Rank unknown → escalate on conflict |
| Version, owner, effective dates *(must)* | "Who updates this and when was it last approved?" | Document owner | Document control record | Not admissible |
| Decision rules | "Give me the rule as IF … THEN …, with thresholds." | Owner | Policy clause | `TBD`; Talent asks human |
| Vocabulary | "Which words mean something specific here?" | SME | Glossary | Lexicon from samples, `INF` |
| Competency questions | "What questions must it always answer correctly?" | Owner + SME | List of real questions | Seed from exceptions |

### 3.5 Talent (G2 / G6 → Platform Step 3)

| Field | Ask | Who | Evidence | Default |
|---|---|---|---|---|
| Trigger phrases | "How would someone ask for this in their own words?" | Performers | Real requests, emails | Builder draft, `INF` |
| Required inputs and missing-input behaviour | "If this input is missing, what do you do?" | Performer | Real case | Ask the user; do not guess |
| Output template | "Which fields must the output always contain?" | Downstream customer | Exemplar | Report layout file |
| Edge cases | "What is the strangest case you handled this year?" | Performer | Case record | Escalate |

### 3.6 Role / Sub-role (G1 / G5 → Platform Step 4)

| Field | Ask | Who | Evidence | Default |
|---|---|---|---|---|
| Job role mirrored *(must)* | "Which job title does this work today?" | Owner | Job description | Block G1 |
| Audiences and tone | "Who reads this and what irritates them?" | Downstream customer | Feedback | Neutral, concise |
| Never-do rules | "What would get someone in trouble here?" | Compliance | Policy | Strictest reading |

### 3.7 Control Envelope and harness level (G3)

| Field | Ask | Who | Evidence | Default |
|---|---|---|---|---|
| HL per Talent *(must)* | "Would you let a new hire do this unsupervised in week one?" | Owner | Owner confirms each HL by name | HL1 |
| Irreversible actions *(must)* | "Which steps cannot be undone?" | Owner + system owner | System behaviour | HL ≤2 |
| Rollback | "If it is wrong, how do you undo it, and how long does it take?" | System owner | Procedure | Treat as irreversible |
| Kill-switch roles *(must)* | "Who can stop this immediately?" | Sponsor | Appointment | Owner only |

### 3.8 Escalation and Decision Desk (G4)

| Field | Ask | Who | Evidence | Default |
|---|---|---|---|---|
| Approver per checkpoint *(must)* | "Who signs this today, and who covers when they are away?" | Owner | Delegation of authority | Block G4 |
| What the approver sees | "What do you check before you approve?" | Approver | Checklist | Full evidence pack |
| Timeout | "How long can this wait before harm?" | Owner | SLA, clock rule | Fail closed: HOLD |
| Calculated choice | "Is there a formula, constraint or optimisation behind this decision?" | Owner | Policy, model | Ordinary human request, not Desk |

### 3.9 Workflow (G6 / G8)

| Field | Ask | Who | Evidence | Default |
|---|---|---|---|---|
| Repeatable outputs *(must)* | "Which outputs do you produce again and again?" | Performer | Output log | One Workflow per named output |
| Human gates | "Where must a person type a decision?" | Owner | RACI | human_request before every write |
| Receipts | "Where is the proof stored after the decision?" | Data owner | System of record | Blocked until a recorder exists |

### 3.10 Data object and connector (G0 / G3)

| Field | Ask | Who | Evidence | Default |
|---|---|---|---|---|
| System of record *(must)* | "Where is the official copy of this record?" | Data owner | System inventory | Read-only |
| Classification | "Does it contain personal, financial or client-confidential data?" | Data owner + compliance | Classification policy | Confidential |
| Connector scope and identity | "Which account connects, and what may it write?" | System owner | Connector settings | Read-only; CONNECTOR_OWNER |
| Retention | "How long must it be kept?" | Records owner | Retention schedule | Keep; no deletion |

### 3.11 Golden set and owner goal (G7)

| Field | Ask | Who | Evidence | Default |
|---|---|---|---|---|
| Goal, primary metric, target, floor *(must)* | "Below which number would you switch this off?" | Owner (signature) | Signed goal | No baseline run |
| Real cases | "Give me 10 past cases, including 3 that went wrong." | Performer | Case records, anonymised | Seed only; mark synthetic |
| Blind holdout | "Who else can write cases we never see?" | Owner | Named reviewer | Holdout open item |

## 4. Playback — closing the loop with the owner

Before G1, G3, G6 and G8, run a **playback** with the process owner using `template-pod-contract.md`:

1. Show only the `INF`, `ASM` and `SME` rows that need their confirmation, grouped by component.
2. Read each back as one plain sentence. Ask "Correct, change or don't know?"
3. Record the answer, the date and the new tag. `Don't know` → Open item with a named owner and due date.
4. Show what changed since the last playback.
5. Ask the gate question word for word.

A playback is not an approval of runtime actions. It confirms facts and design only.

## 5. Name roles, not people

Write approvers, escalation targets and lane owners as **roles** in every ontology source, Talent Operation and Workflow task. Keep one small role-binding source (`role-binding-<pod>.md`, from `assets/template-role-binding.md`) that maps each role to its current holder and a cover role. When people change jobs, update that one file and re-run the playback for the affected rows. A source that names a person as approver goes stale the day that person moves. Record it as an Open item.

## 6. Interview hygiene

- Ask for the **last real case**, not the ideal process.
- Ask the performer for steps and the owner for rules. Do not reverse these.
- One question per field. Write the answer in their words first, then normalise.
- Ask for numbers with a date and sample size.
- When an answer contradicts a document, record both and escalate the conflict. Do not pick one silently.
- Stop elicitation for a field once it is `OWN` or `DOC`.
