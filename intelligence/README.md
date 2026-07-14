# Optional Design Intelligence Sources

This directory may contain searchable design references such as product patterns, styles, palettes, typography candidates, chart guidance, UX rules, animation patterns, or anti-patterns.

These sources are optional and non-authoritative.

Rules:

1. A dataset is never a closed taxonomy.
2. User-defined and custom-generated directions have higher priority.
3. Absence from the dataset does not invalidate a choice.
4. Retrieved rows are raw evidence, not a final design system.
5. Do not automatically map an industry to a color, font, or named style.
6. Store the exact retrieved evidence in `design-profile.json` under `evidence.databaseInputs`.
7. Store original design decisions under `evidence.userInputs` and `evidence.customDecisions`.
8. Final tokens and rules belong in `design-system/MASTER.md`, not in the dataset.

Recommended optional files:

```text
product-rules.csv
style-references.csv
palette-references.csv
typography-references.csv
landing-patterns.csv
chart-guidance.csv
ux-rules.csv
animation-patterns.csv
anti-patterns.csv
```

Do not copy third-party datasets unless their license permits redistribution. The Skill works without these files by using product-grounded custom synthesis.
