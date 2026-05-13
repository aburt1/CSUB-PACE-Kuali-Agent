# CSUB PACE Kuali Agent

This repository contains a portable skill for helping design, inspect, adapt, and improve CSUB Kuali Build apps, forms, workflows, permissions, integrations, notifications, and email templates.

The skill is intentionally written as a reusable operating guide, not as a dump of live Kuali configuration. Do not publish raw app exports, API keys, workflow payloads, document data, user lists, or tenant-specific test artifacts with it.

## Contents

```text
csub-kuali-build-agent/
├── SKILL.md
├── agents/
├── references/
├── scripts/
└── templates/
```

`SKILL.md` is the small router and safety kernel. Detailed guidance lives in `references/`, reusable output shapes live in `templates/`, and deterministic helpers live in `scripts/`.

For reusable copy-paste prompts, see the [CSUB Kuali Prompt Library](references/prompt-library.md).

## Before You Paste The Installer Prompt

The prompt below installs the skill and configures Kuali Connector for you. Before using it, have:

- Codex or Claude Code installed.
- macOS or Windows.
- A Kuali API key from Kuali with only the permissions you should have.

CSUB tenant URLs:

- Production: `https://csub.kualibuild.com`
- Staging: `https://csub-stg.kualibuild.com`
- Sandbox: `https://csub-sbx.kualibuild.com`

Do not paste the API key into chat. The installer prompt tells the agent to use `kuali setup` so you can enter the key locally and securely. This skill does not include credentials and does not grant Kuali access.

## Copy-Paste Installer Prompt

Paste this into Codex or Claude Code. The agent should do the setup work, not just explain it.

```text
Install the CSUB Kuali Build Agent skill and configure Kuali Connector on this computer.

Inputs:
- Skill repository URL or local path: https://github.com/aburt1/CSUB-PACE-Kuali-Agent
- Kuali tenant URL: <choose production, staging, or sandbox below>
  - Production: https://csub.kualibuild.com
  - Staging: https://csub-stg.kualibuild.com
  - Sandbox: https://csub-sbx.kualibuild.com
- Preferred Kuali profile name: <production/default, staging, or sandbox>

Rules:
- Actually perform the installation and verification steps. Do not only give me instructions.
- Assume this is either macOS or Windows, and either Codex or Claude Code.
- Detect the operating system and whether you are running in Codex or Claude Code. If you cannot tell, ask one short question.
- Do not ask me to paste API keys into chat. Use `kuali setup` or another secure Connector command so credentials go into the local keychain/credential store.
- If I do not have a Kuali API key yet, stop and tell me I need to get one from Kuali before Connector setup can finish.
- Do not mutate any Kuali data during setup.
- If configuring production, prefer read-only MCP tools unless I explicitly ask for write tools.
- Stop only for secrets, OS permissions, missing repo URL/path, or an unsupported environment.

Steps:
1. Check whether `kuali` is installed with `kuali version`.
2. If missing, install Kuali Connector from https://connector.kuali.co/:
   - macOS: `curl -fsSL https://connector.kuali.co/install.sh | sh`
   - macOS with Homebrew: `brew update && brew install kualico/tap/kuali`
   - Windows PowerShell: `irm https://connector.kuali.co/install.ps1 | iex`
3. Run `kuali setup` if no usable profile exists. Have me enter the Kuali tenant URL and API key locally when prompted, then run `kuali doctor`.
4. Configure MCP for the target client:
   - Codex: `kuali mcp setup --client codex`
   - Claude Code: `kuali mcp setup --client claude-code`
5. Verify MCP:
   - Codex: `kuali mcp verify --client codex`
   - Claude Code: `kuali mcp verify --client claude-code`
6. Install the skill:
   - If the skill source is a Git repository URL, clone it into a temporary directory first.
   - If running in Codex, copy the `csub-kuali-build-agent` folder into `~/.codex/skills/`.
   - If running in Claude Code, create a local plugin wrapper, put `csub-kuali-build-agent` under the plugin's `skills/` directory, create `.claude-plugin/plugin.json`, then install or enable that plugin. If Claude Code requires a slash command that you cannot execute directly, prepare the plugin folder and tell me the exact command to run.
7. Start or recommend a fresh assistant session.
8. Run a read-only verification prompt or command, such as listing a few Kuali apps or inspecting one sandbox app. Do not create, update, submit, approve, publish, import, or delete anything.

Final response:
- Tell me what was installed or already present.
- Tell me which OS, assistant client, and Kuali profile were configured.
- Tell me how you verified Kuali Connector and the skill.
- Tell me any exact manual restart, trust, or slash-command step still needed.
```

## Kuali Profile Safety

Before any Kuali mutation, verify the target profile and tenant. The skill recommends explicit sandbox checks such as:

```bash
kuali --profile sandbox auth status --output json --quiet
kuali --profile sandbox apps list --search "App Name" --all --output json --quiet
```

Do not assume a connected MCP server is pointed at sandbox. Do not use `smoke` as a read-only probe; it may create, publish, submit, and clean up temporary artifacts.

## Publishing Checklist

Before publishing this repository:

- Keep only the skill folder and intended documentation.
- Remove raw Kuali exports, workflow payloads, document data, local scratch files, and tenant-specific probes.
- Confirm no API keys, user IDs, emails, local file paths, or personal names appear in the published files.
- Keep examples generic unless the owning office explicitly approves public examples.
- Run a final scan:

```bash
rg -n -i 'api[_-]?key|bearer|token|secret|home path|email address|school id|display name|prod app|sandbox app|workflow payload|document id|user id'
```

## Suggested First Prompt

```text
Use the CSUB Kuali Build Agent skill. Help me inspect this Kuali Build app in sandbox, summarize the form/workflow/permissions, identify gaps, and propose improvements before making any changes.
```
