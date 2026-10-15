"""Normal authorized evidence-only publication and exhaustive remote readback."""
import pathlib,subprocess,json,os,datetime,hashlib,urllib.request,urllib.parse,concurrent.futures,time,sys
R=pathlib.Path('/workspace/r7-ir-R7-U07-wave3');REPO=R/'result';PREFIX='review/remediation-seventh-20261015-prepare/integrated-reviews/R7-U07/r1/';BRANCH='codex/r7-ir-u07-20261015-r1';B='e646432c644dec04d306842cc5a559a29c718fbc'
phase=sys.argv[1];receipt={'phase':phase,'start_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'launcher_pid':os.getpid(),'commands':[],'files':[]}
outpath=R/('publication-'+phase+'.json')
def save():outpath.write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n')
def run(args):
 start=datetime.datetime.now(datetime.timezone.utc).isoformat();p=subprocess.Popen(args,cwd=REPO,stdout=subprocess.PIPE,stderr=subprocess.PIPE);o,e=p.communicate();receipt['commands'].append({'argv':args,'cwd':str(REPO),'start_utc':start,'end_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'pid':p.pid,'exit':p.returncode,'stdout':o.decode(),'stderr':e.decode()});save();assert p.returncode==0,(args,e.decode());return o
def git(*args):return run(['git',*args])
def identity(d):return {'bytes':len(d),'sha256':hashlib.sha256(d).hexdigest(),'git_blob':hashlib.sha1(('blob '+str(len(d))+'\0').encode()+d).hexdigest()}
def remote():return git('ls-remote','--heads','origin','refs/heads/'+BRANCH).decode().strip()
try:
 assert git('branch','--show-current').decode().strip()==BRANCH
 old=git('rev-parse','HEAD').decode().strip();before=remote();receipt['previous_local_commit']=old;receipt['remote_before_commit']=before
 if phase=='payload':assert old==B and before==''
 elif phase=='envelope':assert before.split()[0]==old
 else:raise ValueError(phase)
 others=git('ls-files','--others','--exclude-standard','-z').decode().strip('\0').split('\0');assert all(not p or p.startswith(PREFIX) for p in others)
 git('add','--',PREFIX)
 staged=git('diff','--cached','--name-only','-z').decode().strip('\0').split('\0');assert staged and all(p.startswith(PREFIX) for p in staged)
 git('diff','--cached','--check')
 git('commit','-m','review: independently assess R7-U07 actual integration' if phase=='payload' else 'review: attach R7-U07 verified publication receipt')
 commit=git('rev-parse','HEAD').decode().strip();tree=git('rev-parse','HEAD^{tree}').decode().strip();receipt.update(commit=commit,tree=tree,branch=BRANCH)
 paths=git('diff','--name-only','-z',B,commit).decode().strip('\0').split('\0');assert paths and all(p.startswith(PREFIX) for p in paths)
 for p in paths:assert git('diff','--name-status',B,commit,'--',p).decode().startswith('A\t')
 print(json.dumps({'phase':phase,'commit':commit,'tree':tree,'files':len(paths),'action':'normal push then full HTTP readback'}),flush=True)
 git('push','origin','HEAD:refs/heads/'+BRANCH)
 rb_before=remote();assert rb_before.split()[0]==commit;receipt['remote_before_readback']=rb_before
 def fetch(p):
  url=f'https://raw.githubusercontent.com/y805939188/pokemon-essentials-clean-room/{commit}/{urllib.parse.quote(p)}';attempts=[]
  for attempt in range(1,6):
   t=datetime.datetime.now(datetime.timezone.utc).isoformat()
   try:
    with urllib.request.urlopen(url,timeout=45) as resp:d=resp.read();status=resp.status
    local=(REPO/p).read_bytes();expected=subprocess.check_output(['git','-C',str(REPO),'show',commit+':'+p]);assert d==local==expected
    return {'path':p,'url':url,'http_status':status,'start_utc':t,'end_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'response_read':'COMPLETE','expected':identity(expected),'actual':identity(d),'full_bytes_equal':True,'prior_attempts':attempts}
   except Exception as exc:
    attempts.append({'attempt':attempt,'utc':t,'error':repr(exc)})
    if attempt==5:raise
    time.sleep(2)
 with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
  futures=[pool.submit(fetch,p) for p in paths]
  for f in futures:receipt['files'].append(f.result());save()
 rb_after=remote();assert rb_after.split()[0]==commit;receipt['remote_after_readback']=rb_after
 manifest=json.loads((REPO/PREFIX/'artifact-manifest.json').read_text())
 assert {x['path'] for x in manifest['files']}==set(paths)-{PREFIX+'artifact-manifest.json'}
 for x in manifest['files']:assert identity((REPO/x['path']).read_bytes())=={k:x[k] for k in ['bytes','sha256','git_blob']}
 assert git('rev-parse','HEAD:deliverables/final-specification-set').decode().strip()=='ebbe29f2bc88cd17de7072bf440c6fa8c8c7089c'
 assert git('status','--porcelain').decode()==''
 receipt.update(result='ALL_FULL_REMOTE_BYTES_MATCH',file_count=len(paths),bytes=sum(x['actual']['bytes'] for x in receipt['files']),end_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),qualification='Publication only. No acceptance/closure or runtime evidence. Receipt itself is external to the commit it describes, preventing self-reference.');save()
 print(json.dumps({k:receipt[k] for k in ['phase','commit','tree','branch','result','file_count','bytes']},ensure_ascii=False),flush=True)
except Exception as exc:
 receipt.update(result='FAILED',error=repr(exc),end_utc=datetime.datetime.now(datetime.timezone.utc).isoformat());save();raise
