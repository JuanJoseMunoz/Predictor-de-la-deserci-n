import streamlit as st

from utils.components import page_title
from utils.decoder import decode_dataframe
from utils.forms import build_dataframe
from utils.prediction import predict_student, train_model
from utils.style import load_css

st.set_page_config(layout="wide", initial_sidebar_state="expanded")
load_css()

page_title("🎯 Predicción individual")
st.write("Complete la información disponible del estudiante para estimar su riesgo de deserción.")
dataset = st.radio("Modelo de entrenamiento", ["Original", "Híbrido"], horizontal=True)

with st.spinner("Cargando modelo..."):
    model, metrics = train_model(dataset)

with st.form("prediction_form"):
    student_df = build_dataframe()
    predict_button = st.form_submit_button("🔮 Realizar predicción")

if predict_button:
    try:
        prediction, dropout_probability, stay_probability = predict_student(model, student_df)
    except ValueError as error:
        st.error(str(error))
    else:
        st.divider()
        st.header("Resultado")
        if prediction == 0:
            st.error("⚠️ Riesgo de deserción detectado")
        else:
            st.success("✅ No presenta riesgo de deserción")
        c1, c2 = st.columns(2)
        c1.metric("Probabilidad de deserción", f"{dropout_probability * 100:.2f}%")
        c2.metric("Probabilidad de permanencia", f"{stay_probability * 100:.2f}%")
        with st.expander("Ver registro enviado al modelo"):
            st.dataframe(decode_dataframe(student_df))
