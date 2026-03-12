# SKILL: Design Token Validator
Short: Validate a UI component or CSS snapshot against canonical design tokens (colors, spacing, radius limit).

## When to use
During frontend PR review, Storybook checks, or QA.

## Input
- Component CSS/JSON snapshot or Storybook URL
- `DESIGN_TOKENS.json` (canonical, aligné sur le design system Guardlane — rule `design-system-guardlane.md`)

## Output
- Report: pass/fail, mismatched tokens, recommended token replacements
- Visual hints (which property lines to change)
- Radius check: ensure radius ∈ {xs, sm, md} and ≤ `radius.md`

## Steps
1. Ensure `PRODUCT_CONTEXT`, `scope`, `kpi_mapping`.
2. Parse component CSS / computed styles.
3. Map values to tokens; detect hard-coded values.
4. Flag mismatches and produce remediation snippet.

## Examples
Input: `button.css` with `border-radius: 12px` and `radius.md=8px`
Output: fail + "Use `--radius-md` (8px) instead of 12px"

## Failure modes
- Snapshot not accessible → return instructions to export CSS snapshot or Storybook capture.
- Token file missing version → request latest `DESIGN_TOKENS.json`.

## Invocation
`/run design-token-validator --snapshot=story-Button --tokens=DESIGN_TOKENS.json`