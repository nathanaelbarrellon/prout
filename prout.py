import streamlit as st

st.set_page_config(page_title="prout.com", page_icon="💨", layout="centered")

# Titre
st.title("💨 Bienvenue sur prout.com")

st.write("")
# Photo
st.image("Screenshot 2025-11-26 at 09.33.35.png", caption="Pétronille Buthaud, CEO de prout.com")

st.write("")
# Bouton LinkedIn
st.link_button(
    "🔗 Aller donner de la force sur LinkedIn",
    "https://www.linkedin.com/in/petronille-buthaud/"
)
st.write("")
st.link_button(
    "🏃‍♀️‍➡️ Et n'hésitez pas à aller voir ma dernière perf bien pourrave :",
    "https://www.strava.com/athletes/162133893"
)


st.write("---")
st.write("Site 100% optimisé par  Nathanaël™ 💼")
