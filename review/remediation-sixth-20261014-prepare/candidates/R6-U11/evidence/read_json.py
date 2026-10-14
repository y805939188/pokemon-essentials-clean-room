"""Emit full selected JSON nodes from fixed inputs; no summary or source execution."""
import sys,json,hashlib,subprocess,datetime
from pathlib import Path
base=Path(__file__).resolve().parent
start=datetime.datetime.now(datetime.timezone.utc).isoformat()
commit,path,*pointers=sys.argv[1:]
r=subprocess.run(['git','show',commit+':'+path],capture_output=True)
if r.returncode:sys.stderr.buffer.write(r.stderr);sys.exit(r.returncode)
b=r.stdout;j=json.loads(b);out=[]
for pointer in pointers:
 v=j
 for k in pointer.strip('/').split('/') if pointer else []:v=v[int(k)] if isinstance(v,list) else v[k.replace('~1','/').replace('~0','~')]
 out.append({'pointer':pointer,'content':v})
t=json.dumps(out,ensure_ascii=False,indent=2)+'\n'
rec={'argv':sys.argv,'cwd':str(Path.cwd()),'utc_start':start,'utc_end':datetime.datetime.now(datetime.timezone.utc).isoformat(),'exit':0,'stderr':r.stderr.decode(),'commit':commit,'path':path,'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'git_blob':subprocess.check_output(['git','rev-parse',commit+':'+path]).decode().strip(),'json_pointers':pointers,'scope':'Full selected records emitted; unrelated records are not claimed read.','stdout_sha256':hashlib.sha256(t.encode()).hexdigest()}
with (base/'reading-ledger.jsonl').open('a') as f:f.write(json.dumps(rec,ensure_ascii=False)+'\n')
print(t,end='')
