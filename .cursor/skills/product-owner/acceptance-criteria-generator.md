# SKILL: Acceptance Criteria Generator
Short: Generate clear Given/When/Then acceptance criteria from US description.

## When to use
- After a US draft is produced or when acceptance criteria are missing/weak.

## Input
- US description text (1–3 paragraphs)
- Optional: examples / edge cases

## Output
- Structured AC block (Given / When / Then) with 3–6 testable criteria
- Suggested test vectors (input → expected output) for at least 1 acceptance case

## Steps
1. Validate `PRODUCT_CONTEXT`.
2. Extract actors, preconditions, actions, outcomes from text.
3. Produce 3–6 ACs with explicit measurable outcomes.
4. Optionally produce 1–3 JSON test vectors.

## Examples
Input: "Import CSV and compute per-order scan counts"
Output:
- Given CSV with orders X...
- When import runs...
- Then per-order scan count >= 2 for order Y

## Failure modes
- Vague descriptions → return up to 3 clarifying questions.
- Contradictory constraints detected → mark US `INCONSISTENT`.

## Invocation
`/run acceptance-criteria-generator --us="Import CSV and compute per-order scan counts"`