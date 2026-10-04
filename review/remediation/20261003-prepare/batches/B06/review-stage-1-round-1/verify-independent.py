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
CAND = '3c5b280b8ffdbcfb93d0410e2195c79e35b8178c'
EVID = '806c969105f4f2aca916708013ad54f972524d5e'
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

assert git('rev-parse',CAND+'^').decode().strip() == BASE
assert git('rev-parse',EVID+'^').decode().strip() == CAND
assert git('diff','--name-only',CAND,EVID).decode().splitlines() == [AUTHOR+'candidate-manifest.json']
changed = git('diff','--name-only',BASE,CAND).decode().splitlines()
assert {p for p in changed if not p.startswith(AUTHOR)} == set(FORMAL)
git('diff','--check',BASE,CAND)
manifest = json.loads(blob(EVID,AUTHOR+'candidate-manifest.json'))
formal_ids = [identity(CAND,p) for p in FORMAL]
for item in manifest['formal_file_identities']:
    own = identity(CAND,item['path'])
    assert all(own[k] == item[k] for k in ['git_blob','sha256','bytes'])
    assert blob(CAND,item['path']) == blob(EVID,item['path'])
author_ids=[]
for item in manifest['frozen_candidate_author_artifacts']:
    own=identity(CAND,item['path'])
    assert all(own[k]==item[k] for k in ['git_blob','sha256','bytes'])
    assert blob(CAND,item['path']) == blob(EVID,item['path'])
    author_ids.append(own)
patches=json.loads(blob(CAND,AUTHOR+'patch-identities.json'))['patches']
patch_checks=[]
for x in patches:
    actual=git('diff','--binary','--unified=0',BASE,CAND,'--',*x['selected_formal_paths'])
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
            'C120':['PS-32','PS-33','PS-34','PS-35','PS-36']}
test_ids=[]
for p,groups,amended in [(FORMAL[3],{'PT':(28,34),'PS':(28,38),'AQ':(35,36)}, {'PS-11','AQ-04'}),
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
assert len(test_ids)==21

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
 'Data/Scripts/019_Utilities/001_Utilities.rb':[(210,295)],
 'Data/Scripts/001_Settings.rb':[(45,62),(220,220),(222,222),(225,225)],
 'Data/Scripts/015_Trainers and player/002_Trainer_LoadAndNew.rb':[(1,124)],
 'Data/Scripts/014_Pokemon/001_Pokemon-related/004_PokemonStorage.rb':[(1,290)],
 'Data/Scripts/015_Trainers and player/001_Trainer.rb':[(1,110)],
 'Data/Scripts/019_Utilities/002_Utilities_Pokemon.rb':[(1,125)],
 'Data/Scripts/016_UI/017_UI_PokemonStorage.rb':[(315,342),(360,445),(565,635),(970,1070),(1610,1665),(1670,1740)],
 'Data/Scripts/016_UI/007_UI_Bag.rb':[(440,540)],
 'Data/Scripts/010_Data/002_PBS data/006_Item.rb':[(180,205)],
 'PBS/items.txt':[(2938,2955)],
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

author_source=json.loads(blob(CAND,AUTHOR+'source-reading-log.json'))
range_errors=[]
for x in author_source['readings']:
    data=(REF/x['path']).read_bytes();lines=data.splitlines(keepends=True)
    assert sha(data)==x['sha256']
    for span in x['read_ranges']:
        assert sha(b''.join(lines[span['start']-1:span['end']]))==span['range_sha256']
        if not 1<=span['start']<=span['end']<=len(lines):
            range_errors.append({'reading_id':x['reading_id'],'path':x['path'],
                'reported_span':[span['start'],span['end']],'actual_lines':len(lines),
                'recorded_hash_equals_truncated_slice':True})
assert len(range_errors)==1 and range_errors[0]['actual_lines']==124
dump('input-and-preservation.json',{'base':BASE,'candidate':CAND,'author_evidence':EVID,
    'commits':{s:git('rev-parse',s+'^{tree}').decode().strip() for s in [BASE,CAND,EVID,ORIG,PLAN]},
    'formal_identities':formal_ids,'frozen_author_artifacts':author_ids,'patch_identities':patch_checks,'clause_bounds':clause_checks,
    'catalog_checks':catalog_checks,'stage_row_identities':test_ids,'protected_sections':section_ids,
    'protected_whole_files':protected,'B05_handoff_baseline_identity_count':len(freeze['B05_handoff_identity_checks']),
    'plan_intersections':intersections,'unaccepted_B03_commits_are_ancestors':False,
    'semantic_isolation_requires_reading':'See report.md dependency matrix; path intersections alone are insufficient.'})
dump('independent-validation.json',{'identity_and_scope_checks':'PASS','semantic_verdict':'REQUEST_CHANGES',
    'candidate':CAND,'formal_path_count':8,'original_pairs_checked':7,'static_rows_checked':21,
    'new_rows':19,'amended_rows':['PS-11','AQ-04'],'author_script_executed':False,
    'author_script_reason':'It binds the author branch/path and overwrites its frozen static-validation.json; checked by independent read-only validator instead.',
    'author_identity_claims_match':True,'author_source_range_errors':range_errors,
    'new_findings':['B06-S1-R1-N001','B06-S1-R1-N002'],
    'runtime_observations':0,'proven_demo_chains':0,'reference_execution':0,
    'full_B06_ready':False,'integration_accepted':False,'finding_closures':0,'public_registry_writes':0})
print('Independent identity/scope checks pass: 8 formal paths, 21 rows, 7 canonical pairs.')
print('Semantic verdict: REQUEST_CHANGES; N001 format boundary and N002 source-range overrun.')
