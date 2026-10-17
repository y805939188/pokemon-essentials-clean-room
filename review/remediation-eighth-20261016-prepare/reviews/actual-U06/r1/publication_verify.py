#!/usr/bin/env python3
"""Fresh remote full-byte reception of this review directory only."""
import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import subprocess
import tempfile

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
PREFIX = str(HERE.relative_to(ROOT)) + '/'
BRANCH = 'codex/r8-u06-actual-review-r1-20261017'
BASE = '2e2d5e6ab3f531ee902f60574b22e20fb065e04b'
parser = argparse.ArgumentParser()
parser.add_argument('commit')
parser.add_argument('--save-receipt', action='store_true')
args = parser.parse_args()
logs = []

def utc():
    return datetime.now(timezone.utc).isoformat()

def sha(data):
    return hashlib.sha256(data).hexdigest()

def run(cwd, argv):
    start = utc()
    p = subprocess.run(argv, cwd=cwd, capture_output=True)
    entry = {'cwd': str(cwd), 'argv': argv, 'started_utc': start,
             'finished_utc': utc(), 'exit_code': p.returncode,
             'stdout_bytes': len(p.stdout), 'stdout_sha256': sha(p.stdout),
             'stderr_bytes': len(p.stderr), 'stderr_sha256': sha(p.stderr),
             'stderr_utf8': p.stderr.decode(errors='replace')}
    if len(p.stdout) < 1024:
        entry['stdout_utf8'] = p.stdout.decode(errors='replace')
    logs.append(entry)
    if p.returncode:
        raise RuntimeError(entry)
    return p.stdout

started = utc()
url = run(ROOT, ['git', 'remote', 'get-url', 'origin']).decode().strip()
delta = run(ROOT, ['git', 'diff', '--name-only', BASE, args.commit]).decode().splitlines()
assert all(p.startswith(PREFIX) for p in delta), delta
records = []
with tempfile.TemporaryDirectory(prefix='r8-u06-actual-readback-') as scratch:
    remote = Path(scratch) / 'remote.git'
    run(ROOT, ['git', 'init', '--bare', str(remote)])
    run(remote, ['git', 'remote', 'add', 'origin', url])
    run(remote, ['git', 'config', 'remote.origin.promisor', 'true'])
    run(remote, ['git', 'config', 'remote.origin.partialclonefilter', 'blob:none'])
    run(remote, ['git', 'fetch', '--depth=1', '--filter=blob:none', 'origin',
                 'refs/heads/' + BRANCH])
    tip = run(remote, ['git', 'rev-parse', 'FETCH_HEAD']).decode().strip()
    assert tip == args.commit, (tip, args.commit)
    run(remote, ['git', 'cat-file', '-e', args.commit + '^{commit}'])
    tree = run(remote, ['git', 'ls-tree', '-r', args.commit, '--', PREFIX]).decode()
    assert not (remote / 'objects/info/alternates').exists()
    for line in tree.splitlines():
        metadata, path = line.split('\t', 1)
        mode, kind, blob = metadata.split()
        raw = run(remote, ['git', 'show', args.commit + ':' + path])
        local_git = run(ROOT, ['git', 'show', args.commit + ':' + path])
        local_working = (ROOT / path).read_bytes()
        records.append({'path': path, 'mode': mode, 'kind': kind, 'blob': blob,
                        'bytes': len(raw), 'sha256': sha(raw),
                        'local_git_equal': raw == local_git,
                        'working_bytes_equal': raw == local_working})
    refs = run(ROOT, ['git', 'ls-remote', 'origin', 'refs/heads/' + BRANCH,
                     'refs/heads/main',
                     'refs/heads/codex/remediation-eighth-20261017-4575']).decode()

result = {'schema': 'r8-u06-actual-review-publication-readback/v1',
          'started_utc': started, 'finished_utc': utc(), 'remote_url': url,
          'branch': BRANCH, 'payload_commit': args.commit, 'base_commit': BASE,
          'scope': PREFIX, 'new_or_changed_paths_from_base': delta,
          'fresh_bare_without_alternates': True,
          'full_blob_bytes_received': True,
          'records': records, 'files': len(records),
          'total_bytes': sum(x['bytes'] for x in records),
          'all_equal': all(x['local_git_equal'] and x['working_bytes_equal'] for x in records),
          'remote_refs_after': refs, 'commands': logs,
          'qualification': 'TRANSPORT_AND_SCOPE_ONLY; verdict remains BLOCKED',
          'actual_integrated_PASS': False, 'business_execution': 'NOT_EXECUTED'}
assert records and result['all_equal']
if args.save_receipt:
    (HERE / 'publication-readback.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({k: result[k] for k in ['payload_commit', 'files', 'total_bytes', 'all_equal',
      'fresh_bare_without_alternates', 'full_blob_bytes_received', 'remote_refs_after']}, ensure_ascii=False))
