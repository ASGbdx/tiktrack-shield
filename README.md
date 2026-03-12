# Guardlane

Assurance anti-violation VTR pour TikTok Shop : détection des risques avant sanction, alertes et recommandations actionnables.

- **Contexte produit** : [.cursor/README.md](.cursor/README.md) — règles, skills et agents Cursor pour le projet.

## Scripts et CI

- **scripts/create_github_issue.py** : utilisé par le workflow `ci-qa-issue.yml` pour créer ou mettre à jour une issue GitHub en cas d’échec de tests. Dépendance Python : `pip install -r scripts/requirements.txt`.
- **.github/workflows/ci-qa-issue.yml** : s’exécute après le workflow **« CI - Unit & Integration Tests »**. Ce workflow de tests doit exister (dans ce dépôt ou le dépôt applicatif) et publier des artifacts pour que le logger d’issues puisse les joindre.
