import streamlit as st

st.set_page_config(
    page_title="Predicción de Deserción",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded",
)

inicio = st.Page(
    "pages/inicio.py",
    title="Inicio",
    icon="🏠",
    default=True,
)

dashboard = st.Page(
    "pages/dashboard.py",
    title="Dashboard",
    icon="📊",
)

prediccion = st.Page(
    "pages/prediccion.py",
    title="Predicción",
    icon="🎯",
)

prediccion_masiva = st.Page(
    "pages/prediccion_masiva.py",
    title="Predicción masiva",
    icon="📁",
)

acerca = st.Page(
    "pages/acerca.py",
    title="Acerca",
    icon="ℹ️",
)

pg = st.navigation(
    [
        inicio,
        dashboard,
        prediccion,
        prediccion_masiva,
        acerca,
    ]
)

pg.run()