# SKILL: Test Plan Generator
Short: From a US + AC produce a detailed test plan: unit tests, integration tests, e2e scenarios, and coverage targets (>80%).

## When to use
- After US and acceptance criteria exist and before implementation starts.

## Input
- US markdown file path (with AC)
- Code areas in scope (file/module list)

## Output
- Unit test list: test name, objective, sample input/output, target module to test
- Integration/e2e scenarios with seed fixtures and success criteria
- Coverage guidance and which files to instrument to meet >80% target

## Steps
1. Validate `PRODUCT_CONTEXT`.
2. Parse AC and derive test cases (happy path + edge cases + negative).
3. Map each test to target module/file and testing framework (Vitest/Jest/Pytest).
4. Create example test skeletons or test vectors.

## Examples
Input: VTR calc AC
Output:
- Unit: "vtr_calc_handles_duplicate_scans" → input scans X → expected 0.8
- Integration: "csv_import_generates_alert" → seed CSV -> run ingestion -> assert alert created

## Failure modes
- If AC not explicit → return `needs_clarification`.
- If scope lacks code module mapping → request code owners.

## Invocation
`/run test-plan-generator --us=documentation/cadrages/.../01 - CSV Import.md`