# App Design Standards

Use this when designing or improving Kuali form structure.

## Form Principles

- Start with a short title and plain-language purpose.
- Put submitter/student/requester identity near the top.
- Group fields by the user's mental model, not by backend ownership.
- Shape the default path first. Make the common path obvious, then expose exception paths only when they are selected or required.
- Prefer structured fields for reporting and routing.
- Avoid collecting data that does not affect routing, approval, reporting, completion, audit, or communication.
- Make required fields truly required; do not require internal fields from submitters.
- Use help text where users commonly misunderstand eligibility, timing, or next steps.
- Keep office-use sections visually and permission-wise distinct from submitter sections.
- For public-facing language, check official CSUB.edu sources when available so labels, help text, office names, contacts, and links match what users already see outside Kuali.

## Standard Section Patterns

- Title and instructions
- Requester/student information
- Academic/program/department context
- Request or agreement details
- Policy acknowledgment or justification
- Attachments, if needed
- Student/requester certification
- Office-use processing
- Reviewer/approver comments

## Kuali-Native UX Patterns

- Use conditional visibility for clean branches, not for every possible combination.
- Use packages or guided choices to reduce decisions before exposing large checkbox groups.
- Use fixed read-only package output for common paths; avoid pretending Kuali can generate a fully dynamic cart summary without an integration.
- Use final review sections to restate key selected fields, not to compute prose.
- Use task-specific section permissions so each reviewer sees the request context, their relevant details, and their decision/signature fields.
- Use `meta.submittedAt` for post-submit-only sections, employee acknowledgements, and internal processing fields.
- Use email notifications to carry some summary/status burden after submission.

## When To Stop Pushing Kuali UI

Avoid overbuilding inside Kuali when the desired experience requires:

- Looping over arbitrary selections.
- Computed narrative summaries.
- Dynamic reviewer lists shown as generated text.
- Cart-style add/remove behavior.
- Complex dependency logic for every access combination.

When those are required, either simplify the form to fixed packages and exception sections or propose a small integration that returns read-only summary fields.

## Field Naming

- Labels should make sense in exports without the surrounding form.
- Use specific names: `Decision Date`, `Denial Reason`, `Workshop Completion Method`.
- Avoid vague labels: `Other`, `Date`, `Comments`, unless context is unmistakable.
- When a field controls routing or email text, note that dependency in the blueprint.

## Quality Check

Before mutation, ask:

- Would a first-time student or staff member know what to do?
- Can the office process the request from the captured fields?
- Is the default path excellent before polishing rare exceptions?
- Are reporting/export columns understandable?
- Are workflow-required fields visible and editable at the step where they are needed?
- Are hidden or office-use fields protected from submitter edits?
- Are we using Kuali's strengths, or fighting it to behave like a custom web app?
- If the form references policy, deadlines, office contacts, or public instructions, did we verify those against current CSUB.edu sources and cite the source in the blueprint?
