#!/usr/bin/env python3
"""Read Git/document identities only. No reference program or oracle execution."""
import difflib
import hashlib
import json
import re
import subprocess
from pathlib import Path

OUT = Path(__file__).resolve().parent
ROOT = OUT.parents[5]
REF = Path('/tmp/R-B06-reference')
BASE = 'ae230e76e9c041f39c28948321d0960804c02388'
CAND = 'b1b09be809822ffa8ab79684589d104ec783095a'
OLD_CAND = '3c5b280b8ffdbcfb93d0410e2195c79e35b8178c'
OLD_EVID = '806c969105f4f2aca916708013ad54f972524d5e'
R1 = 'e12791309ace5458da29fd91c7bed70ac4175700'
R1DIR = 'review/remediation/20261003-prepare/batches/B06/review-stage-1-round-1/'
REPAIR = 'review/remediation/20261003-prepare/batches/B06/author-stage-1-repair-1/'
EVID = '5059760ea678e3c21ce01a87a13317b5b6cc2e1d'
ORIG = '93e10babe0b9c9ef8b3f5277754541b447beeeb4'
PLAN = '41fffb540c6483f5296ea0d33b789b75180d27ed'
REFSHA = '8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
AUTHOR = 'review/remediation/20261003-prepare/batches/B06/author-stage-1/'
IDS = ['GIR-FD82-' + x for x in ['A032','A033','A035','A036','A037','A038','C120']]
FINAL = 'deliverables/final-specification-set/'
FORMAL = [FINAL+'creature-rpg/'+x+'.md' for x in
          ['wp24-player-trainers-partners','wp25-party-and-storage','wp27-bag-and-item-storage']]
FORMAL += [FINAL+'test-catalog/'+x+'.md' for x in
           ['creature-rpg-wp18-20-24-25-26','creature-rpg-wp27-28-29-30-33']]
FORMAL += ['specs/creature-rpg/'+x+'.md' for x in
           ['wp24-player-trainers-partners','wp25-party-and-storage','wp27-bag-and-item-storage']]

def git(*args, cwd=ROOT):
    return subprocess.check_output(['git', *args], cwd=cwd)

def blob(commit, path):
    return git('show', commit+':'+path)

def sha(data):
    return hashlib.sha256(data).hexdigest()

def canon(obj):
    return sha(json.dumps(obj, ensure_ascii=False, sort_keys=True, separators=(',', ':')).encode())

def dump(name, obj):
    (OUT/name).write_text(json.dumps(obj, ensure_ascii=False, indent=2)+'\n')

def identity(commit, path):
    data = blob(commit, path)
    return {'commit':commit, 'path':path,
            'git_blob':git('rev-parse', commit+':'+path).decode().strip(),
            'sha256':sha(data), 'bytes':len(data)}

def section(data, heading):
    lines = data.decode().splitlines(keepends=True)
    start = next(i for i,s in enumerate(lines) if s.startswith(heading))
    level = len(lines[start].split(' ')[0])
    end = next((i for i in range(start+1,len(lines))
                if re.match(r'^#{1,'+str(level)+r'} ',lines[i])),len(lines))
    return ''.join(lines[start:end]).encode()

def rows(data):
    result = {}
    for n,s in enumerate(data.decode().splitlines(keepends=True),1):
        m = re.match(r'^\| ([A-Z]+-\d+) \|',s)
        if m:
            assert m[1] not in result
            result[m[1]] = (n,s)
    return result

assert git('rev-parse',OLD_CAND+'^').decode().strip() == BASE
assert git('rev-parse',CAND+'^').decode().strip() == OLD_EVID
assert git('rev-parse',EVID+'^').decode().strip() == CAND
assert git('diff','--name-only',CAND,EVID).decode().splitlines() == [REPAIR+'candidate-manifest.json']
changed = git('diff','--name-only',BASE,CAND).decode().splitlines()
assert {p for p in changed if not (p.startswith(AUTHOR) or p.startswith(REPAIR))} == set(FORMAL)
git('diff','--check',BASE,CAND)
manifest = json.loads(blob(EVID,REPAIR+'candidate-manifest.json'))
formal_ids = [identity(CAND,p) for p in FORMAL]
for item in manifest['formal_file_identities']:
    own = identity(CAND,item['path'])
    assert all(own[k] == item[k] for k in ['git_blob','sha256','bytes'])
    assert blob(CAND,item['path']) == blob(EVID,item['path'])
author_ids=[]
historical_items=json.loads(blob(CAND,REPAIR+'input-freeze.json'))['immutable_prior_author_artifacts']
assert len(historical_items)==15
for item in manifest['frozen_candidate_successor_author_artifacts'] + historical_items:
    own=identity(CAND,item['path'])
    assert all(own[k]==item[k] for k in ['git_blob','sha256','bytes'])
    assert blob(CAND,item['path']) == blob(EVID,item['path'])
    author_ids.append(own)
patches=json.loads(blob(CAND,REPAIR+'patch-identities.json'))['patches']
patch_checks=[]
for x in patches:
    actual=git('diff','--binary','--unified=0',x['base_commit'],CAND,'--',*x['paths'])
    assert actual==blob(CAND,x['path']) and sha(actual)==x['sha256'] and len(actual)==x['bytes']
    patch_checks.append(identity(CAND,x['path']))

original_path='review/global-independent-review/2026-10-03-fd82a639/findings.json'
accept_path='review/remediation-20261003-prepare/finding-acceptance.json'
original=json.loads(blob(ORIG,original_path))
accept=json.loads(blob(PLAN,accept_path))
objects=[]
author_inputs=json.loads(blob(CAND,AUTHOR+'finding-inputs.json'))['objects']
for ident in IDS:
    obj=next(x for x in original if x['id']==ident)
    a=next(x for x in author_inputs if x['id']==ident)
    assert a['original_object']==obj and a['approved_acceptance_object']==accept[ident]
    assert a['original_sha256']==canon(obj) and a['acceptance_sha256']==canon(accept[ident])
    objects.append({'id':ident,'original_object':obj,'approved_acceptance_object':accept[ident],
                    'original_sha256':canon(obj),'acceptance_sha256':canon(accept[ident])})
dump('finding-inputs.json',{'original_report':identity(ORIG,original_path),
                          'approved_acceptance':identity(PLAN,accept_path),'objects':objects})

# The whitelist is an independently recorded authorization, not an author's assertion.
allowed={FORMAL[0]:{77,207,216,237},FORMAL[1]:{79,89,185},FORMAL[2]:{102,158},
         FORMAL[5]:{76,203},FORMAL[6]:{77,85,211},FORMAL[7]:{98}}
clause_checks=[]
for p,expected in allowed.items():
    old=blob(BASE,p).decode().splitlines(keepends=True)
    new=blob(CAND,p).decode().splitlines(keepends=True)
    seen=set()
    for kind,i,j,m,n in difflib.SequenceMatcher(a=old,b=new,autojunk=False).get_opcodes():
        if kind=='equal':continue
        assert kind=='replace' and j==i+1 and i+1 in expected,(p,kind,i,j)
        seen.add(i+1)
        clause_checks.append({'path':p,'base_line':i+1,'candidate_lines':[m+1,n],
                              'before_sha256':sha(old[i].encode()),
                              'after_sha256':sha(''.join(new[m:n]).encode())})
    assert seen==expected

catalog_checks=[]
allocation={'A032':['PT-29','PT-30','PT-31'],'A033':['PT-32','PT-33','PT-34'],
            'A035':['PS-29','PS-30','PS-37','PS-38'],'A036':['PS-11','PS-31'],
            'A037':['AQ-04','AQ-36'],'A038':['BG-30','BG-31'],
            'C120':['PS-32','PS-33','PS-34','PS-35','PS-36','PS-39','PS-40','PS-41','PS-42']}
test_ids=[]
for p,groups,amended in [(FORMAL[3],{'PT':(28,34),'PS':(28,42),'AQ':(35,36)}, {'PS-11','AQ-04'}),
                         (FORMAL[4],{'BG':(29,31)},set())]:
    old=blob(BASE,p); new=blob(CAND,p); r0=rows(old);r1=rows(new)
    added={f'{g}-{i:02d}' for g,(a,b) in groups.items() for i in range(a+1,b+1)}
    assert set(r1)-set(r0)==added and not set(r0)-set(r1)
    assert {k for k in r0 if r0[k][1]!=r1[k][1]}==amended
    normalized=new.decode()
    for k in added:normalized=normalized.replace(r1[k][1],'')
    for k in amended:normalized=normalized.replace(r1[k][1],r0[k][1])
    for g,(a,b) in groups.items():
        normalized=normalized.replace(f'（{g}-01～{g}-{b:02d}）',f'（{g}-01～{g}-{a:02d}）')
    assert normalized.encode()==old
    catalog_checks.append({'path':p,'added':sorted(added),'amended':sorted(amended),
                           'all_other_rows_and_text_identical':True})
    for ident,cases in allocation.items():
        for k in cases:
            if k in r1:
                test_ids.append({'finding_id':'GIR-FD82-'+ident,'test_id':k,'path':p,
                                 'line':r1[k][0],'sha256':sha(r1[k][1].encode())})
assert len(test_ids)==25

pres=json.loads(blob(CAND,AUTHOR+'preservation-freeze.json'))
protected=[]
for x in pres['protected_whole_files']:
    assert blob(BASE,x['path'])==blob(CAND,x['path'])
    assert sha(blob(CAND,x['path']))==x['sha256']
    protected.append(identity(CAND,x['path']))
section_ids=[]
for x in pres['protected_sections']:
    before=section(blob(BASE,x['path']),x['heading_prefix'])
    after=section(blob(CAND,x['path']),x['heading_prefix'])
    assert before==after and sha(after)==x['sha256']
    section_ids.append({'path':x['path'],'heading':x['heading_prefix'],'sha256':sha(after)})
for x in pres['protected_test_rows']:
    assert rows(blob(BASE,x['path']))[x['test_id']][1]==rows(blob(CAND,x['path']))[x['test_id']][1]
    assert sha(rows(blob(CAND,x['path']))[x['test_id']][1].encode())==x['sha256']

freeze=json.loads(blob(CAND,AUTHOR+'input-freeze.json'))
for x in freeze['B05_handoff_identity_checks']+freeze['plan_controls']+freeze['formal_baseline']:
    assert sha(blob(x['commit'],x['path']))==x['sha256']
for x in freeze['plan_controls']:
    assert blob(BASE,x['path'])==blob(CAND,x['path'])==blob(PLAN,x['path'])
for p in git('ls-tree','-r','--name-only',BASE,'review/remediation-20261003-prepare').decode().splitlines():
    assert blob(BASE,p)==blob(CAND,p)

batches=json.loads(blob(PLAN,'review/remediation-20261003-prepare/batches.json'))
b3=next(x for x in batches if x['id']=='B03'); b6=next(x for x in batches if x['id']=='B06')
intersections={'B03_write_B06_write':sorted(set(b3['write_paths'])&set(FORMAL)),
               'B03_write_B06_read':sorted(set(b3['write_paths'])&set(b6['read_paths'])),
               'B06_write_B03_read':sorted(set(FORMAL)&set(b3['read_paths']))}
assert not intersections['B03_write_B06_write'] and not intersections['B06_write_B03_read']
assert intersections['B03_write_B06_read']==[FINAL+'test-catalog/engine-overworld-wp11-15-59-60.md']
ancestors=set(git('rev-list',CAND).decode().splitlines())
unaccepted=['f8d0599de751299b7535242a654de7919caeb88d','cdb689ba7f20ec8699329015fc5bdd520ca3a037']
assert not set(unaccepted)&ancestors

assert git('rev-parse','HEAD',cwd=REF).decode().strip()==REFSHA
assert git('rev-parse','HEAD^{tree}',cwd=REF).decode().strip()=='7589c800b61ba13a13040ed0d686979b80a84fd0'
assert not git('status','--porcelain=v1',cwd=REF)
read_ranges={
 'Data/Scripts/019_Utilities/001_Utilities.rb':[(239,283)],
 'Data/Scripts/001_Settings.rb':[(45,62),(220,225)],
 'Data/Scripts/015_Trainers and player/002_Trainer_LoadAndNew.rb':[(1,124)],
 'Data/Scripts/014_Pokemon/001_Pokemon-related/004_PokemonStorage.rb':[(63,76),(101,117),(148,209),(231,259)],
 'Data/Scripts/015_Trainers and player/001_Trainer.rb':[(57,83)],
 'Data/Scripts/019_Utilities/002_Utilities_Pokemon.rb':[(1,100)],
 'Data/Scripts/016_UI/017_UI_PokemonStorage.rb':[(315,332),(378,396),(424,435),(593,613),(1020,1062),(1610,1665),(1705,1722)],
 'Data/Scripts/016_UI/007_UI_Bag.rb':[(479,520)],
 'Data/Scripts/010_Data/002_PBS data/006_Item.rb':[(189,197)],
 'PBS/items.txt':[(2942,2950)],
 'Data/Scripts/015_Trainers and player/004_Player.rb':[(35,75)],
 'Data/Scripts/014_Pokemon/001_Pokemon.rb':[(670,695),(1150,1227)],
 'Data/Scripts/012_Overworld/001_Overworld.rb':[(635,656)],
 'Data/Scripts/007_Objects and windows/011_Messages.rb':[(1,15)],
 'Data/Scripts/003_Game processing/004_Interpreter_Commands.rb':[(120,147)],
 'Data/Scripts/004_Game classes/008_Game_Player.rb':[(90,145)],
 'Data/Scripts/015_Trainers and player/005_Player_Pokedex.rb':[(35,55),(75,130),(140,163),(185,220)],
}
readings=[]
for p,ranges in read_ranges.items():
    data=(REF/p).read_bytes(); lines=data.splitlines(keepends=True)
    assert data==git('show',REFSHA+':'+p,cwd=REF)
    spans=[]
    for start,end in ranges:
        assert 1<=start<=end<=len(lines),(p,start,end,len(lines))
        spans.append({'start':start,'end':end,'sha256':sha(b''.join(lines[start-1:end]))})
    readings.append({'path':p,'commit':REFSHA,'git_blob':git('rev-parse',REFSHA+':'+p,cwd=REF).decode().strip(),
                     'sha256':sha(data),'actual_lines':len(lines),'read_ranges':spans})
dump('source-reading-log.json',{'reference_commit':REFSHA,'tree':'7589c800b61ba13a13040ed0d686979b80a84fd0',
     'separate_git':True,'status_porcelain':'','method':'static text only; navigation is not branch coverage',
     'reference_execution':0,'runtime_observations':0,'proven_demo_chains':0,'readings':readings})

# Verify repair boundaries independently against its actual parent; do not trust scope.json.
repair_paths=[FORMAL[1],FORMAL[3],FORMAL[6]]
assert {p for p in git('diff','--name-only',OLD_EVID,CAND).decode().splitlines()
        if not p.startswith(REPAIR)}==set(repair_paths)
repair_bounds=[]
for p,expected in {FORMAL[1]:{94,201},FORMAL[6]:{77}}.items():
    old=blob(OLD_EVID,p).decode().splitlines(keepends=True)
    new=blob(CAND,p).decode().splitlines(keepends=True)
    seen=set(); insertions=0
    for kind,i,j,m,n in difflib.SequenceMatcher(a=old,b=new,autojunk=False).get_opcodes():
        if kind=='equal':continue
        if kind=='insert':
            assert p==FORMAL[1] and i==95 and n-m==2
            insertions+=1
        else:
            assert kind=='replace' and j==i+1 and i+1 in expected,(p,kind,i,j)
            seen.add(i+1)
        repair_bounds.append({'path':p,'kind':kind,'parent_lines':[i+1,j],
            'candidate_lines':[m+1,n],'before_sha256':sha(''.join(old[i:j]).encode()),
            'after_sha256':sha(''.join(new[m:n]).encode())})
    assert seen==expected and insertions==(1 if p==FORMAL[1] else 0)
for p in set(FORMAL)-set(repair_paths):
    assert blob(OLD_EVID,p)==blob(CAND,p)
oldrows=rows(blob(OLD_EVID,FORMAL[3]));newrows=rows(blob(CAND,FORMAL[3]))
newids={'PS-39','PS-40','PS-41','PS-42'}
assert set(newrows)-set(oldrows)==newids and not set(oldrows)-set(newrows)
assert all(oldrows[k][1]==newrows[k][1] for k in oldrows)
normalized=blob(CAND,FORMAL[3]).decode()
for k in newids:normalized=normalized.replace(newrows[k][1],'')
assert normalized.replace('（PS-01～PS-42）','（PS-01～PS-38）').encode()==blob(OLD_EVID,FORMAL[3])
r1inputs=json.loads(blob(R1,R1DIR+'input-and-preservation.json'))
prior21=[]
for x in r1inputs['stage_row_identities']:
    row=rows(blob(CAND,x['path']))[x['test_id']]
    assert sha(row[1].encode())==x['sha256']
    prior21.append(dict(x,candidate_line=row[0],same_bytes=True))
assert len(prior21)==21
for p in git('ls-tree','-r','--name-only',OLD_EVID,AUTHOR).decode().splitlines():
    assert blob(OLD_EVID,p)==blob(CAND,p)
r1_artifacts=[]
for p in git('ls-tree','-r','--name-only',R1,R1DIR).decode().splitlines():
    r1_artifacts.append(identity(R1,p))
assert len(r1_artifacts)==11
receipt=json.loads(blob(CAND,REPAIR+'review-reading-receipt.json'))
for x in receipt['review_artifacts']:
    assert sha(blob(R1,x['path']))==x['sha256']
assert json.loads(blob(CAND,REPAIR+'review-new-findings-inputs.json'))['complete_new_findings_object']==json.loads(blob(R1,R1DIR+'new-findings.json'))
assert R1 not in ancestors  # Separate review branch is retained; not silently merged.
first_sha='7a118f68902ae215416772c21fa0e604e0d9a7cccba911ef17781597ceb4be7c'
assert sha((OUT/'independent-first-evidence.md').read_bytes())==first_sha

# Execute only the inspected 13-line document helper; never author full verifier/reference.
helper_path=REPAIR+'document_integrity.py'
helper_namespace={}
exec(compile(blob(CAND,helper_path),helper_path,'exec'),helper_namespace)
checked=helper_namespace['checked_range_sha256']
author_source=json.loads(blob(CAND,REPAIR+'source-reading-log.json'))
author_spans=[]
for x in author_source['readings']:
    data=(REF/x['path']).read_bytes();lines=data.splitlines(keepends=True)
    assert data==git('show',REFSHA+':'+x['path'],cwd=REF)
    assert sha(data)==x['sha256'] and len(lines)==x['actual_line_count']
    for span in x['read_ranges']:
        assert type(span['start']) is int and type(span['end']) is int
        assert 1<=span['start']<=span['end']<=len(lines),(x['path'],span,len(lines))
        expected=sha(b''.join(lines[span['start']-1:span['end']]))
        assert expected==span['range_sha256']==checked(data,span['start'],span['end'])
        author_spans.append({'reading_id':x['reading_id'],'path':x['path'],
            'start':span['start'],'end':span['end'],'actual_lines':len(lines),'sha256':expected})
assert len(author_spans)==17
trainer=next(x for x in author_source['readings'] if x['reading_id']=='B06-SR-03')
data=(REF/trainer['path']).read_bytes()
assert trainer['actual_line_count']==124
assert trainer['read_ranges']==[{'start':1,'end':124,'range_sha256':sha(data)}]
old_source=json.loads(blob(OLD_EVID,AUTHOR+'source-reading-log.json'))
old_trainer=next(x for x in old_source['readings'] if x['reading_id']=='B06-SR-03')
assert old_trainer['read_ranges'][0]['end']==135
valid=[]
for a,b in [(1,124),(124,124)]:
    expected=sha(b''.join(data.splitlines(keepends=True)[a-1:b]))
    assert checked(data,a,b)==expected
    valid.append({'start':a,'end':b,'sha256':expected,'accepted':True})
invalid=[]
for a,b in [(1,135),(125,125),(0,124),(124,1),(1,0)]:
    calls=[]
    def forbidden_hash(chunk):
        calls.append(True)
        raise AssertionError('invalid range reached hash')
    try:
        checked(data,a,b,hash_bytes=forbidden_hash)
    except ValueError:
        assert not calls
        invalid.append({'start':a,'end':b,'rejected_before_hash':True,'hash_calls':0})
    else:raise AssertionError(('invalid range accepted',a,b))
claimed_ranges=json.loads(blob(CAND,REPAIR+'source-range-validation.json'))
assert claimed_ranges['checked_actual_source_spans']==author_spans
assert [(x['start'],x['end']) for x in claimed_ranges['document_range_rejection_cases']]==[(x['start'],x['end']) for x in invalid]
assert all(x['rejected_before_hash'] and x['hash_function_calls']==0 for x in claimed_ranges['document_range_rejection_cases'])
responses=json.loads(blob(CAND,REPAIR+'finding-responses.json'))
assert {x['id'] for x in responses['all_seven_stage_responses']}==set(IDS)
assert len(responses['all_seven_stage_responses'])==7
for x in responses['all_seven_stage_responses']:
    obj=next(y for y in objects if y['id']==x['id'])
    assert x['original_object_sha256']==obj['original_sha256']
    assert x['acceptance_object_sha256']==obj['acceptance_sha256']
    assert x['current_qualifications_inherited']==obj['original_object']['current_qualifications']
    assert x['new_independent_verdict'] is None and not x['close']
    for t in x['test_cases']:
        n,row=rows(blob(CAND,t['path']))[t['test_id']]
        assert n==t['candidate_line'] and sha(row.encode())==t['row_sha256']
        columns=row.strip().strip('|').split('|')
        assert columns[1].strip()==t['input_and_premises']
        assert columns[2].strip()==t['static_expected_result']
assert sum(len(x['test_cases']) for x in responses['all_seven_stage_responses'])==25
dump('source-range-validation.json',{'method':'Only inspected document helper; Git/document bytes. No reference program execution.',
    'helper_identity':identity(CAND,helper_path),'trainer_actual_lines':124,'correct_successor':[1,124],
    'historical_range_preserved':[1,135],'author_valid_spans_checked':author_spans,
    'valid_cases':valid,'invalid_cases':invalid,'document_helper_fixture_checks_executed':7,
    'reference_execution':0,'behavioral_vectors_executed':0})
dump('input-and-preservation.json',{'base':BASE,'candidate':CAND,'author_evidence':EVID,
    'parent':OLD_EVID,'previous_candidate':OLD_CAND,'prior_independent_report':R1,
    'commits':{s:git('rev-parse',s+'^{tree}').decode().strip() for s in [BASE,CAND,EVID,OLD_EVID,OLD_CAND,R1,ORIG,PLAN]},
    'first_evidence_sha256':first_sha,
    'formal_identities':formal_ids,'frozen_author_artifacts':author_ids,'patch_identities':patch_checks,
    'full_stage_clause_bounds':clause_checks,'repair_clause_bounds':repair_bounds,
    'repair_formal_paths':repair_paths,'catalog_checks':catalog_checks,'stage_row_identities':test_ids,
    'prior_21_rows_same_bytes':prior21,'protected_sections':section_ids,'protected_whole_files':protected,
    'prior_independent_report_artifacts':r1_artifacts,'prior_report_is_ancestor':False,
    'historical_author_15_artifacts_unchanged':True,
    'B05_handoff_baseline_identity_count':len(freeze['B05_handoff_identity_checks']),
    'plan_intersections':intersections,'unaccepted_B03_commits_are_ancestors':False,
    'semantic_isolation_requires_reading':'See report.md dependency matrix; path intersections alone are insufficient.'})
dump('independent-validation.json',{'identity_and_scope_checks':'PASS',
    'semantic_verdict_recorded_by_manual_review_in':'finding-dispositions.json and report.md',
    'candidate':CAND,'author_evidence':EVID,'formal_path_count':8,'repair_formal_path_count':3,
    'original_pairs_checked':7,'static_rows_checked':25,'prior21_same_bytes':True,
    'new_repair_rows':4,'full_stage_new_rows':23,'full_stage_amended_rows':['PS-11','AQ-04'],
    'author_full_script_executed':False,'document_helper_checks_executed':7,
    'author_identity_and_row_claims_match':True,'all_17_successor_source_spans_valid':True,
    'invalid_document_ranges_rejected_before_hash':5,'invalid_range_hash_calls':0,
    'prior_verdicts_transferred':False,'runtime_observations':0,'proven_demo_chains':0,'reference_execution':0,
    'behavioral_vectors_executed':0,'full_B06_ready':False,'integration_accepted':False,
    'finding_closures':0,'public_registry_writes':0})
print('PASS documentation integrity: 8 scoped formal paths; 3 repair paths; 21 byte-preserved + 4 new static vectors.')
print('PASS document helper: 17 bounded spans; 2 positive / 5 rejection fixtures; invalid hash calls 0.')
print('Semantic decision is manual, fixed in report.md; no reference/behavior execution.')

# Cross-check the manually authored disposition artifacts; no behavioral oracle runs.
dispositions=json.loads((OUT/'finding-dispositions.json').read_text())
assert dispositions['candidate']==CAND and dispositions['author_evidence']==EVID
assert dispositions['verdict']=='PASS_SCOPED' and not dispositions['full_B06_ready']
assert len(dispositions['decisions'])==7
assert {x['id'] for x in dispositions['decisions']}==set(IDS)
for x in dispositions['decisions']:
    assert x['candidate_commit']==CAND and x['verdict']=='PASS_SCOPED'
    assert x['fresh_semantic_reread'] and not x['prior_approval_transferred']
    assert not x['close'] and not x['integration_accepted']
    assert x['static_test_rows']==[t for t in test_ids if t['finding_id']==x['id']]
issues=json.loads((OUT/'new-findings.json').read_text())
assert not issues['new_defects']
assert {x['id'] for x in issues['predecessor_issue_dispositions']}=={'B06-S1-R1-N001','B06-S1-R1-N002'}
assert all(x['verdict']=='REPAIR_VERIFIED_SCOPED' and not x['canonical_close'] for x in issues['predecessor_issue_dispositions'])
limits=json.loads((OUT/'model-and-limits.json').read_text())
assert not limits['effective_runtime_configuration_independently_verified']
assert limits['derived_agents']==0 and not limits['configuration_changed']
assert all(limits[k]==0 for k in ['reference_execution','runtime_observations','proven_demo_event_chains','behavioral_vectors_executed','canonical_closures','public_registry_writes'])
print('PASS disposition identities: all seven fresh scoped decisions, N001/N002 successor repairs, no closure/integration claim.')
