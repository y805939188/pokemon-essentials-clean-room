"""Transport verification only. Fresh filtered receiver; no local object alternates."""
from pathlib import Path
import datetime, hashlib, json, shutil, subprocess, sys

ROOT = Path(__file__).resolve().parent
REPO = Path('/workspace/pokemon-essentials-clean-room')
REL = str(ROOT.relative_to(REPO))
BRANCH = 'codex/r8-external-localization-records-20261016'
URL = 'https://github.com/y805939188/pokemon-essentials-clean-room.git'
commit = sys.argv[1]
output = ROOT / sys.argv[2]
receiver = ROOT / '.transport-readback.git'
if receiver.exists():
    raise SystemExit('Receiver must not pre-exist; preserve any unknown existing material.')
logs = []

def run(argv, cwd=REPO, binary=False):
    start = datetime.datetime.now(datetime.timezone.utc).isoformat()
    p = subprocess.run(argv, cwd=cwd, capture_output=True)
    end = datetime.datetime.now(datetime.timezone.utc).isoformat()
    logs.append({'argv': argv, 'cwd': str(cwd), 'started_utc': start,
                 'ended_utc': end, 'exit_code': p.returncode,
                 'stdout': None if binary else p.stdout.decode('utf-8', 'replace'),
                 'stdout_bytes': len(p.stdout),
                 'stdout_sha256': hashlib.sha256(p.stdout).hexdigest(),
                 'stderr': p.stderr.decode('utf-8', 'replace'),
                 'binary_stdout_qualification': 'Full bytes read and hashed; per-path identities retained below.' if binary else None})
    if p.returncode:
        raise RuntimeError('Command failed: ' + repr(argv))
    return p.stdout if binary else p.stdout.decode().strip()

def g(*args, remote=False, binary=False):
    return run(['git', '-C', str(receiver if remote else REPO), *args], binary=binary)

result = {'schema': 'gr8-full-remote-readback/v1', 'commit': commit, 'branch': BRANCH,
          'evidence_level': 'TOOL_VALIDATION', 'semantic_credit': False,
          'started_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
          'fresh_receiver': str(receiver), 'local_alternates': False,
          'unpublished_private_platform_stream_included': False}
try:
    tip = g('ls-remote', URL, 'refs/heads/' + BRANCH).split()[0]
    assert tip == commit, (tip, commit)
    g('init', '--bare', str(receiver))
    g('remote', 'add', 'origin', URL, remote=True)
    g('config', 'remote.origin.promisor', 'true', remote=True)
    g('config', 'remote.origin.partialclonefilter', 'blob:none', remote=True)
    g('-c', 'fetch.negotiationAlgorithm=noop', 'fetch', '--no-tags', '--depth=1',
      '--filter=blob:none', 'origin', 'refs/heads/' + BRANCH, remote=True)
    assert g('rev-parse', 'FETCH_HEAD', remote=True) == commit
    local_rows = g('ls-tree', '-r', '-l', commit, '--', REL).splitlines()
    remote_rows = g('ls-tree', '-r', '-l', commit, '--', REL, remote=True).splitlines()
    assert local_rows == remote_rows
    expected = []
    for line in local_rows:
        head, path = line.split('\t', 1)
        mode, kind, blob, size = head.split()
        assert kind == 'blob'
        expected.append((mode, blob, int(size), path))
    # Fetch all report blobs explicitly from origin into the fresh receiver.
    # No file bytes are borrowed from the existing repository for this step.
    blobs = sorted({x[1] for x in expected})
    for start in range(0, len(blobs), 64):
        g('-c', 'fetch.negotiationAlgorithm=noop', 'fetch', '--no-tags',
          'origin', *blobs[start:start+64], remote=True)
    records = []
    for mode, blob, size, path in expected:
        local = g('cat-file', 'blob', blob, binary=True)
        actual = g('cat-file', 'blob', blob, remote=True, binary=True)
        assert local == actual and len(actual) == size
        records.append({'path': path, 'mode': mode, 'git_blob': blob, 'bytes': size,
                        'sha256': hashlib.sha256(actual).hexdigest(),
                        'full_remote_bytes_read': True, 'matches_local_fixed_commit': True})
    result.update(status='VERIFIED', workspace_tree=g('rev-parse', commit+'^{tree}', remote=True),
                  report_directory_tree=g('rev-parse', commit+':'+REL, remote=True),
                  file_count=len(records), total_bytes=sum(x['bytes'] for x in records),
                  files=records)
except Exception as e:
    result.update(status='FAILED', error=repr(e))
finally:
    result['ended_utc'] = datetime.datetime.now(datetime.timezone.utc).isoformat()
    result['io'] = logs
    output.write_text(json.dumps(result, ensure_ascii=False, indent=2)+'\n')
    # Only this newly created receiver is removed; report/evidence inputs remain.
    if receiver.exists():
        shutil.rmtree(receiver)
print(json.dumps({k: result.get(k) for k in ['status','commit','workspace_tree',
    'report_directory_tree','file_count','total_bytes','error']}, ensure_ascii=False))
if result['status'] != 'VERIFIED':
    raise SystemExit(1)
