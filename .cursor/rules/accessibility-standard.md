---
name: "Rule — Accessibility Standard"
version: "1.0"
product: "Guardlane"
updated: "2026-03-11"
summary: "Exigences d'accessibilité pour l'UI : WCAG 2.1 AA, design tokens, focus, contraste. Toute livraison front/UX doit être vérifiable."
---

# Accessibility Standard — Quick Rule

**Purpose**  
Garantir que l’interface Guardlane est utilisable par tous (clavier, lecteurs d’écran, contraste, motion). Aligné avec l’agent UX et le design system.

## Rule (must-follow)
1. **Niveau cible** : WCAG 2.1 niveau AA pour l’UI (texte, formulaires, navigation, états).
2. **Contraste** : texte normal ≥ 4,5:1, texte large (≥ 18pt bold / 24pt) ≥ 3:1 ; fournir paires de couleurs vérifiées.
3. **Focus & clavier** : tous les contrôles interactifs accessibles au clavier ; outline de focus visible (tokens design).
4. **Sémantique** : balises appropriées (titres, landmarks, labels), rôles ARIA si nécessaire ; formulaires avec labels associés et messages d’erreur annonçables.
5. **Motion** : respecter `prefers-reduced-motion` ; pas d’animation indispensable à la compréhension sans alternative.
6. **Design tokens** : couleurs et espacements issus de `DESIGN_TOKENS.json` ; radius ≤ token `radius.md` (valeur max., aligné règle UX).

## Required artifacts
- Pour les composants UI : mention des tokens utilisés (couleur, contraste, focus).
- Pour les flows critiques : checklist a11y (clavier, contraste, labels) ou rapport axe / outil équivalent.
- Design system : variantes accessibles et états focus documentés.

## Minimal enforcement checklist
- [ ] Contraste des textes et contrôles vérifié (AA).
- [ ] Navigation et actions possibles au clavier.
- [ ] Labels et erreurs associés aux champs.
- [ ] Réduction de motion prise en compte si animations présentes.

## Programmatic snippet
```yaml
rule: accessibility-standard
wcag_level: AA
contrast_checked: true
keyboard_accessible: true
design_tokens: DESIGN_TOKENS.json
reduced_motion: respected
```
