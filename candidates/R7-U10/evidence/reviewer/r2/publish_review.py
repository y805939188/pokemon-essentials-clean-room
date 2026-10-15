"""Ordinary scoped commits/pushes with exhaustive immutable remote byte readback."""
import concurrent.futures
import datetime
import hashlib
import json
import os
from pathlib import Path
import subprocess
import urllib.parse
import urllib.request

ROOT = Path('/workspace/r7-u10-reviewer-r2')
PREFIX = 'candidates/R7-U10/evidence/reviewer/r2/'
OUT = ROOT/PREFIX
TRANSPORT = Path('/workspace/r7-review-bootstrap/R7-U10-r2/publication')
BRANCH = 'codex/r7-u10-reviewer-20261015-r2'
B = 'e646432c644dec04d306842cc5a559a29c718fbc'
TRANSPORT.mkdir(parents=True,exist_ok=True)
commands=[]

def utc():
    return datetime.datetime.now(datetime.timezone.utc).isoformat()

def identity(data):
    return dict(bytes=len(data),sha256=hashlib.sha256(data).hexdigest(),
                git_blob=hashlib.sha1(f'blob {len(data)}\0'.encode()+data).hexdigest())

def run(argv):
    start=utc()
    process=subprocess.Popen(argv,cwd=ROOT,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    stdout,stderr=process.communicate()
    row={'argv':argv,'cwd':str(ROOT),'start_utc':start,'end_utc':utc(),
         'pid':process.pid,'exit_code':process.returncode,'stdout':stdout.decode(),
         'stderr':stderr.decode()}
    commands.append(row)
    (TRANSPORT/'commands-current.json').write_text(json.dumps(commands,ensure_ascii=False,indent=2)+'\n')
    if process.returncode:
        raise RuntimeError(json.dumps(row,ensure_ascii=False))
    return stdout

def manifest():
    rows=[]
    for path in sorted(OUT.rglob('*')):
        if path.is_file() and path.name!='artifact-manifest.json':
            assert not path.is_symlink()
            rows.append({'path':str(path.relative_to(ROOT)),**identity(path.read_bytes())})
    value={'schema':'r7.u10.r2.reviewer-artifact-manifest.v1','created_utc':utc(),
           'base_commit':B,'branch':BRANCH,'scope':PREFIX,'files':rows,
           'self_binding':'Manifest excludes only its own bytes. Exact output commit/tree and exhaustive immutable remote readback bind manifest itself. Final readback is returned outside its own commit.',
           'integrated_PASS':False,'ACCEPTED':False,'CLOSED':False}
    (OUT/'artifact-manifest.json').write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n')

def commit_and_push(message, expected_parent):
    assert run(['git','branch','--show-current']).decode().strip()==BRANCH
    assert run(['git','rev-parse','HEAD']).decode().strip()==expected_parent
    assert not run(['git','diff','--name-only',B,'--','.',':(exclude)'+PREFIX]).strip()
    extras=run(['git','ls-files','--others','--exclude-standard','-z']).decode().split('\0')
    assert all(not p or p.startswith(PREFIX) for p in extras)
    manifest()
    run(['git','add','--',PREFIX])
    staged=run(['git','diff','--cached','--name-only','-z']).decode().split('\0')
    assert all(not p or p.startswith(PREFIX) for p in staged)
    run(['git','diff','--cached','--check','--',PREFIX,':(exclude)'+PREFIX+'logs/',
         ':(exclude)'+PREFIX+'independent-mirror-diffs.patch'])
    run(['git','commit','-m',message])
    commit=run(['git','rev-parse','HEAD']).decode().strip()
    assert run(['git','rev-parse','HEAD^']).decode().strip()==expected_parent
    run(['git','push','origin','HEAD:refs/heads/'+BRANCH])
    return commit

def readback(commit, label):
    remote=run(['git','ls-remote','--heads','origin','refs/heads/'+BRANCH]).decode().strip()
    assert remote.split()[0]==commit
    run(['git','fetch','--no-tags','--depth=1','origin','refs/heads/'+BRANCH])
    assert run(['git','rev-parse','FETCH_HEAD']).decode().strip()==commit
    tree=run(['git','rev-parse','FETCH_HEAD^{tree}']).decode().strip()
    diff=run(['git','diff','--name-status',B,commit]).decode().splitlines()
    changes=[line.split('\t') for line in diff]
    assert all(s=='A' and p.startswith(PREFIX) for s,p in changes)
    entries=[]
    for raw in run(['git','ls-tree','-r','-z',commit,'--',PREFIX]).split(b'\0'):
        if not raw:continue
        meta,path=raw.decode().split('\t');mode,typ,blob=meta.split()
        assert mode=='100644' and typ=='blob'
        data=(ROOT/path).read_bytes()
        assert identity(data)['git_blob']==blob
        entries.append({'path':path,'mode':mode,**identity(data)})
    assert {p for s,p in changes}=={r['path'] for r in entries}
    destination=TRANSPORT/(label+'-bytes')
    destination.mkdir(exist_ok=False)
    def fetch(row):
        url='https://raw.githubusercontent.com/y805939188/pokemon-essentials-clean-room/'+commit+'/'+urllib.parse.quote(row['path'])
        start=utc()
        with urllib.request.urlopen(url,timeout=60) as response:
            data=response.read(row['bytes']+1);status=response.status
        assert identity(data)=={k:row[k] for k in ['bytes','sha256','git_blob']}
        assert data==(ROOT/row['path']).read_bytes()
        path=destination/row['path'];path.parent.mkdir(parents=True,exist_ok=True)
        path.write_bytes(data)
        return {**row,'url':url,'http_status':status,'start_utc':start,'end_utc':utc(),
                'complete_byte_match':True,'local_readback':str(path)}
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        files=list(pool.map(fetch,entries))
    result={'schema':'r7.u10.r2.exhaustive-remote-readback.v1','status':'ALL_RESULT_BYTES_VERIFIED',
            'utc':utc(),'branch':BRANCH,'commit':commit,'tree':tree,'remote_ref_line':remote,
            'base_commit':B,'complete_diff_against_B':changes,'files':files,
            'files_verified':len(files),'bytes_verified':sum(r['bytes'] for r in files),
            'all_modes':'100644','outside_scope_diff':False,'force_push':False,
            'qualification':'Exact remote bytes, modes, scope and immutable commit/tree only; independent semantic conclusions remain scoped candidate review.',
            'integrated_PASS':False,'ACCEPTED':False,'CLOSED':False}
    (TRANSPORT/(label+'.json')).write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    return result

assert not run(['git','ls-remote','--heads','origin','refs/heads/'+BRANCH]).strip(), 'Protect existing remote branch; no alternate branch or force'
first=commit_and_push('Review frozen R7-U10 candidate independently in r2',B)
first_receipt=readback(first,'first-remote-readback')
archive=OUT/'publication';archive.mkdir(exist_ok=False)
(archive/'first-remote-readback.json').write_text(json.dumps(first_receipt,ensure_ascii=False,indent=2)+'\n')
(archive/'first-publication-commands.json').write_text(json.dumps(commands,ensure_ascii=False,indent=2)+'\n')
final=commit_and_push('Archive R7-U10 r2 complete remote reception evidence',first)
receipt=readback(final,'final-remote-readback')
assert not run(['git','status','--porcelain']).strip()
(TRANSPORT/'commands-final.json').write_text(json.dumps(commands,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:receipt[k] for k in ['status','branch','commit','tree','files_verified','bytes_verified']},ensure_ascii=False,indent=2))
print('FINAL_READBACK',TRANSPORT/'final-remote-readback.json')
