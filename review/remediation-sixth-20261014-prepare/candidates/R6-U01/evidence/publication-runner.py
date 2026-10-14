"""Ordinary branch publication and finite full-byte remote readback; logs in /tmp."""
from pathlib import Path
import subprocess,json,hashlib,datetime,sys,urllib.request,urllib.parse,concurrent.futures,time
ROOT=Path.cwd();B=Path('review/remediation-sixth-20261014-prepare/candidates/R6-U01');BRANCH='codex/remediation-sixth-r6-u01-author-20261014';CORE='d13dc8446d0e47c659f81c86413aeafb2279da01';OUT=Path('/tmp/r6-u01-publication');OUT.mkdir(exist_ok=True)
ident=lambda b:{'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'git_blob':hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()}
now=lambda:datetime.datetime.now(datetime.timezone.utc).isoformat()
def capture(args):
 start=now();r=subprocess.run(args,cwd=ROOT,capture_output=True);n=len(list(OUT.glob('command-*.json')))+1;prefix=OUT/f'command-{n:03d}'
 prefix.with_suffix('.stdout').write_bytes(r.stdout);prefix.with_suffix('.stderr').write_bytes(r.stderr)
 prefix.with_suffix('.json').write_text(json.dumps({'argv':args,'cwd':str(ROOT),'utc_start':start,'utc_end':now(),'exit_code':r.returncode,'stdout_path':str(prefix.with_suffix('.stdout')),'stderr_path':str(prefix.with_suffix('.stderr')),'stdout_identity':ident(r.stdout),'stderr_identity':ident(r.stderr)},ensure_ascii=False,indent=2)+'\n')
 if r.returncode:sys.stdout.buffer.write(r.stdout);sys.stderr.buffer.write(r.stderr);raise RuntimeError((args,r.returncode))
 return r.stdout
head=capture(['git','rev-parse','HEAD']).decode().strip();assert head!=CORE
assert not capture(['git','status','--porcelain'])
push=capture(['git','push','origin','HEAD:refs/heads/'+BRANCH]);print('Ordinary push completed',head,flush=True)
remote=capture(['git','ls-remote','--heads','origin',BRANCH]).decode().split()[0];assert remote==head
DB=OUT/'remote-objects.git'
if not DB.exists():capture(['git','init','--bare',str(DB)])
capture(['git','-C',str(DB),'fetch','--depth=2','--filter=blob:none','https://github.com/y805939188/pokemon-essentials-clean-room.git','refs/heads/'+BRANCH])
remote_head=capture(['git','-C',str(DB),'rev-parse','FETCH_HEAD']).decode().strip();assert remote_head==head
ptree=capture(['git','-C',str(DB),'rev-parse',head+'^{tree}']).decode().strip();ctree=capture(['git','-C',str(DB),'rev-parse',CORE+'^{tree}']).decode().strip();candidate_tree=capture(['git','-C',str(DB),'rev-parse',head+':'+str(B)]).decode().strip()
assert ptree==capture(['git','rev-parse',head+'^{tree}']).decode().strip();assert ctree==capture(['git','rev-parse',CORE+'^{tree}']).decode().strip()
raw=capture(['git','-C',str(DB),'ls-tree','-r','-z',head,'--',str(B)])
entries=[]
for entry in raw.split(b'\0'):
 if not entry:continue
 metadata,path=entry.decode().split('\t',1);mode,kind,blob=metadata.split();b=(ROOT/path).read_bytes();expected=ident(b);assert expected['git_blob']==blob and mode=='100644' and kind=='blob';entries.append({'path':path,'mode':mode,'type':kind,**expected})
# Fetch full bodies once per blob; every path/type/mode is independently bound by fresh remote tree.
unique={r['git_blob']:r for r in entries};body_cache={}
def fetch(item):
 url='https://raw.githubusercontent.com/y805939188/pokemon-essentials-clean-room/'+head+'/'+urllib.parse.quote(item['path'],safe='/');attempts=[]
 for n in range(1,4):
  start=now()
  try:
   with urllib.request.urlopen(url,timeout=30) as response:b=response.read()
   actual=ident(b);assert all(actual[k]==item[k] for k in actual);attempts.append({'attempt':n,'utc_start':start,'utc_end':now(),'result':'FULL_BODY_MATCH','identity':actual});return item['git_blob'],b,attempts
  except Exception as ex:
   attempts.append({'attempt':n,'utc_start':start,'utc_end':now(),'result':'FAILED_RETAINED','error':repr(ex)})
   if n<3:time.sleep(1)
 return item['git_blob'],None,attempts
start=now();attempt_rows=[]
with concurrent.futures.ThreadPoolExecutor(max_workers=8) as pool:
 for blob,b,attempts in pool.map(fetch,list(unique.values())):body_cache[blob]=b;attempt_rows.append({'blob':blob,'attempts':attempts})
failed=[blob for blob,b in body_cache.items() if b is None];(OUT/'remote-body-attempts.json').write_text(json.dumps(attempt_rows,ensure_ascii=False,indent=2)+'\n');assert not failed,failed
readback=[]
for row in entries:
 b=body_cache[row['git_blob']];assert b==(ROOT/row['path']).read_bytes();readback.append(dict(row,full_byte_remote_body_match=True,remote_commit=head,remote_candidate_tree=candidate_tree))
# C manifests all finite core items except itself; each survives unchanged in published P.
core_manifest=json.loads(capture(['git','show',CORE+':'+str(B/'evidence/core-manifest.json')]))
for row in core_manifest['items']:
 b=(ROOT/row['path']).read_bytes();assert all(ident(b)[k]==row[k] for k in ident(b))
assert not capture(['git','diff','--name-only',CORE,head,'--',str(B/'mirror')]);assert not capture(['git','status','--porcelain'])
assert not capture(['git','diff','--name-only','8ea169fbd0f33f378b5d732fd6bea59e854e04a6','--','deliverables/final-specification-set'])
record={'state':'PUBLISHED_AUTHOR_CANDIDATE_FULL_BYTE_READBACK_VERIFIED','utc_start':start,'utc_end':now(),'branch':BRANCH,'core_commit':CORE,'core_tree':ctree,'publication_commit':head,'publication_tree':ptree,'candidate_directory_tree':candidate_tree,'verified_paths':len(entries),'distinct_full_bodies':len(unique),'readback':readback,'body_attempts_file':str(OUT/'remote-body-attempts.json'),'worktree_clean':True,'actual_formal_unchanged':True,'candidate_mirrors_unchanged_from_core':True,'independent_candidate_PASS':'PENDING_NONAUTHOR_ULTRA','integrated_PASS':'PENDING','formal_acceptance':'NOT_GRANTED','CLOSED':'NOT_REGISTERED','source_model_host_UI_Demo_save_execution':0}
(OUT/'remote-readback.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n');print(json.dumps({k:v for k,v in record.items() if k!='readback'},ensure_ascii=False),flush=True)
