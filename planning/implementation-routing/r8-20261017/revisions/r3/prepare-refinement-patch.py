
# Historical author step: never overwrite later calibrated evidence.
import hashlib as _r3_hashlib, pathlib as _r3_pathlib
_r3_guard_manifest = _r3_pathlib.Path(__file__).resolve().parent.parent.parent / 'routing-manifest.json'
if _r3_hashlib.sha256(_r3_guard_manifest.read_bytes()).hexdigest() != '35175c7094b008e77af35cf6a7811c5fcd6f1a0dd20020b64d32b40d5670256e':
    raise SystemExit('Historical R3 author step refuses changed/final manifest; use fixed archive and recorded patch for audit.')
import pathlib,json,hashlib
h=pathlib.Path('/workspace/r8-disposition-tagging/planning/implementation-routing/r8-20261017');r=h/'revisions/r3';m=json.loads((h/'routing-manifest.json').read_text());f={x['feature_id']:x for x in m['features']};p=json.loads((r/'source-plan-refinements.json').read_text());d=json.loads((r/'feature-source-deltas.json').read_text());records=[]
def union(a,b):return a+[x for x in b if x not in a]
for q in p['records']:
 row=f[q['feature_id']]; changes=[]
 def add(ptr,b,a):
  if b!=a:changes.append({'pointer':ptr,'before':b,'after':a})
 fp=row['future_plan'];de=row['dependencies']
 add('/future_plan/rationale',fp['rationale'],q['proposed_future_plan_rationale']);add('/future_plan/responsibilities',fp['responsibilities'],q['proposed_responsibilities']);add('/future_plan/questions',fp['questions'],union(fp['questions'],q['append_questions']));add('/dependencies/feature_refs',de['feature_refs'],union(de['feature_refs'],q['append_feature_refs']));add('/dependencies/direct_refs',de['direct_refs'],union(de['direct_refs'],q['append_direct_refs']))
 w={'FR-000397':['WP18','WP33','WP34'],'FR-000645':['WP12'],'FR-000647':['WP12'],'FR-000699':['WP08','WP15'],'FR-000703':['WP08','WP15']}.get(q['feature_id'],[]);add('/dependencies/wp_refs',de['wp_refs'],union(de['wp_refs'],w));
 records.append({'feature_id':q['feature_id'],'current_source_evidence':q['current_source_evidence'],'field_changes':changes})
for q in d['records']:
 row=f[q['feature_id']];x=next((a for a in records if a['feature_id']==q['feature_id']),None)
 if x is None:x={'feature_id':q['feature_id'],'current_source_evidence':q['current_source'],'field_changes':[]};records.append(x)
 specific=next((a['append_difference'] for a in p['records'] if a['feature_id']==q['feature_id']),q['source_fact_delta']+'；当前已接受源细化上述行为，目标去向/时序/失败前缀仍待验证。')
 diff=specific+' R3逐行证据：revisions/r3/feature-source-deltas.json#'+q['feature_id']+'（final5f与不可变B8来源分别登记）。'
 x['field_changes'].append({'pointer':'/differences','before':row['differences'],'after':union(row['differences'],[diff])})
(r/'source-refinement-patch.json').write_text(json.dumps({'schema_version':'routing-r3-source-refinement-patch.v1','role':'AUTHOR_EXPLICIT_BEFORE_AFTER_NO_CLASSIFICATION_CHANGE','status':'PREPARED_NOT_YET_APPLIED','current_snapshot_commit':m['current_snapshot']['commit'],'input_manifest_sha256':hashlib.sha256((h/'routing-manifest.json').read_bytes()).hexdigest(),'six_future_dependency_refinement_ids':[x['feature_id'] for x in p['records']],'source_delta_reference_feature_count':len(d['records']),'records':records,'protected_fields':['feature_id','source','functional_scope','current_applicability','upstream','future_plan/destination','future_plan/partners','future_plan/stage','future_plan/stage_approval','implementation','destination_verification']},ensure_ascii=False,indent=2)+'\n')
print('prepared',len(records),'features',sum(len(x['field_changes']) for x in records),'field changes')
