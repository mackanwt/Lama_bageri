import streamlit as st
import requests
import json
import base64

st.set_page_config(page_title="GitHub Felsökning", page_icon="🔍")

st.title("🔍 GitHub API Felsökning")

GITHUB_TOKEN = st.secrets.get("GITHUB_TOKEN", "").strip()
GITHUB_REPO = st.secrets.get("GITHUB_REPO", "").strip()

st.write(f"**GITHUB_REPO i Secrets:** `{GITHUB_REPO}`")
st.write(f"**GITHUB_TOKEN i Secrets:** `{'Startar med: ' + GITHUB_TOKEN[:8] + '...' if GITHUB_TOKEN else 'SAKNAS'}`")

st.markdown("---")

if st.button("🧪 Testa anslutning till GitHub", type="primary"):
    if not GITHUB_TOKEN or not GITHUB_REPO:
        st.error("GITHUB_TOKEN eller GITHUB_REPO saknas helt i Secrets!")
    else:
        # Testa att hämta innehållet i rotmappen
        url = f"https://api.github.com/repos/{GITHUB_REPO}/contents"
        headers = {"Authorization": f"token {GITHUB_TOKEN}"}
        
        res = requests.get(url, headers=headers)
        
        st.subheader(f"Statuskod: {res.status_code}")
        
        if res.status_code == 200:
            st.success("🎉 Anslutningen lyckades!")
            files = res.json()
            file_names = [f["name"] for f in files]
            st.write("Filer som hittades på GitHub:")
            st.json(file_names)
            
            for file_name in ["ingredienser.json", "recept.json"]:
                if file_name in file_names:
                    st.success(f"✅ `{file_name}` finns i mappen.")
                    f_res = requests.get(f"{url}/{file_name}", headers=headers)
                    if f_res.status_code == 200:
                        content = f_res.json()["content"]
                        decoded = base64.b64decode(content).decode('utf-8')
                        try:
                            data = json.loads(decoded)
                            st.info(f"Filen `{file_name}` laddades upp och innehåller giltig JSON ({len(data)} rader)!")
                        except Exception as e:
                            st.error(f"❌ JSON-formatfel i `{file_name}`: {e}")
                else:
                    st.error(f"❌ Filen `{file_name}` hittades inte i rotmappen på GitHub.")
                    
        elif res.status_code == 404:
            st.error("❌ GitHub svarade med **404 Not Found**.")
            st.write("Detta betyder antingen:")
            st.write("1. `GITHUB_REPO` stämmer inte exakt med adressen på GitHub (kontrollera stora/små bokstäver).")
            st.write("2. Token har inte lagts till för rätt repository på GitHub under Fine-grained token permissions.")
            st.json(res.json())
        elif res.status_code == 401:
            st.error("❌ GitHub svarade med **401 Unauthorized**. Token kändes inte igen av GitHub.")
        else:
            st.error(f"Ett annat fel uppstod: {res.text}")
