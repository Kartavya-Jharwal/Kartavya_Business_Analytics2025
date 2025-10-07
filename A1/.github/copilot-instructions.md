# AI Coding Agent Instructions for Kartavya Business Analytics A1

## Project Overview

This is a **Streamlit-based business analytics dashboard** analyzing the relationship between GDP per capita, CO₂ emissions, and net-zero climate commitments across 190+ countries. The project demonstrates statistical hypothesis testing, data visualization, and business intelligence insights.

**Core Architecture:**
- **Frontend:** Streamlit multi-page application with custom CSS theming
- **Data Layer:** Local CSV files loaded via pandas with caching
- **Analysis Layer:** Statistical computations using scipy, numpy
- **Visualization:** Plotly and matplotlib for interactive charts

## Key Architectural Patterns

### 1. Data Loading & Processing (`utils/data_loader.py`)
```python
@st.cache_data
def load_gdp_data():
    """Load GDP per capita dataset."""
    data_path = Path(__file__).parent.parent / "gdp-per-capita-worldbank-constant-usd" / "gdp-per-capita-worldbank-constant-usd.csv"
    df = pd.read_csv(data_path)
    df = df.rename(columns={"Entity": "Country"})
    return df
```
**Pattern:** Use `@st.cache_data` for expensive data loading operations. Always rename "Entity" to "Country" for consistency. Use pathlib for cross-platform file paths.

### 2. GDP Categories (`utils/data_loader.py`)
```python
@st.cache_data
def create_gdp_categories(df, low_threshold=5000, high_threshold=15000):
    """Create GDP categories with custom thresholds."""
    df = df.copy()
    gdp_columns = [col for col in df.columns if "gdp" in col.lower() and "capita" in col.lower()]
    gdp_col = gdp_columns[0]
    df[gdp_col] = pd.to_numeric(df[gdp_col], errors="coerce")
    df = df.dropna(subset=[gdp_col])

    df["GDP_Category"] = pd.cut(df[gdp_col], bins=[-float('inf'), low_threshold, high_threshold, float('inf')], labels=["Low", "Medium", "High"])
    return df
```
**Pattern:** Use fixed thresholds (5000, 15000) for GDP categories. Handle missing values with `dropna()`. Use `pd.cut()` with infinite bounds for proper categorization.

### 3. Statistical Analysis Pattern
```python
from scipy import stats
from scipy.stats import shapiro, pearsonr, spearmanr, f_oneway, chi2_contingency

# Always test assumptions first
stat_gdp, p_gdp = shapiro(clean_data[gdp_col])
if p_gdp < 0.05:
    # Use non-parametric tests
    rho, p_spearman = spearmanr(clean_data[gdp_col], clean_data[co2_col])
else:
    # Use parametric tests
    r, p_pearson = pearsonr(clean_data[gdp_col], clean_data[co2_col])
```
**Pattern:** Test normality with Shapiro-Wilk before choosing parametric vs non-parametric tests. Report both Pearson and Spearman correlations for robustness.

### 4. Streamlit Page Structure
```python
st.set_page_config(page_title="Page Title", page_icon="📊", layout="wide")
st.markdown(get_custom_css(), unsafe_allow_html=True)

# Load data with spinner
with st.spinner("Loading data..."):
    data = load_data()

# Use columns for layout
col1, col2 = st.columns(2)
with col1:
    st.metric("Metric", value)
with col2:
    st.dataframe(df)
```
**Pattern:** Always set page config and apply custom CSS. Use spinners for data loading. Leverage Streamlit's column layout system.

## Critical Developer Workflows

### 1. Data Pipeline Execution
```bash
# Install dependencies
uv sync

# Run development server
uv run streamlit run app.py

# Access at http://localhost:8501
```
**Note:** Uses UV package manager. Always run from project root directory.

### 2. Adding New Analysis Pages
1. Create `pages/N_📊_Page_Name.py`
2. Import required utilities from `utils/`
3. Follow the established pattern: load data → process → display results
4. Use `@st.cache_data` for expensive computations

### 3. Statistical Testing Protocol
1. **Formally state hypotheses** (H₀ and H₁)
2. **Check assumptions** (normality, homoscedasticity)
3. **Choose appropriate test** based on data characteristics
4. **Report effect sizes** (R², Cohen's d, Cramér's V)
5. **Provide confidence intervals** for estimates

## Project-Specific Conventions

### 1. Column Naming
- **Country/Entity:** Always standardize to "Country"
- **GDP Column:** Dynamically find via `col.lower()` contains "gdp" and "capita"
- **CO₂ Column:** Dynamically find via `col.lower()` contains "co2" or "emission"
- **Categories:** Use "GDP_Category" with values ["Low", "Medium", "High"]

### 2. Data Quality Handling
```python
# Always clean data before analysis
df = df.dropna(subset=[key_columns])
df[col] = pd.to_numeric(df[col], errors="coerce")
df = df.dropna(subset=[col])
```
**Pattern:** Remove missing values in key columns first, then convert to numeric, then remove NaNs again.

### 3. Visualization Theming
```python
# Use consistent color scheme
colors = {"Low": "#e74c3c", "Medium": "#f39c12", "High": "#27ae60"}
# Apply to plots, bars, and categories
```
**Pattern:** Red for Low, Orange for Medium, Green for High GDP categories.

### 4. Statistical Reporting
```python
# Always report comprehensive statistics
st.write(f"**Statistic:** {stat:.4f}")
st.write(f"**P-value:** {p:.4f}")
st.write(f"**Effect Size:** {effect_size:.4f}")
if p < 0.05:
    st.success("✅ Significant result")
else:
    st.error("❌ Not significant")
```
**Pattern:** Report statistic, p-value, effect size, and clear interpretation.

## Integration Points & Dependencies

### External Data Sources
- **GDP Data:** World Bank via Our World in Data
- **CO₂ Data:** Global Carbon Budget via Our World in Data
- **Net-Zero Data:** Net Zero Tracker via Our World in Data

### Python Package Dependencies
```toml
[project.dependencies]
pandas = ">=2.2.0"
numpy = ">=1.26.0"
scipy = ">=1.11.0"
streamlit = ">=1.50.0"
plotly = ">=5.18.0"
matplotlib = ">=3.8.0"
seaborn = ">=0.13.0"
```

### File Structure Dependencies
```
data/
├── co-emissions-per-capita/co-emissions-per-capita.csv
├── gdp-per-capita-worldbank-constant-usd/gdp-per-capita-worldbank-constant-usd.csv
└── net-zero-targets/net-zero-targets.csv
```

## Common Pitfalls & Solutions

### 1. Data Loading Issues
**Problem:** File paths not found
**Solution:** Use `Path(__file__).parent.parent / "data" / "file.csv"`

### 2. Column Name Variations
**Problem:** Different column names across datasets
**Solution:** Use dynamic column detection with string matching

### 3. Memory Issues with Large Datasets
**Problem:** Performance degradation
**Solution:** Use `@st.cache_data` and sample for statistical tests if needed

### 4. Statistical Test Selection
**Problem:** Wrong test for data characteristics
**Solution:** Always check normality first, use both parametric and non-parametric tests

## Business Context Integration

### EU Regulatory Landscape
- **CBAM (2026):** Carbon tariffs on imports from non-committed countries
- **ETS2 (2027):** Emissions trading for buildings and transport
- **Business Impact:** Supply chain carbon risk assessment

### Key Business Questions
1. Which countries face carbon tariffs in 2026?
2. How should supply chains be restructured?
3. What are the investment implications of net-zero commitments?

### Analytical Approach
- **Descriptive:** Country-level patterns and correlations
- **Inferential:** Hypothesis testing with statistical significance
- **Predictive:** Policy commitment forecasting
- **Prescriptive:** Business strategy recommendations

## Quality Assurance Patterns

### 1. Data Validation
```python
assert len(df) > 0, "Data loading failed"
assert "Country" in df.columns, "Country column missing"
assert df["Year"].nunique() > 10, "Insufficient time coverage"
```

### 2. Statistical Validation
```python
# Check correlation makes sense
assert -1 <= correlation <= 1, "Invalid correlation value"
# Check p-values are valid
assert 0 <= p_value <= 1, "Invalid p-value"
```

### 3. Business Logic Validation
```python
# High GDP should generally have higher emissions
high_gdp_mean = df[df["GDP_Category"] == "High"][co2_col].mean()
low_gdp_mean = df[df["GDP_Category"] == "Low"][co2_col].mean()
assert high_gdp_mean > low_gdp_mean, "Unexpected GDP-emissions relationship"
```

This codebase demonstrates rigorous statistical analysis applied to real business problems, with careful attention to data quality, methodological transparency, and practical business implications.</content>
<parameter name="filePath">d:\KJ\Personal_projects\_web_fun_builds\Kartavya_Business_Analytics2025\A1\.github\copilot-instructions.md