"""Reviewer-owned bounded identity/range checks. No behavior/source programs run."""
import datetime
import difflib
import gzip
import hashlib
import json
import os
from pathlib import Path
import subprocess
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
CTX = Path('/workspace/r7-context/R7-U03-reviewer')
BOOT = Path('/workspace/r7-review-bootstrap/R7-U03-r2')
INPUT = Path('/workspace/r7-review-input/R7-U03-r2-11bff8e7912a98de09691ad7d7b7a2d3194e2757')
REPO = Path('/workspace/r7-u03-reviewer-r2')
B = 'e646432c644dec04d306842cc5a559a29c718fbc'
C = '11bff8e7912a98de09691ad7d7b7a2d3194e2757'

def ident(d):
    return dict(bytes=len(d), sha256=hashlib.sha256(d).hexdigest(),
                git_blob_content_id=hashlib.sha1(f'blob {len(d)}\0'.encode()+d).hexdigest())

def dump(name, obj):
    (ROOT/name).write_text(json.dumps(obj, ensure_ascii=False, indent=2)+'\n')

def load(p):
    return json.loads(p.read_bytes())

def git(*args):
    return subprocess.check_output(['git','-C',str(REPO),*args])

def check(d,r):
    a=ident(d)
    for k,v in a.items():
        expected=r.get(k,r.get('git_blob',r.get('content_git_blob')) if k=='git_blob_content_id' else None)
        if expected is not None: assert v==expected,(k,v,expected)
    return a

original_plan=load(Path('/workspace/r7-bootstrap/R7-U03-reviewer/recovery/batches/R7-U03.json'))
candidate_plan=load(BOOT/'candidate-restore/R7-U03.json')
freeze=load(BOOT/'candidate-input.json')
orig=[]
for r in original_plan['artifacts']+original_plan['evidence']+original_plan['fixed_read_inputs']:
    orig.append(dict(local_path=r['local_path'],**check((CTX/r['local_path']).read_bytes(),r)))
assert len(orig)==34 and sum(r['bytes'] for r in orig)==6088763
frozen={r['path']:r for r in freeze['candidate_and_author_evidence_file_identities']}
candidate=[]
for r in candidate_plan['artifacts']:
    d=(INPUT/r['local_path']).read_bytes(); a=check(d,r); check(d,frozen[r['path']])
    assert frozen[r['path']]['git_mode']=='100644'
    candidate.append(dict(path=r['path'],**a))
assert len(candidate)==84 and sum(r['bytes'] for r in candidate)==774948
tree_rows={}
for line in git('ls-tree','-r',C,'candidates/R7-U03').decode().splitlines():
    meta,path=line.split('\t');mode,kind,blob=meta.split()
    tree_rows[path]=(mode,kind,blob)
assert set(tree_rows)==set(frozen)=={r['path'] for r in candidate}
for r in candidate:
    assert tree_rows[r['path']]==('100644','blob',r['git_blob_content_id'])
assert git('rev-parse',C+'^{tree}').decode().strip()==freeze['candidate_tree']=='b12b63cd5f19b4d550aae3548a618bf10416e56f'
assert git('rev-parse','aa369555b0e8b6c8b077f964b54ed63d3b924f26^{tree}').decode().strip()=='08bd0f362c74ef7645b5bbd70b557489c122ae29'
complete_diff=git('diff','--name-status',B,C).decode().splitlines()
assert set(complete_diff)=={'A\t'+p for p in frozen}

# These four exact dependencies are named by the original member bindings.
bindings=load(CTX/'evidence/tasks/R7-C13/raw-binding-manifest.json')
ids=['p02-23c99e9ff2920dc7376a','p02-85e3801098ab8f9287ae',
     'p02-b879c9a306446f46733b','p02-73783f8cb75fe76adbc4']
supp=[]
for r in bindings:
    if r['binding_id'] not in ids: continue
    sha=r['sha256']; p=CTX/'supplement'/Path(r['snapshot']).name
    p.parent.mkdir(exist_ok=True)
    url=f'https://raw.githubusercontent.com/y805939188/pokemon-essentials-clean-room/4580645dfbfec4a3c7ccbad56ae293cc619b0d25/review/global-independent-review/seventh-2026-10-14-e646432-7a91/publication-transport/core/objects/{sha[:2]}/{sha}.gz'
    if p.exists(): d=p.read_bytes();status='REUSED_EXACT_BYTES'
    else:
        with urllib.request.urlopen(url,timeout=40) as response:
            encoded=response.read(r['bytes']+10000); assert response.status==200
        d=gzip.decompress(encoded);check(d,r);p.write_bytes(d);status='HTTP200_EXACT_DECODED_BYTES'
    supp.append(dict(binding_id=r['binding_id'],url=url,status=status,local_path=str(p),**check(d,r)))

raws={}
for p in [*CTX.rglob('*.raw')]:
    d=p.read_bytes();raws[hashlib.sha256(d).hexdigest()]=d

def pointer(x,p):
    if not p:return x
    for k in p.strip('/').split('/'):
        k=k.replace('~1','/').replace('~0','~'); x=x[int(k)] if isinstance(x,list) else x[k]
    return x

def walk(x):
    if isinstance(x,list):
        for v in x:yield from walk(v)
    if isinstance(x,dict):
        yield x
        for v in x.values():yield from walk(v)

contract=load(CTX/'dispatch/delegation/contracts/R7-U03.json')
normalized=load(CTX/'evidence/tasks/R7-C13/inputs/tasks/R7-P02/normalized-record-candidates.json')
members=[];seen=set()
for r in walk([contract,normalized['records'][6],normalized['records'][7]]):
    if not all(k in r for k in ['input_sha256','json_pointer','raw_member_byte_offsets','raw_member_sha256','canonical_sha256']):continue
    key=(r['input_sha256'],r['json_pointer'],tuple(r['raw_member_byte_offsets']))
    if key in seen:continue
    seen.add(key);d=raws[r['input_sha256']];a,b=r['raw_member_byte_offsets'];part=d[a:b]
    assert len(part)==r['raw_member_bytes'] and hashlib.sha256(part).hexdigest()==r['raw_member_sha256']
    actual=pointer(json.loads(d),r['json_pointer']);assert json.loads(part)==actual
    canonical=json.dumps(actual,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode()
    assert hashlib.sha256(canonical).hexdigest()==r['canonical_sha256']
    members.append(dict(binding_id=r.get('binding_id'),json_pointer=r['json_pointer'],input_sha256=r['input_sha256'],raw_member_byte_offsets=[a,b],raw_member_sha256=r['raw_member_sha256'],canonical_sha256=r['canonical_sha256'],matched=True))

mirrors=[]
for r in candidate_plan['artifacts'][:5]:
    target=r['path'].removeprefix('candidates/R7-U03/')
    old=git('show',B+':'+target);new=(INPUT/r['local_path']).read_bytes()
    check(old,frozen[r['path']]['base_B_identity_or_explicit_new_file'])
    before=old.decode().splitlines(keepends=True);after=new.decode().splitlines(keepends=True)
    ops=[dict(kind=k,base_lines=[a+1,b],candidate_lines=[c+1,d]) for k,a,b,c,d in difflib.SequenceMatcher(None,before,after,autojunk=False).get_opcodes() if k!='equal']
    changed={'MV01','MV02'} if 'wp11-15-59-60' in target else ({'WR01'} if target.endswith('engine-overworld-wp16.md') else ({'普通移动','碰撞'} if target.endswith('wp12-terrain-movement-vehicles.md') else set()))
    table=[line for line in before if line.startswith('|') and line.split('|')[1].strip() not in changed]
    preserved=all(line in after for line in table)
    assert preserved, (target, [line for line in table if line not in after])
    mirrors.append(dict(path=r['path'],target=target,base=ident(old),candidate=ident(new),changes=ops,old_non_target_table_rows=len(table),all_non_target_table_rows_preserved=True))

author=INPUT/'candidate/candidates/R7-U03/evidence/author'
manifest=load(author/'artifact-manifest.json')
declared=[]
for r in walk(manifest):
    if not ('bytes' in r and 'sha256' in r):continue
    path=r.get('path',r.get('candidate_path'))
    if path in frozen:
        p=INPUT/'candidate'/path;check(p.read_bytes(),r);declared.append(path)

dump('input-byte-audit.json',dict(stage='TOOL_VALIDATION',utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),pid=os.getpid(),original=orig,candidate=candidate,supplements=supp,members=members,members_verified=len(members),mirrors=mirrors,author_declared_identities_verified=sorted(set(declared)),actual_candidate_tree=freeze['candidate_tree'],tree_modes_and_blobs_match_all_84=True,complete_diff_against_B=complete_diff,qualification='Byte/range/membership/preservation only; no behavior execution or semantic verdict'))
print(json.dumps(dict(original_files=len(orig),original_bytes=sum(r['bytes'] for r in orig),candidate_files=len(candidate),candidate_bytes=sum(r['bytes'] for r in candidate),supplements=len(supp),members_verified=len(members),mirrors=len(mirrors),preserved_non_target_table_rows=sum(r['old_non_target_table_rows'] for r in mirrors),author_declared_identities_verified=len(set(declared))),ensure_ascii=False))
