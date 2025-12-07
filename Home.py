import streamlit as st
import base64

# ---------------------------
# Configuration de la page
# ---------------------------
st.set_page_config(
    page_title="Projet DPE - M2 SISE",
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
    /* 1 = MAISON (majuscule + icône) */
    [data-testid="stSidebarNav"] li:nth-child(1) a::before {
        content: "🏠  ";
        font-size: 18px;
        font-weight: bold;
    }

    /* 2 = CONTEXTE */
    [data-testid="stSidebarNav"] li:nth-child(2) a::before {
        content: "📚  ";
    }

    /* 3 = VISUALISATIONS */
    [data-testid="stSidebarNav"] li:nth-child(3) a::before {
        content: "📈  ";
    }

    /* 4 = CARTE */
    [data-testid="stSidebarNav"] li:nth-child(4) a::before {
        content: "🗺️  ";
    }

    /* 5 = PREDICTIONS */
    [data-testid="stSidebarNav"] li:nth-child(5) a::before {
        content: "🔮  ";
    }
            
    [data-testid="stSidebarNav"] li:nth-child(6) a::before {
        content: "📬 ";
    }
            

    /* ----- HEADER ----- */
    .header-box {
        background: #2e7d32;
        padding: 40px 30px;
        border-radius: 15px;
        color: white;
        box-shadow: 0 4px 15px rgba(0,0,0,0.15);
        margin-bottom: 35px;
    }

    .subtitle {
        font-size: 18px;
        color: #e8f5e9;
        margin-top: -10px;
    }

    /* ----- CARTES ----- */
    .feature-card {
        background: white;
        padding: 25px;
        border-radius: 12px;
        box-shadow: 0px 4px 12px rgba(0,0,0,0.08);
        border-left: 6px solid #2e7d32;
        transition: transform .2s ease;
    }

    .feature-card:hover {
        transform: translateY(-4px);
        box-shadow: 0px 6px 16px rgba(0,0,0,0.12);
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

    /* Version adaptée pour une image (glow via drop-shadow) */
    @keyframes glowLeaf {
        0%   { filter: drop-shadow(0 0 4px #66bb6a); }
        50%  { filter: drop-shadow(0 0 14px #a5d6a7); }
        100% { filter: drop-shadow(0 0 4px #66bb6a); }
    }

</style>
""", unsafe_allow_html=True)

# ---------------------------
# LOGO EN BASE64
# ---------------------------
def load_image_base64(path):
    with open(path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

logo_base64 = load_image_base64("assets/logo_green.png")

# --------- FOOTER VISUEL DANS LA SIDEBAR ----------
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
st.markdown(f"""
<div class="header-box" style="text-align:center;">
    <img src="data:image/png;base64,{logo_base64}" width="90" style="margin-bottom:15px;">
    <h1 style="color:white; margin-bottom:5px;">
        Bienvenue sur votre site GreenSolutions –
        <br> Rhône-Alpes 69.
    </h1>
    <p class="subtitle">
        Énergie plus propre, avenir plus vert.
    </p>
</div>
""", unsafe_allow_html=True)

# ---------------------------
# CONTENU PRINCIPAL
# ---------------------------
st.markdown("## 🌿 Aperçu des fonctionnalités :")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="feature-card">
        <h3>📚 Contexte</h3>
        <p>Aperçu des données ADEME & Dictionnaire de variables.</p>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("""
    <div class="feature-card">
        <h3>🗺️ Carte</h3>
        <p>Visualisation géographique des logements du département Rhône-Alpes 69.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-card">
        <h3>📈 Visualisations</h3>
        <p>Graphiques interactifs sur les étiquettes DPE et la consommation.</p>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("""
    <div class="feature-card">
        <h3>🔮 Prédictions</h3>
        <p>Modèles ML pour prédire l’étiquette DPE et la consommation de votre logement.</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")
st.info("✅ Les autres pages du site sont accessibles via la barre latérale à gauche.")
