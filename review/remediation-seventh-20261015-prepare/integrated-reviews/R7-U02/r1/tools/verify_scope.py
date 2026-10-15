import datetime
import hashlib
import json
import subprocess
import urllib.request
import urllib.parse
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INPUT = Path('/workspace/r7-ir-R7-U02/actual-input')
B = 'e646432c644dec04d306842cc5a559a29c718fbc'
MI = '45c80832a41c1b56dcd7e9d93497758cbb7721de'
FI = '13d76ba61838b13925ba9d41f58a6b047564d926'
PREFIX = 'review/remediation-seventh-20261015-prepare/'

def git(*args):
    return subprocess.check_output(['git', *args])

def identity(data):
    return dict(bytes=len(data), sha256=hashlib.sha256(data).hexdigest(),
                git_blob=hashlib.sha1(f'blob {len(data)}\0'.encode() + data).hexdigest())

def matches(data, expected):
    actual = identity(data)
    for k, v in actual.items():
        if k in expected:
            assert v == expected[k], (k, v, expected[k])
    return actual

freeze_bytes = git('show', FI + ':' + PREFIX + 'integration/wave2/v1/integrated-input.json')
freeze = json.loads(freeze_bytes)
assert git('rev-parse', MI + '^{tree}').decode().strip() == freeze['actual_MI_tree']
assert git('rev-parse', MI + ':deliverables/final-specification-set').decode().strip() == freeze['actual_formal_subtree']
assert git('rev-parse', B + ':deliverables/final-specification-set').decode().strip() == 'ebbe29f2bc88cd17de7072bf440c6fa8c8c7089c'
table = freeze['all_formal_file_identities']
rows = []
for r in table:
    data = git('show', MI + ':' + r['path'])
    ident = matches(data, r)
    before = git('show', B + ':' + r['path'])
    rows.append(dict(path=r['path'], **ident, equals_B=data == before))
assert len(rows) == 131
assert sum(r['equals_B'] for r in rows) == 105
for plan, dest in [('original-plans', 'original'), ('actual-plans', 'actual-input')]:
    p = Path('/workspace/r7-ir-R7-U02')
    j = json.loads((p/plan/'R7-U02.json').read_text())
    for group in ['artifacts', 'evidence', 'fixed_read_inputs']:
        for row in j[group]:
            data = (p/dest/row['local_path']).read_bytes()
            actual = matches(data, row)
            if 'git_blob_content_id' in row:
                assert actual['git_blob'] == row['git_blob_content_id']

journal = json.loads((INPUT/'integration/applied-clauses.json').read_text())
shared_checks = []
candidate_cache = {}
candidate_receipts = []
def candidate_bytes(h, local):
    key = h['candidate_commit']+':'+h['candidate_path']
    if key in candidate_cache:
        return candidate_cache[key]
    if local.exists():
        data = local.read_bytes()
        provenance = 'restored fixed plan; all identities independently rechecked above'
    else:
        url = 'https://raw.githubusercontent.com/y805939188/pokemon-essentials-clean-room/'+h['candidate_commit']+'/'+urllib.parse.quote(h['candidate_path'],safe='/')
        with urllib.request.urlopen(url, timeout=90) as response:
            assert response.status == 200
            data = response.read()
        cache = Path('/workspace/r7-ir-R7-U02/project-supplemental')/h['candidate_commit']/h['candidate_path']
        cache.parent.mkdir(parents=True, exist_ok=True)
        cache.write_bytes(data)
        provenance = url
    candidate_cache[key] = data
    candidate_receipts.append(dict(commit=h['candidate_commit'],path=h['candidate_path'],**identity(data),provenance=provenance,utc=datetime.datetime.now(datetime.timezone.utc).isoformat()))
    return data
for entry in journal['files']:
    path = entry['path']
    base_data = git('show', B+':'+path) if entry['baseline_identity']['bytes'] else b''
    matches(base_data, entry['baseline_identity'])
    base = base_data.splitlines(keepends=True)
    actual = git('show', MI+':'+path).splitlines(keepends=True)
    assembly = []
    pos = 0
    for h in entry['hunks']:
        a, b = h['base_line_indices_half_open']
        assert a >= pos
        assembly.extend(base[pos:a])
        removed = b''.join(base[a:b])
        assert removed == h['removed_text'].encode()
        matches(removed, h['removed_identity'])
        added = h['added_text'].encode()
        matches(added, h['added_identity'])
        candidate = INPUT/('candidate/candidates/R7-U02' if h['batch_id'] == 'R7-U02' else 'shared-candidate/'+h['batch_id'])/path
        candidate_data = candidate_bytes(h, candidate)
        ca, cb = h['candidate_line_indices_half_open']
        assert b''.join(candidate_data.splitlines(keepends=True)[ca:cb]) == added
        if candidate.exists():
            assert candidate_data == candidate.read_bytes()
        x, y = h['actual_final_line_indices_half_open']
        administrative_json = path.endswith('/current-navigation-errata.json')
        if not administrative_json:
            assert b''.join(actual[x:y]) == added
        shared_checks.append(dict(path=path,batch=h['batch_id'],base_lines=[a,b],actual_lines=[x,y],candidate_verified_from_fixed_commit=True,restored_candidate=candidate.exists(),added_identity=identity(added),exact_candidate_clause=True,actual_slice_exact=not administrative_json))
        assembly.extend(added.splitlines(keepends=True))
        pos = b
    assembly.extend(base[pos:])
    assembled = b''.join(assembly)
    matches(assembled, entry['assembled_candidate_clauses_identity'])
    adjustments = [x for x in journal['root_administrative_reception_adjustments'] if x['path'] == path]
    expected_actual = assembled
    for adj in adjustments:
        matches(expected_actual, adj['before_identity'])
        if 'added_text' in adj:
            expected_actual += adj['added_text'].encode()
        else:
            before_json = json.loads(expected_actual)
            after_json = json.loads(b''.join(actual))
            changed_keys = [k for k in set(before_json)|set(after_json) if before_json.get(k) != after_json.get(k)]
            assert set(changed_keys) == {'status','reception'}, changed_keys
            assert after_json['status'] == 'INTEGRATED_PENDING_INDEPENDENT_ACTUAL_REVIEW'
            assert after_json['reception']['ACCEPTED'] is False and after_json['reception']['CLOSED'] is False
            expected_actual = b''.join(actual)
        matches(expected_actual, adj['after_identity'])
    assert expected_actual == b''.join(actual)

prior = []
for f in (INPUT/'prior-accepted/actual-at-accepted-MI').rglob('*.md'):
    rel = f.relative_to(INPUT/'prior-accepted/actual-at-accepted-MI')
    assert f.read_bytes() == (INPUT/'actual'/rel).read_bytes()
    prior.append(dict(path=str(rel),**identity(f.read_bytes()),qualification='EXACT_PRESERVATION_ONLY'))
result = dict(utc=datetime.datetime.now(datetime.timezone.utc).isoformat(), fixed_B=B, MI=MI, FI=FI,
              FI_identity=identity(freeze_bytes), MI_tree=freeze['actual_MI_tree'], MI_formal_subtree=freeze['actual_formal_subtree'],
              formal_files=rows, formal_counts=dict(total=131,changed=26,unchanged=105),
              candidate_receipts=candidate_receipts,clause_checks=shared_checks, same_boundary_insertions=journal['same_boundary_insertions'],
              root_adjustments=journal['root_administrative_reception_adjustments'],prior_accepted_five=prior,
              qualification='TOOL_VALIDATION; no semantic or behavioral PASS')
(ROOT/'scope-validation.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(formal=131,changed=26,unchanged=105,clause_checks=len(shared_checks),prior_preserved=len(prior)),ensure_ascii=False))
