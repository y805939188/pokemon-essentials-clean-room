"""Capture and display an exact bounded window of this auditor's reading aid.

Static text only. It never imports or executes the reviewed program. A receipt
records successful byte retrieval, not a reader's semantic acceptance.
"""
import datetime
import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
source = (ROOT / sys.argv[1]).resolve()
if ROOT not in source.parents:
    raise ValueError('Only auditor-local frozen input or aid may be displayed')
start, end = int(sys.argv[2]), int(sys.argv[3])
label = sys.argv[4]
if not label.replace('-', '').replace('_', '').isalnum():
    raise ValueError('Unsafe receipt label')
begin = datetime.datetime.now(datetime.timezone.utc).isoformat()
raw = source.read_bytes()
lines = raw.decode('utf-8').splitlines(keepends=True)
if start < 1 or end < start or end > len(lines):
    raise ValueError(f'Out of range: {start}..{end} of {len(lines)}')
output = ''.join(lines[start-1:end])
(ROOT / f'{label}.stdout.txt').write_text(output)
sys.stdout.write(output)
receipt = {
    'source': str(source.relative_to(ROOT)),
    'source_sha256': hashlib.sha256(raw).hexdigest(),
    'source_bytes': len(raw), 'source_lines': len(lines),
    'displayed_view_lines': [start, end],
    'stdout_path': f'{label}.stdout.txt',
    'stdout_bytes': len(output.encode()),
    'stdout_sha256': hashlib.sha256(output.encode()).hexdigest(),
    'stderr': '', 'exit_code': 0, 'began_utc': begin,
    'ended_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'qualification': 'Static retrieval only; no semantic acceptance inferred.'
}
(ROOT / f'{label}.receipt.json').write_text(json.dumps(receipt, indent=2)+'\n')
