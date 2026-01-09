import streamlit as st
from ..config import DISCLAIMER

def render_footer():
    st.divider()
    st.caption(DISCLAIMER)
