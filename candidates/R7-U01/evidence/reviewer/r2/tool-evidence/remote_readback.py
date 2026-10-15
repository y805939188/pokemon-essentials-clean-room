"""Read every delivered file from immutable remote URLs and verify exact bytes."""
from pathlib import Path
import concurrent.futures
import datetime
import hashlib
import json
import subprocess
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

commit, destination = sys.argv[1:]
branch = 'codex/r7-u01-reviewer-20261015-r2'
base = 'e646432c644dec04d306842cc5a559a29c718fbc'
prefix = 'candidates/R7-U01/evidence/reviewer/r2/'
def git(*args):
    return subprocess.check_output(['git',*args])
def utc():
    return datetime.datetime.now(datetime.timezone.utc).isoformat()
def identity(data):
    return {'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest(),
            'git_blob':hashlib.sha1(f'blob {len(data)}\0'.encode()+data).hexdigest()}
def tip():
    return git('ls-remote','--heads','origin','refs/heads/'+branch).decode().strip().split()[0]

receipt = {'schema':'r7.u01-reviewer-remote-full-readback.r2.v1','start_utc':utc(),
           'commit':commit,'tree':git('rev-parse',commit+'^{tree}').decode().strip(),
           'branch':branch,'base':base,'files':[],'qualification':'Complete remote file bytes + actual remote tip and cryptographic commit/tree binding; TOOL_VALIDATION only.'}
def read_one(path):
    assert path.startswith(prefix)
    local = git('show',commit+':'+path)
    mode,kind,blob = git('ls-tree',commit,'--',path).decode().split('\t')[0].split()
    assert mode == '100644' and kind == 'blob' and blob == identity(local)['git_blob']
    url = 'https://raw.githubusercontent.com/y805939188/pokemon-essentials-clean-room/'+commit+'/'+urllib.parse.quote(path)
    attempts = []
    for attempt in range(1,4):
        start = utc()
        try:
            with urllib.request.urlopen(url,timeout=40) as response:
                remote = response.read(len(local)+1)
                status = response.status
            actual = identity(remote)
            assert remote == local and actual['git_blob'] == blob
            attempts.append({'attempt':attempt,'start_utc':start,'end_utc':utc(),'http_status':status,'complete_byte_match':True})
            return {'path':path,'mode':mode,**actual,'url':url,'attempts':attempts}
        except (urllib.error.URLError,TimeoutError) as error:
            attempts.append({'attempt':attempt,'start_utc':start,'end_utc':utc(),'error':str(error)})
            if attempt == 3 or (isinstance(error,urllib.error.HTTPError) and error.code not in [429,500,502,503,504]):
                raise RuntimeError(json.dumps({'path':path,'attempts':attempts})) from error
            time.sleep(attempt)
try:
    receipt['remote_tip_before'] = tip()
    assert receipt['remote_tip_before'] == commit
    changed = git('diff','--name-only',base,commit).decode().splitlines()
    assert changed and all(p.startswith(prefix) for p in changed)
    tree_paths = [line.split('\t')[1] for line in git('ls-tree','-r',commit,'--',prefix).decode().splitlines()]
    assert sorted(tree_paths) == sorted(changed)
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        for row in pool.map(read_one,changed):
            receipt['files'].append(row)
    receipt['remote_tip_after'] = tip()
    assert receipt['remote_tip_after'] == commit
    receipt['status'] = 'COMPLETE_REMOTE_READBACK_EXACT'
except Exception as error:
    receipt['status'] = 'INCOMPLETE_PRESERVED'
    receipt['error'] = str(error)
    raise
finally:
    receipt['end_utc'] = utc()
    receipt['files_verified'] = len(receipt['files'])
    receipt['bytes_verified'] = sum(r['bytes'] for r in receipt['files'])
    Path(destination).write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:receipt[k] for k in ['status','commit','tree','files_verified','bytes_verified','remote_tip_before','remote_tip_after']}))
