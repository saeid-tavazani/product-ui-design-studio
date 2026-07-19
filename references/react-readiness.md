# React-Ready Static Prototype Standards

The prototype remains a static multi-page HTML + Tailwind CSS + vanilla JavaScript deliverable. React is a later implementation target, not part of the design output. Structure the prototype so a developer can migrate it incrementally without redesigning or reverse-engineering the interface.

## Core principle

Optimize for **portable contracts**, not for simulated React inside HTML.

- HTML owns document structure and accessible semantics.
- Tailwind and semantic tokens own presentation.
- JavaScript modules own prototype behavior and mock state.
- Component specifications own reusable contracts.
- Mock data is separated from markup when it represents repeatable product entities.
- React migration replaces rendering and state management, not the design system or interaction model.

Do not add JSX, React imports, virtual DOM utilities, client-side routers, or framework component libraries to make the prototype “React-ready.”

## Component boundaries

Identify reusable interface units with stable, implementation-neutral metadata:

```html
<article
  data-component="ProductCard"
  data-variant="featured"
  data-state="default"
>
  ...
</article>
```

Use PascalCase for `data-component` names so the future React component name is obvious. Use documented lowercase values for variants and states.

Good component candidates:

- repeated visual units
- independent interaction units
- product patterns with meaningful variants
- shared navigation, forms, dialogs, filters, cards, tables, and feedback surfaces

Do not label every wrapper as a component. Layout-only containers that have no reusable contract should remain ordinary semantic HTML.

## Component contract

For every reusable component, document:

- future React component name
- purpose and semantic root element
- child slots or regions
- props/data contract
- optional and required values
- variants and sizes
- states and state transitions
- emitted actions or callbacks
- accessibility behavior
- responsive behavior
- mock data source
- prototype JavaScript module
- migration notes and known framework-specific work

Example:

```md
## ProductCard

Props:
- id: string
- title: string
- image: { src: string, alt: string }
- price: number
- badge?: string
- disabled?: boolean

Callbacks:
- onSelect(id)
- onFavoriteChange(id, nextValue)

Variants:
- default
- featured
- compact

States:
- default
- loading
- unavailable
- selected
```

## Markup rules

Write HTML that converts cleanly to a future component implementation:

- use valid semantic nesting
- close void elements consistently
- avoid malformed optional end tags
- avoid inline `style` unless a dynamic value cannot be represented by a token or utility
- avoid inline event attributes such as `onclick`, `onchange`, and `onsubmit`
- use `class`, `for`, and other normal HTML attributes in the prototype; document future framework attribute changes only in handoff notes
- keep stable IDs only where accessibility relationships require them
- use `data-*` attributes for component identity, behavior hooks, variants, and state
- keep visible content as real text, not CSS-generated content

## Tailwind and tokens

Tailwind classes should transfer to `className` with minimal changes.

- use semantic color utilities rather than raw values
- centralize tokens in `theme.css`
- avoid one-off arbitrary values when a reusable token is appropriate
- keep state styling attached to `data-state`, `aria-*`, pseudo-classes, or documented variants
- avoid JavaScript that depends on presentational class names such as `.bg-red-500` or `.hidden`

Preferred state styling:

```html
<button
  data-component="FavoriteButton"
  data-state="inactive"
  aria-pressed="false"
  class="data-[state=active]:bg-primary"
>
  ...
</button>
```

JavaScript updates `data-state` and `aria-pressed`; React later derives both from component state.

## JavaScript architecture

Use small ES modules and stable behavior hooks:

```html
<button data-action="toggle-favorite" data-item-id="product-42">...</button>
```

```js
export function setFavorite(button, active) {
  button.dataset.state = active ? 'active' : 'inactive';
  button.setAttribute('aria-pressed', String(active));
}
```

Rules:

- select behavior through `data-action`, `data-controller`, or another documented `data-*` hook
- avoid selecting by Tailwind utility classes
- avoid inline handlers
- avoid injecting complete interface sections with `innerHTML`
- keep DOM access inside focused controller modules
- isolate storage and mock services from UI controllers
- represent prototype state with plain serializable objects
- keep side effects explicit
- use custom events only when they clarify boundaries; document their payloads

A future React migration should replace DOM controllers with props, state, hooks, and callbacks while preserving the documented behavior contract.

## Data architecture

Separate repeatable content from HTML when it represents product data:

```text
data/
├── products.js
├── users.js
└── navigation.js
```

Use stable IDs and serializable values. Do not store DOM nodes, CSS classes, or HTML strings as business data.

Good:

```js
export const products = [
  { id: 'p-1', title: 'Starter plan', price: 120, status: 'available' },
];
```

Avoid:

```js
export const products = [
  { html: '<article class="...">...</article>' },
];
```

Small static marketing copy may remain directly in HTML. Do not force every sentence into a data file.

## Page and routing handoff

Every page remains a real HTML file. Also create a route map that records the intended future application route:

| HTML file | Future route | Suggested React page | Layout shell |
|---|---|---|---|
| `pages/products.html` | `/products` | `ProductsPage` | `AppShell` |
| `pages/product-detail.html` | `/products/:id` | `ProductDetailPage` | `AppShell` |

Do not add client-side routing to the prototype.

## Required handoff artifacts

Create:

```text
docs/
├── react-handoff.md
├── route-map.md
└── component-inventory.md

design-system/
└── component-map.json
```

`component-map.json` should contain implementation-neutral contracts:

```json
{
  "components": [
    {
      "name": "ProductCard",
      "selector": "[data-component='ProductCard']",
      "sourcePages": ["pages/products.html"],
      "props": {
        "id": "string",
        "title": "string",
        "price": "number",
        "disabled": "boolean?"
      },
      "variants": ["default", "featured", "compact"],
      "states": ["default", "loading", "unavailable"],
      "actions": ["select", "toggle-favorite"]
    }
  ]
}
```

## Migration sequence

Recommend an incremental conversion:

1. move semantic tokens and Tailwind configuration unchanged
2. create application shells and route mapping
3. convert primitives and shared components
4. convert product patterns
5. move mock data to typed models/API adapters
6. replace vanilla controllers with React state and hooks
7. convert pages route by route
8. replace local mock services with real integrations
9. rerun accessibility and interaction tests

## Migration risk classification

Mark every interaction as:

- `direct`: semantic markup and classes transfer with minor future framework syntax changes
- `state-rewrite`: visual contract transfers; vanilla DOM state becomes React state
- `library-adapter`: a focused library needs a React wrapper or lifecycle integration
- `backend-dependent`: design transfers but real behavior requires API/auth/storage work
- `architecture-review`: behavior depends on application-level concerns such as routing, permissions, or synchronized global state

The final handoff must list these risks accurately. Do not claim automatic conversion.
