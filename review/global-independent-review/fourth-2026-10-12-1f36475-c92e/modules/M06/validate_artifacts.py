"""Validate review artifact structure and local links; never execute reference logic."""
import json
import re
import sys
from pathlib import Path
from collections import Counter

OUT = Path(__file__).resolve().parent
ROOT = OUT.parents[4]
REF = Path('/Users/dingshinn/Desktop/pokemon-framework-reference/reference/pokemon-essentials')
required = ['report.md','capabilities.json','spec-coverage.json','findings.json','regression.json','execution.json','progress.md']
for n in required:
    assert (OUT/n).is_file(), n
objects = {p.name:json.loads(p.read_text()) for p in OUT.glob('*.json')}
caps=objects['capabilities.json']
findings=objects['findings.json']['findings']
assert objects['findings.json']['schema_version']=='1.0'
ids=[c['capability_id'] for c in caps]
assert len(ids)==len(set(ids))
fids=[f['id'] for f in findings]
assert len(fids)==len(set(fids))
evidence={'SOURCE_STATIC','SPEC_STATIC','DERIVED_VECTOR','TOOL_VALIDATION','EXECUTED_MODEL','EXECUTED_REFERENCE','EXECUTED_HOST_OR_DEMO'}
categories={'缺能力','事实错误','数学错误','状态或时序错误','交界矛盾','数据或资源契约缺口','实现信息不足','净室问题','其他'}
statuses={'supported','partial','missing','unresolved','not_reviewed'}
cap_fields='capability_id module description source_anchors spec_anchors entry_and_preconditions configuration_data_host_limits reviewer checked_branches_boundaries evidence_level material_availability status reason related_findings history_links not_checked'.split()
finding_fields='id title module severity disposition status reviewer category source_baseline source_anchors specification_baseline spec_anchors expected_reference_behavior current_spec_behavior gap preconditions minimal_counterexample normal_case failure_or_boundary_case impact_on_independent_implementation negative_evidence_search proposed_spec_change acceptance_criteria affected_files shared_contracts dependencies related_capabilities related_findings root_cause_group history_links evidence_level execution_status confidence unknowns excluded_claims user_decision_needed review_resolution'.split()
spec_fields='path contracts_checked source_anchors status support_evidence dependencies unsupported_assertions not_checked'.split()
for c in caps:
    assert all(k in c for k in cap_fields), c['capability_id']
    assert c['status'] in statuses
    assert set(c['evidence_level'])<=evidence
    assert all(f in fids for f in c['related_findings'])
    assert c['reviewer']=='M06 / thread 01a12fe0-a4a3-75a0-87bd-03c04ac176c8'
for f in findings:
    assert all(k in f for k in finding_fields), f['id']
    assert f['category'] in categories
    assert f['severity'] in {'P1','P2','P3'}
    assert f['disposition'] in {'REQUIRED','OPTIONAL','UNRESOLVED','NO_REQUIRED_REVISION'}
    assert set(f['evidence_level'])<=evidence
    assert all(c in ids for c in f['related_capabilities'])
for s in objects['spec-coverage.json']:
    assert all(k in s for k in spec_fields), s['path']
    assert s['status'] in statuses
    assert (ROOT/s['path']).is_file()

anchors=[]
for c in caps:
    for a in c['source_anchors']:
        assert (REF/a['path']).is_file(), a
        assert a['commit']=='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
        locus=a['lines_or_symbol']
        prefix=re.split(r'\s*\(',locus)[0]
        if re.fullmatch(r'[\d,–\- ]+',prefix):
            nums=[int(n) for n in re.findall(r'\d+',prefix)]
            assert min(nums)>=1 and max(nums)<=len((REF/a['path']).read_text().splitlines()),a
        anchors.append((a['path'],locus))
    for a in c['spec_anchors']:
        assert (ROOT/a['path']).is_file(),a
        assert a['commit']=='1f36475d22120a0d1175967d5b17d71fe8311d88'
assert objects['formal-scope.json']['formal_count']==131
assert objects['formal-scope.json']['direct_domain_count']==14
for h in objects['negative-evidence-search.json']['hits']:
    ls=(ROOT/h['path']).read_text().splitlines()
    assert all(1<=n<=len(ls) for n in h['line_numbers'])
assert objects['negative-evidence-search.json']==findings[0]['negative_evidence_search']
for name in ['report.md','progress.md']:
    for target in re.findall(r'\]\(([^)]+)\)',(OUT/name).read_text()):
        assert (OUT/target).is_file(),(name,target)
for p in OUT.glob('*.json'):
    assert '"evidence_level": "NOT_EXECUTED"' not in p.read_text()
print(json.dumps({'result':'PASS_ARTIFACT_STRUCTURE_ONLY','python':sys.version.splitlines()[0], 'required_files':len(required), 'json_files':len(objects),'capabilities':len(caps),'capability_status':dict(Counter(c['status'] for c in caps)),'findings':fids,'spec_coverage_records':len(objects['spec-coverage.json']),'unique_source_anchors':len(set(anchors)),'formal_search_files':131,'behavior_tests_executed':0},ensure_ascii=False))
