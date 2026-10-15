"""Independent full-byte/pointer/diff inventory. No semantic verdict and no target execution."""
import difflib
import hashlib
import json
from pathlib import Path
import re
import subprocess

OUT = Path(__file__).resolve().parent
CTX = Path('/workspace/r7-context/R7-U10-reviewer')
BOOT = Path('/workspace/r7-review-bootstrap/R7-U10-r2')
CAND = Path('/workspace/r7-review-input/R7-U10-r2-583330fb69935ff6b2eb32ca11ede6c23bde5ecd/candidate')
B = 'e646432c644dec04d306842cc5a559a29c718fbc'
F = 'aa369555b0e8b6c8b077f964b54ed63d3b924f26'
C = '583330fb69935ff6b2eb32ca11ede6c23bde5ecd'

def git(*args):
    return subprocess.check_output(['git', *args])

def identity(data):
    return dict(bytes=len(data), sha256=hashlib.sha256(data).hexdigest(),
                git_blob=hashlib.sha1(f'blob {len(data)}\0'.encode() + data).hexdigest())

def verify(data, row):
    got = identity(data)
    for key, value in got.items():
        expected = row.get(key, row.get('git_blob_content_id') if key == 'git_blob' else None)
        if expected is not None:
            assert expected == value, (row.get('path', row.get('local_path')), key, expected, value)
    return got

freeze = json.loads((BOOT/'candidate-input.json').read_bytes())
assert freeze['candidate_commit'] == C
assert git('rev-parse', C+'^{tree}').decode().strip() == freeze['candidate_tree'] == '7a81a11b22d771fe79f165a265fa108c4a85502c'
assert git('rev-parse', F+'^{tree}').decode().strip() == '08bd0f362c74ef7645b5bbd70b557489c122ae29'
for rel in ['candidate-input.json', 'candidate-restore/R7-U10.json', 'mirror-diffs.patch', 'remote-readback.json']:
    assert (BOOT/rel).read_bytes() == git('show', F+':review/remediation-seventh-20261015-prepare/candidate-freezes/R7-U10/'+rel)
entries = freeze['candidate_and_author_evidence_file_identities']
actual_diff = [line.split('\t') for line in git('diff','--name-status',B,C).decode().splitlines()]
assert actual_diff == [[r['status'],r['path']] for r in freeze['complete_diff_against_B']]
assert {p for s,p in actual_diff} == {r['path'] for r in entries}
assert len(entries) == 61 and sum(r['bytes'] for r in entries) == 1050546
assert all(s == 'A' and p.startswith('candidates/R7-U10/') for s,p in actual_diff)
verified_files = []
for row in entries:
    data = (CAND/row['path']).read_bytes()
    got = verify(data, row)
    assert data == git('show', C+':'+row['path'])
    mode, typ, blob = git('ls-tree', C, '--', row['path']).decode().split('\t')[0].split()
    assert mode == row['git_mode'] == '100644' and typ == 'blob' and blob == got['git_blob']
    verified_files.append({'path':row['path'], **got, 'mode':mode})

raw_by_hash = {}
restored = []
plan = json.loads(Path('/workspace/r7-bootstrap/R7-U10-reviewer/recovery/batches/R7-U10.json').read_bytes())
for row in plan['artifacts']+plan['evidence']+plan['fixed_read_inputs']:
    data = (CTX/row['local_path']).read_bytes()
    restored.append({'path': row['local_path'], **verify(data,row)})
    raw_by_hash[hashlib.sha256(data).hexdigest()] = data
supp = json.loads((OUT/'supplement-recovery.json').read_bytes())
for row in supp['files']:
    data = (CTX/'supplement'/row['path']).read_bytes()
    verify(data,row)
    raw_by_hash[row['sha256']] = data

def pointer(obj, ptr):
    for part in ptr.split('/')[1:]:
        part = part.replace('~1','/').replace('~0','~')
        obj = obj[int(part)] if isinstance(obj,list) else obj[part]
    return obj

checked = {}
def bindings(obj):
    if isinstance(obj, dict):
        if all(key in obj for key in ['input_sha256','json_pointer','raw_member_byte_offsets']):
            data = raw_by_hash[obj['input_sha256']]
            start, end = obj['raw_member_byte_offsets']
            part = data[start:end]
            assert len(part) == obj['raw_member_bytes']
            assert hashlib.sha256(part).hexdigest() == obj['raw_member_sha256']
            member = pointer(json.loads(data),obj['json_pointer'])
            canonical = json.dumps(member,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode()
            assert hashlib.sha256(canonical).hexdigest() == obj['canonical_sha256']
            checked[obj['input_sha256']+'#'+obj['json_pointer']] = obj
        for value in obj.values():
            bindings(value)
    elif isinstance(obj, list):
        for value in obj:
            bindings(value)

contract = json.loads((CTX/'dispatch/delegation/contracts/R7-U10.json').read_bytes())
bindings(contract)
norm = json.loads((CTX/'evidence/tasks/R7-C13/inputs/tasks/R7-P02/normalized-record-candidates.json').read_bytes())
for index in [19,27,21]:
    bindings(norm['records'][index])

mirrors = []
patches = []
for row in entries:
    if row['role'] != 'candidate_mirror':
        continue
    target = row['formal_target']
    old = (CTX/'inputs/project'/target).read_bytes()
    assert old == git('show',B+':'+target)
    verify(old,row['base_B_identity_or_explicit_new_file'])
    new = (CAND/row['path']).read_bytes()
    a,b = old.decode().splitlines(keepends=True), new.decode().splitlines(keepends=True)
    hunks = []
    equal_lines = 0
    for op,i,j,k,l in difflib.SequenceMatcher(None,a,b,autojunk=False).get_opcodes():
        if op == 'equal':
            equal_lines += j-i
        else:
            hunks.append({'operation':op,'B_zero_based_half_open':[i,j], 'candidate_zero_based_half_open':[k,l]})
    mirrors.append({'target':target,'base':identity(old),'candidate':identity(new),'changes':hunks,'exactly_unchanged_base_lines':equal_lines})
    patches.extend(difflib.unified_diff(a,b,fromfile='B/'+target,tofile=row['path'],n=5))

catalog = 'deliverables/final-specification-set/test-catalog/demo-dx-wp72-73-74-75-76-77.md'
old = (CTX/'inputs/project'/catalog).read_text().splitlines()
new = (CAND/'candidates/R7-U10'/catalog).read_text().splitlines()
preserved = []
for line in old:
    if re.match(r'^\| [A-Z0-9][^|]* \|',line) and not line.startswith(('| AN-M09 |','| WE-M17 |')):
        assert new.count(line) == old.count(line), line
        preserved.append(line.split('|')[1].strip())
oldwe = next(s for s in old if s.startswith('| WE-M17 |'))
newwe = next(s for s in new if s.startswith('| WE-M17 |'))
assert newwe.startswith(oldwe[:-2])
assert [re.match(r'^\| (TOOL-AN-\d+) \|',s)[1] for s in new if s.startswith('| TOOL-AN-')] == [f'TOOL-AN-{i:02}' for i in range(1,18)]
assert not (CAND/'candidates/R7-U10/specs').exists()
assert git('rev-parse',B+':deliverables/final-specification-set').decode().strip() == 'ebbe29f2bc88cd17de7072bf440c6fa8c8c7089c'
disassembly = (OUT/'logs/006-current-cil.stdout').read_text()
assert [int(s) for s in re.findall(r'^METHOD (\d+) ',disassembly,re.M)] == list(range(1,16))
assert disassembly.count('EH_CLAUSE ') == 11
arithmetic = {'n0':[960,192],'n6':[960,192*((6+4)//5)],'slot5':[192*(5%5),192*(5//5)],'rect0':[96-56,96-68,56*2,68*2],'rect1':[192+96-56,96-68,56*2,68*2]}
result = dict(qualification='TOOL_VALIDATION_ONLY; semantic review is separately authored',
              candidate_commit=C,candidate_tree=freeze['candidate_tree'],freeze_commit=F,
              candidate_files=verified_files,original_restore_files=restored,
              raw_member_bindings=list(checked.values()),mirrors=mirrors,
              preserved_catalog_rows=preserved,arithmetic=arithmetic,
              methods=15,EH_entries=11,reference_behavior_execution=0,behavior_vectors='NOT_EXECUTED')
(OUT/'input-verification.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
(OUT/'independent-mirror-diffs.patch').write_text(''.join(patches))
print(json.dumps(dict(candidate_files=len(verified_files),candidate_bytes=sum(r['bytes'] for r in verified_files),
                     original_files=len(restored),original_bytes=sum(r['bytes'] for r in restored),
                     raw_bindings=len(checked),mirror_count=len(mirrors),preserved_catalog_rows=len(preserved),
                     arithmetic=arithmetic,methods=15,EH_entries=11,scope='TOOL_VALIDATION_ONLY'),indent=2))
