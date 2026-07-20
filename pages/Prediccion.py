import streamlit as st

from utils.components import page_title
from utils.decoder import decode_dataframe
from utils.forms import build_dataframe
from utils.prediction import predict_student, train_model
from utils.style import load_css
from utils.sidebar import render_sidebar

load_css()
render_sidebar()

page_title("Predicción individual")

st.markdown(
    """
    <div class="page-panel">
        <span class="uc-section-label">Análisis puntual</span>
        <h3>Evalúe el riesgo de deserción de un estudiante</h3>
        <p>
            Complete la información disponible para generar una predicción individual.
            El resultado incluye el nivel de riesgo y las probabilidades de deserción y
            permanencia.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

with st.spinner("Cargando modelo..."):
    model, metrics = train_model()

with st.form("prediction_form"):
    st.markdown(
        """
        <div class="form-card">
            <h3>Datos del estudiante</h3>
            <p>Ingrese los valores solicitados para cada variable usada por el modelo.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    student_df = build_dataframe()
    predict_button = st.form_submit_button("Realizar predicción")

if predict_button:
    try:
        prediction, dropout_probability, stay_probability, risk_level = predict_student(model, student_df)
    except ValueError as error:
        st.error(str(error))
    else:
        st.divider()
        st.markdown(
            """
            <div class="result-card">
                <h3>Resultado de la predicción</h3>
                <p>El modelo ha generado una evaluación del nivel de riesgo con base en los datos ingresados.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

        if risk_level == "Bajo":
            st.success("🟢 Bajo riesgo de deserción")
        elif risk_level == "Medio":
            st.warning("🟡 Riesgo medio de deserción")
        else:
            st.error("🔴 Alto riesgo de deserción")

        c1, c2, c3 = st.columns(3, gap="large")
        c1.metric("Nivel de riesgo", risk_level)
        c2.metric("Probabilidad de deserción", f"{dropout_probability*100:.2f}%")
        c3.metric("Probabilidad de permanencia", f"{stay_probability*100:.2f}%")

        with st.expander("Ver registro enviado al modelo"):
            st.dataframe(decode_dataframe(student_df))
