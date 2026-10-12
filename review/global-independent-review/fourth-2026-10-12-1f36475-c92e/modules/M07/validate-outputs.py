"""Validate review artifact structure and anchor presence, never game behavior."""
import json
from pathlib import Path

p = Path(__file__).resolve().parent
root = p.parents[4]
required = ['report.md', 'capabilities.json', 'spec-coverage.json', 'findings.json',
            'regression.json', 'execution.json', 'progress.md']
for name in required:
    assert (p / name).is_file(), name
data = {f.name: json.loads(f.read_text()) for f in p.glob('*.json')}
caps = data['capabilities.json']
ids = {x['capability_id'] for x in caps}
assert len(ids) == len(caps) == 23
assert data['findings.json'] == {'schema_version': '1.0', 'findings': []}
assert data['data-check-results.json']['all_match']
assert data['regression.json'][0]['id'] == 'GR3-M07-001'
identity = data['review-identity.json']
R = Path(identity['source_baseline']['root'])
levels = {'SOURCE_STATIC', 'SPEC_STATIC', 'DERIVED_VECTOR', 'TOOL_VALIDATION',
          'EXECUTED_MODEL', 'EXECUTED_REFERENCE', 'EXECUTED_HOST_OR_DEMO'}
statuses = {'supported', 'partial', 'missing', 'unresolved', 'not_reviewed'}
fields = {'capability_id', 'module', 'description', 'source_anchors', 'spec_anchors',
          'entry_and_preconditions', 'configuration_data_host_limits', 'reviewer',
          'checked_branches_boundaries', 'evidence_level', 'material_availability',
          'status', 'reason', 'related_findings', 'history_links', 'not_checked'}
anchor_count = 0
for c in caps:
    assert fields <= c.keys(), c['capability_id']
    assert c['module'] == 'M07' and c['status'] in statuses
    assert c['evidence_level'] in levels
    assert c['reviewer']['thread_id'] == '01a13008-af4e-7a31-8ab6-9cc778feff78'
    assert c['reviewer']['pid'] == 21530
    assert c['reviewer']['actual_echo'] == 'UNVERIFIED'
    assert c['not_checked']
    for a in c['source_anchors']:
        assert (R / a['path']).is_file(), a
        assert a['commit'] == identity['source_baseline']['commit']
        assert a['lines_or_symbol'] and a['fact']
        anchor_count += 1
    for a in c['spec_anchors']:
        assert (root / a['path']).is_file(), a
        assert a['commit'] == identity['formal_baseline']['commit']
        anchor_count += 1
cov_fields = {'path', 'contracts_checked', 'source_anchors', 'status',
              'support_evidence', 'dependencies', 'unsupported_assertions', 'not_checked'}
for c in data['spec-coverage.json']:
    assert cov_fields <= c.keys()
    assert c['status'] in statuses
    assert (root / c['path']).is_file()
    assert c['not_checked']
scope = data['source-scope.json']
assert len(scope['formal_files']) == 131
assert len({x['path'] for x in scope['formal_files']}) == 131
assert len(scope['reference_files']) == 209
semantic = sum(x['review_status'] == 'read_semantically' for x in scope['reference_files'])
assert semantic == 33
assert data['execution.json']['behavior_execution_count'] == 0
print(json.dumps({'evidence_level': 'TOOL_VALIDATION', 'artifact_structure': 'PASS',
                  'capabilities': len(caps), 'capability_anchors': anchor_count,
                  'spec_coverage_files': len(data['spec-coverage.json']),
                  'formal_inventory': 131, 'source_inventory': 209,
                  'source_semantic_fragments_files': semantic,
                  'new_findings': 0, 'behavior_tests_executed': 0}, ensure_ascii=False))
