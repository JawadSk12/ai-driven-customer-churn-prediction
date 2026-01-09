import streamlit as st

def render_sidebar():
    st.sidebar.header("Customer Profile")

    tenure = st.sidebar.slider("Tenure (months)", 0, 72, 6)
    monthly = st.sidebar.slider("Monthly Charges", 20, 150, 70)
    total = st.sidebar.number_input("Total Charges", 0, 10000, 500)
    cltv = st.sidebar.number_input("Customer Lifetime Value", 0, 10000, 2500)

    contract = st.sidebar.selectbox(
        "Contract Type", ["Month-to-month", "One year", "Two year"]
    )

    payment = st.sidebar.selectbox(
        "Payment Method",
        ["Electronic check", "Mailed check", "Credit card (automatic)"]
    )

    return {
        "tenure_months": tenure,
        "monthly_charges": monthly,
        "total_charges": total,
        "cltv": cltv,
        "contract_One year": 1 if contract == "One year" else 0,
        "contract_Two year": 1 if contract == "Two year" else 0,
        "payment_method_Electronic check": 1 if payment == "Electronic check" else 0,
        "payment_method_Mailed check": 1 if payment == "Mailed check" else 0,
        "payment_method_Credit card (automatic)": 1 if payment == "Credit card (automatic)" else 0,
        "high_monthly_charge": 1 if monthly > 80 else 0,
        "avg_charge_per_month": monthly
    }
