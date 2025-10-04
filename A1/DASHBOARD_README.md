# Business Analytics A1 Dashboard 🌍

An elegant, interactive Streamlit dashboard analyzing the relationships between GDP per capita, CO₂ emissions, and net-zero climate commitments across 190+ countries.

![Dashboard Preview](https://img.shields.io/badge/Status-Active-success)
![Python](https://img.shields.io/badge/Python-3.12+-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.50+-red)

## 🎯 Features

- **Interactive Data Exploration**: Filter by country, year range, and GDP categories
- **Beautiful Visualizations**: Plotly charts with custom theming inspired by modern carbon tracker designs
- **Statistical Analysis**: Real-time correlation calculations, hypothesis testing, and effect size measurements
- **Responsive Design**: Works seamlessly on desktop and mobile
- **PDF Reports**: Automated GitHub Actions workflow for beautiful PDF generation

## 🚀 Quick Start

### Prerequisites

- Python 3.12+
- [UV package manager](https://docs.astral.sh/uv/) (recommended) or pip

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Kartavya-Jharwal/Kartavya_Business_Analytics2025.git
   cd Kartavya_Business_Analytics2025/A1
   ```

2. **Install dependencies with UV (recommended)**
   ```bash
   uv sync
   ```

   Or with pip:
   ```bash
   pip install -e .
   ```

3. **Run the dashboard**
   ```bash
   uv run streamlit run app.py
   ```

   Or with pip:
   ```bash
   streamlit run app.py
   ```

4. **Open your browser** to `http://localhost:8501`

## 📊 Dashboard Structure

```
├── app.py                 # Main landing page
├── pages/
│   ├── 1_📊_Part_1.py    # GDP vs CO₂ analysis
│   ├── 2_🎯_Part_2.py    # Net-zero commitments
│   └── 3_🔬_Methodology.py # Statistical methods
├── utils/
│   ├── data_loader.py     # Data processing functions
│   └── styling.py         # Custom CSS and themes
├── .streamlit/
│   └── config.toml        # Streamlit configuration
└── templates/
    └── custom_report.tpl  # PDF export template
```

## 🎨 Design Philosophy

The dashboard features a modern, minimalist design inspired by carbon footprint tracking applications:

- **Color Palette**: Soft beige backgrounds (#F5F3F0), muted purples (#8B7D9B), teals (#6B9B91), and earth tones
- **Typography**: Inter font family for elegant, readable text
- **Interactions**: Smooth transitions, hover effects, and responsive components
- **Data Viz**: Custom Plotly themes matching the color scheme

## 📄 PDF Generation

Automated PDF reports are generated via GitHub Actions on every push:

```bash
# Local PDF generation
uv run jupyter nbconvert \
  --to html \
  --template templates/custom_report.tpl \
  --output-dir outputs \
  assignment.ipynb
```

PDFs are available as:
- GitHub Actions artifacts (90-day retention)
- GitHub Releases (permanent)

## 🌐 Deployment

### Streamlit Cloud (Recommended)

1. Fork this repository
2. Go to [streamlit.io/cloud](https://streamlit.io/cloud)
3. Click "New app"
4. Select your fork, branch `main`, and path `A1/app.py`
5. Deploy!

### Docker

```dockerfile
FROM python:3.12-slim
WORKDIR /app
COPY . .
RUN pip install uv && uv sync
EXPOSE 8501
CMD ["uv", "run", "streamlit", "run", "app.py"]
```

Build and run:
```bash
docker build -t analytics-dashboard .
docker run -p 8501:8501 analytics-dashboard
```

## 📚 Data Sources

- **GDP per Capita**: World Bank & OECD national accounts data (via Our World in Data)
- **CO₂ Emissions**: Global Carbon Budget 2024 (via Our World in Data)
- **Net-Zero Targets**: Net Zero Tracker 2023 - ECIU, Data-Driven EnviroLab, NewClimate Institute, Oxford Net Zero

All datasets are included in the repository under their respective folders with proper attribution.

## 🔧 Development

### Project Structure

```
A1/
├── assignment.ipynb       # Original Jupyter notebook
├── app.py                 # Streamlit app entry point
├── pages/                 # Multi-page app structure
├── utils/                 # Helper functions
├── assets/                # Images and static files
├── outputs/               # Generated PDFs (gitignored)
└── .github/workflows/     # CI/CD automation
```

### Adding New Pages

Create a new file in `pages/` following the naming convention:
```python
# pages/4_📈_New_Page.py
import streamlit as st
from utils import load_gdp_data, get_custom_css

st.set_page_config(page_title="New Page", page_icon="📈")
st.markdown(get_custom_css(), unsafe_allow_html=True)

st.title("📈 New Page")
# Your code here
```

Streamlit automatically adds it to the sidebar navigation!

### Custom Styling

Modify `utils/styling.py` to adjust colors, fonts, or add new CSS classes:

```python
def get_custom_css():
    return """
    <style>
    .your-custom-class {
        /* Your styles */
    }
    </style>
    """
```

## 🧪 Running Tests

```bash
# Install dev dependencies
uv sync --dev

# Run tests (when available)
pytest tests/
```

## 📖 Assignment Context

This dashboard accompanies **Assignment A1** for BAN-0200 Business Analytics at Hult International Business School.

**Research Questions:**
1. Is there a statistically significant relationship between GDP per capita and CO₂ emissions per capita?
2. Do wealthier countries (higher GDP) have stronger net-zero commitments?

**Statistical Methods:**
- Pearson & Spearman correlation
- One-way ANOVA
- Chi-square tests
- Effect size calculations (R², Cohen's d, Cramér's V)

## 🤝 Contributing

This is an academic assignment, but suggestions are welcome!

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is created for educational purposes. Data sources retain their original licenses (primarily Creative Commons BY).

## 👤 Author

**Kartavya Jain**
- Institution: Hult International Business School
- Course: BAN-0200 Business Analytics
- GitHub: [@Kartavya-Jharwal](https://github.com/Kartavya-Jharwal)

## 🙏 Acknowledgments

- **Data Providers**: World Bank, OECD, Global Carbon Project, Net Zero Tracker
- **Our World in Data**: For data processing and visualization inspiration
- **Hult IBS**: For the learning opportunity
- **Prof. Glen Joseph**: Course instructor

---

**Made with** ❤️ **and** ☕ **for Business Analytics**

*Last updated: October 2025*
