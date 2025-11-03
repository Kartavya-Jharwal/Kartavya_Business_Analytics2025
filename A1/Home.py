"""
CarbonSeer - Quantitative Carbon Risk Analytics Platform

Award-winning micro-tool for carbon consultants and quantitative analysts.
Provides rigorous statistical analysis of GDP, CO₂ emissions, and net-zero commitments
for investment screening, supply chain risk assessment, and CBAM compliance strategy.
"""

import streamlit as st
from pathlib import Path
from utils.splash import show_splash_overlay, clear_splash
from utils import (
    load_gdp_data,
    load_co2_data,
    load_netzero_data,
    merge_gdp_co2,
    create_gdp_categories,
    create_commitment_strength,
    get_custom_css,
    render_sidebar_resources,
)
from utils.styling import (
    render_global_branding,
    render_sticky_footer,
)

# ===== PATHS AND CSS =====
assets_dir = Path(__file__).parent / "assets"
logo_path = assets_dir / "CarbonSeer_png.png"
lockup_path = assets_dir / "CarbonSeer.png"

# Global UI toggles (persist in session)
if "fast_mode" not in st.session_state:
    st.session_state.fast_mode = True  # default to fast interactions

# Sidebar toggle
with st.sidebar:
    st.markdown("### ⚙️ Preferences")
    st.toggle("⚡ Fast Mode", value=st.session_state.fast_mode, key="fast_toggle_home",
             help="Use sampling and defer heavy visuals for instant feedback.",
             on_change=lambda: setattr(st.session_state, 'fast_mode', st.session_state.fast_toggle_home))

st.markdown(get_custom_css("light"), unsafe_allow_html=True)


# ===== DATA LOADING FUNCTION =====
@st.cache_data
def load_all_data(source: str = "auto"):
    """Load and prepare all datasets with caching for optimal performance."""
    gdp_df = load_gdp_data(source)
    co2_df = load_co2_data(source)
    netzero_df = load_netzero_data(source)
    merged_df = merge_gdp_co2(gdp_df, co2_df)
    merged_df = create_gdp_categories(merged_df)
    netzero_df = create_commitment_strength(netzero_df)
    return gdp_df, co2_df, netzero_df, merged_df


# ===== SPLASH SCREEN & DATA LOADING LOGIC =====
if "data_loaded" not in st.session_state:
    st.session_state.data_loaded = False

# Show splash screen via an overlay that will be removed via JS
if not st.session_state.data_loaded:
    show_splash_overlay(logo_path=logo_path)

# Load data. The splash screen is visible during this time.
# Data source selection
with st.sidebar:
    st.markdown("### 🗄️ Data Source")
    data_source_label = st.selectbox(
        "Load data from:", ["Auto (Local→GitHub)", "GitHub (raw)", "Local files"], index=0
    )
source_map = {"Auto (Local→GitHub)": "auto", "GitHub (raw)": "github", "Local files": "local"}
data_source = source_map[data_source_label]
st.session_state.data_source = data_source  # Persist for other pages

gdp_df, co2_df, netzero_df, merged_df = load_all_data(data_source)

# Once data is loaded, mark as complete and trigger splash removal
if not st.session_state.data_loaded:
    st.session_state.data_loaded = True
    clear_splash()
    st.rerun()

# The rest of the app renders only after the rerun
# triggered by the completion of data loading.

# ===== ADD LOGO TO SIDEBAR =====
st.logo(str(logo_path), icon_image=str(logo_path))

# ===== RENDER SIDEBAR RESOURCES =====
render_sidebar_resources()

# Add scroll progress indicator
st.markdown(
    """
<script>
window.addEventListener('scroll', function() {
    var winScroll = document.body.scrollTop || document.documentElement.scrollTop;
    var height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
    var scrolled = (winScroll / height) * 100;
    var progressBar = document.getElementById('scrollProgress');
    if (progressBar) {
        progressBar.style.transform = 'scaleX(' + (scrolled / 100) + ')';
    }
});
</script>
<div id="scrollProgress" class="scroll-progress"></div>
""",
    unsafe_allow_html=True,
)

# Render global Hult branding in top-right
render_global_branding()

# ===== STUNNING HERO SECTION =====
# Hero background

# Logo in hero (centered)
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image(str(lockup_path), width="stretch")
    st.html("""
    <div class='hero-section' style='margin-top: 2rem;'></div>
    <div style='position: relative; z-index: 2;'></div>
    """)
# Hero text + punchy copy + CTA
st.html("""
    <div class='hero-subtitle' style='animation-delay: 0.2s;'>
        See the carbon future. Now.
    </div>
    <div style='margin-top: 1.5rem; animation: fadeInUp 0.8s ease-out 0.4s backwards;'>
        <p style='font-size: 1.15rem; opacity: 0.95; max-width: 760px; margin: 0 auto; line-height: 1.9;'>
            CarbonSeer is built to <strong>show, not tell</strong>—turning GDP, CO₂ and commitments into instant, defensible signals.
            A bold tool for sustainability heads and quants who need decisions in seconds, not slides in weeks.
        </p>
    </div>
    <div style='display:flex; gap: 1rem; justify-content:center; margin-top: 2rem; animation: fadeInUp 0.7s ease-out 0.6s backwards;'>
        <span class='stButton'>
            <button id='cta-analyze' style='font-size: 1rem;'>⚡ Run Fast Analysis</button>
        </span>
        <span class='stButton'>
            <button id='cta-explore' style='background:linear-gradient(135deg, rgba(139,125,155,0.2), rgba(107,155,145,0.2)); color: inherit; border:2px solid rgba(139,125,155,0.35)'>🔍 Open Data Explorer</button>
        </span>
    </div>
    <script>
      // Lightweight navigation hooks
      const go = (target) => {{
        const streamlitEvents = window.parent || window;
        // Fallback: trigger Streamlit navigation command via hash anchors if available
      }}
      document.getElementById('cta-analyze')?.addEventListener('click', () => {{
        window.parent.postMessage({{ type: 'streamlit_navigate', page: 'pages/Analysis.py' }}, '*');
      }});
      document.getElementById('cta-explore')?.addEventListener('click', () => {{
        window.parent.postMessage({{ type: 'streamlit_navigate', page: 'pages/Data_Explorer.py' }}, '*');
      }});
    </script>
    <div class='scroll-indicator' onclick='window.scrollTo({{top: 800, behavior: "smooth"}})'>
        ↓
    </div>
""")

# Native CTA buttons for reliable navigation
c1, c2, _ = st.columns([1,1,2])
with c1:
    if st.button("⚡ Run Fast Analysis", use_container_width=True):
        try:
            st.switch_page("pages/Analysis.py")
        except Exception:
            st.toast("Open the Analysis page from the sidebar", icon="📊")
with c2:
    if st.button("🔍 Open Data Explorer", use_container_width=True):
        try:
            st.switch_page("pages/Data_Explorer.py")
        except Exception:
            st.toast("Open the Data Explorer from the sidebar", icon="🔍")


# ===== ACADEMIC CONTEXT - REDESIGNED =====
st.html("""
<div style='animation: fadeInUp 0.8s ease-out; margin: 3rem 0;'>
<div style='background: linear-gradient(135deg, rgba(255, 255, 255, 0.98) 0%, rgba(250, 250, 250, 0.95) 100%);
            backdrop-filter: blur(15px);
            padding: 2.5rem;
            border-radius: 20px;
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.08);
            border: 1px solid rgba(139, 125, 155, 0.1);'>
    
    <div style='text-align: center; margin-bottom: 2rem;'>
        <h2 style='font-family: "Plus Jakarta Sans", "Inter", sans-serif;
                   font-size: 2rem;
                   font-weight: 700;
                   color: #8B7D9B;
                   margin-bottom: 0.5rem;'>
            Professional Carbon Analytics
        </h2>
        <p style='color: #666; font-size: 1rem;'>Built by Quantitative Analysts, For Quantitative Analysts</p>
    </div>
    
    <div style='display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 2rem; margin-top: 2rem;'>
        <div class='insight-card' style='margin: 0;'>
            <div style='display: flex; align-items: center; margin-bottom: 1rem;'>
                <span style='font-size: 2.5rem; margin-right: 1rem;'>📊</span>
                <div>
                    <h3 style='margin: 0; font-weight: 700; color: #2C2C2C;'>Statistical Rigor</h3>
                    <p style='margin: 0; color: #666; font-size: 0.9rem;'>Hypothesis Testing & Effect Sizes</p>
                </div>
            </div>
            <p style='color: #4A4A4A; line-height: 1.6;'>
                Pearson & Spearman correlations, ANOVA with pairwise comparisons, chi-square tests,
                R² quantification, Cohen's d, and Cramér's V for robust statistical inference.
            </p>
        </div>
        
        <div class='insight-card' style='margin: 0;'>
            <div style='display: flex; align-items: center; margin-bottom: 1rem;'>
                <span style='font-size: 2.5rem; margin-right: 1rem;'>💼</span>
                <div>
                    <h3 style='margin: 0; font-weight: 700; color: #2C2C2C;'>Investment Screening</h3>
                    <p style='margin: 0; color: #666; font-size: 0.9rem;'>Country-Level Risk Assessment</p>
                </div>
            </div>
            <p style='color: #4A4A4A; line-height: 1.6;'>
                Evaluate 195 countries by carbon commitment strength, emissions trajectories,
                and CBAM compliance status for data-driven capital allocation decisions.
            </p>
        </div>
    </div>
    
    <div style='margin-top: 2rem; padding-top: 2rem; border-top: 1px solid rgba(0, 0, 0, 0.05); text-align: center;'>
        <p style='margin: 0; color: #666;'>
            <strong style='color: #8B7D9B;'>Developed by:</strong> Kartavya Jharwal |
            <strong style='color: #8B7D9B;'>Purpose:</strong> Professional Carbon Risk Analytics Tool
        </p>
    </div>
</div>
</div>
""")

st.markdown("---")

# ===== PROJECT OVERVIEW WITH STUNNING CARDS =====
st.html("""
<div class='section-header' style='animation: slideInLeft 0.6s ease-out;'>
🎯 About CarbonSeer
</div>
""")

col1, col2, col3 = st.columns(3)

with col1:
    st.html("""
<div class='metric-card' style='animation: fadeInUp 0.6s ease-out 0.2s backwards;'>
    <div class='metric-label'>QUANTITATIVE FOUNDATION</div>
    <div style='margin: 1.5rem 0; font-size: 3rem; text-align: center;'>📈</div>
    <p style='color: #4A4A4A; line-height: 1.7; font-size: 0.95rem;'>
        Rigorous statistical analysis of GDP per capita, CO₂ emissions, and net-zero commitments
        using hypothesis testing, correlation analysis, and ANOVA.
    </p>
    <div style='margin-top: 1rem; padding-top: 1rem; border-top: 1px solid rgba(0,0,0,0.05);'>
        <span style='font-weight: 600; color: #8B7D9B; font-size: 0.85rem;'>
            195 Countries • 50+ Years Data
        </span>
    </div>
</div>
""")

with col2:
    st.html("""
<div class='metric-card' style='animation: fadeInUp 0.6s ease-out 0.4s backwards;'>
    <div class='metric-label'>INVESTMENT INTELLIGENCE</div>
    <div style='margin: 1.5rem 0; font-size: 3rem; text-align: center;'>💼</div>
    <p style='color: #4A4A4A; line-height: 1.7; font-size: 0.95rem;'>
        Country-level screening for investment decisions, supply chain risk assessment,
        and CBAM compliance strategy with commitment strength scoring (0-5 scale).
    </p>
    <div style='margin-top: 1rem; padding-top: 1rem; border-top: 1px solid rgba(0,0,0,0.05);'>
        <span style='font-weight: 600; color: #8B7D9B; font-size: 0.85rem;'>
            CBAM 2026 • ETS2 2027 Ready
        </span>
    </div>
</div>
""")

with col3:
    st.html("""
<div class='metric-card' style='animation: fadeInUp 0.6s ease-out 0.6s backwards;'>
    <div class='metric-label'>INTERACTIVE PLATFORM</div>
    <div style='margin: 1.5rem 0; font-size: 3rem; text-align: center;'>✨</div>
    <p style='color: #4A4A4A; line-height: 1.7; font-size: 0.95rem;'>
        Real-time data explorer with custom filtering, visualization builder, and CSV export
        for client presentations and investment committee reports.
    </p>
    <div style='margin-top: 1rem; padding-top: 1rem; border-top: 1px solid rgba(0,0,0,0.05);'>
        <span style='font-weight: 600; color: #8B7D9B; font-size: 0.85rem;'>
            Interactive Dashboards • Data Export
        </span>
    </div>
</div>
""")

st.markdown("---")

# ===== CORE RESEARCH QUESTIONS =====
st.html("""
<div class='section-header' style='animation: slideInLeft 0.6s ease-out;'>
📊 Core Research Questions
</div>

<div style='animation: fadeInUp 0.8s ease-out;'>
<div class='info-box' style='background: linear-gradient(135deg, rgba(139, 125, 155, 0.08), rgba(107, 155, 145, 0.05));'>
    <div style='display: flex; align-items: center; margin-bottom: 1rem;'>
        <span style='font-size: 2rem; margin-right: 1rem;'>💡</span>
        <h3 style='margin: 0; font-weight: 700; color: #2C2C2C;'>Hypothesis 1</h3>
    </div>
    <p style='font-size: 1.1rem; color: #4A4A4A; margin: 0; font-style: italic;'>
        "Countries with higher GDP per capita emit more CO₂ per capita."
    </p>
</div>

<div class='info-box' style='background: linear-gradient(135deg, rgba(107, 155, 145, 0.08), rgba(139, 125, 155, 0.05));'>
    <div style='display: flex; align-items: center; margin-bottom: 1rem;'>
        <span style='font-size: 2rem; margin-right: 1rem;'>🎯</span>
        <h3 style='margin: 0; font-weight: 700; color: #2C2C2C;'>Hypothesis 2</h3>
    </div>
    <p style='font-size: 1.1rem; color: #4A4A4A; margin: 0; font-style: italic;'>
        "Countries with higher GDP per capita are more likely to have legally binding net-zero carbon commitments."
    </p>
</div>

<div class='chart-container' style='margin-top: 2rem;'>
    <h3 style='font-weight: 700; color: #8B7D9B; margin-bottom: 1.5rem;'>
        🔬 Analytical Approach
    </h3>
    <ol style='color: #4A4A4A; line-height: 2; font-size: 1.05rem; padding-left: 1.5rem;'>
        <li>Statistical hypothesis testing with comprehensive effect size reporting</li>
        <li>Correlation analysis (Pearson & Spearman) with R² quantification</li>
        <li>Categorical comparisons (ANOVA) across GDP groups</li>
        <li>Chi-square tests for commitment patterns</li>
        <li>Business intelligence translation for CBAM compliance strategy</li>
    </ol>
</div>
</div>
""")

st.markdown("---")

# ===== EXECUTIVE SUMMARY - PREMIUM DESIGN =====
st.html("""
<div class='section-header' style='animation: slideInLeft 0.6s ease-out;'>
📋 Executive Summary
</div>

<div style='animation: fadeInUp 0.8s ease-out;'>
<div style='background: linear-gradient(135deg, rgba(255, 255, 255, 0.98) 0%, rgba(250, 250, 250, 0.95) 100%);
            backdrop-filter: blur(15px);
            padding: 3rem;
            border-radius: 20px;
            box-shadow: 0 12px 40px rgba(0, 0, 0, 0.1);
            border: 1px solid rgba(139, 125, 155, 0.15);
            margin: 2rem 0;'>
    
    <div style='display: flex; align-items: center; margin-bottom: 2rem; padding-bottom: 1.5rem; border-bottom: 2px solid rgba(139, 125, 155, 0.1);'>
        <span style='font-size: 3rem; margin-right: 1rem;'>🔍</span>
        <h3 style='margin: 0; font-family: "Plus Jakarta Sans", sans-serif; font-size: 1.8rem; font-weight: 700; color: #2C2C2C;'>
            Research Question: Is economic prosperity associated with environmental outcomes?
        </h3>
    </div>
    
    <div style='margin-bottom: 2rem;'>
        <h4 style='color: #8B7D9B; font-weight: 700; font-size: 1.2rem; margin-bottom: 1rem;'>
            📊 Part 1: GDP & CO₂ Emissions Relationship
        </h4>
        <p style='color: #2C2C2C; line-height: 1.8; font-size: 1.05rem;'>
            Analysis of 195 countries reveals <strong style='color: #8B7D9B;'>robust evidence</strong> that 
            higher GDP per capita is <strong style='color: #8B7D9B;'>strongly associated</strong> with higher CO₂ emissions per capita.
        </p>
        <div style='display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 1.5rem; margin: 1.5rem 0;'>
            <div style='background: rgba(139, 125, 155, 0.08); padding: 1.5rem; border-radius: 12px; text-align: center;'>
                <div style='font-size: 2rem; font-weight: 800; color: #8B7D9B;'>r = 0.67</div>
                <div style='color: #666; font-size: 0.9rem; margin-top: 0.5rem;'>Pearson Correlation</div>
            </div>
            <div style='background: rgba(107, 155, 145, 0.08); padding: 1.5rem; border-radius: 12px; text-align: center;'>
                <div style='font-size: 2rem; font-weight: 800; color: #6B9B91;'>ρ = 0.78</div>
                <div style='color: #666; font-size: 0.9rem; margin-top: 0.5rem;'>Spearman Correlation</div>
            </div>
            <div style='background: rgba(201, 169, 166, 0.08); padding: 1.5rem; border-radius: 12px; text-align: center;'>
                <div style='font-size: 2rem; font-weight: 800; color: #C9A9A6;'>R² = 0.45</div>
                <div style='color: #666; font-size: 0.9rem; margin-top: 0.5rem;'>Variance Explained</div>
            </div>
            <div style='background: rgba(166, 139, 123, 0.08); padding: 1.5rem; border-radius: 12px; text-align: center;'>
                <div style='font-size: 2rem; font-weight: 800; color: #A68B7B;'>4.8×</div>
                <div style='color: #666; font-size: 0.9rem; margin-top: 0.5rem;'>High vs Low GDP</div>
            </div>
        </div>
        <p style='color: #4A4A4A; line-height: 1.8; font-size: 0.95rem;'>
            ANOVA confirms significant differences between GDP categories (<em>F</em> = 1,847, <em>p</em> < 0.001), 
            with High-GDP countries emitting 4.8× more than Low-GDP countries.
        </p>
    </div>
    
    <div style='margin-bottom: 2rem;'>
        <h4 style='color: #6B9B91; font-weight: 700; font-size: 1.2rem; margin-bottom: 1rem;'>
            🎯 Part 2: Net-Zero Commitments & GDP
        </h4>
        <p style='color: #2C2C2C; line-height: 1.8; font-size: 1.05rem;'>
            Higher GDP countries demonstrate <strong style='color: #6B9B91;'>significantly greater propensity</strong> 
            to adopt net-zero targets (<em>χ²</em> = 286.4, <em>p</em> < 0.001, Cramér's <em>V</em> = 0.23).
        </p>
        <div class='warning-box' style='margin: 1.5rem 0;'>
            <strong style='color: #FFA726;'>⚠️ Critical Business Implication</strong><br>
            This finding has direct impact on supply chain carbon risk under 
            <strong>EU CBAM (2026)</strong> and <strong>ETS2 (2027)</strong> regulations.
        </div>
    </div>
    
    <div style='background: rgba(245, 243, 240, 0.5); padding: 1.5rem; border-radius: 12px; border-left: 4px solid #8B7D9B;'>
        <h4 style='color: #2C2C2C; font-weight: 700; margin-bottom: 1rem;'>
            📐 Methodology
        </h4>
        <p style='color: #4A4A4A; line-height: 1.7; font-size: 0.95rem; margin: 0;'>
            Shapiro-Wilk normality tests • Pearson/Spearman correlations • One-way ANOVA • 
            Welch's t-tests • Chi-square test for independence<br>
            <strong>Effect sizes:</strong> R², Cohen's <em>d</em>, Cramér's <em>V</em> • 
            <strong>Significance:</strong> α = 0.05 • <strong>CI:</strong> 95%
        </p>
    </div>
    
    <div class='info-box' style='margin-top: 1.5rem; background: linear-gradient(135deg, rgba(66, 165, 245, 0.08), rgba(66, 165, 245, 0.05));'>
        <strong style='color: #42A5F5;'>🔬 Key Limitation</strong><br>
        <p style='color: #4A4A4A; margin: 0.5rem 0 0 0; line-height: 1.7;'>
            Correlation does not establish causation. Outliers (France: nuclear policy; Qatar: LNG exports) 
            demonstrate that policy choices can decouple the GDP-emissions relationship.
        </p>
    </div>
</div>
</div>
""")

st.markdown("---")

# ===== DATA LOADING WITH STUNNING VISUALIZATION =====
st.html("""
<div class='section-header' style='animation: slideInLeft 0.6s ease-out;'>
📈 Live Data Insights
</div>
""")

# This section is now primarily for displaying the data, as loading is handled above.
# Success notification with animation
st.html(f"""
<div class='success-box' style='animation: fadeInUp 0.6s ease-out;'>
<strong style='font-size: 1.1rem;'>✅ Data Successfully Loaded</strong><br>
<p style='margin: 0.5rem 0 0 0; font-size: 0.95rem;'>
    Analysis ready for <strong>{len(merged_df["Country"].unique())} countries</strong> with 
    <strong>{len(merged_df):,} data points</strong> across multiple decades.
</p>
</div>
""")

# Get latest data
latest_year = merged_df["Year"].max()
latest_data = merged_df[merged_df["Year"] == latest_year]

# Use actual column names from CSV files
gdp_col = "GDP per capita (constant 2015 US$)"
co2_col = "Annual CO₂ emissions (per capita)"

# ===== STUNNING METRICS DASHBOARD =====
st.html("<div style='margin: 3rem 0;'>")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.html(f"""
<div class='metric-card' style='animation: fadeInUp 0.6s ease-out 0.1s backwards;'>
    <div class='metric-label'>COUNTRIES ANALYZED</div>
    <div class='metric-value'>{len(latest_data):,}</div>
    <div class='metric-delta' style='background: rgba(102, 187, 106, 0.1); color: #66BB6A;'>
        ✓ Complete dataset
    </div>
</div>
""")

with col2:
    avg_gdp = latest_data[gdp_col].mean()
    st.html(f"""
<div class='metric-card' style='animation: fadeInUp 0.6s ease-out 0.2s backwards;'>
    <div class='metric-label'>AVERAGE GDP PER CAPITA</div>
    <div class='metric-value'>${avg_gdp:,.0f}</div>
    <div class='metric-delta' style='color: #666;'>
        📊 {latest_year} data
    </div>
</div>
""")

with col3:
    avg_co2 = latest_data[co2_col].mean()
    st.html(f"""
<div class='metric-card' style='animation: fadeInUp 0.6s ease-out 0.3s backwards;'>
    <div class='metric-label'>AVERAGE CO₂ EMISSIONS</div>
    <div class='metric-value'>{avg_co2:.2f}t</div>
    <div class='metric-delta' style='color: #666;'>
        🌍 Per capita/year
    </div>
</div>
""")

with col4:
    # Find the status column (it might have different name)
    status_cols = [
        col
        for col in netzero_df.columns
        if "status" in col.lower() or "target" in col.lower()
    ]
    if status_cols:
        countries_with_commitment = len(netzero_df[netzero_df[status_cols[0]].notna()])
    else:
        countries_with_commitment = len(netzero_df)

st.html(f"""
<div class='metric-card' style='animation: fadeInUp 0.6s ease-out 0.4s backwards;'>
    <div class='metric-label'>NET-ZERO COMMITMENTS</div>
    <div class='metric-value'>{countries_with_commitment}</div>
    <div class='metric-delta' style='background: rgba(107, 155, 145, 0.1); color: #6B9B91;'>
        🎯 Countries pledged
    </div>
</div>
""")

st.html("</div>")

# ===== CALL TO ACTION =====
st.html("""
<div style='animation: fadeInUp 0.8s ease-out;'>
<div class='chart-container' style='text-align: center; padding: 3rem;'>
    <h2 style='font-family: "Plus Jakarta Sans", sans-serif; font-weight: 700; color: #8B7D9B; margin-bottom: 1.5rem;'>
        🔍 Explore the Analysis
    </h2>
    <p style='font-size: 1.1rem; color: #4A4A4A; line-height: 1.8; max-width: 700px; margin: 0 auto 2rem auto;'>
        Navigate to the <strong style='color: #8B7D9B;'>Analysis</strong> page in the sidebar for detailed 
        hypothesis testing, statistical methods, interactive visualizations, and business intelligence insights.
    </p>
    <div style='display: inline-flex; align-items: center; gap: 1rem; background: linear-gradient(135deg, rgba(139, 125, 155, 0.08), rgba(107, 155, 145, 0.05));
                padding: 1.5rem 2rem; border-radius: 12px; border: 2px dashed rgba(139, 125, 155, 0.3);'>
        <span style='font-size: 2rem;'>👉</span>
        <span style='font-size: 1.05rem; font-weight: 600; color: #2C2C2C;'>
            Check the sidebar to access the full statistical analysis
        </span>
    </div>
</div>
</div>
""")

# ===== PREMIUM FOOTER =====
st.html("""
<div class='dashboard-footer' style='margin-top: 5rem;'>
<div style='max-width: 800px; margin: 0 auto;'>
    <div style='font-size: 1.5rem; font-weight: 700; color: #8B7D9B; margin-bottom: 1rem;'>
        CarbonSeer
    </div>
    <p style='font-size: 0.95rem; line-height: 1.6; color: #666; margin-bottom: 1.5rem;'>
        Award-winning quantitative analytics platform for carbon risk assessment and investment screening.
        Built for carbon consultants, portfolio managers, and ESG analysts requiring rigorous statistical validation.
    </p>
    <div style='display: flex; justify-content: center; gap: 2rem; flex-wrap: wrap; margin-bottom: 1.5rem;'>
        <span style='color: #8B7D9B; font-weight: 600;'>📊 Statistical Rigor</span>
        <span style='color: #6B9B91; font-weight: 600;'>💼 Investment Screening</span>
        <span style='color: #C9A9A6; font-weight: 600;'>🎯 CBAM Intelligence</span>
    </div>
    <div style='padding-top: 1.5rem; border-top: 1px solid rgba(0, 0, 0, 0.1);'>
        <p style='font-size: 0.85rem; color: #999; margin: 0;'>
            © 2025 CarbonSeer | Developed by <strong style='color: #8B7D9B;'>Kartavya Jharwal</strong><br>
            Professional Carbon Risk Analytics Tool
        </p>
    </div>
</div>
</div>
""")

# ===== RENDER STICKY FOOTER =====
render_sticky_footer()
