"""Inventory complete candidate bytes; own identity must be bound by final remote receipt."""
from pathlib import Path
import json,hashlib,subprocess,datetime
ROOT=Path(__file__).resolve().parents[4];base=ROOT/'candidates/R7-U10';out=base/'evidence/author'
B='e646432c644dec04d306842cc5a559a29c718fbc'
def ident(b):return {'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'git_blob_content_id':hashlib.sha1(f'blob {len(b)}\0'.encode()+b).hexdigest()}
v=json.loads((out/'validation.json').read_text())
files=[]
for p in sorted(base.rglob('*')):
 if not p.is_file() or p==out/'artifact-manifest.json':continue
 rel=p.relative_to(ROOT).as_posix();entry={'path':rel,'new':ident(p.read_bytes())}
 mirror=next((x for x in v['mirrors'] if x['candidate_path']==rel),None)
 if mirror:entry.update({'original_path':mirror['original_path'],'base_commit':B,'base':mirror['base'],'scope_changes':mirror['changes']})
 else:entry.update({'original_path':None,'base':'ABSENT_AT_B; new author evidence only'})
 files.append(entry)
j={'schema':'r7.u10.author.artifact-manifest.v1','status':'CANDIDATE_READY_NOT_REVIEWED','created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'base_commit':B,'branch':'codex/r7-u10-author-20261015-wave1','complete_mirror_count':5,'files':files,'self_identity_rule':'This manifest excludes only its own bytes to avoid circular hashes. Exact final manifest and every newly committed file identity are bound by the immutable-commit full remote readback receipt outside the candidate. No untracked candidate deliverables are excluded.','final_remote_receipt':'/workspace/r7-bootstrap/R7-U10-author/remote-readback-final/receipt.json'}
(out/'artifact-manifest.json').write_text(json.dumps(j,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'inventoried_nonself_files':len(files),'mirrors':sum('base_commit' in x for x in files)},ensure_ascii=False))
