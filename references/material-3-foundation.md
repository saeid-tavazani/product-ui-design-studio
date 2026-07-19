# Material 3 Foundation

Use this reference before creating `design-profile.json`, `visual-system.md`, `tokens.json`, and HTML/Tailwind component contracts.

Source anchors:

- https://m3.material.io/
- https://m3.material.io/foundations
- https://m3.material.io/styles
- https://m3.material.io/components

## Responsibility

Use Material 3 as the UX/UI foundation for adaptive, accessible, coherent product interfaces. Do not copy the default Google look or treat Material as a preset theme.

## What To Borrow

- Color roles: primary, secondary, tertiary, surface, surface container, background, outline, error, success/custom status, and readable foreground pairs.
- State layers: hover, focus, pressed, selected, dragged, disabled, and loading feedback must be visible and consistent.
- Type scale: define display, headline, title, body, label, numeric, and code roles. Adapt font families to the brand.
- Shape: choose component shape by product context. Do not apply one radius to every component.
- Elevation: use tonal surfaces, borders, shadows, and overlays intentionally.
- Motion: make transitions purposeful, quick, interruptible, and respectful of reduced motion.
- Components: use M3 component anatomy as a checklist for expected states, roles, density, and accessibility.
- Adaptive layout: select navigation bars, rails, drawers, panes, grids, and safe areas by device and task frequency.

## Product-Specific Layer

After choosing the M3 baseline, create a project layer that can make the product distinctive:

- brand palette and semantic token mapping
- typography personality
- geometry rules for controls, containers, and decorative forms
- layout rhythm and density
- product-specific navigation model
- iconography and imagery direction
- signature element or signature interaction
- data visualization rules
- localized and cultural behavior

Reject any design that differs from a generic Material starter only through color, content, logo, or imagery.

## Token Mapping

Map every chosen color to semantic roles before implementation:

```json
{
  "m3": {
    "primary": "",
    "onPrimary": "",
    "primaryContainer": "",
    "onPrimaryContainer": "",
    "secondary": "",
    "onSecondary": "",
    "surface": "",
    "onSurface": "",
    "surfaceContainer": "",
    "outline": "",
    "error": "",
    "onError": ""
  },
  "productOverrides": {
    "brandAccent": "",
    "success": "",
    "warning": "",
    "info": "",
    "signatureSurface": ""
  }
}
```

Use OKLCH or accessible hex values. Recheck contrast whenever semantic roles change.

## Component Checklist

For each major component, define:

- M3 ancestor or closest anatomy reference
- project-specific override
- semantic element
- props and data contract
- variants and density modes
- state-layer behavior
- keyboard behavior
- accessible name or labeling rule
- responsive behavior
- reduced-motion behavior

## Creative Guardrail

Material 3 gives the grammar. The product gives the voice. If a healthcare triage app, luxury commerce site, developer tool, and industrial dashboard would all share the same typography, card shape, spacing, and navigation after recoloring, the design system is not finished.
