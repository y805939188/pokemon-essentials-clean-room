"""Serialize this reviewer's authored findings and actual input receipts."""
import datetime
import hashlib
import json
from pathlib import Path

OUT=Path(__file__).resolve().parents[1]
def read(name):return json.loads((OUT/name).read_text())
def save(name,obj):(OUT/name).write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n')
audit=read('tool-evidence/candidate-byte-audit.json')
original=read('tool-evidence/original-input-recheck.json')
context=read('tool-evidence/actual-context.json')
provenance=read('tool-evidence/provenance-receipt.json')
nav=read('tool-evidence/navigation-regression.json')
current=read('tool-evidence/current-navigation-regression.json')
freeze=read('tool-evidence/inputs/candidate-input.json')

def criterion(id,detail,evidence,stage='INDEPENDENT_STATIC_CONTENT_REVIEW'):
    return {'id':id,'result':'SATISFIED_SCOPED','reviewer_observation':detail,'evidence':evidence,'stage':stage,
            'behavior_execution':'NOT_EXECUTED'}
shared_pending=['R7-I serial clause-level integration of CG01/CG07 and preservation of U01/U02/U10/U11/U13 contributions',
                'Root current-supplement/public projection receiver and WP72/domain owner reception',
                'Fresh independent R7-IR of actual cumulative integrated commit/tree',
                'Exact direct/transitive domain and historical regression reception before sole registrar acceptance/closure']
mchecks=[
 criterion('M19-NAV-01 / C01-M19-MISSING','Three full entries: old3+3+4 missing hrefs target exactly four H candidate artifacts; candidate126 remaining inline local destinations resolve and10 fixed H URLs obtain intended bytes.','tool-evidence/navigation-regression.json'),
 criterion('M19-NAV-02 / C01-M19-RECOVER','H README identifies NEW2 author candidate and links trace/eight-chain artifacts; B actual-freeze independently names H as candidate distinct from ACT. Four full HTTP payloads match bytes/SHA/blob; no semantic approval transfer.','tool-evidence/navigation-regression.json#/historical_targets'),
 criterion('M19-NAV-03','Reversing ten href substitutions and removing only three named retrieval notes reconstructs all three full B files byte-for-byte. No rules, IDs, static scenario ordering or historical state rewritten.','tool-evidence/navigation-regression.json#/reversal'),
 criterion('M19-NAV-04 / C01-M19-FAMILY','All17 catalog families and root README/CURRENT-DELIVERY/sixth-delivery controls retained. Formal131 structure untouched; static/not-executed qualification and old56/92 finite scopes retained.','tool-evidence/navigation-regression.json#/family_links_order'),
 criterion('C01-M19-DIRECTORY','user-interface/ is a valid Git directory. Original012 exit1 and erroneous11/5 attempt retained; corrected013 and this independent check give10/4.','tool-evidence/original-C01/tasks/R7-C01/logs/012-M19-independent-linkcheck.json'),
 criterion('M19-ARCHIVE-PREMISE','Exact H commit/path and object-or-matching-archive prerequisite stated consistently in all three notes; missing archive remains unavailable. Candidate/actual/acceptance identities stay separate.','tool-evidence/navigation-regression.json'),
 criterion('M19-NORMAL-CANCEL-FAILURE-PARTIAL','Existing routes work. Abandoning read-only navigation has no domain commit. Missing targets cannot display artifact; neighboring links are no substitute. No save or partial domain mutation asserted.','report.md'),
 criterion('M19-CONSUMERS','Three entry consumers synchronized to same four identities. M20 historical qualification and M21 current supplement decisions remain independent. No invented batch scheduling edge.','report.md')]
hchecks=[
 criterion('H08-NAV-01','B item42 and two public rows say§5.2/WP27; full§5.2 is party/storage and§5.3 L124 is add item. Candidate errata fixes only current navigation and preserves old frozen payload.','tool-evidence/current-navigation-regression.json'),
 criterion('H08-NAV-02','Matrix553/audit1828 each change one line, same§5.3/WP27 and errata target; complete other bytes and status columns unchanged.','tool-evidence/current-navigation-regression.json#/projection_changes'),
 criterion('H08-NAV-03','WP72§5.2/§5.3, WP27 and DG-U08-01–04 not changed; formal131 subtree and full frozen R6 subtree match B. No old ACCEPTED/CLOSED reopened.','tool-evidence/current-navigation-regression.json#/unchanged_actual_subtrees'),
 criterion('H08-NAV-05','Errata original sync-input, frozen R6 contract, WP72 full bytes/L124 with LF and fixed two source identities all independently match. Current-navigation precedence starts only after R7-I integration/acceptance.','tool-evidence/current-navigation-regression.json'),
 criterion('H08-CONSUMERS','Current errata→matrix/audit→WP72§5.3→WP27 inventory and DG controls stays coherent. Root public owner and WP72/M15 domain receiver remain pending; no record-to-record author blocking edge invented.','report.md'),
 criterion('H08-SCOPE','Only mandatory DEBUG001 navigation adopted. Two extra optional navigation facets,7 optional,1 no-required,2 policy not adopted. Reference anomaly facts and future compatibility policy remain distinct.','report.md')]
vectors=[]
for id,premise,expectation in [
 ('H08-NAV-04-normal1','Valid registered item, one available finite slot,max999,initial0,request1; normal helpers','Add1,true; requested1 message; sorting only if configured and successful'),
 ('DG-U08-01','Valid POTION,one finite slot,max999,initial0,request2; normal helpers','Add2,true; requested2 message'),
 ('H08-NAV-04-list-cancel / DG-U08-04','List cancelled','No add; no giving-message request'),
 ('H08-NAV-04-quantity0 / DG-U08-04','Quantity BACK returns0','No add; no giving-message request'),
 ('DG-U08-02','Valid item,one finite slot,max999,initial998,request2; no competing bag mutation; normal helpers','Add1 to999,false; no successful-add sort; normal return still requested2 feedback; added1 retained'),
 ('DG-U08-03','Same finite single slot,max999,initial999,request1; normal helpers','Add0,false; no success sort; normal return still requested1 feedback'),
 ('H08-NAV-04-zero-capacity','Finite zero available capacity,valid item,positive request; add returns normally','Can add0 and returnfalse; caller lacks capacity precheck and still requests giving message'),
 ('H08-NAV-04-add-failure','Add raises after reached writes','Reached writes retained; later giving message not guaranteed reached; no rollback/cleanup/host certificate'),
 ('DG-U08-04-message-failure','Add full/partial writes then message fails','Reached bag writes retained; normal feedback/cleanup not guaranteed'),
 ('DG-U08-04-infinite-pocket','Independent infinite pocket with existing full999 slot,request1; normal dependencies','Capacity may expand by another slot; add1 can succeed; successful sort remains configuration-dependent'),
 ('DG-U08-04-fill-bag-control','Separate fill-bag request3 including valid important and ordinary items,capacity/configuration permits','Clear before fill; important1,ordinary3; unavailable/zero/full pocket skip rules retained')]:
    vectors.append({'id':id,'premise':premise,'independent_static_expectation':expectation,'content_review':'SUPPORTED_WITH_STATED_PREMISES',
                    'stage':['SOURCE_STATIC','DERIVED_VECTOR'],'execution':'NOT_EXECUTED','basis':['R Debug778–797 and fill-bag adjacent control','R Bag81–93,162–164,263–281','B WP72§5.2/§5.3','B WP27§3.2–3.3','B DG-U08-01–04']})
records=[]
for id,checks,paths in [
 ('GR7-M19-001',mchecks,['deliverables/final-specification-set/README.md','deliverables/final-specification-set/scope-statement.md','deliverables/final-specification-set/test-catalog/README.md']),
 ('GR7-H08-001',hchecks,['audit/source-traceability.md','planning/feature-matrix.md','review/remediation-seventh-20261015-prepare/current-navigation-errata.json'])]:
    records.append({'record_id':id,'verdict':'PASS_SCOPED_CANDIDATE','candidate_commit':audit['candidate_commit'],'candidate_tree':audit['candidate_tree'],
        'candidate_files':[r for r in audit['files'] if r['path'] in ['candidates/R7-U12/'+p for p in paths]],
        'criteria':checks,'behavior_vectors':vectors if id=='GR7-H08-001' else [],
        'read_scope':'Full three M19 entries and index; complete changed clauses/errata and named source/consumer/counterproof ranges. Full matrix/audit byte identity and reversal, without unrelated historical semantic reapproval.',
        'source_execution':'NOT_EXECUTED','reference_observation':'NOT_EXECUTED','unmet_candidate_input_or_independence':[],
        'unmet_integration_and_closure':shared_pending+(['M20/M21 qualifications stay independent'] if id=='GR7-M19-001' else []),
        'direct_author_blocking_edges':[],'conditional_sync_writes':[],'optional_policy_adoption':False,
        'integrated_PASS':False,'ACCEPTED':False,'CLOSED':False})
save('per-id.json',{'schema':'r7.u12.independent-reviewer-per-id.v1','reviewer_thread':context['actual_reviewer_thread_id'],
    'dispatch_commit':audit['dispatch_commit'],'freeze_commit':audit['freeze_commit'],'baseline':freeze['fixed_B'],
    'records':records,'progress_denominator':{'required_records':27,'batches':13,'this_candidate_records':2,'new_formal_accepted':0,'new_closed':0},
    'effective_configuration':context['effective'],'L01_L14':'RETAINED','old56_92':'UNCHANGED_FINITE_HISTORICAL_SCOPES',
    'reference_complete_model_host_Demo_native_media_real_save_replay_executions':0,
    'verdict_qualification':'Independent static content review; tool checks/identity/exit0 and author self-review do not substitute for this verdict'})
save('review-input-receipt.json',{'schema':'r7.u12.independent-review-input-receipt.v1','recorded_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'actual_context':context,'dispatch_commit':audit['dispatch_commit'],'dispatch_tree':'577c350364bb4e2eb712325a9095d53d29eeeeb3',
    'candidate_freeze_commit':audit['freeze_commit'],'candidate_freeze_tree':'08bd0f362c74ef7645b5bbd70b557489c122ae29',
    'candidate_input_path':'review/remediation-seventh-20261015-prepare/candidate-freezes/R7-U12/candidate-input.json',
    'fixed_file_bindings':audit['fixed_file_bindings'],'candidate_commit':audit['candidate_commit'],'candidate_tree':audit['candidate_tree'],
    'author_external_task_id':freeze['author_task_id'],'candidate_readonly_destination':'/workspace/r7-review-input/R7-U12-r1-1f33c39804d819c5a55a2b084287fc4a3a4c0919',
    'candidate_files':audit['files'],'candidate_file_count':104,'candidate_bytes':1292206,
    'original_input_destination':'/workspace/r7-context/R7-U12-reviewer','original_input_files':original['files'],'original_input_count':26,'original_input_bytes':7587353,
    'original_C01_pinned_recovery':provenance['original_C01_pinned_remote_objects'],'original_raw_contract_slices':read('tool-evidence/original-raw-bindings.json'),
    'independent_git_scope_check':'Complete B-to-candidate diff104 additions all candidates/R7-U12; all ordinary100644 blobs; freeze/dispatch Git objects match downloaded bytes',
    'recovery_qualification':'Selected immutable files, not full R checkout or runtime certification; no assumed shared parent cache',
    'initial_logging_gap':context['initial_logging_gap'],'effective_configuration':context['effective'],
    'unexecuted':['all behavior vectors','reference programs','author scripts','independent complete behavior model','game host','Demo','native media','real save or replay','browser/fragment checks','full131 semantic/link audit'],
    'L01_L14':'RETAINED','integrated_PASS':False,'ACCEPTED':False,'CLOSED':False})
print(json.dumps({'per_id_verdicts':{r['record_id']:r['verdict'] for r in records},'candidate_files_bound':104,'original_inputs_bound':26,'behavior_vectors':'NOT_EXECUTED'},ensure_ascii=False))
