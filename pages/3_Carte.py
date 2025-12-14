import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
from pyproj import Transformer
import base64

# ---------------------------
# CONFIG DE LA PAGE
# ---------------------------
st.set_page_config(
    page_title="Carte - Projet DPE - M2 SISE",
    page_icon="assets/logo_green.png",
    layout="wide",
)

# ---------------------------
# STYLE GLOBAL
# ---------------------------
st.markdown("""
<style>

    .main {
        background: #f3f7f4;
    }

    h1, h2, h3 {
        color: #1b5e20;
    }

    [data-testid="stSidebar"] {
        background-color: #0f172a !important;
        padding-top: 30px;
    }

    [data-testid="stSidebar"] * {
        color: #e8f5e9 !important;
    }

    .css-1v0mbdj, .css-17lntkn, .css-1jneuhg {
        background-color: #2e7d32 !important;
        color: white !important;
        border-radius: 10px;
        font-weight: bold;
    }

    .css-1oe5cao:hover, .css-1o6k8w4:hover {
        background-color: rgba(46,125,50,0.2) !important;
        border-radius: 10px;
    }

    [data-testid="stSidebarNav"] li:nth-child(1) a::before {
        content: "🏠";
        font-size: 18px;
        font-weight: bold;
    }

    [data-testid="stSidebarNav"] li:nth-child(2) a::before {
        content: "📚";
    }

    [data-testid="stSidebarNav"] li:nth-child(3) a::before {
        content: "📈";
    }

    [data-testid="stSidebarNav"] li:nth-child(4) a::before {
        content: "🗺️";
    }

    [data-testid="stSidebarNav"] li:nth-child(5) a::before {
        content: "🔮";
    }

    [data-testid="stSidebarNav"] li:nth-child(6) a::before {
        content: "📬 ";
    }

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
    <h1>🗺️ Carte interactive des logements DPE</h1>
    <p class="subtitle">
        La carte ci-dessous affiche un échantillon des <b>logements DPE</b> du département.<br>
        Les coordonnées BAN (Lambert-93) ont été converties en <b>latitude/longitude</b>.
    </p>
</div>
""", unsafe_allow_html=True)

# ---------------------------
# DONNÉES & CARTE
# ---------------------------
@st.cache_data
def load_data():
    df = pd.read_csv("data/dpe_existant.csv")

    COL_X = "Coordonnée_cartographique_X_(BAN)"
    COL_Y = "Coordonnée_cartographique_Y_(BAN)"

    df[COL_X] = pd.to_numeric(df[COL_X], errors="coerce")
    df[COL_Y] = pd.to_numeric(df[COL_Y], errors="coerce")

    df = df.dropna(subset=[COL_X, COL_Y]).copy()

    transformer = Transformer.from_crs("EPSG:2154", "EPSG:4326", always_xy=True)
    lons, lats = transformer.transform(df[COL_X].values, df[COL_Y].values)

    df["longitude"] = lons
    df["latitude"] = lats

    return df

df = load_data()
df_sample = df.head(500)

COL_SURF = "Surface_habitable_logement"
COL_DPE = "Etiquette_DPE"
COL_YEAR = "Année_construction"

center_lat = df_sample["latitude"].mean()
center_lon = df_sample["longitude"].mean()

m = folium.Map(location=[center_lat, center_lon], zoom_start=11)

for _, row in df_sample.iterrows():
    popup = (
        f"Surface : {row.get(COL_SURF, 'NA')} m²<br>"
        f"DPE : {row.get(COL_DPE, 'NA')}<br>"
        f"Année : {row.get(COL_YEAR, 'NA')}"
    )

    folium.CircleMarker(
        location=[row["latitude"], row["longitude"]],
        radius=3,
        popup=popup,
        color="blue",
        fill=True,
        fill_opacity=0.6,
    ).add_to(m)

# ---------------------------
# AFFICHAGE CARTE (CORRIGÉ)
# ---------------------------
st_folium(m, width=1200, height=600, key="map_dpe_lyon")
