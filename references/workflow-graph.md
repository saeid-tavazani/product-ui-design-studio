# Workflow Graph

Use for complete-tier, more than five routes, more than two roles, multiple primary flows, high ambiguity, or long-running product design tasks. Keep this graph private unless process detail helps the user.

## Rules

- Use node IDs to reduce repeated stage narration.
- Load detailed references only when a gate needs them.
- Do not skip creative synthesis, Material 3 grounding, accessibility, or validation.

## Nodes

```text
N0 intake
in: prompt, proposal, files, refs
out: facts, assumptions, contradictions, risks
gate: enough context to ask or proceed
next: N1 if blocked, else N2

N1 discovery
out: one answer or documented assumption
gate: highest-impact ambiguity resolved
next: N2

N2 scope
out: routes, flows, states, exclusions, mocked boundaries
gate: build scope explicit
next: N3

N3 contract
out: product statement, users, roles, JTBD, success criteria, phase map
gate: evidence separated from assumptions
next: N4

N4 visual
out: design-profile.json, theme fingerprint, visual-system.md, tokens
gate: M3 baseline, product overrides, signature element, anti-recolor pass
next: N5

N5 architecture
out: static HTML/Tailwind structure, component map, mock data plan, JavaScript module plan
gate: page, component, state, interaction, and service ownership clear
next: N6

N6 build
out: HTML pages, theme.css, interactions, mock services
gate: no dead actions; critical states present
next: N7

N7 validate
out: audit results, responsive/accessibility review, fixes
gate: blocker/critical issues fixed or reported
next: N8

N8 handoff
out: route map, component inventory, data contracts, mocked integrations, future React conversion plan
gate: client can review; engineers can plan production
```

## Reference Map

```text
N0/N1 -> concise-discovery.md; discovery-framework.md when needed
N3 -> research-validation.md when claims or personas matter
N4 -> material-3-foundation.md; design-intelligence.md; visual-system-derivation.md
N5/N6 -> prototype-implementation.md
N7 -> ux-evaluation.md; completion-checklist.md
N8 -> react-product-handoff.md
```

## Compact Marker

```text
done: N0,N1
active: N2
risk: unclear permissions
assume: mobile-first
next: route/state inventory
```

Skip this file for small concept sketches, single-screen edits, tiny reviews, or direct questions.
