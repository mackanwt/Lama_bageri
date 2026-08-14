import streamlit as st
import pandas as pd

st.set_page_config(page_title="Lama bageri - Kalkylator", page_icon="🦙", layout="wide", initial_sidebar_state="collapsed")

# ==========================================
# LOGOTYP MED TEXTEN "Lama bageri"
# ==========================================
LAMA_BAGERI_LOGO = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 350 90" width="320" height="80">
  <g stroke="#2c2c2c" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
    <rect x="25" y="70" width="50" height="8" rx="3" fill="#e5bf92"/>
    <rect x="15" y="72" width="10" height="4" rx="1.5" fill="#b38150"/>
    <rect x="75" y="72" width="10" height="4" rx="1.5" fill="#b38150"/>
  </g>
  <g stroke="#2c2c2c" stroke-width="2.5" stroke-linejoin="round">
    <path d="M 32,25 C 20,10 30,0 36,15 Z" fill="#ffffff"/>
    <path d="M 68,25 C 80,10 70,0 64,15 Z" fill="#ffffff"/>
    <path d="M 33,22 C 25,12 31,6 35,15 Z" fill="#f4c2c2"/>
    <path d="M 67,22 C 75,12 69,6 65,15 Z" fill="#f4c2c2"/>
  </g>
  <path d="M 35,28 C 25,28 22,40 25,50 C 28,60 33,68 50,68 C 67,68 72,60 75,50 C 78,40 75,28 65,28 Z" fill="#ffffff" stroke="#2c2c2c" stroke-width="2.5"/>
  <ellipse cx="50" cy="52" rx="10" ry="7" fill="#fdf0ed" stroke="#2c2c2c" stroke-width="1.8"/>
  <path d="M 45,49 Q 50,46 55,49 Q 50,54 45,49 Z" fill="#f4c2c2" stroke="#2c2c2c" stroke-width="1.5"/>
  <g>
    <circle cx="38" cy="42" r="4.5" fill="#2c2c2c"/>
    <circle cx="62" cy="42" r="4.5" fill="#2c2c2c"/>
    <circle cx="36.5" cy="40" r="1.8" fill="#ffffff"/>
    <circle cx="60.5" cy="40" r="1.8" fill="#ffffff"/>
  </g>
  <ellipse cx="32" cy="50" rx="3.5" ry="2" fill="#f8b195" opacity="0.85"/>
  <ellipse cx="68" cy="50" rx="3.5" ry="2" fill="#f8b195" opacity="0.85"/>
  <g stroke="#2c2c2c" stroke-width="2" stroke-linejoin="round">
    <path d="M 38,18 C 28,5 45,-3 50,2 C 55,-3 72,5 62,18 Z" fill="#ffffff"/>
    <rect x="37" y="16" width="26" height="8" rx="2" fill="#ffffff"/>
  </g>
  <!-- TEXT: Lama bageri -->
  <text x="95" y="48" font-family="'Segoe UI', Roboto, Helvetica, Arial, sans-serif" font-weight="800" font-size="28" fill="#2c2c2c" letter-spacing="0.5">Lama bageri</text>
  <text x="96" y="66" font-family="'Segoe UI', Roboto, Helvetica, Arial, sans-serif" font-weight="500" font-size="12" fill="#777777" letter-spacing="1.5">RECEPT & KALKYLATION</text>
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
            max-width: 1150px !important;
        }
    </style>
""", unsafe_allow_html=True)

# Sidhuvud
st.markdown(LAMA_BAGERI_LOGO, unsafe_allow_html=True)
st.markdown("---")

# ==========================================
# STANDARDDATA
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
    {"Ingrediens": "Kokosflingor (kg)", "Pris": 114.75, "Enhet": "kg", "Kalorier": 6600},
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
    "Orange cake": {"override_kostnad": 48.23, "override_kcal": 820}
}

if "ingredienser" not in st.session_state:
    st.session_state.ingredienser = DEFAULT_INGREDIENSER

if "toppings_lista" not in st.session_state:
    st.session_state.toppings_lista = DEFAULT_TOPPINGS

if "recept" not in st.session_state:
    st.session_state.recept = DEFAULT_RECEPT

if "order_rader" not in st.session_state:
    # Förinlagda exempelrader från Excel-bilden
    st.session_state.order_rader = [
        {
            "Recept": "Muffins", "Topping": "Blåbär (kg)", "Mängd_g": 175, "Satser": 1, 
            "Bakade": 21, "Sålda": 18, "Pris_st": 15.0
        },
        {
            "Recept": "Biskvier", "Topping": "Ingen", "Mängd_g": 0, "Satser": 1, 
            "Bakade": 17, "Sålda": 17, "Pris_st": 20.0
        },
        {
            "Recept": "Oat cookie", "Topping": "Chokladknappar (kg)", "Mängd_g": 150, "Satser": 1, 
            "Bakade": 24, "Sålda": 24, "Pris_st": 15.0
        }
    ]

def berakna_recept_totalt(r_namn):
    r_data = st.session_state.recept.get(r_namn, {})
    if "override_kostnad" in r_data and "override_kcal" in r_data:
        return r_data["override_kostnad"], r_data["override_kcal"]
    return 50.0, 4000 # Standard fallback om nylagd utan beräkning

# HUVUDFLIKAR
tab1, tab2, tab3, tab4 = st.tabs(["🥦 Ingredienser", "🍓 Toppings", "📖 Recept", "🛒 Orderbyggare"])

# ==========================================
# FLIK 1: INGREDIENSER
# ==========================================
with tab1:
    st.subheader("🥦 Ingrediensbibliotek")
    df_ing = pd.DataFrame(st.session_state.ingredienser)
    st.dataframe(df_ing, hide_index=True, use_container_width=True)

# ==========================================
# FLIK 2: TOPPINGS (NY HUVUDFLIK)
# ==========================================
with tab2:
    st.subheader("🍓 Hantera Toppings")
    st.write("Välj vilka ingredienser från ditt bibliotek som ska finnas tillgängliga som **Toppings** i orderbyggaren.")
    
    alla_ingredienser = [i["Ingrediens"] for i in st.session_state.ingredienser if "Ingrediens" in i]
    
    c_top1, c_top2 = st.columns([2, 1])
    with c_top1:
        ny_topping = st.selectbox("Välj ingrediens att lägga till som topping:", alla_ingredienser)
        if st.button("➕ Lägg till i Toppings-listan"):
            if ny_topping not in st.session_state.toppings_lista:
                st.session_state.toppings_lista.append(ny_topping)
                st.success(f"Lade till {ny_topping}!")
                st.rerun()

    st.markdown("---")
    st.markdown("#### Aktiva Toppings i systemet:")
    
    top_data = []
    ing_map = {i["Ingrediens"]: i for i in st.session_state.ingredienser}
    for t_namn in st.session_state.toppings_lista:
        info = ing_map.get(t_namn, {})
        top_data.append({
            "Topping": t_namn,
            "Pris / enhet": f"{info.get('Pris', 0):.2f} kr",
            "Kalorier / enhet": f"{info.get('Kalorier', 0)} kcal"
        })
    
    df_top = pd.DataFrame(top_data)
    st.dataframe(df_top, hide_index=True, use_container_width=True)

    st.markdown("**Ta bort topping:**")
    top_to_remove = st.selectbox("Välj topping att ta bort:", st.session_state.toppings_lista, key="rm_top_sel")
    if st.button("🗑️ Ta bort markerad topping"):
        st.session_state.toppings_lista.remove(top_to_remove)
        st.rerun()

# ==========================================
# FLIK 3: RECEPT
# ==========================================
with tab3:
    st.subheader("📖 Receptöversikt")
    recept_rader = []
    for r_namn in st.session_state.recept.keys():
        k, kcal = berakna_recept_totalt(r_namn)
        recept_rader.append({"Recept": r_namn, "Kostnad": f"{k:.2f} kr", "Kalorier": f"{kcal} kcal"})
    st.dataframe(pd.DataFrame(recept_rader), hide_index=True, use_container_width=True)

# ==========================================
# FLIK 4: ORDERBYGGARE (MATCHAR BILDEN EXAKT)
# ==========================================
with tab4:
    st.subheader("🛒 Orderbyggare")
    order_titel = st.text_input("Ordernamn", value="Order 11-morfar")
    st.caption("2026-06-13")

    with st.expander("➕ Lägg till rad i ordern", expanded=True):
        col_in1, col_in2, col_in3 = st.columns(3)
        
        with col_in1:
            sel_recept = st.selectbox("Huvudrecept", list(st.session_state.recept.keys()))
            # Endast val från st.session_state.toppings_lista
            valbara_toppings = ["Ingen"] + st.session_state.toppings_lista
            sel_topping = st.selectbox("Topping (från Toppings-listan)", valbara_toppings)
            top_g = st.number_input("Mängd topping (g)", min_value=0, value=175 if sel_topping != "Ingen" else 0, step=25)

        with col_in2:
            num_satser = st.number_input("Satser", min_value=1, value=1)
            num_bakade = st.number_input("Bakade (st)", min_value=1, value=21)
            num_salda = st.number_input("Sålda (st)", min_value=1, value=18)

        with col_in3:
            pris_st = st.number_input("Pris/cookie (kr)", min_value=0.0, value=15.0, step=1.0)

        if st.button("➕ Lägg till rad", type="primary"):
            st.session_state.order_rader.append({
                "Recept": sel_recept,
                "Topping": sel_topping,
                "Mängd_g": top_g if sel_topping != "Ingen" else 0,
                "Satser": num_satser,
                "Bakade": num_bakade,
                "Sålda": num_salda,
                "Pris_st": pris_st
            })
            st.rerun()

    # RÄKNA UT OCH VISA EXCEL-TABELLEN
    if st.session_state.order_rader:
        st.markdown(f"### {order_titel}")
        
        ing_map = {i["Ingrediens"]: i for i in st.session_state.ingredienser}
        
        table_rows = []
        tot_bakade = 0
        tot_salda = 0
        tot_kostnad = 0.0
        tot_vinst = 0.0
        tot_pris = 0.0
        tot_kalorier_sats = 0

        for r in st.session_state.order_rader:
            rec_k, rec_kcal = berakna_recept_totalt(r["Recept"])
            
            # Beräkna Topping
            top_k = 0.0
            top_kcal = 0
            if r["Topping"] != "Ingen" and r["Topping"] in ing_map:
                t_info = ing_map[r["Topping"]]
                faktor = r["Mängd_g"] / 1000.0
                top_k = t_info["Pris"] * faktor
                top_kcal = int(t_info["Kalorier"] * faktor)

            # Radberäkningar
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
            
            rad_kalorier_sats = (rec_kcal * rad_satser) + top_kcal
            rad_kalorier_st = int(rad_kalorier_sats / rad_bakade) if rad_bakade > 0 else 0

            # Summeringar för sista raden
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

        # Totalsumma-rad ("Tot")
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

        df_out = pd.DataFrame(table_rows)
        st.dataframe(df_out, hide_index=True, use_container_width=True)

        if st.button("🗑️ Töm ordern"):
            st.session_state.order_rader = []
            st.rerun()
