"""
CarbonSeer - Statistical Analysis & Investment Intelligence (Turbo)

Lean, fast analysis tabs with GitHub-raw data loading.
"""

import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

from utils import (
    load_gdp_data,
    load_co2_data,
    load_netzero_data,
    merge_gdp_co2,
    create_gdp_categories,
    create_commitment_strength,
    get_custom_css,
    get_plotly_theme,
    render_sidebar_resources,
)
from utils.analysis import (
    compute_correlations,
    perform_chi_square_test,
)
from utils.styling import (
    render_global_branding,
    sanitize_df_for_display,
)

st.set_page_config(page_title="CarbonSeer - Analysis", page_icon="📊", layout="wide")

# Preferences
if "fast_mode" not in st.session_state:
    st.session_state.fast_mode = True
if "data_source" not in st.session_state:
    st.session_state.data_source = "auto"

with st.sidebar:
    st.markdown("### ⚙️ Preferences")
    st.toggle("⚡ Fast Mode", value=st.session_state.fast_mode, key="fast_toggle_analysis",
             on_change=lambda: setattr(st.session_state, 'fast_mode', st.session_state.fast_toggle_analysis))

st.markdown(get_custom_css("light"), unsafe_allow_html=True)
render_global_branding()

# Logo + resources
assets_dir = Path(__file__).parent.parent / "assets"
logo_path = assets_dir / "CarbonSeer_png.png"
st.logo(str(logo_path), icon_image=str(logo_path))
render_sidebar_resources()

tab_overview, tab_h1, tab_h2, tab_quick = st.tabs(["📋 Overview", "📊 GDP & CO₂", "🎯 GDP & Net-Zero", "🔎 Quick Peek"]) 

@st.cache_data
def load_data_fast(source: str = "auto"):
    gdp = load_gdp_data(source)
    co2 = load_co2_data(source)
    nz = load_netzero_data(source)
    merged = merge_gdp_co2(gdp, co2)
    merged = create_gdp_categories(merged)
    nz = create_commitment_strength(nz)
    return gdp, co2, nz, merged

with st.spinner("Loading data…"):
    gdp_df, co2_df, nz_df, merged_df = load_data_fast(st.session_state.data_source)

with tab_overview:
    st.html("""
    <div class='section-header'>⚡ Turbo Overview</div>
    <div class='info-box'>GitHub raw data loading enabled. Toggle Fast Mode for snappier charts; switch data source in Home.</div>
    """)
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.metric("Countries", f"{merged_df['Country'].nunique():,}")
    with c2:
        st.metric("Latest Year", int(merged_df['Year'].max()))
    with c3:
        st.metric("Rows (merged)", f"{len(merged_df):,}")
    with c4:
        st.metric("Net-Zero records", f"{len(nz_df):,}")

with tab_h1:
    year = st.slider("Year", int(merged_df["Year"].min()), int(merged_df["Year"].max()), int(merged_df["Year"].max()))
    df = merged_df[merged_df["Year"] == year].dropna()
    gdp_col = [c for c in df.columns if "gdp" in c.lower() and "capita" in c.lower()][0]
    co2_col = [c for c in df.columns if ("co2" in c.lower() or "emission" in c.lower()) and "code" not in c.lower()][0]
    sample_limit = 2000 if st.session_state.fast_mode else 5000
    res = compute_correlations(df, gdp_col, co2_col, sample_limit=sample_limit)
    if res:
        c1, c2, c3, c4 = st.columns(4)
        c1.metric("n", res["n"]) 
        c2.metric("Pearson r", f"{res['pearson_r']:.3f}") 
        c3.metric("Spearman ρ", f"{res['spearman_rho']:.3f}") 
        c4.metric("R²", f"{res['r_squared']:.3f}")
        if st.checkbox("Show scatter (trendline)", value=not st.session_state.fast_mode):
            fig = px.scatter(df, x=gdp_col, y=co2_col, trendline="ols", title=f"GDP vs CO₂ ({year})")
            fig.update_layout(template=get_plotly_theme())
            st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("Not enough data for correlations.")

with tab_h2:
    latest = merged_df[merged_df["Year"] == merged_df["Year"].max()]
    x = pd.merge(latest[["Country", "GDP_Category"]], nz_df[["Country", "Commitment_Strength"]], on="Country", how="inner").dropna()
    if len(x) > 10:
        contingency = pd.crosstab(x["GDP_Category"], x["Commitment_Strength"] >= 4)
        chi = perform_chi_square_test(contingency)
        c1, c2, c3 = st.columns(3)
        c1.metric("Chi-square", f"{chi['chi2_statistic']:.2f}")
        c2.metric("p-value", f"{chi['p_value']:.4f}")
        c3.metric("Cramér's V", f"{chi['cramers_v']:.3f}")
        rates = x.groupby("GDP_Category")["Commitment_Strength"].apply(lambda s: (s >= 4).mean()*100).reset_index(name="Legal_Commitment_Rate")
        fig = px.bar(rates, x="GDP_Category", y="Legal_Commitment_Rate", title="Legal Commitment Rates (%) by GDP Category")
        fig.update_layout(template=get_plotly_theme())
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("Not enough data.")

with tab_quick:
    st.caption("Quick peek – use the full Data Explorer page for advanced views.")
    st.dataframe(sanitize_df_for_display(merged_df.head(200)), use_container_width=True, hide_index=True)

st.markdown("---")
st.markdown("[📓 Open legacy notebook](https://github.com/Kartavya-Jharwal/Kartavya_Business_Analytics2025/blob/main/A1/assignment.ipynb)")
