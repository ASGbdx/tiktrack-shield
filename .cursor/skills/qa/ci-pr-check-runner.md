# SKILL: CI PR Check Runner
Short: Composite skill invoked in PR checks to run a subset: metadata enforcer, unit tests, coverage check, security quick scan, design token validator.

## When to use
- As a GH Action / PR gating step.

## Input
- PR id or diff, env config for tests

## Output
- Pass/fail JSON, artifact links, remediation steps

## Steps
1. Validate PRODUCT_CONTEXT.
2. Run: pr-metadata-enforcer, unit-test-generator (dry-run), coverage-analyzer (if coverage present), security quick scan.
3. Return combined result and suggestions.

## Invocation
`/run ci-pr-check-runner --pr=123`