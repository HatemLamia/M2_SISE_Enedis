# 🏡 GreenSolutions — Analyse & Prédiction du DPE (Rhône – 69)

<p align="center">
  <img src="./assets/logo_green.png" alt="GreenSolutions Logo" width="160">
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Streamlit-App-FF4B4B?logo=streamlit&logoColor=white" />
  <img src="https://img.shields.io/badge/Scikit--Learn-ML-F7931E?logo=scikit-learn&logoColor=white" />
  <img src="https://img.shields.io/badge/ADEME-Données%20publiques-2E7D32" />
</p>

---

## 📘 Présentation générale

**GreenSolutions** est une application web interactive développée dans le cadre du **Master 2 SISE**.  
Elle exploite les **données publiques de l’ADEME (DPE logements existants)** afin d’analyser et d’estimer la performance énergétique des logements du **département du Rhône (69)**.

Le projet s’inscrit dans une **version simplifiée du sujet initial**, conformément aux consignes pédagogiques :
- sans API,
- sans Docker,
- sans intelligence artificielle générative.

---

## 🎯 Objectifs du projet

L’application a pour objectifs de :
- proposer une **exploration visuelle** des diagnostics de performance énergétique,
- offrir une **cartographie interactive** des logements,
- permettre une **estimation du statut énergétique** d’un logement (passoire ou non),
- estimer la **consommation annuelle de chauffage** à partir de caractéristiques déclarées.

---

## ▶️ Lancement de l'application en local

### Prérequis
- Anaconda installé sur votre machine
- Python 3.11

### Étapes d'installation et d'exécution

1. **Cloner le dépôt**
```bash
git clone <url-du-depot>
```
2. **Ouvrir le terminal Anaconda**

3. **Se positionner dans le dossier du projet**
```bash
cd <nom-du-projet>
```
4. **Création et activation de l’environnement**
```bash
conda create -n greensolutions python=3.11
conda activate greensolutions
```

5. **Installation des dépendances**
```bash
pip install -r requirements.txt
```

6. **Préparation des données**
```bash
python clean_dpe_dataset.py
```

7. **Entraînement des modèles**
```bash
python train_models.py
```

8. **Lancement de l’application Streamlit**
```bash
streamlit run Home.py
```
---

## 🧩 Fonctionnalités (vue d’ensemble)

- Consultation du **contexte et des données DPE**
- Visualisations interactives avec filtres dynamiques
- Carte interactive des logements du Rhône
- Formulaire de prédiction énergétique
- Page de contact et informations projet

> Le détail fonctionnel de chaque page est décrit dans la **documentation fonctionnelle**.

---

## 🗂️ Structure du dépôt

```text
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
├── README.md
└── LICENSE
```

## 🚀 Accès à l’application

L’application GreenSolutions est consultable depuis un navigateur web, soit en environnement local, soit via une version déployée en ligne.

| Type d’accès | Adresse | Remarque |
|-------------|---------|----------|
| Local | http://localhost:8501 | Lancement de l’application en local |
| En ligne | https://greensolutions69.streamlit.app/ | Application déployée et accessible via une URL publique |

Les fonctionnalités disponibles sont identiques quel que soit le mode d’accès.

---

## 👤 Auteur

**Hatem Lamia**  
Master 2 SISE  
Projet académique – 2024/2025