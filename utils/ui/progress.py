import streamlit as st


def risk_progress(probability):
    """
    Muestra una barra de riesgo y una interpretación.
    probability[0] = Probabilidad de Deserción
    probability[1] = Probabilidad de Permanencia
    """

    risk = float(probability[0])

    st.markdown("### 📊 Nivel de Riesgo")

    st.progress(risk)

    if risk < 0.30:

        color = "🟢"
        level = "BAJO"

    elif risk < 0.60:

        color = "🟡"
        level = "MODERADO"

    else:

        color = "🔴"
        level = "ALTO"

    st.markdown(
        f"""
### {color} Riesgo {level}

**Probabilidad de deserción:** **{risk*100:.2f}%**
"""
    )


def confidence_card(probability):
    """
    Muestra la confianza del modelo.
    """

    confidence = max(probability)

    st.markdown("### 🎯 Confianza del Modelo")

    st.metric(

        "Confianza",

        f"{confidence*100:.2f}%"

    )


def probability_table(probability):

    st.markdown("### 📈 Probabilidades")

    st.dataframe(

        {
            "Clase": [
                "Deserción",
                "Permanencia"
            ],

            "Probabilidad": [
                f"{probability[0]*100:.2f} %",
                f"{probability[1]*100:.2f} %"
            ]

        },

        use_container_width=True,

        hide_index=True

    )


def interpretation(probability):

    risk = probability[0]

    st.markdown("### 📝 Interpretación")

    if risk < 0.30:

        st.success(
            """
El estudiante presenta un **riesgo bajo** de deserción.

Los indicadores académicos y personales son favorables.
"""
        )

    elif risk < 0.60:

        st.warning(
            """
El estudiante presenta un **riesgo moderado**.

Se recomienda realizar seguimiento preventivo.
"""
        )

    else:

        st.error(
            """
El estudiante presenta un **riesgo alto**.

Se recomienda intervención institucional inmediata.
"""
        )