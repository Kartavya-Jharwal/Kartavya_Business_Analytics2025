"""
Statistical analysis helpers ported from the notebook for use in the Streamlit app.
"""
import pandas as pd
import numpy as np
import streamlit as st
from scipy.stats import pearsonr, spearmanr, f_oneway, ttest_ind


@st.cache_data
def compute_correlations(df, x_col, y_col, sample_limit=5000):
    """Compute Pearson and Spearman correlations between two columns.

    Returns a dict with statistic and p-values plus R^2 for Pearson.
    """
    clean = df[[x_col, y_col]].dropna()
    if len(clean) == 0:
        return None

    # sampling for large data to keep Shapiro/pearson stable as notebook did
    if len(clean) > sample_limit:
        sample = clean.sample(sample_limit, random_state=42)
    else:
        sample = clean

    x = sample[x_col]
    y = sample[y_col]

    pearson_r, pearson_p = pearsonr(x, y)
    spearman_rho, spearman_p = spearmanr(x, y)
    r_squared = pearson_r ** 2

    return {
        "pearson_r": pearson_r,
        "pearson_p": pearson_p,
        "spearman_rho": spearman_rho,
        "spearman_p": spearman_p,
        "r_squared": r_squared,
        "n": len(sample),
    }


def _mean_sem_ci(arr, alpha=0.05):
    arr = np.array(arr)
    arr = arr[~np.isnan(arr)]
    n = len(arr)
    if n == 0:
        return (np.nan, np.nan, np.nan, np.nan)
    mean = arr.mean()
    sem = arr.std(ddof=1) / np.sqrt(n) if n > 1 else 0.0
    z = 1.96  # approximate for 95% CI
    lower = mean - z * sem
    upper = mean + z * sem
    return mean, sem, lower, upper


@st.cache_data
def compute_anova_and_pairwise(df, value_col, group_col):
    """Perform one-way ANOVA across groups and Welch pairwise t-tests.

    Returns (anova_stat, anova_p, pairwise_df)
    """
    groups = df.groupby(group_col)[value_col].apply(lambda s: s.dropna().values)
    # Filter out empty groups
    groups = {k: v for k, v in groups.items() if len(v) > 0}
    if len(groups) < 2:
        return None, None, pd.DataFrame()

    # ANOVA (one-way)
    anova_stat, anova_p = f_oneway(*[groups[k] for k in groups])

    # Pairwise Welch t-tests and Cohen's d
    rows = []
    keys = list(groups.keys())
    from itertools import combinations

    for a, b in combinations(keys, 2):
        data1 = groups[a]
        data2 = groups[b]
        t_stat, p_val = ttest_ind(data1, data2, equal_var=False)

        # Cohen's d (using pooled std) adjusted for unequal variances (approx)
        n1 = len(data1)
        n2 = len(data2)
        m1 = np.mean(data1)
        m2 = np.mean(data2)
        s1 = np.std(data1, ddof=1)
        s2 = np.std(data2, ddof=1)
        # Hedges' g / Cohen's d approximate pooled sd
        try:
            pooled_sd = np.sqrt(((n1 - 1) * s1 ** 2 + (n2 - 1) * s2 ** 2) / (n1 + n2 - 2))
            cohen_d = (m1 - m2) / pooled_sd if pooled_sd > 0 else np.nan
        except Exception:
            cohen_d = np.nan

        mean1, sem1, l1, u1 = _mean_sem_ci(data1)
        mean2, sem2, l2, u2 = _mean_sem_ci(data2)

        rows.append(
            {
                "group1": a,
                "group2": b,
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
