# Assignment A1 - Comprehensive Checklist & Assessment

**Student:** Kartavya Jharwal  
**Course:** BAN-0200 Fundamentals of Business Analytics  
**Due:** October 24, 2025  
**Assessment Date:** October 4, 2025

---

## ✅ PART 1: GDP vs CO₂ Emissions - COMPLETION STATUS

### 1. Data Preparation & Cleaning ✓ COMPLETE
- [x] Load CO₂ emissions dataset
- [x] Load GDP per capita dataset
- [x] Inspect data structure and quality
- [x] Handle missing values
- [x] Standardize country names
- [x] Check for overlapping data
- [x] Document cleaning steps

**Status:** ✅ Excellent - Clear documentation and systematic approach

---

### 2. Data Merging ✓ COMPLETE
- [x] Merge on Country and Year
- [x] Inner join (matching records only)
- [x] Verify merge results
- [x] Document merged dataset characteristics

**Status:** ✅ Well executed

---

### 3. Feature Engineering ✓ COMPLETE
- [x] Create GDP categories (Low, Medium, High)
- [x] Use fixed thresholds ($5,000 and $15,000)
- [x] Document category distributions
- [x] Clear note that categories are for visualization only

**Status:** ✅ Excellent - Good clarification about purpose

---

### 4. Statistical Hypothesis Formulation ✓ COMPLETE
- [x] Null hypothesis (H₀: ρ = 0)
- [x] Alternative hypothesis (H₁: ρ > 0)
- [x] Significance level (α = 0.05)
- [x] Mathematical notation
- [x] Decision rules

**Status:** ✅ Perfect - Formally stated with proper notation

---

### 5. Distribution Analysis ✓ COMPLETE
- [x] Normality testing (Shapiro-Wilk)
- [x] Skewness analysis
- [x] Kurtosis analysis
- [x] Linearity assessment (scatterplots)
- [x] Q-Q plots
- [x] Histograms
- [x] Interpretation of all tests

**Status:** ✅ Outstanding - Very thorough statistical rigor

---

### 6. Primary Hypothesis Test ✓ COMPLETE
- [x] Pearson correlation (linear)
- [x] Spearman correlation (monotonic)
- [x] P-values calculated
- [x] R-squared interpretation
- [x] Formal decision on H₀
- [x] Effect size interpretation

**Status:** ✅ Excellent - Both correlation methods used

---

### 7. Descriptive Analytics ✓ COMPLETE
- [x] Group by GDP Category and Year
- [x] Calculate mean CO₂ emissions
- [x] Calculate SEM (standard error of mean)
- [x] Compute 95% confidence intervals (mean ± 1.96 × SEM)
- [x] Document CI widths

**Status:** ✅ Perfect - Meets all requirements

---

### 8. Supplementary Analyses ✓ COMPLETE
- [x] One-way ANOVA (group differences)
- [x] Welch's t-tests (pairwise comparisons)
- [x] Cohen's d (effect sizes)
- [x] Clear labeling as supplementary

**Status:** ✅ Excellent - Goes beyond requirements

---

### 9. Visualization ✓ COMPLETE
- [x] Line chart: CO₂ by GDP category over time
- [x] Shaded 95% confidence intervals
- [x] Professional formatting
- [x] Color coding by category
- [x] Legends and labels

**Status:** ✅ Professional quality

---

### 10. Interpretation ✓ COMPLETE
- [x] Statistical evidence discussed
- [x] Practical significance noted
- [x] Limitations acknowledged
- [x] Contextual understanding

**Status:** ✅ Well done

---

## ✅ PART 2: Net-Zero Targets Extension - COMPLETION STATUS

### 1. Additional Dataset ✓ COMPLETE
- [x] Net-zero targets dataset loaded
- [x] Data source documented
- [x] Proper citation

**Status:** ✅ Good choice - relevant to topic

---

### 2. New Hypothesis ✓ COMPLETE
- [x] Clear research question stated
- [x] Hypothesis formally stated
- [x] H₀ and H₁ defined
- [x] Significance level specified
- [x] Appropriate test identified (Chi-square)

**Status:** ✅ Well formulated

---

### 3. Data Integration ✓ COMPLETE
- [x] Merge with GDP data
- [x] Country name harmonization
- [x] Binary commitment variable created
- [x] Data quality checks

**Status:** ✅ Properly executed

---

### 4. Analysis ✓ COMPLETE
- [x] Cross-tabulation (GDP category vs commitment)
- [x] Chi-square test for independence
- [x] P-value calculation
- [x] Effect size (Cramér's V)
- [x] Commitment rates by category

**Status:** ✅ Appropriate statistical methods

---

### 5. Visualization ⚠️ NEEDS ADDITION
- [ ] Bar chart or stacked bar showing commitment rates by GDP category
- [ ] Visual comparison of commitment proportions
- [ ] Professional formatting

**Status:** ⚠️ MISSING - This is critical for Part 2

**ACTION REQUIRED:** Add visualization code cell after chi-square test

---

### 6. Interpretation ⚠️ NEEDS COMPLETION
- [x] Statistical results discussed
- [ ] Full interpretation with context
- [ ] Limitations discussed
- [ ] Real-world implications

**Status:** ⚠️ PARTIALLY COMPLETE - Has placeholders, needs actual results

---

## 📊 PRESENTATION & DOCUMENTATION

### Code Quality ✓ EXCELLENT
- [x] Clean, well-commented code
- [x] Consistent style
- [x] No errors visible
- [x] Reproducible

**Status:** ✅ Professional

---

### Markdown Documentation ✓ EXCELLENT
- [x] Clear section headers
- [x] Explanatory text between code
- [x] Mathematical notation
- [x] Tables and formatting

**Status:** ✅ Very professional

---

### References & Citations ⚠️ NEEDS COMPLETION
- [x] Data sources cited
- [x] URLs provided
- [ ] Academic references (if external research used)
- [ ] Complete references section

**Status:** ⚠️ Update final references section with your name and date

---

## 🎯 CRITICAL ACTIONS NEEDED BEFORE SUBMISSION

### Priority 1: MUST ADD
1. **Part 2 Visualization** - Bar chart showing net-zero commitment rates
2. **Complete Final References Section** - Add your name and completion date
3. **Run ALL Cells in Colab** - Ensure all outputs are visible

### Priority 2: SHOULD ENHANCE
4. **Add more interpretation** in Part 2 conclusion
5. **Spell check** all markdown cells
6. **Verify all visualizations display correctly**

---

## 📈 RUBRIC ASSESSMENT (Estimated Scores)

| Criterion | Points | Est. Score | Notes |
|-----------|--------|------------|-------|
| Data Preparation & Cleaning | 20 | 19-20 | Excellent |
| Descriptive Statistics | 15 | 14-15 | Complete with SEM, CI |
| Data Visualization | 15 | 12-13 | Missing Part 2 viz |
| Hypothesis Testing - Part 1 | 15 | 15 | Perfect |
| Extended Hypothesis - Part 2 | 15 | 13-14 | Needs viz |
| Reflection & Interpretation | 10 | 8-9 | Good, could be deeper |
| Code Quality & Documentation | 10 | 10 | Excellent |
| Communication - Clear | 10 | 9-10 | Very clear |
| Communication - Audience | 10 | 9 | Good |
| Grammar/Spelling | 10 | 9-10 | Professional |
| Referencing | 10 | 9-10 | Complete sources |
| Critical Thinking - Framing | 10 | 9-10 | Well framed |
| Critical Thinking - Evidence | 10 | 9-10 | Strong evidence |
| Critical Thinking - Data | 10 | 9-10 | Excellent |
| Critical Thinking - Logic | 10 | 9-10 | Sound reasoning |
| Self-Aware | 10 | 9 | Good awareness |
| Entrepreneurial - Ambiguity | 10 | 9 | Handles well |

**Estimated Total:** 182-194 / 200 points (91-97%)

**Grade Estimate:** A (with additions) or B+ (as is)

---

## 🚀 CODE TO ADD

### 1. Part 2 Visualization (Add after Chi-square test cell)

```python
# Visualization: Net-Zero Commitment Rates by GDP Category
import matplotlib.pyplot as plt
import numpy as np

print("="*80)
print("VISUALIZATION: NET-ZERO COMMITMENTS BY GDP CATEGORY")
print("="*80)

# Calculate commitment rates
commitment_summary = merged_nz.groupby('GDP_Category')['Has_NetZero_Target'].agg([
    ('Total_Countries', 'count'),
    ('Commitments', 'sum')
])
commitment_summary['Commitment_Rate'] = (commitment_summary['Commitments'] / commitment_summary['Total_Countries']) * 100
commitment_summary['No_Commitment'] = commitment_summary['Total_Countries'] - commitment_summary['Commitments']

print("\nCommitment Summary:")
print(commitment_summary)

# Create figure with two subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))
fig.suptitle('Net-Zero Carbon Emissions Target Commitments by GDP Category', 
             fontsize=16, fontweight='bold', y=1.02)

# Plot 1: Stacked bar chart
categories = commitment_summary.index
x_pos = np.arange(len(categories))

colors_commit = {'Committed': '#27ae60', 'Not Committed': '#e74c3c'}

ax1.bar(x_pos, commitment_summary['Commitments'], 
        label='Has Net-Zero Target', color=colors_commit['Committed'], alpha=0.8, edgecolor='black')
ax1.bar(x_pos, commitment_summary['No_Commitment'], 
        bottom=commitment_summary['Commitments'],
        label='No Net-Zero Target', color=colors_commit['Not Committed'], alpha=0.8, edgecolor='black')

ax1.set_xlabel('GDP Category', fontsize=12, fontweight='bold')
ax1.set_ylabel('Number of Countries', fontsize=12, fontweight='bold')
ax1.set_title('Absolute Numbers', fontsize=13, fontweight='bold', pad=10)
ax1.set_xticks(x_pos)
ax1.set_xticklabels(categories)
ax1.legend(loc='upper right', fontsize=10)
ax1.grid(True, alpha=0.3, axis='y')

# Add count labels
for i, cat in enumerate(categories):
    committed = commitment_summary.loc[cat, 'Commitments']
    not_committed = commitment_summary.loc[cat, 'No_Commitment']
    total = commitment_summary.loc[cat, 'Total_Countries']
    
    # Label for committed
    if committed > 0:
        ax1.text(i, committed/2, f'{int(committed)}', 
                ha='center', va='center', fontsize=11, fontweight='bold', color='white')
    
    # Label for not committed
    if not_committed > 0:
        ax1.text(i, committed + not_committed/2, f'{int(not_committed)}', 
                ha='center', va='center', fontsize=11, fontweight='bold', color='white')

# Plot 2: Commitment rates (percentage)
ax2.bar(x_pos, commitment_summary['Commitment_Rate'], 
        color=['#e74c3c', '#f39c12', '#27ae60'], alpha=0.8, edgecolor='black', linewidth=1.5)

ax2.set_xlabel('GDP Category', fontsize=12, fontweight='bold')
ax2.set_ylabel('Net-Zero Commitment Rate (%)', fontsize=12, fontweight='bold')
ax2.set_title('Commitment Rates (Percentage)', fontsize=13, fontweight='bold', pad=10)
ax2.set_xticks(x_pos)
ax2.set_xticklabels(categories)
ax2.set_ylim(0, 100)
ax2.grid(True, alpha=0.3, axis='y')
ax2.axhline(y=50, color='gray', linestyle='--', linewidth=1, alpha=0.5, label='50% threshold')
ax2.legend(loc='upper left', fontsize=9)

# Add percentage labels on bars
for i, cat in enumerate(categories):
    rate = commitment_summary.loc[cat, 'Commitment_Rate']
    ax2.text(i, rate + 2, f'{rate:.1f}%', 
            ha='center', va='bottom', fontsize=11, fontweight='bold')

plt.tight_layout()
plt.show()

# Print interpretation
print("\n" + "="*80)
print("INTERPRETATION")
print("="*80)
print("\nKey Observations:")
for cat in categories:
    rate = commitment_summary.loc[cat, 'Commitment_Rate']
    total = commitment_summary.loc[cat, 'Total_Countries']
    committed = commitment_summary.loc[cat, 'Commitments']
    print(f"\n{cat} GDP Countries:")
    print(f"  • {committed} out of {int(total)} countries ({rate:.1f}%) have net-zero targets")

print("\n" + "="*80)
```

### 2. Enhanced Part 2 Interpretation (Add markdown cell after visualization)

```markdown
## Part 2: Detailed Interpretation

### Statistical Test Results

The chi-square test reveals [INSERT ACTUAL RESULT: significant/non-significant] association between GDP category and net-zero commitments (χ² = [VALUE], p = [VALUE], Cramér's V = [VALUE]).

### Key Findings

1. **High GDP Countries:** Show [XX]% commitment rate, indicating [interpretation]
2. **Medium GDP Countries:** Display [XX]% commitment rate, suggesting [interpretation]
3. **Low GDP Countries:** Have [XX]% commitment rate, which may reflect [interpretation]

### Context and Implications

**Economic Capacity and Climate Action:**
- Wealthier nations demonstrate [higher/lower/similar] commitment rates
- This pattern [supports/contradicts] the hypothesis
- Possible explanations include:
  - Greater economic resources for green transition
  - Historical responsibility for emissions
  - Political pressure from citizens
  - Technological capabilities
  - International climate governance influence

**Limitations:**
- Binary commitment measure (yes/no) doesn't capture:
  - Target ambition (e.g., 2030 vs 2070)
  - Legal bindingness of commitments
  - Implementation progress
  - Sectoral coverage
- Country-level analysis masks within-country variation
- Correlation does not imply causation
- Data availability limitations for some countries

**Future Research Directions:**
- Longitudinal analysis of commitment implementation
- Quality assessment of net-zero targets
- Sectoral breakdown by GDP level
- Role of international climate finance
- Influence of political systems on commitment rates
```

### 3. Complete References Section (Replace placeholder at end)

```markdown
## Data Sources

### Primary Datasets

1. **GDP per Capita Dataset**
   - Title: GDP per capita, PPP (constant 2017 international $)
   - Source: World Bank and OECD national accounts data
   - Processing: Our World in Data (2025)
   - URL: https://ourworldindata.org/grapher/gdp-per-capita-worldbank-constant-usd
   - Accessed: October 2025
   - Variables: Country, Year, GDP per capita (constant 2017 USD)

2. **CO₂ Emissions per Capita Dataset**
   - Title: Annual CO₂ emissions per capita
   - Source: Global Carbon Budget (2024), Population based on various sources (2024)
   - Processing: Our World in Data with major processing
   - URL: https://ourworldindata.org/grapher/co-emissions-per-capita
   - Accessed: October 2025
   - Variables: Country, Year, CO₂ emissions per capita (tonnes)

3. **Net-Zero Targets Dataset**
   - Title: Status of net-zero carbon emissions targets
   - Source: Energy and Climate Intelligence Unit, Data-Driven EnviroLab, NewClimate Institute, Oxford Net Zero - Net Zero Tracker (2023)
   - Processing: Our World in Data with minor processing
   - URL: https://ourworldindata.org/
   - Accessed: October 2025
   - Variables: Country, Net-zero target status, Target year

### Statistical Methods References

- Pearson, K. (1895). Notes on regression and inheritance. *Proceedings of the Royal Society of London*, 58, 240-242.
- Spearman, C. (1904). The proof and measurement of association between two things. *American Journal of Psychology*, 15, 72-101.
- Cohen, J. (1988). *Statistical power analysis for the behavioral sciences* (2nd ed.). Lawrence Erlbaum Associates.
- Welch, B. L. (1947). The generalization of 'Student's' problem when several different population variances are involved. *Biometrika*, 34(1-2), 28-35.

### External Context (if used)

[Add any news articles, policy reports, or academic papers you referenced for interpretation]

---

**Assignment Completed By:** Kartavya Jharwal  
**Student ID:** [Your ID]  
**Date of Completion:** October [XX], 2025  
**Course:** BAN-0200 Fundamentals of Business Analytics  
**Professor:** Prof Glen Joseph  
**Institution:** Hult International Business School

**Acknowledgments:** Data provided by Our World in Data, World Bank, and Net Zero Tracker consortium.

**Word Count:** [Estimated: 3,500-4,000 words including code comments and markdown]
```

---

## ✅ FINAL PRE-SUBMISSION CHECKLIST

### Before Uploading:
- [ ] Run all cells in Colab from top to bottom (Restart Runtime → Run All)
- [ ] Verify all outputs are visible (no "Cell not executed" messages)
- [ ] Check all visualizations render correctly
- [ ] Add Part 2 visualization code
- [ ] Complete interpretation sections with actual results
- [ ] Update references with your name and date
- [ ] Spell check all markdown cells
- [ ] Remove any debugging print statements (if any)
- [ ] Ensure file is named appropriately (e.g., `Jharwal_Kartavya_A1.ipynb`)
- [ ] Download and re-upload to verify file integrity
- [ ] Check file size is reasonable (<10MB typically)

### After Uploading:
- [ ] Download your submitted file
- [ ] Open in Colab to verify it's complete
- [ ] Check all cells executed properly
- [ ] Verify no missing sections

---

## 🎓 OVERALL ASSESSMENT

**Current Status:** VERY STRONG - Approximately 95% complete

**Strengths:**
- Exceptional statistical rigor
- Comprehensive hypothesis testing
- Professional code quality
- Clear documentation
- Goes beyond requirements with supplementary analyses

**Needs:**
- Part 2 visualization (critical)
- Complete interpretation sections
- Final references polish

**Recommendation:** Add the missing visualization and interpretation, then this is an **A-grade** assignment. The statistical approach is sophisticated and well-executed.

**Estimated Time to Complete:** 1-2 hours for additions

---

Good luck with your submission! 🚀
