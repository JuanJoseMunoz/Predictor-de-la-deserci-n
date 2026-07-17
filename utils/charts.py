import pandas as pd


def pie_chart(df, column):
    """Devuelve la distribución de una variable para gráficos nativos de Streamlit."""
    return df[column].value_counts().rename("Cantidad")


def histogram(df, column, bins=20):
    """Agrupa valores numéricos para representar un histograma sin Plotly."""
    values = pd.to_numeric(df[column], errors="coerce").dropna()
    intervals = pd.cut(values, bins=min(bins, max(values.nunique(), 1)))
    counts = intervals.value_counts().sort_index().rename("Cantidad")
    counts.index = counts.index.astype(str)
    return counts


def bar(df, column):
    return df[column].value_counts().sort_index().rename("Cantidad")
