# Rapport d’étude  
## Analyse et modélisation du Diagnostic de Performance Énergétique (DPE)
### Projet GreenSolutions – Master 2 SISE

---

## 1. Introduction

La performance énergétique des logements est un enjeu central de la transition écologique.  
En France, le **Diagnostic de Performance Énergétique (DPE)** constitue un indicateur clé pour informer les occupants sur la consommation énergétique et l’impact environnemental de leur logement.

Ce projet s’inscrit dans un cadre académique et vise à exploiter les **données publiques de l’ADEME** afin de :
- analyser les caractéristiques énergétiques des logements,
- identifier les logements énergivores,
- construire des modèles de Machine Learning permettant d’estimer le statut énergétique et la consommation de chauffage.

L’étude se concentre sur les **logements existants du département du Rhône (69)**.

---

## 2. Données utilisées

### 2.1 Source des données

Les données proviennent de la base **DPE logements existants – ADEME**, mise à disposition en open data.  
Elles regroupent des diagnostics réels réalisés sur des logements résidentiels.

---

### 2.2 Périmètre de l’étude

- Zone géographique : département du Rhône (69)
- Type de logements : logements existants
- Taille du jeu de données après nettoyage : environ 16 000 observations
- Nombre de variables initiales : plus de 200

Un travail de sélection a été réalisé afin de ne conserver que les variables pertinentes pour l’analyse et la modélisation.

---

### 2.3 Variables étudiées

Les variables exploitées concernent principalement :
- les caractéristiques physiques du logement (surface, année de construction),
- le type de bâtiment,
- le type d’énergie principale,
- le système de chauffage.

Les variables directement issues du calcul réglementaire du DPE 
(étiquette DPE, consommations détaillées, indicateurs énergétiques) 
n’ont pas été utilisées comme variables explicatives afin d’éviter tout 
data leakage. Seules des variables descriptives du logement ont été conservées.

---

## 3. Analyse exploratoire des données

L’analyse exploratoire met en évidence plusieurs tendances générales :

- Les logements anciens présentent en moyenne une consommation de chauffage plus élevée.
- Les logements classés **E, F et G** sont majoritairement associés à :
  - des années de construction antérieures aux réglementations thermiques récentes,
  - des systèmes de chauffage moins performants.
- Une relation positive est observée entre la surface habitable et la consommation de chauffage.

Ces constats ont guidé la construction des modèles prédictifs.

---

## 4. Problématiques de modélisation

Deux problématiques distinctes ont été abordées :

### 4.1 Classification : identification des passoires énergétiques

**Objectif**  
Déterminer si un logement est une **passoire énergétique**.

- Variable cible :
  - 1 : passoire énergétique (étiquettes E, F, G)
  - 0 : non passoire (étiquettes A, B, C, D)

Cette formulation permet de simplifier l’analyse tout en répondant à un enjeu énergétique concret.

---

### 4.2 Régression : estimation de la consommation de chauffage

**Objectif**  
Estimer la **consommation annuelle de chauffage** d’un logement à partir de ses caractéristiques physiques.

La variable cible est exprimée en kWh.  
Toutes les variables susceptibles d’introduire un biais ou une fuite d’information ont été exclues.

---

## 5. Méthodologie

### 5.1 Prétraitement

- Suppression des valeurs manquantes critiques
- Encodage des variables catégorielles
- Séparation des variables explicatives et des variables cibles
- Division du jeu de données en ensembles d’entraînement et de test

---

### 5.2 Modèles utilisés

Les algorithmes suivants ont été mobilisés, conformément aux méthodes abordées en cours :

- **Classification** :
  - Random Forest Classifier

- **Régression** :
  - Random Forest Regressor

La Random Forest a été privilégiée pour la classification des passoires énergétiques car elle permet de modéliser des relations non linéaires et des interactions complexes entre les caractéristiques du logement, tout en restant robuste aux variables catégorielles encodées.

Les hyperparamètres ont été optimisés à l’aide de **GridSearchCV**.

---

## 6. Évaluation des modèles

### 6.1 Métriques de classification

Les performances du modèle de classification ont été évaluées à l’aide de :
- l’accuracy,
- la matrice de confusion.


Une attention particulière a été portée au **recall**, afin de limiter le nombre de passoires énergétiques non détectées.

---

### 6.2 Métriques de régression

Les performances du modèle de régression ont été évaluées à l’aide de :
- le coefficient de détermination R²,
- la Root Mean Squared Error (RMSE).


Les résultats obtenus indiquent une capacité satisfaisante du modèle à estimer la consommation de chauffage, compte tenu de la variabilité des logements.

---

## 7. Interprétation des résultats

L’analyse des modèles met en évidence l’importance de plusieurs facteurs :
- l’année de construction,
- la surface habitable,
- le type d’énergie de chauffage,
- le type de bâtiment.

Ces résultats sont cohérents avec l’importance des variables observée dans les modèles de type Random Forest, notamment pour l’année de construction et la surface habitable.


---

## 8. Limites de l’étude

Plusieurs limites doivent être prises en compte :
- hétérogénéité des diagnostics DPE,
- absence de certaines informations techniques détaillées (isolation, équipements),
- périmètre géographique limité à un seul département.

Ces éléments peuvent influencer la précision des prédictions.

---

## 9. Conclusion et perspectives

Ce travail a permis de mettre en œuvre une démarche complète de **data science**, allant de l’exploration des données à la modélisation prédictive.

Les perspectives d’amélioration incluent :
- l’intégration de données climatiques,
- l’extension de l’étude à d’autres départements,
- l’enrichissement des modèles avec davantage de données descriptives.

Ce projet constitue une base solide pour une application d’aide à la compréhension et à la sensibilisation énergétique.

---

