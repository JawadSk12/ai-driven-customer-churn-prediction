📉 AI-Driven Customer Churn Prediction System

A production-style machine learning system that predicts customer churn, explains why customers are at risk using explainable AI (SHAP), and presents insights through a clean, business-ready Streamlit dashboard.

🚀 Why This Project?

Customer churn directly impacts revenue, growth, and customer lifetime value in industries like telecom, SaaS, and banking.

This project goes beyond “just predicting churn” and focuses on:

Actionable predictions

Transparent model explanations

Business-aligned decision making

It is built to demonstrate real-world data science and ML engineering skills, not an academic demo.

🧠 What This System Does

✔ Predicts whether a customer is likely to churn
✔ Outputs churn probability (not just Yes/No)
✔ Explains predictions using local SHAP explainability
✔ Converts ML output into business-friendly insights
✔ Provides an interactive Streamlit UI for live demos

🖥️ Application Preview

Streamlit Dashboard Features

Customer profile simulator (inputs via sidebar)

Churn risk classification (Low / Medium / High Priority)

Visual explanation of top churn drivers

Suggested business actions based on risk

Designed to be clean, minimal, and recruiter-friendly.

🏗️ Project Structure
ai-driven-customer-churn-prediction/
│
├── main.py                  # Streamlit app entry point
│
├── app/                     # Application package
│   ├── config.py            # App configuration & feature mapping
│   ├── services/            # ML & explainability logic
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
├── models/                  # Trained models & metadata
│   ├── random_forest.pkl
│   └── feature_columns.json
│
├── notebooks/               # EDA, preprocessing, model training
├── data/                    # Dataset files
├── reports/                 # Analysis & insights
├── requirements.txt
└── README.md


This structure mirrors real production ML projects, with clear separation between:

UI

ML logic

Explainability

Configuration

📊 Dataset

Dataset: Telco Customer Churn

Target Variable: churn_label

Feature Categories:

Customer demographics

Contract & subscription details

Billing & payment behavior

Service usage patterns

Feature engineering was performed to create business-meaningful variables such as:

Average monthly charge

Support service count

High-cost usage indicators

🤖 Machine Learning Models

Models trained and evaluated:

Logistic Regression (baseline)

Random Forest (final selected model)

XGBoost (experimental)

📈 Evaluation Metrics

ROC-AUC

Confusion Matrix

Precision / Recall / F1-Score

Random Forest was selected due to:

Strong performance

Robust handling of non-linear relationships

Better interpretability with SHAP

🔍 Explainable AI (SHAP)

This system uses SHAP (SHapley Additive exPlanations) to provide local explanations for each prediction.

For every customer, the UI shows:

Top factors increasing churn risk

Top factors reducing churn risk

🔴 Red bars → Increase churn risk
🔵 Blue bars → Reduce churn risk

This ensures the model is transparent, trustworthy, and actionable.

🧠 Business Interpretation

Instead of relying on raw probabilities, the system maps predictions to business-aligned risk bands:

Probability Range	Business Meaning
< 10%	Low Risk
10% – 18%	Medium Risk
> 18%	High Priority Churn Risk

In churn problems, even 15–20% probability is considered serious risk due to low base rates.

🧪 How to Run the Project Locally
1️⃣ Clone the repository
git clone https://github.com/JawadSk12/ai-driven-customer-churn-prediction.git
cd ai-driven-customer-churn-prediction

2️⃣ Create & activate virtual environment
python3 -m venv venv
source venv/bin/activate

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Run the Streamlit app
streamlit run main.py


The app will open at:

http://localhost:8501

💼 Real-World Use Cases

Telecom customer retention

SaaS subscription churn prevention

Banking customer attrition analysis

Proactive customer engagement strategies

🔮 Future Improvements

Probability calibration for threshold optimization

Batch churn prediction for enterprise use

Deployment on Streamlit Cloud

CRM integration for automated retention actions

Model monitoring & retraining pipeline



📌 This project was built to demonstrate end-to-end ML capability, explainable AI, and business-focused thinking.
