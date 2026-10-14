"""Record correction of two checker assumptions, without rerunning author/reference tools."""
from pathlib import Path
import datetime
import hashlib
import json
import subprocess

ROOT = Path('/workspace/pokemon-essentials-clean-room')
P = 'review/remediation-sixth-20261014-prepare'
OUT = ROOT / (P + '/actual-reviews/group-A/payload-audit')
DB = '/tmp/r6-actual-a-payload-20261014.git'
ACTUAL = '86bbc99b28d93db4ed9d6897daf5f3725ccd1808'
PREP = '469a268b92daed7b4d28d7fd0da75520cbb7228f'
PRIOR = '9d5b4e99b617828690e6529b77a1e555d7c9eb1b'
now = lambda: datetime.datetime.now(datetime.timezone.utc).isoformat()
identity = lambda b: {'bytes': len(b), 'sha256': hashlib.sha256(b).hexdigest(),
                      'git_blob': hashlib.sha1(b'blob ' + str(len(b)).encode() + b'\0' + b).hexdigest()}
commands = [json.loads(x) for x in (OUT / 'commands.jsonl').read_text().splitlines()]
checks = json.loads((OUT / 'checks.json').read_text())
summary = json.loads((OUT / 'summary.json').read_text())
original_failed = [x for x in checks if x['result'] != 'PASS_MECHANICAL']

def capture(argv):
    begin = now()
    result = subprocess.run(argv, cwd=ROOT, capture_output=True)
    n = len(commands) + 1
    stdout = OUT / 'logs' / f'{n:04d}.stdout'
    stderr = OUT / 'logs' / f'{n:04d}.stderr'
    stdout.write_bytes(result.stdout)
    stderr.write_bytes(result.stderr)
    commands.append({'argv': argv, 'cwd': str(ROOT), 'utc_start': begin, 'utc_end': now(), 'exit_code': result.returncode,
                     'stdout_path': str(stdout), 'stderr_path': str(stderr), 'stdout_identity': identity(result.stdout),
                     'stderr_identity': identity(result.stderr), 'reference_behavior_execution': False})
    (OUT / 'commands.jsonl').write_text(''.join(json.dumps(x, ensure_ascii=False) + '\n' for x in commands))
    assert result.returncode == 0, result.stderr
    return result.stdout

def tree_entry(commit, path):
    row = capture(['git', '--git-dir=' + DB, 'ls-tree', '-r', '-z', commit, '--', path]).split(b'\0')[0]
    meta, name = row.split(b'\t')
    mode, kind, oid = meta.decode().split()
    return {'path': name.decode(), 'mode': mode, 'type': kind, 'oid': oid}

def newcheck(name, okay, detail):
    checks.append({'check': name, 'result': 'PASS_MECHANICAL' if okay else 'FAIL_MECHANICAL', 'detail': detail})

old_trace = capture(['git', 'show', PREP + ':audit/source-traceability.md'])
actual_trace = capture(['git', 'show', ACTUAL + ':audit/source-traceability.md'])
prior_trace = capture(['git', 'show', PRIOR + ':audit/source-traceability.md'])
for check in checks:
    if check['check'] == 'frozen_integrated_protected_path:audit/source-traceability.md':
        check['superseded_checker_rule'] = {'initial_check': check['check'], 'initial_result': check['result'], 'initial_detail': check['detail'],
                                            'reason': 'Whole-file equality to prepare was an extra rule outside delegated A contract; existing U04 append must remain.'}
        check['check'] = 'public_existing_layers_preserved_and_group_A_final_not_changed'
        check['result'] = 'PASS_MECHANICAL' if actual_trace.startswith(old_trace) and actual_trace == prior_trace else 'FAIL_MECHANICAL'
        check['detail'] = {'baseline_identity': identity(old_trace), 'prior_actual_identity': identity(prior_trace),
                           'actual_identity': identity(actual_trace), 'old_layer_is_exact_prefix': actual_trace.startswith(old_trace),
                           'existing_U04_append_bytes': len(actual_trace) - len(old_trace), 'new_group_A_or_final_edit': actual_trace != prior_trace,
                           'qualification': 'Existing pending-review U04 addition does not grant acceptance/CLOSED or require A administrative revision.'}
status = capture(['git', 'status', '--porcelain', '--untracked-files=all']).decode().splitlines()
for check in checks:
    if check['check'] == 'current_worktree_writes_only_group_A':
        check['superseded_checker_rule'] = {'initial_result': check['result'], 'initial_detail': check['detail'],
                                            'reason': 'Default Git directory folding hides individual paths; corrected to --untracked-files=all.'}
        check['result'] = 'PASS_MECHANICAL' if all(x.startswith('?? ') and x[3:].startswith(P + '/actual-reviews/group-A/') for x in status) else 'FAIL_MECHANICAL'
        check['detail'] = {'expanded_untracked_paths': status, 'tracked_changes': [x for x in status if not x.startswith('?? ')]}
input_data = json.loads((ROOT / (P + '/integration/U01-U14-final-composite-20261014/actual-review-input.json')).read_bytes())
for batch in [x for x in input_data['batches'] if x['batch'] in ['R6-U01', 'R6-U03', 'R6-U14']]:
    review = batch['independent_review']
    entry = tree_entry(review['review_commit'], review['report_path'])
    newcheck('review_report_path_mode_type_blob_binding:' + batch['batch'], entry['oid'] == review['report_identity']['git_blob'] and
             entry['mode'] == '100644' and entry['type'] == 'blob', entry)
source_commit = next(x['candidate_published_commit'] for x in input_data['batches'] if x['batch'] == 'R6-U01')
source_path = P + '/candidates/R6-U01/evidence/source-payload-identities.json'
source_entry = tree_entry(source_commit, source_path)
source_receipt = json.loads((OUT / 'prior-U01-source-identity-list-readback.json').read_text())
source_identity = source_receipt['attempts'][-1]['full_body_identity']
newcheck('prior_source_identity_list_full_body_tree_binding', source_identity['git_blob'] == source_entry['oid'],
         {'metadata': source_entry, 'full_identity': source_identity})
failures = [x for x in checks if x['result'] != 'PASS_MECHANICAL']
summary.update({'result': 'PASS_MECHANICAL_INTEGRITY' if not failures else 'FAIL_MECHANICAL_INTEGRITY',
                'utc_end': now(), 'mechanical_check_count': len(checks), 'command_receipts': len(commands),
                'failed_checks': failures, 'checker_assumption_corrections': 2})
(OUT / 'checks.json').write_text(json.dumps(checks, ensure_ascii=False, indent=2) + '\n')
(OUT / 'summary.json').write_text(json.dumps(summary, ensure_ascii=False, indent=2) + '\n')
note = {'utc': now(), 'corrected_initial_checker_results': original_failed,
        'corrections': ['Public traceability older U04 appendix retained: exact old layer prefix and exact prior/final bytes verified; no extra A public equality gate.',
                        'Expanded Git status instead of collapsed directory path; actual paths only group-A and no tracked modifications.'],
        'original_audit_start': summary['utc_start'], 'updated_audit_script_identity': identity((OUT / 'audit.py').read_bytes()),
        'initial_execution_script_hash': 'UNVERIFIED_NOT_CAPTURED_BEFORE_REFINEMENT',
        'pre_instrumentation_read_only_commands': 'Tool transcript records status/schema/AGENTS and fixed-object attempts; UTC was not independently captured and is UNVERIFIED.',
        'pre_instrumentation_missing_candidate_tree': {'command': 'git ls-tree -r --name-only bcd194b0e4c293764998b7040b0154af8041bf41 -- candidates/R6-U03',
                                                       'exit_code': 128, 'error': 'fatal: not a tree object; resolved via independent fixed-object remote fetch.', 'UTC': 'UNVERIFIED'},
        'scope': 'All 11 semantic verdicts remain root direct review. No author validator/reference/host executed, no project refs modified, no formal/admin write.'}
(OUT / 'checker-refinement-and-execution-note.json').write_text(json.dumps(note, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({'result': summary['result'], 'checks': len(checks), 'commands': len(commands), 'failed': failures}, ensure_ascii=False))
