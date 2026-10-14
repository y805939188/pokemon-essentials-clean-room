"""Independent administrative qualification reconciliation; fixed blob inputs.
Checks all R2/R3 exact owners/record hashes and scope-object hashes, not game
semantics. It produces structural forward/reverse evidence matrices only.
"""
import subprocess,json,pathlib,hashlib,collections,datetime
BASE=pathlib.Path(__file__).resolve().parent
M='8ea169fbd0f33f378b5d732fd6bea59e854e04a6';F='f49d870c6fd616ab6736754a218a4553b5acac7f';C='7533e516bd6e2a34ebeb68af28617c854ac17d50'
P='review/global-independent-review/fifth-2026-10-13-9366d9d-c7d3/'
cache={}
def get(rev,path):
 if (rev,path) not in cache:
  b=subprocess.check_output(['git','show',rev+':'+path]);cache[rev,path]=(b,json.loads(b))
 return cache[rev,path]
def at(d,p):
 for k in p.strip('/').split('/'):
  d=d[int(k)] if isinstance(d,list) else d[k.replace('~1','/').replace('~0','~')]
 return d
def digest(d):return hashlib.sha256(json.dumps(d,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode()).hexdigest()
curpath='review/remediation-fifth-20261013-prepare/integration/R5-U08/candidate-01/historical-regression-input.json'
cur=get(M,curpath)[1];oldregpath='review/remediation-fifth-20261013-prepare/reviews/R5-U08/candidate/round-01/regression-results.json';old=get(C,oldregpath)[1]
print('original candidate regression keys',list(old))
rows=[];errors=[]
for i,r in enumerate(cur['records']):
 if r['historical_file']=='regression-fourth-17.json':continue
 b,d=get(F,P+r['historical_file']);s=at(d,r['frozen_record']['pointer']);q=at(d,r['qualified_scope_binding']['pointer'])
 checks={'whole_blob_sha_matches':hashlib.sha256(b).hexdigest()==r['frozen_record']['sha256'],'whole_blob_bytes_matches':len(b)==r['frozen_record']['bytes'],'frozen_record_hash_matches':digest(s)==r['frozen_record']['record_sha256'],'qualified_scope_hash_matches':digest(q)==r['qualified_scope_binding']['record_sha256'],'identity_id_matches':r['id']==s['id'],'identity_owner_matches':r['batch_owner']==s.get('batch_owner',s.get('primary_owner')),'identity_record_key_matches':r['record_key']==s.get('record_key'),'no_verdict_transferred':r['historical_verdict_transferred'] is False,'original_scope_preserved_flag':r['original_scope_OR_partial_status_preserved'] is True}
 rows.append({'current_pointer':f'/records/{i}','current_id':r['id'],'record_key':r['record_key'],'owner':r['batch_owner'],'frozen_path':P+r['historical_file'],'frozen_pointer':r['frozen_record']['pointer'],'qualified_pointer':r['qualified_scope_binding']['pointer'],'record_sha256':r['frozen_record']['record_sha256'],'qualified_scope_sha256':r['qualified_scope_binding']['record_sha256'],'criteria_count':r['original_criteria_count'],'mandatory_relations':r['mandatory_relations'],'checks':checks,'evidence_level':'TOOL_VALIDATION_ONLY'})
 if not all(checks.values()):errors.append(rows[-1])
(BASE/'qualified-593-bindings.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2))
reg3=get(F,P+'regression-third-23.json')[1];legacy=get(F,P+'regression-legacy-scope.json')[1]
source=get(M,'review/remediation/20261003-prepare/FINAL-closure/registration-cloud-20261011-1/all341-public-source-map.json')[1]
all229=get(M,'review/remediation/20261003-prepare/FINAL-closure/registration-cloud-20261011-1/all229-closure-records.json')[1]
actual3=get(M,'review/remediation-third-20261012-prepare/registration/final-closure-acceptance.json')[1]
tuplefields=['batch','id','candidate','actual','independent_report']
to_tuple=lambda d:tuple(d[k] for k in tuplefields)
checks={'not_game_semantic_PASS':True,'R2_R3_count':len(rows),'all593_scope_identity_checks':not errors,'errors':errors,'R3_criteria_count_from_actual_arrays':sum(len(r['criteria']) for r in reg3['records']),'R3_ID_set_equal_to_activated23':{r['id'] for r in reg3['records']}==set(actual3['activated_required_ids23']),'R2_legacy229_ID_set_equal_to_original_closed229':{r['id'] for r in legacy['controls']}=={r['id'] for r in all229['records']},'R2_legacy341_tuple_set_equal_to_original341':{to_tuple(r['historical_identity_scope_reuse']['identity']) for r in legacy['contributions']}=={to_tuple(r['exact_identity_key']) for r in source['records']},'R3_excluded_originals':reg3['preserved_outside_required_scope']}
oldmap={(r['id'],r['record_key'],r['batch_owner']):r for r in old['historical_records']}
checks['candidate01_all593_identity_and_scope_containers_equal']=all(oldmap[(r['id'],r['record_key'],r['batch_owner'])]['frozen_record']==r['frozen_record'] and oldmap[(r['id'],r['record_key'],r['batch_owner'])]['qualified_scope_binding']==r['qualified_scope_binding'] for r in cur['records'] if r['historical_file']!='regression-fourth-17.json')
checks['candidate01_original_R3_76_criterion_record_hashes_exact']=all(digest(at(reg3,r['original_record_pointer']))==r['original_criterion_sha256'] for r in old['R3_criterion_results'])
act=get('debf59f3c5370df253706969fd4dd1c103300bf2','review/remediation-fifth-20261013-prepare/reviews/R5-U08/actual/round-01/regression-results.json')[1]
checks['actual_current_R3_76_exact_prior_array_hash']=digest(old['R3_criterion_results'])==act['compact_precise_scope_reuse']['R3']['criteria_source']['record_sha256']
(BASE/'qualified-binding-checks.json').write_text(json.dumps(checks,ensure_ascii=False,indent=2));print(json.dumps(checks,ensure_ascii=False,indent=2))
for name in ['forward-matrix.tsv','reverse-matrix.tsv']:
 with (BASE/name).open('w') as f:
  f.write('id\trecord_key\towner\tcurrent_pointer\tfrozen_path\tfrozen_pointer\tqualified_pointer\tcriteria_count\tclassification\n')
  ordered=rows if name.startswith('forward') else sorted(rows,key=lambda r:(r['frozen_path'],r['frozen_pointer']))
  for r in ordered:f.write('\t'.join(str(r[k]) for k in ['current_id','record_key','owner','current_pointer','frozen_path','frozen_pointer','qualified_pointer','criteria_count'])+'\tSTRUCTURAL_EXACT_QUALIFICATION_NOT_CURRENT_GAME_PASS\n')
for (rev,path),(b,d) in cache.items():
 with (BASE/'reading-ledger.jsonl').open('a') as f:f.write(json.dumps({'time':datetime.datetime.now(datetime.timezone.utc).isoformat(),'revision':rev,'path':path,'range':[1,len(b.splitlines())],'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'mode':'FULL_STRUCTURAL_POINTER_AND_RECORD_RECONCILIATION','semantic_review':'NOT_CURRENT_GAME_PASS','evidence_level':'TOOL_VALIDATION'})+'\n')
