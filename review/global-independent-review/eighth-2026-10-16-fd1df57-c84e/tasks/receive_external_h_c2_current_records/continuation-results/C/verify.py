"""Validate evidence integrity/scope only; never run reviewed source or behavior."""
from pathlib import Path
import json,hashlib,gzip,subprocess,datetime
T=Path(__file__).resolve().parent;ROOT=Path('/workspace/pokemon-essentials-clean-room');BASE='1b46a33526f086241c765b700155c5406a86f65e'
def enc(v):return json.dumps(v,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode()
def ident(b):return {'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'git_blob':hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()}
def git(*a):return subprocess.check_output(['git',*a])
branch=git('branch','--show-current').decode().strip();assert branch=='codex/r8-c2-reception-c-20261016'
d=json.loads((T/'frozen-denominator.json').read_text());assert len(d['records'])==11
raw=gzip.decompress((T/'scoped-values.json.gz').read_bytes());bi=json.loads((T/'scoped-values.identity.json').read_text());assert ident(raw)==bi['decoded'];assert ident((T/'scoped-values.json.gz').read_bytes())==bi['encoded'];bundle=json.loads(raw)
for r,c,p in zip(d['records'],bundle['canonical'],bundle['proposals_and_counters']):
 assert r['id']==c['value']['id']==p['value']['id'];assert ident(enc(c['value']))==r['canonical_identity'];assert ident(enc(p['value']))==r['proposal_identity'];assert len(r['seven_groups'])==len(r['seven_original_field_binding_groups'])==7
 assert r['all_fields']=={k:ident(enc(v)) for k,v in c['value'].items()}
state=json.loads((T/'display-ledger.json').read_text())
for name,r in state['prepared'].items():
 if r['ack']:assert set(r['shown'])==set(range(len(r['parts']))) and r['note']
 else:assert name in ['qualifications','b8dependencies'] and r['superseded_by']
 for p in r['parts']:assert (T/p).is_file()
# Every exact value reference in the lossless views resolves to a full selected subtree.
hashes=set()
def scan(v):
 hashes.add(ident(enc(v))['sha256'])
 if isinstance(v,dict):
  for x in v.values():scan(x)
 elif isinstance(v,list):
  for x in v:scan(x)
scan(bundle)
for b in state.get('typed_bindings',[]):scan(b['value'])
refs=[]
for label,r in state['prepared'].items():
 if not r['ack']:continue
 txt=''.join((T/p).read_text() for p in r['parts'])
 try:v=json.loads(txt)
 except json.JSONDecodeError:continue
 def check(v):
  if isinstance(v,dict):
   for k,x in v.items():
    if k in ['$exact_already_read_sha256','$exact_same_display_sha256']:assert x in hashes,(label,x);refs.append(x)
    else:check(x)
  elif isinstance(v,list):
   for x in v:check(x)
 check(v)
sources=json.loads((T/'source-readings.json').read_text());cache={}
for r in sources:
 key=(r['repository'],r['commit'],r['path'])
 if key not in cache:
  repo='/workspace/pokemon-essentials' if key[0]=='R' else str(ROOT);cache[key]=git('-C',repo,'show',key[1]+':'+key[2])
 b=cache[key];assert ident(b)==r['file_identity'];assert r['status']=='ACTUAL_READ';lines=b.decode().splitlines(keepends=True)
 for ranges,i in zip(r['ranges'],r['range_identities']):a,z=ranges;assert ident(''.join(lines[a-1:z]).encode())==i
for r in json.loads((T/'reception-ledger.json').read_text())['records']:
 assert r['status']=='READY_FOR_PARENT_RECEPTION';assert not r['unread_current_assigned_values']
allowed=str(T.relative_to(ROOT))+'/'
changed=git('diff','--name-only',BASE).decode().splitlines();untracked=git('ls-files','--others','--exclude-standard').decode().splitlines();assert all(p.startswith(allowed) for p in changed+untracked)
# Frozen formal subtree must be byte-identical to B8.
assert git('rev-parse','HEAD:deliverables/final-specification-set').decode().strip()=='f292698cdd4a8e725525a9be6dc34b75faaf151e'
out={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'status':'PASS_EVIDENCE_AND_WRITE_SCOPE_ONLY','branch':branch,'base':BASE,'canonical':11,'seven_groups':77,'complete_display_acks':sum(r['ack'] for r in state['prepared'].values()),'superseded_zero_credit_displays':2,'exact_subtree_references_resolved':len(refs),'fixed_source_formal_displays':len(sources),'unique_fixed_files':len(cache),'decoded_bundle':ident(raw),'changes_confined_to':allowed,'behavior_validation':'NOT_EXECUTED; this verifier does not grant semantic PASS'}
(T/'validation.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n');print(json.dumps(out,ensure_ascii=False))
