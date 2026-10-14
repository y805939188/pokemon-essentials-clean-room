#!/usr/bin/env python3
"""Full raw readback of every changed payload at an actual published commit."""
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import urllib.parse
import urllib.request
from datetime import datetime, timezone

e = Path(__file__).resolve().parent
repo = e.parents[4]
base = '469a268b92daed7b4d28d7fd0da75520cbb7228f'
commit, report_name = sys.argv[1:]
assert len(commit) == 40 and all(c in '0123456789abcdef' for c in commit)
assert '/' not in report_name and report_name.endswith('.json')
report = e / report_name
assert not report.exists(), 'Use a new report name; preserve previous attempts.'
branch = 'codex/remediation-sixth-r6-u09-author-20261014'
prefix = str(e.parent.relative_to(repo)) + '/'
start = datetime.now(timezone.utc).isoformat()
def git(*args):
    return subprocess.check_output(['git', *args], cwd=repo)
def identity(data):
    return {'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest(),
            'git_blob':hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()}
remote_argv = ['git','ls-remote','--heads','origin','refs/heads/'+branch]
remote = subprocess.run(remote_argv,cwd=repo,capture_output=True,text=True)
remote_record = {'argv':remote_argv,'exit':remote.returncode,'stdout':remote.stdout,'stderr':remote.stderr}
assert remote.returncode == 0 and remote.stdout.split()[0] == commit, remote_record
tree = git('rev-parse',commit+'^{tree}').decode().strip()
candidate_tree = git('rev-parse',commit+':'+prefix.rstrip('/')).decode().strip()
delta = [line.split('\t') for line in git('diff','--name-status',base,commit).decode().splitlines()]
assert all(status in ('A','M') and path.startswith(prefix) for status,path in delta), delta
rows = []
payload = {'commit':commit,'workspace_tree':tree,'candidate_directory_tree':candidate_tree,
           'fixed_prepare':base,'branch':branch,'cwd':str(repo),'argv':sys.argv,
           'utc_start':start,'remote_ref':remote_record,'files':rows,
           'mode_binding':'published commit SHA cryptographically binds local verified commit/tree/path/mode/type; raw full bytes must match each bound Git blob',
           'evidence_level':'TOOL_VALIDATION','reference_execution':False,
           'candidate_review':'PENDING_NON_AUTHOR_REVIEW','all_full_readback':False}
try:
    for status,path in delta:
        mode,kind,blob,_ = git('ls-tree',commit,'--',path).decode().strip().split(None,3)
        expected = git('show',commit+':'+path)
        assert mode == '100644' and kind == 'blob'
        url = 'https://raw.githubusercontent.com/y805939188/pokemon-essentials-clean-room/'+commit+'/'+urllib.parse.quote(path)
        attempts = []
        row = {'status':status,'path':path,'commit':commit,'mode':mode,'git_type':kind,
               'type':'text','expected':identity(expected),'attempts':attempts,'full_readback':False}
        rows.append(row)
        for attempt in range(1,4):
            begin = datetime.now(timezone.utc).isoformat()
            event = {'attempt':attempt,'url':url,'utc_start':begin}
            attempts.append(event)
            try:
                with urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'R6-U09-candidate-full-readback'}),timeout=30) as response:
                    data=response.read()
                    event.update(http_status=response.status,**identity(data))
                assert data==expected and identity(data)['git_blob']==blob
                row['full_readback']=True
                event['result']='FULL_BYTES_SHA256_BLOB_MATCH'
                break
            except Exception as error:
                event['error']=type(error).__name__+': '+str(error)
            finally:
                event['utc_end']=datetime.now(timezone.utc).isoformat()
        assert row['full_readback'], row
    payload['all_full_readback']=True
finally:
    payload['utc_end']=datetime.now(timezone.utc).isoformat()
    payload['files_total']=len(delta)
    payload['verified_total']=sum(row['full_readback'] for row in rows)
    report.write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'commit':commit,'workspace_tree':tree,'candidate_directory_tree':candidate_tree,
                  'files':len(delta),'full_readback':payload['all_full_readback']},ensure_ascii=False))
