import pandas as pd
import numpy as np

# Load data
df = pd.read_csv('gdp-per-capita-worldbank-constant-usd/gdp-per-capita-worldbank-constant-usd.csv')
co2 = pd.read_csv('co-emissions-per-capita/co-emissions-per-capita.csv')

# Merge
merged = pd.merge(df, co2, on=['Entity', 'Year'], how='inner', suffixes=('_gdp', '_co2'))
merged.rename(columns={'Entity': 'Country'}, inplace=True)

# Create GDP categories
gdp_col = [c for c in merged.columns if 'gdp' in c.lower() and 'capita' in c.lower()][0]
co2_col = [c for c in merged.columns if 'co2' in c.lower() or 'emission' in c.lower()][0]
co2_col = [c for c in [co2_col] if 'code' not in c.lower()][0]

merged[gdp_col] = pd.to_numeric(merged[gdp_col], errors='coerce')
merged = merged.dropna(subset=[gdp_col])

merged['GDP_Category'] = pd.cut(
    merged[gdp_col],
    bins=[-float('inf'), 5000, 15000, float('inf')],
    labels=['Low', 'Medium', 'High']
)

print("="*80)
print("TIMESERIES DATA DIAGNOSTICS")
print("="*80)

print("\n1. GDP Category Distribution:")
print(merged['GDP_Category'].value_counts().sort_index())

print("\n2. Year Range:")
print(f"   Min: {merged['Year'].min()}, Max: {merged['Year'].max()}")

print("\n3. Data by GDP Category and Year:")
grouped = merged.groupby(['GDP_Category', 'Year']).size().reset_index(name='count')
print(grouped.head(15))

print("\n4. Average CO2 by GDP Category and Year (first 10 years with data):")
avg_by_cat = merged.groupby(['Year', 'GDP_Category'])[co2_col].agg(['mean', 'count']).reset_index()
print(avg_by_cat[avg_by_cat['Year'] <= 1995])

print("\n5. Missing data in CO2 column:")
print(f"   {merged[co2_col].isnull().sum()} missing values out of {len(merged)}")

print("\n6. Sample of actual data:")
print(merged[['Country', 'Year', 'GDP_Category', gdp_col, co2_col]].head(10))
