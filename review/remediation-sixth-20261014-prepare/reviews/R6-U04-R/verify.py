"""Independent payload, patch, preservation and evidence-level verification."""
import collections, datetime, difflib, hashlib, json, pathlib, subprocess, sys
ROOT = pathlib.Path('/workspace/pokemon-essentials-clean-room')
OWN = pathlib.Path(__file__).resolve().parent
PREP = 'review/remediation-sixth-20261014-prepare/'
CAND = PREP+'candidates/R6-U04/'
BASE = '469a268b92daed7b4d28d7fd0da75520cbb7228f'
MAIN = '8ea169fbd0f33f378b5d732fd6bea59e854e04a6'
AUTHOR = '22cc12e141ac2c2dd23c1dea218bf0873c5f86ca'
SEMANTIC = '1fa0f30525ae87ff4f3fb22f4d8448b4447b694b'
REF = '8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
RDB = OWN/'.scratch/reference.git'
def git(repo,*args): return subprocess.check_output(['git','-C',str(repo),*args])
def blob(c,p,repo=ROOT): return git(repo,'show',c+':'+p)
def ident(b): return dict(bytes=len(b),sha256=hashlib.sha256(b).hexdigest(),git_blob=hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest())
checks=[]
def ck(name,test,detail=None):
    checks.append(dict(check=name,result='PASS' if test else 'FAIL',detail=detail))
    assert test,name
contract=json.loads(blob(BASE,PREP+'contracts/R6-U04.json'))
prompt=blob(BASE,PREP+'prompts/R6-U04-R.md')
ck('review-prompt-identity',ident(prompt)==dict(bytes=221397,sha256='4de6aa24117b630b22f0de7546d5674e7ef498d1f9578f53957085f3df687a00',git_blob='2bef897e43ce86c1124d61b00da966ac88816ecf'))
ck('embedded-contract-equals-standalone',json.loads(prompt.decode().split('```json\n')[1].split('\n```')[0])==contract)
ck('fixed-author-tree',git(ROOT,'rev-parse',AUTHOR+'^{tree}').decode().strip()=='2e2d4f590983f4e327b2de37cf69014229af7f12')
ck('fixed-reference-tree',git(RDB,'rev-parse',REF+'^{tree}').decode().strip()=='7589c800b61ba13a13040ed0d686979b80a84fd0')
ck('no-author-formal-or-ledger-change',all(p.startswith(CAND) for p in git(ROOT,'diff','--name-only',BASE,AUTHOR).decode().splitlines()))
ck('formal-tree-entire-baseline-preserved',git(ROOT,'rev-parse',AUTHOR+':deliverables/final-specification-set')==git(ROOT,'rev-parse',MAIN+':deliverables/final-specification-set'))
ck('semantic-and-final-mirror-equal',git(ROOT,'rev-parse',AUTHOR+':'+CAND+'mirror')==git(ROOT,'rev-parse',SEMANTIC+':'+CAND+'mirror'))
manifest=json.loads(blob(AUTHOR,CAND+'evidence/package-manifest.json'))
ck('author-manifest-count',manifest['payload_count']==len(manifest['payloads'])==21)
for row in manifest['payloads']:
    b=blob(AUTHOR,row['path']);entry=git(ROOT,'ls-tree',AUTHOR,'--',row['path']).decode().split()
    ck('author-manifest:'+row['path'],all(ident(b)[k]==row[k] for k in ident(b)) and entry[:2]==[row['mode'],row['type']])
binding=dict(repository='y805939188/pokemon-essentials-clean-room',prepare_commit=BASE,semantic_commit=SEMANTIC,published_commit=AUTHOR,
             published_tree='2e2d4f590983f4e327b2de37cf69014229af7f12',mirror_tree=git(ROOT,'rev-parse',AUTHOR+':'+CAND+'mirror').decode().strip(),
             prompt=ident(prompt),contract=ident(blob(BASE,PREP+'contracts/R6-U04.json')),files=[])
patch_dir=OWN/'.scratch/patch-reconstruction'
patch_dir.mkdir(parents=True,exist_ok=True)
for p in contract['candidate_formal_paths']:
    old,new=blob(MAIN,p),blob(AUTHOR,CAND+'mirror/'+p)
    ck('prepared-mirror-exact-baseline:'+p,blob(BASE,CAND+'mirror/'+p)==old)
    ck('candidate-working-copy-still-frozen:'+p,(ROOT/(CAND+'mirror/'+p)).read_bytes()==new)
    target=patch_dir/p;target.parent.mkdir(parents=True,exist_ok=True);target.write_bytes(old)
    binding['files'].append(dict(formal_path=p,candidate_path=CAND+'mirror/'+p,mode='100644',type='blob',baseline=ident(old),candidate=ident(new)))
patch_path=ROOT/(CAND+'evidence/formal-only.patch')
attempts=[]
for args in [['git','apply','--check',str(patch_path)],['git','apply',str(patch_path)]]:
    start=datetime.datetime.now(datetime.timezone.utc).isoformat();r=subprocess.run(args,cwd=patch_dir,capture_output=True)
    attempts.append(dict(argv=args,cwd=str(patch_dir),utc_start=start,utc_end=datetime.datetime.now(datetime.timezone.utc).isoformat(),exit=r.returncode,stdout=r.stdout.decode(),stderr=r.stderr.decode()))
    ck('patch:'+str(len(attempts)),r.returncode==0)
for row in binding['files']: ck('exact-patch-reconstruction:'+row['formal_path'],(patch_dir/row['formal_path']).read_bytes()==blob(AUTHOR,row['candidate_path']))
reproduced=json.loads((OWN/'processes/reproduced-author-337.stdout').read_text())
ck('reproduced-337-static-checks',reproduced['check_count']==len(reproduced['checks'])==337 and all(r['result']=='PASS' for r in reproduced['checks']))
archived=[]
for n in ['static-validation.stdout.json','static-validation-run02.stdout.json']:
    x=json.loads(blob(AUTHOR,CAND+'evidence/'+n));archived.append(x)
    ck('author-result:'+n,x['check_count']==337 and all(r['result']=='PASS' for r in x['checks']))
ck('both-author-run-check-identities-reproduced',all([(r['check'],r['result']) for r in x['checks']]==[(r['check'],r['result']) for r in reproduced['checks']] for x in archived))
vectors=json.loads(blob(AUTHOR,CAND+'evidence/designed-vectors.json'))
ck('eleven-designed-not-executed',len(vectors['vectors'])==11 and all(r['level']=='DERIVED_VECTOR' and not r['reference_execution'] and not r['independent_model_execution'] for r in vectors['vectors']))
recovery=json.loads(prompt.decode().split('```json\n')[2].split('\n```')[0])
for eid in contract['scope_contracts'][0]['bidirectional_evidence']['counter_evidence_ids']:
    row=recovery[eid];b=blob(BASE,PREP+'inputs/evidence/'+row['path'])
    ck('fixed-counterevidence:'+eid,all(ident(b)[k]==row[k] for k in ident(b)))
history=[('9366d9d17aaeac3b4414236468affa650fb3dd27','review/remediation-third-20261012-prepare/required23-acceptance.json'),
 ('13fddb0a217b36974c75657aa68da0caf104ee48','review/remediation-fifth-20261013-prepare/registration/successors/20261014-final-closure-candidate/closure-candidate.json'),
 ('12df95a8e81061a606d50d3f0a0528793b2e6b2c','review/remediation-fifth-20261013-prepare/registration/successors/20261014-final-activation/activation-receipt.json'),
 ('22fba7786b0090a1955ce6211315b0036cddfbcd','review/remediation-fifth-20261013-prepare/contracts/R5-U05/task-packet.json')]
for c,p in history: ck('historical-fixed-object-preserved:'+p,blob(c,p)==blob(AUTHOR,p))
owned_prefix=str(OWN.relative_to(ROOT))+'/'
ck('reviewer-write-scope',all(p.startswith(owned_prefix) for p in git(ROOT,'diff','--name-only',AUTHOR).decode().splitlines()+git(ROOT,'ls-files','--others','--exclude-standard').decode().splitlines()))
binding['author_report']=dict(path=CAND+'evidence/author-report.md',**ident(blob(AUTHOR,CAND+'evidence/author-report.md')))
binding['formal_only_patch']=dict(path=CAND+'evidence/formal-only.patch',**ident(blob(AUTHOR,CAND+'evidence/formal-only.patch')))
(OWN/'candidate-binding.json').write_text(json.dumps(binding,ensure_ascii=False,indent=2)+'\n')
audit=dict(level='TOOL_VALIDATION_ONLY',checks=checks,check_count=len(checks),patch_attempts=attempts,reproduced_author_check_count=337,
           author_check_groups=dict(collections.Counter(x['check'].split(':')[0] for x in reproduced['checks'])),
           reference_execution=0,independent_behavior_model_execution=0,host_demo_execution=0)
(OWN/'static-verification.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(status='PASS_TOOL_VALIDATION',check_count=len(checks),reproduced_author_checks=337,designed_vectors=11,executed_behavior_vectors=0,patch_files=3),ensure_ascii=False))
