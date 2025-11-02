## CarbonSeer — project overview (consolidated)

CarbonSeer is an interdisciplinary microsite that pairs rigorous business analytics with professional brand design. It was created as a demonstration platform (Redshaw Advisors) to explore GDP, CO₂ emissions, and net-zero commitments and to present results in a polished Streamlit microsite.

Essential quick links
- App entry: `app.py`
- Project docs archive: `archives/all_markdowns_archive.md` (all legacy markdown consolidated)
- GitHub agent / developer guidance: `.github/copilot-instructions.md`

Run (local)
```powershell
uv sync
uv run streamlit run app.py
```

Static site (quick view of CSV-driven plots)
```powershell
python -m http.server 8000
# then open http://localhost:8000/site/
```

Design & docs
- Core design system and styling: `utils/styling.py`
- Data loading & analysis utilities: `utils/data_loader.py`, `utils/analysis.py`
- Archived auxiliary docs: `archives/all_markdowns_archive.md`

If you need a specific older document restored, you can recover any removed file from git history or contact the repo owner; the archive file contains an index of moved files.

Enjoy exploring the project — the main app is the canonical, runnable artifact for demonstrations and evaluation.
