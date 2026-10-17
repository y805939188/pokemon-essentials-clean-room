#!/usr/bin/env python3
"""Apply the explicit, fixed-source R3 author patch only with --apply.
Source/current/upstream/IDs/categories/stages/implementation are protected.
"""
import argparse, copy, datetime, hashlib, json, pathlib
HERE=pathlib.Path(__file__).resolve().parent
HOME=HERE.parent.parent
ap=argparse.ArgumentParser();ap.add_argument('--apply',action='store_true');a=ap.parse_args()
p=HERE/'source-refinement-patch.json'; patch=json.loads(p.read_text()); target=HOME/'routing-manifest.json'; raw=target.read_bytes();data=json.loads(raw); before=copy.deepcopy(data)
assert data['current_snapshot']['commit']==patch['current_snapshot_commit']=='5f87743293290de2e219ecdd6c19e88280f60c9a'
rows={x['feature_id']:x for x in data['features']}
allowed={'/future_plan/rationale','/future_plan/responsibilities','/future_plan/questions','/dependencies/feature_refs','/dependencies/direct_refs','/dependencies/wp_refs','/differences'}
refinement=set(patch['six_future_dependency_refinement_ids'])
dependency_repairs=set(patch.get('dependency_repair_feature_ids',[]))
assert hashlib.sha256(raw).hexdigest()==patch['input_manifest_sha256']=='35175c7094b008e77af35cf6a7811c5fcd6f1a0dd20020b64d32b40d5670256e'
for rec in patch['records']:
 row=rows[rec['feature_id']]
 for change in rec['field_changes']:
  ptr=change['pointer'];assert ptr in allowed
  assert ptr=='/differences' or rec['feature_id'] in refinement or (ptr.startswith('/dependencies/') and rec['feature_id'] in dependency_repairs)
  keys=ptr.lstrip('/').split('/'); obj=row
  for key in keys[:-1]:obj=obj[key]
  assert obj[keys[-1]]==change['before'],(rec['feature_id'],ptr,'before mismatch')
  obj[keys[-1]]=copy.deepcopy(change['after'])
# Exact reverse reconstructs entire prior manifest: no hidden mutation.
rev=copy.deepcopy(data); rr={x['feature_id']:x for x in rev['features']}
for rec in patch['records']:
 for c in rec['field_changes']:
  obj=rr[rec['feature_id']];ks=c['pointer'].lstrip('/').split('/')
  for key in ks[:-1]:obj=obj[key]
  obj[ks[-1]]=copy.deepcopy(c['before'])
assert rev==before
result={'schema_version':'routing-r3-author-refinement-application.v1','command':'apply' if a.apply else 'check-only','utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'patch_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'manifest_before_sha256':hashlib.sha256(raw).hexdigest(),'feature_records':len(patch['records']),'explicit_field_changes':sum(len(x['field_changes']) for x in patch['records']),'future_dependency_refinement_ids':sorted(refinement),'dependency_repair_ids':sorted(dependency_repairs),'exact_reverse_preserves_entire_manifest':True,'immutable_source_current_upstream_ID_category_phase_implementation_unchanged':True,'applied':a.apply}
if a.apply:
 target.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n');result['manifest_after_sha256']=hashlib.sha256(target.read_bytes()).hexdigest();(HERE/'author-refinement-application.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(result,ensure_ascii=False,indent=2))
