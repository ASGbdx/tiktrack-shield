---
name: "Rule — Security & Data Ownership"
version: "1.0"
product: "TikTrack Shield"
updated: "2026-03-11"
summary: "Define data classification, storage, access, retention and compliance for any data flow touching PII or business-sensitive data."
---

# Security & Data Ownership — Quick Rule

**Purpose**  
Protect seller data and comply with privacy/regulatory requirements.

## Rule (must-follow)
For any feature or integration that touches data (CSV, API, backups), provide a short Data Ownership doc including:
- Data classification: `PII` | `BusinessSensitive` | `NonSensitive`
- Storage location(s) and residency
- Access roles (who can read/write)
- Retention policy (days)
- Deletion policy & process

Backend/DevOps must provide:
- Data flow diagram (simple)
- Backup policy & restore test freq
- Encryption at rest & transit status

## Required artifacts
- `DATA_FLOW.md` or inline `data_flow` YAML
- `.env.example` & secrets management notes (no real secrets)
- Access control matrix snippet

## Minimal enforcement checklist
- [ ] Data classification defined.
- [ ] Storage & residency documented.
- [ ] Backup & restore plan included.
- [ ] Encryption indicated.

## Programmatic snippet
```yaml
rule: security-data-ownership
data_classification: PII | BusinessSensitive | NonSensitive
storage: {location: string, residency: string}
access_roles:
  - role: Backend
    privileges: read/write
retention_days: 90
```