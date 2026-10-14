import datetime, hashlib, json, pathlib, re, subprocess, sys

BASE = pathlib.Path('/workspace/pokemon-essentials-clean-room')
OUT = BASE / 'review/remediation-sixth-20261014-prepare/actual-reviews/group-E/facility'
ACTUAL = '86bbc99b28d93db4ed9d6897daf5f3725ccd1808'
OLD_REVIEW = '3ef4854ef43eac92fd1dc57350e4cf6aa160082b'
REPAIRED = '9971fe84896786645cdcda3ab45e5caf7785cabc'
REF = '8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
started = datetime.datetime.now(datetime.timezone.utc).isoformat()

def blob(commit, path):
    return subprocess.check_output(['git', 'show', commit + ':' + path])

def identity(raw):
    return {'bytes': len(raw), 'sha256': hashlib.sha256(raw).hexdigest(),
            'git_blob': hashlib.sha1(b'blob ' + str(len(raw)).encode() + b'\0' + raw).hexdigest()}

checks = {}
source_bindings = []
contract_path = 'review/remediation-sixth-20261014-prepare/contracts/R6-U13.json'
contract_raw = blob(ACTUAL, contract_path)
contract = json.loads(contract_raw)
checks['contract_exact_bytes_equal_469a_00b45_9971_actual'] = all(
    blob(c, contract_path) == contract_raw for c in [
        '469a268b92daed7b4d28d7fd0da75520cbb7228f',
        '00b45de642f07cee9953e42f04cce9c35d77346f', REPAIRED])
checks['contract_identity'] = identity(contract_raw)
for i, record in enumerate(contract['scope_contracts']):
    if record['id'] not in ['GR6-F-001', 'GR6-F-002']:
        continue
    derived = json.loads((OUT / (record['id'] + '-actual-contract-record.json')).read_text())
    checks[record['id'] + '_complete_record_projection_equal'] = derived == record
    source_bindings.append({'path': contract_path, 'commit': ACTUAL,
                            'json_pointer': '/scope_contracts/' + str(i),
                            'identity': identity(contract_raw),
                            'projection_path': record['id'] + '-actual-contract-record.json',
                            'projection_identity': identity((OUT / (record['id'] + '-actual-contract-record.json')).read_bytes())})

relevant = json.loads((OUT / 'actual-input-relevant.json').read_text())
file_bindings = []
for record in relevant['files']:
    path = record['path']
    raw = blob(ACTUAL, path)
    checks[path + ':input_actual_identity_matches'] = identity(raw) == record['actual']
    c = record['contributions'][0]
    contributed = blob(c['candidate_commit'], c['candidate_path'])
    checks[path + ':contribution_identity_matches'] = identity(contributed) == c['identity']
    if c['batch'] == 'R6-U13':
        checks[path + ':actual_equals_repaired_mirror'] = raw == contributed
    file_bindings.append({'path': path, 'actual_commit': ACTUAL, 'identity': identity(raw),
                          'contribution': c})

ui_path = 'deliverables/final-specification-set/user-interface/wp66-a-party-and-summary-ui.md'
payload_path = 'review/remediation-sixth-20261014-prepare/reviews/R6-U13-R/facility/wp66-a-receiver-payload.json'
payload_raw = blob(OLD_REVIEW, payload_path)
payload = json.loads(payload_raw)
u10 = next(x for x in relevant['files'] if x['path'] == ui_path)['contributions'][0]
u10_raw = blob(u10['candidate_commit'], u10['candidate_path'])
old_line = payload['old_full_line'].encode()
new_line = payload['proposed_full_line'].encode()
checks['U10_receiver_old_line_exact_single_occurrence'] = u10_raw.count(old_line) == 1
reconstructed = u10_raw.replace(old_line, new_line, 1)
ui_actual = blob(ACTUAL, ui_path)
checks['U10_plus_exact_receiver_full_file_equals_actual'] = reconstructed == ui_actual
checks['WP66A_actual_line132_exact_receiver_full_line'] = ui_actual.decode().splitlines()[131] == payload['proposed_full_line']
checks['WP66A_receiver_byte_delta_245'] = len(ui_actual) - len(u10_raw) == 245
checks['WP66A_previous_actual_byte_equal'] = ui_actual == blob('9d5b4e99b617828690e6529b77a1e555d7c9eb1b', ui_path)
checks['WP66A_U10_every_other_line_preserved'] = (
    u10_raw.splitlines()[:131] + u10_raw.splitlines()[132:]
    == ui_actual.splitlines()[:131] + ui_actual.splitlines()[132:])

baseline = '8ea169fbd0f33f378b5d732fd6bea59e854e04a6'
wp54 = 'deliverables/final-specification-set/combat-requirements/wp54-entry-eligibility-level-adjustment-and-clauses.md'
wp55 = 'deliverables/final-specification-set/combat-requirements/wp55-facility-session-and-restoration.md'
test = 'deliverables/final-specification-set/test-catalog/combat-requirements-wp54-55-56-58.md'
for p, line in [(wp54, 47), (wp55, 48), (wp55, 52), (wp55, 53), (wp55, 54), (wp55, 56),
                (wp55, 61), (wp55, 62), (wp55, 63), (wp55, 64), (wp55, 65), (wp55, 128)]:
    checks[p + ':baseline_line_' + str(line) + '_retained'] = (
        blob(ACTUAL, p).splitlines()[line - 1] == blob(baseline, p).splitlines()[line - 1])

def rows(raw, index):
    text = raw.decode()
    heading = [z for z in text.splitlines() if z.startswith('## ')][index]
    section = text.split(heading, 1)[1].split('\n## ', 1)[0]
    pairs = re.findall(r'^\| (Q\d+|W\d+) \|.*$', section, re.M)
    full = [z for z in section.splitlines() if re.match(r'^\| (Q\d+|W\d+) \|', z)]
    return dict(zip(pairs, full)), pairs

headings = ['## 1.', '## 2.']
test_text = blob(ACTUAL, test).decode()
section_headings = [x for x in test_text.splitlines() if x.startswith('## ')]
checks['test_section_headings'] = section_headings
for label, ids, index in [('QC', ['Q01', 'Q31'], 0),
                           ('WS', ['W14', 'W15', 'W16', 'W28', 'W29', 'W30', 'W35'], 1)]:
    current_rows, current_ids = rows(blob(ACTUAL, test), index)
    old_rows, _ = rows(blob(baseline, test), index)
    checks[label + '_raw_count'] = len(current_ids)
    checks[label + '_unique_count'] = len(set(current_ids))
    checks[label + '_no_duplicates'] = len(current_ids) == len(set(current_ids))
    for id_ in ids:
        checks[label + '-' + id_ + '_exact_baseline_retained'] = current_rows[id_] == old_rows[id_]

old_ledger_path = 'review/remediation-sixth-20261014-prepare/reviews/R6-U13-R/facility/reading-ledger.jsonl'
old_ledger_raw = blob(OLD_REVIEW, old_ledger_path)
old_records = [json.loads(z) for z in old_ledger_raw.splitlines()]
reuse = []
for i, record in enumerate(old_records):
    p = record.get('path', '')
    if (record.get('commit') == REF or '/inputs/evidence/tasks/R6-F/' in p
            or i in [49, 50, 55, 56, 57]):
        entry = {'old_reading_ledger_index': i, 'old_record': record,
                 'reuse_type': 'PREVIOUS_SEMANTIC_READ_EXACT_IDENTITY_RECHECK_NOT_FRESH_SEMANTIC_READ'}
        commit = record['commit']
        # The old owned selected B027 projection was committed only at the review publication.
        if '/reviews/R6-U13-R/facility/history-' in p:
            commit = OLD_REVIEW
        raw = blob(commit, p)
        actual_id = identity(raw)
        entry['recheck_commit'] = commit
        entry['rechecked_identity'] = actual_id
        entry['identity_matches_old_record'] = all(actual_id[k] == record[k] for k in actual_id)
        reuse.append(entry)
checks['reused_fixed_source_counter_history_identity_all_match'] = all(x['identity_matches_old_record'] for x in reuse)

result = {'utc_start': started, 'utc_end': datetime.datetime.now(datetime.timezone.utc).isoformat(),
          'cwd': str(pathlib.Path.cwd()), 'argv': sys.argv, 'exit': 0,
          'kind': 'OWN_REVIEWER_DOCUMENT_AND_IDENTITY_CHECK_ONLY_NO_SOURCE_EXECUTION',
          'actual_commit': ACTUAL,
          'actual_tree': subprocess.check_output(['git', 'rev-parse', ACTUAL + '^{tree}'], text=True).strip(),
          'formal_tree': subprocess.check_output(['git', 'rev-parse', ACTUAL + ':deliverables/final-specification-set'], text=True).strip(),
          'contract_source_bindings': source_bindings, 'file_bindings': file_bindings,
          'receiver_payload_source': {'commit': OLD_REVIEW, 'path': payload_path, 'identity': identity(payload_raw)},
          'old_ledger_source': {'commit': OLD_REVIEW, 'path': old_ledger_path, 'identity': identity(old_ledger_raw)},
          'reused_semantic_evidence': reuse, 'checks': checks,
          'all_boolean_checks_pass': all(v for v in checks.values() if isinstance(v, bool)),
          'limits': 'Identity and literal retention checks do not replace fresh semantic full-file review or establish runtime behavior.'}
(OUT / 'actual-identity-and-regression-checks.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({'all_boolean_checks_pass': result['all_boolean_checks_pass'],
                  'checks': len(checks), 'reused_reading_entries': len(reuse),
                  'QC_count': checks['QC_raw_count'], 'WS_count': checks['WS_raw_count'],
                  'output': str((OUT / 'actual-identity-and-regression-checks.json').relative_to(BASE))}, ensure_ascii=False))
assert result['all_boolean_checks_pass']
