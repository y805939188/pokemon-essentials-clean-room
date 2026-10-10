#!/usr/bin/env python3
"""New B13 ACT review metadata only. No source/game/vector/historical code execution."""
import collections
import csv
import difflib
import hashlib
import io
import json
import re
import subprocess
from pathlib import Path

BASE = '8e67f780c204d593d89f364f585d2c6c2fe74631'
CAND = 'db9e6ed1997efe5bf94dac952aad44fd3b9ebd21'
ACT = 'd81562bfe0e79ca4df3233ada38fa09e800bdafc'
PACKET = '996e4f04bcc34b992c9cc4d25db9548850266a06'
ADMIN = '231c9f25df4dd64961fb9290ff52302782a9fdb8'
FULL = 'a8c819a28588fd0d52f344189fd9348a1252350c'
PEER = '2570ca6dc893cc6bfb1320ef9f2513b5618f6a26'
B = 'review/remediation/20261003-prepare/batches/B13/'
ROOT = 'review/remediation/20261003-prepare/'
OUT = Path(B + 'integration-review-1')

def git(*args):
    return subprocess.check_output(['git', *args])

def sha(data):
    return hashlib.sha256(data).hexdigest()

def objsha(value):
    # Same immutable JSON object serialization used by the qualified controls.
    return sha(json.dumps(value, ensure_ascii=False, sort_keys=True,
                          separators=(',', ':')).encode())

def blob(commit, path):
    return git('show', f'{commit}:{path}')

def J(commit, path):
    return json.loads(blob(commit, path))

def save(name, value):
    (OUT / name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')

def tree(commit):
    result = {}
    for item in git('ls-tree', '-rz', '--full-tree', commit).split(b'\0'):
        if not item:
            continue
        info, path = item.split(b'\t', 1)
        mode, kind, oid = info.decode().split()
        result[path.decode()] = {'mode': mode, 'type': kind, 'git_blob': oid}
    return result

trees = {c: tree(c) for c in [BASE, CAND, ACT, PACKET, ADMIN, FULL, PEER]}

def binding(commit, path):
    data = blob(commit, path)
    if commit not in trees:
        trees[commit] = tree(commit)
    return dict(commit=commit, path=path, **trees[commit][path],
                sha256=sha(data), bytes=len(data))

def check_binding(b, actual_commit=None, actual_path=None):
    current = binding(actual_commit or b['commit'], actual_path or b['path'])
    for key in ['git_blob', 'sha256', 'bytes', 'mode']:
        if key in b:
            assert current[key] == b[key], (b['path'], key, current[key], b[key])
    return current

def pointer(value, p):
    for key in p.strip('/').split('/'):
        if key == '':
            continue
        key = key.replace('~1', '/').replace('~0', '~')
        value = value[int(key)] if isinstance(value, list) else value[key]
    return value

def verify_pointer(b):
    check_binding(b)
    return pointer(J(b['commit'], b['path']), b.get('pointer', ''))

dispatch = J(PACKET, B + 'actual-freeze-1/full-actual-review-dispatch.json')
assert dispatch['reviewed_actual_commit'] == ACT
assert git('rev-parse', ACT + '^{tree}').decode().strip() == dispatch['reviewed_actual_tree']
assert git('rev-parse', CAND + '^{tree}').decode().strip() == dispatch['candidate_tree']
assert dispatch['formal_accepted_predecessor'] == BASE
assert dispatch['administrative_predecessor'] == ADMIN
assert dispatch['contributions'] == 8 and dispatch['primary_minimum'] == 5
assert dispatch['formal_outputs'] == 11 and dispatch['output_directory'] == str(OUT) + '/'

streams = []
changes = {}
for label, start, length, digest, count in [
    ('accepted-predecessor-to-actual', BASE, 22882597,
     'b06a8747eb313d0e27803ba86d37d031c95e708bd981ebddc301c6998b1f72d5', 215),
    ('candidate-to-actual', CAND, 16259629,
     '6c28b82aa419abc0b6546f1f304edea54f9f69ba6ea220b66030b3d9f58057ef', 97),
]:
    args = ['diff', '--no-ext-diff', '--no-textconv', '--binary', '--full-index', start, ACT]
    data = git(*args)
    assert len(data) == length and sha(data) == digest
    packet_path = B + 'actual-freeze-1/' + label + '.full.patch'
    assert data == blob(PACKET, packet_path)
    (OUT / (label + '.full.patch')).write_bytes(data)
    before = trees[start]
    after = trees[ACT]
    rows = []
    for path in sorted(before.keys() | after.keys()):
        if before.get(path) != after.get(path):
            rows.append({'path': path, 'before': before.get(path), 'after': after.get(path)})
    assert len(rows) == count
    assert all(r['after'] is not None for r in rows)
    changes[label] = rows
    streams.append({'name': label, 'command': ['git', *args], 'from': start, 'to': ACT,
                    'bytes': len(data), 'sha256': sha(data), 'changed_paths': len(rows),
                    'full_unfiltered': True, 'all_bytes_equal_dispatch_stream': True,
                    'dispatch_binding': binding(PACKET, packet_path)})

formal_manifest = J(ACT, B + 'integration-stage-1/formal-copy-identities.json')
formal = [r['path'] for r in formal_manifest['records']]
assert len(formal) == len(set(formal)) == 11
assert sum(p.startswith('specs/') for p in formal) == 4
outputs = []
for r in formal_manifest['records']:
    p = r['path']
    check_binding(r['frozen_candidate'])
    check_binding(r['predecessor'])
    assert r['frozen_candidate']['commit'] == CAND
    assert r['predecessor']['commit'] == BASE
    assert trees[CAND][p] == trees[ACT][p]
    assert blob(CAND, p) == blob(ACT, p)
    outputs.append({'path': p, 'accepted_predecessor': binding(BASE, p),
                    'candidate': binding(CAND, p), 'actual': binding(ACT, p),
                    'candidate_actual_whole_bytes_mode_type_equal': True})

public = [ROOT + p for p in ['approval-ledger.tsv', 'traceability-successor.tsv',
                             'final-integration-review.md']]
preservation = []
for start, allowed in [(BASE, set(formal + public)), (CAND, set(public))]:
    checked = [p for p in trees[start] if p not in allowed]
    differences = [p for p in checked if trees[start][p] != trees[ACT].get(p)]
    assert differences == []
    preservation.append({'from': start, 'to': ACT, 'existing_tree_entries': len(trees[start]),
                         'excluded_exact_paths': sorted(allowed), 'checked_paths': len(checked),
                         'mode_type_blob_differences': differences,
                         'independent_whole_tree_inventory': True})

copies = J(ACT, B + 'integration-stage-1/published-artifact-copies.json')['records']
assert len(copies) == len(set(r['path'] for r in copies)) == 153
copy_evidence = []
for r in copies:
    origin = check_binding(r)
    integrated = check_binding(r, ACT)
    assert blob(r['commit'], r['path']) == blob(ACT, r['path'])
    copy_evidence.append({'source': origin, 'actual': integrated, 'whole_bytes_and_mode_equal': True})
copy_paths = {r['path'] for r in copies}
classified = []
for r in changes['accepted-predecessor-to-actual']:
    p = r['path']
    if p in formal:
        category = 'eleven_B13_formal_payloads'
        origin = CAND
    elif p in public:
        category = 'three_public_pending_registration_changes'
        origin = None
    elif p in copy_paths:
        category = '153_byte_exact_published_artifact_copies'
        origin = next(x['commit'] for x in copies if x['path'] == p)
    elif p.startswith(B + 'integration-stage-1/'):
        category = 'twelve_new_G_metadata_records'
        origin = None
    elif trees[ADMIN].get(p) == trees[ACT].get(p):
        category = 'existing_administrative_record_byte_copy'
        origin = ADMIN
        assert blob(ADMIN, p) == blob(ACT, p)
    else:
        raise AssertionError(('unclassified path', p))
    classified.append(dict(r, category=category, source_commit=origin))
category_counts = dict(collections.Counter(r['category'] for r in classified))
assert category_counts == {
    'eleven_B13_formal_payloads': 11,
    'three_public_pending_registration_changes': 3,
    '153_byte_exact_published_artifact_copies': 153,
    'twelve_new_G_metadata_records': 12,
    'existing_administrative_record_byte_copy': 36,
}
assert [r['path'] for r in changes['candidate-to-actual'] if r['before']] == sorted(public)
packet_changes = [p for p in trees[PACKET].keys() | trees[ACT].keys()
                  if trees[PACKET].get(p) != trees[ACT].get(p)]
assert len(packet_changes) == 11
assert all(p.startswith(B + 'actual-freeze-1/') and p not in trees[ACT] for p in packet_changes)

previous_metadata_path = B + 'candidate-review-2/independent-metadata.json'
previous_coverage_path = B + 'candidate-review-2/control-coverage.json'
assert blob(FULL, previous_metadata_path) == blob(ACT, previous_metadata_path)
assert blob(FULL, previous_coverage_path) == blob(ACT, previous_coverage_path)
prior = J(FULL, previous_metadata_path)
prior_cov = J(FULL, previous_coverage_path)
assert prior_cov['reviewed_NEW'] == CAND and prior_cov['verdict'] == 'PASS'
assert prior_cov['contributions'] == 8 and prior_cov['primary'] == 5
inputs = []
for item in prior['all_52_input_bindings']:
    b = item['binding']
    actual = check_binding(b)
    if b['path'] not in trees[ACT]:
        inputs.append({'binding': b, 'source': actual, 'actual': None,
                       'source_binding_independently_equal': True,
                       'immutable_external_commit_input_not_an_ACT_tree_path': True})
        continue
    current = binding(ACT, b['path'])
    same = blob(b['commit'], b['path']) == blob(ACT, b['path'])
    if not same:
        assert b['path'] in set(formal + public)
    inputs.append({'binding': b, 'source': actual, 'actual': current,
                   'source_binding_independently_equal': True,
                   'source_ACT_whole_bytes_equal': same,
                   'approved_formal_or_public_delta_independently_checked': not same})
assert len(inputs) == 52
navigation = []
for group in ['prior_peer_inputs_immutable', 'current_evidence_index_bindings']:
    for item in prior[group]:
        b = item['binding']
        check_binding(b)
        p = b.get('copy', b['path'])
        if p in trees[ACT]:
            assert blob(b['commit'], b['path']) == blob(ACT, p)
            navigation.append({'kind': group, 'source': b, 'actual': binding(ACT, p),
                               'whole_bytes_equal': True})
interfaces = []
for item in prior['current_read_only_interfaces']:
    b = item['NEW']
    check_binding(b, ACT)
    assert trees[BASE][b['path']] == trees[CAND][b['path']] == trees[ACT][b['path']]
    interfaces.append({'accepted': binding(BASE, b['path']), 'candidate': binding(CAND, b['path']),
                       'actual': binding(ACT, b['path']), 'all_whole_bytes_mode_equal': True})
assert len(interfaces) == 4

accepted_guard = J(ACT, B + 'integration-stage-1/accepted-result-preservation.json')
stats_binding = accepted_guard['accepted_statistics']
check_binding(stats_binding)
check_binding(stats_binding, ACT)
stats = J(ACT, stats_binding['path'])
receipts = stats['accepted_contribution_receipts']
assert len(receipts) == stats['contribution_records'] == 232
assert len(stats['accepted_batches']) == 14
assert 'B13' not in stats['accepted_batches'] and 'B16' not in stats['accepted_batches']
assert len({(r['batch'], r['id']) for r in receipts}) == 232
receipt_map = {(r['id'], r['candidate'], r['actual']): r for r in receipts}
assert len(receipt_map) == 232

def rows(data):
    return list(csv.DictReader(io.StringIO(data.decode()), delimiter='\t'))

public_evidence = []
ledger = {}
for p in public[:2]:
    old = blob(BASE, p)
    current = blob(ACT, p)
    assert old == blob(ADMIN, p)
    assert current.startswith(old)
    old_rows, new_rows = rows(old), rows(current)
    assert len(old_rows) == 232 and len(new_rows) == 240
    assert new_rows[:232] == old_rows
    ledger[p] = new_rows
    public_evidence.append({'path': p, 'old': binding(BASE, p), 'actual': binding(ACT, p),
                            'complete_old_raw_bytes_exact_prefix': True,
                            'old_rows': 232, 'actual_rows': 240, 'added_rows': 8,
                            'old_raw_record_hashes': [sha(line) for line in old.splitlines(keepends=True)[1:]],
                            'added_raw_record_hashes': [sha(line) for line in current[len(old):].splitlines(keepends=True)]})
old_receipts = []
for row in ledger[public[0]][:232]:
    key = (row['finding_id'], row['candidate_commit'], row['reviewed_integration_commit'])
    receipt = receipt_map[key]
    expected_reports = receipt.get('required_actual_reports', [receipt['report']])
    public_reports = row['integration_review_commit'].split(';')
    assert public_reports == [receipt['report']] or public_reports == expected_reports
    assert receipt['verdict'] == 'PASS_SCOPED' and 'PASS_SCOPED' in row['integration_verdict']
    assert row['canonical_state'] == 'OPEN'
    old_receipts.append({'record_key': receipt['batch'] + '/' + receipt['id'],
                         'receipt': receipt, 'approval_candidate_actual_and_receipt_report_exact': True,
                         'public_report_fields': public_reports,
                         'accepted_required_reports_preserved_in_statistics': expected_reports,
                         'public_scoped_gate_wording': row['integration_verdict'],
                         'public_original_wording_byte_preserved': True})
assert len({r['record_key'] for r in old_receipts}) == 232
final_old = blob(BASE, public[2])
final_new = blob(ACT, public[2])
assert final_old == blob(ADMIN, public[2]) and final_new.endswith(final_old)
public_evidence.append({'path': public[2], 'old': binding(BASE, public[2]),
                        'actual': binding(ACT, public[2]), 'whole_old_body_exact_suffix': True,
                        'added_prefix_bytes': len(final_new) - len(final_old),
                        'added_prefix_sha256': sha(final_new[:-len(final_old)])})
canonical_path = ROOT + 'finding-ledger.tsv'
canonical = rows(blob(ACT, canonical_path))
assert len(canonical) == 229 and all(r['canonical_state'] == 'OPEN' for r in canonical)
assert blob(BASE, canonical_path) == blob(CAND, canonical_path) == blob(ACT, canonical_path)

author_controls_path = B + 'author-draft-1/original-and-acceptance-controls.json'
author_controls = J(ACT, author_controls_path)['controls']
registrations = J(ACT, B + 'integration-stage-1/finding-registration.json')['records']
assert len(author_controls) == len(registrations) == len(prior_cov['records']) == 8
assert sum(r['primary'] for r in registrations) == 5
assert [r['id'] for r in registrations] == [r['finding_id'] for r in ledger[public[0]][232:]]
assert [r['id'] for r in registrations] == [r['finding_id'] for r in ledger[public[1]][232:]]
control_records = []
for i, (c, r, reused) in enumerate(zip(author_controls, registrations, prior_cov['records'])):
    assert c['id'] == r['id'] == reused['id']
    assert c['primary'] == r['primary'] == reused['primary']
    assert c['complete_current_control_fields'] == r['complete_current_control_fields'] == reused['qualified_current_control']
    assert c['whole_approved_acceptance_object'] == r['complete_minimum_acceptance_fields']
    assert verify_pointer(c['whole_original_object_binding']) == c['whole_original_object']
    assert verify_pointer(c['whole_approved_acceptance_binding']) == c['whole_approved_acceptance_object']
    assert objsha(c['whole_original_object']) == c['whole_original_object_sha256']
    assert objsha(c['whole_approved_acceptance_object']) == c['whole_acceptance_object_sha256']
    for field, value in c['complete_current_control_fields'].items():
        assert c['whole_original_object'][field] == value
    # Fixed whole object hashes are retained exactly across author/current registration.
    for key in ['whole_original_object_sha256', 'whole_acceptance_object_sha256']:
        assert c[key] == r[key]
    assert verify_pointer(r['complete_qualified_control_binding']) == c
    assert verify_pointer(r['candidate_FULL_record']) == reused
    local_author = verify_pointer(r['local_author_output'])
    assert local_author['id'] == r['id']
    assert r['current_status'] == 'CANDIDATE_LOCAL_PASS_INTEGRATED_PENDING_ALL_EXACT_ACTUAL_GATES'
    assert r['canonical_state'] == 'OPEN' and r['final_closure'] is False
    assert r['actual_full_and_affected_receipts'] is None and r['accepted_B13_contributions'] == 0
    assert r['candidate_primary_minimum_satisfied'] == c['primary']
    accepted = sorted(x['batch'] for x in receipts if x['id'] == r['id'])
    assert accepted == sorted(r['accepted_contributors']) == sorted(c['accepted_contributors'])
    assert sorted(r['all_contributors']) == sorted(c['all_contributor_batches'])
    assert sorted(r['remaining_contributors']) == sorted(set(r['all_contributors']) - set(accepted))
    assert sorted(r['prior_accepted_receipt_keys']) == sorted(x['batch'] + '/' + x['id'] for x in receipts if x['id'] == r['id'])
    locators = []
    for loc in r['current_formal_locators']:
        locators.append({'path': loc['path'], 'clauses': loc['clauses'],
                         'actual': check_binding(dict(loc['output'], commit=ACT, path=loc['path'])),
                         'candidate_actual_exact': trees[CAND][loc['path']] == trees[ACT][loc['path']]})
    approval = ledger[public[0]][232+i]
    trace = ledger[public[1]][232+i]
    for row in [approval, trace]:
        assert row['canonical_state'] == 'OPEN' and row['candidate_commit'] == CAND
        assert row['candidate_review_commit'] == FULL
        obligations = json.loads(row['remaining_obligations'])
        assert obligations['record_key'] == r['record_key']
        assert obligations['all_contributors'] == r['all_contributors']
        assert obligations['accepted_contributors'] == r['accepted_contributors']
        assert obligations['remaining_contributors'] == r['remaining_contributors']
        assert obligations['candidate_FULL_report'] == FULL
        assert obligations['candidate_affected_report'] == PEER
        assert obligations['canonical_final_closure'] == 'NOT_PERFORMED'
    assert approval['public_registration_verdict'] == 'REGISTERED_CANDIDATE_CONTRIBUTION_PENDING_ACTUAL'
    assert approval['integration_verdict'] == 'INTEGRATED_PENDING_ALL_EXACT_ACTUAL_GATES'
    assert approval['reviewed_integration_commit'] == 'EXTERNAL_ACTUAL_SHA_PENDING'
    assert approval['integration_review_commit'] == ''
    assert approval['downstream_gate'] == 'B13_C_PENDING; B16_FULL_WAITING_FOR_B13_C'
    assert trace['accepted_candidate_contribution'] == 'B13_CANDIDATE_LOCAL_PASS_NOT_ACTUAL_ACCEPTED'
    assert json.loads(trace['remaining_batches']) == r['remaining_contributors']
    assert 'C_NOT_PERFORMED' in trace['integration_gate']
    fields = c['complete_current_control_fields']
    control_records.append({
        'id': c['id'], 'primary': c['primary'], 'primary_owner': c['primary_owner'],
        'complete_qualified_control_binding': dict(binding(ACT, author_controls_path), pointer=f'/controls/{i}'),
        'whole_original_object_binding': c['whole_original_object_binding'],
        'whole_approved_acceptance_binding': c['whole_approved_acceptance_binding'],
        'whole_original_object_sha256': c['whole_original_object_sha256'],
        'whole_acceptance_object_sha256': c['whole_acceptance_object_sha256'],
        'complete_current_control_fields': fields,
        'complete_approved_acceptance_object': c['whole_approved_acceptance_object'],
        'precise_candidate_semantic_evidence_reused': {
            'binding': dict(binding(FULL, previous_coverage_path), pointer=f'/records/{i}'),
            'record': reused,
            'all_11_outputs_whole_bytes_and_modes_equal_to_ACT': True,
            'semantic_source_and_consumer_version_unchanged': True,
            'not_an_automatic_candidate_to_actual_signature': True},
        'actual_G_registration_full_control_and_minimum_equal': True,
        'actual_current_formal_locators': locators,
        'actual_old_accepted_contributors_independently_recomputed': accepted,
        'remaining_nonlocal_contributors': r['remaining_contributors'],
        'actual_public_pending_registration_correct': True,
        'actual_static_test_navigation_not_executed': r['static_test_ids_not_executed'],
        'actual_current_minimum_verdict': 'PASS_LOCAL_PRIMARY_MINIMUM' if c['primary'] else 'PASS_LOCAL_SHARED_CONTRIBUTION',
        'canonical_or_nonlocal_closed': False,
        'behavior_vectors_executed': 0,
    })

scope = J(ACT, B + 'integration-stage-1/original-scope-application.json')
scope_evidence = []
for key, expected in [('scope1', '2b23c82947bcecec4ab059d63048f9b67586575b'), ('scope2', ADMIN)]:
    b = scope[key]
    assert b['commit'] == expected
    check_binding(b)
    check_binding(b, ACT)
    amendment = J(b['commit'], b['path'])
    patch_binding = amendment['source_whole_patch']
    original_patch = blob(patch_binding['commit'], patch_binding['path'])
    check_binding(patch_binding)
    rebuilt = ''
    records = []
    for r in amendment['records']:
        before_binding = r['before']
        after_binding = r['after_to_apply']
        before = blob(before_binding['commit'], before_binding['path'])
        after = blob(after_binding['commit'], after_binding['path'])
        check_binding(before_binding)
        check_binding(after_binding)
        rebuilt += ''.join(difflib.unified_diff(before.decode().splitlines(keepends=True),
                          after.decode().splitlines(keepends=True),
                          fromfile='a/' + r['path'], tofile='b/' + r['path']))
        records.append({'path': r['path'], 'before': before_binding, 'exact_permitted_after': after_binding})
    assert rebuilt.encode() == original_patch
    scope_evidence.append({'scope_binding': b, 'whole_exact_patch': patch_binding,
                           'independently_rebuilt_patch_equal': True, 'records': records,
                           'scope_permission_is_not_quality_PASS': True})
for r in scope['records']:
    check_binding(r['formal_base_before'])
    check_binding(r['candidate_to_copy'], ACT)
    allowed = r['scope2_after'] or r['scope1_exact_after']
    check_binding(allowed)
    assert blob(allowed['commit'], allowed['path']) == blob(ACT, r['path'])
wp58scope = J(ADMIN, scope['scope2']['path'])['records'][0]
before = blob(wp58scope['before']['commit'], wp58scope['before']['path']).decode()
after = blob(ACT, wp58scope['path']).decode()
assert before.count(wp58scope['exact_before_clause']) == after.count(wp58scope['exact_after_clause']) == 1
before_parts = before.split(wp58scope['exact_before_clause'])
after_parts = after.split(wp58scope['exact_after_clause'])
assert before_parts == after_parts

def catalog(commit, path):
    group = None
    result = []
    for line in blob(commit, path).decode().splitlines():
        heading = re.match(r'^## ([A-Z]{2})：', line)
        if heading:
            group = heading[1]
        cols = [x.strip() for x in line.split('|')]
        if len(cols) >= 5 and re.fullmatch(r'(?:[QWP]\d+[a-z]?|[A-Z]{2}-\d+)', cols[1]):
            result.append({'group': group, 'id': cols[1], 'row': line})
    return result

catalogs = []
for p in [p for p in formal if '/test-catalog/' in p]:
    a, c, z = [catalog(x, p) for x in [BASE, CAND, ACT]]
    assert c == z
    keys = lambda seq: [(r['group'], r['id']) for r in seq]
    oldkeys = keys(a)
    assert len(oldkeys) == len(set(oldkeys))
    assert [k for k in keys(z) if k in set(oldkeys)] == oldkeys
    changed = [{'before': r, 'after': next(v for v in z if (v['group'], v['id']) == (r['group'], r['id']))}
               for r in a if r['row'] != next(v['row'] for v in z if (v['group'], v['id']) == (r['group'], r['id']))]
    added = [r for r in z if (r['group'], r['id']) not in set(oldkeys)]
    if 'combat-requirements' in p:
        assert len(a) == 127 and len(z) == 137 and len(added) == 10
        assert dict(collections.Counter(r['group'] for r in z)) == {'QC':47, 'WS':35, 'PA':28, 'RC':27}
        assert ('RC', 'W22b') in keys(z)
        for key in [('RC','W16'), ('WS','W28'), ('WS','W29'), ('PA','P16')]:
            assert next(r for r in a if (r['group'],r['id']) == key) == next(r for r in z if (r['group'],r['id']) == key)
    else:
        assert len(a) == len(z) == 125 and len(added) == 0
        assert all(x['before']['group'] == 'FC' for x in changed)
        assert [r for r in a if r['group'] != 'FC'] == [r for r in z if r['group'] != 'FC']
        assert len([r for r in z if r['group'] != 'FC']) == 108
    catalogs.append({'path': p, 'accepted_predecessor_count':len(a), 'actual_count':len(z),
                     'actual_group_counts':dict(collections.Counter(r['group'] for r in z)),
                     'old_ID_order_multiplicity_preserved':True, 'changed_old_rows':changed,
                     'added_rows':added, 'candidate_actual_all_rows_exact':True,
                     'all_designs_static_unexecuted':True})

trace_path = B + 'author-draft-1/two-findings-repair-1/static-transition-traces-successor.json'
trace = J(ACT, trace_path)
assert blob(CAND, trace_path) == blob(ACT, trace_path)
nil_case = trace['entry_submission'][1]
assert nil_case['return'] is None and nil_case['return_identity'] == 'nil'
assert nil_case['submit'] is False and nil_case['registration'] == 'P unchanged'
assert nil_case['active_player'] == 'P unchanged'
assert trace['entry_submission'][0]['return'] is False
assert trace['entry_submission'][3]['return'] is True
entry = trace['entry_final_scan']
assert entry['catalog'] == 'RC-W26' and entry['executed'] is False
assert entry['recording_checkpoints'][0]['roundindex'] == -1
assert entry['recording_checkpoints'][0]['rounds'] == []
assert entry['recording_checkpoints'][3]['switches'] == [1]
assert entry['recording_checkpoints'][3]['rounds'] == []
assert entry['recording_checkpoints'][1]['consumer_order'] == ['stat-drop item','cross-half ability']
assert entry['recording_checkpoints'][1]['stop_at_first_true'] is True
play = entry['playback_checkpoints'][1]
assert play['value'] == play['switch_cursor_after'] == 1
assert play['read_switches_at'] == 0 and play['first_command_not_started'] is True
assert play['random_sequence_for_selection'] is False and play['live_owner_UI'] is False
negative = entry['nearby_controls'][1]
assert negative['switches_append'] == -1 and negative['consumer_return'] is False
assert negative['item_consumed'] is True and negative['replacement_submitted'] is False
assert trace['executed_vectors'] == 0
repair_oracles = {'binding':binding(ACT,trace_path),
    'candidate_actual_whole_bytes_equal':True,
    'B027_precise_nil_false_true_and_state_identity_pass':True,
    'B029_W26_entry_before_command_same_consumer_and_negative_consumption_pass':True,
    'W26_present_in_catalog_and_current_trace':True,
    'registration_test_ID_arrays_are_navigation_not_exhaustive_current_catalog':True,
    'oracle_inspection_is_static_text_not_behavior_execution':True}

limits = J(PACKET, B + 'actual-freeze-1/source-limits.json')
limits_evidence = []
for k in ['limits', 'author_source_limits', 'author_inherited_limits', 'independent_candidate_limits']:
    b = limits[k]
    limits_evidence.append({'kind': k, 'actual': check_binding(b),
                            'candidate_actual_byte_equal': b['path'] in trees[CAND] and
                                 trees[CAND][b['path']] == trees[ACT][b['path']]})
limits_evidence.append({'kind': 'independent_source_log',
                        'source': binding(FULL, B+'candidate-review-2/source-reading-log.json'),
                        'actual': binding(ACT, B+'candidate-review-2/source-reading-log.json'),
                        'whole_bytes_equal': blob(FULL,B+'candidate-review-2/source-reading-log.json') ==
                                            blob(ACT,B+'candidate-review-2/source-reading-log.json')})
assert limits_evidence[-1]['whole_bytes_equal']

gate = J(ACT, B + 'integration-stage-1/candidate-gate-receipts.json')
assert len(gate['owners']) == 11
owner_evidence = []
for r in gate['owners']:
    for k in ['result', 'report']:
        b = r[k]
        check_binding(b)
        check_binding(b, ACT)
    owner_evidence.append({'owner': r['owner'], 'candidate_verdict': r['candidate_verdict'],
                           'result': r['result'], 'report': r['report'],
                           'no_actual_owner_signature_by_this_FULL_review': True})

parsed = []
for r in classified:
    p = r['path']
    if p.endswith('.json'):
        json.loads(blob(ACT, p))
        parsed.append(binding(ACT, p))
formal_check = subprocess.run(['git','diff','--check',BASE,ACT,'--',*formal],capture_output=True)
assert formal_check.returncode == 0, formal_check.stdout.decode()
save('control-coverage.json', {'role':'R-B13_FULL_ACTUAL', 'reviewed_actual_commit':ACT,
     'reviewed_actual_tree':dispatch['reviewed_actual_tree'], 'candidate':CAND,
     'accepted_predecessor':BASE, 'verdict':'PASS', 'contributions':8, 'primary':5, 'formal_outputs':11,
     'records':control_records, 'canonical_closed':False, 'B030_count':0, 'B16_WP67A_closed':False,
     'all_eleven_affected_owner_signatures_by_this_report':False, 'C':False,
     'behavior_vectors_executed':0})
save('independent-metadata.json', {
    'kind':'NEW_INDEPENDENT_EXACT_ACTUAL_GIT_JSON_HASH_TEXT_METADATA_ONLY',
    'reviewed_actual_commit':ACT, 'reviewed_actual_tree':dispatch['reviewed_actual_tree'],
    'candidate':CAND, 'candidate_tree':dispatch['candidate_tree'], 'formal_accepted_predecessor':BASE,
    'administrative_predecessor_not_formal_base':ADMIN, 'packet_navigation_only':PACKET,
    'complete_unfiltered_streams':streams, 'full_path_classification':classified,
    'candidate_actual_all_changed_paths':changes['candidate-to-actual'],
    'path_classification_counts':category_counts, 'all_11_formal_output_identities':outputs,
    'whole_existing_tree_protection':preservation, 'all_153_published_source_copies':copy_evidence,
    'packet_only_11_added_paths':sorted(packet_changes),
    'accurate_candidate_FULL_reuse':{'metadata':binding(FULL,previous_metadata_path),
          'coverage':binding(FULL,previous_coverage_path), 'current_semantics_changed':False},
    'all_52_input_bindings_independently_rechecked':inputs,
    'current_navigation_and_frozen_peer_copy_identity_checks':navigation,
    'four_current_read_only_interfaces':interfaces,
    'accepted_statistics_binding':check_binding(stats_binding,ACT),
    'accepted_batches':stats['accepted_batches'], 'all_232_accepted_receipt_public_checks':old_receipts,
    'public_raw_record_protection':public_evidence,
    'new_B13_public_records_pending_only':8, 'accepted_B13_contributions_in_ACT':0,
    'canonical_229_OPEN_0_CLOSED_unchanged':binding(ACT,canonical_path),
    'original_scope_permitted_patch_sequence':scope_evidence,
    'scope2_WP58_outside_5_2_whole_prefix_suffix_exact':True,
    'catalogs':catalogs, 'source_limits_bindings':limits_evidence,
    'current_repair_oracle_static_text_checks':repair_oracles,
    'eleven_candidate_owner_receipts_identity_only_not_actual_signatures':owner_evidence,
    'all_changed_JSON_parsed_and_hashed':parsed,
    'formal_predecessor_ACT_diff_check_exit':formal_check.returncode,
    'historical_source_Ruby_game_behavior_vector_executions':0,
    'fresh_reference_semantic_read_files':0,
    'metadata_success_does_not_replace_quality_judgment':True,
})
save('metadata-validation.json', {'reviewed_actual_commit':ACT, 'status':'PASS_METADATA',
    'independent_complete_streams':streams, 'formal_outputs':11, 'controls':8, 'primary_minima':5,
    'published_artifact_source_copies':153, 'accepted_receipt_records':232,
    'pending_B13_records':8, 'canonical_OPEN':229, 'canonical_CLOSED':0,
    'path_classification_counts':category_counts,
    'whole_existing_tree_protection':preservation, 'all_assertions_passed':True,
    'formal_diff_check_exit':formal_check.returncode,
    'program_scope':'this new Git/JSON/hash/text metadata script only; no historical scripts executed',
    'quality_verdict_separate':True})
print(json.dumps({'status':'PASS_METADATA','streams':streams,'classification':category_counts,
                  'protection':preservation,'catalogs':[dict(path=x['path'],old=x['accepted_predecessor_count'],actual=x['actual_count'],counts=x['actual_group_counts']) for x in catalogs]},ensure_ascii=False))
