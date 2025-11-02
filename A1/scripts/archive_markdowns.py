import shutil
from pathlib import Path

root = Path(__file__).parent.parent
archives_root = root / 'archives' / 'markdowns'
archives_root.mkdir(parents=True, exist_ok=True)

exclude = {
    str(root / 'README.md'),
    str(root / '.github' / 'copilot-instructions.md'),
}

md_files = list(root.glob('**/*.md'))
# Exclude files already in archives directory and the exclude set
md_files = [p for p in md_files if 'archives' not in p.parts and str(p) not in exclude]

print(f'Found {len(md_files)} markdown files to archive (excluding README and copilot-instructions).')

for p in md_files:
    rel = p.relative_to(root)
    target = archives_root / rel
    target.parent.mkdir(parents=True, exist_ok=True)
    # Move the file to archive
    shutil.move(str(p), str(target))
    # Create a stub at original location
    stub = p
    stub.parent.mkdir(parents=True, exist_ok=True)
    with open(stub, 'w', encoding='utf-8') as f:
        f.write(f"# Archived: {rel.name}\n\nThis document has been archived and moved to `archives/markdowns/{rel}`.\n\nTo view the original content, open the file under `archives/markdowns/` or check the git history for older versions.\n")
    print(f'Archived {rel} -> archives/markdowns/{rel}')

print('Archival complete.')
