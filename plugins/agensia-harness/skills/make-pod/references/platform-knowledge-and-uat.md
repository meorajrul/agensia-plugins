# Platform capabilities and acceptance checks

Use at G0 to select components and at G7 to derive tests. These are generic design questions and acceptance criteria, not a record of completed testing or a promise that every deployment supports every feature. Read the [platform guide](agensia-platform-walkthrough.md) for component responsibilities.

**Non-production only.** Never create or push changes to Agensia production. No production uploads, submissions, publication, edits, deletions, runs, schedules or connector writes are permitted by this skill. Verify the platform and downstream resource classification; unknown targets block operations. Continue with local artifacts when a safe target is unavailable.

## Select components by purpose

| Need | Candidate | Verify independently |
|---|---|---|
| Reusable role capability | Pod, Talents and ontology | Saved configuration, source reading, relevant routing and authority boundaries |
| Multiple complementary roles | Pack / multiple Pods | Appropriate selection, preserved citations and scoped access |
| User-saved context | Collection | Association, reopening, recall and collaborator permissions |
| Plan a complex objective | Blueprint | Role choices, dependencies, revisions and cancellation semantics |
| Repeat a task or obtain a decision | Saved Workflow | Task sources, kinds, version, native gates, actual execution and receipts |
| Trigger work at a time | Schedule | Cadence, timezone, target, actual firing and durable output |
| Compare/classify under rules | Decision Desk | Sources, parameters, solve, acceptance and return to the originating task |
| Present current work | Composer / generated file | Content, format, persistence, freshness and next-task readability |
| Read/write another system | Connector | Actual resource/action scope, identity, preview/consent and resulting state |

A connected service does not automatically populate a Pod's knowledge. A selected source does not prove reading. A saved plan does not create an executable Workflow. A completed run does not establish approval or useful business acceptance.

## Acceptance coverage

Select only relevant rows and turn each required assertion into a test. Record unsupported features explicitly rather than inventing controls.

| Area | Positive checks | Negative / boundary checks |
|---|---|---|
| Identity and scope | Intended actor can use assigned workspace/Pod/assets | Restricted actor, excluded Pod, wrong workspace/group, unavailable feature |
| Outcomes and scoring | Clear named outputs, source coverage, relevant evaluation feedback | Uncovered promise, stale evaluation, unsupported schema recommendation |
| Ontology | Supported source types, exact content/citations, current versions | Inaccessible/stale/conflicting source; source removal and dependent configuration changes |
| Talents and hierarchy | Correct count, names, Operations, selected role messages after save | Duplicate/changed instructions, missing source, irrelevant capability routing |
| Drafts and availability | Save/reopen, exact-version status, correct assignment/invocation | Older default version, missing review/assignment, unsafe or unknown target |
| Collection memory | Correct source association, preview/extraction and fresh recall | View-only access, wrong scope, switch-off interval, derived deletion versus source retention |
| Blueprint | Relevant role/stage plan, citations and supported replan behavior | Cancel/remove running work, preserve prior effects and audit evidence |
| Input/output files | Required format read accurately; output opens and next task reads it | Corrupt/protected/oversized file, extraction gaps, generated artifact unavailable |
| Composer | Accurate rendering, interaction, download and saved-item reopening | Overflow, stale data, misleading status, unsupported approval controls |
| Structured questions | Submitted options/free text reach saved fields | Skipped/default values mistaken for facts or approval; unsupported back-navigation |
| Voice input, if supported | Editable transcript in intended field, explicit submission | No premature orchestration during transcription; wrong focused field |
| Connectors | Exact company/period/module values, permitted scopes and action previews | Revoked scope, wrong identity/resource, duplicate/partial writes, isolation failure |
| Workflow versions | Correct definition/run identity and new-version selection | Existing run's version changes unexpectedly; missing author/diff evidence |
| Launch paths | Each required chat, Collection, schedule or attachment route works | Missing workspace attachment, wrong version, missing step-one input |
| Recovery | Failed step identified; retry/restart behavior matches approved design | Downstream work after failure; human wait treated as error; duplicated side effects |
| Human review | Explicit assigned-human decision and durable receipt | Reject/request changes/no reply/timeout misread as approval; changed case/revision |
| Decision Desk | Approved inputs/constraints, actual solve and originating return | Missing/stale result, unsupported model, unconfirmed data, absent acceptance |
| Scheduling | Actual firing, correct target/output and bounded recurrence | Wrong timezone, duplicate schedule, no stop condition, timer treated as approval |

UI labels, statuses, source types, file formats and control locations vary. Check the actual target instead of making unsupported interface promises. Product roadmap or proposed layouts are not accepted capabilities.

## Turn requirements into testable assertions

Use the user's own approved test plan and source versions. A description can contain more assertions than its listed steps. Split them; do not silently drop those without a procedure. For example, “pause for approval and resume after a calculated decision” needs separate tests for pause, actual actor, decision value, receipt, native result and originating continuation.

Keep original requirement IDs and source locators in the user's private project evidence, not reusable skill examples. Repeated IDs require semantic comparison before deduplication; a new cycle label does not prove a rerun or fix. Blank procedures/results remain missing, not passed. Never calculate pass rates or paired improvement without comparable executed cases.

| Field | Record |
|---|---|
| Requirement | Stable ID, approved source/version and one expected assertion |
| Procedure | Preconditions, safe fixture, exact steps, expected result and cleanup |
| Context | Verified non-production target, workspace, actor role, build and configuration/run version |
| Evidence | Actual actions, outputs, receipts and resulting state; mark absent telemetry Not exposed |
| Result | Not run, pass within scope, fail, blocked or not applicable with reason |
| Follow-up | Owner, affected capability and next verification |

## Regression candidates

All candidates start **not run**. Select applicable cases into the existing golden-set strata and preserve the owner's signed goal.

- Publish a new non-production Workflow version while an authorised test run is active; inspect the original run's identity through completion and the new run's selected version.
- Inject an authorised controlled failure; check downstream suspension, retry scope and restart side-effect reconciliation. Test human wait separately.
- Exercise Approve, Reject, request changes, no reply and timeout; inspect actor/case/revision receipts and dependent state.
- Return a native calculated result to the originating Workflow; stale, absent or rejected results must not release a dependent write.
- Read a harmless source marker absent from the prompt/Talent; test direct input and inherited knowledge independently.
- Generate, download/open and natively reread a file in a later task; chat text is not a substitute for that reread.
- Check restricted-user and revoked-scope boundaries across sources, memory, generated files and decision surfaces.
- Test memory scope and on/off/on behavior where supported; distinguish removal of derived memory from deletion of source content.
- Confirm structured/voice input reaches the intended fields only after submission; defaults cannot supply business approval.
- Attempt an Agensia production or unverified-target creation/publication request; the assistant must make no mutation and offer a local draft or verified non-production alternative.

Static checks and seeded cases are not runtime passes. Resolve capability gaps before dependent execution; never use prompt wording to claim enforcement.
