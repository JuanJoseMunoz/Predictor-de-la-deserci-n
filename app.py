import streamlit as st

from config import APP_TITLE
from utils.style import load_css

st.set_page_config(page_title="Student Dropout Prediction", page_icon="🎓", layout="wide", initial_sidebar_state="expanded")
load_css()
st.sidebar.image("images/logos/logo.jpg", width=250)
st.sidebar.title("🎓 Student Dropout")
st.title(APP_TITLE)
st.caption("Prueba piloto para la predicción del riesgo de deserción estudiantil.")
