import datetime, hashlib, json, os, pathlib, sys
root=pathlib.Path('/workspace/r7-ir-R7-U06')
p=pathlib.Path(sys.argv[1]); data=p.read_bytes(); lines=data.decode().splitlines(keepends=True)
start=int(sys.argv[2]) if len(sys.argv)>2 else 1
end=int(sys.argv[3]) if len(sys.argv)>3 else len(lines)
out=''.join(f'{i+1}: {s}' for i,s in enumerate(lines) if start<=i+1<=end)
record={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'pid':os.getpid(),'path':str(p),'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest(),'git_blob':hashlib.sha1(f'blob {len(data)}\0'.encode()+data).hexdigest(),'lines':[start,end],'file_lines':len(lines),'kind':'CONTENT_READ_NOT_EXECUTION'}
with (root/'bootstrap-evidence/read-ledger.jsonl').open('a') as f:f.write(json.dumps(record,ensure_ascii=False)+'\n')
print(out,end='')
