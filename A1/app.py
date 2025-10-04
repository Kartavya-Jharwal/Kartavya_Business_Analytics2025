"""
Business Analytics A1 - Interactive Dashboard
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from scipy import stats

from utils import (
    load_gdp_data,
    load_co2_data,
    load_netzero_data,
    merge_gdp_co2,
    create_gdp_categories,
    create_commitment_strength,
    get_custom_css,
    get_plotly_theme,
)

st.set_page_config(
    page_title="Climate Analytics Dashboard", page_icon="🌍", layout="wide"
)

st.markdown(get_custom_css(), unsafe_allow_html=True)


@st.cache_data
def load_all_data():
    gdp_df = load_gdp_data()
    co2_df = load_co2_data()
    netzero_df = load_netzero_data()
    merged_df = merge_gdp_co2(gdp_df, co2_df)
    merged_df = create_gdp_categories(merged_df)
    netzero_df = create_commitment_strength(netzero_df)
    return gdp_df, co2_df, netzero_df, merged_df


st.title("🌍 Climate & Economics Analytics")
st.markdown(
    "An interactive exploration of GDP, CO2 emissions, and net-zero commitments"
)

with st.spinner("Loading data..."):
    gdp_df, co2_df, netzero_df, merged_df = load_all_data()

st.success(f"Loaded data for {len(merged_df['Country'].unique())} countries")

latest_year = merged_df["Year"].max()
latest_data = merged_df[merged_df["Year"] == latest_year]

# Use actual column names from CSV files
gdp_col = "GDP per capita (constant 2015 US$)"
co2_col = "Annual CO₂ emissions (per capita)"

col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Countries", len(latest_data))
with col2:
    st.metric("Avg GDP", f"${latest_data[gdp_col].mean():.0f}")
with col3:
    st.metric("Avg CO2", f"{latest_data[co2_col].mean():.2f}t")

st.markdown("## 📊 Key Insights")
st.info(
    "This dashboard is currently under development. Navigate to pages in the sidebar for detailed analysis."
)
