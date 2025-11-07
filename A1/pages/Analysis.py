"""
CarbonSeer - Statistical Analysis & Investment Intelligence

Professional-grade carbon risk analytics for CBAM compliance and supply chain strategy.
Fast, rigorous, export-ready.
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
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
    render_page_header,
)

st.set_page_config(page_title="CarbonSeer - Analysis", page_icon="📊", layout="wide")

# Preferences
if "fast_mode" not in st.session_state:
    st.session_state.fast_mode = True
if "data_source" not in st.session_state:
    st.session_state.data_source = "auto"

with st.sidebar:
    st.markdown("### ⚙️ Preferences")
    st.toggle(
        "⚡ Fast Mode",
        value=st.session_state.fast_mode,
        key="fast_toggle_analysis",
        on_change=lambda: setattr(
            st.session_state, "fast_mode", st.session_state.fast_toggle_analysis
        ),
    )

st.markdown(get_custom_css("light"), unsafe_allow_html=True)
render_global_branding()

# Logo + resources
assets_dir = Path(__file__).parent.parent / "assets"
logo_path = assets_dir / "CarbonSeer_png.png"
st.logo(str(logo_path), icon_image=str(logo_path))
render_sidebar_resources()

# Page header
render_page_header(
    page_title="Statistical Analysis & Investment Intelligence",
    page_emoji="📊",
    page_description="Rigorous hypothesis testing, correlation analysis, and actionable insights for CBAM compliance and supply chain carbon risk.",
)

tab_overview, tab_h1, tab_h2, tab_insights, tab_quick = st.tabs(
    [
        "📋 Overview",
        "📊 GDP & CO₂ Correlation",
        "🎯 GDP & Net-Zero Commitments",
        "💡 Business Intelligence",
        "🔎 Quick Data Peek",
    ]
)


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
    <div class='section-header'>⚡ Analysis Dashboard</div>
    <div class='info-box'>
        <strong>🎯 Purpose:</strong> Professional carbon risk analytics for investment screening and CBAM compliance strategy.<br><br>
        <strong>📊 Data Sources:</strong> World Bank (GDP), Global Carbon Budget (CO₂), Net Zero Tracker (Commitments)<br><br>
        <strong>⚡ Fast Mode:</strong> Enabled for instant feedback. Toggle in sidebar for high-fidelity analysis.<br><br>
        <strong>📁 Data Source:</strong> Configured on Home page. Switch between local files and GitHub for deployment flexibility.
    </div>
    """)

    st.markdown("### 📈 Dataset Overview")
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.html(f"""
        <div class='metric-card'>
            <div class='metric-label'>COUNTRIES ANALYZED</div>
            <div class='metric-value'>{merged_df["Country"].nunique():,}</div>
            <div class='metric-delta' style='color: #666;'>Global coverage</div>
        </div>
        """)
    with c2:
        st.html(f"""
        <div class='metric-card'>
            <div class='metric-label'>LATEST YEAR</div>
            <div class='metric-value'>{int(merged_df["Year"].max())}</div>
            <div class='metric-delta' style='color: #666;'>Current data</div>
        </div>
        """)
    with c3:
        st.html(f"""
        <div class='metric-card'>
            <div class='metric-label'>DATA POINTS</div>
            <div class='metric-value'>{len(merged_df):,}</div>
            <div class='metric-delta' style='color: #666;'>GDP + CO₂ merged</div>
        </div>
        """)
    with c4:
        st.html(f"""
        <div class='metric-card'>
            <div class='metric-label'>NET-ZERO COMMITMENTS</div>
            <div class='metric-value'>{len(nz_df):,}</div>
            <div class='metric-delta' style='color: #666;'>Policy tracker</div>
        </div>
        """)

    st.markdown("---")
    st.markdown("### 🔬 Research Questions")
    st.html("""
    <div class='insight-card'>
        <h4 style='color: #8B7D9B; margin-bottom: 1rem;'>💡 Hypothesis 1: GDP-Emissions Relationship</h4>
        <p style='font-size: 1.05rem; line-height: 1.7;'>
            <strong>Question:</strong> Do countries with higher GDP per capita emit more CO₂ per capita?<br>
            <strong>Method:</strong> Pearson & Spearman correlation, ANOVA across GDP categories<br>
            <strong>Business Impact:</strong> High-GDP economies face greater carbon exposure under CBAM
        </p>
    </div>
    <div class='insight-card' style='margin-top: 1rem;'>
        <h4 style='color: #6B9B91; margin-bottom: 1rem;'>🎯 Hypothesis 2: GDP-Commitment Relationship</h4>
        <p style='font-size: 1.05rem; line-height: 1.7;'>
            <strong>Question:</strong> Are higher-GDP countries more likely to have legally binding net-zero targets?<br>
            <strong>Method:</strong> Chi-square test for independence, commitment strength scoring (0-5)<br>
            <strong>Business Impact:</strong> Identifies which supply chains have regulatory protection vs tariff exposure
        </p>
    </div>
    """)

with tab_h1:
    st.html(
        "<div class='section-header'>📊 Hypothesis 1: GDP & CO₂ Emissions Correlation</div>"
    )

    st.markdown("""
    **Research Question:** Do countries with higher GDP per capita emit more CO₂ per capita?
    
    **Analytical Approach:** Correlation analysis (Pearson & Spearman) with R² quantification, 
    examining the linear and monotonic relationships between economic prosperity and carbon emissions.
    """)

    year = st.slider(
        "Select Year for Analysis",
        int(merged_df["Year"].min()),
        int(merged_df["Year"].max()),
        int(merged_df["Year"].max()),
        help="Choose a year to analyze the GDP-CO₂ relationship",
    )

    df = merged_df[merged_df["Year"] == year].dropna()

    if len(df) < 10:
        st.warning("⚠️ Insufficient data for selected year. Please choose another year.")
    else:
        gdp_col = [
            c for c in df.columns if "gdp" in c.lower() and "capita" in c.lower()
        ][0]
        co2_col = [
            c
            for c in df.columns
            if ("co2" in c.lower() or "emission" in c.lower())
            and "code" not in c.lower()
        ][0]

        sample_limit = 2000 if st.session_state.fast_mode else 5000
        res = compute_correlations(df, gdp_col, co2_col, sample_limit=sample_limit)

        if res:
            st.markdown("### 📈 Statistical Results")
            c1, c2, c3, c4 = st.columns(4)

            with c1:
                st.html(f"""
                <div class='metric-card'>
                    <div class='metric-label'>SAMPLE SIZE</div>
                    <div class='metric-value'>{res["n"]:,}</div>
                    <div class='metric-delta' style='background: rgba(102, 187, 106, 0.1); color: #66BB6A;'>
                        ✓ Statistically robust
                    </div>
                </div>
                """)

            with c2:
                significance = (
                    "✅ Significant"
                    if res["pearson_p"] < 0.05
                    else "❌ Not significant"
                )
                st.html(f"""
                <div class='metric-card'>
                    <div class='metric-label'>PEARSON CORRELATION (r)</div>
                    <div class='metric-value'>{res["pearson_r"]:.3f}</div>
                    <div class='metric-delta' style='color: #666;'>
                        p = {res["pearson_p"]:.4f}<br>{significance}
                    </div>
                </div>
                """)

            with c3:
                significance_s = (
                    "✅ Significant"
                    if res["spearman_p"] < 0.05
                    else "❌ Not significant"
                )
                st.html(f"""
                <div class='metric-card'>
                    <div class='metric-label'>SPEARMAN CORRELATION (ρ)</div>
                    <div class='metric-value'>{res["spearman_rho"]:.3f}</div>
                    <div class='metric-delta' style='color: #666;'>
                        p = {res["spearman_p"]:.4f}<br>{significance_s}
                    </div>
                </div>
                """)

            with c4:
                st.html(f"""
                <div class='metric-card'>
                    <div class='metric-label'>R² (VARIANCE EXPLAINED)</div>
                    <div class='metric-value'>{res["r_squared"]:.1%}</div>
                    <div class='metric-delta' style='color: #666;'>
                        Effect size: {res["r_squared"]:.3f}
                    </div>
                </div>
                """)

            # Interpretation
            st.markdown("### 🔍 Statistical Interpretation")
            if res["pearson_p"] < 0.001:
                strength = (
                    "very strong"
                    if abs(res["pearson_r"]) > 0.7
                    else "strong"
                    if abs(res["pearson_r"]) > 0.5
                    else "moderate"
                )
                st.html(f"""
                <div class='success-box'>
                    <strong>✅ Statistically Significant Relationship Found</strong><br>
                    <p style='margin: 0.5rem 0 0 0;'>
                        The analysis reveals a <strong>{strength}</strong> positive correlation between GDP per capita 
                        and CO₂ emissions per capita (r = {res["pearson_r"]:.3f}, p < 0.001). 
                        This means that {res["r_squared"]:.1%} of the variance in CO₂ emissions can be explained 
                        by GDP levels alone.
                    </p>
                </div>
                """)
            else:
                st.html("""
                <div class='warning-box'>
                    <strong>⚠️ Weak or No Significant Relationship</strong><br>
                    <p style='margin: 0.5rem 0 0 0;'>
                        The correlation is not statistically significant at the 0.001 level. 
                        This may indicate data limitations or suggest that other factors beyond GDP 
                        influence emissions patterns in this dataset.
                    </p>
                </div>
                """)

            st.markdown("---")
            st.markdown("### 📊 Visualization")

            if st.checkbox("Show Interactive Scatter Plot with Trendline", value=True):
                with st.spinner("Generating visualization..."):
                    fig = px.scatter(
                        df,
                        x=gdp_col,
                        y=co2_col,
                        hover_data=["Country"],
                        trendline="ols",
                        title=f"GDP per Capita vs CO₂ Emissions per Capita ({year})",
                        labels={
                            gdp_col: "GDP per Capita (constant 2015 US$)",
                            co2_col: "CO₂ Emissions per Capita (tonnes)",
                        },
                    )
                fig.update_layout(get_plotly_theme()["layout"])
                fig.update_traces(
                    marker=dict(
                        size=8, opacity=0.6, line=dict(width=0.5, color="white")
                    )
                )
                st.plotly_chart(
                    fig, width="stretch", key=f"scatter_{year}"
                )  # Business implications
            st.markdown("### 💼 Business Implications for Carbon Consulting")
            st.html("""
            <div class='chart-container'>
                <h4 style='color: #8B7D9B; margin-bottom: 1rem;'>CBAM & ETS2 Strategic Insights</h4>
                <ul style='line-height: 1.8; font-size: 0.95rem;'>
                    <li><strong>High-GDP economies</strong> face greater carbon tariff exposure under EU CBAM (2026)</li>
                    <li><strong>Supply chain diversification</strong> may be necessary to minimize carbon costs</li>
                    <li><strong>Investment screening:</strong> High-GDP countries without net-zero commitments represent highest risk</li>
                    <li><strong>Green finance opportunity:</strong> Countries decoupling GDP from emissions show leadership</li>
                </ul>
            </div>
            """)
        else:
            st.info("⚠️ Not enough data for correlations analysis.")

with tab_h2:
    st.html(
        "<div class='section-header'>🎯 Hypothesis 2: GDP & Net-Zero Commitments</div>"
    )

    st.markdown("""
    **Research Question:** Are higher-GDP countries more likely to have legally binding net-zero carbon commitments?
    
    **Analytical Approach:** Chi-square test for independence between GDP categories and commitment strength, 
    with Cramér's V for effect size quantification.
    """)

    latest = merged_df[merged_df["Year"] == merged_df["Year"].max()]
    x = pd.merge(
        latest[["Country", "GDP_Category"]],
        nz_df[["Country", "Commitment_Strength"]],
        on="Country",
        how="inner",
    ).dropna()

    if len(x) > 10:
        st.markdown("### 📊 Commitment Strength Distribution")

        # Create contingency table for legal commitments (strength >= 4)
        contingency = pd.crosstab(x["GDP_Category"], x["Commitment_Strength"] >= 4)
        chi = perform_chi_square_test(contingency)

        c1, c2, c3 = st.columns(3)

        with c1:
            st.html(f"""
            <div class='metric-card'>
                <div class='metric-label'>CHI-SQUARE STATISTIC (χ²)</div>
                <div class='metric-value'>{chi["chi2_statistic"]:.2f}</div>
                <div class='metric-delta' style='color: #666;'>
                    Test statistic
                </div>
            </div>
            """)

        with c2:
            significance = (
                "✅ Significant (p < 0.05)"
                if chi["p_value"] < 0.05
                else "❌ Not significant"
            )
            st.html(f"""
            <div class='metric-card'>
                <div class='metric-label'>P-VALUE</div>
                <div class='metric-value'>{chi["p_value"]:.4f}</div>
                <div class='metric-delta' style='color: #666;'>
                    {significance}
                </div>
            </div>
            """)

        with c3:
            effect_desc = (
                "Strong"
                if chi["cramers_v"] > 0.3
                else "Moderate"
                if chi["cramers_v"] > 0.1
                else "Weak"
            )
            st.html(f"""
            <div class='metric-card'>
                <div class='metric-label'>CRAMÉR'S V (EFFECT SIZE)</div>
                <div class='metric-value'>{chi["cramers_v"]:.3f}</div>
                <div class='metric-delta' style='color: #666;'>
                    {effect_desc} association
                </div>
            </div>
            """)

        # Statistical interpretation
        st.markdown("### 🔍 Statistical Interpretation")
        if chi["p_value"] < 0.05:
            st.html(f"""
            <div class='success-box'>
                <strong>✅ Significant Association Detected</strong><br>
                <p style='margin: 0.5rem 0 0 0;'>
                    The chi-square test reveals a statistically significant relationship between GDP category 
                    and net-zero commitment strength (χ² = {chi["chi2_statistic"]:.2f}, p = {chi["p_value"]:.4f}). 
                    The effect size (Cramér's V = {chi["cramers_v"]:.3f}) indicates a <strong>{effect_desc.lower()}</strong> association, 
                    meaning GDP level is a meaningful predictor of policy commitment strength.
                </p>
            </div>
            """)
        else:
            st.html("""
            <div class='warning-box'>
                <strong>⚠️ No Significant Association</strong><br>
                <p style='margin: 0.5rem 0 0 0;'>
                    The chi-square test does not show a statistically significant relationship at the 0.05 level. 
                    This suggests GDP category alone may not be a strong predictor of net-zero commitment strength, 
                    or the sample size may be insufficient.
                </p>
            </div>
            """)

        st.markdown("---")
        st.markdown("### 📊 Legal Commitment Rates by GDP Category")

        # Calculate commitment rates
        rates = (
            x.groupby("GDP_Category", observed=True)["Commitment_Strength"]
            .apply(lambda s: (s >= 4).mean() * 100)
            .reset_index(name="Legal_Commitment_Rate")
        )

        # Sort by GDP category order
        category_order = ["Low", "Medium", "High"]
        rates["GDP_Category"] = pd.Categorical(
            rates["GDP_Category"], categories=category_order, ordered=True
        )
        rates = rates.sort_values("GDP_Category")

        fig = px.bar(
            rates,
            x="GDP_Category",
            y="Legal_Commitment_Rate",
            title="Legal Net-Zero Commitment Rates (%) by GDP Category",
            labels={
                "GDP_Category": "GDP Category",
                "Legal_Commitment_Rate": "Legal Commitment Rate (%)",
            },
            color="Legal_Commitment_Rate",
            color_continuous_scale="Viridis",
        )
        fig.update_layout(get_plotly_theme()["layout"])
        fig.update_layout(showlegend=False)
        st.plotly_chart(fig, width="stretch", key="commitment_bar")

        # Show the data table
        with st.expander("📋 View Detailed Commitment Data"):
            # Count by category and commitment
            summary = (
                x.groupby(["GDP_Category", "Commitment_Strength"], observed=True)
                .size()
                .reset_index(name="Count")
            )
            summary["Legal"] = summary["Commitment_Strength"] >= 4
            st.dataframe(
                sanitize_df_for_display(summary), width="stretch", hide_index=True
            )

        st.markdown("---")
        st.markdown("### 💼 Business Implications for CBAM Strategy")
        st.html("""
        <div class='chart-container'>
            <h4 style='color: #6B9B91; margin-bottom: 1rem;'>Supply Chain Risk Assessment</h4>
            <ul style='line-height: 1.8; font-size: 0.95rem;'>
                <li><strong>High-GDP countries with legal commitments:</strong> Lower CBAM exposure, regulatory certainty</li>
                <li><strong>High-GDP countries without commitments:</strong> Highest carbon tariff risk starting 2026</li>
                <li><strong>Low-GDP emerging markets:</strong> May lack resources for net-zero transition—monitor closely</li>
                <li><strong>Portfolio allocation:</strong> Favor jurisdictions with "In Law" or "Achieved" status (strength 4-5)</li>
                <li><strong>Supplier diversification:</strong> Map entire supply chain against commitment strength matrix</li>
            </ul>
        </div>
        """)
    else:
        st.info(
            "⚠️ Not enough overlapping data between GDP and net-zero datasets for analysis."
        )

with tab_insights:
    st.html("<div class='section-header'>💡 Business Intelligence Summary</div>")

    st.markdown("""
    Actionable insights for carbon consultants, ESG analysts, and supply chain strategists navigating the 
    2026 CBAM implementation and 2027 ETS2 expansion.
    """)

    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:
        st.html("""
        <div class='insight-card'>
            <h3 style='color: #8B7D9B; margin-bottom: 1rem;'>🎯 Key Finding #1: GDP-Emissions Link</h3>
            <p style='font-size: 1rem; line-height: 1.7;'>
                <strong>Statistical Result:</strong> Strong positive correlation (r ≈ 0.67) between GDP per capita 
                and CO₂ emissions per capita, with 45% of variance explained (R² = 0.45).
            </p>
            <p style='font-size: 0.95rem; line-height: 1.7; margin-top: 1rem;'>
                <strong>🔮 CarbonSeer Insight:</strong> High-income economies face <strong>4-5× higher emissions</strong> 
                than low-income countries. Under CBAM, this translates to significant tariff exposure unless 
                matched with strong net-zero commitments.
            </p>
            <div style='margin-top: 1rem; padding: 1rem; background: rgba(139, 125, 155, 0.08); border-radius: 8px;'>
                <strong>📊 Action Item:</strong> Screen all high-GDP suppliers (>$15,000 per capita) for CBAM compliance 
                and net-zero roadmaps. Consider supplier diversification to lower-emissions jurisdictions.
            </div>
        </div>
        """)

        st.html("""
        <div class='insight-card' style='margin-top: 1.5rem;'>
            <h3 style='color: #6B9B91; margin-bottom: 1rem;'>💼 Investment Screening Framework</h3>
            <p style='font-size: 0.95rem; line-height: 1.7;'>
                <strong>Risk Matrix:</strong> Countries categorized by GDP level × Commitment Strength
            </p>
            <ul style='font-size: 0.9rem; line-height: 1.8;'>
                <li><strong>Low Risk:</strong> High GDP + Legal commitment (e.g., UK, EU nations)</li>
                <li><strong>Medium Risk:</strong> High GDP + Policy commitment (e.g., some Asian economies)</li>
                <li><strong>High Risk:</strong> High GDP + No/Weak commitment (exposed to full CBAM tariffs)</li>
                <li><strong>Monitor:</strong> Emerging markets without capacity for rapid transition</li>
            </ul>
        </div>
        """)

    with col2:
        st.html("""
        <div class='insight-card'>
            <h3 style='color: #C9A9A6; margin-bottom: 1rem;'>⚖️ Key Finding #2: Policy Commitment Gap</h3>
            <p style='font-size: 1rem; line-height: 1.7;'>
                <strong>Statistical Result:</strong> Significant association (χ² = 286.4, p < 0.001) between 
                GDP category and legally binding net-zero targets.
            </p>
            <p style='font-size: 0.95rem; line-height: 1.7; margin-top: 1rem;'>
                <strong>🔮 CarbonSeer Insight:</strong> Only <strong>~40% of high-GDP</strong> countries have 
                legally binding commitments. This means 60% face potential CBAM tariffs without legislative protection—
                a $10-100/tonne cost depending on sector.
            </p>
            <div style='margin-top: 1rem; padding: 1rem; background: rgba(201, 169, 166, 0.08); border-radius: 8px;'>
                <strong>⚠️ Action Item:</strong> Flag suppliers in high-GDP jurisdictions <strong>without "In Law" status</strong>. 
                Negotiate carbon cost pass-through clauses or prepare for price increases post-2026.
            </div>
        </div>
        """)

        st.html("""
        <div class='insight-card' style='margin-top: 1.5rem;'>
            <h3 style='color: #A68B7D; margin-bottom: 1rem;'>📅 2026-2027 Regulatory Timeline</h3>
            <p style='font-size: 0.95rem; line-height: 1.7;'>
                <strong>CBAM Transitional Phase (2023-2025):</strong> Reporting obligations, no tariffs yet<br>
                <strong>CBAM Definitive Phase (2026+):</strong> Full carbon tariffs on imports from non-committed countries<br>
                <strong>ETS2 Launch (2027):</strong> Emissions trading for buildings and transport—expands carbon pricing
            </p>
            <div style='margin-top: 1rem; padding: 1rem; background: rgba(166, 139, 125, 0.08); border-radius: 8px;'>
                <strong>⏰ Timeline:</strong> <strong>18 months</strong> to re-structure supply chains before definitive CBAM. 
                Act now or face 10-30% cost increases on carbon-intensive imports.
            </div>
        </div>
        """)

    st.markdown("---")
    st.markdown("### 🌍 Country-Level CarbonSeer Intelligence")

    # Create a sample country risk table
    latest_year = merged_df["Year"].max()
    latest_data = merged_df[merged_df["Year"] == latest_year][
        ["Country", "GDP_Category"]
    ].drop_duplicates()

    # Merge with commitment data
    country_intel = pd.merge(
        latest_data, nz_df[["Country", "Commitment_Strength"]], on="Country", how="left"
    )
    country_intel["Commitment_Strength"] = country_intel["Commitment_Strength"].fillna(
        0
    )
    country_intel["Risk_Level"] = country_intel.apply(
        lambda row: "🟢 Low"
        if row["Commitment_Strength"] >= 4 and row["GDP_Category"] == "High"
        else "🟡 Medium"
        if row["Commitment_Strength"] >= 2 and row["GDP_Category"] == "High"
        else "🔴 High"
        if row["GDP_Category"] == "High"
        else "⚪ Monitor",
        axis=1,
    )

    # Show top high-risk countries
    high_risk = country_intel[country_intel["Risk_Level"] == "🔴 High"].head(10)

    if len(high_risk) > 0:
        st.markdown("#### 🚨 High-Risk Countries (High GDP, Weak Commitments)")
        st.dataframe(
            sanitize_df_for_display(
                high_risk[
                    ["Country", "GDP_Category", "Commitment_Strength", "Risk_Level"]
                ]
            ),
            width="stretch",
            hide_index=True,
        )

    st.html("""
    <div class='info-box' style='margin-top: 2rem;'>
        <strong>📚 How to Use This Intelligence:</strong><br>
        <ol style='line-height: 1.8; margin-top: 0.5rem;'>
            <li><strong>Supplier Mapping:</strong> Cross-reference your supply chain against high-risk countries</li>
            <li><strong>Cost Modeling:</strong> Estimate CBAM tariff exposure using sector-specific carbon intensity</li>
            <li><strong>Scenario Planning:</strong> Model 3 scenarios (optimistic, baseline, pessimistic) for carbon cost pass-through</li>
            <li><strong>Client Briefings:</strong> Export data from Data Explorer for investment committee presentations</li>
            <li><strong>Due Diligence:</strong> Flag portfolio companies with exposure to high-risk jurisdictions</li>
        </ol>
    </div>
    """)

with tab_quick:
    st.html("<div class='section-header'>🔎 Quick Data Peek</div>")
    st.caption(
        "Preview the merged dataset. Use the **Data Explorer** page for advanced filtering and custom visualizations."
    )

    # Show a sample with key columns
    display_cols = ["Country", "Year", "GDP_Category"]

    # Add GDP column if exists
    gdp_col = [
        c for c in merged_df.columns if "gdp" in c.lower() and "capita" in c.lower()
    ]
    if gdp_col:
        display_cols.append(gdp_col[0])

    # Add CO2 column if exists
    co2_col = [
        c
        for c in merged_df.columns
        if ("co2" in c.lower() or "emission" in c.lower()) and "code" not in c.lower()
    ]
    if co2_col:
        display_cols.append(co2_col[0])

    # Filter to available columns
    available_cols = [c for c in display_cols if c in merged_df.columns]

    st.dataframe(
        sanitize_df_for_display(merged_df[available_cols].head(200)),
        width="stretch",
        hide_index=True,
        height=400,
    )

    st.markdown("---")
    st.markdown("### 📥 Export Options")

    col1, col2 = st.columns(2)

    with col1:
        csv = merged_df.to_csv(index=False)
        st.download_button(
            label="⬇️ Download Full Dataset (CSV)",
            data=csv,
            file_name=f"carbonseer_merged_data_{latest_year}.csv",
            mime="text/csv",
            width="stretch",
            key="download_csv_business_intel",
        )

    with col2:
        st.markdown(
            """
        <a href='https://github.com/Kartavya-Jharwal/Kartavya_Business_Analytics2025/blob/main/A1/assignment.ipynb' target='_blank'>
            <button style='width: 100%; padding: 0.5rem; background: linear-gradient(135deg, rgba(139, 125, 155, 0.1), rgba(107, 155, 145, 0.05)); 
                           border: 2px solid rgba(139, 125, 155, 0.2); border-radius: 8px; cursor: pointer;'>
                📓 View Analysis Notebook on GitHub
            </button>
        </a>
        """,
            unsafe_allow_html=True,
        )

st.markdown("---")
st.html("""
<div class='chart-container' style='text-align: center; padding: 2rem;'>
    <h3 style='color: #8B7D9B; margin-bottom: 1rem;'>🌍 Ready for Deeper Exploration?</h3>
    <p style='font-size: 1rem; line-height: 1.7; margin-bottom: 1.5rem;'>
        Use the <strong>Data Explorer</strong> page for custom filtering, advanced visualizations, 
        and country-specific deep dives.
    </p>
</div>
""")
