"""Fetch remote metadata and only this task's new blobs; verify the full increment."""
import argparse
import datetime
import hashlib
import json
import pathlib
import subprocess
import tempfile

OUT = pathlib.Path(__file__).resolve().parent
REPO = next(p for p in OUT.parents if (p / '.git').exists())
PREFIX = str(OUT.relative_to(REPO))
BASE = '35d85e4484b892ebc32542346861440638d2183c'
BRANCH = 'codex/r8-cp-reception-02-20261016'
commands = []


def git(repo, *args):
    cmd = ['git', '-C', str(repo), *args]
    p = subprocess.run(cmd, capture_output=True)
    commands.append({'argv':cmd,'exit':p.returncode,'stdout_bytes':len(p.stdout),
                     'stdout_sha256':hashlib.sha256(p.stdout).hexdigest(),
                     'stderr':p.stderr.decode(errors='replace')})
    if p.returncode:
        raise RuntimeError(commands[-1])
    return p.stdout


def tree(repo, commit):
    raw = git(repo, 'ls-tree', '-rz', commit, '--', PREFIX)
    rows = []
    for item in raw.split(b'\0'):
        if not item:
            continue
        left, path = item.split(b'\t', 1)
        mode, typ, blob = left.decode().split()
        assert typ == 'blob'
        rows.append({'path':path.decode(),'mode':mode,'git_blob':blob})
    return rows


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('commit')
    parser.add_argument('--receipt', action='store_true')
    args = parser.parse_args()
    target = git(REPO, 'rev-parse', args.commit).decode().strip()
    remote_url = git(REPO, 'remote', 'get-url', 'origin').decode().strip()
    changed = git(REPO, 'diff', '--name-only', BASE, target).decode().splitlines()
    assert changed and all(p.startswith(PREFIX + '/') for p in changed)
    expected = tree(REPO, target)
    assert set(changed) == {f['path'] for f in expected}
    head = git(REPO, 'ls-remote', '--heads', 'origin', BRANCH).decode().split()[0]
    assert head == target, (head, target)
    remote = pathlib.Path(tempfile.mkdtemp(prefix='r8-cp02-readback-', dir='/tmp')) / 'remote.git'
    git(REPO, 'init', '--bare', str(remote))
    git(remote, 'remote', 'add', 'origin', remote_url)
    git(remote, 'config', 'remote.origin.promisor', 'true')
    git(remote, 'config', 'remote.origin.partialclonefilter', 'blob:none')
    git(remote, 'fetch', '--filter=blob:none', '--depth=1', '--no-tags', 'origin', target)
    observed = tree(remote, target)
    assert observed == expected
    core_tree = git(REPO, 'rev-parse', target + '^{tree}').decode().strip()
    task_tree = git(REPO, 'rev-parse', target + ':' + PREFIX).decode().strip()
    assert git(remote, 'rev-parse', target + '^{tree}').decode().strip() == core_tree
    assert git(remote, 'rev-parse', target + ':' + PREFIX).decode().strip() == task_tree
    for f in observed:
        data = git(remote, 'cat-file', 'blob', f['git_blob'])
        local = git(REPO, 'cat-file', 'blob', f['git_blob'])
        assert data == local
        assert hashlib.sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest() == f['git_blob']
        f.update(bytes=len(data), sha256=hashlib.sha256(data).hexdigest())
    result = {'schema':'r8-cp02-publication/v1','status':'REMOTE_FULL_INCREMENT_READBACK_MATCH',
              'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
              'branch':BRANCH,'contract_commit':BASE,'verified_commit':target,
              'workspace_tree':core_tree,'result_directory':PREFIX,'result_tree':task_tree,
              'remote_head':head,'files':observed,'file_count':len(observed),
              'increment_bytes':sum(f['bytes'] for f in observed),
              'metadata_only_fetch_then_own_increment_blobs':True,
              'commands':commands,'credit':'TRANSPORT_IDENTITY_ONLY',
              'source_recovery_reused':'31 exact fixed input payloads; no re-download or new credit',
              'semantic_result':'READY_FOR_PARENT_RECEPTION_WITH_QUALIFICATIONS',
              'root_decision_open':['GR8-EXTCP-002 overall precision/ownership and actual ELR receipt'],
              'UPDATE_NOT_STARTED':True}
    if args.receipt:
        assert not (OUT / 'publication.json').exists()
        (OUT / 'publication.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({k:result[k] for k in ['status','verified_commit','workspace_tree','result_tree','file_count','increment_bytes']},ensure_ascii=False))


if __name__ == '__main__':
    main()
