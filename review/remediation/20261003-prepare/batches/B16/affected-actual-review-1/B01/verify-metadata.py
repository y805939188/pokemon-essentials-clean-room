#!/usr/bin/env python3
"""New exact-version Git/JSON/TSV/text metadata checks; no source execution."""
import collections, csv, hashlib, io, json, pathlib, re, subprocess

REPO = pathlib.Path('/workspace/pokemon-essentials-clean-room')
TMP = pathlib.Path('/tmp/b16-affected-actual-review-1')
P = 'review/remediation/20261003-prepare/batches/B16/'
R = P + 'affected-actual-review-1/'
ACT = '29b21fe188cce4e76f5a2f566f9144f1c3f53239'
TREE = 'e05903a329f4a18370a17858f4653cbb1273b49e'
C = '27185563f307e16d2612fa86e83b2c9bd772c79e'
NEW = '356b46b320884e57e71a1cab8413e13594524a7d'
PKG = '7372479c763b90271f0bf8fbab68a15862739ba0'
CONTRACT = '8e2753430ccb4bad8098048c814576aa386a09ef'
CAND_AFFECTED = '3d34dd073381e430001ee1b03d10e559fc576c8e'
CAND_FULL = 'da58ab3e8ce5e508b2ed55928c6f334cb64a2445'

def git(*args):
    return subprocess.check_output(['git', *args], cwd=REPO)

def sha(b):
    return hashlib.sha256(b).hexdigest()

def canonical(j):
    return json.dumps(j, ensure_ascii=False, sort_keys=True, separators=(',', ':')).encode()

def read(c, p):
    return git('show', c + ':' + p)

def js(c, p):
    return json.loads(read(c, p))

def pointer(j, p):
    for k in p.lstrip('/').split('/') if p else []:
        k = k.replace('~1', '/').replace('~0', '~')
        j = j[int(k)] if isinstance(j, list) else j[k]
    return j

def identity(c, p):
    b = read(c, p)
    return {'commit': c, 'path': p, 'git_blob': git('rev-parse', c + ':' + p).decode().strip(), 'sha256': sha(b), 'bytes': len(b)}

bindings = {}
def bind(b):
    k = (b['commit'], b['path'])
    if k not in bindings:
        bindings[k] = identity(*k)
    got = bindings[k]
    for field in ('git_blob', 'sha256', 'bytes'):
        if field in b:
            assert got[field] == b[field], (k, field, got[field], b[field])
    return pointer(js(*k), b.get('pointer')) if b.get('pointer') else got

def tree(c):
    out = {}
    for line in git('ls-tree', '-rz', '--full-tree', c).split(b'\0'):
        if line:
            meta, p = line.split(b'\t', 1)
            out[p.decode()] = tuple(meta.decode().split())
    return out

def status(a, b):
    return [{'status': l.split('\t')[0], 'path': l.split('\t')[1]} for l in git('diff', '--name-status', '--no-renames', a, b).decode().splitlines()]

def table(b):
    return list(csv.DictReader(io.StringIO(b.decode()), delimiter='\t'))

assert git('rev-parse', ACT + '^{tree}').decode().strip() == TREE
assert git('rev-parse', C + '^{tree}').decode().strip() == 'e44ed01586846bb42b03105dcc575d463df4ef49'
assert git('rev-parse', NEW + '^{tree}').decode().strip() == '344b606d8368eb09dc9313e09fdda1fa227e6f39'
dispatch = js(PKG, P + 'actual-freeze-1/affected-actual-dispatch.json')
entrances = js(PKG, P + 'actual-freeze-1/affected-owner-entrypoints.json')
outputs = js(PKG, P + 'actual-freeze-1/frozen-output-identities.json')
actual_bindings = js(PKG, P + 'actual-freeze-1/public-registration-actual-binding.json')
for b in dispatch['complete_control_bindings'].values():
    bind(b)
controls_doc = js(CONTRACT, P + 'refreeze-after-B13-C-1/original-and-acceptance-controls.json')
contract = js(CONTRACT, P + 'refreeze-after-B13-C-1/B16-downstream-contract.json')
effects = js(CONTRACT, P + 'refreeze-after-B13-C-1/effective-case-constraints.json')
controls = controls_doc['controls']
assert controls == contract['contribution_controls']
assert len(controls) == 24 and sum(x['primary'] for x in controls) == 20
assert len(effects['full_exact_values']) == effects['case_records'] == effects['aggregation_fields'] == 12

stream_proof = []
for stream in dispatch['complete_unfiltered_streams']:
    command = ['diff', '--binary', '--no-ext-diff', '--no-textconv', '--no-renames', stream['from'], ACT]
    raw = git(*command)
    supplied = read(PKG, stream['path'])
    assert raw == supplied and len(raw) == stream['bytes'] and sha(raw) == stream['sha256']
    changes = status(stream['from'], ACT)
    assert changes == stream['complete_name_status'] and len(changes) == stream['file_count']
    assert all(x['status'] in ('M', 'A') for x in changes)
    stream_proof.append({'from': stream['from'], 'to': ACT, 'to_tree': TREE,
        'command': ['git', *command], 'path_filters': [], 'exclusions': [], 'truncated': False,
        'bytes': len(raw), 'sha256': sha(raw), 'package_copy': identity(PKG, stream['path']),
        'independently_reproduced_all_bytes': True, 'file_count': len(changes),
        'status_counts': dict(collections.Counter(x['status'] for x in changes)), 'complete_name_status': changes})

tC, tN, tA = tree(C), tree(NEW), tree(ACT)
payloads = {x['path'] for x in outputs['outputs']}
public = {'review/remediation/20261003-prepare/approval-ledger.tsv',
    'review/remediation/20261003-prepare/traceability-successor.tsv',
    'review/remediation/20261003-prepare/final-integration-review.md'}
assert len(payloads) == 11
protected = []
for c, old, excepts in [(C, tC, payloads | public), (NEW, tN, public)]:
    kept = {p: v for p, v in old.items() if p not in excepts}
    assert all(tA.get(p) == v for p, v in kept.items())
    assert {p for p in old if tA.get(p) != old[p]} == excepts
    protected.append({'from': c, 'old_tree_paths': len(old), 'exceptions': sorted(excepts),
        'protected_paths': len(kept), 'protected_mode_type_blob_projection_sha256': sha(canonical(kept)),
        'all_modes_types_blobs_identical': True, 'deleted_paths': []})
assert set(x['path'] for x in stream_proof[0]['complete_name_status'] if x['status'] == 'M') == payloads | public
assert set(x['path'] for x in stream_proof[1]['complete_name_status'] if x['status'] == 'M') == public
additions = [x['path'] for x in stream_proof[0]['complete_name_status'] if x['status'] == 'A']
assert all(p.startswith(P) or p.startswith('review/remediation/20261003-prepare/batches/B17/preparation-dispatch-after-B13-C-1/') or p.startswith('review/remediation/20261003-prepare/batches/B18/preparation-dispatch-after-B13-C-1/') for p in additions)
addition_groups = collections.Counter('/'.join(p.split('/')[5:7]) for p in additions)

formal_manifest = js(ACT, P + 'integration-stage-1/formal-copy-identities.json')
output_proof = []
for out in outputs['outputs']:
    for k in ('accepted_C_before', 'reviewed_NEW', 'frozen_ACT'):
        bind(out[k])
    assert read(NEW, out['path']) == read(ACT, out['path'])
    assert tA[out['path']][0] == tN[out['path']][0] == tC[out['path']][0] == '100644'
    output_proof.append(out)
for x in formal_manifest['approved_originals']:
    bind(x['exact_current_scope_after'])
    assert read(ACT, x['path']) == read(x['exact_current_scope_after']['commit'], x['exact_current_scope_after']['path'])
    for b in x['scope_chain']:
        bind(b)
assert len(formal_manifest['final_outputs']) == 6 and len(formal_manifest['approved_originals']) == 5

stats_path = 'review/remediation/20261003-prepare/batches/B13/acceptance-stage-1/completion-statistics-successor.json'
assert read(C, stats_path) == read(ACT, stats_path)
stats = js(C, stats_path)
receipts = stats['accepted_contribution_receipts']
assert len(receipts) == stats['contribution_records'] == 240
assert len(stats['accepted_batches']) == 15 and stats['primary_denominator'] == 154
assert stats['canonical_OPEN'] == 229 and stats['canonical_CLOSED'] == 0
receipt_keys = [x['batch'] + '/' + x['id'] for x in receipts]
assert len(set(receipt_keys)) == 240
ledger_path = 'review/remediation/20261003-prepare/finding-ledger.tsv'
assert read(C, ledger_path) == read(ACT, ledger_path)
canonical_rows = table(read(ACT, ledger_path))
assert len(canonical_rows) == 229 and collections.Counter(x['canonical_state'] for x in canonical_rows) == {'OPEN': 229}

reg_path = P + 'integration-stage-1/finding-registration.json'
registration = js(ACT, reg_path)
assert registration['new_B16_accepted_contributions'] == registration['canonical_CLOSED_increment'] == 0
assert registration['actual_receipts'] is None
assert len(registration['records']) == 24
reuse_controls = js(CAND_AFFECTED, P + 'affected-candidate-review-2/B01/qualified-controls-and-reuse.json')
assert [x['id'] for x in reuse_controls['controls']] == [x['id'] for x in controls]
control_proof = []
for i, (control, reg, reused) in enumerate(zip(controls, registration['records'], reuse_controls['controls'])):
    assert control['id'] == reg['id'] == reused['id']
    assert reg['primary'] == control['primary']
    assert reg['primary_owner'] == control['primary_owner']
    assert reg['complete_current_control_fields'] == control['complete_current_control_fields'] == reused['complete_current_control_fields']
    current_hash = sha(canonical(control['complete_current_control_fields']))
    assert current_hash == reused['current_control_sha256']
    for kind, binding_key, hash_key in [('whole_original_object', 'whole_original_object_binding', 'whole_original_object_sha256'), ('whole_approved_acceptance_object', 'whole_approved_acceptance_binding', 'whole_acceptance_object_sha256')]:
        assert bind(control[binding_key]) == control[kind]
        assert sha(canonical(control[kind])) == control[hash_key] == reg[hash_key] == reused[hash_key]
        assert reg[binding_key] == control[binding_key]
    assert bind(reg['complete_qualified_control_binding']) == control
    for source, destination in [('all_contributor_batches', 'all_contributors'), ('accepted_contributors', 'accepted_contributors'), ('pending_contributors', 'remaining_contributors')]:
        assert reg[destination] == control[source]
    prior_keys = [x['batch'] + '/' + x['id'] for x in receipts if x['id'] == control['id']]
    assert reg['prior_accepted_receipt_keys'] == prior_keys
    assert set(reg['accepted_contributors']) == {x.split('/')[0] for x in prior_keys}
    assert 'B16' in reg['remaining_contributors'] and 'B16' not in reg['accepted_contributors']
    assert reg['canonical_state'] == 'OPEN' and reg['current_status'] == 'CANDIDATE_PASS_INTEGRATED_PENDING_ALL_EXACT_ACTUAL_GATES_AND_C'
    assert reg['actual_identity_external'] is True and reg['actual_full_and_affected_receipts'] is None
    assert reg['accepted_B16_contributions'] == 0 and reg['final_closure'] is False
    ab = actual_bindings['records'][i]
    assert bind(ab['G_record']) == reg
    assert ab['id'] == control['id'] and ab['actual_commit_external_binding'] == ACT and ab['actual_tree'] == TREE
    assert ab['candidate'] == NEW and ab['candidate_review_commit'] == CAND_FULL
    assert ab['actual_review_receipts'] is None and ab['canonical_state'] == 'OPEN' and ab['accepted_B16_contributions'] == 0
    for loc in reg['current_formal_locators']:
        assert loc['commit'] == NEW
        bind(dict(loc['binding'], commit=NEW, path=loc['path']))
        assert read(NEW, loc['path']) == read(ACT, loc['path'])
    cat = reg['catalog_evidence']
    bind(dict(cat['binding'], commit=cat['commit'], path=cat['path']))
    assert reg['static_test_ids_not_executed'] == [cat['id']]
    assert cat['id'] in read(ACT, cat['path']).decode().splitlines()[cat['line'] - 1]
    control_proof.append({'id': control['id'], 'primary': control['primary'], 'primary_owner': control['primary_owner'],
        'complete_control_binding': dict(dispatch['complete_control_bindings']['whole_original_approved_current_controls'], pointer='/controls/' + str(i)),
        'whole_original_object_sha256': control['whole_original_object_sha256'], 'whole_acceptance_object_sha256': control['whole_acceptance_object_sha256'],
        'current_control_sha256': current_hash, 'complete_current_control_fields': control['complete_current_control_fields'],
        'all_contributors': reg['all_contributors'], 'accepted_contributors': reg['accepted_contributors'], 'remaining_contributors': reg['remaining_contributors'],
        'prior_accepted_receipt_keys': prior_keys, 'root_adjudications': len(control['complete_current_control_fields']['root_adjudications']),
        'extensions': len(control['complete_current_control_fields'].get('extensions', [])), 'actual_status': reg['current_status'],
        'scope': 'Complete qualified obligations retained; bounded owner interfaces only; no FULL/other owner/C signature.'})
effective_proof = []
for value, prior in zip(effects['full_exact_values'], reuse_controls['effective']):
    assert value['id'] == prior['id']
    h = sha(canonical(value['aggregate']))
    assert h == value['canonical_json_sha256'] == prior['sha256']
    cid = next(c for c in controls if c['id'] == value['id'])
    assert cid['whole_original_object']['effective_case_constraints'] == value['aggregate']
    effective_proof.append({'id': value['id'], 'aggregate': value['aggregate'], 'canonical_json_sha256': h, 'current_and_reused_exact_equal': True})

gate = js(ACT, P + 'integration-stage-1/candidate-gate-receipts.json')
full = js(gate['FULL']['receipt']['commit'], gate['FULL']['receipt']['path'])
bind(gate['FULL']['receipt'])
assert full['reviewed_NEW'] == NEW and full['reviewed_NEW_tree'] == '344b606d8368eb09dc9313e09fdda1fa227e6f39'
assert full['counts']['contributions'] == 24 and full['counts']['primary'] == 20
assert gate['actual_verdict'] is None and gate['C'] is False
copied = js(ACT, P + 'integration-stage-1/published-artifact-copies.json')
assert len(copied['copied_artifacts']) == 161
for artifact in copied['copied_artifacts']:
    bind(artifact['source'])
    assert read(ACT, artifact['target']) == read(artifact['source']['commit'], artifact['source']['path'])
    assert tA[artifact['target']][0] == artifact['mode']

public_proof = []
for name in ('approval-ledger.tsv', 'traceability-successor.tsv'):
    path = 'review/remediation/20261003-prepare/' + name
    before, after = read(C, path), read(ACT, path)
    assert after.startswith(before)
    old, rows = table(before), table(after)
    assert len(old) == 240 and len(rows) == 264 and rows[:240] == old
    added = rows[240:]
    assert [r['finding_id'] for r in added] == [c['id'] for c in controls]
    for i, (row, control) in enumerate(zip(added, controls)):
        assert row['canonical_state'] == 'OPEN' and row['candidate_commit'] == NEW and row['candidate_review_commit'] == CAND_FULL
        obligations = json.loads(row['remaining_obligations'])
        reg = registration['records'][i]
        for field in ('all_contributors', 'accepted_contributors', 'remaining_contributors'):
            assert obligations[field] == reg[field]
        assert obligations['candidate_FULL'] == CAND_FULL and obligations['candidate_affected'] == CAND_AFFECTED
        assert obligations['C'] == obligations['canonical_final_closure'] == 'NOT_PERFORMED'
        assert obligations['actual_gates'] == 'PENDING_EXACT_ACTUAL_FULL_AND_ALL14_AFFECTED'
        assert obligations['complete_control'] == reg['complete_qualified_control_binding']
        assert bind(obligations['complete_control']) == control
        assert obligations['G_record'] == reg_path + '#/records/' + str(i)
        if name == 'approval-ledger.tsv':
            assert row['candidate_verdict'] == 'PASS_SCOPED'
            assert row['accepted_contribution_kind'] == ('B16_PRIMARY' if control['primary'] else 'B16_SHARED')
            assert row['public_registration_verdict'] == 'B16_INTEGRATED_PENDING_EXACT_ACTUAL_AND_C'
            assert row['integration_verdict'] == 'PENDING_EXACT_ACTUAL_FULL_AND_AFFECTED'
            assert row['downstream_gate'] == 'B17_B18_FORMAL_HELD_UNTIL_B16_C'
            assert row['reviewed_integration_commit'] == 'EXTERNAL_ACTUAL_FREEZE_REQUIRED'
            assert row['integration_review_commit'] == row['integration_disposition'] == 'PENDING'
        else:
            assert row['accepted_candidate_contribution'] == 'B16_CANDIDATE_SCOPED_PASS_INTEGRATED_NOT_ACCEPTED'
            assert row['integration_gate'] == 'PENDING_EXACT_ACTUAL_FULL24_20_ALL14_AFFECTED_AND_C; CANONICAL_OPEN'
            assert json.loads(row['static_test_ids_not_executed']) == reg['static_test_ids_not_executed']
    public_proof.append({'path': path, 'before': identity(C, path), 'after': identity(ACT, path),
        'old240_whole_raw_bytes_exact_prefix': True, 'old240_parsed_records_exact_equal': True,
        'physical_records': 264, 'new_pending': 24, 'new_primary': 20, 'new_shared': 4,
        'all24_full_control_and_contributor_bindings_verified': True, 'new_accepted_contributions': 0,
        'actual_receipts': None, 'C': False})
review_path = 'review/remediation/20261003-prepare/final-integration-review.md'
old_body, act_body = read(C, review_path), read(ACT, review_path)
assert act_body.endswith(old_body)
prefix = act_body[:-len(old_body)].decode()
assert '仅pending' in prefix and 'canonical229OPEN/0CLOSED' in prefix and '240' in prefix

prep_proof = []
for owner in ('B17', 'B18'):
    root = 'review/remediation/20261003-prepare/batches/' + owner + '/preparation-dispatch-after-B13-C-1/'
    pc, pending = js(ACT, root + 'preparation-contract.json'), js(ACT, root + 'pending-B16-inputs.json')
    assert pc['snapshot_C'] == pending['current_snapshot_C'] == C
    assert pc['snapshot_is_not_future_full_author_input'] is True and pending['full_author_allowed_now'] is False
    assert pending['not_accepted_dependency'] == 'B16'
    for field in ('allowed_formal_write_paths_now', 'allowed_original_write_paths_now', 'allowed_candidate_write_paths_now', 'allowed_public_write_paths_now'):
        assert pc[field] == []
    assert pc['allowed_write_prefix_now'] == 'review/remediation/20261003-prepare/batches/' + owner + '/author-preparation-before-B16-C-1/'
    for item in pending['pending_formal_inputs'] + pending['conditionally_pending_original_inputs']:
        bind(item['input'])
        assert item['input']['commit'] == C
    assert pc['full_author_and_review_gate'].startswith('B16 C then sole registrar latest-C')
    prep_proof.append({'owner': owner, 'contract': identity(ACT, root + 'preparation-contract.json'), 'pending': identity(ACT, root + 'pending-B16-inputs.json'),
        'status': pc['status'], 'snapshot_C': C, 'full_author_allowed_now': False,
        'allowed_write_prefix_now': pc['allowed_write_prefix_now'], 'pending_formal_inputs': pending['pending_formal_inputs'],
        'conditionally_pending_original_inputs': pending['conditionally_pending_original_inputs'], 'full_author_and_review_gate': pc['full_author_and_review_gate']})

def catalog_rows(b):
    result, headings, counts = [], [], collections.Counter()
    for line in b.decode().splitlines(keepends=True):
        if re.match(r'^#{1,6} ', line):
            level = len(line) - len(line.lstrip('#'))
            headings = [x for x in headings if x[0] < level] + [(level, line.strip())]
        if line.startswith('|'):
            cells = [x.strip() for x in line.strip().strip('|').split('|')]
            if cells and re.fullmatch(r'[A-Z][A-Za-z0-9-]*\d[A-Za-z0-9-]*', cells[0]):
                key = (' / '.join(x[1] for x in headings), cells[0])
                counts[key] += 1
                result.append((key + (counts[key],), line))
    return result

cat_path = next(p for p in payloads if '/test-catalog/' in p)
base_rows, new_rows, act_rows = [catalog_rows(read(c, cat_path)) for c in (C, NEW, ACT)]
assert len(base_rows) == 460 and len(new_rows) == len(act_rows) == 484 and new_rows == act_rows
base_map, act_map = dict(base_rows), dict(act_rows)
assert all(k in act_map for k in base_map)
changed_old = [k for k, line in base_rows if act_map[k] != line]
assert len(changed_old) == 9 and {k[1] for k in changed_old} == {'T01', 'T03', 'A23', 'A31', 'A32', 'A33', 'A38', 'C05', 'C24'}
assert [k for k, line in act_rows if k in base_map] == [k for k, line in base_rows]
assert len([k for k, line in act_rows if k not in base_map]) == 24

owner_proof = []
for e in entrances['owner_entrances']:
    owner = e['owner']
    bind(e['candidate_verdict_binding']); bind(e['candidate_report_binding'])
    previous = js(e['candidate_verdict_binding']['commit'], e['candidate_verdict_binding']['path'])
    assert previous['reviewed_commit'] == NEW
    assert bind(e['interface_route_binding']) == e['complete_frozen_original_interface_route']
    for item in e['exact_ACT_interface_inputs']:
        bind(item['accepted_C']); bind(item['exact_ACT'])
        equal = read(C, item['accepted_C']['path']) == read(ACT, item['exact_ACT']['path'])
        assert item['changed_from_accepted_C'] is (not equal)
    for receipt in e['accepted_scope_receipts_preserved']:
        assert receipt in receipts
    owner_proof.append({'owner': owner, 'candidate_verdict_binding': e['candidate_verdict_binding'], 'candidate_report_binding': e['candidate_report_binding'],
        'complete_frozen_original_interface_route': e['complete_frozen_original_interface_route'], 'interface_route_binding': e['interface_route_binding'],
        'exact_ACT_interface_inputs': e['exact_ACT_interface_inputs'], 'accepted_scope_receipts_preserved': e['accepted_scope_receipts_preserved'],
        'current_actual_owner_verdict': None, 'candidate_only_status': previous['verdict']})
assert len(owner_proof) == 14

source_provenance = {}
for fn in ('source-reading-log.json', 'milk-interface-check.json'):
    path = P + 'affected-candidate-review-2/B01/' + fn
    source_provenance[fn] = {'binding': identity(CAND_AFFECTED, path), 'complete_evidence': js(CAND_AFFECTED, path), 'copied_ACT_blob_same': tA[path][2] == git('rev-parse', CAND_AFFECTED + ':' + path).decode().strip()}
resolution = P + 'affected-candidate-review-2/B06/resolution.json'
source_provenance['C120_resolution'] = {'binding': identity(CAND_AFFECTED, resolution), 'complete_evidence': js(CAND_AFFECTED, resolution), 'copied_ACT_blob_same': tA[resolution][2] == git('rev-parse', CAND_AFFECTED + ':' + resolution).decode().strip()}
limits = js(ACT, P + 'integration-stage-1/source-limits.json')
for key in ('inherited_complete_candidate_source_limits', 'complete_contract_limits'):
    bind(limits[key])
    source_provenance[key] = {'binding': limits[key], 'complete_limits': js(limits[key]['commit'], limits[key]['path'])}

proof = {'role': 'B16_INDEPENDENT_AFFECTED_EXACT_ACTUAL_SHARED_METADATA_ONLY', 'reviewed_commit': ACT, 'reviewed_tree': TREE,
    'accepted_C': C, 'candidate_NEW': NEW, 'administrative_package': PKG,
    'identity_verified_once_for_all14': True, 'complete_unfiltered_streams': stream_proof,
    'administrative_predecessor_to_ACT_paths': len(status(dispatch['administrative_predecessor'], ACT)),
    'administrative_predecessor_is_not_FIX_BASE': True, 'added_path_groups': dict(addition_groups),
    'tree_protection': protected, 'outputs': output_proof, 'output_count': 11,
    'accepted_statistics': identity(ACT, stats_path), 'old_accepted_statistics_whole_bytes_equal': True,
    'old_accepted_receipts': receipts, 'old_accepted_receipts_canonical_sha256': sha(canonical(receipts)),
    'accepted_batches': stats['accepted_batches'], 'accepted_contributions': 240, 'primary_denominator': 154,
    'canonical_ledger': identity(ACT, ledger_path), 'canonical_OPEN': 229, 'canonical_CLOSED': 0,
    'public_registration': public_proof, 'G_registration': identity(ACT, reg_path),
    'external_ACT_binding': identity(PKG, P + 'actual-freeze-1/public-registration-actual-binding.json'),
    'final_review_old_body_exact_suffix': True, 'final_review_new_prefix': prefix,
    'final_review_identity': identity(ACT, review_path), 'all161_published_artifact_copies_independently_equal': True,
    'catalog': {'old_rows': 460, 'ACT_rows': 484, 'protected_old_rows': 451, 'assigned_old_row_edits': [list(k) for k in changed_old],
        'new_rows': 24, 'old_order_multiplicity_preserved': True, 'NEW_to_ACT_all484_rows_exact_equal': True, 'executed': 0},
    'B17_B18_preparation_only': prep_proof, 'owner_interfaces_and_old_receipts': owner_proof,
    'source_execution': 0, 'historical_program_execution': 0, 'runtime_observations': 0, 'tasks_created': 0,
    'quality_verdict': 'NO_SHARED_QUALITY_SIGNATURE; each owner decides independently',
    'requested_configuration': dispatch['requested_configuration'], 'effective_backend': dispatch['effective_backend']}
qualified = {'reviewed_commit': ACT, 'reviewed_tree': TREE, 'contributions': 24, 'primary': 20, 'effective_count': 12,
    'bindings': dispatch['complete_control_bindings'], 'controls': control_proof, 'full_exact_effective_constraints': effective_proof,
    'policy': 'Complete original, approved and current root/extensions/conditions/minimum/recheck preserved; supported bounded owner decisions; no canonical closure.'}
for n, j in [('shared-proof.json', proof), ('qualified-controls.json', qualified), ('source-reuse.json', source_provenance)]:
    (TMP / n).write_text(json.dumps(j, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({'result': 'PASS_METADATA_ONLY', 'ACT': ACT, 'streams': [(x['file_count'], x['status_counts']) for x in stream_proof],
    'protected': [(x['old_tree_paths'], x['protected_paths']) for x in protected], 'outputs': 11, 'controls': 24, 'primary': 20,
    'effective': 12, 'accepted': 240, 'catalog': proof['catalog'], 'owners': 14, 'copies': 161}, ensure_ascii=False))
