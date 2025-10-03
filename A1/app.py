import streamlit as st
import pandas as pd
import numpy as np

# Set page configuration
st.set_page_config(
    page_title="Basic Streamlit App",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Main title
st.title("🚀 Welcome to My Basic Streamlit App")

# Subtitle
st.markdown("### A simple demonstration of Streamlit capabilities")

# Sidebar
st.sidebar.header("Navigation")
page = st.sidebar.selectbox("Choose a page:", ["Home", "Data Analysis", "Interactive Charts"])

if page == "Home":
    # Introduction section
    st.header("🏠 Home")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("""
        This is a basic Streamlit application demonstrating various components:
        
        - Interactive widgets
        - Data visualization
        - File uploads
        - Charts and graphs
        """)
        
        # User input
        name = st.text_input("What's your name?", placeholder="Enter your name here")
        if name:
            st.success(f"Hello, {name}! 👋")
    
    with col2:
        st.write("### Quick Stats")
        
        # Metrics
        col_a, col_b, col_c = st.columns(3)
        with col_a:
            st.metric("Users", "1,234", "12%")
        with col_b:
            st.metric("Revenue", "$5,678", "-2%")
        with col_c:
            st.metric("Growth", "89%", "15%")

elif page == "Data Analysis":
    st.header("📊 Data Analysis")
    
    # Generate sample data
    @st.cache_data
    def generate_data():
        dates = pd.date_range("2023-01-01", periods=100, freq="D")
        data = pd.DataFrame({
            "Date": dates,
            "Sales": np.random.randn(100).cumsum() + 100,
            "Profit": np.random.randn(100).cumsum() + 50,
            "Category": np.random.choice(["A", "B", "C"], 100)
        })
        return data
    
    data = generate_data()
    
    # Show data
    st.subheader("Sample Dataset")
    st.dataframe(data.head(10), use_container_width=True)
    
    # Statistics
    st.subheader("Data Statistics")
    st.write(data.describe())
    
    # Filter data
    st.subheader("Filter Data")
    category_filter = st.multiselect("Select Categories:", options=data["Category"].unique(), default=data["Category"].unique())
    filtered_data = data[data["Category"].isin(category_filter)]
    
    st.write(f"Showing {len(filtered_data)} rows")
    st.dataframe(filtered_data, use_container_width=True)

elif page == "Interactive Charts":
    st.header("📈 Interactive Charts")
    
    # Generate sample data for charts
    @st.cache_data
    def generate_chart_data():
        return pd.DataFrame({
            "x": range(50),
            "y": np.random.randn(50).cumsum(),
            "category": np.random.choice(["Type A", "Type B", "Type C"], 50)
        })
    
    chart_data = generate_chart_data()
    
    # Chart type selection
    chart_type = st.selectbox("Select Chart Type:", ["Line Chart", "Bar Chart", "Scatter Plot", "Area Chart"])
    
    col1, col2 = st.columns(2)
    
    with col1:
        if chart_type == "Line Chart":
            st.line_chart(chart_data.set_index("x")["y"])
        elif chart_type == "Bar Chart":
            st.bar_chart(chart_data.groupby("category")["y"].sum())
        elif chart_type == "Scatter Plot":
            st.scatter_chart(chart_data.set_index("x")["y"])
        elif chart_type == "Area Chart":
            st.area_chart(chart_data.set_index("x")["y"])
    
    with col2:
        st.write("### Chart Configuration")
        
        # Sliders for customization
        num_points = st.slider("Number of points:", 10, 100, 50)
        noise_level = st.slider("Noise level:", 0.1, 2.0, 1.0)
        
        # Update chart based on sliders
        custom_data = pd.DataFrame({
            "x": range(num_points),
            "y": np.random.randn(num_points).cumsum() * noise_level
        })
        
        st.line_chart(custom_data.set_index("x"))

# Footer
st.markdown("---")
st.markdown("Built with ❤️ using Streamlit and uv")

# Add some interactive widgets in the sidebar
st.sidebar.markdown("---")
st.sidebar.header("Settings")

# Color picker
color = st.sidebar.color_picker("Pick a theme color", "#FF6B6B")
st.sidebar.markdown(f'<div style="background-color: {color}; padding: 10px; border-radius: 5px; color: white; text-align: center;">Selected Color</div>', unsafe_allow_html=True)

# Checkbox
show_debug = st.sidebar.checkbox("Show debug info")

if show_debug:
    st.sidebar.write("Debug Information:")
    st.sidebar.json({
        "Current page": page,
        "Streamlit version": st.__version__,
        "Selected color": color
    })