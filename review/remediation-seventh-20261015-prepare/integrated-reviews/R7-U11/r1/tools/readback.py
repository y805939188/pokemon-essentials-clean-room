"""Fetch an exact normal-pushed tip, then read every changed file's full HTTP body."""
import concurrent.futures
import datetime
import hashlib
import json
import subprocess
import sys
import urllib.parse
import urllib.request
from pathlib import Path

REPO=Path('/workspace/r7-ir-R7-U11/review-checkout')
PREFIX='review/remediation-seventh-20261015-prepare/integrated-reviews/R7-U11/r1/'
BRANCH='codex/r7-ir-u11-20261015-r1'
B='e646432c644dec04d306842cc5a559a29c718fbc'
commit,outfile=sys.argv[1:]
def utc():return datetime.datetime.now(datetime.timezone.utc).isoformat()
def git(*args):return subprocess.check_output(['git',*args],cwd=REPO)
def ident(b):return {'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'git_blob':hashlib.sha1(f'blob {len(b)}\0'.encode()+b).hexdigest()}
def tip():
    rows=git('ls-remote','--heads','origin','refs/heads/'+BRANCH).decode().splitlines()
    assert len(rows)==1
    return rows[0].split()[0]
assert len(commit)==40 and all(c in '0123456789abcdef' for c in commit)
start=utc();before=tip();assert before==commit,(before,commit)
subprocess.run(['git','fetch','--no-tags','origin','refs/heads/'+BRANCH],cwd=REPO,check=True)
assert git('rev-parse','FETCH_HEAD').decode().strip()==commit
assert git('rev-parse','HEAD').decode().strip()==commit
paths=git('diff','--name-only',B,commit,'--').decode().splitlines()
assert paths and all(p.startswith(PREFIX) for p in paths)
rows=[]
def fetch(path):
    expected=git('show',commit+':'+path)
    assert (REPO/path).read_bytes()==expected
    mode_type_blob=git('ls-tree',commit,'--',path).decode().strip().split('\t')[0].split()
    assert mode_type_blob[0]=='100644' and mode_type_blob[1]=='blob'
    url='https://raw.githubusercontent.com/y805939188/pokemon-essentials-clean-room/'+commit+'/'+urllib.parse.quote(path,safe='/')
    attempt_rows=[]
    for attempt in range(1,4):
        began=utc()
        try:
            with urllib.request.urlopen(url,timeout=45) as response:
                status=response.status
                actual=response.read(len(expected)+1)
            assert status==200 and actual==expected
            got=ident(actual);assert got['git_blob']==mode_type_blob[2]
            attempt_rows.append({'attempt':attempt,'start_utc':began,'end_utc':utc(),'http_status':status,'complete_byte_match':True})
            return {'path':path,'url':url,**got,'git_mode':mode_type_blob[0],
                    'actual_git_blob':mode_type_blob[2],'attempts':attempt_rows}
        except Exception as error:
            attempt_rows.append({'attempt':attempt,'start_utc':began,'end_utc':utc(),'error':repr(error)})
            if attempt==3:raise
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:
    rows=list(pool.map(fetch,paths))
after=tip();assert after==before
manifest=json.loads(git('show',commit+':'+PREFIX+'artifact-manifest.json'))
remote={r['path']:r for r in rows}
assert set(remote)=={r['path'] for r in manifest['files']}|{PREFIX+'artifact-manifest.json'}
for row in manifest['files']:
    assert all(row[k]==remote[row['path']][k] for k in ['bytes','sha256','git_blob','git_mode'])
receipt={'schema':'r7.u11.actual-review-complete-remote-readback.v1',
         'start_utc':start,'end_utc':utc(),'branch':BRANCH,'commit':commit,
         'tree':git('rev-parse',commit+'^{tree}').decode().strip(),
         'result_directory_tree':git('rev-parse',commit+':'+PREFIX.rstrip('/')).decode().strip(),
         'remote_tip_before':before,'remote_tip_after':after,
         'files':len(rows),'bytes':sum(x['bytes'] for x in rows),'rows':rows,
         'complete_all_response_bodies_equal_local_and_fixed_Git':True,
         'manifest_nonself_and_self_external_binding':True,
         'qualification':'Normal transport only; all behavior NOT_EXECUTED/configuration UNVERIFIED. Python HTTP threads are ordinary tool I/O, not AI tasks.'}
path=Path(outfile);assert not path.exists();path.parent.mkdir(parents=True,exist_ok=True)
path.write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:receipt[k] for k in ['branch','commit','tree','result_directory_tree','files','bytes','remote_tip_before','remote_tip_after','complete_all_response_bodies_equal_local_and_fixed_Git']}))
