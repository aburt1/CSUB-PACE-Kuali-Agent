# Kuali Tool Gotchas

Use this when copying, adapting, or mutating real Kuali configuration.

Token rule: load this only when the task involves Kuali tooling behavior, prod/sandbox copy, workflow copy, unexpected validation results, or sandbox dependency mismatches. Do not load it for ordinary form-design brainstorming.

## Prod And Sandbox

- Always verify the active profile before mutation.
- Treat `default` as likely prod and `sandbox` as the experimentation profile unless the current environment proves otherwise.
- Show the app name, app ID, profile, and tenant before changing anything.
- Sandbox users, groups, roles, integrations, and lookups may not match prod.
- The Kuali MCP may be pinned to `default`/prod. Passing `--profile sandbox` through `kuali_run` may not change the connected tenant. Verify with returned app IDs/tenant evidence or use explicit CLI `--profile sandbox`.
- Do not run `smoke` as a read-only test. It creates, publishes, submits, and cleans up test artifacts.

Useful checks:

```bash
kuali doctor --profile default
kuali doctor --profile sandbox
kuali --profile sandbox apps list --search "App Name" --all --output json --quiet
```

## App Copying

- Form, workflow, permissions, integrations, and documents are separate concerns.
- `apps create --form` may create only the app shell.
- For copied form bodies, `forms get-template` plus `forms update --skip-validation` has been the reliable round-trip path for legacy/display-heavy Kuali forms.
- Workflow does not necessarily copy with the form. Read it and copy/adapt it separately when needed.
- Do not publish the sandbox copy unless the user explicitly asks.

Reliable form round-trip pattern:

```bash
kuali --profile default forms get-template PROD_APP_ID --output json --quiet > prod-template.json
kuali --profile sandbox forms update --app SANDBOX_APP_ID --data @prod-template.json --skip-validation
```

## Workflow

- Validate workflow by reading it back, not by trusting a successful mutation response.
- Missing workflow is common after app copy; inspect it separately from the form outline.
- Person, group, and role assignee shapes can differ. If sandbox lacks a prod role/group, use an explicit temporary sandbox mapping and label it.
- Do not silently replace a prod office role with a person in final design. Person-based assignees are acceptable for sandbox testing only when clearly marked.

## Reference Forms

- A reference app is usually a design or pattern source, not a literal copy source.
- Do not copy reference-specific signatures, attestations, approvers, emails, permissions, integrations, or policy language unless the target process independently requires them.
- Use the reference adaptation map before mutation.

## CSUB.edu Sources

- CSUB.edu can ground public language, office ownership, links, and policy context.
- Kuali configuration remains the source of truth for actual saved behavior.
- If CSUB.edu conflicts with the current Kuali app, report the conflict and ask which should win.

## Validation Traps

- A form outline can look correct while workflow is still missing.
- A workflow can save with an empty or invalid assignee if the assignee shape is wrong.
- Existing documents do not prove the current draft configuration is correct.
- A successful import/update command does not prove permissions, notifications, integrations, or routing are valid.
- `kuali_summary` can be too expensive and may time out on a large tenant.
- Some list-style tools may return more records than requested. Summarize and redact sensitive details rather than pasting long failure lists.
- `documents list` can return `data: null` when there are no documents, not `data: []`. Handle both.
- `workflows list --app` targets secondary workflows and can error or miss the primary Build workflow. Use GraphQL `app(id){workflow}` for the primary workflow.
- `workflows actions --app` is useful for pending task counts, but no pending work may return `actions: null`.
- `apps icons` returns the full icon registry; do not call it casually or paste the whole result.
- User search can be broad. Treat returned users as candidates and verify exact IDs/emails before permission or workflow mutations.

After mutation, read back:

- app details
- form outline/template
- workflow
- permissions
- integrations or notification settings where available

Then fill out `templates/validation-report.md`.
