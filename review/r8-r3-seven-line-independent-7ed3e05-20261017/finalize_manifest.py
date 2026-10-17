#!/usr/bin/env python3
"""Manifest of review output bytes; its own JSON entry is intentionally excluded."""
from pathlib import Path
import hashlib,json
out=Path(__file__).resolve().parent
records=[]
for p in sorted(out.rglob('*')):
 if not p.is_file()or p.name=='output-file-manifest.json':continue
 b=p.read_bytes();records.append({'path':str(p.relative_to(out)),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()})
(out/'output-file-manifest.json').write_text(json.dumps({'schema':'r8-r3-seven-independent-output-manifest.v1','reviewed_candidate':'7ed3e0554ac24339a7e61cab152f628037111644','files':records,'count':len(records),'self_excluded':'output-file-manifest.json; future commit SHA is externally bound by publication/readback and final handoff, not self-asserted.'},ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'files_except_manifest':len(records),'bytes_except_manifest':sum(x['bytes']for x in records)}))
