import json,re
from pathlib import Path
from collections import Counter
P=Path(__file__).parent
R=Path('/Users/dingshinn/Desktop/pokemon-framework-reference/reference/pokemon-essentials')
B='1f36475d22120a0d1175967d5b17d71fe8311d88'
required=['report.md','capabilities.json','spec-coverage.json','findings.json','regression.json','execution.json','progress.md']
for name in required: assert (P/name).is_file(),name
for path in P.glob('*.json'): json.loads(path.read_text())
caps=json.loads((P/'capabilities.json').read_text()); coverage=json.loads((P/'spec-coverage.json').read_text()); ff=json.loads((P/'findings.json').read_text())
capfields='capability_id module description source_anchors spec_anchors entry_and_preconditions configuration_data_host_limits reviewer checked_branches_boundaries evidence_level material_availability status reason related_findings history_links not_checked'.split()
findfields='id title module severity disposition status reviewer category source_baseline source_anchors specification_baseline spec_anchors expected_reference_behavior current_spec_behavior gap preconditions minimal_counterexample normal_case failure_or_boundary_case impact_on_independent_implementation negative_evidence_search proposed_spec_change acceptance_criteria affected_files shared_contracts dependencies related_capabilities related_findings root_cause_group history_links evidence_level execution_status confidence unknowns excluded_claims user_decision_needed review_resolution'.split()
evidence={'SOURCE_STATIC','SPEC_STATIC','DERIVED_VECTOR','TOOL_VALIDATION','EXECUTED_MODEL','EXECUTED_REFERENCE','EXECUTED_HOST_OR_DEMO'}
statuses={'supported','partial','missing','unresolved','not_reviewed'}
categories={'缺能力','事实错误','数学错误','状态或时序错误','交界矛盾','数据或资源契约缺口','实现信息不足','净室问题','其他'}
capids={c['capability_id'] for c in caps};findids={f['id'] for f in ff['findings']}
assert len(capids)==len(caps)
assert ff['schema_version']=='1.0'
anchor_count=0
for c in caps:
 assert all(k in c for k in capfields)
 assert c['status'] in statuses and c['evidence_level'] in evidence
 assert c['reviewer']=='M12 / thread 01a12ffe-6148-76d0-8038-a1eb8e8bf390'
 assert set(c['related_findings'])<=findids
 for a in c['source_anchors']+c['spec_anchors']:
  root=Path('.') if a.get('commit')==B else R
  f=root/a['path'];assert f.is_file(),str(f)
  loc=a['lines_or_symbol']
  for start,end in re.findall(r'(?<!\d)(\d+)–(\d+)(?!\d)',loc):
   assert 1<=int(start)<=int(end)<=len(f.read_text(errors='replace').splitlines()), (str(f),loc)
  anchor_count+=1
for f in ff['findings']:
 assert all(k in f for k in findfields)
 assert f['category'] in categories and f['evidence_level'] in evidence
 assert f['severity'] in {'P1','P2','P3'} and f['disposition'] in {'REQUIRED','OPTIONAL','UNRESOLVED','NO_REQUIRED_REVISION'}
 assert set(f['related_capabilities'])<=capids
for c in coverage:
 assert all(k in c for k in 'path contracts_checked source_anchors status support_evidence dependencies unsupported_assertions not_checked'.split())
 assert Path(c['path']).is_file() and c['status'] in statuses
scope=json.loads((P/'source-scope.json').read_text());assert len(scope['files'])==432
for row in scope['files']:assert (R/row['path']).is_file()
formal=json.loads((P/'formal-inventory.json').read_text());assert len(formal['files'])==131
assert sum(x['role']=='primary_M12' for x in formal['files'])==11
rr=json.loads((P/'regression.json').read_text());assert {x['id'] for x in rr}=={'GR3-M12-001','GR3-M12-002'}
print(json.dumps({'result':'PASS_STRUCTURAL_ONLY','required_artifacts':7,'capabilities':len(caps),'capability_statuses':dict(Counter(x['status'] for x in caps)),'spec_coverage_rows':len(coverage),'findings':len(ff['findings']),'source_paths':len(scope['files']),'formal_paths':len(formal['files']),'checked_anchor_paths_and_numeric_ranges':anchor_count,'debug_source_count':sum(x['path'].startswith('Data/Scripts/020_Debug/') for x in scope['files']),'meaning':'JSON/required fields/IDs/path and line-range checks only; not semantic or behavior test'},ensure_ascii=False,indent=2))
