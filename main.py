import streamlit as st

from app.config import APP_TITLE, APP_ICON
from app.services.model_service import predict
from app.services.shap_service import get_shap_values
from app.components.header import render_header
from app.components.sidebar import render_sidebar
from app.components.prediction import render_prediction
from app.components.explainability import render_explainability
from app.components.insights import render_insights
from app.components.footer import render_footer

# -----------------------------
# Streamlit App Configuration
# -----------------------------
st.set_page_config(
    page_title=APP_TITLE,
    page_icon=APP_ICON,
    layout="wide"
)

# -----------------------------
# UI Flow
# -----------------------------
render_header()

input_data = render_sidebar()

if st.sidebar.button("Predict Churn"):
    with st.spinner("Analyzing customer risk..."):
        prediction, prob, X = predict(input_data)
        shap_values = get_shap_values(X)

    render_prediction(prediction, prob)
    render_explainability(shap_values, X)
    render_insights(prob)

render_footer()
