"""Read fixed evidence objects and save actual public restoration provenance."""
import datetime
import gzip
import hashlib
import io
import json
from pathlib import Path
import shutil
import subprocess
import urllib.request

OUT=Path(__file__).resolve().parents[1]
CAN=Path('/workspace/r7-review-input/R7-U12-r1-1f33c39804d819c5a55a2b084287fc4a3a4c0919/candidate/candidates/R7-U12')
BOOT=Path('/workspace/r7-review-bootstrap/R7-U12-r1')
CTX=Path('/workspace/r7-context/R7-U12-reviewer')
def ident(b):return {'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'git_blob':hashlib.sha1(f'blob {len(b)}\0'.encode()+b).hexdigest()}
dest=OUT/'tool-evidence/inputs';dest.mkdir(exist_ok=True)
copies=[]
for root,name in [(BOOT,'candidate-input.json'),(BOOT,'candidate-restore/R7-U12.json'),(BOOT,'reviewer-dispatch.md'),
                  (BOOT,'mirror-diffs.patch'),(BOOT,'remote-readback.json'),(BOOT,'candidate-freeze-requirements.json'),(BOOT,'conflict-groups.json'),
                  (CTX,'dispatch/delegation/contracts/R7-U12.json'),
                  (Path('/workspace/r7-bootstrap/R7-U12-reviewer'),'tools/restore_container_context.py'),
                  (Path('/workspace/r7-bootstrap/R7-U12-reviewer'),'recovery/batches/R7-U12.json')]:
    target=dest/name;target.parent.mkdir(parents=True,exist_ok=True)
    data=(root/name).read_bytes();target.write_bytes(data);copies.append({'source':str(root/name),'evidence_path':str(target.relative_to(OUT)),**ident(data)})
for root in [CTX, CAN.parents[2]]:
    for path in root.glob('recovery-receipt-*.json'):
        target=dest/('original-' if root==CTX else 'candidate-')/path.name
        target.parent.mkdir(exist_ok=True);shutil.copyfile(path,target)
        copies.append({'source':str(path),'evidence_path':str(target.relative_to(OUT)),**ident(path.read_bytes())})
results=[]
for row in json.loads((CAN/'evidence/author/extra-recovery.json').read_text()):
    start=datetime.datetime.now(datetime.timezone.utc).isoformat()
    url='https://raw.githubusercontent.com/y805939188/pokemon-essentials-clean-room/'+row['publication_commit']+'/'+row['encoded_transport_path']
    with urllib.request.urlopen(url,timeout=40) as response:
        encoded=response.read(200000);status=response.status
    assert ident(encoded)['git_blob']==row['encoded_git_blob']
    with gzip.GzipFile(fileobj=io.BytesIO(encoded),mode='rb') as stream:decoded=stream.read(row['bytes']+1)
    actual=ident(decoded)
    assert all(actual[k]==row[k] for k in actual)
    assert decoded==(CAN/row['candidate_path'].split('candidates/R7-U12/',1)[1]).read_bytes()
    target=OUT/'tool-evidence/original-C01'/row['logical_path'];target.parent.mkdir(parents=True,exist_ok=True)
    target.write_bytes(decoded)
    results.append({'logical_path':row['logical_path'],'url':url,'start_utc':start,'end_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
                    'http_status':status,'encoded_identity':ident(encoded),'decoded_identity':actual,'matches_author_retained_copy':True,'reexecuted':False})
baseline='e646432c644dec04d306842cc5a559a29c718fbc';dispatch='95c260d8f3fb4a171675dde877137fcd4c2f1c8d'
skill_checks=[]
for commit in [baseline,dispatch]:
    r=subprocess.run(['git','ls-tree','-r','--name-only',commit,'.agents'],capture_output=True,text=True,check=True)
    skill_checks.append({'commit':commit,'argv':['git','ls-tree','-r','--name-only',commit,'.agents'],'stdout':r.stdout,'stderr':r.stderr,'exit_code':r.returncode})
result={'schema':'r7.u12.reviewer-extra-provenance.v1','stage':'TOOL_VALIDATION','snapshot_copies':copies,
        'original_C01_pinned_remote_objects':results,'decoded_files':len(results),'decoded_bytes':sum(r['decoded_identity']['bytes'] for r in results),
        'skills':skill_checks,'workspace_agents_entries':[p.name for p in Path('/workspace/.agents').iterdir()],
        'source_programs_executed':0,'qualification':'Evidence independently reread from fixed C2. Initial file copies preserve actual earlier recovery receipts; copies are not fabricated earlier command logs.'}
(OUT/'tool-evidence/provenance-receipt.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'original_C01_files':len(results),'decoded_bytes':result['decoded_bytes'],'skills':'No project/workspace .agents skill files available','stage':'TOOL_VALIDATION'},ensure_ascii=False))
