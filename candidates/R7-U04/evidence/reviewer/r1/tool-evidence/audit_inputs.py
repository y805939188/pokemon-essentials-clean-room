"""Reviewer-owned bounded byte/scope audit; no reference or author code execution."""
import datetime
import difflib
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess

OUT = Path(__file__).resolve().parent
REPO = OUT.parents[5]
CONTEXT = Path('/workspace/r7-context/R7-U04-reviewer')
BOOT = Path('/workspace/r7-bootstrap/R7-U04-reviewer')
FREEZE = Path('/workspace/r7-review-bootstrap/R7-U04')
CANDIDATE_ROOT = Path('/workspace/r7-review-input/R7-U04-242e1f9fb2fbdf7d609bcdb6de0a95547f9f4c6a')
B = 'e646432c644dec04d306842cc5a559a29c718fbc'
C = '242e1f9fb2fbdf7d609bcdb6de0a95547f9f4c6a'
D = '6ec1d09e9c470954964d72761c83a760ef4f0364'
F = 'f76135fdc8b626de1dabdecf5288fc926b04e7ac'


def now():
    return datetime.datetime.now(datetime.timezone.utc).isoformat()


def identity(data):
    return dict(bytes=len(data), sha256=hashlib.sha256(data).hexdigest(),
                git_blob=hashlib.sha1(f'blob {len(data)}\0'.encode() + data).hexdigest())


def verify(data, row):
    actual = identity(data)
    assert actual['bytes'] == row['bytes']
    assert actual['sha256'] == row['sha256']
    assert actual['git_blob'] == row.get('git_blob', row.get('git_blob_content_id'))
    return actual


def git(*args):
    start = now()
    run = subprocess.run(['git', *args], cwd=REPO, capture_output=True)
    record = dict(argv=['git', *args], cwd=str(REPO), start_utc=start,
                  end_utc=now(), exit_code=run.returncode,
                  stdout=run.stdout.decode(), stderr=run.stderr.decode(),
                  credit='TOOL_VALIDATION_IDENTITY_SCOPE_ONLY')
    with (OUT/'public-command-log.jsonl').open('a') as stream:
        stream.write(json.dumps(record, ensure_ascii=False)+'\n')
    assert run.returncode == 0, record
    return run.stdout


started = now()
freeze = json.loads((FREEZE/'candidate-input.json').read_bytes())
contract = json.loads((BOOT/'dispatch/delegation/contracts/R7-U04.json').read_bytes())
dispatch_bytes = (BOOT/'dispatch/reviewer-dispatch.md').read_bytes()
assert git('rev-parse', D+'^{tree}').decode().strip() == '15f3c40eb9733d04be228b47c6ea52e33c6123b7'
assert git('rev-parse', F+'^{tree}').decode().strip() == '65b3ef0352b10f638ba9867414b2bc68f5a2ae80'
assert git('rev-parse', C+'^{tree}').decode().strip() == freeze['candidate_tree']
assert git('rev-parse', B+'^{tree}').decode().strip() == freeze['fixed_B_tree']
assert git('rev-parse', B+':deliverables/final-specification-set').decode().strip() == 'ebbe29f2bc88cd17de7072bf440c6fa8c8c7089c'
assert hashlib.sha1(f'blob {len(dispatch_bytes)}\0'.encode()+dispatch_bytes).hexdigest() == git('rev-parse', D+':review/remediation-seventh-20261015-prepare/candidate-freezes/R7-U04/reviewer-dispatch.md').decode().strip()
for rel in ['candidate-input.json','candidate-restore/R7-U04.json','mirror-diffs.patch','remote-readback.json']:
    data = (FREEZE/rel).read_bytes()
    blob = git('rev-parse', F+':review/remediation-seventh-20261015-prepare/candidate-freezes/R7-U04/'+rel).decode().strip()
    assert identity(data)['git_blob'] == blob
assert not git('ls-tree','-r','--name-only',D,'--','.agents')
assert not git('ls-tree','-r','--name-only',B,'--','.agents')
for commit, rel, local in [
    ('658488c81f1f3181a488298ab27850c8af951d73','tools/restore_container_context.py',BOOT/'tools/restore_container_context.py'),
    ('658488c81f1f3181a488298ab27850c8af951d73','recovery/batches/R7-U04.json',BOOT/'recovery/batches/R7-U04.json'),
    ('658488c81f1f3181a488298ab27850c8af951d73','recovery/independent-containers.md',BOOT/'recovery/independent-containers.md'),
    ('f622356f3beb9e84ea8cff9db07c7fb382565d3f','delegation/contracts/R7-U04.json',BOOT/'dispatch/delegation/contracts/R7-U04.json'),
    ('f622356f3beb9e84ea8cff9db07c7fb382565d3f','delegation/prompts/R7-U04-reviewer.md',BOOT/'dispatch/delegation/prompts/R7-U04-reviewer.md')]:
    blob=git('rev-parse',commit+':review/remediation-seventh-20261015-prepare/'+rel).decode().strip()
    assert identity(local.read_bytes())['git_blob']==blob

restorations = []
for plan_path, destination in [(BOOT/'recovery/batches/R7-U04.json', CONTEXT),
                               (FREEZE/'candidate-restore/R7-U04.json', CANDIDATE_ROOT)]:
    plan = json.loads(plan_path.read_bytes())
    rows = plan['artifacts']+plan['evidence']+plan['fixed_read_inputs']
    verified = []
    for row in rows:
        data = (destination/row['local_path']).read_bytes()
        actual = verify(data, row)
        if 'encoded_identity' in row:
            encoded = (destination/'transport'/row['transport_path']).read_bytes()
            assert len(encoded) == row['encoded_identity']['bytes']
            assert identity(encoded)['git_blob'] == row['encoded_identity']['git_blob_content_id']
        verified.append(dict(local_path=row['local_path'], **actual))
        (destination/row['local_path']).chmod(0o444)
    restorations.append(dict(plan=str(plan_path), plan_identity=identity(plan_path.read_bytes()),
                             destination=str(destination), count=len(rows), bytes=sum(x['bytes'] for x in rows), files=verified))

changes = git('diff','--name-status',B,C).decode().splitlines()
expected_changes = [r['status']+'\t'+r['path'] for r in freeze['complete_diff_against_B']]
assert changes == expected_changes
tree = git('ls-tree','-r',C,'--','candidates/R7-U04').decode().splitlines()
assert len(tree) == 17
blobs = {}
for line in tree:
    header, path = line.split('\t')
    mode, kind, blob = header.split()
    assert mode == '100644' and kind == 'blob'
    blobs[path] = blob
assert set(blobs) == {r['path'] for r in freeze['candidate_and_author_evidence_file_identities']}
candidate_files = []
for row in freeze['candidate_and_author_evidence_file_identities']:
    actual = verify((CANDIDATE_ROOT/'candidate'/row['path']).read_bytes(),row)
    assert blobs[row['path']] == actual['git_blob']
    candidate_files.append(dict(path=row['path'], git_mode='100644', **actual))

author = CANDIDATE_ROOT/'candidate/candidates/R7-U04/evidence/author'
manifest = json.loads((author/'artifact-manifest.json').read_bytes())
inventory = manifest['evidence_inventory']
for path, value in inventory.items():
    verify((CANDIDATE_ROOT/'candidate'/path).read_bytes(),value)
assert len(inventory)+len(manifest['mirrors']) == 16
assert set(inventory) | {x['path'] for x in manifest['mirrors']} == set(blobs)-{'candidates/R7-U04/evidence/author/artifact-manifest.json'}

raw_bindings = []
def pointers(value):
    if isinstance(value,dict):
        if all(k in value for k in ['raw_member_byte_offsets','raw_member_sha256','canonical_sha256','json_pointer','input_sha256']):
            yield value
        for child in value.values(): yield from pointers(child)
    elif isinstance(value,list):
        for child in value: yield from pointers(child)
seen = set()
for ref in pointers(contract):
    key = (ref['input_sha256'],ref['json_pointer'])
    if key in seen: continue
    seen.add(key)
    raw = (CONTEXT/'evidence/tasks/R7-C13/inputs/tasks/R7-P02/evidence/inputs'/(ref['input_sha256']+'.raw')).read_bytes()
    lo,hi = ref['raw_member_byte_offsets']
    assert hi-lo == ref['raw_member_bytes']
    assert hashlib.sha256(raw[lo:hi]).hexdigest() == ref['raw_member_sha256']
    value = json.loads(raw)
    for token in ref['json_pointer'].split('/')[1:]:
        token = token.replace('~1','/').replace('~0','~')
        value = value[int(token)] if isinstance(value,list) else value[token]
    canonical = json.dumps(value,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode()
    assert hashlib.sha256(canonical).hexdigest() == ref['canonical_sha256']
    raw_bindings.append(ref)

mirrors = []
mirror_diffs = []
author_diffs = []
for row in freeze['candidate_and_author_evidence_file_identities']:
    if row['role'] != 'candidate_mirror': continue
    original = (CONTEXT/'inputs/project'/row['formal_target']).read_bytes()
    verify(original,row['base_B_identity_or_explicit_new_file'])
    updated = (CANDIDATE_ROOT/'candidate'/row['path']).read_bytes()
    old,new = original.decode().splitlines(),updated.decode().splitlines()
    mirror_diffs.extend(difflib.unified_diff(original.decode().splitlines(True),updated.decode().splitlines(True),fromfile='a/'+row['formal_target'],tofile='b/'+row['formal_target']))
    author_diffs.extend(difflib.unified_diff(original.decode().splitlines(True),updated.decode().splitlines(True),fromfile=row['formal_target'],tofile=row['path'],n=0))
    operations = []
    for kind,a,b,c,d in difflib.SequenceMatcher(a=old,b=new,autojunk=False).get_opcodes():
        if kind != 'equal': operations.append(dict(kind=kind,base_lines=[a+1,b],candidate_lines=[c+1,d]))
    mirrors.append(dict(path=row['path'],formal_target=row['formal_target'],base_identity=identity(original),candidate_identity=identity(updated),operations=operations))
assert ''.join(mirror_diffs).encode()==(FREEZE/'mirror-diffs.patch').read_bytes()
assert ''.join(author_diffs).encode()==(author/'clause-contributions.patch').read_bytes()

catalog_path = next(row['formal_target'] for row in mirrors if 'test-catalog/' in row['formal_target'])
old = (CONTEXT/'inputs/project'/catalog_path).read_text().splitlines()
new = (CANDIDATE_ROOT/'candidate/candidates/R7-U04'/catalog_path).read_text().splitlines()
old_rows = [x for x in old if x.startswith('|')]
new_rows = [x for x in new if x.startswith('|')]
assert [x for x in new_rows if x in old_rows] == old_rows
added = [x for x in new_rows if x not in old_rows]
assert len(added) == 12
for tag,count in [('BC',31),('SW',35)]:
    assert re.findall(r'^\| ('+tag+r'-\d+) \|','\n'.join(new),re.M) == [f'{tag}-{i:02}' for i in range(1,count+1)]

parsed = []
for file in author.iterdir():
    if file.suffix == '.json':
        json.loads(file.read_bytes()); parsed.append(file.name)
    elif file.suffix == '.jsonl':
        for line in file.read_text().splitlines(): json.loads(line)
        parsed.append(file.name)
for record in json.loads((author/'per-id.json').read_bytes())['records']:
    for vector in record['vectors']:
        line=(CANDIDATE_ROOT/'candidate'/vector['path']).read_text().splitlines()[vector['line']-1]
        cells=line.split('|')
        assert cells[1].strip()==vector['id'] and cells[2].strip()==vector['premise'] and cells[3].strip()==vector['expected']

result = dict(schema='r7.u04.reviewer-input-audit.v1',start_utc=started,end_utc=now(),pid=os.getpid(),
              actual_thread_id=os.environ.get('CODEX_THREAD_ID','NOT_EXPOSED_UNVERIFIED'),
              status='BYTES_SCOPE_BINDINGS_VERIFIED',restorations=restorations,
              candidate_files=candidate_files,candidate_bytes=sum(r['bytes'] for r in candidate_files),
              complete_diff_against_B=changes,mirrors=mirrors,raw_bindings=raw_bindings,
              raw_binding_count=len(raw_bindings),author_manifest_other_files_verified=16,
              old_catalog_rows_preserved=len(old_rows),new_catalog_rows=12,
              author_json_files_parsed=parsed,skills_at_B_and_dispatch='ABSENT',
              executed_author_programs=0,executed_reference_programs=0,domain_vectors='NOT_EXECUTED',
              semantic_verdict_from_this_tool=False)
(OUT/'input-audit.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:result[k] for k in ['status','pid','actual_thread_id','candidate_bytes','raw_binding_count','old_catalog_rows_preserved','new_catalog_rows','semantic_verdict_from_this_tool']}))
