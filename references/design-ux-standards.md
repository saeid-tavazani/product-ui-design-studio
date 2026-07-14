# Design and UX Standards

## User ownership and database restraint

The user's visual direction has priority over style catalogs and industry presets. Databases may provide candidates, comparisons, UX evidence, and anti-patterns, but they must not narrow the design to listed styles, palettes, fonts, or industries.

When the user provides a custom idea:

- preserve the original words in the design profile
- derive missing semantic rules instead of replacing the idea
- keep exact colors unless an accessibility correction is necessary
- allow unnamed and hybrid styles
- document database influence separately from custom decisions
- verify that the final design still reflects the user's language

A design is weak when its identity is only the nearest catalog result or a standard industry palette.

## Ground the visual system in the subject

Identify the product's real-world materials, tools, rhythms, environments, and language. Use them to inform hierarchy, geometry, imagery, interactions, and copy. Do not copy surface aesthetics from competitors.

Examples:

- logistics may suggest routes, manifests, status transitions, and operational density
- fitness may suggest cadence, measurable progress, body movement, and energetic contrast
- finance may require trust, precision, comparison, and controlled density
- education may emphasize progression, comprehension, feedback, and continuity

## Aesthetic thesis

The design direction must be expressible in one sentence that connects visual behavior to product purpose.

Weak: “Modern dark SaaS interface.”

Better: “A focused training cockpit that uses controlled red accents and measured motion to make progress feel physical without becoming aggressive.”

## Palette

Define semantic roles before component colors:

- background
- surface
- elevated surface
- foreground
- muted foreground
- primary
- primary foreground
- border
- success
- warning
- danger
- focus ring

Use a brand seed to derive hover, active, soft, and border variants. Verify text contrast. Do not use opacity as the only disabled-state signal.

## Typography

Select typefaces by role:

- display: identity and major statements
- body: long-form readability and UI text
- utility/data: labels, metrics, code, timestamps, tabular numbers

Use at most three families. Define a deliberate type scale, line height, and measure. For Persian/Arabic interfaces, verify glyph quality, numeral behavior, punctuation, and mixed LTR content.

## Layout

Design mobile first unless the product is explicitly desktop-first. Mobile-first means prioritizing the mobile task model, not shrinking desktop.

Use structural devices only when they encode meaning. Numbered sections require an actual sequence. Dividers should clarify grouping. Cards should represent real conceptual containers, not become the default wrapper for every element.

Avoid excessive centered layouts. Long-form content, operational tools, and navigation often need asymmetric or edge-aligned compositions.

## Signature element

Choose one memorable device tied to the product:

- an interactive route for logistics
- a live training ring for fitness
- a timeline that doubles as navigation for a project portfolio
- a spatial product model for a physical object

The signature must support comprehension, orientation, confidence, or action. Keep surrounding visuals quieter.

## Motion

Define motion by purpose:

- orientation: shows where content came from or where it went
- feedback: confirms an action
- continuity: connects states
- demonstration: explains a product or process
- atmosphere: supports brand tone

Prefer one orchestrated moment plus functional micro-interactions. Respect `prefers-reduced-motion`. Avoid animating large layout properties when transform/opacity can achieve the same purpose. Heavy motion and 3D must be lazy-loaded and have static fallbacks.

## Content design

Use plain, stable action language. Match button, progress, toast, and history wording.

Bad:
- Submit
- Something went wrong
- No data

Better:
- Save address
- We could not load your orders. Check your connection and retry.
- No saved addresses. Add one to complete checkout faster.

## Forms

- visible labels; placeholders are examples, not labels
- helper text before errors when possible
- errors adjacent to fields and summarized when forms are long
- appropriate input modes and autocomplete attributes
- preserve user input after validation failure
- disable submission only when the reason is clear
- show progress for long operations

## Data-heavy interfaces

- prioritize scan paths and comparison
- align numeric data and use tabular numerals
- preserve filters in URLs or local state when useful
- provide empty, loading, error, and partial-data states
- adapt tables on small screens through prioritization, disclosure, or alternate layouts—not horizontal overflow by default

## Accessibility floor

- semantic landmarks and heading order
- keyboard-accessible actions
- visible focus styles
- labels and accessible names
- adequate contrast
- touch targets appropriate for mobile
- reduced-motion support
- no meaning communicated by color alone
- status updates announced when necessary
- logical reading and focus order in RTL and LTR

## Genericity rejection test

Reject or revise a design when three or more are true without clear product justification:

- generic purple/blue gradient hero
- every section is a rounded card
- centered heading followed by three equal feature cards
- large metric tiles unrelated to the primary job
- decorative glassmorphism
- random 01/02/03 labels
- default Inter/Poppins typography
- vague marketing copy
- animations on every element
- 3D decoration unrelated to product comprehension
