import streamlit as st
import base64

# ---------------------------
# CONFIG DE LA PAGE
# ---------------------------
st.set_page_config(
    page_title="Contact - Projet DPE - M2 SISE",
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
        content: "🔮 ";
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

    /* ----- CARTES ----- */
    .section-card {
        background: white;
        padding: 25px;
        border-radius: 12px;
        box-shadow: 0px 4px 12px rgba(0,0,0,0.08);
        margin-bottom: 25px;
    }

    /* ----- FOOTER ANIMÉ DANS LA SIDEBAR ----- */
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

# ---------------------------
# FOOTER (logo animé dans la sidebar)
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
    <h1>📬 Contact & équipe projet</h1>
    <p class="subtitle">
        Une question, une suggestion ou un retour sur le site DPE ?<br>
        N'hésitez pas à nous écrire, nous serons ravis d'échanger avec vous.
    </p>
</div>
""", unsafe_allow_html=True)

# ---------------------------
# CONTENU PRINCIPAL
# ---------------------------

col_left, col_right = st.columns([2, 1])

# ---- Colonne gauche : formulaire de contact ----
with col_left:
    st.markdown("""
    <div class="section-card">
        <h2>📝 Formulaire de contact</h2>
        <p style="color:#455a64; font-size:14px;">
            Remplissez les informations ci-dessous pour nous envoyer un message.
        </p>
    </div>
    """, unsafe_allow_html=True)

    with st.form("contact_form"):
        name = st.text_input("Nom / Prénom", placeholder="Ex : Marie Dupont")
        email = st.text_input("Adresse e-mail", placeholder="exemple@domaine.fr")
        subject = st.text_input("Sujet", placeholder="Ex : Retour sur l'outil DPE")
        message = st.text_area("Message", height=180, placeholder="Écrivez votre message ici...")

        col_btn1, col_btn2 = st.columns([1, 1])
        with col_btn1:
            submitted = st.form_submit_button("📨 Envoyer le message")

    if submitted:
        if not name or not email or not message:
            st.warning("Merci de remplir au minimum votre nom, votre e-mail et un message.")
        else:
            st.success("✅ Merci pour votre message !")
            st.info(
                f"Récapitulatif :\n\n"
                f"- **Nom :** {name}\n"
                f"- **E-mail :** {email}\n"
                f"- **Sujet :** {subject if subject else '(aucun)'}"
            )

# ---- Colonne droite : infos de contact / équipe ----
with col_right:
    st.markdown("""
    <div class="section-card">
        <h2>👥 Équipe projet</h2>
        <p style="color:#455a64; font-size:14px;">
            Ce projet a été réalisé dans le cadre du <b>Master 2 SISE</b>, à partir des
            données publiques de l'<b>ADEME</b> sur les diagnostics de performance énergétique (DPE) par l'étudiante <b>HATEM Lamia</b>.
        </p>
    </div>

    <div class="section-card">
        <h3>📧 Coordonnées de contact</h3>
        <p style="color:#455a64; font-size:14px;">
            Vous pouvez également nous joindre à l'adresse suivante :<br>
            <b>greensolutions.dpe@exemple.fr</b><br><br>
        </p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")
st.caption("👣 Merci de votre intérêt pour ce projet et pour la transition énergétique.")
