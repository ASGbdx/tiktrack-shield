# SKILL: Coverage Analyzer
Short: Analyze coverage reports, identify hotspots, and recommend targeted tests to reach >80%.

## When to use
- After a test run to guide additional testing efforts.

## Input
- Coverage report (lcov / coverage.xml), target files/modules.

## Output
- List of uncovered functions/lines, prioritized test suggestions
- Estimated tests to add and impact on coverage

## Steps
1. Validate PRODUCT_CONTEXT.
2. Parse coverage report.
3. Map uncovered areas to features/US.
4. Produce prioritized test tasks.

## Invocation
`/run coverage-analyzer --report=coverage/lcov.info --target-modules=src/vtr*`