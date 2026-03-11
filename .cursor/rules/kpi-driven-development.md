---
name: "Rule — KPI-Driven Development"
version: "1.0"
product: "TikTrack Shield"
updated: "2026-03-11"
summary: "Every deliverable must map to at least one product KPI. If none, justify its value."
---

# KPI-Driven Development — Quick Rule

**Purpose**  
Ensure engineering work moves metrics that matter for TikTrack Shield (activation, alert usefulness, retention, Good VTR days).

## Rule (must-follow)
1. Every artifact (PR, spec, mock, infra plan) must include `kpi_mapping`: one or more of:
   - `activation`
   - `alert_usefulness`
   - `retention`
   - `good_vtr_days`
   - `acquisition`
2. If `kpi_mapping` is empty, require a short justification and Product approval.

## Required artifacts
- `kpi_mapping` entry in metadata.
- One sentence explaining how the artifact will be measured (metric, event, or log).

## Minimal enforcement checklist
- [ ] `kpi_mapping` present.
- [ ] Measurement method described (metric / event name).
- [ ] Telemetry hook(s) identified.

## Programmatic snippet
```yaml
rule: kpi-driven
kpi_mapping:
  - activation
measurement:
  metric_name: string
  event_source: string
```