import json,hashlib,datetime,subprocess,difflib,re
from pathlib import Path

OUT=Path(__file__).resolve().parent
PREP=OUT.parents[1].relative_to(Path.cwd())
AUTHOR=PREP/'candidates/R6-U06'
BASE='469a268b92daed7b4d28d7fd0da75520cbb7228f'
HEAD='4d92cda068cd7ce027630ab24f05873a50389c93'
MAIN='8ea169fbd0f33f378b5d732fd6bea59e854e04a6'
R='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
def git(*args):return subprocess.check_output(['git',*args])
def identity(b):return dict(bytes=len(b),sha256=hashlib.sha256(b).hexdigest(),git_blob=hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest())
checks=[]
def check(name,condition,details=None):
    checks.append(dict(name=name,result='PASS' if condition else 'FAIL',details=details))
    assert condition,name
prompt=(PREP/'prompts/R6-U06-R.md').read_bytes()
contract_bytes=(PREP/'contracts/R6-U06.json').read_bytes();contract=json.loads(contract_bytes)
check('Exact frozen reviewer prompt',identity(prompt)==dict(bytes=224129,sha256='b67e8aab419ca64d07c4cd60638aecd154e341ec2e79bf25a31b93a4bb7fd4bf',git_blob='416519b53a66af56a68593d0bce30f2c360ba9b3'))
check('Complete contract literally in prompt',contract_bytes in prompt)
check('Candidate exact frozen tree',git('rev-parse',HEAD+'^{tree}').decode().strip()=='58157870fd6e5e277a4afd29816253b980c58cf5')
check('Reference exact fixed tree',git('rev-parse',R+'^{tree}').decode().strip()=='7589c800b61ba13a13040ed0d686979b80a84fd0')
unique={}
def collect(o):
    if isinstance(o,dict):
        if 'payload_identity' in o:
            v=o['payload_identity'];unique[(v['commit'],v['path'])]=v
        for x in o.values():collect(x)
    elif isinstance(o,list):
        for x in o:collect(x)
collect(contract)
input_rows=[]
for (ref,path),expected in unique.items():
    data=git('show',ref+':'+path);entry=git('ls-tree',ref,'--',path).decode().strip();mode,typ,tail=entry.split(' ',2)
    actual=identity(data);ok=all(actual[k]==expected[k] for k in actual) and mode==expected['mode'] and typ=='blob' and tail.split('\t')[0]==expected['git_blob']
    input_rows.append(dict(commit=ref,path=path,mode=mode,type=typ,**actual,exact=ok))
check('All unique contractual source/formal identities',all(x['exact'] for x in input_rows),len(input_rows))
diffs=[];files=[]
for path in contract['candidate_formal_paths']:
    mirror=str(AUTHOR/'mirror'/path);old=git('show',MAIN+':'+path);new=git('show',HEAD+':'+mirror)
    check('Baseline mirror full bytes '+path,git('show',BASE+':'+mirror)==old)
    check('Formal and author mirror unchanged by reviewer '+path,Path(path).read_bytes()==old and Path(mirror).read_bytes()==new)
    a=old.decode().splitlines();b=new.decode().splitlines();ops=[]
    for tag,i,j,k,l in difflib.SequenceMatcher(None,a,b,autojunk=False).get_opcodes():
        item=dict(operation=tag,baseline_lines=[i+1,j],candidate_lines=[k+1,l])
        if tag!='equal':item.update(old_text=a[i:j],new_text=b[k:l])
        ops.append(item)
    diffs.append(dict(formal_path=path,mirror_path=mirror,baseline=identity(old),candidate=identity(new),opcodes=ops,
                      semantic_read_method='Complete candidate emitted/read; all equal baseline spans identical; every differing old/new line additionally emitted/read. Full baseline has no unaccounted text.'))
    files.append(dict(formal_path=path,candidate_path=mirror,mode='100644',type='blob',**identity(new)))
    print(path)
    for op in ops:
        if op['operation']!='equal':
            print(json.dumps({k:v for k,v in op.items() if k!='new_text'},ensure_ascii=False))
tc=diffs[2];oldtc=git('show',MAIN+':'+tc['formal_path']).decode().splitlines();newtc=git('show',HEAD+':'+tc['mirror_path']).decode().splitlines()
def rows(lines):
    return [(i+1,x.split('|')[1].strip(),x) for i,x in enumerate(lines) if x.startswith('| ') and re.match(r'^(DG-|CE-|WE-|AN-|CV-|GN-|DM-|B17-|B19-|B20-|U07-|U01-)',x.split('|')[1].strip())]
oldrows=rows(oldtc);newrows=rows(newtc);new_ids={f'CE-TYPES-{i:02d}' for i in range(1,7)};changed={'CE-M15','CE-M19','WE-M20','CV-M11','CV-M24'}
check('All old test IDs/order/multiplicity',[x[1] for x in oldrows]==[x[1] for x in newrows if x[1] not in new_ids],len(oldrows))
check('Every unedited old test row byte-exact',[x[2] for x in oldrows if x[1] not in changed]==[x[2] for x in newrows if x[1] not in changed|new_ids])
check('Six and only six new type rows',len(newrows)==len(oldrows)+6 and all(sum(x[1]==n for x in newrows)==1 for n in new_ids))
history_rows=[x for x in oldrows if x[1].startswith(('B17-','B19-','B20-','U07-'))]
check('Exact B17/B19/B20/R5-U07 preservation',all(x[2] in newtc for x in history_rows),len(history_rows))
check('Author changes restricted to candidate directory',all(x.startswith(str(AUTHOR)+'/') for x in git('diff','--name-only',BASE,HEAD).decode().splitlines()))
check('Actual entire formal tree fixed',git('rev-parse',HEAD+':deliverables/final-specification-set').decode().strip()==git('rev-parse',MAIN+':deliverables/final-specification-set').decode().strip())
evidence_map=json.loads(prompt.decode().split('```json\n')[-1].split('\n```')[0]);needed=set()
for s in contract['scope_contracts']:needed.update(s['bidirectional_evidence']['counter_evidence_ids'])
counter_rows=[]
for key in sorted(needed):
    expected=evidence_map[key];p=PREP/'inputs/evidence'/expected['path'];actual=identity(p.read_bytes())
    counter_rows.append(dict(id=key,path=str(p),**actual,exact=all(actual[k]==expected[k] for k in actual)))
check('All fourteen listed counterevidence identities',len(counter_rows)==14 and all(x['exact'] for x in counter_rows))
author=json.loads((AUTHOR/'evidence/author-findings.json').read_text())
check('Exactly four author records',[x['id'] for x in author['records']]==contract['required_ids'])
vectors=[x for r in author['records'] for x in r['premises_and_counterexample']['author_vectors']]
check('Twenty-two unique manual vectors remain unexecuted',len(vectors)==22 and len(set(x['id'] for x in vectors))==22 and all(x['execution']=='NOT_EXECUTED' and x['evidence_level']=='DERIVED_VECTOR' for x in vectors))
v=json.loads((AUTHOR/'evidence/validation.json').read_text())
check('Thirty recorded author checks are document/tool only',len(v['checks'])==30 and all(x['result']=='PASS' for x in v['checks']) and v['reference_execution']==0 and v['derived_vectors_executed']==0)
h=json.loads((AUTHOR/'evidence/historical-regression.json').read_text());history_inputs=[];history_objects={}
for expected in h['r4_B5_input']+[h['r5_frozen_scope'],h['selected_closing_input'],h['unique_activation']]:
    data=git('show',expected['commit']+':'+expected['path']);actual=identity(data)
    history_inputs.append(dict(**expected,exact=all(actual[k]==expected[k] for k in actual)))
    if expected['path'].endswith('.json'):history_objects[expected['path']]=json.loads(data)
check('Exact fixed history objects restored',all(x['exact'] for x in history_inputs))
original=history_objects[h['r5_frozen_scope']['path']]['findings'];semantic=h['r5_complete_relevant_semantic_fields_read']
check('Full relevant historical semantic fields match frozen original',all(all(r.get(k)==v for k,v in s.items()) for s,r in zip(semantic,original)))
closure=history_objects[h['selected_closing_input']['path']]
def locate(o,key):
    if isinstance(o,dict):
        if o.get('id')==key:yield o
        for x in o.values():yield from locate(x,key)
    elif isinstance(o,list):
        for x in o:yield from locate(x,key)
check('Seven selected closure records exact',all(s in list(locate(closure,s['id'])) for s in h['selected_records']))
activation=history_objects[h['unique_activation']['path']]
check('Activation scope and counts exact',all(activation.get(k)==v for k,v in h['activation_scope'].items()))
check('Reviewer current write set exact',all(x[3:].startswith(str(OUT.relative_to(Path.cwd()))+'/') for x in git('status','--porcelain','--untracked-files=all').decode().splitlines()))
(OUT/'baseline-comparison.json').write_text(json.dumps(diffs,ensure_ascii=False,indent=2)+'\n')
result=dict(utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),evidence_level='TOOL_VALIDATION',result='PASS',checks=checks,
            candidate_commit=HEAD,candidate_tree=git('rev-parse',HEAD+'^{tree}').decode().strip(),candidate_files=files,
            contractual_inputs=input_rows,counterevidence_inputs=counter_rows,historical_inputs=history_inputs,
            source_execution=0,derived_vector_execution=0,host_demo_execution=0,semantic_decision='Separately assessed by direct reviewer; checks do not decide behavior.')
(OUT/'verification.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n');print(json.dumps(dict(result='PASS',check_count=len(checks),old_test_rows=len(oldrows),preserved_history_rows=len(history_rows)),ensure_ascii=False))
