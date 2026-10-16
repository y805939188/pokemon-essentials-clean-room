"""Restore immutable Git blobs without importing or executing recovered content."""
from pathlib import Path
import argparse
import datetime
import hashlib
import json
import subprocess

TASK = Path(__file__).resolve().parent

def git(repo, *args):
    return subprocess.check_output(['git', '--git-dir=' + repo, *args])

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--git-dir', required=True)
    args = parser.parse_args()
    readset = json.loads((TASK / 'evidence/contract/receive_external_localization_records.complete.json').read_text())
    commit = readset['target_commit']
    prefix = 'review/global-independent-review/eighth-2026-10-16-fd1df57-c84e/tasks/external_localization_records'
    tree = git(args.git_dir, 'rev-parse', commit + '^{tree}').decode().strip()
    task_tree = git(args.git_dir, 'rev-parse', commit + ':' + prefix).decode().strip()
    assert tree == readset['target_checkout_tree']
    assert task_tree == readset['target_task_tree_observed_from_fixed_commit']
    actual = {}
    for entry in git(args.git_dir, 'ls-tree', '-rz', commit, '--', prefix).split(b'\0'):
        if not entry:
            continue
        attrs, path = entry.split(b'\t', 1)
        mode, kind, blob = attrs.decode().split()
        assert kind == 'blob' and mode == '100644'
        actual[path.decode()] = (mode, blob)
    assert set(actual) == {x['remote_path_at_target_commit'] for x in readset['files']}
    destination = TASK / 'evidence/recovered-target'
    assert not destination.exists()
    destination.mkdir()
    rows = []
    for expected in readset['files']:
        relative = Path(expected['relative_to_target_task'])
        assert not relative.is_absolute() and '..' not in relative.parts
        remote = expected['remote_path_at_target_commit']
        assert remote == prefix + '/' + relative.as_posix()
        mode, blob = actual[remote]
        data = git(args.git_dir, 'cat-file', 'blob', blob)
        sha = hashlib.sha256(data).hexdigest()
        assert (mode, blob, len(data), sha) == (expected['mode'], expected['git_blob'], expected['bytes'], expected['sha256'])
        output = destination / relative
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_bytes(data)
        rows.append({**expected, 'local_path': str(output.relative_to(TASK)), 'actual_mode': mode, 'actual_git_blob': blob, 'actual_bytes': len(data), 'actual_sha256': sha, 'identity_exact': True, 'semantic_credit': 'NONE'})
    receipt = {'schema': 'gr8-independent-fixed-git-recovery/v1', 'utc': datetime.datetime.now(datetime.timezone.utc).isoformat(), 'target_commit': commit, 'checkout_tree': tree, 'task_tree': task_tree, 'isolated_git_dir': args.git_dir, 'ordinary_remote_fetch': True, 'files': rows, 'count': len(rows), 'bytes': sum(x['actual_bytes'] for x in rows), 'collection_exact': True, 'restored_code_executed': False, 'semantic_credit': 'NONE'}
    (TASK / 'evidence/target-recovery.json').write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({k:v for k,v in receipt.items() if k != 'files'}, ensure_ascii=False))

if __name__ == '__main__':
    main()
