# SKILL: Unit Test Generator
Short: Produce unit test skeletons or complete tests for a given module/function.

## When to use
- Given a User Story with AC and a target module/file list.

## Input
- US file path or description
- Target module(s) or function names
- Preferred framework (vitest/jest/pytest)

## Output
- Unit test files (copy-pasteable) under `tests/unit/...`
- Test vectors JSON for each test
- Coverage guidance (which lines to instrument)

## Steps
1. Validate PRODUCT_CONTEXT metadata.
2. Parse AC and map to functions/modules.
3. Generate 3–8 tests: nominal, edge cases, error path.
4. Return YAML summary and file list.

## Example invocation
`/run unit-test-generator --us=... --framework=vitest --targets=src/utils/vtr.ts`

## Failure modes
- Missing AC → ask up to 3 clarifying questions.