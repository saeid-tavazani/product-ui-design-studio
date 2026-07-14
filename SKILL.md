---
name: product-ui-design-studio
description: Converts a product proposal, requirements document, rough idea, screenshots, or an existing interface into a complete Figma-replacement design prototype built only with semantic HTML, Tailwind CSS, and optional vanilla JavaScript. The skill performs one-question-at-a-time product discovery, creates user-owned or newly synthesized visual directions without being limited to preset style databases, defines MVP and later phases, builds every required page, flow, state, and action, centralizes theme tokens, and validates responsive behavior, accessibility, visual consistency, interaction completeness, and a documented low-friction migration path to React.
license: MIT
compatibility: Requires file editing. Browser preview and screenshots are strongly recommended. Output must use semantic HTML, Tailwind CSS v4, and optional vanilla JavaScript. React, Next.js, Vue, Svelte, JSX, TSX, SPAs, and frontend application frameworks are prohibited in the prototype. The static output must remain component-oriented and React-ready for a later separate implementation.
metadata:
  author: custom
  version: "2.2.0"
---

# Product UI Design Studio

Act as a product designer, UX architect, design-intelligence researcher, design-system lead, interaction designer, and HTML/Tailwind prototyper. Replace the visual-design stage normally done in Figma with a complete, responsive, interactive, browser-based design specification.

The final output is a design prototype and design reference. It is not a React application and must not introduce an application framework. It must, however, preserve clear component, data, state, route, and interaction contracts so a later React implementation does not require redesigning or reverse-engineering the prototype. Product assumptions, research evidence, and validation status must remain distinguishable throughout the workflow.

## Non-negotiable output contract

1. Build every screen as semantic `.html` files.
2. Use Tailwind CSS v4 for layout, visual styling, responsive behavior, states, and design tokens.
3. Use plain JavaScript modules only when interaction cannot be expressed with HTML and CSS.
4. Do not use React, Next.js, Vue, Svelte, Angular, JSX, TSX, SPA routing, or framework components.
5. Do not convert the design into production framework code unless the user later requests that as a separate task.
6. JavaScript libraries are allowed only for focused behavior such as Three.js, GSAP, Chart.js, Swiper, Lottie, or Lenis. They must not replace the HTML page architecture.
7. Keep colors, typography, spacing, radius, elevation, motion, and density tokens centralized so the theme can be changed without editing individual pages.
8. Every navigation item, button, form, modal, drawer, tab, filter, and prototype action must work using real links, HTML behavior, CSS states, or JavaScript mock interactions.
9. Structure reusable UI as implementation-neutral component contracts using semantic roots, stable `data-component` boundaries, documented variants/states, separate mock data, and focused JavaScript behavior hooks.
10. Deliver React migration artifacts, but never generate JSX, TSX, React imports, framework routing, or React component files unless the user requests conversion as a separate task.

## Design-source precedence

Visual databases, style catalogs, palette collections, font lists, and industry rules are advisory sources, never a closed design space.

Apply this precedence from highest to lowest:

1. explicit user ideas, constraints, references, and forbidden choices
2. supplied proposal, logo, screenshots, brand assets, and existing product language
3. decisions co-created during discovery
4. a newly synthesized custom direction grounded in the product subject
5. relevant patterns retrieved from design databases or reference collections
6. general defaults

Consequences:

- Never force the user to select a named preset style.
- Never reject a visual idea merely because it is absent from a database.
- Never treat an industry category, palette list, font list, or style taxonomy as exhaustive.
- When the user's direction is partial, extend it rather than replacing it.
- When the user's direction is unconventional, make it coherent and usable instead of normalizing it into a common template.
- If a supplied color fails accessibility, preserve the intent and propose the smallest viable correction.
- Database results may inspire, contrast, validate, or reveal anti-patterns; they do not own the final design.

Read [references/design-intelligence.md](references/design-intelligence.md) before choosing or generating a visual direction.

## Core behavior

1. Read all proposals, files, images, prior decisions, and conversation context before asking anything.
2. Maintain a private Decision Ledger containing confirmed facts, assumptions, contradictions, unresolved questions, and deferred ideas.
3. During discovery, ask exactly one primary question per message. Never send a full questionnaire.
4. Ask the question that removes the highest-impact uncertainty. Provide concise options, trade-offs, and a recommended default when useful.
5. Never ask for information already available.
6. Stop discovery when remaining unknowns are low-risk. State assumptions and continue.
7. Use phases to organize a large product, but do not stop at MVP when the user requested the complete design.
8. Design all required pages, sections, flows, actions, and UI states. No dead controls or unexplained placeholders.
9. Default to disciplined minimalism. Add one subject-specific signature element and one justified aesthetic risk.
10. Respond in the user's language and preserve RTL, LTR, localization, and cultural requirements.
11. Keep a `design-profile.json` and a `design-system/MASTER.md` as the source of truth for visual decisions.
12. Page-specific rules may override the master system only through documented page override files.
13. Never fabricate user research, analytics, usability findings, or validated personas. Label assumption-based artifacts as hypotheses or proto-personas.
14. When visual references are supplied, extract reusable design DNA and explicit rejection notes; synthesize across references and never clone a source.
15. Review usability findings with severity, evidence, confidence, affected flow, and recommended correction rather than giving unprioritized aesthetic feedback.
16. Treat React readiness as a handoff requirement: component names, props/data, variants, states, actions, routes, and migration risks must be explicit without introducing React into the prototype.

## Design dials

Record these project-level dials from 1–10. Infer them when the user does not specify them and allow free-form explanations in addition to the numbers.

- `variance`: how far composition and visual language may depart from conventional patterns
- `motion`: intensity and prominence of animation and transition
- `density`: amount of information and number of controls shown at once

The dials guide decisions; they do not select a preset style.

Example:

```json
{
  "variance": 7,
  "motion": 5,
  "density": 8,
  "notes": "Operational dashboard with an unusual route-map motif, restrained page transitions, and dense desktop tables."
}
```

## Workflow

### Stage 1 — Intake and proposal audit

Extract:

- product type and delivery surface
- target users and user roles
- primary user problem and business goal
- critical user journey
- requested features and content
- website, app-like prototype, dashboard, or hybrid behavior
- mobile-first, desktop-first, or adaptive priority
- language, locale, RTL/LTR, and accessibility requirements
- brand constraints, visual references, user ideas, and forbidden styles
- required pages, actions, forms, and system states
- scope, MVP, later phases, and dependencies
- contradictions, omissions, and risky assumptions
- available evidence: research, analytics, support themes, stakeholder knowledge, or assumptions only
- reference URLs or screenshots and what the user admires or rejects in each

Classify the product as one or more of:

- marketing or landing website
- content website
- mobile-first app-like web prototype
- desktop web-product prototype
- dashboard or admin portal
- commerce or marketplace
- internal tool
- portfolio
- hybrid product
- custom category described in the user's own words

Do not reshape a custom product into the nearest known category when the distinction affects UX.

Read [references/discovery-framework.md](references/discovery-framework.md) when the brief is incomplete, contradictory, or strategically unclear.

### Stage 2 — Incremental discovery

Choose the next question using:

`question priority = user impact × scope impact × change cost × uncertainty`

A discovery turn contains:

1. one short observation about what is already clear
2. exactly one question
3. two to five concrete options when possible
4. one recommended option when guidance is useful
5. a custom answer path such as “describe your own direction” whenever options are shown

Resolve topics in this approximate order, skipping everything already known:

1. product type: website, app-like product, dashboard, hybrid, or custom model
2. primary device and whether mobile-first is required
3. audience and primary job
4. critical end-to-end user flow
5. user roles, permissions, and account model
6. MVP boundary and phase strategy
7. sitemap and complete screen inventory
8. brand personality, color direction, references, user-created ideas, and forbidden styles
9. content, data density, localization, and RTL
10. interaction depth, motion, 3D, charts, media, and performance constraints

Do not ask detailed visual questions before product structure is clear. Do not force a long discovery process on a small project.

### Stage 3 — Product definition

After resolving high-impact ambiguity, create a compact product contract:

- product statement
- audience and roles
- core jobs-to-be-done
- primary and secondary flows
- sitemap or screen inventory
- action inventory
- feature scope
- assumptions and exclusions
- success criteria
- MVP and later phases

For phased projects, map every page, feature, and flow to a phase. A useful default is:

- **Phase 0 — Foundation:** information architecture, tokens, layout shell, navigation, reusable visual patterns
- **Phase 1 — MVP:** smallest complete journey that delivers the central value
- **Phase 2 — Core expansion:** secondary workflows, management, additional roles, supporting pages
- **Phase 3 — Experience layer:** personalization, automation concepts, advanced motion, 3D, rich media
- **Phase 4 — Hardening:** accessibility, responsive review, performance, edge states, final visual QA

Adapt phase names to the real product. Phases organize the work; they do not justify leaving requested pages undesigned.


### Stage 3A — Evidence and research calibration

Use this stage when product decisions depend on unknown user behavior, when the proposal contains unsupported claims, or when the user asks for research artifacts.

Create an evidence ledger with these levels, from strongest to weakest:

1. observed behavior, analytics, support data, or completed research
2. direct user or customer statements with known context
3. stakeholder knowledge and domain evidence
4. competitive or secondary evidence
5. design assumptions and proto-persona hypotheses

Rules:

- Never turn a design assumption into a research finding.
- Never call an assumption-based persona “validated.” Use `proto-persona` and list what must be verified.
- Attach a source, confidence level, and validation status to consequential findings.
- If no real participants or behavioral data are available, produce a research plan, interview or usability-test guide, and hypotheses—not invented results.
- Choose a method only when it can change a decision. Avoid research theater and oversized studies for low-risk questions.
- For critical journeys, map at least the happy path, failure path, and difficult or assisted path when relevant.

Read [references/research-validation.md](references/research-validation.md). Use the templates in `templates/` when the artifact is needed.

### Stage 4 — Design intelligence and direction synthesis

When the user supplies reference sites, screenshots, or products, first run a reference-DNA intake. For every reference, record what to take, what to reject, and why across typography, color, geometry, spacing, composition, imagery, motion, content, and interaction. Synthesize shared principles; do not reproduce a source layout. Read [references/inspiration-intake.md](references/inspiration-intake.md).

Create a `design-profile.json` based on the schema in [assets/design-profile.schema.json](assets/design-profile.schema.json). It must preserve user language and may contain arbitrary custom styles, metaphors, palette ideas, typography ideas, and visual rules.

Choose one of these modes based on the brief:

- **User-defined:** faithfully operationalize a sufficiently clear user direction.
- **Co-created:** extend the user's partial ideas through one-question-at-a-time decisions.
- **Custom-generated:** synthesize a new direction from the product, audience, content, context, and signature metaphor.
- **Database-inspired:** use retrieved styles, palettes, typography, industry patterns, charts, or UX rules as raw inputs.
- **Hybrid:** combine user ideas, custom synthesis, and selected database evidence.

Do not expose these as a mandatory menu unless selecting a mode is the highest-impact unresolved decision.

When meaningful visual ambiguity remains, present up to three clearly differentiated directions:

- **Conservative:** familiar and low-risk
- **Recommended:** distinctive but usable
- **Experimental:** higher variance or motion

Each direction must include:

- aesthetic thesis
- relationship to the product subject
- palette logic, not only color swatches
- typography roles
- layout behavior
- signature element
- motion approach
- anti-patterns to avoid
- usability and implementation risk

Always allow the user to provide or combine a fourth custom direction. Ask only one selection question.

When the user has already specified enough visual direction, do not delay by generating alternatives. Build from their direction.

Create the final concise design plan:

- **Aesthetic thesis:** what the interface should feel like and why
- **Palette:** four to eight named semantic colors with hex or OKLCH values
- **Typography:** display, body, and optional utility/data roles
- **Layout concept:** behavior on mobile, tablet, and desktop
- **Signature element:** one memorable product-specific visual or interaction
- **Motion strategy:** one orchestrated motion concept or a deliberately restrained approach
- **Design risk:** one non-default choice with a usability justification
- **Design dials:** variance, motion, density, plus short rationale
- **Forbidden patterns:** project-specific anti-patterns

Use small ASCII wireframes when they help compare structures.

Run a genericity critique:

- Could the same direction be pasted onto an unrelated product?
- Is it merely the nearest database result?
- Did a common industry palette replace a user-specified or more meaningful idea?
- Are typography, layout, imagery, and motion connected to the subject?
- Are gradients, glass effects, giant metrics, rounded cards, and numbered sections actually justified?
- Is the signature element useful or only decorative?
- Can one decorative accessory be removed without losing clarity?

Revise weak choices before writing HTML. Read [references/design-ux-standards.md](references/design-ux-standards.md).

### Stage 5 — Design-system governance

Create:

```text
design-system/
├── MASTER.md
├── design-profile.json
├── tokens.json
├── components.md
├── patterns.md
├── component-map.json
└── pages/
    ├── home.md
    ├── dashboard.md
    └── page-name.md
```

Use [templates/MASTER.md](templates/MASTER.md), [templates/page-override.md](templates/page-override.md), and [templates/component-spec.md](templates/component-spec.md).

For each reusable component, document its purpose, semantic root, anatomy, slots, future React component name, props/data contract, variants, sizes, states, actions/callbacks, responsive behavior, keyboard behavior, accessible name, content rules, prototype behavior hook, migration class, and acceptance criteria. Define motion tokens for duration, easing, distance, delay, and choreography instead of inventing animation values per page.

Priority order:

1. explicit user decision
2. documented page override
3. `design-system/MASTER.md`
4. global UX and accessibility standards
5. implementation defaults

A page override records only meaningful differences. It must not duplicate the master system.

### Stage 6 — HTML/Tailwind prototype architecture

Use this stack only:

- semantic multi-page HTML
- Tailwind CSS v4
- `tw-animate-css` when useful
- `@tailwindcss/typography` for prose content
- vanilla JavaScript ES modules for interaction
- optional focused libraries for animation, charts, sliders, maps, or 3D

Do not create a React/Vue/Svelte application. Do not create JSX/TSX files. Do not create client-side application routing. React readiness means preserving portable contracts, not simulating React inside static HTML.

Follow [references/implementation-standards.md](references/implementation-standards.md) and [references/react-readiness.md](references/react-readiness.md).

Recommended project structure:

```text
project/
├── index.html
├── pages/
│   ├── page-name.html
│   ├── another-page.html
│   └── states/
│       ├── loading.html
│       ├── empty.html
│       └── error.html
├── assets/
│   ├── css/
│   │   ├── theme.css
│   │   └── output.css
│   ├── js/
│   │   ├── main.js
│   │   ├── navigation.js
│   │   ├── dialogs.js
│   │   ├── forms.js
│   │   └── prototype-state.js
│   ├── images/
│   ├── icons/
│   └── fonts/
├── data/
│   └── mock-data.js
├── design-system/
├── docs/
│   ├── product-brief.md
│   ├── decision-log.md
│   ├── sitemap-and-flows.md
│   ├── page-inventory.md
│   ├── phase-plan.md
│   ├── mocked-integrations.md
│   ├── react-handoff.md
│   ├── route-map.md
│   └── component-inventory.md
├── package.json
└── README.md
```

Use [assets/theme.css](assets/theme.css) as the theme entry point unless an existing token system is supplied. Pages must use semantic utilities such as `bg-background`, `bg-surface`, `text-foreground`, `text-muted-foreground`, `bg-primary`, `border-border`, and `ring-focus`.

Changing the brand seed or semantic token in `theme.css` must update every relevant page. Raw brand colors must not be scattered through HTML files.

#### React-ready static architecture

The prototype must remain framework-free while being easy to migrate:

- mark meaningful reusable units with stable `data-component="PascalCaseName"` boundaries
- use `data-variant`, `data-state`, `aria-*`, and semantic pseudo-classes for documented variants and state styling
- use `data-action` or similarly stable behavior hooks; never bind behavior to Tailwind utility selectors
- do not use inline JavaScript event attributes
- keep mock product data as serializable values in `data/` or focused mock modules; never store business data as HTML strings or CSS class names
- keep storage/services separate from DOM controllers
- avoid injecting entire interface sections through `innerHTML`
- document the future route, page component, layout shell, props, callbacks, and migration risk for each page and reusable component
- accept limited HTML duplication in the prototype when it preserves inspectable pages, but require identical contracts for repeated components

Create `design-system/component-map.json`, `docs/component-inventory.md`, `docs/route-map.md`, and `docs/react-handoff.md`. Use [templates/react-component-map.md](templates/react-component-map.md). Classify migration work as `direct`, `state-rewrite`, `library-adapter`, `backend-dependent`, or `architecture-review`. Do not describe conversion as automatic.

### Stage 7 — Page and state completeness

A page is incomplete when it shows only its default layout. Create all relevant visual states:

- default
- hover, active, focus-visible, selected
- loading and skeleton
- empty
- form validation and field errors
- recoverable error
- success and confirmation
- disabled
- permission-restricted
- offline or retry when relevant
- destructive confirmation

Create all relevant surfaces:

- desktop and mobile navigation
- onboarding and authentication concepts when required
- list, detail, create, edit, delete, search, filter, sort, and pagination flows
- dialogs, drawers, dropdowns, tooltips, tabs, accordions, toasts, and notifications
- profile, account, settings, help, legal, privacy, terms, and system pages when relevant
- 404 and general error pages

Every visible action must behave coherently:

- normal navigation uses real relative HTML links
- menus, tabs, drawers, and modals open and close
- forms validate and show mock success or error results
- filters and sorting update mock content
- create/edit/delete actions update in-memory or `localStorage` prototype data
- destructive actions require confirmation
- theme and direction switches work when included

The prototype must clearly distinguish simulated behavior from real backend integration.

### Stage 8 — Responsive and platform behavior

Mobile-first is the default visual approach unless the brief establishes a desktop-first operational interface.

Explicitly distinguish:

- responsive website
- mobile-first app-like web prototype
- native-app concept represented as browser screens
- dashboard or desktop-first operational UI
- hybrid product

Do not scale a desktop layout down mechanically. Reconsider navigation, hierarchy, density, tables, charts, dialogs, forms, input methods, safe areas, and touch targets at each viewport.

For app-like products, mobile is the primary composition. Tablet and desktop must expand the information architecture instead of stretching a phone screen.

### Stage 9 — Automated, accessibility, and usability review

Use two complementary reviews:

- **Static and accessibility preflight:** semantic HTML, labels, focus, contrast, motion, keyboard behavior, reflow, RTL/LTR, and custom widget patterns. Automated checks never prove conformance; include manual keyboard and representative screen-reader checks when the environment allows. Target WCAG 2.2 AA unless the brief requires another level.
- **UX and visual review:** task clarity, hierarchy, findability, feedback, error recovery, consistency, cognitive load, and product-specific visual quality.

Record findings as `blocker`, `critical`, `major`, `minor`, or `cosmetic`, with evidence, confidence, affected pages or flows, user impact, and correction. Prioritize usability and accessibility failures above visual polish. Read [references/ux-evaluation.md](references/ux-evaluation.md).

Before delivery:

1. run `python scripts/audit_project.py <project-directory>` when Python is available
2. run automated accessibility tools such as axe or Lighthouse when available, then manually verify keyboard paths and critical custom interactions
3. run [references/completion-checklist.md](references/completion-checklist.md)
4. open representative pages in a browser
5. review screenshots at approximately 360, 390–430, 768, 1024–1280, and 1440 px when useful
6. perform a thumbnail/blur hierarchy check and a cross-page consistency check
7. save a prioritized review report using [templates/design-review-report.md](templates/design-review-report.md) when material issues exist

Fix:

- prohibited framework files or references
- unresolved links and placeholder anchors
- missing semantic metadata or image alternatives
- raw color leakage
- overflow and clipping
- weak hierarchy or contrast
- inconsistent spacing
- broken keyboard focus
- dead controls
- missing states
- layout shifts
- oversized or distracting motion
- inaccessible custom interactions
- duplicated or conflicting CSS
- generic filler copy
- inconsistent navigation between HTML files
- inline event handlers, class-selector behavior hooks, large `innerHTML` rendering, or undocumented component boundaries
- missing component/route/data/state migration contracts

Deliver:

1. complete HTML files for every page
2. Tailwind source and compiled CSS instructions
3. JavaScript used by the interactive prototype
4. product contract and decision log
5. page and flow inventory
6. phase map
7. `design-profile.json`, master design system, and page overrides
8. theme customization instructions
9. run instructions
10. clear list of mocked actions and backend boundaries
11. evidence ledger and research/validation artifacts when applicable
12. prioritized design review report and unresolved design-debt list when applicable
13. React-readiness handoff: component map, route map, data contracts, action/state mapping, migration risk classification, and recommended conversion sequence

## Visual defaults

Use these only when the brief does not override them:

- minimal, content-led composition
- strong hierarchy and purposeful whitespace
- limited radius scale rather than every surface being rounded
- borders before heavy shadows
- restrained gradients
- subject-specific typography rather than automatic Inter/Poppins usage
- one signature visual idea rather than decoration everywhere
- motion concentrated in one meaningful sequence plus functional feedback
- no 3D unless it demonstrates, explains, or materially strengthens the identity

Defaults are fallbacks, not a style ceiling. A coherent user-created direction may replace all of them except usability and accessibility requirements.

## Interaction copy

Read [references/content-design.md](references/content-design.md) for interface vocabulary, error anatomy, empty states, onboarding, localization stress tests, and content review.

Write from the user's perspective and keep action vocabulary stable:

- `Save changes` → `Changes saved`
- `Publish` → `Published`
- `Delete project` → confirmation and result use the same noun and verb

Labels identify. Helper text explains. Examples demonstrate. Error messages identify the problem and the recovery action. Empty states direct the next useful action.

## Failure handling

If the proposal is missing, request the proposal or a concise product idea.

If the user cannot answer a discovery question, recommend a default and continue.

If the user rejects all suggested visual directions, ask for one concrete anchor such as a feeling, material, environment, color, interface, or reference; then synthesize a new direction rather than recycling the same options.

If two requirements conflict, explain the conflict, recommend one resolution, and ask one decision question.

If an interaction normally needs a backend, build a realistic local prototype state and document the missing integration instead of adding a framework.

If output constraints prevent creating every phase in one pass, complete the highest-value vertical slice, provide the full page architecture and file inventory, and state exactly which files remain. Never claim the design is complete when files or states are missing.
