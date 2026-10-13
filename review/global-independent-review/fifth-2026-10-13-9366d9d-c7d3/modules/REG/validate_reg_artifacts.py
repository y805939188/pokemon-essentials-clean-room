"""Read-only integrity checks on REG artifacts and fixed text line bounds, no behavior execution."""
from current_evidence import *
from collections import Counter
issues=[];checks={};fixedlines={};current_files={}
def err(kind,**info):issues.append({'kind':kind,**info})
def countlines(p,source=False):
 k=(p,source)
 if k in fixedlines:return fixedlines[k]
 raw=subprocess.check_output(['git','-C',str(REF if source else ROOT),'show',(R if source else B)+':'+p])
 try:t=raw.decode('utf-8');n=len(t.splitlines())
 except UnicodeDecodeError:n=None
 fixedlines[k]=n;return n
for name,records,criteria in [('regression-fourth-17.json',17,76),('regression-third-23.json',23,76)]:
 d=json.loads((HERE/name).read_text());assert len(d['records'])==records;assert sum(len(r['criteria']) for r in d['records'])==criteria
 checks[name]={'records':records,'criteria':criteria,'record_statuses':dict(Counter(r['current_R5_semantic_review']['status'] for r in d['records'])),'criterion_statuses':dict(Counter(c['current_R5_semantic_review']['status'] for r in d['records'] for c in r['criteria']))}
 for r in d['records']:
  j=r['current_R5_semantic_review'].get('fresh_global_review_join',{})
  if not j.get('source_capabilities'):err('finite_missing_capability_join',id=r['id'])
  if not j.get('inverse_clauses'):err('finite_missing_inverse_join',id=r['id'])
D=json.loads((HERE/'regression-legacy-scope.json').read_text());assert len(D['controls'])==229 and len(D['contributions'])==341
assert len({r['id'] for r in D['controls']})==229 and len({r['record_key'] for r in D['contributions']})==341
A=json.loads((HERE/'scope-assessments.json').read_text());assert set(A['records'])=={r['record_key'] for r in D['contributions']}
checks['legacy']={'controls':229,'scoped_contributions':341,'all_original_identities_retained':True,'manual_scope_assessments':341,'source_of_semantic_status':'manual scoped comparison + explicit fresh joins; never identity/count equality'}
for r in D['contributions']:
 for a in r['current_B5_navigation']['clause_candidates']:
  n=countlines(a['path']);lo,hi=a['lines']
  if not n or lo<1 or hi<lo or hi>n:err('current_clause_line_bounds',record_key=r['record_key'],path=a['path'],lines=a['lines'],actual_line_count=n)
 for fld in ['identity','acceptance_receipt','fixed_scoped_disposition','qualification','original_qualified_control']:
  if fld not in r['historical_identity_scope_reuse']:err('legacy_qualification_missing',record_key=r['record_key'],field=fld)
# Stable snapshots bind both exact file address and literal record contents.
def pointer_resolve(o,p):return pointer_get(o,p)
for fn in ['fresh-evidence-snapshots.json','finite-fresh-snapshots.json']:
 d=json.loads((HERE/fn).read_text())
 for key,rec in d['records'].items():
  if digest(rec['snapshot'])!=rec['record_sha256']:err('snapshot_record_digest',file=fn,snapshot_id=key)
  p=ROOT/rec['file']
  if rec['file'] not in current_files:
   raw=p.read_bytes();current_files[rec['file']]=(digest(raw),json.loads(raw))
  sha,obj=current_files[rec['file']]
  if sha!=rec['file_sha256']:continue # report once per file below
  try:cur=pointer_resolve(obj,rec['pointer'])
  except (KeyError,IndexError,TypeError):err('snapshot_pointer_missing',file=rec['file'],pointer=rec['pointer']);continue
  if digest(cur)!=rec['record_sha256']:err('snapshot_current_record_mismatch',file=rec['file'],pointer=rec['pointer'])
checks['current_snapshot_files']={}
for fn in ['fresh-evidence-snapshots.json','finite-fresh-snapshots.json']:
 d=json.loads((HERE/fn).read_text());pairs_seen={(r['file'],r['file_sha256']) for r in d['records'].values()}
 for path,sha in pairs_seen:
  cur=current_files[path][0];checks['current_snapshot_files'][path]={'sha256':sha,'current_sha256':cur,'matches':cur==sha}
  if cur!=sha:err('primary_artifact_updated_since_join',file=path,joined_sha256=sha,current_sha256=cur)
S=json.loads((HERE/'fresh-source-ledger.json').read_text());source_bounds=0
for id,r in S['source_facts'].items():
 if not r['reading_ledger_refs']:err('source_reading_join_missing',source_fact=id,path=r['source_path'])
 for x in r['reading_ledger_refs']:
  if x not in S['reading_records']:err('source_ledger_ref_unresolvable',source_fact=id,ref=x)
 if not r['source_ranges']:continue
 n=countlines(r['source_path'],True)
 if n is None:continue # decoded embedded lines/resources use explicit primary evidence, not physical text bounds
 for lo,hi in r['source_ranges']:
  source_bounds+=1
  if lo<1 or hi<lo or hi>n:err('source_line_bounds',source_fact=id,path=r['source_path'],module=r['primary_projection_module'],lines=[lo,hi],actual_line_count=n)
for id,r in S['reading_records'].items():
 if digest(r['record'])!=r['address']['record_sha256']:err('reading_record_digest',id=id)
O=json.loads((HERE/'original-comparison-joins.json').read_text());checks['originals']={'rows':len(O['records']),'unique_paths':len({r['original'] for r in O['records']}),'pending':sum(r['status']=='not_reviewed' for r in O['records'])}
for r in O['records']:
 p=r['primary_evidence'];raw=(ROOT/p['path']).read_bytes();ob=json.loads(raw)
 if digest(raw)!=p['file_sha256']:err('original_primary_artifact_updated',file=p['path'],original=r['original'])
 elif digest(pointer_get(ob,p['pointer']))!=p['record_sha256']:err('original_record_mismatch',original=r['original'])
checks['physical_source_ranges_checked']=source_bounds
checks['reference_execution']=0;checks['behavior_model_execution']=0;checks['checks_are_semantic_proof']=False
out={**BASE,'complete':False,'validation_kind':'structural addresses, hashes, cardinalities and physical text line bounds only','checks':checks,'issues':issues,'structural_checks_passed':not issues,'semantic_completion_separate':True}
save('artifact-validation.json',out)
print('Validation issues',len(issues));print(dict(Counter(i['kind'] for i in issues)))
for i in issues[:30]:print(i)
