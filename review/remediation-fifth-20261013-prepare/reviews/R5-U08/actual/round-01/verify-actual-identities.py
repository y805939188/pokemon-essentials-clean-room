#!/usr/bin/env python3
"""Bounded document/Git identity validation; no behavior program execution."""
import datetime
import hashlib
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[6]
OUT = Path(__file__).resolve().parent
ACTUAL = 'e9f7590e68347849450fd5cbdba538e605cda0a7'
LOCATOR = 'b5531d79979b49e733d589d5353d252bb83aa0cf'
BASE = '59390e301bac9df82083e9b792d7b04d0fe25884'
PASS = 'a4697d7cfffb0b93d46806ad873343b0eda736e8'
REMOTE = '/tmp/r5-u08-remote-readback.git'
INPUT = 'review/remediation-fifth-20261013-prepare/integration/R5-U08/actual-01/actual-review-input.json'
READS = []

def git(*args, remote=False):
    prefix = ['git', '--git-dir=' + REMOTE] if remote else ['git', '-C', str(ROOT)]
    return subprocess.check_output(prefix + list(args))

def identity(data):
    return {'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest(),
            'git_blob': hashlib.sha1(('blob ' + str(len(data)) + '\0').encode() + data).hexdigest()}

def read(commit, path, purpose):
    data = git('show', commit + ':' + path)
    READS.append({'commit': commit, 'path': path, **identity(data), 'method': 'FULL_BYTES', 'purpose': purpose})
    return data

def verify(ref, purpose):
    data = read(ref['commit'], ref['path'], purpose)
    computed = identity(data)
    assert all(computed[k] == ref[k] for k in computed), (ref['path'], computed)
    assert git('rev-parse', ref['commit'] + ':' + ref['path']).decode().strip() == computed['git_blob']
    return {'commit': ref['commit'], 'path': ref['path'], **computed, 'result': 'PASS'}

def write(name, data):
    (OUT / name).write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n')

packet = json.loads(read(LOCATOR, INPUT, 'Current actual dispatch/qualification and fixed subject'))
assert git('rev-parse', ACTUAL + '^{tree}').decode().strip() == packet['actual']['tree']
assert packet['actual']['tree'] == '85673e78ca28ed7dd446ccdf5f0b23557299e1c9'
locator_tree = git('rev-parse', LOCATOR + '^{tree}').decode().strip()
assert locator_tree == 'b71d51d2169c7d3789706afc09ba51acee900dde'
assert git('rev-parse', ACTUAL + ':deliverables/final-specification-set').decode().strip() == packet['actual']['formal_tree']
assert packet['actual']['formal_tree'] == '1046fbb657882e84b3dfc6d017943a9edf7782e5'
read(ACTUAL, 'review/remediation-fifth-20261013-prepare/integration/R5-U08/actual-01/reviewer-entry.md', 'Current bounded review instructions')

targets = []
for row in packet['approved_source_actual_files']:
    source = read(row['source_candidate']['commit'], row['source_candidate']['path'], 'Exact approved source association')
    current = read(ACTUAL, row['path'], 'Actual target bytes, not a candidate verdict transfer')
    assert source == current
    actual_identity = identity(current)
    assert all(actual_identity[k] == row['actual_after'][k] == row['source_candidate'][k] for k in actual_identity)
    before = read(BASE, row['path'], 'Pinned pre-integration target identity')
    assert all(identity(before)[k] == row['base_before'][k] for k in actual_identity)
    targets.append({'actual_commit': ACTUAL, 'path': row['path'], **actual_identity,
                    'source_commit': row['source_candidate']['commit'], 'source_path': row['source_candidate']['path'],
                    'full_source_actual_equality': True, 'result': 'PASS_DOCUMENT_IDENTITY'})
assert len(targets) == 7

new_declarations = [verify(r, 'New actual package payload identity/full read') for r in packet['actual_review_payloads']]
new_declarations.append(verify(packet['current_ledger'], 'Current pending ledger state/full JSON read'))
prior_artifacts = []
for name in ['report', 'gate_results', 'semantic_results', 'preservation_results']:
    prior_artifacts.append(verify(packet['independent_candidate_PASS'][name], 'Exact prior independently qualified evidence reuse'))
old_gates = json.loads(git('show', PASS + ':' + packet['independent_candidate_PASS']['gate_results']['path']))
assert len(old_gates['items']) == 14 and all(r['result'] == 'PASS' for r in old_gates['items'])
assert old_gates['counts']['native_static'] == 410 and old_gates['counts']['reviewer_schema_checks'] == 568
assert old_gates['prior_independent_FAIL_preserved']['old_gate_results'] == {'U08-G03': 'FAIL', 'U08-G09': 'FAIL'}

unchanged_inputs = []
for name, ref in packet['scope_inputs_reused_by_fixed_identity'].items():
    if 'git_blob' not in ref:
        continue
    blob = git('rev-parse', ref['commit'] + ':' + ref['path']).decode().strip()
    current_blob = git('rev-parse', ACTUAL + ':' + ref['path']).decode().strip()
    assert blob == current_blob == ref['git_blob']
    assert int(git('cat-file', '-s', blob)) == ref['bytes']
    unchanged_inputs.append({'name': name, 'fixed_commit': ref['commit'], 'path': ref['path'],
                             'git_blob': blob, 'bytes': ref['bytes'], 'sha256_from_prior_qualified_identity': ref['sha256'],
                             'current_blob_equal': True, 'method': 'EXACT_IMMUTABLE_BLOB_AND_SIZE_REUSE', 'result': 'PASS'})

core_paths = git('diff', '--name-only', BASE, ACTUAL).decode().splitlines()
new_paths = git('diff', '--name-only', BASE, LOCATOR).decode().splitlines()
assert len(core_paths) == 17 and len(new_paths) == 21
assert set(core_paths) == {r['path'] for r in targets + new_declarations}
assert not Path(REMOTE + '/objects/info/alternates').exists()
assert git('rev-parse', LOCATOR + '^{tree}', remote=True).decode().strip() == locator_tree
remote_rows = []
for path in new_paths:
    local = git('show', LOCATOR + ':' + path)
    remote = git('show', LOCATOR + ':' + path, remote=True)
    assert local == remote
    ident = identity(remote)
    assert git('rev-parse', LOCATOR + ':' + path, remote=True).decode().strip() == ident['git_blob']
    remote_rows.append({'path': path, **ident, 'full_remote_byte_match': True,
                        'actual_core_payload': path in core_paths, 'result': 'PASS'})
core_bytes = sum(r['bytes'] for r in remote_rows if r['actual_core_payload'])
assert core_bytes == 2101300
write('actual-input-remote-readback.json', {'schema': 'r5.u08.actual-independent-input-readback.v1',
      'actual': packet['actual'], 'locator': {'commit': LOCATOR, 'tree': locator_tree},
      'direct_remote_fetch': True, 'local_alternates': False, 'method': 'Full git-show bytes of every17 actual core and4 locator new payloads',
      'rows': remote_rows, 'count': len(remote_rows), 'bytes': sum(r['bytes'] for r in remote_rows),
      'actual_core_payloads': len(core_paths), 'actual_core_bytes': core_bytes, 'result': 'PASS', 'new_behavior_execution': 0})
write('identity-results.json', {'schema': 'r5.u08.actual-independent-identity.v1',
      'actual': packet['actual'], 'locator': {'commit': LOCATOR, 'tree': locator_tree}, 'base': BASE,
      'targets': targets, 'new_payload_declarations': new_declarations, 'prior_independent_candidate_artifacts': prior_artifacts,
      'current_unchanged_qualified_inputs': unchanged_inputs, 'old14_candidate_qualified_gates_unchanged': True,
      'original_FAIL_preserved': True, 'native410_and_reviewer568_separate': True,
      'semantic_actual_conclusion': 'Separate fresh bounded judgments are required; identity check does not itself imply semantic PASS.',
      'result': 'PASS_FIXED_ACTUAL_IDENTITIES_AND_PRECISE_REUSE', 'behavior_execution': 0, 'formal_acceptance_written': False, 'CLOSED': 0})
write('root-reading-log.json', {'schema': 'r5.u08.actual-root-reading.v1', 'issued_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
      'fixed_actual': ACTUAL, 'fixed_locator': LOCATOR, 'files': READS,
      'current_remote_full_read': 'actual-input-remote-readback.json', 'immutable_input_identity_only': unchanged_inputs,
      'whole_old_review_or_source_repeated': False, 'same_original_non_author_task': True,
      'canonical_task_echo': '/root', 'actual_UUID_and_model_parameters': 'UNVERIFIED',
      'parent_reference': '01a13807-81f1-7572-898f-31201a4dd026', 'parent_reference_is_UUID_echo': False,
      'new_behavior_execution': 0, 'scope': 'Only current package/full identities and bounded semantics; old qualified scopes precisely reused.'})
print(json.dumps({'result': 'PASS', 'targets': len(targets), 'new_remote_payloads': len(remote_rows),
                  'new_remote_bytes': sum(r['bytes'] for r in remote_rows), 'core_bytes': core_bytes, 'locator_tree': locator_tree}))
