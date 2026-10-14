#!/usr/bin/env python3
"""Independent finite artifact and fixed-input verification; no reference execution."""
import datetime, difflib, hashlib, json, pathlib, re, subprocess, sys

OWN = pathlib.Path(__file__).resolve().parent
REPO = OWN.parents[3]
PRE = '469a268b92daed7b4d28d7fd0da75520cbb7228f'
MAIN = '8ea169fbd0f33f378b5d732fd6bea59e854e04a6'
C = '9f7825620508589453d750ca5a09c11f1dc14cf4'
P = 'f34eb57fbd2dba4184ac2b6ab1ed7ca26e41062a'
R = '8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
ROOT = 'review/remediation-sixth-20261014-prepare/'
CAND = ROOT+'candidates/R6-U08/'
started = datetime.datetime.now(datetime.timezone.utc).isoformat()
def git(*args, repo=REPO):
    return subprocess.check_output(['git','-C',str(repo),*args])
def identity(b):
    return dict(bytes=len(b), sha256=hashlib.sha256(b).hexdigest(),
                git_blob=hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest())
def payload(commit,path,repo=REPO):
    b=git('show',commit+':'+path,repo=repo)
    mode,typ,blob=git('ls-tree',commit,'--',path,repo=repo).decode().split('\t')[0].split()
    row=dict(commit=commit,path=path,mode=mode,git_type=typ,type='UTF-8 text',**identity(b))
    assert blob==row['git_blob'] and typ=='blob'
    return b,row
contract_b,contract_row=payload(PRE,ROOT+'contracts/R6-U08.json')
contract=json.loads(contract_b)
prompt_b,prompt_row=payload(PRE,ROOT+'prompts/R6-U08-R.md')
assert identity(prompt_b)==dict(bytes=260087,sha256='336dbd3b82899a3a836a12f654bf23ceb0713de7ef8e4f1fc95d1f61046dd9ba',git_blob='0b93448066cfe0647cc1be0c57d9bb8e4c6d0e24')
prompt=prompt_b.decode();a=prompt.index('```json\n')+8;b=prompt.index('\n```',a)
assert json.loads(prompt[a:b])==contract
assert git('rev-parse',P+'^{tree}').decode().strip()=='1a67b846355d2716a53ff3f088bdb0f6b94a4626'
assert git('rev-parse',P+':'+CAND[:-1]).decode().strip()=='280e5aa4e8e1ed309616a051acf0c5f71a1eef15'
assert git('diff','--name-only',C,P).decode().splitlines()==[CAND+'evidence/publication-receipt.json']
all_changed=git('diff','--name-only',PRE,P).decode().splitlines()
assert all(x.startswith(CAND) for x in all_changed)
assert len(all_changed)==15
assert not git('diff',MAIN,P,'--','deliverables/final-specification-set')
assert git('rev-parse',P+':deliverables/final-specification-set').decode().strip()=='1046fbb657882e84b3dfc6d017943a9edf7782e5'
candidate_rows=[]
for p in git('ls-tree','-r','--name-only',P,'--',CAND).decode().splitlines():
    data,row=payload(P,p);assert data==(REPO/p).read_bytes();candidate_rows.append(row)
assert len(candidate_rows)==15
manifest=json.loads(git('show',P+':'+CAND+'evidence/core-manifest.json'))
for row in manifest['files']:
    match=next(x for x in candidate_rows if x['path']==row['path'])
    assert all(row[k]==match[k] for k in ['bytes','sha256','git_blob','mode'])
events=[json.loads(l) for l in (OWN/'read-events.jsonl').read_text().splitlines()]
def read_covers(commit,path,n):
    covered=set()
    for e in events:
        if e['commit']==commit and e['path']==path:
            covered.update(range(e['read_range'][0],e['read_range'][1]+1))
    return set(range(1,n+1))<=covered
pair_rows=[]
for path,expected in zip(contract['candidate_formal_paths'],[{33,59,60,108,123,285},{11,15,20,33}]):
    old,old_row=payload(MAIN,path);new,new_row=payload(P,CAND+'mirror/'+path)
    assert old==git('show','13fddb0a217b36974c75657aa68da0caf104ee48:'+path)
    before=old.decode().splitlines(keepends=True);after=new.decode().splitlines(keepends=True)
    assert read_covers(P,CAND+'mirror/'+path,len(after))
    mapping=[];removed=[]
    for op,a,b,c,d in difflib.SequenceMatcher(None,before,after,autojunk=False).get_opcodes():
        mapping.append(dict(operation=op,baseline=[a+1,b] if b>a else [],candidate=[c+1,d] if d>c else []))
        if op!='equal':removed.extend(range(a+1,b+1))
    assert set(removed)==expected
    for line in removed:
        assert any(e['commit']==MAIN and e['path']==path and e['read_range'][0]<=line<=e['read_range'][1] for e in events)
    pair_rows.append(dict(baseline=old_row,candidate=new_row,full_semantic_read='All candidate lines displayed; baseline equal spans independently byte-mapped to those same readings; every removed original line separately displayed.',mapping=mapping,removed_baseline_lines=removed,retained_baseline_lines=len(before)-len(removed),selected_fifth_candidate_full_bytes_equal=True))
source_rows=[]
for p in contract['read_only_reference_paths']:
    data,row=payload(R,p,'/tmp/r6-u08-review-reference')
    assert read_covers(R,p,len(data.decode().splitlines()))
    source_rows.append(row)
assert git('rev-parse',R+'^{tree}',repo='/tmp/r6-u08-review-reference').decode().strip()=='7589c800b61ba13a13040ed0d686979b80a84fd0'
def visit(v):
    if isinstance(v,dict):
        if 'payload_identity' in v:
            e=v['payload_identity'];repo='/tmp/r6-u08-review-reference' if e['commit']==R else REPO
            data,row=payload(e['commit'],e['path'],repo)
            assert all(row[k]==e[k] for k in ['bytes','sha256','git_blob','mode'])
        for x in v.values():visit(x)
    elif isinstance(v,list):
        for x in v:visit(x)
visit(contract)
packet=json.loads(git('show',P+':'+CAND+'evidence/id-evidence.json'))
cat=git('show',P+':'+CAND+'mirror/'+contract['candidate_formal_paths'][1]).decode()
vector_rows=[l for l in cat.splitlines() if re.match(r'^\| DG-U08-\d+／DEBUG-\d{3} \|',l)]
assert len(vector_rows)==28
vector_ids=re.findall(r'^\| (DG-U08-\d+)／DEBUG-\d{3} \|',cat,re.M)
assert vector_ids==['DG-U08-%02d'%n for n in range(1,29)]
assert sum(len(r['acceptance_and_regression']['vectors']) for r in packet['records'])==28
for r in packet['records']:
    assert r['premises_and_counterexample']['new_author_vectors']==r['acceptance_and_regression']['vectors']
    for v in r['acceptance_and_regression']['vectors']:
        line=next(l for l in vector_rows if l.startswith('| '+v['id']+'／'))
        assert v['input_and_observation'] in line and v['source_static_expected'] in line
history_path='review/global-independent-review/fifth-2026-10-13-9366d9d-c7d3/regression-legacy-scope.json'
history_b,history_row=payload('c0ff33024aea424c68d29f9778fe7c8e807d21e8',history_path)
history=json.loads(history_b);author_history=json.loads(git('show',P+':'+CAND+'evidence/historical-regression.json'))
history_checks=[]
for r in author_history['qualification_fields_read_complete']:
    i=int(r['pointer'].split('/')[-1]);original=history['contributions'][i]
    assert all(r[k]==original[k] for k in r['read_fields'])
    history_checks.append(dict(pointer=r['pointer'],record_key=r['record_key'],fields=r['read_fields'],result='FIXED_ORIGINAL_FIELD_EQUAL',semantic_scope='The exact fields were independently retrieved, match the complete fields read from the author evidence, and were assessed against newly read current/source spans; no old PASS transfer.'))
result=dict(schema='r6-u08-r.fixed-verification.v1',level='TOOL_VALIDATION',semantic_execution=False,
            started_utc=started,ended_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),runtime=sys.version,
            argv=sys.argv,cwd=str(REPO),prompt=prompt_row,contract=contract_row,
            candidate_publication=P,candidate_tree='280e5aa4e8e1ed309616a051acf0c5f71a1eef15',candidate_payload_count=15,
            candidate_payloads=candidate_rows,author_change_paths=all_changed,pair_readings=pair_rows,reference_payloads=source_rows,
            contract_payload_identities_verified=True,reference_tree_verified=True,baseline_formal_tree_unchanged=True,
            vector_row_count=28,vector_payload_text_matches=True,historical_control_identity=history_row,exact_historical_fields=history_checks,
            author_checker_executed_by_reviewer=False,source_loaded_or_executed=False,result='PASS_FINITE_IDENTITY_AND_SCOPE_CHECKS')
(OWN/'fixed-verification.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:result[k] for k in ['result','candidate_payload_count','vector_row_count','baseline_formal_tree_unchanged','contract_payload_identities_verified']},ensure_ascii=False))
