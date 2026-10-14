"""Finite reviewer-owned registry/identity checks; executes no source or author code."""
from pathlib import Path
from collections import Counter
import hashlib
import json
import subprocess

OUT = Path(__file__).resolve().parent
PACKET = '229260cfd5177581bb88bafd84770ceb1c11b117'
REG = 'd35356005f79b9fdffc5a4202a0b39e9255a36fa'
ACTUAL = '86bbc99b28d93db4ed9d6897daf5f3725ccd1808'
PREFIX = 'review/remediation-sixth-20261014-prepare/'
INPUT = PREFIX+'integration/final-acceptance-audit-20261014/input.json'
checks = []

def git(*args):
    r = subprocess.run(['git', *args], capture_output=True)
    if r.returncode:
        raise RuntimeError((args, r.returncode, r.stderr.decode(errors='replace')))
    return r.stdout

def payload(commit, path):
    return git('show',f'{commit}:{path}')

def document(commit, path):
    return json.loads(payload(commit,path))

def identity(b):
    return dict(bytes=len(b),sha256=hashlib.sha256(b).hexdigest(),
                git_blob=hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest())

def pointer(x,p):
    for key in p.split('/')[1:]:
        key=key.replace('~1','/').replace('~0','~')
        x=x[int(key)] if isinstance(x,list) else x[key]
    return x

def check(name, condition, observed=None):
    checks.append(dict(name=name,passed=bool(condition),observed=observed))

def bind(commit,path,expected):
    b=payload(commit,path)
    got=identity(b)
    entry=git('ls-tree',commit,'--',path).decode().strip().split('\t')[0].split()
    check('identity:'+path,got=={k:expected[k] for k in got},got)
    check('tree_entry:'+path,entry==['100644','blob',got['git_blob']],entry)
    return b

def save(name,x):
    (OUT/name).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')

x=document(PACKET,INPUT)
readset=[dict(commit=REG,**f,observed=identity(bind(REG,f['path'],f))) for f in x['frozen_read_set']]
for c,t in [(REG,x['frozen_registration_workspace_tree']),
            (ACTUAL,x['actual_semantic_workspace_tree'])]:
    check('workspace_tree:'+c,git('rev-parse',c+'^{tree}').decode().strip()==t,t)
for c in [PACKET,REG,ACTUAL]:
    t=git('rev-parse',c+':deliverables/final-specification-set').decode().strip()
    check('immutable_formal_tree:'+c,t==x['frozen_formal_tree'],t)
formal_paths=git('ls-tree','-r','--name-only',ACTUAL,'--','deliverables/final-specification-set').decode().splitlines()
changed=git('diff','--name-only',x['fixed_main'],ACTUAL,'--','deliverables/final-specification-set').decode().splitlines()
check('formal_counts',len(formal_paths)==131 and len(changed)==53,dict(paths=len(formal_paths),changed=len(changed),unchanged=len(formal_paths)-len(changed)))

sync=document(REG,PREFIX+'integration/public-sync-20261014/sync-input.json')
ledger=document(REG,PREFIX+'ledger.json')
queue=document(REG,PREFIX+'reception-queue.json')
tasks=document(REG,PREFIX+'task-register.json')
dep=document(REG,x['dependency_status']['path'])
actual=document(ACTUAL,x['actual_input']['path'])
bind(ACTUAL,x['actual_input']['path'],x['actual_input'])
mapping=x['required_mapping']
check('raw_required_unique',len(mapping)==56 and len(Counter(r['id'] for r in mapping))==56)
check('severity_counts',Counter(r['severity'] for r in mapping)==Counter(P2=39,P3=17),dict(Counter(r['severity'] for r in mapping)))
check('group_counts',Counter(r['actual_primary_group'] for r in mapping)==Counter(A=11,B=9,C=19,D=9,E=8),dict(Counter(r['actual_primary_group'] for r in mapping)))
check('required_set_actual',set(r['id'] for r in mapping)==set(actual['required_ids']) and len(actual['required_ids'])==56)
report_docs={}
report_bindings=[]
for r in x['five_independent_actual_reports']:
    b=bind(r['report_commit'],r['report_path'],r['report_identity'])
    s=bind(r['report_commit'],r['structured_verdict_path'],r['structured_verdict_identity'])
    check('report_workspace:'+r['group'],git('rev-parse',r['report_commit']+'^{tree}').decode().strip()==r['report_workspace_tree'])
    directory=r['report_path'].rsplit('/',1)[0]
    check('report_directory:'+r['group'],git('rev-parse',r['report_commit']+':'+directory).decode().strip()==r['report_directory_tree'])
    check('report_text_binding:'+r['group'],ACTUAL.encode() in b and x['frozen_formal_tree'].encode() in b)
    report_docs[r['group']]=json.loads(s)
    report_bindings.append(dict(group=r['group'],commit=r['report_commit'],path=r['report_path'],identity=identity(b),structured_path=r['structured_verdict_path'],structured_identity=identity(s)))

public=[]
for f in x['public_sync_files']:
    before=payload(ACTUAL,f['path']);after=payload(REG,f['path'])
    check('public_old_prefix:'+f['path'],identity(before)==f['before_actual_history_identity'] and after[:len(before)]==before)
    lines=after.decode().splitlines()
    starts=[i for i,l in enumerate(lines) if l==f['current_layer_start_marker']]
    ends=[i for i,l in enumerate(lines) if l==f['current_layer_end_marker']]
    check('single_current_block:'+f['path'],len(starts)==len(ends)==1 and starts[0]<ends[0])
    raw=[]
    for i in range(starts[0],ends[0]+1):
        if lines[i].startswith('| '):
            cells=[c.strip() for c in lines[i].split('|')[1:-1]]
            if cells[0] in {r['id'] for r in mapping}:raw.append(dict(id=cells[0],physical_line=i+1,cells=cells))
    check('public_raw_unique:'+f['path'],len(raw)==56 and len(Counter(r['id'] for r in raw))==56)
    public.append(dict(path=f['path'],current_range=[starts[0]+1,ends[0]+1],old_prefix_bytes=len(before),old_prefix_exact=True,raw_rows=raw))

contracts={}
records=[]
by_batch={b['batch']:b for b in actual['batches']}
for r in mapping:
    id=r['id'];group=r['actual_primary_group'];item=pointer(sync,r['public_registry_item_pointer']);d=pointer(dep,r['dependency_item_pointer'])
    report=pointer(report_docs[group],r['report_per_id_pointer'])
    if r['contract_path'] not in contracts:
        contracts[r['contract_path']]=json.loads(bind(REG,r['contract_path'],r['contract_identity']))
    contract=pointer(contracts[r['contract_path']],r['contract_pointer'])
    lr=[v for v in ledger['required'] if v['id']==id]
    passed=(item['id']==d['id']==report['id']==contract['id']==id and len(lr)==1
            and item['primary_batch']==d['primary_batch']==r['primary_batch']
            and item['actual_group']==d['actual_group']==group
            and contract['identity_and_verdict']['classification']=='required'
            and contract['identity_and_verdict']['severity']==r['severity']
            and id in by_batch[r['primary_batch']]['required_ids']
            and item['severity']==r['severity']
            and item['actual_content_review']==d['primary_actual_review']==lr[0]['integrated_pass']
            and lr[0]['primary_batch']==r['primary_batch'] and lr[0]['severity']==r['severity']
            and not item['formal_acceptance'] and not item['closed'] and not lr[0]['formal_acceptance'] and not lr[0]['closed'])
    if group!='E':
        passed=passed and (report.get('batch') or report.get('primary_batch'))==r['primary_batch']
    verdict=report.get('verdict') or report.get('actual_verdict') or report.get('actual_content_verdict')
    passed=passed and 'PASS' in verdict and (report.get('actual_commit') or report_docs[group].get('actual_commit'))==ACTUAL
    rows=[]
    for p in public:
        pr=next(v for v in p['raw_rows'] if v['id']==id)
        passed=passed and item['rule_summary'] in pr['cells'][1 if p['path'].startswith('audit/') else 2]
        if p['path'].startswith('planning/'):
            passed=passed and pr['cells'][1]==r['primary_batch']+'／'+group
        rows.append(dict(path=p['path'],line=pr['physical_line']))
    check('56_point_binding:'+id,passed)
    records.append(dict(id=id,severity=r['severity'],primary_batch=r['primary_batch'],primary_actual_group=group,
                        report_per_id_pointer=r['report_per_id_pointer'],contract_pointer=r['contract_pointer'],
                        public_registry_item_pointer=r['public_registry_item_pointer'],dependency_item_pointer=r['dependency_item_pointer'],
                        current_public_rows=rows,identity_and_correspondence_check='PASS' if passed else 'FAIL',
                        original_dependencies=item['original_dependencies'],semantic_qualification='Registry/pointer/correspondence only; full rule qualification reviewed separately against the fixed root reports.'))

check('static_vs_acceptance_counts',sync['candidate_PASS']==sync['actual_content_PASS_count']==sync['actually_received']==56 and sync['formal_acceptance']==sync['CLOSED']==0 and sync['OPEN']==56)
check('dependency_counts',len(dep['edges'])==110 and Counter(e['status'] for e in dep['edges'])==Counter(SATISFIED_FOR_STATIC_CONTENT=108,PENDING_EXACT_FINAL_REGISTRY_AUDIT_THEN_FORMAL_ACCEPTANCE=1,PENDING_FORMAL_ACCEPTANCE_THEN_FINAL_CLOSED_REGISTRATION=1))
check('candidate_map_only',len(actual['batches'])==14 and len(actual['files'])==53 and sum(len(f['contributions']) for f in actual['files'])==76)
result=dict(schema='r6.final-audit.root-finite-identity-checks.v1',input_packet_commit=PACKET,registration_commit=REG,
 actual_commit=ACTUAL,formal_tree=x['frozen_formal_tree'],checks=checks,passed=sum(c['passed'] for c in checks),failed=sum(not c['passed'] for c in checks),
 report_bindings=report_bindings,frozen_readset=readset,public_blocks=public,per_id_records=records,
 execution=dict(reference=0,author_script=0,independent_behavior_model=0,host_Demo=0,real_save_load_playback=0),
 qualification='Independent finite document/identity checks; no global semantic source review; eligibility is adjudicated separately.',formal_acceptance=False,CLOSED=False)
save('registry-binding-checks.json',result)
print(json.dumps(dict(passed=result['passed'],failed=result['failed'],records=len(records),group_counts=dict(Counter(r['actual_primary_group'] for r in mapping)),severity_counts=dict(Counter(r['severity'] for r in mapping)),failed_checks=[c for c in checks if not c['passed']]),ensure_ascii=False))
