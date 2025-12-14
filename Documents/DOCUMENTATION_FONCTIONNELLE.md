# Documentation fonctionnelle  
## Application GreenSolutions – Diagnostic de Performance Énergétique (DPE)

---

## Objectif général

L’application web **GreenSolutions** a pour objectif d’analyser, visualiser et estimer la **performance énergétique (DPE)** des logements à partir des **données publiques de l’ADEME (DPE logements existants)**.

Développée dans le cadre du **Master 2 SISE**, l’application propose une version **simplifiée** du sujet initial, sans API externe, sans Docker et sans intelligence artificielle générative.

Elle vise à :
- faciliter la compréhension des diagnostics de performance énergétique,
- permettre l’exploration visuelle des données DPE,
- offrir une représentation géographique des logements,
- fournir une estimation énergétique personnalisée à partir des caractéristiques d’un logement.

---

## Structure et pages de l’application

L’application est structurée en plusieurs pages accessibles via une **barre de navigation latérale**.  
Chaque page correspond à une fonctionnalité précise et s’inscrit dans un parcours utilisateur progressif.

---

## Page d’accueil

**Rôle :** introduction et navigation.

La page d’accueil présente :
- le contexte général du projet GreenSolutions,
- les enjeux liés à la performance énergétique des logements,
- une synthèse des fonctionnalités principales de l’application,
- un point d’entrée vers les différentes pages via la barre latérale.

Cette page permet à l’utilisateur de comprendre rapidement la finalité de l’outil.

---

## Contexte & exploration des données

**Objectif :** comprendre les données utilisées dans l’application.

Fonctionnalités :
- présentation de la source des données (ADEME – DPE logements existants),
- affichage d’indicateurs globaux (taille du jeu de données),
- aperçu tabulaire du dataset,
- consultation d’un dictionnaire simplifié des variables principales.

Cette page permet à l’utilisateur de se familiariser avec les données avant toute analyse ou prédiction.

---

## Visualisations des données

**Objectif :** explorer visuellement les caractéristiques énergétiques des logements.

Fonctionnalités :
- filtres interactifs (année de construction, étiquette DPE, type d’énergie),
- mise à jour dynamique des graphiques selon les filtres sélectionnés,
- plusieurs types de graphiques accessibles via des onglets :
  - histogrammes,
  - diagrammes en barres,
  - boxplots,
  - nuages de points.

Cette page permet d’identifier des tendances et des relations entre les variables énergétiques.

---

## Cartographie énergétique

**Objectif :** visualiser la répartition géographique des logements DPE.

Fonctionnalités :
- carte interactive des logements du département du Rhône (69),
- affichage d’un échantillon de logements sous forme de marqueurs,
- consultation d’informations synthétiques pour chaque logement sélectionné.

La cartographie offre une lecture spatiale des diagnostics énergétiques et met en évidence les zones concentrant des logements énergivores.

---

## Prédiction énergétique

**Objectif :** estimer la performance énergétique d’un logement à partir de ses caractéristiques.

Fonctionnalités :
- formulaire guidé de saisie utilisateur (surface, année de construction, type de bâtiment, énergie, installation de chauffage),
- estimation du statut énergétique du logement (passoire ou non),
- estimation de la consommation annuelle de chauffage,
- affichage clair et visuel des résultats (probabilité, indicateurs clés),
- possibilité de réinitialiser la saisie.

Cette page constitue le cœur fonctionnel de l’application et vise à sensibiliser l’utilisateur à la performance énergétique de son logement.

---

## Page Contact

**Objectif :** fournir des informations sur le projet et permettre un retour utilisateur.

Fonctionnalités :
- formulaire de contact simple,
- message de confirmation après envoi,
- présentation du cadre académique du projet et des sources de données.

Cette page renforce la dimension pédagogique et institutionnelle de l’application.

---

## Parcours utilisateur

1. Découverte de l’application via la page d’accueil.  
2. Consultation du contexte et des données utilisées.  
3. Exploration visuelle des données via les graphiques.  
4. Observation de la répartition géographique sur la carte.  
5. Estimation personnalisée de la performance énergétique via la page Prédictions.  
6. Consultation des informations projet ou prise de contact.

---

## Conclusion

L’application **GreenSolutions** propose une approche progressive et accessible de l’analyse énergétique des logements.  
Elle combine exploration de données, visualisation graphique, cartographie et estimation énergétique dans un cadre académique maîtrisé.

Cette documentation fonctionnelle décrit le rôle et l’intérêt de chaque page de l’application, conformément aux exigences du cahier des charges et au périmètre du projet simplifié.
