📉 AI-Driven Customer Churn Prediction System

An end-to-end machine learning–powered churn prediction system that predicts customer churn, explains why a customer is likely to churn using SHAP, and presents insights through a clean, business-friendly Streamlit dashboard.

This project is designed to be resume-worthy, interview-ready, and portfolio-grade, following real-world ML engineering practices.

🚀 Project Overview

Customer churn is one of the most critical problems faced by subscription-based businesses such as telecom, SaaS, banking, and e-commerce.

This system helps businesses:

Predict whether a customer is likely to churn

Understand the key drivers behind churn

Take data-driven retention actions

The project covers the entire ML lifecycle, from data preprocessing and modeling to explainability and UI deployment.

🧠 Key Features

✔ Predicts customer churn (Yes / No)
✔ Outputs churn probability score
✔ Explains predictions using SHAP-based local explainability
✔ Clean and interactive Streamlit UI
✔ Business-focused insights and recommendations
✔ Modular, production-style code structure

🏗️ Project Structure
churn_prediction_project/
│
├── main.py                  # Streamlit app entry point
│
├── app/                     # Application package
│   ├── config.py            # App configs & feature mappings
│   ├── services/            # ML + SHAP logic
│   │   ├── model_service.py
│   │   └── shap_service.py
│   ├── components/          # UI components
│   │   ├── header.py
│   │   ├── sidebar.py
│   │   ├── prediction.py
│   │   ├── explainability.py
│   │   ├── insights.py
│   │   └── footer.py
│
├── models/                  # Trained models & feature metadata
│   ├── random_forest.pkl
│   └── feature_columns.json
│
├── notebooks/               # Jupyter notebooks (EDA, training, SHAP)
├── data/                    # Dataset files
├── reports/                 # Analysis outputs
├── requirements.txt
└── README.md

📊 Dataset

Source: Telco Customer Churn dataset

Target Variable: churn_label

Features include:

Demographics

Subscription & contract details

Billing & payment behavior

Service usage patterns

⚙️ Machine Learning Models

The following models were trained and evaluated:

Logistic Regression (baseline)

Random Forest (final selected model)

XGBoost (optional experimentation)

Evaluation Metrics:

ROC-AUC

Confusion Matrix

Precision, Recall, F1-score

Random Forest was selected due to:

Strong performance

Robust handling of non-linear relationships

Better explainability with SHAP

🔍 Explainability (SHAP)

This project uses SHAP (SHapley Additive exPlanations) to:

Explain why a customer is predicted to churn

Show top risk drivers and protective factors

Provide local explanations for individual customers

Red bars increase churn risk, while blue bars reduce it — making insights intuitive for business users.

🖥️ Streamlit Dashboard
UI Capabilities:

Interactive customer input form

Real-time churn prediction

Probability-based risk classification

Visual explanation of churn drivers

Suggested business actions

The UI is designed to be:

Minimal

Recruiter-friendly

Business-oriented

🧪 How to Run the Project Locally
1️⃣ Create virtual environment
python3 -m venv venv
source venv/bin/activate

2️⃣ Install dependencies
pip install -r requirements.txt

3️⃣ Run the app
streamlit run main.py

📈 Business Use-Cases

Telecom customer retention

SaaS subscription churn analysis

Banking customer attrition prevention

Proactive customer engagement strategies

🧠 Future Improvements

Retrain model excluding any legacy leakage features

Deploy on Streamlit Cloud

Add batch prediction support

Integrate CRM-style recommendations

Add model monitoring

👨‍💻 Author

Jawad SK
Aspiring Data Scientist | Machine Learning Engineer