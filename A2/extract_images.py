"""
Extract base64-encoded images from Jupyter notebook HTML export.
Improved version - captures all unique chart outputs.
"""

import re
import base64
from pathlib import Path
from hashlib import md5

# Paths
HTML_FILE = Path("Final_export.html")
OUTPUT_DIR = Path("img")

# Ensure output directory exists
OUTPUT_DIR.mkdir(exist_ok=True)

# Read HTML content
print(f"Reading {HTML_FILE}...")
with open(HTML_FILE, "r", encoding="utf-8") as f:
    html_content = f.read()

# More comprehensive pattern - capture full base64 strings
pattern = r'data:image/(png|jpeg|jpg|gif|webp);base64,([A-Za-z0-9+/]+=*)'

matches = re.findall(pattern, html_content)
print(f"Found {len(matches)} total image references")

# Deduplicate by full content hash (some images repeat)
seen_hashes = set()
unique_images = []
for img_type, b64_data in matches:
    # Skip very small images (likely icons, < 1KB)
    if len(b64_data) < 1000:
        continue
    
    # Hash the content for deduplication
    content_hash = md5(b64_data.encode()).hexdigest()[:16]
    if content_hash not in seen_hashes:
        seen_hashes.add(content_hash)
        unique_images.append((img_type, b64_data, len(b64_data)))

# Sort by appearance order (keep original order from HTML)
# Don't sort by size - maintain notebook order
print(f"Found {len(unique_images)} unique images (>1KB)")

# Descriptive names based on expected notebook order
image_names = [
    "01_price_histogram",
    "02_price_boxplot", 
    "03_room_type_boxplot",
    "04_price_vs_accommodates",
    "05_price_vs_bedrooms",
    "06_correlation_matrix",
    "07_geographic_heatmap",
    "08_availability_histogram",
    "09_availability_vs_price",
    "10_minimum_nights_histogram",
    "11_minimum_nights_by_category",
    "12_coefficient_bar_chart",
    "13_observed_vs_predicted",
    "14_residual_histogram",
    "15_residuals_vs_fitted",
    "16_confusion_matrix",
]

# Extract and save each image
saved_count = 0
for i, (img_type, b64_data, size) in enumerate(unique_images):
    # Get name or generate one
    if i < len(image_names):
        name = image_names[i]
    else:
        name = f"chart_{i+1:02d}"
    
    # Determine file extension
    ext = "png" if img_type == "png" else img_type
    filename = OUTPUT_DIR / f"{name}.{ext}"
    
    try:
        # Decode base64
        img_bytes = base64.b64decode(b64_data)
        
        # Save to file
        with open(filename, "wb") as f:
            f.write(img_bytes)
        
        size_kb = len(img_bytes) / 1024
        print(f"  ✓ {filename.name:40s} ({size_kb:,.1f} KB)")
        saved_count += 1
    except Exception as e:
        print(f"  ✗ Failed: {name} - {e}")

print(f"\n{'='*50}")
print(f"Done! {saved_count} images saved to {OUTPUT_DIR}/")
print(f"\nTo use in slides:")
print(f"  ![Chart Name](img/01_price_histogram.png)")
