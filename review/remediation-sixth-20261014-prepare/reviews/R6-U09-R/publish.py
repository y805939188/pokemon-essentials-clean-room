"""Publish this review normally and compare complete fresh remote blob payloads."""
import argparse
import datetime as dt
import hashlib
import json
import pathlib
import subprocess

ROOT = pathlib.Path(__file__).resolve().parent
REPO = ROOT.parents[3]
PREFIX = ROOT.relative_to(REPO).as_posix() + '/'
BRANCH = 'codex/remediation-sixth-r6-u09-review-20261014'
CANDIDATE = 'c3044166390b3d8c36f4cd121bb8619060b58bfe'
REMOTE = 'https://github.com/y805939188/pokemon-essentials-clean-room.git'
OPS = ROOT / 'operations'
OPS.mkdir(exist_ok=True)
records = []

def run(*args, object_repo=None):
    argv = ['git', '-C', str(object_repo or REPO), *args]
    start = dt.datetime.now(dt.timezone.utc).isoformat()
    p = subprocess.run(argv, cwd=REPO, capture_output=True)
    records.append({'argv': argv, 'cwd': str(REPO), 'utc_start': start,
                    'utc_end': dt.datetime.now(dt.timezone.utc).isoformat(),
                    'exit': p.returncode, 'stdout': p.stdout.decode('utf-8','replace'),
                    'stderr': p.stderr.decode('utf-8','replace'),
                    'evidence_level':'TOOL_VALIDATION','reference_execution':False})
    if p.returncode:
        raise RuntimeError(str(argv) + ': ' + p.stderr.decode('utf-8','replace'))
    return p.stdout

def identity(data):
    return {'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest(),
            'git_blob':hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()}

p=argparse.ArgumentParser()
p.add_argument('action',choices=['commit','push','readback'])
p.add_argument('--commit')
p.add_argument('--label',required=True)
p.add_argument('--message')
a=p.parse_args()
try:
    if a.action=='commit':
        staged=run('diff','--cached','--name-only').decode().splitlines()
        assert staged and all(x.startswith(PREFIX) for x in staged), staged
        assert run('branch','--show-current').decode().strip()==BRANCH
        run('diff','--cached','--check')
        print(run('commit','-m',a.message).decode())
        print(json.dumps({'commit':run('rev-parse','HEAD').decode().strip(),
                          'tree':run('rev-parse','HEAD^{tree}').decode().strip()}))
    elif a.action=='push':
        assert a.commit and run('rev-parse','HEAD').decode().strip()==a.commit
        print(run('push','origin','HEAD:refs/heads/'+BRANCH).decode())
        print(json.dumps({'pushed_commit':a.commit,'branch':BRANCH}))
    else:
        assert a.commit
        before=run('ls-remote',REMOTE,'refs/heads/'+BRANCH).decode().split()
        assert before and before[0]==a.commit, before
        cache=ROOT/'remote-readback.git'
        if not cache.exists():run('init','--bare',str(cache))
        run('fetch','--no-tags',REMOTE,a.commit,object_repo=cache)
        changed=run('diff','--name-status',CANDIDATE,a.commit).decode().splitlines()
        assert changed and all(x.startswith('A\t'+PREFIX) for x in changed), changed
        entries=run('ls-tree','-r',a.commit,'--',PREFIX,object_repo=cache).decode().splitlines()
        files=[]
        for line in entries:
            info,path=line.split('\t');mode,kind,blob=info.split()
            remote=run('cat-file','blob',blob,object_repo=cache)
            local=run('show',a.commit+':'+path)
            assert remote==local, path
            assert identity(remote)['git_blob']==blob
            assert mode=='100644' and kind=='blob'
            files.append({'path':path,'mode':mode,'type':kind,**identity(remote),
                          'full_remote_payload_read':True,'full_byte_equal_to_local_committed_payload':True})
        after=run('ls-remote',REMOTE,'refs/heads/'+BRANCH).decode().split()
        assert after==before
        receipt={'schema':'r6.review-remote-full-readback.v1','utc':dt.datetime.now(dt.timezone.utc).isoformat(),
                 'repository':REMOTE,'branch':BRANCH,'commit':a.commit,
                 'tree':run('rev-parse',a.commit+'^{tree}',object_repo=cache).decode().strip(),
                 'review_directory_tree':run('rev-parse',a.commit+':'+PREFIX.rstrip('/'),object_repo=cache).decode().strip(),
                 'base_candidate_commit':CANDIDATE,'changed_path_count':len(changed),
                 'report_file_count':len(files),'payload_bytes':sum(x['bytes'] for x in files),
                 'all_added_only_in_authorized_review_directory':True,'all_full_payloads_equal':True,'files':files,
                 'raw_command_capture':'operations/'+a.label+'.json (complete stdout/stderr/argv/UTC/exit; operational, excluded from recursive publication)',
                 'reference_or_host_execution':False}
        (ROOT/(a.label+'.json') if a.label=='remote-readback-core' else OPS/(a.label+'-receipt.json')).write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n')
        print(json.dumps({k:v for k,v in receipt.items() if k!='files'},ensure_ascii=False))
finally:
    (OPS/(a.label+'.json')).write_text(json.dumps({'action':a.action,'records':records},ensure_ascii=False,indent=2)+'\n')
