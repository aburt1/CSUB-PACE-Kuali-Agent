# Email Patterns

Use this when drafting, reviewing, or adapting Kuali notification templates.

## Email Principles

- Emails are part of workflow design, not copywriting afterthoughts.
- Every email needs a trigger, recipient, purpose, required action, and "when not to send."
- Rewrite reference emails for the target process. Do not preserve promises that are not true for the target app.
- Include enough request details for triage without exposing unnecessary sensitive data.
- Use merge fields only after verifying they exist in the target form/schema.
- Distinguish task emails from notification emails. Task emails should explain the action inside Kuali; notification emails should carry the office signature/contact block.

## Default Tone

Professional, clear, helpful, brief, action-oriented.

## Default Structure

```markdown
Subject: [Action/status] - [Form/request name] - [Requester or record identifier]

Hello [Recipient Name],

[One sentence explaining what happened.]

[One sentence explaining what action is needed, if any.]

Request details:
- Request:
- Submitted by:
- Student/employee ID or department:
- Status:
- Due date, if applicable:

[Open the Kuali item.]

Thank you,
[Office or Team Name]
```

## Common Templates

**Submission confirmation**
- Recipient: submitter
- Trigger: form submitted
- Purpose: confirm receipt and set expectations
- Avoid: promising approval or completion before review

**Reviewer task**
- Recipient: reviewer/approver
- Trigger: workflow reaches review step
- Purpose: explain exactly what to inspect and complete
- Include: decision fields, editable sections, send-back guidance
- Use "View Task" language.
- Include a "Next Steps" section with access, review, send-back/feedback, and finalize instructions.
- Do not include a closing signature block in task emails unless the user explicitly asks for one.

**Send-back**
- Recipient: submitter
- Trigger: reviewer returns for correction
- Purpose: explain what to fix and how to resubmit
- Include: `{{workflow.sendbackComment}}` if available
- Include "Reason for Return" and a clear "Next Steps" list.
- Send-back emails are notifications, so include the office signature/contact block when the office owner is known.

**Denial**
- Recipient: submitter
- Trigger: denied path
- Purpose: state decision, reason, and next contact/next step
- Include: denial reason merge field only if that field exists and is required

**Completion/final**
- Recipient: submitter and/or record owner
- Trigger: workflow complete or processing complete
- Purpose: confirm the final state
- Avoid: saying a system update happened if the workflow only queues manual work
- Use formal notification language such as "We are pleased to inform you..." only when the request is actually complete or processed.
- Mention the form attachment only if Kuali is configured to attach the completed form.
- Include the full office signature/contact block for final notifications.

## CSUB Kuali Email Builder Pattern

Use this when the user asks for the CSUB-style Kuali email format:

- Initial submission acknowledgement: notification to initiator only; include office signature/contact.
- Approval/reviewer task: action-required subject, "View Task" or "Begin Review" wording as appropriate, "Next Steps", no closing signature.
- Task completion step: "View Task" wording, four-step "Next Steps", no closing signature.
- Send-back: "Reason for Return", structured "Next Steps", office signature/contact.
- Final notification: formal processed/completed tone, individual recipient emails when possible, office signature/contact.

Subject patterns:

- `Action Required: <FormName> for <SubmitterName> (CSUB ID: <SubmitterID>)`
- `Revisions Needed - <FormName>`
- `Notification - <FormName> Processed`
- `Confirmation of Submission - <FormName>`
