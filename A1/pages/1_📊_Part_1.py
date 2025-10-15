"""
Part 1: Hypothesis Testing with Provided Datasets
Core Hypothesis: "Countries with higher GDP per capita emit more CO₂ per capita."
"""

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import shapiro, skew, kurtosis
import warnings

from utils import (
    load_gdp_data,
    load_co2_data,
    merge_gdp_co2,
    create_gdp_categories,
    get_custom_css,
)
from utils.analysis import compute_correlations, compute_anova_and_pairwise


# Suppress warnings for cleaner output
warnings.filterwarnings("ignore")

# Set plotting style and parameters
plt.style.use("seaborn-v0_8")
plt.rcParams["figure.figsize"] = (12, 8)
plt.rcParams["font.size"] = 11

st.set_page_config(
    page_title="Part 1: Hypothesis Testing", page_icon="📊", layout="wide"
)

st.markdown(get_custom_css(), unsafe_allow_html=True)

# Title and Overview
st.markdown("# 📊 Part 1: Hypothesis Testing with Provided Datasets")

st.markdown("""
## Core Hypothesis

> *"Countries with higher GDP per capita emit more CO₂ per capita."*

### Datasets to be Analyzed

#### 1. CO₂ Emissions per Capita
```
co-emissions-per-capita/co-emissions-per-capita.csv
```
**Source:** Global Carbon Budget (2024), Population based on various sources (2024) – with major processing by Our World in Data

#### 2. GDP per Capita in Constant USD
```
gdp-per-capita-worldbank-constant-usd/gdp-per-capita-worldbank-constant-usd.csv
```
**Source:** National statistical organizations and central banks, OECD national accounts, and World Bank staff estimates (2025) – with minor processing by Our World in Data

### Analysis Steps

1. Load and inspect both datasets
2. Clean and standardize the data
3. Merge datasets on Country and Year
4. Create GDP categories (Low, Medium, High)
5. Calculate descriptive statistics with confidence intervals
6. Create visualizations
7. Interpret results
""")

st.markdown("---")

# Load data
@st.cache_data
def load_analysis_data():
    gdp_df = load_gdp_data()
    co2_df = load_co2_data()
    merged_df = merge_gdp_co2(gdp_df, co2_df)
    analysis_df = create_gdp_categories(merged_df)
    return gdp_df, co2_df, analysis_df

st.markdown("## Step 1: Load and Inspect Datasets")

with st.spinner("Loading datasets..."):
    gdp_df, co2_df, analysis_df = load_analysis_data()

col1, col2 = st.columns(2)

with col1:
    st.markdown("### CO₂ Emissions Dataset")
    st.write(f"**Shape:** {co2_df.shape[0]} rows, {co2_df.shape[1]} columns")
    st.write(f"**Year range:** {co2_df['Year'].min()} - {co2_df['Year'].max()}")
    st.write(f"**Unique countries:** {co2_df['Country'].nunique()}")
    st.dataframe(co2_df.head(), use_container_width=True)

with col2:
    st.markdown("### GDP Dataset")
    st.write(f"**Shape:** {gdp_df.shape[0]} rows, {gdp_df.shape[1]} columns")
    st.write(f"**Year range:** {gdp_df['Year'].min()} - {gdp_df['Year'].max()}")
    st.write(f"**Unique countries:** {gdp_df['Country'].nunique()}")
    st.dataframe(gdp_df.head(), use_container_width=True)

st.markdown("---")

# Step 2: Data Cleaning
st.markdown("## Step 2: Clean and Standardize Data")

st.markdown("""
Before merging the datasets, we need to:

1. **Standardize country names** between datasets
2. **Identify overlapping years** across both datasets
3. **Handle missing or inconsistent data points**
4. **Ensure data quality** for meaningful analysis
""")

# Show overlap analysis
co2_countries = set(co2_df["Country"].unique())
gdp_countries = set(gdp_df["Country"].unique())
common_countries = co2_countries.intersection(gdp_countries)

col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Common Countries", len(common_countries))
with col2:
    st.metric("CO₂ Only", len(co2_countries - gdp_countries))
with col3:
    st.metric("GDP Only", len(gdp_countries - co2_countries))

st.markdown("---")

# Step 3: Merge Datasets
st.markdown("## Step 3: Merge Datasets")

st.markdown("""
**Data Integration Process**

We'll merge the cleaned CO₂ and GDP datasets on Country and Year to create our analysis dataset. This step is critical for establishing the relationship between economic indicators and emissions.

**Key Operations:**
- Join on matching 'Country' and 'Year' columns
- Handle potential many-to-many relationships
- Create a unified analysis-ready dataset
""")

st.write(f"**Merged dataset:** {len(analysis_df)} rows")
st.write(f"**Countries in merged data:** {analysis_df['Country'].nunique()}")
st.write(f"**Year range:** {analysis_df['Year'].min()} - {analysis_df['Year'].max()}")

st.dataframe(analysis_df.head(), use_container_width=True)

st.markdown("---")

# Step 4: GDP Categories
st.markdown("## Step 4: Feature Engineering - GDP Categories")

st.markdown("""
Create GDP categories using **fixed thresholds** to ensure consistency across all analyses:

- **Low GDP:** < $5,000 per capita
- **Medium GDP:** $5,000 - $15,000 per capita
- **High GDP:** > $15,000 per capita

**Note:** These categories are for descriptive analysis only. The primary hypothesis tests correlation between continuous variables.
""")

# Show GDP category distribution
gdp_col = "GDP per capita (constant 2015 US$)"
category_counts = analysis_df["GDP_Category"].value_counts()
total = len(analysis_df)

st.markdown("### GDP Category Distribution")
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Low GDP", f"{category_counts.get('Low', 0)} ({category_counts.get('Low', 0)/total*100:.1f}%)")
with col2:
    st.metric("Medium GDP", f"{category_counts.get('Medium', 0)} ({category_counts.get('Medium', 0)/total*100:.1f}%)")
with col3:
    st.metric("High GDP", f"{category_counts.get('High', 0)} ({category_counts.get('High', 0)/total*100:.1f}%)")

# GDP statistics by category
st.markdown("### GDP Statistics by Category")
gdp_stats = (
    analysis_df.groupby("GDP_Category")[gdp_col]
    .agg(["count", "mean", "median", "std", "min", "max"])
    .round(2)
)
st.dataframe(gdp_stats, use_container_width=True)

st.info("**Note:** Categories use FIXED thresholds for consistency. Core hypothesis tests correlation between continuous variables.")

st.markdown("---")

# Statistical Hypothesis Formulation
st.markdown("## Statistical Hypothesis Formulation")

st.markdown("""
Before conducting the analysis, we must formally state our hypotheses:

### Null Hypothesis (H₀)
**Statement:** There is no linear relationship between GDP per capita and CO₂ emissions per capita.

**Mathematical Notation:**
$$H_0: \\rho = 0$$

Where ρ (rho) is the population correlation coefficient between GDP per capita and CO₂ emissions per capita.

### Alternative Hypothesis (H₁)
**Statement:** There is a positive linear relationship between GDP per capita and CO₂ emissions per capita. As GDP per capita increases, CO₂ emissions per capita also increase.

**Mathematical Notation:**
$$H_1: \\rho > 0$$

### Significance Level
α = 0.05 (5% significance level)

**Decision Rule:**
- If p-value < 0.05, reject H₀ (evidence of significant positive correlation)
- If p-value ≥ 0.05, fail to reject H₀ (insufficient evidence of correlation)

**Note:** GDP categories (Low, Medium, High) are created for descriptive analysis and visualization purposes only. The core hypothesis tests the relationship between the continuous variables.
""")

st.markdown("---")

# Distribution Analysis
st.markdown("## Distribution Analysis: Checking Assumptions")

st.markdown("""
Before applying parametric tests (correlation), we must verify that our **continuous variables** meet necessary assumptions:

1. **Normality** - Are GDP and CO₂ normally distributed?
2. **Skewness** - Is the distribution symmetrical or skewed?
3. **Kurtosis** - Does the distribution have heavy tails or outliers?
4. **Linearity** - Is the relationship between variables linear?

These checks determine whether we can use Pearson correlation or need Spearman correlation (non-parametric alternative).
""")

# Normality testing
st.markdown("### Normality Testing: Shapiro-Wilk Test")

# Get continuous variables
co2_col = "Annual CO₂ emissions (per capita)"
clean_data = analysis_df[[gdp_col, co2_col]].dropna()

col1, col2 = st.columns(2)

with col1:
    st.markdown("#### GDP per Capita")
    # Test GDP per capita
    if len(clean_data) > 5000:
        gdp_sample = clean_data[gdp_col].sample(5000, random_state=42)
        st.write("(Using random sample of 5000 for computational efficiency)")
    else:
        gdp_sample = clean_data[gdp_col]

    stat_gdp, p_gdp = shapiro(gdp_sample)
    st.write(f"**Statistic:** {stat_gdp:.6f}")
    st.write(f"**P-value:** {p_gdp:.6f}")
    conclusion = "NOT normal" if p_gdp < 0.05 else "Approximately normal"
    st.write(f"**Conclusion:** {conclusion} (α=0.05)")

with col2:
    st.markdown("#### CO₂ Emissions per Capita")
    # Test CO2 emissions
    if len(clean_data) > 5000:
        co2_sample = clean_data[co2_col].sample(5000, random_state=42)
        st.write("(Using random sample of 5000 for computational efficiency)")
    else:
        co2_sample = clean_data[co2_col]

    stat_co2, p_co2 = shapiro(co2_sample)
    st.write(f"**Statistic:** {stat_co2:.6f}")
    st.write(f"**P-value:** {p_co2:.6f}")
    conclusion = "NOT normal" if p_co2 < 0.05 else "Approximately normal"
    st.write(f"**Conclusion:** {conclusion} (α=0.05)")

# Interpretation
if p_gdp < 0.05 or p_co2 < 0.05:
    st.warning("⚠ At least one variable is NOT normally distributed")
    st.markdown("""
    **Recommendations:**
    - Use BOTH Pearson and Spearman correlation
    - Spearman is more robust to non-normality
    - Large sample size (n > 1000) → Central Limit Theorem applies
    - Results should be similar if relationship is monotonic
    """)
else:
    st.success("✓ Both variables are approximately normally distributed")
    st.markdown("""
    - Pearson correlation is appropriate
    - Can also use Spearman for confirmation
    """)

st.info("**Note:** With large samples (n > 1000), parametric tests are robust to moderate departures from normality due to the Central Limit Theorem.")

st.markdown("---")

# Skewness and Kurtosis Analysis
st.markdown("## Skewness and Kurtosis Analysis")

st.markdown("Examine the shape of both continuous variables to understand asymmetry and tail behavior.")

# Analyze GDP per capita
gdp_data = clean_data[gdp_col]
gdp_skewness = skew(gdp_data)
gdp_kurtosis = kurtosis(gdp_data)

# Analyze CO2 emissions
co2_data = clean_data[co2_col]
co2_skewness = skew(co2_data)
co2_kurtosis = kurtosis(co2_data)

col1, col2 = st.columns(2)

with col1:
    st.markdown("#### GDP per Capita")
    st.write(f"**Mean:** ${gdp_data.mean():,.2f}")
    st.write(f"**Median:** ${gdp_data.median():,.2f}")
    st.write(f"**Std Dev:** ${gdp_data.std():,.2f}")
    st.write(f"**Skewness:** {gdp_skewness:.4f}")
    st.write(f"**Kurtosis:** {gdp_kurtosis:.4f}")

with col2:
    st.markdown("#### CO₂ Emissions per Capita")
    st.write(f"**Mean:** {co2_data.mean():.4f} tonnes")
    st.write(f"**Median:** {co2_data.median():.4f} tonnes")
    st.write(f"**Std Dev:** {co2_data.std():.4f} tonnes")
    st.write(f"**Skewness:** {co2_skewness:.4f}")
    st.write(f"**Kurtosis:** {co2_kurtosis:.4f}")

# Summary table
st.markdown("### Summary Table")
summary_data = pd.DataFrame(
    {
        "Variable": ["GDP per Capita", "CO₂ Emissions"],
        "n": [len(gdp_data), len(co2_data)],
        "Mean": [gdp_data.mean(), co2_data.mean()],
        "Median": [gdp_data.median(), co2_data.median()],
        "Std_Dev": [gdp_data.std(), co2_data.std()],
        "Skewness": [gdp_skewness, co2_skewness],
        "Kurtosis": [gdp_kurtosis, co2_kurtosis],
    }
)
st.dataframe(summary_data.round(4), use_container_width=True)

# Overall interpretation
st.markdown("### Interpretation for Correlation Analysis")

# Check if any variable is problematic
problematic_skew = any(abs(summary_data["Skewness"]) > 1)
problematic_kurt = any(abs(summary_data["Kurtosis"]) > 3)

if problematic_skew or problematic_kurt:
    st.warning("⚠ CAUTION: Data shows significant departures from normality")
    st.markdown("""
    **Recommendations:**
    - High skewness detected → Data is asymmetric
    - Spearman correlation preferred (robust to skewness)
    - Consider log transformation for visualization
    - High kurtosis detected → Outliers present
    - Spearman correlation more robust to outliers
    - Pearson correlation can be influenced by extreme values
    - We will use BOTH Pearson and Spearman correlation
    - Pearson: Tests linear relationship
    - Spearman: Tests monotonic relationship (more robust)
    """)
else:
    st.success("✓ Data is reasonably close to normal distribution")
    st.markdown("""
    - Pearson correlation is appropriate
    - Spearman correlation will provide confirmation
    """)

st.info("Large sample size (n > 1000) provides robustness via Central Limit Theorem")

# Correlation analysis (Pearson and Spearman)
st.markdown("---")
st.markdown("## Correlation Analysis: Pearson & Spearman")

with st.spinner("Computing correlations..."):
    corr_res = compute_correlations(analysis_df, gdp_col, co2_col)

if corr_res is None:
    st.warning("Not enough data to compute correlations")
else:
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### Pearson Correlation (linear)")
        st.write(f"**r:** {corr_res['pearson_r']:.3f}")
        st.write(f"**P-value:** {corr_res['pearson_p']:.4g}")
        st.write(f"**R²:** {corr_res['r_squared']:.3f}")

    with col2:
        st.markdown("### Spearman Correlation (rank)")
        st.write(f"**ρ:** {corr_res['spearman_rho']:.3f}")
        st.write(f"**P-value:** {corr_res['spearman_p']:.4g}")

    if corr_res['pearson_p'] < 0.05:
        st.success("✓ Pearson correlation is statistically significant (p < 0.05)")
    else:
        st.info("Pearson correlation not statistically significant at α=0.05")

# ANOVA and pairwise comparisons
st.markdown("---")
st.markdown("## ANOVA & Pairwise Comparisons (Welch's t-tests)")

with st.spinner("Running ANOVA and pairwise tests..."):
    anova_stat, anova_p, pairwise_df = compute_anova_and_pairwise(analysis_df, co2_col, "GDP_Category")

if anova_stat is None:
    st.warning("Insufficient groups/data to run ANOVA")
else:
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### One-way ANOVA")
        st.write(f"**F-statistic:** {anova_stat:.4f}")
        st.write(f"**P-value:** {anova_p:.4g}")
        if anova_p is not None and anova_p < 0.05:
            st.success("✓ Significant differences between GDP categories (reject H₀)")
        else:
            st.info("No significant differences detected between GDP categories (fail to reject H₀)")

    with col2:
        st.markdown("### Pairwise Comparisons (Welch)")
        if pairwise_df.empty:
            st.write("No pairwise results available")
        else:
            # Show a nicely formatted dataframe
            display_df = pairwise_df.copy()
            # round numeric columns for display
            for c in ["t_stat", "p_value", "cohen_d", "mean1", "mean2"]:
                if c in display_df.columns:
                    display_df[c] = display_df[c].round(4)
            st.dataframe(display_df, use_container_width=True)

    st.markdown("---")
    st.info("Pairwise tests use Welch's t-test (unequal variances). Cohen's d approximates effect size.")