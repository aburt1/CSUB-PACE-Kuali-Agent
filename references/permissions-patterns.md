# Permissions Patterns

Use this when designing or comparing Kuali app permissions.

## Permission Questions

- Who can submit?
- Who can view submitted requests?
- Who can edit drafts?
- Who can edit after submission?
- Who can approve, review, or complete tasks?
- Who can administer the app?
- Who can export or report?

## Defaults

- Use least privilege.
- In student-facing forms, `All Authenticated Users` often needs create access, but verify the business process first.
- Anonymous access should usually have no actions unless the app is intentionally public.
- Administer should be limited to app owners and support staff.
- Read/update should go to processing roles, not necessarily all admins.

## Reference Adaptation

- Reference permissions are a pattern, not a set of identities to copy.
- Map prod roles/groups to target-environment equivalents.
- If the equivalent group is missing in sandbox, document the gap and use a sandbox tester only for testing.
- Never broaden access just because the reference app is broad.

## Validation

After changes, read permissions back and summarize:

- Admin policy groups
- Submitter access
- Processor/reviewer access
- Anonymous access
- Any sandbox-only mappings
