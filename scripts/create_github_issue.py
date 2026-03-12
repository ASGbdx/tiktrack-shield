#!/usr/bin/env python3
"""
scripts/create_github_issue.py

Usage (example):
  python3 scripts/create_github_issue.py \
    --repo myorg/guardlane \
    --fingerprint <sha256> \
    --title "QA: CI test failures ..." \
    --severity high \
    --description "Steps..." \
    --artifact ./qa-artifacts-20260311T120000Z.tar.gz \
    --test-id "ci/12345"

Notes:
- Expects GITHUB_TOKEN in env.
- Does basic sanitization and deduplication by fingerprint.
"""

import argparse
import hashlib
import json
import os
import re
import sys
import time
from base64 import b64encode
from typing import Optional

import requests

GITHUB_API = "https://api.github.com"


def sanitize_text(s: str) -> str:
    # Basic PII masking examples: emails and tokens
    s = re.sub(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,6}", "[redacted-email]", s)
    s = re.sub(r"(token|password|secret)[:=]\s*[A-Za-z0-9_\-+.=\/]+", r"\1:[redacted]", s, flags=re.I)
    return s


def find_existing_issue_by_fingerprint(repo: str, fingerprint: str, headers: dict) -> Optional[dict]:
    # We store fingerprint in issue body like "Fingerprint: <hash>"
    query = f'repo:{repo} in:body "{fingerprint}" state:open'
    url = f"{GITHUB_API}/search/issues"
    resp = requests.get(url, headers=headers, params={"q": query})
    resp.raise_for_status()
    items = resp.json().get("items", [])
    return items[0] if items else None


def create_issue(repo: str, title: str, body: str, labels: list, headers: dict) -> dict:
    url = f"{GITHUB_API}/repos/{repo}/issues"
    payload = {"title": title, "body": body, "labels": labels}
    resp = requests.post(url, headers=headers, json=payload)
    resp.raise_for_status()
    return resp.json()


def comment_on_issue(repo: str, issue_number: int, comment: str, headers: dict) -> dict:
    url = f"{GITHUB_API}/repos/{repo}/issues/{issue_number}/comments"
    resp = requests.post(url, headers=headers, json={"body": comment})
    resp.raise_for_status()
    return resp.json()


def upload_artifact_as_gist_or_storage(artifact_path: str) -> str:
    """
    Option A: upload to a storage you control (S3) and return URL.
    Option B: as a fallback, create a gist with small logs (not binary) OR return artifact filename
    Here we simply return the artifact filename (CI artifact URL available in workflow UI)
    """
    # In production, replace with S3 upload or linking to GitHub Actions artifacts page
    return f"artifact://{os.path.basename(artifact_path)} (uploaded to CI artifacts)"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", required=True, help="owner/repo")
    parser.add_argument("--fingerprint", required=True)
    parser.add_argument("--title", required=True)
    parser.add_argument("--severity", default="medium", choices=["critical", "high", "medium", "low"])
    parser.add_argument("--description", default="")
    parser.add_argument("--artifact", default=None)
    parser.add_argument("--test-id", default=None)
    parser.add_argument("--force", default="false", help="force create new issue even if duplicate")
    args = parser.parse_args()

    token = os.environ.get("GITHUB_TOKEN")
    if not token:
        print(json.dumps({"action": "skipped", "reason": "missing_token"}))
        sys.exit(0)

    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json",
        "User-Agent": "qa-issue-logger"
    }

    fingerprint = args.fingerprint
    title = args.title
    severity = args.severity
    description = sanitize_text(args.description or "")
    artifact_url = upload_artifact_as_gist_or_storage(args.artifact) if args.artifact else None

    # Compose issue body
    body_lines = [
        f"PRODUCT_CONTEXT: {os.environ.get('PRODUCT_CONTEXT', 'Guardlane')}",
        f"Severity: {severity}",
        f"Fingerprint: {fingerprint}",
        "",
        "## Short description",
        description,
        ""
    ]
    if args.test_id:
        body_lines.append(f"- Test id: `{args.test_id}`")
    if artifact_url:
        body_lines.append(f"- Sanitized artifact: {artifact_url}")
    body_lines.append("")
    body_lines.append("## Reproduction steps")
    body_lines.append("1. See attached sanitized logs / artifacts in CI.")
    body_lines.append("")
    body_lines.append("## Suggested labels")
    body_lines.append(f"- triage")
    body_lines.append(f"- bug")
    body_lines.append(f"- severity:{severity}")
    body = "\n".join(body_lines)

    # Deduplicate
    existing = None
    if args.force.lower() not in ("true", "1"):
        try:
            existing = find_existing_issue_by_fingerprint(args.repo, fingerprint, headers)
        except Exception as e:
            print(f"Warning: search failed: {e}")

    if existing:
        issue_number = existing["number"]
        comment = f"New test run reported additional evidence (see sanitized artifacts):\n\n{artifact_url or 'no artifact provided'}\n\nCI run: {os.environ.get('CI_RUN_URL', 'n/a')}"
        comment = sanitize_text(comment)
        comment_resp = comment_on_issue(args.repo, issue_number, comment, headers)
        print(json.dumps({"action": "updated", "issue_number": issue_number, "issue_url": existing["html_url"]}))
        return

    # Create new issue
    labels = ["triage", "bug", f"severity:{severity}"]
    try:
        created = create_issue(args.repo, f"[QA][{severity}] {title}", body, labels, headers)
        print(json.dumps({"action": "created", "issue_number": created["number"], "issue_url": created["html_url"]}))
    except Exception as e:
        print(json.dumps({"action": "skipped", "reason": str(e)}))
        sys.exit(1)


if __name__ == "__main__":
    main()