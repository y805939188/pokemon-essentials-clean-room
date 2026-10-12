"""Read-only structure and anchor checks. No reference code is imported or executed."""
from pathlib import Path
import collections
import json
import re

HERE = Path(__file__).resolve().parent
WORKSPACE = HERE.parents[4]
REFERENCE = Path('/Users/dingshinn/Desktop/pokemon-framework-reference/reference/pokemon-essentials')
SOURCE_COMMIT = '8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
SPEC_COMMIT = '1f36475d22120a0d1175967d5b17d71fe8311d88'
THREAD = '01a12ff3-bed1-77a0-a54b-3045c1f98e88'
LEVELS = {'SOURCE_STATIC', 'SPEC_STATIC', 'DERIVED_VECTOR', 'TOOL_VALIDATION',
          'EXECUTED_MODEL', 'EXECUTED_REFERENCE', 'EXECUTED_HOST_OR_DEMO'}
STATUSES = {'supported', 'partial', 'missing', 'unresolved', 'not_reviewed'}
required = ['report.md', 'capabilities.json', 'spec-coverage.json', 'findings.json',
            'regression.json', 'execution.json', 'progress.md']
for name in required:
    assert (HERE / name).is_file(), name
objects = {p.name: json.loads(p.read_text()) for p in HERE.glob('*.json')}
caps = objects['capabilities.json']
capfields = {'capability_id', 'module', 'description', 'source_anchors', 'spec_anchors',
             'entry_and_preconditions', 'configuration_data_host_limits', 'reviewer',
             'checked_branches_boundaries', 'evidence_level', 'material_availability',
             'status', 'reason', 'related_findings', 'history_links', 'not_checked'}
ids = set()
anchors_checked = 0
for cap in caps:
    assert capfields <= cap.keys(), cap['capability_id']
    assert re.fullmatch(r'GR4-CAP-M09-\d{3}', cap['capability_id'])
    assert cap['capability_id'] not in ids
    ids.add(cap['capability_id'])
    assert cap['reviewer']['thread_id'] == THREAD
    assert cap['module'] == 'M09'
    assert cap['evidence_level'] in LEVELS
    assert cap['status'] in STATUSES
    assert cap['execution_status'] == 'NOT_EXECUTED'
    assert cap['source_anchors'] and cap['spec_anchors']
    for field, base, commit in [('source_anchors', REFERENCE, SOURCE_COMMIT),
                                ('spec_anchors', WORKSPACE, SPEC_COMMIT)]:
        for anchor in cap[field]:
            target = base / anchor['path']
            assert target.is_file(), target
            assert anchor['commit'] == commit
            nlines = len(target.read_text().splitlines())
            loc = anchor['lines_or_symbol']
            # For source anchors, only numeric locations are used here.
            if field == 'source_anchors':
                nums = [int(n) for n in re.findall(r'\d+', loc)]
                assert nums and all(1 <= n <= nlines for n in nums), (target, loc, nlines)
            else:
                for match in re.finditer(r'L(\d+)(?:[–-](\d+))?', loc):
                    assert 1 <= int(match.group(1)) <= nlines, (target, loc)
                    if match.group(2):
                        assert int(match.group(1)) <= int(match.group(2)) <= nlines
            anchors_checked += 1
coverage = objects['spec-coverage.json']
assert len({x['path'] for x in coverage}) == len(coverage)
for row in coverage:
    assert {'path','contracts_checked','source_anchors','status','support_evidence',
            'dependencies','unsupported_assertions','not_checked'} <= row.keys()
    assert (WORKSPACE / row['path']).is_file(), row['path']
    assert row['status'] in STATUSES
    for contract in row['contracts_checked']:
        assert contract['capability_id'] in ids
findings = objects['findings.json']
assert findings == {'schema_version': '1.0', 'findings': []}
assert objects['regression.json'] == []
for row in objects['derived-vectors.json']:
    assert row['related_capability'] in ids
    assert row['evidence_level'] == 'DERIVED_VECTOR'
    assert row['execution_status'] == 'NOT_EXECUTED'
scope = objects['source-scope.json']
for row in scope['files']:
    assert (REFERENCE / row['path']).is_file()
    assert row['review_state'] in {'read_semantically','inventoried_only','not_reviewed'}
assert len({x['path'] for x in scope['files']}) == len(scope['files'])
assert sum(x['group'] == 'primary' for x in scope['files']) == 41
for query in objects['search-evidence.json']:
    assert query['files_in_scope'] == 131
    assert query['new_missing_or_contradiction_asserted'] is False
# Verify the declared formal domain contains all 15 primary documents.
formal = WORKSPACE / 'deliverables/final-specification-set'
owned = [p for p in formal.rglob('*.md')
         if re.match(r'wp(?:51|52|53|54|55|56|57|58)(?:-|\.)', p.name)]
assert len(owned) == 15
assert {str(p.relative_to(WORKSPACE)) for p in owned} <= {x['path'] for x in coverage}
assert len(list(formal.rglob('*.md'))) == 131
print(json.dumps({'result':'PASS_STRUCTURE_ONLY','capabilities':len(caps),
                  'capability_status_counts':dict(collections.Counter(c['status'] for c in caps)),
                  'spec_coverage_files':len(coverage),
                  'spec_coverage_status_counts':dict(collections.Counter(c['status'] for c in coverage)),
                  'primary_source_files':41,'inventoried_source_and_data_files':len(scope['files']),
                  'derived_vectors_not_executed':len(objects['derived-vectors.json']),
                  'new_findings':0,'regression_required_items':0,
                  'source_and_spec_anchor_references_checked':anchors_checked,
                  'behavior_tests_executed':0,'side_effects':'none; read-only validation'},
                 ensure_ascii=False))
