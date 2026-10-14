import sys,json,pathlib,subprocess,hashlib,datetime
out=pathlib.Path(__file__).resolve().parent
start=datetime.datetime.now(datetime.timezone.utc).isoformat()
kind,ident=sys.argv[1:3]
rec={'reader':'/root/variants','scope':'final-audit-01/dependencies','kind':kind,'input':ident,'argv':sys.argv,'start_utc':start}
try:
 if kind in ('git','json'):
  r=subprocess.run(['git','show',ident],stdout=subprocess.PIPE,stderr=subprocess.PIPE,cwd='/workspace/pokemon-essentials-clean-room');rec.update(exit=r.returncode,stderr=r.stderr.decode());data=r.stdout
  if r.returncode:raise RuntimeError(r.stderr.decode())
 else:data=pathlib.Path(ident).read_bytes();rec.update(exit=0,stderr='')
 rec.update(bytes=len(data),sha256=hashlib.sha256(data).hexdigest(),git_blob=hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest())
 lines=data.decode().splitlines();rec['total_lines']=len(lines)
 if kind=='json':
  d=json.loads(data);rec['semantic_pointers']=[]
  for ptr in sys.argv[3:]:
   v=d
   for part in ptr.strip('/').split('/'):v=v[int(part)] if isinstance(v,list) else v[part]
   print('POINTER',ptr,json.dumps(v,ensure_ascii=False,indent=2));rec['semantic_pointers'].append(ptr)
 else:
  rec['semantic_ranges']=[]
  for rr in sys.argv[3:] or [f'1-{len(lines)}']:
   a,b=map(int,rr.split('-'));assert 1<=a<=b<=len(lines)
   print('INPUT',ident,'RANGE',a,b,'TOTAL',len(lines))
   for i in range(a,b+1):print(f'{i:4} {lines[i-1]}')
   rec['semantic_ranges'].append([a,b])
 rec['qualification']='Complete displayed ranges/pointers semantically read; identity reads separately recorded. No reference/behavior execution.'
except Exception as e:
 rec.update(exit=rec.get('exit') or 1,error=repr(e),qualification='Only prior successfully displayed ranges/pointers eligible; failed operation not full reading.')
 raise
finally:
 rec['end_utc']=datetime.datetime.now(datetime.timezone.utc).isoformat()
 with (out/'reading-ledger.jsonl').open('a') as f:f.write(json.dumps(rec,ensure_ascii=False)+'\n')
