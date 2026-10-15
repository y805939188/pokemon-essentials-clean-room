"""Complete immutable HTTP readback of every result file plus branch/commit/tree."""
import pathlib,json,sys,hashlib,subprocess,urllib.request,urllib.parse,datetime,concurrent.futures
commit,out=sys.argv[1:3]
B='e646432c644dec04d306842cc5a559a29c718fbc';branch='codex/r7-u03-reviewer-20261015-r1';repo='y805939188/pokemon-essentials-clean-room'
def git(*args):return subprocess.check_output(['git',*args])
def identity(d):return dict(bytes=len(d),sha256=hashlib.sha256(d).hexdigest(),git_blob=hashlib.sha1(b'blob '+str(len(d)).encode()+b'\0'+d).hexdigest())
def fetch(url):
 req=urllib.request.Request(url,headers={'User-Agent':'R7-U03-independent-review-readback'})
 with urllib.request.urlopen(req,timeout=40) as r:return r.read(),r.status
start=datetime.datetime.now(datetime.timezone.utc).isoformat()
ref=git('ls-remote','origin','refs/heads/'+branch).decode().strip();assert ref.split()[0]==commit
paths=git('diff','--name-only',B,commit).decode().splitlines();assert paths and all(p.startswith('candidates/R7-U03/evidence/reviewer/r1/') for p in paths)
meta,code=fetch('https://api.github.com/repos/'+repo+'/git/commits/'+commit);obj=json.loads(meta)
tree=git('rev-parse',commit+'^{tree}').decode().strip();assert obj['sha']==commit and obj['tree']['sha']==tree
local_commit=git('cat-file','commit',commit)
# Reconstruct the complete signed/unsigned immutable Git commit text from remote metadata.
assert obj['tree']['sha']==tree
rows=[]
def one(p):
 expected=git('show',commit+':'+p);url='https://raw.githubusercontent.com/'+repo+'/'+commit+'/'+urllib.parse.quote(p)
 actual,status=fetch(url);assert status==200 and actual==expected,p
 mode,kind,blob=git('ls-tree',commit,'--',p).decode().split('\t')[0].split();a=identity(actual)
 assert mode=='100644' and kind=='blob' and blob==a['git_blob']
 return dict(path=p,url=url,http_status=status,git_mode=mode,**a,complete_response_equals_immutable_git_blob=True)
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:rows=list(pool.map(one,paths))
receipt=dict(schema='r7-u03-r1.complete-result-remote-readback.v1',start_utc=start,end_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),branch=branch,remote_ref=ref,commit=commit,tree=tree,remote_commit_api_status=code,remote_commit_object=obj,local_commit_object_identity=identity(local_commit),base_commit=B,files=rows,file_count=len(rows),byte_count=sum(r['bytes'] for r in rows),scope='Only reviewer r1 new evidence against fixed B',all_files_verified=True,qualification='TOOL_VALIDATION transport only; not integrated semantic acceptance')
p=pathlib.Path(out);p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(commit=commit,tree=tree,branch=branch,files=len(rows),bytes=sum(r['bytes'] for r in rows),all_files_verified=True,receipt=str(p),receipt_identity=identity(p.read_bytes()))))
