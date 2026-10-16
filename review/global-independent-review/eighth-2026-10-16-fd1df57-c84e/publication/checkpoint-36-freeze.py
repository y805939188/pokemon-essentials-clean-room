"""Exact C36 root-authorized report transport freeze; never executes recovered code."""
from pathlib import Path
import datetime,hashlib,json,stat,subprocess,sys
W=Path('/workspace/pokemon-essentials-clean-room');RR=W/'review/global-independent-review/eighth-2026-10-16-fd1df57-c84e'
PUB=RR/'publication';IO=PUB/'checkpoint-36-io';PREFIX=str(RR.relative_to(W))+'/'
HEAD='2460370f1e410bd49cc29e377b89662838aed2b3';BRANCH='codex/review-eighth-20261016-fd1df57-c84e'
OLD={PREFIX+'tasks/pbs_creature_current_cloud/'+n for n in ['dependency-identities.json','formal-dependency-identities.json','record-field-ledger.json','sync_current_state.py']}
events=[];hash_events=[]
def utc():return datetime.datetime.now(datetime.timezone.utc).isoformat()
def sha(b):return hashlib.sha256(b).hexdigest()
def oid(b):return hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()
def put(p,d):p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
def run(args,label,stdin=None):
 t=utc();p=subprocess.run(args,cwd=W,input=stdin,capture_output=True);e=dict(args=args,start_utc=t,end_utc=utc(),exit=p.returncode)
 for k,b in [('stdout',p.stdout),('stderr',p.stderr)]:
  f=IO/(label+'.'+k);assert not f.exists();f.write_bytes(b);e.update({k:str(f.relative_to(RR)),k+'_bytes':len(b),k+'_sha256':sha(b)})
 if stdin is not None:e.update(stdin_bytes=len(stdin),stdin_sha256=sha(stdin))
 f=IO/(label+'.operation.json');assert not f.exists();put(f,e);events.append(e);assert p.returncode==0,e
 return p.stdout
def git(*args,label):return run(['git','-C',str(W),*args],label)
def guard(label):
 assert git('rev-parse','HEAD',label=label+'-head').decode().strip()==HEAD
 assert git('branch','--show-current',label=label+'-branch').decode().strip()==BRANCH
 assert not git('diff','--cached','--name-only','-z',label=label+'-index')
def safe(path):
 q=Path(path);assert not q.is_absolute() and '..' not in q.parts and str(q).startswith(PREFIX)
 assert not any(c.endswith('.git') for c in q.parts) and '__pycache__' not in q.parts and 'tmp_pack_' not in str(q)
 assert not str(q).endswith(('.pyc','.tmp')) and str(q) not in OLD
 return str(q)
def exact(path,entry):
 path=safe(path);f=W/path;s=f.lstat();assert stat.S_ISREG(s.st_mode) and not f.is_symlink()
 b=f.read_bytes();assert len(b)==entry['bytes'] and sha(b)==entry['sha256'],path
 if 'blob' in entry:assert oid(b)==entry['blob'],path
 return path
def metadata(path):
 path=safe(path);f=W/path;s=f.lstat();assert stat.S_ISREG(s.st_mode) and not f.is_symlink()
 b=f.read_bytes();assert len(b)<100000000
 fmt='RAW_BYTES_NOT_JSON'
 if f.suffix in ['.json','.jsonl','.ndjson']:
  if f.suffix=='.json':json.loads(b);fmt='WHOLE_JSON_PARSED_MECHANICALLY'
  else:
   for line in b.splitlines():
    if line.strip():json.loads(line)
   fmt='EXPLICIT_NDJSON_ALL_NONEMPTY_LINES_PARSED'
 t=utc();p=subprocess.run(['git','-C',str(W),'hash-object','-w','--stdin'],input=b,capture_output=True)
 hash_events.append(dict(path=path,args=['git','-C',str(W),'hash-object','-w','--stdin'],start_utc=t,end_utc=utc(),exit=p.returncode,stdin_bytes=len(b),stdin_sha256=sha(b),stdout=p.stdout.decode(),stderr=p.stderr.decode(errors='replace')))
 assert p.returncode==0 and p.stdout.decode().strip()==oid(b) and f.read_bytes()==b
 return dict(path=path,mode='100644',type='blob',blob=oid(b),bytes=len(b),sha256=sha(b),actual_filesystem_mode=oct(stat.S_IMODE(s.st_mode)),format=fmt)
def main():
 assert sys.argv[1:]==['freeze-root-authorized'];assert not (PUB/'checkpoint-36-candidates.json').exists();guard('freeze-initial')
 source=(PUB/'checkpoint-35-prepare.py').read_text().replace('81cc98eec7cc81706e51c8b274e9ff7042c0868b',HEAD).replace('checkpoint-35-','checkpoint-36-').replace("'preflight-%02d.%s'","'freeze-preflight-%02d.%s'").replace('checkpoint-36-preflight.json','checkpoint-36-freeze-preflight.json').replace('gr8-checkpoint35-preflight/v1','gr8-checkpoint36-freeze-preflight/v1')
 pp=PUB/'checkpoint-36-freeze-preflight.py';assert not pp.exists();pp.write_text(source);run([sys.executable,'-B',str(pp)],'freeze-fresh-protected-preflight')
 hm=RR/'handoff/payload-manifest.json';raw=hm.read_bytes()
 assert len(raw)==32019 and sha(raw)=='775ec0036af0da8cf77c635ec08ac9836a04b9665cf4adeff73cedc52ccff746'
 handoff=json.loads(raw);assert handoff['payload_file_count']==45 and handoff['payload_bytes']==5535925
 allow={exact(x['path'],x) for x in handoff['payloads']};allow.add(str(hm.relative_to(W)))
 actual={str(p.relative_to(W)) for p in (RR/'handoff').rglob('*') if p.is_file()}
 assert actual==allow and len(actual)==46
 anchors=[('handoff/cloud-eighth-update-handoff-prompt.md',16227,'b61751391213d735fa93496ecbae371ed42064175ead7120d86ae6ef0d89741e'),('handoff/cloud-eighth-update-handoff-manifest.json',53340,'0f5e125014e95b7ee3e905fe4ccc81cc9796d34762c1748bf0f6875bd1895375'),('adjudication/root-final-cloud-handoff-acceptance.v1.json',57180,'d50f07cfab46109d88cce37f1fa9bb2dd82d8327972fbe3c6276b07fcd5217b9')]
 for rel,n,h in anchors:allow.add(exact(PREFIX+rel,dict(bytes=n,sha256=h)))
 bind='publication/root-actual-semantic-core-binding.v1.json';binding_raw=(RR/bind).read_bytes();binding=json.loads(binding_raw);allow.add(PREFIX+bind)
 changed={x.decode() for x in git('diff','--name-only','-z',HEAD,label='freeze-tracked').split(b'\0') if x}
 changed.update(x.decode() for x in git('ls-files','--others','--exclude-standard','-z',label='freeze-untracked').split(b'\0') if x)
 assert all(x.startswith(PREFIX) for x in changed)
 for path in changed:
  rel=path[len(PREFIX):]
  if rel.startswith('publication/checkpoint-35-') or rel.startswith('publication/checkpoint-36-'):allow.add(safe(path))
 allow.add(PREFIX+'publication/r8-final-semantic-core-readback-35.json')
 proof=(RR/'publication/r8-final-semantic-core-readback-35.json').read_bytes();assert len(proof)==27888640 and sha(proof)=='267b44094dc9e4f7e0d6443e2df7e333f4656cc37b76f7c7941e959322b21b20'
 cmap={x['original_path']:x for x in json.loads((PUB/'compressed-artifacts.json').read_bytes())['artifacts']};assert len(cmap)==116
 rows=[];excluded=[]
 for path in sorted(changed):
  rel=path[len(PREFIX):]
  if path in OLD:excluded.append(dict(path=path,reason='EXPLICIT_OLD_LIVE_UNQUALIFIED_PRESERVE_LOCAL'));continue
  if path not in allow:excluded.append(dict(path=path,reason='OUTSIDE_EXACT_COMPLETED_C36_ALLOWLIST_PRESERVE_LOCAL'));continue
  if rel in cmap:
   b=(W/path).read_bytes();entry=cmap[rel]
   if len(b)==entry['original_bytes'] and sha(b)==entry['original_sha256']:
    excluded.append(dict(path=path,reason='EXACT_PUBLISHED_GZIP_ORIGINAL_BYTES_AND_SHA_MATCH'));continue
  rows.append(metadata(path))
 guard('freeze-final');included={x['path'] for x in rows}
 for p in sorted(IO.rglob('*')):
  if p.is_file() and str(p.relative_to(W)) not in included:rows.append(metadata(str(p.relative_to(W))));included.add(str(p.relative_to(W)))
 log=IO/'freeze-hash-object-events.json';assert not log.exists();put(log,dict(events=hash_events,semantic_credit='NONE'));rows.append(metadata(str(log.relative_to(W))))
 data=dict(schema='gr8-checkpoint36-exact-frozen-candidates/v1',utc=utc(),baseline_HEAD=HEAD,branch=BRANCH,root_authorized_freeze=True,
  files=rows,count=len(rows),bytes=sum(x['bytes'] for x in rows),publication_binding=dict(actual_C35_core=binding,handoff_payload_manifest=dict(path='handoff/payload-manifest.json',bytes=len(raw),sha256=sha(raw)),root_acceptance='adjudication/root-final-cloud-handoff-acceptance.v1.json',handoff_files=46,handoff_payload_files=45,handoff_payload_bytes=5535925),
  explicit_old_live_excludes=sorted(OLD),excluded=excluded,candidate_envelope='publication/checkpoint-36-candidates.json separately added by exact SHA, no self recursion',
  post_freeze_root_writes='NOT_STAGED',new_contexts=0,new_votes=0,new_source_FULL_credit=0,semantic_credit='NONE added by transport',business='NOT_EXECUTED',UPDATE_NOT_STARTED=True)
 f=PUB/'checkpoint-36-candidates.json';put(f,data);raw=f.read_bytes()
 print(json.dumps(dict(status='C36_EXACT_CANDIDATES_FROZEN',count=len(rows),bytes=data['bytes'],candidate_bytes=len(raw),candidate_sha256=sha(raw),handoff46_exact=True,old_live_four_excluded=True,fresh_protected_preflight='PASS'),ensure_ascii=False),flush=True)
if __name__=='__main__':main()
