"""Fresh origin object store, complete-byte comparison; no behavior execution."""
import argparse
import datetime
import hashlib
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[6]
PREFIX = 'review/remediation-fourth-20261012-prepare/batches/R4-U01/review/'
BASE = 'c1e5c8a780426aef1611a5b139375de15e6cd468'
PACK = '08a57fb55118914a74ac1ffaf617647c01df8938'
CAND = 'db879d9034acf2fa3a3721ad3b94614827922ec4'
BRANCH = 'review/r4-u01-independent-20261012-codex'
REMOTE = 'https://github.com/y805939188/pokemon-essentials-clean-room.git'


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
assert not fresh.exists(), 'Fresh directory must not already exist'
run('git', 'init', '--bare', str(fresh))


def remote(*git_args):
    return run('git', '--git-dir=' + str(fresh), *git_args)


remote('fetch', '--no-tags', REMOTE, 'refs/heads/' + BRANCH)
head = remote('rev-parse', 'FETCH_HEAD').decode().strip()
assert head == args.commit, (head, args.commit)
assert not (fresh / 'objects/info/alternates').exists()
local_tree = local('rev-parse', head + '^{tree}').decode().strip()
assert local_tree == remote('rev-parse', head + '^{tree}').decode().strip()
report_paths = local('diff', '--name-only', BASE, head).decode().splitlines()
assert report_paths and all(p.startswith(PREFIX) for p in report_paths)
candidate_paths = local('diff', '--name-only', PACK, CAND).decode().splitlines()
author_paths = local('diff', '--name-only', CAND, BASE).decode().splitlines()
records = []
for c, paths, role in [(head, report_paths, 'independent_report'),
                        (CAND, candidate_paths, 'frozen_candidate'),
                        (BASE, author_paths, 'author_evidence_successor')]:
    for p in paths:
        own = local('show', c + ':' + p)
        fetched = remote('show', c + ':' + p)
        assert own == fetched, (c, p)
        blob = local('rev-parse', c + ':' + p).decode().strip()
        assert blob == remote('rev-parse', c + ':' + p).decode().strip()
        records.append({'role': role, 'commit': c, 'path': p, 'bytes': len(fetched),
                        'sha256': hashlib.sha256(fetched).hexdigest(), 'git_blob': blob,
                        'complete_remote_bytes_read': True, 'byte_for_byte_local_match': True})
advertisement = local('ls-remote', 'origin', 'refs/heads/main',
                      'refs/tags/delivery/third-round-clean-20261012').decode()
assert all(line.startswith('1f36475d22120a0d1175967d5b17d71fe8311d88\t')
           for line in advertisement.splitlines()) and len(advertisement.splitlines()) == 2
result = {
    'status': 'PASS_FULL_REMOTE_BYTES', 'evidence_level': 'TOOL_VALIDATION',
    'completed_at': datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'commit': head, 'tree': local_tree, 'branch': BRANCH, 'fresh_object_store': str(fresh),
    'no_local_objects_or_alternates_copied': True,
    'report_changed_paths_only_own_review_directory': True,
    'report_file_count': len(report_paths), 'candidate_files': len(candidate_paths),
    'author_successor_files': len(author_paths), 'files': records,
    'total_complete_bytes_compared': sum(x['bytes'] for x in records),
    'main_and_delivery_tag_advertisement': advertisement,
    'new_behavior_execution': 'NOT_EXECUTED_THIS_UPDATE',
    'scope': 'Remote byte receipt only; semantic verdict binds candidate db879d9, never ACTUAL_PASS or acceptance/closure.'
}
output = Path(args.output).resolve()
assert output == ROOT.joinpath(PREFIX, 'candidate-v1/publication-readback.json') or str(output).startswith('/tmp/')
output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({k: result[k] for k in ['status', 'commit', 'tree', 'report_file_count',
                                       'candidate_files', 'author_successor_files', 'total_complete_bytes_compared']}))
