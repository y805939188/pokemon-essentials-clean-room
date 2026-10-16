import collections
import datetime
import hashlib
import json
import pathlib

OWN = pathlib.Path(__file__).resolve().parent
BASE = OWN.parent.parent
started = datetime.datetime.now(datetime.timezone.utc).isoformat()
names = ['progress.json', 'input-identities.json', 'reading-ledger.json', 'file-coverage.json',
         'atomic-and-interface-denominator.json', 'acceptance-register.json', 'coverage-gaps.json',
         'next-dispatch.json', 'execution-records.json']
docs = {name: json.loads((OWN / name).read_text()) for name in names}
assert (OWN / 'review.md').is_file()
ledger = docs['reading-ledger.json']
groups = collections.defaultdict(list)
for row in ledger['snapshot_payloads']:
    raw = (BASE / row['snapshot']).read_bytes()
    assert len(raw) == row['bytes']
    assert hashlib.sha256(raw).hexdigest() == row['sha256']
    groups[row['sha256']].append(row)
assert len(ledger['snapshot_payloads']) == 301 and len(groups) == 289
pending = [rows[0] for rows in groups.values()
           if not any(r['read_state'].startswith(('FULL_', 'SAME_BYTES_LINK')) for r in rows)]
unread_bytes = sum(r['bytes'] for r in pending)
read_count = len(groups) - len(pending)
progress = docs['progress.json']
assert progress['personally_current_semantic_full_frozen_artifacts'] == read_count
assert progress['pending_unique_sha'] == len(pending)
assert progress['pending_unique_bytes'] == unread_bytes
assert ledger['current_semantically_read_unique_sha'] == read_count
assert ledger['remaining_not_fully_personally_semantically_read_unique_sha'] == len(pending)
assert ledger['remaining_not_fully_personally_semantically_read_unique_bytes'] == unread_bytes
dispatch = docs['next-dispatch.json']['auditor_remaining_reception']
assert dispatch['remaining_unique_sha'] == len(pending)
assert dispatch['remaining_unique_bytes'] == unread_bytes
assert progress['own_R_full_source_reads'] == ledger['audit_own_R_full_text_reads']
assert progress['own_F_full_source_reads'] == ledger['audit_own_formal_full_text_reads']
assert progress['update_started'] is False
files = docs['file-coverage.json']['files']
assert len(files) == 563
assert len({(r['repo'], r['path']) for r in files}) == 563
assert sum(r['repo'] == 'R' for r in files) == 432
assert sum(r['repo'] != 'R' for r in files) == 131
assert progress['own_R_full_source_reads'] == sum(r['repo'] == 'R' and r['audit_own_source_or_formal_full_read'] for r in files)
assert progress['own_F_full_source_reads'] == sum(r['repo'] != 'R' and r['audit_own_source_or_formal_full_read'] for r in files)
assert all(r['accepted_full_file_count_credit'] == 0 for r in files)
atomic = docs['atomic-and-interface-denominator.json']
assert len(atomic['old_locator_rows']) == 4643
assert docs['acceptance-register.json']['global_or_full_domain_pass_signed_by_this_auditor'] is False
assert docs['acceptance-register.json']['whole_review_required_count'] in (None, 'UNKNOWN_NOT_FINAL')
receipt_count = 0
receipt_output_bytes = 0
for path in sorted(OWN.glob('*.receipt.json')):
    receipt = json.loads(path.read_text())
    if not {'source', 'source_sha256', 'stdout_path', 'stdout_sha256', 'displayed_view_lines'} <= set(receipt):
        continue
    source = (OWN / receipt['source']).read_bytes()
    output = (OWN / receipt['stdout_path']).read_bytes()
    assert hashlib.sha256(source).hexdigest() == receipt['source_sha256'], path
    assert len(output) == receipt['stdout_bytes'], path
    assert hashlib.sha256(output).hexdigest() == receipt['stdout_sha256'], path
    start, end = receipt['displayed_view_lines']
    assert 1 <= start <= end <= receipt['source_lines'], path
    exact_window = ''.join(source.decode('utf-8').splitlines(keepends=True)[start-1:end]).encode('utf-8')
    assert exact_window == output, path
    assert receipt['exit_code'] == 0 and receipt['stderr'] == '', path
    receipt_count += 1
    receipt_output_bytes += len(output)
metrics = json.loads((OWN / 'supporting-submission-metrics.v1.json').read_text())
assert metrics['current_field_or_explicit_purpose_qualified_unique_sha'] == read_count == 289
assert metrics['standalone_strict_or_mixed_purpose_unique_artifacts'] == 15
assert metrics['other_current_field_receipt_qualified_unique_artifacts'] == 274
assert metrics['literal_all_original_payloads_read'] is False
purpose = json.loads((OWN / 'candidate5-strict-purpose-actual-reception.v1.json').read_text())
assert purpose['complete_current_json_fields_read'] is False
assert purpose['all_candidate_literal_bodies_personally_read'] is False
assert purpose['captured_UNREAD_records'] == 78213
assert purpose['source_formal_atomic_interface_task_global_credit'] == 0
late = json.loads((OWN / 'pending-late-deltas.fixed.v1.json').read_text())
assert late['not_part_of_original301_or289'] is True
assert late['all_text_bodies_not_fully_received_in_this_context'] is True
for item in late['files']:
    raw = (OWN / item['frozen_copy']).read_bytes()
    assert len(raw) == item['bytes']
    assert hashlib.sha256(raw).hexdigest() == item['sha256']
    assert item['source_formal_atomic_consumer_task_credit'] == 0
assert len(late['files']) == late['path_count'] == 59
assert sum(r['bytes'] for r in late['files']) == late['path_bytes'] == 108228892
overlay = json.loads((OWN / 'exited35-current-supporting-overlay.v2.json').read_text())
assert len(overlay['rows']) == 35
assert all(r['task_final_accepted'] is False for r in overlay['rows'])
assert overlay['task_final_accepted_count'] == 0
jobs = json.loads((OWN / 'remaining-semantic-consumer-reception-jobs.v1.json').read_text())
assert len(jobs['jobs']) == 9
assert jobs['not_actual_start_or_new_context_count'] is True
assert {h for j in jobs['jobs'] for h in j['input_exact_sha']} == {r['sha256'] for r in late['files']}
ended = datetime.datetime.now(datetime.timezone.utc).isoformat()
result = {'schema': 'gr8-incremental-current-package-integrity/v2', 'began_utc': started,
          'ended_utc': ended, 'exit_code': 0, 'result': 'STRUCTURAL_IDENTITY_ONLY_PASS',
          'required_artifacts_present': 10, 'json_parse_documents': len(docs),
          'fixed_original_paths': 301, 'fixed_unique_sha': 289,
          'current_field_read_or_strict_purpose_qualified_sha': read_count,
          'current_not_full_received_sha': len(pending), 'current_not_full_received_original_bytes': unread_bytes,
          'per_file_rows': 563, 'old_pending_locator_rows': 4643,
          'own_captured_read_receipts_identity_checked': receipt_count,
          'captured_stdout_bytes_identity_checked': receipt_output_bytes,
          'receipt_exact_source_windows_identity_checked': True,
          'standalone_strict_or_mixed_purpose_artifacts': 15,
          'other_current_field_qualified_artifacts': 274,
          'all_original_candidate_literal_bodies_read': False,
          'selected_late_unreceived_handoff_paths': 59,
          'selected_late_unreceived_handoff_bytes': 108228892,
          'exited35_overlay_rows': 35, 'new_ready_receiving_jobs_not_starts': 9,
          'receipt_output_identity_is_not_actual_semantic_reading': True,
          'upstream_raw_source_IO_EOF_independently_verified_by_this_check': False,
          'global_semantic_pass': False, 'audit_contract_complete': False,
          'supporting_work_delivered_for_root_reception': True,
          'audit_contract_complete_false_qualification': 'No self-signed task-final; actual independent root supporting-contract reception is pending. This is not a requirement to redo all primary domains inside the supporting task.',
          'business_execution': 'NOT_EXECUTED', 'update_state': 'UPDATE_NOT_STARTED'}
old = OWN / 'validation.json'
backup = OWN / 'validation.before-current-integrity.json'
if old.exists() and not backup.exists():
    backup.write_bytes(old.read_bytes())
old.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
print(json.dumps(result))
