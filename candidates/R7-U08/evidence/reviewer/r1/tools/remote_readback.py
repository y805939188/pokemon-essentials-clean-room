"""Read every published reviewer file from a fixed commit, independently of local blobs."""
import argparse,concurrent.futures,datetime,hashlib,json,pathlib,subprocess,time,urllib.request,urllib.parse,urllib.error
p=argparse.ArgumentParser();p.add_argument('--commit',required=True);p.add_argument('--output',required=True);a=p.parse_args()
W=pathlib.Path('/workspace/r7-u08-reviewer');B='e646432c644dec04d306842cc5a559a29c718fbc';branch='codex/r7-u08-reviewer-20261015-r1';prefix='candidates/R7-U08/evidence/reviewer/r1/'
assert len(a.commit)==40 and all(c in '0123456789abcdef' for c in a.commit)
def utc():return datetime.datetime.now(datetime.timezone.utc).isoformat()
def call(argv,cwd=None):
 s=utc();p=subprocess.Popen(argv,cwd=cwd,stdout=subprocess.PIPE,stderr=subprocess.PIPE);out,err=p.communicate();r={'argv':argv,'cwd':str(cwd) if cwd else None,'pid':p.pid,'start_utc':s,'end_utc':utc(),'exit_code':p.returncode,'stdout':out.decode(),'stderr':err.decode()};assert p.returncode==0,r;return out,r
def git(*x):return subprocess.check_output(['git','-C',str(W),*x])
start=utc();remote,ls=call(['git','-C',str(W),'ls-remote','--heads','origin',branch]);assert remote.decode().split()[0]==a.commit
receiver=pathlib.Path('/workspace/r7-u08-published-readback')/a.commit
assert not receiver.exists();receiver.parent.mkdir(exist_ok=True)
_,init=call(['git','init','--bare',str(receiver)])
_,fetch=call(['git','-C',str(receiver),'-c','protocol.version=2','fetch','--depth=1','--filter=blob:none','https://github.com/y805939188/pokemon-essentials-clean-room.git',a.commit])
remote_commit,rc=call(['git','-C',str(receiver),'rev-parse','FETCH_HEAD']);assert remote_commit.decode().strip()==a.commit
remote_tree,rt=call(['git','-C',str(receiver),'rev-parse',a.commit+'^{tree}']);tree=git('rev-parse',a.commit+'^{tree}').decode().strip();assert remote_tree.decode().strip()==tree
names=git('diff','--name-only','--no-renames','-z',B,a.commit).decode().split('\0');names=[x for x in names if x];assert all(x.startswith(prefix) for x in names)
rows=[]
for path in names:
 b=git('show',a.commit+':'+path);entry=git('ls-tree',a.commit,'--',path).decode().split();assert entry[0]=='100644' and entry[1]=='blob'
 rows.append({'path':path,'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'git_blob':entry[2],'mode':entry[0]})
def read(row):
 url='https://raw.githubusercontent.com/y805939188/pokemon-essentials-clean-room/'+a.commit+'/'+urllib.parse.quote(row['path']);attempts=[]
 for n in range(1,4):
  begin=utc()
  try:
   with urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'R7-U08-independent-result-readback'}),timeout=40) as response:b=response.read(row['bytes']+1);status=response.status
   actual={'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'git_blob':hashlib.sha1(f'blob {len(b)}\0'.encode()+b).hexdigest()}
   assert all(actual[k]==row[k] for k in actual),(row,actual)
   attempts.append({'attempt':n,'start_utc':begin,'end_utc':utc(),'http_status':status,'identity_match':True});return {**row,'url':url,'attempts':attempts,'all_bytes_match':True}
  except (urllib.error.URLError,TimeoutError) as e:
   attempts.append({'attempt':n,'start_utc':begin,'end_utc':utc(),'error':str(e)})
   if n==3:raise
   time.sleep(n)
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:results=list(pool.map(read,rows))
d={'schema':'r7.u08.complete-review-result-remote-readback.v1','start_utc':start,'end_utc':utc(),'branch':branch,'commit':a.commit,'tree':tree,'base':B,'remote_git_tool_io':[ls,init,fetch,rc,rt],'files':results,'files_verified':len(results),'bytes_verified':sum(x['bytes'] for x in results),'status':'COMPLETE_REMOTE_BYTES_TREE_VERIFIED','qualification':'Independent fresh remote Git commit/tree plus full immutable raw bytes for every result diff path; TOOL_VALIDATION only; no semantic/runtime/integration credit.'}
out=pathlib.Path(a.output);assert not out.exists();out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:d[k] for k in ['status','branch','commit','tree','files_verified','bytes_verified']},indent=2));print('receipt_sha256',hashlib.sha256(out.read_bytes()).hexdigest());print('receipt_path',str(out))
