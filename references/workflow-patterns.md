# Workflow Patterns

Use this when designing routing, approvals, tasks, send-back, denial, completion, reminders, or branch logic.

## Workflow Principles

- Keep approval chains short.
- Use conditional routing only when it changes the actual work.
- Prefer stable groups/roles over named people in production.
- Named-person assignment is acceptable for sandbox testing when clearly labeled.
- Define what happens on approve, deny, send-back, correction, and completion.
- Ensure workflow-required fields are editable at the step that needs them.

## Approval Matrix

```markdown
| Step | Type | Trigger | Assignee | Action | Outcomes | Email | Send-back | Edit/View Rights | Notes |
```

## Common Patterns

**Simple review**
- Submitter submits.
- Office review task.
- Approved/denied notification.
- Office record notification.

**Send-back enabled review**
- Reviewer can return for corrections.
- Send-back email includes the comment and exact next steps.
- Submitter resubmits into the same review path.

**Branch by decision**
- Decision field controls approved/denied path.
- Denial reason field is required only when denied.
- Approval and denial emails use different subject/body text.

**Office completion task**
- Use when approval is not the end of the work.
- Capture completion notes or completion date only if useful for audit/reporting.

**Submitted on behalf**
- Treat "submitted for self" and "submitted on behalf" as different workflow paths when assignees depend on the employee, not the initiator.
- Use the submit-on-behalf checkbox to branch before Manager/MPP review.
- For self-submitted requests, route Manager/MPP review to the submitter's system-found manager unless a manual manager override is checked.
- For on-behalf requests, route Manager/MPP review to the selected employee's system-found manager unless a manual manager override is checked.
- If the employee must acknowledge a request submitted by someone else, add an employee task before Manager/MPP review and assign it to the selected employee field.

**Post-submission employee signature**
- When a signature should not block the initial submitter, use visibility rules with `meta.submittedAt`.
- Example pattern: self-submit requestor signature is visible/required when the submit-on-behalf checkbox is empty.
- Example pattern: employee acknowledgement signature is visible/required when submit-on-behalf is checked and `meta.submittedAt` is not empty.
- In the employee acknowledgement task, make only the employee signature section editable; keep request details view-only and office review sections hidden.
- Validate the saved form and workflow together. A required signature hidden during initial submission can still be valid if it only becomes visible after submission for the assigned task.

## Sandbox/Prod Mapping

If a production role/group does not exist in sandbox:

- Do not silently drop the assignee.
- Map to a named sandbox tester only after saying so.
- Keep the production role in the proposed final design.
- Validate the saved workflow, because invalid assignee shapes may be accepted but saved empty.
