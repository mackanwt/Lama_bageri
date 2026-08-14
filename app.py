import streamlit as st
import pandas as pd

st.set_page_config(page_title="Bagerikalkylatorn", page_icon="🦙", layout="wide", initial_sidebar_state="collapsed")

# ==========================================
# OUTLINE LAMA-LOGOTYP (MED KOCKHATT & KAVEL)
# ==========================================
LLAMA_SVG = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200" width="70" height="70" style="vertical-align: middle;">
  <!-- Kavel undertill -->
  <g stroke="#2c2c2c" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round">
    <rect x="35" y="162" width="130" height="16" rx="6" fill="#e5bf92"/>
    <rect x="15" y="166" width="20" height="8" rx="3" fill="#b38150"/>
    <rect x="165" y="166" width="20" height="8" rx="3" fill="#b38150"/>
  </g>
  <!-- Öron -->
  <g stroke="#2c2c2c" stroke-width="3.5" stroke-linejoin="round">
    <path d="M 52,58 C 30,30 50,10 62,38 Z" fill="#ffffff"/>
    <path d="M 148,58 C 170,30 150,10 138,38 Z" fill="#ffffff"/>
    <path d="M 54,52 C 40,34 52,22 60,38 Z" fill="#f4c2c2"/>
    <path d="M 146,52 C 160,34 148,22 140,38 Z" fill="#f4c2c2"/>
  </g>
  <!-- Luddig Huvudform -->
  <path d="M 60,65 C 40,65 35,90 40,110 C 45,130 55,148 100,148 C 145,148 155,130 160,110 C 165,90 160,65 140,65 C 135,65 130,55 120,55 C 110,55 105,62 100,62 C 95,62 90,55 80,55 C 70,55 65,65 60,65 Z" fill="#ffffff" stroke="#2c2c2c" stroke-width="4" stroke-linejoin="round"/>
  <!-- Mulle / Nosparti -->
  <ellipse cx="100" cy="115" rx="22" ry="16" fill="#fdf0ed" stroke="#2c2c2c" stroke-width="3"/>
  <path d="M 90,108 Q 100,102 110,108 Q 100,118 90,108 Z" fill="#f4c2c2" stroke="#2c2c2c" stroke-width="2.5"/>
  <path d="M 100,114 L 100,122 M 94,122 Q 100,126 106,122" stroke="#2c2c2c" stroke-width="2.5" fill="none" stroke-linecap="round"/>
  <!-- Ögon -->
  <g>
    <circle cx="72" cy="92" r="10" fill="#2c2c2c"/>
    <circle cx="128" cy="92" r="10" fill="#2c2c2c"/>
    <circle cx="69" cy="88" r="4" fill="#ffffff"/>
    <circle cx="125" cy="88" r="4" fill="#ffffff"/>
    <circle cx="74" cy="95" r="2" fill="#ffffff"/>
    <circle cx="130" cy="95" r="2" fill="#ffffff"/>
    <!-- Ögonfransar -->
    <path d="M 62,86 Q 56,80 54,84 M 64,82 Q 60,74 60,80" stroke="#2c2c2c" stroke-width="3" stroke-linecap="round"/>
    <path d="M 138,86 Q 144,80 146,84 M 136,82 Q 140,74 140,80" stroke="#2c2c2c" stroke-width="3" stroke-linecap="round"/>
  </g>
  <!-- Kinder -->
  <ellipse cx="60" cy="110" rx="8" ry="5" fill="#f8b195" opacity="0.85"/>
  <ellipse cx="140" cy="110" rx="8" ry="5" fill="#f8b195" opacity="0.85"/>
  <!-- Solid Kockhatt -->
  <g stroke="#2c2c2c" stroke-width="3.5" stroke-linejoin="round">
    <path d="M 68,40 C 50,15 80,0 100,8 C 120,0 150,15 132,40 Z" fill="#ffffff"/>
    <rect x="66" y="36" width="68" height="16" rx="4" fill="#ffffff"/>
  </g>
</svg>"""

st.markdown("""
    <style>
        div[data-testid="stDataObjectViz"] td, div[data-testid="stDataObjectViz"] th {
            padding: 3px 10px !important;
            font-size: 14px !important;
        }
        .block-container {
            padding-top: 1.2rem !important;
            padding-bottom: 1.2rem !important;
            max-width: 950px !important;
        }
    </style>
""", unsafe_allow_html=True)

# Sidhuvud
col_logo, col_title = st.columns([1, 7])
with col_logo:
    st.markdown(LLAMA_SVG, unsafe_allow_html=True)
with col_title:
    st.title("Bagerikalkylatorn")

# ==========================================
# 1. INGREDIENSER OCH EXAKTA RECEPT FRÅN KALKYLARKET
# ==========================================
DEFAULT_INGREDIENSER = [
    {"Ingrediens": "Apelsin (st)", "Pris": 6.37, "Enhet": "st", "Kalorier": 50},
    {"Ingrediens": "Bakchoklad ljus (kg)", "Pris": 199.75, "Enhet": "kg", "Kalorier": 5500},
    {"Ingrediens": "Bakchoklad mörk (kg)", "Pris": 199.75, "Enhet": "kg", "Kalorier": 5500},
    {"Ingrediens": "Bakchoklad vit (kg)", "Pris": 199.75, "Enhet": "kg", "Kalorier": 5500},
    {"Ingrediens": "Bakpulver (kg)", "Pris": 66.44, "Enhet": "kg", "Kalorier": 100},
    {"Ingrediens": "Bikarbonat (kg)", "Pris": 74.45, "Enhet": "kg", "Kalorier": 100},
    {"Ingrediens": "Blåbär (kg)", "Pris": 79.00, "Enhet": "kg", "Kalorier": 570},
    {"Ingrediens": "Brunsocker (kg)", "Pris": 39.90, "Enhet": "kg", "Kalorier": 4000},
    {"Ingrediens": "Chokladknappar (kg)", "Pris": 216.67, "Enhet": "kg", "Kalorier": 5400},
    {"Ingrediens": "Egg (st)", "Pris": 1.90, "Enhet": "st", "Kalorier": 75},
    {"Ingrediens": "Filmjölk (kg)", "Pris": 22.95, "Enhet": "kg", "Kalorier": 600},
    {"Ingrediens": "Florsocker (kg)", "Pris": 31.90, "Enhet": "kg", "Kalorier": 4000},
    {"Ingrediens": "Färskost (kg)", "Pris": 112.50, "Enhet": "kg", "Kalorier": 3400},
    {"Ingrediens": "Gräddfil (kg)", "Pris": 39.00, "Enhet": "kg", "Kalorier": 1200},
    {"Ingrediens": "Havregryn (kg)", "Pris": 13.30, "Enhet": "kg", "Kalorier": 3700},
    {"Ingrediens": "Honung (kg)", "Pris": 117.00, "Enhet": "kg", "Kalorier": 3000},
    {"Ingrediens": "Ingefära (kg)", "Pris": 615.00, "Enhet": "kg", "Kalorier": 3300},
    {"Ingrediens": "Jordgubbar (kg)", "Pris": 31.95, "Enhet": "kg", "Kalorier": 330},
    {"Ingrediens": "Jäst (kg)", "Pris": 303.57, "Enhet": "kg", "Kalorier": 1100},
    {"Ingrediens": "Kaffe (kg)", "Pris": 435.00, "Enhet": "kg", "Kalorier": 0},
    {"Ingrediens": "Kakao (kg)", "Pris": 194.88, "Enhet": "kg", "Kalorier": 4000},
    {"Ingrediens": "Kanel (kg)", "Pris": 587.50, "Enhet": "kg", "Kalorier": 3300},
    {"Ingrediens": "Kardemumma (kg)", "Pris": 924.24, "Enhet": "kg", "Kalorier": 3300},
    {"Ingrediens": "Kokosflingor (kg)", "Pris": 114.75, "Enhet": "kg", "Kalorier": 6600},
    {"Ingrediens": "Mandel (kg)", "Pris": 330.00, "Enhet": "kg", "Kalorier": 6500},
    {"Ingrediens": "Mjöl (kg)", "Pris": 7.19, "Enhet": "kg", "Kalorier": 3500},
    {"Ingrediens": "Mjölk (kg)", "Pris": 10.90, "Enhet": "kg", "Kalorier": 450},
    {"Ingrediens": "Morot (kg)", "Pris": 13.95, "Enhet": "kg", "Kalorier": 400},
    {"Ingrediens": "Nejlika (kg)", "Pris": 630.00, "Enhet": "kg", "Kalorier": 3300},
    {"Ingrediens": "Olja (kg)", "Pris": 28.24, "Enhet": "kg", "Kalorier": 8800},
    {"Ingrediens": "Rågsikt (kg)", "Pris": 9.45, "Enhet": "kg", "Kalorier": 3400},
    {"Ingrediens": "Salt (kg)", "Pris": 11.50, "Enhet": "kg", "Kalorier": 0},
    {"Ingrediens": "Sesamfrön (kg)", "Pris": 97.33, "Enhet": "kg", "Kalorier": 5700},
    {"Ingrediens": "Smör (kg)", "Pris": 125.90, "Enhet": "kg", "Kalorier": 7200},
    {"Ingrediens": "Socker (kg)", "Pris": 23.95, "Enhet": "kg", "Kalorier": 4000},
    {"Ingrediens": "Vallmofrön (kg)", "Pris": 202.67, "Enhet": "kg", "Kalorier": 5200},
    {"Ingrediens": "Valnötter (kg)", "Pris": 167.38, "Enhet": "kg", "Kalorier": 6500},
    {"Ingrediens": "Vaniljextrakt (kg)", "Pris": 1199.00, "Enhet": "kg", "Kalorier": 3000},
    {"Ingrediens": "Vaniljsocker (kg)", "Pris": 115.00, "Enhet": "kg", "Kalorier": 3900},
    {"Ingrediens": "Vispgrädde (kg)", "Pris": 74.00, "Enhet": "kg", "Kalorier": 3500},
    {"Ingrediens": "Yoghurt (kg)", "Pris": 28.50, "Enhet": "kg", "Kalorier": 600}
]

DEFAULT_RECEPT = {
    "Brownie": {
        "ingredienser": [
            {"Ingrediens": "Smör (kg)", "Mängd": 0.170},
            {"Ingrediens": "Brunsocker (kg)", "Mängd": 0.350},
            {"Ingrediens": "Egg (st)", "Mängd": 1},
            {"Ingrediens": "Vaniljextrakt (kg)", "Mängd": 0.005},
            {"Ingrediens": "Mjöl (kg)", "Mängd": 0.094},
            {"Ingrediens": "Kakao (kg)", "Mängd": 0.065},
            {"Ingrediens": "Salt (kg)", "Mängd": 0.004},
            {"Ingrediens": "Chokladknappar (kg)", "Mängd": 0.100}
        ]
    },
    "Cookie": {
        "ingredienser": [
            {"Ingrediens": "Smör (kg)", "Mängd": 0.180},
            {"Ingrediens": "Socker (kg)", "Mängd": 0.160},
            {"Ingrediens": "Brunsocker (kg)", "Mängd": 0.050},
            {"Ingrediens": "Egg (st)", "Mängd": 2},
            {"Ingrediens": "Vaniljextrakt (kg)", "Mängd": 0.005},
            {"Ingrediens": "Mjöl (kg)", "Mängd": 0.210},
            {"Ingrediens": "Bakpulver (kg)", "Mängd": 0.002},
            {"Ingrediens": "Bikarbonat (kg)", "Mängd": 0.004}
        ]
    },
    "Muffins": {
        "ingredienser": [
            {"Ingrediens": "Smör (kg)", "Mängd": 0.110},
            {"Ingrediens": "Socker (kg)", "Mängd": 0.300},
            {"Ingrediens": "Filmjölk (kg)", "Mängd": 0.240},
            {"Ingrediens": "Egg (st)", "Mängd": 2},
            {"Ingrediens": "Vaniljextrakt (kg)", "Mängd": 0.010},
            {"Ingrediens": "Mjöl (kg)", "Mängd": 0.360},
            {"Ingrediens": "Bakpulver (kg)", "Mängd": 0.010},
            {"Ingrediens": "Bikarbonat (kg)", "Mängd": 0.005},
            {"Ingrediens": "Olja (kg)", "Mängd": 0.070},
            {"Ingrediens": "Gräddfil (kg)", "Mängd": 0.080}
        ]
    },
    "Oat cookie": {
        "ingredienser": [
            {"Ingrediens": "Smör (kg)", "Mängd": 0.285},
            {"Ingrediens": "Brunsocker (kg)", "Mängd": 0.220},
            {"Ingrediens": "Egg (st)", "Mängd": 2},
            {"Ingrediens": "Vaniljextrakt (kg)", "Mängd": 0.010},
            {"Ingrediens": "Mjöl (kg)", "Mängd": 0.240},
            {"Ingrediens": "Bakpulver (kg)", "Mängd": 0.005},
            {"Ingrediens": "Bikarbonat (kg)", "Mängd": 0.005},
            {"Ingrediens": "Havregryn (kg)", "Mängd": 0.225}
        ]
    },
    "Bagels": {
        "ingredienser": [
            {"Ingrediens": "Mjöl (kg)", "Mängd": 0.550},
            {"Ingrediens": "Rågsikt (kg)", "Mängd": 0.165},
            {"Ingrediens": "Salt (kg)", "Mängd": 0.018},
            {"Ingrediens": "Olja (kg)", "Mängd": 0.028},
            {"Ingrediens": "Honung (kg)", "Mängd": 0.021},
            {"Ingrediens": "Sesamfrön (kg)", "Mängd": 0.015},
            {"Ingrediens": "Vallmofrön (kg)", "Mängd": 0.015},
            {"Ingrediens": "Jäst (kg)", "Mängd": 0.025}
        ]
    },
    "Morotskaka": {
        "ingredienser": [
            {"Ingrediens": "Smör (kg)", "Mängd": 0.115},
            {"Ingrediens": "Socker (kg)", "Mängd": 0.100},
            {"Ingrediens": "Brunsocker (kg)", "Mängd": 0.167},
            {"Ingrediens": "Egg (st)", "Mängd": 3},
            {"Ingrediens": "Vaniljextrakt (kg)", "Mängd": 0.008},
            {"Ingrediens": "Mjöl (kg)", "Mängd": 0.300},
            {"Ingrediens": "Bakpulver (kg)", "Mängd": 0.002},
            {"Ingrediens": "Bikarbonat (kg)", "Mängd": 0.005},
            {"Ingrediens": "Florsocker (kg)", "Mängd": 0.120},
            {"Ingrediens": "Salt (kg)", "Mängd": 0.003},
            {"Ingrediens": "Kanel (kg)", "Mängd": 0.006},
            {"Ingrediens": "Ingefära (kg)", "Mängd": 0.002},
            {"Ingrediens": "Nejlika (kg)", "Mängd": 0.001},
            {"Ingrediens": "Yoghurt (kg)", "Mängd": 0.080},
            {"Ingrediens": "Färskost (kg)", "Mängd": 0.120},
            {"Ingrediens": "Morot (kg)", "Mängd": 0.240}
        ]
    },
    "Biskvier": {
        "ingredienser": [
            {"Ingrediens": "Smör (kg)", "Mängd": 0.125},
            {"Ingrediens": "Socker (kg)", "Mängd": 0.085},
            {"Ingrediens": "Florsocker (kg)", "Mängd": 0.090},
            {"Ingrediens": "Egg (st)", "Mängd": 1},
            {"Ingrediens": "Vaniljsocker (kg)", "Mängd": 0.006},
            {"Ingrediens": "Bakchoklad mörk (kg)", "Mängd": 0.200},
            {"Ingrediens": "Mandel (kg)", "Mängd": 0.100}
        ]
    },
    "Chokladkaka": {
        "ingredienser": [
            {"Ingrediens": "Smör (kg)", "Mängd": 0.338},
            {"Ingrediens": "Socker (kg)", "Mängd": 0.815},
            {"Ingrediens": "Florsocker (kg)", "Mängd": 0.875},
            {"Ingrediens": "Egg (st)", "Mängd": 3},
            {"Ingrediens": "Vaniljextrakt (kg)", "Mängd": 0.008},
            {"Ingrediens": "Bakpulver (kg)", "Mängd": 0.006},
            {"Ingrediens": "Bikarbonat (kg)", "Mängd": 0.018},
            {"Ingrediens": "Kakao (kg)", "Mängd": 0.050},
            {"Ingrediens": "Yoghurt (kg)", "Mängd": 0.128},
            {"Ingrediens": "Vispgrädde (kg)", "Mängd": 0.140},
            {"Ingrediens": "Filmjölk (kg)", "Mängd": 0.240},
            {"Ingrediens": "Olja (kg)", "Mängd": 0.170},
            {"Ingrediens": "Kaffe (kg)", "Mängd": 0.006}
        ]
    },
    "Kanelbullar": {
        "ingredienser": [
            {"Ingrediens": "Smör (kg)", "Mängd": 0.300},
            {"Ingrediens": "Mjöl (kg)", "Mängd": 0.750},
            {"Ingrediens": "Socker (kg)", "Mängd": 0.228},
            {"Ingrediens": "Mjölk (kg)", "Mängd": 0.500},
            {"Ingrediens": "Jäst (kg)", "Mängd": 0.014},
            {"Ingrediens": "Salt (kg)", "Mängd": 0.004},
            {"Ingrediens": "Kanel (kg)", "Mängd": 0.008},
            {"Ingrediens": "Egg (st)", "Mängd": 1}
        ]
    },
    "Crumble toppings": {
        "ingredienser": [
            {"Ingrediens": "Smör (kg)", "Mängd": 0.055},
            {"Ingrediens": "Mjöl (kg)", "Mängd": 0.080},
            {"Ingrediens": "Brunsocker (kg)", "Mängd": 0.060},
            {"Ingrediens": "Socker (kg)", "Mängd": 0.015}
        ]
    },
    "Orange cake": {
        "ingredienser": [
            {"Ingrediens": "Apelsin (st)", "Mängd": 2},
            {"Ingrediens": "Mjöl (kg)", "Mängd": 0.220},
            {"Ingrediens": "Egg (st)", "Mängd": 3},
            {"Ingrediens": "Socker (kg)", "Mängd": 0.200},
            {"Ingrediens": "Bakpulver (kg)", "Mängd": 0.008},
            {"Ingrediens": "Florsocker (kg)", "Mängd": 0.150},
            {"Ingrediens": "Vaniljextrakt (kg)", "Mängd": 0.010},
            {"Ingrediens": "Filmjölk (kg)", "Mängd": 0.120},
            {"Ingrediens": "Olja (kg)", "Mängd": 0.120}
        ]
    },
    "Cinnamon loaf": {
        "ingredienser": [
            {"Ingrediens": "Smör (kg)", "Mängd": 0.145},
            {"Ingrediens": "Mjöl (kg)", "Mängd": 0.345},
            {"Ingrediens": "Egg (st)", "Mängd": 2},
            {"Ingrediens": "Socker (kg)", "Mängd": 0.200},
            {"Ingrediens": "Bakpulver (kg)", "Mängd": 0.005},
            {"Ingrediens": "Bikarbonat (kg)", "Mängd": 0.003},
            {"Ingrediens": "Vaniljsocker (kg)", "Mängd": 0.005},
            {"Ingrediens": "Gräddfil (kg)", "Mängd": 0.200},
            {"Ingrediens": "Olja (kg)", "Mängd": 0.018},
            {"Ingrediens": "Kanel (kg)", "Mängd": 0.007},
            {"Ingrediens": "Brunsocker (kg)", "Mängd": 0.060}
        ]
    }
}

if "ingredienser" not in st.session_state:
    st.session_state.ingredienser = DEFAULT_INGREDIENSER

if "recept" not in st.session_state:
    st.session_state.recept = DEFAULT_RECEPT

if "order_rader" not in st.session_state:
    st.session_state.order_rader = []

if "edit_mode_ing" not in st.session_state:
    st.session_state.edit_mode_ing = False

def berakna_recept_totalt(recept_data, ingrediens_lista):
    """Beräknar totalkostnad och totala kalorier dynamiskt utifrån råvaror."""
    ing_map = {item["Ingrediens"]: item for item in ingrediens_lista if "Ingrediens" in item}
    tot_kostnad = 0.0
    tot_kcal = 0.0
    for r_ing in recept_data.get("ingredienser", []):
        namn = r_ing.get("Ingrediens")
        mangd = float(r_ing.get("Mängd", 0.0))
        if namn in ing_map:
            pris = float(ing_map[namn].get("Pris", 0.0))
            kcal = float(ing_map[namn].get("Kalorier", 0.0))
            tot_kostnad += pris * mangd
            tot_kcal += kcal * mangd
    return round(tot_kostnad, 2), int(tot_kcal)

tab1, tab2, tab3 = st.tabs(["🥦 Ingredienser", "📖 Recept", "🛒 Orderbyggare"])

# ==========================================
# FLIK 1: INGREDIENSBIBLIOTEK
# ==========================================
with tab1:
    col_head, col_btn = st.columns([3, 1])
    with col_head:
        st.subheader("🥦 Ingrediensbibliotek")
    with col_btn:
        if st.session_state.edit_mode_ing:
            if st.button("💾 Spara & Lås", type="primary", use_container_width=True):
                st.session_state.edit_mode_ing = False
                st.rerun()
        else:
            if st.button("✏️ Aktivera Redigering", use_container_width=True):
                st.session_state.edit_mode_ing = True
                st.rerun()

    with st.expander("➕ Lägg till ny ingrediens"):
        i_namn = st.text_input("Ingrediensnamn")
        col_p1, col_p2, col_p3 = st.columns(3)
        i_pris = col_p1.number_input("Pris (kr)", min_value=0.0, step=1.0)
        i_enhet = col_p2.selectbox("Enhet", ["kg", "st", "liter", "g"])
        i_kcal = col_p3.number_input("Kalorier per enhet", min_value=0, step=10)
        
        if st.button("💾 Spara Ingrediens"):
            if i_namn:
                st.session_state.ingredienser.append({
                    "Ingrediens": i_namn,
                    "Pris": i_pris,
                    "Enhet": i_enhet,
                    "Kalorier": i_kcal
                })
                st.success(f"Lade till {i_namn}!")
                st.rerun()

    df_ing = pd.DataFrame(st.session_state.ingredienser)
    ing_config = {
        "Ingrediens": st.column_config.TextColumn("Ingrediens", width="medium"),
        "Pris": st.column_config.NumberColumn("Pris (kr)", format="%.2f kr", width="small"),
        "Enhet": st.column_config.TextColumn("Enhet", width="small"),
        "Kalorier": st.column_config.NumberColumn("Kalorier", format="%d kcal", width="small"),
    }

    if st.session_state.edit_mode_ing:
        edited_df = st.data_editor(
            df_ing,
            column_config=ing_config,
            use_container_width=False,
            hide_index=True,
            num_rows="dynamic",
            key="ing_editor"
        )
        st.session_state.ingredienser = edited_df.to_dict(orient="records")
    else:
        st.dataframe(df_ing, column_config=ing_config, use_container_width=False, hide_index=True)

# ==========================================
# FLIK 2: RECEPT (MED KALORIKOLUMN I REDIGERING)
# ==========================================
with tab2:
    st.subheader("📖 Receptöversikt")
    
    # 3 rena kolumner
    recept_rader = []
    for r_namn, r_data in st.session_state.recept.items():
        kostnad, kcal = berakna_recept_totalt(r_data, st.session_state.ingredienser)
        recept_rader.append({
            "Recept": r_namn,
            "Kostnad per recept": f"{kostnad:.2f} kr",
            "Totala kalorier": f"{kcal} kcal"
        })
    
    df_recept_view = pd.DataFrame(recept_rader)
    st.dataframe(
        df_recept_view,
        column_config={
            "Recept": st.column_config.TextColumn("Recept", width="medium"),
            "Kostnad per recept": st.column_config.TextColumn("Kostnad per recept", width="medium"),
            "Totala kalorier": st.column_config.TextColumn("Totala kalorier", width="medium")
        },
        use_container_width=False,
        hide_index=True
    )

    st.markdown("---")
    col_act1, col_act2 = st.columns(2)

    # LÄGG TILL RECEPT
    with col_act1:
        with st.expander("➕ Lägg till recept", expanded=False):
            nytt_namn = st.text_input("Receptnamn", key="nytt_rec_namn")
            all_ing_names = [i["Ingrediens"] for i in st.session_state.ingredienser if "Ingrediens" in i]
            
            st.markdown("**Välj ingredienser:**")
            if "temp_ing" not in st.session_state:
                st.session_state.temp_ing = []

            c1, c2, c3 = st.columns([3, 2, 1])
            sel_ing = c1.selectbox("Ingrediens", all_ing_names, key="add_rec_ing_sel")
            sel_mangd = c2.number_input("Mängd (st / kg)", min_value=0.001, value=0.100, step=0.050, key="add_rec_mangd")
            
            if c3.button("➕ Rad"):
                st.session_state.temp_ing.append({"Ingrediens": sel_ing, "Mängd": sel_mangd})

            if st.session_state.temp_ing:
                st.dataframe(pd.DataFrame(st.session_state.temp_ing), hide_index=True, use_container_width=True)
                calc_k, calc_kcal = berakna_recept_totalt({"ingredienser": st.session_state.temp_ing}, st.session_state.ingredienser)
                st.caption(f"Beräknat: **{calc_k:.2f} kr** | **{calc_kcal} kcal**")

            if st.button("💾 Spara Recept", type="primary"):
                if nytt_namn and st.session_state.temp_ing:
                    st.session_state.recept[nytt_namn] = {
                        "ingredienser": st.session_state.temp_ing
                    }
                    st.session_state.temp_ing = []
                    st.success(f"Receptet '{nytt_namn}' har sparats!")
                    st.rerun()

    # REDIGERA RECEPT
    with col_act2:
        with st.expander("✏️ Redigera recept", expanded=False):
            recept_lista = list(st.session_state.recept.keys())
            all_ing_names = [i["Ingrediens"] for i in st.session_state.ingredienser if "Ingrediens" in i]
            ing_map = {item["Ingrediens"]: item for item in st.session_state.ingredienser if "Ingrediens" in item}
            
            if recept_lista:
                edit_target = st.selectbox("Välj recept att redigera", recept_lista)
                rec_obj = st.session_state.recept[edit_target]
                
                raw_ings = rec_obj.get("ingredienser", [])
                
                # Skapa dataram med ingrediens, mängd och beräknade kalorier per rad
                table_rows = []
                for r in raw_ings:
                    i_namn = r.get("Ingrediens")
                    i_mngd = float(r.get("Mängd", 0.0))
                    unit_kcal = float(ing_map.get(i_namn, {}).get("Kalorier", 0))
                    table_rows.append({
                        "Ingrediens": i_namn,
                        "Mängd": i_mngd,
                        "Kalorier": int(unit_kcal * i_mngd)
                    })
                
                current_ings = pd.DataFrame(table_rows)
                if current_ings.empty:
                    current_ings = pd.DataFrame([{"Ingrediens": all_ing_names[0], "Mängd": 0.1, "Kalorier": 0}])

                st.markdown("**Ändra ingredienser i tabellen:**")
                edited_ing_df = st.data_editor(
                    current_ings,
                    column_config={
                        "Ingrediens": st.column_config.SelectboxColumn("Ingrediens", options=all_ing_names, required=True),
                        "Mängd": st.column_config.NumberColumn("Mängd", min_value=0.001, format="%.3f"),
                        "Kalorier": st.column_config.NumberColumn("Kalorier (kcal)", format="%d kcal", disabled=True)
                    },
                    num_rows="dynamic",
                    use_container_width=True,
                    key=f"editor_{edit_target}"
                )

                col_s1, col_s2 = st.columns(2)
                if col_s1.button("💾 Spara Ändringar", type="primary"):
                    updated_records = edited_ing_df.dropna().to_dict(orient="records")
                    saved_ings = [{"Ingrediens": row["Ingrediens"], "Mängd": row["Mängd"]} for row in updated_records]
                    st.session_state.recept[edit_target] = {
                        "ingredienser": saved_ings
                    }
                    st.success(f"Uppdaterade '{edit_target}'!")
                    st.rerun()
                
                if col_s2.button("🗑️ Ta bort recept"):
                    del st.session_state.recept[edit_target]
                    st.rerun()

# ==========================================
# FLIK 3: ORDERBYGGARE
# ==========================================
with tab3:
    st.subheader("🛒 Bygg Order (ex. Order 11-morfar)")
    
    order_namn = st.text_input("Ordernamn / Kund", value="Order 11-morfar")
    
    st.markdown("---")
    st.markdown("#### Lägg till bakverk i ordern")
    
    col_a, col_b = st.columns(2)
    with col_a:
        valgt_recept = st.selectbox("Välj Recept", list(st.session_state.recept.keys()))
        
        ing_namn_lista = ["Ingen"] + [i["Ingrediens"] for i in st.session_state.ingredienser if "Ingrediens" in i]
        valgd_topping = st.selectbox("Topping / Extra Ingrediens", ing_namn_lista)
        
        topping_mangd = 0.0
        topping_enhet = "g"
        if valgd_topping != "Ingen":
            col_t1, col_t2 = st.columns(2)
            topping_mangd = col_t1.number_input("Mängd topping", min_value=0.0, value=175.0, step=5.0)
            topping_enhet = col_t2.selectbox("Enhet för mängd", ["g", "st", "kg"])

    with col_b:
        bakade_st = st.number_input("Bakade (st)", min_value=1, value=18)
        salda_st = st.number_input("Sålda (st)", min_value=1, value=18)
        pris_per_st = st.number_input("Pris / cookie (kr)", min_value=0.0, value=15.0, step=1.0)

    # Räkna ut grundkostnad för receptet
    rec_info = st.session_state.recept[valgt_recept]
    bas_k, bas_kcal = berakna_recept_totalt(rec_info, st.session_state.ingredienser)

    topping_kostnad = 0.0
    topping_kcal = 0
    if valgd_topping != "Ingen":
        ing_info = next((item for item in st.session_state.ingredienser if item.get("Ingrediens") == valgd_topping), None)
        if ing_info:
            faktor = topping_mangd / 1000.0 if topping_enhet == "g" else topping_mangd
            topping_kostnad = float(ing_info.get("Pris", 0)) * faktor
            topping_kcal = float(ing_info.get("Kalorier", 0)) * faktor

    if st.button("➕ Lägg till rad i ordern", type="primary"):
        tot_rad_kostnad = bas_k + topping_kostnad
        tot_rad_pris = salda_st * pris_per_st
        vinst = tot_rad_pris - tot_rad_kostnad
        vinstpaslag = (vinst / tot_rad_kostnad * 100) if tot_rad_kostnad > 0 else 0

        st.session_state.order_rader.append({
            "Recept": valgt_recept,
            "Toppings": f"{valgd_topping} ({topping_mangd}{topping_enhet})" if valgd_topping != "Ingen" else "-",
            "Bakade": bakade_st,
            "Sålda": salda_st,
            "Kostnad": round(tot_rad_kostnad, 2),
            "Kostnad/såld": round(tot_rad_kostnad / salda_st, 2),
            "Pris/st": pris_per_st,
            "Vinstpåslag": f"{round(vinstpaslag)}%",
            "Vinst": round(vinst, 2),
            "Totalt Pris": round(tot_rad_pris, 2),
            "Kalorier/st": int((bas_kcal + topping_kcal) / bakade_st)
        })

    if st.session_state.order_rader:
        st.markdown("---")
        st.markdown(f"### 📋 Översikt: {order_namn}")
        
        df_order = pd.DataFrame(st.session_state.order_rader)
        st.dataframe(df_order, use_container_width=True, hide_index=True)

        tot_kostnad = df_order["Kostnad"].sum()
        tot_pris = df_order["Totalt Pris"].sum()
        tot_vinst = tot_pris - tot_kostnad
        tot_salda = df_order["Sålda"].sum()
        snitt_margin = (tot_vinst / tot_kostnad * 100) if tot_kostnad > 0 else 0

        st.markdown("#### 💰 Totalsumma")
        m1, m2, m3, m4 = st.columns(4)
        m1.metric("Totalt Antal Sålda", f"{tot_salda} st")
        m2.metric("Total Råvarukostnad", f"{tot_kostnad:.2f} kr")
        m3.metric("Total Vinst", f"{tot_vinst:.2f} kr", delta=f"{snitt_margin:.0f}% vinstpåslag")
        m4.metric("Totalt Orderpris", f"{tot_pris:.2f} kr")

        if st.button("🗑️ Rensa Order"):
            st.session_state.order_rader = []
            st.rerun()
