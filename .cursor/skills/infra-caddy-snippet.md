# SKILL: Infra Caddy Snippet Generator
Short: Generate secure Caddyfile snippets (reverse_proxy, headers, rate limits) per service.

## When to use
When provisioning routes for new services, or during PR review for ingress changes.

## Input
- Service name & internal URL (e.g., `http://backend:8000`)
- Domain/subdomain
- Desired rate limits / security headers / acl (Tailscale-only admin)

## Output
- Caddyfile snippet with:
  - `reverse_proxy` block
  - security headers (HSTS, CSP, X-Frame-Options)
  - TLS config (recommend Full Strict via Cloudflare)
  - Optional rate limiting examples
- Notes on deployment & reload steps

## Steps
1. Ensure `PRODUCT_CONTEXT`, `scope`, `kpi_mapping`.
2. Generate minimal secure snippet with comments.
3. Provide testing checklist (how to validate).

## Examples
Input: `service=api, domain=api.tiktrack.example.com`
Output: Caddyfile with `reverse_proxy /api http://backend:8000` + security headers.

## Failure modes
- Unknown domain provider → provide generic snippet and DNS checklist.
- If Cloudflare in front → note `X-Forwarded-For` and `real ip` handling.

## Invocation
`/run infra-caddy-snippet --service=api --domain=api.tiktrack.local --rate=100/m`