"""Read all published review blobs from a fresh remote clone; artifact I/O only."""
import datetime
import hashlib
import json
import pathlib
import subprocess
import sys
import tempfile

ROOT = pathlib.Path('/workspace/r6-actual-c')
PREFIX = 'review/remediation-sixth-20261014-prepare/actual-reviews/group-C'
URL = 'https://github.com/y805939188/pokemon-essentials-clean-room.git'
BRANCH = 'codex/remediation-sixth-actual-c-20261014'
ACTUAL = '86bbc99b28d93db4ed9d6897daf5f3725ccd1808'
commit, output_name = sys.argv[1:3]
assert len(commit) == 40 and all(c in '0123456789abcdef' for c in commit)
output_path = pathlib.Path(output_name).resolve()
assert output_path.is_relative_to(ROOT / PREFIX) or output_path.is_relative_to('/tmp')
cache = pathlib.Path(tempfile.mkdtemp(prefix='r6-actual-c-remote-',dir='/tmp'))/'fresh.git'
assert not cache.exists()
commands = []


def run(argv, payload=False):
    result = subprocess.run(argv,cwd=ROOT,capture_output=True)
    row = {'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
           'argv':argv,'exit':result.returncode,'stderr':result.stderr.decode(errors='replace')}
    if payload:
        row.update({'stdout_bytes':len(result.stdout),
                    'stdout_sha256':hashlib.sha256(result.stdout).hexdigest(),
                    'full_stdout_read':True})
    else:
        row['stdout'] = result.stdout.decode(errors='replace')
    commands.append(row)
    assert result.returncode == 0,row
    return result.stdout


run(['git','clone','--bare','--filter=blob:none','--depth=1','--single-branch',
     '--branch',BRANCH,URL,str(cache)])
remote_git = ['git','--git-dir='+str(cache)]
head = run(remote_git+['rev-parse','HEAD']).decode().strip()
assert head == commit,(head,commit)
remote_head = run(['git','ls-remote',URL,'refs/heads/'+BRANCH]).decode().strip()
assert remote_head.split()[0] == commit
tree = run(remote_git+['rev-parse',commit+'^{tree}']).decode().strip()
directory_tree = run(remote_git+['rev-parse',commit+':'+PREFIX]).decode().strip()
formal_tree = run(remote_git+['rev-parse',commit+':deliverables/final-specification-set']).decode().strip()
actual_formal_tree = subprocess.check_output(['git','-C',str(ROOT),'rev-parse',ACTUAL+':deliverables/final-specification-set']).decode().strip()
assert formal_tree == actual_formal_tree
remote_ls = run(remote_git+['ls-tree','-r',commit,'--',PREFIX]).decode().splitlines()
local_ls = subprocess.check_output(['git','-C',str(ROOT),'ls-tree','-r',commit,'--',PREFIX]).decode().splitlines()
assert remote_ls == local_ls
rows = []
for line in remote_ls:
    descriptor,path = line.split('\t',1)
    mode,kind,blob = descriptor.split()
    assert kind == 'blob'
    raw = run(remote_git+['show',commit+':'+path],payload=True)
    expected = subprocess.check_output(['git','-C',str(ROOT),'show',commit+':'+path])
    actual_blob = hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()
    assert raw == expected and actual_blob == blob
    rows.append({'path':path,'mode':mode,'git_blob':blob,'bytes':len(raw),
                 'sha256':hashlib.sha256(raw).hexdigest(),
                 'full_remote_bytes_read':True,'exact_local_fixed_blob_match':True})
receipt = {'status':'PASS_FULL_REMOTE_PAYLOAD_READBACK','commit':commit,
           'workspace_tree':tree,'review_directory_tree':directory_tree,
           'actual_commit':ACTUAL,'formal_tree_unchanged':formal_tree,
           'entry':PREFIX+'/report.md','branch':BRANCH,'remote_head':remote_head,
           'fresh_bare_cache':str(cache),'read_payload_count':len(rows),
           'read_bytes':sum(row['bytes'] for row in rows),'payloads':rows,
           'commands':commands,'reference_or_host_behavior_execution':0,
           'readback_is_identity_evidence_only':True}
output_path.write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({key:receipt[key] for key in ['status','commit','workspace_tree',
                  'review_directory_tree','read_payload_count','read_bytes','entry']},ensure_ascii=False))
