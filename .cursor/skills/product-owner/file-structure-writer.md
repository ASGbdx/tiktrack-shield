# SKILL: File Structure Writer
Short: Generate the exact markdown files and folder tree under /documentation/cadrages/ per PO template.

## When to use
- When PO finalizes a Theme/Epic/US and wants files created in repository structure.

## Input
- Theme/Epic/US drafts (titles and content blocks)
- Target root folder (default: /documentation/cadrages/)

## Output
- Files: README.md for Theme and Epic, US .md files with PO template populated
- A zip or file list and short diff summary

## Steps
1. Validate `PRODUCT_CONTEXT`.
2. Sanitize titles into allowed filenames (two-digit prefix, hyphenated name).
3. Create folders and write files with exact US template and YAML header.
4. Validate file encoding/line endings.

## Examples
Input: Theme "Core VTR Detection", Epic "Ingest & Normalize", US list
Output: Folder tree and three files created with content.

## Failure modes
- If file path exists → return `exists` and show diff; create staged files with `.new.md` suffix.
- If invalid characters in title → sanitise and show mapping.

## Invocation
`/run file-structure-writer --theme="Core VTR Detection" --epic="Ingest & Normalize" --us="CSV Import - TikTok Exports"`