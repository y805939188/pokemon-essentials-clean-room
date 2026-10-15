"""Read back the exact R7-U09 reviewer branch and every new result file.

Usage: python3 <this-file> --commit <expected-40hex> --receipt <path>
Only read-only remote operations are performed. Does not push or execute inputs.
"""
import argparse
import concurrent.futures
import datetime
import hashlib
import json
from pathlib import Path
import re
import subprocess
import urllib.parse
import urllib.request

ROOT = Path('/workspace/r7-u09-reviewer-checkout')
BASE = 'e646432c644dec04d306842cc5a559a29c718fbc'
BRANCH = 'codex/r7-u09-reviewer-20261015-r1'
PREFIX = 'candidates/R7-U09/evidence/reviewer/r1/'


def utc():
    return datetime.datetime.now(datetime.timezone.utc).isoformat()


def git(*args):
    return subprocess.check_output(['git', *args], cwd=ROOT)


def identity(b):
    return {'bytes': len(b), 'sha256': hashlib.sha256(b).hexdigest(),
            'git_blob': hashlib.sha1(f'blob {len(b)}\0'.encode() + b).hexdigest()}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--commit', required=True)
    parser.add_argument('--receipt', required=True, type=Path)
    args = parser.parse_args()
    assert re.fullmatch('[0-9a-f]{40}', args.commit)
    result = {'schema': 'r7.u09-reviewer-complete-remote-readback.v1', 'start_utc': utc(),
              'expected_commit': args.commit, 'branch': BRANCH, 'baseline': BASE, 'files': [],
              'qualification': 'TOOL_VALIDATION only. No behavioral execution or acceptance/closure.'}
    refs = git('ls-remote', '--heads', 'origin', 'refs/heads/' + BRANCH).decode().split()
    assert refs == [args.commit, 'refs/heads/' + BRANCH], refs
    fetch = subprocess.run(['git', 'fetch', '--no-tags', 'origin', 'refs/heads/' + BRANCH],
                           cwd=ROOT, capture_output=True, text=True)
    assert fetch.returncode == 0, fetch.stderr
    assert git('rev-parse', 'FETCH_HEAD').decode().strip() == args.commit
    result['fetch_stdout'] = fetch.stdout
    result['fetch_stderr'] = fetch.stderr
    result['fetch_exit'] = fetch.returncode
    result['actual_remote_commit'] = refs[0]
    result['actual_tree'] = git('rev-parse', args.commit + '^{tree}').decode().strip()
    result['parents'] = git('show', '-s', '--format=%P', args.commit).decode().strip().split()
    diffs = git('diff', '--name-status', BASE, args.commit).decode().splitlines()
    paths = []
    for row in diffs:
        status, path = row.split('\t')
        assert status == 'A' and path.startswith(PREFIX), row
        paths.append(path)
    assert paths
    result['complete_diff_against_B'] = diffs
    def read_one(p):
        expected = git('show', args.commit + ':' + p)
        mode, typ, blob_path = git('ls-tree', args.commit, '--', p).decode().strip().split(' ', 2)
        blob, path = blob_path.split('\t')
        assert mode == '100644' and typ == 'blob' and path == p
        url = 'https://raw.githubusercontent.com/y805939188/pokemon-essentials-clean-room/' + args.commit + '/' + urllib.parse.quote(p)
        start = utc()
        with urllib.request.urlopen(url, timeout=40) as response:
            actual = response.read(len(expected) + 1)
            status = response.status
        assert actual == expected, p
        ident = identity(actual)
        assert ident['git_blob'] == blob
        return {'path': p, 'mode': mode, 'url': url, 'start_utc': start, 'end_utc': utc(),
                'http_status': status, **ident, 'full_remote_bytes_equal_commit_blob': True}
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        result['files'] = list(pool.map(read_one, paths))
    result['file_count'] = len(paths)
    result['byte_count'] = sum(r['bytes'] for r in result['files'])
    assert git('ls-remote', '--heads', 'origin', 'refs/heads/' + BRANCH).decode().split() == refs
    result['remote_ref_unchanged_after_full_read'] = True
    result['status'] = 'COMPLETE_REMOTE_BYTES_VERIFIED'
    result['end_utc'] = utc()
    args.receipt.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
