# HTML + Tailwind Implementation Standards

## Mandatory stack

The design prototype must use:

- semantic multi-page HTML
- Tailwind CSS v4
- vanilla JavaScript ES modules only when required
- `tw-animate-css` when useful
- `@tailwindcss/typography` for prose content
- inline SVG or a lightweight icon set

Prohibited:

- React
- Next.js
- Vue
- Svelte
- Angular
- JSX or TSX
- SPA routers
- framework component files
- converting the prototype into a production application without a separate user request

A build or preview tool may compile Tailwind or serve static files, but it must not change the output architecture from HTML pages. The static prototype must follow [react-readiness.md](react-readiness.md) so later React conversion is low-friction without placing React code in the prototype.

## Tailwind theme architecture

Keep one clear project-specific theme source such as `assets/css/theme.css`:

```css
@import "tailwindcss";
@import "tw-animate-css";
@plugin "@tailwindcss/typography";
```

Use `assets/semantic-token-template.css` from this skill only as a semantic-token structure reference. Do not copy it into a generated project, and do not preserve its visual values as hidden defaults.

Map Tailwind semantic utilities to CSS custom properties. Use names such as:

- `bg-background`
- `bg-surface`
- `bg-surface-elevated`
- `text-foreground`
- `text-muted-foreground`
- `bg-primary`
- `text-primary-foreground`
- `border-border`
- `ring-focus`
- `text-danger`

Semantic token values must be derived from the current project's Visual System Derivation and Theme Fingerprint. Do not rely on a single brand seed alone. Do not scatter raw brand values across HTML pages.

Centralize:

- colors
- typography families and scale
- spacing additions
- radius scale
- borders and shadows
- animation durations and easing
- container widths
- z-index roles when needed

Also centralize project-specific:

- typography roles and numeric/code typography when applicable
- density rhythm
- component anatomy tokens
- layout measures
- motion duration, easing, distance, and reduced-motion behavior

## HTML page architecture

Each major screen is a real HTML file with a stable URL:

```text
index.html
pages/login.html
pages/dashboard.html
pages/profile.html
pages/settings.html
pages/404.html
```

Use relative links that work from the chosen folder structure. Avoid `href="#"` for navigation. Use a `<button>` for an in-page action and an `<a>` for navigation.

Each file should include:

- correct `lang` and `dir`
- descriptive `<title>`
- viewport metadata
- a skip-to-content link on substantial navigational pages
- semantic landmarks and one clear page-level heading
- logical heading order
- shared Tailwind output stylesheet
- required JavaScript module only when the page needs it

## Reusable visual patterns without frameworks

Reuse patterns through consistent HTML contracts, classes, and documented snippets. Typical layers:

1. tokens
2. primitives: buttons, links, inputs, badges, icon buttons, surfaces
3. composites: fields, search controls, cards, toolbars, dialogs
4. product patterns: booking cards, order timelines, workout summaries
5. page compositions

Do not hide the document structure behind a client-side rendering system. Minor HTML duplication is acceptable in a design prototype when it keeps pages inspectable and portable.

Mark meaningful reusable units with stable contracts:

```html
<article data-component="ProjectCard" data-variant="default" data-state="ready">
  ...
</article>
```

Use `data-component` only for units that are genuinely reusable or independently interactive. Keep the same anatomy and state names wherever the component appears. Record future React names, props, callbacks, and migration notes in the component inventory.

## Vanilla JavaScript structure

Use small focused ES modules:

```text
assets/js/
├── main.js
├── navigation.js
├── dialogs.js
├── tabs.js
├── forms.js
├── filters.js
└── prototype-state.js
```

Rules:

- select elements with stable `data-action`, `data-controller`, or other documented `data-*` attributes
- never select behavior by Tailwind utility classes
- use event delegation where it simplifies repeated controls
- keep behavior independent from visual Tailwind classes when possible
- use native HTML behavior before adding ARIA
- when a custom widget is unavoidable, implement its complete role, state, keyboard, focus, and announcement behavior
- use ARIA state attributes such as `aria-expanded`, `aria-selected`, and `aria-hidden` only when they accurately track behavior
- restore focus after closing dialogs and drawers
- avoid positive `tabindex` values
- avoid inline event attributes such as `onclick`, `onchange`, and `onsubmit`
- avoid large global scripts
- do not inject complete components or pages through `innerHTML`; keep product data serializable and markup structural
- update explicit state through `data-state` and accurate `aria-*` attributes so React can later derive the same output from component state

## Prototype state and mock actions

When no backend exists, use plain objects, arrays, URL parameters, and `localStorage`.

Example data service:

```js
const storageKey = 'prototype-projects';

export function listProjects() {
  return JSON.parse(localStorage.getItem(storageKey) ?? '[]');
}

export function saveProjects(projects) {
  localStorage.setItem(storageKey, JSON.stringify(projects));
}
```

Keep mock data in a clear `data/` or `assets/js/mock/` location. Do not scatter business data through unrelated event handlers.

Every simulated action must provide visible feedback. Announce asynchronous status changes when needed, preserve user input after recoverable errors, and document which actions are mock-only.

## Interaction implementation

All visible controls must be operational:

- navigation resolves to real HTML files
- forms validate required fields and show outcomes
- tabs use selected state and keyboard behavior
- dialogs and drawers open, close, trap focus when practical, and restore focus
- dropdown menus support keyboard access
- destructive actions require confirmation
- toasts and inline messages use consistent language
- loading actions prevent duplicate execution
- search, filter, sorting, and pagination affect mock content where shown

Prefer native elements such as `<button>`, `<a href>`, `<dialog>`, `<details>`, `<summary>`, `<select>`, and built-in form controls when they meet the interaction requirement.

Accessibility implementation rules:

- every form control has a visible label unless the visual context makes an equivalent accessible name unambiguous
- helper text and errors are programmatically associated with their fields
- form-level errors may use an error summary linked to invalid fields
- buttons inside forms declare `type`
- icon-only controls have an accessible name and visible tooltip when useful
- links opening a new tab use safe `rel` values and should disclose the behavior when it may surprise users
- custom dialogs manage initial focus, containment, Escape behavior, and focus restoration
- status messages use an appropriate live region only when native behavior does not expose the update
- decorative SVGs are hidden from assistive technology; informative SVGs have an accessible name
- touch controls should normally provide at least a 44×44 CSS-pixel interaction area unless dense operational context requires an explicitly justified alternative

## Page completeness

For every page define:

- purpose
- entry points
- primary action
- secondary actions
- required content/data
- loading state
- empty state
- error state
- success state
- responsive transformation
- accessibility risks

State examples may exist inside the main page, as dedicated state HTML files, or both, depending on what communicates the design most clearly.

## Responsive implementation

Test at minimum around:

- 360 px narrow mobile
- 390–430 px standard mobile
- 768 px tablet
- 1024–1280 px desktop
- 1440 px wide desktop when useful

These are review widths, not mandatory breakpoints.

Avoid:

- fixed heights around variable content
- absolute positioning for core document flow
- desktop controls that are too small for touch
- horizontal scrolling for primary forms
- compressed desktop sidebars on mobile
- tables that simply overflow without an intentional small-screen pattern

For mobile-first app-like designs, use bottom navigation, sheets, safe-area spacing, concise headers, and touch-friendly controls when appropriate. On larger screens, introduce columns, side navigation, persistent context, and denser controls only when useful.

## RTL and localization

- set `lang` and `dir` correctly
- use logical alignment and spacing
- isolate mixed-direction values such as email, code, phone, and URLs
- verify directional icons
- localize dates, numbers, currency, and plural forms
- do not mirror logos or neutral icons automatically
- test navigation, drawers, tables, charts, and form alignment in RTL

## Animation and 3D

Allowed focused libraries include:

- GSAP
- Three.js using vanilla JavaScript
- Lottie
- Lenis
- Swiper

Do not use React Three Fiber or framework wrappers.

Before adding heavy motion or 3D, document:

- user benefit
- loading strategy
- reduced-motion behavior
- mobile or low-power fallback
- mouse, touch, and keyboard behavior when interactive

Lazy-load heavy scripts. Decorative animation must not block the primary content or action.

## Images and assets

Use relevant, realistic content. When tools allow:

- research visual references without copying complete designs
- generate custom product-specific assets
- optimize formats and dimensions
- reserve image aspect ratios to prevent layout shift
- write useful alt text for informative images
- use empty alt text for decorative images

## CSS safety

- keep global base styles minimal
- avoid conflicting element selectors
- use one source of truth for theme values
- use `@layer` intentionally
- avoid large `@apply` abstractions
- keep state variants close to their HTML pattern
- avoid arbitrary raw colors when semantic tokens exist
- avoid excessive custom CSS that bypasses Tailwind without a clear reason

## Package and scripts

A minimal Tailwind CLI setup may use:

```json
{
  "scripts": {
    "dev:css": "tailwindcss -i ./assets/css/theme.css -o ./assets/css/output.css --watch",
    "build:css": "tailwindcss -i ./assets/css/theme.css -o ./assets/css/output.css --minify",
    "serve": "serve ."
  }
}
```

The exact command can vary with the installed Tailwind CSS v4 CLI package. The generated deliverable remains static HTML, CSS, JavaScript, and assets.

## Browser and accessibility verification

Static linting is only a preflight. When tools permit, verify representative critical flows with:

- keyboard-only navigation
- visible and unobscured focus
- 200% zoom and narrow reflow
- longer localized text and mixed RTL/LTR values
- reduced motion
- representative screen-reader output
- automated accessibility tools, followed by manual review of issues they cannot determine

Save material findings with severity, evidence, confidence, user impact, and verification criteria.

## Documentation

`README.md` must explain:

- product and prototype purpose
- page list
- folder structure
- how to install and build Tailwind
- how to serve the static files
- how to change the theme
- where interactions and mock data live
- which behaviors are simulated
- which backend integrations remain unimplemented


## React migration handoff

The prototype is not a React project. It must still include:

- `design-system/component-map.json`
- `docs/component-inventory.md`
- `docs/route-map.md`
- `docs/react-handoff.md`

For each reusable component record the future React name, semantic root, props/data, children/slots, variants, states, callbacks, source pages, mock data source, JavaScript controller, accessibility contract, and migration class.

For each page record its HTML file, intended future route, suggested page component, layout shell, data dependencies, and route-level state.

Migration classes:

- `direct`: semantic markup and Tailwind transfer with minor future framework syntax edits
- `state-rewrite`: DOM controller becomes React state/hooks
- `library-adapter`: focused JS library needs lifecycle integration or a React wrapper
- `backend-dependent`: real API/auth/storage integration remains
- `architecture-review`: routing, permissions, synchronized global state, or another application concern needs an explicit decision

See [react-readiness.md](react-readiness.md) for the complete contract and migration sequence.
