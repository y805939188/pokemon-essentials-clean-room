"""Artifact-only checks. No reference program is loaded or executed."""
import json
import sys
import subprocess
from datetime import datetime, timezone
from pathlib import Path

OUT=Path(__file__).resolve().parent
ROOT=OUT.parents[4]
REF=Path('/Users/dingshinn/Desktop/pokemon-framework-reference/reference/pokemon-essentials')
START=datetime.now(timezone.utc).isoformat()
command=['python3',str(Path(__file__).resolve().relative_to(ROOT))]
req_cap='capability_id module description source_anchors spec_anchors entry_and_preconditions configuration_data_host_limits reviewer checked_branches_boundaries evidence_level material_availability status reason related_findings history_links not_checked'.split()
req_finding='id title module severity disposition status reviewer category source_baseline source_anchors specification_baseline spec_anchors expected_reference_behavior current_spec_behavior gap preconditions minimal_counterexample normal_case failure_or_boundary_case impact_on_independent_implementation negative_evidence_search proposed_spec_change acceptance_criteria affected_files shared_contracts dependencies related_capabilities related_findings root_cause_group history_links evidence_level execution_status confidence unknowns excluded_claims user_decision_needed review_resolution'.split()
req_spec='path contracts_checked source_anchors status support_evidence dependencies unsupported_assertions not_checked'.split()
statuses={'supported','partial','missing','unresolved','not_reviewed'}
levels={'SOURCE_STATIC','SPEC_STATIC','DERIVED_VECTOR','TOOL_VALIDATION','EXECUTED_MODEL','EXECUTED_REFERENCE','EXECUTED_HOST_OR_DEMO'}
categories={'缺能力','事实错误','数学错误','状态或时序错误','交界矛盾','数据或资源契约缺口','实现信息不足','净室问题','其他'}
files=['capabilities.json','spec-coverage.json','findings.json','regression.json','execution.json','source-scope.json','transitions-inventory.json','negative-searches.json']
d={n:json.loads((OUT/n).read_text()) for n in files}
caps=d['capabilities.json'];findings=d['findings.json']['findings'];specs=d['spec-coverage.json']
capids={c['capability_id'] for c in caps};fids={f['id'] for f in findings}
assert len(capids)==len(caps) and len(fids)==len(findings)
assert len(list((ROOT/'deliverables/final-specification-set').rglob('*.md')))==131
for c in caps:
    assert set(req_cap)<=c.keys(),c['capability_id']
    assert c['status'] in statuses
    assert set(c['related_findings'])<=fids
    assert c['reviewer']=='M10 / thread 01a12ff1-a1b1-7212-84b3-c3fdcd6552a9'
for f in findings:
    assert set(req_finding)<=f.keys(),f['id']
    assert f['severity'] in {'P1','P2','P3'} and f['disposition'] in {'REQUIRED','OPTIONAL','UNRESOLVED','NO_REQUIRED_REVISION'}
    assert f['category'] in categories and f['status'] in statuses
    assert set(f['related_capabilities'])<=capids
for s in specs:
    assert set(req_spec)<=s.keys(),s['path']
    assert s['status'] in statuses and (ROOT/s['path']).is_file()
    assert set(s['unsupported_assertions'])<=fids
anchor_count=0
def visit(x):
    global anchor_count
    if isinstance(x,dict):
        if 'evidence_level' in x:
            val=x['evidence_level'];val=[val] if isinstance(val,str) else val
            assert set(val)<=levels,val
        if {'path','commit','lines_or_symbol','fact'}<=x.keys():
            base=ROOT if x['path'].startswith('deliverables/') else REF
            assert (base/x['path']).is_file(),x['path']
            anchor_count+=1
        for v in x.values():visit(v)
    elif isinstance(x,list):
        for v in x:visit(v)
for x in d.values():visit(x)
assert len(d['regression.json'])==4
assert all(x['historical_status_preserved']=='CLOSED' for x in d['regression.json'])
ti=d['transitions-inventory.json']
assert ti['concrete_effect_count']==23 and ti['compatibility_name_count']==35
assert len({n for x in ti['effects'] for n in x['compatibility_names']})==35
for x in d['source-scope.json']['files']:assert (REF/x['path']).is_file()
check=subprocess.run(['git','diff','--exit-code','--','AGENTS.md','deliverables/final-specification-set'],cwd=ROOT,text=True,capture_output=True)
assert check.returncode==0,check.stdout+check.stderr
summary={'result':'PASS_TOOL_VALIDATION_ONLY','json_files':len(files),'capabilities':len(caps),
 'findings':len(findings),'spec_coverage_rows':len(specs),'regression_rows':4,
 'anchor_path_checks':anchor_count,'formal_tracked_diff_exit_code':check.returncode,
 'concrete_effects':23,'compatibility_names':35,'behavior_execution_count':0}
END=datetime.now(timezone.utc).isoformat()
receipt={'evidence_level':'TOOL_VALIDATION','tool':'exec_command / Python',
 'command':command,'version':sys.version,'started_at':START,'finished_at':END,
 'inputs':files,'stdout':summary,'stderr':'','exit_code':0,
 'side_effects':['M10/validation-result.json','M10/execution.json.actual_executions'],
 'not_a_behavior_test':True}
(OUT/'validation-result.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n')
execution=d['execution.json'];execution['actual_executions'].append(receipt)
(OUT/'execution.json').write_text(json.dumps(execution,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(summary,ensure_ascii=False))
