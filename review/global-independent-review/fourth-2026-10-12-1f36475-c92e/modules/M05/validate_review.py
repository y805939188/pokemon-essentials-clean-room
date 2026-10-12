from pathlib import Path
import json, sys, subprocess
from collections import Counter
from datetime import datetime,timezone
out=Path(__file__).resolve().parent
root=Path.cwd(); ref=Path('/Users/dingshinn/Desktop/pokemon-framework-reference/reference/pokemon-essentials')
started=datetime.now(timezone.utc).isoformat()
mandatory=['report.md','capabilities.json','spec-coverage.json','findings.json','regression.json','execution.json','progress.md']
for name in mandatory:assert (out/name).is_file(), name
objects={p.name:json.loads(p.read_text()) for p in out.glob('*.json')}
cap=objects['capabilities.json']; cov=objects['spec-coverage.json']; fi=objects['findings.json']['findings'];reg=objects['regression.json']
allowed_status={'supported','partial','missing','unresolved','not_reviewed'}
levels={'SOURCE_STATIC','SPEC_STATIC','DERIVED_VECTOR','TOOL_VALIDATION','EXECUTED_MODEL','EXECUTED_REFERENCE','EXECUTED_HOST_OR_DEMO'}
cat={'缺能力','事实错误','数学错误','状态或时序错误','交界矛盾','数据或资源契约缺口','实现信息不足','净室问题','其他'}
ids={x['capability_id'] for x in cap};fids={x['id'] for x in fi}
assert len(cap)==len(ids)==29
assert len(cov)==len({x['path'] for x in cov})==131
assert len(objects['source-scope.json']['entries'])==432
assert objects['source-scope.json']['counts']['pbs']==73
for entry in objects['source-scope.json']['entries']:assert (ref/entry['path']).is_file(),entry['path']
for c in cap:
 assert c['status'] in allowed_status
 assert set(c['evidence_level'])<=levels
 assert c['reviewer']['thread_id']=='01a12fdc-b1dc-7f62-8311-aa6a002b9432'
 assert c['execution_status']=='NOT_EXECUTED'
 assert set(c['related_findings'])<=fids
 for a in c['source_anchors']:assert (ref/a['path']).is_file(), a
 for a in c['spec_anchors']:assert (root/a['path']).is_file(), a
for s in cov:
 assert s['status'] in allowed_status
 assert (root/s['path']).is_file()
 assert all(k in s for k in ['contracts_checked','source_anchors','status','support_evidence','dependencies','unsupported_assertions','not_checked'])
required='id title module severity disposition status reviewer category source_baseline source_anchors specification_baseline spec_anchors expected_reference_behavior current_spec_behavior gap preconditions minimal_counterexample normal_case failure_or_boundary_case impact_on_independent_implementation negative_evidence_search proposed_spec_change acceptance_criteria affected_files shared_contracts dependencies related_capabilities related_findings root_cause_group history_links evidence_level execution_status confidence unknowns excluded_claims user_decision_needed review_resolution'.split()
for f in fi:
 assert all(k in f for k in required),set(required)-set(f)
 assert f['category'] in cat
 assert f['severity'] in ['P1','P2','P3']
 assert f['disposition'] in ['REQUIRED','OPTIONAL','UNRESOLVED','NO_REQUIRED_REVISION']
 assert set(f['related_capabilities'])<=ids
 assert set(f['evidence_level'])<=levels
 assert f['reviewer']['module']=='M05'
for r in reg:
 assert r['id'] in ['GR3-M05-001','GR3-M05-002']
 assert r['execution_status']=='NOT_EXECUTED'
 assert r['source_anchors'] and r['current_file_anchors']
# 验证脚本仅检查产物结构、存在的路径和枚举/交叉引用，不运行行为模型。
tracked_diff=subprocess.check_output(['git','diff','--name-only','HEAD','--'],text=True).splitlines()
assert not tracked_diff,tracked_diff
result={'validation':'PASS','json_files_parsed':len(objects),'capabilities':len(cap),'capability_status_counts':dict(Counter(c['status'] for c in cap)),'formal_files_inventoried':len(cov),'formal_status_counts':dict(Counter(c['status'] for c in cov)),'source_inventory_counts':objects['source-scope.json']['counts'],'finding_ids':sorted(fids),'regression_ids':[r['id'] for r in reg],'tracked_diff_paths':tracked_diff,'behavior_executions':0}
print(json.dumps(result,ensure_ascii=False))
finished=datetime.now(timezone.utc).isoformat()
e=objects['execution.json']
e['actual_executions']=e.get('actual_executions',[])+[{'evidence_level':'TOOL_VALIDATION','purpose':'核对M05审查产物JSON字段、枚举、源/规格路径、交叉引用和tracked差异；非语义测试。','tool':'exec_command / Python standard library','command':'python3 review/global-independent-review/fourth-2026-10-12-1f36475-c92e/modules/M05/validate_review.py','version':'Python '+sys.version.split()[0],'git_version':subprocess.check_output(['git','--version'],text=True).strip(),'started_at':started,'finished_at':finished,'input':'本目录JSON和必需产物；只读当前正式/参考路径存在性及git diff --name-only HEAD','output':result,'exit_code':0,'side_effects':['仅写本目录execution.json记录本次结构验证；不执行参考，不改正式/参考/历史或存档。'],'behavior_test':False}]
(out/'execution.json').write_text(json.dumps(e,ensure_ascii=False,indent=2)+'\n')
