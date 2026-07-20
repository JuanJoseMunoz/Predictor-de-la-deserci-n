import json

import pandas as pd
import streamlit as st

from config import (
    METRICS_HYBRID,
    METRICS_ORIGINAL,
    ORIGINAL_DATASET,
    SYNTHETIC_DATASET,
    DATASETS_DIR,
)

@st.cache_data
def load_hybrid():
    """Conjunto híbrido: registros originales más registros sintéticos."""
    original = pd.read_csv(ORIGINAL_DATASET)
    synthetic = pd.read_csv(SYNTHETIC_DATASET)
    return pd.concat([original, synthetic], ignore_index=True)

@st.cache_data
def load_train_hybrid():
    return _load_train("hybrid")

def _load_train(dataset):
    train_dir = DATASETS_DIR / "train"
    X = pd.read_csv(train_dir / f"X_train_{dataset}.csv")
    y = pd.read_csv(train_dir / f"y_train_{dataset}.csv").squeeze("columns")
    return X, y

@st.cache_data
def load_test():
    test_dir = DATASETS_DIR / "test"
    X = pd.read_csv(test_dir / "X_test.csv")
    y = pd.read_csv(test_dir / "y_test.csv").squeeze("columns")
    return X, y

def get_dataset():
    return load_hybrid()

def _load_metrics(path):
    with open(path, encoding="utf-8") as file:
        return json.load(file)

def load_metrics_hybrid():
    return _load_metrics(METRICS_HYBRID)
