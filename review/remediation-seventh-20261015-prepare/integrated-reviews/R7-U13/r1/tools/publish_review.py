"""Ordinary authorized evidence-only publication and full immutable readback.

All command/readback outputs go outside the tree being committed, avoiding
self-modifying logs or a claim that a commit contains its own final attestation.
ThreadPoolExecutor handles ordinary HTTP I/O only; there are no AI/model calls.
"""
from pathlib import Path
import subprocess,json,datetime,os,sys,hashlib,urllib.request,urllib.parse,concurrent.futures,traceback
from run_logged import identity
W=Path('/workspace/r7-ir-R7-U13');repo=W/'checkout';E=Path(__file__).resolve().parent.parent
prefix=str(E.relative_to(repo))+'/';branch='codex/r7-ir-u13-20261015-r1';B='e646432c644dec04d306842cc5a559a29c718fbc'
stage=sys.argv[1];expected_remote=sys.argv[2];O=W/'publication'/stage;O.mkdir(parents=True,exist_ok=False)
def utc():return datetime.datetime.now(datetime.timezone.utc).isoformat()
def dump(p,d):p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
def run(label,*argv):
    start=utc();p=subprocess.Popen(argv,cwd=repo,stdout=subprocess.PIPE,stderr=subprocess.PIPE);a,b=p.communicate();end=utc()
    (O/(label+'.stdout')).write_bytes(a);(O/(label+'.stderr')).write_bytes(b)
    r={'label':label,'argv':list(argv),'cwd':str(repo),'pid':p.pid,'start_utc':start,'end_utc':end,'exit_code':p.returncode,'stdout':identity(a),'stderr':identity(b),'phase':'TOOL_VALIDATION / ordinary authorized publication only'}
    with (O/'commands.jsonl').open('a') as f:f.write(json.dumps(r,ensure_ascii=False)+'\n')
    if p.returncode:raise RuntimeError(label+' exited '+str(p.returncode))
    return a
def git(label,*args):return run(label,'git',*args)
def remote(label):
    d=git(label,'ls-remote','--heads','origin','refs/heads/'+branch).decode().strip()
    return d.split()[0] if d else None
receipt={'schema':'r7.u13.actual-ir.ordinary-publication.v1','stage':stage,'started_utc':utc(),'evidence_process_pid':os.getpid(),'branch':branch,'authorized_prefix':prefix,'files':[],'complete':False,'ACCEPTED':False,'CLOSED':False,'qualification':'Full response body read/identity verification, not browser/behavior/model configuration credit; this external receipt binds only its stated immutable commit.'}
try:
    assert git('branch','branch','--show-current').decode().strip()==branch
    r=remote('remote-before');assert r==(None if expected_remote=='absent' else expected_remote),(r,expected_remote)
    m=json.loads((E/'artifact-manifest.json').read_bytes());decl={r['path']:r for r in m['artifacts']}
    actual={str(p.relative_to(E)):p for p in E.rglob('*') if p.is_file() and p.name!='artifact-manifest.json'}
    assert set(actual)==set(decl),(set(actual)-set(decl),set(decl)-set(actual))
    for p,path in actual.items():
        assert not path.is_symlink()
        for k,v in identity(path.read_bytes()).items():assert decl[p][k]==v,(p,k)
    git('add','add','--',prefix)
    staged=git('staged-paths','diff','--cached','--name-only').decode().splitlines();assert staged and all(p.startswith(prefix) for p in staged)
    # Both checks are actual commands; full historical literal logs may have
    # whitespace. Restrict the required clean prose/code check explicitly.
    git('whitespace-new-work','diff','--cached','--check','--',prefix+'report.md',prefix+'per-id.json',prefix+'review-input-receipt.json',prefix+'artifact-manifest.json',prefix+'tools/*.py')
    git('commit','commit','-m','review: independently verify R7 U13 actual integration ('+stage+')')
    commit=git('commit-id','rev-parse','HEAD').decode().strip();tree=git('tree-id','rev-parse','HEAD^{tree}').decode().strip()
    assert git('formal-tree','rev-parse','HEAD:deliverables/final-specification-set').decode().strip()=='ebbe29f2bc88cd17de7072bf440c6fa8c8c7089c'
    allchanged=git('all-changed-paths','diff','--name-only',B,commit).decode().splitlines();assert all(p.startswith(prefix) for p in allchanged)
    git('push','push','origin','HEAD:refs/heads/'+branch)
    assert remote('remote-after-push')==commit
    git('fetch-published','fetch','--no-tags','origin',commit)
    assert git('remote-object-tree','rev-parse',commit+'^{tree}').decode().strip()==tree
    receipt.update(commit=commit,tree=tree,base=B,readback_remote_head_before=remote('readback-head-before'))
    assert receipt['readback_remote_head_before']==commit
    entries=[]
    for row in git('published-tree-files','ls-tree','-r','-z',commit,'--',prefix).split(b'\0'):
        if not row:continue
        meta,name=row.split(b'\t',1);mode,kind,blob=meta.decode().split();path=name.decode();assert mode=='100644' and kind=='blob'
        body=subprocess.check_output(['git','-C',str(repo),'show',commit+':'+path]);assert identity(body)['git_blob_content_id']==blob
        assert body==(repo/path).read_bytes()
        entries.append((path,mode,blob,body))
    def fetch_one(e):
        path,mode,blob,expected=e;url='https://raw.githubusercontent.com/y805939188/pokemon-essentials-clean-room/'+commit+'/'+urllib.parse.quote(path,safe='/')
        start=utc();req=urllib.request.Request(url,headers={'User-Agent':'R7-U13-fixed-evidence-readback'})
        with urllib.request.urlopen(req,timeout=45) as response:
            status=response.status;body=response.read();returned_url=response.url
        assert status==200 and body==expected,(path,status,len(body),len(expected))
        a=identity(body);assert a['git_blob_content_id']==blob
        dest=O/'readback-files'/path;dest.parent.mkdir(parents=True,exist_ok=True);dest.write_bytes(body)
        return {'path':path,'url':url,'returned_url':returned_url,'http_status':status,'start_utc':start,'end_utc':utc(),'response_body_complete':True,'mode_from_published_Git_tree':mode,'identity':a,'local_and_committed_bytes_equal':True,'stored_response':str(dest)}
    print(json.dumps({'stage':stage,'ordinary_push_commit':commit,'tree':tree,'files_to_read':len(entries)}),flush=True)
    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as pool:
        futures=[pool.submit(fetch_one,e) for e in entries]
        for f in concurrent.futures.as_completed(futures):
            receipt['files'].append(f.result())
            if len(receipt['files'])%50==0:print(json.dumps({'stage':stage,'complete_HTTP_bodies_verified':len(receipt['files'])}),flush=True)
    receipt['files'].sort(key=lambda x:x['path'])
    receipt['readback_remote_head_after']=remote('readback-head-after');assert receipt['readback_remote_head_after']==commit
    receipt['file_count']=len(entries);receipt['bytes']=sum(r['identity']['bytes'] for r in receipt['files']);receipt['complete']=True;receipt['completed_utc']=utc()
    assert len(receipt['files'])==len(entries)
    git('final-worktree-status','status','--porcelain=v1','--untracked-files=all')
    dump(O/'publication-and-full-readback.json',receipt)
    print(json.dumps({'commit':commit,'tree':tree,'branch':branch,'files':receipt['file_count'],'bytes':receipt['bytes'],'all_full_remote_bodies_match':True,'receipt':str(O/'publication-and-full-readback.json')},ensure_ascii=False),flush=True)
except BaseException as ex:
    receipt['failure_utc']=utc();receipt['failure']=repr(ex);receipt['traceback']=traceback.format_exc();dump(O/'publication-and-full-readback.json',receipt);print(receipt['traceback'],file=sys.stderr);raise
