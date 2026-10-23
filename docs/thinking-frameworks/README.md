# Thinking frameworks

Four cards support Agensia Harness: MECE, decision types, one-way/two-way doors, and RACI/DACI. Each retains its public origin attribution and source links. Frameworks never waive evidence, human approval or the production prohibition.

Edit `frameworks.json` or `skill-map.json`, then run `python3 scripts/thinking_frameworks.py` from the collection root. The generator updates the marked skill section and its bundled reference. Run it with `--check` to check for drift. Do not edit generated content directly.

Run `python3 scripts/skill_bundle.py docs` after resource changes, then validate the collection. The per-skill `reference_intro` keeps its introduction self-contained. Tests are in `scripts/tests/`.
