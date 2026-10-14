from pathlib import Path
import datetime,hashlib,json,subprocess,sys
ROOT=Path('/workspace/pokemon-essentials-clean-room');OUT=Path(__file__).resolve().parent
commit,path,a,z=sys.argv[1:];a=int(a);z=int(z);start=datetime.datetime.now(datetime.timezone.utc).isoformat()
p=subprocess.run(['git','show',commit+':'+path],cwd=ROOT,capture_output=True);e=subprocess.run(['git','ls-tree',commit,'--',path],cwd=ROOT,capture_output=True)
ledger=OUT/'reading-ledger.jsonl';n=len(ledger.read_text().splitlines())+1 if ledger.exists() else 1;tag=f'read-{n:03d}'
b=p.stdout;lines=b.decode().splitlines(keepends=True);z=min(z,len(lines));data=''.join(lines[a-1:z]);(OUT/(tag+'.stdout.txt')).write_text(data);(OUT/(tag+'.stderr.txt')).write_bytes(p.stderr+e.stderr)
x={'reader':'/root/history_payload','argv':sys.argv,'git_argv':['git','show',commit+':'+path],'cwd':str(ROOT),'runtime':sys.version,'start_utc':start,'end_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'commit':commit,'path':path,'entry':e.stdout.decode().strip(),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'git_blob':hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest(),'total_lines':len(lines),'start_line':a,'end_line':z,'returned_bytes':len(data.encode()),'returned_sha256':hashlib.sha256(data.encode()).hexdigest(),'git_read_exit':p.returncode,'entry_read_exit':e.returncode,'stdout':tag+'.stdout.txt','stderr':tag+'.stderr.txt','scope':'Full displayed range; no semantic claim for unrequested ranges.'}
with ledger.open('a') as f:f.write(json.dumps(x,ensure_ascii=False)+'\n')
print(json.dumps(x,ensure_ascii=False));assert p.returncode==e.returncode==0,(p.stderr,e.stderr)
for i,l in enumerate(data.splitlines(),a):print(f'{i:5d} {l}')
