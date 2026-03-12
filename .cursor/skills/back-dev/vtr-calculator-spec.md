# SKILL: VTR Calculator Spec
Short: Produce canonical VTR calculation spec and JSON test vectors.

## When to use
When creating or changing VTR rules, or to generate test cases for backend logic.

## Input
- Window definition (e.g., last 30 days)
- Rule variations (min_scans=2, time_between_scans, carrier weighting)
- Edge-case notes

## Output
- Human-readable spec describing algorithm & edge cases
- JSON test vectors: list of inputs → expected VTR result
- Suggested unit-test cases

## Steps
1. Ensure `PRODUCT_CONTEXT`, `scope`, `kpi_mapping`.
2. Define inputs: orders, scans, timestamps, carriers.
3. Formalize calculation steps (filter, dedupe, per-order checks).
4. Provide edge-case rules (missing timestamps, duplicate scans).
5. Output spec + test vectors.

## Examples
Input: window=7d, min_scans=2
Output: Spec + sample events where result = 0.75

## Failure modes
- Missing event timestamp data → include normalization rules.
- If schema mismatch → link to CSV schema required.

## Invocation
`/run vtr-calculator-spec --window=7d --min-scans=2`