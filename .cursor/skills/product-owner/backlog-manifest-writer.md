# SKILL: Backlog Manifest Writer
Short: Create or update /documentation/cadrages/BACKLOG_MANIFEST.yaml with canonical entries.

## When to use
- After themes/epics/US are drafted and need to be recorded in the manifest.

## Input
- List of Themes / Epics / US (titles + paths + metadata)
- Existing BACKLOG_MANIFEST.yaml (optional)

## Output
- Updated BACKLOG_MANIFEST.yaml (YAML) following PO schema
- Summary diff of changes

## Steps
1. Validate `PRODUCT_CONTEXT`.
2. Load existing manifest or create new.
3. Validate uniqueness of IDs and zero-padded numbering.
4. Append/update entries with metadata (`llm_model_recommended`, `scope`, `kpi_mapping`).
5. Output the new manifest and a change summary.

## Examples
Input: new US file path + metadata
Output: updated manifest with new entry and `added: true` flag.

## Failure modes
- If numbering conflicts → return `conflict` and propose renumbering.
- If path invalid → return path error.

## Invocation
`/run backlog-manifest-writer --add=path/to/us.md --manifest=documentation/cadrages/BACKLOG_MANIFEST.yaml`