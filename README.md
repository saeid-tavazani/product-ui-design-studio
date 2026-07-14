# Product UI Design Studio Skill

**Version 2.2.0**

A reusable Agent Skill for replacing the Figma design stage with complete, responsive, interactive prototypes built entirely with HTML, Tailwind CSS, and optional vanilla JavaScript.

## Important constraints

This Skill does not generate React, Next.js, Vue, Svelte, Angular, JSX, TSX, or SPA projects. It does generate a React-ready static prototype: component boundaries, props/data contracts, variants, states, actions, route mapping, and migration risks are documented so the later implementation can be converted incrementally without redesigning the UI. Each screen is delivered as a real HTML file. JavaScript is used only for prototype interactions such as menus, dialogs, tabs, forms, filters, mock state, animation, charts, and 3D.

Design databases and reference collections are optional intelligence sources, not limitations. Product assumptions are also kept separate from actual user evidence; the Skill never invents research findings or calls a proto-persona validated. The user may define an original style, palette, font direction, visual metaphor, or hybrid direction that does not exist in any dataset.

## Design decision priority

```text
User-defined direction
        ↓
Co-created direction
        ↓
Custom product-grounded synthesis
        ↓
Database-inspired evidence
        ↓
Fallback defaults
```

A database result can inspire or validate a decision, but it never overrides the user's explicit direction and never acts as a closed taxonomy.

## Contents

- `SKILL.md` — complete discovery, design intelligence, product definition, design-system governance, implementation, and review workflow
- `PROMPT.md` — standalone prompt for environments without Agent Skills
- `references/discovery-framework.md` — adaptive one-question-at-a-time discovery
- `references/design-intelligence.md` — open-ended style generation and non-limiting database rules
- `references/research-validation.md` — evidence ladder, proto-personas, method choice, journey mapping, and usability testing
- `references/inspiration-intake.md` — reference DNA extraction with take/reject synthesis
- `references/ux-evaluation.md` — severity-based UX, accessibility, and visual review
- `references/content-design.md` — interface vocabulary, microcopy, errors, empty states, onboarding, and localization
- `references/design-ux-standards.md` — visual, UX, accessibility, copy, motion, and genericity rules
- `references/implementation-standards.md` — HTML, Tailwind, vanilla JavaScript, interactions, RTL, responsive behavior, and file structure
- `references/react-readiness.md` — component boundaries, data/state contracts, route handoff, and incremental React migration rules
- `references/completion-checklist.md` — final quality gate
- `assets/theme.css` — Tailwind CSS v4 semantic theme starter
- `assets/design-profile.schema.json` — open schema that allows custom style and palette values
- `templates/MASTER.md` — master design-system template
- `templates/page-override.md` — page-specific override template
- `templates/component-spec.md` — variants, states, accessibility, motion, React handoff contract, and acceptance criteria
- `templates/react-component-map.md` — component inventory and migration mapping template
- `templates/proto-persona.md`, `journey-map.md`, `usability-test-plan.md` — evidence-aware research artifacts
- `templates/design-review-report.md` — prioritized findings and design debt
- `templates/design-profile.example.json` — example of a custom direction that is not selected from a preset catalog
- `intelligence/README.md` — rules for attaching optional design datasets without becoming constrained by them
- `scripts/audit_project.py` — static audit for framework leakage, links, semantics, theme tokens, and common prototype problems
- `references/source-review.md` — external ideas incorporated or intentionally rejected
- `CHANGELOG.md` — version history

## Installation

Place the folder in the skill directory supported by the agent:

```text
.agents/skills/product-ui-design-studio/
.claude/skills/product-ui-design-studio/
```

The folder name must match the `name` value in `SKILL.md`.

## Typical trigger

```text
Use product-ui-design-studio on this proposal. Analyze missing decisions and ask me one question at a time. My visual ideas have priority; use design databases only as optional inspiration. Then design the complete product as a multi-page HTML + Tailwind CSS prototype with vanilla JavaScript interactions. Do not use React or another frontend framework, but keep the output component-oriented and include the complete React migration handoff.
```

## Expected generated project

```text
project/
├── index.html
├── pages/
├── assets/
│   ├── css/theme.css
│   ├── css/output.css
│   ├── js/
│   ├── images/
│   └── icons/
├── data/
├── design-system/
│   ├── MASTER.md
│   ├── design-profile.json
│   ├── tokens.json
│   ├── components.md
│   ├── patterns.md
│   ├── pages/
│   └── component-map.json
├── docs/
│   ├── component-inventory.md
│   ├── route-map.md
│   └── react-handoff.md
├── package.json
└── README.md
```

## Theme usage

Copy `assets/theme.css` to the generated project's CSS directory. Change `--brand` to update primary, hover, active, soft, border, and focus colors across every HTML page. More advanced projects may replace all semantic tokens based on a custom palette in `design-profile.json`.

The theme file is a starter, not a mandatory palette. The Skill may generate a completely different semantic palette from the user's colors, logo, screenshots, material references, or verbal direction.

## Project audit

```bash
python scripts/audit_project.py /path/to/generated-project
python scripts/audit_project.py /path/to/generated-project --format json --output audit-report.json
```

The audit reports prohibited framework files, broken relative links, placeholder links, missing HTML metadata, common semantic and form-accessibility risks, duplicate IDs, unsafe target links, raw colors in HTML attributes, missing semantic theme tokens, missing reduced-motion/focus handling, inline handlers, class-based behavior hooks, large `innerHTML` rendering, unstable component names, and missing React-readiness handoff files. It is a static preflight, not proof of WCAG conformance.


## React-ready, not React-based

The generated prototype remains ordinary HTML files. React readiness is provided through stable contracts:

- semantic component roots marked with `data-component`
- documented props/data, variants, states, slots, and actions
- behavior hooks based on `data-action` rather than Tailwind classes
- serializable mock data separated from UI controllers
- semantic Tailwind tokens that transfer to `className`
- a future route map without adding client-side routing
- migration classifications for direct transfer, state rewrites, library adapters, backend work, and architecture decisions

Markup and most Tailwind utilities can transfer with small JSX syntax changes. Vanilla DOM state, routing, shared application state, and backend integrations still require deliberate React implementation.
