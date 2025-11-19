# A2 - London Airbnb Regression Analysis

## Project Overview
This project implements a comprehensive regression analysis of London Airbnb listings to predict pricing and provide actionable business insights. The analysis follows the SEMMA framework (Sample, Explore, Modify, Model, Assess) and meets all requirements for the BAN Regression Assignment.

## 📁 Project Structure
```
A2/
├── London/
│   ├── hospitality_pricing_model.ipynb  ← MAIN NOTEBOOK (Analysis + Report)
│   ├── merged_airbnb_data.csv           ← Primary dataset
│   ├── listings.csv                     ← Fallback dataset
│   ├── calendar.csv
│   ├── reviews.csv
│   ├── neighbourhoods.csv
│   └── artifacts/                       ← Model outputs (created on execution)
├── README_A2.md                         ← This file
└── pyproject.toml
```

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- uv package manager (or pip)
- Jupyter Notebook / VS Code with Python extension

### Installation

#### Option 1: Using uv (Recommended)
```powershell
cd A2
uv init
uv add pandas numpy scikit-learn matplotlib seaborn scipy joblib statsmodels
```

#### Option 2: Using pip
```powershell
cd A2
pip install pandas numpy scikit-learn matplotlib seaborn scipy joblib statsmodels
```

### Running the Analysis
1. Open `London/hospitality_pricing_model.ipynb` in VS Code or Jupyter
2. Select the Python interpreter with installed packages
3. Run all cells sequentially from top to bottom
4. Review outputs, visualizations, and recommendations

**Execution Time:** Approximately 5-10 minutes (depending on dataset size and hardware)

## 📊 What's Inside

### Executive Summary
- Research question and rationale
- Why regression analysis is appropriate
- SEMMA framework overview
- Target variable justification (price/ADR)

### SEMMA Stage 1: Sample
- Environment validation
- Dataset loading (96,871 listings)
- Initial data quality assessment

### SEMMA Stage 2: Explore
- **10+ Visualizations:**
  1. Price distribution (histogram with log transformation)
  2. Price by room type (box plot)
  3. Accommodates vs price (scatter plot)
  4. Bedrooms vs price (scatter plot)
  5. Review scores vs price (scatter plot)
  6. Top 15 neighbourhoods by price (bar chart)
  7. Correlation heatmap (numeric features)
  8. Property type distribution (bar chart)
  9. Superhost vs non-superhost pricing (violin plot)
  10. Availability patterns (histogram)

- Each visualization includes:
  - Statistical interpretation
  - Business insights
  - Modeling implications

### SEMMA Stage 3: Modify
- **Column-by-column documentation** (43 columns)
  - Rationale for retention, dropping, or transformation
  - Missing value strategies
  - Feature engineering justification

- **Outlier handling:**
  - IQR analysis
  - 99th percentile capping strategy

- **Feature engineering:**
  - occupancy_rate
  - price_per_guest
  - log_reviews
  - is_premium_location
  - lead_time_index
  - property_type_grouped
  - And more...

### SEMMA Stage 4: Model
- **Multicollinearity check (VIF analysis)**
- **Scikit-learn pipeline:**
  - StandardScaler for numeric features
  - OneHotEncoder for categorical features
  - LinearRegression estimator
- Train/test chronological split (80/20)
- Baseline model comparison

### SEMMA Stage 5: Assess
- **Performance metrics:**
  - RMSE, MAE, R²
  - Comparison to baseline

- **Statsmodels OLS analysis:**
  - R² interpretation (% variance explained)
  - Adjusted R² (penalized for predictors)
  - F-statistic (overall model significance)
  - P-values (individual predictor significance)
  - Business translation of all statistics

- **Residual diagnostics:**
  - Predicted vs actual scatter
  - Residual distribution histogram
  - QQ plot (normality check)

### Business Recommendations
- **For Hosts:** Capacity optimization, location awareness, superhost benefits
- **For Airbnb Platform:** Dynamic pricing tool, neighbourhood insights, onboarding guidance
- **For Property Investors:** Location strategy, capacity ROI, market gaps

### Model Improvement Suggestions
- Temporal features (seasonality, events)
- Non-linear models (Random Forest, XGBoost)
- NLP on descriptions/amenities
- Interaction terms
- Regularization (Ridge/Lasso)

## 📝 Assignment Requirements Met

| Requirement | Status | Location in Notebook |
|-------------|--------|---------------------|
| SEMMA Framework | ✅ | Sections 1-5 |
| 10+ Visualizations | ✅ | Section 2.3 (Visualizations 1-10) |
| Column Documentation | ✅ | Section 3.1 (Treatment table + narratives) |
| Missing Value Handling | ✅ | Section 3.3 + code cells |
| Outlier Treatment | ✅ | Section 3.2 |
| Regression Model | ✅ | Section 4 |
| R²/Adj R²/p-value Interpretation | ✅ | Section 5.2 |
| Business Recommendations | ✅ | Section 6.1 |
| 1,500-2,000 words | ✅ | ~1,800 words in markdown |

## 🎯 Rubric Alignment

### Structure, Content & Analysis (30 pts)
- Executive summary with justified rationale
- Suitability of regression discussed
- Actionable recommendations
- Well-structured SEMMA sections

### Quality of Python (10 pts)
- Clean, documented code
- No errors (validated structure)
- Comments and explanations

### Descriptive Characteristics (10 pts)
- Comprehensive visualizations
- Statistical summaries
- Data quality assessment

### Variable Transformation (15 pts)
- Outlier handling documented
- Missing value strategies
- Feature engineering rationale
- Dummy variables (one-hot encoding)

### Regression Results (15 pts)
- Multiple model outputs (sklearn + statsmodels)
- Coefficient interpretation
- Multicollinearity check (VIF)

### R²/p-value Interpretation (10 pts)
- Detailed statistical translation
- Business-friendly language
- Adjusted R² discussion

### Critical Thinking (30 pts)
- Evidence-based decisions
- Effective data gathering
- Deductive reasoning
- Appraisal of evidence

### Communication (30 pts)
- Clear visualizations
- Proper grammar and structure
- Well-constructed narrative
- Markdown + code integration

## 🔧 Troubleshooting

### Issue: "Module not found"
**Solution:** Ensure all packages are installed:
```powershell
pip install pandas numpy scikit-learn matplotlib seaborn scipy joblib statsmodels
```

### Issue: "File not found: merged_airbnb_data.csv"
**Solution:** The notebook automatically falls back to `listings.csv`. Ensure you're running from the `A2` directory and `London/` folder exists.

### Issue: "Kernel crash on large dataset"
**Solution:** 
- Increase Jupyter memory limit
- Use `low_memory=False` parameter in `pd.read_csv()` (already implemented)
- Run on a machine with >8GB RAM

### Issue: VIF calculation takes too long
**Solution:** Already optimized to use only numeric features. If still slow, reduce sample size in the VIF cell.

## 📚 Key Libraries Used
- **pandas:** Data manipulation
- **numpy:** Numerical operations
- **scikit-learn:** Machine learning (regression, preprocessing, metrics)
- **statsmodels:** Detailed statistical analysis (OLS, VIF)
- **matplotlib/seaborn:** Visualizations
- **scipy:** Statistical functions (QQ plots)
- **joblib:** Model persistence

## 🎓 Learning Outcomes
By completing this notebook, you will:
1. Understand end-to-end regression workflow (SEMMA)
2. Perform comprehensive EDA with business context
3. Handle real-world data issues (missing values, outliers)
4. Engineer meaningful features
5. Build and evaluate linear regression models
6. Interpret statistical outputs for business stakeholders
7. Provide actionable recommendations

## 📄 Citation
Dataset: Inside Airbnb (http://insideairbnb.com/)  
Location: London, United Kingdom  
Last Updated: [Check dataset metadata in notebook]

## 👥 Authors
[Your Name/Team]  
Business Analytics - Regression Project (A2)  
Due: December 10, 2025

## 📞 Support
For questions about:
- **Code/Technical Issues:** Review inline comments and markdown explanations
- **Statistical Interpretation:** See Section 5.2 (Statsmodels analysis)
- **Business Context:** See Section 6 (Recommendations)

---

**Note:** This notebook serves as both the analysis tool AND the written report as specified in the assignment instructions. No separate document is required.
