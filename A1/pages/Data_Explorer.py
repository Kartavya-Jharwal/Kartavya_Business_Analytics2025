"""
CarbonSeer - Interactive Data Explorer
Real-time data exploration, filtering, and custom visualizations.
"""

import streamlit as st
import plotly.express as px
from pathlib import Path

from utils import (
    load_gdp_data,
    load_co2_data,
    load_netzero_data,
    merge_gdp_co2,
    create_gdp_categories,
    create_commitment_strength,
    get_custom_css,
    get_plotly_theme,
    render_sidebar_resources,
)
from utils.styling import (
    render_global_branding,
    render_page_lockup,
    render_sticky_footer,
)

# Page configuration
st.set_page_config(
    page_title="CarbonSeer - Data Explorer",
    page_icon="🔍",
    layout="wide",
)

# Apply preferences and styling
if "fast_mode" not in st.session_state:
    st.session_state.fast_mode = True
with st.sidebar:
    st.markdown("### ⚙️ Preferences")
    st.toggle("⚡ Fast Mode", value=st.session_state.fast_mode, key="fast_toggle_explorer",
             on_change=lambda: setattr(st.session_state, 'fast_mode', st.session_state.fast_toggle_explorer))

st.markdown(get_custom_css("light"), unsafe_allow_html=True)

# Use global branding helpers
render_global_branding()

# Add logo and sidebar resources
assets_dir = Path(__file__).parent.parent / "assets"
logo_path = assets_dir / "CarbonSeer_png.png"
st.logo(str(logo_path), icon_image=str(logo_path))
render_sidebar_resources()

# Show CarbonSeer lockup
render_page_lockup()

st.html("""
<div class='section-header' style='animation: slideInLeft 0.6s ease-out;'>
🔍 Interactive Data Explorer
</div>
""")

st.markdown("""
Explore the datasets interactively with custom filters, search capabilities, and real-time visualizations.
Perfect for deep-dive analysis and discovering insights in the data.
""")

st.markdown("---")

# Load data
@st.cache_data
def load_explorer_data(source: str = "auto"):
    """Load all datasets for the explorer."""
    gdp_df = load_gdp_data(source)
    co2_df = load_co2_data(source)
    netzero_df = load_netzero_data(source)
    merged_df = merge_gdp_co2(gdp_df, co2_df)
    merged_df = create_gdp_categories(merged_df)
    netzero_df = create_commitment_strength(netzero_df)
    return gdp_df, co2_df, netzero_df, merged_df


with st.spinner("Loading datasets for exploration..."):
    # Reuse data source choice from Home if available
    data_source = st.session_state.get("data_source", "auto")
    gdp_df, co2_df, netzero_df, merged_df = load_explorer_data(data_source)

# ===== DATASET SELECTION =====
st.html("""
<div class='metric-card'>
    <div class='metric-label'>SELECT DATASET TO EXPLORE</div>
</div>
""")

dataset_choice = st.radio(
    "Choose a dataset:",
    ["📊 GDP & CO₂ (Merged)", "💰 GDP per Capita", "🌍 CO₂ Emissions", "🎯 Net-Zero Commitments"],
    horizontal=True
)

# Select the appropriate dataset
if dataset_choice == "📊 GDP & CO₂ (Merged)":
    df = merged_df.copy()
    dataset_name = "GDP & CO₂ (Merged)"
elif dataset_choice == "💰 GDP per Capita":
    df = gdp_df.copy()
    dataset_name = "GDP per Capita"
elif dataset_choice == "🌍 CO₂ Emissions":
    df = co2_df.copy()
    dataset_name = "CO₂ Emissions"
else:
    df = netzero_df.copy()
    dataset_name = "Net-Zero Commitments"

st.markdown("---")

# ===== DATA OVERVIEW =====
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.html(f"""
<div class='metric-card'>
    <div class='metric-label'>TOTAL ROWS</div>
    <div class='metric-value'>{len(df):,}</div>
</div>
""")

with col2:
    st.html(f"""
<div class='metric-card'>
    <div class='metric-label'>COLUMNS</div>
    <div class='metric-value'>{len(df.columns)}</div>
</div>
""")

with col3:
    if "Country" in df.columns:
        unique_countries = df["Country"].nunique()
    else:
        unique_countries = "N/A"
    st.html(f"""
<div class='metric-card'>
    <div class='metric-label'>COUNTRIES</div>
    <div class='metric-value'>{unique_countries}</div>
</div>
""")

with col4:
    if "Year" in df.columns:
        year_range = f"{df['Year'].min()}-{df['Year'].max()}"
    else:
        year_range = "N/A"
    st.html(f"""
<div class='metric-card'>
    <div class='metric-label'>TIME RANGE</div>
    <div class='metric-value' style='font-size: 1.8rem;'>{year_range}</div>
</div>
""")

st.markdown("---")

# ===== FILTERING SECTION =====
st.html("""
<div class='section-header' style='animation: slideInLeft 0.6s ease-out;'>
🎛️ Filter & Search
</div>
""")

col1, col2 = st.columns(2)

with col1:
    # Country filter
    if "Country" in df.columns:
        st.markdown("#### 🌍 Select Countries")
        all_countries = sorted(df["Country"].unique())
        selected_countries = st.multiselect(
            "Countries (leave empty for all):",
            options=all_countries,
            default=[]
        )
        if selected_countries:
            df = df[df["Country"].isin(selected_countries)]

with col2:
    # Year filter
    if "Year" in df.columns:
        st.markdown("#### 📅 Select Time Period")
        min_year = int(df["Year"].min())
        max_year = int(df["Year"].max())
        year_range_sel = st.slider(
            "Year range:",
            min_value=min_year,
            max_value=max_year,
            value=(min_year, max_year)
        )
        df = df[(df["Year"] >= year_range_sel[0]) & (df["Year"] <= year_range_sel[1])]

# GDP Category filter if available
if "GDP_Category" in df.columns:
    st.markdown("#### 💰 GDP Category")
    gdp_categories = st.multiselect(
        "Select GDP categories:",
        options=["Low", "Medium", "High"],
        default=["Low", "Medium", "High"]
    )
    df = df[df["GDP_Category"].isin(gdp_categories)]

st.markdown("---")

# ===== DATA TABLE =====
st.html("""
<div class='section-header' style='animation: slideInLeft 0.6s ease-out;'>
📋 Filtered Data Table
</div>
""")

st.markdown(f"**Showing {len(df):,} rows after filtering**")

# Column selection
st.markdown("#### 📊 Select Columns to Display")
all_columns = list(df.columns)
default_columns = all_columns[:10] if len(all_columns) > 10 else all_columns
selected_columns = st.multiselect(
    "Choose columns:",
    options=all_columns,
    default=default_columns
)

if selected_columns:
    display_df = df[selected_columns]
else:
    display_df = df

# Display the table
st.dataframe(
    display_df.head(100),
    use_container_width=True,
    height=400
)

# Download button
csv = display_df.to_csv(index=False).encode('utf-8')
st.download_button(
    label="📥 Download Filtered Data as CSV",
    data=csv,
    file_name=f"carbonseer_{dataset_name.lower().replace(' ', '_')}_filtered.csv",
    mime="text/csv",
)

st.markdown("---")

# ===== CUSTOM VISUALIZATION =====
st.html("""
<div class='section-header' style='animation: slideInLeft 0.6s ease-out;'>
📈 Custom Visualization Builder
</div>
""")

st.markdown("Build your own interactive charts from the filtered data.")

col1, col2, col3 = st.columns(3)

with col1:
    chart_type = st.selectbox(
        "Chart Type:",
        ["Scatter Plot", "Line Chart", "Bar Chart", "Box Plot", "Histogram"]
    )

numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns.tolist()
categorical_cols = df.select_dtypes(include=['object', 'category']).columns.tolist()

with col2:
    if chart_type in ["Scatter Plot", "Line Chart", "Bar Chart"]:
        x_col = st.selectbox("X-axis:", options=df.columns.tolist())
    elif chart_type == "Box Plot":
        x_col = st.selectbox("Category (X-axis):", options=categorical_cols if categorical_cols else df.columns.tolist())
    else:
        x_col = st.selectbox("Column:", options=numeric_cols if numeric_cols else df.columns.tolist())

with col3:
    if chart_type in ["Scatter Plot", "Line Chart", "Bar Chart", "Box Plot"]:
        y_col = st.selectbox("Y-axis:", options=numeric_cols if numeric_cols else df.columns.tolist())
    else:
        y_col = None

# Color by category
color_col = None
if categorical_cols and chart_type != "Histogram":
    use_color = st.checkbox("Color by category?")
    if use_color:
        color_col = st.selectbox("Color by:", options=categorical_cols)

# Generate the chart
try:
    if chart_type == "Scatter Plot":
        fig = px.scatter(
            df, 
            x=x_col, 
            y=y_col, 
            color=color_col,
            title=f"{y_col} vs {x_col}",
            template=get_plotly_theme(),
            height=500
        )
    elif chart_type == "Line Chart":
        fig = px.line(
            df, 
            x=x_col, 
            y=y_col, 
            color=color_col,
            title=f"{y_col} over {x_col}",
            template=get_plotly_theme(),
            height=500
        )
    elif chart_type == "Bar Chart":
        fig = px.bar(
            df, 
            x=x_col, 
            y=y_col, 
            color=color_col,
            title=f"{y_col} by {x_col}",
            template=get_plotly_theme(),
            height=500
        )
    elif chart_type == "Box Plot":
        fig = px.box(
            df, 
            x=x_col, 
            y=y_col, 
            color=color_col,
            title=f"{y_col} distribution by {x_col}",
            template=get_plotly_theme(),
            height=500
        )
    else:  # Histogram
        fig = px.histogram(
            df, 
            x=x_col, 
            color=color_col,
            title=f"Distribution of {x_col}",
            template=get_plotly_theme(),
            height=500
        )
    
    st.plotly_chart(fig, use_container_width=True)
except Exception as e:
    st.error(f"Error generating chart: {str(e)}")
    st.info("Try selecting different columns or adjusting your filters.")

st.markdown("---")

# ===== SUMMARY STATISTICS =====
st.html("""
<div class='section-header' style='animation: slideInLeft 0.6s ease-out;'>
📊 Summary Statistics
</div>
""")

if numeric_cols:
    st.markdown("#### Descriptive Statistics for Numeric Columns")
    stats_df = df[numeric_cols].describe()
    st.dataframe(stats_df, use_container_width=True)
else:
    st.info("No numeric columns available for statistical summary.")

st.markdown("---")

# ===== FOOTER =====
render_sticky_footer()
