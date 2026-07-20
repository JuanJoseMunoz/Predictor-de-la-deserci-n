import pandas as pd
import streamlit as st

from utils.components import page_title
from utils.prediction import predict_dataframe, train_model
from utils.style import load_css
from utils.sidebar import render_sidebar

load_css()
render_sidebar()

page_title("Predicción masiva")
st.markdown(
    """
    <div class="page-panel">
        <span class="uc-section-label">Carga por lote</span>
        <h3>Genere predicciones para múltiples estudiantes</h3>
        <p>
            Cargue un CSV con las variables del modelo y obtenga una estimación de
            riesgo para cada registro. La columna <strong>Target</strong> es opcional.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="form-card">
        <h3>Suba su archivo CSV</h3>
        <p>El modelo procesará automáticamente todas las entradas y mostrará un resumen
           de los niveles de riesgo asociados.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

file = st.file_uploader("Seleccione un archivo CSV", type="csv")

with st.spinner("Preparando el modelo de predicción..."):
    model, metrics = train_model()

with st.expander("Columnas requeridas"):
    st.code("\n".join(model.feature_names_in_))

if file is not None:
    try:
        uploaded = pd.read_csv(file)
        results = predict_dataframe(model, uploaded)
    except (UnicodeDecodeError, pd.errors.ParserError, ValueError) as error:
        st.error(f"No fue posible procesar el archivo: {error}")
    else:
        low = (results["Nivel de riesgo"] == "Bajo").sum()
        medium = (results["Nivel de riesgo"] == "Medio").sum()
        high = (results["Nivel de riesgo"] == "Alto").sum()

        st.markdown(
            """
            <div class="result-card">
                <h3>Resumen de predicción</h3>
                <p>Los resultados se categorizan en niveles de riesgo para facilitar la revisión y priorización de intervenciones.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown(
            f"""
            <div class="prediction-stat-grid">
                <div class="feature-card">
                    <h3>Registros</h3>
                    <p>{len(results)}</p>
                </div>
                <div class="feature-card">
                    <h3>🟢 Bajo</h3>
                    <p>{low}</p>
                </div>
                <div class="feature-card">
                    <h3>🟡 Medio</h3>
                    <p>{medium}</p>
                </div>
                <div class="feature-card">
                    <h3>🔴 Alto</h3>
                    <p>{high}</p>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        filter_option = st.radio(
            "Mostrar resultados",
            ["Todos", "Bajo", "Medio", "Alto"],
            horizontal=True,
        )

        if filter_option == "Bajo":
            filtered_results = results[results["Nivel de riesgo"] == "Bajo"]
        elif filter_option == "Medio":
            filtered_results = results[results["Nivel de riesgo"] == "Medio"]
        elif filter_option == "Alto":
            filtered_results = results[results["Nivel de riesgo"] == "Alto"]
        else:
            filtered_results = results

        st.caption(f"Mostrando {len(filtered_results)} de {len(results)} registros.")
        st.dataframe(filtered_results, height=420)
        st.download_button(
            "Descargar resultados filtrados",
            filtered_results.to_csv(index=False).encode("utf-8"),
            file_name="predicciones_desercion.csv",
            mime="text/csv",
        )
