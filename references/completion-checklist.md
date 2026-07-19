# Completion Checklist

Do not claim the project is complete until relevant checks pass.

## Product and scope

- [ ] The primary user, problem, and core flow are explicit.
- [ ] Every requested feature is implemented, phased, or explicitly excluded.
- [ ] MVP is a complete vertical journey, not a collection of disconnected screens.
- [ ] Later phases have page/feature mappings.
- [ ] Contradictions and assumptions are documented.
- [ ] User-defined visual ideas are preserved in the design profile.
- [ ] Visual System Derivation is complete before page implementation.
- [ ] `visualSystem.themeFingerprint` exists in `design-profile.json`.
- [ ] `visualSystem.derivedDimensions` contains unique values.
- [ ] Concept-tier work has at least five derived dimensions; standard and complete work have at least eight.
- [ ] The visual rationale is product-specific and not generic phrasing alone.
- [ ] Signature element is defined and tied to product meaning.
- [ ] Distinctiveness checks are completed.
- [ ] The design remains distinct in grayscale and without logo/images.
- [ ] Intentional similarity to an existing brand or product family is documented when applicable.
- [ ] Database suggestions did not silently override user decisions.
- [ ] Research findings, direct statements, secondary evidence, and assumptions are clearly separated.
- [ ] Assumption-based personas are labeled as proto-personas.
- [ ] Critical flows include failure and difficult/assisted paths when relevant.

## Information architecture

- [ ] Every page has a clear purpose.
- [ ] Navigation labels match user language.
- [ ] Primary and secondary actions are distinguishable.
- [ ] Users can enter, complete, cancel, and return from critical flows.
- [ ] 404, error, and required legal/system surfaces exist when relevant.

## Interaction

- [ ] No dead buttons or links.
- [ ] Forms validate and preserve input after errors.
- [ ] Loading, empty, error, success, disabled, and destructive states exist where relevant.
- [ ] Dialogs, menus, and drawers are keyboard usable.
- [ ] Feedback uses consistent action vocabulary.
- [ ] Error copy explains recovery and preserves entered data when possible.
- [ ] Important controls and states use the documented product vocabulary.
- [ ] Mock actions are clearly isolated from real integrations.
- [ ] Reusable interaction state is expressed through documented `data-state`/`aria-*` contracts rather than presentational Tailwind class selectors.
- [ ] Inline event handlers and large `innerHTML` component injection are absent.

## Visual system

- [ ] Colors come from semantic tokens.
- [ ] Changing the brand seed updates brand-dependent UI.
- [ ] Typography roles and scale are consistent.
- [ ] Spacing, radius, borders, and elevation follow a defined system.
- [ ] Geometry, elevation, and motion differ from the starter system unless explicitly justified.
- [ ] Component anatomy follows the Theme Fingerprint rather than a universal card/button style.
- [ ] Layout model follows tasks and content hierarchy rather than the default hero/cards or dashboard/table pattern.
- [ ] The design has one product-specific signature element.
- [ ] Decorative effects are justified and restrained.
- [ ] Copy is specific to the actual product.
- [ ] The design is not merely an industry-to-preset mapping.
- [ ] Custom or hybrid styles remain allowed even when absent from reference datasets.
- [ ] Design dials and page overrides are documented.
- [ ] Supplied references have take/reject notes and the final design does not clone one source.
- [ ] Reusable components include a documented state and accessibility matrix.
- [ ] Meaningful reusable units have stable `data-component` names and matching component contracts.
- [ ] Props/data, variants, states, actions/callbacks, slots, and migration classes are documented for later React conversion.
- [ ] Motion values come from shared tokens rather than page-specific improvisation.

## Responsive behavior

- [ ] Tested on narrow mobile, standard mobile, tablet, desktop, and wide desktop where relevant.
- [ ] Navigation changes appropriately by viewport.
- [ ] Tables and dense data have a deliberate small-screen pattern.
- [ ] Touch targets and control spacing are usable.
- [ ] No unintended horizontal overflow.
- [ ] No clipped text or fixed-height content failures.

## Accessibility

- [ ] Semantic landmarks and heading order.
- [ ] Visible focus states.
- [ ] Accessible names and labels.
- [ ] Sufficient contrast.
- [ ] Color is not the only status signal.
- [ ] Reduced-motion support.
- [ ] Logical focus and reading order.
- [ ] RTL/LTR and mixed-direction content tested when applicable.
- [ ] Skip navigation, landmarks, focus movement/restoration, and status announcements are checked where relevant.
- [ ] Critical flows have a manual keyboard pass and representative screen-reader spot check when tools permit.
- [ ] Layout survives zoom/reflow and longer localized strings.

## Performance

- [ ] Images are sized and optimized.
- [ ] Heavy libraries are justified and lazy-loaded.
- [ ] 3D/motion has static or low-power fallback.
- [ ] No unnecessary layout shift.
- [ ] Primary content and action are not blocked by decorative assets.

## Code quality

- [ ] Clear project structure.
- [ ] Shared primitives are reused without over-abstraction.
- [ ] Behavior hooks use stable `data-*` attributes, not Tailwind utility selectors.
- [ ] Repeatable business data is serializable and separated from DOM markup when appropriate.
- [ ] Storage/mock services are separate from DOM controllers.
- [ ] No scattered raw brand colors.
- [ ] No conflicting global CSS rules.
- [ ] Tailwind compilation and static-file serving succeed.
- [ ] No prohibited framework, JSX, TSX, or SPA routing exists.
- [ ] Every screen is available as a real HTML file.
- [ ] Run and theme instructions are documented.

## Final handoff

- [ ] Source files included.
- [ ] Implemented page and flow inventory included.
- [ ] Phase map included.
- [ ] `design-profile.json`, `MASTER.md`, and relevant page overrides included.
- [ ] Theme customization documented.
- [ ] Backend/mock boundaries documented.
- [ ] Limitations are stated accurately.
- [ ] Review findings are prioritized by severity and include evidence, confidence, impact, and verification criteria.
- [ ] Deferred design debt is explicitly recorded rather than silently omitted.
- [ ] `component-map.json`, component inventory, route map, and React handoff are included.
- [ ] Every migration item is classified as direct, state-rewrite, library-adapter, backend-dependent, or architecture-review.
- [ ] The handoff states clearly that React conversion is not fully automatic.
