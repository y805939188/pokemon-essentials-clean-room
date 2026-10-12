#!/usr/bin/env python3
"""Finite v2 identity/delta checks; no reference, model, or host execution."""
from pathlib import Path
import datetime
import hashlib
import json
import subprocess

ROOT = Path('/workspace/r4-u02-independent-v2')
OUT = ROOT / 'review/remediation-fourth-20261012-prepare/batches/R4-U02/review/candidate-v2'
PACK = 'review/remediation-fourth-20261012-prepare/'
AUTHOR = PACK + 'batches/R4-U02/author/'
CONTRACT = '08a57fb55118914a74ac1ffaf617647c01df8938'
V1 = 'b1bcab79b02d1dd67cbb300fc52372292edf25a0'
V1_SUCCESSOR = '4583350f7b219af3dc82848f07344fd505957a93'
V2 = '46255c6c4445b1f6d0bb18cce850deff85eb82a3'
V2_SUCCESSOR = '7fdec6c45ae190d05578c897477704f797a00e7d'
V1_REPORT = 'be0be4c4c8fb1040b21ec9d3bee6ee270e537457'
REF = '8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
TESTS = 'deliverables/final-specification-set/test-catalog/engine-overworld-wp11-15-59-60.md'


def git(*args):
    return subprocess.check_output(['git', '-C', str(ROOT), *args])


def blob(commit, path):
    return git('show', commit + ':' + path)


def data(commit, path):
    return json.loads(blob(commit, path))


def identity(commit, path):
    b = blob(commit, path)
    return {'commit': commit, 'path': path, 'bytes': len(b),
            'sha256': hashlib.sha256(b).hexdigest(),
            'git_blob': git('rev-parse', commit + ':' + path).decode().strip(),
            'complete_bytes_read': True}


def verify(expected, commit=None):
    actual = identity(commit or expected['commit'], expected['path'])
    for k in ['bytes', 'sha256', 'git_blob']:
        assert actual[k] == expected[k], (k, actual, expected)
    return actual


def main():
    assert git('rev-parse', V2 + '^{tree}').decode().strip() == '34c9a09b2762cfca7160e1fb65d9e2a8dc0de068'
    assert git('rev-parse', V2 + '^').decode().strip() == V1_SUCCESSOR
    assert git('rev-parse', V2_SUCCESSOR + '^').decode().strip() == V2
    assert git('diff', '--name-only', V1, V2, '--', 'deliverables/final-specification-set').decode().splitlines() == [TESTS]
    changed = git('diff', '--name-only', V1_SUCCESSOR, V2).decode().splitlines()
    assert all(p == TESTS or p.startswith(AUTHOR) for p in changed)
    assert git('diff', '--name-only', V2, V2_SUCCESSOR).decode().splitlines() == [AUTHOR + 'candidate-publication-v2.json']
    old = blob(V1, TESTS).splitlines(keepends=True)
    new = blob(V2, TESTS).splitlines(keepends=True)
    assert len(old) == len(new)
    differing = [i + 1 for i, (a, b) in enumerate(zip(old, new)) if a != b]
    assert differing == [521]
    current_row = new[520].decode().rstrip('\n')
    assert current_row.startswith('| GR4-SF04 |') and current_row.endswith('| NOT_EXECUTED |')
    for s in ['(11,10)', 'can_surf=true', '无岩架/冰/瀑布', 'ending_surf保持假', 'SF06']:
        assert s in current_row
    protected_vectors = []
    for row in new:
        if row.startswith((b'| GR4-RM', b'| GR4-SF', b'| GR4-ER')) and not row.startswith(b'| GR4-SF04 |'):
            assert row in old
            protected_vectors.append({'id': row.decode().split('|')[1].strip(),
                                      'row_sha256': hashlib.sha256(row.rstrip(b'\n')).hexdigest(),
                                      'byte_equal_v1': True, 'semantic_verdict_source': 'original v1; not re-reviewed'})
    assert len(protected_vectors) == 25
    contract = data(CONTRACT, PACK + 'tasks/R4-U02/batch-contract.json')
    formal = []
    for path in contract['allowed_formal_write_paths']:
        rec = identity(V2, path)
        rec['unchanged_from_reviewed_v1'] = blob(V1, path) == blob(V2, path)
        assert blob(V2, path) == blob(V2_SUCCESSOR, path) == (ROOT / path).read_bytes()
        formal.append(rec)
    assert sum(r['unchanged_from_reviewed_v1'] for r in formal) == 7
    for pair in data(V2, AUTHOR + 'formal-identities.json')['files']:
        verify(pair['after'], V2)
    pub = data(V2_SUCCESSOR, AUTHOR + 'candidate-publication-v2.json')
    assert pub['candidate_commit'] == V2 and pub['candidate_tree'] == '34c9a09b2762cfca7160e1fb65d9e2a8dc0de068'
    assert pub['candidate_parent'] == V1_SUCCESSOR and pub['new_behavior_execution'] == 'NOT_EXECUTED_THIS_UPDATE'
    previous_report = data(V1_REPORT, PACK + 'batches/R4-U02/review/candidate-v1/findings.json')
    assert [r['result'] for r in previous_report['findings']] == ['PASS', 'REQUIRES_CHANGES', 'PASS']
    assert len(previous_report['required_changes']) == 1 and previous_report['required_changes'][0]['id'] == 'R4-U02-CV1-001'
    revision = data(V2, AUTHOR + 'revision-sf04.json')
    assert revision['formal_change']['after_row'] == current_row
    assert revision['formal_change']['before_row'] == old[520].decode().rstrip('\n')
    reviewed_prior = [verify(revision[k]) for k in ['fixed_review_report', 'fixed_review_findings']]
    acceptance_v1 = data(V1, AUTHOR + 'acceptance-map.json')
    acceptance_v2 = data(V2, AUTHOR + 'acceptance-map.json')
    binding = acceptance_v2['records'][1]['criteria'][1]['review_followup']
    assert binding['complete_updated_row'] == current_row and binding['line'] == 521
    assert binding['row_sha256'] == hashlib.sha256(current_row.encode()).hexdigest()
    assert binding == revision['formal_change']['updated_binding']
    untouched_mapping = json.loads(json.dumps(acceptance_v2))
    del untouched_mapping['records'][1]['criteria'][1]['review_followup']
    assert untouched_mapping == acceptance_v1
    counter_v1 = data(V1, AUTHOR + 'counterevidence.json')
    counter_v2 = data(V2, AUTHOR + 'counterevidence.json')
    followup = counter_v2.pop('SF04_independent_review_followup')
    assert counter_v2 == counter_v1 and followup['updated_vector'] == binding
    assert followup['required_change'] == previous_report['required_changes'][0]
    old_qualified_evidence = []
    for path in [AUTHOR + 'execution.json', AUTHOR + 'affected-regression.json',
                 AUTHOR + 'integration-proposals.json', AUTHOR + 'source-and-consumer-read-log.json']:
        assert blob(V1, path) == blob(V2, path)
        old_qualified_evidence.append(identity(V2, path))
    evidence_paths = git('ls-tree', '-r', '--name-only', V2_SUCCESSOR, AUTHOR).decode().splitlines()
    for p in evidence_paths:
        if p.endswith('.json'):
            data(V2_SUCCESSOR, p)
    git('diff', '--check', V1_SUCCESSOR, V2)
    result = {'status': 'PASS_FINITE_TOOL_VALIDATION_ONLY', 'evidence_level': 'TOOL_VALIDATION',
              'completed_at': datetime.datetime.now(datetime.timezone.utc).isoformat(),
              'candidate_commit': V2, 'candidate_tree': '34c9a09b2762cfca7160e1fb65d9e2a8dc0de068',
              'author_publication_commit': V2_SUCCESSOR,
              'author_publication_tree': git('rev-parse', V2_SUCCESSOR + '^{tree}').decode().strip(),
              'formal_identities': formal, 'formal_changed_lines': differing,
              'current_sf04_complete_row': current_row, 'protected_vectors': protected_vectors,
              'v1_review_identity_verified': reviewed_prior,
              'unchanged_mapping_except_sf04_followup': True,
              'unchanged_counterevidence_except_sf04_followup': True,
              'unchanged_qualified_evidence': old_qualified_evidence,
              'author_input_full_identities': [identity(V2_SUCCESSOR, p) for p in evidence_paths],
              'candidate_delta_paths': changed,
              'new_behavior_execution': 'NOT_EXECUTED_THIS_UPDATE',
              'historical_four_reference_calls': 'qualified history preserved; not rerun',
              'full_batch_semantic_review_repeated': False, 'not_behavior_pass': True,
              'semantic_verdict': 'Separate independent SF04/source assessment required.'}
    (OUT / 'input-validation.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({'status': result['status'], 'changed_formal_lines': differing,
                      'unchanged_formal_files': 7, 'unchanged_vectors': 25}))


if __name__ == '__main__':
    main()
