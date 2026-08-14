import streamlit as st
import pandas as pd

st.set_page_config(page_title="Lama Bageri", page_icon="🦙", layout="wide", initial_sidebar_state="collapsed")

# ==========================================
# REKONSTRUERAD LOGOTYP SOM MATCHAR LOGGA.JPG EXAKT
# ==========================================
EXAKT_LAMA_LOGO = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 550" width="180" height="200" style="display: block; margin: auto;">
  <g stroke="#3A3F47" stroke-width="7" fill="none" stroke-linecap="round" stroke-linejoin="round">
    <!-- Öron -->
    <path d="M 125,180 C 100,100 130,50 165,100 C 185,130 170,170 155,190" fill="#ffffff"/>
    <path d="M 135,160 C 120,110 138,80 155,110"/>
    
    <!-- Bagarhatt -->
    <path d="M 195,120 C 170,40 280,10 380,40 C 430,70 440,140 375,170 Z" fill="#ffffff"/>
    <path d="M 200,102 C 200,102 330,160 370,190 L 340,230 C 290,190 170,140 170,140 Z" fill="#ffffff"/>
    
    <!-- Blommor på hatt/band -->
    <!-- Blomma vänster hatt -->
    <circle cx="180" cy="45" r="8" fill="#ffffff"/><circle cx="180" cy="30" r="8" fill="#ffffff"/><circle cx="195" cy="40" r="8" fill="#ffffff"/><circle cx="165" cy="40" r="8" fill="#ffffff"/><circle cx="180" cy="40" r="5" fill="#3A3F47"/>
    <!-- Blomma höger hatt -->
    <circle cx="385" cy="75" r="8" fill="#ffffff"/><circle cx="385" cy="60" r="8" fill="#ffffff"/><circle cx="400" cy="70" r="8" fill="#ffffff"/><circle cx="370" cy="70" r="8" fill="#ffffff"/><circle cx="385" cy="70" r="5" fill="#3A3F47"/>
    <!-- Blomma mitt på bandet -->
    <circle cx="290" cy="150" r="10" fill="#ffffff"/><circle cx="290" cy="130" r="10" fill="#ffffff"/><circle cx="310" cy="142" r="10" fill="#ffffff"/><circle cx="270" cy="142" r="10" fill="#ffffff"/><circle cx="290" cy="142" r="6" fill="#3A3F47"/>

    <!-- Huvud/Ull-kontur -->
    <path d="M 155,190 C 130,220 120,260 130,300 C 120,340 140,380 170,400 C 200,420 250,430 300,425 C 350,420 380,390 390,340 C 400,300 390,260 375,230" fill="#ffffff"/>
    
    <!-- Ansikte (Mule och mun) -->
    <ellipse cx="250" cy="270" rx="42" ry="32" fill="#ffffff"/>
    <path d="M 230,250 C 240,235 260,235 270,250 C 275,260 260,275 250,275 C 240,275 225,260 230,250 Z" fill="#ffffff"/>
    <path d="M 250,275 L 250,290 M 230,290 C 240,305 260,305 270,290" fill="#ffffff"/>
    
    <!-- Ögon med fransar och pupiller -->
    <ellipse cx="185" cy="230" rx="20" ry="22" fill="#3A3F47"/>
    <ellipse cx="315" cy="230" rx="20" ry="22" fill="#3A3F47"/>
    <!-- Glans i ögon -->
    <circle cx="178" cy="220" r="7" fill="#ffffff"/>
    <circle cx="190" cy="235" r="3.5" fill="#ffffff"/>
    <circle cx="308" cy="220" r="7" fill="#ffffff"/>
    <circle cx="320" cy="235" r="3.5" fill="#ffffff"/>
    <!-- Ögonfransar -->
    <path d="M 165,218 C 150,210 145,220 150,225 M 168,212 L 160,202 M 175,210 L 172,198"/>
    <path d="M 335,218 C 350,210 355,220 350,225 M 332,212 L 340,202 M 325,210 L 328,198"/>
    
    <!-- Kinder -->
    <ellipse cx="170" cy="268" rx="14" ry="9" fill="#ffffff"/>
    <ellipse cx="330" cy="268" rx="14" ry="9" fill="#ffffff"/>

    <!-- Kropp / Päls -->
    <path d="M 145,340 C 140,420 150,490 200,500 C 250,510 330,510 350,480" fill="#ffffff"/>
    <path d="M 180,420 Q 200,440 220,420 M 280,410 Q 300,430 320,410 M 230,460 Q 250,480 270,460"/>

    <!-- Kavel och Tass -->
    <g transform="rotate(-15 380 340)">
      <rect x="380" y="220" width="30" height="150" rx="8" fill="#ffffff"/>
      <path d="M 395,190 L 395,220 M 395,370 L 395,400" stroke-width="10"/>
      <!-- Tass som håller -->
      <path d="M 350,320 C 330,320 330,360 360,370 C 380,375 400,360 390,330 Z" fill="#ffffff"/>
    </g>

    <!-- Stjärnor och Blommor runt om -->
    <!-- Stjärnor -->
    <path d="M 90,140 L 93,148 L 101,148 L 95,153 L 97,161 L 90,156 L 83,161 L 85,153 L 79,148 L 87,148 Z" fill="#ffffff"/>
    <path d="M 60,238 L 63,246 L 71,246 L 65,251 L 67,259 L 60,254 L 53,259 L 55,251 L 49,246 L 57,246 Z" fill="#ffffff"/>
    <path d="M 115,335 L 118,343 L 126,343 L 120,348 L 122,356 L 115,351 L 108,356 L 110,348 L 104,343 L 112,343 Z" fill="#ffffff"/>
    <!-- Blommor vänster -->
    <circle cx="75" cy="185" r="10" fill="#ffffff"/><circle cx="75" cy="170" r="10" fill="#ffffff"/><circle cx="90" cy="178" r="10" fill="#ffffff"/><circle cx="60" cy="178" r="10" fill="#ffffff"/><circle cx="75" cy="178" r="6" fill="#3A3F47"/>
    <circle cx="85" cy="295" r="10" fill="#ffffff"/><circle cx="85" cy="280" r="10" fill="#ffffff"/><circle cx="100" cy="288" r="10" fill="#ffffff"/><circle cx="70" cy="288" r="10" fill="#ffffff"/><circle cx="85" cy="288" r="6" fill="#3A3F47"/>
  </g>
  
  <!-- TEXT UNDER LOGGAN EXAKT SOM BILDEN -->
  <text x="250" y="535" text-anchor="middle" font-family="'Segoe UI', Roboto, sans-serif" font-weight="700" font-size="46" fill="#3A3F47" letter-spacing="1">Lama Bageri</text>
</svg>"""

st.markdown("""
    <style>
        div[data-testid="stDataObjectViz"] td, div[data-testid="stDataObjectViz"] th {
            padding: 4px 8px !important;
            font-size: 13px !important;
        }
        .block-container {
            padding-top: 1.0rem !important;
            padding-bottom: 1.0rem !important;
            max-width: 1200px !important;
        }
    </style>
""", unsafe_allow_html=True)

# Visar loggan centrerat
st.markdown(EXAKT_LAMA_LOGO, unsafe_allow_html=True)
st.markdown("---")

# ==========================================
# INGREDIENSER, TOPPINGS OCH RECEPTDATA
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
    "Order 7-Eivor": {
        "datum": "2026-04-29/2026-05-15",
        "rader": [
            {"Recept": "Muffins", "Topping": "Blåbär (kg)", "Mängd_g": 175, "Satser": 1, "Bakade": 19, "Sålda": 17, "Pris_st": 15.0},
            {"Recept": "Cookie", "Topping": "Chokladknappar (kg)", "Mängd_g": 100, "Satser": 1, "Bakade": 27, "Sålda": 25, "Pris_st": 10.0},
            {"Recept": "Cookie", "Topping": "Kokosflingor (kg)", "Mängd_g": 100, "Satser": 1, "Bakade": 25, "Sålda": 24, "Pris_st": 10.0},
            {"Recept": "Oat cookie", "Topping": "Chokladknappar (kg)", "Mängd_g": 150, "Satser": 1, "Bakade": 24, "Sålda": 24, "Pris_st": 15.0},
            {"Recept": "Biskvier", "Topping": "Ingen", "Mängd_g": 0, "Satser": 1, "Bakade": 18, "Sålda": 18, "Pris_st": 20.0},
            {"Recept": "Kanelbullar", "Topping": "Ingen", "Mängd_g": 0, "Satser": 1, "Bakade": 38, "Sålda": 36, "Pris_st": 10.0}
        ]
    },
    "Order 8-mamma": {
        "datum": "2026-04-29/2026-05-15",
        "rader": [
            {"Recept": "Muffins", "Topping": "Blåbär (kg)", "Mängd_g": 175, "Satser": 1, "Bakade": 19, "Sålda": 17, "Pris_st": 15.0},
            {"Recept": "Cinnamon loaf", "Topping": "Ingen", "Mängd_g": 0, "Satser": 0.5, "Bakade": 1, "Sålda": 1, "Pris_st": 70.0},
            {"Recept": "Cookie", "Topping": "Chokladknappar (kg)", "Mängd_g": 100, "Satser": 1, "Bakade": 27, "Sålda": 25, "Pris_st": 10.0}
        ]
    },
    "Order 9-Pappa": {
        "datum": "2026-06-02",
        "rader": [
            {"Recept": "Kanelbullar", "Topping": "Ingen", "Mängd_g": 0, "Satser": 1, "Bakade": 34, "Sålda": 25, "Pris_st": 10.0}
        ]
    },
    "Order 10-mamma": {
        "datum": "2026-06-13",
        "rader": [
            {"Recept": "Muffins", "Topping": "Blåbär (kg)", "Mängd_g": 175, "Satser": 1, "Bakade": 21, "Sålda": 18, "Pris_st": 15.0},
            {"Recept": "Biskvier", "Topping": "Ingen", "Mängd_g": 0, "Satser": 1, "Bakade": 18, "Sålda": 17, "Pris_st": 20.0},
            {"Recept": "Orange cake", "Topping": "Ingen", "Mängd_g": 0, "Satser": 1, "Bakade": 1, "Sålda": 1, "Pris_st": 120.0}
        ]
    },
    "Order 11-morfar": {
        "datum": "2026-06-13",
        "rader": [
            {"Recept": "Muffins", "Topping": "Blåbär (kg)", "Mängd_g": 175, "Satser": 1, "Bakade": 21, "Sålda": 18, "Pris_st": 15.0},
            {"Recept": "Biskvier", "Topping": "Ingen", "Mängd_g": 0, "Satser": 1, "Bakade": 17, "Sålda": 17, "Pris_st": 20.0},
            {"Recept": "Oat cookie", "Topping": "Chokladknappar (kg)", "Mängd_g": 150, "Satser": 1, "Bakade": 24, "Sålda": 24, "Pris_st": 15.0}
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

# FLIKAR
tab1, tab2, tab3, tab4 = st.tabs(["🥦 Ingredienser", "🍓 Toppings", "📖 Recept", "🛒 Orderbyggare"])

# ==========================================
# FLIK 1 & 2 & 3: STANDARD
# ==========================================
with tab1:
    st.subheader("🥦 Ingrediensbibliotek")
    st.dataframe(pd.DataFrame(st.session_state.ingredienser), hide_index=True, use_container_width=True)

with tab2:
    st.subheader("🍓 Hantera Toppings")
    alla_ingredienser = [i["Ingrediens"] for i in st.session_state.ingredienser if "Ingrediens" in i]
    ny_topping = st.selectbox("Välj ingrediens att lägga till i Toppings-listan:", alla_ingredienser)
    if st.button("➕ Lägg till i Toppings"):
        if ny_topping not in st.session_state.toppings_lista:
            st.session_state.toppings_lista.append(ny_topping)
            st.rerun()
    st.dataframe(pd.DataFrame([{"Topping": t} for t in st.session_state.toppings_lista]), hide_index=True, use_container_width=True)

with tab3:
    st.subheader("📖 Receptöversikt")
    recept_rader = [{"Recept": r, "Kostnad": f"{berakna_recept_totalt(r)[0]:.2f} kr", "Kalorier": f"{berakna_recept_totalt(r)[1]} kcal"} for r in st.session_state.recept]
    st.dataframe(pd.DataFrame(recept_rader), hide_index=True, use_container_width=True)

# ==========================================
# FLIK 4: ORDERBYGGARE MED ALLA 5 ORDRAR
# ==========================================
with tab4:
    st.subheader("🛒 Orderbyggare")
    
    valj_order_nycklar = list(st.session_state.orders_db.keys())
    valj_order = st.selectbox("📋 Välj order att granska eller redigera:", valj_order_nycklar)

    nuvarande_order = st.session_state.orders_db[valj_order]
    
    st.markdown(f"### {valj_order}")
    st.caption(f"Datum: {nuvarande_order['datum']}")

    # Form för att lägga till ny rad i vald order
    with st.expander("➕ Lägg till rad i denna order", expanded=False):
        c1, c2, c3 = st.columns(3)
        sel_rec = c1.selectbox("Huvudrecept", list(st.session_state.recept.keys()))
        valbara_toppings = ["Ingen"] + st.session_state.toppings_lista
        sel_top = c2.selectbox("Topping", valbara_toppings)
        top_mngd = c3.number_input("Mängd (g)", min_value=0, value=100 if sel_top != "Ingen" else 0)
        
        c4, c5, c6 = st.columns(3)
        sats = c4.number_input("Satser", min_value=0.1, value=1.0, step=0.5)
        bakade = c5.number_input("Bakade (st)", min_value=1, value=20)
        salda = c6.number_input("Sålda (st)", min_value=1, value=20)
        pris = st.number_input("Pris/cookie (kr)", min_value=0.0, value=15.0)

        if st.button("➕ Spara rad i ordern"):
            nuvarande_order["rader"].append({
                "Recept": sel_rec, "Topping": sel_top, "Mängd_g": top_mngd,
                "Satser": sats, "Bakade": bakade, "Sålda": salda, "Pris_st": pris
            })
            st.rerun()

    # GENERERA EXCEL-TABELLEN FÖR VALD ORDER
    ing_map = {i["Ingrediens"]: i for i in st.session_state.ingredienser}
    table_rows = []
    
    tot_bakade = 0
    tot_salda = 0
    tot_kostnad = 0.0
    tot_vinst = 0.0
    tot_pris = 0.0
    tot_kalorier_sats = 0

    for r in nuvarande_order["rader"]:
        rec_k, rec_kcal = berakna_recept_totalt(r["Recept"])
        
        top_k = 0.0
        top_kcal = 0
        if r["Topping"] != "Ingen" and r["Topping"] in ing_map:
            t_info = ing_map[r["Topping"]]
            faktor = r["Mängd_g"] / 1000.0
            top_k = t_info["Pris"] * faktor
            top_kcal = int(t_info["Kalorier"] * faktor)

        rad_satser = r["Satser"]
        rad_bakade = r["Bakade"]
        rad_salda = r["Sålda"]
        rad_pris_st = r["Pris_st"]

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
            "Recept": r["Recept"],
            "Toppings": r["Topping"] if r["Topping"] != "Ingen" else "",
            "Mängd": f"{r['Mängd_g']} g" if r["Topping"] != "Ingen" else "",
            "Topping kr": f"{top_k:.2f} kr" if top_k > 0 else "",
            "Topping kcal": f"{top_kcal} kcal" if top_kcal > 0 else "",
            "Satser": rad_satser,
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

    # Totalsumma (Tot)
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

    st.dataframe(pd.DataFrame(table_rows), hide_index=True, use_container_width=True)
