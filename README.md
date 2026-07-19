# Product UI Design Studio

This skill turns proposals, rough ideas, screenshots, and existing interfaces into complete Figma-replacement product design prototypes.

Default output:

- semantic multi-page HTML
- Tailwind CSS v4 with project-specific semantic tokens
- vanilla JavaScript ES modules for prototype interactions
- Material 3 as a UX/UI foundation
- React-readiness handoff documents for a later separate implementation

The prototype itself must not contain React, Next.js, JSX, TSX, TypeScript, SPA routing, or framework component files.

Useful resources:

- `SKILL.md`: primary workflow and rules
- `PROMPT.md`: compact prompt version
- `references/prototype-implementation.md`: HTML/Tailwind/vanilla JS implementation standards
- `references/react-readiness.md`: static prototype contracts for later React migration
- `references/react-product-handoff.md`: final handoff guidance
- `scripts/audit_project.py`: preflight for generated static prototypes
- `templates/package.static.json`: minimal static/Tailwind package template
