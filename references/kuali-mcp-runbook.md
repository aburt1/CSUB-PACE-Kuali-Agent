# Kuali MCP / CLI Runbook

Use this when inspecting or mutating real Kuali configuration.

## Connector Setup Check

This skill assumes Kuali Connector is installed and wired into the active AI client. If Kuali tools are missing, start with the official setup path:

```bash
kuali version
kuali setup
kuali doctor
kuali mcp setup --client codex
kuali mcp setup --client claude-code
kuali mcp verify --client codex
kuali mcp verify --client claude-code
```

Use the client-specific setup and verify commands that match the user's assistant. Do not collect API keys in chat; let `kuali setup` prompt locally and store credentials in the OS credential store.

CSUB tenant URLs:

- Production: `https://csub.kualibuild.com`
- Staging: `https://csub-stg.kualibuild.com`
- Sandbox: `https://csub-sbx.kualibuild.com`

## MCP Capability Map

Observed Kuali MCP tool families:

- Generic command runner: `kuali_run`
- Instance overview: `kuali_summary`
- Apps: `kuali_apps_get`; use `kuali_run "apps list ..."` for app search/listing
- Forms: `kuali_forms_list`; use `kuali_run` or CLI for outline/template/update operations not exposed as typed tools
- Documents: `kuali_documents_get`, `kuali_documents_sendback`, `kuali_import_csv`
- Workflows: `kuali_workflows_list`, `kuali_workflows_executions`, `kuali_workflows_sendback`, `kuali_workflows_retry`
- Permissions: `kuali_permissions_list`, `kuali_permissions_get`, `kuali_permissions_grant`
- Groups: `kuali_groups_list`, `kuali_groups_get`, `kuali_groups_members`
- Integrations: `kuali_integrations_list`, `kuali_integrations_failures`, `kuali_integrations_run`

Typed tools are convenient, but they use the connector's configured profile. If the task requires sandbox, verify the MCP profile before using typed tools or use the explicit CLI profile.

## Profile Safety

In one tenant setup, the Kuali MCP was observed running against the connector's default profile:

```text
profile: default
api_url: https://example.kualibuild.com
```

Passing `--profile sandbox` through `kuali_run` did not switch the MCP to sandbox during testing; it still returned prod app IDs. For sandbox-only work, use explicit CLI calls unless the MCP connector has been reconfigured and re-verified:

```bash
kuali --profile sandbox auth status --output json --quiet
kuali --profile sandbox apps list --search "App Name" --all --output json --quiet
```

Do not use typed MCP mutation tools for sandbox work while the MCP is pointed at prod/default.

## Environment Check

Before mutation:

```bash
kuali --profile sandbox auth status --output json --quiet
kuali --profile default auth status --output json --quiet
kuali --profile sandbox apps list --search "App Name" --all --output json --quiet
```

Confirm target profile and app ID in the response.

Avoid `kuali_run "smoke"` as a harmless connectivity check. It creates an app, updates a form, publishes it, creates/submits a document, then cleans up. Use `auth status`, app list, or other read-only probes instead.

## Existing App Inspection Flow

```bash
kuali --profile PROFILE apps list --search "Name" --all --output json --quiet
kuali --profile PROFILE apps get APP_ID --output json --quiet
kuali --profile PROFILE forms outline APP_ID --output json --quiet
kuali --profile PROFILE forms list --app APP_ID --output json --quiet
kuali --profile PROFILE forms get-template APP_ID --output json --quiet
kuali --profile PROFILE permissions list --app APP_ID --output json --quiet
```

## Sandbox Build Capability Probe

Use this read-mostly sequence when exploring what Kuali Build can do in sandbox:

```bash
kuali --profile sandbox auth status --output json --quiet
kuali --profile sandbox apps list --limit 10 --output json --quiet
kuali --profile sandbox apps list --all --output json --quiet
kuali --profile sandbox apps get APP_ID --output json --quiet
kuali --profile sandbox forms outline APP_ID --output json --quiet
kuali --profile sandbox forms list --app APP_ID --output json --quiet
kuali --profile sandbox forms get-template APP_ID --output json --quiet
kuali --profile sandbox permissions list --app APP_ID --output json --quiet
kuali --profile sandbox documents list --app APP_ID --limit 5 --output json --quiet
kuali --profile sandbox workflows actions --app APP_ID --limit 5 --output json --quiet
kuali --profile sandbox groups list --limit 10 --output json --quiet
kuali --profile sandbox integrations list --limit 10 --output json --quiet
kuali --profile sandbox categories list --limit 10 --output json --quiet
```

Useful safe previews:

```bash
kuali --profile sandbox apps create --name "Probe Name" --dry-run --output json --quiet
kuali --profile sandbox forms update --app APP_ID --data @template.json --skip-validation --dry-run --output json --quiet
kuali --profile sandbox documents create --form APP_ID --data '{}' --dry-run --output json --quiet
```

`--dry-run` previews intent for app creation, form update, and document creation without saving.

Primary workflow may require GraphQL:

```bash
KUALI_API_URL="https://your-tenant.kualibuild.com"
KUALI_BEARER_TOKEN="<token-from-your-secure-store>"
curl -sS -X POST "${KUALI_API_URL}/app/api/v0/graphql" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer ${KUALI_BEARER_TOKEN}" \
  --data '{"query":"query($id: ID!) { app(id: $id) { id name workflow } }","variables":{"id":"APP_ID"}}'
```

For Build apps, `workflows list --app APP_ID` is for secondary workflows and may not expose the primary workflow. Use `workflows actions --app APP_ID` for pending tasks and GraphQL `app(id){workflow}` for the primary workflow definition.

Primary workflow summary example:

```bash
jq '{name:.data.app.workflow.name,status:.data.app.workflow.status,stepCount:(.data.app.workflow.steps|length),steps:(.data.app.workflow.steps|map({id:._id,type,stepName,assigneeType:(.assignee.type? // .assigneeType?),subject}))}' workflow.json
```

## Copying App Shape

- `apps create --form` may create only the shell depending on template shape.
- Always validate form outline after creation.
- If form body does not land, use `forms update --skip-validation` for round-tripped Kuali templates that contain legacy/display gadgets.
- Workflow is separate from form. Copy/update workflow separately and validate saved steps.

## Validation After Mutation

Read back:

- app details
- form outline
- form schema/list
- workflow
- permissions

Do not call a mutation successful until Kuali returns the expected saved state.
