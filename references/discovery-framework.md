# Discovery Framework

Use this reference only while auditing a brief or selecting the next question.

## Decision Ledger

Maintain this structure privately and update it after every user response:

```md
## Confirmed
- ...

## Assumptions
- ...

## Contradictions
- ...

## Open high-impact decisions
- ...

## Deferred low-impact decisions
- ...
```

Do not show the whole ledger every turn. Summarize it when discovery ends or when a contradiction requires a decision.

## One-question protocol

Each discovery response must ask one primary question only.

Recommended format:

```md
[What is already understood and why this decision matters.]

[Single question?]

A. ...
B. ...
C. ...

Recommended: B — [brief reason].
```

Options are optional. Never hide multiple questions in one sentence with “and”. Do not ask “Anything else?” as a substitute for design leadership.

## Question-selection algorithm

1. Parse the proposal and prior answers.
2. Remove all resolved dimensions.
3. Identify contradictions and assumptions.
4. Score each unresolved dimension from 1–5:
   - user impact
   - scope impact
   - cost of changing later
   - uncertainty
5. Multiply the four values.
6. Ask the highest-scoring question.
7. After the answer, update the ledger and repeat.
8. Stop when no unresolved item has both high impact and high uncertainty.

## Adaptive question bank

These are prompts to select from, not a questionnaire to send.

### Product surface

- Is this primarily a marketing website, a working web application, a mobile-first app experience, a dashboard, or a hybrid?
- Should the web version behave like a full product or mainly present/download the native app?
- Is installation as a PWA part of the intended experience?

### Audience and job

- Who is the primary user in the first complete journey?
- What must that user accomplish successfully in one session?
- Which user group creates value, and which user group consumes it?

### Flow

- What is the single most important start-to-finish workflow?
- What should happen immediately after the primary call to action?
- Does the user need to return later and continue previous work?

### Account and permissions

- Can users browse or act without an account?
- Are there separate customer, provider, operator, manager, or administrator roles?
- Which actions need approval, payment, verification, or moderation?

### Scope and phases

- What must work in the MVP for the product to be useful rather than merely demonstrable?
- Which features are essential now, valuable later, or experimental?
- Should the first phase optimize for validation, launch speed, operational completeness, or visual impact?

### Information architecture

- Which content or task deserves the home screen?
- What should always be reachable from global navigation?
- Which features belong in settings rather than the primary flow?

### Brand and aesthetics

- Which three adjectives should describe the product, and which three should never describe it?
- Are there existing logo, colors, typography, photography, or brand rules?
- Should the design feel calm, premium, technical, playful, editorial, sporty, institutional, or something else?
- Which existing products are useful references, and what exactly should or should not be borrowed?
- Does the user want to define a visual direction in their own words rather than select from suggested styles?
- Which colors, materials, environments, cultural references, or visual metaphors should seed a new custom direction?

### Content and language

- Is real production copy available, or should interface copy be created?
- Which languages and writing directions are required?
- Are dates, currency, phone numbers, addresses, and units locale-specific?

### Data and integrations

- Is the interface driven by real APIs, mock data, CMS content, or static content?
- Which external services affect the flow: maps, payment, email, chat, analytics, media, AI, or identity?
- Are there data-dense screens requiring tables, charts, export, or bulk operations?

### Motion and 3D

- Does motion need to explain a process, establish brand character, or simply add polish?
- Would a 3D object demonstrate the product, or would it be decorative overhead?
- What performance devices or network conditions must be supported?

### Delivery

- Is the output a visual prototype, production-ready frontend, design reference, or all three?
- Will the prototype be standalone static HTML or integrated into an existing HTML/Tailwind repository?
- Which JavaScript behavior libraries, Tailwind plugins, icon sets, or asset sources are allowed or prohibited?

## Helping users form ideas

When the user has no answer:

1. infer two or three plausible directions from the domain
2. explain the consequences of each in concrete product terms
3. recommend one
4. ask for acceptance, combination, or a different user-defined direction as a single question

Example:

```md
For a fitness service, there are three viable home-screen models:

A. Booking-first — fastest path to finding and reserving a trainer.
B. Progress-first — retention-oriented dashboard for existing members.
C. Content-first — acquisition through programs and education.

Recommended: A for the MVP because it proves the core transaction.

Which model should define the first release, or is there a different model you want to describe?
```

## Discovery stopping conditions

End discovery when these are known or safely assumed:

- product surface
- primary audience
- core flow
- MVP boundary
- page/screen family
- visual personality
- implementation constraints

Do not delay implementation for low-impact decisions such as exact icon family, minor radius values, or final marketing wording.
