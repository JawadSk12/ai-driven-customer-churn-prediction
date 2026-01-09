import pandas as pd
import joblib
import json

# ===============================
# Load model
# ===============================
model = joblib.load("models/random_forest.pkl")  # or gradient_boosting.pkl

# ===============================
# Load feature columns
# ===============================
with open("models/feature_columns.json", "r") as f:
    feature_columns = json.load(f)

# ===============================
# Create a sample customer (TEST INPUT)
# ===============================
sample_customer = {
    "tenure_months": 3,
    "monthly_charges": 95,
    "total_charges": 280,
    "cltv": 2500,
    "gender_Male": 1,
    "senior_citizen_Yes": 0,
    "partner_Yes": 0,
    "dependents_Yes": 0,
    "phone_service_Yes": 1,
    "multiple_lines_No phone service": 0,
    "multiple_lines_Yes": 1,
    "internet_service_Fiber optic": 1,
    "internet_service_No": 0,
    "online_security_No internet service": 0,
    "online_security_Yes": 0,
    "online_backup_No internet service": 0,
    "online_backup_Yes": 0,
    "device_protection_No internet service": 0,
    "device_protection_Yes": 0,
    "tech_support_No internet service": 0,
    "tech_support_Yes": 0,
    "streaming_tv_No internet service": 0,
    "streaming_tv_Yes": 1,
    "streaming_movies_No internet service": 0,
    "streaming_movies_Yes": 1,
    "contract_One year": 0,
    "contract_Two year": 0,
    "paperless_billing_Yes": 1,
    "payment_method_Credit card (automatic)": 0,
    "payment_method_Electronic check": 1,
    "payment_method_Mailed check": 0,
    "high_monthly_charge": 1,
    "avg_charge_per_month": 93,
    "support_service_count": 0,
    "streaming_service_count": 2
}

# ===============================
# Convert to DataFrame with correct order
# ===============================
input_df = pd.DataFrame([sample_customer])
input_df = input_df.reindex(columns=feature_columns, fill_value=0)

# ===============================
# Prediction
# ===============================
prediction = model.predict(input_df)[0]
probability = model.predict_proba(input_df)[0][1]

# ===============================
# Output
# ===============================
print("Churn Prediction:", "YES" if prediction == 1 else "NO")
print("Churn Probability:", round(probability, 3))
