# React Conversion Handoff

Use this reference before final delivery and whenever the user asks how the approved design becomes a real React or Next.js product later.

## Responsibility

Document how the static HTML/Tailwind/vanilla JavaScript design prototype should become a production React or Next.js application after client approval. Do not write React, Next.js, JSX, TSX, or TypeScript source files during the prototype stage.

## Required outputs

Create:

- `docs/route-map.md`
- `docs/component-inventory.md`
- `docs/state-inventory.md`
- `docs/action-map.md`
- `docs/data-contracts.md`
- `docs/mocked-integrations.md`
- `docs/react-handoff.md`
- `design-system/component-map.json`

## Route map

For each page, record:

- current HTML file
- intended future route
- suggested future page component
- layout shell
- user goal
- primary actions
- data dependencies
- states
- auth or permission assumptions
- production API needs

## Component inventory

For each component, record:

- current semantic selector such as `[data-component='BookingCard']`
- current source HTML file(s)
- suggested future React component name and path
- owner layer: primitive UI, product UI, layout, page, provider, or utility
- props and data contract
- state ownership
- callbacks/actions
- variants
- accessibility rules
- Material 3 baseline
- product-specific override
- prototype JavaScript controller
- migration risk

Use migration risk labels:

- `direct`
- `state-rewrite`
- `library-adapter`
- `backend-dependent`
- `performance-review`
- `architecture-review`

## Production conversion plan

Sequence production work:

1. confirm page inventory and product scope
2. preserve semantic tokens and Tailwind theme decisions
3. create production application shell and routing
4. convert primitives and shared patterns from documented HTML contracts
5. convert product components and pages route by route
6. replace vanilla DOM controllers with React state, hooks, and callbacks
7. replace mock services with real API adapters
8. add validation, auth, permissions, analytics, persistence, and tests
9. rerun accessibility, responsive, performance, and interaction reviews
10. remove prototype-only fixtures and demo switches

Do not claim conversion is automatic. The prototype reduces redesign and ambiguity; production still requires engineering work.
