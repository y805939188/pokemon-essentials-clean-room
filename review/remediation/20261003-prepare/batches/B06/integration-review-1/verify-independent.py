#!/usr/bin/env python3
"""Read-only Git/document verifier. Does not execute or model reference behavior.

Writes receipts only beside this new script. Historical verifiers are not run.
"""
import collections
import csv
import difflib
import hashlib
import io
import json
import re
import subprocess
import sys
from pathlib import Path

sys.dont_write_bytecode = True
OUT = Path(__file__).resolve().parent
ROOT = OUT.parents[5]
REF = Path('/tmp/R-B06-reference')
A = 'c67f400c000df4fd73ab1440e1487a3d534336aa'
P = 'cdba36a3bc0fcb4629945180fcc3879188f7517b'
B = '1fd612d47dcda164de61ab2d25a1cb5e0fbde085'
C = '4076a3fbbf6fe355b73f3fe2229d1f981fe735d2'
E = 'ee7461e90ad5e0943e39c56c22a080f761f4e1c0'
R = '70babef632539c952aa988e7762d0c2aa19cfeb3'
O = '93e10babe0b9c9ef8b3f5277754541b447beeeb4'
PLAN = '41fffb540c6483f5296ea0d33b789b75180d27ed'
REFSHA = '8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
D = 'review/remediation/20261003-prepare/batches/B06/'
G = D+'integration-stage-1/'
FR = D+'review-full-round-1/'
PL = 'review/remediation-20261003-prepare/'
ORIGINAL = 'review/global-independent-review/2026-10-03-fd82a639/findings.json'
F = 'deliverables/final-specification-set/'
FORMAL = [F+'creature-rpg/wp24-player-trainers-partners.md',F+'creature-rpg/wp25-party-and-storage.md',
          F+'creature-rpg/wp27-bag-and-item-storage.md',F+'test-catalog/creature-rpg-wp18-20-24-25-26.md',
          F+'test-catalog/creature-rpg-wp27-28-29-30-33.md','specs/creature-rpg/wp24-player-trainers-partners.md',
          'specs/creature-rpg/wp25-party-and-storage.md','specs/creature-rpg/wp27-bag-and-item-storage.md']
IDS = ['GIR-FD82-'+s for s in ['A032','A033','A034','A035','A036','A037','A038','A059','C103','C120']]
PUBLIC = ['audit/source-traceability.md',F+'README.md',F+'scope-statement.md',F+'test-catalog/README.md',
          'planning/coverage.md','planning/feature-matrix.md',
          'review/remediation/20261003-prepare/historical-errata.md',
          'review/remediation/20261003-prepare/final-integration-review.md',
          'review/remediation/20261003-prepare/approval-ledger.tsv',
          'review/remediation/20261003-prepare/traceability-successor.tsv']
OPTIONS = ['--no-ext-diff','--no-textconv','--no-color','--no-renames','--binary','--full-index','--unified=3']
CHECKS = []
CACHE = {}
ROWCACHE = {}

def git(*args,cwd=ROOT):
    return subprocess.check_output(['git',*args],cwd=cwd)

def sha(data):
    return hashlib.sha256(data).hexdigest()

def norm(obj):
    return json.dumps(obj,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode()

def check(label,value):
    CHECKS.append({'check':label,'passed':bool(value)})
    if not value:
        raise AssertionError(label)

def data(commit,path):
    key=(commit,path)
    if key not in CACHE:
        CACHE[key]=git('show',commit+':'+path)
    return CACHE[key]

def load(commit,path):
    return json.loads(data(commit,path))

def dump(name,value):
    (OUT/name).write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n')

def identity(commit,path):
    raw=data(commit,path)
    return {'commit':commit,'path':path,'git_blob':git('rev-parse',commit+':'+path).decode().strip(),
            'sha256':sha(raw),'bytes':len(raw)}

def verify_id(item,commit=None):
    got=identity(commit or item['commit'],item['path'])
    check('identity '+got['commit']+':'+got['path'],all(got[k]==item[k] for k in ['git_blob','sha256','bytes']))
    return got

def nested_ids(obj):
    if isinstance(obj,dict):
        if all(k in obj for k in ['commit','path','git_blob','sha256','bytes']):
            yield obj
        for val in obj.values():
            yield from nested_ids(val)
    elif isinstance(obj,list):
        for val in obj:
            yield from nested_ids(val)

def tree(commit):
    return {r.split(b'\t',1)[1].decode():r.split(b'\t',1)[0].split()[2].decode()
            for r in git('ls-tree','-rz','--full-tree',commit).split(b'\0') if r}

def statuses(base,target):
    return [{'change':line.split('\t',1)[0],'path':line.split('\t',1)[1]}
            for line in git('diff','--no-renames','--name-status',base,target).decode().splitlines()]

def rowmap(raw):
    key=sha(raw)
    if key in ROWCACHE:
        return ROWCACHE[key]
    result={}
    for number,line in enumerate(raw.splitlines(keepends=True),1):
        m=re.match(rb'^\| ([A-Z]+-\d+) \|',line)
        if m:
            rid=m[1].decode();check('unique row '+rid,rid not in result);result[rid]=(number,line)
    ROWCACHE[key]=result
    return result

check('review branch',git('branch','--show-current').decode().strip()=='remediation/20261003-prepare/review-B06-integration-1')
check('reviewed actual exists',git('rev-parse',A).decode().strip()==A)
for commit,expected_tree,parents in [
    (A,'def2e2afbf344c3f73d2d330e282bad341af0f70',[P]),
    (P,'32766f33d349a215e279e3d47bac6c063b6a57de',['7be085aa10663d79bfab2108432ffbfe07efe040']),
    (C,'cd171b364f01b300aed5694c7d49af5308b8a330',['df65e346d85213742a2538588818a10f50b819e5']),
    (E,'deb7ced5a49bdbbb61b0cf09b8b224737aa0fd4b',[C]),
    (R,'f8153a6ead9edfddee48ddcef427c99566132ca2',[E]),
    (B,'f31e24bc54c3641d74497a8cc32015ca4cfb9a9a',['dea9d118d7ed3b7ddb57b1c4e7bd40db8dd06497'])]:
    check('tree '+commit,git('rev-parse',commit+'^{tree}').decode().strip()==expected_tree)
    check('parents '+commit,git('show','-s','--format=%P',commit).decode().split()==parents)
m=load(A,G+'integration-manifest.json')
freeze=load(A,G+'diff-and-freeze.json')
hand=load(A,G+'downstream-handshake.json')
reg=load(A,G+'finding-registration.json')
hist=load(A,G+'historical-repair-registration.json')
impact=load(A,G+'merge-and-dependency-impact.json')
counts=load(A,G+'scope-counts.json')
for label,obj in [('manifest',m),('freeze',freeze),('handshake',hand),('registration',reg),('history',hist),('impact',impact)]:
    for item in nested_ids(obj):
        verify_id(item)
    check(label+' zero reference execution',obj.get('reference_execution',0)==0)
check('candidate/current/report separation',m['full_candidate']==C and m['author_handoff']==E and m['candidate_report']==R and m['accepted_upstream']==B)
check('payload exact separation',freeze['payload_commit']==P and freeze['payload_tree']==git('rev-parse',P+'^{tree}').decode().strip())
source=m['source_identities']
check('103 unique sources',len(source)==103 and len({r['path'] for r in source})==103)
check('source inventories identical across manifests',source==impact['source_identities_preserved']==freeze['all_103_source_identities_unchanged'])
source_receipts=[]
for rec in source:
    verify_id(rec)
    actual=verify_id(rec,A);verify_id(rec,P)
    source_receipts.append({'source':rec,'actual':actual,'equal_bytes':data(rec['commit'],rec['path'])==data(A,rec['path'])})
    check('source byte equality '+rec['path'],source_receipts[-1]['equal_bytes'])
check('source formal exactly eight',{r['path'] for r in source if r['path'] in FORMAL}==set(FORMAL))
# Directory names are independently inventoried; historical author repair uses its actual name.
source_groups=collections.Counter(r['path'][len(D):].split('/')[0] if r['path'].startswith(D) else 'formal' for r in source)
check('8 formal +53 author +42 reports',len([r for r in source if r['path'] in FORMAL])==8 and
      sum(v for k,v in source_groups.items() if k.startswith('author'))==53 and
      sum(v for k,v in source_groups.items() if k.startswith('review'))==42)
check('public ten exact',set(r['path'] for r in m['current_public_paths'])==set(PUBLIC))
for rec in m['current_public_paths']:
    verify_id(rec,A);verify_id(rec,P)
formal_receipts=[]
for path in FORMAL:
    check('actual equals candidate formal '+path,data(A,path)==data(C,path)==data(P,path))
    formal_receipts.append({'candidate':identity(C,path),'actual':identity(A,path),'unchanged_from_candidate':True})
check('only actual three added evidence files',statuses(P,A)==[{'change':'A','path':p} for p in sorted(freeze['final_actual_changed_paths'])])
check('final freeze filenames',set(freeze['final_actual_changed_paths'])=={G+'candidate-to-payload.patch',G+'upstream-to-payload.patch',G+'diff-and-freeze.json'})
base_tree=tree(B);actual_tree=tree(A)
changed_existing={p for p,v in base_tree.items() if actual_tree.get(p)!=v}
check('all older files protected outside eight and ten',changed_existing==set(FORMAL+PUBLIC))
newpaths=set(actual_tree)-set(base_tree)
source_new={r['path'] for r in source if r['path'] not in FORMAL}
management={p for p in actual_tree if p.startswith(G)}
check('new paths exactly95 sources and13 management',len(source_new)==95 and len(management)==13 and newpaths==source_new|management)
full_upstream=statuses(B,A)
check('126 complete upstream delta',len(full_upstream)==126 and all(r['change'] in ['A','M'] for r in full_upstream))
merge_specs=[('c564f5575364a395dfd5ef6a4c1bcad2a890cc60',[B,R],None),
             ('3835d0ac24596bfdac5654e28dde5be8eba253b6',['c564f5575364a395dfd5ef6a4c1bcad2a890cc60','e12791309ace5458da29fd91c7bed70ac4175700'],D+'review-stage-1-round-1/'),
             ('7be085aa10663d79bfab2108432ffbfe07efe040',['3835d0ac24596bfdac5654e28dde5be8eba253b6','296a26070cf14b49a42c1c2767274fd7b4e5f7dc'],D+'review-stage-1-round-2/')]
merge_receipts=[]
for commit,parents,prefix in merge_specs:
    check('ordinary merge parents '+commit,git('show','-s','--format=%P',commit).decode().split()==parents)
    delta=statuses(parents[0],commit)
    allowed={r['path'] for r in source if prefix is None and (r['path'] in FORMAL or '/author' in r['path'] or '/review-full-round-1/' in r['path']) or prefix and r['path'].startswith(prefix)}
    check('merge delta only expected imported paths '+commit,{r['path'] for r in delta}==allowed)
    for path in allowed:
        check('merge uses right parent bytes '+path,data(commit,path)==data(parents[1],path)==data(A,path))
    merge_receipts.append({'commit':commit,'parents':parents,'delta':delta,'no_formal_resolution_rewrite':True})
check('merge manifest exact order',m['normal_merge_commits']==[x[0] for x in merge_specs])
check('payload only10 public and10 initial management',{r['path'] for r in statuses(merge_specs[-1][0],P)}==set(PUBLIC)|set(m['new_payload_paths']) and len(m['new_payload_paths'])==10)
diff_receipts=[]
for rec in freeze['full_patches']:
    check('unfiltered payload diff options',rec['git_diff_options']==OPTIONS and rec['selected_paths']=='ALL; no path filter')
    generated=git('diff',*OPTIONS,rec['base_commit'],rec['target_commit'])
    stored=data(A,rec['path'])
    check('full payload patch exact '+rec['path'],generated==stored and sha(generated)==rec['sha256'] and len(generated)==rec['bytes'])
    check('payload complete path statuses',statuses(rec['base_commit'],P)==rec['complete_path_statuses'])
    actual_generated=git('diff',*OPTIONS,rec['base_commit'],A)
    actual_status=statuses(rec['base_commit'],A)
    key='final_actual_complete_upstream_diff_contract' if rec['base_commit']==B else 'final_actual_complete_candidate_diff_contract'
    contract=freeze[key]
    check('final complete diff contract '+key,contract['base']==rec['base_commit'] and
          sorted(contract['payload_path_statuses']+[{'change':'A','path':p} for p in contract['append_exact_three_added_final_evidence_paths']],key=lambda r:r['path'])==actual_status and
          len(actual_status)==contract['expected_path_count'])
    diff_receipts.append({'base':rec['base_commit'],'target':A,'options':OPTIONS,'unfiltered':True,
                         'bytes':len(actual_generated),'sha256':sha(actual_generated),'complete_path_statuses':actual_status,
                         'preserved_payload_patch':identity(A,rec['path'])})
for rec in freeze['payload_public_and_management_identities']:
    verify_id(rec,A)
hashrows=list(csv.DictReader(io.StringIO(data(A,G+'current-hashes.tsv').decode()),delimiter='\t'))
check('current hashes113 exact pathset',len(hashrows)==113 and {r['path'] for r in hashrows}=={r['path'] for r in source}|set(PUBLIC))
for row in hashrows:
    rec={**row,'bytes':int(row['bytes'])}
    verify_id(rec,A)
    if row['commit']:
        verify_id(rec)

findings=load(O,ORIGINAL);original={r['id']:r for r in findings}
acceptance=load(PLAN,PL+'finding-acceptance.json')
plans={r['id']:r for r in load(PLAN,PL+'batches.json')}
controls=load(R,FR+'canonical-controls.json')
old_dispositions=load(R,FR+'finding-contribution-dispositions.json')
old_byid={r['id']:r for r in old_dispositions['findings']}
canon_byid={r['id']:r for r in controls['findings']}
check('original229 required',sum(r['required_revision'] is True for r in findings)==229)
check('registration ten exact',len(reg['dispositions'])==10 and {r['id'] for r in reg['dispositions']}==set(IDS))
check('registration7primary',sum(r['B06_primary'] for r in reg['dispositions'])==7)
canonical_receipts=[]
for r in reg['dispositions']:
    fid=r['id'];orig=original[fid];ac=acceptance[fid];ctrl=canon_byid[fid]
    check('original object preserved '+fid,ctrl['complete_original_object']==orig)
    check('acceptance object preserved '+fid,ctrl['complete_approved_acceptance']==ac)
    check('original canonical hash '+fid,r['original_complete_object_sha256']==sha(norm(orig)))
    check('approved canonical hash '+fid,r['acceptance_object_sha256']==sha(norm(ac)))
    for k in ['priority','current_qualifications','adjudication_precedence','minimum_revision','determinate_recheck','acceptance_gate']:
        check('canonical field '+fid+':'+k,r[k]==ac[k])
    check('effective constraints '+fid,r['effective_case_constraints']==orig.get('effective_case_constraints'))
    check('candidate disposition preserved '+fid,r['independent_candidate_disposition_preserved']==old_byid[fid])
    check('formal and static bindings preserved '+fid,r['formal_clause_bindings']==old_byid[fid]['formal_clause_bindings'] and r['static_rows_not_executed']==old_byid[fid]['static_row_bindings'])
    check('registry candidate-only open gates '+fid,r['canonical_state']=='OPEN' and not r['canonical_edited'] and r['candidate']==C and r['candidate_handoff']==E and r['candidate_report']==R and r['candidate_verdict']=='PASS_SCOPED' and r['actual_integration_verdict']=='NOT_REVIEWED_PENDING_R_B06_ULTRA' and r['downstream_gate']=='BLOCKED_UNTIL_ACTUAL_B06_ULTRA_AND_PARENT_ACCEPTANCE')
    allcontributors=[bid for bid,plan in plans.items() if fid in plan['contribution_finding_ids']]
    check('all contributor ownership retained '+fid,r['all_contributor_batches']==allcontributors)
    check('other contributors retained '+fid,set(r['other_batch_obligations'])==set(allcontributors)-{'B06'})
    for item in r['formal_clause_bindings']:
        lo,hi=item['lines'];lines=data(A,item['path']).splitlines(keepends=True)
        check('current clause range and hash '+fid,type(lo) is int and type(hi) is int and 1<=lo<=hi<=len(lines) and sha(b''.join(lines[lo-1:hi]))==item['range_sha256'])
    canonical_receipts.append({'id':fid,'original_object_sha256':sha(norm(orig)),'acceptance_object_sha256':sha(norm(ac)),
        'all_contributors':allcontributors,'remaining_other_contributors':r['other_batch_obligations'],
        'canonical_state':'OPEN','actual_review_scope':'B06 contribution only'})
check('A034 remains B08',next(r for r in canonical_receipts if r['id'].endswith('A034'))['all_contributors']==['B06','B08'])
check('A059 all owners',next(r for r in canonical_receipts if r['id'].endswith('A059'))['all_contributors']==['B04','B06','B09','B17','B21'])
check('C103 all owners',next(r for r in canonical_receipts if r['id'].endswith('C103'))['all_contributors']==['B06','B14'])
check('C120 all owners',next(r for r in canonical_receipts if r['id'].endswith('C120'))['all_contributors']==['B06','B16'])
rows60=load(R,FR+'all60-static-row-identities.json')['rows']
check('60 unique allocated rows',len(rows60)==60 and len({(r['path'],r['test_id']) for r in rows60})==60)
actual_rows=[]
for r in rows60:
    rows=rowmap(data(A,r['path']));num,line=rows[r['test_id']]
    check('actual exact row '+r['test_id'],num==r['line'] and sha(line)==r['sha256'])
    actual_rows.append({**r,'reviewed_actual':A,'execution':'NOT_EXECUTED_STATIC_DOCUMENT_ROW'})
catalog_receipts=[]
for path in FORMAL[3:5]:
    old=rowmap(data(B,path));now=rowmap(data(A,path))
    changed=[rid for rid in old if now[rid][1]!=old[rid][1]]
    new=[rid for rid in now if rid not in old]
    check('no removed catalog rows '+path,set(old)<=set(now))
    check('only PS11 AQ04 old row changes '+path,set(changed)==({'PS-11','AQ-04'} if path==FORMAL[3] else set()))
    families=dict(collections.Counter(rid.split('-')[0] for rid in now))
    count=counts['catalogs'][path]
    check('catalog counter exact '+path,len(old)==count['old_total'] and len(now)==count['current_total'] and len(new)==count['added_row_count'] and families==count['family_counts'])
    catalog_receipts.append({'path':path,'old_count':len(old),'current_count':len(now),'added':new,'changed_old':changed,'family_counts':families,'all_unallocated_old_rows_preserved':True})
check('catalog389 total',sum(r['current_count'] for r in catalog_receipts)==389 and sum(len(r['added']) for r in catalog_receipts)==58)
tsv_receipts=[]
for path in PUBLIC[-2:]:
    old=data(B,path);now=data(A,path)
    check('old TSV exact prefix '+path,now.startswith(old))
    oldrows=list(csv.DictReader(io.StringIO(old.decode()),delimiter='\t'))
    currows=list(csv.DictReader(io.StringIO(now.decode()),delimiter='\t'))
    check('69+10 contribution rows '+path,len(oldrows)==69 and len(currows)==79 and currows[:69]==oldrows)
    added=currows[69:];check('ten registry IDs '+path,[r['finding_id'] for r in added]==IDS)
    for row in added:
        fid=row['finding_id'];r=next(v for v in reg['dispositions'] if v['id']==fid)
        check('TSV exact candidate report/open '+fid,row['canonical_state']=='OPEN' and row['candidate_commit']==C and row['candidate_review_commit']==R)
        if 'candidate_verdict' in row:
            check('approval pending gate '+fid,row['candidate_verdict']=='PASS_SCOPED' and row['integration_verdict']=='NOT_REVIEWED_PENDING_ULTRA' and row['downstream_gate']=='BLOCKED')
        else:
            check('trace formal clause bindings '+fid,json.loads(row['current_clause_inputs'])==r['formal_clause_bindings'])
            check('trace static IDs '+fid,row['static_test_ids_not_executed'].split(';')==[s['test_id'] for s in r['static_rows_not_executed']])
            check('trace remaining owners '+fid,[s for s in row['remaining_batches'].split(';') if s]==r['other_batch_obligations'])
            check('trace pending gate '+fid,row['integration_gate']=='PENDING_R_B06_ULTRA_OF_EXACT_NEW_ACTUAL')
        obligations=json.loads(row['remaining_obligations'])
        check('TSV full remaining obligations '+fid,obligations['all_contributor_batches']==r['all_contributor_batches'] and obligations['other_batch_obligations']==r['other_batch_obligations'] and obligations['actual_integration']=='PENDING_R_B06_ULTRA' and obligations['canonical_closure'].startswith('OPEN;'))
    tsv_receipts.append({'path':path,'old69_byte_sha256':sha(old),'current79_sha256':sha(now),'old69_unchanged':True,'new_ids':IDS})
public_edits=[]
for path in PUBLIC[:-2]:
    old=data(B,path).splitlines(keepends=True);now=data(A,path).splitlines(keepends=True)
    edits=[(tag,a,b,c,d) for tag,a,b,c,d in difflib.SequenceMatcher(None,old,now,autojunk=False).get_opcodes() if tag!='equal']
    if path==F+'test-catalog/README.md':
        replacements=[e for e in edits if e[0]=='replace']
        check('catalog README only2 replacements',len(replacements)==1 and replacements[0][2]-replacements[0][1]==2 and replacements[0][4]-replacements[0][3]==2)
        for e in edits:
            check('catalog index no deletions',e[0] in ['insert','replace'])
    else:
        check('historical public body append-only '+path,all(e[0]=='insert' for e in edits))
    public_edits.append({'path':path,'operations':[{'kind':t,'old_lines':[a+1,b],'actual_lines':[c+1,d]} for t,a,b,c,d in edits],'older_body_preserved':True})

downstream_receipts=[]
for bid in ['B04','B07']:
    h=hand[bid];plan=plans[bid]
    check(bid+' deps exact',h['planned_dependencies']==plan['dependencies'])
    check(bid+' read contract exact',[r['path'] for r in h['planned_reads']]==plan['read_paths'])
    writes=h['allowed_formal_write_paths'] if bid=='B04' else h['allowed_write_paths']
    check(bid+' write contract exact',writes==plan['write_paths'] and len(writes)==8)
    ext=[]
    for r in h['planned_reads']:
        if 'commit' in r:
            verify_id(r);ext.append(r)
            check(bid+' external original binding',r['commit']==O)
        else:
            verify_id(r,A);verify_id(r,P)
    check(bid+' exactly2 external immutable reads',len(ext)==2)
    ctrls=h['contribution_controls'];check(bid+' controls exact',[r['id'] for r in ctrls]==plan['contribution_finding_ids'])
    for r in ctrls:
        fid=r['id'];contrib=[k for k,p in plans.items() if fid in p['contribution_finding_ids']]
        check(bid+' full original acceptance controls '+fid,r['original_object_sha256']==sha(norm(original[fid])) and r['acceptance_object_sha256']==sha(norm(acceptance[fid])) and r['priority']==acceptance[fid]['priority'] and r['all_contributors']==contrib and r['canonical_state']=='OPEN' and r['read_all_current_qualifications_root_extensions_required'])
    downstream_receipts.append({'batch':bid,'plan':PLAN,'read_count':len(h['planned_reads']),'write_count':len(writes),'external_reads':ext,'original_and_acceptance_controls':ctrls,'read_identity_target':A})
check('B04 74+8',len(hand['B04']['planned_reads'])==74 and hand['B04']['planned_read_count']==74 and not hand['B04']['original_specs_write_authorized'])
check('B04 explicit eight-write count',hand['B04']['allowed_formal_write_count']==8)
check('B04 primary23 and contribution35 contract',hand['B04']['primary_finding_ids']==plans['B04']['primary_finding_ids'] and len(hand['B04']['primary_finding_ids'])==23 and hand['B04']['contribution_finding_ids']==plans['B04']['contribution_finding_ids'] and len(hand['B04']['contribution_finding_ids'])==35)
check('B04 write input set',len(hand['B04']['allowed_write_input_identities'])==8 and {r['path'] for r in hand['B04']['allowed_write_input_identities']}==set(plans['B04']['write_paths']))
check('B04 additional evidence12',len(hand['B04']['additional_read_only_current_B06_B03_evidence'])==12)
for item in hand['B04']['allowed_write_input_identities']+hand['B04']['additional_read_only_current_B06_B03_evidence']:
    verify_id(item,A);verify_id(item,P)
check('B07 64+8',len(hand['B07']['planned_reads'])==64)
pair=hand['B04_B07_pair'];w4=set(plans['B04']['write_paths']);w7=set(plans['B07']['write_paths']);r4=set(plans['B04']['read_paths']);r7=set(plans['B07']['read_paths'])
check('B04/B07 zero W/W but four forward+two reverse',not w4&w7 and {r['path'] for r in pair['B04_write_B07_read']}==w4&r7 and len(w4&r7)==4 and {r['path'] for r in pair['B07_write_B04_read']}==w7&r4 and len(w7&r4)==2)
shared=set(plans['B04']['contribution_finding_ids'])&set(plans['B07']['contribution_finding_ids'])
check('C003 shared exact',shared==set(pair['shared_canonical_ids'])=={'GIR-FD82-C003'})
check('pair serial/stale input rule',not pair['parallel_safety_established'] and pair['recommendation'].startswith('SERIAL_COMPLETE_CONTRACTS_B04_THEN_B07') and 'targeted B04 affected review' in pair['recommendation'] and 'all8 finalized extensions' in pair['shared_C003_rule'])
interface=hand['B04_B06_frozen_interfaces'];b6=plans['B06']
check('B04/B06 interfaces recomputed',set(interface['B04_write_B06_read'])==w4&set(b6['read_paths']) and len(interface['B04_write_B06_read'])==4 and set(interface['B06_write_B04_read'])==set(b6['write_paths'])&r4 and len(interface['B06_write_B04_read'])==1)
check('B04 preparation not byteverified',not hand['B04']['completed_read_only_investigation']['content_identity_verified'] and hand['B04']['completed_read_only_investigation']['fixed_artifact_commit_path']=='NOT_PROVIDED_OR_READ')
check('no downstream dispatch/global closure',hand['downstream_tasks_dispatched']==0 and not hand['global_gate_passed'] and hand['canonical_required_open']==229 and hand['canonical_closed']==0 and hand['actual_integration']=='PENDING_R_B06_ULTRA' and hand['parent_acceptance']=='NOT_PERFORMED')
c003=original['GIR-FD82-C003'];ac003=acceptance['GIR-FD82-C003']
check('C003 all8 extensions preserved',len(ac003['extension_decisions'])==8)
check('historical two defects not closed',hist['local_issue_ids']==['B06-S1-R1-N001','B06-S1-R1-N002'] and not hist['issues_closed'] and hist['canonical229_inventory_mutations']==0)
first=load('e12791309ace5458da29fd91c7bed70ac4175700',D+'review-stage-1-round-1/new-findings.json')
check('original two new findings complete preserved',hist['complete_first_report_new_findings']==first)
check('two full-candidate regressions preserved',hist['full_ten_regression_dispositions']==old_dispositions['historical_new_defect_regressions'])

check('reference outside repository',not REF.is_relative_to(ROOT))
check('reference HEAD',git('rev-parse','HEAD',cwd=REF).decode().strip()==REFSHA)
check('reference tree',git('rev-parse','HEAD^{tree}',cwd=REF).decode().strip()=='7589c800b61ba13a13040ed0d686979b80a84fd0')
check('reference clean',git('status','--porcelain',cwd=REF)==b'')
refmeta=[]
for r in load(R,FR+'independent-source-reading.json')['readings']:
    raw=git('show',REFSHA+':'+r['path'],cwd=REF);lines=raw.splitlines(keepends=True)
    check('reference file metadata '+r['path'],sha(raw)==r['sha256'] and ('bytes' not in r or len(raw)==r['bytes']) and len(lines)==r['actual_line_count'] and ('git_blob' not in r or git('rev-parse',REFSHA+':'+r['path'],cwd=REF).decode().strip()==r['git_blob']))
    for span in r['human_read_ranges']:
        lo,hi=span['start'],span['end']
        check('bounded historical navigation '+r['path'],type(lo) is int and type(hi) is int and 1<=lo<=hi<=len(lines) and sha(b''.join(lines[lo-1:hi]))==span['range_sha256'])
    refmeta.append({'path':r['path'],'sha256':sha(raw),'actual_line_count':len(lines),'historical_navigation_metadata_verified':True})
spans=load(R,FR+'author-evidence-crosscheck.json')['reference_declared_spans']
check('40 author spans metadata count',len(spans)==40)
current_log=load(A,D+'author-stage2/source-reading-log.json')
current_spans=[]
for reading in current_log['fresh_readings']+current_log['inherited_corrected_readings']:
    raw=git('show',REFSHA+':'+reading['path'],cwd=REF);lines=raw.splitlines(keepends=True)
    check('current author source identity '+reading['reading_id'],sha(raw)==reading['sha256'] and len(lines)==reading['actual_line_count'] and git('rev-parse',REFSHA+':'+reading['path'],cwd=REF).decode().strip()==reading['git_blob'])
    for span in reading['read_ranges']:
        lo,hi=span['start'],span['end']
        valid=type(lo) is int and type(hi) is int and 1<=lo<=hi<=len(lines)
        check('current author source bounds '+reading['reading_id'],valid)
        check('current author source range hash '+reading['reading_id'],sha(b''.join(lines[lo-1:hi]))==span['range_sha256'])
        current_spans.append({'reading_id':reading['reading_id'],'path':reading['path'],'start':lo,'end':hi,'range_sha256':span['range_sha256'],'bounds_valid':True})
check('current40 author spans identical to previously reviewed metadata',current_spans==spans)
for span in spans:
    raw=git('show',REFSHA+':'+span['path'],cwd=REF);lines=raw.splitlines(keepends=True)
    lo,hi=span['start'],span['end']
    check('author range freshly bounded '+span['reading_id'],span['bounds_valid'] and type(lo) is int and type(hi) is int and 1<=lo<=hi<=len(lines))
    check('author range freshly hashed '+span['reading_id'],sha(b''.join(lines[lo-1:hi]))==span['range_sha256'])
lock=json.loads((OUT/'first-evidence-lock.json').read_text())
check('first semantic lock unchanged',sha((OUT/'independent-first-evidence.md').read_bytes())==lock['first_evidence']['sha256'])
check('AGENTS unchanged',data(A,'AGENTS.md')==data(B,'AGENTS.md')==(ROOT/'AGENTS.md').read_bytes())
author_responses={r['id']:r for r in load(E,D+'author-stage2/finding-responses.json')['all_ten_responses']}
for r in reg['dispositions']:
    check('full author response immutable '+r['id'],r['author_stage2_response_preserved']==author_responses[r['id']])
b03=load(B,'review/remediation/20261003-prepare/batches/B03/acceptance-stage-1/downstream-handshake.json')
check('accepted B03 actual/report exact',b03['accepted_B03_actual_commit']=='e24f2ac6f43642ea0e68bd9aa21fb2c313d6ebdf' and b03['accepted_B03_integration_report']=='dea9d118d7ed3b7ddb57b1c4e7bd40db8dd06497')
check('B03 actual tree',git('rev-parse',b03['accepted_B03_actual_commit']+'^{tree}').decode().strip()==b03['accepted_B03_actual_tree']=='d773aa6c96be4ca878350bd0a3ce6098ca71971b')
check('B03 report parent actual',git('show','-s','--format=%P',b03['accepted_B03_integration_report']).decode().strip()==b03['accepted_B03_actual_commit'])
check('B03 thirteen accepted formal inputs',len(b03['accepted_B03_thirteen_formal_inputs'])==13)
for item in b03['accepted_B03_thirteen_formal_inputs']:
    verify_id(item);verify_id(item,A)
range_cases=[]
trainer_path='Data/Scripts/015_Trainers and player/002_Trainer_LoadAndNew.rb'
trainer_lines=git('show',REFSHA+':'+trainer_path,cwd=REF).splitlines(keepends=True)
check('N002 actual124',len(trainer_lines)==124)
for lo,hi,expected in [(1,124,True),(124,124,True),(1,135,False),(0,1,False),(3,2,False),(1,125,False),(True,124,False),(1.0,124,False),(1,'124',False)]:
    valid=type(lo) is int and type(hi) is int and 1<=lo<=hi<=len(trainer_lines)
    hashed=sha(b''.join(trainer_lines[lo-1:hi])) if valid else None
    check('independent document bounds '+repr((lo,hi)),valid==expected and (valid or hashed is None))
    range_cases.append({'start':lo,'end':hi,'expected_valid':expected,'actual_valid':valid,'range_sha256':hashed,'rejected_before_hash':not valid})
dump('independent-range-validation.json',{'meaning':'new reviewer document-bound validation only; no author helper or reference behavior executed','path':trainer_path,'actual_line_count':124,'cases':range_cases,'valid':2,'invalid_rejected_before_hash':7})
dump('git-and-source-identities.json',{'actual':A,'actual_tree':git('rev-parse',A+'^{tree}').decode().strip(),'accepted_upstream':B,'candidate':C,'author_evidence':E,'candidate_report':R,'formal':formal_receipts,'source103':source_receipts,'source_groups':dict(source_groups),'merges':merge_receipts,'complete_diffs':diff_receipts,'actual_final_three':[identity(A,p) for p in freeze['final_actual_changed_paths']],'all_prior_paths_outside_eight_and_ten_unchanged':True})
dump('canonical-and-contribution-checks.json',{'actual':A,'canonical_required_open':229,'closed':0,'contribution_records79_not_canonical_count':True,'findings':canonical_receipts,'N001_N002':{'historical_objects_preserved':True,'closed':False,'actual_scoped_regression_rechecked':True}})
dump('all60-actual-static-rows.json',{'actual':A,'meaning':'exact document rows freshly read and bounded hashes recalculated; no executed behavior','rows':actual_rows,'catalog_inventory':catalog_receipts})
dump('public-layer-checks.json',{'actual':A,'public_paths10':PUBLIC,'old69_contribution_rows':tsv_receipts,'public_increment_operations':public_edits,'all_previous_acceptance_layers_preserved':True,'actual_approval_not_prematurely_claimed':True})
dump('downstream-contract-checks.json',{'actual':A,'plan':PLAN,'contracts':downstream_receipts,'B04_B07_pair':pair,'B04_B06_interfaces':interface,'C003_original_sha256':sha(norm(c003)),'C003_acceptance_sha256':sha(norm(ac003)),'C003_finalized_extensions_count':8,'dispatch':0,'parent_acceptance_pending':True,'required_accepted_successor_re_freeze':True})
dump('reference-metadata-checks.json',{'reference':REFSHA,'reference_tree':'7589c800b61ba13a13040ed0d686979b80a84fd0','reference_program_execution':0,'behavior_vectors_executed':0,'historical_navigation_metadata':refmeta,'author_range_metadata_count':40,'historical_author_verifiers_executed':False})
dump('independent-validation.json',{'actual':A,'kind':'independent Git/document assertions; not reference execution or behavior coverage','checks':CHECKS,'passed':sum(r['passed'] for r in CHECKS),'failed':sum(not r['passed'] for r in CHECKS),'runtime_observations':0,'proven_demo_event_chains':0,'behavior_vectors_executed':0,'reference_program_execution':0,'old6594_or_integrator1031_checks_rerun':False})
print(json.dumps({'passed':len(CHECKS),'failed':0,'actual':A,'source103':103,'formal8':8,'allocated_static_rows':60,'reference_execution':0}))
