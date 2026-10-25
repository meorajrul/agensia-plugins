# Agensia Plugins

The plugin is `agensia-harness`; its skill is `make-pod`.

Download installable ZIPs from [GitHub Releases](https://github.com/meorajrul/agensia-plugins/releases/latest). ZIP archives are release assets and are not stored in the source tree.

The skill supports builders who are not the process owner: elicitation cards per Agensia component, provenance tags, a TOGAF crosswalk, and Pod Charter, SIPOC + RACI, Data and Connector Catalogue, role-binding and Pod Contract templates. The plugin README has Mermaid visual documentation.

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

Start with [the skill](plugins/agensia-harness/skills/make-pod/SKILL.md). Keep its resources together when importing or sharing it. See [portability and exports](docs/PORTABILITY.md), [the catalog](docs/skill-catalog.md) and [maintenance instructions](AGENTS.md).

The plugin is named `agensia-harness` and its skill is `make-pod`; hosts may qualify the invocation as `agensia-harness:make-pod`. This collection contains only the generic harness skill; no customer evidence or environment configuration is bundled.

<!-- BEGIN BUNDLE CATALOG -->
## Department map

These are intended users of the plugins. PMO means project management; GTM means sales and marketing.

| Plugin | Intended departments | Skills |
|---|---|---|
| [agensia-harness](plugins/agensia-harness/README.md) | Engineering, PMO, Operations | 1 |

**1 plugins · 1 top-level skills.** Nested helper skills are bundled resources, not separate catalog entries.

[Browse every skill](docs/skill-catalog.md) · [Name migration](docs/skill-name-migration.json)

Catalog fingerprint: `a257b59959a8bae8f33cab87ca294b9c24aff919ea6443fe106fe9da6df56d8a`.
<!-- END BUNDLE CATALOG -->
