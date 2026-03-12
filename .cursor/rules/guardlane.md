---
name: "Rule — Guardlane (product-context)"
product: "Guardlane"
version: "1.0"
updated: "2026-03-12"
summary: "Règle centrale et contexte produit pour tous les agents : positionnement, cible, MVP, KPIs, tone & constraints. Chaque agent doit inclure `PRODUCT_CONTEXT: Guardlane` dans ses livrables et vérifier la conformité avec ces règles."
---

# GUARDLANE — PRODUCT RULE (quick reference)

## TL;DR (1 phrase)
Guardlane protège les sellers TikTok Shop des violations VTR en détectant les risques avant sanction et en fournissant alertes et recommandations actionnables.

---

## Positionnement & Vision
- Produit : assurance anti-violation VTR pour TikTok Shop.  
- Promesse : **« Stopper les violations TikTok Shop avant qu’elles ne tuent ton shop. »**  
- Angle : hyper-niche (prévention sanctions VTR), pas un outil de shipping/gain de coûts.

---

## Message obligatoire à inclure dans tout livrable
Tous les agents doivent insérer clairement au début de leurs réponses/fichiers :

PRODUCT_CONTEXT: Guardlane — "Stopper les violations TikTok Shop avant qu’elles ne tuent ton shop."


---

## Audience cible (ICP) — ordre de priorité
1. SMB TikTok Sellers (10–500 orders/day) — PRIORITAIRE  
2. Agencies TikTok Shop (gèrent 3–20 shops) — stratégique pour scale  
3. DTC Brands testing TikTok Shop — opportunité secondaire

---

## MVP (déploiement rapide — 3–5 semaines)
- Dashboard VTR-like (ratio commandes ≥2 scans)
- Import CSV TikTok
- Intégrations basiques transporteurs (scope initial limité)
- Alertes seuil & tendance 7 jours
- Rapport "what changed"

**Contraintes MVP** : simple, actionnable, faible friction onboarding.

---

## Objectif 90 jours
- 100+ shops activés
- Premiers case studies chiffrés
- KPIs : activation rate, alerts/useful per shop, churn < 8% target

---

## KPIs clés (doivent être référencés par tous les agents)
- North Star: `jours en "Good VTR"` / `violations évitées`
- Acquisition: waitlist → beta → paid conversion
- Activation: % shops with ≥1 transport connected; upload 30j history
- Retention: 90-day logo retention; correlation alert usefulness ↔ retention

---

## Valeur & Bénéfices à garder en tête (pour copy, UX, infra, tests)
1. Détection préventive (alerte avant dépassement)
2. Diagnostic rapide (what changed)
3. Recommandations actionnables (service change, split batch, fallback FBT)

---

## Contraintes produit / guardrails
- Positionnement : **prévention**, pas optimisation logistique.
- Messages clients : prudence juridique (« résultats probables », « hypothèse à valider »).
- Données sensibles : respecter GDPR / data residency selon shop.
- Time-to-market prioritaire : MVP minimal viable.

---

## Assets prioritaires (à produire / référencer)
- Landing page & waitlist
- Dashboard mockups (VTR view)
- CSV import spec (TikTok export mapping)
- Transporteurs: API contract stubs / fallback CSV ingestion
- Beta case study template
- Onboarding scripts & support flows
- FAQ & legal disclaimers (claims prudents)

---

## Règles opérationnelles pour les agents (obligatoire)
1. **Inclure le product context** (voir Message obligatoire ci-dessus) au début de chaque réponse, PR, ticket ou livrable.  
2. **Rester aligné sur le scope MVP** sauf si l’Architect / PO valide extension. Tout écart doit être expliqué (impact, effort, tradeoff).  
3. **Mesurables obligatoires** : tout deliverable fonctionnel doit exposer comment il permettra de mesurer au moins un KPI listé ci-dessus (activation, alerts/useful, retention...).  
4. **Privacy & Compliance** : backend/infra agents doivent documenter data flows et points de stockage; UX/marketing must avoid privacy assumptions.  
5. **Testing acceptance** : features must include tests and metrics hooks to compute relevant KPI.  
6. **Communications** : pour outreach agencies, prepare templated pitch + onboarding checklist.

---

## Exigences de validation (checklist rapide — à joindre à PRs / livrables)
- [ ] `PRODUCT_CONTEXT` présent en tête du livrable.  
- [ ] Lié à au moins 1 KPI (défini).  
- [ ] Conforme au scope MVP (ou justification incluse).  
- [ ] Assets nécessaires (mockups, API contract, CSV spec) fournis ou référencés.  
- [ ] Respect des contraintes légales / privacy (données clients).  
- [ ] Pour UI: respecter tokens/design system fournis par UX agent (voir `design-system-guardlane.md`).  
- [ ] Pour infra: montrer plan de backups & sécurité pour données PII.  
- [ ] Pour e2e/tests: provide test scenarios showing alert generation and action flows.

---

## Scénarios d’échec & actions requises
- Si un agent propose une fonctionnalité hors scope majeur (ex: optimisation shipping complète) → **stop** : demander justification, estimer effort, valider avec Product/Architect.  
- Si l'intégration TikTok API impossible → fallback CSV flow mandatory.  
- Si la donnée client est stockée hors zone autorisée → block and require remediation plan.

---

## Communication & ownership
- Product Owner / PM : décide priorité & exceptions.  
- System Architect : valide alignement infra / non-fonctionnel.  
- UX : validate UX patterns and token compliance.  
- Backend / DevOps : ensure data flows, security, backups.  
- Marketing / Growth : responsible for outreach & early access pipeline.

---

## How agents should reference this rule programmatically
- Add header to outputs: `PRODUCT_CONTEXT: Guardlane`
- When producing artifacts, include metadata:
```yaml
product: Guardlane
artifact_type: <e.g., api-spec | ui-mock | infra-plan>
kpi_mapping: <which KPI this artifact enables>
scope: MVP | V2 | OutOfScope
```
