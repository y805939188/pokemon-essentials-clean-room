import datetime, difflib, hashlib, json, pathlib, subprocess

OUT = pathlib.Path(__file__).resolve().parent
ACTUAL = '9d5b4e99b617828690e6529b77a1e555d7c9eb1b'
INPUT = 'review/remediation-sixth-20261014-prepare/integration/U01-U12-U14-composite-20261014/actual-review-input.json'
GROUP = ['R6-U10', 'R6-U11', 'R6-U12']
calls = []

def git(*args):
    start = datetime.datetime.now(datetime.timezone.utc).isoformat()
    p = subprocess.run(['git', *args], capture_output=True)
    calls.append({'argv': ['git', *args], 'cwd': str(pathlib.Path.cwd()), 'start_utc': start,
                  'end_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
                  'exit_code': p.returncode, 'stdout_bytes': len(p.stdout),
                  'stdout_sha256': hashlib.sha256(p.stdout).hexdigest(),
                  'stderr': p.stderr.decode('utf-8', errors='replace')})
    if p.returncode:
        raise RuntimeError(calls[-1])
    return p.stdout

def ident(data):
    return {'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest(),
            'git_blob': hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()}

input_bytes = git('show', ACTUAL+':'+INPUT)
j = json.loads(input_bytes)
expected_input = {'bytes': 124082, 'sha256': '7b63483a915792c077b2f8cf84208e9f5a7ac94e55ce93cfc8bbde718bf6d9aa', 'git_blob': 'f7f220a4ee7c4b2ff6dc94b799fe54b13879b6c8'}
assert ident(input_bytes) == expected_input
assert git('rev-parse', ACTUAL+'^{tree}').decode().strip() == 'faae3b9a22c37a2e2e994553f59e7099c6394db0'
assert git('rev-parse', ACTUAL+':deliverables/final-specification-set').decode().strip() == '74dccc64506d008d50cf1cdfd906f701931020cc'
batches = [b for b in j['batches'] if b['batch'] in GROUP]
assert len(batches) == 3
paths = sorted(set(p for b in batches for p in b['all_candidate_allowlist_paths']))
records = []
for b in batches:
    contract = git('show', ACTUAL+':'+b['contract_path'])
    assert ident(contract) == b['contract_identity']
    review = b['independent_review']
    report = git('show', review['review_commit']+':'+review['report_path'])
    assert ident(report) == review['report_identity']
    assert git('rev-parse', b['candidate_published_commit']+'^{tree}').decode().strip() == b['candidate_workspace_tree']
    assert git('rev-parse', review['review_commit']+'^{tree}').decode().strip() == review['review_workspace_tree']
for path in paths:
    f = next(f for f in j['files'] if f['path'] == path)
    data = git('show', ACTUAL+':'+path)
    assert ident(data) == f['actual']
    base = git('show', j['fixed_main']+':'+path)
    assert ident(base) == f['baseline']
    line_data = data.decode('utf-8').splitlines(keepends=True)
    line_base = base.decode('utf-8').splitlines(keepends=True)
    contributions = []
    for c in f['contributions']:
        cand = git('show', c['candidate_commit']+':'+c['candidate_path'])
        assert ident(cand) == c['identity']
        clines = cand.decode('utf-8').splitlines(keepends=True)
        blocks = []
        for kind, a, z, x, y in difflib.SequenceMatcher(None, line_base, clines, autojunk=False).get_opcodes():
            if kind == 'equal':
                continue
            replacement = ''.join(clines[x:y]).encode('utf-8')
            blocks.append({'kind': kind, 'baseline_lines': [a+1,z], 'candidate_lines': [x+1,y],
                           'replacement_bytes': len(replacement), 'replacement_sha256': hashlib.sha256(replacement).hexdigest(),
                           'replacement_present_in_actual': replacement in data if replacement else None})
        contributions.append({'batch': c['batch'], 'candidate_commit': c['candidate_commit'], 'candidate_path': c['candidate_path'],
                              'identity': c['identity'], 'same_as_actual': cand == data, 'blocks': blocks})
    tree_entry = git('ls-tree', ACTUAL, path).decode().strip()
    assert tree_entry.startswith('100644 blob '+f['actual']['git_blob']+'\t')
    records.append({'path': path, 'identity': ident(data), 'physical_lines': len(line_data), 'mode': '100644',
                    'contributions': contributions, 'pending_primary_writers': f['pending_primary_writers']})
payload_commit = j['receiver_delta']['payload_commit']
payload_path = j['receiver_delta']['payload_path']
payload_bytes = git('show', payload_commit+':'+payload_path)
payload = json.loads(payload_bytes)
receiver = next(f for f in records if f['path'] == payload['receiver_path'])
receiver_contribution = receiver['contributions'][0]
receiver_candidate = git('show', receiver_contribution['candidate_commit']+':'+receiver_contribution['candidate_path'])
receiver_actual = git('show', ACTUAL+':'+payload['receiver_path'])
old = payload['old_full_line'].encode('utf-8')
new = payload['proposed_full_line'].encode('utf-8')
assert receiver_candidate.count(old) == 1
assert receiver_candidate.replace(old, new) == receiver_actual
receiver_check = {'exact_single_clause_replacement': True, 'delta_bytes': len(receiver_actual)-len(receiver_candidate),
                  'acceptance': 'COPY_PRESENT_ONLY_PENDING_U13', 'signature_excludes_id': 'GR6-F-002'}
ui_path = 'deliverables/final-specification-set/test-catalog/user-interface-wp17-63-65-66-67-68-69-70-71.md'
ui_base = git('show', j['fixed_main']+':'+ui_path).decode('utf-8').splitlines()
ui_actual = git('show', ACTUAL+':'+ui_path).decode('utf-8').splitlines()
old_rows = [r for r in ui_base if r.startswith('|')]
new_rows = [r for r in ui_actual if r.startswith('|')]
replaced = [r for r in old_rows if r not in new_rows]
assert len(replaced) == 2 and replaced[0].startswith('| C12 |') and replaced[1].startswith('| C36 |')
ui_check = {'baseline_physical_lines': len(ui_base), 'actual_physical_lines': len(ui_actual),
            'baseline_table_lines': len(old_rows), 'actual_table_lines': len(new_rows),
            'table_count_includes_headers_and_separators': True,
            'old_table_lines_replaced': ['C12', 'C36'], 'other_old_table_lines_retained': True,
            'composition_physical_line_deltas': {'R6-U11':31, 'R6-U10':64, 'R6-U12':17},
            'counts_do_not_mean_executed_vectors': True}
result = {'schema': 'r6.actual.group-d.fixed-validation.v1', 'actual_commit': ACTUAL,
          'workspace_tree': 'faae3b9a22c37a2e2e994553f59e7099c6394db0',
          'formal_tree': '74dccc64506d008d50cf1cdfd906f701931020cc',
          'input_path': INPUT, 'input_identity': ident(input_bytes), 'group': GROUP,
          'scope_ids': [i for b in batches for i in b['required_ids']],
          'batches': batches, 'files': records,
          'pending_candidates': j['pending_candidates'], 'receiver_delta': j['receiver_delta'],
          'receiver_payload_identity': ident(payload_bytes), 'receiver_payload': payload, 'receiver_check': receiver_check,
          'administrative_sync': j['administrative_sync'], 'shared_ui_retention': ui_check,
          'qualification': 'Mechanical identity and replacement retention only; semantic reading is separately attributed in report and ledgers.',
          'all_assertions_passed': True}
(OUT/'fixed-validation.json').write_text(json.dumps(result, ensure_ascii=False, indent=2)+'\n')
(OUT/'validation-command-receipts.json').write_text(json.dumps(calls, ensure_ascii=False, indent=2)+'\n')
missing = [(f['path'], c['batch'], b['candidate_lines']) for f in records for c in f['contributions'] for b in c['blocks'] if b['replacement_present_in_actual'] is False]
print(json.dumps({'files': len(records), 'bytes': sum(f['identity']['bytes'] for f in records), 'ids': result['scope_ids'],
                  'input_identity': ident(input_bytes), 'replacement_blocks_not_literal': missing,
                  'commands': len(calls), 'receiver_payload': payload}, ensure_ascii=False, indent=2))
