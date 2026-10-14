"""Bounded read-only range display; append retrieval evidence, never semantic PASS."""
import datetime
import hashlib
import json
from pathlib import Path
import sys

ROOT = Path('/Users/dingshinn/Desktop/pokemon-framework-reference')
OUT = ROOT / 'review/global-independent-review/sixth-2026-10-14-8ea169f-46ae/tasks/R6-CM'
path = (ROOT / sys.argv[1]).resolve()
allowed = [ROOT / 'reference/pokemon-essentials', ROOT / 'deliverables/final-specification-set']
if not any(path.is_relative_to(base) for base in allowed):
    raise SystemExit('Input outside bound source/formal roots')
start, stop = map(int, sys.argv[2:4])
raw = path.read_bytes()
lines = raw.decode('utf-8-sig').splitlines()
if start < 1 or stop < start or start > len(lines):
    raise SystemExit('Invalid line range')
stop = min(stop, len(lines))
print(f'FILE {path.relative_to(ROOT)} RANGE {start}-{stop}/{len(lines)}')
for index in range(start - 1, stop):
    print(f'{index + 1:5}: {lines[index]}')
entry = {
    'timestamp': datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'path': str(path.relative_to(ROOT)), 'range': [start, stop],
    'sha256': hashlib.sha256(raw).hexdigest(),
    'mode': 'actual_text_retrieval', 'semantic_review': 'pending_separate_annotation',
    'tool': 'R6-CM/tools/read_range.py', 'copy_to_output': False,
}
with (OUT / 'reading-ledger.jsonl').open('a') as stream:
    stream.write(json.dumps(entry, ensure_ascii=False) + '\n')
