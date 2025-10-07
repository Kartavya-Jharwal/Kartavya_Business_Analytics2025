"""
Data loading and processing utilities for the Streamlit dashboard.
"""

import pandas as pd
import streamlit as st
from pathlib import Path


@st.cache_data
def load_gdp_data():
    """Load GDP per capita dataset."""
    data_path = (
        Path(__file__).parent.parent
        / "gdp-per-capita-worldbank-constant-usd"
        / "gdp-per-capita-worldbank-constant-usd.csv"
    )
    df = pd.read_csv(data_path)
    
    # Rename Entity to Country for clarity
    df = df.rename(columns={"Entity": "Country"})
    
    return df


@st.cache_data
def load_co2_data():
    """Load CO2 emissions per capita dataset."""
    data_path = (
        Path(__file__).parent.parent
        / "co-emissions-per-capita"
        / "co-emissions-per-capita.csv"
    )
    df = pd.read_csv(data_path)
    
    # Rename Entity to Country for clarity
    df = df.rename(columns={"Entity": "Country"})
    
    return df


@st.cache_data
def load_netzero_data():
    """Load net-zero targets dataset."""
    data_path = (
        Path(__file__).parent.parent / "net-zero-targets" / "net-zero-targets.csv"
    )
    df = pd.read_csv(data_path)
    
    # Rename Entity to Country for clarity
    df = df.rename(columns={"Entity": "Country"})
    
    return df


@st.cache_data
def merge_gdp_co2(gdp_df, co2_df):
    """Merge GDP and CO2 datasets."""
    merged = pd.merge(
        co2_df, gdp_df, on=["Country", "Year"], how="inner", suffixes=("_co2", "_gdp")
    )
    
    # Remove rows with missing values in key columns
    # Actual column names from CSVs
    merged = merged.dropna(subset=["Annual CO₂ emissions (per capita)", "GDP per capita (constant 2015 US$)"])
    
    return merged


@st.cache_data
def create_gdp_categories(df, low_threshold=5000, high_threshold=15000):
    """Create GDP categories with custom thresholds."""
    df = df.copy()
    
    # Find the GDP column dynamically (same as notebook)
    gdp_columns = [
        col
        for col in df.columns
        if "gdp" in col.lower() and "capita" in col.lower()
    ]
    
    if not gdp_columns:
        raise ValueError("No GDP per capita column found in dataframe")
    
    gdp_col = gdp_columns[0]
    
    # Convert to numeric and remove missing values
    df[gdp_col] = pd.to_numeric(df[gdp_col], errors="coerce")
    df = df.dropna(subset=[gdp_col])
    
    # Create categories using pd.cut (same as notebook)
    df["GDP_Category"] = pd.cut(
        df[gdp_col],
        bins=[-float('inf'), low_threshold, high_threshold, float('inf')],
        labels=["Low", "Medium", "High"],
    )
    
    return df


@st.cache_data
def create_commitment_strength(netzero_df):
    """Map net-zero status to commitment strength scores."""
    df = netzero_df.copy()

    # Find the status column dynamically
    status_columns = [col for col in df.columns if "status" in col.lower() and "net" in col.lower()]
    if not status_columns:
        # Fallback to exact column name from CSV
        status_col = "Status of net-zero carbon emissions targets"
    else:
        status_col = status_columns[0]

    commitment_mapping = {
        "Achieved (self-declared)": 5,
        "In law": 4,
        "In policy document": 3,
        "Declaration / pledge": 2,
        "Proposed / in discussion": 1,
    }

    df["Commitment_Strength"] = df[status_col].map(commitment_mapping).fillna(0)
    df["Has_NetZero_Target"] = (df["Commitment_Strength"] > 0).astype(int)

    return df


@st.cache_data
def get_latest_year_data(df):
    """Get most recent year for each country."""
    return df.sort_values("Year").groupby("Country").tail(1).reset_index(drop=True)


def format_large_number(num):
    """Format large numbers with K, M, B suffixes."""
    if num >= 1_000_000_000:
        return f"${num / 1_000_000_000:.1f}B"
    elif num >= 1_000_000:
        return f"${num / 1_000_000:.1f}M"
    elif num >= 1_000:
        return f"${num / 1_000:.1f}K"
    else:
        return f"${num:.0f}"
