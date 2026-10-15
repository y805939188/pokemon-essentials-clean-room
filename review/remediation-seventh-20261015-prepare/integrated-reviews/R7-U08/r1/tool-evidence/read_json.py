import sys,json,os,datetime,hashlib
from pathlib import Path
p=Path(sys.argv[1]);b=p.read_bytes();j=json.loads(b)
for pointer in sys.argv[2:]:
 x=j
 for key in pointer.strip('/').split('/') if pointer else []:x=x[int(key)] if isinstance(x,list) else x[key.replace('~1','/').replace('~0','~')]
 row={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'tool_pid':os.getpid(),'path':str(p),'file_bytes':len(b),'file_sha256':hashlib.sha256(b).hexdigest(),'json_pointer':pointer,'stage':'STATIC_JSON_READ','semantic_pass_from_tool':False}
 with Path(__file__).with_name('reading-ledger.jsonl').open('a') as f:f.write(json.dumps(row)+'\n')
 print(json.dumps(row));print(json.dumps(x,ensure_ascii=False))
