import streamlit as st

def render_insights(prob):
    st.subheader("Suggested Business Actions")

    if prob > 0.6:
        st.markdown("""
        - Offer pricing incentives
        - Promote long-term contracts
        - Proactive customer outreach
        """)
    else:
        st.markdown("""
        - Maintain service quality
        - Upsell bundled services
        - Encourage referrals
        """)
