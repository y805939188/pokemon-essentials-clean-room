"""Validate and manifest only this task's review deliverables."""
from pathlib import Path
import datetime,hashlib,json,subprocess
root=Path(__file__).resolve().parent.parent
repo=Path.cwd().resolve()
prefix=root.relative_to(repo).as_posix()+'/'
def identity(b):return {'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'git_blob':hashlib.sha1(f'blob {len(b)}\0'.encode()+b).hexdigest()}
r=json.loads((root/'per-id.json').read_bytes());assert len(r['records'])==3
vectors=0
for record in r['records']:
 assert record['verdict']=='PASS_SCOPED_ACTUAL_INTEGRATION' and not record['formal_ACCEPTED'] and not record['CLOSED']
 for a in record['actual_clauses']+[v['actual_anchor'] for v in record['vectors']]:
  b=subprocess.check_output(['git','show',a['commit']+':'+a['path']]);assert identity(b)==a['file_identity'];lo,hi=a['byte_offsets_half_open'];assert identity(b[lo:hi])==a['span_identity']
 vectors+=len(record['vectors'])
assert vectors==21
for p in root.rglob('*.json'):json.loads(p.read_bytes())
changed=subprocess.check_output(['git','diff','--name-only','e646432c644dec04d306842cc5a559a29c718fbc']).decode().splitlines()
assert all(p.startswith(prefix) for p in changed)
validation={'schema':'r7.ir-artifact-validation.v1','utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'records':3,'vector_rows':21,'actual_anchors_match_MI':True,'all_json_parse':True,'existing_changed_paths_within_write_prefix':True,'semantic_credit_from_this_tool':False,'domain_execution':0}
(root/'tool-evidence/artifact-validation.json').write_text(json.dumps(validation,indent=2)+'\n')
files=[]
for p in sorted(root.rglob('*')):
 if p.is_file() and p.name!='artifact-manifest.json':
  assert not p.is_symlink();files.append({'path':p.relative_to(repo).as_posix(),'git_mode':'100644',**identity(p.read_bytes())})
manifest={'schema':'r7.ir-artifact-manifest.v1','branch':'codex/r7-ir-u04-u05-20261015-r1','base':'e646432c644dec04d306842cc5a559a29c718fbc','allowed_prefix':prefix,'files':files,'file_count_excluding_self':len(files),'bytes_excluding_self':sum(r['bytes'] for r in files),'self_binding':'Excluded from self-hash; manifest and all final files bound by actual result commit/tree and final full remote readback.','ACCEPTED':False,'CLOSED':False}
(root/'artifact-manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'status':'ARTIFACT_CHECKS_PASS','files_including_manifest':len(files)+1,'vectors':21,'semantic_credit':False}))
