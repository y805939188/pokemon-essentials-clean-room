"""Extract finite historical scopes and current navigation; no semantic verdicts generated."""
from reg_io import *
from functools import lru_cache
import re,hashlib,difflib
@lru_cache(None)
def obj(c,p):return jfixed(p,c)
def at(o,p):
 for k in p.strip('/').split('/') if p.strip('/') else []:o=o[int(k)] if isinstance(o,list) else o[k.replace('~1','/').replace('~0','~')]
 return o
fields={
'B01':'accepted_candidate_paths accepted_integration_public_repairs candidate_independent_basis',
'B02':'approved_scope current_formal_navigation_contribution_verified',
'B03':'clauses actual_project_evidence actual_static_case_evidence',
'B04':'local_scope actual_formal_clause_bindings static_designs_not_executed fresh_reference_ranges',
'B05':'candidate_scope formal_byte_evidence tests',
'B06':'formal_clause_bindings static_row_bindings',
'B07':'contribution_scope actual_body_and_static_locators actual_related_file_identity_bindings independent_reference_locators candidate_static_ids',
'B08':'review_topic actual_clause_locator static_locator actual_static_row_identities preserved_inputs_and_boundary',
'B09':'title formal_clause_locators static_catalog_ids source_evidence',
'B10':'actual_formal_evidence static_test_IDs independent_actual_result',
'B11':'scope project_evidence source_evidence static_design_ids legal_static_positive neighboring_reverse',
'B12':'formal_identities actual_minimum_judgment actual_legal_positive_reverse_and_old_regression_judgment static_test_ids_not_executed',
'B13':'actual_current_formal_locators actual_static_test_navigation_not_executed counterexamples_reverse_cross_surface_current',
'B14':'current_formal_locations current_test_rows static_test_ids_not_executed independent_legal_input independent_ordered_result neighbor_reverse_contrast source_bindings NOT_AFFECTED_asserted',
'B15':'scope actual_formal_locator static_test_ids_not_executed effective_premises minimum_counterexample candidate_static_assessment_verbatim candidate_legal_contrast_or_resolution_verbatim',
'B16':'scope actual_formal_locators actual_catalog_locator legal_premises normal_legal_static_positive minimum_counterexample neighboring_reverse',
'B17':'scope qualified_premises ACT_locators static_test_ids_NOT_EXECUTED normal_positive counterexample neighboring_reverse',
'B18':'scope qualified_premises exact_ACT_locators normal_positive counterexample neighboring_reverse',
'B19':'scope qualified_premises normal_positive counterexample neighboring_reverse original_formal_catalog_trace_coherence',
'B20':'actual_clauses_and_cases actual_payloads normal_consumer_conditions reverse_regression_and_limits',
'B21':'independent_semantic_basis actual_specific_judgment evidence'}
D=json.loads((HERE/'regression-legacy-scope.json').read_text())
for r in D['contributions']:
 b=r['batch_owner'];bind=r['historical_identity_scope_reuse']['fixed_scoped_disposition'];raw=at(obj(bind['commit'],bind['path']),bind['pointer'])
 selected={k:raw[k] for k in fields[b].split() if k in raw}
 r['accepted_local_scope_fields']=selected
 r['accepted_local_scope_extraction']={'binding':bind,'fields':list(selected),'status':'historical_identity_scope_reuse_only','excluded':'Historical verdict/quality conclusion not current evidence; scope prose containing historical judgments remains attributed historical scope.'}
 if b=='B19':
  p=raw['original_formal_catalog_trace_coherence']['actual_internal_semantic_check']
  selected['exact_local_semantic_scope']=at(obj(bind['commit'],p['path']),p['pointer'])
 def paths(x):
  out=[]
  if isinstance(x,dict):
   for k,v in x.items():
    if k in ['original','original_affected_paths','remaining_contributors','remaining_paths_or_obligations']:continue
    out+=paths(v)
  elif isinstance(x,list):
   for v in x:out+=paths(v)
  elif isinstance(x,str):out+=re.findall(r'(?:deliverables/final-specification-set|specs)/[^\s\"\[\]{}<>;；,，]+?\.md',x)
  return list(dict.fromkeys(out))
 ps=paths(selected)+paths(r['original_contribution_scope'])
 if b=='B01' and r['id'] in ['GIR-FD82-001','WP80-B02-R02']:ps+=['deliverables/final-specification-set/scope-statement.md','deliverables/final-specification-set/README.md']
 ps=list(dict.fromkeys(ps))
 r['current_B5_navigation']['candidate_paths']=[p for p in ps if p.startswith('deliverables/')]
 r['current_B5_navigation']['original_paths']=[p for p in ps if p.startswith('specs/')]
 r['current_B5_navigation']['mapping_status']='scope_extracted_current_clause_join_pending'
for r in D['controls']:
 r['current_B5_paths']=list(dict.fromkeys(p for c in D['contributions'] if c['id']==r['id'] for p in c['current_B5_navigation']['candidate_paths']))
 r['scoped_contribution_pointers']=[{'record_key':c['record_key'],'pointer':'/contributions/'+str(i)} for i,c in enumerate(D['contributions']) if c['id']==r['id']]
save('regression-legacy-scope.json',D)
print('Enriched',len(D['contributions']),'finite scope records; no semantic statuses promoted.')
for b in fields:
 rs=[r for r in D['contributions'] if r['batch_owner']==b]
 print(b,len(rs),'without formal paths',[(r['id']) for r in rs if not r['current_B5_navigation']['candidate_paths']])
