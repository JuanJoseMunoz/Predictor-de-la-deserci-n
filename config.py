from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATASETS_DIR = BASE_DIR / "datasets"
MODELS_DIR = BASE_DIR / "models"

APP_TITLE = "Sistema para la Predicción del Riesgo de Deserción"
ORIGINAL_DATASET = DATASETS_DIR / "original.csv"
SYNTHETIC_DATASET = DATASETS_DIR / "hybrid.csv"
RF_ORIGINAL = MODELS_DIR / "rf_original.pkl"
RF_HYBRID = MODELS_DIR / "rf_hybrid.pkl"
FEATURE_COLUMNS = MODELS_DIR / "feature_columns.pkl"
METRICS_ORIGINAL = MODELS_DIR / "metrics_original.json"
METRICS_HYBRID = MODELS_DIR / "metrics_hybrid.json"
FEATURE_IMPORTANCE_ORIGINAL = MODELS_DIR / "feature_importance_original.csv"
FEATURE_IMPORTANCE_HYBRID = MODELS_DIR / "feature_importance_hybrid.csv"
