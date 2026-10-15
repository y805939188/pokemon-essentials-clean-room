import sys,json,hashlib,datetime,os
from pathlib import Path
p=Path(sys.argv[1]);b=p.read_bytes();s=b.decode();mode=sys.argv[2] if len(sys.argv)>2 else 'full'
record={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'tool_pid':os.getpid(),'path':str(p),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'git_blob_content_id':hashlib.sha1(f'blob {len(b)}\0'.encode()+b).hexdigest(),'mode':mode}
if mode=='lines':
 a,z=map(int,sys.argv[3:5]);lines=s.splitlines();out='\n'.join(f'{i+1}: {lines[i]}' for i in range(a-1,min(z,len(lines))));record['lines']=[a,min(z,len(lines))]
elif mode=='pointer':
 value=json.loads(s);pointer=sys.argv[3]
 for part in pointer.strip('/').split('/'):
  value=value[int(part)] if isinstance(value,list) else value[part.replace('~1','/').replace('~0','~')]
 out=json.dumps(value,ensure_ascii=False,indent=2);record['pointer']=pointer
else: out=s
record['returned_utf8_bytes']=len(out.encode())
with Path('/workspace/r7-ir-R7-U03-final/audit/read-log.jsonl').open('a') as f:f.write(json.dumps(record,ensure_ascii=False)+'\n')
print('READ',json.dumps(record,ensure_ascii=False));print(out)
