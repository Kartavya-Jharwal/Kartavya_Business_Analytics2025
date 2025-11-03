"""
CarbonSeer - Carbon Risk Analytics Platform
Entry point for the Streamlit multi-page application
"""
import streamlit as st

st.set_page_config(
    page_title="CarbonSeer | Carbon Risk Analytics",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ===== NAVIGATION =====
home_page = st.Page("Home.py", title="Home", icon="🏠")
analysis_page = st.Page("pages/Analysis.py", title="Analysis", icon="📊")
explorer_page = st.Page("pages/Data_Explorer.py", title="Data Explorer", icon="🔍")

pg = st.navigation([home_page, analysis_page, explorer_page])
pg.run()
