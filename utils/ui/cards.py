import streamlit as st


def model_card(dataset: str):
    """
    Tarjeta con la información del modelo utilizado.
    """

    with st.container(border=True):

        st.markdown("### 🤖 Modelo de Predicción")

        c1, c2 = st.columns(2)

        with c1:

            st.metric(
                "Algoritmo",
                "Random Forest"
            )

            st.metric(
                "Problema",
                "Clasificación Binaria"
            )

        with c2:

            st.metric(
                "Dataset",
                dataset
            )

            st.metric(
                "Variables",
                "36"
            )


def metrics_card(metrics: dict):
    """
    Tarjeta con las métricas del modelo.
    """

    with st.container(border=True):

        st.markdown("### 📈 Desempeño del Modelo")

        c1, c2 = st.columns(2)

        with c1:

            st.metric(
                "Accuracy",
                f"{metrics['accuracy']:.3f}"
            )

            st.metric(
                "Precision",
                f"{metrics['precision']:.3f}"
            )

        with c2:

            st.metric(
                "Recall",
                f"{metrics['recall']:.3f}"
            )

            st.metric(
                "F1 Score",
                f"{metrics['f1']:.3f}"
            )


def dataset_card(df):
    """
    Información general del dataset.
    """

    with st.container(border=True):

        st.markdown("### 📂 Dataset")

        c1, c2 = st.columns(2)

        with c1:

            st.metric(
                "Registros",
                f"{len(df):,}"
            )

            st.metric(
                "Variables",
                len(df.columns)
            )

        with c2:

            st.metric(
                "Valores faltantes",
                int(df.isna().sum().sum())
            )

            st.metric(
                "Clases",
                df["Target"].nunique()
            )


def result_card(
    prediction,
    probability,
    dataset
):
    """
    Tarjeta con el resultado de la predicción.
    """

    st.markdown("---")

    st.markdown("# 🎯 Resultado de la Predicción")

    risk = probability[0]
    permanence = probability[1]

    if prediction == 0:

        st.error(
            "## ⚠ Alto Riesgo de Deserción"
        )

    else:

        st.success(
            "## ✅ Bajo Riesgo de Deserción"
        )

    c1, c2, c3 = st.columns(3)

    with c1:

        st.metric(
            "Probabilidad Deserción",
            f"{risk*100:.2f}%"
        )

    with c2:

        st.metric(
            "Probabilidad Permanencia",
            f"{permanence*100:.2f}%"
        )

    with c3:

        st.metric(
            "Modelo",
            dataset
        )


def technical_information(df):
    """
    Panel técnico.
    """

    with st.expander("🔧 Información Técnica"):

        st.markdown("### Registro enviado al modelo")

        st.dataframe(
            df,
            use_container_width=True
        )

        st.markdown("### Tipos de datos")

        st.dataframe(
            df.dtypes.astype(str),
            use_container_width=True
        )