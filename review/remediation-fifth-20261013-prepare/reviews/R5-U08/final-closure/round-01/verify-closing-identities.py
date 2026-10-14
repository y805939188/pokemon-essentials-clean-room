#!/usr/bin/env python3
"""Limited immutable closing document/Git checks; no behavior execution."""
import datetime
import hashlib
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[6]
OUT = Path(__file__).resolve().parent
CORE = '13fddb0a217b36974c75657aa68da0caf104ee48'
LOCATOR = 'bd9399c30d56640cf4f336acfb71bb9f11ea7393'
ACCEPT = 'b0e5a90fe954a02f81e05c5c0062b977617bd1f0'
ACTUAL = 'e9f7590e68347849450fd5cbdba538e605cda0a7'
REVIEW = 'debf59f3c5370df253706969fd4dd1c103300bf2'
REMOTE = '/tmp/r5-u08-remote-readback.git'
PREFIX = 'review/remediation-fifth-20261013-prepare/'
INPUT = PREFIX + 'integration/R5-U08/final-closure/candidate-01/closing-review-input.json'
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
    ident = identity(data)
    assert all(ident[k] == ref[k] for k in ident), ref['path']
    assert git('rev-parse', ref['commit'] + ':' + ref['path']).decode().strip() == ident['git_blob']
    return {'commit': ref['commit'], 'path': ref['path'], **ident, 'result': 'PASS'}

def write(name, data):
    (OUT / name).write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n')

packet = json.loads(read(LOCATOR, INPUT, 'Fixed closing dispatch and seven limited gates'))
subjects = [packet['closing_candidate_core'], packet['acceptance_baseline'], packet['accepted_actual'], packet['actual_independent_PASS']]
subjects.append({'commit': LOCATOR, 'tree': '31f482807059d97f8f380e977e4627c5b3f8fe5f'})
for subject in subjects:
    assert git('rev-parse', subject['commit'] + '^{tree}').decode().strip() == subject['tree']
assert packet['closing_candidate_core']['commit'] == CORE and packet['acceptance_baseline']['commit'] == ACCEPT
assert git('rev-parse', CORE + ':deliverables/final-specification-set').decode().strip() == '1046fbb657882e84b3dfc6d017943a9edf7782e5'
core_declarations = [verify(r, 'Full new closing payload and declared identity') for r in packet['fixed_closing_core_payloads']]
acceptance_refs = [packet[n] for n in ['unique_U08_acceptance', 'shared21_qualified_receipts', 'effective_current_ledger']]
acceptance_declarations = [verify(r, 'New unique acceptance/qualified receipts/effective ledger fixed identity') for r in acceptance_refs]
proposal = json.loads(git('show', CORE + ':' + packet['exact_closing_status_payload']['path']))
contract = json.loads(git('show', CORE + ':' + packet['activation_contract']['path']))
gate_state = json.loads(git('show', CORE + ':' + packet['preactivation_current_state']['path']))
assert len(proposal['records']) == 92
assert len({r['id'] for r in proposal['records']}) == 92
assert sum(r['severity'] == 'P2' for r in proposal['records']) == 51
assert sum(r['severity'] == 'P3' for r in proposal['records']) == 41
assert all(r['current_effective'] == {'status': 'OPEN_REQUIRED', 'final_CLOSED': False} for r in proposal['records'])
assert all(r['proposed_only_after_valid_activation'] == {'status': 'CLOSED', 'final_CLOSED': True} for r in proposal['records'])
assert all(not r['activation_receipt_issued'] for r in proposal['records'])
assert proposal['effective_CLOSED'] == 0
assert gate_state['effective_counts'] == {'OPEN_REQUIRED': 92, 'CLOSED': 0}
assert proposal['counts']['native_static'] == 410 and proposal['counts']['schema_checks'] == 568
assert proposal['counts']['additional_schema_units'] == 158
assert not contract['activation_issued_now'] and not contract['main_merge_authorized']
assert contract['effective_state_resolution']['new_unreviewed_closing_status_payload_allowed'] is False
activation_path = packet['expected_activation_receipt_path']
assert not git('ls-tree', '-r', '--name-only', CORE, '--', activation_path).strip()
assert not git('ls-tree', '-r', '--name-only', LOCATOR, '--', activation_path).strip()
assert not (ROOT / activation_path).exists()

prior_manifest_path = PREFIX + 'reviews/R5-U08/actual/round-01/review-manifest.json'
prior_manifest = json.loads(read(REVIEW, prior_manifest_path, 'Precise original actual review payload identity reuse, not whole review repetition'))
prior_rows = []
for name in ['report.md', 'gate-results.json', 'semantic-results.json', 'dependency-results.json', 'criteria-results.json', 'boundary-results.json', 'regression-results.json']:
    path = PREFIX + 'reviews/R5-U08/actual/round-01/' + name
    row = next(r for r in prior_manifest['payloads'] if r['path'] == path)
    blob = git('rev-parse', REVIEW + ':' + path).decode().strip()
    assert blob == row['git_blob'] and int(git('cat-file', '-s', blob)) == row['bytes']
    prior_rows.append({'commit': REVIEW, **row, 'method': 'EXACT_PRIOR_INDEPENDENT_MANIFEST_BLOB_SIZE_REUSE', 'result': 'PASS'})

core_paths = git('diff', '--name-only', ACCEPT, CORE).decode().splitlines()
locator_paths = git('diff', '--name-only', CORE, LOCATOR).decode().splitlines()
assert len(core_paths) == 8 and set(core_paths) == {r['path'] for r in core_declarations}
assert len(locator_paths) == 4
assert not Path(REMOTE + '/objects/info/alternates').exists()
assert git('rev-parse', LOCATOR + '^{tree}', remote=True).decode().strip() == subjects[-1]['tree']
assert git('rev-parse', ACCEPT + '^{tree}', remote=True).decode().strip() == packet['acceptance_baseline']['tree']
remote_rows = []
for commit, paths, scope in [(CORE, core_paths, 'CLOSING_CORE'), (LOCATOR, locator_paths, 'CLOSING_LOCATOR'),
                             (ACCEPT, [r['path'] for r in acceptance_refs], 'ACCEPTANCE_PREREQUISITE')]:
    for path in paths:
        local = git('show', commit + ':' + path)
        remote = git('show', commit + ':' + path, remote=True)
        assert remote == local
        ident = identity(remote)
        assert git('rev-parse', commit + ':' + path, remote=True).decode().strip() == ident['git_blob']
        remote_rows.append({'commit': commit, 'path': path, **ident, 'scope': scope, 'full_remote_bytes_match': True, 'result': 'PASS'})
core_bytes = sum(r['bytes'] for r in remote_rows if r['scope'] == 'CLOSING_CORE')
assert core_bytes == 544052
write('closing-input-remote-readback.json', {'schema': 'r5.closing-independent-input-full-readback.v1',
      'closing_core': packet['closing_candidate_core'], 'locator': subjects[-1], 'acceptance': packet['acceptance_baseline'],
      'direct_remote_fetch': True, 'local_alternates': False, 'method': 'Full git-show bytes for8 core,4 locator,3 exact acceptance prerequisite payloads',
      'rows': remote_rows, 'count': len(remote_rows), 'bytes': sum(r['bytes'] for r in remote_rows),
      'closing_core_count': 8, 'closing_core_bytes': core_bytes, 'result': 'PASS', 'new_behavior_execution': 0})
write('identity-results.json', {'schema': 'r5.closing-independent-fixed-identity.v1', 'subjects': subjects,
      'core_payloads': core_declarations, 'acceptance_payloads': acceptance_declarations, 'prior_actual_review_precise_reuse': prior_rows,
      'core_additions_only': core_paths, 'locator_additions_only': locator_paths,
      'state_check': {'records': 92, 'P2': 51, 'P3': 41, 'current_effective_OPEN': 92, 'current_effective_CLOSED': 0,
                      'proposed_CLOSED_only_after_valid_activation': 92, 'activation_receipt_absent': True,
                      'unreviewed_closing_status_payload_permitted': False},
      'result': 'PASS_FIXED_CLOSING_IDENTITIES_AND_PREACTIVATION_STATE',
      'identity_is_semantic_or_activation_PASS': False, 'new_behavior_execution': 0, 'activation_written': False, 'CLOSED_written': 0})
write('root-reading-log.json', {'schema': 'r5.closing-independent-root-reading.v1', 'issued_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
      'fixed_candidate': CORE, 'fixed_locator': LOCATOR, 'fixed_acceptance': ACCEPT, 'files': READS,
      'fresh_limited_structured_reads': ['closing records/current_effective and proposed status objects', 'activation gate/contract/gate-state',
                                        'Unique acceptance and qualified shared receipt/current ledger declared endpoint identities'],
      'old_actual_full_semantic_review_repeated': False, 'same_original_non_author_task': True,
      'canonical_task_echo': '/root', 'actual_UUID_and_model_parameters': 'UNVERIFIED',
      'parent_reference': '01a13807-81f1-7572-898f-31201a4dd026', 'parent_reference_is_UUID_echo': False,
      'new_behavior_execution': 0, 'activation_written': False, 'CLOSED_written': 0})
print(json.dumps({'result': 'PASS', 'core_payloads': 8, 'core_bytes': core_bytes,
                  'remote_payloads': len(remote_rows), 'remote_bytes': sum(r['bytes'] for r in remote_rows), 'effective_CLOSED': 0}))
