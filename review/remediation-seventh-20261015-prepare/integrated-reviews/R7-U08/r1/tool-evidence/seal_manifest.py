import json,hashlib,datetime,os
from pathlib import Path
OUT=Path(__file__).parent.parent
rows=[]
for p in sorted(OUT.rglob('*')):
 if p.is_file() and p.name!='artifact-manifest.json':
  b=p.read_bytes();rows.append({'path':p.relative_to(OUT).as_posix(),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'git_blob':hashlib.sha1(f'blob {len(b)}\0'.encode()+b).hexdigest()})
j={'schema':'r7.u08.independent-actual-review-artifact-manifest.v1','utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'tool_pid':os.getpid(),'files':rows,'file_count_excluding_manifest':len(rows),'total_bytes_excluding_manifest':sum(x['bytes'] for x in rows),'self_qualification':'Manifest excludes only itself. Exact manifest bytes and every result file, modes, result commit and tree are bound by the complete immutable-commit remote readback. No guessed self hash/commit.','behavior_execution_credit':False,'configuration_credit':False}
(OUT/'artifact-manifest.json').write_text(json.dumps(j,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'files_excluding_manifest':len(rows),'bytes_excluding_manifest':j['total_bytes_excluding_manifest'],'utc':j['utc'],'tool_pid':os.getpid()}))
