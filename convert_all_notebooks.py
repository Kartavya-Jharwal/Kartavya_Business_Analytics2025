#!/usr/bin/env python3
"""
Recursively convert all Jupyter notebooks to HTML and PDF formats
"""
import os
import subprocess
import sys
from pathlib import Path

def find_notebooks(root_dir):
    """Find all .ipynb files recursively"""
    root_path = Path(root_dir)
    notebooks = list(root_path.rglob("*.ipynb"))
    return notebooks

def create_output_dir(notebook_path):
    """Create outputs directory next to the notebook"""
    output_dir = notebook_path.parent / "outputs"
    output_dir.mkdir(exist_ok=True)
    return output_dir

def convert_notebook(notebook_path, output_format="html"):
    """Convert a single notebook to specified format"""
    output_dir = create_output_dir(notebook_path)
    
    try:
        cmd = [
            "uv", "run", "jupyter", "nbconvert",
            "--to", output_format,
            "--output-dir", str(output_dir),
            str(notebook_path)
        ]
        
        print(f"Converting {notebook_path.name} to {output_format.upper()}...")
        result = subprocess.run(cmd, capture_output=True, text=True, cwd=Path.cwd())
        
        if result.returncode == 0:
            print(f"✅ Success: {notebook_path.name} → {output_format.upper()}")
            return True
        else:
            print(f"❌ Failed: {notebook_path.name} → {output_format.upper()}")
            print(f"Error: {result.stderr}")
            return False
            
    except Exception as e:
        print(f"❌ Exception converting {notebook_path.name}: {e}")
        return False

def main():
    """Main conversion function"""
    root_dir = Path.cwd()
    print(f"🔍 Searching for notebooks in: {root_dir}")
    
    notebooks = find_notebooks(root_dir)
    print(f"📚 Found {len(notebooks)} notebooks")
    
    html_success = 0
    pdf_success = 0
    total = len(notebooks)
    
    for notebook in notebooks:
        print(f"\n📄 Processing: {notebook.relative_to(root_dir)}")
        
        # Convert to HTML
        if convert_notebook(notebook, "html"):
            html_success += 1
            
        # Convert to PDF using webpdf
        if convert_notebook(notebook, "webpdf"):
            pdf_success += 1
    
    print(f"\n🎉 Conversion Summary:")
    print(f"   📊 Total notebooks: {total}")
    print(f"   🌐 HTML success: {html_success}/{total}")
    print(f"   📄 PDF success: {pdf_success}/{total}")

if __name__ == "__main__":
    main()