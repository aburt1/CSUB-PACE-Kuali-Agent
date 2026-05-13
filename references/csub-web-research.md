# CSUB.edu Web Research

Use this when a Kuali Build app design needs CSUB public-facing context, process language, policy framing, contact details, service ownership, or links.

## When To Search CSUB.edu

Search official CSUB sources when the app touches:

- Student-facing academic processes, forms, petitions, withdrawals, leave, academic standing, records, graduation, admissions, financial aid, or advising.
- Staff/faculty administrative services such as ITS, Payment Services, Procurement, Distribution Services, HR, Facilities, or department-specific forms.
- Policy-sensitive language, eligibility, deadlines, prerequisites, required documentation, or consequences.
- Public help text, intro language, confirmation emails, denial messages, or completion instructions.
- Office ownership, routing assumptions, contact emails, phone numbers, service pages, or published form links.

## Source Hierarchy

1. Kuali app JSON/configuration: source of truth for actual fields, workflow, notifications, permissions, integrations, and saved behavior.
2. Official CSUB.edu office/service pages: source of truth for public-facing instructions, ownership, contacts, and terminology.
3. CSUB catalog pages: source of truth for academic policy context, with catalog year/date checked before use.
4. CSUB PDFs and handbooks: useful supporting context, but check publication date and owning office.
5. Non-CSUB sources: do not use for CSUB process requirements unless the user explicitly asks.

Do not let a web page silently override the live Kuali app. If the two conflict, report the conflict and ask whether the form should align with the published page, the current Kuali behavior, or a new desired process.

## Search Patterns

Use targeted searches such as:

```text
site:csub.edu "Kuali Build" "forms"
site:csub.edu "Forms Gateway" "Kuali"
site:csub.edu "[process name]" "Kuali"
site:csub.edu "[process name]" "[owning office]"
site:csub.edu "[process name]" "CSUB"
site:csub.edu "Leave of Absence" "Registrar"
site:csub.edu "Registrar" "[policy or form name]"
site:catalog.csub.edu "[academic policy term]"
```

Prefer current HTML pages over older PDFs when both exist, unless the PDF is the official published policy or handbook.

## What To Extract

Capture concise, implementation-useful facts:

- Official process name and alternate names users may search for.
- Owning office and support contact.
- Who the process is for.
- Eligibility, prerequisites, deadlines, and required documentation.
- Published instructions users already see before opening Kuali.
- Status language and expected next steps.
- Links that should appear in form help text or emails.
- Contradictions between web content, Kuali config, and the requested redesign.

## How To Use The Findings

Use CSUB.edu findings to improve:

- Form title, description, section labels, help text, and acknowledgment language.
- Required-document guidance and attachment labels.
- Email subject lines, action wording, and contact blocks.
- Workflow role naming and office ownership assumptions.
- Testing checklists for policy-sensitive paths.
- Reporting fields that need consistent public terminology.

Do not copy long policy passages into a form or email by default. Summarize plainly and link to the official source when the policy is too detailed, likely to change, or owned by another office.

## Blueprint Citation Format

Include a short source section in app blueprints when web research was used:

```markdown
CSUB.edu sources referenced:
- [Page title](https://www.csub.edu/...) - used for office ownership/contact/help text.
- [Catalog policy](https://catalog.csub.edu/...) - used for policy context; confirm catalog year before launch.

Source-derived facts:
- [Fact]

Assumptions to confirm:
- [Assumption]
```

## Safety Rules

- Treat contact names, phone numbers, policy pages, and deadlines as drift-prone; verify them in the current turn before presenting them as current.
- Clearly label any unverified or older source.
- Never broaden permissions or change workflow routing from a web page alone.
- Never add a published contact as an approver unless the Kuali configuration or user confirms that routing.
- If a CSUB page links to a Kuali form, use the link as context, not as proof that the sandbox/prod app IDs match.
