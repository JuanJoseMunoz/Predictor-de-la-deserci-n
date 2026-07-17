import pandas as pd
import streamlit as st
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score

from utils.load_data import load_test, load_train_hybrid, load_train_original

BEST_PARAMS = {
    "n_estimators": 175,
    "max_depth": 21,
    "min_samples_split": 2,
    "min_samples_leaf": 1,
    "max_features": "log2",
    "criterion": "entropy",
    "bootstrap": False,
    "random_state": 42,
    "n_jobs": -1,
}


@st.cache_resource
def train_model(dataset):
    X_train, y_train = load_train_original() if dataset == "Original" else load_train_hybrid()
    X_test, y_test = load_test()
    model = RandomForestClassifier(**BEST_PARAMS)
    model.fit(X_train, y_train)
    prediction = model.predict(X_test)
    metrics = {
        "accuracy": accuracy_score(y_test, prediction),
        "precision": precision_score(y_test, prediction, pos_label=0, zero_division=0),
        "recall": recall_score(y_test, prediction, pos_label=0, zero_division=0),
        "f1": f1_score(y_test, prediction, pos_label=0, zero_division=0),
    }
    return model, metrics


def validate_features(dataframe: pd.DataFrame, model):
    expected = list(model.feature_names_in_)
    missing = [column for column in expected if column not in dataframe.columns]
    if missing:
        raise ValueError("Faltan columnas requeridas: " + ", ".join(missing))
    result = dataframe.loc[:, expected].copy()
    result = result.apply(pd.to_numeric, errors="coerce")
    if result.isna().any().any():
        invalid = result.columns[result.isna().any()].tolist()
        raise ValueError("Hay valores vacíos o no numéricos en: " + ", ".join(invalid))
    return result


def predict_student(model, student):
    student = validate_features(student, model)
    prediction = int(model.predict(student)[0])
    probability_by_class = dict(zip(model.classes_, model.predict_proba(student)[0]))
    return prediction, float(probability_by_class.get(0, 0.0)), float(probability_by_class.get(1, 0.0))


def predict_dataframe(model, dataframe):
    features = validate_features(dataframe, model)
    probabilities = model.predict_proba(features)
    probability_by_class = {label: probabilities[:, index] for index, label in enumerate(model.classes_)}
    result = dataframe.copy()
    result["Predicción"] = model.predict(features)
    result["Riesgo de deserción"] = probability_by_class.get(0, 0.0)
    result["Probabilidad de permanencia"] = probability_by_class.get(1, 0.0)
    result["Resultado"] = result["Predicción"].map({0: "Riesgo de deserción", 1: "Sin riesgo"})
    return result
