---
name: "Rule — Guardlane Design System (elevated neutrals, semantic palette)"
product: "Guardlane"
version: "1.0"
updated: "2026-03-12"
summary: "Système de design Guardlane : neutres surélevés (elevated neutrals), bleu signalétique, palette sémantique monitoring, typographie, widget d'alerte. Référence pour UX et frontend."
---

# Guardlane — Design System (guidelines)

Ce système utilise une approche de **neutres surélevés** (elevated neutrals) pour le fond, combinée à un bleu signalétique précis pour inspirer confiance.

---

## 1. Primary Brand & Neutrals (L’infrastructure)

- **Background (Light Mode) :** `#F8FAFC` (Slate 50). Gris très légèrement bleuté pour reposer les yeux des vendeurs TikTok.
- **Surface / Cards :** `#FFFFFF` (Pure white). Conteneurs de données (tableaux, widgets) pour créer une profondeur avec le fond.
- **Primary Brand (Le "Guard") :** `#0284C7` (Clearway Blue). Bleu céruléen profond mais dynamique. À utiliser **exclusivement** pour le bouton d’appel à l’action principal (ex. « Connecter TikTok Shop »).
- **Text Primary :** `#0F172A` (Slate 900). Ne jamais utiliser de noir pur (`#000000`) pour le texte (fatigue oculaire sur fond clair).

---

## 2. Semantic Palette (Le monitoring)

Ces couleurs ont un rôle **strictement fonctionnel**. Ne pas les utiliser pour la décoration.

- **Safe / All Clear (Vert) :** `#10B981` (Emerald). VTR sain, statuts « Synchronisé », checks de bonne santé.
- **Early Warning (Ambre) :** `#F59E0B` (Amber). Anomalies mineures (ex. « Scan transporteur manquant, risque modéré »).
- **Violation Alert (Crimson) :** `#E11D48` (Rose/Crimson). Rouge froid, digne d’un outil d’analyse B2B — pas un rouge pur type erreur.

---

## 3. Dark Mode (Agences / Power users)

- **Background :** `#0B0F19` (très sombre, légèrement bleuté).
- **Surface :** `#1E293B` (Slate 800).
- **Primary Action :** `#38BDF8` (Light Sky Blue), ajusté pour contraste WCAG 2.2 sur fond sombre.

---

## 4. Typography

- **Marketing & Headlines :** `Plus Jakarta Sans` ou `Manrope`. Géométrique, propre, B2B SaaS. Titres H1, titres de sections.
- **UI & Dashboard Body :** `Inter`. Lisibilité petits textes, labels, menus ; alignement tabulaire des chiffres (colonnes VTR, prix).
- **Monospace & Data :** `JetBrains Mono`. IDs de commande, erreurs API, clés — séparation visuelle « donnée brute » vs « interface ».

---

## 5. Widget d’alerte (Application UI)

Ne pas se contenter d’une pastille rouge. L’UI doit être **explicative**.

- **À éviter :** `[Pastille Rouge] VTR trop bas.` (anxiogène, peu actionnable).
- **Design Guardlane :** Carte blanche avec **bordure gauche épaisse** en Crimson (`#E11D48`). Titre en **Inter SemiBold** : *Risque de Suspension : VTR à 88% (Seuil : 95%)*. En dessous, pastille grise avec action claire : *[Voir les 4 commandes sans scan 3PL]*. L’utilisateur passe de la panique à l’action ciblée.

---

## 6. Contraintes communes (radius, tokens)

- Border radius : ne pas dépasser le token `radius.md` (voir agent UX et `DESIGN_TOKENS.json`).
- Tous les composants doivent référencer les tokens ; pas de couleurs ou rayons en dur sauf exception documentée.
