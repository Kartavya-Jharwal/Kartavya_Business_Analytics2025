#!/usr/bin/env python3
"""
Recursively convert all Jupyter notebooks to HTML and PDF formats.

Output location policy
- Outputs are saved in the SAME DIRECTORY as the source notebook (no separate outputs folders).
- Example: foo/bar/notebook.ipynb -> foo/bar/notebook.html + foo/bar/notebook.pdf

If you previously exported into subfolders like "outputs", see the end-of-run tip
for a ready-to-copy robocopy command to flatten those folders back into their parents.
"""

from pathlib import Path
import subprocess

TEMPLATE_PATH = Path(__file__).parent / "A1" / "templates" / "custom_report.tpl"


def find_notebooks(root_dir):
    """Find all .ipynb files recursively, excluding hidden directories"""
    root_path = Path(root_dir)
    notebooks = [
        nb
        for nb in root_path.rglob("*.ipynb")
        if not any(part.startswith(".") for part in nb.parts)
    ]
    return notebooks


def convert_notebook(notebook_path, output_format="html"):
    """Convert a single notebook to specified format in the same directory"""
    output_dir = notebook_path.parent
    stem = notebook_path.stem
    expected_name = (
        f"{stem}.pdf" if output_format in ("webpdf", "pdf") else f"{stem}.html"
    )
    expected_path = output_dir / expected_name

    try:
        cmd = [
            "uv",
            "run",
            "jupyter",
            "nbconvert",
            "--to",
            output_format,
            "--output-dir",
            str(output_dir),
        ]

        # Only add template for A1 notebooks (assignment)
        if TEMPLATE_PATH.exists() and output_format in ["html", "webpdf", "pdf"]:
            if "A1" in str(notebook_path):
                cmd.extend(["--template", str(TEMPLATE_PATH)])

        cmd.append(str(notebook_path))

        print("📓 Converting:")
        print(f"  • Notebook     : {notebook_path.relative_to(Path.cwd())}")
        print(f"  • Output dir   : {output_dir.relative_to(Path.cwd())}")
        print(f"  • Will produce : {expected_name} (same directory policy)")

        result = subprocess.run(cmd, capture_output=True, text=True, cwd=Path.cwd())

        if result.returncode == 0:
            print(f"  ✓ Success: {expected_path.relative_to(Path.cwd())}")
            return True
        else:
            print(f"  ✗ Failed: {output_format.upper()} conversion")
            if result.stderr:
                # Show a longer chunk to aid debugging, but keep it bounded
                print(f"  Error (truncated): {result.stderr[:800]}")
            return False

    except Exception as e:
        print(f"  ✗ Exception: {e}")
        return False


def main():
    """Main conversion function"""
    root_dir = Path.cwd()
    print(
        "🏗️ Output policy: HTML/PDF files are written to the SAME folder as their source .ipynb"
    )
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

    # Guidance: If any historical runs wrote into subfolders like "outputs",
    # provide a ready-to-copy robocopy command to flatten them.
    outputs_dirs = sorted(
        {p.parent for p in root_dir.rglob("outputs/*.ipynb")}
    )  # unlikely, but placeholder
    # Better: find any directory actually named 'outputs'
    outputs_dirs = sorted({d for d in root_dir.rglob("outputs") if d.is_dir()})
    if outputs_dirs:
        print(
            "\n🧹 Flattening tip (Windows): Move HTML/PDF up from any 'outputs' folders to their parent directories"
        )
        print(
            "   Use robocopy with /MOV to move (not copy) files and remove them from the subfolder."
        )
        for d in outputs_dirs:
            parent = d.parent
            # Quote paths for safety
            src = str(d)
            dst = str(parent)
            print("\n   Example for:")
            print(f"   • Source : {src}")
            print(f"   • Dest   : {dst}")
            print("   Command (copy & run in PowerShell):")
            print(
                '   robocopy "'
                + src
                + '" "'
                + dst
                + '" *.html *.pdf /MOV /V /ETA /NP /R:1 /W:1'
            )


if __name__ == "__main__":
    main()
