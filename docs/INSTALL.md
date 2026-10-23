# Install Agensia Harness

## Choose your download

- [Skill ZIP](https://github.com/meorajrul/agensia-plugins/raw/refs/heads/main/downloads/agensia-harness.zip): use for custom-skill upload in ChatGPT or Claude, or manual folder installation.
- [Portable plugin ZIP](https://github.com/meorajrul/agensia-plugins/raw/refs/heads/main/downloads/agensia-harness-plugin.zip): use only in a host supporting Agent Plugins v1. It is not the custom-skill upload ZIP.

## ChatGPT Desktop

1. Download the **Skill ZIP** above and keep it zipped.
2. Open the app's Plugins area and select Skills. Use its add/upload skill control when available, select the ZIP, review the imported instructions and enable the skill.
3. Start a chat and select Agensia Harness using the skill picker or an `@` mention.
4. Try: “Use Agensia Harness to draft a governed Pod for our purchase-request process. Work locally and leave missing facts open.”

Availability and upload labels depend on the app version, account and workspace policy. If upload is unavailable, use the account's supported web Skills interface or ask the workspace administrator about skill access. Attaching a ZIP to an ordinary chat supplies context; it does not establish persistent installation. A GitHub URL is a download/source location, not an automatically installed ChatGPT plugin.

Official guidance: [Skills and Plugins](https://learn.chatgpt.com/docs/skills-and-plugins) and [Build skills](https://learn.chatgpt.com/docs/build-skills). Check those pages for current product controls.

## Claude Desktop

1. Download the **Skill ZIP** and keep it zipped.
2. Enable **Code execution and file creation** under Settings → Capabilities, if required. Organisation policy may control this capability.
3. Open **Customize → Skills → + → Create skill → Upload a skill**.
4. Upload `agensia-harness.zip`, then enable it in the skills list.
5. Start a chat and request a governed Pod draft using Agensia Harness.

If the upload control is missing, check organisation permissions and the current app version. The skill ZIP contains one top-level skill folder with `SKILL.md` and supporting resources.

Official guidance: [Use skills in Claude](https://support.claude.com/en/articles/12512180-use-skills-in-claude).

## Manual ZIP installation for local skill hosts

1. Download and extract the **Skill ZIP**.
2. Keep the complete `agensia-harness/` folder, including `SKILL.md`, `assets/`, `references/` and `evals/`.
3. Put that folder directly inside the host's supported skill directory. For Codex project discovery use `<project>/.agents/skills/agensia-harness/`; for Claude Code project discovery use `<project>/.claude/skills/agensia-harness/`.
4. Start a fresh session and confirm the host lists the skill. Avoid an extra nested `agensia-harness/agensia-harness/` folder.

Desktop chat applications use their upload/import controls; copying into a coding host's project directory does not install a skill in every desktop app.

## Claude Code marketplace installation

Run in Claude Code:

```text
/plugin marketplace add meorajrul/agensia-plugins
/plugin install agensia-harness@agensia-plugins
```

The plugin and skill are both named `agensia-harness`. Some hosts show the qualified name `agensia-harness:agensia-harness`.

## Confirm installation and update

Ask for a local draft with a missing owner or source. The skill should keep missing facts open and preserve G0–G8 approval gates. Check that it refuses production changes. This smoke check is not a full behavioral evaluation.

To update, download the newer ZIP and use the host's replace/update control. For manual installs, replace the complete skill folder while retaining your own project documents elsewhere. Remove or disable older duplicate installations to avoid ambiguous selection.

## Production boundary

Never create or push changes to Agensia production. The restriction includes connectors and delegated agents. Platform operations require verified non-production platform and downstream targets; unknown or mixed targets block dependent operations. Installing the skill grants no credentials or platform permissions.

Installation instructions were reviewed against official documentation on 23 October 2026. Static package checks passed; desktop installations were not exercised in this repository's checks.
