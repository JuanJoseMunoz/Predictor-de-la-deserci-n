import streamlit as st

from utils.load_data import get_dataset
from utils.components import page_title

from utils.charts import pie_chart
from utils.charts import histogram
from utils.charts import bar
from utils.decoder import decode_dataframe
from utils.style import load_css
from utils.sidebar import render_sidebar
from utils.load_data import load_metrics_hybrid

load_css()
render_sidebar()

page_title("Dashboard académico")

metrics = load_metrics_hybrid()
df = decode_dataframe(get_dataset())

st.markdown(
    f"""
    <div class="uc-panel dashboard-summary">
        <div>
            <span class="uc-section-label">Visión general</span>
            <h2>Resumen del rendimiento del modelo</h2>
            <p>
                El sistema emplea un modelo <strong>Random Forest</strong> entrenado con el
                conjunto de datos híbrido. Las métricas siguientes corresponden a la clase
                <strong>Dropout</strong> (riesgo de deserción).
            </p>
        </div>
        <div class="dashboard-summary-metrics">
            <div class="dashboard-stat-card">
                <div class="dashboard-stat-title">Precisión</div>
                <div class="dashboard-stat-value">{metrics['precision']:.3f}</div>
            </div>
            <div class="dashboard-stat-card">
                <div class="dashboard-stat-title">Recall</div>
                <div class="dashboard-stat-value">{metrics['recall']:.3f}</div>
            </div>
            <div class="dashboard-stat-card">
                <div class="dashboard-stat-title">F1 Score</div>
                <div class="dashboard-stat-value">{metrics['f1']:.3f}</div>
            </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    f"""
    <div class="dashboard-card-grid">
        <div class="dashboard-stat-card">
            <div class="dashboard-stat-title">Estudiantes</div>
            <div class="dashboard-stat-value">{len(df)}</div>
        </div>
        <div class="dashboard-stat-card">
            <div class="dashboard-stat-title">Variables</div>
            <div class="dashboard-stat-value">{len(df.columns)}</div>
        </div>
        <div class="dashboard-stat-card">
            <div class="dashboard-stat-title">Valores faltantes</div>
            <div class="dashboard-stat-value">{int(df.isnull().sum().sum())}</div>
        </div>
        <div class="dashboard-stat-card">
            <div class="dashboard-stat-title">Clases</div>
            <div class="dashboard-stat-value">{df['Target'].nunique()}</div>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.divider()

c1, c2 = st.columns(2, gap="large")

distribution = df["Target"].replace({
    "Enrolled": "No desertores",
    "Graduate": "No desertores",
    "Dropout": "Desertores"
})

chart = distribution.value_counts().sort_index()

with c1:
    st.markdown(
        """
        <div class="dashboard-chart-card">
            <div class="dashboard-chart-title">Distribución del resultado</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.bar_chart(chart)

with c2:
    st.markdown(
        """
        <div class="dashboard-chart-card">
            <div class="dashboard-chart-title">Edad de matrícula</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.bar_chart(histogram(df, "Age at enrollment"))

st.divider()

c1, c2 = st.columns(2, gap="large")

with c1:
    st.markdown(
        """
        <div class="dashboard-chart-card">
            <div class="dashboard-chart-title">Género</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.bar_chart(bar(df, "Gender"))

with c2:
    st.markdown(
        """
        <div class="dashboard-chart-card">
            <div class="dashboard-chart-title">Estado civil</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.bar_chart(bar(df, "Marital status"))

st.divider()

st.markdown(
    """
    <div class="dashboard-table-panel">
        <div class="dashboard-chart-title">Vista previa del dataset</div>
        <p class="dashboard-table-caption">
            Explore las primeras filas del conjunto de datos utilizados para entrenar
            y validar el modelo.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

st.dataframe(df, height=350)

csv = df.to_csv(index=False)

st.download_button(
    "Descargar dataset",
    csv,
    file_name="dataset.csv",
    mime="text/csv"
)