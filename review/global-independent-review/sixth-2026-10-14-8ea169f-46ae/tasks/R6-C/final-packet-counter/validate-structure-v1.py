import json,hashlib,collections,datetime
from pathlib import Path
b=Path(__file__).parent;r=json.loads((b/'findings__normative-records.json').read_text());pack=json.loads((b/'handoff__batch-assignment.json').read_text());issues=[];loc_checks=[];field_checks=[]
def nonempty(v):
 if v is None:return False
 if isinstance(v,(str,list,dict)):return len(v)>0
 return True
def walk(x,record,path=''):
 if isinstance(x,dict):
  if 'locator'in x and 'payload_identity'in x:
   loc=x['locator'];pid=x['payload_identity'];lp=loc.get('path');pp=Path(pid['repository'])/pid['path'];q={'record':record,'jsonpath':path,'locator':lp,'payload':str(pp),'role':x.get('payload_role'),'resolved':x.get('identity_resolved')}
   if not pp.exists():issues.append({'type':'MISSING_PAYLOAD','record':record,'path':str(pp)})
   else:
    data=pp.read_bytes();sha=hashlib.sha256(data).hexdigest();blob=hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest();n=len(data.decode('utf-8').splitlines())if pid.get('type')=='text'else None
    q.update(sha_match=sha==pid.get('sha256'),blob_match=blob==pid.get('git_blob'),bytes_match=len(data)==pid.get('bytes'),linecount_match=n==pid.get('lines')if n is not None else'BINARY_NO_TEXT_CHECK')
    lines=loc.get('lines',loc.get('range'));lines=lines if isinstance(lines,list) else [loc.get('line')]if loc.get('line')else []
    q['locator_lines_valid']=bool(lines)and all(isinstance(z,int)and z>=1 and(n is None or z<=n)for z in lines)
    q['path_suffix_consistent']=lp==pid['path']or lp=='reference/pokemon-essentials/'+pid['path']
    if not all(q[k]for k in['sha_match','blob_match','bytes_match','locator_lines_valid','path_suffix_consistent']):issues.append({'type':'IDENTITY_OR_LOCATOR_MISMATCH','detail':q})
   loc_checks.append(q)
  for k,v in x.items():walk(v,record,path+'/'+k)
 elif isinstance(x,list):
  for i,v in enumerate(x):walk(v,record,path+'/'+str(i))
required={q['id']for q in r if q['identity_and_verdict']['classification']=='required'};ids=[q['id']for q in r];assert len(ids)==len(set(ids))
for q in r:
 id=q['id'];walk(q,id)
 if id in required:
  groups={'source':q['bidirectional_evidence'].get('source'),'formal':q['bidirectional_evidence'].get('formal'),'input_domain':q['premises_and_counterexample'].get('input_domain'),'counterexample':q['premises_and_counterexample'].get('minimal_counterexample'),'control':q['premises_and_counterexample'].get('ordinary_control'),'revision_rule':q['minimum_revision_contract'].get('rule'),'preserve_scope':q['minimum_revision_contract'].get('preserve_correct_scope'),'acceptance':q['acceptance_and_regression'].get('conditions_and_vectors'),'counter_records':q['independent_adjudication'].get('non_proposer_records')}
  fields={k:nonempty(v)for k,v in groups.items()};field_checks.append({'id':id,'nonempty_checks':fields,'semantic_inference':False})
  for k,v in fields.items():
   if not v:issues.append({'type':'REQUIRED_EMPTY_FIELD','id':id,'field':k})
assigned=[i for p in pack['batches']for i in p['required_ids']];counts=collections.Counter(assigned)
for id in required:
 if counts[id]!=1:issues.append({'type':'PRIMARY_BATCH_MULTIPLICITY','id':id,'count':counts[id]})
for id in assigned:
 if id not in required:issues.append({'type':'NONREQUIRED_IN_PRIMARY_BATCH','id':id})
# Identity mapping must never accidentally reactivate the withdrawn Entry-stale-command hypothesis.
withdrawn=[q for q in r if 'PARTY-004'in q['id']or any('PARTY-004'in a for a in q['aggregation_aliases'])]
if any(q['identity_and_verdict']['classification']=='required'for q in withdrawn):issues.append({'type':'WITHDRAWN_UI_PARTY004_REQUIRED'})
afi=[q for q in r if any('AF001'in str(v)for v in[q['id'],q['aggregation_aliases']])]
for q in afi:
 if 'V001'not in q['id']:issues.append({'type':'AF001_NEW_STANDALONE_ROOT_CAUSE','id':q['id']})
for p in pack['batches']:
 if p['frozen_main']!='8ea169fbd0f33f378b5d732fd6bea59e854e04a6'or p['frozen_reference']!='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b':issues.append({'type':'BATCH_INPUT_DRIFT','batch':p['id']})
 for path in p['candidate_formal_paths']:
  if not path.startswith('deliverables/final-specification-set/'):issues.append({'type':'NONFORMAL_AUTHOR_TARGET','batch':p['id'],'path':path})
 if not all(nonempty(p[k])for k in['author','reviewer','candidate_pass','integrated_acceptance','closure_gate','policy_limits']):issues.append({'type':'EMPTY_BATCH_STAGE_OR_ROLE','batch':p['id']})
summary={'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'records':len(r),'required':len(required),'batches':len(pack['batches']),'primary_assignments':len(assigned),'unique_required_primary':len(set(assigned)),'nested_payload_locators_checked':len(loc_checks),'required_nonempty_groups_checked':len(field_checks),'issues':issues,'withdrawn_ui_party004':[{'id':q['id'],'verdict':q['identity_and_verdict']['classification']}for q in withdrawn],'AF001_records':afi,'status':'STRUCTURAL_CHECK_ONLY_NOT_SEMANTIC_PASS'}
(b/'structure-validation.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n');(b/'locator-checks.jsonl').write_text(''.join(json.dumps(q,ensure_ascii=False)+'\n'for q in loc_checks));(b/'nonempty-required-checks.jsonl').write_text(''.join(json.dumps(q,ensure_ascii=False)+'\n'for q in field_checks));print(json.dumps({k:v for k,v in summary.items()if k!='AF001_records'},ensure_ascii=False,indent=2))
