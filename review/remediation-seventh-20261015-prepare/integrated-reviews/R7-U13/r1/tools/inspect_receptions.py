"""Select and bind the exact approval boundaries used for shared preservation."""
from pathlib import Path
import json,datetime,os
from run_logged import identity
W=Path('/workspace/r7-ir-R7-U13');T=Path(__file__).parent
out={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'pid':os.getpid(),'scope':'Read shared approval clauses and qualifications only; no re-review of other IDs','batches':[]}
def load(p):return json.loads(p.read_bytes())
for batch in ['R7-U01','R7-U02','R7-U11','R7-U12']:
    base=W/'actual-input/shared-candidate-review'/batch
    p=base/'per-id.json';d=load(p);r={'batch':batch,'per_id_identity':identity(p.read_bytes())}
    r['approval_records']=[]
    for rec in d['records']:
        keys=['id','record_id','conclusion','verdict','candidate_commit','candidate_tree','scope','clauses','candidate_locations','preservation_review','minimum_and_preservation','shared_contributions','unmet_later_gates','remaining_dependencies','candidate_review_unmet_dependencies','remaining_integration_or_broader_scope_dependencies','direct_author_blocking_edges','unmet_integration_and_closure','optional_policy_adoption','conditional_sync_writes']
        r['approval_records'].append({k:rec[k] for k in keys if k in rec})
    r['shared_approval']={k:d[k] for k in ['conflict_groups','conditional_sync','shared_receivers','qualification','limits','all_vectors_execution','L01_L14','effective_configuration','verdict_qualification'] if k in d}
    e=W/'actual-input/shared-root-reception'/batch/'eligibility.json';r['root_eligibility']=load(e);r['root_eligibility_identity']=identity(e.read_bytes())
    rp=base/'review-input-receipt.json';receipt=load(rp)
    r['input_receipt_identity']=identity(rp.read_bytes());r['input_receipt_top_level_keys']=list(receipt)
    out['batches'].append(r)
p=W/'actual-input/prior-accepted/decision.json';d=load(p)
out['prior_acceptance']={'identity':identity(p.read_bytes()),'authorizer':d['authorizer'],'counts':d['counts'],'records':[{k:v for k,v in x.items() if k in ['id','status','decision','verdict','actual_review_commit','actual_MI','qualification','scope','root_acceptance']} for x in d['records']]}
(T/'shared-approval-boundaries.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(out,ensure_ascii=False,indent=2))
