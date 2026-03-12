# SKILL: Fixture Generator (sanitizer)
Short: Convert real CSV / logs into sanitized test fixtures JSON, with PII masking.

## When to use
- When building tests from production-like data or user-provided CSV.

## Input
- CSV or JSON file, PII mask rules (optional)

## Output
- Sanitized fixtures under `tests/fixtures/...`
- Mapping file (original_row -> fixture id)
- Masking report

## Steps
1. Validate PRODUCT_CONTEXT.
2. Parse and normalize values (date -> ISO).
3. Apply PII masks.
4. Emit JSON fixtures and mapping.

## Invocation
`/run fixture-generator --file=sample.csv --mask=default`