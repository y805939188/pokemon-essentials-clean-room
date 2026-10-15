"""Ordinary push to sole branch, then read every exact committed artifact from remote."""
import concurrent.futures, datetime, hashlib, json, pathlib, subprocess, sys, time, urllib.parse, urllib.request
ROOT=pathlib.Path.cwd()
P=pathlib.Path(__file__).parent
PREFIX='candidates/R7-U10/evidence/reviewer/r1/'
BRANCH='codex/r7-u10-reviewer-20261015-r1'
B='e646432c644dec04d306842cc5a559a29c718fbc'
REPO='y805939188/pokemon-essentials-clean-room'
def git(*a):return subprocess.check_output(['git',*a],cwd=ROOT)
def ident(b):return {'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'git_blob':hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()}
def readone(row,commit):
    url='https://raw.githubusercontent.com/'+REPO+'/'+commit+'/'+urllib.parse.quote(row['path'])
    attempts=[]
    for attempt in range(1,4):
        start=datetime.datetime.now(datetime.timezone.utc).isoformat()
        try:
            with urllib.request.urlopen(url,timeout=40) as response:
                data=response.read(row['bytes']+1);status=response.status
            actual=ident(data)
            assert actual=={k:row[k] for k in actual},row['path']
            attempts.append({'start_utc':start,'end_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'http_status':status})
            return {**row,'remote_identity':actual,'url':url,'attempts':attempts,'match':True}
        except Exception as error:
            attempts.append({'start_utc':start,'end_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'error':str(error)})
            if attempt==3:raise
            time.sleep(attempt)
def main():
    label=sys.argv[1]
    commit=git('rev-parse','HEAD').decode().strip();tree=git('rev-parse','HEAD^{tree}').decode().strip()
    assert git('branch','--show-current').decode().strip()==BRANCH
    rows=[]
    changed=git('diff','--name-only','-z',B,commit).split(b'\0')
    assert all(not x or x.decode().startswith(PREFIX) for x in changed)
    for raw in git('ls-tree','-r','-z',commit,'--',PREFIX).split(b'\0'):
        if not raw:continue
        meta,path=raw.split(b'\t');mode,kind,blob=meta.decode().split();path=path.decode()
        assert mode=='100644' and kind=='blob'
        data=git('show',commit+':'+path);identity=ident(data);assert identity['git_blob']==blob
        rows.append({'path':path,**identity,'mode':mode})
    assert len(rows)==len([x for x in changed if x])
    result={'schema':'r7.u10.reviewer.actual-remote-readback.v1','start_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'branch':BRANCH,'commit':commit,'tree':tree,'base_commit':B,'files':[],'operation':'ordinary git push; exact immutable commit raw reads; no force/main/tag/author/integration push'}
    command=['git','-c','credential.helper=!gh auth git-credential','push','origin','HEAD:refs/heads/'+BRANCH]
    publication_logs=pathlib.Path('/workspace/r7-u10-publication-logs')
    publication_logs.mkdir(exist_ok=True)
    start=datetime.datetime.now(datetime.timezone.utc).isoformat()
    with (publication_logs/(label+'-push.stdout')).open('xb') as out,(publication_logs/(label+'-push.stderr')).open('xb') as err:
        proc=subprocess.Popen(command,cwd=ROOT,stdout=out,stderr=err);code=proc.wait()
    result['push']={'argv':command,'pid':proc.pid,'exit_code':code,'start_utc':start,'end_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'stdout_path':str(publication_logs/(label+'-push.stdout')),'stderr_path':str(publication_logs/(label+'-push.stderr')),'stdout':(publication_logs/(label+'-push.stdout')).read_text(),'stderr':(publication_logs/(label+'-push.stderr')).read_text()}
    assert code==0
    result['remote_ref']=git('-c','credential.helper=!gh auth git-credential','ls-remote','origin','refs/heads/'+BRANCH).decode().strip()
    assert result['remote_ref'].split()[0]==commit
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:result['files']=list(pool.map(lambda r:readone(r,commit),rows))
    assert len(result['files'])==len(rows) and all(r['match'] for r in result['files'])
    result.update({'status':'FULL_REMOTE_BYTES_VERIFIED','files_verified':len(rows),'bytes_verified':sum(r['bytes'] for r in rows),'end_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'semantic_credit':False,'manifest':next(r for r in rows if r['path'].endswith('/artifact-manifest.json'))})
    # Outer receipt avoids claiming a file can contain its own final commit hash.
    dest=pathlib.Path('/workspace/r7-u10-reviewer-'+label+'-remote-readback.json')
    with dest.open('x') as stream:json.dump(result,stream,ensure_ascii=False,indent=2);stream.write('\n')
    print(json.dumps({k:result[k] for k in ['status','branch','commit','tree','files_verified','bytes_verified','manifest']},ensure_ascii=False))
if __name__=='__main__':main()
