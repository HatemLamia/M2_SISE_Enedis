# -*- coding: utf-8 -*-
# Script pour entraîner les modèles de classification (passoire) et de régression
# à partir de data/dpe_existant.csv

import os
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    r2_score,
    mean_squared_error,
)
import joblib

# ============================================================
# 0. Création du dossier models/ s'il n'existe pas
# ============================================================
os.makedirs("models", exist_ok=True)

# ============================================================
# 1. Chargement des données
# ============================================================
DATA_PATH = "data/dpe_existant.csv"
print(f"📂 Chargement des données depuis {DATA_PATH} ...")
df = pd.read_csv(DATA_PATH, low_memory=False)

# ============================================================
# 1.0 Correction des éventuels problèmes d'encodage des colonnes
# (AnnÃ©e_construction, Type_bÃ¢timent, Type_Ã©nergie_principale_chauffage)
# ============================================================
rename_map = {
    "AnnÃ©e_construction": "Année_construction",
    "Type_bÃ¢timent": "Type_bâtiment",
    "Type_Ã©nergie_principale_chauffage": "Type_énergie_principale_chauffage",
}
df = df.rename(columns=rename_map)

# ============================================================
# 1.1 Définition des colonnes utilisées
# ============================================================
COL_SURF = "Surface_habitable_logement"
COL_YEAR = "Année_construction"
COL_ENERGIE = "Type_énergie_principale_chauffage"
COL_BAT = "Type_bâtiment"
COL_INSTALL = "Type_installation_chauffage"
COL_CP = "Code_postal_(brut)"

COL_DPE = "Etiquette_DPE"              # étiquette DPE (pour créer la cible passoire)
COL_CONSO = "Conso_chauffage_é_finale" # variable cible pour la régression

# Toutes les colonnes nécessaires (features + cibles)
required_cols = [
    COL_SURF,
    COL_YEAR,
    COL_ENERGIE,
    COL_BAT,
    COL_INSTALL,
    COL_CP,
    COL_DPE,
    COL_CONSO,
]

# On garde uniquement ces colonnes (si elles existent bien)
missing_cols = [c for c in required_cols if c not in df.columns]
if missing_cols:
    raise ValueError(f"Colonnes manquantes dans le CSV : {missing_cols}")

df = df[required_cols].copy()

# ============================================================
# 1.2 Conversions en numérique + filtre sur les codes postaux de Lyon
# ============================================================

# Colonnes numériques
df[COL_SURF] = pd.to_numeric(df[COL_SURF], errors="coerce")
df[COL_YEAR] = pd.to_numeric(df[COL_YEAR], errors="coerce")
df[COL_CONSO] = pd.to_numeric(df[COL_CONSO], errors="coerce")

# Code postal : numérique pour filtrer, puis reconverti en string (pour OneHotEncoder)
df[COL_CP] = pd.to_numeric(df[COL_CP], errors="coerce")

# Filtre : uniquement Lyon 69000 à 69009
df = df[(df[COL_CP] >= 69000) & (df[COL_CP] <= 69009)]

# Re-conversion en string pour le modèle (catégorielle)
df[COL_CP] = df[COL_CP].astype("Int64").astype(str)

# Suppression des lignes incomplètes sur les colonnes utilisées
df = df.dropna(subset=[
    COL_SURF,
    COL_YEAR,
    COL_ENERGIE,
    COL_BAT,
    COL_INSTALL,
    COL_CP,
    COL_DPE,
    COL_CONSO,
])
if df.empty:
    raise ValueError("Le dataframe est vide après nettoyage/filtrage. Vérifie les colonnes et les données.")
print("✅ Nombre de lignes après nettoyage :", len(df))

# ============================================================
# 2. Variable cible CLASSIFICATION : passoire (E/F/G) ou non
# ============================================================
df["passoire"] = df[COL_DPE].isin(["E", "F", "G"]).astype(int)

# Features pour la classification : les 6 champs du formulaire
feature_cols = [
    COL_SURF,
    COL_YEAR,
    COL_ENERGIE,
    COL_BAT,
    COL_INSTALL,
    COL_CP,
]

X_clf = df[feature_cols]
y_clf = df["passoire"]

# ============================================================
# 3. Préprocesseur (numérique + catégoriel)
# ============================================================
num_cols = [COL_SURF, COL_YEAR]
cat_cols = [COL_ENERGIE, COL_BAT, COL_INSTALL, COL_CP]

preprocess = ColumnTransformer(
    transformers=[
        ("num", "passthrough", num_cols),
        ("cat", OneHotEncoder(handle_unknown="ignore"), cat_cols),
    ]
)

# ============================================================
# 4. MODELE DE CLASSIFICATION (RandomForestClassifier)
# ============================================================
print("\n==== Entraînement modèle de CLASSIFICATION (passoires) ====")

clf = RandomForestClassifier(random_state=0)

pipe_clf = Pipeline(
    steps=[
        ("preprocess", preprocess),
        ("model", clf),
    ]
)

param_grid_clf = {
    "model__n_estimators": [100, 200],
    "model__max_depth": [5, 10, None],
}

Xc_train, Xc_test, yc_train, yc_test = train_test_split(
    X_clf,
    y_clf,
    test_size=0.2,
    random_state=0,
    stratify=y_clf,
)

grid_clf = GridSearchCV(pipe_clf, param_grid_clf, cv=3, n_jobs=-1)
grid_clf.fit(Xc_train, yc_train)

yc_pred = grid_clf.predict(Xc_test)
acc = accuracy_score(yc_test, yc_pred)
cm = confusion_matrix(yc_test, yc_pred)

print("⭐ Meilleurs paramètres (classification) :", grid_clf.best_params_)
print("🎯 Accuracy sur le test :", acc)
print("📊 Matrice de confusion :\n", cm)

joblib.dump(grid_clf.best_estimator_, "models/model_classification.pkl")
print("💾 Modèle de classification sauvegardé dans models/model_classification.pkl")

# ============================================================
# 5. MODELE DE REGRESSION (RandomForestRegressor)
# ============================================================
print("\n==== Entraînement modèle de REGRESSION (conso chauffage) ====")

# mêmes features que la classification (les 6 champs du formulaire)
X_reg = df[feature_cols]
y_reg = df[COL_CONSO]

reg = RandomForestRegressor(random_state=0)

pipe_reg = Pipeline(
    steps=[
        ("preprocess", preprocess),
        ("model", reg),
    ]
)

param_grid_reg = {
    "model__n_estimators": [100, 200],
    "model__max_depth": [5, 10, None],
}

Xr_train, Xr_test, yr_train, yr_test = train_test_split(
    X_reg,
    y_reg,
    test_size=0.2,
    random_state=0,
)

grid_reg = GridSearchCV(pipe_reg, param_grid_reg, cv=3, n_jobs=-1)
grid_reg.fit(Xr_train, yr_train)

yr_pred = grid_reg.predict(Xr_test)
r2 = r2_score(yr_test, yr_pred)
rmse = np.sqrt(mean_squared_error(yr_test, yr_pred))

print("⭐ Meilleurs paramètres (régression) :", grid_reg.best_params_)
print("📈 R² sur le test :", r2)
print("📉 RMSE sur le test :", rmse)

joblib.dump(grid_reg.best_estimator_, "models/model_regression.pkl")
print("💾 Modèle de régression sauvegardé dans models/model_regression.pkl")

print("\n🎉 Entraînement terminé.")
