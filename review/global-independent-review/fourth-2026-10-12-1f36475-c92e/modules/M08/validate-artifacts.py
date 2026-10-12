"""Read-only artifact/schema checks; no reference or behavior execution."""
from pathlib import Path
import json

out = Path(__file__).resolve().parent
workspace = Path.cwd()
reference = Path('/Users/dingshinn/Desktop/pokemon-framework-reference/reference/pokemon-essentials')
required = ['report.md', 'capabilities.json', 'spec-coverage.json', 'findings.json',
            'regression.json', 'execution.json', 'progress.md']
for name in required:
    assert (out / name).is_file(), name
objects = {p.name: json.loads(p.read_text()) for p in out.glob('*.json')}
caps = objects['capabilities.json']
coverage = objects['spec-coverage.json']
assert len({c['capability_id'] for c in caps}) == len(caps)
fields = {'capability_id', 'module', 'description', 'source_anchors', 'spec_anchors',
          'entry_and_preconditions', 'configuration_data_host_limits', 'reviewer',
          'checked_branches_boundaries', 'evidence_level', 'material_availability',
          'status', 'reason', 'related_findings', 'history_links', 'not_checked'}
levels = {'SOURCE_STATIC', 'SPEC_STATIC', 'DERIVED_VECTOR', 'TOOL_VALIDATION',
          'EXECUTED_MODEL', 'EXECUTED_REFERENCE', 'EXECUTED_HOST_OR_DEMO'}
statuses = {'supported', 'partial', 'missing', 'unresolved', 'not_reviewed'}
for c in caps:
    assert fields <= c.keys(), c['capability_id']
    assert c['status'] in statuses
    assert set(c['evidence_level']) <= levels
    assert c['reviewer']['thread_id'] == '01a12fed-322b-7010-9c6b-24c58c272a4d'
    for a in c['source_anchors']:
        assert (reference / a['path']).is_file(), a
        assert a['commit'] == '8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
    for a in c['spec_anchors']:
        assert (workspace / a['path']).is_file(), a
        assert a['commit'] == '1f36475d22120a0d1175967d5b17d71fe8311d88'
for c in coverage:
    assert {'path', 'contracts_checked', 'source_anchors', 'status', 'support_evidence',
            'dependencies', 'unsupported_assertions', 'not_checked'} <= c.keys()
    assert c['status'] in statuses
    assert (workspace / c['path']).is_file()
assert len(objects['source-scope.json']['formal_inventory']) == 131
formal = list((workspace / 'deliverables/final-specification-set').rglob('*.md'))
assert len(formal) == 131
covered = {Path(c['path']).name for c in coverage}
for p in formal:
    if p.name.startswith(('wp43-', 'wp44-', 'wp45-', 'wp46-', 'wp47-', 'wp48-', 'wp49-', 'wp50-')):
        assert p.name in covered, p
assert objects['findings.json'] == {'schema_version': '1.0', 'findings': []}
assert len(objects['regression.json']) == 1
assert objects['regression.json'][0]['id'] == 'GR3-M08-001'
print(json.dumps({'result': 'PASS_STRUCTURE_ONLY', 'capability_samples': len(caps),
                  'spec_files_scoped': len(coverage), 'formal_files_inventoried': len(formal),
                  'findings': 0, 'behavior_tests_executed': 0}, ensure_ascii=False))
