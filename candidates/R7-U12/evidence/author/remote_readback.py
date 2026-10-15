"""Read every candidate commit file in full from immutable remote URLs."""
import concurrent.futures
import datetime
import json
import subprocess
import sys
import time
import urllib.request
import urllib.error
from build_candidate import B, ROOT, EVID, identity

BRANCH='codex/r7-u12-author-20261015-wave1'
REPO='y805939188/pokemon-essentials-clean-room'

def utc():return datetime.datetime.now(datetime.timezone.utc).isoformat()

def command(argv):
    start=utc();proc=subprocess.Popen(argv,cwd=ROOT,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    out,err=proc.communicate()
    row={'argv':argv,'start_utc':start,'end_utc':utc(),'audit_pid':proc.pid,
         'exit_code':proc.returncode,'stdout':out.decode(),'stderr':err.decode()}
    assert proc.returncode==0,row
    return out,row

def http(url,limit):
    attempts=[]
    for i in range(3):
        start=utc()
        try:
            with urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'R7-U12-immutable-readback'}),timeout=40) as r:
                data=r.read(limit+1);status=r.status
            attempts.append({'start_utc':start,'end_utc':utc(),'http_status':status,'bytes_read':len(data)})
            return data,attempts
        except (urllib.error.URLError,TimeoutError) as error:
            attempts.append({'start_utc':start,'end_utc':utc(),'error':str(error)})
            if i==2:raise RuntimeError({'url':url,'attempts':attempts}) from error
            time.sleep(i+1)

def main():
    commit=sys.argv[1]; start=utc()
    tip,ls=command(['git','ls-remote','--heads','origin',BRANCH])
    assert tip.decode().split()[0]==commit
    _,fetch=command(['git','fetch','origin','refs/heads/'+BRANCH])
    fetched,_=command(['git','rev-parse','FETCH_HEAD']);assert fetched.decode().strip()==commit
    tree,_=command(['git','rev-parse',commit+'^{tree}']);tree=tree.decode().strip()
    remote_doc,api_attempts=http('https://api.github.com/repos/'+REPO+'/git/commits/'+commit,100000)
    document=json.loads(remote_doc);assert document['sha']==commit and document['tree']['sha']==tree
    paths,_=command(['git','diff-tree','--no-commit-id','--name-only','-r',B,commit]);paths=paths.decode().splitlines()
    assert paths and all(p.startswith('candidates/R7-U12/') for p in paths)
    def read(path):
        expected,_=command(['git','show',commit+':'+path])
        url='https://raw.githubusercontent.com/'+REPO+'/'+commit+'/'+path
        actual,attempts=http(url,len(expected))
        assert actual==expected
        return {'path':path,'url':url,**identity(actual),'full_body_compared_equal':True,'attempts':attempts}
    with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:
        files=list(pool.map(read,paths))
    manifest=json.loads(subprocess.check_output(['git','show',commit+':candidates/R7-U12/evidence/author/artifact-manifest.json'],cwd=ROOT))
    assert len(files)==manifest['expected_total_files_in_final_commit']
    declared={r['path']:r['new'] for r in manifest['all_new_commit_files_except_self']}
    for row in files:
        if row['path'] in declared:assert {k:row[k] for k in ('bytes','sha256','git_blob')}==declared[row['path']]
        else:assert row['path']=='candidates/R7-U12/evidence/author/artifact-manifest.json'
    result={'schema':'r7.u12.full-remote-readback.v1','status':'ALL_NEW_FILES_FULL_REMOTE_READBACK_MATCH',
        'start_utc':start,'end_utc':utc(),'branch':BRANCH,'commit':commit,'tree':tree,
        'ls_remote':ls,'fetch':fetch,'remote_commit_document':document,'remote_commit_api_attempts':api_attempts,
        'files':files,'file_count':len(files),'bytes_read_and_matched':sum(r['bytes'] for r in files),
        'qualification':'Remote full bytes and commit/tree identity only; not independent review, semantic acceptance, or runtime certification.'}
    if len(sys.argv)>2:
        target=EVID/sys.argv[2]
        assert target.parent==EVID
        target.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(result,ensure_ascii=False,indent=2))

if __name__=='__main__':main()
