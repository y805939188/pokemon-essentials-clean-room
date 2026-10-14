import sys,json,hashlib,datetime,subprocess
from pathlib import Path

OUT=Path(__file__).resolve().parent
label=sys.argv[1]
assert label in ['package-manifest','publication-manifest']
target=OUT/(label+'.json'); assert not target.exists()
rows=[]
for p in sorted(OUT.rglob('*')):
 if not p.is_file() or p==target:continue
 if subprocess.run(['git','check-ignore','-q',str(p)],capture_output=True).returncode==0:continue
 data=p.read_bytes()
 rows.append({'path':str(p.relative_to(Path.cwd())),'mode':'100644','type':'blob','bytes':len(data),
 'sha256':hashlib.sha256(data).hexdigest(),'git_blob':hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()})
manifest={'schema':'R6.U06.reviewer-finite-manifest.v1','utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'phase':label,'payloads':rows,'path_count':len(rows),'byte_count':sum(r['bytes'] for r in rows),
 'excluded':[str(target.relative_to(Path.cwd())),'Git-ignored remote object caches/bytecode',
  'post-freeze future commit/push/readback artifacts are not part of this finite cohort; included at next finite publication or final external receipt'],
 'self_identity':'Own bytes/blob not recursively included; entire actual Git tree externally bound by frozen C/P.',
 'transport_logs':'Raw stdout/stderr preserved; meaningful whitespace is not rewritten for style checks.'}
target.write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'result':'MANIFEST_WRITTEN','phase':label,'path_count':len(rows),'byte_count':manifest['byte_count']}))
