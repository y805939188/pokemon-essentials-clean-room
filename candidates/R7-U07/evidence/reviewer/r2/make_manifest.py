"""Inventory reviewer evidence. Manifest self is bound by final Git commit/tree."""
import datetime,hashlib,json,os
from pathlib import Path
E=Path(__file__).resolve().parent;root=Path('/workspace/r7-u07-reviewer-r2')
rows=[]
for p in sorted(E.rglob('*')):
 if not p.is_file() or p==E/'artifact-manifest.json':continue
 assert not p.is_symlink()
 d=p.read_bytes();rows.append({'path':str(p.relative_to(root)),'bytes':len(d),'sha256':hashlib.sha256(d).hexdigest(),'git_blob':hashlib.sha1(f'blob {len(d)}\0'.encode()+d).hexdigest(),'git_mode':'100644','role':'reviewer_evidence_or_public_tool_io','base_B':'NEW_REVIEWER_EVIDENCE_FILE'})
v={'schema':'r7.u07.r2.reviewer-artifact-manifest.v1','utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'actual_context':os.environ['CODEX_THREAD_ID'],'batch_id':'R7-U07','required_ids':['GR7-M12-001'],'verdict':'PASS_SCOPED_CANDIDATE','base_commit':'e646432c644dec04d306842cc5a559a29c718fbc','output_branch':'codex/r7-u07-reviewer-20261015-r2','write_prefix':'candidates/R7-U07/evidence/reviewer/r2/','dispatch_commit':'c64774c60d91e522cb515ef71e3e9d4ea6b4712c','freeze_commit':'aa369555b0e8b6c8b077f964b54ed63d3b924f26','candidate_commit':'2649ed2bd2cc3afdfa636cd643fc1975de5eae32','candidate_tree':'6b2e6a6122cb24b330a052137750dc985908e796','files':rows,'declared_nonself_file_count':len(rows),'declared_nonself_bytes':sum(x['bytes'] for x in rows),'self_binding':'This manifest and complete result are bound by actual final result commit/tree plus exhaustive fixed-commit remote byte readback in final tool return. Self hash intentionally not recursive.','candidate_mirrors_carried':False,'effective_configuration':{k:'UNVERIFIED' for k in ['model','effort','tier','speed']},'behavior_vectors':'NOT_EXECUTED','prior_r1_final_WAIT':'RETAINED_UNWAIVED','integrated_PASS':False,'ACCEPTED':False,'CLOSED':False}
(E/'artifact-manifest.json').write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'manifest_nonself_files':len(rows),'manifest_nonself_bytes':v['declared_nonself_bytes'],'total_files_including_manifest':len(rows)+1}))
