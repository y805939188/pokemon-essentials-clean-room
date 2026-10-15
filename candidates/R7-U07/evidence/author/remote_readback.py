"""Read complete committed candidate bytes from immutable remote raw URLs."""
from pathlib import Path
import concurrent.futures
import datetime
import hashlib
import json
import re
import subprocess
import sys
import urllib.parse
import urllib.request

ROOT = Path(__file__).resolve().parents[4]
PREFIX = 'candidates/R7-U07/'
BRANCH = 'codex/r7-u07-author-20261015-wave1'
BASE = 'e646432c644dec04d306842cc5a559a29c718fbc'
commit = sys.argv[1]
assert re.fullmatch('[0-9a-f]{40}', commit)
stdout_only = '--stdout-only' in sys.argv[2:]
utc = lambda: datetime.datetime.now(datetime.timezone.utc).isoformat()


def git(*args):
    return subprocess.check_output(['git', *args], cwd=ROOT)


def identity(data):
    return {'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest(),
            'git_blob': hashlib.sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest()}


receipt = {'schema': 'r7.u07.complete-remote-readback.v1', 'start_utc': utc(),
           'commit': commit, 'branch': BRANCH, 'argv': sys.argv,
           'cwd': str(ROOT), 'files': [],
           'qualification': 'Complete remote byte/identity verification only. No independent semantic PASS, ACCEPTED, CLOSED or game execution.'}
try:
    args = ['git', '-c', 'credential.helper=!f() { printf "%s\\n" "username=x-access-token" "password=$GH_TOKEN"; }; f',
            'ls-remote', '--heads', 'origin', BRANCH]
    remote = subprocess.run(args, cwd=ROOT, capture_output=True, text=True, timeout=45)
    receipt['remote_head_io'] = {'argv': args, 'stdout': remote.stdout,
                                 'stderr': remote.stderr, 'exit_code': remote.returncode}
    assert remote.returncode == 0
    assert remote.stdout.split() == [commit, 'refs/heads/' + BRANCH], remote.stdout
    receipt['tree'] = git('rev-parse', commit + '^{tree}').decode().strip()
    changed = git('diff', '--name-only', BASE, commit).decode().splitlines()
    assert changed and all(p.startswith(PREFIX) for p in changed), changed
    paths = git('ls-tree', '-r', '--name-only', commit, PREFIX).decode().splitlines()
    assert sorted(paths) == sorted(changed), 'Only newly added candidate files expected'

    def fetch(path):
        expected = identity(git('show', commit + ':' + path))
        url = 'https://raw.githubusercontent.com/y805939188/pokemon-essentials-clean-room/' + commit + '/' + urllib.parse.quote(path)
        start = utc()
        request = urllib.request.Request(url, headers={'User-Agent': 'R7-U07-author-fixed-commit-readback'})
        with urllib.request.urlopen(request, timeout=40) as response:
            data = response.read(expected['bytes'] + 1)
            status = response.status
        actual = identity(data)
        assert status == 200 and actual == expected, path
        return {'path': path, 'url': url, 'start_utc': start, 'end_utc': utc(),
                'http_status': status, 'expected': expected, 'actual': actual,
                'complete_bytes_match': True}

    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        receipt['files'] = sorted(pool.map(fetch, paths), key=lambda row: row['path'])
    receipt['status'] = 'COMPLETE_REMOTE_BYTES_VERIFIED'
    receipt['file_count'] = len(receipt['files'])
    receipt['bytes_verified'] = sum(row['actual']['bytes'] for row in receipt['files'])
except Exception as error:
    receipt['status'] = 'REMOTE_READBACK_FAILED'
    receipt['error'] = repr(error)
    raise
finally:
    receipt['end_utc'] = utc()
    if not stdout_only:
        name = 'publication-receipt.json' if receipt['status'] == 'COMPLETE_REMOTE_BYTES_VERIFIED' else 'publication-failure-' + datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%dT%H%M%S%fZ') + '.json'
        target = ROOT / PREFIX / 'evidence/author' / name
        assert not target.exists(), target
        target.write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps(receipt if stdout_only else {k: receipt[k] for k in ['status', 'commit', 'tree', 'file_count', 'bytes_verified'] if k in receipt}, ensure_ascii=False))
