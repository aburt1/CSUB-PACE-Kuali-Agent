# Reference Adaptation Rules

Use this when a user asks to use an existing Kuali app as a reference, template, model, example, or quality bar.

## Intent Types

**Design reference**
- Borrow clarity, pacing, section order, label quality, help text style, and overall polish.
- Do not copy concrete fields or workflow artifacts unless they independently fit the target process.

**Pattern reference**
- Borrow reusable patterns such as send-back communication, final notification structure, office-use separation, approval matrix style, and permission discipline.
- Rewrite all patterns for the target process.

**Functional copy**
- Copy concrete fields, workflow steps, assignees, permissions, integrations, or email text only when explicitly requested or approved.

## Adaptation Map

Before mutation, produce:

```markdown
Reference intent:

Borrow:
- 

Adapt:
- 

Keep:
- 

Do Not Copy:
- 

Risks / Unknowns:
- 

Proposed changes:
- Form:
- Workflow:
- Emails:
- Permissions:
- Testing:
```

## Guardrails

- Reference fields are process-specific until proven reusable.
- Reference signatures are evidence requirements, not design decoration.
- Reference integrations must be verified in the target environment.
- Reference permissions should inspire a target permission model, not identity copying.
- Reference emails must be rewritten so the action, promise, recipient, and status match the target workflow.
- Reference workflow routing must be checked against target fields and merge variables.
- Reference policy text, eligibility rules, deadlines, and academic/regulatory language must be verified against the target process and current CSUB sources before reuse.

## Known Failure Case

Observed: The agent copied a process-specific office signature from a reference app into a target app.

Rule: A reference form's signatures, attestations, and processing fields do not transfer unless the target process independently requires that evidence.

Better behavior: Borrow the reference app's clear intro, requester identity layout, office-use separation, send-back pattern, final notification clarity, and permission discipline. Do not copy reference-specific fields, durations, dates, signatures, assignees, or policy text into the target by default.
