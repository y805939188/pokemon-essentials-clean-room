"""Complete remote HTTP bytes plus independently fetched Git objects for one fixed result."""
import json,hashlib,subprocess,datetime,os,sys,urllib.request,urllib.parse
from pathlib import Path
PREFIX='review/remediation-seventh-20261015-prepare/integrated-reviews/R7-U08/r1/';B='e646432c644dec04d306842cc5a559a29c718fbc';BRANCH='codex/r7-ir-u08-20261015-r1';REPO='https://github.com/y805939188/pokemon-essentials-clean-room.git'
commit,repo_dir,receipt_path=sys.argv[1:];repo_dir=Path(repo_dir);receipt_path=Path(receipt_path);start=datetime.datetime.now(datetime.timezone.utc).isoformat()
def git(*args,remote=False):return subprocess.check_output(['git',*(['-C',str(repo_dir)] if remote else []),*args],stderr=subprocess.PIPE)
def ident(b):return {'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'git_blob':hashlib.sha1(f'blob {len(b)}\0'.encode()+b).hexdigest()}
remote_ref=git('ls-remote','--heads',REPO,'refs/heads/'+BRANCH).decode().split();assert remote_ref==[commit,'refs/heads/'+BRANCH],remote_ref
assert not repo_dir.exists(),repo_dir
git('init','--bare',str(repo_dir));git('remote','add','origin',REPO,remote=True)
git('config','remote.origin.promisor','true',remote=True);git('config','remote.origin.partialclonefilter','blob:none',remote=True)
git('fetch','--depth=1','--filter=blob:none','--no-tags','origin',commit,remote=True)
tree=git('rev-parse',commit+'^{tree}',remote=True).decode().strip();assert tree==git('rev-parse',commit+'^{tree}').decode().strip()
formal=git('rev-parse',commit+':deliverables/final-specification-set',remote=True).decode().strip();assert formal=='ebbe29f2bc88cd17de7072bf440c6fa8c8c7089c'
changed=git('diff','--name-only',B,commit).decode().splitlines();assert changed and all(p.startswith(PREFIX) for p in changed)
entries=git('ls-tree','-r','-z',commit,'--',PREFIX,remote=True).split(b'\0');rows=[]
for entry in entries:
 if not entry:continue
 meta,path=entry.split(b'\t',1);mode,kind,blob=meta.decode().split();path=path.decode();assert mode=='100644' and kind=='blob'
 expected=git('show',commit+':'+path);remote_bytes=git('show',commit+':'+path,remote=True);assert remote_bytes==expected
 url='https://raw.githubusercontent.com/y805939188/pokemon-essentials-clean-room/'+commit+'/'+urllib.parse.quote(path,safe='/')
 t=datetime.datetime.now(datetime.timezone.utc).isoformat()
 with urllib.request.urlopen(url,timeout=60) as response:b=response.read();status=response.status;resolved=response.url
 assert b==expected and ident(b)['git_blob']==blob
 rows.append({'path':path,'mode':mode,'tree_blob':blob,**ident(b),'http_status':status,'url':url,'resolved_url':resolved,'read_utc':t,'remote_git_bytes':'EXACT_MATCH','remote_HTTP_bytes':'EXACT_MATCH'})
assert {x['path'] for x in rows}==set(changed)
m=json.loads(git('show',commit+':'+PREFIX+'artifact-manifest.json'));assert len(rows)==len(m['files'])+1
for f in m['files']:
 row=next(x for x in rows if x['path']==PREFIX+f['path']);assert all(row[k]==f[k] for k in ['bytes','sha256','git_blob'])
receipt={'schema':'r7.u08.complete-remote-readback.v1','start_utc':start,'end_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'tool_pid':os.getpid(),'branch':BRANCH,'remote_ref_commit':commit,'commit':commit,'tree':tree,'formal_subtree':formal,'base_B':B,'independent_bare_fetch_directory':str(repo_dir),'files':rows,'file_count':len(rows),'total_bytes':sum(x['bytes'] for x in rows),'all_files_verified':True,'complete_HTTP_and_independent_Git_readback':'MATCH','exclusive_write_scope':PREFIX,'semantic_PASS_from_tool':False,'behavior_execution_credit':False,'configuration_credit':False,'self_qualification':'Receipt stored outside the commit being verified; no recursive self-hash claim.'}
receipt_path.parent.mkdir(parents=True,exist_ok=True);receipt_path.write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n');print(json.dumps({k:v for k,v in receipt.items() if k!='files'},ensure_ascii=False))
