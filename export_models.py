"""Genera artefactos reproducibles de los modelos y sus métricas."""
import json

import joblib
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score

from config import (
    FEATURE_COLUMNS,
    FEATURE_IMPORTANCE_HYBRID,
    FEATURE_IMPORTANCE_ORIGINAL,
    METRICS_HYBRID,
    METRICS_ORIGINAL,
    MODELS_DIR,
    RF_HYBRID,
    RF_ORIGINAL,
)
from utils.load_data import load_test, load_train_hybrid, load_train_original
from utils.prediction import BEST_PARAMS


def export_model(name, X_train, y_train, model_path, metrics_path, importance_path):
    model = RandomForestClassifier(**BEST_PARAMS)
    model.fit(X_train, y_train)
    X_test, y_test = load_test()
    prediction = model.predict(X_test)
    metrics = {
        "model": "Random Forest",
        "dataset": name,
        "accuracy": round(float(accuracy_score(y_test, prediction)), 4),
        "precision": round(float(precision_score(y_test, prediction, zero_division=0)), 4),
        "recall": round(float(recall_score(y_test, prediction, zero_division=0)), 4),
        "f1": round(float(f1_score(y_test, prediction, zero_division=0)), 4),
    }
    joblib.dump(model, model_path)
    pd.DataFrame({"variable": X_train.columns, "importance": model.feature_importances_}).sort_values(
        "importance", ascending=False
    ).to_csv(importance_path, index=False)
    metrics_path.write_text(json.dumps(metrics, indent=2), encoding="utf-8")
    return metrics


def main():
    MODELS_DIR.mkdir(exist_ok=True)
    X_original, y_original = load_train_original()
    X_hybrid, y_hybrid = load_train_hybrid()
    joblib.dump(list(X_original.columns), FEATURE_COLUMNS)
    original = export_model("Original", X_original, y_original, RF_ORIGINAL, METRICS_ORIGINAL, FEATURE_IMPORTANCE_ORIGINAL)
    hybrid = export_model("Híbrido", X_hybrid, y_hybrid, RF_HYBRID, METRICS_HYBRID, FEATURE_IMPORTANCE_HYBRID)
    print("Modelos exportados")
    print(json.dumps({"original": original, "hybrid": hybrid}, indent=2))


if __name__ == "__main__":
    main()
