"""Independent byte/range audit, not a behavior model or candidate execution."""
from pathlib import Path
import datetime
import difflib
import hashlib
import json
import subprocess

OUT = Path(__file__).resolve().parent
CTX = Path('/workspace/r7-context/R7-U01-reviewer')
INPUT = Path('/workspace/r7-review-input/R7-U01-r2-a3938bbb8f8c2294465b75363a39fd4598b82a15')
B = 'e646432c644dec04d306842cc5a559a29c718fbc'
C = 'a3938bbb8f8c2294465b75363a39fd4598b82a15'
F = 'aa369555b0e8b6c8b077f964b54ed63d3b924f26'

def ident(data):
    return {'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest(),
            'git_blob': hashlib.sha1(f'blob {len(data)}\0'.encode() + data).hexdigest()}

def git(*argv):
    return subprocess.check_output(['git', *argv])

def load(path):
    return json.loads(path.read_bytes())

def check(data, row):
    actual = ident(data)
    for key, value in actual.items():
        expected = row.get(key, row.get('git_blob_content_id') if key == 'git_blob' else None)
        if expected is not None:
            assert value == expected, (key, value, expected)
    return actual

freeze = load(OUT/'frozen-candidate-input.json')
prefix = 'review/remediation-seventh-20261015-prepare/'
for local, rev, remote in [
    ('reviewer-dispatch.md', '95c260d8f3fb4a171675dde877137fcd4c2f1c8d', prefix+'candidate-freezes/R7-U01/versions/r2/reviewer-dispatch.md'),
    ('context-restore-plan.json', '658488c81f1f3181a488298ab27850c8af951d73', prefix+'recovery/batches/R7-U01.json'),
    ('restore_container_context.py', '658488c81f1f3181a488298ab27850c8af951d73', prefix+'tools/restore_container_context.py'),
    ('candidate-restore-plan.json', F, prefix+'candidate-freezes/R7-U01/versions/r2/candidate-restore/R7-U01.json')]:
    assert (OUT/local).read_bytes() == git('show', rev+':'+remote)
assert git('rev-parse', C+'^{tree}').decode().strip() == freeze['candidate_tree']
assert git('rev-parse', F+'^{tree}').decode().strip() == '08bd0f362c74ef7645b5bbd70b557489c122ae29'
restored = []
for plan_file, root in [('context-restore-plan.json', CTX), ('candidate-restore-plan.json', INPUT)]:
    plan = load(OUT/plan_file)
    for row in plan['artifacts'] + plan['evidence'] + plan['fixed_read_inputs']:
        actual = check((root/row['local_path']).read_bytes(), row)
        restored.append({'plan': plan_file, 'path': row['local_path'], **actual})

changed = git('diff', '--name-status', B, C).decode().splitlines()
expected = [x['status']+'\t'+x['path'] for x in freeze['complete_diff_against_B']]
assert changed == expected
files = []
diffs = []
repair_diffs = []
mirrors = []
for row in freeze['candidate_and_author_evidence_file_identities']:
    path = row['path']
    data = (INPUT/'candidate'/path).read_bytes()
    actual = check(data, row)
    mode, kind, blob = git('ls-tree', C, '--', path).decode().split('\t')[0].split()
    assert mode == row['git_mode'] == '100644' and kind == 'blob' and blob == actual['git_blob']
    assert git('show', C+':'+path) == data
    files.append({**row, 'independently_verified': True})
    if row['role'] == 'candidate_mirror':
        target = row['formal_target']
        base = git('show', B+':'+target)
        check(base, row['base_B_identity_or_explicit_new_file'])
        assert base == (CTX/'inputs/project'/target).read_bytes()
        diff = ''.join(difflib.unified_diff(base.decode().splitlines(True), data.decode().splitlines(True),
                                          fromfile='a/'+target, tofile='b/'+target))
        diffs.append(diff)
        old = (INPUT/'prior-candidate'/path).read_bytes()
        repair = ''.join(difflib.unified_diff(old.decode().splitlines(True), data.decode().splitlines(True),
                                            fromfile='r1/'+target, tofile='r2/'+target))
        if repair:
            repair_diffs.append({'target': target, 'diff': repair})
        matcher = difflib.SequenceMatcher(None, base.decode().splitlines(True), data.decode().splitlines(True), autojunk=False)
        hunks = [{'operation': tag, 'base_lines': [i+1, j], 'candidate_lines': [k+1, l]}
                 for tag,i,j,k,l in matcher.get_opcodes() if tag != 'equal']
        mirrors.append({'target': target, 'hunks': hunks, 'r1_r2_identical': old == data,
                        'base_prefix_preserved': data.startswith(base)})
patch = ''.join(diffs)
assert patch == load(OUT/'frozen-mirror-diffs.json')['patch_utf8']
assert {x['target'] for x in repair_diffs} == {
    'deliverables/final-specification-set/generic-kernel/wp03-content-identity-and-schema.md',
    'deliverables/final-specification-set/test-catalog/generic-kernel-wp02-03-04.md'}

author = INPUT/'candidate/candidates/R7-U01/evidence/author'
old_author = INPUT/'prior-candidate/candidates/R7-U01/evidence/author'
current_ids = load(author/'per-id.json')
prior_ids = load(old_author/'per-id.json')
assert current_ids['actual_thread'] == freeze['author_task_id']
assert current_ids['actual_thread'] != load(OUT/'identity-observation.json')['reviewer_thread_id']
vector_lists = []
def vectors(v, path=''):
    if isinstance(v, dict):
        for k, x in v.items():
            if k == 'vectors':
                vector_lists.append((path+'/'+k, x))
            else:
                vectors(x, path+'/'+k)
    elif isinstance(v, list):
        for i,x in enumerate(v): vectors(x, path+'/'+str(i))
vectors(current_ids)
old_vectors = []
for record in prior_ids['records']:
    for k,x in record.items():
        if k == 'vectors': old_vectors.extend(x)
new_vectors = []
for _, rows in vector_lists: new_vectors.extend(rows)
for row in old_vectors:
    assert row in new_vectors, row.get('id')
assert len(old_vectors) == 16
manifest = load(author/'artifact-manifest.json')
# Enumerate all declared file identity rows, without relying on a manifest self-hash.
declared = []
def find_rows(v):
    if isinstance(v, dict):
        if 'path' in v and 'bytes' in v and 'sha256' in v:
            declared.append(v)
        for x in v.values(): find_rows(x)
    elif isinstance(v, list):
        for x in v: find_rows(x)
find_rows(manifest)
for row in declared:
    path = row['path']
    if path.startswith('candidates/R7-U01/'):
        target = INPUT/'candidate'/path
    else:
        target = CTX/'inputs/project'/path
    check(target.read_bytes(), row)

contract = load(CTX/'dispatch/delegation/contracts/R7-U01.json')
all_evidence = {hashlib.sha256(p.read_bytes()).hexdigest(): p for p in (CTX/'evidence').rglob('*') if p.is_file()}
bindings = []
seen = set()
def verify_bindings(v):
    if isinstance(v, dict):
        if 'raw_member_byte_offsets' in v and 'input_sha256' in v:
            key = (v['input_sha256'], tuple(v['raw_member_byte_offsets']), v['canonical_sha256'])
            if key not in seen:
                seen.add(key)
                raw = all_evidence[v['input_sha256']].read_bytes()
                a,b = v['raw_member_byte_offsets']
                member = raw[a:b]
                assert len(member) == v['raw_member_bytes']
                assert hashlib.sha256(member).hexdigest() == v['raw_member_sha256']
                obj = json.loads(raw)
                for part in v['json_pointer'].strip('/').split('/') if v['json_pointer'] else []:
                    part = part.replace('~1','/').replace('~0','~')
                    obj = obj[int(part)] if isinstance(obj,list) else obj[part]
                canonical = json.dumps(obj,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode()
                assert hashlib.sha256(canonical).hexdigest() == v['canonical_sha256']
                bindings.append({'binding_id': v['binding_id'], 'pointer': v['json_pointer'], 'raw_and_canonical_verified': True})
        for x in v.values(): verify_bindings(x)
    elif isinstance(v, list):
        for x in v: verify_bindings(x)
verify_bindings(contract)
result = {'utc': datetime.datetime.now(datetime.timezone.utc).isoformat(), 'status': 'PASS_TOOL_VALIDATION_ONLY',
          'candidate_commit': C, 'candidate_tree': freeze['candidate_tree'], 'restored_files': restored,
          'changed_against_B': changed, 'candidate_files': files, 'mirrors': mirrors,
          'full_patch_exact': True, 'repair_diffs': repair_diffs, 'manifest_declared_rows_checked': len(declared),
          'old_vector_objects_exactly_preserved': len(old_vectors), 'binding_checks': bindings,
          'semantic_PASS_from_tool': False, 'behavior_execution': 'NOT_EXECUTED'}
(OUT/'mechanical-audit.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
(OUT/'independent-mirror-diffs.json').write_text(json.dumps({'patch': patch, 'identity': ident(patch.encode())},ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:result[k] for k in ['status','candidate_commit','candidate_tree','full_patch_exact','manifest_declared_rows_checked','old_vector_objects_exactly_preserved']}))
print('Restored files:',len(restored),'candidate files:',len(files),'binding checks:',len(bindings))
