import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def _normalize_shap(shap_values, n_features):
    """
    Normalize SHAP output to 1D array of length = n_features
    Handles all common SHAP output shapes safely.
    """
    arr = np.array(shap_values)

    # Case 1: (1, n_features)
    if arr.ndim == 2 and arr.shape[0] == 1:
        arr = arr[0]

    # Case 2: (n_features, 2) or (1, n_features, 2)
    if arr.ndim == 3:
        # take class = 1 (churn)
        arr = arr[:, :, 1] if arr.shape[-1] == 2 else arr
        arr = arr[0] if arr.ndim == 2 else arr

    # Final safety check
    if arr.ndim != 1 or arr.shape[0] != n_features:
        raise ValueError(
            f"SHAP alignment error: got {arr.shape}, expected ({n_features},)"
        )

    return arr


def render_explainability(shap_values, X):
    """
    Render local SHAP explanation for a single customer.
    Stable, Streamlit-safe, interview-grade.
    """

    st.subheader("🔍 Why this prediction?")

    st.markdown(
        "The chart below shows the **top factors influencing this customer's churn prediction**. "
        "Red bars increase churn risk, blue bars reduce it."
    )

    # Normalize SHAP values
    shap_1d = _normalize_shap(shap_values, X.shape[1])

    # Build aligned DataFrame
    shap_df = pd.DataFrame({
        "feature": X.columns,
        "impact": np.abs(shap_1d),
        "direction": shap_1d
    })
     
    shap_df = shap_df[~shap_df["feature"].str.contains("churn_label")]


    # Top 10 drivers
    shap_df = shap_df.sort_values("impact", ascending=False).head(10)

    # Plot
    fig, ax = plt.subplots(figsize=(8, 5))

    colors = shap_df["direction"].apply(
        lambda x: "#d62728" if x > 0 else "#1f77b4"
    )

    ax.barh(shap_df["feature"], shap_df["impact"], color=colors)
    ax.invert_yaxis()
    ax.set_xlabel("Impact on Churn Prediction")
    ax.set_title("Top Drivers for This Customer")

    st.pyplot(fig)
