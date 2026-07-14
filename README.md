# Product UI Design Studio

> A product-discovery and UI/UX design skill that replaces the traditional Figma-first design stage with complete, responsive, interactive, React-ready prototypes built using semantic HTML, Tailwind CSS, and optional vanilla JavaScript.

![Version](https://img.shields.io/badge/version-2.2.0-111827)
![Stack](https://img.shields.io/badge/output-HTML%20%2B%20Tailwind%20CSS-0F172A)
![React Ready](https://img.shields.io/badge/handoff-React--ready-149ECA)
![License](https://img.shields.io/badge/license-MIT-16A34A)

## Table of contents

- [Why this project exists](#why-this-project-exists)
- [What this skill does](#what-this-skill-does)
- [What makes it different](#what-makes-it-different)
- [Main capabilities](#main-capabilities)
- [Output contract](#output-contract)
- [Workflow](#workflow)
- [Theme system](#theme-system)
- [React-ready architecture](#react-ready-architecture)
- [Installation](#installation)
- [Quick start](#quick-start)
- [Audit tool](#audit-tool)
- [Inspiration and combined ideas](#inspiration-and-combined-ideas)
- [Repository structure](#repository-structure)
- [Current limitations](#current-limitations)
- [Contributing](#contributing)
- [License](#license)

## Why this project exists

Modern AI design workflows often depend on Figma integrations, MCP servers, paid plans, platform limits, or a design-to-code step that still requires substantial cleanup before implementation.

I created **Product UI Design Studio** for two practical reasons:

1. **To avoid depending on a paid Figma/MCP workflow for product design.**
2. **To produce design output that can be converted into a React application with less redesign and less reverse engineering.**

Instead of generating static frames, the skill creates a real browser-based prototype:

- each screen is a real HTML page;
- the design system is represented by editable Tailwind and CSS tokens;
- interactions can be tested directly in the browser;
- responsive behavior is implemented rather than merely illustrated;
- components, states, data contracts, and routes are documented for later React migration.

The result is not intended to replace every capability of a visual design tool. It replaces the part of the workflow where product requirements are clarified, screens are designed, responsive layouts are explored, interactions are prototyped, and implementation handoff is prepared.

---

## What this skill does

Product UI Design Studio turns any of the following into a complete product prototype:

- product proposals;
- requirements documents;
- rough product ideas;
- screenshots and visual references;
- existing interfaces that need redesign;
- partial page lists;
- brand guidelines;
- mobile-app concepts;
- dashboards, marketplaces, portfolios, landing pages, or hybrid products.

It does not immediately start generating pages. It first identifies unclear or missing product decisions and asks **one high-impact question at a time**.

After discovery, it defines the product structure, visual direction, design system, pages, actions, states, responsive behavior, and implementation-ready prototype.

---

## Core idea

```text
Proposal, idea, screenshots, or existing product
                        ↓
              Proposal and evidence audit
                        ↓
          One-question-at-a-time discovery
                        ↓
 Product definition, roles, flows, sitemap, and phases
                        ↓
   Custom visual direction and semantic design system
                        ↓
 Responsive multi-page HTML + Tailwind CSS prototype
                        ↓
     Vanilla JavaScript interactions when required
                        ↓
 Accessibility, UX, interaction, and theme audit
                        ↓
     Component map and documented React handoff
```

---

## What makes it different

### 1. It is a discovery system, not only a UI generator

The skill does not treat an incomplete proposal as a complete brief.

It identifies ambiguity around:

- website, web app, mobile-first product, or hybrid product;
- primary device;
- user roles and permissions;
- critical user journey;
- MVP boundaries;
- project phases;
- required pages;
- design personality;
- content density;
- RTL and localization;
- animation, charts, 3D, or rich media;
- accessibility and performance constraints.

Questions are prioritized using:

```text
question priority = user impact × scope impact × change cost × uncertainty
```

Only one main question is asked per turn, so the user can develop the product idea gradually without receiving a large questionnaire.

### 2. It is a Figma-replacement prototype workflow

The output is not a collection of screenshots or isolated mockups.

Every page is implemented as a real `.html` file with:

- responsive layouts;
- navigation;
- working buttons;
- forms and validation states;
- tabs, filters, dialogs, drawers, and menus;
- loading, empty, error, success, disabled, permission, and offline states;
- mobile, tablet, and desktop behavior;
- keyboard and accessibility considerations.

### 3. It is React-ready without generating React

The prototype stack remains intentionally simple:

```text
Semantic HTML
Tailwind CSS v4
Optional vanilla JavaScript modules
```

However, the structure is designed so it can later be migrated to React without reconstructing the design.

Reusable sections receive stable contracts such as:

```html
<article
  data-component="ProductCard"
  data-variant="featured"
  data-state="default"
>
  ...
</article>
```

The future React equivalent is documented separately:

```tsx
<ProductCard
  product={product}
  variant="featured"
  onSelect={handleSelect}
/>
```

The prototype itself does **not** contain JSX, TSX, React imports, framework routing, or React components.

### 4. Design databases inspire decisions but never limit them

The skill may use style collections, palette libraries, font pairings, industry rules, chart patterns, or UX guidelines as optional intelligence sources.

They are not treated as a closed catalog.

The decision priority is:

```text
Explicit user direction
        ↓
Provided brand assets and project material
        ↓
Decisions co-created during discovery
        ↓
New product-specific visual synthesis
        ↓
Database and reference inspiration
        ↓
General fallback defaults
```

A user can:

- define an entirely original visual style;
- combine multiple styles;
- provide exact colors;
- describe a mood, material, environment, or metaphor;
- reject all database recommendations;
- create a direction that has no predefined name.

### 5. It separates evidence from assumptions

The skill does not invent UX research.

It distinguishes between:

- observed behavior and analytics;
- direct user statements;
- stakeholder or domain knowledge;
- secondary research;
- design assumptions.

When real research does not exist, personas are labeled as **proto-personas**, and validation needs are documented instead of presenting invented findings as facts.

---

## Main capabilities

### Product discovery

- proposal audit;
- contradiction and ambiguity detection;
- incremental questioning;
- product-type classification;
- audience and jobs-to-be-done definition;
- role and permission modeling;
- sitemap and screen inventory;
- action inventory;
- MVP and phase planning;
- assumptions, exclusions, and success criteria.

### UX architecture

- primary and secondary user flows;
- happy paths;
- failure and recovery paths;
- difficult or assisted paths;
- offline and interrupted flows;
- information architecture;
- responsive navigation models;
- form behavior and validation;
- empty, loading, error, success, and permission states.

### Visual direction

- user-defined visual directions;
- co-created design directions;
- custom product-grounded synthesis;
- reference DNA analysis;
- semantic color systems;
- typography roles;
- spacing, radius, elevation, and density systems;
- design dials for variance, motion, and density;
- product-specific signature elements;
- anti-generic and anti-template review.

### Design system

- master design-system rules;
- page-specific overrides;
- semantic design tokens;
- component specifications;
- variants and state matrices;
- motion tokens;
- content vocabulary;
- accessibility behavior;
- acceptance criteria.

### Prototype implementation

- semantic multi-page HTML;
- Tailwind CSS v4;
- optional vanilla JavaScript modules;
- mobile-first responsive behavior;
- RTL and LTR support;
- accessible interactions;
- real relative links;
- mock data separated from markup;
- focused integration with libraries such as GSAP, Three.js, Chart.js, Swiper, Lottie, or Lenis when justified.

### React-ready handoff

- stable component boundaries;
- `data-component`, `data-variant`, `data-state`, and `data-action` contracts;
- component inventory;
- future props and callbacks;
- route map;
- mock data contracts;
- state ownership notes;
- migration risk classification;
- incremental React conversion plan.

### Quality review

- UX heuristic review;
- severity and confidence ratings;
- accessibility preflight;
- semantic HTML review;
- keyboard and focus review;
- theme-token review;
- broken-link detection;
- React-readiness checks;
- responsive and visual consistency checks.

---

## Output contract

The generated design must follow these rules:

1. Every screen is a real `.html` file.
2. Tailwind CSS v4 is used for layout, styling, responsive behavior, and visual states.
3. Vanilla JavaScript is used only when interaction requires it.
4. React, Next.js, Vue, Svelte, Angular, JSX, TSX, and SPA routing are prohibited in the prototype.
5. All colors, typography, spacing, radius, elevation, motion, and density values are centralized.
6. Every visible action must work in the prototype.
7. All required pages, flows, and interface states must be designed.
8. Reusable UI must have stable component boundaries.
9. Data, behavior, and visual styling must remain separated.
10. React migration artifacts must be included without generating React code.

---

## Expected generated project

```text
project/
├── index.html
├── pages/
│   ├── login.html
│   ├── dashboard.html
│   ├── profile.html
│   ├── settings.html
│   ├── 404.html
│   └── ...
├── assets/
│   ├── css/
│   │   ├── theme.css
│   │   └── output.css
│   ├── js/
│   │   ├── main.js
│   │   ├── dialogs.js
│   │   ├── forms.js
│   │   └── filters.js
│   ├── images/
│   └── icons/
├── data/
│   └── mock-data.js
├── design-system/
│   ├── MASTER.md
│   ├── design-profile.json
│   ├── tokens.json
│   ├── component-map.json
│   ├── components.md
│   ├── patterns.md
│   └── pages/
│       ├── dashboard.md
│       ├── profile.md
│       └── ...
├── docs/
│   ├── product-contract.md
│   ├── page-inventory.md
│   ├── component-inventory.md
│   ├── route-map.md
│   ├── react-handoff.md
│   └── design-review.md
├── package.json
└── README.md
```

The exact structure may be adapted to the product, but the separation between pages, design tokens, behavior, mock data, design-system documentation, and React handoff should remain.

---

## Workflow

### Stage 1 — Proposal audit

The skill reads all supplied material before asking questions:

- proposal;
- requirements;
- screenshots;
- logos;
- reference products;
- previous decisions;
- technical constraints.

It records what is known, unclear, contradictory, assumed, or missing.

### Stage 2 — Incremental discovery

The skill asks exactly one high-impact question per turn.

A typical question includes:

- one short observation;
- one question;
- two to five concrete options when useful;
- one recommended option;
- an open path for the user's own answer.

### Stage 3 — Product definition

The skill creates:

- product statement;
- target users and roles;
- jobs-to-be-done;
- critical flows;
- page and action inventories;
- MVP scope;
- later phases;
- assumptions and exclusions.

### Stage 4 — Design direction

The direction may be:

- user-defined;
- co-created;
- custom-generated;
- database-inspired;
- hybrid.

When meaningful ambiguity remains, the skill may propose conservative, recommended, and experimental directions. The user can always describe or combine a custom fourth direction.

### Stage 5 — Design system

The skill defines:

- semantic palette;
- typography roles;
- spacing scale;
- radius and elevation;
- motion rules;
- component anatomy;
- variants and states;
- accessibility behavior;
- content vocabulary;
- page-specific overrides.

### Stage 6 — Complete prototype

All requested pages, states, flows, actions, and phases are implemented using HTML, Tailwind CSS, and optional JavaScript.

### Stage 7 — Review and audit

The skill checks:

- responsive behavior;
- visual consistency;
- accessibility risks;
- incomplete actions;
- broken navigation;
- raw colors outside the token system;
- missing states;
- framework leakage;
- React-readiness.

### Stage 8 — React handoff

The final documentation explains:

- which HTML regions become React components;
- component props and callbacks;
- state ownership;
- route mapping;
- library adapters;
- backend-dependent behavior;
- recommended migration order.

---

## Design phases and MVP

For larger products, the skill organizes work into phases without leaving requested pages undesigned.

A common structure is:

```text
Phase 0 — Foundation
Information architecture, tokens, shell, navigation, component foundations

Phase 1 — MVP
Smallest complete end-to-end journey that delivers the core product value

Phase 2 — Core expansion
Secondary workflows, management tools, supporting roles, additional pages

Phase 3 — Experience layer
Personalization, advanced motion, automation concepts, 3D, rich media

Phase 4 — Hardening
Accessibility, edge cases, performance, responsive review, final QA
```

Phase names and boundaries are adapted to the real product.

---

## Theme system

The included `assets/theme.css` uses semantic Tailwind CSS v4 theme variables.

A project should use semantic classes such as:

```html
<button class="bg-primary text-primary-foreground hover:bg-primary-hover">
  Save changes
</button>
```

Instead of scattering raw colors through pages:

```html
<!-- Avoid -->
<button class="bg-[#E51B32] text-white hover:bg-[#C9152A]">
  Save changes
</button>
```

Changing the main brand token can update the entire prototype:

```css
:root {
  --brand: oklch(0.58 0.23 25);
}
```

The provided theme is only a starter. The skill may create a completely new token system based on:

- user-provided colors;
- logos;
- screenshots;
- physical materials;
- environments;
- brand metaphors;
- custom visual descriptions.

---

## React-ready architecture

React-ready does not mean adding React syntax to the HTML prototype.

It means preserving the contracts that React will need later.

### Component boundary

```html
<section
  data-component="PricingCard"
  data-variant="recommended"
  data-state="default"
>
  ...
</section>
```

### Behavior hook

```html
<button data-action="select-plan" data-plan-id="pro">
  Select plan
</button>
```

JavaScript binds to behavioral attributes rather than Tailwind utility classes:

```js
const buttons = document.querySelectorAll('[data-action="select-plan"]');
```

### Data separation

```js
export const plans = [
  {
    id: 'pro',
    name: 'Pro',
    price: 29,
    recommended: true,
  },
];
```

### Future React contract

```text
Component: PricingCard
Props: plan, variant, state
Callbacks: onSelect
State owner: PricingPage
Migration difficulty: state-rewrite
```

### Migration categories

- `direct` — mostly markup and class conversion;
- `state-rewrite` — DOM state becomes React state or hooks;
- `library-adapter` — third-party JavaScript needs a React wrapper;
- `backend-dependent` — behavior requires API or authentication integration;
- `architecture-review` — migration requires a higher-level implementation decision.

---

## Installation

Clone the repository:

```bash
git clone https://github.com/saeid-tavazani/product-ui-design-studio.git
```

Then place the skill folder in the directory supported by your agent.

### Claude

```text
.claude/skills/product-ui-design-studio/
```

### Agent-compatible environments

```text
.agents/skills/product-ui-design-studio/
```

The folder name should match the `name` field in `SKILL.md`:

```yaml
name: product-ui-design-studio
```

### Environments without Agent Skills

Use the standalone instructions in:

```text
PROMPT.md
```

---

## Quick start

Give the agent a product proposal, idea, screenshots, or requirements and use a prompt similar to this:

```text
Use product-ui-design-studio for this project.

First analyze the proposal and identify missing or ambiguous decisions. Ask me only one important question at a time. Do not ask again about anything already defined.

My ideas and visual preferences have priority. Design databases may be used only as optional inspiration and must not limit the final direction.

After discovery, define the product structure, users, flows, complete page inventory, MVP, and later phases. Then build every required page and interface state as a responsive multi-page prototype using semantic HTML, Tailwind CSS, and vanilla JavaScript only when interaction requires it.

Do not use React or another frontend framework in the prototype. Keep the result component-oriented and provide a documented React-ready handoff.
```

---

## Example requests

### Product proposal

```text
Use Product UI Design Studio on this proposal. Find contradictions and missing decisions, then ask one question at a time. After discovery, design the complete product including MVP and later phases.
```

### Existing product redesign

```text
Analyze these screenshots and redesign the product. Preserve the useful behavior, identify UX problems, create a custom visual direction, and rebuild every screen as HTML and Tailwind CSS.
```

### Mobile-first application

```text
This is an app with a web version, not a traditional website. Treat mobile as the primary experience, define the bottom navigation and critical flows first, then adapt the same design system to tablet and desktop.
```

### User-defined visual direction

```text
I want the interface to feel like precision sports equipment: matte black surfaces, controlled red accents, compact typography, and subtle mechanical motion. Do not replace this direction with a preset style; develop it into a complete design system.
```

---

## Optional libraries

The prototype may use focused libraries when they clearly improve the product experience:

- `tw-animate-css`;
- `@tailwindcss/typography`;
- GSAP;
- Three.js;
- Chart.js;
- Swiper;
- Lottie;
- Lenis.

Libraries must remain optional and focused. They must not replace the multi-page HTML architecture or introduce a frontend application framework.

---

## Audit tool

Run the static audit against a generated project:

```bash
python scripts/audit_project.py /path/to/generated-project
```

Generate a JSON report:

```bash
python scripts/audit_project.py /path/to/generated-project \
  --format json \
  --output audit-report.json
```

The audit checks for issues such as:

- React, Vue, Svelte, JSX, TSX, or other prohibited framework files;
- inline event handlers;
- behavior attached to Tailwind utility selectors;
- broken relative links;
- placeholder `href="#"` links;
- missing `lang`, `dir`, viewport, `<main>`, or `<h1>`;
- duplicate IDs;
- images without `alt`;
- form controls without labels;
- buttons without accessible names or explicit types;
- dialogs without accessible names;
- unsafe `target="_blank"` links;
- raw colors in HTML;
- missing focus-visible styles;
- missing reduced-motion handling;
- missing React-ready component boundaries.

The audit is a static preflight. It does not prove WCAG conformance and does not replace browser, keyboard, screen-reader, or usability testing.

---

## Inspiration and combined ideas

Product UI Design Studio is an independent skill. It combines useful ideas from several public design and artifact-building resources while keeping its own constraints and workflow.

### Anthropic Frontend Design

Source:

- <https://claudemarketplaces.com/skills/anthropics/skills/frontend-design>

Ideas adapted:

- deliberate, product-specific visual direction;
- avoiding generic AI-generated aesthetics;
- typography as part of product identity;
- one meaningful signature element;
- design critique before and after implementation;
- restrained use of motion;
- writing interface copy from the user's point of view.

How this project extends it:

- adds proposal audit and product discovery;
- adds complete page, flow, action, and state inventories;
- adds MVP and phase planning;
- adds multi-page HTML and Tailwind delivery;
- adds React-ready component and migration documentation.

### Anthropic Web Artifacts Builder

Source:

- <https://claudemarketplaces.com/skills/anthropics/skills/web-artifacts-builder>

Ideas adapted:

- building complete, runnable browser artifacts;
- using a multi-file structure for non-trivial products;
- treating interaction as part of the deliverable rather than a static visual note.

How this project differs:

- the output stack is intentionally restricted to HTML, Tailwind CSS, and optional vanilla JavaScript;
- React and other frontend frameworks are not generated during the design stage;
- product discovery, design-system governance, and React handoff are first-class parts of the workflow.

### UI UX Pro Max Skill

Source:

- <https://github.com/nextlevelbuilder/ui-ux-pro-max-skill>

Ideas adapted:

- searchable design-intelligence collections;
- product and industry pattern research;
- palette, typography, chart, animation, and UX-rule recommendations;
- design dials for variance, motion, and density;
- master design-system rules with page-level overrides;
- structured UX priority checks.

Important modification:

The database is treated only as an intelligence source. It never becomes a closed set of allowed styles, colors, fonts, layouts, or industries. User-defined and newly synthesized visual directions always have higher priority.

### UI/UX Design Pro

Source:

- <https://mcpmarket.com/tools/skills/ui-ux-design-pro>

Ideas adapted:

- treating product design as a combination of information architecture, visual hierarchy, interaction design, personas, testing, and design systems;
- iterative review rather than considering the first output final.

Ideas intentionally not adopted:

- framework-specific implementation assumptions;
- treating Material Design, Apple HIG, or another system as the universal visual default.

### Claude Marketplaces Design/UI skills

Source:

- <https://claudemarketplaces.com/skills/category/design-ui>

Patterns adapted after reviewing relevant skills:

- evidence-aware UX research;
- explicit separation between validated findings and assumptions;
- proto-personas instead of fabricated validated personas;
- reference DNA extraction with take/reject notes;
- happy, failure, and difficult journey variants;
- structured usability-test plans;
- component state matrices;
- motion tokens;
- severity-based UX review;
- accessibility and keyboard review;
- UX writing and localization stress testing.

Patterns intentionally rejected:

- closed aesthetic taxonomies;
- mandatory premium-font assumptions;
- arbitrary universal bans on specific fonts, shadows, easings, or layouts;
- React, Next.js, Vue, native-mobile, or framework component output;
- claims that automated audits prove accessibility compliance.

---

## What this project is not

Product UI Design Studio is not:

- a Figma plugin;
- an MCP server;
- a React code generator;
- a production backend generator;
- an automatic accessibility-certification tool;
- a guarantee that every visual decision is correct without user validation;
- a replacement for real user research when high-risk product decisions require it.

It is a structured system for moving from an incomplete idea to a complete, testable, implementation-aware product design prototype.

---

## Repository structure

```text
product-ui-design-studio/
├── SKILL.md
├── PROMPT.md
├── README.md
├── CHANGELOG.md
├── assets/
│   ├── theme.css
│   └── design-profile.schema.json
├── references/
│   ├── completion-checklist.md
│   ├── content-design.md
│   ├── design-intelligence.md
│   ├── implementation-standards.md
│   ├── inspiration-intake.md
│   ├── react-readiness.md
│   ├── research-validation.md
│   ├── source-review.md
│   └── ux-evaluation.md
├── scripts/
│   └── audit_project.py
└── templates/
    ├── MASTER.md
    ├── component-spec.md
    ├── design-profile.example.json
    ├── design-review-report.md
    ├── journey-map.md
    ├── page-override.md
    ├── proto-persona.md
    ├── react-component-map.md
    └── usability-test-plan.md
```

### Important files

| File | Purpose |
|---|---|
| `SKILL.md` | Main agent behavior and workflow |
| `PROMPT.md` | Standalone prompt for environments without Agent Skills |
| `assets/theme.css` | Semantic Tailwind theme starter |
| `assets/design-profile.schema.json` | Open-ended schema for custom design directions |
| `references/react-readiness.md` | Rules for low-friction React migration |
| `references/implementation-standards.md` | HTML, Tailwind, JavaScript, responsive, and interaction rules |
| `references/completion-checklist.md` | Final quality gate |
| `templates/MASTER.md` | Master design-system template |
| `templates/component-spec.md` | Component anatomy, variants, states, accessibility, and React contract |
| `scripts/audit_project.py` | Static project and React-readiness audit |

---

## Design principles

1. **The user's direction has priority.**
2. **The product subject should shape the visual identity.**
3. **A database is a source, not a cage.**
4. **Product structure is resolved before detailed decoration.**
5. **Every action and state is part of the design.**
6. **Responsive behavior is implemented, not described vaguely.**
7. **HTML should be semantic and implementation-neutral.**
8. **Theme values should be centralized and semantic.**
9. **Accessibility requires manual verification.**
10. **The prototype should be easy to migrate, but it should not pretend to be production React code.**

---

## Current limitations

- Shared HTML components may still be duplicated across static pages unless a build-time include strategy is introduced.
- Complex JavaScript state must be rewritten using React state, hooks, or a state-management solution during migration.
- Third-party animation, chart, and 3D libraries may require React adapters.
- Authentication, APIs, persistence, permissions, and backend validation remain mock behavior unless implemented separately.
- Visual and usability quality still depends on the completeness of the proposal, user feedback, and review process.

---

## Roadmap ideas

Potential future improvements:

- optional reusable HTML partials or static-site generation;
- visual-regression screenshots;
- automated responsive screenshot generation;
- contrast and accessibility integrations;
- component catalog generation;
- automated HTML-to-JSX migration assistance;
- example projects and reference implementations;
- CI workflow for running the audit script;
- optional structured design-intelligence datasets.

---

## Contributing

Contributions should preserve the core contract:

- prototype output remains HTML + Tailwind CSS + optional vanilla JavaScript;
- user-defined visual directions remain higher priority than presets;
- external data must not become a closed design taxonomy;
- new rules should improve product clarity, UX quality, accessibility, implementation quality, or React migration;
- framework-specific output should remain outside the design-stage prototype.

When proposing a change, explain:

1. the problem it solves;
2. where it belongs in the workflow;
3. whether it affects discovery, design, implementation, audit, or React handoff;
4. how it avoids creating unnecessary complexity.

---

## License

Released under the MIT License. Add a `LICENSE` file to the repository when publishing if it is not already present.

The external resources listed in the inspiration section remain the work of their respective authors and are referenced for attribution and architectural context. This project does not claim ownership of those resources and does not require them as runtime dependencies.

---

## Summary

Product UI Design Studio was created to make product design more accessible, executable, and implementation-aware.

It replaces a paid or tool-dependent Figma-first workflow with a structured process that:

- clarifies the product before designing it;
- asks one important question at a time;
- respects user-created visual ideas;
- builds the entire product, not only a hero page;
- produces responsive and interactive browser prototypes;
- centralizes the design system;
- audits UX, accessibility, and implementation quality;
- prepares the result for a cleaner React migration.

The prototype is static by design, but the thinking, contracts, and structure are intended to survive into production.
