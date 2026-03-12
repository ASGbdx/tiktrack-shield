# SKILL: E2E Orchestrator (Playwright)
Short: Generate Playwright scenarios, orchestrate running them, collect artifacts.

## When to use
- For critical user journeys (alert generation, login & onboarding).

## Input
- Scenario description (Given/When/Then), env config (staging/ephemeral)

## Output
- Playwright test files under `playwright/tests/`
- Runner commands and env seeding steps
- Artifact collection (videos, traces, screenshots)

## Steps
1. Validate PRODUCT_CONTEXT.
2. Create scenario script with explicit selectors and test IDs.
3. Provide commands to run headless / headed.
4. Optionally provide GH Action snippet for E2E run.

## Invocation
`/run e2e-orchestrator --scenario=alert_flow --env=staging`