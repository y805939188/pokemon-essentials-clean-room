import datetime
import hashlib
import json
import pathlib
import subprocess
import sys

ROOT = pathlib.Path('/workspace/pokemon-essentials-clean-room')
OWN = ROOT / 'review/remediation-sixth-20261014-prepare/reviews/R6-U13-R/recording-save'
kind, name, start, end = sys.argv[1:5]
start, end = int(start), int(end)
if kind == 'git':
    data = subprocess.check_output(['git', 'show', name], cwd=ROOT)
else:
    data = (ROOT / name).read_bytes()
lines = data.decode().splitlines()
end = len(lines) if end == 0 else min(end, len(lines))
identity = dict(kind=kind, locator=name, bytes=len(data), lines=len(lines),
                sha256=hashlib.sha256(data).hexdigest(),
                git_blob=hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest())
rec = dict(identity, presented_range=[start,end], utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
           argv=sys.argv, cwd=str(ROOT), evidence_level='SOURCE_STATIC_OR_DOCUMENT_READ',
           note='Presentation receipt; semantic reading attested in final report. No source execution.')
with (OWN/'reading-ledger.jsonl').open('a') as f:
    f.write(json.dumps(rec,ensure_ascii=False)+'\n')
print(json.dumps(identity,ensure_ascii=False))
for n in range(start,end+1):
    print(f'{n}: {lines[n-1]}')
