---
name: "Rule — Data Ingestion Standard"
version: "1.0"
product: "Guardlane"
updated: "2026-03-11"
summary: "Standard for ingestions (CSV, APIs). Versioned schemas, strict validation, clear error handling and fallback modes."
---

# Data Ingestion Standard — Quick Rule

**Purpose**  
Keep ingestion robust and debuggable (TikTok exports, carrier APIs, CSV fallback).

## Rule (must-follow)
1. Provide a versioned schema for each ingest source (e.g., `tik_tok_export_v1`).
2. Validate incoming payloads strictly; log and surface errors with clear codes.
3. Support fallback ingestion (CSV) if API not available.
4. Maintain mapping documentation and migration notes when schema changes.
5. Store raw original payloads (masked as needed) for debugging for a limited retention.

## Required artifacts
- Schema file (JSON Schema / OpenAPI snippet) with version.
- Validation & error code list.
- Mapping doc & transformation steps.
- Ingestion test with sample fixture.

## Minimal enforcement checklist
- [ ] Schema versioned & attached.
- [ ] Validation errors defined.
- [ ] Fallback mode documented.

## Programmatic snippet
```yaml
rule: data-ingestion
source: tik_tok_csv | carrier_api
schema_version: v1
validation: strict
fallback: csv
```