# CarbonSeer

**A Dual-Purpose Analytics & Brand Design Project**

CarbonSeer is an interdisciplinary microsite combining quantitative business analytics with creative brand design. Built as a demonstration platform for **Redshaw Advisors** (a carbon consulting company), it showcases data-driven carbon risk analysis through an interactive web application.

## 🎓 Academic Context

### **Business Analytics (BAN-0200)** - Prof Glen Joseph
Statistical analysis exploring:
- GDP per capita vs CO₂ emissions correlation
- Net-zero commitment patterns across economic development levels
- CBAM (Carbon Border Adjustment Mechanism) business implications
- Hypothesis testing with comprehensive effect size reporting

### **Creativity in Advertising & Marketing (DSN-0303)** - Prof Lindsay Butcher
Brand design work for Redshaw Advisors:
- Visual identity and UI/UX design
- Data storytelling and marketing positioning
- Standalone microsite demonstrating consulting capabilities
- Integration of analytical rigor with creative brand narrative

## 🌍 Project Purpose

CarbonSeer serves as a **demo microsite** for Redshaw Advisors, illustrating how quantitative carbon risk analysis can be presented as an accessible, visually compelling tool for business decision-making in the context of upcoming EU carbon regulations (CBAM 2026, ETS2 2027).

## Features

- **Interactive Dashboard**: Overview of global carbon risk metrics
- **Assignment Analysis**: 10 navigable sections with statistical deep-dives
- **Data Visualizations**: Plotly charts with custom theming
- **Statistical Testing**: ANOVA, Chi-square, correlation analysis with effect sizes
- **Business Intelligence**: Supply chain carbon risk assessment insights

## Setup and Installation

1. Make sure you have `uv` installed. If not, install it from [https://docs.astral.sh/uv/](https://docs.astral.sh/uv/)

2. Clone or navigate to this directory

3. Install dependencies:
   ```bash
   uv sync
   ```

## Running the Application

To run the Streamlit app:

```bash
uv run streamlit run app.py
```

This will start the Streamlit server and you can view the app in your browser at `http://localhost:8501`

## Static interactive site

This repository now includes a static single-page interactive site built for quick local exploration of the CSV datasets.

To view it locally:

1. From the repository root, start a simple HTTP server so the browser can fetch the CSV files by relative paths:

```powershell
python -m http.server 8000
```

2. Open your browser to http://localhost:8000/site/

The `site/` folder contains `index.html`, `script.js`, and `styles.css` and uses Plotly to render interactive charts from the CSVs present at the repository root.

## Project Structure

```
├── app.py              # Main Streamlit application
├── pyproject.toml      # Project configuration and dependencies
├── uv.lock            # Lock file for reproducible builds
└── README.md          # This file
```

## Dependencies

- **Streamlit**: Web app framework
- **Pandas**: Data manipulation and analysis
- **Numpy**: Numerical computing

## Features Demonstrated

- Page navigation with sidebar
- Interactive widgets (text input, sliders, selectbox, etc.)
- Data display with DataFrames
- Various chart types (line, bar, scatter, area)
- Metrics and statistics display
- Color picker and settings
- Responsive layout with columns

## Customization

You can easily extend this app by:
- Adding new pages to the navigation
- Incorporating your own datasets
- Adding more chart types
- Implementing user authentication
- Adding database connectivity

Enjoy building with Streamlit and uv! 🚀
