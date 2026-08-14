import streamlit as st
import pandas as pd

st.set_page_config(page_title="Bagerikalkylatorn", page_icon="🦙", layout="wide", initial_sidebar_state="collapsed")

# ==========================================
# KOMPAKT CSS & TEKNAD LAMA-LOGOTYP (SVG)
# ==========================================
LLAMA_LOGO_SVG = """
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="55" height="55" style="vertical-align: middle; margin-right: 12px;">
  <!-- Kavel bakom/under hakan -->
  <rect x="15" y="74" width="70" height="8" rx="3" fill="#d2b48c" stroke="#8b5a2b" stroke-width="2"/>
  <rect x="5" y="75" width="10" height="6" rx="2" fill="#8b5a2b"/>
  <rect x="85" y="75" width="10" height="6" rx="2" fill="#8b5a2b"/>
  
  <!-- Öron -->
  <ellipse cx="30" cy="38" rx="6" ry="16" fill="#fdfbf7" stroke="#d0c0b0" stroke-width="2" transform="rotate(-15 30 38)"/>
  <ellipse cx="70" cy="38" rx="6" ry="16" fill="#fdfbf7" stroke="#d0c0b0" stroke-width="2" transform="rotate(15 70 38)"/>
  <ellipse cx="30" cy="38" rx="3" ry="10" fill="#f0e6df" transform="rotate(-15 30 38)"/>
  <ellipse cx="70" cy="38" rx="3" ry="10" fill="#f0e6df" transform="rotate(15 70 38)"/>
  
  <!-- Huvud -->
  <path d="M 33,45 C 33,32 67,32 67,45 C 67,65 62,76 50,76 C 38,76 33,65 33,45 Z" fill="#fdfbf7" stroke="#d0c0b0" stroke-width="2"/>
  
  <!-- Mulle / Nos -->
  <ellipse cx="50" cy="62" rx="10" ry="8" fill="#f0e6df" stroke="#d0c0b0" stroke-width="1"/>
  <path d="M 46,59 L 54,59 L 50,63 Z" fill="#8b5a2b"/>
  <path d="M 50,63 L 50,67" stroke="#8b5a2b" stroke-width="1.5"/>
  
  <!-- Ögon -->
  <circle cx="42" cy="50" r="3.5" fill="#2c2c2c"/>
  <circle cx="58" cy="50" r="3.5" fill="#2c2c2c"/>
  <circle cx="43.5" cy="48.5" r="1.2" fill="#ffffff"/>
  <circle cx="59.5" cy="48.5" r="1.2" fill="#ffffff"/>
  
  <!-- Kinder -->
  <ellipse cx="37" cy="56" rx="3.5" ry="2" fill="#ffb6c1" opacity="0.6"/>
  <ellipse cx="63" cy="56" rx="3.5" ry="2" fill="#ffb6c1" opacity="0.6"/>
  
  <!-- Kockhatt -->
  <path d="M 36,32 C 28,18 40,8 50,10 C 60,8 72,18 64,32 Z" fill="#ffffff" stroke="#cccccc" stroke-width="2"/>
  <rect x="35" y="30" width="30" height="8" rx="2" fill="#ffffff" stroke="#cccccc" stroke-width="1.5"/>
</svg>
"""

st.markdown(f"""
    <head>
        <meta name="apple-mobile-web-app-capable" content="yes">
        <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
        <meta name="apple-mobile-web-app-title" content="BageriApp">
        <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    </head>
    <style>
        /* Krymp vaddering och höjd på rader i alla tabeller */
        div[data-testid="stDataObjectViz"] td, div[data-testid="stDataObjectViz"] th {{
            padding: 2px 10px !important;
            font-size: 14px !important;
        }}
        .block-container {{
            padding-top: 1.5rem !important;
            padding-bottom: 1.5rem !important;
            max-width: 1000px !important;
        }}
        .main-header {{
            display: flex;
            align-items: center;
            margin-bottom: 10px;
        }}
    </style>
""", unsafe_allow_html=True)

# Rubrik med den tecknade lamalogo
st.markdown(f"""
    <div class="main-header">
        {LLAMA_LOGO_SVG}
        <h1 style="display: inline; margin: 0; vertical-align: middle;">Bagerikalkylatorn</h1>
    </div>
""", unsafe_allow_html=True)

# ==========================================
# 1. DATA-INITIALISERING
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
    {"Ingrediens": "Jordgubbar (kg)", "Pris": 31.95, "Enhet": "kg", "Kalorier": 330},
    {"Ingrediens": "Jäst (kg)", "Pris": 303.57, "Enhet": "kg", "Kalorier": 1100},
    {"Ingrediens": "Kakao (kg)", "Pris": 194.88, "Enhet": "kg", "Kalorier": 4000},
    {"Ingrediens": "Kanel (kg)", "Pris": 587.50, "Enhet": "kg", "Kalorier": 3300},
    {"Ingrediens": "Kardemumma (kg)", "Pris": 924.24, "Enhet": "kg", "Kalorier": 3300},
    {"Ingrediens": "Kokosflingor (kg)", "Pris": 114.75, "Enhet": "kg", "Kalorier": 6600},
    {"Ingrediens": "Mandel (kg)", "Pris": 330.00, "Enhet": "kg", "Kalorier": 6500},
    {"Ingrediens": "Mjöl (kg)", "Pris": 7.19, "Enhet": "kg", "Kalorier": 3500},
    {"Ingrediens": "Mjölk (kg)", "Pris": 19.50, "Enhet": "kg", "Kalorier": 450},
    {"Ingrediens": "Morot (kg)", "Pris": 13.95, "Enhet": "kg", "Kalorier": 400},
    {"Ingrediens": "Olja (kg)", "Pris": 28.24, "Enhet": "kg", "Kalorier": 8800},
    {"Ingrediens": "Salt (kg)", "Pris": 11.50, "Enhet": "kg", "Kalorier": 0},
    {"Ingrediens": "Smör (kg)", "Pris": 125.90, "Enhet": "kg", "Kalorier": 7200},
    {"Ingrediens": "Socker (kg)", "Pris": 23.95, "Enhet": "kg", "Kalorier": 4000},
    {"Ingrediens": "Valnötter (kg)", "Pris": 167.38, "Enhet": "kg", "Kalorier": 6500},
    {"Ingrediens": "Vaniljextrakt (kg)", "Pris": 1199.00, "Enhet": "kg", "Kalorier": 3000},
    {"Ingrediens": "Vispgrädde (kg)", "Pris": 74.00, "Enhet": "kg", "Kalorier": 3500},
    {"Ingrediens": "Yoghurt (kg)", "Pris": 28.50, "Enhet": "kg", "Kalorier": 600}
]

DEFAULT_RECEPT = {
    "Muffins": {"sats_antal": 22, "bas_kostnad": 51.05, "kcal_sats": 4650},
    "Biskvier": {"sats_antal": 18, "bas_kostnad": 96.19, "kcal_sats": 3350},
    "Oat cookie": {"sats_antal": 20, "bas_kostnad": 65.87, "kcal_sats": 4100},
    "Kanelbullar": {"sats_antal": 40, "bas_kostnad": 69.26, "kcal_sats": 5450},
    "Cookie": {"sats_antal": 21, "bas_kostnad": 40.22, "kcal_sats": 3200},
    "Brownie": {"sats_antal": 9, "bas_kostnad": 78.32, "kcal_sats": 3850},
    "Bagels": {"sats_antal": 12, "bas_kostnad": 21.06, "kcal_sats": 2850},
    "Morotskaka": {"sats_antal": 20, "bas_kostnad": 69.86, "kcal_sats": 4400},
    "Chokladkaka": {"sats_antal": 24, "bas_kostnad": 143.69, "kcal_sats": 9800},
    "Orange cake": {"sats_antal": 1, "bas_kostnad": 48.23, "kcal_sats": 820},
    "Cinnamon loaf": {"sats_antal": 2, "bas_kostnad": 45.27, "kcal_sats": 820}
}

if "ingredienser" not in st.session_state:
    st.session_state.ingredienser = DEFAULT_INGREDIENSER

if "order_rader" not in st.session_state:
    st.session_state.order_rader = []

if "edit_mode_ing" not in st.session_state:
    st.session_state.edit_mode_ing = False

tab1, tab2, tab3 = st.tabs(["🥦 Ingredienser", "📖 Recept", "🛒 Orderbyggare"])

# Kolumnkonfiguration för kompakt visning i Ingrediens-fliken
ing_col_config = {
    "Ingrediens": st.column_config.TextColumn("Ingrediens", width="medium"),
    "Pris": st.column_config.NumberColumn("Pris (kr)", format="%.2f kr", width="small"),
    "Enhet": st.column_config.TextColumn("Enhet", width="small"),
    "Kalorier": st.column_config.NumberColumn("Kalorier", format="%d kcal", width="small"),
}

# ==========================================
# FLIK 1: INGREDIENSBIBLIOTEK
# ==========================================
with tab1:
    col_head, col_btn = st.columns([3, 1])
    with col_head:
        st.subheader("🥦 Ingrediensbibliotek")
    with col_btn:
        if st.session_state.edit_mode_ing:
            if st.button("💾 Spara & Lås tabell", type="primary", use_container_width=True):
                st.session_state.edit_mode_ing = False
                st.rerun()
        else:
            if st.button("✏️ Aktivera Redigering", use_container_width=True):
                st.session_state.edit_mode_ing = True
                st.rerun()

    with st.expander("➕ Lägg till ny ingrediens"):
        i_namn = st.text_input("Ingrediensnamn (t.ex. Pecannötter (kg))")
        col_p1, col_p2, col_p3 = st.columns(3)
        i_pris = col_p1.number_input("Pris (SEK)", min_value=0.0, step=1.0)
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

    if st.session_state.edit_mode_ing:
        st.info("💡 **Redigeringsläge:** Ändra värden direkt i cellerna nedan.")
        edited_df = st.data_editor(
            df_ing,
            column_config=ing_col_config,
            use_container_width=False,
            hide_index=True,
            num_rows="dynamic",
            key="ing_editor"
        )
        st.session_state.ingredienser = edited_df.to_dict(orient="records")
    else:
        st.dataframe(
            df_ing,
            column_config=ing_col_config,
            use_container_width=False,
            hide_index=True
        )

# ==========================================
# FLIK 2: RECEPTÖVERSIKT
# ==========================================
with tab2:
    st.subheader("📖 Basrecept & Kalkyler")
    recept_data = []
    for k, v in DEFAULT_RECEPT.items():
        recept_data.append({
            "Recept": k,
            "Antal/sats": f"{v['sats_antal']} st",
            "Bas Kostnad/sats": f"{v['bas_kostnad']:.2f} kr",
            "Kostnad/st": f"{(v['bas_kostnad'] / v['sats_antal']):.2f} kr",
            "Kalorier/st": f"{int(v['kcal_sats'] / v['sats_antal'])} kcal"
        })
    st.dataframe(
        pd.DataFrame(recept_data),
        use_container_width=False,
        hide_index=True
    )

# ==========================================
# FLIK 3: ORDERBYGGARE (Order 11-morfar stil)
# ==========================================
with tab3:
    st.subheader("🛒 Bygg Order (ex. Order 11-morfar)")
    
    order_namn = st.text_input("Ordernamn / Kund", value="Order 11-morfar")
    
    st.markdown("---")
    st.markdown("#### Lägg till bakverk i ordern")
    
    col_a, col_b = st.columns(2)
    with col_a:
        valgt_recept = st.selectbox("Välj Recept", list(DEFAULT_RECEPT.keys()))
        
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

    topping_kostnad = 0.0
    topping_kcal = 0
    if valgd_topping != "Ingen":
        ing_info = next((item for item in st.session_state.ingredienser if item.get("Ingrediens") == valgd_topping), None)
        if ing_info:
            faktor = topping_mangd / 1000.0 if topping_enhet == "g" else topping_mangd
            topping_kostnad = float(ing_info.get("Pris", 0)) * faktor
            topping_kcal = float(ing_info.get("Kalorier", 0)) * faktor

    if st.button("➕ Lägg till rad i ordern", type="primary"):
        bas_k = DEFAULT_RECEPT[valgt_recept]["bas_kostnad"]
        bas_kcal = DEFAULT_RECEPT[valgt_recept]["kcal_sats"]
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
