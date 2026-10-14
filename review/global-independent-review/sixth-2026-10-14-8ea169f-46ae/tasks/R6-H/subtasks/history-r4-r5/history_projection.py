import json, subprocess, hashlib, datetime
from pathlib import Path
OUT=Path(__file__).resolve().parent
COMMIT='f49d870c6fd616ab6736754a218a4553b5acac7f'
ROOT='review/global-independent-review/fifth-2026-10-13-9366d9d-c7d3/'
def fetch(name):
    raw=subprocess.check_output(['git','show',COMMIT+':'+ROOT+name])
    return raw,json.loads(raw)
raw,d=fetch('findings.json')
keys=['id','title','disposition','status','category','expected_reference_behavior','current_spec_behavior','gap','preconditions','minimal_counterexample','normal_case','failure_or_boundary_case','negative_evidence_search','impact_on_independent_implementation','proposed_spec_change','affected_files','acceptance_criteria','dependencies','history_links','evidence_level','execution_status','unknowns','excluded_claims','user_decision_needed','review_resolution','canonical_input']
projection=[]
for i,r in enumerate(d['findings']):
    if r['disposition']!='required':
        projection.append({'origin':{'commit':COMMIT,'path':ROOT+'findings.json','pointer':f'/findings/{i}'},'qualification_clauses':{k:r[k] for k in keys if k in r},'unprojected_keys':[k for k in r if k not in keys]})
(OUT/'R5-qualification-projection.json').write_text(json.dumps(projection,ensure_ascii=False,indent=2)+'\n')
metadata=[]
for item in projection:
    index=int(item['origin']['pointer'].split('/')[-1])
    record=d['findings'][index]
    metadata.append({'origin':item['origin'],'remaining_record_fields':{k:record[k] for k in item['unprojected_keys']}})
(OUT/'R5-metadata-projection.jsonl').write_text('\n'.join(json.dumps(x,ensure_ascii=False,separators=(',',':')) for x in metadata)+'\n')
raw4,d4=fetch('regression-fourth-17.json')
p4=[]
for i,r in enumerate(d4['records']):
    scope=r['historical_identity_scope_reuse']
    p4.append({'origin':{'commit':COMMIT,'path':ROOT+'regression-fourth-17.json','pointer':f'/records/{i}'},'id':r['id'],'batch_owner':r['batch_owner'],'scope':scope,'criteria':[{'id':c['criterion_id'],'criterion':c['criterion'],'kind':c['kind'],'status':c['current_R5_semantic_review']['status'],'boundary':c['current_R5_semantic_review'].get('boundary'),'assessment':c['current_R5_semantic_review'].get('assessment')} for c in r['criteria']],'status':r['current_R5_semantic_review']['status'],'unprojected_evidence_layers':['current_R5_semantic_review/evidence','current_R5_semantic_review/fresh_global_review_join','criteria/*/current_R5_semantic_review/evidence','criteria/*/current_R5_semantic_review/fresh_global_review_join']})
(OUT/'R4-qualification-projection.json').write_text(json.dumps(p4,ensure_ascii=False,indent=2)+'\n')
rec={'timestamp':datetime.datetime.now(datetime.timezone.utc).isoformat(),'mode':'STRUCTURE_PARSE_ONLY_NOT_SEMANTIC','inputs':[{'path':ROOT+'findings.json','sha256':hashlib.sha256(raw).hexdigest(),'records':len(d['findings'])},{'path':ROOT+'regression-fourth-17.json','sha256':hashlib.sha256(raw4).hexdigest(),'records':len(d4['records']),'criteria':sum(len(r['criteria']) for r in d4['records'])}],'outputs':['R5-qualification-projection.json','R4-qualification-projection.json'],'semantic_pass':False}
with(OUT/'reading-ledger.jsonl').open('a')as f:f.write(json.dumps(rec,ensure_ascii=False)+'\n')
print(json.dumps(rec,ensure_ascii=False))
