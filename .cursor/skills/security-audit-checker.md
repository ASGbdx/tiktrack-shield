# SKILL: Security Audit Checker
Short: Run quick security checks (dependency scan, config flags) and produce remediation list.

## When to use
Before merge of infra/backend changes, or periodically.

## Input
- Repo snapshot or lockfile (`package.json`/`pyproject.toml`)
- Optional: Dockerfile, Caddyfile, infra configs

## Output
- Report: dependency vulnerabilities, insecure configs, secrets in repo
- Suggested fixes with priority (critical/high/medium)
- Command list to reproduce scans (Trivy, ruff, bandit)

## Steps
1. Verify `PRODUCT_CONTEXT`, `scope`, `kpi_mapping`.
2. Run dependency scanner on lockfile (simulate via rules if offline).
3. Lint Dockerfile/Caddyfile for common pitfalls.
4. Scan diffs for accidental secrets (regex).
5. Output remediation guidance.

## Examples
Input: `Dockerfile` with `USER root`
Output: flag + "Run as non-root and add explicit user"

## Failure modes
- Offline environment → return checklist and commands to run locally.
- No lockfile → require list of dependencies.

## Invocation
`/run security-audit-checker --path=. --quick`