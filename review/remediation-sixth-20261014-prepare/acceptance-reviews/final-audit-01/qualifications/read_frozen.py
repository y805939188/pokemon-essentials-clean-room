import sys,subprocess,hashlib,json,datetime
from pathlib import Path
BASE=Path(__file__).resolve().parent;loc=sys.argv[1];mode=sys.argv[2] if len(sys.argv)>2 else 'text'
t0=datetime.datetime.now(datetime.timezone.utc).isoformat();r=subprocess.run(['git','show',loc],stdout=subprocess.PIPE,stderr=subprocess.PIPE);t1=datetime.datetime.now(datetime.timezone.utc).isoformat()
if r.returncode: raise RuntimeError(r.stderr.decode())
b=r.stdout;lines=b.decode().splitlines();rec={'locator':loc,'bytes':len(b),'lines':len(lines),'sha256':hashlib.sha256(b).hexdigest(),'git_blob':hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest(),'argv':sys.argv,'cwd':str(Path.cwd()),'start_utc':t0,'end_utc':t1,'git_show_exit':r.returncode,'git_show_stderr':r.stderr.decode(),'source_or_author_execution':False}
if mode=='text':
 lo=int(sys.argv[3]) if len(sys.argv)>3 else 1;hi=int(sys.argv[4]) if len(sys.argv)>4 else len(lines);hi=hi or len(lines);assert 1<=lo<=hi<=len(lines);rec['range']=[lo,hi];output='\n'.join(f'{n+1}: {lines[n]}' for n in range(lo-1,hi))
elif mode.startswith('json'):
 x=json.loads(b)
 if mode=='json-general':y={k:v for k,v in x.items() if k!='required_mapping'};rec['pointers']=['/'+k for k in y]
 elif mode=='json-mapping-a':y=x['required_mapping'][:28];rec['pointers']=['/required_mapping/'+str(i) for i in range(28)]
 elif mode=='json-mapping-b':y=x['required_mapping'][28:];rec['pointers']=['/required_mapping/'+str(i) for i in range(28,len(x['required_mapping']))]
 else: raise ValueError(mode)
 output=json.dumps(y,ensure_ascii=False,separators=(',',':'))
else:raise ValueError(mode)
with (BASE/'reading-ledger.jsonl').open('a') as f:f.write(json.dumps(rec,ensure_ascii=False)+'\n')
print(json.dumps(rec,ensure_ascii=False));print(output)
