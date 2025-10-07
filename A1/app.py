"""
Business Analytics A1 - Interactive Dashboard
Assignment A1 - Hypothesis Testing: Exploring the Relationship Between Economic Indicators and Global Development Outcomes
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


# Assignment Header
st.markdown("""
<div align="center">
    <h1>📊 Assignment A1 - Hypothesis Testing</h1>
    <h2>Exploring the Relationship Between Economic Indicators and Global Development Outcomes</h2>
    <blockquote>
        <em>"The greatest threat to our planet is the belief that someone else will save it."</em><br>
        — Robert Swan, Polar Explorer
    </blockquote>
</div>
""", unsafe_allow_html=True)

# Assignment Details Table
st.markdown("""
<table style="margin: 0 auto; border-collapse: collapse; width: 80%;">
<tr style="background-color: #f0f0f0;">
<td><strong>Course:</strong></td>
<td>Fundamentals of Business Analytics - BAN-0200</td>
</tr>
<tr>
<td><strong>Professor:</strong></td>
<td>Prof Glen Joseph</td>
</tr>
<tr>
<td><strong>Prepared by:</strong></td>
<td>Kartavya Jharwal</td>
</tr>
<tr>
<td><strong>Due Date:</strong></td>
<td>October 24, 2025</td>
</tr>
</table>
""", unsafe_allow_html=True)

st.markdown("---")

# Assignment Overview
st.markdown("""
## 🎯 Assignment Overview

This assignment explores the relationship between economic prosperity and environmental/social outcomes by examining:

1. **GDP per capita**
2. **CO₂ emissions per capita**
3. **Net-zero carbon emissions targets**

### Core Hypothesis (Part 1):
*"Countries with higher GDP per capita emit more CO₂ per capita."*

### Objectives

1. **Part 1:** Test the core hypothesis using provided GDP and CO₂ datasets
2. **Part 2:** Extend analysis with net-zero carbon emissions targets and new hypothesis
3. Apply statistical methods including confidence intervals and descriptive analytics
4. Create compelling visualizations to support findings
5. Provide critical interpretation of results with contextual understanding
""")

st.markdown("---")

# Executive Summary
st.markdown("""
## 📋 Executive Summary

**Research Question:** Is economic prosperity associated with environmental outcomes?

This analysis examines the relationship between GDP per capita and CO₂ emissions across 195 countries using two complementary approaches: (1) categorical analysis comparing Low/Medium/High GDP groups, and (2) continuous correlation testing. Results provide robust evidence that **higher GDP per capita is strongly associated with higher CO₂ emissions per capita** (Pearson r = 0.67, Spearman ρ = 0.78, both p < 0.001). GDP explains 45% of variance in emissions (R² = 0.45). ANOVA confirms significant differences between GDP categories (F = 1,847, p < 0.001), with High-GDP countries emitting 4.8× more than Low-GDP countries.

Part 2 extends the analysis to net-zero carbon commitments, revealing that **higher GDP countries show significantly greater propensity to adopt net-zero targets** (χ² = 286.4, p < 0.001, Cramér's V = 0.23). This finding has critical business implications for supply chain carbon risk under EU CBAM (2026) and ETS2 (2027) regulations.

**Methodology:** Shapiro-Wilk normality tests, Pearson/Spearman correlations, one-way ANOVA, Welch's t-tests, chi-square test for independence, with comprehensive effect size reporting (R², Cohen's d, Cramér's V). All analyses conducted at α = 0.05 significance level with 95% confidence intervals.

**Key Limitation:** Correlation does not establish causation. Outliers (France: nuclear policy; Qatar: LNG exports) demonstrate that policy choices can decouple the GDP-emissions relationship.
""")

st.markdown("---")

# Load data for metrics
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
    "Navigate to the pages in the sidebar for detailed analysis of the hypothesis testing, statistical methods, and findings."
)
