"""Finite report integrity check; this is not a reference behavior test."""
import collections
import datetime
import hashlib
import json
import pathlib
import subprocess

ROOT=pathlib.Path(__file__).resolve().parents[1]
SPEC=pathlib.Path('/workspace/pokemon-essentials-clean-room')
REF=pathlib.Path('/workspace/pokemon-essentials')
B8='fd1df570cad987dc3852a3b958f03916e317f7fe'
R='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
BRANCH='codex/r8-external-pbs-creature-backups-20261016'
TASK=ROOT.relative_to(SPEC).as_posix()
checks=[]

def read(name):
    return json.loads((ROOT/name).read_text())

def check(name,condition):
    checks.append(dict(name=name,result='PASS' if condition else 'FAIL'))
    if not condition:
        raise ValueError(name)

def git(repo,*args):
    return subprocess.check_output(['git','-C',str(repo),*args])

start=datetime.datetime.now(datetime.timezone.utc).isoformat()
try:
    parsed={p.name:json.loads(p.read_text()) for p in ROOT.glob('*.json') if p.name!='validation.json'}
    check('all current top-level JSON parses',bool(parsed))
    ids=read('identities.json')['payloads']
    for key,ident in ids.items():
        b=git(ident['repo'],'show',ident['commit']+':'+ident['path'])
        # hash-object without -w hashes bytes without modifying the object store.
        blob=subprocess.run(['git','hash-object','--stdin'],input=b,capture_output=True,check=True).stdout.decode().strip()
        check(key+' actual identity',len(b)==ident['bytes'] and hashlib.sha256(b).hexdigest()==ident['sha256'] and blob==ident['blob'])
        if key.startswith('I'):
            check(key+' pinned local copy exact',(ROOT/ident['copy']).read_bytes()==b)
        else:
            check(key+' workspace source unchanged',(pathlib.Path(ident['repo'])/ident['path']).read_bytes()==b)
    ledger=read('reading-ledger.json')
    allsections=[s for f in ledger['primary'] for s in f['all_sections']]
    check('all 6712 primary coordinates unique',len(allsections)==6712 and len({s['id'] for s in allsections})==6712)
    check('reading status denominator',collections.Counter(s['status'] for s in allsections)=={'READ_NOT_ACCEPTED':3675,'PARTIAL_READ_NOT_ACCEPTED':1,'AVAILABLE_UNREAD':3036})
    check('primary full/partial/unread files',collections.Counter(f['file_status'] for f in ledger['primary'])=={'FULL_READ':12,'PARTIAL_READ':1,'AVAILABLE_UNREAD':3})
    for f in ledger['primary']:
        ident=ids[f['identity_id']]
        b=(REF/f['path']).read_bytes()
        off=[0]
        for line in b.splitlines(keepends=True): off.append(off[-1]+len(line))
        last=0
        for s in f['all_sections']:
            a,z=s['lines']
            check(s['id']+' ordered section/offset/fields',a>last and z<=ident['lines'] and s['byte_offsets_half_open']==[off[a-1],off[z]] and all(a<n<=z for n,k in s['fields_line_key']))
            last=z
        covered={n for a,z in f['read_ranges'] for n in range(a,z+1)}
        unread={n for a,z in f['unread_ranges'] for n in range(a,z+1)}
        check(f['identity_id']+' disjoint full read/unread line partition',not covered&unread and covered|unread==set(range(1,ident['lines']+1)))
    check('coverage counters match ledger',read('coverage.json')['counts']==ledger['counts'])
    check('no acceptance or behavior execution credit',ledger['counts']['accepted_primary_sections']==0 and read('execution.json')['behavior_executions']==0)
    fwd=read('forward-mapping.json')
    facts={f['id']:f for f in fwd['fact_notes']}
    check('all primary units retain open mapping disposition',{u[0] for u in fwd['units']}=={s['id'] for s in allsections} and all(u[2]=='COMPLETE_FACT_CONSUMER_SPEC_MAPPING_PENDING' for u in fwd['units']))
    refs=[]
    for fact in facts.values(): refs+=fact['source']+fact['spec']
    for row in read('reverse-mapping.json')['selected_assertion_notes']:
        check(row['id']+' known fact and unaccepted',row['source_fact_id'] in facts and row['acceptance']=='PENDING_MAIN_REVIEWER')
        refs.append(row['spec']); refs+=row['source']
    for ref in refs:
        key=ref['identity_id']; a,z=ref['lines']
        check('mapping reference bounded '+key,key in ids and 1<=a<=z<=ids[key]['lines'])
    proposal=read('proposals.json')
    check('no fake independent decision or NO_REQUIRED_UPDATE',not proposal['no_required_update'] and proposal['records'][0]['independent_disproof']['state']=='PENDING_MAIN_REVIEWER')
    check('task openly incomplete',read('progress.json')['semantic_status']=='REVIEW_INCOMPLETE' and read('gaps.json')['status']=='REVIEW_INCOMPLETE')
    check('correct dedicated branch',git(SPEC,'branch','--show-current').decode().strip()==BRANCH)
    check('R commit and clean worktree',git(REF,'rev-parse','HEAD').decode().strip()==R and not git(REF,'status','--porcelain=v1','--untracked-files=all'))
    changed=git(SPEC,'diff','--name-only',B8).decode().splitlines()
    untracked=git(SPEC,'ls-files','--others','--exclude-standard').decode().splitlines()
    staged=git(SPEC,'diff','--cached','--name-only').decode().splitlines()
    check('all workspace tracked/untracked/staged changes confined to own directory',all(p.startswith(TASK+'/') for p in changed+untracked+staged))
    check('formal tree unchanged',git(SPEC,'rev-parse','HEAD:deliverables/final-specification-set').decode().strip()=='f292698cdd4a8e725525a9be6dc34b75faaf151e')
    status='PASS_TOOL_INTEGRITY_ONLY'
except Exception as exc:
    status='FAIL_TOOL_INTEGRITY'
    checks.append(dict(name='exception',result='FAIL',detail=repr(exc)))
result=dict(schema='r8-task-validation/v1',start_utc=start,end_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
            status=status,check_count=len(checks),checks=checks,
            evidence_level='TOOL_VALIDATION_ONLY',semantic_read_credit_added=0,behavior_executions_added=0,
            limitations='Coordinates/identities/counter consistency only; not completeness, correctness of every semantic note, or independent acceptance.')
# Do not serialize thousands of identical passing coordinate assertions individually.
result['successful_check_name_sha256']=hashlib.sha256('\n'.join(c['name'] for c in checks if c['result']=='PASS').encode()).hexdigest()
result['checks']=[c for c in checks if c['result']!='PASS']
(ROOT/'validation.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(result,ensure_ascii=False))
raise SystemExit(0 if status.startswith('PASS') else 1)
