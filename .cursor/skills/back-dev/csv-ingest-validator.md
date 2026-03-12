# SKILL: CSV Ingest Validator
Short: Validate TikTok CSV exports, produce validation report and mapping to internal model.

## When to use
On CSV upload, PR adding a new CSV mapping, or during onboarding when users provide sample exports.

## Input
- CSV file (or sample rows)
- Optional: declared schema name (e.g., `tik_tok_export_v1`)

## Output
- JSON report: `{ valid: bool, errors: [...], warnings: [...], mapping: {internal_field -> csv_column} }`
- Example corrected CSV rows (small sample)
- Suggested JSON Schema for ingestion

## Steps
1. Check required metadata: `PRODUCT_CONTEXT`, `scope`, `kpi_mapping`.
2. Parse CSV header; compare against expected columns.
3. Validate types and sample rows (dates, tracking numbers).
4. Detect common issues (missing scans, null timestamps, mixed locales).
5. Propose mapping and sample fixes.
6. Return report and mapping file.

## Examples
Input: `orders.csv` with columns `order_id, carrier, last_scan_at`
Output: mapping `{ order_id: "order_id", carrier: "carrier", last_scan_at: "last_scan_at" }` and `errors: []`

## Failure modes
- Missing CSV or unreadable encoding → return error code and explain required encoding (UTF-8).
- If metadata missing → refuse and ask to include `PRODUCT_CONTEXT` etc.

## Invocation
- UI: invoked on file upload
- CLI / Cursor: `/run csv-ingest-validator path/to/sample.csv --schema=tik_tok_export_v1`