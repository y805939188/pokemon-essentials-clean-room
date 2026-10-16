"""Read every committed task file completely from immutable GitHub raw URLs.

An optional receipt records an earlier core. With no receipt, the result is
returned on stdout, avoiding a file attempting to contain its own future hash.
No source behavior is run. No credentials are queried.
"""
import argparse
import concurrent.futures
import datetime
import hashlib
import json
from pathlib import Path
import subprocess
import urllib.parse
import urllib.request

parser=argparse.ArgumentParser()
parser.add_argument('commit')
parser.add_argument('--receipt')
args=parser.parse_args()
HERE=Path(__file__).resolve().parent
REPO=Path('/workspace/r8-external-legacy')
ROOT=str(HERE.relative_to(REPO))
OWNER='y805939188/pokemon-essentials-clean-room'
BRANCH='codex/r8-external-legacy-manifest-currentness-20261016'
START=datetime.datetime.now(datetime.timezone.utc).isoformat()

def git(*items):
    return subprocess.check_output(['git','-C',str(REPO),*items])

commit=git('rev-parse',args.commit+'^{commit}').decode().strip()
tree=git('rev-parse',commit+'^{tree}').decode().strip()
subtree=git('rev-parse',commit+':'+ROOT).decode().strip()
remote=git('ls-remote','origin','refs/heads/'+BRANCH).decode().strip()
assert remote.split()[0]==commit,(remote,commit)

def get(url):
    req=urllib.request.Request(url,headers={'User-Agent':'r8-external-legacy-evidence-readback','Accept':'application/vnd.github+json'})
    with urllib.request.urlopen(req,timeout=45) as response:
        return response.status,response.read()

status,raw=get('https://api.github.com/repos/'+OWNER+'/git/commits/'+commit)
remote_commit=json.loads(raw)
assert status==200 and remote_commit['sha']==commit and remote_commit['tree']['sha']==tree
status,raw=get('https://api.github.com/repos/'+OWNER+'/git/trees/'+subtree+'?recursive=1')
remote_tree=json.loads(raw)
assert status==200 and remote_tree['sha']==subtree and not remote_tree.get('truncated')
remote_entries={ROOT+'/'+x['path']:x for x in remote_tree['tree'] if x['type']=='blob'}
expected=[]
for row in git('ls-tree','-r','-z',commit,'--',ROOT).split(b'\0'):
    if not row:continue
    header,path=row.split(b'\t',1)
    mode,kind,blob=header.decode().split()
    path=path.decode()
    assert kind=='blob'
    item=remote_entries[path]
    assert item['mode']==mode and item['sha']==blob
    expected.append((path,mode,blob))
assert len(expected)==len(remote_entries)

def verify(row):
    path,mode,blob=row
    payload=git('show',commit+':'+path)
    url='https://raw.githubusercontent.com/'+OWNER+'/'+commit+'/'+urllib.parse.quote(path,safe='/')
    status,download=get(url)
    actual_blob=hashlib.sha1(('blob '+str(len(download))+'\0').encode()+download).hexdigest()
    assert status==200 and download==payload and actual_blob==blob,path
    return {'path':path,'mode':mode,'blob':blob,'bytes':len(download),'sha256':hashlib.sha256(download).hexdigest(),
            'http_status':status,'full_bytes_equal':True,'url':url}

with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
    items=list(pool.map(verify,expected))
result={'schema':'r8-external-legacy-remote-readback/v1','start_utc':START,
 'end_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'commit':commit,'tree':tree,'task_subtree':subtree,
 'branch':BRANCH,'remote_ref':remote,'github_commit_tree_verified':True,'github_subtree_modes_blobs_verified':True,
 'file_count':len(items),'bytes':sum(x['bytes'] for x in items),'all_files_full_readback':True,
 'method':'Fresh HTTPS reads of every immutable raw file; compare entire bytes, SHA256, Git blob; GitHub commit/tree APIs and real-time ls-remote bind root/subtree. No local-object-only readback.',
 'command':['python',str(Path(__file__).relative_to(REPO)),args.commit]+(['--receipt',args.receipt] if args.receipt else []),
 'bottom_exit':0,'stderr':'','evidence_level':'TOOL_VALIDATION_ONLY','business_vectors':'NOT_EXECUTED','files':items}
if args.receipt:
    destination=(REPO/args.receipt).resolve()
    assert destination.parent==HERE
    destination.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(result,ensure_ascii=False,indent=2))
