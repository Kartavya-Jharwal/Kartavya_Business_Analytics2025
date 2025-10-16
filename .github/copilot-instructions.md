# Copilot Instructions for Kartavya_Business_Analytics2025

This repo contains teaching dashboards and notebooks for Business Analytics. The Streamlit app lives in `A1/` and there is repository-level tooling (notebook export, PDF generation) managed at the repo root.

# Copilot Instructions for Kartavya_Business_Analytics2025

This repository contains teaching dashboards and notebooks for Business Analytics. The Streamlit app lives in `A1/` and repository-level tooling (notebook export, PDF generation) is managed at the repo root.

What changed / why you're here
- The repo uses UV (astral-sh) for reproducible environments. The project previously had two UV configurations; this repository has been consolidated to a single root-level UV environment:
  - Root `pyproject.toml` — now contains both repo-wide tooling (nbconvert, pypandoc, PDF/system deps) and the Streamlit app runtime dependencies (matplotlib, seaborn, streamlit-extras, etc.).
  - The original `A1/pyproject.toml` has been moved to `A1/pyproject.toml.bak` for history.

Top-level facts (quick scan)
- Dashboard entrypoint: `A1/app.py` (uses `A1/utils/*` for data and styling).
- Notebooks: `A1/assignment.ipynb` is the CI target for HTML/PDF export; templates live in `A1/templates/custom_report.tpl`.
- Datasets live under `A1/` (gdp, co2, net-zero targets). Data loaders normalize `Entity` → `Country`.

Developer workflows — exact commands (PowerShell)
Recommended workflows now (single root UV)

- Install all dependencies (root):

```pwsh
cd <repo-root>
uv sync --locked --all-extras --dev
```

- Run the Streamlit app (root uv still runs the app from A1):

```pwsh
cd <repo-root>
uv run streamlit run A1/app.py
```

- Generate notebook HTML/PDF locally (mirrors CI; processes all notebooks in repo). Note: outputs are written to the same directory as the source notebook by policy:

```pwsh
cd <repo-root>
# Example: writes files next to the notebook (same-directory policy)
uv run jupyter nbconvert --to html --template A1/templates/custom_report.tpl --output-dir <notebook-folder> --output <notebook-name>.html <path-to-notebook>.ipynb
uv run jupyter nbconvert --to webpdf --template A1/templates/custom_report.tpl --output-dir <notebook-folder> --output <notebook-name>.pdf <path-to-notebook>.ipynb
```

CI and workflow notes
 - The repository-level workflow is `.github/workflows/generate-pdf.yml` (repo root). It:
  - Checks out the repo, installs uv (astral-sh/setup-uv@v6), and runs `uv sync --locked --all-extras --dev`.
  - Installs system PDF deps (pandoc, TeX packages, wkhtmltopdf) on runner.
  - Runs `uv run jupyter nbconvert` using the template at `A1/templates/custom_report.tpl` and writes outputs to the same directory as each notebook.
  - Uploads HTML/PDF artifacts and (on pushes to main) creates a GitHub release with the generated artifacts.

Repository-specific conventions (do not change unless intentional)
- Data loading: `A1/utils/data_loader.py` uses `@st.cache_data` for all loaders/transformers — preserve or consciously refactor caching behavior.
- Column naming: CSVs use `Entity` originally; data loaders rename to `Country`. New transforms should keep the `Country` column.
- Styling: `A1/utils/styling.py` exposes `get_custom_css()` and theming helpers used by `A1/app.py`.
-- Outputs: CI and local nbconvert write outputs to the same directory as each source notebook (no mandatory `outputs/` folder). Some older docs may still reference `A1/outputs/` — those will be updated shortly.

Integration points and edge cases
- PDF toolchain: CI installs pandoc + TeX + wkhtmltopdf. On Windows, prefer `--to webpdf` (nbconvert) or install wkhtmltopdf/pandoc locally.
- Keep `A1/pyproject.toml` for the app. The root `pyproject.toml` is for notebooks and CI. If you merge them, update the workflow to `uv sync` at the single chosen location.
- When editing CI workflow or templates, run a local export from the repo root to validate (see commands above).

Key files to inspect when making changes
- `A1/app.py` — Streamlit entrypoint and UI layout
- `A1/utils/data_loader.py` — data loading, merging, and category helpers (uses `@st.cache_data`)
- `A1/utils/styling.py` — CSS and Plotly theme helpers
- `A1/templates/custom_report.tpl` — nbconvert template for HTML/PDF
- `pyproject.toml` (repo root) — repo-wide tooling and nbconvert deps
- `A1/pyproject.toml` — app runtime deps
- `.github/workflows/generate-pdf.yml` — repo-level CI workflow (generates PDF/HTML)

When to edit the `pyproject.toml`
- The canonical dependency file is now the root `pyproject.toml`. Add or update dependencies there. After editing, run `uv sync` at repo root.
- `A1/pyproject.toml.bak` is a preserved copy of the previous app-specific file; do not edit it.

Quick checklist for common tasks
- Add a Streamlit feature: Edit `A1/app.py` + `A1/utils/*` → test locally with `cd A1 && uv run streamlit run app.py`.
- Change PDF template: Edit `A1/templates/custom_report.tpl` → test by running nbconvert from repo root.
- Change CI behavior: Edit `.github/workflows/generate-pdf.yml` (repo root) and validate with a manual workflow dispatch.

If you want a single `uv` environment instead
- Tell me which environment you prefer (root or `A1/`) and I will:
  - Consolidate dependencies into a single `pyproject.toml`,
  - Update the CI workflow to run `uv sync` in the chosen directory,
  - Run quick local validations and update this instruction doc.

---
If anything above is unclear or you want me to consolidate the `uv` environments and fully validate (run `uv sync`, run a local nbconvert test), tell me which option you prefer and I will proceed.
