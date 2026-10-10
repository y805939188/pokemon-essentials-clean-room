#!/usr/bin/env python3
"""New independent metadata checks only. No reference or historical program execution."""
import collections
import hashlib
import json
from pathlib import Path
import re
import subprocess

ROOT = Path(__file__).resolve().parents[6]
OUT = Path(__file__).resolve().parent
BASE = '27185563f307e16d2612fa86e83b2c9bd772c79e'
CANDIDATE = 'ae223d7bfb9ff6ed8a1ac153debb986115345957'
PUBLICATION = '5c70c6945ede498f1d7d59592da1d37a96c07a98'
PACKET = '8e2753430ccb4bad8098048c814576aa386a09ef'
REF = '8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
PREFIX = 'review/remediation/20261003-prepare/batches/B16/'
REF_GIT = '/tmp/b16-reference.git'
checks = []
bindings = []
cache = {}

def git(*args, reference=False):
    cmd = ['git', '--git-dir=' + REF_GIT] if reference else ['git', '-C', str(ROOT)]
    return subprocess.check_output(cmd + list(args))

def blob(commit, path, reference=False):
    key = (commit, path, reference)
    if key not in cache:
        cache[key] = git('show', commit + ':' + path, reference=reference)
    return cache[key]

def digest(data):
    return hashlib.sha256(data).hexdigest()

def canonical(obj):
    return json.dumps(obj, ensure_ascii=False, sort_keys=True, separators=(',', ':')).encode()

def check(name, ok, detail=None):
    checks.append({'check': name, 'pass': bool(ok), 'detail': detail})

def load(commit, path):
    return json.loads(blob(commit, path))

def pointer(obj, p):
    for key in p.strip('/').split('/') if p else []:
        key = key.replace('~1', '/').replace('~0', '~')
        obj = obj[int(key)] if isinstance(obj, list) else obj[key]
    return obj

def verify(binding, label, reference=False):
    b = blob(binding['commit'], binding['path'], reference)
    actual = {'git_blob': git('rev-parse', binding['commit'] + ':' + binding['path'], reference=reference).decode().strip(), 'sha256': digest(b), 'bytes': len(b)}
    ok = all(actual[k] == binding[k] for k in actual if k in binding)
    check(label, ok)
    bindings.append({'label': label, 'commit': binding['commit'], 'path': binding['path'], **actual, 'verified': ok})
    return b

dispatch = load(PUBLICATION, PREFIX + 'author-draft-1/original-sync-3/full-review-dispatch.json')
for key, binding in dispatch.items():
    if isinstance(binding, dict) and all(k in binding for k in ('commit', 'path', 'git_blob', 'sha256', 'bytes')):
        verify(binding, 'dispatch/' + key)
contract = load(PACKET, PREFIX + 'refreeze-after-B13-C-1/B16-downstream-contract.json')
controls = load(PACKET, PREFIX + 'refreeze-after-B13-C-1/original-and-acceptance-controls.json')
effective = load(PACKET, PREFIX + 'refreeze-after-B13-C-1/effective-case-constraints.json')
manifest = load(CANDIDATE, PREFIX + 'candidate-1/complete-after-original-scope-3/manifest.json')
for planned in contract['planned_reads']:
    verify(planned['input'], 'planned-identity/' + planned['path'])
reuse = load(CANDIDATE, PREFIX + 'author-draft-1/input-verification.json')['reused_files']
check('reuse/49-finite-identities', len(reuse) == 49)
for entry in reuse:
    verify(entry, 'finite-reuse-identity/' + entry['path'])
check('candidate/tree', git('rev-parse', CANDIDATE + '^{tree}').decode().strip() == dispatch['candidate_tree'])
check('base/tree', git('rev-parse', BASE + '^{tree}').decode().strip() == dispatch['formal_input_tree'])
check('publication/immediate-parent', git('rev-parse', PUBLICATION + '^').decode().strip() == CANDIDATE)
check('controls/24-20', len(controls['controls']) == 24 and sum(c['primary'] for c in controls['controls']) == 20)
check('controls/ordered-ids', [c['id'] for c in controls['controls']] == dispatch['contribution_ids'])
check('controls/primary-ids', [c['id'] for c in controls['controls'] if c['primary']] == dispatch['primary_ids'])
control_inventory = []
for i, c in enumerate(controls['controls']):
    for field, bindkey, hashkey in [('whole_original_object', 'whole_original_object_binding', 'whole_original_object_sha256'), ('whole_approved_acceptance_object', 'whole_approved_acceptance_binding', 'whole_acceptance_object_sha256')]:
        binding = c[bindkey]
        raw = verify(binding, c['id'] + '/' + field)
        exact = pointer(json.loads(raw), binding['pointer'])
        check(c['id'] + '/' + field + '/complete-equality', exact == c[field])
        check(c['id'] + '/' + field + '/canonical-hash', digest(canonical(c[field])) == c[hashkey])
    q = c['complete_current_control_fields']
    accepted = c['whole_approved_acceptance_object']
    check(c['id'] + '/all-current-fields', all(q[k] == accepted[k] for k in q))
    control_inventory.append({'id': c['id'], 'primary': c['primary'], 'pointer': '/controls/' + str(i), 'original_object_sha256': c['whole_original_object_sha256'], 'approved_object_sha256': c['whole_acceptance_object_sha256'], 'current_fields': list(q), 'root_count': len(q.get('root_adjudications', [])), 'extension_count': len(q.get('extensions', [])), 'complete_fields_canonical_sha256': digest(canonical(q))})
check('effective/all-12', len(effective['full_exact_values']) == 12)
for x in effective['full_exact_values']:
    q = next(c for c in controls['controls'] if c['id'] == x['id'])['complete_current_control_fields']
    check(x['id'] + '/effective-complete-equality', q['effective_case_constraints'] == x['aggregate'])
    check(x['id'] + '/effective-canonical-hash', digest(canonical(x['aggregate'])) == x['canonical_json_sha256'])

diff = git('diff', '--binary', BASE, CANDIDATE)
(OUT / 'complete-FIX_BASE-to-candidate.diff').write_bytes(diff)
status = git('diff', '--name-status', '-z', BASE, CANDIDATE).decode().split('\0')[:-1]
changed = list(zip(status[::2], status[1::2]))
paths = [p for s, p in changed]
payload = {x['path'] for x in manifest['outputs']}
check('diff/78-files', len(changed) == 78)
check('diff/11-existing-payload-67-own-added', all((s == 'M' and p in payload) or (s == 'A' and p.startswith(PREFIX + ('author-draft-1/' if 'author-draft-1/' in p else 'candidate-1/'))) for s, p in changed) and len(payload) == 11)
diff_inventory = []
blocks = re.split(rb'(?m)(?=^diff --git )', diff)
check('diff/complete-unfiltered-records', len([b for b in blocks if b]) == len(changed))
for (s, path), block in zip(changed, [b for b in blocks if b]):
    data = blob(CANDIDATE, path)
    rec = {'status': s, 'path': path, 'bytes': len(data), 'sha256': digest(data), 'git_blob': git('rev-parse', CANDIDATE + ':' + path).decode().strip(), 'diff_block_bytes': len(block), 'diff_block_sha256': digest(block), 'hunks': re.findall(r'^@@.*@@.*$', block.decode(), re.M), 'role': 'payload' if path in payload else 'own-evidence'}
    if path.endswith('.json'):
        obj = json.loads(data)
        rec['parsed_complete_JSON'] = True
        rec['top_level_keys'] = list(obj) if isinstance(obj, dict) else None
    diff_inventory.append(rec)
output_inventory = []
for o in manifest['outputs']:
    path = o['path']
    verify(o['before'], path + '/before')
    b = verify({'commit': CANDIDATE, 'path': path, **o['after']}, path + '/after')
    if 'authorized_after' in o:
        after = verify(o['authorized_after'], path + '/authorized-after')
        check(path + '/scope3-after-exact', b == after)
    else:
        check(path + '/six-net-unchanged-from-prior-author', b == blob('2c2b11e03e24155b5eda8508ec8172c5912156cf', path))
    output_inventory.append({'path': path, 'kind': o['kind'], 'before': o['before'], 'after': o['after']})

# Independently replay only the textual combined patch in memory, not git apply or old programs.
scope = load(dispatch['scope_receipt']['commit'], dispatch['scope_receipt']['path'])
request = load('b038cbb8b98bb6c374854b745ccce4ac1a4b3983', PREFIX + 'author-draft-1/original-scope-request-3/scope-request.json')
scope_ids = {i for f in request['files'] for i in f['qualified_ids']}
check('scope3/5-files-20-ids-21-groups-28-replacements', len(request['files']) == 5 and len(scope_ids) == 20 and sum(len(f['qualified_ids']) for f in request['files']) == 21 and sum(len(f['clauses']) for f in request['files']) == 28)
for f, grant in zip(request['files'], scope['granted_files']):
    check(f['path'] + '/scope3-qualified-groups', f['path'] == grant['path'] and f['qualified_ids'] == grant['qualified_ids'] and len(f['clauses']) == grant['declared_clause_count'])
    for key in ('current_before', 'before_snapshot_reuse', 'complete_combined_patch', 'complete_proposed_after', 'scope_request_file'):
        verify(grant[key], f['path'] + '/scope3/' + key)
    before_text = blob(BASE, f['path']).decode()
    after_text = blob(CANDIDATE, f['path']).decode()
    for n, clause in enumerate(f['clauses']):
        check(f['path'] + '/clause/' + str(n), before_text.count(clause['before']) == 1 and after_text.count(clause['proposed_after']) == 1)
patch_records = []
for o in manifest['outputs'][6:]:
    path = o['path']; name = Path(path).name
    patchpath = PREFIX + 'author-draft-1/original-scope-request-3/combined-patches/' + name + '.patch'
    patch = blob(CANDIDATE, patchpath).decode().splitlines(keepends=True)
    before = blob(BASE, path).decode().splitlines(keepends=True)
    produced = []; cursor = 0; hunks = 0; i = 0
    while i < len(patch):
        header = re.match(r'@@ -(\d+)(?:,(\d+))? \+(\d+)(?:,(\d+))? @@', patch[i])
        if not header:
            i += 1; continue
        start = int(header[1]) - 1
        produced.extend(before[cursor:start]); cursor = start; i += 1; hunks += 1
        while i < len(patch) and not patch[i].startswith('@@'):
            line = patch[i]; i += 1
            if line.startswith((' ', '-')):
                assert before[cursor] == line[1:], (path, cursor)
                cursor += 1
            if line.startswith((' ', '+')):
                produced.append(line[1:])
    produced.extend(before[cursor:])
    check(path + '/one-complete-textual-patch', ''.join(produced).encode() == blob(CANDIDATE, path))
    patch_records.append({'path': path, 'patch_path': patchpath, 'hunks': hunks, 'textual_applications': 1, 'patch_sha256': digest(blob(CANDIDATE, patchpath))})

def tree(commit):
    result = {}
    for entry in git('ls-tree', '-r', '-z', commit).split(b'\0'):
        if entry:
            meta, path = entry.split(b'\t'); result[path.decode()] = meta.decode()
    return result

bt = tree(BASE); ct = tree(CANDIDATE)
old_changes = [p for p in bt if ct.get(p) != bt[p]]
check('all-existing-files-except-11-byte-preserved', set(old_changes) == payload, old_changes)
old_B16 = [p for p in bt if p.startswith(PREFIX)]
check('baseline-existing-B16-evidence-preserved', all(bt[p] == ct[p] for p in old_B16), len(old_B16))
prior_tree = tree('2c2b11e03e24155b5eda8508ec8172c5912156cf')
old64 = [p for p in prior_tree if p.startswith(PREFIX + 'author-draft-1/') or p.startswith(PREFIX + 'candidate-1/')]
old64 += [o['path'] for o in manifest['outputs'][:6]]
check('prior-author-64-physical-artifacts-byte-preserved', len(old64) == 64 and all(prior_tree[p] == ct[p] for p in old64), {'count': len(old64), 'composition': '58 prior own evidence files plus six sanitized outputs; distinct from 23 B16 administrative files already at FIX_BASE'})
receipt_binding = contract['reading_preparation_reuse']['complete_current_accepted_receipts']
receipt_bytes = verify(receipt_binding, 'accepted240/fixed-receipts')
receipt_path = receipt_binding['path']; rb = json.loads(receipt_bytes)
receipts = rb['accepted_contribution_receipts']
check('accepted240/receipt-file-byte-preserved', receipt_bytes == blob(CANDIDATE, receipt_path))
check('accepted240/exact-count-and-unique-batch-id', len(receipts) == 240 and len({(r['batch'], r['id']) for r in receipts}) == 240)
check('accepted240/all-PASS_SCOPED', all(r['verdict'] == 'PASS_SCOPED' for r in receipts))
receipt_inventory = [{**r, 'receipt_canonical_sha256': digest(canonical(r)), 'preservation': 'Entire fixed receipt file and all preexisting formal/review files except the 11 explicitly examined B16 outputs retained. Changed shared clauses require this FULL quality comparison and separate affected gate, not 240 recursive reapprovals.'} for r in receipts]

catalog = manifest['outputs'][0]['path']
def rows(data):
    result = []; section = ''
    for line in data.decode().splitlines():
        if line.startswith('## '): section = line
        m = re.match(r'^\| ([A-Z][A-Z0-9-]*\d[A-Za-z0-9-]*) \|', line)
        if m: result.append({'section': section, 'id': m[1], 'text': line})
    return result

old_rows = rows(blob(BASE, catalog)); new_rows = rows(blob(CANDIDATE, catalog))
new_old = [r for r in new_rows if not r['id'].startswith('B16-')]
check('catalog/old-order-and-multiplicity', [(r['section'], r['id']) for r in old_rows] == [(r['section'], r['id']) for r in new_old])
row_changes = [{'before': a, 'after': b} for a, b in zip(old_rows, new_old) if a != b]
changed_ids = ['T01', 'T03', 'A23', 'A31', 'A32', 'A33', 'A38', 'C05', 'C24']
check('catalog/460-old-451-unchanged-9-assigned', len(old_rows) == 460 and len(row_changes) == 9 and [x['before']['id'] for x in row_changes] == changed_ids)
check('catalog/24-new-exact-ids', [r['id'] for r in new_rows if r['id'].startswith('B16-')] == [x.replace('GIR-FD82-', 'B16-') for x in dispatch['contribution_ids']])
check('catalog/old-C29-byte-preserved', next(r for r in old_rows if r['id'] == 'C29') == next(r for r in new_rows if r['id'] == 'C29'))

source_log_path = PREFIX + 'author-preparation-1/source-reading-log.json'
source_log = load('b48e919cce08058bcd29453232d4eb55aa9e9563', source_log_path)
reused_sources = []
for e in source_log['reading']:
    if e['commit'] != REF:
        continue  # Prior project locators are navigation; current payloads checked above.
    data = verify(e, 'reused-source/' + e['path'], reference=True)
    range_results = []
    for r in e['ranges']:
        a, b = map(int, r['lines'].split('-'))
        actual = digest(b''.join(data.splitlines(keepends=True)[a-1:b]))
        check('reused-source/' + e['path'] + '/' + r['lines'], actual == r['sha256'])
        range_results.append({'lines': r['lines'], 'sha256': actual, 'exact_equal_prior_log': actual == r['sha256']})
    reused_sources.append({'commit': REF, 'path': e['path'], 'git_blob': e['git_blob'], 'sha256': e['sha256'], 'bytes': e['bytes'], 'ranges': range_results, 'use': 'Exact prior bounded static reading reused; byte/range verification here is metadata, not new whole-source semantic inspection.'})
check('reference/fixed-tree', git('rev-parse', REF + '^{tree}', reference=True).decode().strip() == '7589c800b61ba13a13040ed0d686979b80a84fd0')

result = {'role': 'INDEPENDENT_CANDIDATE_FULL_R-B16', 'reviewed_commit': CANDIDATE, 'reviewed_tree': dispatch['candidate_tree'], 'FIX_BASE': BASE, 'publication_read_only': PUBLICATION, 'checks': checks, 'check_count': len(checks), 'failed_checks': [c for c in checks if not c['pass']], 'inputs': bindings, 'complete_unfiltered_diff': {'command': ['git', 'diff', '--binary', BASE, CANDIDATE], 'bytes': len(diff), 'sha256': digest(diff), 'files': len(changed), 'no_path_filter': True, 'inventory': diff_inventory}, 'outputs': output_inventory, 'controls': control_inventory, 'effective_cases': effective['full_exact_values'], 'scope3_patch_checks': patch_records, 'accepted240': receipt_inventory, 'catalog': {'old_rows': len(old_rows), 'unchanged_old_rows': len(old_rows)-len(row_changes), 'changes': row_changes, 'new_rows': [r for r in new_rows if r['id'].startswith('B16-')]}, 'reused_source_evidence': {'commit': 'b48e919cce08058bcd29453232d4eb55aa9e9563', 'path': source_log_path, 'git_blob': git('rev-parse', 'b48e919cce08058bcd29453232d4eb55aa9e9563:' + source_log_path).decode().strip(), 'sha256': digest(blob('b48e919cce08058bcd29453232d4eb55aa9e9563', source_log_path)), 'entries': reused_sources}, 'execution_boundary': {'new_metadata_verifier_only': True, 'reference_game_Ruby': 0, 'historical_programs': 0, 'behavior_vectors': 0, 'runtime_observations': 0, 'proven_Demo_chains': 0}, 'metadata_checks_are_not_semantic_quality_verdict': True}
(OUT / 'metadata-verification.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({'checks': len(checks), 'failed': result['failed_checks'], 'diff_bytes': len(diff), 'diff_files': len(changed), 'payloads': len(payload), 'old_B16_files': len(old_B16), 'accepted_receipts': len(receipts), 'old_catalog_rows': len(old_rows), 'changed_old_rows': len(row_changes), 'reused_source_files': len(reused_sources)}, ensure_ascii=False))
