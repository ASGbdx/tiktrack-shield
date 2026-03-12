# SKILL: Stakeholder Question Generator
Short: Generate up to 3 crisp clarifying questions for stakeholders when a US/epic lacks clarity.

## When to use
- When any stage hits `needs_clarification` or ambiguous constraints detected.

## Input
- US/Epic text
- Areas of ambiguity detected (optional)

## Output
- Up to 3 prioritized questions, each with rationale and suggested acceptable answers.

## Steps
1. Validate `PRODUCT_CONTEXT`.
2. Identify missing decision points (APIs, data, performance, legal).
3. Produce 1–3 precise questions with expected answer format (yes/no, exact value, link to doc).

## Examples
Input: "Implement carrier integration" (no carriers listed)
Output:
1. Which carrier(s) to support first? [list: USPS/UPS/FedEx/Other]
2. Does the carrier require OAuth or API key? [provide doc]
3. Provide SLA for ingestion latency? [value in seconds]

## Failure modes
- If no ambiguity found -> return `no_questions_required`.

## Invocation
`/run stakeholder-question-generator --us=...`