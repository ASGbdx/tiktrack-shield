# SKILL: PR Metadata Enforcer
Short: Validate PR contains required Guardlane metadata and produce a checklist.

## When to use
On PR creation or reviewer checklist step.

## Input
- PR title & body
- Changed files list

## Output
- Checklist: presence of `PRODUCT_CONTEXT`, `scope`, `kpi_mapping`, `data_flow` etc.
- Auto-suggested fixes for missing items (template snippets)

## Steps
1. Read PR body and files.
2. Check for required YAML/headers: `PRODUCT_CONTEXT`, `scope`, `kpi_mapping`.
3. Validate `scope` + `kpi_mapping` semantics.
4. Return pass/fail and suggested PR body patch.

## Examples
Input: PR missing `kpi_mapping`
Output: Fail + snippet to paste:
```yaml
PRODUCT_CONTEXT: Guardlane
scope: MVP
kpi_mapping: [activation]
```

## Failure modes
- Private repo access denied → return instructions for manual checks.
- If required artifacts missing → produce template and block merge suggestion.

## Invocation
CI: runs as PR check; Manual: `/run pr-metadata-enforcer --pr=123`