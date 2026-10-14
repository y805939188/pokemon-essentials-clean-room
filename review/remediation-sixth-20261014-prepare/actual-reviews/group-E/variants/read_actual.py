import sys,json,hashlib,pathlib,datetime,subprocess
out=pathlib.Path(__file__).resolve().parent
cwd=pathlib.Path('/workspace/pokemon-essentials-clean-room')
start=datetime.datetime.now(datetime.timezone.utc).isoformat()
kind,ident=sys.argv[1:3]
if kind=='git':
 r=subprocess.run(['git','show',ident],cwd=cwd,stdout=subprocess.PIPE,stderr=subprocess.PIPE);data=r.stdout;stderr=r.stderr.decode();code=r.returncode
else:
 data=(cwd/ident).read_bytes();stderr='';code=0
rec=dict(reader='/root/variants',cwd=str(cwd),argv=sys.argv,kind=kind,input=ident,start_utc=start,read_exit=code,read_stderr=stderr)
if code:
 rec['end_utc']=datetime.datetime.now(datetime.timezone.utc).isoformat();(out/'reading-ledger.jsonl').open('a').write(json.dumps(rec,ensure_ascii=False)+'\n');print(stderr);sys.exit(code)
rec.update(bytes=len(data),sha256=hashlib.sha256(data).hexdigest(),git_blob=hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest())
lines=data.decode().splitlines();rec['total_lines']=len(lines)
if kind=='json':
 d=json.loads(data);ptrs=sys.argv[3:];rec['semantic_pointers']=ptrs
 for ptr in ptrs:
  v=d
  try:
   for part in ptr.strip('/').split('/'):
    v=v[int(part)] if isinstance(v,list) else v[part]
  except (KeyError,IndexError,ValueError) as e:
   rec.update(read_exit=1,failed_pointer=ptr,read_stderr=repr(e),end_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),semantic_attestation='Only pointers printed before this failure were displayed; failed pointer not read.')
   (out/'reading-ledger.jsonl').open('a').write(json.dumps(rec,ensure_ascii=False)+'\n')
   raise
  print('JSON POINTER',ptr,json.dumps(v,ensure_ascii=False,indent=2))
else:
 ranges=[list(map(int,s.split('-'))) for s in sys.argv[3:]] or [[1,len(lines)]]
 if any(a<1 or b>len(lines) or a>b for a,b in ranges):raise ValueError('Invalid read range')
 rec['read_ranges']=ranges
 for a,b in ranges:
  print('INPUT',ident,'RANGE',a,b,'TOTAL',len(lines))
  for i in range(a,b+1):print(f'{i:4} {lines[i-1]}')
rec['end_utc']=datetime.datetime.now(datetime.timezone.utc).isoformat();rec['semantic_attestation']='Displayed complete indicated ranges and semantically read; identity-only reads separately labeled.'
(out/'reading-ledger.jsonl').open('a').write(json.dumps(rec,ensure_ascii=False)+'\n')
