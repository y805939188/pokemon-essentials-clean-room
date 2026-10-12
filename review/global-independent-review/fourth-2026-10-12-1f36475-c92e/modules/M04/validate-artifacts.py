from pathlib import Path
import json
D=Path('review/global-independent-review/fourth-2026-10-12-1f36475-c92e/modules/M04')
R=Path('/Users/dingshinn/Desktop/pokemon-framework-reference/reference/pokemon-essentials')
need=['report.md','capabilities.json','spec-coverage.json','findings.json','regression.json','execution.json','progress.md']
for n in need: assert (D/n).is_file() and (D/n).stat().st_size>0,n
for p in D.glob('*.json'): json.loads(p.read_text())
caps=json.loads((D/'capabilities.json').read_text())
spec=json.loads((D/'spec-coverage.json').read_text())
finds=json.loads((D/'findings.json').read_text())['findings']
levels={'SOURCE_STATIC','SPEC_STATIC','DERIVED_VECTOR','TOOL_VALIDATION','EXECUTED_MODEL','EXECUTED_REFERENCE','EXECUTED_HOST_OR_DEMO'}
status={'supported','partial','missing','unresolved','not_reviewed'}
capfields='capability_id module description source_anchors spec_anchors entry_and_preconditions configuration_data_host_limits reviewer checked_branches_boundaries evidence_level material_availability status reason related_findings history_links not_checked'.split()
ffields='id title module severity disposition status reviewer category source_baseline source_anchors specification_baseline spec_anchors expected_reference_behavior current_spec_behavior gap preconditions minimal_counterexample normal_case failure_or_boundary_case impact_on_independent_implementation negative_evidence_search proposed_spec_change acceptance_criteria affected_files shared_contracts dependencies related_capabilities related_findings root_cause_group history_links evidence_level execution_status confidence unknowns excluded_claims user_decision_needed review_resolution'.split()
sfields='path contracts_checked source_anchors status support_evidence dependencies unsupported_assertions not_checked'.split()
cids={c['capability_id'] for c in caps}; fids={f['id'] for f in finds}
assert len(cids)==len(caps) and len(fids)==len(finds)
for obj,fields in [(x,capfields) for x in caps]+[(x,ffields) for x in finds]+[(x,sfields) for x in spec]:
 assert not set(fields)-obj.keys(),set(fields)-obj.keys()
 if 'evidence_level' in obj:assert set(obj['evidence_level'])<=levels
 if obj in caps or obj in spec:assert obj['status'] in status
 for a in obj.get('source_anchors',[]):assert (R/a['path']).is_file(),a
 for a in obj.get('spec_anchors',[]):assert Path(a['path']).is_file(),a
for c in caps:assert set(c['related_findings'])<=fids
for f in finds:
 assert set(f['related_capabilities'])<=cids
 assert f['category'] in {'缺能力','事实错误','数学错误','状态或时序错误','交界矛盾','数据或资源契约缺口','实现信息不足','净室问题','其他'}
 assert f['severity'] in {'P1','P2','P3'}
 assert f['disposition'] in {'REQUIRED','OPTIONAL','UNRESOLVED','NO_REQUIRED_REVISION'}
 assert f['reviewer']['thread_id']=='01a12fdc-618e-7ea1-be11-c267b26fdb3d'
for s in spec: assert Path(s['path']).is_file()
assert len(spec)==13 and len(caps)==26 and len(finds)==1
print(json.dumps({'result':'STRUCTURE_AND_PATHS_VALID','required_artifacts':7,'capabilities':len(caps),'spec_coverage_records':len(spec),'finding_ids':sorted(fids),'behavior_test':False},ensure_ascii=False))
