"""Independent byte/scope/member audit; never imports or executes author/reference files."""
import json,hashlib,subprocess,pathlib,gzip,datetime,os
HERE=pathlib.Path(__file__).resolve().parents[1]
REPO=pathlib.Path('/workspace/pokemon-essentials-clean-room')
BOOT=pathlib.Path('/workspace/r7-review-bootstrap/R7-U03-r1')
CTX=pathlib.Path('/workspace/r7-context/R7-U03-reviewer')
CAN=pathlib.Path('/workspace/r7-review-input/R7-U03-r1-11bff8e7912a98de09691ad7d7b7a2d3194e2757')
B='e646432c644dec04d306842cc5a559a29c718fbc';C='11bff8e7912a98de09691ad7d7b7a2d3194e2757';F='aa369555b0e8b6c8b077f964b54ed63d3b924f26';D='95c260d8f3fb4a171675dde877137fcd4c2f1c8d';P='4580645dfbfec4a3c7ccbad56ae293cc619b0d25'
def git(*a): return subprocess.check_output(['git',*a],cwd=REPO)
def ident(d):return dict(bytes=len(d),sha256=hashlib.sha256(d).hexdigest(),git_blob=hashlib.sha1(b'blob '+str(len(d)).encode()+b'\0'+d).hexdigest())
def check(d,r):
 a=ident(d)
 for k in ['bytes','sha256','git_blob']:
  key='git_blob_content_id' if k=='git_blob' and 'git_blob_content_id' in r else k
  if key in r:assert a[k]==r[key],(k,a[k],r[key])
 return a
freeze=json.loads((BOOT/'candidate-input.json').read_bytes())
for n in ['candidate-input.json','candidate-restore/R7-U03.json','mirror-diffs.patch','remote-readback.json']:
 assert (BOOT/n).read_bytes()==git('show',F+':review/remediation-seventh-20261015-prepare/candidate-freezes/R7-U03/'+n)
assert git('rev-parse',F+'^{tree}').decode().strip()=='08bd0f362c74ef7645b5bbd70b557489c122ae29'
assert git('rev-parse',C+'^{tree}').decode().strip()==freeze['candidate_tree']
assert freeze['fixed_B']==B
assert subprocess.run(['git','merge-base','--is-ancestor',B,C],cwd=REPO).returncode==0
rows=freeze['candidate_and_author_evidence_file_identities']
changes=git('diff','--name-status',B,C).decode().splitlines()
assert changes==[r['status']+'\t'+r['path'] for r in freeze['complete_diff_against_B']]
assert len(changes)==84 and all(x.startswith('A\tcandidates/R7-U03/') for x in changes)
files=[];mirrors=[]
for r in rows:
 d=(CAN/'candidate'/r['path']).read_bytes(); a=check(d,r)
 assert d==git('show',C+':'+r['path'])
 mode,kind,blob=git('ls-tree',C,'--',r['path']).decode().split('\t')[0].split()
 assert mode=='100644' and kind=='blob' and blob==a['git_blob']
 files.append(dict(path=r['path'],**a,git_mode=mode))
 if r['role']=='candidate_mirror':
  base=git('show',B+':'+r['formal_target']);check(base,r['base_B_identity_or_explicit_new_file'])
  mirrors.append(dict(path=r['path'],base=ident(base),candidate=a))
assert sum(r['bytes'] for r in files)==774948 and len(mirrors)==5
original_plan=json.load(open('/workspace/r7-bootstrap/R7-U03-reviewer/recovery/batches/R7-U03.json'))
original=[]
for r in original_plan['artifacts']+original_plan['evidence']+original_plan['fixed_read_inputs']:
 d=(CTX/r['local_path']).read_bytes(); a=check(d,r)
 if r['repository']=='y805939188/pokemon-essentials-clean-room' and r in original_plan['fixed_read_inputs']:assert d==git('show',r['commit']+':'+r['path'])
 original.append(dict(path=r['local_path'],**a))
contract=json.load(open(CTX/'dispatch/delegation/contracts/R7-U03.json'))
normalized=json.load(open(CTX/'evidence/tasks/R7-C13/inputs/tasks/R7-P02/normalized-record-candidates.json'))
bindings={r['binding_id']:r for r in json.load(open(CTX/'evidence/tasks/R7-C13/raw-binding-manifest.json'))}
seen={};supplements={}
SUP=pathlib.Path('/workspace/r7-review-bootstrap/R7-U03-r1/supplemental');SUP.mkdir(exist_ok=True)
def pointer(x,p):
 for k in p.split('/')[1:]:
  k=k.replace('~1','/').replace('~0','~');x=x[int(k)] if isinstance(x,list) else x[k]
 return x
def walk(x):
 if isinstance(x,dict):
  if all(k in x for k in ['binding_id','json_pointer','raw_member_byte_offsets','raw_member_sha256']):
   key=x['binding_id']+x['json_pointer']
   if key not in seen:
    r=bindings[x['binding_id']];p=CTX/'evidence/tasks/R7-C13'/r['c13_snapshot']
    if not p.exists():
     sha=r['sha256'];p=SUP/(sha+'.raw');t='review/global-independent-review/seventh-2026-10-14-e646432-7a91/publication-transport/core/objects/'+sha[:2]+'/'+sha+'.gz'
     encoded=git('show',P+':'+t);d=gzip.decompress(encoded)
     check(d,dict(bytes=r['bytes'],sha256=sha,git_blob=r['content_git_blob']))
     if p.exists():assert p.read_bytes()==d
     else:p.write_bytes(d)
     supplements[sha]=dict(path=r['report_relative_path'],binding_id=r['binding_id'],transport_commit=P,transport_path=t,encoded_identity=ident(encoded),**ident(d))
    d=p.read_bytes();assert ident(d)['sha256']==x['input_sha256']
    s,e=x['raw_member_byte_offsets'];f=d[s:e]
    assert len(f)==x['raw_member_bytes'] and hashlib.sha256(f).hexdigest()==x['raw_member_sha256']
    value=pointer(json.loads(d),x['json_pointer']);assert json.loads(f)==value
    canonical=json.dumps(value,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode()
    assert hashlib.sha256(canonical).hexdigest()==x['canonical_sha256']
    seen[key]=dict(binding_id=x['binding_id'],json_pointer=x['json_pointer'],input_sha256=x['input_sha256'],raw_member_sha256=x['raw_member_sha256'],canonical_sha256=x['canonical_sha256'],offsets=[s,e],matched=True)
  for v in x.values():walk(v)
 elif isinstance(x,list):
  for v in x:walk(v)
walk(contract)
for i in [6,7]:walk(normalized['records'][i])
manifest=json.load(open(CAN/'candidate/candidates/R7-U03/evidence/author/artifact-manifest.json'))
assert manifest['base_commit']==B
# Check every identity declaration wherever this author's manifest nests file rows.
filemap={r['path']:r for r in files};decl=[]
def declarations(x):
 if isinstance(x,dict):
  p=x.get('path')
  if p in filemap and 'bytes' in x and 'sha256' in x:
   check((CAN/'candidate'/p).read_bytes(),x);decl.append(p)
  for v in x.values():declarations(v)
 elif isinstance(x,list):
  for v in x:declarations(v)
declarations(manifest)
assert not manifest['conditional_wp06_adopted']
# Precise local skill availability, no fabricated application.
skills=dict(workspace_agents_entries=sorted(p.name for p in pathlib.Path('/workspace/.agents').iterdir()),fixed_dispatch_agents=git('ls-tree','-r','--name-only',D,'.agents').decode(),fixed_B_agents=git('ls-tree','-r','--name-only',B,'.agents').decode(),project_agents_exists=(REPO/'.agents/skills').exists())
# Additional immutable read dependencies, always outside candidate inputs.
extras=[]
for path in ['deliverables/final-specification-set/engine-overworld/wp13-move-route-matrix.md','review/global-independent-review/third-2026-10-12-86b4d7e-manual-a731/M03/spec-coverage.tsv']:
 d=git('show',B+':'+path);dest=SUP/path;dest.parent.mkdir(parents=True,exist_ok=True)
 if dest.exists():assert dest.read_bytes()==d
 else:dest.write_bytes(d)
 extras.append(dict(commit=B,path=path,**ident(d)))
sha='96ced6f8253d991b19b72617b4cd74c29343ef4af1b9e6067cf9787568ea4473'
t='review/global-independent-review/seventh-2026-10-14-e646432-7a91/publication-transport/core/objects/96/'+sha+'.gz'
d=gzip.decompress(git('show',P+':'+t));assert hashlib.sha256(d).hexdigest()==sha
(SUP/'proposal-successor-deltas-C04-C06.json').write_bytes(d)
extras.append(dict(commit=P,path=t,decoded_identity=ident(d)))
result=dict(schema='r7-u03-r1.independent-frozen-byte-audit.v1',utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),reviewer_thread=os.getenv('CODEX_THREAD_ID'),dispatch_commit=D,freeze_commit=F,candidate_commit=C,candidate_tree=freeze['candidate_tree'],fixed_B=B,fixed_B_tree=git('rev-parse',B+'^{tree}').decode().strip(),original_files=original,candidate_files=files,mirrors=mirrors,member_bindings=list(seen.values()),targeted_supplements=list(supplements.values()),additional_fixed_dependencies=extras,author_manifest_declared_identity_checks=len(decl),skills=skills,qualification='TOOL_VALIDATION only; content judgment separately documented. No author/reference/native program executed.')
(HERE/'byte-audit.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(status='VERIFIED_BYTES_SCOPE_AND_JSON_BINDINGS',original_files=len(original),original_bytes=sum(r['bytes'] for r in original),candidate_files=len(files),candidate_bytes=sum(r['bytes'] for r in files),mirror_files=len(mirrors),raw_members=len(seen),targeted_supplements=len(supplements),manifest_declarations=len(decl),skills=skills)))
