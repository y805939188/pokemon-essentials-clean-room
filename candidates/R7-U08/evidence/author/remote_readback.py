"""Read every added candidate file in full from immutable GitHub raw URLs.

No downloaded program is executed. Exact byte comparison, length, SHA256 and
content Git blob are checked independently of the local Git object transport.
"""
import argparse
import concurrent.futures
import datetime
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import urllib.parse
import urllib.request

B = 'e646432c644dec04d306842cc5a559a29c718fbc'
BRANCH = 'codex/r7-u08-author-20261015-wave1'


def utc():
    return datetime.datetime.now(datetime.timezone.utc).isoformat()


def git(*args):
    p = subprocess.run(['git', *args], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if p.returncode:
        raise RuntimeError(json.dumps({'argv': ['git', *args], 'exit': p.returncode,
                                       'stdout': p.stdout.decode(), 'stderr': p.stderr.decode()}))
    return p.stdout


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--commit', required=True)
    parser.add_argument('--output')
    args = parser.parse_args()
    assert re.fullmatch('[0-9a-f]{40}', args.commit)
    start = utc()
    advertised = git('ls-remote', '--heads', 'origin', 'refs/heads/' + BRANCH).decode()
    assert advertised.split() == [args.commit, 'refs/heads/' + BRANCH], advertised
    # Ordinary read-only remote fetch; updates FETCH_HEAD, never a branch or tag.
    fetched = subprocess.run(['git', 'fetch', '--no-tags', 'origin', BRANCH],
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    assert fetched.returncode == 0, fetched.stderr.decode()
    assert git('rev-parse', 'FETCH_HEAD').decode().strip() == args.commit
    changes = git('diff', '--name-status', B, args.commit).decode().splitlines()
    paths = []
    for row in changes:
        status, path = row.split('\t')
        assert status == 'A' and path.startswith('candidates/R7-U08/'), row
        paths.append(path)
    assert paths

    def read_one(path):
        expected = git('show', f'{args.commit}:{path}')
        url = ('https://raw.githubusercontent.com/y805939188/pokemon-essentials-clean-room/'
               + args.commit + '/' + urllib.parse.quote(path))
        began = utc()
        request = urllib.request.Request(url, headers={'User-Agent': 'R7-U08-author-byte-readback'})
        with urllib.request.urlopen(request, timeout=40) as response:
            actual = response.read(len(expected) + 1)
            status = response.status
        assert actual == expected, path
        blob = hashlib.sha1(f'blob {len(actual)}\0'.encode() + actual).hexdigest()
        assert blob == git('rev-parse', f'{args.commit}:{path}').decode().strip()
        return {'path': path, 'bytes': len(actual), 'sha256': hashlib.sha256(actual).hexdigest(),
                'git_blob_content_id': blob, 'http_status': status,
                'start_utc': began, 'end_utc': utc(), 'complete_bytes_match': True, 'url': url}

    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        results = list(pool.map(read_one, paths))
    result = {'schema': 'r7.u08.complete-remote-readback.v1', 'commit': args.commit,
              'tree': git('rev-parse', args.commit + '^{tree}').decode().strip(),
              'branch': BRANCH, 'remote_advertisement': advertised,
              'fetch': {'exit': fetched.returncode, 'stdout': fetched.stdout.decode(),
                        'stderr': fetched.stderr.decode()},
              'pid': os.getpid(), 'start_utc': start, 'end_utc': utc(),
              'status': 'ALL_ADDED_FILES_COMPLETE_REMOTE_BYTE_MATCH',
              'file_count': len(results), 'bytes_read': sum(r['bytes'] for r in results),
              'files': results, 'semantic_acceptance': False,
              'author_status': 'CANDIDATE_READY_NOT_REVIEWED'}
    if args.output:
        target = Path(args.output)
        assert target.parent.resolve() == Path(__file__).resolve().parent
        with target.open('x') as stream:
            json.dump(result, stream, ensure_ascii=False, indent=2)
            stream.write('\n')
        print(json.dumps({k: result[k] for k in ('commit', 'tree', 'status', 'file_count', 'bytes_read')}))
    else:
        # Final publication receipt stays in the platform transcript, so no
        # uncommitted self-referential receipt is left in the frozen checkout.
        print(json.dumps(result, ensure_ascii=False, separators=(',', ':')))


if __name__ == '__main__':
    main()
