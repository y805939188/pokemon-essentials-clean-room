from pathlib import Path
import datetime,hashlib,json,subprocess,sys
ROOT=Path('/workspace/pokemon-essentials-clean-room')
OUT=Path(__file__).resolve().parent
commit,path,a,z=sys.argv[1:];a=int(a);z=int(z)
start=datetime.datetime.now(datetime.timezone.utc).isoformat()
proc=subprocess.run(['git','show',commit+':'+path],cwd=ROOT,capture_output=True)
entry=subprocess.run(['git','ls-tree',commit,'--',path],cwd=ROOT,capture_output=True)
if proc.returncode:raise RuntimeError(proc.stderr.decode())
b=proc.stdout;lines=b.decode().splitlines(keepends=True)
assert 1<=a<=z and a<=len(lines)
z=min(z,len(lines));payload=''.join(lines[a-1:z])
rows=[json.loads(l) for l in (OUT/'reading-ledger.jsonl').read_text().splitlines()] if (OUT/'reading-ledger.jsonl').exists() else []
seq=len(rows)+1;tag=f'read-{seq:03d}'
(OUT/(tag+'.stdout.txt')).write_text(payload)
(OUT/(tag+'.stderr.txt')).write_bytes(proc.stderr+entry.stderr)
row={'reader':'/root/history_payload','argv':sys.argv,'git_argv':['git','show',commit+':'+path],'cwd':str(ROOT),'runtime':sys.version,'start_utc':start,'end_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'commit':commit,'path':path,'git_entry':entry.stdout.decode().strip(),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'git_blob':hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest(),'total_lines':len(lines),'start_line':a,'end_line':z,'returned_bytes':len(payload.encode()),'returned_sha256':hashlib.sha256(payload.encode()).hexdigest(),'source_read_exit':proc.returncode,'entry_read_exit':entry.returncode,'stdout_file':tag+'.stdout.txt','stderr_file':tag+'.stderr.txt','semantic_read':'Complete requested line range presented; identity does not imply unrequested semantic scope.'}
with (OUT/'reading-ledger.jsonl').open('a') as f:f.write(json.dumps(row,ensure_ascii=False)+'\n')
print(json.dumps(row,ensure_ascii=False))
for i,line in enumerate(payload.splitlines(),a):print(f'{i:5d} {line}')
