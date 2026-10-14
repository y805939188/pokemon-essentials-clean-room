import datetime
import hashlib
import json
import pathlib
import subprocess
import sys

ROOT=pathlib.Path('/workspace/pokemon-essentials-clean-room')
OWN=ROOT/'review/remediation-sixth-20261014-prepare/reviews/R6-U13-R/repair-01/recording-save'
locator,start,end=sys.argv[1:4]
start,end=int(start),int(end)
begin=datetime.datetime.now(datetime.timezone.utc).isoformat()
result=subprocess.run(['git','show',locator],cwd=ROOT,capture_output=True)
if result.returncode:
    print(result.stderr.decode());sys.exit(result.returncode)
raw=result.stdout
lines=raw.decode().splitlines()
end=len(lines) if end==0 else min(end,len(lines))
record=dict(locator=locator,bytes=len(raw),lines=len(lines),
            sha256=hashlib.sha256(raw).hexdigest(),
            git_blob=hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest(),
            range=[start,end],argv=sys.argv,cwd=str(ROOT),start_utc=begin,
            end_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
            git_show_exit=result.returncode,git_show_stderr=result.stderr.decode(),
            evidence_level='IMMUTABLE_DOCUMENT_PRESENTATION',
            note='Semantic reading attested in repair report; no reference/author program execution.')
with (OWN/'reading-ledger.jsonl').open('a') as file:
    file.write(json.dumps(record,ensure_ascii=False)+'\n')
print(json.dumps({k:v for k,v in record.items() if k in ['locator','bytes','lines','sha256','git_blob','range']},ensure_ascii=False))
for line in range(start,end+1):print(f'{line}: {lines[line-1]}')
