# SKILL: Priority Scoring (RICE-like)
Short: Score user stories or epics by Reach / Impact / Confidence / Effort and return sorted priority list.

## When to use
- During backlog grooming, sprint planning, or when PO needs to prioritize.

## Input
- List of US/Epics (title + short description + rough effort)
- Optional: numeric estimates for reach/impact/confidence

## Output
- Table with R/I/C/E values and computed score
- Sorted list of items to prioritize
- Recommended next sprint picks (based on capacity param)

## Steps
1. Validate `PRODUCT_CONTEXT`.
2. For each item, if numeric inputs missing, use heuristics to suggest values and ask for confirmation.
3. Compute RICE score and sort.
4. Produce recommended sprint pack (sum effort <= capacity).

## Examples
Input: 5 US, capacity S+M+M
Output: priority order and recommended 3 US for next sprint

## Failure modes
- Incomplete estimates -> produce suggested defaults and mark as `needs_review`.

## Invocation
`/run priority-scoring --items=... --capacity=3`