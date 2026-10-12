#!/usr/bin/env python3
"""Verify this frozen integration and reused evidence; never execute behavior."""
from pathlib import Path
import datetime
import hashlib
import json
import subprocess

ROOT = Path('/workspace/r4-u02-independent-actual')
OUT = ROOT / 'review/remediation-fourth-20261012-prepare/batches/R4-U02/review/actual-v1'
PACK = 'review/remediation-fourth-20261012-prepare/'
REG = PACK + 'registration/R4-U02/'
ACTUAL = '8a61dc3e4e123ac0a734793dffc9261f9911b7a6'
TASK = '1784673abf1024b1eb5b265ad548280ff4713f2b'
PARENT = 'e6d147c613b7456ff8fa267ce78432a63ae84014'
CAND = '46255c6c4445b1f6d0bb18cce850deff85eb82a3'
BASE = '1f36475d22120a0d1175967d5b17d71fe8311d88'
U01 = '1ec8655fc3186ad88e3fb1ff1700540eb33d41ff'


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


def check(record, commit):
    actual = identity(commit, record['path'])
    for k in ['bytes', 'sha256', 'git_blob']:
        assert record[k] == actual[k], (k, record['path'])
    return actual


def main():
    trees = {ACTUAL: '20a0d63b352b80f1d8aae9b3d3e8a5819b93b115',
             TASK: '777c66a65bb18e841cee813240b5fe53619d0803',
             CAND: '34c9a09b2762cfca7160e1fb65d9e2a8dc0de068'}
    for c, t in trees.items():
        assert git('rev-parse', c + '^{tree}').decode().strip() == t
    assert git('rev-parse', ACTUAL + '^').decode().strip() == PARENT
    handoff = data(TASK, REG + 'actual-review-handoff.json')
    integration = data(TASK, REG + 'integration-check.json')
    handshake = data(TASK, REG + 'wp59-handshake.json')
    assert handoff['actual_commit'] == ACTUAL and handoff['actual_tree'] == trees[ACTUAL]
    assert handoff['candidate']['commit'] == CAND and handoff['formal_write_paths'] == []
    assert not git('diff', '--name-only', ACTUAL, TASK, '--', 'deliverables/final-specification-set')
    accept_path = PACK + 'registration/R4-U01/acceptance.json'
    acceptance = data(PARENT, accept_path)
    assert acceptance['status'] == 'ACCEPTED_SCOPED' and acceptance['effective'] is True
    assert len(acceptance['accepted_finding_ids']) == 5 and acceptance['CLOSED'] is False
    assert acceptance['actual']['commit'] == U01
    assert blob(PARENT, accept_path) == blob(ACTUAL, accept_path) == blob(TASK, accept_path)
    u01_paths = {r['path'] for r in acceptance['formal_file_identities']}
    u02_paths = set(handoff['formal_read_paths'])
    assert len(u01_paths) == 4 and len(u02_paths) == 8 and not u01_paths & u02_paths
    assert set(git('diff', '--name-only', PARENT, ACTUAL, '--', 'deliverables/final-specification-set').decode().splitlines()) == u02_paths
    candidate_patch = git('diff', '--binary', BASE, CAND, '--', *sorted(u02_paths))
    actual_patch = git('diff', '--binary', PARENT, ACTUAL, '--', *sorted(u02_paths))
    assert candidate_patch == actual_patch
    actual_paths = git('ls-tree', '-r', '--name-only', ACTUAL, 'deliverables/final-specification-set').decode().splitlines()
    assert len(actual_paths) == 131
    inventory = {r['path']: r for r in integration['formal_file_identities']}
    assert set(inventory) == set(actual_paths)
    counts = {'U02_v2_exact_candidate': 0, 'U01_accepted_exact_bytes': 0, 'unchanged_B_exact_bytes': 0}
    formal = []
    for path in actual_paths:
        if path in u02_paths:
            origin, qualified = CAND, 'U02_v2_exact_candidate'
        elif path in u01_paths:
            origin, qualified = U01, 'U01_accepted_exact_bytes'
        else:
            origin, qualified = BASE, 'unchanged_B_exact_bytes'
        assert inventory[path]['qualification'] == qualified
        rec = check(inventory[path], ACTUAL)
        assert blob(ACTUAL, path) == blob(origin, path) == blob(TASK, path)
        assert (ROOT / path).read_bytes() == blob(ACTUAL, path)
        rec.update({'qualification': qualified, 'byte_equal_origin_commit': origin,
                    'semantic_read': 'Only named U02 clauses/current shared consumer ranges; other files integrity only.'})
        counts[qualified] += 1
        formal.append(rec)
    assert list(counts.values()) == [8, 4, 119]
    copied = []
    for rec in integration['copied_evidence_exact_bytes']:
        actual = check(rec, ACTUAL)
        assert blob(ACTUAL, rec['path']) == blob(rec['origin_commit'], rec['path']) == blob(TASK, rec['path'])
        actual['byte_equal_origin_commit'] = rec['origin_commit']
        copied.append(actual)
    assert len(copied) == 36
    review_root = PACK + 'batches/R4-U02/review/'
    v1 = data(ACTUAL, review_root + 'candidate-v1/findings.json')
    v2 = data(ACTUAL, review_root + 'candidate-v2/findings.json')
    assert v1['result'] == 'REQUIRES_CHANGES' and v2['result'] == 'CANDIDATE_PASS_SCOPED'
    assert all(x['latest_candidate_result'] == 'PASS' for x in v2['findings'])
    assert sum(len(x['criteria']) for x in v2['findings']) == 15
    assert all(c['result'] == 'PASS' for x in v2['findings'] for c in x['criteria'])
    tests_path = 'deliverables/final-specification-set/test-catalog/engine-overworld-wp11-15-59-60.md'
    tests = blob(ACTUAL, tests_path).decode().splitlines()
    vectors = [x for x in tests if x.startswith(('| GR4-RM', '| GR4-SF', '| GR4-ER'))]
    assert len(vectors) == 26 and all(x.endswith('| NOT_EXECUTED |') for x in vectors)
    assert tests[520] == integration['SF04_actual_row']
    assert 'can_surf=true' in tests[520] and 'SF06' in tests[520]
    consumers = [check(rec, ACTUAL) for rec in handoff['required_shared_consumers']]
    for rec in handshake['consumer_identities']:
        check(rec, ACTUAL)
    wp59 = 'deliverables/final-specification-set/engine-overworld/wp59-world-time-weather-field-moves.md'
    def time_section(commit):
        text = blob(commit, wp59).decode()
        return text[text.index('## 3. '):text.index('## 4. ')]
    assert time_section(ACTUAL) == time_section(BASE) == time_section(PARENT)
    source_tree = subprocess.check_output(['git', '--git-dir=/tmp/r4-u02-independent-reference.git',
                                          'rev-parse', '8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b^{tree}'], text=True).strip()
    assert source_tree == '7589c800b61ba13a13040ed0d686979b80a84fd0'
    git('diff', '--check', PARENT, ACTUAL)
    result = {'status': 'PASS_ACTUAL_INTEGRITY_TOOL_VALIDATION_ONLY', 'evidence_level': 'TOOL_VALIDATION',
              'completed_at': datetime.datetime.now(datetime.timezone.utc).isoformat(),
              'actual_commit': ACTUAL, 'actual_tree': trees[ACTUAL], 'task_publication_commit': TASK,
              'task_publication_tree': trees[TASK], 'candidate_commit': CAND,
              'candidate_tree': trees[CAND], 'integration_parent': PARENT,
              'U01_dependency': {'receipt': identity(PARENT, accept_path), 'status': 'ACCEPTED_SCOPED',
                                 'accepted_actual': U01, 'accepted_ids': acceptance['accepted_finding_ids'],
                                 'CLOSED': False, 'not_reaccepted_by_U02_reviewer': True},
              'formal_counts': counts, 'formal_full_identities': formal,
              'eight_file_complete_candidate_to_actual_equality': True,
              'actual_formal_delta_exact_candidate_patch': True,
              'candidate_evidence_copies_full_identities': copied,
              'required_shared_consumer_identities': consumers,
              'WP59_time_calendar_section_exact_base_and_U01_parent': True,
              'WP59_new_SURF_clause_scope': 'Independent current semantic handshake in assessments/wp59-handshake.json; U01 signature not extended.',
              'criteria_latest_candidate_PASS': 15, 'vectors_NOT_EXECUTED': 26,
              'SF04_actual_row': tests[520], 'v1_historical_RC_preserved': True,
              'new_behavior_execution': 'NOT_EXECUTED_THIS_UPDATE', 'historical_reference_calls': 4,
              'source_tree': source_tree, 'not_behavior_pass': True, 'not_semantic_verdict': True,
              'global_semantic_review_repeated': False, 'historical_admin_acceptance_reperformed': False}
    (OUT / 'validation-result.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({'status': result['status'], 'formal': counts, 'evidence_copies': len(copied),
                      'criteria': 15, 'vectors_unexecuted': 26}))


if __name__ == '__main__':
    main()
