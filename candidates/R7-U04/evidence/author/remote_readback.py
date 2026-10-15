"""Read full candidate bytes from immutable remote URLs and compare to Git blobs."""
import argparse
import concurrent.futures
import datetime
import hashlib
import json
from pathlib import Path
import re
import subprocess
import time
import urllib.error
import urllib.parse
import urllib.request

parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--commit',required=True)
parser.add_argument('--repo',type=Path,default=Path(__file__).resolve().parents[4])
parser.add_argument('--receipt',type=Path)
args=parser.parse_args()
assert re.fullmatch('[0-9a-f]{40}',args.commit)
branch='codex/r7-u04-author-20261015-pilot1'
prefix='candidates/R7-U04/'

def now(): return datetime.datetime.now(datetime.timezone.utc).isoformat()
def git(*argv): return subprocess.check_output(['git',*argv],cwd=args.repo)
def identity(data):
    return {'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest(),
            'git_blob':hashlib.sha1(f'blob {len(data)}\0'.encode()+data).hexdigest()}
def remote_head():
    raw=git('ls-remote','--exit-code','--heads','origin',branch).decode()
    assert raw==args.commit+'\trefs/heads/'+branch+'\n',raw
    return raw

started=now()
head_before=remote_head()
paths=git('ls-tree','-r','--name-only',args.commit,'--',prefix).decode().splitlines()
assert paths and all(p.startswith(prefix) for p in paths)
changed=git('diff','--name-only','e646432c644dec04d306842cc5a559a29c718fbc',args.commit).decode().splitlines()
assert changed==paths

def read_one(path):
    original=git('show',args.commit+':'+path)
    url='https://raw.githubusercontent.com/y805939188/pokemon-essentials-clean-room/'+args.commit+'/'+urllib.parse.quote(path)
    attempts=[]
    for attempt in range(1,4):
        start=now()
        try:
            request=urllib.request.Request(url,headers={'User-Agent':'R7-U04-author-full-byte-readback'})
            with urllib.request.urlopen(request,timeout=40) as response:
                data=response.read(len(original)+1)
                status=response.status
            assert status==200 and data==original,'Remote candidate byte mismatch: '+path
            attempts.append({'attempt':attempt,'start_utc':start,'end_utc':now(),'http_status':status})
            return {'path':path,'url':url,**identity(data),'full_byte_equality':True,'attempts':attempts}
        except (urllib.error.URLError,TimeoutError) as error:
            attempts.append({'attempt':attempt,'start_utc':start,'end_utc':now(),'error':str(error)})
            if isinstance(error,urllib.error.HTTPError) and error.code not in (429,500,502,503,504): raise
            if attempt==3: raise
            time.sleep(attempt)

with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
    files=list(pool.map(read_one,paths))
head_after=remote_head()
receipt={'schema':'r7.u04.author-remote-readback.v1','status':'REMOTE_COMPLETE_BYTES_MATCH',
         'start_utc':started,'end_utc':now(),'branch':branch,'commit':args.commit,
         'tree':git('rev-parse',args.commit+'^{tree}').decode().strip(),
         'ls_remote_before':head_before,'ls_remote_after':head_after,
         'all_changes_within_prefix':True,'file_count':len(files),'total_bytes':sum(row['bytes'] for row in files),
         'files':files,'semantic_PASS':False,'independent_review':'NOT_REACHED',
         'qualification':'Immutable remote HTTP response bodies compared byte-for-byte with committed Git blobs. Transport identity only, not behavior or independent review.'}
if args.receipt:
    with args.receipt.open('x') as stream:
        stream.write(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({key:receipt[key] for key in ['status','branch','commit','tree','file_count','total_bytes','semantic_PASS','independent_review']},ensure_ascii=False))
