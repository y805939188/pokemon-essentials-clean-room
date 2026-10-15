"""Inventory complete new payload. Own bytes are externally bound by candidate commit/readback."""
from pathlib import Path
import datetime,hashlib,json
E=Path(__file__).resolve().parent;ROOT=E.parents[1]
def identity(b):return {'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'git_blob_content_id':hashlib.sha1(f'blob {len(b)}\0'.encode()+b).hexdigest()}
recipe=json.loads((E/'edits.json').read_bytes());mirrors={r['path']:r for r in recipe['mirrors']}
rows=[]
for p in sorted(ROOT.rglob('*')):
 if not p.is_file() or p.name=='artifact-manifest.json':continue
 name=str(p.relative_to(Path.cwd()));row={'path':name,'new':identity(p.read_bytes()),'kind':'complete_candidate_mirror' if name in mirrors else 'author_evidence'}
 if name in mirrors:row.update({'base_commit':mirrors[name]['base_commit'],'base_path':mirrors[name]['formal_path'],'base':mirrors[name]['base']})
 else:row['base']='ABSENT_NEW_FILE'
 rows.append(row)
rows.append({'path':str(E.relative_to(Path.cwd())/'artifact-manifest.json'),'kind':'manifest','base':'ABSENT_NEW_FILE','new':None,'binding':'Own bytes/SHA/blob in immutable post-commit remote readback; cannot self-hash.'})
out={'schema':'r7.u11.artifact-manifest.v1','created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'batch_id':'R7-U11','status':'CANDIDATE_READY_NOT_REVIEWED','base_commit':'e646432c644dec04d306842cc5a559a29c718fbc','base_root_tree':'84f79ec6e772aacbf3a464fde68cdc5a280e2950','base_formal_subtree':'ebbe29f2bc88cd17de7072bf440c6fa8c8c7089c','branch':'codex/r7-u11-author-20261015-wave1','files':rows,'write_set':'Only four required complete mirrors and evidence/author under candidates/R7-U11; conditional specs/demo not created.','remote_receipt':'/workspace/r7-bootstrap/R7-U11-author/final-publication-receipt.json and platform public tool I/O, created after candidate commit','commit_tree_binding':'Actual commit and tree are reported by post-commit publication; never precomputed or self-asserted.'}
(E/'artifact-manifest.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'status':'MANIFEST_CREATED','files_including_self':len(rows),'mirrors':len(mirrors),'other_evidence':len(rows)-len(mirrors)-1,'identity_self_reference':'EXTERNAL_COMMIT_AND_READBACK_BINDING'}))
