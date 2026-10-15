"""Read every new reviewer file from immutable remote URLs and verify bytes.

The receipt is written after publication; it cannot bind itself at the same commit.
"""
import concurrent.futures
import datetime
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import urllib.parse
import urllib.request

ROOT=Path(__file__).resolve().parents[6]
B='e646432c644dec04d306842cc5a559a29c718fbc'
BRANCH='codex/r7-u06-reviewer-20261015-r1'
PREFIX='candidates/R7-U06/evidence/reviewer/r1/'
REPOSITORY='y805939188/pokemon-essentials-clean-room'
utc=lambda:datetime.datetime.now(datetime.timezone.utc).isoformat()

def git(*args):
    return subprocess.check_output(['git','-C',str(ROOT),*args]).decode().strip()

def identity(data):
    return {'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest(),
            'git_blob_content_id':hashlib.sha1(f'blob {len(data)}\0'.encode()+data).hexdigest()}

def main():
    output=Path(sys.argv[1])
    if output.exists():raise SystemExit('Do not overwrite a publication receipt')
    start=utc();commit=git('rev-parse','HEAD');tree=git('rev-parse','HEAD^{tree}')
    ref=git('ls-remote','--heads','origin','refs/heads/'+BRANCH)
    assert ref.split()==[commit,'refs/heads/'+BRANCH],ref
    fetch=subprocess.run(['git','-C',str(ROOT),'fetch','--no-tags','origin','refs/heads/'+BRANCH],capture_output=True,text=True)
    assert fetch.returncode==0,(fetch.stdout,fetch.stderr)
    fetched_commit=git('rev-parse','FETCH_HEAD')
    fetched_tree=git('rev-parse','FETCH_HEAD^{tree}')
    assert fetched_commit==commit and fetched_tree==tree
    changes=git('diff','--name-status',B,commit).splitlines()
    paths=[]
    for row in changes:
        status,path=row.split('\t')
        assert status=='A' and path.startswith(PREFIX),row
        paths.append(path)
    def read(path):
        data=subprocess.check_output(['git','-C',str(ROOT),'show',commit+':'+path])
        mode,kind,blob=git('ls-tree',commit,'--',path).split('\t')[0].split()
        assert mode=='100644' and kind=='blob'
        url=f'https://raw.githubusercontent.com/{REPOSITORY}/{commit}/'+urllib.parse.quote(path)
        attempts=[]
        for attempt in range(1,4):
            begin=utc()
            try:
                with urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'R7-U06-independent-reviewer'}),timeout=40) as response:
                    got=response.read(len(data)+1);status=response.status
                assert got==data,(path,'full byte mismatch')
                actual=identity(got);assert actual['git_blob_content_id']==blob
                attempts.append({'attempt':attempt,'start_utc':begin,'end_utc':utc(),'http_status':status})
                return {'path':path,'url':url,'git_mode':mode,**actual,'complete_byte_match':True,'attempts':attempts}
            except Exception as error:
                attempts.append({'attempt':attempt,'start_utc':begin,'end_utc':utc(),'error':str(error)})
                if attempt==3:raise
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:rows=list(pool.map(read,paths))
    final_ref=git('ls-remote','--heads','origin','refs/heads/'+BRANCH)
    assert final_ref==ref
    receipt={'schema':'r7.u06.reviewer-full-remote-readback.v1','status':'ALL_NEW_REVIEWER_FILES_FULL_REMOTE_BYTES_VERIFIED',
             'start_utc':start,'end_utc':utc(),'branch':BRANCH,'commit':commit,'tree':tree,'fixed_B':B,
             'remote_ref_before_and_after':ref,
             'git_protocol_fetch':{'argv':['git','fetch','--no-tags','origin','refs/heads/'+BRANCH],
                                   'stdout':fetch.stdout,'stderr':fetch.stderr,'exit_code':fetch.returncode,
                                   'FETCH_HEAD':fetched_commit,'FETCH_HEAD_tree':fetched_tree},
             'commit_api_qualification':'Not used. Original API attempt received proxy 403; see commands/011-payload-readback.json.',
             'remote_commit_tree_matches':True,'files':rows,'files_verified':len(rows),
             'bytes_verified':sum(x['bytes'] for x in rows),'qualification':'TOOL_VALIDATION_ONLY; no formal acceptance or closure'}
    output.parent.mkdir(parents=True,exist_ok=True)
    with output.open('x') as f:json.dump(receipt,f,ensure_ascii=False,indent=2);f.write('\n')
    print(json.dumps({k:receipt[k] for k in ['status','branch','commit','tree','files_verified','bytes_verified']}))

if __name__=='__main__':main()
