"""Structural/path validation of review artifacts. No reference code execution."""
from pathlib import Path
from datetime import datetime, timezone
import json
import subprocess
import sys

out = Path(__file__).resolve().parent
root = out.parents[4]
reference = Path('/Users/dingshinn/Desktop/pokemon-framework-reference/reference/pokemon-essentials')
start = datetime.now(timezone.utc).isoformat()
cmd = [sys.executable, str(out/'build_review.py')]
build = subprocess.run(cmd, cwd=root, text=True, capture_output=True)
assert build.returncode == 0, build.stderr
docs = {p.name: json.loads(p.read_text()) for p in out.glob('*.json')}
caps = docs['capabilities.json']
findings = docs['findings.json']['findings']
coverage = docs['spec-coverage.json']
regression = docs['regression.json']
cap_fields = 'capability_id module description source_anchors spec_anchors entry_and_preconditions configuration_data_host_limits reviewer checked_branches_boundaries evidence_level material_availability status reason related_findings history_links not_checked'.split()
find_fields = 'id title module severity disposition status reviewer category source_baseline source_anchors specification_baseline spec_anchors expected_reference_behavior current_spec_behavior gap preconditions minimal_counterexample normal_case failure_or_boundary_case impact_on_independent_implementation negative_evidence_search proposed_spec_change acceptance_criteria affected_files shared_contracts dependencies related_capabilities related_findings root_cause_group history_links evidence_level execution_status confidence unknowns excluded_claims user_decision_needed review_resolution'.split()
coverage_fields = 'path contracts_checked source_anchors status support_evidence dependencies unsupported_assertions not_checked'.split()
for objects, fields in [(caps,cap_fields),(findings,find_fields),(coverage,coverage_fields)]:
    for obj in objects:assert not (set(fields)-obj.keys()), (obj.get('id',obj.get('path')),set(fields)-obj.keys())
ids = {f['id'] for f in findings}
cap_ids = {c['capability_id'] for c in caps}
assert len(ids)==len(findings)==3
assert len(cap_ids)==len(caps)==24
assert len(regression)==4
assert docs['formal-inventory.json']['count']==131
for c in caps:
    assert c['status'] in ['supported','partial','missing','unresolved','not_reviewed']
    assert set(c['related_findings']) <= ids
for f in findings:
    assert set(f['related_capabilities']) <= cap_ids
    assert f['execution_status']=='NOT_EXECUTED'
    assert f['id'] in docs['negative-evidence.json']
    for q in docs['negative-evidence.json'][f['id']]['searches']:
        assert q['exit_code'] in [0,1]

def check_anchors(anchors, base):
    for anchor in anchors:assert (base/anchor['path']).is_file(), anchor

for c in caps:
    check_anchors(c['source_anchors'],reference)
    check_anchors(c['spec_anchors'],root)
for f in findings:
    check_anchors(f['source_anchors'],reference)
    check_anchors(f['spec_anchors'],root)
for row in coverage:
    assert (root/row['path']).is_file()
    check_anchors(row['source_anchors'],reference)
for row in docs['source-scope.json']['entries']:
    assert (reference/row['path']).is_file()
assert len({row['path'] for row in coverage})==len(coverage)
for name in ['report.md','progress.md']:
    assert (out/name).is_file()
summary = {
 'purpose':'审查产物生成/JSON结构/必需字段/ID关联/源与正式路径存在性校验；不判定行为正确性。',
 'result':'PASS_TOOL_VALIDATION_ONLY','capability_samples':24,
 'capability_statuses':{s:sum(c['status']==s for c in caps) for s in ['supported','partial']},
 'findings':sorted(ids),'spec_coverage_entries':len(coverage),
 'source_scope_entries':len(docs['source-scope.json']['entries']),
 'formal_search_files':131,'historical_recheck_entries':4,
}
end = datetime.now(timezone.utc).isoformat()
execution=docs['execution.json']
execution['actual_executions']=[{
 'evidence_level':'TOOL_VALIDATION','tool':'functions.exec / exec_command / python3',
 'command':[sys.executable,str(Path(__file__).resolve())],
 'nested_generation_command':cmd,'version':sys.version,
 'started_at_utc':start,'finished_at_utc':end,
 'inputs':'M03/build_review.py、M03现有报告、固定B正式文本/固定R路径；生成器的rg只检索文本。',
 'output':summary,'generation_stdout':build.stdout.strip(),'generation_stderr':build.stderr,
 'exit_code':0,
 'side_effects':'仅M03内JSON产物与progress.md；不执行参考、不改正式/历史/全局文件。',
 'not_behavior_execution':True,
}]
(out/'execution.json').write_text(json.dumps(execution,ensure_ascii=False,indent=2)+'\n')
(out/'validation.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n')
(out/'progress.md').write_text('# M03 审查进度\n\nCOMPLETED — 本轮有界双向语义审查与全部产物已完成。\n\n24项能力样本：21 supported_static、3 partial；3项P2/REQUIRED：GR4-M03-001、002、003。四项GR3固定验收核心已定点回查，旧CLOSED身份保持，116新增消费者单列。\n\n来源盘点131路径（38定点语义阅读/90仅盘点/3未解析），正式反证搜索131文件，逐文件覆盖33项。报告含可读未审/缺材料/未执行边界。结构及引用路径校验通过；仅TOOL_VALIDATION，行为执行0。\n\n下一步：交主汇总者接收，并由其安排三项必修的独立针对性反证；本审者停止扩审。\n')
print(json.dumps(summary,ensure_ascii=False))
