# CSUB Kuali Prompt Library

Use this when the user wants reusable prompts, a team prompt library, or a stronger prompt for a Kuali task.

Token rule: do not load or return the whole library for one prompt request. Use headings or `rg` to locate the relevant prompt, then return only the selected prompt or a concise adaptation.

This library is adapted from the Kuali Connector prompt-library pattern: name the environment, describe the exact app/product/task, require a preview before mutations, list likely tool families, and define the final validation output. CSUB additions include sandbox-first experimentation, CSUB.edu source grounding, reference-form adaptation discipline, workflow/email/permission completeness, and lessons-learned capture.

## Prompt Design Rules

Every strong CSUB Kuali prompt should include:

- Environment: prod/default, sandbox, or read-only.
- Target: app name, product, form, workflow, group, document, CSV, or source page.
- Intent: inspect, design, compare, copy, update, publish, import, submit, report, or delete.
- Mutation boundary: read-only first, preview changes, wait for explicit go before major or destructive changes.
- Scope preservation: what must stay intact.
- Source grounding: reference app, CSUB.edu page, PDF, CSV, policy, or existing Kuali JSON.
- Output format: blueprint, diff, adaptation map, approval matrix, email set, testing checklist, report, or command.
- Validation: read the app/workflow/permissions/documents back after changes.

App-name rule: users should be able to provide the app name. The agent should resolve the underlying Kuali app record with read-only search/list/get tools, show a short candidate list only if the name is ambiguous, and include the resolved app name plus technical identifier in any mutation preview.

Use this skeleton when creating a new prompt:

```markdown
Using the [kuali-sandbox | kuali prod/default | read-only] Kuali tools, [inspect/design/update/copy/import/report] [target app name or process].

Context:
- App name:
- Business process:
- Submitter:
- Reviewers/approvers:
- Final record owner:
- Reference app or source:
- CSUB.edu source, if relevant:

Before making changes:
- Resolve the exact app from the name. If several apps match, show me the candidates and ask which one to use.
- Inspect the current app/configuration after resolving it.
- Show me the proposed changes as [blueprint/diff/adaptation map].
- Call out assumptions, risks, and anything that needs web UI/manual follow-up.
- Wait for "go" before mutating anything.

After changes:
- Read back form, workflow, permissions, and integrations where relevant.
- Summarize what changed and what still needs manual review.
- Provide a testing checklist.
```

## Install Connector And Skill

```markdown
Install the CSUB Kuali Build Agent skill and configure Kuali Connector on this computer.

Inputs:
- Skill repository URL or local path: `https://github.com/aburt1/CSUB-PACE-Kuali-Agent`
- Kuali tenant URL: `<choose production or sandbox below>`
  - Production: `https://csub.kualibuild.com`
  - Sandbox: `https://csub-sbx.kualibuild.com`
- Preferred Kuali profile name: `<production/default or sandbox>`

Rules:
- Actually perform the installation and verification steps. Do not only give me instructions.
- Assume this is either macOS or Windows, and either Codex or Claude Code.
- Detect the operating system and whether you are running in Codex or Claude Code. If you cannot tell, ask one short question.
- Do not ask me to paste API keys into chat. Use `kuali setup` or another secure Connector command so credentials are handled by the local keychain/credential store.
- If I do not have a Kuali API key yet, stop and tell me I need to get one from Kuali before Connector setup can finish.
- Do not mutate any Kuali data during setup.
- If configuring production, prefer read-only MCP tools unless I explicitly ask for write tools.
- Stop only for secrets, OS permissions, missing repo URL/path, or an unsupported environment.

Do this:
1. Check whether Kuali Connector is installed with `kuali version`.
2. If missing, install it from https://connector.kuali.co/:
   - macOS: `curl -fsSL https://connector.kuali.co/install.sh | sh`
   - macOS with Homebrew: `brew update && brew install kualico/tap/kuali`
   - Windows PowerShell: `irm https://connector.kuali.co/install.ps1 | iex`
3. Run `kuali setup` if no usable profile exists. Have me enter the Kuali tenant URL and API key locally when prompted, then run `kuali doctor`.
4. Configure MCP for my target client:
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

Report:
- What was installed or already present
- Which OS, assistant client, and Kuali profile were configured
- How Kuali Connector and the skill were verified
- Any exact manual restart, trust, or slash-command step still needed
```

Likely tools/actions: local shell checks, Kuali Connector install/setup commands, client-specific MCP setup/verify, skill-folder copy or Claude Code plugin wrapper creation. No Kuali write tools should be used.

## Build Or Improve A CSUB Kuali App

```markdown
Using the kuali-sandbox tools, help me design or improve the Kuali Build app named `<app name>`.

Start read-only. Resolve the app from its name, then inspect the current form, workflow, permissions, integrations, and existing documents only if needed. Search CSUB.edu for official public-facing context, office ownership, policy language, contact information, or links that should influence form language or emails.

Before making any changes, show me:
- App summary and business process summary
- Current gaps
- Proposed form section outline and field list
- Workflow map and approval matrix
- Notification and email template plan
- Permission model
- CSUB.edu sources referenced
- Risks, assumptions, and manual review items
- Testing checklist

Wait for "go" before making changes.
```

Likely tools/actions: app search/get, form outline/schema/template, workflow read, permissions read, integrations read, CSUB.edu web search, then update tools only after confirmation.

## Use A Reference App Without Literal Copying

```markdown
Using the kuali-sandbox tools, improve the app named `<target app name>` using `<reference app name>` as a design reference, not a literal copy.

Resolve both apps by name, then inspect them first. Classify the reference intent as design reference, pattern reference, or functional copy. Borrow only the structure, clarity, workflow patterns, email discipline, and permission ideas that fit the target process.

Do not copy reference-specific fields, signatures, policy text, roles, assignees, integrations, permissions, or email promises unless the target process independently requires them and I confirm.

Before changing anything, provide:
- Reference summary
- Target summary
- Borrow/adapt/keep/do-not-copy map
- Proposed form changes
- Proposed workflow changes
- Proposed email changes
- Proposed permission changes
- CSUB.edu sources to verify public-facing language
- Risks and testing checklist

Wait for "go" before mutating the target app.
```

Likely tools/actions: app search/get for both apps, form templates, workflow read, permissions read, comparison helper script, CSUB.edu web search.

## Copy Prod App To Sandbox Safely

```markdown
Copy the prod Kuali Build app named `<prod app name>` into kuali-sandbox for experimentation.

Before copying:
- Verify the prod/default and sandbox profiles.
- Resolve the exact prod app from the name and show app name plus technical identifier.
- Explain what will and will not copy automatically.
- Confirm whether workflow, permissions, integrations, and groups should be copied, adapted, or left manual.

After I say "go":
- Create the sandbox draft.
- Copy the form template/body.
- Copy or adapt workflow separately if requested.
- Do not publish unless I explicitly ask.
- Read back the sandbox form outline, workflow, and permissions.
- Report missing sandbox dependencies such as groups, roles, users, integrations, or lookups.
```

Likely tools/actions: doctor/auth status, apps list/get/create, forms get-template/update, workflow GraphQL or workflow tools, permissions read.

## Explore Sandbox Capabilities

```markdown
Using only the kuali-sandbox profile, probe what Kuali Build operations are available.

Start read-only:
- Verify the sandbox tenant/profile.
- List a small sample of apps.
- Pick the target sandbox app named `<app name>` and inspect app details, form outline, form schema, permissions, document count, pending workflow actions, groups, integrations, categories, and available read-only export options.
- Use GraphQL only for read-only primary workflow inspection if the normal workflow command does not expose it.

Safe previews:
- Use `--dry-run` to preview app creation, form update, and document creation.
- Do not publish, submit, approve, bypass, run integrations, create users, grant permissions, or delete anything unless I explicitly ask.

Output:
- Capability map
- Commands that worked
- Commands that were misleading or unsafe
- Sandbox-only edits made, if any
- Skill updates recommended
```

Likely tools/actions: explicit CLI `--profile sandbox`, app/form/permission/document/action/group/integration/category list commands, GraphQL primary workflow read, dry-run mutation previews.

## Workflow Repair Or Audit

```markdown
Using the kuali-sandbox tools, audit the workflow for the app named `<app name>`.

Start read-only. Resolve the app from its name, then walk through every workflow step and show:
- Step name and type
- Trigger condition
- Assignee role/group/person
- Action required
- Possible outcomes
- Emails or notifications
- Send-back behavior
- Edit/view rights
- Risks or missing paths

Specifically check for missing approval, denial, send-back, completion, final notification, reminder, and final record-owner paths.

Recommend improvements, but do not change the workflow until I approve the proposed map.
```

Likely tools/actions: apps get, workflow read, documents/workflow executions if troubleshooting real routing, permissions read.

## Email Template Improvement Pack

```markdown
For the Kuali app named `<app name>`, draft a complete CSUB email template set.

Resolve the app from its name and inspect the app/workflow first if available. Search CSUB.edu for the owning office name, contact block, and any public instructions or links that belong in the email.

Create templates for the relevant events:
- Submission confirmation
- Reviewer or approver task notification
- Returned for correction
- Approval confirmation
- Denial notification
- Completion notification
- Admin/office notification
- Integration failure/manual intervention, if applicable

For each template include:
- Template name
- Trigger
- Recipient
- Subject
- Body
- Merge placeholders to confirm
- When not to send it

Do not install/update templates until I approve.
```

Likely tools/actions: app/workflow read, CSUB.edu web search, then notification/email update tools only after confirmation if available.

## Permission Audit

```markdown
Using the Kuali tools, audit permissions for the app named `<app name>`.

Start read-only. Resolve the app from its name, then show who can submit, view, edit drafts, edit after submission, approve/complete tasks, administer, export/report, and manage integrations if visible.

Compare the current permissions to least-privilege expectations for this process. Identify broad access, missing reviewer access, sandbox/prod identity mismatches, and permissions copied from a reference app that do not fit.

Do not change permissions until I approve a proposed permission model.
```

Likely tools/actions: apps get, permissions list, groups/users lookup where needed.

## CSV Import With Mapping Review

```markdown
Using the kuali-sandbox tools, prepare to import `<csv file>` into the app named `<app name>`.

Before importing:
- Resolve the target app from its name.
- Read the form fields and identify likely CSV-to-field mappings.
- Show the mapping and any ambiguous columns.
- Recommend whether to dry-run first.
- Confirm whether rows should remain drafts or be submitted through workflow.

Wait for "go" before importing. If importing many rows, chunk the file and verify progress after each chunk. On the first failure, stop and show the failing row, error, and options.

After import, verify document counts and summarize rows imported, failures, and cleanup items.
```

Likely tools/actions: apps list, forms list/schema, import CSV dry-run/import, documents list.

## CSUB.edu-Grounded Form Language

```markdown
Improve the user-facing language for the app named `<app name>` using official CSUB.edu sources.

Resolve the app from its name and inspect the current form first. Search CSUB.edu for the owning office, service page, catalog/policy page, or public process instructions.

Then propose:
- Revised app description
- Section intro text
- Field help text
- Attachment instructions
- Certification/acknowledgment text
- Confirmation and completion email language
- Source links to include

Separate source-derived facts from assumptions. Do not change workflow, permissions, or policy requirements based only on web content. Wait for approval before updating the form.
```

Likely tools/actions: form outline/template, CSUB.edu web search, update only after confirmation.

## Prompt Improvement Prompt

```markdown
Rewrite this Kuali request into a safer, more complete CSUB Kuali prompt:

`<paste rough request>`

Make the improved prompt include:
- Environment/profile
- App name, with the Kuali app record resolved by the agent
- Read-only inspection first
- Exact target identification
- Reference apps or CSUB.edu sources
- Mutation confirmation boundary
- Expected output artifacts
- Validation steps
- Testing checklist

Keep it concise and copy-paste ready.
```

Use this when a request is too vague, risky, or likely to cause the agent to mutate the wrong app.
