"""Print exact selected UTF-8 lines; record the I/O range without semantic credit."""
import datetime
import hashlib
import json
import os
from pathlib import Path
import sys

p = Path(sys.argv[1]).resolve()
b = p.read_bytes()
lines = b.decode('utf-8').splitlines(keepends=True)
start = int(sys.argv[2]) if len(sys.argv) > 2 else 1
end = int(sys.argv[3]) if len(sys.argv) > 3 else len(lines)
assert 1 <= start <= end <= len(lines)
selected = ''.join(lines[start-1:end])
print(f'FILE {p} L{start}-L{end}/{len(lines)}', flush=True)
print(selected, end='', flush=True)
row = {'utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
       'tool_pid': os.getpid(), 'path': str(p), 'file_bytes': len(b),
       'file_sha256': hashlib.sha256(b).hexdigest(), 'start_line': start,
       'end_line': end, 'total_lines': len(lines),
       'output_bytes': len(selected.encode()),
       'output_sha256': hashlib.sha256(selected.encode()).hexdigest(),
       'qualification': 'Exact static text printed; no execution or semantic PASS inferred.'}
with Path('/workspace/r7-ir-R7-U01/tool-evidence/read-io.jsonl').open('a') as f:
    f.write(json.dumps(row, ensure_ascii=False)+'\n')
