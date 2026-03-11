# SKILL: E2E Playwright Runner
Short: Orchestrate Playwright runs against staging/ephemeral envs and collect artifacts.

## When to use
CI pre-merge for critical flows (login, alert flow) or local QA.

## Input
- Scenario id(s) or test folder
- Environment config (staging URL, seeding instructions)

## Output
- Test results (pass/fail)
- Artifacts: traces, videos, screenshots
- Fail summary with failing step & logs

## Steps
1. Verify metadata: `PRODUCT_CONTEXT`, `scope`, `kpi_mapping`.
2. Prepare env (seed test shop via API or fixture).
3. Launch Playwright with retries.
4. Collect and upload artifacts.
5. Emit result JSON for CI.

## Examples
`/run e2e-playwright-runner --scenario=alert_flow --env=staging`

## Failure modes
- Env unreachable → return diagnostics (DNS, Caddy, Cloudflare issues).
- Seeding fail → return seed logs & remediation.

## Invocation
CI step or `/run e2e-playwright-runner --scenario=...`