import streamlit as st

st.set_page_config(page_title="prout.com", page_icon="💨", layout="centered")

# Titre
st.title("💨 Bienvenue sur prout.com")

# Photo
st.image("Screenshot 2025-11-26 at 09.33.35.png", caption="Pétronille Buthaud, CEO de prout.com")

st.write("")
# Bouton LinkedIn
st.link_button(
    "🔗 Aller donner de la force sur LinkedIn",
    "https://www.linkedin.com/in/petronille-buthaud/"
)

st.write("---")
st.write("Site 100% optimisé par  Nathanaël™ 💼")
