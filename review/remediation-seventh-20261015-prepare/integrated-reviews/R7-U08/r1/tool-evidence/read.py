import sys,json,hashlib,os,datetime
from pathlib import Path
p=Path(sys.argv[1]); data=p.read_bytes(); lines=data.decode().splitlines(keepends=True)
a=int(sys.argv[2]) if len(sys.argv)>2 else 1;b=int(sys.argv[3]) if len(sys.argv)>3 else len(lines)
selected=''.join(lines[a-1:b]); row={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'tool_pid':os.getpid(),'path':str(p),'file_bytes':len(data),'file_sha256':hashlib.sha256(data).hexdigest(),'git_blob':hashlib.sha1(f'blob {len(data)}\0'.encode()+data).hexdigest(),'lines':[a,min(b,len(lines))],'total_lines':len(lines),'output_bytes':len(selected.encode()),'stage':'STATIC_READ_ONLY','semantic_pass_from_tool':False}
with Path(__file__).with_name('reading-ledger.jsonl').open('a') as f:f.write(json.dumps(row,ensure_ascii=False)+'\n')
print(json.dumps(row,ensure_ascii=False))
for n,s in enumerate(lines[a-1:b],a):print(f'{n}: {s}',end='')
