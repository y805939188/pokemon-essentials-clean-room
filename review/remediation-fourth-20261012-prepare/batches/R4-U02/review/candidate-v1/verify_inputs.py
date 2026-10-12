#!/usr/bin/env python3
"""Independent immutable-input and scope checks. Does not execute game behavior."""
from pathlib import Path
import datetime
import hashlib
import json
import os
import re
import subprocess

ROOT = Path('/workspace/r4-u02-independent')
OUT = ROOT / 'review/remediation-fourth-20261012-prepare/batches/R4-U02/review/candidate-v1'
PACK = 'review/remediation-fourth-20261012-prepare/'
AUTHOR = PACK + 'batches/R4-U02/author/'
START = '08a57fb55118914a74ac1ffaf617647c01df8938'
BASE = '1f36475d22120a0d1175967d5b17d71fe8311d88'
CAND = 'b1bcab79b02d1dd67cbb300fc52372292edf25a0'
SUCC = '4583350f7b219af3dc82848f07344fd505957a93'
REF = '8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
REF_GIT = '/tmp/r4-u02-independent-reference.git'
REPORT = '130452d902530140331c21064a3188b7887f72ae'


def git(*args, reference=False):
    prefix = ['git', '--git-dir=' + REF_GIT] if reference else ['git', '-C', str(ROOT)]
    return subprocess.check_output(prefix + list(args))


def blob(commit, path, reference=False):
    return git('show', commit + ':' + path, reference=reference)


def data(commit, path):
    return json.loads(blob(commit, path))


def identity(commit, path, reference=False):
    b = blob(commit, path, reference)
    return {'commit': commit, 'path': path, 'bytes': len(b),
            'sha256': hashlib.sha256(b).hexdigest(),
            'git_blob': git('rev-parse', commit + ':' + path, reference=reference).decode().strip(),
            'full_bytes_read': True}


def check_identity(expected, commit=None, reference=False):
    actual = identity(commit or expected['commit'], expected['path'], reference)
    for k in ('bytes', 'sha256', 'git_blob'):
        assert actual[k] == expected[k], (k, actual, expected)
    return actual


def main():
    contract = data(START, PACK + 'tasks/R4-U02/batch-contract.json')
    scope = data(START, PACK + 'tasks/R4-U02/read-scope.json')
    canonical = data(START, PACK + 'tasks/R4-U02/findings-input.json')
    authoritative = data(canonical['authority']['commit'], canonical['authority']['path'])
    records = authoritative['findings'] if isinstance(authoritative, dict) else authoritative
    assert all(f == next(x for x in records if x['id'] == f['id']) for f in canonical['canonical_root_records'])
    trees = {}
    expected_trees = {START: '8fc388710e3433890416f6d01247fd09df9d2ea8',
                      BASE: 'd696e23ce4a0eae12b0bb2a5e74bf9cd4c74764a',
                      CAND: '2c5a2ffafbf17f7894fb0d53d2d1867dab4c425e',
                      REPORT: 'b2677e819a85422c353bd3eac3ff55409698d5d8'}
    for c in [START, BASE, CAND, SUCC, REPORT]:
        trees[c] = git('rev-parse', c + '^{tree}').decode().strip()
        if c in expected_trees:
            assert trees[c] == expected_trees[c]
    reference_tree = git('rev-parse', REF + '^{tree}', reference=True).decode().strip()
    assert reference_tree == '7589c800b61ba13a13040ed0d686979b80a84fd0'
    changed = git('diff', '--name-only', START, CAND).decode().splitlines()
    allowed = set(contract['allowed_formal_write_paths'])
    formal_changed = {p for p in changed if p.startswith('deliverables/')}
    assert formal_changed == allowed and len(allowed) == 8
    assert all(p in allowed or p.startswith(AUTHOR) for p in changed)
    assert git('diff', '--name-only', CAND, SUCC).decode().splitlines() == [AUTHOR + 'candidate-publication.json']
    assert git('rev-parse', SUCC + '^').decode().strip() == CAND
    assert not git('diff', '--name-only', BASE, START, '--', 'deliverables/final-specification-set')
    git('diff', '--check', START, CAND)
    formal = []
    for record in data(CAND, AUTHOR + 'formal-identities.json')['files']:
        before = check_identity(record['before'])
        after = check_identity(record['after'], CAND)
        assert blob(CAND, after['path']) == blob(SUCC, after['path']) == (ROOT / after['path']).read_bytes()
        formal.append({'before': before, 'candidate': after, 'successor_and_worktree_equal': True})
    source = []
    for anchor in scope['source']:
        source.append(check_identity({'path': anchor['path'], 'commit': REF, **anchor['identity']}, reference=True))
    inputs = data(CAND, AUTHOR + 'input-verification.json')
    frozen_files = []
    for rec in inputs['package_inputs'] + inputs['external_handoff_manifest_receipt_full_bytes'] + [inputs['publication_receipt']]:
        frozen_files.append(check_identity(rec))
    freeze = data(inputs['publication_receipt']['commit'], inputs['publication_receipt']['path'])
    assert freeze['task_package_commit'] == START and freeze['author_start_commit'] == START
    assert freeze['task_package_tree'] == trees[START]
    author_files = [identity(SUCC, p) for p in git('ls-tree', '-r', '--name-only', SUCC, AUTHOR).decode().splitlines()]
    acceptance = data(CAND, AUTHOR + 'acceptance-map.json')
    assert len(acceptance['records']) == 3 and sum(len(r['criteria']) for r in acceptance['records']) == 15
    for r in acceptance['records']:
        original = next(f for f in canonical['canonical_root_records'] if f['id'] == r['id'])
        assert [c['complete_criterion'] for c in r['criteria']] == original['acceptance_criteria']
        assert r['preconditions'] == original['preconditions']
        assert r['all_required_refinements'] == original['review_resolution']['independent_counterreview']['required_refinements']
        assert r['independent_verdict'] is None
        for criterion in r['criteria']:
            assert criterion['execution_status'] == 'NOT_EXECUTED_THIS_UPDATE'
            for anchor in criterion['anchors']:
                lines = blob(CAND, anchor['path']).decode().splitlines()
                assert anchor['contains'] in lines[anchor['line'] - 1]
    tests_path = 'deliverables/final-specification-set/test-catalog/engine-overworld-wp11-15-59-60.md'
    tests = blob(CAND, tests_path).decode().splitlines()
    vectors = [r for r in tests if re.match(r'\| GR4-(RM|SF|ER)\d{2} \|', r)]
    assert len(vectors) == 26 and len(set(r.split('|')[1] for r in vectors)) == 26
    assert all(r.endswith('| NOT_EXECUTED |') for r in vectors)
    regression = data(CAND, AUTHOR + 'affected-regression.json')
    old_tests = blob(BASE, tests_path).decode().splitlines()
    protected_rows = []
    for row in regression['protected_rows_checked']:
        token = '| ' + row['id'] + ' |'
        old = next(x for x in old_tests if x.startswith(token))
        new = next(x for x in tests if x.startswith(token))
        assert new == old and hashlib.sha256(new.encode()).hexdigest() == row['row_sha256']
        protected_rows.append(row['id'])
    consumers = []
    for record in regression['unchanged_consumers']:
        consumers.append(check_identity(record))
        assert blob(BASE, record['path']) == blob(CAND, record['path'])
    nav = data(START, PACK + 'tasks/R4-U02/legacy-navigation.json')
    historical = []
    for key in ('selected_original229', 'selected_exact341'):
        for item in nav[key]:
            binding = item['immutable_scope'] if key == 'selected_original229' else item['qualified_scope_binding']
            rec = binding['file_identity']
            historical.append(check_identity(rec))
            obj = data(rec['commit'], rec['path'])
            for part in binding['pointer'].split('/')[1:]:
                obj = obj[int(part)] if isinstance(obj, list) else obj[part]
            digest = hashlib.sha256(json.dumps(obj, ensure_ascii=False, sort_keys=True, separators=(',', ':')).encode()).hexdigest()
            assert digest == binding['object_sha256']
            if key == 'selected_original229':
                assert regression['GIR_FD82_C064']['original_qualified_scope'] == obj
            else:
                assert regression['GIR_FD82_C064']['exact341_qualified_scope'] == obj
                assert regression['GIR_FD82_C064']['exact_tuple'] == item['exact_tuple']
    execution = data(CAND, AUTHOR + 'execution.json')
    assert execution['new_behavior_execution'] == 'NOT_EXECUTED_THIS_UPDATE'
    assert all(execution[k] == 0 for k in ('EXECUTED_REFERENCE', 'EXECUTED_MODEL', 'EXECUTED_HOST_OR_DEMO'))
    check_identity(execution['historical_fourth_review']['identity'])
    check_identity(execution['historical_fourth_review']['M03_own_historical_execution'])
    assert len(execution['historical_fourth_review']['reference_probe_runs']) == 4
    result = {'status': 'PASS_TOOL_VALIDATION_ONLY', 'evidence_level': 'TOOL_VALIDATION',
              'completed_at': datetime.datetime.now(datetime.timezone.utc).isoformat(),
              'reviewer_task': '/root', 'reviewer_platform_thread_id': os.environ.get('CODEX_THREAD_ID', 'UNVERIFIED'),
              'commit_trees': trees, 'reference_commit': REF, 'reference_tree': reference_tree,
              'full_formal_identities': formal, 'source_anchor_full_identities': source,
              'frozen_input_full_identities': frozen_files, 'author_evidence_full_identities': author_files,
              'canonical_findings_equal_authority': True, 'criteria_mapping_count': 15,
              'derived_vectors_count': 26, 'protected_rows_byte_equal': protected_rows,
              'unchanged_consumers': consumers, 'qualified_historical_input_identities': historical,
              'candidate_change_paths': changed, 'execution_status': 'NOT_EXECUTED_THIS_UPDATE',
              'historical_reference_calls': 4, 'new_reference_model_host_calls': 0,
              'not_behavior_pass': True, 'not_semantic_verdict': True,
              'author_validator_not_run': 'It writes author/validation-result.json; reviewer ran this own read-only validator instead.'}
    (OUT / 'input-validation.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({'status': result['status'], 'formal_files': len(formal), 'criteria': 15,
                      'vectors': 26, 'protected_rows': len(protected_rows),
                      'thread_id': result['reviewer_platform_thread_id']}))


if __name__ == '__main__':
    main()
