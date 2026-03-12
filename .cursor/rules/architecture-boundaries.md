---
name: "Rule — Architecture Boundaries"
version: "1.0"
product: "Guardlane"
updated: "2026-03-11"
summary: "Clear responsibility per layer to prevent leakage of concerns between frontend/backend/infra."
---

# Architecture Boundaries — Quick Rule

**Purpose**  
Maintain separation of concerns and clear ownership.

## Canonical responsibilities
- **Frontend**: UI rendering, visualization, user interactions, tokenized styling (UX tokens). No business rule computation.
- **Backend**: VTR calculation, alert logic, business rules, auth, persistent storage.
- **DevOps**: infra, backups, security posture.
- **UX**: design tokens, visual acceptance.
- **System Architect**: approve cross-cutting changes and non-functional requirements.

## Rule (must-follow)
- Any business rule must have backend owner & tests.
- Any visual-only change must reference UX tokens.
- Cross-layer changes must show API contract and owner at each side.

## Minimal enforcement checklist
- [ ] Owner identified for each responsibility.
- [ ] API contract / interface spec attached.
- [ ] No business logic in UI components.

## Programmatic snippet
```yaml
rule: architecture-boundaries
owners:
  frontend: <user/id>
  backend: <user/id>
  devops: <user/id>
api_contract: path/to/openapi.yaml
```