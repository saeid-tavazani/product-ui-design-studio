# Visual System Derivation

Use this reference after product discovery and before implementation. The goal is cross-project diversity with within-project consistency: every project receives one coherent product-specific visual system, and different products do not inherit the same default system unless the user intentionally asks for brand-family continuity.

## Mandatory Stage

Create a **Visual System Derivation** artifact before writing pages. It must explain how the system follows:

- product category
- audience
- user goals
- brand personality
- content type
- platform and device priority
- interaction model
- supplied references
- accessibility requirements
- cultural and localization context

Reject generic rationale such as “modern and clean,” “professional,” “user-friendly,” “beautiful,” or “minimal and elegant” unless it is followed by concrete decisions for typography, geometry, density, surface, motion, and composition.

## Archetype Selection

Select a visual archetype based on the product, audience, task frequency, content type, brand personality, and interaction complexity. Do not default to minimalism when another visual language better supports the product.

Allowed starting points include:

- editorial
- operational
- industrial
- luxury
- playful
- educational
- expressive
- technical
- institutional
- calm-service
- retail
- media-rich
- community-oriented
- developer-tool
- spatial
- data-dense
- custom

Treat archetypes as reasoning prompts, not presets.

## Required Dimensions

For standard and complete projects, derive at least eight unique dimensions. For concept-tier projects, derive at least five. Changing only colors never satisfies this requirement.

Useful dimensions:

- color
- typography
- geometry
- spacing
- density
- surface treatment
- borders
- elevation
- composition
- navigation
- imagery
- iconography
- motion
- data visualization
- content rhythm
- interaction emphasis

## Theme Fingerprint

Add this structure to `design-profile.json` before implementation:

```json
{
  "visualSystem": {
    "id": "unique-project-visual-system-id",
    "archetype": "industrial",
    "rationale": "Specific product-linked explanation.",
    "themeFingerprint": {
      "designArchetype": "industrial-operational",
      "paletteModel": "cool neutral surfaces with amber status accents",
      "typographyModel": "compact grotesk with tabular numeric emphasis",
      "geometryModel": "sharp controls and slightly rounded containers",
      "spacingModel": "compact horizontal rhythm with moderate vertical separation",
      "surfaceModel": "flat bordered surfaces",
      "borderModel": "high-clarity one-pixel borders",
      "elevationModel": "minimal elevation used only for overlays",
      "layoutModel": "dense modular workspace",
      "navigationModel": "persistent side navigation",
      "imageryModel": "functional diagrams and product screenshots",
      "iconographyModel": "outlined technical icons",
      "motionModel": "fast functional transitions",
      "densityModel": "compact",
      "signatureElement": "status rail with operational color coding"
    },
    "derivedDimensions": ["color", "typography", "geometry", "density", "surface treatment", "borders", "composition", "motion"],
    "rejectedGenericPatterns": ["header-hero-three-cards-cta", "medium rounded cards everywhere"],
    "referenceInfluence": [
      {
        "source": "supplied screenshot",
        "take": "dense comparison rhythm",
        "reject": "low-contrast gray text"
      }
    ],
    "distinctivenessChecks": {
      "distinctInGrayscale": true,
      "distinctWithoutLogoOrImages": true,
      "typographyGeometrySpacingSpecific": true,
      "navigationMatchesUsage": true,
      "statesMatchArchetype": true,
      "transferToUnrelatedProductWouldFeelWrong": true,
      "notes": "The workspace density and status rail would not suit a children’s learning app."
    },
    "similarityIntent": {
      "intentional": false,
      "reason": "",
      "referenceSystem": ""
    }
  }
}
```

`themeFingerprint.signatureElement` is required. `visualSystem.id` must be unique. `derivedDimensions` must contain unique values.

## Visual Alternatives

When the user has not supplied a strong visual direction, generate three meaningfully different directions and select or recommend one. Each direction must differ in at least five dimensions and must not be a color variant.

| Dimension | Direction A | Direction B | Direction C |
|---|---|---|---|
| Layout | Asymmetric editorial | Dense modular workspace | Full-width spatial sequence |
| Typography | Serif-led display | Compact neutral grotesk | Condensed technical display |
| Geometry | Sharp editorial rules | Subtle operational corners | Mixed spatial panels |
| Surface | Paper-like flat sections | Bordered panels | Layered depth planes |
| Density | Spacious | Compact | Balanced |
| Motion | Restrained reveals | Fast functional feedback | Spatial transitions |

When the user already provides a clear direction, do not generate unnecessary alternatives.

## Layout Diversity

Do not automatically generate this website pattern for every site:

```text
header -> hero -> three feature cards -> statistics -> CTA -> footer
```

Do not automatically generate this application pattern for every app:

```text
sidebar -> top bar -> four metric cards -> data table -> modal
```

Before implementation, define:

```json
{
  "layoutModel": {
    "contentStructure": "",
    "navigationPattern": "",
    "gridBehavior": "",
    "hierarchyStrategy": "",
    "responsiveTransformation": "",
    "reasoning": ""
  }
}
```

The layout must follow user tasks and content hierarchy, not common template habits.

## Component Anatomy Variation

Component anatomy must follow the Theme Fingerprint. Do not assume the same radius, padding, shadow, icon position, card header, button shape, input shape, or surface style for every project.

Examples:

- editorial projects may use section dividers instead of cards
- operational dashboards may use dense rows and bordered panels
- luxury projects may use typography and whitespace instead of visible containers
- playful products may use irregular geometry and expressive states
- developer tools may use compact technical controls
- mobile services may use large touch targets and bottom navigation

## Typography Model

Define role hierarchy, display typography, body typography, UI typography, numeric typography, code typography when applicable, line-height model, letter-spacing model, text density, and responsive behavior. Heading size alone does not count as typography differentiation.

## Geometry Model

Do not define one universal radius scale. Define:

```json
{
  "geometryModel": {
    "controls": "sharp | subtle | rounded | pill | mixed",
    "containers": "sharp | subtle | rounded | mixed",
    "decorativeShapes": "",
    "rationale": ""
  }
}
```

Prevent all projects from becoming medium-rounded card systems by default.

## Elevation Model

Choose one:

- flat
- bordered
- soft-shadow
- layered
- floating
- inset
- mixed

Use elevation intentionally. Do not apply shadows to every card.

## Motion Model

Choose one:

- none
- restrained
- functional
- expressive
- spatial

Define durations, easing, distance, entrance behavior, feedback behavior, navigation transitions, and reduced-motion fallback. Do not reuse one fade-and-slide animation for all projects.

## Anti-Recolor Validation

A generated design is invalid when it differs from the starter system or previous project only through color, content, logo, imagery, or dark/light mode.

At least five major visual-system dimensions must differ from a generic starter. Standard and complete projects require at least eight explicitly derived dimensions.

Ask:

- Would the project still look distinct in grayscale?
- Would it remain distinct if the logo and images were removed?
- Are typography, geometry, spacing, surfaces, and composition product-specific?
- Does the navigation model match the product usage?
- Are component states visually consistent with the selected archetype?
- Could this exact design system be moved to an unrelated product without appearing inappropriate?

If the final question is answered “yes,” revise the direction.

## Product-Category Mismatch Review

Check for mismatches:

- a medical service should not automatically use gaming-style neon visuals
- an enterprise dashboard should not automatically use oversized marketing cards
- a luxury product should not use generic SaaS component styling
- a children’s educational app should not inherit dense enterprise spacing
- a developer tool should not use decorative motion that slows expert workflows
- a mobile-first service app should not behave like a desktop marketing website

## Intentional Similarity

User-provided direction, references, logos, brand systems, and explicit aesthetic constraints remain highest priority. Do not force artificial difference when the user wants continuity with an existing brand, previous product, design system, reference application, or company product family. Document intentional similarity with:

```json
{
  "similarityIntent": {
    "intentional": true,
    "reason": "Part of the same product suite.",
    "referenceSystem": "Existing Acme admin design system"
  }
}
```

