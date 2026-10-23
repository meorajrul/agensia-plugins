# Agensia Plugins

[Installation guide: ChatGPT Desktop, Claude Desktop and manual ZIP import](docs/INSTALL.md).

Dedicated platform skills for designing governed Agensia Pods and agent harnesses. Bring your own process, approved sources and accountable owner.

## Agensia Harness

[Agensia Harness](plugins/agensia-harness/README.md) turns a business process into a Pod specification, authority controls, ontology packs, Workflow specifications, acceptance cases and an operating handoff. Its G0–G8 design gates preserve explicit human ownership.

**Never create or push changes to Agensia production.** Local drafting is the default; any authorised platform operation requires verified non-production platform and downstream targets. The rule covers tools, connectors and delegated agents. Unknown or mixed targets block dependent operations.

```mermaid
flowchart LR
  A["Agensia platform skills"] --> H["Agensia Harness"]
  H --> E["Engineering"]
  H --> P["PMO"]
  H --> O["Operations"]
```

## Use

Start with [the skill](plugins/agensia-harness/skills/agensia-harness/SKILL.md). Keep its resources together when importing or sharing it. See [portability and exports](docs/PORTABILITY.md), [the catalog](docs/skill-catalog.md) and [maintenance instructions](AGENTS.md).

The plugin and skill are both named `agensia-harness`; hosts may qualify the invocation as `agensia-harness:agensia-harness`. The [migration map](docs/skill-name-migration.json) records previous software identifiers. Historical identifiers are not installed aliases. This collection contains only the generic harness skill; no customer evidence or environment configuration is bundled.

<!-- BEGIN BUNDLE CATALOG -->
## Department map

These are intended users of the plugins. PMO means project management; GTM means sales and marketing.

| Plugin | Intended departments | Skills |
|---|---|---|
| [agensia-harness](plugins/agensia-harness/README.md) | Engineering, PMO, Operations | 1 |

**1 plugins · 1 top-level skills.** Nested helper skills are bundled resources, not separate catalog entries.

[Browse every skill](docs/skill-catalog.md) · [Name migration](docs/skill-name-migration.json)

Catalog fingerprint: `afbbeb1c01b76dd076bd17710c71f8ea7bd0993e6c88ea03f7fee8ecf6f0beae`.
<!-- END BUNDLE CATALOG -->
