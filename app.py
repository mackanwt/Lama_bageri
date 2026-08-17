import streamlit as st
import pandas as pd

# ------------------------------------------
# 1. INITIALISERA SESSION STATE & DATA
# ------------------------------------------

# Ingrediensbibliotek
if "ingredienser" not in st.session_state:
    st.session_state.ingredienser = [
        {"Ingrediens": "Smör (kg)", "Pris": 125.88, "Kalorier": 7170, "Enhet": "kg"},
        {"Ingrediens": "Socker (kg)", "Pris": 23.97, "Kalorier": 4000, "Enhet": "kg"},
        {"Ingrediens": "Brunsocker (kg)", "Pris": 39.91, "Kalorier": 3800, "Enhet": "kg"},
        {"Ingrediens": "Florsocker (kg)", "Pris": 31.90, "Kalorier": 3890, "Enhet": "kg"},
        {"Ingrediens": "Ägg (st)", "Pris": 1.90, "Kalorier": 75, "Enhet": "st"},
        {"Ingrediens": "Vaniljextrakt (kg)", "Pris": 1199.00, "Kalorier": 2880, "Enhet": "kg"},
        {"Ingrediens": "Vaniljsocker (kg)", "Pris": 115.00, "Kalorier": 3900, "Enhet": "kg"},
        {"Ingrediens": "Mjöl (kg)", "Pris": 7.20, "Kalorier": 3400, "Enhet": "kg"},
        {"Ingrediens": "Rågsikt (kg)", "Pris": 9.45, "Kalorier": 3350, "Enhet": "kg"},
        {"Ingrediens": "Bakpulver (kg)", "Pris": 66.00, "Kalorier": 1000, "Enhet": "kg"},
        {"Ingrediens": "Bikarbonat (kg)", "Pris": 74.00, "Kalorier": 0, "Enhet": "kg"},
        {"Ingrediens": "Kakao (kg)", "Pris": 194.80, "Kalorier": 3800, "Enhet": "kg"},
        {"Ingrediens": "Salt (kg)", "Pris": 12.50, "Kalorier": 0, "Enhet": "kg"},
        {"Ingrediens": "Chokladknappar (kg)", "Pris": 216.70, "Kalorier": 5400, "Enhet": "kg"},
        {"Ingrediens": "Filmjölk (kg)", "Pris": 22.96, "Kalorier": 600, "Enhet": "kg"},
        {"Ingrediens": "Gräddfil (kg)", "Pris": 39.00, "Kalorier": 1150, "Enhet": "kg"},
        {"Ingrediens": "Yoghurt (kg)", "Pris": 28.50, "Kalorier": 620, "Enhet": "kg"},
        {"Ingrediens": "Vispgrädde (kg)", "Pris": 74.00, "Kalorier": 3360, "Enhet": "kg"},
        {"Ingrediens": "Färskost (kg)", "Pris": 112.50, "Kalorier": 2350, "Enhet": "kg"},
        {"Ingrediens": "Olja (kg)", "Pris": 28.24, "Kalorier": 8840, "Enhet": "kg"},
        {"Ingrediens": "Havregryn (kg)", "Pris": 13.29, "Kalorier": 3700, "Enhet": "kg"},
        {"Ingrediens": "Honung (kg)", "Pris": 117.14, "Kalorier": 3040, "Enhet": "kg"},
        {"Ingrediens": "Sesamfrön (kg)", "Pris": 97.33, "Kalorier": 5730, "Enhet": "kg"},
        {"Ingrediens": "Vallmofrön (kg)", "Pris": 202.67, "Kalorier": 5250, "Enhet": "kg"},
        {"Ingrediens": "Jäst (kg)", "303.60": 303.60, "Pris": 303.60, "Kalorier": 1050, "Enhet": "kg"},
        {"Ingrediens": "Kanel (kg)", "Pris": 588.33, "Kalorier": 2470, "Enhet": "kg"},
        {"Ingrediens": "Ingefära (kg)", "Pris": 615.00, "Kalorier": 3350, "Enhet": "kg"},
        {"Ingrediens": "Nejlika (kg)", "Pris": 630.00, "Kalorier": 2740, "Enhet": "kg"},
        {"Ingrediens": "Morot (kg)", "Pris": 13.96, "Kalorier": 410, "Enhet": "kg"},
        {"Ingrediens": "Bakchoklad mörk (kg)", "Pris": 199.75, "Kalorier": 5350, "Enhet": "kg"},
        {"Ingrediens": "Mandel (kg)", "Pris": 330.00, "Kalorier": 5790, "Enhet": "kg"},
        {"Ingrediens": "Kaffe (kg)", "Pris": 435.00, "Kalorier": 20, "Enhet": "kg"},
        {"Ingrediens": "Kardemumma (kg)", "Pris": 500.00, "Kalorier": 3000, "Enhet": "kg"},
        {"Ingrediens": "Apelsin ...", "Pris": 6.37, "Kalorier": 62, "Enhet": "st"},
        {"Ingrediens": "Blåbär (kg)", "Pris": 78.97, "Kalorier": 570, "Enhet": "kg"}
    ]

# Toppingslista
if "toppings_lista" not in st.session_state:
    st.session_state.toppings_lista = ["Chokladknappar (kg)", "Blåbär (kg)", "Mandel (kg)", "Sesamfrön (kg)"]

# Alla uppdaterade recept
if "recept" not in st.session_state:
    st.session_state.recept = {
        "Brownie": {
            "Smör (kg)": 170, "Brunsocker (kg)": 350, "Ägg (st)": 1, 
            "Vaniljextrakt (kg)": 5, "Mjöl (kg)": 94, "Kakao (kg)": 65, 
            "Salt (kg)": 4, "Chokladknappar (kg)": 100
        },
        "Cookie": {
            "Smör (kg)": 180, "Socker (kg)": 160, "Brunsocker (kg)": 50, 
            "Ägg (st)": 2, "Vaniljextrakt (kg)": 5, "Mjöl (kg)": 210, 
            "Bakpulver (kg)": 2, "Bikarbonat (kg)": 4
        },
        "Muffins": {
            "Smör (kg)": 110, "Socker (kg)": 300, "Filmjölk (kg)": 240, 
            "Ägg (st)": 2, "Vaniljextrakt (kg)": 10, "Mjöl (kg)": 360, 
            "Bakpulver (kg)": 10, "Bikarbonat (kg)": 5, "Olja (kg)": 70, "Gräddfil (kg)": 80
        },
        "Oat cookie": {
            "Smör (kg)": 285, "Brunsocker (kg)": 220, "Ägg (st)": 2, 
            "Vaniljextrakt (kg)": 10, "Mjöl (kg)": 240, "Bakpulver (kg)": 5, 
            "Bikarbonat (kg)": 5, "Havregryn (kg)": 225
        },
        "Bagels": {
            "Mjöl (kg)": 550, "Rågsikt (kg)": 165, "Salt (kg)": 18, 
            "Olja (kg)": 28, "Honung (kg)": 21, "Sesamfrön (kg)": 15, 
            "Vallmofrön (kg)": 15, "Jäst (kg)": 25
        },
        "Morotskaka": {
            "Smör (kg)": 115, "Socker (kg)": 100, "Brunsocker (kg)": 167, 
            "Ägg (st)": 3, "Vaniljextrakt (kg)": 8, "Mjöl (kg)": 300, 
            "Bakpulver (kg)": 2, "Bikarbonat (kg)": 5, "Florsocker (kg)": 120, 
            "Salt (kg)": 3, "Kanel (kg)": 6, "Ingefära (kg)": 2, 
            "Nejlika (kg)": 1, "Yoghurt (kg)": 80, "Färskost (kg)": 120, "Morot (kg)": 240
        },
        "Biskvier": {
            "Smör (kg)": 125, "Socker (kg)": 85, "Florsocker (kg)": 90, 
            "Ägg (st)": 1, "Vaniljsocker (kg)": 6, "Bakchoklad mörk (kg)": 200, "Mandel (kg)": 100
        },
        "Chokladkaka": {
            "Smör (kg)": 338, "Socker (kg)": 815, "Florsocker (kg)": 875, 
            "Ägg (st)": 3, "Vaniljextrakt (kg)": 8, "Bakpulver (kg)": 6, 
            "Bikarbonat (kg)": 18, "Kakao (kg)": 50, "Yoghurt (kg)": 128, 
            "Vispgrädde (kg)": 140, "Filmjölk (kg)": 240, "Olja (kg)": 170, "Kaffe (kg)": 6
        },
        "Kanelbullar": {
            "Smör (kg)": 300, "Mjöl (kg)": 1250, "Socker (kg)": 228, 
            "Jäst (kg)": 14, "Salt (kg)": 4, "Kardemumma (kg)": 0, 
            "Kanel (kg)": 8, "Ägg (st)": 1
        },
        "Crumble toppings": {
            "Smör (kg)": 55, "Mjöl (kg)": 80, "Brunsocker (kg)": 60, "Socker (kg)": 15
        },
        "Orange cake": {
            "Apelsin ...": 2, "Mjöl (kg)": 220, "Ägg (st)": 3, 
            "Socker (kg)": 200, "Bakpulver (kg)": 8, "Florsocker (kg)": 150, 
            "Vaniljextrakt (kg)": 10, "Filmjölk (kg)": 120, "Olja (kg)": 120
        },
        "Cinnamon loaf": {
            "Smör (kg)": 145, "Mjöl (kg)": 345, "Ägg (st)": 2, 
            "Socker (kg)": 200, "Bakpulver (kg)": 5, "Bikarbonat (kg)": 3, 
            "Vaniljsocker (kg)": 5, "Gräddfil (kg)": 200, "Olja (kg)": 18, 
            "Kanel (kg)": 7, "Brunsocker (kg)": 60
        }
    }

# Orderdatabas
if "orders_db" not in st.session_state:
    st.session_state.orders_db = {
        "Order 11-morfar": {
            "datum": "2026-06-13",
            "rader": [
                {
                    "Recept": "Muffins", 
                    "Toppings_dict": {"Blåbär (kg)": 175.0}, 
                    "Satser": 1.0, "Bakade": 21, "Sålda": 18, "Pris_st": 15.0
                },
                {
                    "Recept": "Biskvier", 
                    "Toppings_dict": {}, 
                    "Satser": 1.0, "Bakade": 17, "Sålda": 17, "Pris_st": 20.0
                },
                {
                    "Recept": "Oat cookie", 
                    "Toppings_dict": {"Chokladknappar (kg)": 150.0}, 
                    "Satser": 1.0, "Bakade": 24, "Sålda": 24, "Pris_st": 15.0
                }
            ]
        }
    }

if "aktiv_recept_vy" not in st.session_state:
    st.session_state.aktiv_recept_vy = None

# ------------------------------------------
# 2. HJÄLPFUNKTIONER
# ------------------------------------------
def berakna_recept_totalt(recept_namn):
    rec = st.session_state.recept.get(recept_namn, {})
    ing_map = {i["Ingrediens"]: i for i in st.session_state.ingredienser if "Ingrediens" in i}
    
    tot_kr = 0.0
    tot_kcal = 0
    for ing, mangd in rec.items():
        if ing in ing_map:
            i_info = ing_map[ing]
            enhet = i_info.get("Enhet", "kg")
            faktor = (mangd / 1000.0) if enhet in ["kg", "l"] else mangd
            tot_kr += i_info.get("Pris", 0.0) * faktor
            tot_kcal += int(i_info.get("Kalorier", 0) * faktor)
            
    return tot_kr, tot_kcal

# ------------------------------------------
# 3. HUVUDNAVIGERING & FLIKAR
# ------------------------------------------
st.set_page_config(layout="wide", page_title="Lama Bageri")
st.title("🦙 Lama Bageri")

tab1, tab2, tab3, tab4 = st.tabs(["🌱 Ingredienser", "🍓 Toppings", "📖 Recept", "🛒 Orderbyggare"])

# --- TAB 1: INGREDIENSER ---
with tab1:
    st.subheader("🌱 Ingrediensbibliotek")
    df_ing = pd.DataFrame(st.session_state.ingredienser)
    st.dataframe(df_ing, use_container_width=True)

# --- TAB 2: TOPPINGS ---
with tab2:
    st.subheader("🍓 Toppingshantering")
    st.write("Valbara toppings i orderbyggaren:")
    st.write(st.session_state.toppings_lista)

# --- TAB 3: RECEPT & BYGGARE (Komprimerad vy) ---
with tab3:
    st.subheader("📖 Receptöversikt & Byggare")
    
    # Om ett recept redigeras
    if st.session_state.aktiv_recept_vy:
        r_namn = st.session_state.aktiv_recept_vy
        if st.button("⬅️ Tillbaka till receptlistan"):
            st.session_state.aktiv_recept_vy = None
            st.rerun()
            
        st.write(f"### Redigerar: {r_namn if r_namn != 'NYTT' else 'Nytt Recept'}")
        # Redigeringslogik för recept...
    else:
        # HUVUDVY FÖR RECEPT (Begränsad bredd [6, 6])
        col_main, _ = st.columns([6, 6])
        
        with col_main:
            if st.button("➕ Skapa nytt recept"):
                st.session_state.aktiv_recept_vy = "NYTT"
                st.rerun()
                
            st.markdown("---")
            
            recept_lista_ta_bort = None
            for r_namn in list(st.session_state.recept.keys()):
                k, kcal = berakna_recept_totalt(r_namn)
                col_r1, col_r2, col_r3, col_r4 = st.columns([4, 4, 1, 1])
                with col_r1:
                    st.write(f"**{r_namn}**")
                with col_r2:
                    st.caption(f"{k:.2f} kr | {kcal} kcal")
                with col_r3:
                    if st.button("✏️", key=f"edit_rec_{r_namn}"):
                        st.session_state.aktiv_recept_vy = r_namn
                        st.rerun()
                with col_r4:
                    if st.button("🗑️", key=f"del_rec_{r_namn}"):
                        recept_lista_ta_bort = r_namn

            if recept_lista_ta_bort:
                del st.session_state.recept[recept_lista_ta_bort]
                st.rerun()

# --- TAB 4: ORDERBYGGARE (Stöd för flera toppings + Datum i listan) ---
with tab4:
    st.subheader("🛒 Orderbyggare")
    
    valj_order_nycklar = list(st.session_state.orders_db.keys())
    valj_order = st.selectbox(
        "📋 Välj order att granska eller redigera:", 
        valj_order_nycklar,
        format_func=lambda x: f"{x} ({st.session_state.orders_db[x]['datum']})"
    )

    nuvarande_order = st.session_state.orders_db[valj_order]
    st.markdown(f"### {valj_order}")
    st.caption(f"Datum: {nuvarande_order['datum']}")

    # Redigeringssektion
    with st.expander("✏️ Redigera orderrader & toppings", expanded=True):
        rader_ta_bort = []
        
        for idx, r in enumerate(nuvarande_order["rader"]):
            st.markdown(f"**Rad {idx+1}: {r.get('Recept', 'Recept')}**")
            c1, c2, c3, c4, c5 = st.columns([3, 2, 2, 2, 1])
            
            with c1:
                r["Recept"] = st.selectbox("Recept", list(st.session_state.recept.keys()), index=list(st.session_state.recept.keys()).index(r.get("Recept", "Muffins")), key=f"rec_{valj_order}_{idx}")
            with c2:
                r["Satser"] = st.number_input("Satser", min_value=0.1, value=float(r.get("Satser", 1.0)), step=0.1, key=f"sat_{valj_order}_{idx}")
            with c3:
                r["Bakade"] = st.number_input("Bakade (st)", min_value=1, value=int(r.get("Bakade", 1)), key=f"bak_{valj_order}_{idx}")
            with c4:
                r["Sålda"] = st.number_input("Sålda (st)", min_value=0, value=int(r.get("Sålda", 0)), key=f"sal_{valj_order}_{idx}")
            with c5:
                r["Pris_st"] = st.number_input("Pris/st (kr)", min_value=0.0, value=float(r.get("Pris_st", 0.0)), step=0.5, key=f"prs_{valj_order}_{idx}")

            existerande_toppings = r.get("Toppings_dict", {})
            if not existerande_toppings and r.get("Topping") and r.get("Topping") != "Ingen":
                existerande_toppings = {r["Topping"]: r.get("Mängd_g", 0)}

            valda_toppings = st.multiselect(
                "Välj Toppings:",
                options=st.session_state.toppings_lista,
                default=list(existerande_toppings.keys()),
                key=f"top_multi_{valj_order}_{idx}"
            )

            nya_toppings_dict = {}
            if valda_toppings:
                top_cols = st.columns(len(valda_toppings))
                for t_idx, t_namn in enumerate(valda_toppings):
                    with top_cols[t_idx]:
                        start_mängd = float(existerande_toppings.get(t_namn, 50))
                        nya_toppings_dict[t_namn] = st.number_input(
                            f"Mängd {t_namn} (g/st):",
                            min_value=0.0,
                            value=start_mängd,
                            step=5.0,
                            key=f"mngd_{valj_order}_{idx}_{t_namn}"
                        )
            
            r["Toppings_dict"] = nya_toppings_dict
            
            if st.button("🗑️ Ta bort rad", key=f"del_row_{valj_order}_{idx}"):
                rader_ta_bort.append(idx)
            st.markdown("---")

        if rader_ta_bort:
            for index in sorted(rader_ta_bort, reverse=True):
                nuvarande_order["rader"].pop(index)
            st.rerun()

        if st.button("➕ Lägg till ny orderrad"):
            nuvarande_order["rader"].append({
                "Recept": list(st.session_state.recept.keys())[0],
                "Toppings_dict": {},
                "Satser": 1.0,
                "Bakade": 10,
                "Sålda": 10,
                "Pris_st": 15.0
            })
            st.rerun()

    # Beräkningar & Tabellvy
    ing_map = {i["Ingrediens"]: i for i in st.session_state.ingredienser if "Ingrediens" in i}
    table_rows = []
    
    tot_bakade, tot_salda, tot_kostnad, tot_vinst, tot_pris, tot_kalorier_sats = 0, 0, 0.0, 0.0, 0.0, 0

    for r in nuvarande_order["rader"]:
        rec_k, rec_kcal = berakna_recept_totalt(r.get("Recept", "Muffins"))
        
        top_k_tot = 0.0
        top_kcal_tot = 0
        top_beskrivning_list = []
        top_mängd_list = []

        top_dict = r.get("Toppings_dict", {})
        for t_namn, m_g in top_dict.items():
            if t_namn in ing_map and m_g > 0:
                t_info = ing_map[t_namn]
                enhet = t_info.get("Enhet", "kg")
                faktor = (m_g / 1000.0) if enhet in ["kg", "l"] else m_g
                
                top_k_tot += t_info.get("Pris", 0.0) * faktor
                top_kcal_tot += int(t_info.get("Kalorier", 0) * faktor)
                
                top_beskrivning_list.append(t_namn)
                top_mängd_list.append(f"{int(m_g)}g" if enhet == "kg" else f"{int(m_g)}st")

        rad_satser = float(r.get("Satser", 1.0))
        rad_bakade = int(r.get("Bakade", 1))
        rad_salda = int(r.get("Sålda", 0))
        rad_pris_st = float(r.get("Pris_st", 0.0))

        rad_tot_kostnad = (rec_k * rad_satser) + top_k_tot
        rad_kostnad_bakad = rad_tot_kostnad / rad_bakade if rad_bakade > 0 else 0
        rad_kostnad_sald = rad_tot_kostnad / rad_salda if rad_salda > 0 else 0
        
        rad_tot_intakt = rad_salda * rad_pris_st
        rad_vinst = rad_tot_intakt - rad_tot_kostnad
        rad_vinstpaslag = (rad_vinst / rad_tot_kostnad * 100) if rad_tot_kostnad > 0 else 0
        
        rad_kalorier_sats = int((rec_kcal * rad_satser) + top_kcal_tot)
        rad_kalorier_st = int(rad_kalorier_sats / rad_bakade) if rad_bakade > 0 else 0

        tot_bakade += rad_bakade
        tot_salda += rad_salda
        tot_kostnad += rad_tot_kostnad
        tot_vinst += rad_vinst
        tot_pris += rad_tot_intakt
        tot_kalorier_sats += rad_kalorier_sats

        table_rows.append({
            "Recept": r.get("Recept", ""),
            "Toppings": ", ".join(top_beskrivning_list) if top_beskrivning_list else "-",
            "Mängd": ", ".join(top_mängd_list) if top_mängd_list else "-",
            "Topping kr": f"{top_k_tot:.2f} kr" if top_k_tot > 0 else "-",
            "Topping kcal": f"{top_kcal_tot} kcal" if top_kcal_tot > 0 else "-",
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
