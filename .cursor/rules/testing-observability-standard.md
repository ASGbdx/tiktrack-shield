---
name: "Rule — Testing & Observability Standard"
version: "1.0"
product: "TikTrack Shield"
updated: "2026-03-11"
summary: "Standardize tests and telemetry so alerting features can be validated. Every feature must include tests and metrics."
---

# Testing & Observability Standard — Quick Rule

**Purpose**  
Ensure delivered functionality can be validated and contributes telemetry for KPIs.

## Rule (must-follow)
1. Unit tests + integration tests for backend logic that computes alerts.
2. Test scenario "alert triggered" must exist for each alerting rule.
3. Telemetry hooks:
   - metrics for counts (alerts_generated, alerts_acknowledged)
   - trace/log entries for root-cause diagnosis
4. Monitoring:
   - expose metrics (Prometheus, StatsD) for key flows
   - add health checks and readiness probes

## Required artifacts
- `tests/` folder with representative test files
- `telemetry.md` noting metric names and events
- CI step for test & coverage

## Minimal enforcement checklist
- [ ] Unit tests present.
- [ ] Integration tests for alert flow present.
- [ ] Metrics names listed & instrumentation points indicated.
- [ ] Coverage target noted (>= configured threshold).

## Programmatic snippet
```yaml
rule: testing-observability
unit_tests: true
integration_tests: true
alert_test_case: true
metrics:
  - alerts_generated
  - alerts_useful_ratio
```