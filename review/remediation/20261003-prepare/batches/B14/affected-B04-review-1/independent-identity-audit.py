import hashlib,json,re,subprocess
from pathlib import Path
R=Path('/workspace/b14-affected-b04-review')
B='1e6b11a47370f1c7c4659a32443fc1afda597bac'
C='47f7514765f8569ae9172bb06a2cd615e2b83b8a'
A='b37533ef1cfc7808ed41d64215647a78d165ada4'
G='93e10babe0b9c9ef8b3f5277754541b447beeeb4'
P='41fffb540c6483f5296ea0d33b789b75180d27ed'
O=Path('/tmp/b14-b04-audit')
def git(*args,repo=R): return subprocess.check_output(['git',*args],cwd=repo)
def blob(c,p):return git('show',c+':'+p)
def load(c,p):return json.loads(blob(c,p))
def canon(x):return hashlib.sha256(json.dumps(x,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def identity(c,p):
 b=blob(c,p);return dict(commit=c,path=p,git_blob=git('rev-parse',c+':'+p).decode().strip(),sha256=hashlib.sha256(b).hexdigest(),bytes=len(b))
def save(p,x): (O/p).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
contract=load(B,'review/remediation/20261003-prepare/batches/B09/acceptance-stage-1/B14-downstream-contract.json')
refreeze=load(C,'review/remediation/20261003-prepare/batches/B14/author-stage-1/input-refreeze.json')
originals={x['id']:x for x in load(G,'review/global-independent-review/2026-10-03-fd82a639/findings.json')}
acceptance=load(P,'review/remediation-20261003-prepare/finding-acceptance.json')
controls=[]
for x in contract['contribution_controls']:
 i=x['id'];o=originals[i];a=acceptance[i]
 mismatches=[]
 for k,v in x['complete_current_control_fields'].items():
  if o.get(k)!=v:mismatches.append('current:'+k)
 for k,v in x['complete_minimum_acceptance_fields'].items():
  if a.get(k)!=v:mismatches.append('acceptance:'+k)
 h1=canon(o);h2=canon(a)
 if h1!=x['whole_original_object_sha256']:mismatches.append('whole original')
 if h2!=x['whole_acceptance_object_sha256']:mismatches.append('whole acceptance')
 rf=next(y for y in refreeze['complete_control_bindings'] if y['id']==i)
 if rf['whole_original_sha256']!=h1 or rf['whole_acceptance_sha256']!=h2:mismatches.append('refreeze hash')
 controls.append(dict(id=i,primary=x['primary'],whole_original_sha256=h1,whole_acceptance_sha256=h2,mismatches=mismatches,current_qualification=o.get('current_qualifications'),complete_current_control_fields=x['complete_current_control_fields'],complete_minimum_acceptance_fields=x['complete_minimum_acceptance_fields']))
save('qualified-controls.json',controls)
bindings=[]
for family,items in [('planned_reads',refreeze['planned_reads']),('write_inputs',refreeze['write_inputs']),('current_extra_inputs',refreeze['current_extra_inputs'])]:
 for item in items:
  binding_commit=item.get('verified_commit',item.get('commit',B))
  got=identity(binding_commit,item['path']);bad=[k for k in ['git_blob','sha256','bytes'] if got[k]!=item[k]]
  same=blob(B,item['path'])==blob(C,item['path']) if binding_commit==B else None
  bindings.append(dict(family=family,**got,mismatches=bad,candidate_same_bytes=same))
for item in refreeze['fixed_controls']:
 got=identity(item['commit'],item['path']);bindings.append(dict(family='fixed_controls',**got,mismatches=[k for k in ['git_blob','sha256','bytes'] if got[k]!=item[k]]))
save('refrozen-input-verification.json',bindings)
changes=[]
for row in git('diff','--name-status','--no-renames',B,C).decode().splitlines():
 status,p=row.split('\t');changes.append(dict(status=status,path=p,before=identity(B,p) if status!='A' else None,after=identity(C,p)))
allowed=contract['allowed_formal_write_paths']+[x['original_path'] for x in contract['potential_original_sync_contract']]
scope=load(C,'review/remediation/20261003-prepare/batches/B14/scope-proposal-1/scope-manifest.json')
scopechecks=[]
for x in scope['records']:
 p=x['path'];before=identity(B,p);after=identity(C,p);patch=blob(C,'review/remediation/20261003-prepare/batches/B14/scope-proposal-1/'+x['complete_diff'])
 scopechecks.append(dict(path=p,before_match=all(before[k]==x['before'][k] for k in ['git_blob','sha256','bytes']),after_match=all(after[k]==x['intended_after'][k] for k in ['git_blob','sha256','bytes']),approved_checkpoint_patch_unchanged=patch==blob(A,'review/remediation/20261003-prepare/batches/B14/scope-proposal-1/'+x['complete_diff']),patch_sha256=hashlib.sha256(patch).hexdigest(),patch_hash_match=hashlib.sha256(patch).hexdigest()==x['diff_sha256']))
own=load(B,'review/remediation/20261003-prepare/batches/B04/acceptance-stage-1/acceptance-manifest.json')['accepted_formal_identities']
owner=[]
for x in own:
 p=x['path'];owner.append(dict(path=p,accepted_identity=x,baseline=identity(B,p),candidate=identity(C,p),baseline_candidate_equal=blob(B,p)==blob(C,p),accepted_baseline_equal=x['git_blob']==identity(B,p)['git_blob']))
save('B04-formal-preservation.json',owner)
cats=contract['allowed_formal_write_paths'][-2:];catchecks=[]
for p in cats:
 def rows(c):return [(m.group(1),s) for s in blob(c,p).decode().splitlines() if (m:=re.match(r'^\| ([A-Za-z][A-Za-z0-9_-]*\d+) \|',s))]
 old=rows(B);new=rows(C);oldids=[i for i,_ in old];newids=[i for i,_ in new]
 assert len(set(oldids))==len(oldids) and len(set(newids))==len(newids)
 oldmap=dict(old);newmap=dict(new)
 changed=[dict(id=i,before=oldmap[i],after=newmap.get(i)) for i in oldids if oldmap[i]!=newmap.get(i)]
 added=[dict(id=i,row=s) for i,s in new if i not in oldmap]
 protected=[i for i in oldids if i.startswith(('RS','B04-R'))]
 catchecks.append(dict(path=p,old_count=len(old),new_count=len(new),old_ids_order_preserved=[i for i in newids if i in oldmap]==oldids,old_multiplicity_preserved=all(newids.count(i)==1 for i in oldids),changed_old_rows=changed,added_rows=added,protected_rows=[dict(id=i,byte_equal=oldmap[i]==newmap.get(i)) for i in protected]))
save('catalog-comparison.json',catchecks)
pkg=load(C,'review/remediation/20261003-prepare/batches/B14/candidate-1/reverse-impact-packages.json')
def find_owner(obj):
 if isinstance(obj,dict):
  if obj.get('accepted_owner')=='B04':return obj
  for v in obj.values():
   a=find_owner(v)
   if a:return a
 elif isinstance(obj,list):
  for v in obj:
   a=find_owner(v)
   if a:return a
ownerpkg=find_owner(pkg);oldgate=next(x for x in contract['accepted_reverse_review_gates'] if x['accepted_batch']=='B04')
save('reverse-package-comparison.json',dict(package=ownerpkg,contract_gate_equal=ownerpkg['contract_gate']==oldgate,changed_reader_bindings=[dict(path=x['path'],match=all(identity(B,x['path'])[k]==x['current_baseline'][k] for k in ['git_blob','sha256','bytes'])) for x in ownerpkg['contract_gate']['changed_planned_reverse_readers']]))
summary=dict(candidate_commit=C,candidate_tree=git('rev-parse',C+'^{tree}').decode().strip(),candidate_parents=git('show','-s','--format=%P',C).decode().strip().split(),approved_scope_checkpoint=A,accepted_predecessor=B,predecessor_tree=git('rev-parse',B+'^{tree}').decode().strip(),controls=len(controls),primary=sum(x['primary'] for x in controls),control_mismatches=[x['id'] for x in controls if x['mismatches']],binding_counts={f:sum(x['family']==f for x in bindings) for f in set(x['family']for x in bindings)},binding_mismatches=[x['path'] for x in bindings if x['mismatches']],changes=changes,modified_count=sum(x['status']=='M' for x in changes),added_count=sum(x['status']=='A' for x in changes),modified_exactly_allowed=set(x['path'] for x in changes if x['status']=='M')==set(allowed),all_additions_under_B14=all(x['path'].startswith('review/remediation/20261003-prepare/batches/B14/') for x in changes if x['status']=='A'),original_scope_checks=scopechecks,B04_full_paths_unchanged=sum(x['baseline_candidate_equal'] for x in owner),B04_formal_count=len(owner),old_catalog_rows=sum(x['old_count']for x in catchecks),new_catalog_rows=sum(x['new_count']for x in catchecks),changed_old_catalog_rows=sum(len(x['changed_old_rows'])for x in catchecks),added_catalog_rows=sum(len(x['added_rows'])for x in catchecks),full_diff_bytes=(O/'complete-predecessor-to-candidate.diff').stat().st_size,full_diff_sha256=hashlib.sha256((O/'complete-predecessor-to-candidate.diff').read_bytes()).hexdigest(),runtime_observations=0,proven_Demo_chains=0,behavior_vectors_executed=0,own_check_scope='Git/UTF-8/JSON/hash comparison only; no reference/author/historical program execution or behavior simulation')
save('identity-and-scope-audit.json',summary)
print(json.dumps({k:v for k,v in summary.items() if k not in ['changes','original_scope_checks']},ensure_ascii=False,indent=2))
