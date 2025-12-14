# -*- coding: utf-8 -*-
"""
Nettoyage MINIMAL du dataset DPE
Objectif : sécuriser les données avant entraînement des modèles ML
Sans modifier la logique de train_models.py
"""

import pandas as pd

# ============================================================
# 1. Chemins
# ============================================================
INPUT_PATH = "data/dpe_existant.csv"
OUTPUT_PATH = "data/dpe_existant_clean.csv"

print(f"📂 Chargement des données depuis {INPUT_PATH}")
df = pd.read_csv(INPUT_PATH, low_memory=False)
print("Avant nettoyage :", df.shape)

# ============================================================
# 2. Correction des problèmes d'encodage des colonnes
# ============================================================
rename_map = {
    "AnnÃ©e_construction": "Année_construction",
    "Type_bÃ¢timent": "Type_bâtiment",
    "Type_Ã©nergie_principale_chauffage": "Type_énergie_principale_chauffage",
}
df = df.rename(columns=rename_map)

# ============================================================
# 3. Colonnes strictement nécessaires au modèle
# ============================================================
REQUIRED_COLS = [
    "Surface_habitable_logement",
    "Année_construction",
    "Type_énergie_principale_chauffage",
    "Type_bâtiment",
    "Type_installation_chauffage",
    "Code_postal_(brut)",
    "Etiquette_DPE",
    "Conso_chauffage_é_finale",
]

missing = [c for c in REQUIRED_COLS if c not in df.columns]
if missing:
    raise ValueError(f"Colonnes manquantes dans le CSV : {missing}")

df = df.copy()

# ============================================================
# 4. Conversions numériques minimales
# ============================================================
for col in [
    "Surface_habitable_logement",
    "Année_construction",
    "Conso_chauffage_é_finale",
    "Code_postal_(brut)",
]:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# ============================================================
# 5. Suppression STRICTE des lignes inutilisables
# ============================================================
df = df.dropna(subset=REQUIRED_COLS)

print("Après suppression NaN critiques :", df.shape)

# ============================================================
# 6. Export du dataset nettoyé
# ============================================================
df.to_csv(OUTPUT_PATH, index=False, encoding="utf-8")

print(f"✅ Dataset nettoyé enregistré : {OUTPUT_PATH}")
