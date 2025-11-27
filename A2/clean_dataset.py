"""
Dataset Cleaning Script for London Airbnb Regression Analysis
=============================================================
This script preprocesses the raw Inside Airbnb dataset:
1. Cleans price column (removes $ symbols, converts to numeric)
2. Retains only columns needed for regression analysis
3. Drops rows with missing price values

Columns Retained (13 total):
- price: Target variable (nightly listing price)
- accommodates, bedrooms, beds: Core property characteristics
- room_type: Categorical predictor (entire home, private room, etc.)
- latitude, longitude: Geographic location for spatial analysis
- availability_365: Annual availability metric
- minimum_nights, maximum_nights: Booking constraints
- number_of_reviews: Popularity/reputation proxy
- property_type: Property classification
- bathrooms_text: Bathroom count (text format in raw data)

Columns Dropped (66 total):
- Identifiers: id, host_id, scrape_id
- URLs: listing_url, host_url, picture_url, host_thumbnail_url, etc.
- Text descriptions: name, description, neighborhood_overview, host_about
- Redundant/derived: calculated_host_listings_count variants, reviews_per_month
- High missingness (>50%): license, calendar_updated, neighbourhood_group_cleansed
- Temporal: first_review, last_review, host_since, calendar_last_scraped
"""

import pandas as pd

print("="*70)
print("LONDON AIRBNB DATASET CLEANING SCRIPT")
print("="*70)

# Load raw dataset
print("\n[1/4] Loading raw dataset...")
df = pd.read_csv('london_sample_10k.csv')
print(f"      Original shape: {df.shape[0]:,} rows × {df.shape[1]} columns")

# Clean price column
print("\n[2/4] Cleaning price column...")
df['price'] = df['price'].astype(str).str.replace(r'[\$,]', '', regex=True)
df['price'] = pd.to_numeric(df['price'], errors='coerce')
print(f"      Price range: £{df['price'].min():.2f} - £{df['price'].max():.2f}")
print(f"      Missing prices: {df['price'].isna().sum():,} rows ({df['price'].isna().sum()/len(df)*100:.1f}%)")

# Define columns to KEEP (based on regression analysis needs)
columns_to_keep = [
    # Target variable
    'price',
    
    # Core property characteristics (model predictors)
    'accommodates',
    'bedrooms', 
    'beds',
    'room_type',
    'property_type',
    'bathrooms_text',
    
    # Geographic location (for EDA visualizations)
    'latitude',
    'longitude',
    
    # Availability and booking (for EDA)
    'availability_365',
    'minimum_nights',
    'maximum_nights',
    
    # Reputation proxy
    'number_of_reviews',
]

# Filter to only existing columns
columns_to_keep = [col for col in columns_to_keep if col in df.columns]

print("\n[3/4] Selecting analysis columns...")
print(f"      Keeping {len(columns_to_keep)} columns:")
for col in columns_to_keep:
    missing = df[col].isna().sum()
    print(f"        - {col:20s} ({missing:,} missing)")

# Create cleaned dataframe
df_clean = df[columns_to_keep].copy()

# Drop rows with missing price (can't use for regression)
rows_before = len(df_clean)
df_clean = df_clean.dropna(subset=['price'])
rows_dropped = rows_before - len(df_clean)
print(f"\n      Dropped {rows_dropped:,} rows with missing price")

# Summary of what was dropped
columns_dropped = [col for col in df.columns if col not in columns_to_keep]
print(f"      Dropped {len(columns_dropped)} unnecessary columns")

print("\n[4/4] Saving cleaned dataset...")

# Save to new file first, then can be renamed
output_file = 'london_sample_10k_cleaned.csv'
df_clean.to_csv(output_file, index=False)
print(f"      ✓ Saved to: {output_file}")

print("\n" + "="*70)
print("CLEANING COMPLETE")
print("="*70)
print(f"  Original:  {df.shape[0]:,} rows × {df.shape[1]} columns")
print(f"  Cleaned:   {df_clean.shape[0]:,} rows × {df_clean.shape[1]} columns")
print(f"  Reduction: {len(columns_dropped)} columns dropped, {rows_dropped:,} rows removed")
print(f"  Price:     Converted from '$X,XXX.XX' string to numeric float")
print("="*70)

# Print columns dropped for documentation
print("\n" + "-"*70)
print("COLUMNS DROPPED (for appendix documentation):")
print("-"*70)
for i, col in enumerate(sorted(columns_dropped), 1):
    print(f"  {i:2d}. {col}")
