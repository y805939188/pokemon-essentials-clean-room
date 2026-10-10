import subprocess,json,hashlib,re
from pathlib import Path
r=Path('/workspace/pokemon-essentials-clean-room');a=r/'review/remediation/20261003-prepare/batches/B13/author-draft-1';p=r/'review/remediation/20261003-prepare/batches/B13/candidate-1';base='8e67f780c204d593d89f364f585d2c6c2fe74631'
def git(*args):return subprocess.check_output(['git','-C',str(r),*args])
def ident(d):return {'git_blob':subprocess.check_output(['git','hash-object','--stdin'],input=d,cwd=r).decode().strip(),'sha256':hashlib.sha256(d).hexdigest(),'bytes':len(d)}
c=json.loads((a/'B13-downstream-contract.json').read_text());allowed=c['allowed_formal_write_paths'];own=[str(a.relative_to(r))+'/',str(p.relative_to(r))+'/']
changed=git('diff','--name-only',base).decode().splitlines();untracked=git('ls-files','--others','--exclude-standard').decode().splitlines();assert all(f in allowed or any(f.startswith(d) for d in own) for f in changed+untracked),(changed,untracked);assert len([f for f in changed if f in allowed])==7
# Whole all tracked tree diff is authoritative for protected paths; all original/scope/public/ref/other owner files remain byte-identical.
protected=[f for f in git('ls-tree','-r','--name-only',base).decode().splitlines() if f not in allowed and not any(f.startswith(d) for d in own)];assert not set(protected)&set(changed)
for name in ['B13-downstream-contract.json','original-and-acceptance-controls.json','independent-review-requirements.json','affected-interface-map.json','catalog-locks.json','preparation-reuse-and-input-delta.json']:
 assert (a/name).read_bytes()==Path('/tmp/B13-packet',name).read_bytes(),name
for o in json.loads((a/'formal-output-identities.json').read_text())['records']:assert o['output']==ident((r/o['path']).read_bytes()) and o['input']==ident(git('show',base+':'+o['path']))
proposal=json.loads((a/'original-scope-proposal-1/proposal.json').read_text());assert hashlib.sha256((a/'original-scope-proposal-1/whole.patch').read_bytes()).hexdigest()==proposal['whole_patch_sha256']
for x in proposal['records']:
 assert (r/x['path']).read_bytes()==git('show',base+':'+x['path']),x['path'];after=(a/'original-scope-proposal-1/proposed-after'/x['path']).read_bytes();assert ident(after)=={k:v for k,v in x['proposed_after'].items() if k in ['git_blob','sha256','bytes']}
 subprocess.run(['git','-C',str(r),'apply','--check',str(a/'original-scope-proposal-1/whole.patch')],check=True,capture_output=True)
# Independent static metadata enumerations, never a behavior-vector execution.
cr=r/allowed[-2];lines=cr.read_text().splitlines();secs={};sec=None
for i,l in enumerate(lines):
 if l.startswith('## '):sec=l.split('：')[0][3:]
 if re.match(r'^\| (Q\d+|W\d+\w*|P\d+) \|',l):
  secs.setdefault(sec,[]).append(l.split('|')[1].strip());assert lines[i-1].startswith('|'),('split table',i+1)
assert {k:len(v) for k,v in secs.items()}=={'QC':47,'WS':35,'PA':28,'RC':26};assert len(set(secs['RC']))==26 and 'W22b' in secs['RC']
# Literal key identity and setting/consumer division; unaffected factory and Palace probabilities are exact row comparisons.
appendix=r/allowed[1];old=git('show',base+':'+allowed[1]).decode();new=appendix.read_text();oldfactory=old.split('## 1.')[1].split('## 2.')[0];newfactory=new.split('## 1.')[1].split('## 2.')[0];assert oldfactory==newfactory
keypart=new.split('## 5.')[1];keys=re.findall(r'^\| ([a-z]+) \|',keypart,re.M);expected=['souldewclause','sleepclause','freezeclause','evasionclause','ohkoclause','perishsongclause','selfkoclause','selfdestructclause','sonicboomclause','modifiedsleepclause','skillswapclause','drawclause','modifiedselfdestructclause','suddendeath'];assert keys==expected
wp56=allowed[3];old56=git('show',base+':'+wp56).decode();new56=(r/wp56).read_text();assert old56.split('## 2. Palace')[1].split('## 3. Arena')[0]==new56.split('## 2. Palace')[1].split('## 3. Arena')[0]
wp58=allowed[4];old58=git('show',base+':'+wp58).decode();new58=(r/wp58).read_text();assert old58.split('## 3.')[1].split('## 4.')[0]==new58.split('## 3.')[1].split('## 4.')[0]
lock=json.loads((a/'catalog-preservation.json').read_text());shared=lock['records'][1];assert [x['id'] for x in shared['changed_old_rows']]==['FC-10'];assert shared['added_static_rows']==[]
for series,ids in [('WS',['W28','W29']),('PA',['P16']),('RC',['W16','W22','W23'])]:
 assert not any(x['series']==series and x['id'] in ids for x in lock['records'][0]['changed_old_rows'])
formalcheck=subprocess.run(['git','-C',str(r),'diff','--check',base,'--',*allowed],capture_output=True,text=True);assert formalcheck.returncode==0,formalcheck.stdout
# All JSON readable, UTF8 outputs readable, no symlink/environment escape in author payload.
files=sorted([f for d in [a,p] for f in d.rglob('*') if f.is_file()]);assert all(not f.is_symlink() for f in files)
for f in files:
 d=f.read_bytes();d.decode('utf8')
 if f.suffix=='.json':json.loads(d)
result={'role':'NEW_AUTHOR_METADATA_VERIFICATION_ONLY','formal_FIX_BASE':base,'formal_tree':git('rev-parse',base+'^{tree}').decode().strip(),'allowed_formal_changed':allowed,'formal_changed_count':7,'protected_tracked_paths_unchanged_count':len(protected),'public_original_reference_history_AGENTS_unchanged':True,'planned_input_identity_count':52,'whole_control_object_equality_count':8,'old_catalog_ID_order_multiplicity_preserved':True,'old_catalog_actual':127,'new_catalog_static_designs':136,'new_design_delta':9,'vectors_executed':0,'shared_catalog_only_FC10_changed':True,'WS28_29_PA16_RC16_22_23_byte_identical':True,'all10_factory_rows_byte_identical':True,'all_Palace_section_byte_identical':True,'WP58_18key_initial_condition_and_layout_contract_byte_identical':True,'14_clause_keys_exact_11set_3consumer':True,'whole_original_proposal_apply_check':'PASS; not applied, all originals FIX_BASE bytes','original_scope_confirmation':'PENDING','formal_git_diff_check':'PASS','full_patch_content_whitespace':'Whole patches preserve context blank-line spaces intentionally; full unfiltered diff --check recorded separately after staging','independent_review_verdict':None,'full_acceptance_ready':False,'executed_reference_Ruby_game_historical_programs':0}
(a/'new-metadata-verification.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n');(a/'new-metadata-verifier.py').write_bytes(Path('/tmp/B13-verify.py').read_bytes())
# Inventory excludes itself only; all other payload bytes bound before candidate commit. Later publication receipts are separate reports.
allfiles=sorted([r/f for f in allowed]+[f for d in [a,p] for f in d.rglob('*') if f.is_file() and f.name!='output-inventory.json']);inv={'stage':'PRECOMMIT_FROZEN_PAYLOAD','FIX_BASE':base,'role':'AUTHOR_OUTPUT_IDENTITIES','self_inventory_excluded_only':True,'records':[{'path':str(f.relative_to(r)),**ident(f.read_bytes())} for f in allfiles]};(p/'output-inventory.json').write_text(json.dumps(inv,ensure_ascii=False,indent=2)+'\n')
print('metadata PASS: 7 formal; protected paths',len(protected),'; 52 input identities; 8 full controls; 136 unexecuted designs; original proposal cleanly applies but PENDING; payload files',len(allfiles)+1)
