import streamlit as st

def render_sidebar():

    st.sidebar.image(
        "images/logos/coimbra_seal.svg",
        width=150,
    )

    st.sidebar.title("Universidade de Coimbra")

    st.sidebar.caption(
        "Predicción temprana de riesgo académico"
    )