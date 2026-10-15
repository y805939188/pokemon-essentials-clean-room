"""Ordinary push to the sole authorized branch, then full immutable raw readback.

Publication receipts live outside the frozen candidate to avoid self-reference.
No source/reference program, credentials inspection, force push, tag, or merge.
"""
import concurrent.futures
import datetime
import hashlib
import json
import os
from pathlib import Path
import subprocess
import urllib.parse
import urllib.request


REPO = Path(__file__).resolve().parents[4]
BASE = 'e646432c644dec04d306842cc5a559a29c718fbc'
BRANCH = 'codex/r7-u02-author-20261015-wave1'
SLUG = 'y805939188/pokemon-essentials-clean-room'
ENVELOPE = Path('/workspace/r7-bootstrap/R7-U02-author/final-publication')


def utc():
    return datetime.datetime.now(datetime.timezone.utc).isoformat()


def identity(data):
    return {'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest(),
            'git_blob_content_id': hashlib.sha1(f'blob {len(data)}\0'.encode() + data).hexdigest()}


def git(*args):
    return subprocess.check_output(['git', *args], cwd=REPO)


def command(name, argv):
    start = utc()
    process = subprocess.Popen(argv, cwd=REPO, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                               env={**os.environ, 'GIT_TERMINAL_PROMPT': '0'})
    stdout, stderr = process.communicate()
    (ENVELOPE / (name + '.stdout')).write_bytes(stdout)
    (ENVELOPE / (name + '.stderr')).write_bytes(stderr)
    result = {'argv': argv, 'pid': process.pid, 'start_utc': start, 'end_utc': utc(),
              'exit_code': process.returncode, 'stdout': stdout.decode(errors='replace'),
              'stderr': stderr.decode(errors='replace')}
    (ENVELOPE / (name + '.json')).write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    return result


def fetch(url, maximum):
    start = utc()
    request = urllib.request.Request(url, headers={'User-Agent': 'R7-U02-immutable-candidate-readback'})
    with urllib.request.urlopen(request, timeout=40) as response:
        data = response.read(maximum + 1)
        status = response.status
    assert len(data) <= maximum
    return data, {'url': url, 'start_utc': start, 'end_utc': utc(), 'http_status': status}


def main():
    assert not ENVELOPE.exists(), 'Protect earlier publication evidence'
    ENVELOPE.mkdir(parents=True)
    receipt = {'start_utc': utc(), 'author_context': os.environ.get('CODEX_THREAD_ID', 'UNAVAILABLE'),
               'branch': BRANCH, 'base_commit': BASE, 'status': 'STARTED',
               'ordinary_push_only': True, 'semantic_acceptance': False}
    try:
        assert git('branch', '--show-current').decode().strip() == BRANCH
        assert git('status', '--porcelain').strip() == b''
        commit = git('rev-parse', 'HEAD').decode().strip()
        tree = git('rev-parse', 'HEAD^{tree}').decode().strip()
        assert git('rev-parse', 'HEAD^').decode().strip() == BASE
        assert git('rev-parse', 'HEAD:deliverables/final-specification-set').decode().strip() == 'ebbe29f2bc88cd17de7072bf440c6fa8c8c7089c'
        paths = git('diff', '--name-only', BASE, commit).decode().splitlines()
        allowed_mirrors = {
            'candidates/R7-U02/audit/source-traceability.md',
            'candidates/R7-U02/deliverables/final-specification-set/test-catalog/user-interface-wp17-63-65-66-67-68-69-70-71.md',
            'candidates/R7-U02/deliverables/final-specification-set/user-interface/wp17-messages-windows-input.md',
            'candidates/R7-U02/planning/feature-matrix.md'}
        assert all(p in allowed_mirrors or p.startswith('candidates/R7-U02/evidence/author/') for p in paths)
        assert allowed_mirrors.issubset(set(paths))
        receipt.update({'commit': commit, 'tree': tree, 'changed_file_count': len(paths)})
        pushed = command('ordinary-push', ['git', 'push', 'origin', 'HEAD:refs/heads/' + BRANCH])
        receipt['push'] = pushed
        assert pushed['exit_code'] == 0, 'Ordinary push failed; do not substitute another mutation path'
        remote = command('remote-ref-before', ['git', 'ls-remote', '--heads', 'origin', 'refs/heads/' + BRANCH])
        assert remote['exit_code'] == 0 and remote['stdout'].split()[0] == commit
        commit_bytes, commit_http = fetch('https://api.github.com/repos/' + SLUG + '/git/commits/' + commit, 1000000)
        (ENVELOPE / 'remote-commit.json').write_bytes(commit_bytes)
        remote_commit = json.loads(commit_bytes)
        assert remote_commit['sha'] == commit and remote_commit['tree']['sha'] == tree
        assert [p['sha'] for p in remote_commit['parents']] == [BASE]
        receipt['remote_commit_http'] = commit_http

        def read_one(path):
            local = git('show', commit + ':' + path)
            url = 'https://raw.githubusercontent.com/' + SLUG + '/' + commit + '/' + urllib.parse.quote(path)
            data, http = fetch(url, len(local))
            assert data == local, path
            output = ENVELOPE / 'readback' / path
            output.parent.mkdir(parents=True, exist_ok=True)
            output.write_bytes(data)
            return {'path': path, **identity(data), 'full_byte_match': True, 'transport': http}

        with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
            receipts = list(pool.map(read_one, paths))
        final_ref = command('remote-ref-after', ['git', 'ls-remote', '--heads', 'origin', 'refs/heads/' + BRANCH])
        assert final_ref['exit_code'] == 0 and final_ref['stdout'].split()[0] == commit
        assert git('status', '--porcelain').strip() == b''
        receipt.update({'status': 'PUSHED_FULL_REMOTE_READBACK_VERIFIED', 'files': receipts,
                        'remote_file_count': len(receipts), 'remote_bytes': sum(r['bytes'] for r in receipts),
                        'state': 'CANDIDATE_READY_NOT_REVIEWED', 'frozen_no_further_candidate_writes': True})
    except Exception as error:
        receipt['status'] = 'BLOCKED'
        receipt['error'] = str(error)
        raise
    finally:
        receipt['end_utc'] = utc()
        (ENVELOPE / 'publication-final.json').write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({k: receipt[k] for k in ['status', 'branch', 'commit', 'tree', 'remote_file_count', 'remote_bytes', 'state']}, ensure_ascii=False))
    print(str(ENVELOPE / 'publication-final.json'))


if __name__ == '__main__':
    main()
