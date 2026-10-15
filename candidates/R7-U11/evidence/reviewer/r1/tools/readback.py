"""Read every published reviewer file through immutable raw HTTPS and Git tree."""
import concurrent.futures,datetime,hashlib,json,pathlib,subprocess,sys,time,urllib.request,urllib.error
repo=pathlib.Path('/workspace/r7-u11-reviewer-checkout');branch='codex/r7-u11-reviewer-20261015-r1';prefix='candidates/R7-U11/evidence/reviewer/r1/';B='e646432c644dec04d306842cc5a559a29c718fbc'
def now():return datetime.datetime.now(datetime.timezone.utc).isoformat()
def git(*a):return subprocess.check_output(['git',*a],cwd=repo)
def ident(b):return {'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'git_blob':hashlib.sha1(f'blob {len(b)}\0'.encode()+b).hexdigest()}
start=now();sha=git('rev-parse','HEAD').decode().strip();tree=git('rev-parse',sha+'^{tree}').decode().strip();remote=git('ls-remote','--heads','origin','refs/heads/'+branch).decode();assert remote.split()[0]==sha
p=subprocess.run(['git','fetch','--no-tags','origin','refs/heads/'+branch],cwd=repo,stdout=subprocess.PIPE,stderr=subprocess.PIPE);assert p.returncode==0;assert git('rev-parse','FETCH_HEAD').decode().strip()==sha
changes=[s.split('\t') for s in git('diff','--name-status',B,sha).decode().splitlines()];assert all(s=='A' and path.startswith(prefix) for s,path in changes)
paths=[path for s,path in changes];assert sorted(paths)==sorted(git('ls-tree','-r','--name-only',sha,'--',prefix).decode().splitlines())
def fetch(path):
 local=git('show',sha+':'+path);mode,typ,blob,_=git('ls-tree',sha,'--',path).decode().strip().split(maxsplit=3);assert mode=='100644' and typ=='blob';url='https://raw.githubusercontent.com/y805939188/pokemon-essentials-clean-room/'+sha+'/'+path;attempts=[]
 for n in range(1,4):
  t=now()
  try:
   with urllib.request.urlopen(url,timeout=40) as resp:data=resp.read(len(local)+1);status=resp.status
   assert data==local,path;actual=ident(data);assert actual['git_blob']==blob
   attempts.append({'attempt':n,'start_utc':t,'end_utc':now(),'http_status':status,'complete_byte_match':True});return {'path':path,**actual,'git_mode':mode,'url':url,'attempts':attempts,'complete_remote_read':True}
  except (urllib.error.URLError,TimeoutError) as e:
   attempts.append({'attempt':n,'start_utc':t,'end_utc':now(),'error':str(e)})
   if n==3:raise
   time.sleep(n)
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:rows=list(pool.map(fetch,paths))
r={'schema':'r7.u11.reviewer-complete-remote-readback.v1','start_utc':start,'end_utc':now(),'branch':branch,'commit':sha,'tree':tree,'remote_ref_output':remote,'git_fetch':{'exit_code':p.returncode,'stdout':p.stdout.decode(),'stderr':p.stderr.decode()},'changed_files':changes,'files':rows,'files_verified':len(rows),'bytes_verified':sum(r['bytes'] for r in rows),'outside_write_scope':[],'every_remote_file_matches_commit_blob_and_mode':True,'qualification':'Actual complete immutable HTTP response body of every new evidence file plus remote ref and Git tree. No candidate behavior or formal integration credit.'}
p=pathlib.Path(sys.argv[1]);p.parent.mkdir(parents=True,exist_ok=True)
with p.open('x') as f:json.dump(r,f,ensure_ascii=False,indent=2);f.write('\n')
print(json.dumps({'branch':branch,'commit':sha,'tree':tree,'files_verified':len(rows),'bytes_verified':r['bytes_verified'],'every_remote_file_matches_commit_blob_and_mode':True,'receipt':str(p),'receipt_identity':ident(p.read_bytes())}))
