import streamlit as st
import pandas as pd

st.set_page_config(page_title="Lama Bageri", page_icon="🦙", layout="wide", initial_sidebar_state="collapsed")

# ==========================================
# DESIGN & STIL (CSS)
# ==========================================
st.markdown("""
    <style>
        /* Bakgrund */
        .stApp {
            background-color: #FAF6F0;
            color: #3C2A21;
        }
        .block-container {
            padding-top: 1.0rem !important;
            padding-bottom: 2.0rem !important;
            padding-left: 1.5rem !important;
            padding-right: 1.5rem !important;
            max-width: 98% !important;
        }

        /* Knappar */
        .stButton>button {
            border-radius: 10px !important;
            background-color: #D9826C !important;
            color: #FFFFFF !important;
            border: none !important;
            font-weight: 600 !important;
        }
        .stButton>button:hover {
            background-color: #C86D51 !important;
        }

        /* Styling för Flikar */
        .stTabs [data-baseweb="tab-list"] {
            gap: 8px;
            margin-top: 10px;
        }
        .stTabs [data-baseweb="tab"] {
            border-radius: 8px 8px 0 0;
            padding: 8px 16px;
            background-color: #EFE6DC;
            color: #5C4033;
            font-weight: 600;
        }
        .stTabs [aria-selected="true"] {
            background-color: #D9826C !important;
            color: #FFFFFF !important;
        }

        /* Bild-mixmode för transparent logga */
        div[data-testid="stImage"] img {
            mix-blend-mode: multiply;
            object-fit: contain;
        }

        /* Tabellstyling */
        div[data-testid="stDataObjectViz"] td, div[data-testid="stDataObjectViz"] th {
            padding: 5px 8px !important;
            font-size: 13px !important;
        }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# DEFAULT DATA
# ==========================================
DEFAULT_INGREDIENSER = [
    {"Ingrediens": "Apelsin (st)", "Pris": 6.37, "Enhet": "st", "Kalorier": 40},
    {"Ingrediens": "Bakchoklad mörk (kg)", "Pris": 199.75, "Enhet": "kg", "Kalorier": 5400},
    {"Ingrediens": "Bakpulver (kg)", "Pris": 65.00, "Enhet": "kg", "Kalorier": 0},
    {"Ingrediens": "Bikarbonat (kg)", "Pris": 74.00, "Enhet": "kg", "Kalorier": 0},
    {"Ingrediens": "Blåbär (kg)", "Pris": 79.00, "Enhet": "kg", "Kalorier": 570},
    {"Ingrediens": "Brunsocker (kg)", "Pris": 39.90, "Enhet": "kg", "Kalorier": 3800},
    {"Ingrediens": "Chokladknappar (kg)", "Pris": 216.70, "Enhet": "kg", "Kalorier": 5400},
    {"Ingrediens": "Egg (st)", "Pris": 1.90, "Enhet": "st", "Kalorier": 70},
    {"Ingrediens": "Filmjölk (kg)", "Pris": 22.95, "Enhet": "kg", "Kalorier": 600},
    {"Ingrediens": "Florsocker (kg)", "Pris": 31.90, "Enhet": "kg", "Kalorier": 4000},
    {"Ingrediens": "Färskost (kg)", "Pris": 112.50, "Enhet": "kg", "Kalorier": 2500},
    {"Ingrediens": "Gräddfil (kg)", "Pris": 39.00, "Enhet": "kg", "Kalorier": 1150},
    {"Ingrediens": "Havregryn (kg)", "Pris": 13.30, "Enhet": "kg", "Kalorier": 3700},
    {"Ingrediens": "Honung (kg)", "Pris": 117.00, "Enhet": "kg", "Kalorier": 3000},
    {"Ingrediens": "Ingefära (kg)", "Pris": 615.00, "Enhet": "kg", "Kalorier": 0},
    {"Ingrediens": "Jäst (kg)", "Pris": 303.57, "Enhet": "kg", "Kalorier": 1000},
    {"Ingrediens": "Kaffe (kg)", "Pris": 435.00, "Enhet": "kg", "Kalorier": 0},
    {"Ingrediens": "Kakao (kg)", "Pris": 194.88, "Enhet": "kg", "Kalorier": 3500},
    {"Ingrediens": "Kanel (kg)", "Pris": 587.50, "Enhet": "kg", "Kalorier": 0},
    {"Ingrediens": "Kokosflingor (kg)", "Pris": 114.80, "Enhet": "kg", "Kalorier": 6600},
    {"Ingrediens": "Mandel (kg)", "Pris": 330.00, "Enhet": "kg", "Kalorier": 6000},
    {"Ingrediens": "Mjöl (kg)", "Pris": 7.20, "Enhet": "kg", "Kalorier": 3500},
    {"Ingrediens": "Mjölk (kg)", "Pris": 10.90, "Enhet": "kg", "Kalorier": 450},
    {"Ingrediens": "Morot (kg)", "Pris": 13.95, "Enhet": "kg", "Kalorier": 400},
    {"Ingrediens": "Nejlika (kg)", "Pris": 630.00, "Enhet": "kg", "Kalorier": 0},
    {"Ingrediens": "Olja (kg)", "Pris": 28.24, "Enhet": "kg", "Kalorier": 8800},
    {"Ingrediens": "Rågsikt (kg)", "Pris": 9.45, "Enhet": "kg", "Kalorier": 3400},
    {"Ingrediens": "Salt (kg)", "Pris": 11.50, "Enhet": "kg", "Kalorier": 0},
    {"Ingrediens": "Sesamfrön (kg)", "Pris": 97.33, "Enhet": "kg", "Kalorier": 5700},
    {"Ingrediens": "Smör (kg)", "Pris": 125.90, "Enhet": "kg", "Kalorier": 7200},
    {"Ingrediens": "Socker (kg)", "Pris": 23.95, "Enhet": "kg", "Kalorier": 4000},
    {"Ingrediens": "Vallmofrön (kg)", "Pris": 202.67, "Enhet": "kg", "Kalorier": 5200},
    {"Ingrediens": "Valnötter (kg)", "Pris": 167.38, "Enhet": "kg", "Kalorier": 6500},
    {"Ingrediens": "Vaniljextrakt (kg)", "Pris": 1199.00, "Enhet": "kg", "Kalorier": 0},
    {"Ingrediens": "Vaniljsocker (kg)", "Pris": 115.00, "Enhet": "kg", "Kalorier": 4000},
    {"Ingrediens": "Vispgrädde (kg)", "Pris": 74.00, "Enhet": "kg", "Kalorier": 3500},
    {"Ingrediens": "Yoghurt (kg)", "Pris": 28.50, "Enhet": "kg", "Kalorier": 600}
]

DEFAULT_TOPPINGS = ["Blåbär (kg)", "Chokladknappar (kg)", "Kokosflingor (kg)", "Valnötter (kg)", "Sesamfrön (kg)", "Vallmofrön (kg)"]

DEFAULT_RECEPT = {
    "Muffins": {"override_kostnad": 51.05, "override_kcal": 4650},
    "Biskvier": {"override_kostnad": 96.19, "override_kcal": 3350},
    "Oat cookie": {"override_kostnad": 65.87, "override_kcal": 4100},
    "Brownie": {"override_kostnad": 78.32, "override_kcal": 3850},
    "Cookie": {"override_kostnad": 40.22, "override_kcal": 3200},
    "Bagels": {"override_kostnad": 21.06, "override_kcal": 2850},
    "Morotskaka": {"override_kostnad": 69.86, "override_kcal": 4400},
    "Chokladkaka": {"override_kostnad": 143.69, "override_kcal": 9800},
    "Kanelbullar": {"override_kostnad": 69.26, "override_kcal": 5450},
    "Orange cake": {"override_kostnad": 48.23, "override_kcal": 820},
    "Cinnamon loaf": {"override_kostnad": 45.27, "override_kcal": 820}
}

DEFAULT_ORDERS = {
    "Order 11-morfar": {
        "datum": "2026-06-13",
        "rader": [
            {"Recept": "Muffins", "Topping": "Blåbär (kg)", "Mängd_g": 175, "Satser": 1.0, "Bakade": 21, "Sålda": 18, "Pris_st": 15.0},
            {"Recept": "Biskvier", "Topping": "Ingen", "Mängd_g": 0, "Satser": 1.0, "Bakade": 17, "Sålda": 17, "Pris_st": 20.0},
            {"Recept": "Oat cookie", "Topping": "Chokladknappar (kg)", "Mängd_g": 150, "Satser": 1.0, "Bakade": 24, "Sålda": 24, "Pris_st": 15.0}
        ]
    },
    "Order 7-Eivor": {
        "datum": "2026-04-29/2026-05-15",
        "rader": [
            {"Recept": "Muffins", "Topping": "Blåbär (kg)", "Mängd_g": 175, "Satser": 1.0, "Bakade": 19, "Sålda": 17, "Pris_st": 15.0},
            {"Recept": "Cookie", "Topping": "Chokladknappar (kg)", "Mängd_g": 100, "Satser": 1.0, "Bakade": 27, "Sålda": 25, "Pris_st": 10.0},
            {"Recept": "Kanelbullar", "Topping": "Ingen", "Mängd_g": 0, "Satser": 1.0, "Bakade": 38, "Sålda": 36, "Pris_st": 10.0}
        ]
    }
}

if "ingredienser" not in st.session_state:
    st.session_state.ingredienser = DEFAULT_INGREDIENSER

if "toppings_lista" not in st.session_state:
    st.session_state.toppings_lista = DEFAULT_TOPPINGS

if "recept" not in st.session_state:
    st.session_state.recept = DEFAULT_RECEPT

if "orders_db" not in st.session_state:
    st.session_state.orders_db = DEFAULT_ORDERS

def berakna_recept_totalt(r_namn):
    r_data = st.session_state.recept.get(r_namn, {})
    if "override_kostnad" in r_data and "override_kcal" in r_data:
        return r_data["override_kostnad"], r_data["override_kcal"]
    return 50.0, 4000

# ==========================================
# LOGGA HÖGST UPP (SÄKER INLÄSNING)
# ==========================================
try:
    st.image("Logga.jpg", width=80)
except Exception:
    try:
        st.image("Logga.png", width=80)
    except Exception:
        pass

# ==========================================
# FLIKAR UNDER LOGGAN
# ==========================================
tab1, tab2, tab3, tab4 = st.tabs(["🥦 Ingredienser", "🍓 Toppings", "📖 Recept", "🛒 Orderbyggare"])

# Flik 1: Ingredienser
with tab1:
    st.subheader("🥦 Ingrediensbibliotek")
    col1, _ = st.columns([5, 5])
    with col1:
        st.dataframe(
            pd.DataFrame(st.session_state.ingredienser),
            hide_index=True,
            column_config={
                "Ingrediens": st.column_config.TextColumn("Ingrediens", width="medium"),
                "Pris": st.column_config.NumberColumn("Pris", width="small", format="%.2f kr"),
                "Enhet": st.column_config.TextColumn("Enhet", width="small"),
                "Kalorier": st.column_config.NumberColumn("Kalorier", width="small")
            }
        )

# Flik 2: Toppings
with tab2:
    st.subheader("🍓 Hantera Toppings")
    col2, _ = st.columns([4, 6])
    with col2:
        alla_ingredienser = [i["Ingrediens"] for i in st.session_state.ingredienser if "Ingrediens" in i]
        ny_topping = st.selectbox("Välj ingrediens att lägga till i Toppings-listan:", alla_ingredienser)
        if st.button("➕ Lägg till i Toppings"):
            if ny_topping not in st.session_state.toppings_lista:
                st.session_state.toppings_lista.append(ny_topping)
                st.rerun()
        st.dataframe(
            pd.DataFrame([{"Topping": t} for t in st.session_state.toppings_lista]),
            hide_index=True,
            column_config={"Topping": st.column_config.TextColumn("Topping", width="medium")}
        )

# Flik 3: Recept
with tab3:
    st.subheader("📖 Receptöversikt")
    col3, _ = st.columns([4, 6])
    with col3:
        recept_rader = [{"Recept": r, "Kostnad": f"{berakna_recept_totalt(r)[0]:.2f} kr", "Kalorier": f"{berakna_recept_totalt(r)[1]} kcal"} for r in st.session_state.recept]
        st.dataframe(
            pd.DataFrame(recept_rader),
            hide_index=True,
            column_config={
                "Recept": st.column_config.TextColumn("Recept", width="medium"),
                "Kostnad": st.column_config.TextColumn("Kostnad", width="small"),
                "Kalorier": st.column_config.TextColumn("Kalorier", width="small")
            }
        )

# Flik 4: Orderbyggare
with tab4:
    st.subheader("🛒 Orderbyggare")
    
    valj_order_nycklar = list(st.session_state.orders_db.keys())
    valj_order = st.selectbox("📋 Välj order att granska eller redigera:", valj_order_nycklar)

    nuvarande_order = st.session_state.orders_db[valj_order]
    
    st.markdown(f"### {valj_order}")
    st.caption(f"Datum: {nuvarande_order['datum']}")

    with st.expander("✏️ Redigera orderrader direkt i tabellen", expanded=True):
        df_edit = pd.DataFrame(nuvarande_order["rader"])
        
        edited_df = st.data_editor(
            df_edit,
            num_rows="dynamic",
            use_container_width=True,
            column_config={
                "Recept": st.column_config.SelectboxColumn("Recept", options=list(st.session_state.recept.keys()), required=True),
                "Topping": st.column_config.SelectboxColumn("Topping", options=["Ingen"] + st.session_state.toppings_lista, required=True),
                "Mängd_g": st.column_config.NumberColumn("Mängd (g)", min_value=0, step=10),
                "Satser": st.column_config.NumberColumn("Satser", min_value=0.1, step=0.1, format="%.1f"),
                "Bakade": st.column_config.NumberColumn("Bakade (st)", min_value=1, step=1),
                "Sålda": st.column_config.NumberColumn("Sålda (st)", min_value=0, step=1),
                "Pris_st": st.column_config.NumberColumn("Pris/st (kr)", min_value=0.0, step=0.5, format="%.1f kr")
            },
            key=f"editor_{valj_order}"
        )
        
        nuvarande_order["rader"] = edited_df.to_dict(orient="records")

    ing_map = {i["Ingrediens"]: i for i in st.session_state.ingredienser}
    table_rows = []
    
    tot_bakade = 0
    tot_salda = 0
    tot_kostnad = 0.0
    tot_vinst = 0.0
    tot_pris = 0.0
    tot_kalorier_sats = 0

    for r in nuvarande_order["rader"]:
        rec_k, rec_kcal = berakna_recept_totalt(r.get("Recept", "Muffins"))
        
        top_k = 0.0
        top_kcal = 0
        topping_namn = r.get("Topping", "Ingen")
        mängd_g = r.get("Mängd_g", 0)
        
        if topping_namn != "Ingen" and topping_namn in ing_map:
            t_info = ing_map[topping_namn]
            faktor = mängd_g / 1000.0
            top_k = t_info["Pris"] * faktor
            top_kcal = int(t_info["Kalorier"] * faktor)

        rad_satser = float(r.get("Satser", 1.0))
        rad_bakade = int(r.get("Bakade", 1))
        rad_salda = int(r.get("Sålda", 0))
        rad_pris_st = float(r.get("Pris_st", 0.0))

        rad_tot_kostnad = (rec_k * rad_satser) + top_k
        rad_kostnad_bakad = rad_tot_kostnad / rad_bakade if rad_bakade > 0 else 0
        rad_kostnad_sald = rad_tot_kostnad / rad_salda if rad_salda > 0 else 0
        
        rad_tot_intakt = rad_salda * rad_pris_st
        rad_vinst = rad_tot_intakt - rad_tot_kostnad
        rad_vinstpaslag = (rad_vinst / rad_tot_kostnad * 100) if rad_tot_kostnad > 0 else 0
        
        rad_kalorier_sats = int((rec_kcal * rad_satser) + top_kcal)
        rad_kalorier_st = int(rad_kalorier_sats / rad_bakade) if rad_bakade > 0 else 0

        tot_bakade += rad_bakade
        tot_salda += rad_salda
        tot_kostnad += rad_tot_kostnad
        tot_vinst += rad_vinst
        tot_pris += rad_tot_intakt
        tot_kalorier_sats += rad_kalorier_sats

        table_rows.append({
            "Recept": r.get("Recept", ""),
            "Toppings": topping_namn if topping_namn != "Ingen" else "",
            "Mängd": f"{mängd_g} g" if topping_namn != "Ingen" else "",
            "Topping kr": f"{top_k:.2f} kr" if top_k > 0 else "",
            "Topping kcal": f"{top_kcal} kcal" if top_kcal > 0 else "",
            "Satser": f"{rad_satser:.1f}",
            "Bakade": f"{rad_bakade} st",
            "Sålda": f"{rad_salda} st",
            "Kostnad": f"{round(rad_tot_kostnad)} kr",
            "Kostnad/bakad kaka": f"{rad_kostnad_bakad:.1f} kr",
            "Kostnad/såld kaka": f"{rad_kostnad_sald:.1f} kr",
            "Pris/cookie": f"{int(rad_pris_st)} kr",
            "vinstpåslag": f"{int(rad_vinstpaslag)}%",
            "vinst": f"{int(rad_vinst)} kr",
            "Pris": f"{int(rad_tot_intakt)} kr",
            "Kalorier/sats": f"{rad_kalorier_sats} kcal",
            "Kalorier/st": f"{rad_kalorier_st} kcal"
        })

    tot_vinstpaslag = (tot_vinst / tot_kostnad * 100) if tot_kostnad > 0 else 0
    tot_snitt_bakad = tot_kostnad / tot_bakade if tot_bakade > 0 else 0
    tot_snitt_sald = tot_kostnad / tot_salda if tot_salda > 0 else 0
    tot_snitt_pris = tot_pris / tot_salda if tot_salda > 0 else 0

    table_rows.append({
        "Recept": "Tot",
        "Toppings": "", "Mängd": "", "Topping kr": "", "Topping kcal": "",
        "Satser": "",
        "Bakade": f"{tot_bakade} st",
        "Sålda": f"{tot_salda} st",
        "Kostnad": f"{round(tot_kostnad)} kr",
        "Kostnad/bakad kaka": f"{tot_snitt_bakad:.1f} kr",
        "Kostnad/såld kaka": f"{tot_snitt_sald:.1f} kr",
        "Pris/cookie": f"{int(tot_snitt_pris)} kr",
        "vinstpåslag": f"{int(tot_vinstpaslag)}%",
        "vinst": f"{int(tot_vinst)} kr",
        "Pris": f"{int(tot_pris)} kr",
        "Kalorier/sats": f"{tot_kalorier_sats} kcal",
        "Kalorier/st": ""
    })

    df_display = pd.DataFrame(table_rows)

    def fargkoda_kolumner(df):
        styles = pd.DataFrame('', index=df.index, columns=df.columns)
        
        farger = {
            "grå": "background-color: #E2E8F0; color: #1E293B;",
            "gul": "background-color: #FEF9C3; color: #713F12;",
            "vit": "background-color: #FFFFFF; color: #0F172A;",
            "rosa": "background-color: #FCE7F3; color: #831843;",
            "grön": "background-color: #DCFCE7; color: #14532D;",
            "blå": "background-color: #DBEAFE; color: #1E3A8A;",
            "beige": "background-color: #FEF3C7; color: #78350F;",
            "tot_rad": "background-color: #475569; color: #FFFFFF; font-weight: bold;"
        }

        styles["Recept"] = farger["grå"]
        styles["Toppings"] = farger["gul"]
        styles["Mängd"] = farger["gul"]
        styles["Topping kr"] = farger["gul"]
        styles["Topping kcal"] = farger["gul"]
        styles["Satser"] = farger["vit"]
        styles["Bakade"] = farger["rosa"]
        styles["Sålda"] = farger["rosa"]
        styles["Kostnad"] = farger["grön"]
        styles["Kostnad/bakad kaka"] = farger["grön"]
        styles["Kostnad/såld kaka"] = farger["grön"]
        styles["Pris/cookie"] = farger["blå"]
        styles["vinstpåslag"] = farger["blå"]
        styles["vinst"] = farger["blå"]
        styles["Pris"] = farger["blå"]
        styles["Kalorier/sats"] = farger["beige"]
        styles["Kalorier/st"] = farger["beige"]

        tot_idx = df[df["Recept"] == "Tot"].index
        for idx in tot_idx:
            styles.loc[idx] = farger["tot_rad"]

        return styles

    styled_df = df_display.style.apply(fargkoda_kolumner, axis=None)

    st.markdown("#### 📊 Sammanställning & Kalkyl")
    st.dataframe(styled_df, hide_index=True, use_container_width=True)
