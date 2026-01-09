import streamlit as st

def render_prediction(prediction, prob):
    st.subheader("Prediction Result")

    if prob < 0.10:
        st.success(f"🟢 Low Churn Risk ({prob:.2%})")
        st.caption("Customer shows strong retention signals.")

    elif prob < 0.18:
        st.warning(f"🟡 Medium Churn Risk ({prob:.2%})")
        st.caption("Customer shows early signs of churn. Monitoring recommended.")

    else:
        st.error(f"🔴 High Priority Churn Risk ({prob:.2%})")
        st.caption("Customer requires proactive retention action.")
