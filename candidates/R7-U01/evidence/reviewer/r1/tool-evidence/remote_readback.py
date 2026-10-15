"""Reviewer-owned exact HTTP/Git readback. Does not execute received programs."""
import concurrent.futures,datetime,hashlib,json,pathlib,subprocess,sys,time,urllib.error,urllib.parse,urllib.request

REPO=pathlib.Path(sys.argv[1]); EXPECTED=sys.argv[2]; OUTPUT=pathlib.Path(sys.argv[3])
BASE='e646432c644dec04d306842cc5a559a29c718fbc'
BRANCH='codex/r7-u01-reviewer-20261015-r1'
PREFIX='candidates/R7-U01/evidence/reviewer/r1/'
logs=[]
now=lambda:datetime.datetime.now(datetime.timezone.utc).isoformat()
def git(*args):
    cmd=['git',*args];start=now();p=subprocess.run(cmd,cwd=REPO,text=True,capture_output=True)
    logs.append(dict(command=cmd,cwd=str(REPO),start_utc=start,end_utc=now(),exit_code=p.returncode,stdout=p.stdout,stderr=p.stderr))
    assert p.returncode==0,logs[-1]
    return p.stdout.strip()
assert git('rev-parse','HEAD')==EXPECTED
assert git('branch','--show-current')==BRANCH
before=git('ls-remote','--heads','origin',BRANCH);assert before.split()[0]==EXPECTED
git('fetch','--no-tags','origin',BRANCH)
assert git('rev-parse','FETCH_HEAD')==EXPECTED
tree=git('rev-parse',EXPECTED+'^{tree}');assert git('rev-parse','FETCH_HEAD^{tree}')==tree
paths=git('diff','--name-only',BASE,EXPECTED).splitlines();assert paths and all(p.startswith(PREFIX) for p in paths)
git('merge-base','--is-ancestor',BASE,EXPECTED)
def read(path):
    expected=subprocess.check_output(['git','show',EXPECTED+':'+path],cwd=REPO)
    listing=subprocess.check_output(['git','ls-tree',EXPECTED,'--',path],cwd=REPO).decode()
    url='https://raw.githubusercontent.com/y805939188/pokemon-essentials-clean-room/'+EXPECTED+'/'+urllib.parse.quote(path)
    attempts=[]
    for attempt in range(1,4):
        start=now()
        try:
            with urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'R7-U01-independent-reviewer-readback'}),timeout=40) as r:
                actual=r.read(len(expected)+1);status=r.status
            assert status==200 and actual==expected,(path,status,len(actual))
            blob=hashlib.sha1(f'blob {len(actual)}\0'.encode()+actual).hexdigest()
            assert listing.startswith('100644 blob '+blob)
            attempts.append(dict(attempt=attempt,start_utc=start,end_utc=now(),http_status=status,complete_byte_match=True))
            return dict(path=path,url=url,attempts=attempts,git_mode='100644',bytes=len(actual),sha256=hashlib.sha256(actual).hexdigest(),git_blob=blob)
        except (urllib.error.URLError,TimeoutError) as error:
            attempts.append(dict(attempt=attempt,start_utc=start,end_utc=now(),error=str(error)))
            if attempt==3:raise
            time.sleep(attempt)
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool: files=list(pool.map(read,paths))
after=git('ls-remote','--heads','origin',BRANCH);assert after==before
assert not git('status','--porcelain=v1')
result=dict(schema='r7.u01-reviewer-exact-readback.v1',status='REMOTE_COMPLETE_BYTES_VERIFIED',commit=EXPECTED,tree=tree,branch=BRANCH,base=BASE,
            remote_tip_before_and_after=EXPECTED,write_prefix=PREFIX,files_verified=len(files),bytes_verified=sum(x['bytes'] for x in files),
            files=files,commands=logs,end_utc=now(),semantic_credit_from_transport=False)
OUTPUT.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k not in ['files','commands']},ensure_ascii=False))
