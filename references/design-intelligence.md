# Design Intelligence and Open-Ended Synthesis

Use this reference when interpreting visual preferences, consulting design databases, generating directions, or resolving palette and typography decisions.

## Core rule

A design database is a library, not a boundary.

The final direction may be:

- exactly described by the user
- a modified or expanded version of the user's idea
- a hybrid of multiple references
- a newly invented style without a standard name
- derived from the subject's real environment, tools, materials, movement, and language
- informed by database patterns without matching a stored record

Do not reduce a custom idea to the nearest named style.

## Source precedence

1. Explicit user decisions
2. Existing brand assets and supplied visual references
3. Product requirements and user behavior
4. Co-created decisions
5. Custom synthesis
6. Database search results
7. General defaults

When sources conflict, preserve the higher-priority source unless it creates an accessibility or usability failure. Explain the issue and propose the smallest correction.

## What design databases are good for

Use structured collections to:

- discover relevant interaction patterns
- compare common industry conventions
- find palette relationships and contrast starting points
- suggest type roles and language coverage
- identify chart types suitable for a data relationship
- surface UX rules and common failure modes
- generate alternatives when the user has no visual starting point
- challenge a weak direction with a contrasting option

Do not use them to:

- declare that only listed styles are valid
- automatically map an industry to one color
- copy a complete preset unchanged
- replace the user's palette with a popular palette
- make every product in one category look alike
- produce a design solely by nearest-neighbor matching

## Open design vocabulary

Treat style as a set of dimensions rather than a finite list of names.

Useful dimensions include:

- emotional tone: calm, assertive, playful, ceremonial, technical, intimate, urgent
- geometry: rectilinear, rounded, chamfered, organic, modular, irregular
- contrast: soft, moderate, high, luminous, monochromatic
- material character: paper, metal, glass, rubber, fabric, stone, light, ink, screen phosphor
- information density: spacious, balanced, dense, operational
- editoriality: interface-led, content-led, editorial, cinematic, data-led
- motion character: still, responsive, rhythmic, physical, elastic, cinematic
- image behavior: absent, documentary, illustrative, diagrammatic, 3D, generative
- surface behavior: flat, layered, bordered, textured, translucent, spatial
- temporal character: timeless, contemporary, retro-future, archival, seasonal

A direction can combine these dimensions without needing a recognized style label.

## User-owned direction protocol

When the user provides a direction:

1. quote or preserve its key terms in the design profile
2. identify what is complete and what remains undefined
3. infer only the missing dimensions
4. ask one high-impact visual question if necessary
5. derive semantic tokens and rules from the user's language
6. document any accessibility correction separately

Example:

User input:

> Dark navy, copper accents, no gradients, feels like nautical instruments but not vintage.

Do not map this to “dark luxury dashboard.” Instead derive:

- instrument-like precision and calibrated ticks
- matte navy surfaces
- copper only for active or meaningful signals
- contemporary typography
- restrained depth and no faux-aged textures
- a signature navigation or progress indicator inspired by bearings

## Custom synthesis algorithm

When generating a new direction:

1. Identify the product's subject and primary user action.
2. List real materials, tools, environments, rhythms, and vocabulary from that subject.
3. Select one useful metaphor, not several decorative metaphors.
4. Translate it into hierarchy, geometry, spacing, typography, color, imagery, and motion.
5. Add design dials: variance, motion, density.
6. Check against industry conventions only after the custom concept exists.
7. Borrow conventions that improve comprehension; reject conventions that erase identity.
8. Run a genericity test against at least two unrelated product categories.
9. Remove one decorative choice.
10. Record the result in `design-profile.json` and `MASTER.md`.

## Palette generation

The user may provide:

- one seed color
- several exact colors
- a verbal color idea
- a material or environmental reference
- a screenshot or logo
- no palette direction

Rules:

- Exact user colors remain the source colors unless readability requires correction.
- Generate semantic variants such as hover, active, soft, border, focus, and foreground.
- Separate brand colors from status colors.
- Do not infer “industry standard” colors when the user has a stronger concept.
- A palette does not need to resemble an existing database row.
- Use OKLCH or another perceptual model for derived relationships when practical.
- Document original input colors and adjusted accessible colors separately.

## Typography generation

Font databases provide candidates, not compulsory pairings.

Select fonts based on:

- language and glyph coverage
- body readability
- brand voice
- numeric and tabular needs
- loading cost and licensing
- display/body contrast
- mixed RTL/LTR behavior

A user may request a font outside the database. Validate it and use it when suitable.

## Direction comparison

When alternatives are necessary, ensure they differ structurally, not only by palette.

Each direction should vary at least three of:

- layout model
- typography character
- geometry
- color logic
- density
- image strategy
- motion character
- signature element

Always include an explicit custom path:

> Or describe a different direction in your own words; it does not need to match these options.

## Anti-generic review

Reject or revise a direction when:

- it is only an industry-to-preset mapping
- its identity depends only on changing the primary color
- the same hero, card grid, metric row, and gradient could serve unrelated products
- the copy and imagery are generic
- the signature element has no product meaning
- the user language disappeared from the final system
- the database label is more visible than the product idea
