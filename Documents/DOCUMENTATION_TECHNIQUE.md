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

### Installation
```bash
pip install -r requirements.txt
```

### Lancement
```bash
streamlit run Home.py
```

## Accès à l’application en local

Une fois l’application lancée en local via Streamlit, l’utilisateur peut accéder à l’interface web depuis un navigateur.

| Service | URL locale | Description |
|--------|-----------|-------------|
| Application Streamlit | http://localhost:8501 | Interface utilisateur de l’application GreenSolutions |

L’ensemble des fonctionnalités (visualisations, cartographie, prédictions) est accessible depuis cette interface.


---

## 8. Conclusion

Cette documentation technique présente une architecture simple et reproductible, conforme aux exigences du cahier des charges et adaptée à un projet académique en version simplifiée.
