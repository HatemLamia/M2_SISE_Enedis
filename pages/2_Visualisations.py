import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import base64  # pour le footer

# ---------------------------
# CONFIG DE LA PAGE
# ---------------------------
st.set_page_config(
    page_title="Visualisations - Projet DPE - M2 SISE",
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

    /* Bouton actif → vert */
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
    [data-testid="stSidebarNav"] li:nth-child(1) a::before {
        content: "🏠";
        font-size: 18px;
        font-weight: bold;
    }

    [data-testid="stSidebarNav"] li:nth-child(2) a::before {
        content: "📚  ";
    }

    [data-testid="stSidebarNav"] li:nth-child(3) a::before {
        content: "📈  ";
    }

    [data-testid="stSidebarNav"] li:nth-child(4) a::before {
        content: "🗺️  ";
    }

    [data-testid="stSidebarNav"] li:nth-child(5) a::before {
        content: "🔮  ";
    }

    [data-testid="stSidebarNav"] li:nth-child(6) a::before {
        content: "📬 ";
    }

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

    /* ----- TABS (onglets) ----- */
    div[data-testid="stTabs"] {
        margin-top: 10px;
    }

    div[data-testid="stTabs"] button {
        border-radius: 8px 8px 0 0;
        padding: 0.5rem 1.5rem;
        font-weight: 600;
        border: none;
    }

    div[data-testid="stTabs"] button[aria-selected="true"] {
        background-color: #2e7d32;
        color: white;
    }

    div[data-testid="stTabs"] button[aria-selected="false"] {
        background-color: #e8f5e9;
        color: #1b5e20;
    }

    /* ----- FOOTER ANIMÉ DANS LA SIDEBAR ----- */
    .sidebar-footer {
        position: fixed;
        bottom: 25px;
        left: 0;
        width: 16rem;              /* approx largeur sidebar */
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

    @keyframes floatLeaf {
        0%   { transform: translateY(0px); }
        50%  { transform: translateY(-6px); }
        100% { transform: translateY(0px); }
    }

    @keyframes glowLeaf {
        0%   { filter: drop-shadow(0 0 4px #66bb6a); }
        50%  { filter: drop-shadow(0 0 14px #a5d6a7); }
        100% { filter: drop-shadow(0 0 4px #66bb6a); }
    }

</style>
""", unsafe_allow_html=True)

# ---------- FOOTER VISUEL DANS LA SIDEBAR ----------
def load_image_base64(path):
    with open(path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

logo_base64 = load_image_base64("assets/logo_green.png")

with st.sidebar:
    st.markdown(f"""
    <div class="sidebar-footer">
        <img src="data:image/png;base64,{logo_base64}" class="sidebar-footer-icon">
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
    <h1>📈 Visualisations des diagnostics DPE</h1>
    <p class="subtitle">
        Cette page permet d'explorer les données DPE avec des <b>filtres</b> et plusieurs
        <b>types de graphiques</b> (histogramme, barres, boxplot, nuage de points) accessibles via les onglets ci-dessous.
    </p>
</div>
""", unsafe_allow_html=True)

# =========================
# 1. Chargement des données
# =========================
@st.cache_data
def load_data():
    # adapte le nom de fichier si besoin (data_69.csv ou dpe_existant.csv)
    df = pd.read_csv("data/dpe_existant.csv")

    # On s'assure que certaines colonnes sont bien numériques
    if "Année_construction" in df.columns:
        df["Année_construction"] = pd.to_numeric(df["Année_construction"], errors="coerce")

    if "Surface_habitable_logement" in df.columns:
        df["Surface_habitable_logement"] = pd.to_numeric(
            df["Surface_habitable_logement"], errors="coerce"
        )

    if "Conso_chauffage_é_finale" in df.columns:
        df["Conso_chauffage_é_finale"] = pd.to_numeric(
            df["Conso_chauffage_é_finale"], errors="coerce"
        )

    return df

df = load_data()

# Colonnes importantes (adaptées à ton dataset ADEME)
COL_DPE = "Etiquette_DPE"
COL_YEAR = "Année_construction"
COL_SURF = "Surface_habitable_logement"
COL_CONSO = "Conso_chauffage_é_finale"
COL_ENERGIE = "Type_énergie_n°1"

# =========================
# 2. Filtres
# =========================
st.markdown("### 🔍 Filtres")

col_f1, col_f2 = st.columns(2)

with col_f1:
    # Filtre sur l'année de construction
    if COL_YEAR in df.columns:
        min_year = int(df[COL_YEAR].min())
        max_year = int(df[COL_YEAR].max())
        year_range = st.slider(
            "Année de construction",
            min_year, max_year,
            (min_year, max_year)
        )
        df = df[(df[COL_YEAR] >= year_range[0]) & (df[COL_YEAR] <= year_range[1])]

with col_f2:
    # Filtre sur l'étiquette DPE
    if COL_DPE in df.columns:
        dpe_unique = sorted(df[COL_DPE].dropna().unique())
        dpe_selected = st.multiselect(
            "Étiquettes DPE",
            options=dpe_unique,
            default=dpe_unique
        )
        df = df[df[COL_DPE].isin(dpe_selected)]

# Ligne suivante : filtre énergie sur toute la largeur
# (tu peux le remettre en colonne si tu préfères)
if COL_ENERGIE in df.columns:
    energies = sorted(df[COL_ENERGIE].dropna().unique())
    energie_selected = st.multiselect(
        "Énergie principale (Type_énergie_n°1)",
        options=energies,
        default=energies
    )
    df = df[df[COL_ENERGIE].isin(energie_selected)]

st.success(f"Nombre de lignes après filtres : {len(df)}")

# Séparateur visuel avant les graphiques
st.markdown("---")

# =========================
# 3. ONGLETs DE VISUALISATION
# =========================
tab1, tab2, tab3, tab4 = st.tabs([
    "📏 Surfaces habitables",
    "🏷️ Répartition des étiquettes DPE",
    "🔥 Conso chauffage vs DPE (boxplot)",
    "🌡️ Surface vs conso chauffage"
])

# ---- Tab 1 : histogramme des surfaces ----
with tab1:
    st.subheader("📏 Répartition des surfaces habitables")
    if COL_SURF in df.columns:
        fig, ax = plt.subplots()
        df[COL_SURF].dropna().plot(kind="hist", bins=30, ax=ax)
        ax.set_xlabel("Surface habitable du logement (m²)")
        ax.set_ylabel("Nombre de logements")
        st.pyplot(fig)
    else:
        st.info("La colonne 'Surface_habitable_logement' est introuvable dans le dataset.")

# ---- Tab 2 : barres des étiquettes DPE ----
with tab2:
    st.subheader("🏷️ Répartition des étiquettes DPE")
    if COL_DPE in df.columns:
        fig, ax = plt.subplots()
        df[COL_DPE].value_counts().sort_index().plot(kind="bar", ax=ax)
        ax.set_xlabel("Étiquette DPE")
        ax.set_ylabel("Nombre de logements")
        st.pyplot(fig)
    else:
        st.info("La colonne 'Etiquette_DPE' est introuvable dans le dataset.")

# ---- Tab 3 : boxplot conso vs DPE ----
with tab3:
    st.subheader("🔥 Consommation de chauffage par étiquette DPE (boxplot)")
    if COL_CONSO in df.columns and COL_DPE in df.columns:
        fig, ax = plt.subplots()
        df.boxplot(column=COL_CONSO, by=COL_DPE, ax=ax)
        ax.set_xlabel("Étiquette DPE")
        ax.set_ylabel("Conso_chauffage_é_finale")
        plt.suptitle("")  # enlève le titre automatique de pandas
        st.pyplot(fig)
    else:
        st.info("Impossible de construire le boxplot (colonne conso ou DPE manquante).")

# ---- Tab 4 : nuage de points surface vs conso ----
with tab4:
    st.subheader("🌡️ Relation entre surface et consommation de chauffage")
    if COL_SURF in df.columns and COL_CONSO in df.columns:
        fig, ax = plt.subplots()
        ax.scatter(df[COL_SURF], df[COL_CONSO], alpha=0.3)
        ax.set_xlabel("Surface habitable (m²)")
        ax.set_ylabel("Conso_chauffage_é_finale")
        st.pyplot(fig)
    else:
        st.info("Impossible d'afficher le nuage de points (surface ou conso manquante).")
