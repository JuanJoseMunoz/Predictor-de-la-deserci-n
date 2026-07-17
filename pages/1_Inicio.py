import streamlit as st
from utils.style import load_css

st.set_page_config(layout="wide", initial_sidebar_state="expanded")
load_css()

st.title("Sistema para la Predicción del Riesgo de Deserción")

st.markdown("---")

c1, c2 = st.columns([2,1])

with c1:

    st.markdown(
    """
    ## Bienvenido

    Este prototipo implementa un modelo de Machine Learning basado en
    **Random Forest** para la predicción del riesgo de deserción estudiantil.

    El sistema permite:

    - Visualizar el conjunto de datos.
    - Analizar estadísticas descriptivas.
    - Realizar predicciones individuales.
    - Realizar predicciones masivas.
    """
    )

with c2:

    st.image(
        "images/logos/logo.jpg",
        width=250
    )

st.markdown("---")

st.info(
    "Seleccione una opción del menú lateral."
)
