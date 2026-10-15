import datetime
import hashlib
import json
import os
import sys
from pathlib import Path

root = Path(__file__).resolve().parents[1]
folder = Path('/workspace/r7-ir-R7-U02/actual-input/actual')
files = sorted(folder.rglob('*.md'))
index, start, end = map(int, sys.argv[1:4])
path = files[index]
data = path.read_bytes()
lines = data.decode().splitlines(keepends=True)
end = min(end, len(lines))
print(f'FILE {index}: {path.relative_to(folder)} | {start}-{end} / {len(lines)}')
for i in range(start-1,end):
    print(f'{i+1}: '+lines[i],end='')
entry = dict(path=str(path.relative_to(folder)),start_line=start,end_line=end,total_lines=len(lines),
             bytes=len(data),sha256=hashlib.sha256(data).hexdigest(),utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),pid=os.getpid(),
             qualification='Content output to current reviewer; I/O receipt alone is not semantic PASS')
with (root/'read-delivery.jsonl').open('a') as stream:
    stream.write(json.dumps(entry,ensure_ascii=False)+'\n')
