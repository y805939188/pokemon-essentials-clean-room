"""Read every newly published preparation file from its immutable remote URL."""
from pathlib import Path
import concurrent.futures
import datetime
import hashlib
import json
import subprocess
import urllib.parse
import urllib.request

PROJECT = Path(__file__).resolve().parents[3]
OUT = Path(__file__).resolve().parents[1]


def git(*args):
    return subprocess.check_output(['git', '-C', str(PROJECT), *args])


def main():
    commit = git('rev-parse', 'HEAD').decode().strip()
    branch = git('branch', '--show-current').decode().strip()
    remote = git('ls-remote', 'origin', 'refs/heads/' + branch).decode().strip()
    assert remote.split()[0] == commit
    paths = git('diff', '--name-only', '-z', '4580645dfbfec4a3c7ccbad56ae293cc619b0d25', commit).decode().strip('\0').split('\0')
    destination = Path('/workspace/r7-remote-readback') / commit
    destination.mkdir(parents=True, exist_ok=False)

    def check(path):
        url = 'https://raw.githubusercontent.com/y805939188/pokemon-essentials-clean-room/' + commit + '/' + urllib.parse.quote(path)
        with urllib.request.urlopen(url, timeout=40) as response:
            data = response.read()
            status = response.status
        expected = git('show', commit + ':' + path)
        assert data == expected, path
        target = destination / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(data)
        return {'path': path, 'url': url, 'http_status': status, 'bytes': len(data),
                'sha256': hashlib.sha256(data).hexdigest(),
                'git_blob': hashlib.sha1(f'blob {len(data)}\0'.encode() + data).hexdigest(),
                'complete_byte_match': True}

    with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:
        checked = list(pool.map(check, paths))
    receipt = {'schema': 'r7.cloud-preparation-remote-readback.v1', 'utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
               'commit': commit, 'tree': git('rev-parse', commit + '^{tree}').decode().strip(),
               'remote_branch_readback': remote, 'status': 'ALL_NEW_FILES_FULL_REMOTE_BYTES_MATCH',
               'counts': {'files': len(checked), 'bytes': sum(x['bytes'] for x in checked)},
               'files': checked, 'local_remote_byte_copies': str(destination),
               'scope': 'Only this remediation preparation delta from C2; inherited R7 package not redundantly rescanned. Identity/transport only; zero semantic candidate/integration acceptance.'}
    target = OUT / ('startup/remote-readback-' + commit[:8] + '.json')
    with target.open('x') as stream:
        json.dump(receipt, stream, ensure_ascii=False, indent=2)
        stream.write('\n')
    print(json.dumps({'commit': commit, 'status': receipt['status'], 'counts': receipt['counts'], 'receipt': str(target.relative_to(PROJECT))}))


if __name__ == '__main__':
    main()
