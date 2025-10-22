import pandas as pd
import numpy as np

# Load and process data exactly as your notebook does
df_gdp = pd.read_csv('gdp-per-capita-worldbank-constant-usd/gdp-per-capita-worldbank-constant-usd.csv')
df_co2 = pd.read_csv('co-emissions-per-capita/co-emissions-per-capita.csv')

# Merge
merged = pd.merge(df_gdp, df_co2, on=['Entity', 'Year'], how='inner', suffixes=('_gdp', '_co2'))
merged.rename(columns={'Entity': 'Country'}, inplace=True)

# Find columns
gdp_col = [c for c in merged.columns if 'gdp' in c.lower() and 'capita' in c.lower()][0]
co2_col = [c for c in merged.columns if ('co2' in c.lower() or 'emission' in c.lower()) and 'code' not in c.lower()][0]

# Create GDP categories
merged[gdp_col] = pd.to_numeric(merged[gdp_col], errors='coerce')
merged = merged.dropna(subset=[gdp_col])
merged['GDP_Category'] = pd.cut(merged[gdp_col], bins=[-np.inf, 5000, 15000, np.inf], labels=['Low', 'Medium', 'High'])

# Group by Year and GDP_Category
grouped_stats = (
    merged.groupby(['GDP_Category', 'Year'])[co2_col]
    .agg(['count', 'mean', 'std'])
    .reset_index()
)
grouped_stats['sem'] = grouped_stats['std'] / np.sqrt(grouped_stats['count'])
grouped_stats['ci_lower'] = grouped_stats['mean'] - 1.96 * grouped_stats['sem']
grouped_stats['ci_upper'] = grouped_stats['mean'] + 1.96 * grouped_stats['sem']

print("="*100)
print("TIMESERIES DATA DIAGNOSTICS - WHY YOUR GRAPH IS JAGGED")
print("="*100)

for category in ['Low', 'Medium', 'High']:
    cat_data = grouped_stats[grouped_stats['GDP_Category'] == category].sort_values('Year')
    print(f"\n{category.upper()} GDP COUNTRIES:")
    print(f"  • Years with data: {cat_data['Year'].min()} to {cat_data['Year'].max()}")
    print(f"  • Number of year points: {len(cat_data)}")
    print(f"  • Years MISSING (gaps): ", end="")
    
    all_years = set(range(int(cat_data['Year'].min()), int(cat_data['Year'].max()) + 1))
    available_years = set(cat_data['Year'].values)
    missing = sorted(all_years - available_years)
    
    if missing:
        print(f"{len(missing)} gaps")
        if len(missing) < 10:
            print(f"    Missing years: {missing}")
    else:
        print("None (continuous data)")
    
    print(f"\n  Sample observations (every 5th year):")
    for idx, row in cat_data.iterrows():
        if int(row['Year']) % 5 == 0:
            print(f"    Year {int(row['Year'])}: n={int(row['count']):4d}, mean={row['mean']:7.2f}, "
                  f"CI=[{row['ci_lower']:7.2f}, {row['ci_upper']:7.2f}]")

print("\n" + "="*100)
print("DIAGNOSIS:")
print("="*100)
print("\nJagged lines usually happen when:")
print("1. ✗ Missing years in data (causes jumps)")
print("2. ✗ Small sample sizes per year (high variance in mean)")
print("3. ✗ Data not sorted by Year before plotting")
print("4. ✗ Different countries included in different years")
