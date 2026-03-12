# SKILL: Performance Test Generator (k6)
Short: Create k6 scripts and scenarios for load / spike / soak tests for critical endpoints.

## When to use
- When performance SLOs or critical endpoints need verification.

## Input
- Endpoint(s), expected load (RPS), success criteria (p95, error rate)

## Output
- k6 script(s), run commands, suggested CI job, result parsing guidance
- Recommended thresholds to assert in CI

## Steps
1. Validate PRODUCT_CONTEXT.
2. Create scripts for baseline & stress tests.
3. Provide commands and thresholds to stop on violation.

## Invocation
`/run perf-test-generator --endpoint=/api/v1/ingest --rps=200`