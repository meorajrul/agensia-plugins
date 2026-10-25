# TOGAF crosswalk — make-pod in enterprise-architecture terms

Use this when a client, architect or consultant expects TOGAF-style deliverables, or when you need to check that a Pod design has not skipped the business-architecture work that comes before configuration. It maps the TOGAF Architecture Development Method (ADM) to make-pod gates and Agensia components. It does not make a Pod a TOGAF-certified architecture, and it adds no authority.

## Scale

TOGAF architects an enterprise. make-pod architects **one job role (Pod)** inside one process. Apply each phase at that scale: a Pod charter is one page, not a Statement of Architecture Work for a programme. Several Pods grouped into a Pack or AI Department may justify a fuller, programme-level ADM cycle.

## Phase map

| ADM phase | TOGAF intent | make-pod gate | Agensia artefact | Template |
|---|---|---|---|---|
| Preliminary | Principles, governance, tailoring | Before G0 | Deployment profile, company operating-model principles, non-production rule | `template-pod-charter.md` §Principles |
| A — Architecture Vision | Stakeholders, drivers, goals, scope, value, approval to proceed | G0 | **Pod Charter** | `template-pod-charter.md` |
| B — Business Architecture | Baseline and target business, actors/roles, value stream, capability | G0–G2 | Process card (as-is / to-be), SIPOC + RACI, capability card | `template-process-card.md`, `template-sipoc-raci.md`, `template-capability.md` |
| C — Data Architecture | Data entities, classification, lifecycle | G0, G3, G6 | Data object catalogue, case-operations contract | `template-data-connector-catalogue.md` |
| C — Application Architecture | Applications, interfaces | G0, G3 | Connector catalogue, harness Know/Do | `template-data-connector-catalogue.md`, `template-harness-spec.md` |
| D — Technology Architecture | Platform, environments | G0, G8 | Environment register, deployment handoff | `template-pod-spec.md` §Deployment handoff |
| E — Opportunities & Solutions | Gap analysis, building blocks, reuse | G2, G3 | Gap matrix, Talent / Workflow allocation, AAS scoring, Browse uniqueness | `template-pod-spec.md` §Gap matrix, `assignment-method.md` |
| F — Migration Planning | Transition architectures, roadmap | G3, G7 | **HL roadmap** per Talent | `template-pod-spec.md` §HL roadmap |
| G — Implementation Governance | Architecture contract, compliance review | G8 | **Pod Contract**, configuration verification, platform pre-checks | `template-pod-contract.md`, `configuration-verification.md` |
| H — Architecture Change Mgmt | Change requests, drift, re-entry | After G8 | Retrofit review, evaluation loop, change classification, HL change history | `retrofit-review.md`, `pod-evaluation.md` |
| Requirements Management | Central requirements register traced through all phases | All gates | Requirements register traced to golden-case IDs | `template-pod-spec.md` §Requirements register |

## TOGAF artefacts and their Pod equivalents

| TOGAF artefact | Pod equivalent | Where |
|---|---|---|
| Stakeholder map matrix | Stakeholder table with RACI and provenance | Charter §Stakeholders |
| Driver / goal / objective catalogue | Driver → goal → Outcome → primary metric chain | Charter §Drivers |
| Architecture principles | Pod principles (non-production, HL caps, fail-closed) | Charter §Principles |
| Statement of Architecture Work | Charter sign-off | Charter §Approval |
| Business scenario | Last real case walkthrough | Process card §As-is |
| Organisation / actor catalogue, role catalogue | RACI matrix + role binding (roles in sources, holders in one file) | SIPOC + RACI, `template-role-binding.md` |
| Value stream / capability map | Capability card | `template-capability.md` |
| Process flow, event diagram | Activity table, gateways, BPMN | Process card |
| Data entity catalogue | Data object catalogue | Data & connector catalogue |
| Interface catalogue, application portfolio | Connector catalogue | Data & connector catalogue |
| Gap analysis matrix | Gap matrix (as-is → to-be → Pod component) | Pod spec |
| Transition architecture, roadmap | HL roadmap (HL0 → HL1 → HL2, evidence gates) | Pod spec |
| Architecture contract | Pod Contract | `template-pod-contract.md` |
| Compliance assessment | Platform pre-checks, 14-point ontology gate, configuration read-back | Pod spec, ontology pack |
| Requirements catalogue | Requirements register | Pod spec |
| Change request | Change classification + gate reopening | `pod-evaluation.md` |

## What make-pod adds that TOGAF does not

TOGAF governs architecture artefacts. It does not specify agent authority. Keep these make-pod controls whenever a TOGAF deliverable is requested:

- Harness levels and the HL ≤2 rule for irreversible or consequential actions.
- Control verification status: `specified`, `verified` or `blocked`. A document is not a control.
- Golden sets, signed owner goals and paired non-inferiority gates.
- Separation of design approval, runtime approval and production release.

## Minimum set by engagement type

| Engagement | Minimum TOGAF-derived additions |
|---|---|
| Internal Bronze Pod, owner is the builder | Charter (short), RACI |
| Builder is not the process owner | Charter, SIPOC + RACI, elicitation cards, playback in the Pod Contract |
| External client or Silver tier | All of the above + data & connector catalogue + gap matrix + requirements register |
| Gold tier, regulated or multi-Pod Pack | All of the above + HL roadmap with dated evidence gates and a programme-level ADM cycle |
