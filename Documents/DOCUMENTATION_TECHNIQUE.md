# Documentation technique  
## Application GreenSolutions – Diagnostic de Performance Énergétique (DPE)

---

## 1. Objectif du document

Cette documentation technique décrit l’architecture logicielle, l’organisation du code et les éléments nécessaires à l’installation et à l’exécution de l’application **GreenSolutions**.

Elle se concentre exclusivement sur les aspects techniques de l’application.  
Les fonctionnalités utilisateur et l’analyse des modèles sont décrites dans des documents distincts.

---

## 2. Architecture générale de l’application

L’application repose sur une architecture **monolithique Streamlit**, adaptée à un projet académique individuel et à une exécution locale.

L’ensemble des composants (préparation des données, chargement des modèles, visualisations et prédictions) est regroupé dans une même application Python.

<p align="center">
  <img src="../assets/architecture_greensolutions.png" alt="Schéma d’architecture GreenSolutions" width="100%">
</p>

---

## 3. Pipeline technique

Le fonctionnement technique de l’application suit les étapes suivantes :

1. **Préparation des données**  
   Les données DPE issues de l’ADEME sont nettoyées et préparées via un script Python dédié, puis exportées au format CSV.

2. **Entraînement des modèles**  
   Deux modèles sont entraînés hors application :
   - un modèle de classification (passoire énergétique ou non),
   - un modèle de régression (consommation de chauffage).  
   Les modèles sont sauvegardés au format `.pkl`.

3. **Chargement dans l’application**  
   Les modèles sauvegardés sont chargés au démarrage de l’application Streamlit.

4. **Interaction utilisateur**  
   L’utilisateur interagit avec l’application via un navigateur web pour accéder aux visualisations, à la cartographie et aux prédictions.

---

## 4. Organisation du projet

```
M2_ENEDIS/
│
├── assets/                     # Ressources graphiques
│   ├── architecture_greensolutions.png
│   ├── logo_green.png
│   ├── good.png
│   └── bad.png
│
├── data/                       # Données DPE
│   ├── dpe_existant.csv
│   └── dpe_existant_clean.csv
│
├── Documents/                  # Livrables Markdown
│   ├── RAPPORT_ETUDE_DPE.md
│   ├── DOCUMENTATION_TECHNIQUE.md
│   └── DOCUMENTATION_FONCTIONNELLE.md
│
├── models/                     # Modèles entraînés
│   ├── model_classification.pkl
│   └── model_regression.pkl
│
├── pages/                      # Pages Streamlit
│   ├── 1_Contexte.py
│   ├── 2_Visualisations.py
│   ├── 3_Carte.py
│   ├── 4_Predictions.py
│   └── 5_Contact.py
│
├── clean_dpe_dataset.py        # Préparation des données
├── train_models.py             # Entraînement des modèles
├── Home.py                     # Point d’entrée Streamlit
├── requirements.txt            # Dépendances Python
├── runtime.txt # Version Python pour le déploiement
└── README.md
```

---

## 5. Description des composants techniques

- **clean_dpe_dataset.py**  
  Script de nettoyage et de préparation des données DPE.

- **train_models.py**  
  Script dédié à l’entraînement et à la sauvegarde des modèles de Machine Learning.

- **Home.py**  
  Point d’entrée principal de l’application Streamlit.

- **pages/**  
  Modules correspondant aux différentes pages de l’interface utilisateur.

---

## 6. Technologies et bibliothèques

- **Langage** : Python 3.11  
- **Framework** : Streamlit  

Bibliothèques principales :
- pandas
- numpy
- scikit-learn
- matplotlib
- folium
- streamlit-folium
- pyproj
- joblib

---
## 7. Installation et exécution locale

```bash
# Création et activation d’un environnement Python dédié afin d’isoler les dépendances du projet
conda create -n greensolutions python=3.11
conda activate greensolutions

# Installation des bibliothèques Python requises (Streamlit, Machine Learning, visualisation, etc.)
pip install -r requirements.txt

# Nettoyage et préparation des données DPE à partir des fichiers bruts ADEME
# Cette étape génère un jeu de données prêt pour l’apprentissage des modèles
python clean_dpe_dataset.py

# Entraînement des modèles de Machine Learning :
# - classification des passoires énergétiques
# - régression de la consommation de chauffage
# Les modèles entraînés sont sauvegardés dans le dossier models/
python train_models.py

# Lancement de l’application Streamlit en local
streamlit run Home.py
```
## 8. Accès à l’application

L’application GreenSolutions est accessible via un navigateur web, aussi bien en local pour le développement que via une version déployée en ligne.  
Le fonctionnement et les fonctionnalités sont identiques dans les deux cas.

| Mode d’accès | URL | Description |
|-------------|-----|-------------|
| Accès local | http://localhost:8501 | Accès à l’application Streamlit en environnement local |
| Accès web (déployé) | https://greensolutions69.streamlit.app/ | Accès à l’application GreenSolutions via une URL publique |

L’interface permet d’accéder à l’ensemble des fonctionnalités : visualisations, cartographie et prédictions énergétiques.


---
## 9. Conclusion

Ce document présente l’organisation technique du projet et le déroulement des différentes étapes, depuis l’entraînement des modèles jusqu’à l’exécution de l’application.

