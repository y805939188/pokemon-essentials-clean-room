"""Inventory reviewer artifacts; the manifest itself is bound by published Git commit/tree."""
import datetime,hashlib,json,pathlib
O=pathlib.Path(__file__).resolve().parents[1];W=O.parents[4]
rows=[]
for p in sorted(O.rglob('*')):
 if p.is_file() and p!=O/'artifact-manifest.json':
  b=p.read_bytes();rows.append({'path':str(p.relative_to(W)),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'git_blob':hashlib.sha1(f'blob {len(b)}\0'.encode()+b).hexdigest(),'mode':'100644'})
d={'schema':'r7.u08.reviewer-artifact-manifest.v1','generated_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'base':'e646432c644dec04d306842cc5a559a29c718fbc','branch':'codex/r7-u08-reviewer-20261015-r1','candidate_commit':'d6e07340aa14eb8b45728020cad018a22d7559b2','candidate_tree':'ed37cf1d27414f8f7411f079f1f717e55f3213a3','reviewer_thread_id':'01a13ff0-a716-77b3-bbda-7ad40ff90032','exact_write_prefix':'candidates/R7-U08/evidence/reviewer/r1/','files':rows,'manifest_self_identity':'Own exact bytes bound by resulting commit/tree and final complete remote readback; excluded from own content inventory.','qualification':'Reviewer evidence only; no author mirror or reference source included; final publication readback necessarily external to the self-containing commit.'}
(O/'artifact-manifest.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n');print('manifest_files_without_self',len(rows),'bytes_without_self',sum(x['bytes'] for x in rows))
