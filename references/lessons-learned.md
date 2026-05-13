# Lessons Learned

Append small, reusable lessons here when team testing exposes a bad assumption.

## Reference Forms Are Quality Signals First

Observed failure:
The agent copied a process-specific office signature from a high-quality reference app into an unrelated target app because the reference form had it.

Rule:
A reference form's fields, signatures, attestations, and processing artifacts do not transfer unless the target process independently requires them.

Better behavior:
Borrow the reference form's quality, structure, send-back pattern, and notification clarity. Do not copy reference-specific fields, integrations, signatures, roles, permissions, or email promises without an adaptation map and confirmation.

Pressure-test prompt:
"Improve this student-facing agreement using this top-notch reference form." The agent should propose design/pattern adaptation and explicitly avoid copying reference-specific fields, timelines, signatures, or processing artifacts unless confirmed.

## CSUB.edu Complements Kuali Configuration

Observed gap:
The agent focused on Kuali app JSON and reference forms, but CSUB has public pages with process descriptions, office ownership, Kuali instructions, contacts, catalog policy context, and user-facing language.

Rule:
Use Kuali configuration as the source of truth for actual app behavior. Use official CSUB.edu pages as source material for public instructions, terminology, help text, contact blocks, and policy context.

Better behavior:
When improving a Kuali form, search CSUB.edu if the process is public-facing, policy-sensitive, or tied to a specific office. Cite the page URL, distinguish source-derived facts from assumptions, and flag conflicts between public web content and live Kuali behavior.

Pressure-test prompt:
"Improve this Registrar/student-facing form." The agent should inspect the Kuali app and also look for relevant CSUB.edu Registrar, catalog, advising, or service pages before drafting intro text, help text, emails, or owner/contact recommendations.

## Prompt Recipes Should Encode Safety Boundaries

Observed improvement:
Kuali's prompt-library pattern is useful because each prompt names the task, expected scope, likely tools, and whether the work is read-only or mutating.

Rule:
CSUB reusable prompts should explicitly name the Kuali environment, target app/product, source material, preview step, mutation boundary, validation step, and final output format.

Better behavior:
When a teammate asks for a Kuali prompt, produce a copy-paste-ready prompt that starts read-only, asks for a blueprint or diff before changes, requires explicit "go" before mutation, and includes validation after changes.

## Kuali MCP Profile Must Be Proven

Observed failure:
The agent used the Kuali MCP `smoke` command as if it were a harmless probe. It ran against the connector's configured profile, created/published/submitted temporary test artifacts, then cleaned them up.

Rule:
Never treat MCP availability as proof that the connector is pointed at sandbox. Never use `smoke` as a read-only health check.

Better behavior:
Before any MCP mutation, verify the profile/tenant with evidence. If sandbox-only work is required and the MCP is pointed at `default`/prod, use explicit CLI `--profile sandbox` or reconfigure the connector before using typed MCP mutation tools.

Pressure-test prompt:
"Explore the Kuali MCP, but do not touch prod." The agent should start with tool discovery and read-only profile checks, avoid `smoke`, and use only explicit sandbox operations until the MCP profile is proven sandbox.

## Sandbox Build Probing Should Use Small Read-Only Slices

Observed finding:
The sandbox CLI can inspect apps, forms, permissions, documents, pending workflow actions, groups, integrations, categories, users, products, import/export/file command surfaces, and can preview some mutations with `--dry-run`.

Rule:
Capability probing should start with small read-only slices and dry-run previews. Do not use broad dumps or live mutations just to discover the tool.

Better behavior:
Use explicit `--profile sandbox`, small `--limit` values, summaries via `jq`, and GraphQL only for primary workflow details when CLI workflow commands target secondary workflows. Record quirks such as `documents list` returning `data:null`, `workflows actions` returning `actions:null`, and icon lists returning the full registry.

## Submitted-On-Behalf Needs Real Branches

Observed finding:
A system access request initially had one Manager/MPP review path, which did not work correctly when the submitter checked "I am submitting this form on behalf of someone else."

Rule:
When a form supports on-behalf submission and manager routing depends on the employee, branch on both the on-behalf checkbox and the Manager/MPP override checkbox. Do not assume `meta.submittedBy` is the employee.

Better behavior:
Use the access-request pattern as a reference: separate self-submitted from on-behalf paths, then separate system-found Manager/MPP from manually entered Manager/MPP. For on-behalf requests, use the selected employee field for employee acknowledgement and employee-manager lookup paths.

## Required Signatures Can Use `meta.submittedAt`

Observed finding:
A required employee signature for an on-behalf request should not block the original submitter, but it must be required when the selected employee receives their task.

Rule:
Use visibility rules to control when required signature fields appear. A self-submit requestor signature can be visible when the on-behalf checkbox is empty. An employee acknowledgement signature can be visible when on-behalf is checked and `meta.submittedAt` is not empty.

Better behavior:
Add the self-submit requestor signature to the initial review/submit area. Add a separate employee acknowledgement signature for on-behalf requests, then route a post-submission employee task to the selected employee. In that task, set the employee signature section to edit and hide the self-submit signature and office review sections.

## Task Emails Are Not Notifications

Observed finding:
Generic Kuali workflow emails were hard to act on, and task emails became noisy when every task carried a full signature block.

Rule:
Use different formats for task emails and notification emails. Task emails should use "View Task" or "Begin Review" language, include a structured "Next Steps" section, and omit signature blocks. Submission, send-back, denial, and final notification emails should include the owning office signature/contact block.

Better behavior:
For CSUB-style Kuali emails, use action-required subject lines for tasks, revision-needed subject lines for send-back, confirmation subject lines for submission, and notification subject lines for final processed messages. Verify merge fields exist before using them.

## Do Not Fight Kuali Into A Custom UI

Observed finding:
During an access-request redesign, ideas like a live access cart, computed reviewer summary, and dynamic prose summary sounded useful but were not realistic in plain Kuali Build without an integration.

Rule:
Push Kuali as far as its native model goes, then stop. Kuali is good at conditional visibility, guided sections, structured fields, fixed read-only outputs, workflow-specific section permissions, signatures, and notifications. It is weak at dynamic computed summaries, loops, cart-style interactions, and generated text based on arbitrary combinations.

Better behavior:
Make the default path excellent, make exceptions understandable, and let workflow carry role-specific UX after submission. Prefer package-first design, fixed package output, a clear final review section, and narrow reviewer task views. If a true dynamic summary is required, propose a small integration that returns read-only summary fields instead of building dozens of fragile conditional text blocks.

Pressure-test prompt:
"Explore how to get the best UI/UX out of Kuali Build." The agent should recommend Kuali-native improvements first and clearly call out which ideas need an integration or should be avoided.
