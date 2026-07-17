import pandas as pd
import streamlit as st

from utils.components import page_title
from utils.prediction import predict_dataframe, train_model
from utils.style import load_css

st.set_page_config(layout="wide", initial_sidebar_state="expanded")
load_css()

page_title("📥 Predicción masiva")
st.write("Cargue un CSV con las 36 variables usadas por el modelo. La columna `Target` es opcional y se conserva si está presente.")
dataset = st.radio("Modelo de entrenamiento", ["Original", "Híbrido"], horizontal=True, key="bulk_dataset")
file = st.file_uploader("Archivo CSV", type="csv")

with st.spinner("Cargando modelo..."):
    model, metrics = train_model(dataset)

with st.expander("Columnas requeridas"):
    st.code("\n".join(model.feature_names_in_))

if file is not None:
    try:
        uploaded = pd.read_csv(file)
        results = predict_dataframe(model, uploaded)
    except (UnicodeDecodeError, pd.errors.ParserError, ValueError) as error:
        st.error(f"No fue posible procesar el archivo: {error}")
    else:
        risk_count = int((results["Predicción"] == 0).sum())
        c1, c2, c3 = st.columns(3)
        c1.metric("Registros procesados", len(results))
        c2.metric("Con riesgo", risk_count)
        c3.metric("Sin riesgo", len(results) - risk_count)

        filter_option = st.radio(
            "Mostrar resultados",
            ["Todos", "Solo con riesgo", "Solo sin riesgo"],
            horizontal=True,
        )

        if filter_option == "Solo con riesgo":
            filtered_results = results[results["Predicción"] == 0]
        elif filter_option == "Solo sin riesgo":
            filtered_results = results[results["Predicción"] == 1]
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
