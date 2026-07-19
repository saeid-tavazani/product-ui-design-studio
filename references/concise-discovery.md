# Concise Discovery

Use this reference whenever asking questions, summarizing decisions, or presenting options.

Source anchor:

- https://github.com/JuliusBrussee/caveman

## Responsibility

Borrow the useful part of caveman-style communication: fewer words, same technical substance, no filler. Keep the user's language. Do not turn the product conversation into a gimmick.

## Rules

- Ask one primary question per message.
- Start with one short observation when it helps the user orient.
- Offer two to five options only when choices reduce ambiguity.
- Mark one option as recommended when momentum matters.
- Include a free-form path when options are shown.
- Remove pleasantries, repeated caveats, and status padding.
- Keep exact product names, technical terms, commands, routes, filenames, errors, and code unchanged.
- Use full clarity for risk, destructive choices, payments, privacy, compliance, safety, and legal issues.
- Continue with assumptions when the question would not materially improve output.

## Question Shape

Good:

```text
The core user seems to be a busy clinic manager, so navigation density matters.
Which primary device should lead the design: mobile-first, desktop-first, or adaptive? Recommended: desktop-first if daily operations happen at a desk.
```

Weak:

```text
I have many questions before I can begin. What is the audience? What pages do you want? What colors do you like? What competitors matter? What should the dashboard show?
```

## Decision Summary Shape

Use short records:

```md
Confirmed:
- Primary audience: clinic managers
- First flow: schedule review to appointment action

Assumptions:
- Desktop-first because workflow is operational
- Mobile supports quick status checks

Next:
- Build route inventory and visual directions
```

## Stop Asking When

- the missing answer is low-risk
- the user provided enough proposal detail
- the question would only refine taste, not structure
- a clear default can be documented and revised later
