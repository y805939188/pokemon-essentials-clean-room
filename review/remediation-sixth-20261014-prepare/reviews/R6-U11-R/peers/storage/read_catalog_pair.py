import datetime, hashlib, json, pathlib, subprocess, sys

ROOT = pathlib.Path('/workspace/pokemon-essentials-clean-room')
OUT = ROOT / 'review/remediation-sixth-20261014-prepare/reviews/R6-U11-R/peers/storage'
FORMAL = 'deliverables/final-specification-set/test-catalog/user-interface-wp17-63-65-66-67-68-69-70-71.md'
CANDIDATE = 'review/remediation-sixth-20261014-prepare/candidates/R6-U11/mirror/' + FORMAL
REVISION = '8ea169fbd0f33f378b5d732fd6bea59e854e04a6'
lo, hi = map(int, sys.argv[1:])
assert hi < 287 or lo >= 287, 'split at the insertion boundary'
offset = 31 if lo >= 287 else 0
started = datetime.datetime.now(datetime.timezone.utc).isoformat()
argv = ['git', 'show', REVISION + ':' + FORMAL]
p = subprocess.run(argv, cwd=ROOT, capture_output=True, check=True)
before, after = p.stdout, (ROOT / CANDIDATE).read_bytes()
first, second = before.decode().splitlines(), after.decode().splitlines()
assert first[lo - 1:hi] == second[lo + offset - 1:hi + offset]
for path, data, start, end, commit in [(FORMAL, before, lo, hi, REVISION), (CANDIDATE, after, lo + offset, hi + offset, None)]:
    record = {'utc_start': started, 'utc_end': datetime.datetime.now(datetime.timezone.utc).isoformat(), 'cwd': str(ROOT), 'reader_argv': sys.argv, 'source_argv': argv if commit else None, 'kind': 'git' if commit else 'work', 'commit': commit, 'path': path, 'bytes': len(data), 'lines': len(data.decode().splitlines()), 'sha256': hashlib.sha256(data).hexdigest(), 'git_blob': hashlib.sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest(), 'read_interval': [start, end], 'semantic_read_mode': 'FRESH_PAIRED_IDENTICAL_TEXT_WITH_BOTH_COORDINATES', 'paired_span_byte_equal': True, 'evidence_level': 'STATIC_DOCUMENT_READ', 'exit': 0, 'source_stderr': ''}
    with (OUT / 'reading-ledger.jsonl').open('a') as f:
        f.write(json.dumps(record, ensure_ascii=False) + '\n')
    print(json.dumps(record, ensure_ascii=False))
for n in range(lo, hi + 1):
    print('F' + str(n) + '/C' + str(n + offset) + ': ' + first[n - 1])
