"""Bounded manifest/publication transport for this reviewer evidence only."""
import concurrent.futures
import datetime
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import urllib.parse
import urllib.request

ROOT = Path('/workspace/r7-u07-reviewer-r1')
REL = 'candidates/R7-U07/evidence/reviewer/r1/'
OUT = ROOT / REL
B = 'e646432c644dec04d306842cc5a559a29c718fbc'
BRANCH = 'codex/r7-u07-reviewer-20261015-r1'


def utc():
    return datetime.datetime.now(datetime.timezone.utc).isoformat()


def identity(data):
    return {'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest(),
            'git_blob': hashlib.sha1(f'blob {len(data)}\0'.encode() + data).hexdigest()}


def git(*args):
    return subprocess.check_output(['git', *args], cwd=ROOT)


def check_scope():
    assert git('branch', '--show-current').decode().strip() == BRANCH
    assert git('rev-parse', 'HEAD:deliverables/final-specification-set') == git('rev-parse', B + ':deliverables/final-specification-set')
    paths = set(git('diff', '--name-only', B).decode().splitlines())
    paths.update(git('ls-files', '--others', '--exclude-standard').decode().splitlines())
    assert paths and all(p.startswith(REL) for p in paths), sorted(paths)
    return paths


def manifest():
    paths = check_scope()
    paths.add(REL + 'artifact-manifest.json')
    files = []
    for p in sorted(OUT.rglob('*')):
        if p.is_dir():
            continue
        assert not p.is_symlink()
        if p.name == 'artifact-manifest.json':
            continue
        data = p.read_bytes()
        if p.suffix == '.json':
            json.loads(data)
        files.append({'path': str(p.relative_to(ROOT)), 'base_B_identity_or_explicit_new_file': 'NEW_REVIEWER_EVIDENCE', **identity(data), 'git_mode': '100644'})
    result = {'schema': 'r7.u07.reviewer-artifact-manifest.v1', 'base_commit': B, 'branch': BRANCH,
              'actual_context': os.environ.get('CODEX_THREAD_ID', 'NOT_EXPOSED'),
              'verdict': 'WAIT_INPUT_OR_INDEPENDENCE', 'content_assessment': 'PASS_SCOPED_CANDIDATE',
              'files': files, 'nonself_count': len(files), 'nonself_bytes': sum(row['bytes'] for row in files),
              'self_identity': {'path': REL + 'artifact-manifest.json', 'qualification': 'Excluded from recursive hashing. Fixed final commit/tree and complete final remote readback bind its bytes externally.'},
              'generation': {'utc': utc(), 'pid': os.getpid(), 'cwd': str(ROOT), 'argv': sys.argv,
                             'stdout': 'MANIFEST_SCOPE_AND_BYTES_VALIDATED', 'stderr': '', 'exit_code': 0},
              'qualification': 'Evidence identity only. Candidate review gate remains WAIT; no integration, acceptance or closure.'}
    assert {row['path'] for row in files} | {REL + 'artifact-manifest.json'} == paths
    (OUT / 'artifact-manifest.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({'status': 'MANIFEST_SCOPE_AND_BYTES_VALIDATED', 'nonself_files': len(files), 'nonself_bytes': result['nonself_bytes']}))


def readback(commit, output):
    start = utc()
    head = git('ls-remote', '--heads', 'origin', 'refs/heads/' + BRANCH).decode()
    assert head.split()[0] == commit
    tree = git('rev-parse', commit + '^{tree}').decode().strip()
    diff = git('diff', '--name-status', B, commit).decode()
    changed = []
    for line in diff.splitlines():
        status, path = line.split('\t')
        assert status == 'A' and path.startswith(REL)
        changed.append(path)
    modes = {}
    for line in git('ls-tree', '-r', commit, REL).decode().splitlines():
        meta, path = line.split('\t'); mode, typ, blob = meta.split()
        assert mode == '100644' and typ == 'blob'
        modes[path] = blob
    assert set(changed) == set(modes)

    def one(path):
        url = 'https://raw.githubusercontent.com/y805939188/pokemon-essentials-clean-room/' + commit + '/' + urllib.parse.quote(path)
        expected = git('show', commit + ':' + path)
        request_start = utc()
        with urllib.request.urlopen(url, timeout=45) as response:
            actual = response.read(len(expected) + 1)
            status = response.status
        assert actual == expected
        row = identity(actual)
        assert row['git_blob'] == modes[path]
        return {'path': path, **row, 'git_mode': '100644', 'url': url, 'http_status': status,
                'request_start_utc': request_start, 'request_end_utc': utc(), 'complete_byte_match': True}

    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        files = list(pool.map(one, sorted(changed)))
    manifest_data = json.loads(git('show', commit + ':' + REL + 'artifact-manifest.json'))
    manifest_paths = set()
    for row in manifest_data['files']:
        expected = identity(git('show', commit + ':' + row['path']))
        assert all(row[k] == expected[k] for k in expected)
        manifest_paths.add(row['path'])
    assert manifest_paths | {REL + 'artifact-manifest.json'} == set(changed)
    end_head = git('ls-remote', '--heads', 'origin', 'refs/heads/' + BRANCH).decode()
    assert end_head == head
    result = {'schema': 'r7.u07.reviewer-complete-remote-readback.v1', 'start_utc': start, 'end_utc': utc(),
              'actual_context': os.environ.get('CODEX_THREAD_ID', 'NOT_EXPOSED'), 'pid': os.getpid(),
              'commit': commit, 'tree': tree, 'branch': BRANCH, 'remote_head_before': head, 'remote_head_after': end_head,
              'complete_diff_against_B': diff, 'files': files, 'file_count': len(files),
              'bytes_verified': sum(row['bytes'] for row in files), 'status': 'COMPLETE_REMOTE_BYTES_VERIFIED',
              'manifest_nonself_and_self_coverage': True,
              'qualification': 'All changed evidence files read in full from immutable remote URLs and equal Git blobs; complete diff/modes and branch head bound. No semantic/integration/acceptance/closure or behavior-execution credit.'}
    with Path(output).open('x') as f:
        json.dump(result, f, ensure_ascii=False, indent=2); f.write('\n')
    print(json.dumps({k: result[k] for k in ['status', 'commit', 'tree', 'branch', 'file_count', 'bytes_verified', 'manifest_nonself_and_self_coverage']}, ensure_ascii=False))


if __name__ == '__main__':
    if sys.argv[1:] == ['manifest']:
        manifest()
    elif len(sys.argv) == 4 and sys.argv[1] == 'readback':
        readback(sys.argv[2], sys.argv[3])
    else:
        raise SystemExit('usage: manifest | readback <full-commit> <new-output-json>')
