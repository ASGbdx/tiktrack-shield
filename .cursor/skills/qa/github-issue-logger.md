# SKILL: GitHub Issue Logger (QA)
Short: When QA detects a bug, anomaly or risk, create or update a GitHub Issue in the project repo with structured metadata and artefacts.

version: 1.0
product_required: true

## When to use
- QA detects a reproducible bug, an intermittent anomaly, a regression, a test flake affecting reliability, or a security risk during test/execution.

## Input
- Minimal required:
  - `PRODUCT_CONTEXT` (must be present)
  - `repo` (owner/repo e.g., `myorg/guardlane`)
  - `title` (short descriptive title)
  - `severity` (critical | high | medium | low)
  - `description` (steps to reproduce, expected vs actual)
  - `artifacts` (optional list of artifact URLs or paths: logs, screenshots, videos, traces)
  - `test_id` (optional: identifier of test that found it, e.g., `playwright/alert_flow.spec.ts::should_trigger_alert`)
  - `fingerprint` (optional: auto-generated hash to deduplicate similar issues)

- Configuration (env / secrets, not embedded in skill):
  - `GITHUB_TOKEN` (stored in runner/CI secrets; minimal scope)

## Output
- Human-readable comment with short reproduction steps + link to artefacts.
- JSON object summarizing created/updated issue:
  ```json
  {
    "action": "created" | "updated" | "skipped",
    "issue_number": 123,
    "issue_url": "https://github.com/owner/repo/issues/123",
    "reason": "duplicate" | "new" | "skipped_missing_token"
  }
  ``` 



## Steps
1. Validate metadata: ensure PRODUCT_CONTEXT present. If missing → return error with patch snippet to add metadata.
2. Sanitize inputs: remove or mask any PII from description and artifacts. (If artifact contains PII, attach sanitized excerpt only.)
3. Compute fingerprint (if not provided): hash of title + repro steps + normalized stacktrace to deduplicate.
4. Search existing issues in the repo for identical or similar fingerprint/title (use GitHub Search API or list issues with relevant labels).
  - If existing open issue found (same fingerprint or similar title) → add a comment with new artefacts / test result and update labels (e.g., bump severity if needed) and return action: updated.
  - Else → create a new issue using the Issue Template:
    - Title: [QA][<SEVERITY>] <short title>
    - Body: structured template (see below).
    - Labels: triage, bug (or security), severity:critical|high|medium|low, area:<backend|frontend|devops|infra> if derivable.
    - Assignee: optional; by default leave unassigned or add triage-team placeholder.
5. Attach artifacts: upload files to a secure artifact store (CI artifact or S3) and include their URLs in the issue body. If using GitHub REST to attach images, ensure token has repos scope and file size within limits.
6. Return JSON result indicating created/updated/skipped plus issue URL.

Issue body template (to create/upload)
```markdown
PRODUCT_CONTEXT: <product>   # auto-inserted
Title: [QA][<SEVERITY>] <short title>
Severity: <critical|high|medium|low>
Area: <frontend|backend|devops|other>
Fingerprint: <computed_hash>

## Short description
<one-paragraph summary>

## Reproduction steps
1. Given ...
2. When ...
3. Then ...

## Expected vs Actual
- Expected: ...
- Actual: ...

## Test info
- Test id: <test_id>
- Test run: <CI job id / build url>
- Environment: <staging / ephemeral / local>
- Time: <ISO timestamp>

## Artifacts (sanitized)
- logs: <artifact_url>
- screenshot: <artifact_url>
- video: <artifact_url>

## Impact & Risk
- Business impact: <e.g., blocks alert generation; affects X% of shops>
- Suggested priority: <fix asap / triage>

## Suggested labels
- bug / security / flaky / regression
- severity:<critical|high|medium|low>
- area:<backend|frontend|devops>

## Optional: remediation hints
- Short hints for engineers (e.g., files to inspect, suspected root cause)
``` 

## Labels & mapping (recommended)
- severity → severity:critical|severity:high|severity:medium|severity:low
- type → bug, security, flaky, regression, risk
- triage status → triage (new issues)
- component → area:backend|area:frontend|area:devops|area:ux

## Deduplication strategy
- Compute fingerprint (SHA256 of normalized title + repro steps + stacktrace).
- On create: search recent open issues for same fingerprint via issue.search by label/fingerprint.
- If found: append a comment linking new artifact & test run instead of creating new issue.

## Examples
Invocation example (CI)
```bash
export GITHUB_TOKEN="${{ secrets.GITHUB_TOKEN }}"
/run github-issue-logger \
  --repo="myorg/guardlane" \
  --title="Alert not triggered when only single scan exists" \
  --severity=high \
  --description="Steps...\n1. upload CSV ...\n2. run ingest...\nExpected: alert, Actual: no alert" \
  --test_id="tests/integration/test_ingest_to_alert.py::test_alert_on_low_vtr" \
  --artifacts='["https://ci.example.com/artifacts/123/log.txt","https://ci.example.com/artifacts/123/video.mp4"]'
```

## GitHub API curl snippet (example, DO NOT embed tokens in repo)
```bash
curl -H "Authorization: token $GITHUB_TOKEN" \
     -H "Accept: application/vnd.github.v3+json" \
     https://api.github.com/repos/myorg/guardlane/issues \
     -d '{
       "title":"[QA][high] Alert not triggered when only single scan exists",
       "body":"<issue body template filled>",
       "labels":["triage","bug","severity:high","area:backend"]
     }'
```

## Failure modes & safeguards
- Missing GITHUB_TOKEN → do not create issue; return skipped_missing_token with instructions to configure secret.
- Token lacks scope → return error with required scopes list.
- Network failure / GitHub API rate limit → retry with backoff; if repeated failure, persist issue draft locally (artifact) and notify owners.
- Duplicate detection false negative → provide convenient "create anyway" option with force=true (manual intervention).
- Sensitive data found in attachments → redact automatically and include sanitized excerpt; mark in issue body that sensitive data was removed.

## Invocation
- CLI / skill runner:
  ```bash
  /run github-issue-logger --repo=myorg/guardlane --title="..." --severity=high --description="..." --artifacts='["..."]'
  ```
- Recommended: integrate into CI (post-test step) to auto-log failures labeled `integration` or `regression`.


---

### Recommandations d’intégration & bonnes pratiques
1. **Triage flow** : create new issues with `triage` label and optionally as **draft** to avoid immediate backlog noise. Have a scheduled triage job (team) to convert & assign.
2. **Artifacts storage** : store large artifacts (video, logs) in CI artifacts or S3 and reference URLs in the issue body (avoid uploading huge binaries to GitHub).
3. **Security** : store `GITHUB_TOKEN` in GH Actions secrets or Vault; token minimum privileges (issues:write). For cross-repo ops, use a machine user with scoped access.
4. **Rate limiting** : implement exponential backoff on API calls.
5. **Visibility** : include `PRODUCT_CONTEXT` and `US` path in the issue to make tracing to backlog easy.
6. **Automated linking** : where possible, add `backlog_manifest` metadata to the issue body so downstream PO/triage agents can auto-link the issue to the relevant US in `/documentation/cadrages/`.
