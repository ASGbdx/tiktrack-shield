# SKILL: Flaky Test Detector
Short: Detect flaky tests by analyzing historical CI runs (retry patterns) and annotate tests with flakiness level.

## When to use
- In CI evaluation or PR triage for unstable tests.

## Input
- CI run history (last N builds) or test results with timestamps

## Output
- Flaky test list with frequency, suggested mitigation (fix, isolation, retry)
- GH Action snippet to block merges if flakiness > threshold

## Steps
1. Validate PRODUCT_CONTEXT.
2. Analyze test outcomes across runs.
3. Flag tests with inconsistent outcomes.
4. Recommend fixes (increase timeouts, mock external calls).

## Invocation
`/run flaky-test-detector --ci-history=./ci/history.json --threshold=0.05`