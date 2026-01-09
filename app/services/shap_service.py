import shap
from .model_service import model

explainer = shap.TreeExplainer(model)

def get_shap_values(X):
    shap_values = explainer.shap_values(X)
    if isinstance(shap_values, list):
        shap_values = shap_values[1]
    return shap_values
