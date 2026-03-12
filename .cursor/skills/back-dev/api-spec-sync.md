# SKILL: API Spec Sync
Short: Keep OpenAPI / API contract in sync with backend code when adding or changing endpoints.

## When to use
When implementing or reviewing new API routes, changing request/response schemas, or before release to ensure docs match code.

## Input
- OpenAPI spec path (e.g. `openapi.yaml`, `api-spec.json`) or contract file
- Changed or new route modules / FastAPI routers
- Optional: existing spec version and changelog policy

## Output
- Updated OpenAPI snippet or full spec diff (paths, schemas, examples)
- Checklist: paths present, request/response schemas, status codes, auth
- Breaking-change note if response shape or status codes changed
- Suggested changelog line for API version

## Steps
1. Ensure `PRODUCT_CONTEXT`, `scope`, `kpi_mapping`.
2. Parse existing OpenAPI (or note "no spec yet").
3. From code (FastAPI routers / Pydantic models), extract paths, methods, request/response bodies, status codes.
4. Diff against current spec; list added/changed/removed.
5. Emit updated spec fragment and breaking-change summary if needed.
6. Suggest version bump or changelog entry when contract changed.

## Examples
Input: New `POST /shops/{id}/alerts` in `app/api/alerts.py`
Output: New path in OpenAPI with `requestBody`, `responses.201`, `responses.422`, and schema refs.

## Failure modes
- No OpenAPI file → produce minimal spec skeleton and instructions to add to repo.
- Code and spec both changed elsewhere → show conflict list and ask which source is canonical.
- Async vs sync route mismatch → align with backend agent (FastAPI async by default).

## Invocation
`/run api-spec-sync --spec=openapi.yaml --routes=app/api/` or on PR that touches `app/api/` or `openapi.yaml`.
