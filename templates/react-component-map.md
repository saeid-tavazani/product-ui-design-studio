# React Component Map

The prototype is static HTML + Tailwind CSS + vanilla JavaScript. This document records the future React contracts that should survive a later production implementation after client approval. Do not generate React files as part of the prototype.

## Component inventory

| Prototype component | Source file | Production name | Source routes | Migration class |
|---|---|---|---|---|
| | | | | direct / state-rewrite / library-adapter / backend-dependent / architecture-review |

## Component contract: [Name]

### Semantic root

### Suggested future component path

`src/components/[path]/[Name]`

### Props/data

| Prop | Type | Required | Source | Notes |
|---|---|---:|---|---|
| | | | | |

### Slots/children

### Variants

### States

### Callbacks/actions

### Prototype behavior

- Mock data source:
- State owner:
- Service boundary:

### Accessibility contract

### Responsive behavior

### Migration notes

### Acceptance criteria

- [ ] Source prototype remains HTML, Tailwind CSS, and vanilla JavaScript only.
- [ ] Tailwind utilities use shared tokens.
- [ ] State and variants have explicit names.
- [ ] Prototype behavior maps to future production state, service, or route ownership.
- [ ] No business data is stored as CSS class names.
- [ ] No JSX, TSX, React imports, or framework routing exists in the prototype.
