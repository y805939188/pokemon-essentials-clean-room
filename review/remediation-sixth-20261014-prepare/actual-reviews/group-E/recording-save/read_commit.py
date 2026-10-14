import sys,subprocess,hashlib,json,datetime
from pathlib import Path
BASE=Path(__file__).resolve().parent
locator=sys.argv[1];lo=int(sys.argv[2]) if len(sys.argv)>2 else 1;hi=int(sys.argv[3]) if len(sys.argv)>3 else 0
start=datetime.datetime.now(datetime.timezone.utc).isoformat()
r=subprocess.run(['git','show',locator],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
end=datetime.datetime.now(datetime.timezone.utc).isoformat()
if r.returncode: raise RuntimeError(r.stderr.decode())
b=r.stdout;lines=b.decode().splitlines();hi=hi or len(lines)
assert 1<=lo<=hi<=len(lines)
rec={'locator':locator,'bytes':len(b),'lines':len(lines),'sha256':hashlib.sha256(b).hexdigest(),'git_blob':hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest(),'range':[lo,hi],'argv':sys.argv,'cwd':str(Path.cwd()),'start_utc':start,'end_utc':end,'git_show_exit':r.returncode,'git_show_stderr':r.stderr.decode(),'evidence_level':'IMMUTABLE_DOCUMENT_PRESENTATION','note':'Semantic reading separate from identity/source execution; no reference or author program execution.'}
with (BASE/'reading-ledger.jsonl').open('a') as f: f.write(json.dumps(rec,ensure_ascii=False)+'\n')
print(json.dumps({k:rec[k] for k in ['locator','bytes','lines','sha256','git_blob','range']},ensure_ascii=False))
for n in range(lo-1,hi): print(f'{n+1}: {lines[n]}')
