"""Recover only manifest-bound regular blobs from an independently fetched bare repository.

No recovered code is imported, executed, or granted semantic reading credit.
"""
from pathlib import Path
import datetime
import hashlib
import json
import subprocess

TASK = Path(__file__).resolve().parents[1]
ROOT = TASK.parents[1]
BARE = Path('/tmp/r8-receive-pbs-target.git')
READSET = ROOT / 'delegation/readsets/receive_external_pbs_creature_backups.complete.json'
DEST = TASK / 'recovered-target'

def git(*args):
    return subprocess.check_output(['git', '--git-dir=' + str(BARE), *args])

def main():
    rs = json.loads(READSET.read_text())
    commit = rs['target_commit']
    taskpath = 'review/global-independent-review/eighth-2026-10-16-fd1df57-c84e/tasks/external_pbs_creature_backups'
    assert git('rev-parse', commit + '^{tree}').decode().strip() == rs['target_checkout_tree']
    assert git('rev-parse', commit + ':' + taskpath).decode().strip() == rs['target_task_tree_observed_from_fixed_commit']
    entries = {}
    for line in git('ls-tree', '-rz', commit, '--', taskpath).split(b'\0'):
        if not line:
            continue
        metadata, path = line.split(b'\t', 1)
        mode, typ, blob = metadata.decode().split()
        assert typ == 'blob' and mode == '100644'
        entries[path.decode()] = (mode, blob)
    expected = {r['remote_path_at_target_commit'] for r in rs['files']}
    assert len(expected) == len(rs['files']) == rs['input_file_count']
    assert set(entries) == expected, (set(entries) - expected, expected - set(entries))
    assert not DEST.exists() and not DEST.is_symlink()
    rows = []
    for row in rs['files']:
        rel = Path(row['relative_to_target_task'])
        assert not rel.is_absolute() and '..' not in rel.parts
        mode, blob = entries[row['remote_path_at_target_commit']]
        assert mode == row['mode'] and blob == row['git_blob']
        data = git('cat-file', 'blob', blob)
        assert len(data) == row['bytes']
        assert hashlib.sha256(data).hexdigest() == row['sha256']
        p = DEST / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        with p.open('xb') as f:
            f.write(data)
        p.chmod(0o644)
        rows.append(dict(row, local_path=str(p.relative_to(TASK)), status='IDENTITY_VERIFIED_ONLY', semantic_reading_credit=0))
    assert sum(r['bytes'] for r in rows) == rs['input_bytes']
    result = dict(schema='r8-independent-exact-recovery/v1', utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
                  commit=commit, checkout_tree=rs['target_checkout_tree'], task_tree=rs['target_task_tree_observed_from_fixed_commit'],
                  bare_repository=str(BARE), files=rows, collection_exact=True, bytes=sum(r['bytes'] for r in rows),
                  restored_code_executed=False, semantic_reading_credit=0)
    (TASK / 'recovery.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({k: result[k] for k in ['commit','checkout_tree','task_tree','collection_exact','bytes','semantic_reading_credit']}))

if __name__ == '__main__':
    main()
