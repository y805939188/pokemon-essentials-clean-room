import datetime, hashlib, json, pathlib, subprocess, sys

ROOT = pathlib.Path('/workspace/pokemon-essentials-clean-room')
OUT = ROOT / 'review/remediation-sixth-20261014-prepare/reviews/R6-U11-R/peers/storage'
kind, revision, path, lo, hi = sys.argv[1:]
lo, hi = int(lo), int(hi)
started = datetime.datetime.now(datetime.timezone.utc).isoformat()
argv = ['git', 'show', revision + ':' + path] if kind == 'git' else None
if argv:
    proc = subprocess.run(argv, cwd=ROOT, capture_output=True)
    if proc.returncode:
        print(proc.stderr.decode(), file=sys.stderr)
        raise SystemExit(proc.returncode)
    payload = proc.stdout
    entry = subprocess.run(['git', 'ls-tree', revision, '--', path], cwd=ROOT, capture_output=True, check=True).stdout.decode().strip()
else:
    payload = (ROOT / path).read_bytes()
    entry = 'filesystem regular file; Git blob computed without write'
lines = payload.decode('utf-8').splitlines()
assert 1 <= lo <= hi <= len(lines), (lo, hi, len(lines))
record = {'utc_start': started, 'utc_end': datetime.datetime.now(datetime.timezone.utc).isoformat(), 'cwd': str(ROOT), 'reader_argv': sys.argv, 'source_argv': argv, 'kind': kind, 'commit': revision if argv else None, 'path': path, 'bytes': len(payload), 'lines': len(lines), 'sha256': hashlib.sha256(payload).hexdigest(), 'git_blob': hashlib.sha1(b'blob ' + str(len(payload)).encode() + b'\0' + payload).hexdigest(), 'git_entry': entry, 'read_interval': [lo, hi], 'evidence_level': 'SOURCE_STATIC' if argv and revision.startswith('8c5911') else 'STATIC_DOCUMENT_READ', 'exit': 0, 'source_stderr': ''}
with (OUT / 'reading-ledger.jsonl').open('a') as f:
    f.write(json.dumps(record, ensure_ascii=False) + '\n')
print(json.dumps(record, ensure_ascii=False))
for n in range(lo, hi + 1):
    print(str(n) + ': ' + lines[n - 1])
