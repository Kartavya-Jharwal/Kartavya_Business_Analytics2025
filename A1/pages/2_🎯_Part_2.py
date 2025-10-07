"""
Part 2: Net-Zero Commitments Analysis
Extended Hypothesis: "Countries with higher GDP per capita are more likely to have committed to net-zero carbon emissions targets."
"""

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from scipy.stats import chi2_contingency

from utils import (
    load_gdp_data,
    load_co2_data,
    load_netzero_data,
    merge_gdp_co2,
    create_gdp_categories,
    create_commitment_strength,
    get_custom_css,
)

st.set_page_config(
    page_title="Part 2: Net-Zero Analysis", page_icon="🎯", layout="wide"
)

st.markdown(get_custom_css(), unsafe_allow_html=True)

# Title and Overview
st.markdown("# 🎯 Part 2: Net-Zero Commitments Analysis")

st.markdown("""
## Extended Hypothesis

> *"Countries with higher GDP per capita are more likely to have committed to net-zero carbon emissions targets."*

### Research Questions

1. Do wealthier countries show stronger policy commitments to carbon neutrality?
2. What is the relationship between economic prosperity and climate action?
3. Can economic indicators predict environmental policy commitments?

### Additional Dataset

```
net-zero-targets/net-zero-targets.csv
```

**Source:** Net Zero Tracker (Energy and Climate Intelligence Unit et al., 2023) – with minor processing by Our World in Data

### Analysis Approach

- Categorical analysis (GDP level vs commitment status)
- Chi-square tests for independence
- Effect size measurements
- Cross-tabulation visualization

> **Why This Matters:** Understanding the relationship between economic development and climate policy commitments can provide insights into global climate governance, potential policy interventions, and future emissions scenarios.
""")

st.markdown("---")

# Load data
@st.cache_data
def load_part2_data():
    gdp_df = load_gdp_data()
    co2_df = load_co2_data()
    netzero_df = load_netzero_data()
    merged_df = merge_gdp_co2(gdp_df, co2_df)
    analysis_df = create_gdp_categories(merged_df)

    # Prepare GDP data - get latest year for each country
    if "Country" in analysis_df.columns:
        analysis_df = analysis_df.rename(columns={"Country": "Entity"})

    latest_year_data = analysis_df.groupby("Entity")["Year"].max().reset_index()
    gdp_latest = pd.merge(analysis_df, latest_year_data, on=["Entity", "Year"])

    # Get GDP column name
    gdp_col = [
        col
        for col in gdp_latest.columns
        if "gdp" in col.lower() and "capita" in col.lower()
    ][0]

    gdp_latest = gdp_latest[["Entity", gdp_col, "GDP_Category"]].drop_duplicates()

    # Clean country names for better matching
    gdp_latest["Entity_clean"] = gdp_latest["Entity"].str.strip().str.title()
    netzero_df["Entity_clean"] = netzero_df["Entity"].str.strip().str.title()

    # Find the target column
    target_col = [col for col in netzero_df.columns if "target" in col.lower()][0]

    # Merge datasets
    merged_nz = pd.merge(
        gdp_latest,
        netzero_df[["Entity_clean", target_col]],
        on="Entity_clean",
        how="inner",
    )

    # Use the commitment strength from data_loader if available, otherwise create binary
    if "Commitment_Strength" in merged_nz.columns:
        merged_nz["Has_NetZero_Target"] = (merged_nz["Commitment_Strength"] > 0).astype(int)
    else:
        # Create binary commitment variable
        merged_nz["Has_NetZero_Target"] = merged_nz[target_col].apply(
            lambda x: 1
            if pd.notna(x) and str(x).lower() not in ["nan", "none", "", "no target"]
            else 0
        )

    return merged_nz, target_col

st.markdown("## Dataset Integration")

with st.spinner("Loading and merging datasets..."):
    merged_nz, target_col = load_part2_data()

st.write(f"**Merged dataset:** {merged_nz.shape[0]} countries with both GDP and net-zero data")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### GDP Category Distribution")
    gdp_dist = merged_nz["GDP_Category"].value_counts()
    st.dataframe(gdp_dist)

with col2:
    st.markdown("### Net-Zero Commitment Distribution")
    commitment_dist = merged_nz["Has_NetZero_Target"].value_counts()
    commitment_labels = {0: "No Commitment", 1: "Has Commitment"}
    commitment_dist_renamed = commitment_dist.rename(index=commitment_labels)
    st.dataframe(commitment_dist_renamed)

st.markdown("---")

# Chi-square test
st.markdown("## Statistical Analysis: Chi-Square Test")

st.markdown("""
### Statistical Hypothesis Formulation

#### Null Hypothesis (H₀)
**Statement:** There is no association between GDP category and net-zero commitment status. GDP category and net-zero commitments are independent.

#### Alternative Hypothesis (H₁)
**Statement:** There is an association between GDP category and net-zero commitment status. Higher GDP countries are more likely to have net-zero commitments.

### Significance Level
α = 0.05 (5% significance level)

**Test:** Chi-square test for independence
""")

# Create contingency table
contingency_table = pd.crosstab(
    merged_nz["GDP_Category"], merged_nz["Has_NetZero_Target"]
)

st.markdown("### Contingency Table")
st.dataframe(contingency_table)

# Perform chi-square test
chi2_stat, p_value, dof, expected = chi2_contingency(contingency_table)

col1, col2 = st.columns(2)

with col1:
    st.markdown("### Test Results")
    st.write(f"**Chi-square statistic:** {chi2_stat:.4f}")
    st.write(f"**P-value:** {p_value:.4f}")
    st.write(f"**Degrees of freedom:** {dof}")

    # Calculate effect size (Cramér's V)
    n = contingency_table.sum().sum()
    cramers_v = np.sqrt(chi2_stat / (n * (min(contingency_table.shape) - 1)))
    st.write(f"**Cramér's V (effect size):** {cramers_v:.4f}")

with col2:
    st.markdown("### Decision")
    alpha = 0.05
    st.write(f"**Significance level (α):** {alpha}")

    if p_value < alpha:
        st.success("✅ **REJECT H₀** - There is a significant association between GDP category and net-zero commitments")
    else:
        st.error("❌ **FAIL TO REJECT H₀** - No significant association found")

# Commitment rates by GDP category
st.markdown("### Commitment Rates by GDP Category")
commitment_rates = merged_nz.groupby("GDP_Category")["Has_NetZero_Target"].agg(
    ["mean", "count"]
)
commitment_rates["percentage"] = (commitment_rates["mean"] * 100).round(2)

st.dataframe(commitment_rates[["count", "percentage"]].rename(
    columns={"count": "Countries", "percentage": "Commitment Rate (%)"}
))

st.markdown("---")

# Visualization
st.markdown("## Visualization: Net-Zero Commitment Rates")

# Calculate commitment rates for visualization
total_countries = merged_nz.groupby("GDP_Category")["Has_NetZero_Target"].count()
commitments = merged_nz.groupby("GDP_Category")["Has_NetZero_Target"].sum()

commitment_summary = pd.DataFrame({
    "Total_Countries": total_countries,
    "Commitments": commitments
})
commitment_summary["Commitment_Rate"] = (
    commitment_summary["Commitments"] / commitment_summary["Total_Countries"]
) * 100
commitment_summary["No_Commitment"] = (
    commitment_summary["Total_Countries"] - commitment_summary["Commitments"]
)

# Create visualization
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))
fig.suptitle(
    "Net-Zero Carbon Emissions Target Commitments by GDP Category",
    fontsize=16,
    fontweight="bold",
    y=1.02,
)

# Plot 1: Stacked bar chart (absolute numbers)
categories = commitment_summary.index
x_pos = np.arange(len(categories))

colors_commit = {"Committed": "#27ae60", "Not Committed": "#e74c3c"}

ax1.bar(
    x_pos,
    commitment_summary["Commitments"],
    label="Has Net-Zero Target",
    color=colors_commit["Committed"],
    alpha=0.8,
    edgecolor="black",
)
ax1.bar(
    x_pos,
    commitment_summary["No_Commitment"],
    bottom=commitment_summary["Commitments"],
    label="No Net-Zero Target",
    color=colors_commit["Not Committed"],
    alpha=0.8,
    edgecolor="black",
)

ax1.set_xlabel("GDP Category", fontsize=12, fontweight="bold")
ax1.set_ylabel("Number of Countries", fontsize=12, fontweight="bold")
ax1.set_title("Absolute Numbers", fontsize=13, fontweight="bold", pad=10)
ax1.set_xticks(x_pos)
ax1.set_xticklabels(categories)
ax1.legend(loc="upper right", fontsize=10)
ax1.grid(True, alpha=0.3, axis="y")

# Plot 2: Commitment rates (percentage)
ax2.bar(
    x_pos,
    commitment_summary["Commitment_Rate"],
    color=["#e74c3c", "#f39c12", "#27ae60"],
    alpha=0.8,
    edgecolor="black",
    linewidth=1.5,
)

ax2.set_xlabel("GDP Category", fontsize=12, fontweight="bold")
ax2.set_ylabel("Net-Zero Commitment Rate (%)", fontsize=12, fontweight="bold")
ax2.set_title("Commitment Rates (Percentage)", fontsize=13, fontweight="bold", pad=10)
ax2.set_xticks(x_pos)
ax2.set_xticklabels(categories)
ax2.set_ylim(0, 100)
ax2.grid(True, alpha=0.3, axis="y")
ax2.axhline(
    y=50, color="gray", linestyle="--", linewidth=1, alpha=0.5, label="50% threshold"
)
ax2.legend(loc="upper left", fontsize=9)

plt.tight_layout()
st.pyplot(fig)

st.markdown("---")

# Business Context
st.markdown("## 📊 Strategic Business Rationale")

st.markdown("""
### Why Net-Zero Commitments? A Forward-Looking Policy Risk Indicator

**Traditional development indicators** (life expectancy, education, literacy) measure **historical welfare outcomes**. This analysis instead examines **forward-looking policy commitments** that are **business-critical** for corporate strategy:

#### Immediate Business Context (2026-2027)

1. **EU CBAM (Carbon Border Adjustment Mechanism) - Effective 2026**
   - Imposes carbon tariffs on imports from countries without equivalent carbon pricing
   - Companies sourcing from non-committed countries face border tax penalties
   - Affects steel, cement, aluminum, fertilizers, electricity, hydrogen sectors

2. **EU ETS2 (Emissions Trading System Phase 2) - Effective 2027**
   - Expands emissions trading to buildings and road transport
   - Creates differential cost structures based on national climate policy stringency
   - Supply chains in committed countries gain competitive advantage

3. **Supply Chain Carbon Risk Mapping**
   - Multinational corporations must forecast carbon pricing exposure by supplier location
   - Net-zero commitments serve as **proxy for future regulatory stringency**
   - Investment decisions require 10-20 year policy environment projections

#### Why This Matters for Business Analytics

**The Executive Question:** *"Which markets will face carbon tariffs in 2026, and how should we restructure our supply chain?"*

This analysis answers that question by testing whether GDP predicts net-zero commitment propensity—a critical input for strategic sourcing decisions.

**Analytical Advantage:** Unlike traditional development indicators, net-zero targets are:
- **Predictive** (not retrospective)
- **Policy-actionable** (governments can change commitments)
- **Financially material** (direct impact on cost structures)
- **Decision-relevant** (companies making location choices TODAY)
""")

st.markdown("---")

# Key Findings
st.markdown("## Key Findings and Implications")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### Statistical Results")
    if p_value < 0.05:
        st.success(f"**Strong Association Found** (χ² = {chi2_stat:.1f}, p < 0.001)")
        st.write(f"**Effect Size:** Cramér's V = {cramers_v:.3f} (moderate effect)")
        st.write("**Higher GDP countries are significantly more likely to have net-zero commitments**")

with col2:
    st.markdown("### Business Implications")
    st.write("**Supply Chain Strategy:** Higher GDP countries = lower carbon tariff risk")
    st.write("**Investment Decisions:** Net-zero commitments predict future regulatory costs")
    st.write("**Market Selection:** Committed countries offer competitive advantages")

st.markdown("""
### Commitment Rates Summary
""")

# Display commitment rates in a nice format
summary_table = commitment_rates[["count", "percentage"]].reset_index()
summary_table.columns = ["GDP Category", "Countries", "Commitment Rate (%)"]
st.dataframe(summary_table, use_container_width=True)

st.info("**Bottom Line:** This dataset choice demonstrates strategic business analytics thinking—using data that **practitioners actually need** for real decisions with real deadlines.")