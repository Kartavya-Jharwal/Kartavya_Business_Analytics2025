#!/usr/bin/env python3
"""
NBPrint - Recursive Notebook to PDF Converter

Usage:
    uv run nbprint <notebook_name.ipynb>

Searches the current directory tree recursively for the notebook and converts it to PDF.
"""
import sys
import subprocess
from pathlib import Path


def find_notebook(notebook_name: str, search_root: Path = None) -> Path | None:
    """
    Recursively search for a notebook file starting from search_root.
    
    Args:
        notebook_name: Name of the notebook file (e.g., 'Week_10_Session_2.ipynb')
        search_root: Directory to start searching from (defaults to current directory)
    
    Returns:
        Path object if found, None otherwise
    """
    if search_root is None:
        search_root = Path.cwd()
    
    print(f"🔍 Searching for '{notebook_name}' in {search_root}...")
    
    # Search recursively, excluding hidden directories and common ignore patterns
    for notebook_path in search_root.rglob(notebook_name):
        # Skip hidden directories and common ignore patterns
        if any(part.startswith('.') for part in notebook_path.parts):
            continue
        if any(part in ['node_modules', '__pycache__', 'dist', 'build'] for part in notebook_path.parts):
            continue
        
        print(f"✓ Found: {notebook_path.relative_to(Path.cwd())}")
        return notebook_path
    
    return None


def convert_to_pdf(notebook_path: Path) -> bool:
    """
    Convert notebook to PDF using jupyter nbconvert.
    
    Args:
        notebook_path: Path to the notebook file
    
    Returns:
        True if conversion succeeded, False otherwise
    """
    output_dir = notebook_path.parent
    output_name = notebook_path.stem  # filename without extension
    
    print(f"📄 Converting to PDF...")
    print(f"  • Notebook: {notebook_path.name}")
    print(f"  • Output dir: {output_dir.relative_to(Path.cwd())}")
    print(f"  • Output file: {output_name}.pdf")
    
    try:
        # Run nbconvert with webpdf
        result = subprocess.run(
            [
                "jupyter", "nbconvert",
                "--to", "webpdf",
                "--output-dir", str(output_dir),
                "--output", output_name,
                str(notebook_path)
            ],
            capture_output=True,
            text=True,
            check=True
        )
        
        # Show any warnings
        if "WARNING" in result.stderr:
            print(f"⚠️  Warnings:")
            for line in result.stderr.split('\n'):
                if "WARNING" in line:
                    print(f"    {line.strip()}")
        
        pdf_path = output_dir / f"{output_name}.pdf"
        if pdf_path.exists():
            size_mb = pdf_path.stat().st_size / (1024 * 1024)
            print(f"✅ Success! PDF created: {pdf_path.relative_to(Path.cwd())} ({size_mb:.2f} MB)")
            return True
        else:
            print(f"❌ Error: PDF file not found after conversion")
            return False
            
    except subprocess.CalledProcessError as e:
        print(f"❌ Conversion failed!")
        print(f"Error output:")
        print(e.stderr)
        return False
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return False


def main():
    """Main entry point for nbprint CLI."""
    if len(sys.argv) != 2:
        print("Usage: uv run nbprint <notebook_name.ipynb>")
        print("\nExample:")
        print("  uv run nbprint Week_10_Session_2.ipynb")
        sys.exit(1)
    
    notebook_name = sys.argv[1]
    
    # Ensure the filename ends with .ipynb
    if not notebook_name.endswith('.ipynb'):
        notebook_name += '.ipynb'
    
    # Search for the notebook
    notebook_path = find_notebook(notebook_name)
    
    if notebook_path is None:
        print(f"❌ Could not find '{notebook_name}' in the current directory tree")
        sys.exit(1)
    
    # Convert to PDF
    success = convert_to_pdf(notebook_path)
    
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
