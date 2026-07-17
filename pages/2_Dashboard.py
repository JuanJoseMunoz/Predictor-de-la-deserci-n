import streamlit as st

from utils.load_data import get_dataset
from utils.components import page_title
from utils.components import metric_card
from utils.components import section

from utils.charts import pie_chart
from utils.charts import histogram
from utils.charts import bar
from utils.decoder import decode_dataframe
from utils.style import load_css

st.set_page_config(layout="wide", initial_sidebar_state="expanded")
load_css()

page_title("Dashboard")

dataset = st.selectbox(

    "Conjunto de datos",

    [

        "Original",

        "Híbrido"

    ]

)

from utils.load_data import (
    load_metrics_original,
    load_metrics_hybrid
)

if dataset == "Original":
    metrics = load_metrics_original()
else:
    metrics = load_metrics_hybrid()

st.divider()
st.subheader("📈 Desempeño del modelo Random Forest")

st.caption("Métricas para la clase 0: Dropout (riesgo de deserción).")
c1, c2, c3= st.columns(3)

c1.metric("Precision", f"{metrics['precision']:.3f}")
c2.metric("Recall", f"{metrics['recall']:.3f}")
c3.metric("F1 Score", f"{metrics['f1']:.3f}")

df = decode_dataframe(get_dataset(dataset))

st.write("")

##############################################################

c1, c2, c3, c4 = st.columns(4)

with c1:

    metric_card(

        "Estudiantes",

        len(df)

    )

with c2:

    metric_card(

        "Variables",

        len(df.columns)

    )

with c3:

    metric_card(

        "Valores faltantes",

        int(df.isnull().sum().sum())

    )

with c4:

    metric_card(

        "Clases",

        df["Target"].nunique()

    )

##############################################################

st.divider()

c1, c2 = st.columns(2)

with c1:

    section("Distribución del Target")

    st.bar_chart(pie_chart(df, "Target"))

with c2:

    section("Edad de matrícula")

    st.bar_chart(histogram(df, "Age at enrollment"))

##############################################################

st.divider()

c1, c2 = st.columns(2)

with c1:

    section("Sexo")

    st.bar_chart(bar(df, "Gender"))

with c2:

    section("Estado civil")

    st.bar_chart(bar(df, "Marital status"))

##############################################################

st.divider()

section("Vista previa")

st.dataframe(

    df,

    height=350

)

##############################################################

csv = df.to_csv(index=False)

st.download_button(

    "Descargar Dataset",

    csv,

    file_name=f"{dataset}.csv",

    mime="text/csv"

)
