import json
import joblib
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]
MODELS_DIR = BASE_DIR / "models"

model = joblib.load(MODELS_DIR / "random_forest.pkl")

with open(MODELS_DIR / "feature_columns.json", "r") as f:
    FEATURE_COLUMNS = json.load(f)

def prepare_input(input_dict):
    df = pd.DataFrame([input_dict])
    df = df.reindex(columns=FEATURE_COLUMNS, fill_value=0)
    return df

def predict(input_dict):
    X = prepare_input(input_dict)
    prediction = model.predict(X)[0]
    probability = model.predict_proba(X)[0][1]
    return prediction, probability, X
