# AI Coding Agent Instructions for CarbonSeer

## Project Overview

CarbonSeer is a **dual-purpose interdisciplinary project** combining quantitative business analytics with brand design:

### **Academic Context:**
1. **Business Analytics (BAN-0200)** - Prof Glen Joseph
   - Statistical analysis of GDP, CO₂ emissions, and net-zero commitments
   - Hypothesis testing, correlation analysis, and ANOVA
   - CBAM (Carbon Border Adjustment Mechanism) business implications

2. **Creativity in Advertising & Marketing (DSN-0303)** - Prof Lindsay Butcher
   - Brand design for **Redshaw Advisors** (carbon consulting company)
   - CarbonSeer as a standalone microsite demonstrating data-driven insights
   - Visual identity, UI/UX design, and marketing positioning

### **Project Purpose:**
CarbonSeer serves as a **demo microsite** illustrating quantitative carbon risk analysis for Redshaw Advisors' brand portfolio. It bridges analytical rigor with creative brand storytelling, showcasing how data visualization can support carbon consulting services.

**Core Architecture:**
- **Frontend:** Streamlit multi-page application with custom CSS theming and loading splash screens
- **Data Layer:** Local CSV files loaded via pandas with `@st.cache_data` caching
- **Analysis Layer:** Statistical computations using scipy, numpy with comprehensive effect size reporting
- **Visualization:** Plotly and matplotlib for interactive charts with custom themes
- **Export Layer:** Jupyter nbconvert with custom templates for PDF report generation
- **Brand Layer:** Custom styling, color schemes, and visual identity aligned with Redshaw Advisors positioning

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
**Pattern:** Use `@st.cache_data` for all data loading operations. Always rename "Entity" to "Country" for consistency. Use pathlib for cross-platform file paths. Data files are stored in root-level directories (not in a data/ folder).

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
**Pattern:** Use fixed thresholds (5000, 15000) for GDP categories. Handle missing values with `dropna()`. Use `pd.cut()` with infinite bounds for proper categorization. Dynamic column detection via string matching.

### 3. Statistical Analysis Pattern (`utils/analysis.py`)
```python
@st.cache_data
def compute_correlations(df, x_col, y_col, sample_limit=5000):
    """Compute Pearson and Spearman correlations between two columns."""
    clean = df[[x_col, y_col]].dropna()
    if len(clean) > sample_limit:
        sample = clean.sample(sample_limit, random_state=42)
    else:
        sample = clean

    pearson_r, pearson_p = pearsonr(x, y)
    spearman_rho, spearman_p = spearmanr(x, y)
    r_squared = pearson_r**2

    return {
        "pearson_r": pearson_r,
        "pearson_p": pearson_p,
        "spearman_rho": spearman_rho,
        "spearman_p": spearman_p,
        "r_squared": r_squared,
        "n": len(sample),
    }
```
**Pattern:** Always compute both parametric (Pearson) and non-parametric (Spearman) correlations. Use sampling for large datasets to maintain statistical stability. Report comprehensive statistics including R², p-values, and sample sizes.

### 4. Streamlit Page Structure (`app.py`, `pages/`)
```python
st.set_page_config(page_title="CarbonSeer Dashboard", page_icon="🌍", layout="wide")
st.markdown(get_custom_css(), unsafe_allow_html=True)

# Show splash screen during loading
show_splash(cover_path, message="Loading datasets...")

# Load data with spinner
with st.spinner("Processing data..."):
    data = load_all_data()

# Use columns for responsive layout
col1, col2 = st.columns(2)
with col1:
    st.metric("Countries", len(data))
with col2:
    st.dataframe(data.head())
```
**Pattern:** Always set page config with wide layout. Apply custom CSS globally. Use splash screens for heavy loading operations. Leverage Streamlit's column system for responsive design. Cache all data operations.

## Critical Developer Workflows

### 1. Environment Setup & Dependencies
```bash
# Install all dependencies (uses UV package manager)
uv sync

# Install development dependencies
uv sync --dev
```
**Note:** Project uses UV for dependency management with both `project.dependencies` and `tool.uv.dev-dependencies` in `pyproject.toml`. Hatchling is used as the build backend.

### 2. Development Server
```bash
# Run the Streamlit application
uv run streamlit run app.py

# Access at http://localhost:8501
```
**Note:** Always run from project root directory. The app uses multi-page navigation with files in the `pages/` directory.

### 3. PDF Report Generation
```python
# Export notebook to PDF with custom template
from nbconvert import PDFExporter
from utils.data_loader import load_all_data

# Load data and export
data = load_all_data()
exporter = PDFExporter(template_file='templates/custom_report.tpl')
```
**Note:** Uses nbconvert with custom Jinja2 template (`templates/custom_report.tpl`) for professional PDF reports. Template includes custom CSS for typography and layout.

### 4. Static Site Generation
```bash
# Serve static interactive site for data exploration
python -m http.server 8000
# Then visit http://localhost:8000/site/
```
**Note:** Includes a static HTML site in `site/` folder for quick data exploration using Plotly.js directly from CSV files.

## Project-Specific Conventions

### 1. Column Naming & Detection
- **Country/Entity:** Always standardize to "Country"
- **GDP Column:** Dynamically find via `col.lower()` contains "gdp" and "capita"
- **CO₂ Column:** Dynamically find via `col.lower()` contains "co2" or "emission"
- **Net-Zero Status:** Find via "status" and "net" in column name
- **Categories:** Use "GDP_Category" with values ["Low", "Medium", "High"]
- **Commitment Strength:** Numeric scale 0-5 for net-zero target binding strength

### 2. Data Quality Handling
```python
# Always clean data before analysis
df = df.dropna(subset=[key_columns])
df[col] = pd.to_numeric(df[col], errors="coerce")
df = df.dropna(subset=[col])
```
**Pattern:** Remove missing values in key columns first, then convert to numeric, then remove NaNs again. Use `errors="coerce"` for robust numeric conversion.

### 3. Commitment Strength Mapping (`utils/data_loader.py`)
```python
commitment_mapping = {
    "Achieved (self-declared)": 5,
    "In law": 4,
    "In policy document": 3,
    "Declaration / pledge": 2,
    "Proposed / in discussion": 1,
}
df["Commitment_Strength"] = df[status_col].map(commitment_mapping).fillna(0)
```
**Pattern:** Map net-zero commitment levels to numeric strength scores. Only legally binding commitments (4-5) provide regulatory protection.

### 4. Visualization Theming (`utils/styling.py`)
```python
# Consistent color scheme for GDP categories
colors = {"Low": "#e74c3c", "Medium": "#f39c12", "High": "#27ae60"}
# Applied to plots, bars, and category indicators
```
**Pattern:** Red for Low GDP, Orange for Medium, Green for.p High GDP categories. Custom CSS with Inter font and beige/purple/teal color palette.

### 5. Statistical Reporting (`utils/analysis.py`)
```python
# Comprehensive statistical reporting
st.write(f"**Pearson r:** {r:.4f}")
st.write(f"**Spearman ρ:** {rho:.4f}")
st.write(f"**R²:** {r_squared:.4f}")
st.write(f"**p-value:** {p:.4f}")
if p < 0.05:
    st.success("✅ Significant relationship")
else:
    st.error("❌ Not significant")
```
**Pattern:** Report both correlation types, effect sizes (R², Cohen's d), confidence intervals, and clear statistical interpretation.

## Integration Points & Dependencies

### External Data Sources
- **GDP Data:** World Bank via Our World in Data (`gdp-per-capita-worldbank-constant-usd/`)
- **CO₂ Data:** Global Carbon Budget via Our World in Data (`co-emissions-per-capita/`)
- **Net-Zero Data:** Net Zero Tracker via Our World in Data (`net-zero-targets/`)

### Python Package Dependencies (`pyproject.toml`)
```toml
[project.dependencies]
pandas = ">=2.2.0"
numpy = ">=1.26.0"
scipy = ">=1.11.0"
streamlit = ">=1.50.0"
plotly = ">=5.18.0"
matplotlib = ">=3.8.0"
seaborn = ">=0.13.0"
jupyter = ">=1.0.0"
nbconvert = ">=7.16.0"
pypandoc = ">=1.13"
pillow = ">=10.0.0"
streamlit-lottie = ">=0.0.5"
streamlit-extras = ">=0.4.0"
```

### File Structure Dependencies
```
├── gdp-per-capita-worldbank-constant-usd/     # GDP dataset directory
├── co-emissions-per-capita/                   # CO₂ dataset directory
├── net-zero-targets/                          # Net-zero dataset directory
├── utils/                                     # Core utilities package
│   ├── data_loader.py                         # Data loading functions
│   ├── analysis.py                            # Statistical computations
│   ├── styling.py                             # CSS and theming
│   └── splash.py                              # Loading screens
├── pages/                                     # Streamlit multi-page app
├── templates/                                 # nbconvert PDF templates
│   └── custom_report.tpl                      # Custom PDF styling
├── outputs/                                   # Generated reports directory
└── assets/                                    # Images and static assets
```

## Common Pitfalls & Solutions

### 1. Data Loading Path Issues
**Problem:** File paths not found in different environments
**Solution:** Use `Path(__file__).parent.parent / "dataset-directory" / "file.csv"` for reliable cross-platform paths

### 2. Dynamic Column Detection Failures
**Problem:** Column names vary across datasets
**Solution:** Use flexible string matching: `col.lower()` contains required substrings. Always include fallback exact column names.

### 3. Memory Issues with Large Datasets
**Problem:** Performance degradation with full datasets
**Solution:** Use `@st.cache_data` and implement sampling in statistical functions (sample_limit=5000) for correlation stability

### 4. Net-Zero Commitment Misinterpretation
**Problem:** Treating all commitments equally
**Solution:** Use commitment strength mapping - only "In law" and "Achieved" provide legal protection for CBAM compliance

### 5. Statistical Test Selection Errors
**Problem:** Wrong parametric/non-parametric choice
**Solution:** Always test normality assumptions first. Report both correlation types for robustness.

## Business Context Integration

### EU Regulatory Landscape
- **CBAM (2026):** Carbon tariffs on imports from non-committed countries
- **ETS2 (2027):** Emissions trading for buildings and transport
- **Business Impact:** Supply chain carbon risk assessment and compliance planning

### Key Business Questions
1. Which countries face carbon tariffs in 2026?
2. How should supply chains be restructured for CBAM compliance?
3. What are the investment implications of net-zero commitments?
4. Which countries demonstrate successful emissions decoupling?

### Analytical Approach
- **Descriptive:** Country-level patterns and correlations
- **Inferential:** Hypothesis testing with statistical significance
- **Predictive:** Policy commitment forecasting
- **Prescriptive:** Business strategy recommendations for carbon risk management

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

CarbonSeer demonstrates rigorous statistical analysis applied to real business problems, with careful attention to data quality, methodological transparency, and practical business implications for carbon risk management in global supply chains.</content>
<parameter name="filePath">d:\KJ\Personal_projects\_web_fun_builds\Kartavya_Business_Analytics2025\A1\.github\copilot-instructions.md