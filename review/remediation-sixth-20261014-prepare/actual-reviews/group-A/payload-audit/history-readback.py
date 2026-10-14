"""Fetch fixed historical pointers and finite evidence packets; static parsing only."""
from pathlib import Path
import concurrent.futures
import datetime
import hashlib
import json
import subprocess
import urllib.parse
import urllib.request

ROOT = Path('/workspace/pokemon-essentials-clean-room')
P = 'review/remediation-sixth-20261014-prepare'
OUT = ROOT / (P + '/actual-reviews/group-A/payload-audit')
DB = '/tmp/r6-actual-a-payload-20261014.git'
H = OUT / 'historical-packets'
H.mkdir(exist_ok=True)
now = lambda: datetime.datetime.now(datetime.timezone.utc).isoformat()
identity = lambda b: {'bytes': len(b), 'sha256': hashlib.sha256(b).hexdigest(), 'git_blob': hashlib.sha1(b'blob ' + str(len(b)).encode() + b'\0' + b).hexdigest()}
commands = [json.loads(x) for x in (OUT / 'commands.jsonl').read_text().splitlines()]

def capture(argv, stdin=None):
    begin = now()
    result = subprocess.run(argv, cwd=ROOT, capture_output=True, input=stdin)
    n = len(commands) + 1
    stdout = OUT / 'logs' / f'{n:04d}.stdout'
    stderr = OUT / 'logs' / f'{n:04d}.stderr'
    stdout.write_bytes(result.stdout)
    stderr.write_bytes(result.stderr)
    commands.append({'argv': argv, 'cwd': str(ROOT), 'utc_start': begin, 'utc_end': now(), 'exit_code': result.returncode,
                     'stdout_path': str(stdout), 'stderr_path': str(stderr), 'stdout_identity': identity(result.stdout),
                     'stderr_identity': identity(result.stderr), 'stdin_identity': identity(stdin) if stdin else None,
                     'reference_behavior_execution': False})
    (OUT / 'commands.jsonl').write_text(''.join(json.dumps(x, ensure_ascii=False) + '\n' for x in commands))
    assert result.returncode == 0, result.stderr
    return result.stdout

packets = [
    ('U03-C', 'bcd194b0e4c293764998b7040b0154af8041bf41', 'candidates/R6-U03/evidence', [
        'historical-regression-input.json', 'R2-B21-regression-binding.json', 'id-evidence.json',
        'normative-input-binding.json', 'reading-ledger.json', 'author-report.md', 'verify_candidate.py']),
    ('U03-R', '034403bb9fbce7e49ea2784d38295c5260a1e0dd', 'reviews/R6-U03-R', [
        'historical-review.json', 'historical-readback.json', 'original-evidence-binding.json', 'reading-ledger.json', 'id-review.json']),
    ('U14-C', '12a35f0d4635524ab2148c0979a1a4d69eeb982e', 'candidates/R6-U14/evidence', [
        'historical-qualified-spans.json', 'historical-case-premises.json', 'newline-byte-validation.json',
        'per-id-author-handoff.json', 'author-tool-validation.json', 'packet-validation.json', 'author-report.md']),
    ('U14-R', '7cdf74a0b2494e2ec71ca39db6d917f81f420973', 'reviews/R6-U14-R', [
        'per-id-adjudication.json', 'reading-and-independence.json', 'independent-validation.json', 'peer-findings.md']),
]
jobs = []
for label, commit, prefix, names in packets:
    raw = capture(['git', '--git-dir=' + DB, 'ls-tree', '-r', '-z', commit, '--', P + '/' + prefix])
    metadata = {}
    for entry in raw.split(b'\0'):
        if entry:
            meta, path = entry.split(b'\t')
            mode, kind, oid = meta.decode().split()
            metadata[path.decode()] = {'mode': mode, 'type': kind, 'git_blob': oid}
    for name in names:
        path = P + '/' + prefix + '/' + name
        jobs.append({'label': label, 'commit': commit, 'path': path, 'local_path': str(H / (label + '-' + name)), **metadata[path]})

def fetch(item):
    url = 'https://raw.githubusercontent.com/y805939188/pokemon-essentials-clean-room/' + item['commit'] + '/' + urllib.parse.quote(item['path'], safe='/')
    attempts = []
    body = None
    for n in range(1, 4):
        begin = now()
        try:
            with urllib.request.urlopen(url, timeout=25) as response:
                full = response.read()
                status = response.status
            actual = identity(full)
            good = actual['git_blob'] == item['git_blob'] and item['mode'] == '100644' and item['type'] == 'blob'
            attempts.append({'attempt': n, 'utc_start': begin, 'utc_end': now(), 'url': url,
                             'HTTP_status': status, 'exit_code': 0 if good else 1, 'identity': actual})
            if good:
                body = full
                Path(item['local_path']).write_bytes(full)
                break
        except Exception as ex:
            attempts.append({'attempt': n, 'utc_start': begin, 'utc_end': now(), 'url': url, 'exit_code': 1, 'error': repr(ex)})
    return item, body, dict(item, attempts=attempts, full_body_match=body is not None)

bodies = []
receipts = []
with concurrent.futures.ThreadPoolExecutor(max_workers=8) as pool:
    for item, body, receipt in pool.map(fetch, jobs):
        bodies.append(body)
        receipts.append(receipt)
(OUT / 'historical-packet-fixed-object-readback.json').write_text(json.dumps(receipts, ensure_ascii=False, indent=2) + '\n')
assert all(body is not None for body in bodies)
packed = bytearray()
for n, body in enumerate(bodies, 1):
    packed.extend(b'blob\nmark :' + str(n).encode() + b'\ndata ' + str(len(body)).encode() + b'\n' + body + b'\n')
capture(['git', '--git-dir=' + DB, 'fast-import', '--quiet', '--done'], stdin=bytes(packed) + b'done\n')
print(json.dumps({'packets': len(receipts), 'all_complete_body_identity_match': True, 'local_packet_directory': str(H),
                  'scratch_database': DB, 'reference_execution': 0}, ensure_ascii=False))
