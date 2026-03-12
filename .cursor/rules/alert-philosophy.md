---
name: "Rule — Alert Philosophy"
version: "1.0"
product: "Guardlane"
updated: "2026-03-11"
summary: "Rules that define what an alert is, when to send it, and what accompanying action must exist."
---

# Alert Philosophy — Quick Rule

**Purpose**  
Keep alerts actionable, low-noise, and explainable.

## Rule (must-follow)
1. An alert must be **actionable** — include at least one recommended action.
2. An alert must include **why** it fired (root cause hint) and **confidence** (low/med/high).
3. Alerts should be throttled and aggregated to avoid noise.
4. Provide severity levels: `info` | `warning` | `critical`.
5. Each alert definition must include test case(s) and a remediation recipe.

## Required artifacts
- Alert spec:
  - name, trigger condition, severity, confidence, recommended actions, test case id
- Notification channels and rate limits (email/Slack/webhook)

## Minimal enforcement checklist
- [ ] Recommended action present.
- [ ] Confidence level present.
- [ ] Test case mapped.

## Programmatic snippet
```yaml
rule: alert-philosophy
alert:
  name: string
  trigger: string
  severity: info|warning|critical
  confidence: low|med|high
  recommended_actions: [string]
```