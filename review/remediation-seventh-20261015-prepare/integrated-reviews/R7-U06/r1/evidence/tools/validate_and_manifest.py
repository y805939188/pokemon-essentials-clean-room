import datetime, hashlib, json, os, pathlib, subprocess, sys
ROOT=pathlib.Path('/workspace/r7-ir-R7-U06')
REPO=ROOT/'result'
PREFIX='review/remediation-seventh-20261015-prepare/integrated-reviews/R7-U06/r1/'
OUT=REPO/PREFIX
B='e646432c644dec04d306842cc5a559a29c718fbc'
def git(*args):return subprocess.check_output(['git',*args],cwd=REPO)
def ident(data):return {'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest(),'git_blob':hashlib.sha1(f'blob {len(data)}\0'.encode()+data).hexdigest()}
def entries():
    return [{'path':str(p.relative_to(REPO)), 'git_mode':'100644', **ident(p.read_bytes())} for p in sorted(OUT.rglob('*')) if p.is_file() and p.name!='artifact-manifest.json']
assert git('branch','--show-current').decode().strip()=='codex/r7-ir-u06-20261015-r1'
assert git('merge-base',B,'HEAD').decode().strip()==B
for item in git('status','--porcelain','-uall','-z').decode().split('\0'):
    if item:assert item[3:].startswith(PREFIX),item
changed=git('diff','--name-only',B).decode().splitlines()
assert all(p.startswith(PREFIX) for p in changed)
assert not git('diff','--name-only',B,'--','deliverables','candidates','audit','planning','.agents','.codex').strip()
for p in OUT.rglob('*.json'):json.loads(p.read_text())
per=json.loads((OUT/'per-id.json').read_text())
input_receipt=json.loads((OUT/'review-input-receipt.json').read_text())
for row in input_receipt['supplemental_actual_consumers']:
    blob=git('show',row['fixed_commit']+':'+row['path'])
    expected={key:row[key] for key in ['bytes','sha256','git_blob']}
    assert ident(blob)==expected and pathlib.Path(row['local_path']).read_bytes()==blob
assert {r['record_id'] for r in per['records']}=={'GR7-M09-001','GR7-M10-001'}
assert all(r['verdict']=='WAIT' and not r['PASS_SCOPED_ACTUAL_INTEGRATION'] and not r['ACCEPTED'] and not r['CLOSED'] for r in per['records'])
vectors=[v for r in per['records'] for v in r['vectors']]
assert len(vectors)==30 and len({v['id'] for v in vectors})==30
for v in vectors:
    assert v['execution']=='NOT_EXECUTED' and v['independent_review_reason'] and v['common_premises']['content']
    row=v['actual_MI_row'];p=ROOT/'actual-input/actual'/row['path'];a,b=row['byte_offsets_zero_based_half_open']
    assert ident(p.read_bytes())==row['full_file_identity']
    assert p.read_bytes()[a:b].decode()==row['content'] and ident(p.read_bytes()[a:b])==row['slice_identity']
orig=ROOT/'original/evidence/tasks/R7-C17/limits-and-alias-reception.json'
assert orig.read_bytes()==(OUT/'evidence/limits-and-alias-reception.json').read_bytes()
for p in OUT.rglob('*'):
    if p.is_file():
        assert not p.is_symlink()
        assert 'reference/' not in str(p.relative_to(OUT)),p
if '--generate' in sys.argv:
    data={'schema':'r7.U06.actual-review-artifact-manifest.r1','utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'pid':os.getpid(),'branch':'codex/r7-ir-u06-20261015-r1','fixed_B':B,'allowed_prefix':PREFIX,'files':entries(),'self_binding':'This manifest cannot contain its own byte hash or the future commit hash. Its full bytes/mode are bound by the result commit/tree and complete remote per-file readback.','runtime':'TOOL_VALIDATION only; all behavior NOT_EXECUTED','ACCEPTED':False,'CLOSED':False}
    (OUT/'artifact-manifest.json').write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
manifest=json.loads((OUT/'artifact-manifest.json').read_text());assert manifest['files']==entries()
subprocess.run(['git','diff','--check',B],cwd=REPO,check=True)
print(json.dumps({'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'pid':os.getpid(),'artifacts_including_manifest':len(manifest['files'])+1,'bytes_including_manifest':sum(x['bytes'] for x in manifest['files'])+(OUT/'artifact-manifest.json').stat().st_size,'records':2,'vectors':30,'primary_verdicts':['WAIT','WAIT'],'scope':'ONLY_ALLOWED_PREFIX','formal_and_candidates_unchanged':True,'manifest':'ALL_NONSELF_BYTES_MATCH','kind':'TOOL_VALIDATION_NOT_BEHAVIOR_PASS'},ensure_ascii=False))
