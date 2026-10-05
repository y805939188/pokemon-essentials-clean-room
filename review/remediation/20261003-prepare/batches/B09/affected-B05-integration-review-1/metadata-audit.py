#!/usr/bin/env python3
"""Own Git/text/JSON identity audit; no reference code or behavioral vectors run."""
import csv, hashlib, io, json, re, subprocess
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

ROOT=Path('/workspace/b09-affected-b05-actual-review')
REF=Path('/workspace/b05-reference')
B='407536adb682a04161d3e9c82f153a62b1becd97'
C='18873059e56314fcd48f6081d5a65a79301a52f6'
T='dc64807c2d726171827017ec636c6a73efd8e4b5'
O='93e10babe0b9c9ef8b3f5277754541b447beeeb4'
P='41fffb540c6483f5296ea0d33b789b75180d27ed'
R='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
PREFIX='review/remediation/20261003-prepare/batches/B09/'
STAGE=PREFIX+'integration-stage-1/'
OUT=ROOT/(PREFIX+'affected-B05-integration-review-1')
OUT.mkdir(parents=True,exist_ok=True)
checks=[]
def check(name,ok,evidence):
    checks.append({'check':name,'pass':bool(ok),'evidence':evidence})
def git(*args,root=ROOT):
    return subprocess.check_output(['git',*args],cwd=root)
def sha(b):return hashlib.sha256(b).hexdigest()
def save(name,x):
    (OUT/name).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
batch=subprocess.Popen(['git','cat-file','--batch'],cwd=ROOT,stdin=subprocess.PIPE,stdout=subprocess.PIPE)
cache={}
def blob(commit,path):
    key=(commit,path)
    if key not in cache:
        batch.stdin.write((commit+':'+path+'\n').encode());batch.stdin.flush()
        header=batch.stdout.readline().decode().strip().split()
        if header[-1]=='missing':raise ValueError(f'missing {key}')
        oid,typ,size=header;data=batch.stdout.read(int(size));batch.stdout.read(1)
        assert typ=='blob'
        cache[key]=({'commit':commit,'path':path,'git_blob':oid,'sha256':sha(data),'bytes':len(data)},data)
    return cache[key]
def identity(commit,path):return blob(commit,path)[0]
def data(commit,path):return blob(commit,path)[1]
def load(commit,path):return json.loads(data(commit,path))
def matches(i,commit=None,path=None):
    c=commit or i.get('commit');p=path or i.get('path')
    a=identity(c,p)
    return all(a[k]==i[k] for k in ['git_blob','sha256','bytes'] if k in i)
stage={p.name:json.loads(p.read_text()) for p in (ROOT/STAGE).glob('*.json')}
m=stage['integration-manifest.json'];scope=stage['scope-and-observation-registration.json']
readers=stage['current-readers.json'];counts=stage['scope-counts.json'];fr=stage['finding-registration.json']
payload=git('rev-parse',T+'^').decode().strip()
norm={x['path'] for x in m['reviewed_normative_identities']}
public=set(m['public_write_paths']);manage=set(m['management_stage_paths']);freeze=set(m['final_freeze_paths'])
check('frozen actual and graph',git('rev-parse','HEAD').decode().strip()==T and payload=='3ec4af10f9822999b329ac794e4694bc5aa89aac',{'T':T,'parent':payload,'tree':git('rev-parse',T+'^{tree}').decode().strip()})
check('normative/public/stage class sizes',len(norm)==14 and len(public)==10 and len(manage|freeze)==14,{'normative':len(norm),'public':len(public),'management':len(manage),'freeze':len(freeze)})
def diff_names(a,b):
    raw=git('diff','--no-ext-diff','--no-textconv','--no-renames','--name-status','-z',a,b)
    cells=raw.decode().rstrip('\0').split('\0');return list(zip(cells[::2],cells[1::2]))
def kind(p):
    if p in norm:return 'normative'
    if p in public:return 'public_registration'
    if p in manage|freeze:return 'integration_stage'
    if p.startswith(PREFIX):return 'author_or_independent_report_evidence'
    return 'OUTSIDE'
def diff_summary(a,b,expected):
    changes=diff_names(a,b)
    cmd=['git','diff','--no-ext-diff','--no-textconv','--no-renames','--binary',a,b]
    raw=git(*cmd[1:]);cs=Counter(kind(p) for _,p in changes)
    result={'before':a,'after':b,'command':cmd,'path_filter_used':False,'sha256':sha(raw),'bytes':len(raw),'lines':raw.count(b'\n'),'changed_path_count':len(changes),'classes':dict(cs),'paths':[]}
    for s,p in changes:
        result['paths'].append({'change':s,'path':p,'classification':kind(p),'before':None if s=='A' else identity(a,p),'after':None if s=='D' else identity(b,p)})
    check('whole diff '+a[:7]+' to '+b[:7],len(changes)==expected and cs.get('OUTSIDE',0)==0,{'path_count':len(changes),'sha256':result['sha256'],'classes':dict(cs)})
    return result
whole=[diff_summary(B,T,199),diff_summary(C,T,112)]
save('whole-diff-identities.json',whole)
for file in ['upstream-to-payload-identities.json','candidate-to-payload-identities.json']:
    d=stage[file];raw=git(*d['command'][1:]);paths=diff_names(d['before_commit'],payload)
    declared=[(x['change'],x['path']) for x in d['changed_paths']]
    ok=sha(raw)==d['diff_sha256'] and len(raw)==d['diff_bytes'] and raw.count(b'\n')==d['diff_lines'] and paths==declared and len(paths)==d['changed_path_count']
    check('reconstruct full payload diff '+file,ok,{'sha256':sha(raw),'bytes':len(raw),'lines':raw.count(b'\n'),'paths':len(paths)})
check('actual adds only three final freeze files',diff_names(payload,T)==[('A',p) for p in sorted(freeze)],{'paths':diff_names(payload,T)})
check('candidate normative preserved at actual',all(matches(i,T) and matches(i,C) for i in m['reviewed_normative_identities']),{'count':len(norm)})
check('all 175 author/report/normative sources preserved',all(matches(i) and matches(i,T) for i in m['source_identities']),{'count':len(m['source_identities'])})
report_receipts=[]
for receipt in m['candidate_reports']:
    files=git('ls-tree','-r','--name-only',receipt['commit'],'--',receipt['report_directory']).decode().splitlines()
    preserved=all(data(receipt['commit'],p)==data(T,p) for p in files)
    report_receipts.append({'role':receipt['role'],'commit':receipt['commit'],'files':len(files),'preserved':preserved,'actual_gate_satisfied':False})
check('five immutable candidate receipts preserved, no PASS transfer',all(x['preserved'] for x in report_receipts) and sum(x['files'] for x in report_receipts)==88 and all(x['actual_gate_satisfied'] is False for x in m['candidate_reports']),report_receipts)
merge_results=[]
for x in m['normal_native_merges']:
    ps=git('show','-s','--format=%P',x['result']).decode().strip().split()
    tr=git('rev-parse',x['result']+'^{tree}').decode().strip()
    if x['mode']=='--ff-only':ok=ps==x['parents'] and subprocess.run(['git','merge-base','--is-ancestor',x['before'],x['source']],cwd=ROOT).returncode==0
    else:ok=ps==[x['before'],x['source']]
    merge_results.append({'result':x['result'],'mode':x['mode'],'parents':ps,'tree':tr,'pass':ok and tr==x['tree']})
check('six native merge lineage',len(merge_results)==6 and all(x['pass'] for x in merge_results),merge_results)

# Verify every explicit historical identity and every explicitly actual-bound identity
# in the 12 JSON stage files. Do not rebind null/unspecified historical inputs to T.
identity_checks=[];unbound=[]
def walk(v,loc):
    if isinstance(v,dict):
        if all(k in v for k in ['path','git_blob','sha256','bytes']):
            c=v.get('commit')
            if not c and str(v.get('binding','')).startswith('B09-G actual'):c=T
            if c:
                ok=matches(v,c);identity_checks.append({'locator':loc,'commit':c,'path':v['path'],'pass':ok})
            else:unbound.append({'locator':loc,'path':v['path'],'reason':'no commit/explicit actual binding; checked only in its parent-specific audit where applicable'})
        for k,x in v.items():walk(x,loc+'/'+k)
    elif isinstance(v,list):
        for n,x in enumerate(v):walk(x,loc+'/'+str(n))
for n,d in stage.items():walk(d,n)
check('all explicit integration-stage identity bindings',all(x['pass'] for x in identity_checks),{'checks':len(identity_checks),'unique_commit_paths':len({(x['commit'],x['path']) for x in identity_checks}),'unbound':len(unbound)})
save('integration-identity-bindings.json',{'checked':identity_checks,'unbound_not_silently_rebound':unbound,'stage_files':[identity(T,str(p.relative_to(ROOT))) for p in sorted((ROOT/STAGE).iterdir())]})
check('all 70 current reader bindings independently resolved',len(readers['readers'])==70 and all(matches(x['actual_current'],x['actual_current'].get('commit') or T) and matches(x['reviewed_candidate']) and matches(x['declared_frozen_input']) and x['candidate_to_actual_changed']==(data(x['reviewed_candidate']['commit'],x['path'])!=data(x['actual_current'].get('commit') or T,x['path'])) for x in readers['readers']),{'count':len(readers['readers']),'planned':readers['planned_original62'],'amended':readers['amended_extra8'],'explicit_fixed_historical_bindings_preserved':True})
affected=next(x for x in readers['affected_current_scopes'] if x['accepted_batch']=='B05')
check('all nine bounded B05 current inputs',len(affected['actual_current_inputs'])==9 and all(matches(i,T) for i in affected['actual_current_inputs']) and affected['same_normative_blob_does_not_transfer_PASS'] is True,{'current_inputs':affected['actual_current_inputs'],'candidate_receipt':affected['candidate_receipt']['commit']})
check('ten public current identities independently resolved',len(readers['current_public_versions'])==10 and all(matches(x,T) for x in readers['current_public_versions']),{'paths':sorted(public)})

# Scope authority is permission only. Audit exact WP20 substitutions and all other
# original approved before/after identities; do not assert original write chronology.
am=load(C,PREFIX+'scope-amendment-2/approval.json');application=load(C,PREFIX+'scope-amendment-2/application.json')
wp20_checks=[]
for f in am['files']:
    before=data(B,f['path']).decode();after=before
    ok=matches(f['before'],B)
    for clause in f['clause_changes']:
        old=clause['before_text'];new=clause['intended_after_text']
        ok=ok and after.count(old)==1;after=after.replace(old,new,1)
    ok=ok and after.encode()==data(T,f['path']) and matches(f['intended_after'],T,f['path'])
    wp20_checks.append({'path':f['path'],'approved_clause_count':len(f['clause_changes']),'exact_only_changes':ok})
check('exact four WP20 approved clauses, all remaining bytes protected',sum(x['approved_clause_count'] for x in wp20_checks)==4 and all(x['exact_only_changes'] for x in wp20_checks) and am['scope_authorization_only'] and not am['independent_correctness_approval'],wp20_checks)
origapp=load(C,PREFIX+'candidate-1/original-application.json');origapproval=load(C,PREFIX+'candidate-1/original-scope-approval.json')
origchecks=[]
for f in origapp['exact_approved_originals_applied']:
    ok=matches(f['before'],B,f['path']) and matches(f['actual_after'],T,f['path']) and f['approved_patch_sha256']==origapproval['exact_original_patch_sha256'][f['path']]
    origchecks.append({'path':f['path'],'clause_count':f['clauses_applied'],'approved_before_after_match':ok})
check('five original scope approvals preserved and exact after identities',len(origchecks)==5 and sum(x['clause_count'] for x in origchecks)==30 and all(x['approved_before_after_match'] for x in origchecks) and not origapproval['correctness_approval'],origchecks)
origproposal=load(C,scope['five_original_scope_proposal']['path']);exact_originals=[]
for f in origproposal['files']:
    before=data(B,f['path']).decode();after=before;ok=True
    for clause in f['clauses']:
        ok=ok and after.count(clause['before_text'])==1
        after=after.replace(clause['before_text'],clause['intended_after_text'],1)
    ok=ok and after.encode()==data(T,f['path']) and sha(data(C,f['complete_diff_path']))==f['complete_diff_sha256'] and f['complete_diff_sha256']==origapproval['exact_original_patch_sha256'][f['path']] and matches(f['intended_after'],T,f['path'])
    exact_originals.append({'path':f['path'],'exact_whole_document_from_approved_text_substitutions':ok,'clause_count':len(f['clauses']),'approved_patch_sha256':f['complete_diff_sha256']})
check('all 30 approved original substitutions independently reconstruct actual bytes',len(exact_originals)==5 and all(x['exact_whole_document_from_approved_text_substitutions'] for x in exact_originals),exact_originals)

def table_rows(raw):
    rows={}
    for line in raw.decode().splitlines(keepends=True):
        if line.startswith('|'):
            cells=[x.strip() for x in line.split('|')]
            if len(cells)>1 and re.fullmatch(r'[A-Z]+-?\d+[a-z]?',cells[1]):
                if cells[1] in rows:raise ValueError('duplicate '+cells[1])
                rows[cells[1]]=line.encode()
    return rows
catalog=[]
for path,d in counts['catalog_counts'].items():
    old=table_rows(data(B,path));new=table_rows(data(T,path))
    added=sorted(set(new)-set(old));changed=sorted(k for k in old if k in new and old[k]!=new[k])
    ok=len(old)==d['before'] and len(new)==d['after'] and set(added)==set(d['added_ids']) and set(changed)==set(d['changed_old_ids']) and set(old)<=set(new)
    catalog.append({'path':path,'before':len(old),'after':len(new),'added':added,'changed_old':changed,'pass':ok})
check('whole two catalog counts and all changed IDs reconstructed',all(x['pass'] for x in catalog),catalog)
protected=[]
for x in counts['protected_whole_sections']:
    def section(c):
        text=data(c,x['path']).decode();start=text.index(x['heading']);end=text.find('\n## ',start+1)
        return text[start:end+1 if end>=0 else len(text)].encode()
    old=section(B);cur=section(T)
    protected.append({'path':x['path'],'heading':x['heading'],'sha256':sha(cur),'bytes':len(cur),'pass':old==cur and sha(cur)==x['sha256'] and len(cur)==x['bytes']})
check('all ten whole protected sections unchanged',all(x['pass'] for x in protected),protected)
hp='deliverables/final-specification-set/test-catalog/creature-rpg-wp18-20-24-25-26.md'
oldhp=table_rows(data(B,hp));curhp=table_rows(data(T,hp))
check('HP24-31 exact protected bytes unchanged',all(oldhp['HP-'+str(n)]==curhp['HP-'+str(n)] for n in range(24,32)),{'ids':['HP-'+str(n) for n in range(24,32)],'catalog_current':identity(T,hp),'static_not_executed':True})
newrows=[]
for x in counts['new_static_designs_not_executed']:
    row=table_rows(data(T,x['path']))[x['id']]
    newrows.append({'path':x['path'],'id':x['id'],'pass':len(row)==x['bytes'] and sha(row)==x['sha256'] and data(T,x['path']).splitlines(keepends=True)[x['line']-1]==row})
check('all 24 new static row hashes/line locators',len(newrows)==24 and all(x['pass'] for x in newrows),newrows)

# Public ledgers: preserve all 150 earlier raw rows; append exactly 20 candidate-
# scoped pending rows. Canonical closure and B09 acceptance remain zero.
ledger_audits=[]
for p in ['review/remediation/20261003-prepare/approval-ledger.tsv','review/remediation/20261003-prepare/traceability-successor.tsv']:
    old=data(B,p);cur=data(T,p)
    oldrows=list(csv.DictReader(io.StringIO(old.decode()),delimiter='\t'));rows=list(csv.DictReader(io.StringIO(cur.decode()),delimiter='\t'))
    new=[x for x in rows if x['candidate_commit']==C]
    prior=[x for x in rows if x['candidate_commit']!=C]
    # Stable row order and bytes, even though updated header comments are permitted.
    priorraw=[x for x in cur.splitlines(keepends=True)[1:] if C.encode() not in x]
    ok=len(oldrows)==150 and prior==oldrows and priorraw==old.splitlines(keepends=True)[1:] and len(new)==20 and len(rows)==170 and all(x['canonical_state']=='OPEN' for x in new) and {x['finding_id'] for x in new}=={x['id'] for x in fr['dispositions']}
    if 'approval-ledger' in p:ok=ok and all(x['integration_verdict']=='NOT_REVIEWED_PENDING_FIVE_ULTRA_STANDARD' and x['downstream_gate']=='BLOCKED' and x['candidate_verdict']=='PASS_SCOPED' for x in new)
    else:ok=ok and all('PENDING_FULL_R09_AND_SEPARATE_AFFECTED_B04_B05_B07_B08_EXACT_ACTUAL_ULTRA_THEN_PARENT_C'==x['integration_gate'] for x in new)
    ledger_audits.append({'path':p,'prior_rows':len(prior),'new_candidate_rows':len(new),'total':len(rows),'prior_raw_preserved':priorraw==old.splitlines(keepends=True)[1:],'pass':ok,'B013':next(x for x in new if x['finding_id']=='GIR-FD82-B013')})
check('both public ledgers preserve 150 accepted rows and add 20 pending',all(x['pass'] for x in ledger_audits),[{k:v for k,v in x.items() if k!='B013'} for x in ledger_audits])
save('public-and-control-audit.json',{'ledgers':ledger_audits,'catalogs':catalog,'protected_sections':protected,'WP20_scope':wp20_checks,'other_original_scope':origchecks})
original=load(O,fr['fixed_original_findings_file']['path']);acceptance=load(P,fr['fixed_approved_acceptance_file']['path'])
origmap={x['id']:x for x in original}
projection=[]
for x in fr['dispositions']:
    source=origmap[x['id']];approved=acceptance[x['id']]
    fields=x['complete_current_control_fields'];acc=x['complete_minimum_acceptance_fields']
    # compare source objects rather than a previous reviewer verdict
    ok=all(v==source.get(k) for k,v in fields.items()) and all(v==approved.get(k) for k,v in acc.items())
    projection.append({'id':x['id'],'control_fields_exact':all(v==source.get(k) for k,v in fields.items()),'acceptance_fields_exact':all(v==approved.get(k) for k,v in acc.items()),'pass':ok})
check('all 20 complete current qualification/acceptance projections',all(x['pass'] for x in projection),projection)
b013=next(x for x in fr['dispositions'] if x['id']=='GIR-FD82-B013')
save('B013-current-controls.json',{'original_file':identity(O,fr['fixed_original_findings_file']['path']),'approved_acceptance_file':identity(P,fr['fixed_approved_acceptance_file']['path']),'current_actual_registration':identity(T,STAGE+'finding-registration.json'),'current_control_fields':b013['complete_current_control_fields'],'minimum_acceptance_fields':b013['complete_minimum_acceptance_fields'],'projection_matches_fixed_controls':next(x for x in projection if x['id']=='GIR-FD82-B013')['pass'],'public_B013_rows':[x['B013'] for x in ledger_audits],'canonical_state':'OPEN','canonical_closure':False})
canonical_index_path='review/global-independent-review/2026-10-03-fd82a639/root/remediation-index.tsv'
canonical_rows=list(csv.DictReader(io.StringIO(data(O,canonical_index_path).decode()),delimiter='\t'))
check('canonical report remains fixed external history and 229 canonical roots OPEN',matches(fr['fixed_original_findings_file'],O) and all(not p.startswith('review/global-independent-review/') for _,p in diff_names(B,T)) and len(canonical_rows)==229 and all(x['status']=='OPEN_NOT_EDITED_IN_THIS_REVIEW' for x in canonical_rows),{'fixed_total_objects':len(original),'canonical_index':identity(O,canonical_index_path),'canonical_OPEN':len(canonical_rows),'original_report_fixed_commit':O,'not_rebound_to_actual_tree':True,'original_object_semantic_status_not_used_as_closure_state':True})
check('current 20/13 contributions and zero accepted B09, 5 independent actual gates',fr['contribution_count']==20 and fr['primary_count']==13 and sum(x['B09_primary'] for x in fr['dispositions'])==13 and m['accepted_B09_contributions']==0 and len(m['actual_gates'])==5 and m['parent_C']=='NOT_PERFORMED',{'actual_gates':m['actual_gates'],'parent_C':m['parent_C'],'accepted_B09':m['accepted_B09_contributions']})

hashrows=list(csv.DictReader(io.StringIO(data(T,STAGE+'current-hashes.tsv').decode()),delimiter='\t'))
check('18 current TSV hash snapshots all resolve at actual',len(hashrows)==18 and all(matches({**x,'bytes':int(x['bytes'])},T) for x in hashrows),{'rows':len(hashrows),'paths':[x['path'] for x in hashrows]})
narrative=[]
for p in sorted(public):
    if not p.endswith('.md'):continue
    raw=git('diff','--no-ext-diff','--no-textconv','--no-renames','--unified=0',C,T,'--',p).decode()
    dels=[l[1:] for l in raw.splitlines() if l.startswith('-') and not l.startswith('---')]
    current=data(T,p).decode()
    ok=('B04/B05/B07/B08' in current and '同一最终actual SHA' in current and 'B14' in current)
    if p.endswith('test-catalog/README.md'):
        ok=ok and len(dels)==2 and all(l.startswith('| [') for l in dels) and '139→159' in current and '136→140' in current
    else:ok=ok and not dels and 'B09-G-O01' in current and 'B09接受贡献0' in current and '229 OPEN／0 CLOSED' in current
    narrative.append({'path':p,'deleted_lines':len(dels),'historical_content_preserved_except_two_catalog_index_rows':ok,'pass':ok})
check('all eight public narratives preserve history and pending actual gates',len(narrative)==8 and all(x['pass'] for x in narrative),narrative)
dep=stage['downstream-dependency-assessment.json'];b14=dep['B14'];serial=dep['B09_B14_serialization']
reads14={x['path'] for x in b14['all72_current_assessment_inputs']};writes14={x['path'] for x in b14['allowed6_write_input_versions']};reads09={x['path'] for x in readers['readers']}
cross09=norm&reads14;cross14=writes14&reads09;ww=norm&writes14
check('B14 72 reads / 6 writes and six cross dependencies reconstructed',len(reads14)==72 and len(writes14)==6 and cross09==set(serial['B09_writes_B14_reads']) and cross14==set(serial['B14_writes_B09_reads']) and not ww and len(cross09|cross14)==6 and serial['shared_control_IDs']==['GIR-FD82-003'] and not serial['semantic_independence'] and not b14['formal_writer_authorized'] and dep['tasks_dispatched']==0 and dep['parallel_formal_writers_authorized']==0,{'B09_writes_B14_reads':sorted(cross09),'B14_writes_B09_reads':sorted(cross14),'write_write':sorted(ww),'B14_status':b14['status'],'after_C_rule':b14['after_C_rule']})
residuals=dep['existing_cross_owner_residuals'];others=dep['other_readers']
check('B16/B17 and global residuals retained, no owner substitution',{'GIR-FD82-A048','GIR-FD82-C003','GIR-FD82-D023'}<={x['id'] for x in residuals} and any(x['owner']=='B17' and x['disposition']=='AFFECTED_PENDING_OWNER' for x in others) and any('B14/B15/B21' in x for x in dep['global_and_domain_residuals']),{'existing_residuals':residuals,'B17':[x for x in others if x['owner']=='B17'],'global':dep['global_and_domain_residuals']})
oldreport=PREFIX+'review-round-1/report.md';oldmachine=PREFIX+'review-round-1/contribution-review.json';oldcommit='d6b1c1d7af3498321c779d38a8cc3edbabdefd77'
oldjudgment=next(x for x in load(oldcommit,oldmachine)['contributions'] if x['id']=='GIR-FD82-B013')['independent_judgment']
obs=next(x for x in scope['report_wording_observations'] if x['id']=='B09-G-O01')
check('O01 historical erroneous proof preserved and observation explicit',data(oldcommit,oldreport)==data(T,oldreport) and data(oldcommit,oldmachine)==data(T,oldmachine) and 'restored to X' in oldjudgment and 'later receive Y' in oldjudgment and 'two restoration passes' in data(T,oldreport).decode() and obs['canonical_finding_added'] is False and obs['formal_edit'] is False and obs['report_edit'] is False,{'historical_report':identity(oldcommit,oldreport),'historical_machine':identity(oldcommit,oldmachine),'current_observation':obs,'current_independent_resolution':'successor erratum; boxA=Y, liveB=nil, single held-item restoration pass; full R09 actual gate still required'})
save('dependency-and-current-public-readings.json',{'actual':T,'narrative_audit':narrative,'current_hash_TSV_rows':hashrows,'B14_serialization_recomputed':{'B09_writes_B14_reads':sorted(cross09),'B14_writes_B09_reads':sorted(cross14),'write_write':sorted(ww),'shared_root':['GIR-FD82-003'],'rule':b14['after_C_rule']},'existing_cross_residuals':residuals,'other_reader_residuals':others,'global_residuals':dep['global_and_domain_residuals'],'actual_gates':m['actual_gates'],'parent_C':'NOT_PERFORMED'})

# Reference checkout identity and fresh source reading log. This only hashes text;
# no Ruby/game/compile/behavioral code is evaluated.
reference_reads=[
('Data/Scripts/012_Overworld/002_Battle triggering/001_Overworld_BattleStarting.rb',[[171,201],[306,329],[608,651],[713,748]],'partner eligibility/merged shared identities; external heal and current-item/world consumers'),
('Data/Scripts/011_Battle/001_Battle/001_Battle.rb',[[119,159],[303,305]],'battle parties and mutable restoration records; terminal participation reader'),
('Data/Scripts/011_Battle/007_Other battle code/005_Battle_CatchAndStoreMixin.rb',[[35,85],[137,142],[165,195]],'boxing old identity, shifting player records, appending capture and qualified Shadow permission'),
('Data/Scripts/014_Pokemon/001_Pokemon-related/004_PokemonStorage.rb',[[38,44],[170,175],[231,249]],'storage saves same identity'),
('Data/Scripts/011_Battle/001_Battle/002_Battle_StartAndEnd.rb',[[479,511]],'single normal-terminal restoration pass after reception'),
('Data/Scripts/011_Battle/002_Battler/001_Battle_Battler.rb',[[81,89],[664,672],[709,714]],'persistent item write-through and mutable initial-item accessor'),
('Data/Scripts/011_Battle/002_Battler/006_Battler_AbilityAndItem.rb',[[224,242]],'permanent consumption clears matching restoration record'),
('Data/Scripts/011_Battle/003_Move/011_MoveEffects_Items.rb',[[5,25],[179,188]],'temporary Knock Off, wild-opponent exclusion, permanent acquisition'),
('Data/Scripts/014_Pokemon/001_Pokemon.rb',[[552,599],[274,309],[976,980]],'individual unknown item/mail distinction; heal does not restore item'),
('Data/Scripts/013_Items/003_Item_BattleEffects.rb',[[29,64]],'legal ball gate and Shadow Snag capture path'),
('Data/Scripts/010_Data/002_PBS data/006_Item.rb',[[174,180]],'Snag identity accepts player machine'),
('Data/Scripts/011_Battle/007_Other battle code/004_Battle_Peers.rb',[[5,24],[48,77]],'normal capture storage and caught append restoration registration'),
('Data/Scripts/010_Data/001_Hardcoded data/007_Evolution.rb',[[413,437]],'evolution reads current persistent held item'),
('Data/Scripts/015_Trainers and player/001_Trainer.rb',[[161,168]],'partner player party healing only heals')]
source_log=[]
for p,ranges,purpose in reference_reads:
    raw=git('show',R+':'+p,root=REF);oid=git('rev-parse',R+':'+p,root=REF).decode().strip()
    source_log.append({'source_id':'SRC%02d'%(len(source_log)+1),'path':p,'commit':R,'git_blob':oid,'sha256':sha(raw),'bytes':len(raw),'read_ranges':ranges,'purpose':purpose,'runtime_or_vector_executed':False})
refhead=git('rev-parse','HEAD',root=REF).decode().strip();reftree=git('rev-parse','HEAD^{tree}',root=REF).decode().strip();refstatus=git('status','--porcelain','--untracked-files=all',root=REF).decode()
check('separate reference fixed SHA/tree clean and read only',refhead==R and reftree=='7589c800b61ba13a13040ed0d686979b80a84fd0' and refstatus=='',{'path':str(REF),'head':refhead,'tree':reftree,'status':refstatus,'origin':git('remote','get-url','origin',root=REF).decode().strip()})
save('source-reading-log.json',{'reference':{'outside_project_git':True,'path':str(REF),'commit':refhead,'tree':reftree,'clean':refstatus==''},'fresh_read_entries':source_log,'reading_is_static_only':True,'reference_execution':0,'behavior_vectors_executed':0,'runtime_observations':0,'proven_Demo_chains':0,'unlisted_ranges_unread_this_round':True,'retained_limits_verbatim_from_actual':scope['source_limits'],'retained_unknowns':['U01–U10','G01–G12','AX01–AX20'],'configuration_effective':'UNVERIFIED / Plan A retained'})
save('metadata-check-results.json',{'actual':T,'candidate':C,'predecessor':B,'timestamp_UTC':datetime.now(timezone.utc).isoformat(),'program_mode':'own Git/text/JSON bookkeeping only; no author/reference/reviewer historical program executed','checks':checks,'pass_count':sum(x['pass'] for x in checks),'fail_count':sum(not x['pass'] for x in checks),'independent_semantic_verdict_separate':True})
batch.stdin.close();batch.wait()
print(json.dumps({'checks':len(checks),'passed':sum(x['pass'] for x in checks),'failed':[x['check'] for x in checks if not x['pass']],'out':str(OUT)},ensure_ascii=False))
