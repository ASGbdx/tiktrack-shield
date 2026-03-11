# SKILL: Alert Definition Tester
Short: Run an alert rule against sample data to see if it would fire and produce tuning suggestions.

## When to use
Before merging new alert rules or adjusting thresholds.

## Input
- Alert definition (trigger condition, window, severity)
- Sample dataset (CSV/JSON)
- Optional: aggregation rules

## Output
- Test report: fired/not-fired, timestamps, how many times, affected shops
- Recommendations: thresholds, aggregation window, confidence adjustment
- Suggested test cases for CI

## Steps
1. Verify `PRODUCT_CONTEXT`, `scope`, `kpi_mapping`.
2. Load rule and sample data.
3. Simulate evaluation over sample timeline.
4. Produce report and recommend parameter changes for target noise level.

## Examples
Input: alert `vtr_below_0.8` over 7d
Output: fired for shop X at timestamps [..], recommendation: increase window to 14d to reduce noise.

## Failure modes
- Insufficient sample diversity → request more fixtures.
- Missing timestamps → cannot evaluate; return required columns.

## Invocation
`/run alert-definition-tester --rule=vtr_below_0.8 --data=fixtures/shopA.json`