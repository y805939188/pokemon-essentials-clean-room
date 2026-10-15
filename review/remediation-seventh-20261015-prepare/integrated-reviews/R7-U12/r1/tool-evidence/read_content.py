"""Page every distinct complete line, retaining a full source-line coverage map.

Exact repeated lines are emitted once. This avoids rereading identical historical
paragraphs across the entry documents; it does not replace content review with hashes.
"""
from pathlib import Path
import json
import hashlib
import sys

root = Path('/workspace/r7-ir-R7-U12/actual-input/actual')
out = Path(__file__).resolve().parent
files = sorted(p for p in root.rglob('*') if p.is_file())
seen = {}
pages = ['']
mapping = []
for path in files:
    rel = path.relative_to(root).as_posix()
    data = path.read_bytes()
    rows = []
    for number, line in enumerate(data.decode().splitlines(keepends=True), 1):
        if not line.strip():
            rows.append(dict(line=number, blank=True))
            continue
        if line in seen:
            rows.append(dict(line=number, identical_to=seen[line]))
            continue
        text = f'{rel}:{number}: {line}'
        if len((pages[-1]+text).encode()) > 26000 and pages[-1]: pages.append('')
        position = dict(page=len(pages), path=rel, line=number)
        seen[line] = position
        pages[-1] += text
        rows.append(dict(line=number, **{'read_page':len(pages)}))
    mapping.append(dict(path=rel,bytes=len(data),sha256=hashlib.sha256(data).hexdigest(),
                        lines=rows))
(out/'complete-content-line-map.json').write_text(json.dumps(dict(files=mapping,pages=len(pages),
    qualification='Every nonblank line is emitted once or points to an exactly identical emitted line. Tool generation is not semantic PASS.'),ensure_ascii=False,indent=2)+'\n')
if len(sys.argv)==1:
    print(json.dumps(dict(files=len(files),pages=len(pages),original_bytes=sum(p.stat().st_size for p in files),unique_line_bytes=sum(len(p.encode()) for p in pages))))
else:
    for n in map(int,sys.argv[1:]):
        print(f'PAGE {n}/{len(pages)}')
        print(pages[n-1])
