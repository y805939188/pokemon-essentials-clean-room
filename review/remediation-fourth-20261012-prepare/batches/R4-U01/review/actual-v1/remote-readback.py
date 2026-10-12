"""Fresh remote complete-byte verification for report and fixed actual input."""
import argparse
import datetime
import hashlib
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[6]
OUT = Path(__file__).resolve().parent
BASE = '7f41a945df38097f5f5b5c8d4ee3f2b5d5e4aae2'
ACTUAL = '1ec8655fc3186ad88e3fb1ff1700540eb33d41ff'
PUB = 'afb5f5021964b7d7dbd8bd615948741919670f99'
PREFIX = 'review/remediation-fourth-20261012-prepare/'
REPORT_PREFIX = PREFIX + 'batches/R4-U01/review/actual-v1/'
REG = PREFIX + 'registration/R4-U01/'
BRANCH = 'review/r4-u01-independent-20261012-codex'
URL = 'https://github.com/y805939188/pokemon-essentials-clean-room.git'


def run(*args):
    return subprocess.check_output(list(args))


def local(*args):
    return run('git', '-C', str(ROOT), *args)


parser = argparse.ArgumentParser()
parser.add_argument('--commit', required=True)
parser.add_argument('--fresh-dir', required=True)
parser.add_argument('--output', required=True)
args = parser.parse_args()
fresh = Path(args.fresh_dir)
assert not fresh.exists(), 'Fresh object store required'
run('git', 'init', '--bare', str(fresh))


def remote(*git_args):
    return run('git', '--git-dir=' + str(fresh), *git_args)


remote('fetch', '--no-tags', URL, 'refs/heads/' + BRANCH + ':refs/heads/report-readback', ACTUAL, PUB)
head = remote('rev-parse', 'refs/heads/report-readback').decode().strip()
assert head == args.commit
assert not (fresh / 'objects/info/alternates').exists()
tree = local('rev-parse', head + '^{tree}').decode().strip()
assert tree == remote('rev-parse', head + '^{tree}').decode().strip()
assert remote('rev-parse', ACTUAL + '^{tree}').decode().strip() == '7d5ab5e59473ca2c3f86a61b281aa62712516d5e'
assert remote('rev-parse', PUB + '^{tree}').decode().strip() == 'cd5024597091353a62c332371fb8bf5cd7fd8488'
report_paths = local('diff', '--name-only', BASE, head).decode().splitlines()
assert report_paths and all(x.startswith(REPORT_PREFIX) for x in report_paths)
formal_paths = local('ls-tree', '-r', '--name-only', ACTUAL, 'deliverables/final-specification-set').decode().splitlines()
assert len(formal_paths) == 131
integration = json.loads(local('show', ACTUAL + ':' + REG + 'integration-check.json'))
copied = [x['path'] for x in integration['copied_evidence_exact_bytes']]
task_paths = local('ls-tree', '-r', '--name-only', PUB, REG).decode().splitlines()
assert len(copied) == 18 and len(task_paths) == 6
records = []
for commit, paths, role in [(head, report_paths, 'actual_independent_report'),
                             (ACTUAL, formal_paths, 'fixed_actual_formal'),
                             (ACTUAL, copied, 'preserved_candidate_author_evidence'),
                             (PUB, task_paths, 'fixed_actual_task_package')]:
    for path in paths:
        own = local('show', commit + ':' + path)
        fetched = remote('show', commit + ':' + path)
        assert own == fetched, (commit, path)
        blob = local('rev-parse', commit + ':' + path).decode().strip()
        assert blob == remote('rev-parse', commit + ':' + path).decode().strip()
        records.append({'role': role, 'commit': commit, 'path': path, 'bytes': len(fetched),
                        'sha256': hashlib.sha256(fetched).hexdigest(), 'git_blob': blob,
                        'complete_remote_bytes_read': True, 'byte_for_byte_local_match': True})
advertisement = local('ls-remote', 'origin', 'refs/heads/main', 'refs/tags/delivery/third-round-clean-20261012').decode()
assert len(advertisement.splitlines()) == 2
assert all(x.startswith('1f36475d22120a0d1175967d5b17d71fe8311d88\t') for x in advertisement.splitlines())
result = {
    'status': 'PASS_FULL_REMOTE_BYTES', 'evidence_level': 'TOOL_VALIDATION',
    'completed_at': datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'report_commit': head, 'report_tree': tree, 'branch': BRANCH,
    'actual_commit': ACTUAL, 'actual_tree': '7d5ab5e59473ca2c3f86a61b281aa62712516d5e',
    'task_publication_commit': PUB, 'task_publication_tree': 'cd5024597091353a62c332371fb8bf5cd7fd8488',
    'fresh_object_store': str(fresh), 'no_copied_local_objects_or_alternates': True,
    'report_changes_only_own_actual_review_directory': True,
    'report_file_count': len(report_paths), 'actual_formal_file_count': len(formal_paths),
    'preserved_evidence_files': len(copied), 'actual_task_files': len(task_paths),
    'files_count': len(records), 'total_complete_bytes_compared': sum(x['bytes'] for x in records),
    'files': records, 'main_and_delivery_tag_advertisement': advertisement,
    'WP59_handshake': 'PENDING_U02_ACTUAL_NOT_CLOSED_NOT_PRE_SIGNED',
    'historical_fourth_execution_records': {'M01': 1, 'M02': 2, 'M12': 1, 'total': 4},
    'new_behavior_execution': 'NOT_EXECUTED_THIS_UPDATE',
    'acceptance_or_closure_registered': False,
    'receipt_is_byte_validation_not_new_behavior_execution': True
}
target = Path(args.output).resolve()
assert target == OUT / 'publication-readback.json' or str(target).startswith('/tmp/')
target.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({k: result[k] for k in ('status', 'report_commit', 'report_tree', 'report_file_count',
                                       'files_count', 'total_complete_bytes_compared')}))
