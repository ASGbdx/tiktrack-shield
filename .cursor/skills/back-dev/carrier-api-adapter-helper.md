# SKILL: Carrier API Adapter Helper
Short: Scaffold carrier API client stub, contract, and sample responses.

## When to use
When implementing a new carrier connector (e.g., USPS, UPS) or reviewing carrier integration PRs.

## Input
- Carrier name
- Link to API docs or sample API responses (optional)
- Desired features (tracking status, scan history)

## Output
- Client stub (pseudo-code / interface) in preferred language
- Contract JSON (example endpoints + request/response shapes)
- Sample fixtures (success, transient error, not-found)
- Retry/backoff & idempotency recommendations

## Steps
1. Validate metadata: `PRODUCT_CONTEXT`, `scope`, `kpi_mapping`.
2. Parse provided API docs or sample response.
3. Generate minimal client contract: `GET /tracking/{id}` → response schema.
4. Provide sample responses (ok, partial, fail).
5. Provide idempotency & retry guidance (HTTP codes -> action).

## Examples
Input: "Carrier: UPS, need last 7 scans"
Output: `GET /v1/track/{id}` contract + sample JSON with `scans: [{timestamp, location, code}]`

## Failure modes
- No docs provided → produce checklist of required docs and fallback instructions to use CSV fallback.
- Proprietary/paid API → recommend credential handling + rate limits.

## Invocation
`/run carrier-api-adapter-helper --carrier=UPS --features=scans,events`