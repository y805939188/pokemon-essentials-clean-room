"""Fetch a fixed report from origin into a fresh bare cache and read every blob."""
import datetime
import hashlib
import json
import pathlib
import subprocess
import sys

ROOT = pathlib.Path('/workspace/r6-u07-review')
PREFIX = 'review/remediation-sixth-20261014-prepare/reviews/R6-U07-R'
URL = 'https://github.com/y805939188/pokemon-essentials-clean-room.git'
BRANCH = 'codex/remediation-sixth-r6-u07-review-20261014'
commit, output_path = sys.argv[1:3]
assert len(commit) == 40 and all(c in '0123456789abcdef' for c in commit)
cache = pathlib.Path('/tmp/r6-u07-remote-readback-' + commit[:12] + '.git')
assert not cache.exists(), 'Use a fresh cache; do not silently reuse local objects'
commands = []


def run(argv, cwd=ROOT, payload=False):
    r = subprocess.run(argv, cwd=cwd, capture_output=True)
    row = {'utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
           'cwd': str(cwd), 'argv': argv, 'exit': r.returncode,
           'stderr': r.stderr.decode(errors='replace')}
    if payload:
        row.update({'stdout_bytes':len(r.stdout),
                    'stdout_sha256':hashlib.sha256(r.stdout).hexdigest(),
                    'full_stdout_read':True})
    else:
        row['stdout'] = r.stdout.decode(errors='replace')
    commands.append(row)
    assert r.returncode == 0, row
    return r.stdout


run(['git','clone','--bare','--filter=blob:none','--depth=1','--single-branch',
     '--branch',BRANCH,URL,str(cache)])
g = ['git','--git-dir='+str(cache)]
head = run(g+['rev-parse','HEAD']).decode().strip()
assert head == commit, (head,commit)
remote_head = run(['git','ls-remote',URL,'refs/heads/'+BRANCH]).decode().strip()
assert remote_head.split()[0] == commit
tree = run(g+['rev-parse',commit+'^{tree}']).decode().strip()
directory_tree = run(g+['rev-parse',commit+':'+PREFIX]).decode().strip()
remote_ls = run(g+['ls-tree','-r',commit,'--',PREFIX]).decode().splitlines()
local_ls = subprocess.check_output(['git','-C',str(ROOT),'ls-tree','-r',commit,'--',PREFIX]).decode().splitlines()
assert remote_ls == local_ls
rows = []
for line in remote_ls:
    descriptor,path = line.split('\t',1)
    mode,kind,blob = descriptor.split()
    assert kind == 'blob'
    raw = run(g+['show',commit+':'+path],payload=True)
    expected = subprocess.check_output(['git','-C',str(ROOT),'show',commit+':'+path])
    actual_blob = hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()
    assert raw == expected and actual_blob == blob
    rows.append({'path':path,'mode':mode,'git_blob':blob,'bytes':len(raw),
                 'sha256':hashlib.sha256(raw).hexdigest(),
                 'full_remote_bytes_read':True,'exact_local_fixed_blob_match':True})
receipt = {'status':'PASS_FULL_REMOTE_PAYLOAD_READBACK','commit':commit,
           'workspace_tree':tree,'review_directory_tree':directory_tree,
           'entry':PREFIX+'/report.md','branch':BRANCH,'remote_head':remote_head,
           'fresh_bare_cache':str(cache),'read_payload_count':len(rows),
           'read_bytes':sum(r['bytes'] for r in rows),'payloads':rows,
           'commands':commands,'reference_or_host_behavior_execution':0}
pathlib.Path(output_path).write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:receipt[k] for k in ['status','commit','workspace_tree',
                  'review_directory_tree','read_payload_count','read_bytes','entry']},ensure_ascii=False))
