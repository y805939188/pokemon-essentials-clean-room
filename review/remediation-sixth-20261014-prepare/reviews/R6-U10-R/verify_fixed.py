"""Independent identity and preservation checks; no reference execution."""
import datetime, difflib, hashlib, json, pathlib, re, subprocess, sys

ROOT = pathlib.Path('/workspace/pokemon-essentials-clean-room')
OUT = ROOT / 'review/remediation-sixth-20261014-prepare/reviews/R6-U10-R'
BASE = 'review/remediation-sixth-20261014-prepare/'
CAND = 'd3554f9479fadcd1255cf8103b19e4aa88e1825b'
PREP = '469a268b92daed7b4d28d7fd0da75520cbb7228f'
MAIN = '8ea169fbd0f33f378b5d732fd6bea59e854e04a6'
REF = '8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
started = datetime.datetime.now(datetime.timezone.utc).isoformat()
attempts = []
def git(*args):
    p = subprocess.run(['git', *args], cwd=ROOT, capture_output=True)
    attempts.append(dict(argv=['git',*args], exit_code=p.returncode, stdout_bytes=len(p.stdout),
                         stdout_sha256=hashlib.sha256(p.stdout).hexdigest(), stderr=p.stderr.decode()))
    if p.returncode: raise RuntimeError(p.stderr.decode())
    return p.stdout
def ident(ref, path):
    data = git('show', ref+':'+path)
    row = git('ls-tree', ref, '--', path).decode().strip().split(None,3)
    return dict(ref=ref,path=path,mode=row[0],type=row[1],git_blob=row[2],bytes=len(data),
                sha256=hashlib.sha256(data).hexdigest(),physical_lines=len(data.splitlines()))
def check_id(ref,path,expected):
    actual=ident(ref,path)
    for k in ['bytes','sha256','git_blob']: assert actual[k]==expected[k], (path,k,actual[k],expected[k])
    assert actual['mode']=='100644' and actual['type']=='blob'
    return actual
prompt=git('show',PREP+':'+BASE+'prompts/R6-U10-R.md')
assert len(prompt)==232998 and hashlib.sha256(prompt).hexdigest()=='5fa1d5ad291e305f1c347f99a2fb634d6983bd6346567139428207f0a15c229d'
blocks=re.findall(r'```json\n(.*?)\n```',prompt.decode(),re.S)
contract_data=git('show',PREP+':'+BASE+'contracts/R6-U10.json')
contract=json.loads(contract_data)
assert json.loads(blocks[0])==contract
assert git('rev-parse',CAND+'^{tree}').decode().strip()=='f71699038cbd900eedaeb76f28f7fd1910ec9185'
assert git('rev-parse',REF+'^{tree}').decode().strip()=='7589c800b61ba13a13040ed0d686979b80a84fd0'
assert git('rev-parse',MAIN+':deliverables/final-specification-set').decode().strip()==git('rev-parse',CAND+':deliverables/final-specification-set').decode().strip()=='1046fbb657882e84b3dfc6d017943a9edf7782e5'
sources={}
def walk(value):
    if isinstance(value,dict):
        if 'payload_identity' in value:
            e=value['payload_identity']; p=e['path']; ref=e['commit']
            if ref==REF and p not in sources: sources[p]=check_id(ref,p,e)
        for v in value.values(): walk(v)
    elif isinstance(value,list):
        for v in value: walk(v)
walk(contract)
manifest=json.loads(git('show',CAND+':'+BASE+'candidates/R6-U10/evidence/candidate-path-manifest.json'))
mirrors=[]
replacements=[]
for r in manifest['changed_formal_mirrors']:
    before=check_id(MAIN,r['formal_target_for_integrator_only'],r['before'])
    after=check_id(CAND,r['candidate_path'],r['candidate'])
    a=git('show',MAIN+':'+r['formal_target_for_integrator_only']).decode().splitlines(keepends=True)
    b=git('show',CAND+':'+r['candidate_path']).decode().splitlines(keepends=True)
    removed=[]
    for tag,i,j,k,l in difflib.SequenceMatcher(a=a,b=b,autojunk=False).get_opcodes():
        if tag in ['replace','delete']: removed.extend(range(i+1,j+1))
    assert removed==r['removed_or_replaced_frozen_lines'],(r['candidate_path'],removed)
    replacements += [(r['formal_target_for_integrator_only'],n) for n in removed]
    mirrors.append(dict(before=before,candidate=after,removed_or_replaced_frozen_lines=removed))
assert len(mirrors)==5 and len(replacements)==8
catalog=next(r for r in manifest['changed_formal_mirrors'] if '/test-catalog/' in r['candidate_path'])
old=git('show',MAIN+':'+catalog['formal_target_for_integrator_only'])
new=git('show',CAND+':'+catalog['candidate_path'])
assert new.startswith(old) and len(old.splitlines())==914
vectors=re.findall(r'^\| (U10-(CP|SF|MK|RL)\d{2}) \|',new.decode(),re.M)
assert len(vectors)==32 and len(set(x[0] for x in vectors))==32
counts={prefix:sum(x[1]==prefix for x in vectors) for prefix in ['CP','SF','MK','RL']}
assert counts==dict(CP=9,SF=5,MK=9,RL=9)
changes=git('diff','--name-status',PREP,CAND).decode().splitlines()
assert len(changes)==25 and all(x.split('\t')[1].startswith(BASE+'candidates/R6-U10/') for x in changes)
evidence=json.loads(blocks[1]); evidence_rows=[]
for ev in contract['scope_contracts'][0]['bidirectional_evidence']['counter_evidence_ids']:
    e=evidence[ev]; p=BASE+'inputs/evidence/'+e['path']
    actual=check_id(PREP,p,e); actual['evidence_id']=ev
    evidence_rows.append(actual)
result=dict(kind='INDEPENDENT_TOOL_VALIDATION_NOT_SEMANTIC_PASS',candidate_commit=CAND,candidate_tree='f71699038cbd900eedaeb76f28f7fd1910ec9185',
    prompt=ident(PREP,BASE+'prompts/R6-U10-R.md'),contract=ident(PREP,BASE+'contracts/R6-U10.json'),
    separate_contract_full_json_matches_prompt=True,formal_tree_unchanged='1046fbb657882e84b3dfc6d017943a9edf7782e5',
    mirrors=mirrors,source_payloads=list(sources.values()),counterevidence_payloads=evidence_rows,
    changed_candidate_payloads=25,all_candidate_changes_inside_author_allowlist=True,old_catalog_lines=914,old_catalog_bytes=len(old),
    old_catalog_complete_byte_prefix_preserved=True,replaced_old_lines=8,vector_count=32,vector_family_counts=counts,
    vector_execution='NOT_EXECUTED',reference_execution_count=0,independent_behavior_model_execution_count=0,host_demo_execution_count=0,
    semantic_read_warning='Hash and preservation checks are not semantic reading; primary and peer reading recorded separately',
    started_utc=started,ended_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),cwd=str(ROOT),argv=sys.argv,
    runtime=sys.version,exit_code=0,stderr='',processes=attempts)
(OUT/'independent-tool-validation.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:result[k] for k in ['candidate_commit','candidate_tree','changed_candidate_payloads','old_catalog_lines','old_catalog_complete_byte_prefix_preserved','replaced_old_lines','vector_count','vector_family_counts','formal_tree_unchanged']},ensure_ascii=False,indent=2))
