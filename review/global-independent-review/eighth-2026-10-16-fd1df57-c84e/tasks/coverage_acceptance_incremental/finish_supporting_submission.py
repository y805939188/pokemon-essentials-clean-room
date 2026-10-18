"""Record this auditor's bounded submission; never grant task or global PASS."""
import collections
import datetime
import hashlib
import json
from pathlib import Path

OWN = Path(__file__).resolve().parent
BASE = OWN.parent.parent
now = datetime.datetime.now(datetime.timezone.utc).isoformat()
read = lambda n: json.loads((OWN / n).read_text())
write = lambda n, d: (OWN / n).write_text(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
view_path = OWN / 'candidate5-strict-inventory-purpose-view.json'
view = json.loads(view_path.read_text())
receipts = [f'candidate5-purpose-read{i:02d}.receipt.json' for i in range(1, 4)]
assert [read(n)['displayed_view_lines'] for n in receipts] == [[1, 220], [221, 450], [451, 680]]
assert all(read(n)['source_sha256'] == hashlib.sha256(view_path.read_bytes()).hexdigest() for n in receipts)
proof = {
    'schema': 'r8.coverage.candidate-five.strict-purpose-actual-reception/v1',
    'recorded_utc': now,
    'reader': '/root/coverage_acceptance_incremental',
    'source_indices': [8, 10, 12, 13, 14],
    'source_identities': [r['source'] for r in view['files']],
    'complete_current_json_fields_read': False,
    'all_current_operative_statuses_and_field_purpose_qualifications_received': True,
    'all_candidate_literal_bodies_personally_read': False,
    'administrative_candidate_identity_rows_personally_literal_read': False,
    'candidate_rows': view['all_rows_count'],
    'occurrences': view['all_occurrences_count'],
    'captured_UNREAD_records': view['U_rows_with_UNREAD_at_capture'],
    'candidate_text_unique_machine_inventory_only': view['distinct_literal_count_machine_inventory_not_reading'],
    'candidate_text_unique_utf8_bytes_machine_inventory_only': view['distinct_literal_utf8_bytes_machine_inventory_not_reading'],
    'view': {'output': view_path.name, 'bytes': view_path.stat().st_size,
             'sha256': hashlib.sha256(view_path.read_bytes()).hexdigest(), 'lines': 680},
    'actual_receipts': receipts,
    'generation_execution': 'candidate5-purpose-generation.execution.json',
    'all_field_purposes': view['complete_field_purposes'],
    'all_five_captured_statuses': [
        {'index': r['index'], 'captured_utc': r['source']['captured_utc'],
         'rows': r['row_count'], 'occurrences': r['occurrence_count'],
         'status': r['status_at_snapshot']} for r in view['files']],
    'exact_inventory_relationships': view['exact_inventory_relationships'],
    'captured_author_claims_separate': view['capture_vs_later_actual_reception'],
    'static_origin_source_receptions': {
        'cab9_controller_prepare': 'candidate5-origin-controller-read.receipt.json',
        'cab9_controller_disposition_consumer': 'candidate5-origin-controller-dispose-read.receipt.json',
        'current_remaining_prepare': 'candidate5-origin-remaining-prepare-read.receipt.json',
        'current_continuation_generator': 'candidate5-origin-continuation-read.receipt.json',
        'current_numeric_filter_generator': 'candidate5-origin-numeric-read.receipt.json',
        'current_game_pending_generator': 'candidate5-origin-game-structure-read.receipt.json',
        'identity_receipts': ['candidate5-origin-retrieval.execution.json',
                              'candidate5-origin-current-source-freeze.execution.json',
                              'candidate5-origin-final-retrieval.execution.json'],
        'qualification': 'All six named helper sources actually read complete, none executed. Four CURRENT helper sources are explicit late local identities, not backfilled as cab9 artifacts. Exact S-index construction operation not locally located; fixed S content/allowlist and consumer routing are directly checked, no original I/O invented.',
    },
    'failed_checks_preserved': [
        {'execution': 'candidate5-purpose-generation.execution.json.failed-01-preserved',
         'actual_tool_chunk': 'f6f451', 'exit_code': 1,
         'reason': 'My overly strong all-reference-equality assumption rejected the real U29194 one-reference delta. Original data preserved; complete two records read, no source bug inferred.'},
        {'execution': 'candidate5-purpose-generation.execution.json.failed-02-preserved',
         'actual_tool_chunk': '5c7971', 'exit_code': 1,
         'reason': 'My diagnostic changed list contains string IDs; incorrect string dictionary access. Fixed own helper, no source problem or missing host capability.'},
        {'execution': 'candidate5-origin-retrieval.execution.json',
         'actual_tool_chunk': '38cb19', 'individual_git_show_exit': 128,
         'reason': 'Three remaining-task helper paths absent in cab9 Git tree though locally available. Exact stderr retained and later CURRENT local static-source freeze/read explicitly separate. Not a host/material limit.'},
    ],
    'supporting_purpose_rule': 'Original5545B contract permits administrative/identity indexes inventory-only. Parent expressly confirmed only true generated candidate indexes with no manual facts/clauses/consumer judgments may receive this typed-purpose disposition; actual mixed effective values must be read. Exhaustive field allowlist and actual complete purpose/status view satisfy this limited classification; it is not literal full reading.',
    'no_program_body_silent_disposal': view['why_generated_index_and_not_a_manual_semantic_rule_carrier'],
    'source_formal_atomic_interface_task_global_credit': 0,
    'remaining_literal_and_program_scope': 'Exact original five frozen indexes retain all110924 candidate text fields and139269 occurrence references. Except earlier named finite receptions and explicitly emitted selections, candidate text bodies were not fully read here. Native function/CFG/consumer, serialized programs, formal clauses and actual primary reception remain separately OPEN and available.',
    'invalid_r2_preserved': view['original_invalid_index'],
    'business_execution': 'NOT_EXECUTED', 'update_state': 'UPDATE_NOT_STARTED',
    'global_pass': False, 'task_final_accepted': False,
}
write('candidate5-strict-purpose-actual-reception.v1.json', proof)

ledger = read('reading-ledger.json')
old_rows = []
selected = {r['source']['sha256']: r for r in view['files']}
for row in ledger['snapshot_payloads']:
    if row['sha256'] in selected:
        old_rows.append(dict(row))
        row['previous_read_state_before_candidate_purpose_disposition'] = row['read_state']
        row.update(
            read_state='FULL_TYPED_GENERATED_CANDIDATE_INDEX_PURPOSE_ONLY_NOT_LITERAL_TEXT_READING',
            reader='/root/coverage_acceptance_incremental',
            source_or_formal_semantic_credit=False,
            all_candidate_literal_bodies_personally_read=False,
            complete_current_json_fields_read=False,
            actual_read_receipts=receipts,
            lossless_view='candidate5-strict-inventory-purpose-view.json',
            semantic_qualification='All actual operative captured statuses/field purposes received. Exact generated-index literal bodies and occurrence metadata retained inventory-only; NOT literal FULL_READ and NOT native/program/consumer acceptance.',
            exact_unread_scope='Candidate literal bodies not fully read here; original native/serialized source and all actual consumer semantics remain OPEN. Captured U statuses remain UNREAD; S index status absent. Supporting index purpose fully disposed, distinct from body reading.',
            purpose_reception_proof='candidate5-strict-purpose-actual-reception.v1.json',
            purpose_reception_recorded_utc=now)
write('candidate5-prior-reading-states-preserved.json', {'utc': now, 'rows': old_rows})
groups = collections.defaultdict(list)
for row in ledger['snapshot_payloads']:
    groups[row['sha256']].append(row)
pending = [v[0] for v in groups.values() if not any(r['read_state'].startswith(('FULL_', 'SAME_BYTES_LINK')) for r in v)]
assert len(groups) == 289 and not pending
strict_indices = [4, 88, 137, 141, 146, 150, 155, 167, 205, 212, 8, 10, 12, 13, 14]
strict_sha = {ledger['snapshot_payloads'][i]['sha256'] for i in strict_indices}
assert len(strict_sha) == 15
metrics = {
    'recorded_utc': now, 'original_paths': 301, 'unique_sha': 289,
    'original_path_bytes': 118161094,
    'current_field_or_explicit_purpose_qualified_unique_sha': 289,
    'not_yet_qualified_original_unique_sha': 0, 'not_yet_qualified_original_unique_bytes': 0,
    'standalone_strict_or_mixed_purpose_unique_artifacts': 15,
    'standalone_strict_or_mixed_purpose_indices': strict_indices,
    'other_current_field_receipt_qualified_unique_artifacts': 274,
    'other274_are_not_a_literal_full_read_claim': 'Inspect each exact read_state/receipt and in-ledger identity-only qualifiers. Same-byte links are not a second independent reading. Historical74 literal artifact count is not a current total.',
    'literal_all_original_payloads_read': False,
    'literal_candidate_unique_text_full_read_here': False,
    'actual_current_global_source_reading_counts': 'UNVERIFIED_NOT_ZERO_BY_THIS_SUPPORTING_AUDIT',
    'actual_global_atomic_or_interface_denominator': 'NOT_FINAL_FROZEN',
    'source_or_formal_or_full_domain_or_task_or_global_credit_from_this_count': 0,
}
ledger.update(current_semantically_read_unique_sha=289,
              remaining_not_fully_personally_semantically_read_unique_sha=0,
              remaining_not_fully_personally_semantically_read_unique_bytes=0,
              current_metric_qualification='Legacy semantic/full names mean current field OR strict named purpose qualification only. Fifteen standalone strict/mixed-purpose artifacts and274 other qualified artifacts are separate; this is NOT289 literal payload/source/primary full reads.',
              updated_utc=now,
              candidate5_strict_purpose_actual_reception=proof,
              supporting_submission_metrics=metrics)
write('reading-ledger.json', ledger)
write('supporting-submission-metrics.v1.json', metrics)

for name in ['progress.json', 'input-identities.json', 'file-coverage.json', 'coverage-gaps.json',
             'acceptance-register.json', 'atomic-and-interface-denominator.json',
             'execution-records.json', 'next-dispatch.json']:
    doc = read(name)
    doc['candidate5_strict_purpose_actual_reception'] = proof
    doc['supporting_submission_metrics'] = metrics
    doc['updated_utc'] = now
    doc['supporting_submission_status'] = 'DELIVERED_FOR_LIMITED_ROOT_CONTRACT_RECEPTION_NOT_SELF_ACCEPTED'
    doc['supporting_task_final_accepted'] = False
    if name == 'progress.json':
        doc.update(process='SUPPORTING_WORK_DELIVERED_PENDING_INDEPENDENT_ROOT_RECEPTION',
                   deliverable_state='TEN_ARTIFACTS_AND_EXACT_EVIDENCE_READY_FOR_LIMITED_ROOT_RECEPTION',
                   conclusion='BOUNDED_SUPPORTING_AUDIT_SUBMITTED; PRIMARY_AND_GLOBAL_OPEN',
                   personally_current_semantic_full_frozen_artifacts=289,
                   pending_unique_sha=0, pending_unique_bytes=0,
                   current_metric_qualification=ledger['current_metric_qualification'])
    if name == 'coverage-gaps.json':
        doc['conclusion'] = 'SUPPORTING_FIXED_INPUT_PURPOSE_RECEPTION_SUBMITTED; SOURCE_PRIMARY_TASK_GLOBAL_OPEN'
    if name == 'next-dispatch.json':
        doc['auditor_remaining_reception'].update(remaining_unique_sha=0,
                                                   remaining_unique_bytes=0, updated_utc=now,
                                                   qualification='Zero unqualified original index/current-field payloads; NOT zero literal/source/program/atomic/consumer work. See exact candidate purpose and pending late deltas.')
        doc['latest_original289_pending'] = []
    write(name, doc)

print(json.dumps({'recorded_utc': now, 'qualified': 289, 'strict_or_mixed': 15, 'other_current_fields': 274,
                  'original_unqualified': 0, 'literal_full_read': False,
                  'own_R_full': 2, 'own_F_full': 3, 'semantic_or_task_or_global_pass': False}))
