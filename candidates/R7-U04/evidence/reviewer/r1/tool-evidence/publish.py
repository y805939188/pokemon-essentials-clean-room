"""Ordinary commits/pushes restricted to this reviewer's sole authorized branch."""
import argparse
import datetime
import hashlib
import json
import os
from pathlib import Path
import subprocess

TOOLS=Path(__file__).resolve().parent
REPO=TOOLS.parents[5]
PREFIX='candidates/R7-U04/evidence/reviewer/r1/'
BRANCH='codex/r7-u04-reviewer-20261015-r1'
BASE='e646432c644dec04d306842cc5a559a29c718fbc'
parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--stage',choices=['payload','evidence'],required=True)
args=parser.parse_args()
records=[]
def now():return datetime.datetime.now(datetime.timezone.utc).isoformat()
def git(*argv):
    start=now();run=subprocess.run(['git',*argv],cwd=REPO,capture_output=True)
    record=dict(argv=['git',*argv],start_utc=start,end_utc=now(),exit_code=run.returncode,stdout=run.stdout.decode(),stderr=run.stderr.decode())
    records.append(record)
    assert run.returncode==0,record
    return run.stdout.decode().strip()
assert os.environ.get('CODEX_THREAD_ID')=='01a13f7e-d577-727a-9565-f64f6a663024'
assert git('branch','--show-current')==BRANCH
git('merge-base','--is-ancestor',BASE,'HEAD')
before=git('ls-remote','--heads','origin',BRANCH)
if args.stage=='payload':
    assert before==''
    assert git('rev-parse','HEAD')==BASE
else:
    payload=json.loads((TOOLS/'payload-publication.json').read_bytes())
    assert before==payload['commit']+'\trefs/heads/'+BRANCH
    assert git('rev-parse','HEAD')==payload['commit']
manifest=json.loads((TOOLS.parent/'artifact-manifest.json').read_bytes())
for row in manifest['files']:
    data=(REPO/row['path']).read_bytes()
    assert len(data)==row['bytes'] and hashlib.sha256(data).hexdigest()==row['sha256']
    assert hashlib.sha1(f'blob {len(data)}\0'.encode()+data).hexdigest()==row['git_blob']
git('add','--',PREFIX)
git('diff','--cached','--check')
changed=git('diff','--cached','--name-only').splitlines()
assert changed and all(p.startswith(PREFIX) for p in changed)
all_changed=git('diff','--cached','--name-only',BASE).splitlines()
assert all(p.startswith(PREFIX) for p in all_changed)
git('commit','-m','Add independent R7 U04 r1 candidate review' if args.stage=='payload' else 'Record complete remote readback for R7 U04 r1 review')
commit=git('rev-parse','HEAD');tree=git('rev-parse','HEAD^{tree}')
git('push','origin','HEAD:refs/heads/'+BRANCH)
after=git('ls-remote','--heads','origin',BRANCH)
assert after==commit+'\trefs/heads/'+BRANCH
result=dict(schema='r7.u04.r1.publication.v1',stage=args.stage,pid=os.getpid(),actual_thread_id=os.environ.get('CODEX_THREAD_ID'),commit=commit,tree=tree,branch=BRANCH,base=BASE,ordinary_push=True,ls_remote_before=before,ls_remote_after=after,public_commands=records,qualification='Commit/push and ref readback only. Complete HTTP body readback is a separate tool invocation.')
if args.stage=='payload':
    with (TOOLS/'payload-publication.json').open('x') as stream:stream.write(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(result,ensure_ascii=False))
