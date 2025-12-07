import streamlit as st
import pandas as pd
import base64   # <-- nécessaire pour le footer

# ---------------------------------
# CONFIG PAGE
# ---------------------------------
st.set_page_config(
    page_title="Contexte - Projet DPE - M2 SISE",
    page_icon="assets/logo_green.png",
    layout="wide",
)

# ---------------------------------
# STYLE GLOBAL
# ---------------------------------
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

    [data-testid="stSidebarNav"] li:nth-child(6) a::before {
        content: "📬 ";
    }


    [data-testid="stSidebarNav"] li:nth-child(5) a::before {
        content: "  ";
    }

    /* ----- HEADER ----- */
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

    /* ----- CARTES DE CONTENU ----- */
    .section-card {
        background: white;
        padding: 25px;
        border-radius: 12px;
        box-shadow: 0px 4px 12px rgba(0,0,0,0.08);
        margin-bottom: 25px;
    }

    /* ----- FOOTER ANIME DANS LA SIDEBAR ----- */
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


# ---------------------------------
# FOOTER (logo animé)
# ---------------------------------

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


# ---------------------------------
# HEADER 
# ---------------------------------
st.markdown("""
<div class="header-box">
    <h1>📚 Contexte & Données DPE</h1>
    <p class="subtitle">
        Cette page présente les <b>données DPE</b> utilisées dans l'application.<br>
        Source : ADEME – DPE logements existants<br>
    </p>
</div>
""", unsafe_allow_html=True)

# ---------------------------------
# CHARGEMENT DONNÉES
# ---------------------------------
@st.cache_data
def load_data():
    df = pd.read_csv("data/dpe_existant.csv")
    return df

df = load_data()

# ---------------------------------
# CONTENU PRINCIPAL
# ---------------------------------
st.markdown("""
<div class="section-card">
    <h2>Aperçu du jeu de données</h2>
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Nombre de lignes", len(df))

with col2:
    st.metric("Nombre de colonnes", df.shape[1])

with col3:
    if "classe_consommation_energie" in df.columns:
        pct_passoires = df["classe_consommation_energie"].isin(["E", "F", "G"]).mean() * 100
        st.metric("% de passoires (E/F/G)", f"{pct_passoires:.1f} %")
    else:
        st.write("Étiquette DPE non trouvée")

st.markdown("""
<div class="section-card">
    <h2>Aperçu du tableau</h2>
</div>
""", unsafe_allow_html=True)

nb_lignes = st.slider("Nombre de lignes à afficher", 5, 50, 10)
st.dataframe(df.head(nb_lignes))

st.markdown("""
<div class="section-card">
    <h2>Dictionnaire de variables</h2>
    <p>
    Quelques colonnes importantes :<br><br>
    - <code>surface_habitable</code> : surface du logement (m²)<br>
    - <code>annee_construction</code> : année de construction du bâtiment<br>
    - <code>classe_consommation_energie</code> : étiquette DPE (A à G)<br>
    - <code>consommation_chauffage</code> : estimation conso chauffage<br>
    - <code>type_energie_chauffage</code> : type d'énergie de chauffage<br>
    - <code>longitude</code>, <code>latitude</code> : localisation<br>
    </p>
</div>
""", unsafe_allow_html=True)
