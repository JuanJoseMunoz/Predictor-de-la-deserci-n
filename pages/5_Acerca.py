import streamlit as st

from config import APP_TITLE
from utils.components import page_title
from utils.style import load_css

st.set_page_config(layout="wide", initial_sidebar_state="expanded")
load_css()

page_title("ℹ️ Acerca de")
st.markdown(f"## {APP_TITLE}")
st.write("Aplicación piloto desarrollada como apoyo a una tesis sobre predicción temprana de riesgo de deserción estudiantil.")
st.markdown("""
### Alcance

- Analiza variables académicas, sociodemográficas y económicas.
- Usa modelos Random Forest entrenados con los conjuntos original e híbrido.
- Permite estimaciones individuales y por lotes.

### Interpretación

El resultado es una estimación de apoyo y no debe usarse como decisión automática. Toda intervención debe complementarse con revisión académica y humana.
""")
