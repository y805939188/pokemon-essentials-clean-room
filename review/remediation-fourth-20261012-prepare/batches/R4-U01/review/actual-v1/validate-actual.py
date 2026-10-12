"""One bounded actual integration/object check; no reference/model execution."""
import datetime
import hashlib
import json
import os
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[6]
OUT = Path(__file__).resolve().parent
PACK = '08a57fb55118914a74ac1ffaf617647c01df8938'
BASE = '1f36475d22120a0d1175967d5b17d71fe8311d88'
CAND = 'db879d9034acf2fa3a3721ad3b94614827922ec4'
AUTHOR = 'c1e5c8a780426aef1611a5b139375de15e6cd468'
CAND_REPORT = '7f41a945df38097f5f5b5c8d4ee3f2b5d5e4aae2'
ACTUAL = '1ec8655fc3186ad88e3fb1ff1700540eb33d41ff'
PUB = 'afb5f5021964b7d7dbd8bd615948741919670f99'
PREFIX = 'review/remediation-fourth-20261012-prepare/'
REG = PREFIX + 'registration/R4-U01/'
CAND_REVIEW = PREFIX + 'batches/R4-U01/review/candidate-v1/'
HISTORY = 'review/global-independent-review/fourth-2026-10-12-1f36475-c92e/'


def git(*args):
    return subprocess.check_output(['git', '-C', str(ROOT), *args])


def read(commit, path):
    return git('show', commit + ':' + path)


def decoded(commit, path):
    return json.loads(read(commit, path))


def identity(commit, path):
    data = read(commit, path)
    return {'commit': commit, 'path': path, 'bytes': len(data),
            'sha256': hashlib.sha256(data).hexdigest(),
            'git_blob': git('rev-parse', commit + ':' + path).decode().strip()}


def verify(item, commit):
    actual = identity(commit, item['path'])
    assert all(actual[k] == item[k] for k in ('bytes', 'sha256', 'git_blob')), item['path']
    return actual


handoff = decoded(PUB, REG + 'actual-review-handoff.json')
integration = decoded(ACTUAL, REG + 'integration-check.json')
dispositions = decoded(ACTUAL, REG + 'shared-proposal-dispositions.json')
prior_findings = decoded(CAND_REPORT, CAND_REVIEW + 'findings.json')
prior_identity = decoded(CAND_REPORT, CAND_REVIEW + 'identity.json')
contract = decoded(PACK, PREFIX + 'tasks/R4-U01/batch-contract.json')
formal = contract['allowed_formal_write_paths']
assert os.environ.get('CODEX_THREAD_ID') == handoff['same_independent_reviewer_thread_id']
assert prior_identity['reviewer']['thread_id'] == handoff['same_independent_reviewer_thread_id']
assert prior_findings['verdict'] == 'CANDIDATE_PASS_SCOPED'
assert handoff['actual_commit'] == ACTUAL and handoff['candidate_commit'] == CAND
assert handoff['candidate_report_commit'] == CAND_REPORT
assert handoff['finding_ids'] == contract['finding_ids']
assert handoff['formal_read_paths'] == formal and handoff['formal_write_paths'] == []
trees = {}
for commit, expected in [(ACTUAL, '7d5ab5e59473ca2c3f86a61b281aa62712516d5e'),
                         (PUB, 'cd5024597091353a62c332371fb8bf5cd7fd8488'),
                         (CAND, 'f47c43195a60b8edb2922f40d38582874a675cc5'),
                         (CAND_REPORT, '2b403913a92ebb9245d4eef2597e9ee520b97086')]:
    trees[commit] = git('rev-parse', commit + '^{tree}').decode().strip()
    assert trees[commit] == expected
parent = git('rev-parse', ACTUAL + '^').decode().strip()
assert parent == integration['integration_parent'] == 'cec42093a677e868340d58b151c11ab7152db774'

formal_paths = git('ls-tree', '-r', '--name-only', ACTUAL, 'deliverables/final-specification-set').decode().splitlines()
assert len(formal_paths) == 131
assert set(formal_paths) == set(git('ls-tree', '-r', '--name-only', BASE, 'deliverables/final-specification-set').decode().splitlines())
assert set(formal_paths) == {x['path'] for x in handoff['formal_files_131']}
assert set(formal_paths) == {x['path'] for x in integration['formal_file_identities']}
integration_by_path = {x['path']: x for x in integration['formal_file_identities']}
file_records = []
for item in handoff['formal_files_131']:
    path = item['path']
    observed = verify(item, ACTUAL)
    verify(integration_by_path[path], ACTUAL)
    compare_commit = CAND if path in formal else BASE
    assert read(ACTUAL, path) == read(compare_commit, path)
    assert read(PUB, path) == read(ACTUAL, path)
    observed.update({'full_bytes_equal_to': compare_commit,
                     'qualification': 'exact_candidate' if path in formal else 'unchanged_B'})
    file_records.append(observed)
assert git('diff', '--binary', parent, ACTUAL, '--', *formal) == git('diff', '--binary', PACK, CAND, '--', *formal)
git('diff', '--check', parent, ACTUAL, '--', *formal)

evidence_records = []
assert len(integration['copied_evidence_exact_bytes']) == 18
for item in integration['copied_evidence_exact_bytes']:
    observed = verify(item, ACTUAL)
    assert item['origin_commit'] in (AUTHOR, CAND_REPORT)
    assert read(ACTUAL, item['path']) == read(item['origin_commit'], item['path'])
    observed['origin_commit'] = item['origin_commit']
    evidence_records.append(observed)
actual_delta = git('diff', '--name-only', parent, ACTUAL).decode().splitlines()
allowed = set(formal) | {x['path'] for x in evidence_records} | {
    REG + 'integration-check.json', REG + 'shared-proposal-dispositions.json',
    PREFIX + 'registration/status-ledger.json'}
assert set(actual_delta) == allowed
publication_delta = git('diff', '--name-only', ACTUAL, PUB).decode().splitlines()
assert set(publication_delta) == {REG + 'README.md', REG + 'actual-review-handoff.json',
                                   REG + 'actual-review-task.md', REG + 'publication-readback.json',
                                   PREFIX + 'registration/status-ledger.json'}

frozen_paths = git('ls-tree', '-r', '--name-only', PACK, PREFIX + 'tasks').decode().splitlines()
frozen_paths += [PREFIX + x for x in ('README.md', 'dispatch-plan.json', 'input-verification.json',
                                    'resource-scope.json', 'task-file-identities.json')]
assert all(read(PACK, p) == read(ACTUAL, p) == read(PUB, p) for p in frozen_paths)
protected = ['audit/source-traceability.md', 'review/global-independent-review',
             'review/remediation-third-20261012-prepare', 'CURRENT-DELIVERY.md', 'delivery']
assert git('diff', '--name-only', BASE, ACTUAL, '--', *protected) == b''
assert git('diff', '--name-only', BASE, parent, '--', 'deliverables/final-specification-set') == b''

consumers = []
for item in handoff['required_current_shared_consumers']:
    observed = verify(item, ACTUAL)
    assert read(ACTUAL, item['path']) == read(BASE, item['path'])
    observed['ranges'] = item['ranges']
    consumers.append(observed)
assert len(consumers) == 7
assert len(dispositions['dispositions']) == 2
assert dispositions['dispositions'][0]['action'] == 'NO_SHARED_FILE_CHANGE_REQUIRED'
assert dispositions['dispositions'][1]['action'] == 'DEFER_BOUNDED_HANDSHAKE_TO_U02_ACTUAL'
assert not dispositions['acceptance_registered'] and dispositions['formal_paths_added'] == []
ledger = decoded(PUB, PREFIX + 'registration/status-ledger.json')
assert ledger['accepted_scoped_GR4'] == ledger['effective_CLOSED_GR4'] == 0
for record in ledger['records']:
    if record['batch'] == 'R4-U01':
        assert record['state'] == 'ACTUAL_FROZEN' and record['actual']['commit'] == ACTUAL
        assert record['actual']['review_verdict'] is None and record['acceptance'] is None
assert 'Do not integrate U02 before U01 actual scoped acceptance' in ledger['actual_integration_schedule']['gate']

execution = decoded('130452d902530140331c21064a3188b7887f72ae', HISTORY + 'execution-evidence.json')
history_modules = [x['origin_module'] for x in execution['reference_probe_runs']]
assert history_modules == ['M01', 'M02', 'M02', 'M12']
assert execution['counts_by_record_not_testcase']['EXECUTED_REFERENCE'] == 4
result = {
    'batch': 'R4-U01', 'status': 'PASS_BOUNDED_ACTUAL_TOOL_VALIDATION',
    'evidence_level': 'TOOL_VALIDATION', 'completed_at': datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'actual_commit': ACTUAL, 'actual_tree': trees[ACTUAL], 'task_publication_commit': PUB,
    'task_publication_tree': trees[PUB], 'integration_parent': parent,
    'candidate_commit': CAND, 'candidate_report_commit': CAND_REPORT,
    'formal_files': file_records, 'formal_files_exact_candidate': 4, 'formal_files_exact_B': 127,
    'formal_integration_diff_exact_candidate_diff': True,
    'actual_changed_paths': actual_delta, 'task_publication_changed_paths': publication_delta,
    'copied_evidence_exact_bytes': evidence_records,
    'frozen_task_and_input_paths_unchanged': frozen_paths,
    'old_reports_original_delivery_and_real_audit_unchanged': True,
    'current_shared_consumer_identities': consumers,
    'public_proposals': dispositions,
    'WP59_handshake': 'PENDING_U02_ACTUAL_NOT_CLOSED_NOT_PRE_SIGNED',
    'registration_read_only': {'accepted_scoped_GR4': 0, 'effective_CLOSED_GR4': 0,
                               'U02_gate': ledger['actual_integration_schedule']['gate']},
    'historical_fourth_reference_records': {'M01': 1, 'M02': 2, 'M12': 1, 'total': 4},
    'candidate_report_erratum': 'M03 in candidate execution paragraph was a reviewer attribution typo; fourth record is M12. Frozen candidate evidence retained byte-for-byte.',
    'new_reference_model_host_demo_execution': 0,
    'new_behavior_execution': 'NOT_EXECUTED_THIS_UPDATE',
    'semantic_verdict_is_separate_from_tool_checks': True,
    'limits': 'No rerun of candidate administration/source behavior, no whole131 semantic review, no global/history recertification, no acceptance/closure registration.'
}
(OUT / 'validation-result.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({k: result[k] for k in ('status', 'actual_commit', 'actual_tree', 'formal_files_exact_candidate',
                                       'formal_files_exact_B', 'formal_integration_diff_exact_candidate_diff',
                                       'WP59_handshake')}))
