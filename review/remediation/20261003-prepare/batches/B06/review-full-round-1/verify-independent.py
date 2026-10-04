#!/usr/bin/env python3
"""Independent Git/document identity checks only; never evaluates reference behavior."""
import collections
import difflib
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

sys.dont_write_bytecode = True
OUT = Path(__file__).resolve().parent
ROOT = OUT.parents[5]
REF = Path('/tmp/R-B06-reference')
C = '4076a3fbbf6fe355b73f3fe2229d1f981fe735d2'
E = 'ee7461e90ad5e0943e39c56c22a080f761f4e1c0'
B = 'df65e346d85213742a2538588818a10f50b819e5'
HIST = '5059760ea678e3c21ce01a87a13317b5b6cc2e1d'
OLD = 'b1b09be809822ffa8ab79684589d104ec783095a'
ACCEPT = '1fd612d47dcda164de61ab2d25a1cb5e0fbde085'
ACTUAL = 'e24f2ac6f43642ea0e68bd9aa21fb2c313d6ebdf'
REVIEW = 'dea9d118d7ed3b7ddb57b1c4e7bd40db8dd06497'
REFERENCE = '8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
AUTHOR = 'review/remediation/20261003-prepare/batches/B06/author-stage2/'
HANDSHAKE = 'review/remediation/20261003-prepare/batches/B03/acceptance-stage-1/downstream-handshake.json'
F = 'deliverables/final-specification-set/'
FORMAL = [F+'creature-rpg/wp24-player-trainers-partners.md', F+'creature-rpg/wp25-party-and-storage.md',
          F+'creature-rpg/wp27-bag-and-item-storage.md', F+'test-catalog/creature-rpg-wp18-20-24-25-26.md',
          F+'test-catalog/creature-rpg-wp27-28-29-30-33.md', 'specs/creature-rpg/wp24-player-trainers-partners.md',
          'specs/creature-rpg/wp25-party-and-storage.md', 'specs/creature-rpg/wp27-bag-and-item-storage.md']
DELTA = [FORMAL[0], FORMAL[5], FORMAL[3]]
IDS = ['GIR-FD82-'+x for x in ['A032','A033','A034','A035','A036','A037','A038','A059','C103','C120']]
CACHE = {}
CHECKS = []

def git(*args, cwd=ROOT):
    return subprocess.check_output(['git',*args],cwd=cwd)

def check(label, value):
    CHECKS.append({'check':label,'passed':bool(value)})
    if not value:
        raise AssertionError(label)

def sha(data):
    return hashlib.sha256(data).hexdigest()

def blob(commit,path):
    key=(commit,path)
    if key not in CACHE:
        CACHE[key]=git('show',commit+':'+path)
    return CACHE[key]

def load(commit,path):
    return json.loads(blob(commit,path))

def dump(name,value):
    (OUT/name).write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n')

def identity(commit,path):
    data=blob(commit,path)
    return {'commit':commit,'path':path,'git_blob':git('rev-parse',commit+':'+path).decode().strip(),
            'sha256':sha(data),'bytes':len(data)}

def verify_identity(item):
    actual=identity(item['commit'],item['path'])
    check('identity '+item['commit']+':'+item['path'],all(actual[k]==item[k] for k in ['git_blob','sha256','bytes']))

def identity_records(obj):
    if isinstance(obj,dict):
        if all(k in obj for k in ['commit','path','git_blob','sha256','bytes']):
            yield obj
        for value in obj.values():
            yield from identity_records(value)
    elif isinstance(obj,list):
        for value in obj:
            yield from identity_records(value)

def rows(data):
    result={}
    for number,line in enumerate(data.splitlines(keepends=True),1):
        m=re.match(rb'^\| ([A-Z]+-\d+) \|',line)
        if m:
            key=m[1].decode()
            check('unique document row '+key,key not in result)
            result[key]=(number,line)
    return result

def section(data,prefix):
    lines=data.splitlines(keepends=True)
    i=next(n for n,l in enumerate(lines) if l.startswith(prefix.encode()))
    level=len(lines[i].split(b' ')[0])
    j=next((n for n in range(i+1,len(lines)) if re.match(rb'^#{1,'+str(level).encode()+rb'} ',lines[n])),len(lines))
    return b''.join(lines[i:j])

def normalize(obj):
    return json.dumps(obj,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode()

check('review branch',git('branch','--show-current').decode().strip()=='remediation/20261003-prepare/review-B06-full-1')
check('review evidence ancestor',subprocess.run(['git','merge-base','--is-ancestor',E,'HEAD'],cwd=ROOT,capture_output=True).returncode==0)
for commit,tree,parents in [(C,'cd171b364f01b300aed5694c7d49af5308b8a330',[B]),
                          (E,'deb7ced5a49bdbbb61b0cf09b8b224737aa0fd4b',[C]),
                          (B,'974dc9062cd991700c933ef27f1ad27775f3fcb8',[HIST,ACCEPT]),
                          (ACCEPT,'f31e24bc54c3641d74497a8cc32015ca4cfb9a9a',[REVIEW]),
                          (REVIEW,'4e4659d12aff5a7150194df64b2bc0717d954993',[ACTUAL]),
                          (ACTUAL,'d773aa6c96be4ca878350bd0a3ce6098ca71971b',None)]:
    check('tree '+commit,git('rev-parse',commit+'^{tree}').decode().strip()==tree)
    if parents is not None:
        check('parents '+commit,git('show','-s','--format=%P',commit).decode().split()==parents)
check('evidence successor only manifest',git('diff','--name-only',C,E).decode().splitlines()==[AUTHOR+'candidate-manifest.json'])
h=load(ACCEPT,HANDSHAKE)
am=load(ACCEPT,'review/remediation/20261003-prepare/batches/B03/acceptance-stage-1/acceptance-manifest.json')
check('B03 accepted actual binding',h['accepted_B03_actual_commit']==ACTUAL and h['accepted_B03_integration_report']==REVIEW)
check('B03 acceptance has scoped verdict','REGISTERED_PASS_SCOPED_AT_EXACT_REVIEWED_SHA' in json.dumps(am))
check('ten exact original IDs',h['complete_original_ten_ids']==IDS)
check('contract formal scope',h['inherited_eight_total_formal_scope']==FORMAL)
check('new formal delta',set(git('diff','--name-only',B,C,'--','deliverables','specs').decode().splitlines())==set(DELTA))
changed=git('diff','--name-only',B,C).decode().splitlines()
check('no other author candidate paths',all(p in DELTA or p.startswith(AUTHOR) for p in changed))
check('candidate whitespace',subprocess.run(['git','diff','--check',B,C],cwd=ROOT,capture_output=True).returncode==0)
check('contract serial ordering',h['B04_B06_order']=='SERIAL_B06_FIRST_B04_WAITING_NO_WRITE_DISPATCH' and not h['parallel_safety_established'])
check('fixed AGENTS',blob(C,'AGENTS.md')==blob(ACCEPT,'AGENTS.md')==(ROOT/'AGENTS.md').read_bytes())

identity_results=[]
for label,obj in [('accepted_handshake',h),('author_freeze',load(E,AUTHOR+'input-freeze.json')),
                  ('author_manifest',load(E,AUTHOR+'candidate-manifest.json'))]:
    items=list(identity_records(obj))
    for item in items:
        verify_identity(item)
    identity_results.append({'set':label,'declared_identity_records_verified':len(items)})
freeze=load(E,AUTHOR+'input-freeze.json')
check('author guards equal accepted contract',freeze['all15_preserved_clause_guards']==h['existing_seven_exact_clause_guards']
      and freeze['all25_preserved_static_rows']==h['existing_twentyfive_static_row_guards'])
for item in h['B06_local_eight_formal_bytes']:
    check('restored local bytes '+item['path'],blob(B,item['path'])==blob(OLD,item['path']))
for item in h['accepted_B03_thirteen_formal_inputs']:
    check('accepted B03 preserved '+item['path'],blob(B,item['path'])==blob(ACTUAL,item['path'])==blob(C,item['path'])==blob(E,item['path']))
for item in h['additional_read_only_context']:
    check('context preserved '+item['path'],blob(C,item['path'])==blob(item['commit'],item['path']))
hist=[]
for directory in h['B06_historical_evidence_file_identities']:
    present=0
    for item in directory['files']:
        verify_identity(item)
        p=ROOT/item['path']
        if p.exists():
            check('historical current bytes '+item['path'],p.read_bytes()==blob(item['commit'],item['path'])==blob(C,item['path']))
            present+=1
    hist.append({'commit':directory['commit'],'directory':directory['directory'],'fixed_files':len(directory['files']),'present_and_unchanged':present})
check('32 historical author files',sum(x['present_and_unchanged'] for x in hist)==32)
for item in h['five_local_whole_file_guards']:
    check('five whole file guard '+item['path'],blob(C,item['path'])==blob(item['commit'],item['path']))
for item in h['protected_upstream_version_successor']:
    g=item['accepted_successor']
    check('protected successor '+g['path'],blob(C,g['path'])==blob(g['commit'],g['path']))
clauses=[]
for g in h['existing_seven_exact_clause_guards']:
    data=blob(C,g['path']);literal=g['literal_text'].encode();old=blob(OLD,g['path'])
    s,e=g['lines_at_frozen_candidate']
    check('clause original range '+g['path']+':'+str(s),b''.join(old.splitlines(keepends=True)[s-1:e])==literal)
    check('clause exact '+g['path']+':'+str(s),sha(literal)==g['sha256'] and len(literal)==g['bytes'] and data.count(literal)==1)
    clauses.append({'path':g['path'],'old_range':[s,e],'candidate_line':data[:data.index(literal)].count(b'\n')+1,'sha256':g['sha256']})
for path in sorted(set(g['path'] for g in h['existing_seven_exact_clause_guards'])):
    offsets=[blob(C,path).index(g['literal_text'].encode()) for g in h['existing_seven_exact_clause_guards'] if g['path']==path]
    check('clause order '+path,offsets==sorted(offsets))
catalogrows={path:rows(blob(C,path)) for path in FORMAL[3:5]}
oldrows=[]
for g in h['existing_twentyfive_static_row_guards']:
    number,line=catalogrows[g['path']][g['test_id']]
    check('old static row '+g['test_id'],sha(line)==g['sha256'] and rows(blob(OLD,g['path']))[g['test_id']][1]==line)
    oldrows.append(dict(g,candidate_line=number))
protected=[]
for g in h['protected_sections_successor']:
    if g['successor_rule']=='PRESERVE_EXACT_BYTES':
        q=g['historical_frozen_guard']
        check('protected section '+q['path']+q['heading'],sha(section(blob(C,q['path']),q['heading']))==q['sha256'])
        protected.append(q)
# Independent allowed anchors from recovered Git, not author's edit ledger.
edits=[]
for path in DELTA[:2]:
    a=blob(B,path).splitlines(keepends=True);b=blob(C,path).splitlines(keepends=True)
    limits=({98,195},{160,238}) if path==FORMAL[0] else ({95,184},{153})
    for kind,i,j,m,n in difflib.SequenceMatcher(a=a,b=b,autojunk=False).get_opcodes():
        if kind=='equal':continue
        check('WP24 allowed anchor '+path+':'+str(i), (kind=='replace' and j==i+1 and i+1 in limits[0]) or (kind=='insert' and i in limits[1]))
        edits.append({'path':path,'kind':kind,'parent_lines':[i+1,j],'candidate_lines':[m+1,n],
                      'before_sha256':sha(b''.join(a[i:j])),'after_sha256':sha(b''.join(b[m:n]))})
    for heading in ['### 5.1','### 5.2','### 5.3','### 6.1']:
        check('WP24 unchanged section '+path+heading,section(blob(B,path),heading)==section(blob(C,path),heading))
    check('original-final audio section equal '+path,section(blob(C,FORMAL[0]),'### 5.4').rstrip(b'\n-')==section(blob(C,FORMAL[5]),'### 5.4').rstrip(b'\n-'))
check('seven WP24 edit hunks',len(edits)==7)
oldcatalog=blob(B,FORMAL[3]);newcatalog=blob(C,FORMAL[3]);prior=rows(oldcatalog);current=catalogrows[FORMAL[3]]
added={f'PT-{n:02d}' for n in range(35,70)}
check('exact35 additions',set(current)-set(prior)==added and set(prior)<=set(current))
check('every previous catalog row preserved',all(prior[k][1]==current[k][1] for k in prior))
reconstructed=newcatalog
for key in sorted(added):reconstructed=reconstructed.replace(current[key][1],b'')
reconstructed=reconstructed.replace('（PT-01～PT-69）'.encode(),'（PT-01～PT-34）'.encode())
check('whole previous catalog reconstructs',reconstructed==oldcatalog)
check('old PT navigation retained',section(blob(B,FORMAL[0]),'## 10.').splitlines()[2] in blob(C,FORMAL[0]).splitlines())
controls=load('93e10babe0b9c9ef8b3f5277754541b447beeeb4','review/global-independent-review/2026-10-03-fd82a639/findings.json')
controls={x['id']:x for x in controls}
accepts=load('41fffb540c6483f5296ea0d33b789b75180d27ed','review/remediation-20261003-prepare/finding-acceptance.json')
author_inputs=load(E,AUTHOR+'finding-inputs.json')['objects']
check('ten complete inputs',len(author_inputs)==10 and {x['id'] for x in author_inputs}==set(IDS))
for item in author_inputs:
    i=item['id']
    check('complete original '+i,item['original_object']==controls[i] and sha(normalize(controls[i]))==item['original_sha256'])
    check('complete acceptance '+i,item['approved_acceptance_object']==accepts[i] and sha(normalize(accepts[i]))==item['acceptance_sha256'])
for item in h['remaining_three_complete_original_controls']:
    i=item['id']
    check('accepted contract controls '+i,item['complete_original_object']==controls[i] and item['complete_approved_acceptance']==accepts[i])
vectors=load(E,AUTHOR+'new-static-vectors.json')['cases']
check('all35 vector object rows',len(vectors)==35 and {x['test_id'] for x in vectors}==added)
for item in vectors:
    number,line=current[item['test_id']]
    check('vector exact '+item['test_id'],line.decode()==item['row_text'] and number==item['candidate_line'] and sha(line)==item['row_sha256'])
responses=load(E,AUTHOR+'finding-responses.json')['all_ten_responses']
allocation=[]
for item in responses:
    check('response bounded '+item['id'],item['new_independent_verdict'] is None and not item['close'])
    for case in item['test_cases']:
        n,line=catalogrows[case['path']][case['test_id']]
        check('response row '+case['test_id'],n==case['candidate_line'] and sha(line)==case['row_sha256'])
        allocation.append({'finding_id':item['id'],'test_id':case['test_id'],'path':case['path'],'line':n,'sha256':sha(line)})
check('60 distinct allocated rows',len(allocation)==60 and len({(x['path'],x['test_id']) for x in allocation})==60)

# Recovery was precisely the accepted upstream bytes, including public-layer differences.
delta=git('diff','--name-only',HIST,B).decode().splitlines()
merge_inventory=[]
for path in delta:
    check('merge equals accepted '+path,blob(B,path)==blob(ACCEPT,path))
    merge_inventory.append(identity(B,path))
mi=load(E,AUTHOR+'merge-and-dependency-impact.json')['complete_merge_delta']
mergepatch=git('diff','--binary','--full-index',HIST,B)
check('complete recovery merge inventory',set(delta)=={x['path'] for x in mi['all_path_identities']} and len(delta)==129)
check('complete recovery merge patch',len(mergepatch)==mi['bytes'] and sha(mergepatch)==mi['sha256'])
for item in mi['all_path_identities']:
    verify_identity(item['after'])
    if 'before' in item:verify_identity(item['before'])
for item in load(E,AUTHOR+'patch-identities.json')['patches']:
    patch=git('diff','--binary','--unified=0',item['base_commit'],C,'--',*item['selected_formal_paths'])
    check('independent patch '+item['path'],patch==blob(E,item['path']) and sha(patch)==item['sha256'] and len(patch)==item['bytes'])
    (OUT/Path(item['path']).name).write_bytes(patch)
drift=[x['path'] for x in h['planned25_read_identity_pairs'] if x['old_accepted']['sha256']!=x['new_accepted_actual']['sha256']]
check('one planned upstream drift',drift==[F+'test-catalog/engine-overworld-wp11-15-59-60.md'])

# Only the pure author document-range helper is evaluated. No reference source is imported/evaluated.
namespace={}
helper=blob(E,AUTHOR+'document_integrity.py')
exec(compile(helper,AUTHOR+'document_integrity.py','exec'),namespace)
range_hash=namespace['checked_range_sha256']
check('reference exact HEAD/tree',git('rev-parse','HEAD',cwd=REF).decode().strip()==REFERENCE and git('rev-parse','HEAD^{tree}',cwd=REF).decode().strip()=='7589c800b61ba13a13040ed0d686979b80a84fd0')
check('reference clean',not git('status','--porcelain',cwd=REF))
reading=load(E,AUTHOR+'source-reading-log.json');spans=[]
for item in reading['fresh_readings']+reading['inherited_corrected_readings']:
    data=git('show',REFERENCE+':'+item['path'],cwd=REF)
    check('reference file bytes '+item['path'],data==(REF/item['path']).read_bytes() and sha(data)==item['sha256'] and len(data.splitlines(keepends=True))==item['actual_line_count'])
    for r in item['read_ranges']:
        check('reference declared range '+item['reading_id']+str(r['start']),1<=r['start']<=r['end']<=item['actual_line_count'] and range_hash(data,r['start'],r['end'])==r['range_sha256'])
        spans.append({'reading_id':item['reading_id'],'path':item['path'],**r,'bounds_valid':True})
trainer='Data/Scripts/015_Trainers and player/002_Trainer_LoadAndNew.rb'
td=(REF/trainer).read_bytes()
check('N002 actual line count',len(td.splitlines(keepends=True))==124)
check('N002 valid entire range',range_hash(td,1,124)==sha(td))
check('N002 valid final line',range_hash(td,124,124)==sha(td.splitlines(keepends=True)[123]))
invalid=[(trainer,1,135),(trainer,125,125),(trainer,0,124),(trainer,124,1),(trainer,1,0),
         ('Data/Scripts/013_Items/005_Item_PokeRadar.rb',155,280),('Data/Scripts/004_Game classes/008_Game_Player.rb',596,638)]
rejected=[]
for path,start,end in invalid:
    calls=[]
    def observed_hasher(chunk):
        calls.append(True)
        return sha(chunk)
    try:
        range_hash((REF/path).read_bytes(),start,end,hash_bytes=observed_hasher)
    except ValueError:
        check('N002 rejects before hash '+path+str(start)+str(end),not calls)
        rejected.append({'path':path,'range':[start,end],'rejected_before_hash':True,'hash_calls':len(calls)})
    else:
        raise AssertionError('invalid range accepted')
matches=git('grep','-n','pbGetTrainerBattleBGMFromType',REFERENCE,'--','Data/Scripts',cwd=REF).decode().splitlines()
check('FromType fixed Scripts definition only',len(matches)==1 and ':105:def pbGetTrainerBattleBGMFromType' in matches[0])
for path in FORMAL:
    check('formal current bytes '+path,(ROOT/path).read_bytes()==blob(C,path)==blob(E,path))
lock=json.loads((OUT/'first-evidence-lock.json').read_text())
check('first evidence lock',sha((ROOT/lock['path']).read_bytes())==lock['sha256'])
worktree=set(git('diff','--name-only',E).decode().splitlines())|set(git('ls-files','--others','--exclude-standard').decode().splitlines())
prefix=OUT.relative_to(ROOT).as_posix()+'/'
check('review writes only new directory',all(x.startswith(prefix) for x in worktree))
dump('independent-validation.json',{'result':'DOCUMENT_IDENTITY_AND_SCOPE_CHECKS_PASS_NOT_BEHAVIOR_EXECUTION','checks':CHECKS,
     'check_count':len(CHECKS),'candidate':C,'author_evidence':E,'new_delta_paths':DELTA,'all_eight_formal_identities':[identity(C,p) for p in FORMAL],
     'identity_sets':identity_results,'historical_files':hist,'old_clause_guards':clauses,'old_row_guards':oldrows,
     'protected_sections':protected,'WP24_edit_hunks':edits,'prior_catalog_rows_preserved':len(prior),
     'new_rows':35,'allocated_static_rows':60,'reference_declared_spans_validated':len(spans),
     'range_helper_valid_cases':2,'range_helper_invalid_cases':rejected,'behavior_vectors_executed':0,
     'reference_execution':0,'runtime_observations':0,'proven_demo_chains':0})
dump('all60-static-row-identities.json',{'candidate':C,'meaning':'Exact document rows reviewed manually against first evidence; not executed cases.','rows':allocation})
dump('recovery-and-protection.json',{'recovery_commit':B,'parents':[HIST,ACCEPT],'all_129_merge_paths_equal_accepted_upstream':merge_inventory,
     'merge_patch_bytes':len(mergepatch),'merge_patch_sha256':sha(mergepatch),'planned_upstream_drift':drift,
     'accepted_B03_13_input_identities':h['accepted_B03_thirteen_formal_inputs'],'historical_file_checks':hist,
     'B04_B06_order':h['B04_B06_order'],'B04_write_B06_read':h['B04_write_B06_read'],'B06_write_B04_read':h['B06_write_B04_read'],
     'parallel_safety_established':False,'B04_unavoidable_conditions':h['B04_unavoidable_conditions']})
dump('author-evidence-crosscheck.json',{'identity_sets':identity_results,'reference_declared_spans':spans,
     'author_full_ten_controls_equal_original_and_approved':True,'author_selfcheck_not_used_as_independent_verdict':True,
     'author_scripts_not_run_except_pure_document_range_helper':True,'FromType_fixed_Scripts_text_search':matches,
     'no_reference_behavior_evaluated':True})
print(json.dumps({'checks':len(CHECKS),'passed':True,'old_rows':25,'new_rows':35,'historical_current_files':32,
                  'B03_inputs':13,'merge_paths':129,'reference_declared_spans':len(spans),'range_checks_executed':9}))
