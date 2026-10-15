import json,subprocess,datetime,os,hashlib,urllib.request,urllib.parse,sys
from pathlib import Path
root=Path('/workspace/r7-ir-R7-U03-final');wt=root/'review-worktree';prefix='review/remediation-seventh-20261015-prepare/integrated-reviews/R7-U03/r1/';branch='codex/r7-ir-u03-20261015-r1';B='e646432c644dec04d306842cc5a559a29c718fbc';dst=wt/prefix
logdir=root/'publication';logdir.mkdir(exist_ok=True);records=[]
def ident(b):return dict(bytes=len(b),sha256=hashlib.sha256(b).hexdigest(),git_blob=hashlib.sha1(f'blob {len(b)}\0'.encode()+b).hexdigest())
def run(label,args):
 start=datetime.datetime.now(datetime.timezone.utc).isoformat();p=subprocess.Popen(args,cwd=wt,stdout=subprocess.PIPE,stderr=subprocess.PIPE);out,err=p.communicate();rec=dict(label=label,argv=args,cwd=str(wt),wrapper_pid=os.getpid(),tool_pid=p.pid,start_utc=start,end_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),exit_code=p.returncode,stdout=out.decode(),stderr=err.decode());records.append(rec)
 (logdir/(sys.argv[1]+'-commands.json')).write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n')
 assert p.returncode==0,(label,p.returncode,err.decode());return out
def manifest():
 rows=[]
 for p in sorted(dst.rglob('*')):
  if p.is_file() and p.name!='artifact-manifest.json':rows.append(dict(path=str(p.relative_to(wt)),git_mode='100644',**ident(p.read_bytes())))
 (dst/'artifact-manifest.json').write_text(json.dumps(dict(schema='r7-u03-ir-r1.artifact-manifest.v1',branch=branch,base_commit=B,allowed_prefix=prefix,files=rows,nonself_file_count=len(rows),nonself_bytes=sum(x['bytes'] for x in rows),self_binding='Manifest identity and complete final path universe bound externally by actual commit/tree and full immutable remote readback; no recursive self hash.'),ensure_ascii=False,indent=2)+'\n')
def validate():
 for p in dst.rglob('*.json'):json.loads(p.read_text())
 d=json.loads((dst/'per-id.json').read_text());assert [r['verdict'] for r in d['records']]==['PASS_SCOPED_ACTUAL_INTEGRATION']*2
 assert d['reviewer']['AI_subtasks_created']==0 and d['reviewer']['auth_and_quota_queries']==0
 m=json.loads((dst/'artifact-manifest.json').read_text());expected={r['path'] for r in m['files']}|{prefix+'artifact-manifest.json'};actual={str(p.relative_to(wt)) for p in dst.rglob('*') if p.is_file()};assert expected==actual
 for r in m['files']:assert ident((wt/r['path']).read_bytes())=={k:r[k] for k in ['bytes','sha256','git_blob']}
 assert run('branch',['git','branch','--show-current']).decode().strip()==branch
 changes=run('working-changes',['git','status','--porcelain','--untracked-files=all']).decode().splitlines();assert changes and all(x[3:].startswith(prefix) for x in changes)
def publish(message):
 manifest();validate();run('stage',['git','add','--',prefix]);cached=run('staged-paths',['git','diff','--cached','--name-status']).decode().splitlines();assert cached and all(x.startswith('A\t'+prefix) or x.startswith('M\t'+prefix) for x in cached)
 # Raw historical I/O and original input snapshots retain their exact bytes.
 run('authored-whitespace',['git','diff','--cached','--check','--',prefix+'report.md',prefix+'per-id.json',prefix+'review-input-receipt.json',prefix+'artifact-manifest.json',prefix+'evidence/tools'])
 run('commit',['git','commit','-m',message]);commit=run('commit-id',['git','rev-parse','HEAD']).decode().strip();tree=run('tree-id',['git','rev-parse','HEAD^{tree}']).decode().strip()
 changes=run('complete-result-scope',['git','diff','--name-status',B,commit]).decode().splitlines();assert all(x.startswith('A\t'+prefix) for x in changes)
 run('push',['git','push','origin','HEAD:refs/heads/'+branch]);print(json.dumps(dict(commit=commit,tree=tree,branch=branch,files=len(changes))))
def readback():
 commit=run('local-head',['git','rev-parse','HEAD']).decode().strip();before=run('remote-ref-before',['git','ls-remote','--heads','origin','refs/heads/'+branch]).decode().split();assert before[0]==commit
 run('fetch-exact-result',['git','fetch','--no-tags','origin','refs/heads/'+branch]);remote=run('remote-head',['git','rev-parse','FETCH_HEAD']).decode().strip();assert remote==commit
 tree=run('remote-tree',['git','rev-parse',remote+'^{tree}']).decode().strip();diff=run('remote-result-diff',['git','diff','--name-status',B,remote]).decode().splitlines();assert diff and all(x.startswith('A\t'+prefix) for x in diff)
 rows=[]
 for change in diff:
  path=change.split('\t')[1];stored=run('blob-'+str(len(rows)),['git','show',remote+':'+path]);assert stored==(wt/path).read_bytes();url='https://raw.githubusercontent.com/y805939188/pokemon-essentials-clean-room/'+remote+'/'+urllib.parse.quote(path);start=datetime.datetime.now(datetime.timezone.utc).isoformat()
  with urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'R7-U03-independent-review-readback'}),timeout=60) as response:
   body=response.read();status=response.status;length=response.headers.get('Content-Length')
  assert status==200 and body==stored
  if length is not None:assert int(length)==len(body)
  mode=run('mode-'+str(len(rows)),['git','ls-tree',remote,'--',path]).decode().split()[0];assert mode=='100644'
  rows.append(dict(path=path,url=url,http_status=status,content_length=length,complete_response_body_read=True,start_utc=start,end_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),tool_pid=os.getpid(),git_mode=mode,**ident(body)))
  (logdir/(sys.argv[1]+'-readback.json')).write_text(json.dumps(dict(commit=commit,tree=tree,branch=branch,files=rows,file_count=len(rows),bytes=sum(r['bytes'] for r in rows),complete=False),ensure_ascii=False,indent=2)+'\n')
 after=run('remote-ref-after',['git','ls-remote','--heads','origin','refs/heads/'+branch]).decode().split();assert after[0]==commit
 result=dict(commit=commit,tree=tree,branch=branch,files=rows,file_count=len(rows),bytes=sum(r['bytes'] for r in rows),complete=True,remote_ref_stable=True,qualification='Every full HTTP response body equals local bytes and immutable fetched Git blob; path universe, tree and 100644 modes checked. Transport only.')
 (logdir/(sys.argv[1]+'-readback.json')).write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n');print(json.dumps({k:v for k,v in result.items() if k!='files'}))
if sys.argv[1]=='manifest':manifest();print('manifest built')
elif sys.argv[1]=='publish':publish(sys.argv[2])
elif sys.argv[1] in ['readback-content','readback-final']:readback()
else:raise ValueError(sys.argv[1])
