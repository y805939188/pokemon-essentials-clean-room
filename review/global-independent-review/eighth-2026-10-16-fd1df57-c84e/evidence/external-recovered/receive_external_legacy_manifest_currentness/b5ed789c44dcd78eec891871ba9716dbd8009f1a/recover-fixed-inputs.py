"""Recover inert fixed blobs into an absent directory; never execute restored code."""
from pathlib import Path
import subprocess, json, hashlib, datetime

TASK = Path(__file__).resolve().parent
ROOT = TASK.parents[1]
READSET = ROOT / 'delegation/readsets/receive_external_legacy_manifest_currentness.complete.json'
BARE = '/tmp/r8-receive-legacy-input.git'
DEST = TASK / 'inputs/target-93d7df7f'

def git(*args):
    return subprocess.check_output(['git', '--git-dir=' + BARE, *args])

def main():
    readset = json.loads(READSET.read_text())
    commit = readset['target_commit']
    assert not DEST.exists() and not any(p.is_symlink() for p in DEST.parents)
    assert git('rev-parse', commit + '^{tree}').decode().strip() == readset['target_checkout_tree']
    prefix = readset['files'][0]['remote_path_at_target_commit'].rsplit('/', 1)[0]
    tree = git('rev-parse', commit + ':' + prefix).decode().strip()
    assert tree == readset['target_task_tree_observed_from_fixed_commit']
    entries = {}
    for entry in git('ls-tree', '-rz', commit, prefix).split(b'\0'):
        if entry:
            meta, path = entry.split(b'\t')
            mode, kind, blob = meta.decode().split()
            assert kind == 'blob' and mode == '100644'
            entries[path.decode()] = (mode, blob)
    assert set(entries) == {r['remote_path_at_target_commit'] for r in readset['files']}
    DEST.mkdir(parents=True)
    rows = []
    for row in readset['files']:
        rel = Path(row['relative_to_target_task'])
        assert not rel.is_absolute() and '..' not in rel.parts
        data = git('show', commit + ':' + row['remote_path_at_target_commit'])
        digest = hashlib.sha256(data).hexdigest()
        blob = hashlib.sha1(f'blob {len(data)}\0'.encode() + data).hexdigest()
        assert (len(data), digest, blob) == (row['bytes'], row['sha256'], row['git_blob'])
        assert entries[row['remote_path_at_target_commit']] == (row['mode'], blob)
        destination = DEST / rel
        destination.parent.mkdir(parents=True, exist_ok=True)
        with destination.open('xb') as stream:
            stream.write(data)
        rows.append({**row, 'local_path': str(destination.relative_to(TASK)), 'identity_verified': True, 'semantic_credit': 0})
    receipt = {'schema': 'r8-lmc-input-recovery/v1', 'utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
               'commit': commit, 'checkout_tree': readset['target_checkout_tree'], 'task_tree': tree,
               'files': rows, 'file_count': len(rows), 'bytes': sum(r['bytes'] for r in rows),
               'set_exact': True, 'restored_code_executed': False, 'semantic_credit': 0}
    (TASK / 'evidence/input-recovery.json').write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({k: v for k, v in receipt.items() if k != 'files'}))

if __name__ == '__main__':
    main()
