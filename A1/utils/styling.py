"""
Custom styling and design utilities inspired by carbon footprint tracker aesthetic.
"""


def get_custom_css():
    """
    Return custom CSS for elegant, minimalist design.
    Inspired by beige/purple/teal carbon tracker interface.
    """
    return """
    <style>
    /* Import elegant font */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    /* Global styles */
    * {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    }
    
    /* Main container */
    .main {
        background-color: #F5F3F0;
    }
    
    /* Hero section */
    .hero-section {
        background: linear-gradient(135deg, #8B7D9B 0%, #A89BB3 100%);
        padding: 3rem 2rem;
        border-radius: 20px;
        margin-bottom: 2rem;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
        color: white;
    }
    
    .hero-title {
        font-size: 3.5rem;
        font-weight: 700;
        margin-bottom: 1rem;
        line-height: 1.2;
    }
    
    .hero-subtitle {
        font-size: 1.3rem;
        font-weight: 300;
        opacity: 0.9;
        line-height: 1.6;
    }
    
    /* Metric cards */
    .metric-card {
        background: white;
        padding: 2rem;
        border-radius: 16px;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.06);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        border-left: 4px solid #8B7D9B;
    }
    
    .metric-card:hover {
        transform: translateY(-4px);
        box-shadow: 0 8px 30px rgba(0, 0, 0, 0.12);
    }
    
    .metric-value {
        font-size: 2.5rem;
        font-weight: 700;
        color: #8B7D9B;
        margin: 0.5rem 0;
    }
    
    .metric-label {
        font-size: 0.9rem;
        color: #666;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        font-weight: 500;
    }
    
    .metric-delta {
        font-size: 0.85rem;
        margin-top: 0.5rem;
    }
    
    /* Section headers */
    .section-header {
        font-size: 2rem;
        font-weight: 600;
        color: #2C2C2C;
        margin: 2.5rem 0 1.5rem 0;
        padding-left: 1rem;
        border-left: 5px solid #8B7D9B;
    }
    
    .section-subheader {
        font-size: 1.5rem;
        font-weight: 500;
        color: #4A4A4A;
        margin: 2rem 0 1rem 0;
    }
    
    /* Info boxes */
    .info-box {
        background: linear-gradient(135deg, #F5F3F0 0%, #FFFFFF 100%);
        border-left: 4px solid #8B7D9B;
        padding: 1.5rem;
        border-radius: 12px;
        margin: 1.5rem 0;
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.05);
    }
    
    .success-box {
        background: linear-gradient(135deg, #E8F5E9 0%, #F1F8E9 100%);
        border-left: 4px solid #66BB6A;
        padding: 1.5rem;
        border-radius: 12px;
        margin: 1.5rem 0;
    }
    
    .warning-box {
        background: linear-gradient(135deg, #FFF3E0 0%, #FFECB3 100%);
        border-left: 4px solid #FFA726;
        padding: 1.5rem;
        border-radius: 12px;
        margin: 1.5rem 0;
    }
    
    /* Data insights cards */
    .insight-card {
        background: white;
        padding: 1.5rem;
        border-radius: 12px;
        margin: 1rem 0;
        box-shadow: 0 2px 12px rgba(0, 0, 0, 0.05);
        border-top: 3px solid #8B7D9B;
    }
    
    .insight-number {
        font-size: 2rem;
        font-weight: 700;
        color: #8B7D9B;
        margin-right: 0.5rem;
    }
    
    /* Streamlit elements customization */
    .stMetric {
        background: white;
        padding: 1rem;
        border-radius: 12px;
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.05);
    }
    
    /* Buttons */
    .stButton > button {
        background: linear-gradient(135deg, #8B7D9B 0%, #A89BB3 100%);
        color: white;
        border: none;
        border-radius: 10px;
        padding: 0.75rem 2rem;
        font-weight: 600;
        transition: all 0.3s ease;
        box-shadow: 0 4px 12px rgba(139, 125, 155, 0.3);
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(139, 125, 155, 0.4);
    }
    
    /* Sliders */
    .stSlider > div > div > div {
        background-color: #8B7D9B;
    }
    
    /* Selectbox */
    .stSelectbox > div > div {
        border-radius: 8px;
    }
    
    /* Data tables */
    .dataframe {
        border-radius: 10px;
        overflow: hidden;
        box-shadow: 0 2px 12px rgba(0, 0, 0, 0.08);
    }
    
    /* Sidebar */
    .css-1d391kg {
        background-color: #FFFFFF;
    }
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* Smooth transitions */
    * {
        transition: background-color 0.3s ease, color 0.3s ease;
    }
    
    /* Chart containers */
    .chart-container {
        background: white;
        padding: 2rem;
        border-radius: 16px;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.06);
        margin: 1.5rem 0;
    }
    
    /* Tabs styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 2rem;
    }
    
    .stTabs [data-baseweb="tab"] {
        border-radius: 8px 8px 0 0;
        padding: 1rem 2rem;
        font-weight: 600;
    }
    
    /* Expander styling */
    .streamlit-expanderHeader {
        background-color: #F5F3F0;
        border-radius: 8px;
        font-weight: 600;
    }
    
    /* Color palette classes */
    .color-purple { color: #8B7D9B; }
    .color-teal { color: #6B9B91; }
    .color-beige { color: #D4C5B9; }
    .color-earth { color: #A68B7B; }
    
    .bg-purple { background-color: #8B7D9B; }
    .bg-teal { background-color: #6B9B91; }
    .bg-beige { background-color: #F5F3F0; }
    
    /* Loading animation container */
    .loading-container {
        display: flex;
        justify-content: center;
        align-items: center;
        padding: 3rem;
    }
    
    /* Footer styling */
    .dashboard-footer {
        text-align: center;
        padding: 2rem;
        color: #666;
        font-size: 0.85rem;
        margin-top: 4rem;
        border-top: 2px solid #E0E0E0;
    }
    </style>
    """


def get_plotly_theme():
    """
    Return Plotly theme configuration matching the design system.
    """
    return {
        "layout": {
            "paper_bgcolor": "#FFFFFF",
            "plot_bgcolor": "#F5F3F0",
            "font": {"family": "Inter, sans-serif", "size": 12, "color": "#2C2C2C"},
            "colorway": [
                "#8B7D9B",  # Purple
                "#C9A9A6",  # Dusty rose
                "#6B9B91",  # Teal
                "#A68B7B",  # Earth
                "#D4C5B9",  # Beige
                "#98887D",  # Taupe
            ],
            "title": {
                "font": {"size": 20, "family": "Inter, sans-serif", "color": "#2C2C2C"}
            },
            "xaxis": {
                "gridcolor": "#E0E0E0",
                "linecolor": "#CCCCCC",
            },
            "yaxis": {
                "gridcolor": "#E0E0E0",
                "linecolor": "#CCCCCC",
            },
        }
    }


def create_metric_card_html(value, label, delta=None, delta_color="normal"):
    """
    Create a custom HTML metric card.
    """
    delta_html = ""
    if delta:
        color_map = {"normal": "#666", "positive": "#66BB6A", "negative": "#EF5350"}
        color = color_map.get(delta_color, "#666")
        delta_html = f'<div class="metric-delta" style="color: {color};">{delta}</div>'

    return f"""
    <div class="metric-card">
        <div class="metric-label">{label}</div>
        <div class="metric-value">{value}</div>
        {delta_html}
    </div>
    """
