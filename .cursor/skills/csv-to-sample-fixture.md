# SKILL: CSV → Test Fixture
Short: Convert real CSV rows into sanitized JSON fixtures for tests.

## When to use
When building unit/integration tests from real customer CSVs or carrier exports.

## Input
- CSV file
- PII masking rules (optional)

## Output
- JSON fixtures sanitized (PII masked)
- Fixture metadata: original_row_index -> fixture id
- Mapping summary

## Steps
1. Check `PRODUCT_CONTEXT`, `scope`, `kpi_mapping`.
2. Parse CSV and normalize fields (dates -> ISO, trim).
3. Apply PII mask rules (emails, phone numbers, names).
4. Output JSON fixtures and mapping file.

## Examples
Input: CSV with `tracking_no,scan_time`
Output: `fixtures/shopA/scan_events.json` with masked fields.

## Failure modes
- CSV with inconsistent columns → return list of offending rows.
- If PII masking rules absent → apply default minimal masking and warn.

## Invocation
`/run csv-to-sample-fixture --file=orders.csv --mask=default`