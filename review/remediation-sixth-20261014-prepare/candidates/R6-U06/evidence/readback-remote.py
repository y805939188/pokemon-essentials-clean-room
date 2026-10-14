#!/usr/bin/env python3
"""Read every task payload from fixed remote commit; compare exact Git blob bytes."""
import datetime
import hashlib
import json
import subprocess
import sys
import urllib.parse
import urllib.request
from pathlib import Path

E = Path(__file__).resolve().parent
ROOT = E.parents[4]
BASE = '469a268b92daed7b4d28d7fd0da75520cbb7228f'
PREFIX = str(E.parent.relative_to(ROOT))+'/'
commit, output = sys.argv[1:]
assert len(commit) == 40 and all(c in '0123456789abcdef' for c in commit)
out = Path(output).resolve()
assert out.is_relative_to(E) or out.is_relative_to(Path('/tmp'))
def git(*args):
    return subprocess.check_output(['git','-C',str(ROOT),*args])
paths = git('diff','--name-only',BASE,commit).decode().splitlines()
assert paths and all(p.startswith(PREFIX) for p in paths)
branch = 'codex/remediation-sixth-r6-u06-author-20261014'
remote = git('ls-remote','--heads','origin',branch).decode().strip()
started = datetime.datetime.now(datetime.timezone.utc).isoformat()
rows = []
attempts = []
commit_response = None
commit_url = 'https://api.github.com/repos/y805939188/pokemon-essentials-clean-room/git/commits/'+commit
for n in range(1,4):
    t = datetime.datetime.now(datetime.timezone.utc).isoformat()
    try:
        with urllib.request.urlopen(commit_url,timeout=25) as response:
            commit_response = json.loads(response.read())
        attempts.append(dict(path='GIT_COMMIT_OBJECT',attempt=n,started_utc=t,ended_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),status=200))
        break
    except Exception as ex:
        attempts.append(dict(path='GIT_COMMIT_OBJECT',attempt=n,started_utc=t,ended_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),error=repr(ex)))
local_tree = git('rev-parse',commit+'^{tree}').decode().strip()
remote_tree = None if commit_response is None else commit_response['tree']['sha']
remote_tree_exact = remote_tree == local_tree
for path in paths:
    expected = git('cat-file','blob',commit+':'+path)
    mode, typ, tail = git('ls-tree',commit,'--',path).decode().strip().split(' ',2)
    blob, _ = tail.split('\t',1)
    url = 'https://raw.githubusercontent.com/y805939188/pokemon-essentials-clean-room/'+commit+'/'+urllib.parse.quote(path,safe='/')
    data = None
    for n in range(1,4):
        t = datetime.datetime.now(datetime.timezone.utc).isoformat()
        try:
            with urllib.request.urlopen(url,timeout=25) as response:
                data = response.read()
                status = response.status
            attempts.append(dict(path=path,attempt=n,started_utc=t,ended_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),status=status,bytes=len(data)))
            break
        except Exception as ex:
            attempts.append(dict(path=path,attempt=n,started_utc=t,ended_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),error=repr(ex)))
    actual_blob = None if data is None else hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
    rows.append(dict(path=path,commit=commit,mode=mode,type=typ,bytes=len(expected),
                     sha256=hashlib.sha256(expected).hexdigest(),git_blob=blob,
                     remote_bytes=None if data is None else len(data),
                     remote_sha256=None if data is None else hashlib.sha256(data).hexdigest(),
                     remote_git_blob=actual_blob,exact=data == expected and actual_blob == blob))
    print(json.dumps(dict(path=path,exact=rows[-1]['exact'],bytes=len(expected))),flush=True)
result = dict(evidence_level='TOOL_VALIDATION_REMOTE_FULL_BYTE_READBACK',commit=commit,
              tree=local_tree,remote_tree=remote_tree,remote_tree_exact=remote_tree_exact,
              candidate_directory_tree=git('rev-parse',commit+':'+PREFIX.rstrip('/')).decode().strip(),
              base=BASE,remote_branch=branch,ls_remote=remote,
              remote_branch_exact=remote.split()[0] == commit if remote else False,
              cwd=str(ROOT),argv=sys.argv,started_utc=started,
              ended_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
              rows=rows,attempts=attempts,payload_count=len(rows),
              all_payloads_exact=all(x['exact'] for x in rows),
              no_undeclared_write_paths=True,reference_execution=False,
              mode_type_binding='Remote Git commit API independently reports the exact same complete tree SHA, binding every path/mode/type/blob; every changed raw payload independently read in full and compared. ls-remote binds branch to commit.')
out.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:result[k] for k in ['commit','tree','candidate_directory_tree','payload_count','all_payloads_exact','remote_branch_exact','remote_tree_exact']}))
sys.exit(0 if result['all_payloads_exact'] and result['remote_branch_exact'] and remote_tree_exact else 1)
