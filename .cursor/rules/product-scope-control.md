---
name: "Rule — Product Scope Control (Anti-Feature Creep)"
version: "1.0"
product: "TikTrack Shield"
updated: "2026-03-11"
summary: "Enforce MVP boundaries: every feature must be classified as MVP | V2 | OutOfScope. OutOfScope requires justification + Product approval."
---

# Product Scope Control — Quick Rule

**Purpose**  
Protect time-to-market and product positioning by preventing feature creep. All agents must classify proposed work and surface deviations.

## Rule (must-follow)
1. Every feature/PR/ticket must include a `scope` field: `MVP` | `V2` | `OutOfScope`.
2. If `OutOfScope`, include:
   - short justification (why important)
   - estimated effort (days)
   - product approval (PO or Architect sign-off)
3. If agent proposes `OutOfScope` work, **stop** and request Product approval before implementation.

## Required artifacts
- Feature card / ticket with `scope` metadata.
- Impact analysis (1 paragraph).
- KPI mapping (see KPI rule).

## Minimal enforcement checklist (to attach to PRs)
- [ ] `scope` declared.
- [ ] If `OutOfScope`, Product approval attached.
- [ ] Impact & tradeoffs documented.

## Programmatic snippet (agents should add)
```yaml
rule: product-scope-control
scope: MVP | V2 | OutOfScope
justification: string (required when OutOfScope)
product_approval: <user/id> (required when OutOfScope)
```