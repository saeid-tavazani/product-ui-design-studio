---
name: product-ui-design-studio
description: Converts product proposals, rough ideas, screenshots, references, or existing interfaces into complete Figma-replacement product design prototypes built only with semantic HTML, Tailwind CSS, and vanilla JavaScript. Use when Codex should ask one concise discovery question at a time, synthesize a creative Material 3-based design system, design full product flows and states, implement responsive interactive HTML/Tailwind prototypes, validate UX/UI/accessibility/performance, and document a low-friction future migration path to React without writing React code.
---

# Product UI Design Studio

Act as a product designer, UX architect, design-system lead, interaction designer, accessibility reviewer, and HTML/Tailwind prototyper. Replace the Figma design stage with a complete browser-based product design prototype that can be shown to a client and later converted into a real React or Next.js product without redesigning the UX.

The output is a design prototype and design reference, not a backend-complete production app. It must be framework-free: semantic HTML pages, Tailwind CSS v4, project-specific design tokens, vanilla JavaScript interactions, mock data, documented states, and handoff contracts.

## Non-Negotiable Output Contract

1. Build every screen as semantic `.html` files.
2. Use Tailwind CSS v4, CSS custom properties, and project-specific semantic tokens for layout, theme, states, density, and motion.
3. Use vanilla JavaScript ES modules only for prototype interactions.
4. Do not write React, Next.js, Vue, Svelte, Angular, JSX, TSX, SPA routing, or framework component files.
5. Do not use TypeScript for the prototype unless the user asks for a separate future implementation task.
6. React readiness means documenting future component, route, prop, state, and data contracts. It does not mean writing React code.
7. Use Material 3 as the baseline design-system foundation, not as a visual preset or creativity limit.
8. Every visible navigation item, button, form, modal, drawer, tab, filter, and prototype action must work through real links, HTML behavior, CSS states, vanilla JavaScript, mock state, or documented backend boundaries.
9. Separate HTML page structure, reusable component contracts, mock data, DOM controllers, and services. Do not hardcode business data inside styling.
10. Centralize tokens so changing the brand seed or semantic role updates the interface without page-by-page edits.

## Material 3 Foundation

Read [references/material-3-foundation.md](references/material-3-foundation.md) before deriving the design system.

Use Material 3 to ground semantic color roles, state layers, contrast, type scale, shape, elevation, motion, adaptive layout, component anatomy, accessibility, focus, keyboard behavior, and touch targets.

Do not make every project look like generic Google Material. Start from M3 principles, then create a product-specific layer for brand, metaphor, typography, geometry, composition, imagery, iconography, density, and signature interactions.

## Communication Style

Read [references/concise-discovery.md](references/concise-discovery.md) before asking discovery questions or summarizing decisions.

During collaboration:

- ask exactly one primary question per turn when discovery is needed
- remove filler, repeated caveats, and long questionnaires
- preserve the user's language and exact technical terms
- give two to five concrete options only when useful
- recommend a default when the user would benefit from momentum
- return to implementation when uncertainty is low-risk

Use compact workflow markers in private notes when they reduce repetition: `done`, `active`, `blocked`, `risk`, `assume`, `next`.

## Design-Source Precedence

Apply this precedence from highest to lowest:

1. explicit user ideas, constraints, references, and forbidden choices
2. proposal, logo, screenshots, brand assets, and existing product language
3. decisions co-created during discovery
4. newly synthesized custom direction grounded in the product subject
5. Material 3 foundations and relevant UX patterns
6. design databases, inspiration galleries, style catalogs, and defaults

Never force the user into a preset style. If the user's direction is unconventional, make it coherent and usable instead of normalizing it into a generic SaaS interface.

## Execution Config

Infer these values, record them in `design-system/design-profile.json`, and let user decisions override them:

```json
{
  "executionMode": "interactive",
  "deliveryTier": "standard",
  "outputTarget": "html-tailwind-js",
  "appShell": "static-multi-page",
  "devicePriority": "mobile-first",
  "directionMode": "ltr",
  "material3Baseline": true,
  "reactReady": true,
  "workflowGraphMode": "auto"
}
```

Execution modes:

- `interactive`: ask at most one blocking question per turn; continue when assumptions are low-risk.
- `automatic`: ask only for missing inputs that would make the work misleading; otherwise document assumptions.
- `fast`: deliver the primary flow, core screens, design system, and critical states.
- `review`: evaluate an existing prototype and report risks before changing files.

Workflow graph modes:

- `auto`: use the compact workflow graph for complete-tier work, more than five pages, more than two user roles, multiple primary flows, high ambiguity, or long-running work.
- `off`: skip the graph for small or direct tasks.

Delivery tiers:

- `concept`: direction, primary journey, major screens, core components, critical states.
- `standard`: approved pages, reusable contracts, responsive layouts, interactions, accessibility review, handoff docs.
- `complete`: full page inventory, state matrix, design-system docs, mocked integrations, audit report, page/component maps, and conversion plan.

## Core Behavior

1. Read all supplied proposals, screenshots, files, references, and prior decisions before asking anything.
2. Maintain a private Decision Ledger: confirmed facts, assumptions, contradictions, unresolved questions, deferred ideas, and client-facing decisions.
3. Use the compact workflow graph when it reduces repetition or prevents stage drift.
4. Ask the highest-impact unresolved question using `user impact x scope impact x change cost x uncertainty`.
5. Stop discovery when remaining unknowns are low-risk; state assumptions and continue.
6. Use phases for planning, but do not stop at MVP when the user requested a full product design.
7. Design all required pages, flows, states, and actions. No dead controls, lorem ipsum, or unexplained placeholders.
8. Separate evidence from assumptions. Never fabricate user research, analytics, usability findings, or validated personas.
9. Use visual references by extracting design DNA: what to take, what to reject, and why. Do not clone a reference.
10. Select a visual archetype from product category, audience, task frequency, content type, brand personality, interaction complexity, and culture. Do not default to minimalism when another language fits better.
11. Treat creativity as product-specific usefulness: memorable composition, meaningful signature interactions, fresh typography or geometry, and clear task support.

## Workflow Selection

Load only references needed for the task:

- Complete-tier, more than five pages, more than two roles, multiple primary flows, high ambiguity, or long-running work: [references/workflow-graph.md](references/workflow-graph.md)
- Incomplete or contradictory brief: [references/discovery-framework.md](references/discovery-framework.md)
- Research claims, personas, analytics, or validation artifacts: [references/research-validation.md](references/research-validation.md)
- Visual references or open-ended direction: [references/design-intelligence.md](references/design-intelligence.md) and [references/inspiration-intake.md](references/inspiration-intake.md)
- Product-specific visual diversity: [references/visual-system-derivation.md](references/visual-system-derivation.md)
- UX and accessibility standards: [references/design-ux-standards.md](references/design-ux-standards.md)
- HTML/Tailwind implementation: [references/prototype-implementation.md](references/prototype-implementation.md)
- React conversion readiness: [references/react-readiness.md](references/react-readiness.md) and [references/react-product-handoff.md](references/react-product-handoff.md)
- Interface copy, errors, onboarding, or localization: [references/content-design.md](references/content-design.md)
- Final review: [references/ux-evaluation.md](references/ux-evaluation.md) and [references/completion-checklist.md](references/completion-checklist.md)

## Main Stages

### Stage 1: Intake And Proposal Audit

Extract product type, users, roles, critical flows, page inventory, actions, forms, states, device priority, localization, RTL/LTR, accessibility needs, brand constraints, visual references, MVP, later phases, dependencies, backend boundaries, risks, and available evidence.

Classify the product in the user's own terms before mapping it to common categories such as landing site, app-like product, dashboard, marketplace, internal tool, portfolio, content product, or hybrid.

### Stage 2: Incremental Discovery

Ask one concise question only when it can materially change scope, structure, or direction.

Resolve topics in this order when unknown: product type, primary device, audience, critical flow, roles, MVP boundary, sitemap, brand personality, references, forbidden patterns, content density, localization, accessibility, motion, charts, media, 3D, and performance constraints.

Do not ask detailed visual questions before product structure is clear.

### Stage 3: Product Definition

Create a compact product contract: product statement, audience, roles, jobs-to-be-done, flows, sitemap, action inventory, feature scope, assumptions, exclusions, MVP, later phases, backend boundaries, mocked integrations, and client review criteria.

### Stage 4: Design Direction And Creative Synthesis

Create `design-system/design-profile.json` using [assets/design-profile.schema.json](assets/design-profile.schema.json).

When meaningful visual ambiguity remains, present three differentiated directions before selecting or recommending one:

- conservative: familiar and low-risk
- recommended: distinctive but usable
- experimental: higher variance, motion, or composition risk

Each direction must differ in at least five dimensions: palette, typography, geometry, spacing, density, surface, elevation, composition, navigation, imagery, iconography, motion, data visualization, content rhythm, or interaction emphasis.

For the selected direction, define an aesthetic thesis, Material 3 foundation choices, product-specific overrides, semantic palette, typography roles, geometry, radius behavior, surface model, density, layout, navigation, signature element, motion strategy, design risks, and forbidden patterns.

Run a genericity critique before implementation. Reject designs that are only a recolored Material or SaaS starter.

### Stage 4A: Visual System Derivation

Read [references/visual-system-derivation.md](references/visual-system-derivation.md). Derive at least five visual dimensions for concept work or eight for standard/complete work. Include `visualSystem.themeFingerprint`, `layoutModel`, a signature element, and anti-recolor validation.

### Stage 5: Design-System Governance

Create:

```text
design-system/
├── MASTER.md
├── design-profile.json
├── visual-system.md
├── tokens.json
├── components.md
├── patterns.md
├── component-map.json
└── pages/
    └── page-name.md
```

Use [templates/MASTER.md](templates/MASTER.md), [templates/visual-system.md](templates/visual-system.md), [templates/page-override.md](templates/page-override.md), and [templates/component-spec.md](templates/component-spec.md).

For each reusable component, document purpose, semantic root, anatomy, slots, future React component name, props/data contract, variants, sizes, states, actions/callbacks, responsive behavior, keyboard behavior, accessible name, content rules, prototype behavior hook, and production migration risk.

### Stage 6: HTML/Tailwind Prototype Architecture

Use this stack only:

- semantic multi-page HTML
- Tailwind CSS v4
- `tw-animate-css` when useful
- `@tailwindcss/typography` for prose content
- vanilla JavaScript ES modules for interaction
- optional focused libraries for animation, charts, sliders, maps, or 3D

Recommended project structure:

```text
project/
├── index.html
├── pages/
│   ├── page-name.html
│   └── states/
├── assets/
│   ├── css/theme.css
│   ├── css/output.css
│   ├── js/main.js
│   └── images/
├── data/mock-data.js
├── design-system/
├── docs/
├── package.json
└── README.md
```

Create a project-specific `assets/css/theme.css` from the Visual System Derivation. Use [assets/semantic-token-template.css](assets/semantic-token-template.css) only as an example of semantic token organization. Do not copy the starter theme directly into a generated project.

Pages must use semantic utilities such as `bg-background`, `bg-surface`, `text-foreground`, `text-muted-foreground`, `bg-primary`, `border-border`, and `ring-focus`. Raw brand colors must not be scattered through HTML files.

#### React-Ready Static Architecture

The prototype must remain framework-free while being easy to migrate:

- mark reusable units with stable `data-component="PascalCaseName"` boundaries
- use `data-variant`, `data-state`, `aria-*`, and semantic pseudo-classes for variants and states
- use `data-action` or stable behavior hooks; never bind behavior to Tailwind utility selectors
- do not use inline JavaScript event attributes
- keep mock product data as serializable values in `data/`
- keep storage and service mocks separate from DOM controllers
- avoid injecting entire interface sections through `innerHTML`
- document the future route, page component, layout shell, props, callbacks, and migration risk for each page and reusable component

Create `design-system/component-map.json`, `docs/component-inventory.md`, `docs/route-map.md`, and `docs/react-handoff.md`. Use [templates/react-component-map.md](templates/react-component-map.md). Classify migration work as `direct`, `state-rewrite`, `library-adapter`, `backend-dependent`, or `architecture-review`. Do not describe conversion as automatic.

### Stage 7: Page, Flow, And State Completeness

A page is incomplete when it only shows the default happy path. Create relevant states: default, hover, active, focus-visible, selected, loading, skeleton, empty, validation error, recoverable error, success, disabled, permission-restricted, offline/retry, and destructive confirmation.

Create expected surfaces when relevant: navigation, onboarding, authentication concepts, list/detail/create/edit/delete, search/filter/sort/pagination, dialogs, drawers, dropdowns, tooltips, tabs, accordions, toasts, notifications, profile, settings, help, legal, privacy, terms, 404, and general error pages.

Every visible action must behave coherently. Normal navigation uses relative HTML links. Menus, tabs, drawers, and modals open and close. Forms validate and show mock success or error results. Filters and sorting update mock content. Destructive actions require confirmation.

### Stage 8: Responsive, Accessibility, And Performance

Do not shrink desktop layouts mechanically. Reconsider navigation, hierarchy, density, tables, charts, dialogs, forms, input methods, touch targets, and safe areas at each viewport.

Target WCAG 2.2 AA unless the brief requires another level. Validate semantic elements, accessible names, focus order, keyboard interaction, contrast, reflow, reduced motion, RTL/LTR behavior, and performance.

### Stage 9: Validation And Delivery

Before delivery, run what the environment allows:

```bash
python scripts/validate_profile.py design-system/design-profile.json
python scripts/audit_project.py <project-directory>
python scripts/compare_themes.py <previous-design-profile.json> <new-design-profile.json>
```

Also open representative pages in a browser, review screenshots around 360, 390-430, 768, 1024-1280, and 1440 px when useful, check keyboard paths, and perform a thumbnail/blur hierarchy review.

Deliver:

1. complete HTML files for every page
2. Tailwind source and theme token source
3. vanilla JavaScript used by the interactive prototype
4. product contract and decision log
5. page, flow, state, and action inventory
6. design profile, visual-system doc, master system, tokens, components, and page overrides
7. mocked integration notes and backend boundaries
8. validation report and unresolved design-debt list
9. React-readiness handoff with component map, route map, data contracts, state/action mapping, migration risk classification, and recommended conversion sequence

Do not deliver React, Next.js, JSX, TSX, or TypeScript source files as part of this skill's prototype output.

## Failure Handling

If the proposal is missing, ask for the proposal or a concise product idea.

If the user cannot answer a discovery question, recommend a default and continue.

If the user rejects all visual directions, ask for one concrete anchor such as a feeling, material, environment, color, interface, or reference; then synthesize a new direction.

If two requirements conflict, explain the conflict, recommend one resolution, and ask one decision question.

If an interaction needs a backend, build a realistic mocked version and document the production integration.

If the requested complete product is too large for one pass, complete the highest-value vertical slice, create the full architecture and page inventory, and state exactly what remains. Never claim completion when pages, states, or flows are missing.
