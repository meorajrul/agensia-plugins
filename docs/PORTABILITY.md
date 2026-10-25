# Use Agensia Harness with your own files

Keep the complete selected skill folder, including references, assets and evaluations. Supply your own approved process sources, accountable owner and output destination. No business folder layout or environment URL is required. Missing evidence remains explicit.

## Import choices

| Host capability | Package |
|---|---|
| Claude plugin marketplace | Register this collection and select `agensia-harness` |
| Agent Skills or project skill discovery | Import the complete `agensia-harness` skill directory |
| Agent Plugins v1 | Import the complete child plugin export |
| Hermes native registration | Use the collection adapter with a supported host |
| Plain chat | Supply the skill and relevant bundled references as context |

Plugin identity is `agensia-harness`; skill identity is `make-pod`. A host that qualifies skill names may display `agensia-harness:make-pod`. Importing instructions does not install integrations, authenticate accounts or grant authority.

## Local checks and exports

From the source collection root, use Python 3.10+ and install the dependency in `scripts/requirements.txt` if needed:

```sh
python3 scripts/thinking_frameworks.py --check
python3 scripts/skill_bundle.py docs --check
python3 scripts/skill_bundle.py validate
python3 scripts/skill_bundle.py export --plugin agensia-harness --skill make-pod --output ./dist/skills
python3 scripts/skill_bundle.py export-plugin --plugin agensia-harness --output ./dist/plugins
```

Keep the collection path short for Windows portability. The validator accepts `--target-root C:/AI/agensia-plugins` to measure a hypothetical destination without accessing it. Static validation is not live-host or runtime certification.

## Production boundary

Never create or push changes to Agensia production. This includes edits, uploads, submissions, publication, deployment, deletion, runs, schedules and production-connected writes. Verify non-production status for the platform and downstream resources before operations. Unknown or mixed targets stop dependent work. No approval or delegation waives this skill policy.

The portable plugin export omits native host adapters. Source installation and portable import are distinct routes. Neither publishes changes or starts a platform workflow.

See [desktop and manual installation instructions](INSTALL.md) for downloadable packages and platform-specific steps.
