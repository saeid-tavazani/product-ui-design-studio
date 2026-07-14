# UX, Accessibility, and Visual Evaluation

Use this reference after a representative flow exists and again before delivery.

## Review lenses

### Task and information architecture

- Can the primary user identify the next action without explanation?
- Are labels based on user language rather than implementation terms?
- Can users enter, complete, cancel, recover, and return?
- Is important content findable at the point of need?

### Interaction and feedback

- Does every action acknowledge input and expose progress, success, failure, and recovery?
- Are destructive and irreversible actions distinguishable and confirmed?
- Are controls visibly interactive without relying on hover?
- Is state preserved after recoverable errors?

### Accessibility preflight

Target WCAG 2.2 AA unless the brief specifies otherwise.

- native semantic HTML before ARIA
- skip link and landmarks on substantial pages
- logical heading, reading, and focus order
- visible focus and focus restoration
- labels, descriptions, error association, and error summary where useful
- keyboard operation for all interactive elements
- status messages announced when necessary
- sufficient contrast and non-color status cues
- zoom/reflow and text expansion
- reduced motion and low-power/static fallbacks
- RTL/LTR and mixed-direction behavior
- representative screen-reader spot checks

Automated tools are useful preflight checks but do not prove accessibility conformance.

### Visual and system quality

- clear focal sequence at full size and thumbnail scale
- consistent tokens and component states
- composition appropriate to density and device
- typography, imagery, icons, and motion share one design language
- the signature element helps identity or comprehension
- no unnecessary card, gradient, glass, shadow, or animation repetition

## Finding format

Every finding should include:

- severity: blocker, critical, major, minor, cosmetic
- category
- affected page, component, and user flow
- evidence or reproduction steps
- confidence: high, medium, low
- user impact
- recommendation
- verification criteria

Severity guidance:

- **blocker:** critical task cannot be completed or severe access failure has no workaround
- **critical:** likely failure, data loss, unsafe action, or broad accessibility barrier
- **major:** substantial confusion, friction, inconsistency, or recoverability problem
- **minor:** localized usability or consistency issue with a clear workaround
- **cosmetic:** visual polish with negligible task impact

Prioritize by severity, reach/frequency, confidence, and repair dependency. Do not hide critical UX problems inside a long list of cosmetic observations.
