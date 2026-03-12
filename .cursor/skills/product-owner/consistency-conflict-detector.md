# SKILL: Consistency & Conflict Detector
Short: Scan a set of US/Epics for contradictions (UI tokens, wording, technical constraints) and report conflicts.

## When to use
- Before finalizing or merging a bundle of US/Epics.

## Input
- Paths to US / Epic markdown files
- Canonical design token file (optional) and UX constraints file

## Output
- Conflict report with severity: `minor|major|blocking`
- Suggested remediation (which US to modify or merge to resolve)
- Cross-reference examples showing exact conflicting lines

## Steps
1. Validate `PRODUCT_CONTEXT`.
2. Parse each US for token usages, color/background instructions, wording constraints, and API contracts.
3. Detect contradictions (e.g., US1 background=light vs US2 background=dark for same screen).
4. Produce actionable report with file lines and recommended changes.

## Examples
Input: US A uses `background: light token`; US B uses `background: dark token` for same route.
Output: conflict (blocking) with suggestion "unify to light token; move B to V2 or change wording".

## Failure modes
- If US files missing → return missing list.
- If ambiguous references (no route provided) → ask up to 3 clarifying questions.

## Invocation
`/run consistency-conflict-detector --paths=documentation/cadrages/01/**`