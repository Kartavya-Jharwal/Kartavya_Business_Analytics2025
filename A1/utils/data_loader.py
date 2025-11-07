"""
Data loading and processing utilities for the CarbonSeer Streamlit dashboard.

This module provides functions for:
- Loading GDP, CO2 emissions, and net-zero commitments data
- Merging datasets on common keys (Country, Year)
- Creating categorical variables for analysis
- Formatting and validating data

All functions use @st.cache_data for optimal performance.
"""

import pandas as pd
import streamlit as st
from pathlib import Path
from typing import Optional


RAW_BASE = "https://raw.githubusercontent.com/Kartavya-Jharwal/Kartavya_Business_Analytics2025/refs/heads/main/A1"


def _read_csv_auto(
    local_path: Path,
    github_path: Optional[str] = None,
    source: str = "auto",
    **read_csv_kwargs,
) -> pd.DataFrame:
    """
    Read a CSV from local path or GitHub raw with graceful fallback.

    Args:
        local_path: Path to local CSV
        github_path: Raw GitHub URL (if None, constructed from RAW_BASE and relative)
        source: "auto" (try local then GitHub), "local", or "github"
        **read_csv_kwargs: forwarded to pandas.read_csv
    """
    # Defaults that improve type inference for large CSVs
    read_csv_kwargs.setdefault("low_memory", False)

    if source == "local":
        return pd.read_csv(local_path, **read_csv_kwargs)
    if source == "github":
        if not github_path:
            raise FileNotFoundError("github_path must be provided when source='github'")
        return pd.read_csv(github_path, **read_csv_kwargs)

    # auto: prefer local then fallback to GitHub
    if local_path.exists():
        return pd.read_csv(local_path, **read_csv_kwargs)
    if github_path:
        return pd.read_csv(github_path, **read_csv_kwargs)
    raise FileNotFoundError(
        f"Data not found locally and no GitHub URL provided: {local_path}"
    )


@st.cache_data
def load_gdp_data(source: str = "auto") -> pd.DataFrame:
    """
    Load GDP per capita dataset from World Bank source.

    Data Structure:
    - Entity: Country name (renamed to 'Country')
    - Year: Calendar year
    - GDP per capita (constant 2015 US$): Main metric

    Returns:
        pd.DataFrame: GDP dataset with standardized column names

    Raises:
        FileNotFoundError: If data file not found at expected path

    Example:
        >>> gdp_df = load_gdp_data()
        >>> print(gdp_df.shape)
        (5000, 3)
    """
    data_path = (
        Path(__file__).parent.parent
        / "gdp-per-capita-worldbank-constant-usd"
        / "gdp-per-capita-worldbank-constant-usd.csv"
    )
    github_url = f"{RAW_BASE}/gdp-per-capita-worldbank-constant-usd/gdp-per-capita-worldbank-constant-usd.csv"

    df = _read_csv_auto(data_path, github_url, source)

    # Standardize column names
    df = df.rename(columns={"Entity": "Country"})

    return df


@st.cache_data
def load_co2_data(source: str = "auto") -> pd.DataFrame:
    """
    Load CO2 emissions per capita dataset from Global Carbon Budget.

    Data Structure:
    - Entity: Country name (renamed to 'Country')
    - Year: Calendar year
    - Annual CO₂ emissions (per capita): Main metric in metric tons

    Returns:
        pd.DataFrame: CO2 emissions dataset with standardized column names

    Raises:
        FileNotFoundError: If data file not found at expected path

    Example:
        >>> co2_df = load_co2_data()
        >>> print(co2_df['Annual CO₂ emissions (per capita)'].describe())
    """
    data_path = (
        Path(__file__).parent.parent
        / "co-emissions-per-capita"
        / "co-emissions-per-capita.csv"
    )
    github_url = f"{RAW_BASE}/co-emissions-per-capita/co-emissions-per-capita.csv"

    df = _read_csv_auto(data_path, github_url, source)

    # Standardize column names
    df = df.rename(columns={"Entity": "Country"})

    return df


@st.cache_data
def load_netzero_data(source: str = "auto") -> pd.DataFrame:
    """
    Load net-zero targets dataset from Net Zero Tracker.

    Data Structure:
    - Entity: Country name (renamed to 'Country')
    - Status of net-zero carbon emissions targets: Commitment status

    Commitment Types (Ordered by strength):
    1. Proposed / in discussion
    2. Declaration / pledge
    3. In policy document
    4. In law
    5. Achieved (self-declared)

    Returns:
        pd.DataFrame: Net-zero commitments dataset

    Raises:
        FileNotFoundError: If data file not found at expected path

    Example:
        >>> nz_df = load_netzero_data()
        >>> print(nz_df['Status of net-zero carbon emissions targets'].unique())
    """
    data_path = (
        Path(__file__).parent.parent / "net-zero-targets" / "net-zero-targets.csv"
    )
    github_url = f"{RAW_BASE}/net-zero-targets/net-zero-targets.csv"

    df = _read_csv_auto(data_path, github_url, source)

    # Standardize column names
    df = df.rename(columns={"Entity": "Country"})

    return df


@st.cache_data
def merge_gdp_co2(gdp_df: pd.DataFrame, co2_df: pd.DataFrame) -> pd.DataFrame:
    """
    Merge GDP and CO2 datasets on Country and Year.

    This function performs an inner join, keeping only records where
    both GDP and CO2 data are available. Missing values in key columns
    are dropped to ensure data quality.

    Args:
        gdp_df: GDP per capita dataset
        co2_df: CO2 emissions per capita dataset

    Returns:
        pd.DataFrame: Merged dataset with both metrics

    Note:
        Inner join means only countries with data in both datasets
        are retained. This reduces the dataset size but ensures
        analytical validity.

    Example:
        >>> merged = merge_gdp_co2(gdp_df, co2_df)
        >>> print(len(merged))
        4500
    """
    merged = pd.merge(
        co2_df, gdp_df, on=["Country", "Year"], how="inner", suffixes=("_co2", "_gdp")
    )

    # Remove rows with missing values in key columns
    required_columns = [
        "Annual CO₂ emissions (per capita)",
        "GDP per capita (constant 2015 US$)",
    ]

    # Check if required columns exist
    available_co2_cols = [col for col in required_columns if col in merged.columns]
    if available_co2_cols:
        merged = merged.dropna(subset=available_co2_cols)

    return merged


@st.cache_data
def create_gdp_categories(
    df: pd.DataFrame, low_threshold: float = 5000, high_threshold: float = 15000
) -> pd.DataFrame:
    """
    Create GDP categorical variable using quantile-based thresholds.

    This function creates three categories:
    - Low: GDP per capita < $5,000
    - Medium: $5,000 ≤ GDP per capita < $15,000
    - High: GDP per capita ≥ $15,000

    Args:
        df: Input dataframe containing GDP data
        low_threshold: Lower boundary for GDP categories (default: $5,000)
        high_threshold: Upper boundary for GDP categories (default: $15,000)

    Returns:
        pd.DataFrame: DataFrame with new 'GDP_Category' column

    Raises:
        ValueError: If no GDP per capita column found in dataframe

    Note:
        The thresholds are based on World Bank income classifications
        adapted for analytical purposes.

    Example:
        >>> df_cat = create_gdp_categories(merged_df)
        >>> print(df_cat['GDP_Category'].value_counts())
    """
    df = df.copy()

    # Find the GDP column dynamically
    gdp_columns = [
        col for col in df.columns if "gdp" in col.lower() and "capita" in col.lower()
    ]

    if not gdp_columns:
        raise ValueError("No GDP per capita column found in dataframe")

    gdp_col = gdp_columns[0]

    # Convert to numeric and remove missing values
    df[gdp_col] = pd.to_numeric(df[gdp_col], errors="coerce")
    df = df.dropna(subset=[gdp_col])

    # Create categories using pd.cut
    df["GDP_Category"] = pd.cut(
        df[gdp_col],
        bins=[-float("inf"), low_threshold, high_threshold, float("inf")],
        labels=["Low", "Medium", "High"],
    )

    return df


@st.cache_data
def create_commitment_strength(netzero_df: pd.DataFrame) -> pd.DataFrame:
    """
    Map net-zero commitment status to ordinal strength scores.

    Commitment Strength Scale:
    - 0: No commitment
    - 1: Proposed / in discussion
    - 2: Declaration / pledge
    - 3: In policy document
    - 4: In law (✅ LEGAL PROTECTION)
    - 5: Achieved / self-declared (✅ LEGAL PROTECTION)

    This function creates two new columns:
    - Commitment_Strength: Numeric ordinal score (0-5)
    - Has_NetZero_Target: Binary indicator (1 = has target, 0 = no target)

    Args:
        netzero_df: Net-zero commitments dataset

    Returns:
        pd.DataFrame: DataFrame with commitment strength variables

    Note:
        Only scores 4 and 5 provide regulatory protection under CBAM
        and other carbon-adjustment mechanisms.

    Example:
        >>> nz_enhanced = create_commitment_strength(nz_df)
        >>> print(nz_enhanced['Commitment_Strength'].describe())
    """
    df = netzero_df.copy()

    # Find the status column dynamically
    status_columns = [
        col for col in df.columns if "status" in col.lower() and "net" in col.lower()
    ]

    if not status_columns:
        status_col = "Status of net-zero carbon emissions targets"
    else:
        status_col = status_columns[0]

    # Commitment strength mapping
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
def get_latest_year_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Extract the most recent year of data for each country.

    This is useful for cross-sectional analysis or when you need
    the most current snapshot of the data.

    Args:
        df: Input dataframe with Year column

    Returns:
        pd.DataFrame: One row per country with latest available data

    Example:
        >>> latest = get_latest_year_data(merged_df)
        >>> print(f"Latest year data: {latest['Year'].max()}")
    """
    return df.sort_values("Year").groupby("Country").tail(1).reset_index(drop=True)


def format_large_number(num: float) -> str:
    """
    Format large numbers with K, M, B suffixes for readability.

    Args:
        num: Numeric value to format

    Returns:
        str: Formatted string with appropriate suffix

    Example:
        >>> format_large_number(1500000)
        '$1.5M'
        >>> format_large_number(5000)
        '$5.0K'
    """
    if num >= 1_000_000_000:
        return f"${num / 1_000_000_000:.1f}B"
    elif num >= 1_000_000:
        return f"${num / 1_000_000:.1f}M"
    elif num >= 1_000:
        return f"${num / 1_000:.1f}K"
    else:
        return f"${num:.0f}"
