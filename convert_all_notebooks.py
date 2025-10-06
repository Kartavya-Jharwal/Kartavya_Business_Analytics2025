#!/usr/bin/env python3
"""
Recursively convert all Jupyter notebooks to HTML and PDF formats.
Outputs are saved in the same directory as the source notebook.
"""
from pathlib import Path
import subprocess

TEMPLATE_PATH = Path(__file__).parent / "A1" / "templates" / "custom_report.tpl"

def find_notebooks(root_dir):
    """Find all .ipynb files recursively, excluding hidden directories"""
    root_path = Path(root_dir)
    notebooks = [
        nb for nb in root_path.rglob("*.ipynb")
        if not any(part.startswith('.') for part in nb.parts)
    ]
    return notebooks

def convert_notebook(notebook_path, output_format="html"):
    """Convert a single notebook to specified format in the same directory"""
    output_dir = notebook_path.parent
    
    try:
        cmd = [
            "uv", "run", "jupyter", "nbconvert",
            "--to", output_format,
            "--output-dir", str(output_dir),
        ]
        
        # Add template if it exists and format is HTML or PDF
        if TEMPLATE_PATH.exists() and output_format in ["html", "webpdf", "pdf"]:
            cmd.extend(["--template", str(TEMPLATE_PATH)])
        
        cmd.append(str(notebook_path))
        
        print(f"📓 Converting {notebook_path.relative_to(Path.cwd())} to {output_format.upper()}...")
        result = subprocess.run(cmd, capture_output=True, text=True, cwd=Path.cwd())
        
        if result.returncode == 0:
            print(f"  ✓ Success: {output_format.upper()} created in {output_dir.relative_to(Path.cwd())}")
            return True
        else:
            print(f"  ✗ Failed: {output_format.upper()} conversion")
            if result.stderr:
                print(f"  Error: {result.stderr[:200]}")
            return False
            
    except Exception as e:
        print(f"  ✗ Exception: {e}")
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
    
    print("\n🎉 Conversion Summary:")
    print(f"   📊 Total notebooks: {total}")
    print(f"   🌐 HTML success: {html_success}/{total}")
    print(f"   📄 PDF success: {pdf_success}/{total}")

if __name__ == "__main__":
    main()