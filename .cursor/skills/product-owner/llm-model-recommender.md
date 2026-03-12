# SKILL: LLM Model Recommender
Short: Recommend the best LLM model for a User Story and provide a short justification, aligned with the PO model rules.

## When to use
- When assigning an US to an LLM agent or to pick a model for automated generation.

## Input
- User Story summary + task list + complexity hints (code heavy? infra? documentation?).

## Output
- Recommended model (one of allowed models)
- Short justification (1–3 lines)
- Seniority note (e.g., "use high-capacity Codex/GPT 5.3 for codegen; Sonnet for prose")

## Steps
1. Validate `PRODUCT_CONTEXT`.
2. Classify task types: code generation / architecture / copy / small formatting.
3. Map to model according to PO guidelines.
4. Provide fallback model suggestions and cost/latency considerations.

## Examples
Input: US involves writing DB migration + SQL -> recommend `GPT 5.3 Codex` with justification.
Output:
- model: GPT 5.3 Codex
- justification: "Codegen-heavy with SQL; Codex better for accurate code scaffolding."

## Failure modes
- If tasks mix conflicting types → recommend hybrid approach (model A for code, model B for docs) and note orchestration.

## Invocation
`/run llm-model-recommender --us-file=...`