# SKILL: Integration Test Generator
Short: Create integration tests that wire components (DB, APIs, queues) to validate end-to-end behavior in an isolated env.

## When to use
- For US that require DB / multiple services interaction.

## Input
- US path, list of services, seed fixtures, preferred test runner

## Output
- Integration test scripts (tests/integration/...)
- Docker-compose or testcontainers snippet to provision ephemeral infra
- Seed scripts and fixtures
- Commands to run locally and in CI

## Steps
1. Validate PRODUCT_CONTEXT.
2. Create provisioning steps (testcontainers/docker-compose).
3. Generate integration test with seed -> action -> assertion.
4. Provide cleanup instructions.

## Invocation
`/run integration-test-generator --us=... --services=postgres,redis`