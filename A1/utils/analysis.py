"""
Statistical analysis utilities for the CarbonSeer Streamlit dashboard.

This module provides comprehensive statistical functions for:
- Correlation analysis (Pearson and Spearman)
- ANOVA and pairwise comparisons
- Chi-square tests of independence
- Normality testing

All computationally intensive functions use @st.cache_data for performance optimization.
"""

import pandas as pd
import numpy as np
import streamlit as st
from typing import Dict, Tuple, Optional
from scipy.stats import (
    pearsonr,
    spearmanr,
    f_oneway,
    ttest_ind,
    chi2_contingency,
    shapiro,
)


def _mean_sem_ci(
    arr: np.ndarray, alpha: float = 0.05
) -> Tuple[float, float, float, float]:
    """
    Calculate mean, standard error, and 95% confidence interval for an array.

    Args:
        arr: Input array of numeric values
        alpha: Significance level (default: 0.05 for 95% CI)

    Returns:
        Tuple of (mean, standard_error, ci_lower, ci_upper)

    Note:
        Uses z-score of 1.96 for 95% confidence interval (approximation).
        Removes NaN values before calculation.
    """
    arr = np.array(arr)
    arr = arr[~np.isnan(arr)]
    n = len(arr)

    if n == 0:
        return (np.nan, np.nan, np.nan, np.nan)

    mean = arr.mean()
    sem = arr.std(ddof=1) / np.sqrt(n) if n > 1 else 0.0
    z = 1.96  # Approximately 95% confidence interval
    lower = mean - z * sem
    upper = mean + z * sem

    return mean, sem, lower, upper


@st.cache_data
def compute_correlations(
    df: pd.DataFrame, x_col: str, y_col: str, sample_limit: int = 5000
) -> Optional[Dict]:
    """
    Compute Pearson and Spearman correlations between two variables.

    This function computes both parametric (Pearson) and non-parametric (Spearman)
    correlations, providing robust correlation estimates. Large datasets are sampled
    to maintain statistical stability and computational efficiency.

    Args:
        df: Input dataframe containing both variables
        x_col: Column name for first variable
        y_col: Column name for second variable
        sample_limit: Maximum sample size for correlation computation (default: 5000)

    Returns:
        Dict with keys:
        - pearson_r: Pearson correlation coefficient (-1 to 1)
        - pearson_p: P-value for Pearson correlation
        - spearman_rho: Spearman rank correlation coefficient
        - spearman_p: P-value for Spearman correlation
        - r_squared: R² value (coefficient of determination) for Pearson
        - n: Sample size used in computation
        Returns None if no valid data pairs exist

    Raises:
        KeyError: If x_col or y_col not found in dataframe

    Note:
        Both columns must contain numeric data. Missing values (NaN) are
        automatically removed. If sample_limit is exceeded, a random sample
        is drawn with fixed seed (42) for reproducibility.

    Example:
        >>> results = compute_correlations(df, 'GDP_per_capita', 'CO2_emissions')
        >>> print(f"Pearson r = {results['pearson_r']:.3f}, p = {results['pearson_p']:.4f}")
    """
    # Validate columns exist
    if x_col not in df.columns or y_col not in df.columns:
        missing = [c for c in [x_col, y_col] if c not in df.columns]
        raise KeyError(f"Column(s) not found in dataframe: {missing}")

    # Extract and clean data
    clean = df[[x_col, y_col]].dropna()

    if len(clean) == 0:
        return None

    # Sample if necessary to maintain computational efficiency
    if len(clean) > sample_limit:
        sample = clean.sample(sample_limit, random_state=42)
    else:
        sample = clean

    x = sample[x_col].values
    y = sample[y_col].values

    # Compute correlations
    pearson_r, pearson_p = pearsonr(x, y)
    spearman_rho, spearman_p = spearmanr(x, y)
    r_squared = pearson_r**2

    return {
        "pearson_r": float(pearson_r),
        "pearson_p": float(pearson_p),
        "spearman_rho": float(spearman_rho),
        "spearman_p": float(spearman_p),
        "r_squared": float(r_squared),
        "n": len(sample),
    }


@st.cache_data
def compute_anova_and_pairwise(
    df: pd.DataFrame, value_col: str, group_col: str
) -> Tuple[Optional[float], Optional[float], pd.DataFrame]:
    """
    Perform one-way ANOVA and pairwise Welch t-tests with effect sizes.

    This function performs a comprehensive group comparison including:
    1. One-way ANOVA (omnibus test)
    2. Pairwise Welch t-tests (does not assume equal variances)
    3. Cohen's d effect sizes for each pairwise comparison
    4. 95% confidence intervals for group means

    Args:
        df: Input dataframe with grouping and value columns
        value_col: Column name containing numeric values to compare
        group_col: Column name containing group membership

    Returns:
        Tuple of (f_statistic, p_value, pairwise_results_df)
        - f_statistic: F-statistic from ANOVA
        - p_value: P-value from ANOVA
        - pairwise_results_df: DataFrame with pairwise comparison results

    Raises:
        KeyError: If value_col or group_col not found in dataframe

    Note:
        - Requires at least 2 non-empty groups
        - Missing values are automatically removed
        - Welch t-tests do not assume equal variances (Welch's adjustment)
        - Cohen's d is calculated using pooled standard deviation

    Example:
        >>> f_stat, p_val, pairwise = compute_anova_and_pairwise(
        ...     df, 'CO2_emissions', 'GDP_Category'
        ... )
        >>> print(f"ANOVA F={f_stat:.3f}, p={p_val:.4f}")
    """
    # Validate columns exist
    if value_col not in df.columns or group_col not in df.columns:
        missing = [c for c in [value_col, group_col] if c not in df.columns]
        raise KeyError(f"Column(s) not found in dataframe: {missing}")

    # Extract groups and filter empty ones
    groups = df.groupby(group_col)[value_col].apply(lambda s: s.dropna().values)
    groups = {k: v for k, v in groups.items() if len(v) > 0}

    if len(groups) < 2:
        return None, None, pd.DataFrame()

    # Perform one-way ANOVA
    anova_stat, anova_p = f_oneway(*[groups[k] for k in groups])

    # Pairwise Welch t-tests with effect sizes
    rows = []
    keys = list(groups.keys())
    from itertools import combinations

    for group_a, group_b in combinations(keys, 2):
        data1 = groups[group_a]
        data2 = groups[group_b]

        # Welch's t-test (does not assume equal variances)
        t_stat, p_val = ttest_ind(data1, data2, equal_var=False)

        # Calculate Cohen's d using pooled standard deviation
        n1 = len(data1)
        n2 = len(data2)
        m1 = np.mean(data1)
        m2 = np.mean(data2)
        s1 = np.std(data1, ddof=1)
        s2 = np.std(data2, ddof=1)

        try:
            pooled_sd = np.sqrt(((n1 - 1) * s1**2 + (n2 - 1) * s2**2) / (n1 + n2 - 2))
            cohen_d = (m1 - m2) / pooled_sd if pooled_sd > 0 else np.nan
        except Exception:
            cohen_d = np.nan

        # Calculate confidence intervals
        mean1, sem1, l1, u1 = _mean_sem_ci(data1)
        mean2, sem2, l2, u2 = _mean_sem_ci(data2)

        rows.append(
            {
                "group1": group_a,
                "group2": group_b,
                "t_stat": float(t_stat),
                "p_value": float(p_val),
                "cohen_d": float(cohen_d) if not np.isnan(cohen_d) else np.nan,
                "mean1": float(mean1),
                "mean2": float(mean2),
                "n1": int(n1),
                "n2": int(n2),
                "ci1_lower": float(l1),
                "ci1_upper": float(u1),
                "ci2_lower": float(l2),
                "ci2_upper": float(u2),
            }
        )

    pairwise_df = pd.DataFrame(rows)
    return float(anova_stat), float(anova_p), pairwise_df


@st.cache_data
def perform_anova_test(groups: list) -> Dict:
    """
    Perform one-way ANOVA test on multiple groups.

    This function performs a standard one-way ANOVA and calculates
    eta-squared as a measure of effect size (proportion of variance explained).

    Args:
        groups: List of arrays, one for each group (each containing numeric values)

    Returns:
        Dict with keys:
        - f_statistic: F-statistic from ANOVA test
        - p_value: P-value indicating significance
        - eta_squared: Effect size (0 to 1, proportion of variance explained)

    Note:
        Requires at least 2 non-empty groups. Empty groups are automatically
        filtered out. Eta-squared of 0.01, 0.06, 0.14 represent small, medium,
        and large effects respectively.

    Example:
        >>> group1 = np.array([1.2, 1.5, 1.8])
        >>> group2 = np.array([2.1, 2.3, 2.5])
        >>> results = perform_anova_test([group1, group2])
        >>> print(f"F={results['f_statistic']:.3f}, η²={results['eta_squared']:.3f}")
    """
    if len(groups) < 2:
        return {"f_statistic": np.nan, "p_value": np.nan, "eta_squared": np.nan}

    # Filter out empty groups
    valid_groups = [g for g in groups if len(g) > 0]
    if len(valid_groups) < 2:
        return {"f_statistic": np.nan, "p_value": np.nan, "eta_squared": np.nan}

    # Perform ANOVA
    f_stat, p_value = f_oneway(*valid_groups)

    # Calculate eta squared (effect size)
    all_data = np.concatenate(valid_groups)
    grand_mean = np.mean(all_data)
    ss_total = np.sum((all_data - grand_mean) ** 2)
    ss_between = sum(len(g) * (np.mean(g) - grand_mean) ** 2 for g in valid_groups)
    eta_squared = ss_between / ss_total if ss_total > 0 else 0

    return {
        "f_statistic": float(f_stat),
        "p_value": float(p_value),
        "eta_squared": float(eta_squared),
    }


@st.cache_data
def perform_chi_square_test(contingency_table: "pd.DataFrame | np.ndarray") -> Dict:
    """
    Perform chi-square test of independence on a contingency table.

    Tests whether two categorical variables are independent. The null hypothesis
    is that the variables are independent (no association).

    Args:
        contingency_table: 2D array or DataFrame with observed frequencies

    Returns:
        Dict with keys:
        - chi2_statistic: Chi-square test statistic
        - p_value: P-value indicating significance of association
        - cramers_v: Effect size (0 to 1, Cramér's V)

    Raises:
        ValueError: If contingency table has fewer than 2 dimensions

    Note:
        Cramér's V ranges from 0 (no association) to 1 (perfect association).
        Values of 0.1, 0.3, 0.5 represent small, medium, and large effects.
        Expected cell counts should generally be ≥ 5.

    Example:
        >>> ct = np.array([[10, 20], [30, 40]])
        >>> results = perform_chi_square_test(ct)
        >>> print(f"χ²={results['chi2_statistic']:.3f}, V={results['cramers_v']:.3f}")
    """
    if isinstance(contingency_table, pd.DataFrame):
        contingency_table = contingency_table.values

    # Perform chi-square test
    chi2_stat, p_value, dof, expected = chi2_contingency(contingency_table)

    # Calculate Cramér's V (effect size for chi-square)
    n = np.sum(contingency_table)
    min_dim = min(contingency_table.shape) - 1
    cramers_v = np.sqrt(chi2_stat / (n * min_dim)) if min_dim > 0 else 0

    return {
        "chi2_statistic": float(chi2_stat),
        "p_value": float(p_value),
        "cramers_v": float(cramers_v),
    }


def test_normality_assumptions(data: np.ndarray, alpha: float = 0.05) -> Dict:
    """
    Test normality assumptions using Shapiro-Wilk test.

    The Shapiro-Wilk test evaluates whether a sample comes from a
    normally distributed population. Important for parametric tests.

    Args:
        data: Array-like data to test for normality
        alpha: Significance level (default: 0.05)

    Returns:
        Dict with keys:
        - statistic: Shapiro-Wilk test statistic
        - p_value: P-value of the test
        - is_normal: Boolean indicating if data is normal at alpha level

    Note:
        Requires at least 3 data points. NaN values are automatically removed.
        If p-value > alpha, fail to reject null hypothesis of normality.
        Sensitivity increases with sample size.

    Example:
        >>> data = np.random.normal(100, 15, 100)
        >>> results = test_normality_assumptions(data)
        >>> print(f"Normal: {results['is_normal']}, p={results['p_value']:.4f}")
    """
    data = np.array(data)
    data = data[~np.isnan(data)]  # Remove NaN values

    if len(data) < 3:
        return {"statistic": np.nan, "p_value": np.nan, "is_normal": False}

    stat, p_value = shapiro(data)

    return {
        "statistic": float(stat),
        "p_value": float(p_value),
        "is_normal": p_value > alpha,
    }
