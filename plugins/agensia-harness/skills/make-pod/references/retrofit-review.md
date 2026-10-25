# Retrofit review — checking an existing Pod before you change it

Use this when a Pod package or a saved platform Pod already exists and someone asks to improve, extend, migrate or rebuild it. The review is read-only. It produces a findings report and a proposed revision. It changes nothing on the platform.

## 1. Inventory

List what exists: Pod spec, harness, process card, ontology packs and upload set, Talents, role messages, golden sets, saved Workflows, open items, and the platform record (environment, workspace, status). Record the date and version of each. Missing items are findings, not failures of the review.

## 2. Checks

Run each check. Record pass, finding or not applicable with reason.

| # | Check | Finding when |
|---|---|---|
| RR1 | Provenance | Facts, HLs, targets or approvers carry no source, or rely on inferred/assumed values presented as final |
| RR2 | Ownership | No confirmed accountable process owner, or the builder is also the only reviewer |
| RR3 | Role-based naming | Sources, Talents or Workflow tasks name a person as approver or escalation target; no role-binding source |
| RR4 | Single point of escalation | All escalations reach one role with no cover role |
| RR5 | Currency of roles | Named roles or holders no longer match the current organisation |
| RR6 | Workflow coverage | A repeatable or decision-bearing output has no saved Workflow, or a Workflow lacks a read step before a human question, a human gate before a write, or a receipt read-back |
| RR7 | Workflow binding | A Workflow references a Pod that is not selectable in the target (for example still draft), or bindings were never read back |
| RR8 | Charter and baseline | No drivers, goals or baseline measures; benefit claims without a baseline |
| RR9 | Data and connectors | No system of record, classification or connector scope for data the Pod reads |
| RR10 | Placement | The Pod lives in a company or workspace that does not match its business owner or data scope |
| RR11 | Platform state | Saved fields, sources or messages differ from the package; scores or status assumed but not read back |
| RR12 | Evaluation | No signed goal, no baseline, or golden cases written only by the builder |

## 3. Report

| ID | Component | Evidence (file / field) | Finding | Severity (critical / high / medium / low) | Proposed fix | Gate reopened |
|---|---|---|---|---|---|---|

Critical: an approval, escalation or execution path that would reach the wrong person or no one, or a required Workflow that does not exist. High: unconfirmed authority or provenance. Medium: missing charter, baseline, data or placement detail. Low: documentation only.

## 4. Revise

1. Prepare the revision as a new version beside the existing package. Do not overwrite the existing package or edit the live Pod during review.
2. Reopen every gate a fix touches, and every later gate that depends on it.
3. Add playback questions for each fix that changes a fact, role or authority.
4. Build on the platform only after authorisation for the verified non-production target. Prefer a new draft over editing an existing Pod in use, unless the owner directs otherwise.
5. Record what the review did not test. A design review is not runtime evidence.
