# Agensia Harness

Reference guidance now uses self-contained, company-neutral design checks for coverage, decision risk, reversibility and ownership.

[Installation guide: ChatGPT Desktop, Claude Desktop and manual ZIP import](../../docs/INSTALL.md).

Design governed AI Pods from business processes, approved sources and explicit human responsibilities. P2A connects **Outcome, Context, Sources, Scope, Authority, Output and Verification** through nine design gates, G0–G8.

## Agensia Harness

Start with [the skill](skills/agensia-harness/SKILL.md). Supply a process/SOP, intended users and outputs, approved knowledge, systems and accountable owner. A partial brief is enough to begin a labelled draft; missing facts remain open.

The skill produces a Pod specification, harness/control specification, ontology packs, per-outcome golden tests, platform field mapping and operating handoff. Local drafting is the default. No private reference library, environment URL or particular workspace folder structure is required. Keep the whole skill folder together when sharing it.

```mermaid
flowchart LR
  P[Process and approved sources] --> D[Governed Pod design]
  D --> G[Owner design gates]
  G --> L[Local specification and test plan]
  L --> N[Authorised non-production verification]
```

## Strict production prohibition

**Agensia Harness must never create or push changes to Agensia production.** This includes uploads, submissions, publication, edits, deletions, runs, schedules and writes through production-connected integrations. It applies equally to UI actions, APIs, scripts, connectors and delegated agents. Verify non-production status for the platform and downstream resources before operations; unknown targets block operations. No owner request or design-gate approval waives this rule.

Production release is a separate human-controlled process outside this skill. The skill can supply local specifications and non-production test plans; it does not perform production release.

## Core distinctions

- Pods coordinate job-role capabilities; Talents define triggered operations; ontology supplies versioned knowledge, procedures and templates.
- Saved Workflows execute repeatable or decision-bearing tasks. Blueprints plan work, Collections organise saved context, and schedules time authorised work.
- Native calculated decisions require their own inputs, solve, acceptance and return to the originating task.
- Source binding, actual reading, saved configuration, execution, human decision and useful outcome require separate evidence.
- Harness levels define authority; prompt wording and evaluation scores do not enforce it. Consequential actions remain human-controlled.

## References

| Guide | Purpose |
|---|---|
| [Platform guide](skills/agensia-harness/references/agensia-platform-walkthrough.md) | Components and four-part configuration |
| [Capabilities and acceptance](skills/agensia-harness/references/platform-knowledge-and-uat.md) | Generic coverage and negative tests |
| [Onboarding verification](skills/agensia-harness/references/platform-evidence-and-onboarding.md) | Actor/access map and evidence-based handoff |
| [Workflow contract](skills/agensia-harness/references/workflow-execution-contract.md) | Versioned tasks, bindings, native gates and recovery |
| [Prompt playbook](skills/agensia-harness/references/converse-prompt-playbook.md) | Templates for authorised non-production operation |
| [Evaluation](skills/agensia-harness/references/pod-evaluation.md) | Owner goals, paired comparison and regression gates |

## Use and verification

Use the host's available tools and the recipient's approved sources. Read applicable local instructions. No installation, account connection or permission follows from importing this package. Reference guidance uses company-neutral design checks.

Version **1.0.0** provides self-contained generic guidance, a non-waivable production boundary and synthetic refusal scenarios. Test cases start unrun; static package validation is not runtime certification. Intended departments: Engineering, PMO and Operations.

The plugin and skill are both named `agensia-harness`. The P2A method, resources and production prohibition are preserved under this name.

<!-- BEGIN SKILL CATALOG -->
## Departments and portable skills

**Intended departments:** Engineering, PMO, Operations.

**1 skills.** [Full catalog](../../docs/skill-catalog.md) · [Cross-platform setup](../../docs/PORTABILITY.md).

Skill paths and names below are the current invocation identifiers. Previous names are recorded in the [migration map](../../docs/skill-name-migration.json).

| Skill | Intended departments |
|---|---|
| [agensia-harness](skills/agensia-harness/SKILL.md) | Engineering, PMO, Operations |

Catalog fingerprint: `46b601466afee2d1cedaeb5dbfcd351d9a8e3c5f7a257eeaf6a62f382498e297`.
<!-- END SKILL CATALOG -->
