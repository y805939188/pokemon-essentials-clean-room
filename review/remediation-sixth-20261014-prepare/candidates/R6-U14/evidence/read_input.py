"""Bounded complete-text reads, with exact input/range and process receipts."""
import datetime
import hashlib
import json
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[5]
OUT = Path(__file__).resolve().parent
start = datetime.datetime.now(datetime.timezone.utc).isoformat()
kind, ref, path, first, last = sys.argv[1:]
first, last = int(first), int(last)
argv = ['git', 'show', ref + ':' + path] if kind == 'git' else ['read_bytes', path]
if kind == 'git':
    result = subprocess.run(argv, cwd=ROOT, capture_output=True)
    data, stderr, code = result.stdout, result.stderr, result.returncode
else:
    data, stderr, code = (ROOT / path).read_bytes(), b'', 0
lines = data.decode('utf-8').splitlines(keepends=True) if code == 0 else []
selected = ''.join(lines[first-1:last])
receipt = dict(kind=kind, ref=ref, path=path, argv=argv, cwd=str(ROOT),
               utc_start=start, utc_end=datetime.datetime.now(datetime.timezone.utc).isoformat(),
               input_bytes=len(data), input_sha256=hashlib.sha256(data).hexdigest(),
               input_lines=len(lines), range=[first, min(last, len(lines))],
               stdout_bytes=len(selected.encode()), stdout_sha256=hashlib.sha256(selected.encode()).hexdigest(),
               stderr=stderr.decode(), exit_code=code,
               evidence_level='SOURCE_STATIC_OR_DOCUMENT_READ; semantic review requires assistant inspection')
with (OUT / 'reading-receipts.jsonl').open('a') as stream:
    stream.write(json.dumps(receipt, ensure_ascii=False) + '\n')
print(json.dumps({k: receipt[k] for k in ['path', 'range', 'input_lines', 'exit_code']}, ensure_ascii=False))
print(selected, end='')
sys.exit(code)
