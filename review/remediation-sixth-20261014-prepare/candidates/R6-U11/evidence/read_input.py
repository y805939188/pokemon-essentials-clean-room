"""Read fixed Git payload/ranges; log identity. No project code is executed."""
import sys,subprocess,hashlib,json,datetime
from pathlib import Path
base=Path(__file__).resolve().parent
start=datetime.datetime.now(datetime.timezone.utc).isoformat()
commit,path,lo,hi=sys.argv[1:5];lo=int(lo);hi=int(hi)
r=subprocess.run(['git','show',commit+':'+path],capture_output=True)
if r.returncode: sys.stderr.buffer.write(r.stderr);sys.exit(r.returncode)
b=r.stdout;lines=b.decode('utf-8').splitlines();assert 1<=lo<=hi<=len(lines)
out='\n'.join(lines[lo-1:hi])+'\n'
rec={'argv':sys.argv,'git_argv':['git','show',commit+':'+path],'cwd':str(Path.cwd()),'utc_start':start,'utc_end':datetime.datetime.now(datetime.timezone.utc).isoformat(),'exit':r.returncode,'stderr':r.stderr.decode(),'commit':commit,'path':path,'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'git_blob':subprocess.check_output(['git','rev-parse',commit+':'+path]).decode().strip(),'git_entry':subprocess.check_output(['git','ls-tree',commit,path]).decode().strip(),'range':[lo,hi],'total_lines':len(lines),'stdout_scope':'Full selected range emitted in task tool transcript; hash below. Fixed Git payload recovers content.','stdout_sha256':hashlib.sha256(out.encode()).hexdigest(),'evidence_level':'SOURCE_STATIC' if commit.startswith('8c5911') else 'INPUT_READ'}
with (base/'reading-ledger.jsonl').open('a') as f:f.write(json.dumps(rec,ensure_ascii=False)+'\n')
print(out,end='')
