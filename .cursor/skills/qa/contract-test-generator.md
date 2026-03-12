# SKILL: Contract Test Generator (OpenAPI/Pact)
Short: Generate contract tests from OpenAPI or interface spec to validate service boundaries.

## When to use
- When API contract exists or when frontend/back integration must be validated.

## Input
- OpenAPI snippet or endpoint spec
- Consumer expectations (example responses)

## Output
- Contract test files (consumer/provider) or pact-like artifacts
- Example stubs / mock server configs

## Steps
1. Validate PRODUCT_CONTEXT.
2. Parse OpenAPI and generate tests for successful + error cases.
3. Suggest mock server (MSW for frontend, wiremock/httpx-mock for backend).

## Invocation
`/run contract-test-generator --openapi=spec.yaml`