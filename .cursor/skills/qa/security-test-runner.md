# SKILL: Security Test Runner
Short: Run or produce commands for dependency & container scanning (Trivy, Snyk), static checks (bandit/ruff).

## When to use
- As part of PR gating or periodic audits.

## Input
- Repo snapshot or image name, optional: scan depth

## Output
- Security scan report with prioritized findings and remediation hints
- CLI commands to reproduce scans locally

## Steps
1. Validate PRODUCT_CONTEXT.
2. Run quick vulnerability scan (or simulate results if offline).
3. Produce actionable remediation list.

## Invocation
`/run security-test-runner --image=my-app:latest --quick`