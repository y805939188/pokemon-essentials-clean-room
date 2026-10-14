#!/usr/bin/env python3
"""Fixed-object, three-line and reuse checks; no behavior execution."""
import collections
import hashlib
import json
import pathlib
import subprocess

ROOT = pathlib.Path(__file__).resolve().parents[6]
P = 'review/remediation-fifth-20261013-prepare'
I = P + '/integration/R5-U08/candidate-02'
O = P + '/reviews/R5-U08/candidate/limited-c01-01'
C = '40d4f08f4c3a3325e3f53c2de7dd7597224101e4'
L = '59390e301bac9df82083e9b792d7b04d0fe25884'
OLD = 'f623c2ecdd1c6a52d44145fdc7599624a8c64f7b'
FORMAL = 'e4ea8d03b0e2c7c20fc41fce92f0b2b7b7f02514'
REVIEW = '7533e516bd6e2a34ebeb68af28617c854ac17d50'
LOG = {}


def git(*args):
    return subprocess.check_output(['git', '-C', str(ROOT), *args])


def read(commit, path):
    data = git('show', commit + ':' + path)
    LOG[(commit, path)] = {'commit': commit, 'path': path, 'bytes': len(data),
                          'sha256': hashlib.sha256(data).hexdigest(),
                          'git_blob': hashlib.sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest(),
                          'kind': 'complete_byte_validation_or_structured_input_read'}
    return data


def load(commit, path):
    return json.loads(read(commit, path))


def verify(item):
    read(item['commit'], item['path'])
    result = LOG[(item['commit'], item['path'])].copy()
    result['result'] = 'PASS' if all(result[k] == item[k] for k in ('bytes', 'sha256', 'git_blob')) else 'FAIL'
    assert result['result'] == 'PASS', item['path']
    return result


def save(name, value):
    (ROOT / O / name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')


def main():
    entry = load(L, I + '/limited-review-input.json')
    payloads = [verify(x) for x in entry['fixed_candidate_inputs']]
    old_reports = [verify(x) for x in entry['independent_original_FAIL'].values()
                   if isinstance(x, dict) and 'path' in x]
    target = entry['new_candidate_target']['target_path']
    before = read(FORMAL, target)
    after = read(C, entry['new_candidate_target']['source']['path'])
    a, b = before.splitlines(keepends=True), after.splitlines(keepends=True)
    assert len(a) == len(b)
    lines = [i + 1 for i, (x, y) in enumerate(zip(a, b)) if x != y]
    assert lines == [206, 207, 242] and len(after) - len(before) == 169
    assert read(OLD, target) == before
    rowmap = load(C, I + '/three-row-map.json')
    for op in rowmap['operations']:
        assert a[op['line'] - 1].decode() == op['before_row']
        assert b[op['line'] - 1].decode() == op['after_row']
        assert before.index(op['before_row'].encode()) == op['before_utf8_byte_offset']
        assert after.index(op['after_row'].encode()) == op['after_utf8_byte_offset']
    restored = after
    for op in rowmap['operations']:
        assert restored.count(op['after_row'].encode()) == 1
        restored = restored.replace(op['after_row'].encode(), op['before_row'].encode(), 1)
    assert restored == before
    preservation = load(C, I + '/preservation-and-projection.json')
    shared_old = load(REVIEW, P + '/reviews/R5-U08/candidate/round-01/shared-file-results.json')
    shared_by_path = {x['path']: x for x in shared_old['files']}
    shared_reuse = []
    for row in preservation['unaffected_twenty_shared_full_files']:
        path = row['path']
        blob = git('rev-parse', C + ':' + path).decode().strip()
        assert blob == row['identity']['git_blob'] == shared_by_path[path]['current_identity']['git_blob']
        assert shared_by_path[path]['result'] == 'PASS'
        assert blob == git('rev-parse', OLD + ':' + path).decode().strip()
        shared_reuse.append({'path': path, 'git_blob': blob, 'result': 'PASS_EXACT_UNCHANGED_OLD_SCOPE_REUSE',
                             'prior_review': REVIEW, 'fresh_whole_text_read': False})
    mirror_reuse = []
    for row in preservation['six_administrative_mirrors']:
        source = row['source']
        original = read(source['commit'], source['path'])
        assert original == read(C, source['path'])
        assert LOG[(C, source['path'])]['git_blob'] == source['git_blob']
        mirror_reuse.append({'target': row['target'], 'source_path': source['path'],
                             'git_blob': source['git_blob'], 'result': 'PASS_CANDIDATE_ONLY_EXACT_UNCHANGED_REUSE'})
    assert len(shared_reuse) == 20 and len(mirror_reuse) == 6
    assert git('rev-parse', C + ':deliverables/final-specification-set') == git('rev-parse', FORMAL + ':deliverables/final-specification-set')
    wp = 'deliverables/final-specification-set/user-interface/wp66-a-party-and-summary-ui.md'
    assert read(C, wp) == read(FORMAL, wp) == read(OLD, wp)
    assert a[207] == b[207]
    old_gates = load(REVIEW, P + '/reviews/R5-U08/candidate/round-01/gate-results.json')
    assert [x['id'] for x in old_gates['gates'] if x['result'] == 'FAIL'] == ['U08-G03', 'U08-G09']
    diff = git('diff', '--name-status', '9f19756ab9eb73d94ceb2707ea97bfe0986d43dd', L).decode().splitlines()
    assert len(diff) == 16 and all(x.startswith('A\t' + P + '/') for x in diff)
    value = {'schema': 'independent.r5.u08.limited-identities.v1', 'candidate': C, 'locator': L,
             'candidate_tree': git('rev-parse', C + '^{tree}').decode().strip(),
             'locator_tree': git('rev-parse', L + '^{tree}').decode().strip(),
             'result': 'PASS_DOCUMENT_IDENTITY_AND_REUSE', 'fixed_candidate_payloads': payloads,
             'original_FAIL_evidence_identities': old_reports, 'changed_lines': lines,
             'line_count': len(a), 'delta_bytes': 169, 'all_other_lines_identical': True,
             'inverse_full_file_exact': True, 'A07_unchanged': True, 'WP66_A_unchanged': True,
             'twenty_shared_reuse': shared_reuse, 'six_mirror_reuse': mirror_reuse,
             'candidate_and_locator_additions_only': diff, 'live_formal_tree_unchanged': True,
             'old_92_410_568': 'Exact prior qualified scopes retained; no newly generated/repeated full row review.',
             'old12_gate_reuse': [x for x in old_gates['gates'] if x['result'] == 'PASS'],
             'behavior_execution': 0, 'CLOSED': 0, 'identity_checks_are_semantic_PASS': False}
    save('identity-and-reuse-results.json', value)
    save('root-reading-log.json', {'schema': 'independent.r5.u08.limited-root-reading.v1', 'files': list(LOG.values()),
         'fresh_semantic_ranges': [{'commit': C, 'path': entry['new_candidate_target']['source']['path'], 'lines': [190, 250]},
                                  {'commit': C, 'path': wp, 'lines': [210, 240]}],
         'old_full_source_and_twenty_shared_texts': 'Precisely reuse original review; not repeated global source-first or full-text workflow.',
         'model_and_UUID_actual_echo': 'UNVERIFIED', 'new_behavior_execution': 0})
    print(json.dumps({'three_rows': lines, 'unchanged_shared': len(shared_reuse), 'unchanged_mirrors': len(mirror_reuse),
                      'new_input_payloads': len(diff), 'result': value['result']}))


if __name__ == '__main__':
    main()
