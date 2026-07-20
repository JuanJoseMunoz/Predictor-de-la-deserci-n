import streamlit as st
from utils.style import load_css
from utils.sidebar import render_sidebar

load_css()
render_sidebar()

st.markdown(
    """
    <div class="uc-hero">
        <div class="uc-kicker">Universidade de Coimbra</div>
        <h1>Sistema para la Predicción del Riesgo de Deserción</h1>
        <p>
            Prototipo académico para apoyar la identificación temprana de estudiantes
            que podrían requerir acompañamiento, construido a partir del dataset de la
            Universidad de Coimbra, Portugal.
        </p>
        <div class="uc-badge-row">
            <span class="uc-badge">Random Forest</span>
            <span class="uc-badge">Análisis académico</span>
            <span class="uc-badge">Predicción individual y masiva</span>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="page-panel">
        <span class="uc-section-label">Introducción</span>
        <h3>Descubra cómo el sistema apoya la permanencia estudiantil</h3>
        <p>
            Esta herramienta une datos académicos y aprendizaje automático para ofrecer
            una visión clara del riesgo de deserción y facilitar intervenciones tempranas.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="feature-card-grid">
        <div class="feature-card">
            <h3>Dashboard académico</h3>
            <p>Explora métricas del modelo, distribuciones clave del dataset y la información que sustenta el análisis.</p>
        </div>
        <div class="feature-card">
            <h3>Predicción individual</h3>
            <p>Ingresa los datos de un estudiante y recibe una evaluación personalizada del riesgo de abandono.</p>
        </div>
        <div class="feature-card">
            <h3>Predicción masiva</h3>
            <p>Procesa archivos CSV completos para generar estimaciones de riesgo en lotes y apoyar decisiones a escala.</p>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown("---")

st.info(
    "Seleccione una opción del menú lateral para explorar el dashboard, crear una predicción individual o procesar un archivo CSV."
)
