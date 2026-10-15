"""Validate final review package scope and identities; no behavior execution."""
import hashlib,json,subprocess
from pathlib import Path
E=Path(__file__).resolve().parent;root=Path('/workspace/r7-u07-reviewer-r2');prefix='candidates/R7-U07/evidence/reviewer/r2/';base='e646432c644dec04d306842cc5a559a29c718fbc'
def git(*args):return subprocess.check_output(['git',*args],cwd=root).decode()
assert git('branch','--show-current').strip()=='codex/r7-u07-reviewer-20261015-r2'
assert git('merge-base',base,'HEAD').strip()==base
assert git('rev-parse','HEAD:deliverables/final-specification-set').strip()=='ebbe29f2bc88cd17de7072bf440c6fa8c8c7089c'
for path in git('diff','--name-only',base).splitlines()+git('ls-files','--others','--exclude-standard').splitlines():assert path.startswith(prefix),path
m=json.loads((E/'artifact-manifest.json').read_bytes());rows=m['files'];expected={x['path'] for x in rows}
actual={str(p.relative_to(root)) for p in E.rglob('*') if p.is_file()}
assert actual==expected|{prefix+'artifact-manifest.json'},(actual-expected,expected-actual)
assert len(rows)==m['declared_nonself_file_count']
for row in rows:
 d=(root/row['path']).read_bytes();assert len(d)==row['bytes'];assert hashlib.sha256(d).hexdigest()==row['sha256'];assert hashlib.sha1(f'blob {len(d)}\0'.encode()+d).hexdigest()==row['git_blob']
for p in E.rglob('*.json'):json.loads(p.read_bytes())
per=json.loads((E/'per-id.json').read_bytes());assert len(per['records'])==1 and per['records'][0]['record_id']=='GR7-M12-001'
assert per['records'][0]['decision']==m['verdict']=='PASS_SCOPED_CANDIDATE'
assert per['independence']['different_visible_actual_contexts'] and per['independence']['subtasks_created']==0
assert [x['id'] for x in per['records'][0]['vectors']]==['GR7-M12-001-C'+str(i) for i in range(1,7)]
assert all(x['execution']=='NOT_EXECUTED' for x in per['records'][0]['vectors'])
assert set(per['configuration']['effective'].values())=={'UNVERIFIED'}
assert all(x=='NOT_ASSERTED' for k,x in per['gates'].items() if k!='candidate')
a=json.loads((E/'input-validation.json').read_bytes());assert a['candidate_files_count']==32 and a['candidate_bytes']==241426 and len(a['author_manifest_checked_declarations'])==31
assert len(a['bound_raw_refs_verified'])==54
print(json.dumps({'status':'REVIEW_ARTIFACT_IDENTITIES_SCOPE_JSON_AND_QUALIFICATIONS_VALIDATED','files_including_manifest':len(actual),'bytes_including_manifest':sum(p.stat().st_size for p in E.rglob('*') if p.is_file()),'decision':'PASS_SCOPED_CANDIDATE','behavior_execution':'NOT_EXECUTED','effective_config':'UNVERIFIED','write_prefix':prefix,'qualification':'TOOL_VALIDATION only'}))
