"""
Methodology: Statistical Methods and Data Sources
"""

import streamlit as st

from utils import get_custom_css

st.set_page_config(
    page_title="Methodology", page_icon="🔬", layout="wide"
)

st.markdown(get_custom_css(), unsafe_allow_html=True)

# Title
st.markdown("# 🔬 Methodology: Statistical Methods and Data Sources")

st.markdown("""
This page provides comprehensive documentation of the statistical methods, data sources, and analytical approach used in this business analytics assignment.
""")

st.markdown("---")

# Statistical Methods
st.markdown("## 📊 Statistical Methods")

st.markdown("""
### Hypothesis Testing Framework

#### Primary Analysis (Part 1): GDP vs CO₂ Emissions

**Core Hypothesis:** Countries with higher GDP per capita emit more CO₂ per capita.

**Statistical Tests Applied:**
1. **Pearson Correlation** - Tests linear relationship between continuous variables
2. **Spearman Correlation** - Tests monotonic relationship (robust to non-normality)
3. **One-way ANOVA** - Tests differences between GDP categories
4. **Welch's t-tests** - Pairwise comparisons between categories
5. **Shapiro-Wilk Test** - Assesses normality of distributions
6. **Skewness & Kurtosis** - Evaluates distribution shape

#### Extended Analysis (Part 2): Net-Zero Commitments

**Extended Hypothesis:** Countries with higher GDP per capita are more likely to have committed to net-zero carbon emissions targets.

**Statistical Tests Applied:**
1. **Chi-square Test for Independence** - Tests association between categorical variables
2. **Cramér's V** - Measures effect size for categorical associations
3. **Cross-tabulation Analysis** - Descriptive statistics by category
""")

st.markdown("### Significance Level and Decision Criteria")

st.markdown("""
- **Alpha (α):** 0.05 (5% significance level)
- **Decision Rule:** Reject H₀ if p-value < 0.05
- **Effect Size Reporting:** R², Cohen's d, Cramér's V, confidence intervals
- **Multiple Testing:** Bonferroni correction applied where appropriate
""")

st.markdown("---")

# Data Sources
st.markdown("## 📄 Data Sources")

st.markdown("""
### Primary Datasets

#### 1. GDP per Capita Dataset
- **Source:** World Bank and OECD national accounts data
- **Processing:** Our World in Data (2024-2025)
- **URL:** https://ourworldindata.org/grapher/gdp-per-capita-worldbank-constant-usd
- **Coverage:** Global, 1990-2023
- **License:** Creative Commons BY
- **Notes:** Constant 2015 USD for comparability across time

#### 2. CO₂ Emissions per Capita Dataset
- **Source:** Global Carbon Budget (2024), Population data (2024)
- **Processing:** Our World in Data with major processing
- **URL:** https://ourworldindata.org/grapher/co-emissions-per-capita
- **Coverage:** Global, 1990-2023
- **Notes:** Includes emissions from fossil fuels and industry, excludes land use change
- **License:** Creative Commons BY

#### 3. Net-Zero Targets Dataset
- **Source:** Net Zero Tracker - Energy and Climate Intelligence Unit, Data-Driven EnviroLab, NewClimate Institute, Oxford Net Zero (2023)
- **Processing:** Our World in Data with minor processing
- **URL:** https://ourworldindata.org/net-zero-targets
- **Coverage:** Global, status as of 2023
- **License:** Creative Commons BY
""")

st.markdown("---")

# Analytical Approach
st.markdown("## 🔍 Analytical Approach")

st.markdown("""
### Data Processing Pipeline

1. **Data Loading:** Import CSV files from local data directory
2. **Data Cleaning:** Handle missing values, standardize country names
3. **Data Integration:** Merge datasets on Country and Year columns
4. **Feature Engineering:** Create GDP categories, commitment indicators
5. **Statistical Analysis:** Apply appropriate tests based on data characteristics
6. **Visualization:** Create charts and graphs for interpretation
7. **Interpretation:** Contextual analysis with business implications

### Quality Assurance

- **Data Validation:** Cross-check data integrity and completeness
- **Statistical Assumptions:** Test normality, homoscedasticity, independence
- **Robustness Checks:** Multiple testing methods, sensitivity analysis
- **Reproducibility:** Documented code and clear methodological steps
""")

st.markdown("---")

# References
st.markdown("## 📚 References")

st.markdown("""
### Statistical Methods References

- **Cohen, J. (1988).** *Statistical Power Analysis for the Behavioral Sciences* (2nd ed.). Routledge.
- **Field, A. (2013).** *Discovering Statistics Using IBM SPSS Statistics* (4th ed.). SAGE Publications.
- **Pearson, K. (1895).** Notes on regression and inheritance in the case of two parents. *Proceedings of the Royal Society of London*, 58, 240-242.
- **Shapiro, S. S., & Wilk, M. B. (1965).** An analysis of variance test for normality (complete samples). *Biometrika*, 52(3-4), 591-611.
- **Spearman, C. (1904).** The proof and measurement of association between two things. *American Journal of Psychology*, 15(1), 72-101.
- **Welch, B. L. (1947).** The generalization of 'Student's' problem when several different population variances are involved. *Biometrika*, 34(1-2), 28-35.

### Climate and Policy Context References

- **IPCC (2021).** *Climate Change 2021: The Physical Science Basis*. Cambridge University Press.
- **IPCC (2022).** *Climate Change 2022: Mitigation of Climate Change*. Cambridge University Press.
- **European Commission (2023).** *Carbon Border Adjustment Mechanism*. Retrieved from https://taxation-customs.ec.europa.eu/carbon-border-adjustment-mechanism_en
- **European Parliament (2023).** *Regulation (EU) 2023/956 establishing a carbon border adjustment mechanism*. Official Journal of the European Union.
- **IEA (2023).** *Net Zero Roadmap: A Global Pathway to Keep the 1.5°C Goal in Reach*. International Energy Agency.
- **UNFCCC (2015).** *Paris Agreement*. United Nations Framework Convention on Climate Change.
""")

st.markdown("---")

# Technical Implementation
st.markdown("## 💻 Technical Implementation")

st.markdown("""
### Software Environment

- **Python Version:** 3.12+
- **Package Manager:** UV (recommended) or pip
- **Key Libraries:**
  - **Data Processing:** pandas, numpy
  - **Statistical Analysis:** scipy, statsmodels
  - **Visualization:** matplotlib, seaborn, plotly
  - **Web Interface:** streamlit

### Code Organization

```
├── app.py                 # Main application entry point
├── pages/                 # Multi-page application structure
│   ├── 1_📊_Part_1.py    # Hypothesis testing analysis
│   ├── 2_🎯_Part_2.py    # Net-zero commitments analysis
│   └── 3_🔬_Methodology.py # This page
├── utils/                 # Utility functions
│   ├── data_loader.py     # Data loading functions
│   └── styling.py         # Custom CSS and themes
└── data/                  # Raw data files
    ├── co-emissions-per-capita/
    ├── gdp-per-capita-worldbank-constant-usd/
    └── net-zero-targets/
```

### Reproducibility

- **Version Control:** Git repository with complete history
- **Dependency Management:** pyproject.toml with pinned versions
- **Documentation:** Comprehensive docstrings and comments
- **Testing:** Statistical validation and cross-verification
""")

st.markdown("---")

# Academic Integrity
st.markdown("## 🎓 Academic Integrity Statement")

st.markdown("""
**Author:** Kartavya Jharwal  
**Course:** BAN-0200 Business Analytics  
**Institution:** Hult International Business School  
**Submission Date:** October 24, 2025

This assignment represents my own work and analysis. All data sources are properly cited. Statistical analysis was conducted using Python (pandas, numpy, scipy, matplotlib, seaborn) in Google Colab environment. AI tools were used for code assistance and writing refinement while maintaining analytical independence and academic standards.

**Data Sources:** All datasets are from reputable academic and international organizations with Creative Commons licensing.  
**Statistical Methods:** Based on established statistical literature and best practices.  
**Analysis:** Original interpretation and business insights derived from the data.
""")

st.markdown("---")

# Future Research
st.markdown("## 🔮 Future Research Directions")

st.markdown("""
### Methodological Improvements

1. **Longitudinal Analysis:** Track countries over time; assess progress toward targets
2. **Causal Inference:** Use instrumental variables, difference-in-differences, synthetic controls
3. **Granular Data:** Sub-national analysis, sectoral breakdowns, company-level data
4. **Additional Variables:** Political systems, energy resources, trade patterns, cultural factors
5. **Quality Assessments:** Target ambition scoring, implementation evaluation, achievement tracking

### Analytical Extensions

1. **Integrated Modeling:** Economic-climate models, energy transition scenarios, cost-benefit analysis
2. **Machine Learning:** Predictive modeling of net-zero adoption, clustering analysis
3. **Network Analysis:** International cooperation patterns, technology transfer flows
4. **Scenario Planning:** Multiple climate policy futures and business implications

### Business Applications

1. **Supply Chain Analytics:** Carbon footprint mapping, supplier risk assessment
2. **Investment Optimization:** Portfolio analysis incorporating carbon pricing trajectories
3. **Regulatory Forecasting:** Predictive modeling of policy adoption and implementation
4. **Market Intelligence:** Competitive positioning in low-carbon transition
""")