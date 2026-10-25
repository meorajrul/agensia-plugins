---
artifact: data-connector-catalogue
framework: p2a
version: "0.1"
status: draft
owner: <data or system owner role>
updated: <YYYY-MM-DD>
pod: pod-<role>-<subrole>.md
togaf_phase: "C (Data and Application) + D (Technology)"
---

> **Non-production only.** Every connector row must name a verified non-production instance before any operation. Unknown targets block operations.

# Data and connector catalogue — <Pod name>

Tag values `[OWN]` `[DOC]` `[SME]` `[OBS]` `[INF]` `[ASM]`.

## 1. Data objects

| ID | Data object | System of record | Owner | Classification (public / internal / confidential / personal / regulated) | Read by (Talent) | Written by (human / Workflow step) | Retention | Tag |
|---|---|---|---|---|---|---|---|---|
| DO1 | | | | | S1 | human only | | |

## 2. Connectors and integrations

| ID | System / connector | Environment (verified non-prod?) | Identity model | Read scope | Write scope | Approval before write | Receipt / read-back | Status | Tag |
|---|---|---|---|---|---|---|---|---|---|
| CN1 | | unknown → blocked | CONNECTOR_OWNER | | none | | | specified | |

Status: `specified`, `verified` (with date and evidence) or `blocked`. A required connector that is `blocked` stops the dependent Workflow (make-pod rule 14).

## 3. Environments

| Environment | URL / identifier (no credentials) | Company / workspace | Classification evidence | Verified by / date |
|---|---|---|---|---|
| Staging | | | | |

## 4. Checks before G3

- [ ] Every data object has a system of record and an owner.
- [ ] Personal or regulated data has a lawful basis or is excluded.
- [ ] Every write scope has a human approver and a read-back step.
- [ ] No credential, token or secret appears in this file.
