"""Validate review publication scope and artifact binding; no behavior execution."""
import hashlib, json, pathlib, subprocess

ROOT=pathlib.Path(__file__).resolve().parent.parent
REPO=ROOT.parents[4]
BASE='e646432c644dec04d306842cc5a559a29c718fbc'
PREFIX='candidates/R7-U01/evidence/reviewer/r1/'

def git(*args): return subprocess.check_output(['git',*args],cwd=REPO).decode().strip()
def identity(data):
    return dict(bytes=len(data),sha256=hashlib.sha256(data).hexdigest(),git_blob=hashlib.sha1(f'blob {len(data)}\0'.encode()+data).hexdigest())

assert git('branch','--show-current')=='codex/r7-u01-reviewer-20261015-r1'
changes=git('diff','--name-only',BASE).splitlines()+git('ls-files','--others','--exclude-standard').splitlines()
assert changes and all(p.startswith(PREFIX) for p in changes), changes
assert not git('diff',BASE,'--','.',':(exclude)'+PREFIX)
assert git('rev-parse',BASE+':deliverables/final-specification-set')=='ebbe29f2bc88cd17de7072bf440c6fa8c8c7089c'
per=json.loads((ROOT/'per-id.json').read_text())
assert [(r['id'],r['conclusion']) for r in per['records']]==[('GR7-M01-001','PASS_SCOPED_CANDIDATE'),('GR7-J01-001','FAIL_SCOPED_CANDIDATE')]
assert all(v['behavior_execution']=='NOT_EXECUTED' for r in per['records'] for v in r['vectors'])
assert not any(per[k] for k in ['integrated_PASS','ACCEPTED','CLOSED'])
receipt=json.loads((ROOT/'review-input-receipt.json').read_text())
assert receipt['identity']['different_context_confirmed'] and receipt['identity']['subtasks_created']==0
assert receipt['candidate_commit']=='de550bb9fe5d2b80312b1a4f6f166d2a6aa5fc67'
assert all(v=='UNVERIFIED' for v in receipt['configuration']['effective'].values())
files=sorted(p for p in ROOT.rglob('*') if p.is_file())
for p in files:
    assert not p.is_symlink()
    if p.suffix=='.json':json.loads(p.read_text())
manifest=ROOT/'artifact-manifest.json'
rows=[dict(path=str(p.relative_to(REPO)),**identity(p.read_bytes())) for p in files if p!=manifest]
manifest.write_text(json.dumps(dict(schema='r7.u01-reviewer-artifact-manifest.v1',base_commit=BASE,reviewer_context=receipt['identity']['actual_context'],
    candidate_commit=receipt['candidate_commit'],candidate_tree=receipt['candidate_tree'],files=rows,
    self_identity='Manifest own bytes/blob are bound externally by final commit/tree and exact final remote readback; no recursive self-hash assertion.',
    phase='Independent scoped static candidate review; no integrated PASS, ACCEPTED or CLOSED.'),ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(status='PASS_OUTPUT_SCOPE_AND_IDENTITIES_ONLY',files_excluding_self=len(rows),write_prefix=PREFIX,
                     M01='PASS_SCOPED_CANDIDATE',J01='FAIL_SCOPED_CANDIDATE',behavior='NOT_EXECUTED')))
