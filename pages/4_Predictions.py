import numpy as np
import pandas as pd
import joblib
from pathlib import Path
import streamlit as st
import base64  # pour le footer

# ---------------------------
# CONFIG DE LA PAGE
# ---------------------------
st.set_page_config(
    page_title="Prédictions - Projet DPE - M2 SISE",
    page_icon="assets/logo_green.png",
    layout="wide",
)

# ---------------------------
# STYLE GLOBAL
# ---------------------------
st.markdown("""
<style>

    /* ----- STYLE GLOBAL ----- */
    .main {
        background: #f3f7f4;
    }

    h1, h2, h3 {
        color: #1b5e20;
    }

    /* ----- SIDEBAR ----- */
    [data-testid="stSidebar"] {
        background-color: #0f172a !important;
        padding-top: 30px;
    }

    /* Texte en blanc */
    [data-testid="stSidebar"] * {
        color: #e8f5e9 !important;
    }

    /* Bouton actif */
    .css-1v0mbdj, .css-17lntkn, .css-1jneuhg {
        background-color: #2e7d32 !important;
        color: white !important;
        border-radius: 10px;
        font-weight: bold;
    }

    /* Hover */
    .css-1oe5cao:hover, .css-1o6k8w4:hover {
        background-color: rgba(46,125,50,0.2) !important;
        border-radius: 10px;
    }

    /* ----- ICÔNES DU MENU ----- */
    [data-testid="stSidebarNav"] li:nth-child(1) a::before { content: "🏠"; font-size: 18px; font-weight: bold; }
    [data-testid="stSidebarNav"] li:nth-child(2) a::before { content: "📚"; }
    [data-testid="stSidebarNav"] li:nth-child(3) a::before { content: "📈"; }
    [data-testid="stSidebarNav"] li:nth-child(4) a::before { content: "🗺️"; }
    [data-testid="stSidebarNav"] li:nth-child(5) a::before { content: "🔮"; }
    [data-testid="stSidebarNav"] li:nth-child(6) a::before { content: "📬"; }        

    /* ----- HEADER (barre verte) ----- */
    .header-box {
        background: #2e7d32;
        padding: 30px 30px;
        border-radius: 15px;
        color: white;
        box-shadow: 0 4px 15px rgba(0,0,0,0.15);
        margin-bottom: 35px;
    }

    .subtitle {
        font-size: 16px;
        color: #e8f5e9;
        margin-top: 5px;
    }

    /* ----- FOOTER ANIMÉ ----- */
    .sidebar-footer {
        position: fixed;
        bottom: 25px;
        left: 0;
        width: 16rem;
        text-align: center;
        pointer-events: none;
    }

    .sidebar-footer-icon {
        width: 55px;
        height: 55px;
        margin-bottom: 4px;
        display: inline-block;
        animation: floatLeaf 3s ease-in-out infinite, glowLeaf 2.5s ease-in-out infinite;
    }

    .sidebar-footer-text {
        font-size: 11px;
        opacity: 0.9;
        line-height: 1.3;
    }

    @keyframes floatLeaf { 0%{transform:translateY(0);} 50%{transform:translateY(-6px);} 100%{transform:translateY(0);} }
    @keyframes glowLeaf { 0%{filter:drop-shadow(0 0 4px #66bb6a);} 50%{filter:drop-shadow(0 0 14px #a5d6a7);} 100%{filter:drop-shadow(0 0 4px #66bb6a);} }

</style>
""", unsafe_allow_html=True)

# ---------------------------
# FOOTER
# ---------------------------
def load_image_base64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

logo_b64 = load_image_base64("assets/logo_green.png")

with st.sidebar:
    st.markdown(f"""
    <div class="sidebar-footer">
        <img src="data:image/png;base64,{logo_b64}" class="sidebar-footer-icon">
        <div class="sidebar-footer-text">
            GreenSolutions<br>
            <span>Énergie plus propre, avenir plus vert</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ---------------------------
# HEADER
# ---------------------------
st.markdown("""
<div class="header-box">
    <h1>🔮 Prédiction du statut énergétique de votre logement</h1>
    <p class="subtitle">
        Décrivez votre logement et obtenez :<br>
        • si c’est une <b>passoire énergétique</b> (E/F/G) ou pas (A/B/C/D)<br>
        • une estimation de la <b>consommation de chauffage</b>.
    </p>
</div>
""", unsafe_allow_html=True)

# ======================================================
# 1. Load data & models
# ======================================================
@st.cache_data
def load_data():
    df_local = pd.read_csv("data/dpe_existant.csv", low_memory=False)

    # Correction éventuelle des noms de colonnes mal encodés
    rename_map = {
        "AnnÃ©e_construction": "Année_construction",
        "Type_bÃ¢timent": "Type_bâtiment",
        "Type_Ã©nergie_principale_chauffage": "Type_énergie_principale_chauffage",
    }
    df_local = df_local.rename(columns=rename_map)
    return df_local

@st.cache_resource
def load_models():
    clf = joblib.load("models/model_classification.pkl")
    reg = joblib.load("models/model_regression.pkl")
    return clf, reg

try:
    df = load_data()
    model_clf, model_reg = load_models()
except Exception as e:
    st.error("❌ Erreur de chargement : " + str(e))
    st.stop()

# ======================================================
# 2. Constantes & préparation des infos pour le formulaire
# ======================================================
COL_SURF = "Surface_habitable_logement"
COL_YEAR = "Année_construction"
COL_ENERGIE = "Type_énergie_principale_chauffage"
COL_BAT = "Type_bâtiment"
COL_INSTALL = "Type_installation_chauffage"
COL_CP = "Code_postal_(brut)"

# Préparation pour sliders
df[COL_SURF] = pd.to_numeric(df[COL_SURF], errors="coerce")
df[COL_YEAR] = pd.to_numeric(df[COL_YEAR], errors="coerce")
df = df.dropna(subset=[COL_SURF, COL_YEAR])

min_surf, max_surf = df[COL_SURF].min(), df[COL_SURF].max()
min_year, max_year = int(df[COL_YEAR].min()), int(df[COL_YEAR].max())
median_year = int(df[COL_YEAR].median())

# On pourrait prendre les énergies du dataset, mais tu as spécifié des valeurs possibles fixes
energies = ["Électricité", "Gaz", "Fioul", "Bois", "Autre"]

# Codes postaux valides pour la ville de Lyon (arrondissements 1 à 9)
LYON_ZIP_CODES = {str(c) for c in range(69001, 69010)}

# ======================================================
# 3. Formulaire utilisateur
# ======================================================
st.markdown("### 🧾 Décrire le logement")

cout_total = None  # coût annuel estimé (toujours calculé, plus de saisie)

with st.form("form_pred"):

    # --- Localisation ---
    st.subheader("🏙️ Localisation")
    postal_code = st.selectbox(
        "Code postal (Lyon uniquement)",
        sorted(LYON_ZIP_CODES),
        key="cp_input",
    )

    # --- Caractéristiques quantitatives ---
    st.subheader("🔹 Caractéristiques quantitatives")

    col1, col2 = st.columns(2)
    with col1:
        surface = st.slider(
            "Surface habitable du logement (m²)",
            9.0, 100.0, 70.0,
            key="surface_input"
        )
    with col2:
        year_built = st.slider(
            "Année de construction",
            1900, 2024, median_year,
            key="year_input"
        )

    # âge du bâtiment (si tu veux l'afficher ou l'utiliser plus tard)
    building_age = 2024 - year_built

    # --- Caractéristiques qualitatives ---
    st.subheader("🔹 Caractéristiques qualitatives")
    col5, col6 = st.columns(2)

    with col5:
        building_type = st.selectbox(
            "Type de bâtiment",
            ["Maison", "Immeuble", "Appartement", "RDC"],
            key="type_batiment_input"
        )

    with col6:
        energie = st.selectbox(
            "Type d’énergie principale de chauffage",
            energies,
            key="energie_input"
        )

    type_installation = st.selectbox(
        "Type d’installation de chauffage",
        ["Individuelle", "Collectif", "Mixte"],
        key="type_installation_input"
    )

    # ---- Boutons ----
    col_btn1, col_btn2 = st.columns(2)
    with col_btn1:
        submitted = st.form_submit_button(
            "🔮 Lancer la prédiction",
            use_container_width=True
        )
    with col_btn2:
        reset_pressed = st.form_submit_button(
            "🧹 Réinitialiser",
            use_container_width=True
        )

# RESET
if reset_pressed:
    for k in list(st.session_state.keys()):
        if k.endswith("_input"):
            del st.session_state[k]
    st.rerun()

# ======================================================
# 4. Prédiction
# ======================================================
if submitted:

    # --- contrôle du code postal ---
    cp = postal_code.strip()

    if not cp:
        st.error("❌ Merci d'indiquer un code postal.")
        st.stop()

    if not cp.isdigit() or len(cp) != 5:
        st.error("❌ Merci de saisir un code postal à 5 chiffres (ex : 69003).")
        st.stop()

    if cp not in LYON_ZIP_CODES:
        st.error("❌ Ce code postal n'appartient pas à la ville de Lyon (69001 à 69009).")
        st.stop()

    # =========================================
    # CONSTRUCTION DE X_new AVEC TOUTES LES COLONNES
    # =========================================
    X_new = pd.DataFrame({
        COL_SURF: [surface],
        COL_YEAR: [year_built],
        COL_ENERGIE: [energie],
        COL_BAT: [building_type],
        COL_INSTALL: [type_installation],
        COL_CP: [cp],   # string, comme dans l'entraînement
    })

    # DEBUG éventuel :
    # st.write("X_new :", X_new)
    # st.write("Colonnes X_new :", list(X_new.columns))

    # --- Classification ---
    y_proba = model_clf.predict_proba(X_new)[0, 1]
    y_pred = model_clf.predict(X_new)[0]

    # --- Régression ---
    conso_pred = model_reg.predict(X_new)[0]

    # coût estimé automatiquement (ex : 0.20 €/kWh)
    if cout_total is None:
        estimated_cost = conso_pred * 0.20
    else:
        estimated_cost = cout_total

    # Interprétation du résultat classification
    if y_pred == 1:
        # Passoire
        dpe_letter = "F"
        dpe_group = "E–G (passoire énergétique)"
        color_bg = "#ffebee"
        color_border = "#c62828"
        color_text = "#b71c1c"
        emoji = "🔴"
        texte = "Logement évalué comme PASSOIRE énergétique (E–G)"
        result_img = "assets/bad.png"
    else:
        # Non passoire
        dpe_letter = "C"
        dpe_group = "A–D (non passoire)"
        color_bg = "#e8f5e9"
        color_border = "#2e7d32"
        color_text = "#1b5e20"
        emoji = "🟢"
        texte = "Logement évalué comme NON passoire (A–D)"
        result_img = "assets/good.png"

    # Formatage des nombres
    cout_fmt = f"{estimated_cost:,.0f}".replace(",", " ")
    conso_fmt = f"{conso_pred:,.0f}".replace(",", " ")
    proba_fmt = f"{y_proba*100:,.1f}".replace(",", " ")

    # =====================
    # Affichage des résultats
    # =====================
    st.markdown("## 🧠 Résultat de la prédiction")

    colA, colB = st.columns([2, 1])
    with colA:
        st.markdown(f"""
        <div style="
            background:{color_bg};
            border-left:6px solid {color_border};
            padding:18px 20px;
            border-radius:12px;
        ">
            <div style="font-size:20px; font-weight:700; color:{color_text}; margin-bottom:6px;">
                {emoji} {texte}
            </div>
            <div style="font-size:14px; color:#37474f;">
                Probabilité : <b>{proba_fmt} %</b><br>
                Classe estimée : <b>{dpe_group}</b>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with colB:
        if Path(result_img).exists():
            st.image(result_img, width=220)
        else:
            st.error(f"Image introuvable : {result_img}")

    # --- Metrics
    st.markdown("### 📊 Indicateurs clés")
    col1, col2, col3 = st.columns(3)
    col1.metric("Coût annuel estimé", f"{cout_fmt} € / an")
    col2.metric("Conso chauffage", conso_fmt)
    col3.metric("Surface", f"{surface:.1f} m²")
