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
- pyproj
- joblib

---

## 7. Installation et exécution locale

### Prérequis
- Python 3.11
- pip

### Installation des prèrequis
Après avoir cloné le dépôt et s’être positionné à la racine du projet, installer les dépendances :
```bash
pip install -r requirements.txt
```
### Entraînement des modèles de Machine Learning

Avant de lancer l’application Streamlit, il est nécessaire d’entraîner les modèles de Machine Learning utilisés pour la classification et la régression.

Cette étape permet de générer les fichiers de modèles sauvegardés au format .pkl, qui seront ensuite chargés automatiquement par l’application.

L’entraînement s’effectue à l’aide du script suivant :
```bash
python train_models.py
```

À l’issue de l’exécution, les fichiers suivants sont générés dans le dossier models/ :

- model_classification.pkl : modèle de classification des passoires énergétiques,

- model_regression.pkl : modèle de régression de la consommation de chauffage.

⚠️ Cette étape est requise une seule fois, sauf en cas de modification des données ou des paramètres d’entraînement.

### Lancement de l'application
Une fois les modèles entraînés, lancer l’application Streamlit :
```bash
streamlit run Home.py
```

## Accès à l’application

L’application GreenSolutions est accessible via un navigateur web, aussi bien en local pour le développement que via une version déployée en ligne.  
Le fonctionnement et les fonctionnalités sont identiques dans les deux cas.

| Mode d’accès | URL | Description |
|-------------|-----|-------------|
| Accès local | http://localhost:8501 | Accès à l’application Streamlit en environnement local |
| Accès web (déployé) | https://greensolutions-app.example.com | Accès à l’application GreenSolutions via une URL publique |

L’interface permet d’accéder à l’ensemble des fonctionnalités : visualisations, cartographie et prédictions énergétiques.


---
## 8. Conclusion

Ce document présente l’organisation technique du projet et le déroulement des différentes étapes, depuis l’entraînement des modèles jusqu’à l’exécution de l’application.

