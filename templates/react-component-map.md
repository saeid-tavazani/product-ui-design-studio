# React Migration Component Map

The prototype itself remains HTML + Tailwind + vanilla JavaScript. This document records implementation-neutral contracts for a later React conversion.

## Component inventory

| Prototype component | Selector | Suggested React name | Source pages | Migration class |
|---|---|---|---|---|
| | | | | direct / state-rewrite / library-adapter / backend-dependent / architecture-review |

## Component contract: [Name]

### Semantic root

### Suggested React file

`src/components/[path]/[Name].tsx`

### Props/data

| Prop | Type | Required | Source | Notes |
|---|---|---:|---|---|
| | | | | |

### Slots/children

### Variants

### States

### Callbacks/actions

### Prototype hooks

- `data-component`:
- `data-action`:
- JavaScript module:
- Mock data source:

### Accessibility contract

### Responsive behavior

### Migration notes

### Acceptance criteria

- [ ] Markup can be represented without changing semantics.
- [ ] Tailwind utilities use shared tokens and transfer to `className`.
- [ ] State and variants have explicit names.
- [ ] DOM behavior has a documented React-state equivalent.
- [ ] No business data is stored as HTML strings or CSS class names.
