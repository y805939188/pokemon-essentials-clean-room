"""Build exact legacy navigation, NEVER a semantic PASS generator."""
from reg_io import *
import csv, io

H='167296dbe9e2384627b0ed696e87aeb01f211252'
F='c2bc1a341ba6acdf7c8c111dc88d39a162a093d6'
HP='review/remediation/20261003-prepare/FINAL-closure/registration-cloud-20261011-1/'
FP='review/remediation/20261003-prepare/FINAL-1/independent-review-cloud-20261011-1/'
c229=jfixed(HP+'all229-closure-records.json',H)['records']
c341=jfixed(HP+'all341-public-source-map.json',H)['records']
q229=jfixed(FP+'all229-dispositions.json',F)['records']
q341=jfixed(FP+'public-registry-and-provenance.json',F)['all341_receipt_public_dispositions']
approved=jfixed('review/remediation-20261003-prepare/finding-acceptance.json','41fffb540c6483f5296ea0d33b789b75180d27ed')
rows=list(csv.DictReader(io.StringIO(fixed('review/remediation/20261003-prepare/traceability-successor.tsv')),delimiter='\t'))
lookup={(r['finding_id'],r['candidate_commit']):(i,r) for i,r in enumerate(rows)}

def paths(obj):
    out=[]
    def walk(x):
        if isinstance(x,dict):
            if isinstance(x.get('path'),str): out.append(x['path'])
            for v in x.values(): walk(v)
        elif isinstance(x,list):
            for v in x: walk(v)
        elif isinstance(x,str) and (x.startswith('deliverables/') or x.startswith('specs/') or x.startswith('Data/')): out.append(x)
    walk(obj)
    return list(dict.fromkeys(out))

out229=[];out341=[]
for i,(c,q) in enumerate(zip(c229,q229)):
    assert c['id']==q['id']
    a=approved[c['id']]
    out229.append({'id':c['id'],'title':a['title'],'primary_owner':q['primary_owner'],'all_contribution_keys':c['all_accepted_contribution_keys'],'historical_identity_scope_reuse':{'closure_binding':{'commit':H,'path':HP+'all229-closure-records.json','pointer':f'/records/{i}'},'original_control':c['whole_original_control'],'approved_control':c['whole_approved_control'],'qualified_scope':{k:a[k] for k in ['current_qualifications','adjudication_precedence','effective_case_constraints','minimum_revision','determinate_recheck','premises','minimum_counterexample','evidence_limits','extension_decisions'] if k in a},'qualification_details_binding':{'commit':F,'path':FP+'all229-dispositions.json','pointer':f'/records/{i}'},'reuse_boundary':'Identity and qualified original control only; no historical semantic verdict transfer.'},'current_B5_paths':[p for p in paths(q) if p.startswith(('deliverables/','specs/'))],'current_R5_semantic_review':{'status':'not_reviewed','fresh_evidence_joins':[],'reason':'Exact scope/current-clause/fresh-semantic join in progress; NOT missing_material.'}})
for i,(c,q) in enumerate(zip(c341,q341)):
    assert c['record_key']==q['record_key']
    idx,row=lookup[(c['id'],c['exact_identity_key']['candidate'])]
    try: scope=json.loads(row['current_clause_inputs']) if row['current_clause_inputs'] else {}
    except json.JSONDecodeError: scope={'literal':row['current_clause_inputs']}
    b=c['exact_identity_key']['batch']
    out341.append({'record_key':c['record_key'],'id':c['id'],'batch_owner':b,'primary':q['primary'],'primary_owner':q['primary_owner'],'historical_identity_scope_reuse':{'exact_binding':{'commit':H,'path':HP+'all341-public-source-map.json','pointer':f'/records/{i}'},'identity':c['exact_identity_key'],'acceptance_receipt':q['receipt'],'fixed_scoped_disposition':q['actual_provenance']['fixed_scoped_disposition'],'qualification':q['actual_provenance']['scope_and_qualification_fields_retained'],'accepted_contribution_kind':q['approval_join']['accepted_contribution_kind'],'scope_not_whole_ID_or_FINAL1':True,'original_qualified_control':q['original_complete_qualified_control'],'reuse_boundary':'Preserve partial, read-only NOT_AFFECTED and effective case qualifications exactly; history is navigation only.'},'original_contribution_scope':scope,'current_B5_navigation':{'version':B,'path':'review/remediation/20261003-prepare/traceability-successor.tsv','data_row_1based':idx+1,'static_vector_ids':row['static_test_ids_not_executed'],'paths':paths(scope)},'current_R5_semantic_review':{'status':'not_reviewed','fresh_evidence_joins':[],'reason':'Pending exact semantic scope join; mechanical parsing is not semantic review.'}})
save('regression-legacy-scope.json',{**BASE,'complete':False,'denominators':{'canonical_controls':229,'scoped_contributions':341,'round3_criteria':76,'round4_criteria':76,'counts_not_interchangeable':True},'mapping_method':'Exact original ID/batch/candidate key. Full qualified scope and effective cases remain at fixed pointers. B5 current navigation imported without propagating historical PASS. Fresh semantic joins require manual review.','controls':out229,'contributions':out341})
print('Navigation created:',len(out229),'controls and',len(out341),'scoped contributions; all semantic joins not_reviewed')
