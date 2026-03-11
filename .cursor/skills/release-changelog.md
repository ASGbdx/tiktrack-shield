# SKILL: Release & Changelog
Short: Prepare release notes, version bump, and changelog entries from merged work (PRs, scope, KPIs).

## When to use
Before tagging a release, when cutting a new version, or when maintaining CHANGELOG for stakeholders or users.

## Input
- Version to release (e.g. `v0.2.0`) or "next" (suggest bump: patch/minor/major)
- Range of commits or list of merged PRs since last tag
- Optional: convention (Conventional Commits, or scope-based: MVP / V2)

## Output
- **Changelog entry** (Markdown) : Added / Changed / Fixed / Security, grouped by scope or KPI if useful
- **Version bump suggestion** (patch / minor / major) with short rationale
- **Release notes draft** (user-facing, concise) if needed
- Optional: tag message and GitHub release body snippet

## Steps
1. Ensure `PRODUCT_CONTEXT`, `scope`, `kpi_mapping` are available from PR/commit metadata.
2. List commits/PRs since last tag; classify by type (feat, fix, chore, etc.) or by scope (MVP, V2).
3. Deduplicate and group entries; write clear, user-oriented lines (no raw commit messages).
4. Propose version bump from semver (breaking → major, new feature → minor, fixes → patch).
5. Emit changelog block and optional release notes.
6. If CHANGELOG.md exists, show exact insertion point and suggested block.

## Examples
Input: `since=v0.1.0, next=minor`
Output: Changelog section for `## [0.2.0]` with Added (e.g. "Alert threshold configuration"), Fixed (e.g. "CSV date parsing for EU locale"), plus suggested tag `v0.2.0`.

## Failure modes
- No previous tag → treat full history or ask for "first release" baseline.
- Mixed or missing metadata → infer from commit messages; flag entries without scope/kpi for manual review.
- Non-semver version scheme → ask for version policy and adapt format.

## Invocation
`/run release-changelog --since=v0.1.0 --next=minor` or `/run release-changelog --prs=12,14,16 --version=0.2.0`
