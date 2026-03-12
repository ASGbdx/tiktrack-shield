# SKILL: Task Assigner by Agent
Short: Convert a User Story into concrete tasks grouped by agent (Backend, Frontend, DevOps, UX, QA, Marketing).

## When to use
- After US + AC exist and you need agent-level task lists and deliverables.

## Input
- Full US (markdown format per PO template)
- Optional: preferred owners or team availability hints

## Output
- Tasks grouped by agent with stepwise instructions and deliverables (file paths, endpoints, mocks)
- Flag required dependencies and sequence order

## Steps
1. Validate `PRODUCT_CONTEXT`.
2. Read US + acceptance criteria.
3. For each domain (backend, frontend, devops...), produce 2–8 tasks with detailed steps.
4. For each task include: objective, step-by-step instructions, outputs, approx effort band.

## Examples
Input: US "CSV Import - TikTok Exports"
Output:
- Backend tasks: create ingestion API POST /ingest/csv, create migration orders_raw, add normalization step...
- Frontend tasks: upload UI /dashboard/import, progress + toast messages...
- DevOps tasks: temporary storage S3-compatible bucket with retention X...

## Failure modes
- Missing US metadata -> refuse and request the US file with YAML header.
- If tasks imply forbidden scope → flag `OutOfScope` and require PO approval.

## Invocation
`/run task-assigner-by-agent --us-file=documentation/cadrages/01/.../01 - CSV Import.md`