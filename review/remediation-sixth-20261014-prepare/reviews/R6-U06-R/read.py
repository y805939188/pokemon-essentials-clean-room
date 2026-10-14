import sys, json, hashlib, subprocess, datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent
args = sys.argv[1:]
ref, path = args[:2]
if ref == 'worktree':
    data = Path(path).read_bytes()
    mode = '100644'
else:
    data = subprocess.check_output(['git', 'show', ref + ':' + path])
    mode = subprocess.check_output(['git', 'ls-tree', ref, '--', path], text=True).split()[0]
lines = data.decode().splitlines()
start, end = (int(args[2]), int(args[3])) if len(args) >= 4 else (1, len(lines))
blob = hashlib.sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest()
record = dict(ref=ref, path=path, bytes=len(data), sha256=hashlib.sha256(data).hexdigest(),
              git_blob=blob, mode=mode, type='blob', lines=len(lines), range=[start, end],
              emitted_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
              method='Full exact bytes read; numbered bounded ranges emitted to reviewer transcript; emission is not automatic semantic PASS')
with (ROOT / 'readings.jsonl').open('a') as f:
    f.write(json.dumps(record, ensure_ascii=False) + '\n')
print(json.dumps(record, ensure_ascii=False))
for i in range(start - 1, min(end, len(lines))):
    print(f'{i + 1}: {lines[i]}')
