"""Read-only full-range display; preserves actual stdout and UTC, never grants review credit."""
import datetime
import hashlib
import json
import pathlib
import sys

task = pathlib.Path(__file__).resolve().parent
path = pathlib.Path(sys.argv[1]).resolve()
start = int(sys.argv[2])
end = int(sys.argv[3])
raw = path.read_bytes()
lines = raw.decode('utf-8-sig').splitlines(keepends=True)
assert 1 <= start <= end <= len(lines), (start, end, len(lines))
began = datetime.datetime.now(datetime.timezone.utc).isoformat()
body = ''.join(f'{i:05d} {lines[i-1]}' for i in range(start, end+1))
if not body.endswith('\n'):
    body += '\n'
metadata = {'path':str(path), 'range':[start,end], 'file_lines':len(lines),
            'bytes':len(raw), 'sha256':hashlib.sha256(raw).hexdigest(),
            'began_utc':began, 'evidence':'READ_DISPLAY_ONLY',
            'semantic_acceptance':'REQUIRES_REVIEWER_JUDGMENT'}
out = json.dumps(metadata,ensure_ascii=False)+'\n'+body
seq = len(list((task/'read-io').glob('*.stdout.txt'))) if (task/'read-io').exists() else 0
(task/'read-io').mkdir(exist_ok=True)
stem = f'{seq+1:04d}'
(task/'read-io'/f'{stem}.stdout.txt').write_text(out)
metadata['ended_utc'] = datetime.datetime.now(datetime.timezone.utc).isoformat()
metadata['exit_code'] = 0
metadata['stdout'] = f'read-io/{stem}.stdout.txt'
with (task/'read-io'/'index.jsonl').open('a') as stream:
    stream.write(json.dumps(metadata,ensure_ascii=False)+'\n')
sys.stdout.write(out)
