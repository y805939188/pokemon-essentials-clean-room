import datetime, hashlib, json, os, pathlib, subprocess

ROOT = pathlib.Path('/workspace/r7-ir-R7-U06')
REPO = ROOT / 'result'
B = 'e646432c644dec04d306842cc5a559a29c718fbc'
MI = '45c80832a41c1b56dcd7e9d93497758cbb7721de'
FI = '13d76ba61838b13925ba9d41f58a6b047564d926'
DISPATCH = 'c64774c60d91e522cb515ef71e3e9d4ea6b4712c'
PRE = 'review/remediation-seventh-20261015-prepare/'

def git(*args):
    return subprocess.check_output(['git', '-c', 'credential.helper=', '-c', 'http.extraHeader=', *args], cwd=REPO)

def ident(data):
    return dict(bytes=len(data), sha256=hashlib.sha256(data).hexdigest(), git_blob=hashlib.sha1(f'blob {len(data)}\0'.encode()+data).hexdigest())

def verify(data, expected):
    got = ident(data)
    for key, value in expected.items():
        if key in got:
            assert got[key] == value, (key, got[key], value)
    return got

j = json.loads((ROOT/'actual-input/integration/applied-clauses.json').read_text())
bindings = {x['id']: x for x in j['source_bindings']}
adjustments = {x['path']: x for x in j['root_administrative_reception_adjustments']}
rows = []
errata_diff = None
for f in j['files']:
    if f['baseline_identity']['bytes'] == 0 and not git('ls-tree', B, '--', f['path']).strip():
        base = b''
    else:
        base = git('show', B+':'+f['path'])
    actual = git('show', MI+':'+f['path'])
    verify(base, f['baseline_identity'])
    lines = base.decode().splitlines(keepends=True)
    assembled = []
    cursor = 0
    prior = None
    for h in f['hunks']:
        a, b = h['base_line_indices_half_open']
        assert a >= cursor
        if prior and prior['base_line_indices_half_open'] == [a, b] and a == b:
            assert prior['batch_id'] == 'R7-U01' and h['batch_id'] == 'R7-U02'
            assert any(x['path'] == f['path'] and x['base_boundary'] == a for x in j['same_boundary_insertions'])
        assert ''.join(lines[a:b]) == h['removed_text']
        verify(h['removed_text'].encode(), h['removed_identity'])
        verify(h['added_text'].encode(), h['added_identity'])
        assert h['candidate_commit'] == bindings[h['batch_id']]['candidate_commit']
        assembled.extend(lines[cursor:a])
        assembled.append(h['added_text'])
        cursor = b
        prior = h
    assembled.extend(lines[cursor:])
    before = ''.join(assembled).encode()
    verify(before, f['assembled_candidate_clauses_identity'])
    if f['path'] in adjustments:
        adj = adjustments[f['path']]
        verify(before, adj['before_identity'])
        verify(actual, adj['after_identity'])
        if 'added_text' in adj:
            assert before+adj['added_text'].encode() == actual
        else:
            before_obj, after_obj = json.loads(before), json.loads(actual)
            changed = {key: {'before': before_obj.get(key), 'after': after_obj.get(key)} for key in before_obj.keys() | after_obj.keys() if before_obj.get(key) != after_obj.get(key)}
            errata_diff = changed
    else:
        assert before == actual
    rows.append({'path': f['path'], 'contributors': f['contributors'], 'hunks': len(f['hunks']), 'actual_MI': ident(actual), 'journal_reconstruction_exact': True, 'semantic_approval_for_other_batches': False})

fixed_files = []
for commit, path, local in [
    (DISPATCH, PRE+'integration/wave2/v1/dispatch/R7-U06-R7IR.md', 'bootstrap-evidence/dispatch.md'),
    (FI, PRE+'integration/wave2/v1/integrated-input.json', 'bootstrap-evidence/integrated-input.json'),
    (FI, PRE+'integration/wave2/v1/integrated-restore/R7-U06.json', 'actual-plans/R7-U06.json'),
    (MI, 'AGENTS.md', 'actual-input/actual/AGENTS.md'),
]:
    data = git('show', commit+':'+path)
    assert data == (ROOT/local).read_bytes()
    fixed_files.append({'commit': commit, 'path': path, 'local_path': local, **ident(data), 'git_and_restored_bytes_equal': True})

links = []
for path in [PRE+'integration/wave2/v1/public-reception.json', PRE+'current-navigation-errata.json']:
    data = git('show', MI+':'+path)
    links.append({'fixed_commit': MI, 'path': path, **ident(data), 'exists': True})
pub = json.loads((ROOT/'actual-input/integration/public-reception.json').read_text())
assert pub['source_bindings'] == j['source_bindings']
assert [x for x in pub['source_bindings'] if x['id']=='R7-U06'][0]['candidate_commit'] == 'fd0c1e6f50587331846921d446d893f1c1e84f3d'

ledger = [json.loads(line) for line in (ROOT/'bootstrap-evidence/read-ledger.jsonl').read_text().splitlines()]
coverage = []
for p in sorted((ROOT/'actual-input/actual').rglob('*')):
    if not p.is_file():
        continue
    n = len(p.read_text().splitlines())
    seen = set()
    for entry in ledger:
        if entry['path'] == str(p):
            seen.update(range(entry['lines'][0], entry['lines'][1]+1))
    missing = sorted(set(range(1, n+1))-seen)
    assert not missing, (p, missing)
    coverage.append({'path': str(p.relative_to(ROOT/'actual-input/actual')), 'file_lines': n, 'numbered_read_ranges_cover_all_lines': True, 'qualification': 'Read trace only; semantic reasoning is in per-id.json/report.md; hash/coverage alone is not PASS'})

out = {'utc': datetime.datetime.now(datetime.timezone.utc).isoformat(), 'pid': os.getpid(), 'kind': 'TOOL_VALIDATION_ONLY', 'behavior_execution': 'NOT_EXECUTED', 'cumulative_journal_reconstruction': rows, 'same_boundary_insertions': j['same_boundary_insertions'], 'root_errata_changed_fields': errata_diff, 'fixed_files': fixed_files, 'reception_links': links, 'U06_shared_preservation_checks': [], 'U06_targets_other_current_contributors': [], 'complete_required_actual_read_trace': coverage, 'limits': 'Only U06 receives content review. Reconstructing other journal text is transport/integration metadata validation, never a new semantic PASS, dependency receipt, acceptance or closure.'}
(ROOT/'bootstrap-evidence/cumulative-metadata-audit.json').write_text(json.dumps(out, ensure_ascii=False, indent=2)+'\n')
print(json.dumps({'cumulative_targets': len(rows), 'hunks': sum(x['hunks'] for x in rows), 'required_actual_full_read_files': len(coverage), 'errata_changed_fields': errata_diff, 'result': 'MECHANICAL_METADATA_VERIFIED_NO_ADDITIONAL_SEMANTIC_CREDIT'}, ensure_ascii=False))
