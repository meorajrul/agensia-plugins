---
artifact: pod-charter
framework: p2a
version: "0.1"
status: draft   # draft → approved (G0) ; reopened when a driver, owner or scope changes
owner: <accountable process owner role>
sponsor: <sponsor role>
builder: <builder role; state if not the process owner>
updated: <YYYY-MM-DD>
pod: pod-<role>-<subrole>.md
process: process-<apqc>-<slug>.md
togaf_phase: "Preliminary + A (Architecture Vision)"
---

> **Non-production only.** This charter approves design work. It grants no platform, connector, publication or runtime authority.

# Pod Charter — <working Pod name>

Tag every value with provenance: `[OWN]` `[DOC]` `[SME]` `[OBS]` `[INF]` `[ASM]`. See `references/elicitation-cards.md`. G0 cannot pass while a *must* row is `INF` or `ASM`.

## 1. Problem and drivers *(must)*

| # | Driver (why change now) | Evidence | Tag |
|---|---|---|---|
| D1 | | | |

## 2. Goals and measures *(must)*

| Driver | Business goal | Measure | Baseline (date, sample) | Target | Candidate Outcome # | Tag |
|---|---|---|---|---|---|---|
| D1 | | | TBD | TBD | 1 | |

No benefit claim may be made while the baseline is `TBD`.

## 3. Stakeholders

| Stakeholder / role | Interest | RACI for this Pod | Must answer (elicitation card) | Contacted? | Tag |
|---|---|---|---|---|---|
| Sponsor | | A (funding) | §3.1 | ☐ | |
| Process owner | | A (design) | §3.1–3.11 | ☐ | |
| Performer / SME | | R | §3.2, 3.5 | ☐ | |
| Approver | | C | §3.8 | ☐ | |
| Data / system owner | | C | §3.10 | ☐ | |
| Risk / compliance | | C | §3.4, 3.6 | ☐ | |
| Output consumer | | I | §3.3 | ☐ | |

## 4. Scope

| In scope | Out of scope (Pod must refuse) | Tag |
|---|---|---|
| | | |

## 5. Principles and constraints

| # | Principle / constraint | Source | Consequence for the design |
|---|---|---|---|
| P1 | No production changes by this build | make-pod | Non-production targets only |
| P2 | Irreversible or consequential actions stay human | make-pod | HL ≤2 |
| P3 | | | |

## 6. Assumptions, risks and dependencies

| ID | Type (A/R/D) | Statement | Owner | Due | Tag |
|---|---|---|---|---|---|
| | | | | | ASM |

## 7. Approval to proceed (Gate G0)

| Role | Name | Decision | Date |
|---|---|---|---|
| Process owner | | approve / change | |
| Sponsor (optional) | | | |
