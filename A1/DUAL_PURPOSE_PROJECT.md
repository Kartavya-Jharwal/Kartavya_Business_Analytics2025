# CarbonSeer: Dual-Purpose Project Overview

## 🎯 Project Identity

**CarbonSeer** is an interdisciplinary project bridging two academic disciplines:

### 1️⃣ **Business Analytics (BAN-0200)**
**Professor:** Glen Joseph  
**Focus:** Quantitative analysis and statistical rigor

**Core Deliverables:**
- Statistical hypothesis testing on GDP, CO₂ emissions, and net-zero commitments
- Correlation analysis (Pearson & Spearman) with R² quantification
- ANOVA testing across GDP categories
- Chi-square tests for commitment patterns
- Comprehensive effect size reporting (Cohen's d, η², Cramér's V)
- Business implications for CBAM (Carbon Border Adjustment Mechanism) compliance

### 2️⃣ **Creativity in Advertising & Marketing (DSN-0303)**
**Professor:** Lindsay Butcher  
**Focus:** Brand design and creative storytelling

**Core Deliverables:**
- Brand identity development for **Redshaw Advisors** (carbon consulting company)
- Demo microsite showcasing data-driven carbon consulting services
- Visual design and UI/UX implementation
- Marketing positioning and brand narrative
- Integration of complex data analysis into accessible brand storytelling

---

## 🏢 About Redshaw Advisors

**Redshaw Advisors** is a carbon consulting company that provides:
- Supply chain carbon risk assessment
- CBAM compliance strategy
- Net-zero transition planning
- Carbon accounting and reporting
- Regulatory navigation for EU carbon policies

**CarbonSeer** serves as a **standalone demo microsite** within Redshaw Advisors' brand portfolio, illustrating how data analytics can drive business strategy in the era of carbon regulations.

---

## 📊 Technical Implementation

### Architecture
- **Frontend:** Streamlit multi-page application
- **Data Layer:** CSV-based datasets with pandas processing
- **Analysis:** Statistical computations using scipy, numpy
- **Visualization:** Plotly and matplotlib with custom theming
- **Styling:** Custom CSS aligned with brand identity

### Key Features
1. **Interactive Dashboard** - Overview metrics and data loading
2. **Assignment Analysis Page** - 10 navigable sections with statistical deep-dives
3. **Data Visualizations** - Custom color schemes and responsive charts
4. **Statistical Testing** - Comprehensive hypothesis testing suite
5. **Business Intelligence** - Translation of statistical findings into business strategy

---

## 🎨 Design Philosophy

### Brand Integration
- **Color Palette:** Custom colors reflecting Redshaw Advisors' visual identity
- **Typography:** Inter font family for professional, modern aesthetic
- **Layout:** Wide format with responsive columns for data-dense content
- **Theming:** Consistent visual language across all pages

### User Experience
- **Navigation:** Sidebar with section selection for easy exploration
- **Progressive Disclosure:** Complex analysis presented in digestible sections
- **Interactive Controls:** Year selection, analysis type toggles, dynamic filtering
- **Accessibility:** Clear visual hierarchy and readable typography

---

## 📈 Business Context

### EU Carbon Regulations
- **CBAM 2026:** Carbon tariffs on imports from countries without net-zero commitments
- **ETS2 2027:** Extended emissions trading for buildings and transport

### Strategic Insights
CarbonSeer demonstrates how quantitative analysis can:
1. Identify high-risk supply chain partners (low GDP, no legal commitments)
2. Assess regulatory exposure by country and sector
3. Support supplier diversification strategies
4. Inform carbon reduction investment priorities

---

## 🎓 Academic Learning Outcomes

### Business Analytics Skills
- Advanced statistical hypothesis testing
- Effect size interpretation and reporting
- Data quality assessment and cleaning
- Assumption validation (normality, homogeneity of variance)
- Statistical visualization best practices
- Critical interpretation of results with business context

### Marketing & Design Skills
- Brand identity development from concept to execution
- Data storytelling and visual communication
- UI/UX design for data-dense applications
- Marketing positioning for B2B services
- Integration of technical content with brand narrative
- Microsite design as a marketing tool

---

## 🚀 Running CarbonSeer

### Setup
```bash
# Install UV package manager
# Visit: https://docs.astral.sh/uv/

# Install dependencies
uv sync

# Run the application
uv run streamlit run app.py
```

### Access
- **Local URL:** http://localhost:8501
- **Main Dashboard:** Landing page with project overview
- **Assignment Analysis:** Complete statistical analysis (pages/Experiment.py)

---

## 📁 Project Structure

```
CarbonSeer/
├── app.py                          # Main dashboard (landing page)
├── pages/
│   └── Experiment.py               # Complete assignment analysis
├── utils/
│   ├── data_loader.py             # Data loading and processing
│   ├── analysis.py                # Statistical functions
│   ├── styling.py                 # Custom CSS and theming
│   └── splash.py                  # Loading screens
├── assets/                         # Images and brand assets
├── gdp-per-capita-worldbank-constant-usd/
├── co-emissions-per-capita/
├── net-zero-targets/
├── templates/
│   └── custom_report.tpl          # PDF export template
└── outputs/                        # Generated reports
```

---

## 🎯 Key Achievements

### Quantitative Rigor
✅ Comprehensive statistical testing with multiple methods  
✅ Effect size reporting for practical significance  
✅ Assumption validation before parametric tests  
✅ Both parametric and non-parametric approaches  
✅ Confidence intervals and hypothesis testing at α = 0.05  

### Creative Excellence
✅ Professional brand identity aligned with consulting industry  
✅ Accessible presentation of complex statistical content  
✅ Interactive user experience with Streamlit  
✅ Custom styling and visual design  
✅ Demo microsite demonstrating real business value  

### Business Impact
✅ Actionable insights for CBAM compliance strategy  
✅ Supply chain carbon risk assessment framework  
✅ Translation of statistics into business intelligence  
✅ Strategic recommendations for carbon management  

---

## 📝 Citation & Attribution

**Prepared by:** Kartavya Jharwal  
**Institutions:** Business Analytics (BAN-0200) × Marketing Design (DSN-0303)  
**Due Date:** October 24, 2025  

**Data Sources:**
- GDP per capita: World Bank (constant 2015 USD) via Our World in Data
- CO₂ emissions: Global Carbon Budget via Our World in Data
- Net-zero commitments: Net Zero Tracker via Our World in Data

**Brand Context:**
CarbonSeer is a demonstration project created for academic purposes. Redshaw Advisors serves as the conceptual brand context for this microsite design and analytics showcase.

---

## 🔮 Future Enhancements

### Technical
- Real-time data updates via APIs
- User authentication for client portals
- PDF report generation with custom templates
- Export functionality for datasets and charts

### Analytical
- Sector-specific carbon risk analysis
- Time-series forecasting of commitment progression
- Machine learning for supplier risk scoring
- Integration with enterprise carbon accounting systems

### Design
- Mobile-responsive layouts
- Dark mode theme option
- Additional brand microsite pages (About, Services, Contact)
- Case study presentations of successful decarbonization

---

## 📞 Contact & Support

For questions about this project:
- **Business Analytics:** Contact Prof Glen Joseph
- **Brand Design:** Contact Prof Lindsay Butcher
- **Technical Implementation:** Refer to .github/copilot-instructions.md

---

**CarbonSeer** © 2025 - An interdisciplinary demonstration of analytics meets creative design.
