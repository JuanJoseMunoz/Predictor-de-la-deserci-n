import streamlit as st

from config import APP_TITLE
from utils.components import page_title
from utils.style import load_css
from utils.sidebar import render_sidebar

load_css()
render_sidebar()

page_title("Acerca de")
st.markdown(
    f"""
    <div class="page-panel">
        <span class="uc-section-label">Contexto</span>
        <h3>{APP_TITLE}</h3>
        <p>
            Aplicación piloto desarrollada como apoyo a una tesis sobre predicción temprana
            de riesgo de deserción estudiantil, contextualizada con datos de educación superior de Portugal.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="feature-card-grid">
        <div class="feature-card">
            <h3>Alcance</h3>
            <p>Analiza variables académicas, sociodemográficas y económicas para aportar una mirada integral al acompañamiento estudiantil.</p>
        </div>
        <div class="feature-card">
            <h3>Modelos</h3>
            <p>Emplea Random Forest entrenados con los conjuntos original y sintéticos para lograr mejores estimaciones.</p>
        </div>
        <div class="feature-card">
            <h3>Funcionalidad</h3>
            <p>Permite generar predicciones individuales y por lote, apoyando procesos de vigilancia y detección temprana.</p>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="page-panel">
        <span class="uc-section-label">Interpretación</span>
        <h3>Uso responsable del resultado</h3>
        <p>
            El resultado es una estimación de apoyo y no debe usarse como decisión automática.
            Toda intervención debe complementarse con revisión académica y humana.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)
