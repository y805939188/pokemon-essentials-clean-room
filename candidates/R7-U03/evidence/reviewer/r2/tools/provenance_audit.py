"""Re-read precise immutable administrative inputs; verify supplemental identities."""
import concurrent.futures
import datetime
import hashlib
import json
from pathlib import Path
import subprocess
import urllib.parse
import urllib.request

OUT=Path(__file__).resolve().parents[1]
REPO=OUT.parents[4]
BOOT=Path('/workspace/r7-review-bootstrap/R7-U03-r2')
CTX=Path('/workspace/r7-context/R7-U03-reviewer')
D='c64774c60d91e522cb515ef71e3e9d4ea6b4712c'
F='aa369555b0e8b6c8b077f964b54ed63d3b924f26'
OLD='e75aa46a17e99bcc17795e051461a727c795aa6c'
CON='f622356f3beb9e84ea8cff9db07c7fb382565d3f'
BASE='review/remediation-seventh-20261015-prepare/'

def ident(d):
    return dict(bytes=len(d),sha256=hashlib.sha256(d).hexdigest(),git_blob=hashlib.sha1(f'blob {len(d)}\0'.encode()+d).hexdigest())

def git(*a):return subprocess.check_output(['git','-C',str(REPO),*a])

rows=[(D,BASE+'review-rechecks/R7-U03/r2/reviewer-dispatch.md',Path('/workspace/r7-bootstrap/R7-U03-reviewer/reviewer-dispatch.md')),
      (D,BASE+'delegation/parallel-dispatch/candidate-freeze-requirements.json',BOOT/'candidate-freeze-requirements.json'),
      (D,BASE+'delegation/conflict-groups.json',BOOT/'conflict-groups.json')]
for name in ['candidate-input.json','mirror-diffs.patch','remote-readback.json']:
    rows.append((F,BASE+'candidate-freezes/R7-U03/'+name,BOOT/name))
rows.append((F,BASE+'candidate-freezes/R7-U03/candidate-restore/R7-U03.json',BOOT/'candidate-restore/R7-U03.json'))
for name in ['report.md','per-id.json','review-input-receipt.json','artifact-manifest.json']:
    rows.append((OLD,'candidates/R7-U03/evidence/reviewer/r1/'+name,BOOT/'prior-r1'/name))
for batch in ['R7-U01','R7-U09','R7-U13']:
    rows.append((CON,BASE+'delegation/contracts/'+batch+'.json',BOOT/'shared-contracts'/(batch+'.json')))

def reread(row):
    commit,path,local=row
    u='https://raw.githubusercontent.com/y805939188/pokemon-essentials-clean-room/'+commit+'/'+urllib.parse.quote(path)
    start=datetime.datetime.now(datetime.timezone.utc).isoformat()
    with urllib.request.urlopen(u,timeout=40) as r:d=r.read(local.stat().st_size+1);status=r.status
    assert status==200 and d==local.read_bytes(),path
    a=ident(d)
    if commit!=CON:
        t=git('ls-tree',commit,path).decode().split();assert t[:3]==['100644','blob',a['git_blob']],t
    return dict(commit=commit,path=path,url=u,local_path=str(local),start_utc=start,end_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),http_status=status,complete_bytes_match=True,**a)

with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
    files=list(pool.map(reread,rows))

inventory=json.loads((CTX/'supplement/9f68b18a4a3f12cff0b452977d24171aca0165b74f3a50a615c95f9927f9765c.raw').read_bytes())
supp=[]
for path in ['Data/Scripts/001_Technical/002_RubyUtilities.rb','Data/Scripts/010_Data/002_PBS data/018_MapMetadata.rb']:
    p=CTX/'supplement/reference'/path;d=p.read_bytes();a=ident(d)
    expected=next(r for r in inventory if r['path']==path)
    assert a['bytes']==expected['bytes'] and a['sha256']==expected['sha256']
    blob=expected.get('git_blob',expected.get('blob'))
    if blob:assert blob==a['git_blob']
    supp.append(dict(path=path,local_path=str(p),fixed_R='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b',source_inventory_identity=expected,**a))

absent={}
for commit in ['e646432c644dec04d306842cc5a559a29c718fbc',D]:
    v=git('ls-tree','-r','--name-only',commit,'.agents').decode();assert not v
    absent[commit]=dict(agents_tree_entries=[],skills_present=False)

result=dict(stage='TOOL_VALIDATION',files=files,supplemental_reference=supp,skills_check=absent,
            prior_r1_qualification='Original two content PASS statements and pre-contract read-only AI auxiliary disclosure preserved at fixed OLD. R7-I process qualification remains WAIT_INPUT_OR_INDEPENDENCE; neither waiver nor semantic migration.',
            qualification='Exact byte/metadata checks only. Shared contracts read only for clause receiver boundaries; no review of other candidates.')
(OUT/'provenance-audit.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(immutable_administrative_files_reread=len(files),supplemental_reference_files=len(supp),skills_present=False,old_r1_unchanged=True,stage='TOOL_VALIDATION')))
