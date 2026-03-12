---
name: "Rule — Go-To-Market (GTM) Alignment"
version: "1.0"
product: "Guardlane"
updated: "2026-03-11"
summary: "Ensure messaging, assets and outreach tactics are tightly aligned with product positioning (anti-VTR violation)."
---

# GTM Alignment — Quick Rule

**Purpose**  
Keep market message clear: prevention of VTR violations, not shipping optimization.

## Rule (must-follow)
1. All marketing assets (landing, copy, outreach templates) must use approved phrasing:
   - Acceptable: "Prevent VTR violations", "Good VTR days", "anti-VTR"
   - Forbidden: "Optimize shipping", "reduce shipping cost" (unless explicit V2)
2. Provide required assets for each launch stage (waitlist, beta, public):
   - Landing copy, onboarding flow, early-access email templates, agency pitch.
3. Claims must be evidence-tagged: every claim with numbers must reference a source (beta result, study, or labeled hypothesis).

## Required artifacts
- Approved messaging snippets
- Templates for outreach and onboarding
- Case study template with fields for metrics

## Minimal enforcement checklist
- [ ] Messaging uses approved phrasing.
- [ ] Any quantitative claim includes source or is labeled hypothesis.
- [ ] Agency pitch template included for outreach.

## Programmatic snippet
```yaml
rule: gtm-alignment
phase: waitlist|beta|public
approved_phrasing: true
claim_source: url | hypothesis
```