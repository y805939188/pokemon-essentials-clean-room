"""Read only the published task subtree from a fresh network clone.

Outputs transport/tool evidence only. Does not award semantic or behavior credit.
The receipt is external to the commit it binds; no recursive self identity.
"""
from pathlib import Path
import argparse
import base64
import datetime
import gzip
import hashlib
import json
import os
import subprocess
import tempfile

TASK = 'review/global-independent-review/eighth-2026-10-16-fd1df57-c84e/tasks/handoff_preparation_cloud'
BRANCH = 'codex/r8-handoff-preparation-20261016'


def run(args, cwd=None):
    p = subprocess.run(args, cwd=cwd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if p.returncode:
        raise RuntimeError(json.dumps({'command': args[:2], 'exit': p.returncode,
                                       'stderr': p.stderr.decode(errors='replace')}))
    return p.stdout


def git(repo, *args):
    return run(['git', '-C', str(repo), *args])


def sha(data):
    return hashlib.sha256(data).hexdigest()


def blob(data):
    return hashlib.sha1(('blob ' + str(len(data)) + '\0').encode() + data).hexdigest()


def identities(repo, commit):
    rows = []
    for entry in git(repo, 'ls-tree', '-rz', commit, '--', TASK).split(b'\0'):
        if not entry:
            continue
        meta, name = entry.split(b'\t', 1)
        mode, typ, object_id = meta.decode().split()
        assert typ == 'blob'
        p = name.decode()
        data = git(repo, 'show', commit + ':' + p)
        assert blob(data) == object_id
        rows.append({'path': p, 'mode': mode, 'blob': object_id,
                     'bytes': len(data), 'sha256': sha(data)})
    return rows


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--commit', required=True)
    ap.add_argument('--output', required=True)
    args = ap.parse_args()
    repo = Path.cwd()
    commit = git(repo, 'rev-parse', args.commit + '^{commit}').decode().strip()
    start = datetime.datetime.now(datetime.timezone.utc).isoformat()
    # Capture expected fixed objects before network retrieval, without modifying them.
    expected = identities(repo, commit)
    expected_tree = git(repo, 'rev-parse', commit + ':' + TASK).decode().strip()
    remote_url = git(repo, 'remote', 'get-url', 'origin').decode().strip()
    isolation = Path(tempfile.mkdtemp(prefix='r8-handoff-network-readback-'))
    clone = isolation / 'repo'
    # The network URL is taken from the existing authorized origin and not printed.
    run(['git', 'clone', '--depth=1', '--filter=blob:none', '--no-checkout',
         '--single-branch', '--branch', BRANCH, remote_url, str(clone)])
    git(clone, 'sparse-checkout', 'init', '--no-cone')
    git(clone, 'sparse-checkout', 'set', '--no-cone', '/' + TASK + '/')
    git(clone, 'checkout', BRANCH)
    actual_commit = git(clone, 'rev-parse', 'HEAD').decode().strip()
    assert actual_commit == commit, (actual_commit, commit)
    alternates = clone / '.git/objects/info/alternates'
    assert not alternates.exists()
    assert not os.environ.get('GIT_ALTERNATE_OBJECT_DIRECTORIES')
    actual_tree = git(clone, 'rev-parse', 'HEAD:' + TASK).decode().strip()
    assert actual_tree == expected_tree
    actual = identities(clone, commit)
    assert actual == expected
    disk_paths = sorted(str(p.relative_to(clone)) for p in (clone / TASK).rglob('*') if p.is_file())
    assert disk_paths == sorted(x['path'] for x in expected)
    for row in expected:
        path = clone / row['path']
        data = path.read_bytes()
        assert len(data) == row['bytes'] and sha(data) == row['sha256'] and blob(data) == row['blob']
        expected_mode = '100755' if path.stat().st_mode & 0o111 else '100644'
        assert expected_mode == row['mode']
    compressed = []
    for row in expected:
        if row['path'].endswith('.gz'):
            data = gzip.decompress((clone / row['path']).read_bytes())
            # Compare complete decompressed bytes, not merely JSON equality.
            local = gzip.decompress(git(repo, 'show', commit + ':' + row['path']))
            assert data == local
            json.loads(data)
            compressed.append({'path': row['path'], 'restored_bytes': len(data),
                               'restored_sha256': sha(data), 'status': 'PASS_TOOL_VALIDATION'})
    bundle = json.loads(gzip.decompress((clone / TASK / 'audit/exact-payload-bytes.json.gz').read_bytes()))
    restored = []
    for row in bundle['payloads']:
        data = base64.b64decode(row['base64'], validate=True)
        assert len(data) == row['bytes'] and sha(data) == row['sha256'] and blob(data) == row['blob']
        restored.append({k: row[k] for k in ['phase', 'commit', 'tree', 'path', 'mode', 'blob', 'bytes', 'sha256']})
    assert len(restored) == 72
    receipt = {
        'schema': 'r8-task-isolated-network-readback/v1',
        'status': 'PASS_TRANSPORT_TOOL_ONLY', 'start_utc': start,
        'end_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'branch': BRANCH, 'commit': commit,
        'workspace_tree': git(clone, 'rev-parse', 'HEAD^{tree}').decode().strip(),
        'task_path': TASK, 'task_tree': actual_tree,
        'fresh_network_clone': str(clone), 'local_object_alternates': False,
        'file_count': len(actual), 'files': actual,
        'full_remote_path_mode_blob_bytes_sha256_set_tree': 'PASS',
        'compressed_restore': compressed, 'raw_payloads_restored': restored,
        'semantic_credit': 0, 'behavior_credit': 0, 'update_started': False,
        'root_core': 'PENDING_ROOT_CORE_FREEZE',
        'self_identity_rule': 'This receipt binds an earlier fixed commit; its own later publication is bound externally.'
    }
    Path(args.output).write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({k: receipt[k] for k in ['status', 'commit', 'workspace_tree', 'task_tree', 'file_count']}))


if __name__ == '__main__':
    main()
