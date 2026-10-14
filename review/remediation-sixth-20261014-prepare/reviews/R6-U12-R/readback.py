"""Full raw-HTTPS payload comparison with remote Git tree/commit metadata."""
import concurrent.futures,datetime,hashlib,json,subprocess,sys,time,urllib.request,urllib.parse
from pathlib import Path
commit,prefix,output=sys.argv[1:4];prefix=prefix.rstrip('/');repo='y805939188/pokemon-essentials-clean-room'
def utc():return datetime.datetime.now(datetime.timezone.utc).isoformat()
def git(*args):return subprocess.check_output(['git',*args])
def fetch(url):
 req=urllib.request.Request(url,headers={'User-Agent':'R6-U12-R-byte-review'})
 with urllib.request.urlopen(req,timeout=45) as f:return f.status,f.read()
def ident(data):return {'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest(),'git_blob':hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()}
t0=utc();tree=git('rev-parse',commit+'^{tree}').decode().strip();subtree=git('rev-parse',commit+':'+prefix).decode().strip()
binding_path=sys.argv[4] if len(sys.argv)>4 else '-'
bindings=json.loads(Path(binding_path).read_text() if binding_path!='-' else sys.stdin.read())
remote_commit=next(x['payload'] for x in bindings['records'] if x['payload'].get('sha')==commit)
assert remote_commit['sha']==commit and remote_commit['tree']['sha']==tree
remote_tree=next(x['payload'] for x in bindings['records'] if x['payload'].get('sha')==subtree)
assert remote_tree['sha']==subtree and not remote_tree['truncated']
entries=[x for x in remote_tree['tree'] if x['type']=='blob'];local=git('ls-tree','-r',commit,'--',prefix).decode().splitlines();assert len(entries)==len(local)
by={prefix+'/'+x['path']:x for x in entries}
def read(line):
 meta,path=line.split('\t',1);mode,typ,blob=meta.split();remote=by[path];assert (mode,typ,blob)==(remote['mode'],remote['type'],remote['sha']);data=git('show',commit+':'+path);expected=ident(data);assert expected['git_blob']==blob
 attempts=[]
 for n in range(1,4):
  a=utc()
  try:
   http,got=fetch('https://raw.githubusercontent.com/'+repo+'/'+commit+'/'+urllib.parse.quote(path));actual=ident(got);match=got==data and actual==expected;attempts.append({'number':n,'start_utc':a,'end_utc':utc(),'http_status':http,'status':'MATCH_FULL_BYTES' if match else 'MISMATCH'})
   assert match,(path,actual,expected)
   return dict(expected,path=path,mode=mode,type=typ,commit=commit,attempts=attempts,status='REMOTE_FULL_PAYLOAD_MATCH')
  except Exception as e:
   attempts.append({'number':n,'start_utc':a,'end_utc':utc(),'error':str(e)})
   if n==3:return dict(expected,path=path,mode=mode,type=typ,commit=commit,attempts=attempts,status='FAIL')
   time.sleep(.5)
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:records=list(pool.map(read,local))
result={'kind':'REMOTE_FULL_PAYLOAD_READBACK_TOOL_VALIDATION','argv':sys.argv,'cwd':str(Path.cwd()),'start_utc':t0,'end_utc':utc(),'commit':commit,'tree':tree,'directory':prefix,'directory_tree':subtree,'remote_commit_tree_binding':'GitHub connector fetched exact remote Git commit and directory tree, truncated=false; full raw HTTPS payloads independently matched','payload_count':len(records),'bytes':sum(x['bytes'] for x in records),'records':records,'complete':all(x['status']=='REMOTE_FULL_PAYLOAD_MATCH' for x in records),'source_execution':0}
if output!='-':Path(output).write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:result[k] for k in ['kind','commit','tree','directory_tree','payload_count','bytes','complete','start_utc','end_utc']},ensure_ascii=False))
if output=='-':print('RECORDS_SHA256 '+hashlib.sha256(json.dumps(records,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode()).hexdigest())
assert result['complete']
