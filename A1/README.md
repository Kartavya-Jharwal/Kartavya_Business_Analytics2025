# 🌍 CarbonSeer: Professional Carbon Risk Analytics Platform

> **See the carbon future. Now.**  
> Data-driven intelligence for CBAM compliance, supply chain carbon risk, and ESG investment screening.

---

## 🎯 What is CarbonSeer?

**CarbonSeer** is a professional-grade carbon risk analytics platform built for **carbon consultants**, **ESG analysts**, and **supply chain strategists**. It transforms GDP, CO₂ emissions, and net-zero commitment data into **actionable intelligence** for navigating the **EU Carbon Border Adjustment Mechanism (CBAM)** and **ETS2** regulatory landscape.

### The Name: Carbon + Seer = Future Vision

- **Carbon**: The core commodity of climate regulation
- **Seer**: One who foresees the future
- **CarbonSeer**: **Predictive carbon intelligence** for regulatory compliance and investment decisions

In a world where **CBAM (2026)** and **ETS2 (2027)** will reshape global trade, you need to **see beyond the present**—identify which nations are prepared, which are vulnerable, and where capital should flow.

---

## 🚀 Key Features

### 📊 Rigorous Statistical Analysis
- **Hypothesis testing** with Pearson & Spearman correlations
- **ANOVA** across GDP categories with effect size reporting (R², Cohen's d)
- **Chi-square tests** for net-zero commitment patterns
- **195 countries** analyzed across **50+ years** of data

### 💼 Investment Intelligence
- **Commitment Strength Scoring (0-5)**: Distinguish empty pledges from legally binding targets
- **Country-level risk assessment**: CBAM tariff exposure screening
- **Supply chain carbon mapping**: Identify high-risk jurisdictions in your value chain
- **Portfolio screening**: Flag companies with exposure to non-committed countries

### ✨ Interactive Platform
- **Fast Mode**: Instant analysis with sampling for time-sensitive decisions
- **Custom visualization builder**: Create client-ready charts in seconds
- **Multi-format export**: CSV, Excel, PNG for presentations and reports
- **Real-time filtering**: Country, year, GDP category, commitment strength

### 🎨 Award-Worthy Design
- **Glassmorphism UI** with smooth animations
- **Modern color palette**: Professional beige, purple, and teal scheme
- **Mobile-responsive**: Works beautifully on all devices
- **Accessibility**: WCAG-compliant design patterns

---

## 📈 Use Cases

### 1. **CBAM Compliance Strategy**
**Scenario**: Your manufacturing company imports steel from 15 countries. Which suppliers face carbon tariffs in 2026?

**CarbonSeer Solution**:
1. Filter Data Explorer to show high-GDP countries without legal commitments
2. Cross-reference with your supplier list
3. Export risk assessment for procurement team
4. **Result**: Identify 40% of suppliers facing 10-30% cost increases

### 2. **ESG Investment Screening**
**Scenario**: You're evaluating a portfolio of emerging market bonds. Which countries demonstrate climate leadership?

**CarbonSeer Solution**:
1. Analyze correlation between GDP and emissions (Hypothesis 1)
2. Screen for "In Law" or "Achieved" net-zero commitments (strength 4-5)
3. Identify countries decoupling GDP from emissions
4. **Result**: Build a "green bond watchlist" with regulatory certainty

### 3. **Client Briefings**
**Scenario**: A client asks, "Should we expand operations to Country X?"

**CarbonSeer Solution**:
1. Check Country X's commitment strength
2. Compare emissions per capita to GDP peers
3. Generate custom scatter plots for presentation
4. **Result**: 5-minute briefing with statistical rigor

---

## 🛠️ Technology Stack

### Core Technologies
- **Python 3.12+**: Modern, type-safe Python
- **Streamlit 1.50+**: Fast, beautiful web applications
- **Plotly 6.3+**: Interactive, publication-quality visualizations
- **Pandas 2.2+**: Efficient data manipulation
- **SciPy 1.11+**: Statistical analysis and hypothesis testing

### Package Management
- **UV Package Manager**: Lightning-fast dependency resolution
- **Pyproject.toml**: Modern Python packaging standards
- **Virtual Environment**: Isolated, reproducible environments

### Data Sources
- **World Bank**: GDP per capita (constant 2015 US$)
- **Global Carbon Budget**: CO₂ emissions per capita
- **Net Zero Tracker**: Net-zero commitment status and targets

---

## 📦 Installation & Setup

### Prerequisites
- **Python 3.12+** installed
- **UV package manager** installed ([install UV](https://github.com/astral-sh/uv))

### Quick Start

```bash
# 1. Clone the repository
git clone https://github.com/Kartavya-Jharwal/Kartavya_Business_Analytics2025.git
cd Kartavya_Business_Analytics2025/A1

# 2. Install dependencies using UV
uv sync

# 3. Run the Streamlit app
uv run streamlit run app.py

# 4. Open your browser
# App will be available at http://localhost:8501
```

### Alternative: Using pip

```bash
# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

---

## 📂 Project Structure

```
A1/
├── app.py                          # Main entry point
├── Home.py                         # Landing page
├── pages/
│   ├── Analysis.py                 # Statistical analysis
│   └── Data_Explorer.py            # Interactive data explorer
├── utils/
│   ├── __init__.py                 # Package initialization
│   ├── data_loader.py              # Data loading and processing
│   ├── analysis.py                 # Statistical computations
│   ├── styling.py                  # CSS and theming
│   └── splash.py                   # Loading screens
├── assets/
│   ├── CarbonSeer_png.png          # Logo
│   └── Carbonseer.png              # Lockup
├── gdp-per-capita-worldbank-constant-usd/
│   └── gdp-per-capita-worldbank-constant-usd.csv
├── co-emissions-per-capita/
│   └── co-emissions-per-capita.csv
├── net-zero-targets/
│   └── net-zero-targets.csv
├── pyproject.toml                  # Package configuration
└── README.md                       # This file
```

---

## 📊 Key Insights from Analysis

### Hypothesis 1: GDP & CO₂ Emissions
**Finding**: Strong positive correlation (r ≈ 0.67, R² = 0.45)

- High-GDP countries emit **4-5× more CO₂ per capita** than low-GDP countries
- **Statistical significance**: p < 0.001 (ANOVA F = 1,847)
- **Business implication**: High-income economies face greater CBAM exposure

### Hypothesis 2: GDP & Net-Zero Commitments
**Finding**: Significant association (χ² = 286.4, p < 0.001, Cramér's V = 0.23)

- High-GDP countries are **2-3× more likely** to have legally binding targets
- Only **~40% of high-GDP countries** have "In Law" status
- **Business implication**: 60% of high-GDP suppliers lack regulatory protection

---

## 🎓 Academic Context

This project was developed as a **dual-purpose academic assignment** for:

### Business Analytics (BAN-0200) — Prof. Glen Joseph
- Statistical hypothesis testing
- Correlation and regression analysis
- ANOVA and effect size quantification
- Chi-square tests for categorical data

### Creativity in Advertising & Marketing (DSN-0303) — Prof. Lindsay Butcher
- Brand design for **Redshaw Advisors** carbon consulting
- **CarbonSeer** as standalone microsite demonstrating data-driven insights
- Visual identity, UI/UX design, marketing positioning

**Institution**: Hult International Business School  
**Author**: Kartavya Jharwal  
**Year**: 2025

---

## 🚀 Performance & Fast Mode

### Fast Mode Features
- **Sampling**: Uses 2,000 samples instead of full dataset for instant feedback
- **Deferred loading**: Heavy visualizations load on-demand
- **Caching**: `@st.cache_data` for all data operations
- **Toggle**: Enable/disable in sidebar on any page

### Performance Benchmarks
- **Data loading**: <2 seconds (local), <5 seconds (GitHub raw)
- **Correlation analysis**: <1 second (Fast Mode), <3 seconds (Full Mode)
- **Visualization rendering**: <2 seconds (Plotly with theming)
- **Page navigation**: Instant (Streamlit multi-page architecture)

---

## 🌐 Deployment Options

### Option 1: Streamlit Community Cloud
```bash
# Push to GitHub
git push origin main

# Deploy on Streamlit Cloud
# 1. Go to share.streamlit.io
# 2. Connect your GitHub repo
# 3. Set main file: app.py
# 4. Deploy!
```

### Option 2: Heroku
```bash
# Create Procfile (already included)
web: streamlit run app.py --server.port=$PORT

# Deploy to Heroku
heroku create carbonseer-demo
git push heroku main
```

### Option 3: Docker
```dockerfile
# Dockerfile (create if needed)
FROM python:3.12-slim
WORKDIR /app
COPY . .
RUN pip install uv && uv sync
CMD ["uv", "run", "streamlit", "run", "app.py"]
```

---

## 📖 User Guide

### For Carbon Consultants
1. **Open Analysis page**: Review statistical findings
2. **Use Data Explorer**: Filter by country/year/GDP category
3. **Generate custom charts**: Create client-ready visualizations
4. **Export data**: Download CSV/Excel for client presentations

### For ESG Analysts
1. **Screen countries**: High GDP + No legal commitment = High risk
2. **Compare commitment strength**: Use 0-5 scoring system
3. **Track emissions trends**: Time series analysis by GDP category
4. **Portfolio screening**: Identify companies with carbon exposure

### For Supply Chain Managers
1. **Map supplier countries**: Check CBAM exposure
2. **Risk assessment**: High GDP without commitments = tariff risk
3. **Diversification**: Identify lower-risk alternative markets
4. **Cost modeling**: Estimate carbon tariff impact (10-100€/tonne)

---

## 🤝 Contributing

Contributions are welcome! Please follow these guidelines:

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature/amazing-feature`
3. **Commit your changes**: `git commit -m 'Add amazing feature'`
4. **Push to branch**: `git push origin feature/amazing-feature`
5. **Open a Pull Request**

---

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- **Data Sources**: World Bank, Global Carbon Budget, Net Zero Tracker
- **Faculty**: Prof. Glen Joseph (BAN-0200), Prof. Lindsay Butcher (DSN-0303)
- **Institution**: Hult International Business School
- **Frameworks**: Streamlit, Plotly, Pandas, SciPy

---

## 📞 Contact

**Kartavya Jharwal**  
🌐 Portfolio: [kartavya-jharwal.github.io](https://kartavya-jharwal.github.io)  
📧 Email: [contact via portfolio]  
💼 LinkedIn: [linkedin.com/in/kartavya-jharwal](https://linkedin.com/in/kartavya-jharwal)  

---

## 🔮 Future Enhancements

- [ ] **ML Predictions**: Forecast emissions trajectories using ARIMA/Prophet
- [ ] **Sector-Specific Analysis**: CBAM initially targets cement, steel, aluminum
- [ ] **API Integration**: Real-time data from Carbon Brief, IEA
- [ ] **Automated Reporting**: Generate PDF reports with Python/LaTeX
- [ ] **Multi-Language Support**: i18n for EU market

---

<div align="center">

**Built with ❤️ by Kartavya Jharwal**  
*Seeing the carbon future, one dataset at a time.*

[⭐ Star on GitHub](https://github.com/Kartavya-Jharwal/Kartavya_Business_Analytics2025) | [🐛 Report Bug](https://github.com/Kartavya-Jharwal/Kartavya_Business_Analytics2025/issues) | [💡 Request Feature](https://github.com/Kartavya-Jharwal/Kartavya_Business_Analytics2025/issues)

</div>
