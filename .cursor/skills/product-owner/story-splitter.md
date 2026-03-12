# SKILL: Story Splitter
Short: Split large epics or monstrous user stories into smaller, implementable user stories (US) that fit the PO file structure.

## When to use
- You have an Epic or very large US and need a clear set of smaller USs (S/M-sized) that agents can implement.

## Input
- Epic description or large User Story (text / markdown)
- Optional: target scope (MVP | V2), constraints (timebox in weeks)

## Output
- List of new US drafts (title + short description + suggested scope + estimated effort band)
- For each draft: suggested acceptance criteria bullets
- Warnings if splitting cannot preserve atomicity

## Steps
1. Validate `PRODUCT_CONTEXT` presence.
2. Parse the epic/US and extract discrete user outcomes.
3. Apply splitting rules: vertical slices, minimal deliverables, keep acceptance testable.
4. Return a numbered list of US drafts with suggested numbering placeholders (e.g., 01.01 → 01.02).
5. Suggest which US belong to MVP vs V2 when relevant.

## Examples
Input: Epic "Ingest & Normalize Tracking for carriers"
Output: 
- US 01: "CSV Import - TikTok Exports" (MVP, S)
- US 02: "Carrier API: basic scan ingestion" (MVP, M)
- US 03: "Normalization: unify scan timestamps" (MVP, S)

## Failure modes
- If input is too vague → return `needs_clarification` and produce 1–3 clarifying questions.
- If epic is already atomic → return `no_split_needed`.

## Invocation
`/run story-splitter --epic="Ingest & Normalize Tracking" --scope=MVP`