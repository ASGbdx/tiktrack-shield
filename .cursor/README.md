# Guardlane — Cursor workspace

Contexte produit, règles, skills et agents pour aligner l'IA sur le projet Guardlane.

## Structure

| Dossier   | Rôle |
|----------|------|
| **rules/**  | Règles persistantes (scope, KPIs, ingestion, alertes, sécurité, GTM, design). Référence centrale : `guardlane.md`. |
| **skills/** | Skills procédurales : quand faire quoi, entrées/sorties, étapes, modes d’échec. À invoquer explicitement ou en CI. |
| **agents/**  | Définitions de sous-agents (Backend, Frontend, DevOps, UX, System Architect) avec responsabilités et flux de travail. |

## Règles (rules/)

- **guardlane.md** — Contexte produit, positionnement, MVP, KPIs, contraintes. À inclure (`PRODUCT_CONTEXT`, `scope`, `kpi_mapping`) dans tout livrable.
- **design-system-guardlane.md** — Design system Guardlane (neutres surélevés, palette sémantique, typo, widget d’alerte).
- **product-scope-control.md** — Scope `MVP | V2 | OutOfScope`, anti feature creep.
- **kpi-driven-development.md** — Chaque livrable mappe à au moins un KPI.
- **architecture-boundaries.md** — Frontend / Backend / DevOps / UX / Architect, pas de fuite de responsabilités.
- **data-ingestion-standard.md** — Schémas versionnés, validation, fallback CSV.
- **alert-philosophy.md** — Alertes actionnables, avec confiance et recommandations.
- **testing-observability-standard.md** — Tests, métriques, health checks.
- **security-data-ownership.md** — Classification données, stockage, rétention, conformité.
- **accessibility-standard.md** — Accessibilité UI : WCAG 2.1 AA, contraste, clavier, tokens, reduced-motion.
- **gtm-alignment.md** — Message marché (anti-VTR), pas optimisation shipping.

## Skills (skills/)

Les skills sont dans des sous-dossiers : **back-dev/** , **front-dev/** , **devops/** , **product-owner/** , **qa/** (ex. `skills/qa/github-issue-logger.md`), plus quelques skills à la racine de `skills/`.

| Skill | Quand l’utiliser |
|-------|-------------------|
| **infra-caddy-snippet** | Nouvelle route / service, review Caddyfile (reverse_proxy, headers, rate limit). |
| **security-audit-checker** | Avant merge infra/back, scan deps, config, secrets. |
| **csv-to-sample-fixture** | Générer des fixtures JSON à partir de CSV réels (PII masquées). |
| **csv-ingest-validator** | Valider exports CSV TikTok, rapport + mapping modèle interne. |
| **e2e-playwright-runner** | Lancer E2E (staging/ephemeral), scénarios critiques. |
| **design-token-validator** | Vérifier composants/CSS vs `DESIGN_TOKENS.json`, radius ≤ md. |
| **pr-metadata-enforcer** | Vérifier PR : PRODUCT_CONTEXT, scope, kpi_mapping, etc. |
| **alert-definition-tester** | Tester une règle d’alerte sur des données échantillon. |
| **vtr-calculator-spec** | Spéc et vecteurs de test pour le calcul VTR. |
| **carrier-api-adapter-helper** | Nouveau connecteur transporteur : stub, contrat, exemples. |
| **api-spec-sync** | Garder OpenAPI / contrat API aligné avec le code (nouveaux endpoints, changements). |
| **release-changelog** | Préparer release (version, changelog, release notes) à partir des PR/commits mergés. |

## Agents (agents/)

- **dev-back.md** — Backend (Python, FastAPI, PostgreSQL), plan → implémentation → tests.
- **dev-front.md** — Frontend (Next.js 16, TS, Tailwind v4), design system, RBAC, E2E.
- **devops.md** — Infra (Caddy, Cloudflare, Tailscale), sécurité, CI/CD, pas de code métier.
- **ux-designer.md** — Tokens, composants, accessibilité, radius ≤ md.
- **system-architect.md** — Stack, composants, contrats, SLOs, gouvernance ; pas d’implémentation.
- **product-owner.md** — Themes / Epics / US, backlog, tâches agent-ready, recommandation modèle LLM.
- **qa.md** — Stratégie de test, plans de test, CI, flaky, accessibilité, contract/perf/security.

## Scripts et CI (hors .cursor)

- **scripts/create_github_issue.py** : appelé par `.github/workflows/ci-qa-issue.yml` ; nécessite `requests` (voir `scripts/requirements.txt`).
- Le workflow **ci-qa-issue** est déclenché par **« CI - Unit & Integration Tests »** ; ce workflow de tests doit exister et publier des artifacts.

## Conventions communes

- Inclure **PRODUCT_CONTEXT: Guardlane** dans les livrables.
- Toujours renseigner **scope** (MVP / V2 / OutOfScope) et **kpi_mapping**.
- Règles et skills peuvent référencer les métadonnées : `rule:`, `scope:`, `kpi_mapping:`, `data_flow`.
