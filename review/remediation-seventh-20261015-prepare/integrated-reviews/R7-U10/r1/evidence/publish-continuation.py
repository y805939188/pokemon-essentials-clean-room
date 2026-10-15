"""Ordinary fast-forward publication and complete immutable remote byte readback."""
from pathlib import Path
import subprocess,json,datetime,hashlib,os,urllib.request,urllib.error,concurrent.futures,time
ROOT=Path('/workspace/r7-ir-R7-U10-wave3');REPO=ROOT/'result-checkout'
OUT=ROOT/'continuation-remote-readback';OUT.mkdir(exist_ok=True)
BRANCH='codex/r7-ir-u10-20261015-r1'
PREFIX='review/remediation-seventh-20261015-prepare/integrated-reviews/R7-U10/r1/'
B='e646432c644dec04d306842cc5a559a29c718fbc'
OLD='4188ee2bfb8e4b6f3c5ac2c8e8be24384f93d0f4'
def utc():return datetime.datetime.now(datetime.timezone.utc).isoformat()
def ident(b):return {'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'git_blob':hashlib.sha1(f'blob {len(b)}\0'.encode()+b).hexdigest()}
log=[]
def git(*args):
    t=utc();p=subprocess.Popen(['git','-C',str(REPO),*args],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    out,err=p.communicate()
    log.append({'argv':['git',*args],'cwd':str(REPO),'start_utc':t,'end_utc':utc(),'child_pid':p.pid,'returncode':p.returncode,'stdout':out.decode(errors='replace'),'stderr':err.decode(errors='replace')})
    (OUT/'git-commands.json').write_text(json.dumps({'pid':os.getpid(),'commands':log},ensure_ascii=False,indent=2)+'\n')
    if p.returncode:raise RuntimeError('Git failed: '+str(args))
    return out
assert git('branch','--show-current').decode().strip()==BRANCH
assert git('rev-parse','HEAD').decode().strip()==OLD
assert git('show','-s','--format=%P',OLD).decode().strip()==B
existing=git('ls-remote','--heads','origin',BRANCH).decode().split()[0]
assert existing==OLD,'Remote advanced: do not overwrite another result'
status=git('status','--porcelain','-z').split(b'\0')
assert all(x[3:].decode().startswith(PREFIX) for x in status if x)
git('add','--',PREFIX)
staged=git('diff','--cached','--name-only').decode().splitlines();assert staged and all(x.startswith(PREFIX) for x in staged)
git('diff','--cached','--check')
git('commit','-m','Complete R7 U10 actual integration review; preserve initial WAIT')
sha=git('rev-parse','HEAD').decode().strip();tree=git('rev-parse','HEAD^{tree}').decode().strip()
assert git('show','-s','--format=%P','HEAD').decode().strip()==OLD
assert git('status','--porcelain')==b''
paths=git('diff','--name-only',B,sha).decode().splitlines();assert all(x.startswith(PREFIX) for x in paths)
assert git('ls-remote','--heads','origin',BRANCH).decode().split()[0]==OLD
git('push','origin','HEAD:refs/heads/'+BRANCH)
before=git('ls-remote','--heads','origin',BRANCH).decode().split()[0];assert before==sha
git('fetch','--no-tags','origin','refs/heads/'+BRANCH+':refs/remotes/origin/'+BRANCH)
assert git('rev-parse','refs/remotes/origin/'+BRANCH).decode().strip()==sha
assert git('rev-parse','refs/remotes/origin/'+BRANCH+'^{tree}').decode().strip()==tree
rows=[]
for entry in git('ls-tree','-r','-z',sha,'--',PREFIX).split(b'\0'):
    if not entry:continue
    head,p=entry.split(b'\t');mode,kind,blob=head.decode().split();path=p.decode()
    assert mode=='100644' and kind=='blob'
    local=(REPO/path).read_bytes();assert ident(local)['git_blob']==blob
    rows.append({'path':path,'expected':ident(local),'mode':mode})
assert sorted(paths)==sorted(x['path'] for x in rows)
def fetch(row):
    path=row['path'];url='https://raw.githubusercontent.com/y805939188/pokemon-essentials-clean-room/'+sha+'/'+path;attempts=[]
    for n in range(1,4):
        t=utc()
        try:
            with urllib.request.urlopen(url,timeout=40) as r:body=r.read();code=r.status
            assert ident(body)==row['expected'],path
            dest=OUT/'files'/path;dest.parent.mkdir(parents=True,exist_ok=True);dest.write_bytes(body)
            attempts.append({'attempt':n,'start_utc':t,'end_utc':utc(),'http_status':code,'complete_response_body':True})
            return {'path':path,'url':url,**ident(body),'mode':row['mode'],'matches_local_and_actual_git_blob':True,'attempts':attempts}
        except urllib.error.HTTPError as e:
            body=e.read();dest=OUT/'failed'/path/(str(n)+'.body');dest.parent.mkdir(parents=True,exist_ok=True);dest.write_bytes(body)
            attempts.append({'attempt':n,'start_utc':t,'end_utc':utc(),'http_status':e.code,'failed_body_identity':ident(body)})
            if n==3 or e.code not in [404,429,500,502,503,504]:raise
            time.sleep(n)
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:results=list(pool.map(fetch,rows))
manifest=json.loads((REPO/PREFIX/'artifact-manifest.json').read_text())
by_path={r['path']:r for r in results}
for r in manifest['files']:assert all(by_path[r['path']][k]==r[k] for k in ['bytes','sha256','git_blob'])
after=git('ls-remote','--heads','origin',BRANCH).decode().split()[0];assert before==after==sha
result={'schema':'r7.u10.continuation-complete-remote-readback.v1','utc':utc(),'pid':os.getpid(),'branch':BRANCH,'commit':sha,'tree':tree,'base':B,'parent':OLD,'initial_WAIT_preserved_as_parent':True,'ordinary_fast_forward_push':True,'remote_ref_before_readback':before,'remote_ref_after_readback':after,'remote_fetched_tree_verified':True,'all_result_paths_within_authorized_prefix':True,'file_count':len(results),'total_bytes':sum(r['bytes'] for r in results),'files':results,'all_manifest_declarations_verified':True,'manifest_itself_bound_by_actual_commit_tree_and_full_remote_body':True,'worktree_clean':git('status','--porcelain')==b'','verdicts':{i:'PASS_SCOPED_ACTUAL_INTEGRATION' for i in ['GR7-M15-001','GR7-M15-002','GR7-M17-001']},'ACCEPTED':False,'CLOSED':False,'readback_is_transport_evidence_only':True}
(OUT/'complete-remote-readback.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:result[k] for k in ['branch','commit','tree','parent','file_count','total_bytes','worktree_clean','verdicts']},ensure_ascii=False))
for r in results:print(json.dumps({k:r[k] for k in ['path','bytes','sha256','git_blob']},ensure_ascii=False))
