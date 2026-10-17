#!/usr/bin/env python3
"""Manifest of review output bytes; its own JSON entry is intentionally excluded."""
from pathlib import Path
import hashlib,json
out=Path(__file__).resolve().parent
records=[]
for p in sorted(out.rglob('*')):
 if not p.is_file()or p.name=='output-file-manifest.json':continue
 b=p.read_bytes();records.append({'path':str(p.relative_to(out)),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()})
(out/'output-file-manifest.json').write_text(json.dumps({'schema':'r8-disposition-r1-independent-output-manifest.v1','reviewed_candidate':'5666b7b912e2fb79b5119283ee6a37401a7071db','files':records,'count':len(records),'self_excluded':'output-file-manifest.json; future commit SHA is externally bound by publication/readback and final handoff, not self-asserted.'},ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'files_except_manifest':len(records),'bytes_except_manifest':sum(x['bytes']for x in records)}))
