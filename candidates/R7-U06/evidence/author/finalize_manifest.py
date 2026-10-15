"""Bind complete mirrors and all existing supporting files, excluding self-hash."""
import datetime
import hashlib
import json
from pathlib import Path
import subprocess

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[3]
PREFIX=ROOT/'candidates/R7-U06'
B='e646432c644dec04d306842cc5a559a29c718fbc'
def identity(data):
    return dict(bytes=len(data),sha256=hashlib.sha256(data).hexdigest(),
        git_blob_content_id=hashlib.sha1(f'blob {len(data)}\0'.encode()+data).hexdigest())
mirrors=[]; support=[]
for p in sorted(PREFIX.rglob('*')):
    if not p.is_file() or p==HERE/'artifact-manifest.json':continue
    relative=str(p.relative_to(ROOT));actual=identity(p.read_bytes())
    if p.is_relative_to(PREFIX/'deliverables'):
        formal=str(p.relative_to(PREFIX))
        old=subprocess.check_output(['git','show',B+':'+formal],cwd=ROOT)
        mirrors.append(dict(candidate_path=relative,original_path=formal,original_B=identity(old),candidate=actual))
    else:
        support.append(dict(path=relative,**actual))
manifest={'schema':'r7.u06.author-artifact-manifest.v1',
    'status':'CANDIDATE_READY_NOT_REVIEWED','created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'B':B,'branch':'codex/r7-u06-author-20261015-wave1','complete_mirrors':mirrors,'supporting_files':support,
    'self_hash_rule':'This manifest excludes its own identity. Final immutable Git commit/tree and full remote readback bind every file including this manifest.',
    'publication_binding':'Final commit/tree and final post-push receipt are external to that commit. Earlier publication receipts explicitly identify their subject commit.',
    'conditional_WP43':'NOT_CREATED_NO_CONTRADICTION','formal_files_modified':False,
    'forbidden_writes':'No formal/reference/other batch/public ledger/main/tag/integration branch changes.'}
(HERE/'artifact-manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'complete_mirrors':len(mirrors),'supporting_files':len(support),'manifest':'candidates/R7-U06/evidence/author/artifact-manifest.json'}))
