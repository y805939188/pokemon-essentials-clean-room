"""Build candidate identities and per-record audit metadata, not behavior models."""
import datetime
import difflib
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess


REPO = Path(__file__).resolve().parents[4]
OUT = Path(__file__).resolve().parent
CONTEXT = Path('/workspace/r7-context/R7-U02-author')
BASE = 'e646432c644dec04d306842cc5a559a29c718fbc'
DISPATCH = '6ec1d09e9c470954964d72761c83a760ef4f0364'


def identity(data):
    return {'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest(),
            'git_blob_content_id': hashlib.sha1(f'blob {len(data)}\0'.encode() + data).hexdigest()}


def write(name, value):
    (OUT / name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')


def git(*args):
    return subprocess.check_output(['git', *args], cwd=REPO)


def main():
    contract_path = CONTEXT / 'dispatch/delegation/contracts/R7-U02.json'
    contract = json.loads(contract_path.read_bytes())
    payload = json.loads((CONTEXT / 'evidence/tasks/R7-C13/inputs/tasks/R7-P02/normalized-record-candidates.json').read_bytes())
    expected_formal_tree = 'ebbe29f2bc88cd17de7072bf440c6fa8c8c7089c'
    assert git('rev-parse', BASE + ':deliverables/final-specification-set').decode().strip() == expected_formal_tree
    assert git('branch', '--show-current').decode().strip() == 'codex/r7-u02-author-20261015-wave1'
    copies = []
    diffs = []
    for row in contract['paths']:
        old = git('show', BASE + ':' + row['path'])
        new = (REPO / row['candidate_path']).read_bytes()
        assert old == (CONTEXT / 'inputs/project' / row['path']).read_bytes()
        changes = []
        for tag, a, b, c, d in difflib.SequenceMatcher(None, old.splitlines(True), new.splitlines(True), autojunk=False).get_opcodes():
            if tag != 'equal':
                changes.append({'kind': tag, 'base_lines_half_open_0_based': [a, b],
                                'candidate_lines_half_open_0_based': [c, d]})
        copies.append({'path': row['candidate_path'], 'base_path': row['path'], 'base_commit': BASE,
                       'base': identity(old), 'candidate': identity(new), 'hunks': changes,
                       'record_scopes': row['scopes']})
        diffs.extend(difflib.unified_diff(old.decode().splitlines(True), new.decode().splitlines(True),
                                         fromfile='B/' + row['path'], tofile=row['candidate_path'], n=0))
    (OUT / 'clauses.patch').write_text(''.join(diffs))
    write('mirror-identities.json', {'qualification': 'Four full B-byte mirrors with bounded clause contributions.', 'mirrors': copies})
    recovery = sorted(CONTEXT.glob('recovery-receipt-*.json'))
    assert len(recovery) == 1
    shutil.copyfile(recovery[0], OUT / 'context-recovery.json')
    limits = json.loads((CONTEXT / 'evidence/tasks/R7-C17/limits-and-alias-reception.json').read_bytes())
    qualifications = {
        'role': 'R7-U02 author only', 'source_thread_id': '01a13f49-a154-7054-9b04-ce31f924d01c',
        'actual_context_thread_id': os.environ.get('CODEX_THREAD_ID', 'UNAVAILABLE'),
        'actual_task_id': os.environ.get('CODEX_TASK_ID', 'UNAVAILABLE'),
        'context_id_extra': os.environ.get('CODEX_CONTEXT_ID', 'UNAVAILABLE'),
        'metadata_process_pid': os.getpid(), 'utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'requested_configuration': {'model': 'gpt-6.1-sol', 'effort': 'xhigh',
            'service_tier': 'default', 'speed': 'normal', 'Fast': 'FORBIDDEN'},
        'effective_configuration': {key: 'UNVERIFIED' for key in ['model', 'effort', 'service_tier', 'speed']},
        'effective_configuration_reason': 'No authoritative effective-configuration response available; requests/self-report/exit0 are not certification.',
        'new_tasks_or_reviewers_created': 0, 'independent_reviewer': 'NOT_STARTED_BY_THIS_AUTHOR',
        'source_reference_native_host_Demo_media_real_save_replay_executions': 0,
        'independent_complete_model_executions': 0,
        'state': 'CANDIDATE_READY_NOT_REVIEWED',
        'new_reference_observation': 'NOT_EXECUTED',
        'global_denominator': {'items': 27, 'batches': 13}, 'old_56_92_closure_boundary': 'UNCHANGED',
        'retained_limits': [x['id'] for x in limits['limits']],
        'skills_lookup': {'paths': ['/workspace/.agents/skills', '/workspace/pokemon-essentials-clean-room/.agents/skills',
                                   '/home/agent/.agents/skills', '/run/codex-environment/codex-home/.agents/skills'],
                          'result': 'NOT_PRESENT; no relevant .agents/skills in fixed B or dispatch tree',
                          'unrelated_dependency_skill_used': False},
        'early_log_qualification': 'Initial reconnaissance/read commands are present in platform tool I/O, but did not independently save local start/end UTC, PID and split stdout/stderr. Do not backfill these metadata. Recovery has its own real per-file HTTP UTC receipt. run_audit.py begins fresh separated public audit logs; it does not repair initial provenance gaps.',
        'publication_qualification': 'Source excerpts/machine code and private model stream are not copied into public evidence. Only bounded source identities, locators, static observations and public audit I/O are included. Final commit/tree/push/readback receipt is bound outside its own immutable commit to avoid recursive self-hashing.'
    }
    write('context.json', qualifications)
    catalog_rel = 'deliverables/final-specification-set/test-catalog/user-interface-wp17-63-65-66-67-68-69-70-71.md'
    catalog = (REPO / 'candidates/R7-U02' / catalog_rel).read_text()
    vectors = []
    for line in catalog.splitlines():
        if line.startswith('| R7-U02-'):
            cells = [x.strip() for x in line.strip('|').split('|')]
            vectors.append({'id': cells[0], 'catalog_cells': cells[1:], 'stage': 'DERIVED_VECTOR',
                            'execution': 'NOT_EXECUTED', 'author_static_disposition': 'DOCUMENTED_FROM_BOUNDED_SOURCE',
                            'non_author_semantic_review': 'PENDING', 'host_result': 'NOT_OBSERVED'})
    assert len(vectors) == 51 and len({v['id'] for v in vectors}) == 51
    source_reads = []
    entries = []
    families = [('SS',), ('IN',), ('DB', 'BT', 'AX')]
    original_mapping = [
        {'C04-SS-A': ['SS01', 'SS02'], 'C04-SS-B': ['SS04', 'SS05'], 'C04-SS-C': ['SS06', 'SS07'],
         'C04-SS-D': ['SS03', 'SS09'], 'C04-SS-E': ['SS08', 'SS10', 'SS12'], 'partial_commit_audio_failure': ['SS11']},
        {'C04-IN-A': ['IN01', 'IN02'], 'C04-IN-B': ['IN03'], 'C04-IN-C': ['IN05', 'IN06', 'IN07', 'IN08'],
         'C04-IN-D': ['IN09'], 'C04-IN-E': ['IN13'], 'local_party_summary': ['IN04'],
         'nil_missing_commands': ['IN10'], 'busy_four_states_and_business_prefix': ['IN11'], 'exception_prefix': ['IN12']},
        {'C08_DB0087': ['DB01'], 'C08_all_15_plus_6_names': ['BT01–15', 'AX01–06'],
         'C08_allocation_failure_separate': ['DB02'], 'C08_no_interactive_cancel': ['DB03'],
         'C08_bridge_dependency': ['DB04'], 'C08_counts_not_semantic_acceptance': ['DB05']}
    ]
    for index, item in enumerate(contract['original_full_contracts']):
        groups = item['complete_seven_groups']
        record = payload['records'][[5, 8, 28][index]]
        assert record['id'] == item['record_id']
        read_set = groups['六_依赖接收_精确读写集']['读取义务']['items']
        for read in read_set:
            source_reads.append({'record_id': item['record_id'], **read,
                'actual_qualification': 'Source exact bounded ranges read; project full bytes ingested/identity checked and relevant clauses read. Whole-file byte scope does not certify every unrelated historical row semantically.'})
        entry = {'record_id': item['record_id'], 'status': 'CANDIDATE_READY_NOT_REVIEWED',
                 'classification': item['classification'], 'severity': item['severity'],
                 'full_contract': {'fixed_commit': 'f622356f3beb9e84ea8cff9db07c7fb382565d3f',
                     'path': 'review/remediation-seventh-20261015-prepare/delegation/contracts/R7-U02.json',
                     'record_index': index, 'all_seven_groups_read': True, 'file_identity': identity(contract_path.read_bytes())},
                 'minimum_revision': groups['三_最小修订_正确保留'],
                 'normal_cancel_failure_partial': {k: v for k, v in groups['二_证据_前提_反例_四路径'].items()
                                                     if k != '原始证据'},
                 'required_read_set': read_set,
                 'actual_write_set': [r for r in copies if any(s['record_id'] == item['record_id'] for s in r['record_scopes'])],
                 'conditional_write_set': [],
                 'received_counterproof': record['groups']['verification']['nonauthor_counterproof'],
                 'original_acceptance': record['groups']['verification']['acceptance_items'],
                 'original_to_candidate_vector_mapping': original_mapping[index],
                 'candidate_vectors': [v for v in vectors if any(v['id'].startswith('R7-U02-' + f) for f in families[index])],
                 'stages': {'SOURCE_STATIC': 'BOUNDED_AUTHOR_READ', 'DERIVED_VECTOR': 'DOCUMENTED_NOT_EXECUTED',
                            'TOOL_VALIDATION': ['33 input identities', '18 raw-member/pointer/canonical bindings', '15+6 name pointers', 'candidate scope and preservation checks'],
                            'REFERENCE_OBSERVATION': 'NOT_EXECUTED', 'independent_complete_model': 'NOT_EXECUTED',
                            'game_host_Demo_native_media_real_save_replay': 'NOT_EXECUTED'},
                 'dependencies_from_frozen_record': record['groups']['dependencies'],
                 'unfulfilled_reception_dependencies': ['R7-I exact candidate identity and conflict-group reception',
                     'Different actual context ultra candidate review', 'R7-I serial clause integration',
                     'New R7-IR review of actual integrated bytes', 'Exact historical and direct/transitive consumer regression reception'],
                 'gates': {key: 'OPEN_NOT_REACHED' for key in ['candidate_PASS', 'integrated_PASS', 'ACCEPTED', 'CLOSED']}}
        if index == 1:
            entry['historical_qualification'] = 'Original canonical_candidate null retained in immutable payload; no fabricated historic ID. GR6-O-002/R6-EV01–06 correct graphic-freeze branch stays unchanged. C04/H12/H13 identity/old reception is not a fresh author certification.'
        if index == 2:
            entry['unfulfilled_reception_dependencies'] += ['CC04 registration/host-query bridge NOT_READ',
                'Actual device/backend validation NOT_EXECUTED', 'Full 1923 record-field semantics/76 fields in 48 records/registration priority NOT_SIGNED']
            entry['non_adopted_original_vectors'] = {'D06-TV02–05': 'Wider platform/empty-field/axis overlap/registration-priority facets not adopted by the narrowed C08 contract; not executed or newly asserted.',
                'D06-TV06': 'Logical consumers remain under their original scopes, no hardware bridge inferred or old approval reissued.'}
        entries.append(entry)
    write('source-read-ledger.json', {'read_set': source_reads,
        'additional_read_scopes': ['R:011_Messages.rb L650–686 for generic normal post-loop refresh',
            'R:Game.exe name-string byte ranges [11551187,11551195), [11552166,11552264), [11552416,11552461)',
            'B:WP17 full 302 lines', 'B:UI catalog MG01–28, B04-M01–18, U05 text controls, U06-M10-001-A–E, R6-U12-TS01–05; headings/conflict locator over full bytes',
            'B:audit T-WP17-01, field conventions, current R6 sync header/tail; append-only preservation of full B',
            'B:feature-matrix F05-05/F05-06, maintenance rules, current R6 sync; append-only preservation of full B',
            'Frozen C04 records/2 and /5; C08 challenges/3 full; C17 all L01–L14; D06 late reception records/2; normalized records/5,/8,/28 verification/dependency/stage fields'],
        'remaining_semantic_scope': 'No exhaustive fresh reading of all unrelated audit/matrix/catalog historical prose. No source outside named ranges or CC04/full native bridge claimed.'})
    write('per-id.json', {'schema': 'r7.u02.author-per-id.v1', 'base_commit': BASE,
        'dispatch_commit': DISPATCH, 'context': qualifications, 'records': entries,
        'candidate_vector_rows': len(vectors), 'all_candidate_vectors_execution': 'NOT_EXECUTED'})
    print(json.dumps({'mirrors': len(copies), 'vector_rows': len(vectors), 'records': len(entries),
                      'state': 'CANDIDATE_READY_NOT_REVIEWED', 'formal_tree': expected_formal_tree}))


if __name__ == '__main__':
    main()
