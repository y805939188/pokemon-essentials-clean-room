"""Classify fixed corpus paths; this is disposition inventory, not semantic signoff."""
import json,pathlib,collections,hashlib,subprocess
O=pathlib.Path(__file__).resolve().parents[2]
I=json.loads((O/'corpus-inventory.json').read_text());B5='9366d9d17aaeac3b4414236468affa650fb3dd27'
read=json.loads((O/'modules/C00/reading-coverage.json').read_text())
full={x['path'] for x in read['records'] if x.get('review_extent')=='full'}
current_cases={
'review/remediation/20261003-prepare/batches/B09/candidate-2/static-cases.json':'43 catalog projections,18 supplementary designs andB013 premises; semantic fields read C00, source reverse review assigned M06/M07/M10',
'review/remediation/20261003-prepare/batches/B17/author-draft-1/static-cases.json':'40 static-case condition records; semantic fields read C00, source reverse review assigned M10/M12B',
'review/wp78-consistency-review-2026-10-03/revision-v3/anomaly-register.json':'20 named reference anomalies still retained by scope-statement; all fact rows read C00; current source checks belong primary modules and junction audit'}
trace={
'review/remediation/20261003-prepare/batches/B16/author-draft-1/traceability.json',
'review/remediation/20261003-prepare/batches/B17/author-draft-1/traceability.json',
'review/remediation/20261003-prepare/batches/B18/author-draft-2/traceability.json',
'review/remediation/20261003-prepare/wp78-junction-successor.tsv',
'review/remediation/20261003-prepare/wp79-source-successor.json',
'review/remediation/20261003-prepare/wp79-config-successor.tsv',
'review/remediation/20261003-prepare/wp79-ui-successor.tsv',
}
counts=collections.Counter()
for r in I['specification_repository']:
 p=r['path'];r['classification_reviewer']='root C00';r['classification_basis']='modules/C00/supplemental-scope.json'
 if p.startswith('deliverables/final-specification-set/'):
  kind='current_formal';why='Authoritative131 at B5; body/table/vector review by explicit module ledger, never inferred from path ownership.'
 elif p.startswith('specs/'):
  kind='current_original_or_effective_supplement';why='All113 original bodies retained for reverse comparison; counterpart or explicit three extra inputs. No exclusion by matching name.'
 elif p in current_cases:kind='effective_supplemental_case_constraints';why=current_cases[p]
 elif p in trace:kind='effective_audit_or_scope_navigation';why='Explicit present formal/audit navigation; old identity/qualification fields are evidence provenance, while any behavior/case constraint must join current domain review.'
 elif p=='audit/source-traceability.md':kind='current_traceability_with_historical_layers';why='Whole file read; T-table anchors/qualification and GR3 successors are audit inputs, not an independent set of accepted B5 rules.'
 elif p.startswith('analysis/inventory/out/'):
  kind='superseded_generated_inventory';why='Whole236-line appendix and exact diff reviewed. One LANGUAGES row is corrected in current specs appendix; output is not same bytes and is not authoritative. No independent correct fact lost;118/default/facility inventory is shared with current counterpart.'
 elif p.startswith('analysis/inventory/') and p.endswith('.py'):
  kind='audit_generation_utility';why='Whole helper body read for provenance, not run; no independent gameplay contract. Default generator target is protected original specs; do not execute it there. Fixed historical output is not current reproduction proof.'
 elif p=='analysis/inventory/wp02-regen-check-2026-09-19.md':
  kind='historical_tool_validation_receipt';why='Whole dated receipt read; old exact equality and validation are limited to its date; current appendix differs in one corrected language row.'
 elif p.startswith(('analysis/','planning/')):
  kind='planning_or_reconnaissance_navigation';why='Domain/feature/package/evidence scope read for independent discovery and retained limits. review-manifest is a historical version/approval register; old hashes/PASS are not current semantic proof.'
 elif p in ['CURRENT-DELIVERY.md','README.md'] or p.startswith('delivery/'):
  kind='delivery_provenance_navigation';why='Current root/fourth entry establishes precedence over frozen old stages; old approved controls and scoped tuples feed separate regression ledger. No gameplay facts are accepted solely from a receipt.'
 elif p in ['AGENTS.md','.gitignore']:
  kind='project_instructions_or_repository_metadata';why='Repository scope/read-only/clean-room constraints or tracking exclusions; no gameplay implementation contract.'
 elif p.startswith('handoff'):
  kind='historical_recovery_or_update_handoff';why='Dated handoffs/preparations superseded by current B5 delivery; cloud-dot README explicitly preserves unfinished preparation as non-accepted. Underlying current113 originals and131 formal bodies are independently reviewed; legacy private proof/extra-reader work is not resumed.'
 elif p.startswith('review/'):
  kind='historical_review_candidate_snapshot_or_receipt';why='Preserved frozen review/remediation history. Current delivery distinguishes old candidates/actual/acceptance; these are not additional current specification copies. Effective explicitly cited cases/AX/scope navigation are exceptions above;229/341/GR3/GR4 binding fields are reused only with exact qualification in regression work.'
 else:
  kind='unclassified';why='Requires manual classification before completion.'
 r['currentness']=kind;r['disposition_reason']=why
 if p in full:r['classification_body_read']='full_by_root_C00'
 else:r['classification_body_read']='see_primary_module_or_specific_disposition; no full-read implication'
 counts[kind]+=1
# Add fixed historical files absent from current tree, without recursively copying packages.
fixed=[]
for commit,path,role in [
('3f521e6dea0b442e4bb174a9715c458416386b37','review/remediation/20261003-prepare/batches/B20/author-draft-1/six-family-fixtures.json','explicit_current_B20-C034_input_fixture'),
('e58486178e746273fb6fab55df00722807f1dc44','review/remediation/20261003-prepare/batches/B21/author-draft-1/static-cases.json','formal_index_explicit_supplemental_static_cases'),
('e58486178e746273fb6fab55df00722807f1dc44','review/remediation/20261003-prepare/batches/B21/author-draft-1/eight-chains.json','retained_scoped_chain_premises_and_provenance_navigation'),
('e58486178e746273fb6fab55df00722807f1dc44','review/remediation/20261003-prepare/batches/B21/author-draft-1/traceability.json','formal_root_explicit_audit_pointer')]:
 b=subprocess.check_output(['git','show',commit+':'+path]);blob=subprocess.check_output(['git','rev-parse',commit+':'+path],text=True).strip()
 fixed.append({'commit':commit,'path':path,'git_blob':blob,'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'role':role,'availability':'available_fixed_git_object','semantic_status':'see C00/M12 and assigned domain ledgers; no inherited PASS','current_tree_presence':pathlib.Path(path).exists()})
I['fixed_historical_effective_supplements']=fixed
I['classification_summary']={'counts':dict(counts),'unclassified_count':counts['unclassified'],'basis':'root direct scope reads + explicit current delivery/accepted-history qualification + exact path exception list','not_semantic_completion':True}
(O/'corpus-inventory.json').write_text(json.dumps(I,ensure_ascii=False,indent=2)+'\n')
scope={'schema_version':'gr5.supplemental-scope.v1','reviewer':'root direct C00','formal_baseline':B5,'scope_completion':False,'classification_counts':dict(counts),'per_path_dispositions':'../../corpus-inventory.json/specification_repository','rules':{'current':'131 formal plus all113 originals and explicitly retained cases/data/audit qualifiers','history':'Not every archived proof/snapshot is another active specification; source-first whole current material review remains mandatory. Exact effective cases, anomaly facts and qualified original controls are retained individually.','identity_reuse':'Existing blob identities reused from fixed inventory; same basename never proves equivalence. Generated settings output demonstrably differs by one corrected language row, so no exact-copy reuse is claimed.','historical_facts':'Old17/23/229/341/54/8/18 are navigation and scope, never R5 capability denominator or blanket PASS.'},'explicit_current_case_files':current_cases,'explicit_audit_navigation':sorted(trace),'fixed_effective_files':fixed,'source_anomalies':{'path':'review/wp78-consistency-review-2026-10-03/revision-v3/anomaly-register.json','ids':['AX'+str(i).zfill(2) for i in range(1,21)],'current_source_review':'assigned by exact fact topic to domain and junction review; not passed by C00 reading'},'pending':['Complete necessary explicit trace/navigation semantic fields, join original113 domain comparison results, and exact history scope joins before declaring corpus closure.'],'findings':[]}
(O/'modules/C00/supplemental-scope.json').write_text(json.dumps(scope,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(counts),ensure_ascii=False));print('fixed',[(x['path'],x['bytes']) for x in fixed])
