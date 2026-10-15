import json,pathlib,urllib.request,hashlib,subprocess,datetime,os,concurrent.futures,difflib
R=pathlib.Path('/workspace/r7-ir-R7-U07-wave3'); O=R/'result/review/remediation-seventh-20261015-prepare/integrated-reviews/R7-U07/r1/evidence'; O.mkdir(exist_ok=True)
MI='e54f54a2cb32e546eabd46aaf53ed45b30a8af89';FI='b98fa82f8a08b5630ac568cbe8c34f607f623cfb'; B='e646432c644dec04d306842cc5a559a29c718fbc'
def ident(d):return dict(bytes=len(d),sha256=hashlib.sha256(d).hexdigest(),git_blob=hashlib.sha1(f'blob {len(d)}\0'.encode()+d).hexdigest())
def save(p,v):p.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
def get(commit,path,local):
 t=R/'supplemental'/local;t.parent.mkdir(parents=True,exist_ok=True);url=f'https://raw.githubusercontent.com/y805939188/pokemon-essentials-clean-room/{commit}/{urllib.parse.quote(path)}'
 if t.exists():data=t.read_bytes();status='REUSED'
 else:data=urllib.request.urlopen(url,timeout=40).read();t.write_bytes(data);status='HTTP_COMPLETE'
 return dict(commit=commit,path=path,local_path=str(t),url=url,status=status,**ident(data))
def read(p):return p.read_bytes()
J=json.load(open(R/'actual-input/integration/applied-clauses.json')); F=json.load(open(R/'supplemental/FI/integrated-input.json'))
requests={}
for f in J['cumulative_files']:
 for h in f['hunks']:requests[(h['candidate_commit'],h['candidate_path'])]='candidates/'+h['batch_id']+'/'+f['path']
for b in J['new_source_bindings']+J['prior_source_bindings']:
 for n in ['report.md','per-id.json']:
  path=f"candidates/{b['id']}/evidence/reviewer/{'r2' if b['id'] in ['R7-U01','R7-U07','R7-U10'] else 'r1'}/{n}";requests[(b['candidate_review_commit'],path)]='approvals/'+b['id']+'/'+n
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
 futs=[pool.submit(get,c,p,l) for (c,p),l in requests.items()];rows=[];errors=[]
 for fut in futs:
  try:rows.append(fut.result())
  except Exception as e:errors.append(str(e))
save(O/'supplemental-shared-fetch.json',dict(utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),pid=os.getpid(),files=rows,errors=errors));assert not errors,errors
checks=[];maps={(r['commit'],r['path']):pathlib.Path(r['local_path']) for r in rows}
def locate(kind,path):
 for root in [R/'actual-input',R/'supplemental']:
  p=root/kind/path
  if p.exists():return p
 raise FileNotFoundError((kind,path))
for f in J['cumulative_files']:
 p=f['path'];base=read(locate('baseline',p)) if f['baseline_identity']['bytes'] else b'';actual=read(locate('actual',p));bl=base.decode().splitlines(keepends=True)
 assert ident(base)==f['baseline_identity']
 # Rebuild by B anchor order plus explicit wave rank/batch order; same-EOF order is tested independently.
 hunks=sorted(f['hunks'],key=lambda h:(h['base_line_indices_half_open'][0],h.get('integration_wave_rank',0),h['batch_order']))
 out=[];cursor=0;hs=[]
 for h in hunks:
  a,z=h['base_line_indices_half_open'];ca,cz=h['candidate_line_indices_half_open'];cand=read(maps[(h['candidate_commit'],h['candidate_path'])]).decode().splitlines(keepends=True)
  removed=''.join(bl[a:z]).encode();added=''.join(cand[ca:cz]).encode()
  assert a>=cursor,(p,a,cursor)
  assert ident(removed)==h['removed_identity'];assert ident(added)==h['added_identity']
  if 'removed_text' in h:assert removed.decode()==h['removed_text']
  if 'added_text' in h:assert added.decode()==h['added_text']
  out.extend(bl[cursor:a]);out.extend(cand[ca:cz]);cursor=z
  hs.append(dict(batch=h['batch_id'],required_ids=h['required_ids'],B_lines=[a,z],candidate_lines=[ca,cz],candidate_commit=h['candidate_commit'],candidate_path=h['candidate_path'],removed=ident(removed),added=ident(added),actual_occurrences=actual.count(added) if added else None,match=True))
 out.extend(bl[cursor:]);assembled=''.join(out).encode();assert ident(assembled)==f['assembled_candidate_clauses_identity'],p
 admin=[a for a in J['root_administrative_adjustments'] if a['path']==p]
 if admin:assembled+=admin[0]['added_text'].encode()
 if p.endswith('current-navigation-errata.json'):
  cj=json.loads(assembled);aj=json.loads(actual)
  save(O/'prior-navigation-administrative-delta.json',dict(path=p,candidate_status=cj['status'],actual_status=aj['status'],candidate_reception=cj['reception'],actual_reception=aj['reception'],qualification='Prior wave administrative status delta, not new wave3 behavior; kept separate from exact candidate hunk preservation.'))
  del cj['status'];del aj['status'];del cj['reception'];del aj['reception'];assert cj==aj
 else:assert assembled==actual,p
 checks.append(dict(path=p,baseline=ident(base),actual=ident(actual),hunks=hs,reconstructed_exactly=(assembled==actual),prior_navigation_administrative_delta=p.endswith('current-navigation-errata.json'),administrative_append=bool(admin)))
# Validate every FI identity against actual MI object metadata and full bytes; unchanged files read from verified B Git objects.
ids=F['all_formal_file_identities'];print('FI entry sample',ids[0])
formal=[]
for row in ids:
 p=row['path'];d=None
 try:d=read(locate('actual',p))
 except FileNotFoundError:d=subprocess.check_output(['git','-C',str(R/'result'),'show',B+':'+p])
 expected=row.get('actual_identity',row.get('identity',row));real=ident(d)
 for k,v in real.items():
  key=k if k in expected else ('git_blob_content_id' if k=='git_blob' else k)
  if key in expected:assert v==expected[key],(p,k,v,expected[key])
 formal.append(dict(path=p,**real))
# Original bound raw members and every in-file origin reference.
norm=json.load(open(R/'original/evidence/tasks/R7-C13/inputs/tasks/R7-P02/normalized-record-candidates.json'))['records'][14]
rawroot=R/'original/evidence/tasks/R7-C13/inputs/tasks/R7-P02/evidence/inputs';bindings=[]
def walk(x):
 if isinstance(x,dict):
  if all(k in x for k in ['input_sha256','raw_member_byte_offsets','raw_member_sha256']):
   fp=rawroot/(x['input_sha256']+'.raw')
   if fp.exists():
    a,z=x['raw_member_byte_offsets'];d=fp.read_bytes()[a:z];assert len(d)==x['raw_member_bytes'];assert hashlib.sha256(d).hexdigest()==x['raw_member_sha256'];bindings.append(dict(input=x['input_sha256'],pointer=x.get('json_pointer'),offsets=[a,z],match=True))
  for v in x.values():walk(v)
 elif isinstance(x,list):
  for v in x:walk(v)
walk(norm)
prior=[]
for p in (R/'actual-input/prior-accepted/previous-actual').rglob('*'):
 if p.is_file():rel=str(p.relative_to(R/'actual-input/prior-accepted/previous-actual'));a=locate('actual',rel);assert read(a)==read(p);prior.append(dict(path=rel,identity=ident(read(a)),exact=True))
save(O/'cumulative-byte-audit.json',dict(utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),pid=os.getpid(),files=checks,FI_formal_files=formal,raw_bindings=bindings,prior8=prior,qualification='TOOL_VALIDATION only; no content or behavior PASS inferred'))
print(json.dumps(dict(cumulative_files=len(checks),candidate_hunks=sum(len(x['hunks']) for x in checks),formal_files=len(formal),bindings=len(bindings),prior8=len(prior))))
