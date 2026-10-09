"""New bounded ACT review metadata check. No repository/reference program imports."""
import collections
import csv
import hashlib
import io
import json
import pathlib
import re
import subprocess

ACT = 'ccf0c49394995e779262375726f7002680d938bf'
BASE = '0cfe99094b76f8d75fded0d638694677855a5f0c'
CAND = '4fa6b5fcf726e8723ba1aa31b2f22a7f53390c52'
ADMIN = '4cb51a33402ec6559a396226239afe308a4b8849'
PACKET = 'f4424d30eacae80a0a5e78439488c320b6e1c5c7'
OWN = '99cecddd021d22092ebc9b78081a0ea360371a68'
FULL = 'e03a392a0374ed5aa896ff31be9ee6840ba54162'
AUTHOR_WRAPPER = 'd65a76268997051a4e5df178af9abcbd254ffa02'
ROOT = 'review/remediation/20261003-prepare/'
B11 = ROOT + 'batches/B11/'
OUT = B11 + 'integration-affected-B10-review-1/'


def git(*args):
    return subprocess.check_output(['git', *args])


def text(*args):
    return git(*args).decode().strip()


def blob(commit, path):
    return git('show', commit + ':' + path)


def digest(data):
    return hashlib.sha256(data).hexdigest()


def identity(commit, path):
    data = blob(commit, path)
    return dict(commit=commit, path=path, git_blob=text('rev-parse', commit + ':' + path),
                sha256=digest(data), bytes=len(data))


def load(commit, path):
    return json.loads(blob(commit, path))


def pointer(obj, ptr):
    for part in ptr.lstrip('/').split('/'):
        part = part.replace('~1', '/').replace('~0', '~')
        obj = obj[int(part)] if isinstance(obj, list) else obj[part]
    return obj


def canonical(obj):
    return digest(json.dumps(obj, ensure_ascii=False, sort_keys=True, separators=(',', ':')).encode())


def binding(record):
    actual = identity(record['commit'], record['path'])
    for key in ['git_blob', 'sha256', 'bytes']:
        assert actual[key] == record[key], (record['path'], key)
    return actual


assert text('remote', 'get-url', 'origin') == 'https://github.com/y805939188/pokemon-essentials-clean-room.git'
assert text('rev-parse', ACT + '^{tree}') == 'dfe7da57b26ab3f09ae5727f5e78025ebc01a617'
freeze = load(PACKET, B11 + 'actual-freeze-1/actual-freeze.json')
request = load(ACT, B11 + 'integration-stage-1/actual-review-request.json')
formal = request['formal_scope']
assert len(formal) == 10
sources = [CAND, AUTHOR_WRAPPER, OWN, FULL, ADMIN]
source_blobs = {}
for c in sources:
    source_blobs[c] = {}
    for raw in git('ls-tree', '-r', c).decode().splitlines():
        meta, path = raw.split('\t', 1)
        source_blobs[c][path] = meta.split()[2]
flows = []
for record in freeze['complete_unfiltered_differences']:
    stream = git('diff', '--binary', '--full-index', record['from'], ACT)
    assert digest(stream) == record['sha256'] and len(stream) == record['bytes']
    paths = text('diff', '--name-only', record['from'], ACT).splitlines()
    chunks = [b'diff --git ' + c for c in re.split(rb'^diff --git ', stream, flags=re.MULTILINE)[1:]]
    assert len(chunks) == len(paths) == record['changed_path_count']
    entries = []
    for path, chunk in zip(paths, chunks):
        assert chunk.splitlines()[0].decode() == 'diff --git a/' + path + ' b/' + path
        after = identity(ACT, path)
        equal_sources = [c for c in sources if source_blobs[c].get(path) == after['git_blob']]
        if path in formal:
            kind = 'FORMAL_PAYLOAD_REVIEWED_CANDIDATE_EXACT'
            assert CAND in equal_sources
        elif equal_sources:
            kind = 'EXACT_VERSIONED_EVIDENCE_OR_ADMIN_COPY'
        elif path.startswith(B11 + 'integration-stage-1/'):
            kind = 'NEW_ACTUAL_MANAGEMENT_NO_QUALITY_INFERENCE'
            if path.endswith('.json'):
                load(ACT, path)
        else:
            assert path in [ROOT + f for f in ['approval-ledger.tsv', 'traceability-successor.tsv', 'final-integration-review.md']], path
            kind = 'PUBLIC_PENDING_REGISTRATION_AND_PRESERVATION'
        assert not path.startswith('reference/')
        entries.append(dict(path=path, classification=kind, after=after,
                            exact_source_commits=equal_sources, diff_chunk_sha256=digest(chunk),
                            hunk_count=sum(l.startswith(b'@@ ') for l in chunk.splitlines())))
    flows.append(dict(command=record['command'], from_commit=record['from'], to_commit=ACT,
                      sha256=digest(stream), bytes=len(stream), changed_paths=len(paths),
                      unfiltered=True, categories=dict(collections.Counter(e['classification'] for e in entries)),
                      complete_path_inventory=entries))
assert not text('diff', '--name-only', CAND, ACT, '--', 'deliverables', 'specs', 'reference')
assert set(text('diff', '--name-only', BASE, ACT, '--', 'deliverables', 'specs').splitlines()) == set(formal) - {formal[6]}
formal_checks = [dict(path=p, BASE=identity(BASE, p), candidate=identity(CAND, p), actual=identity(ACT, p)) for p in formal]
assert all(r['candidate']['git_blob'] == r['actual']['git_blob'] for r in formal_checks)
copies = load(ACT, B11 + 'integration-stage-1/formal-copy-identities.json')
copy_checks = []
for record in copies['author_and_report_artifacts_copied']:
    binding(record)
    assert blob(record['commit'], record['path']) == blob(ACT, record['path'])
    copy_checks.append(dict(source=record, actual=identity(ACT, record['path']), equal=True))
assert len(copy_checks) == 84
own_report_checks = []
for role in ['B07', 'B09', 'B10']:
    directory = B11 + f'affected-{role}-review-round-1/'
    paths = text('ls-tree', '-r', '--name-only', OWN, '--', directory).splitlines()
    assert len(paths) == (9 if role == 'B10' else 8)
    assert all(blob(OWN, p) == blob(ACT, p) for p in paths)
    own_report_checks += [identity(ACT, p) for p in paths]

controls = load(ACT, B11 + 'refreeze-after-B10-C-1/B11-downstream-contract.json')['contribution_controls']
assert blob(ACT, B11 + 'refreeze-after-B10-C-1/B11-downstream-contract.json') == blob(ADMIN, B11 + 'refreeze-after-B10-C-1/B11-downstream-contract.json')
registration = load(ACT, B11 + 'integration-stage-1/finding-registration.json')
accepted_stats = registration['accepted_statistics_retained']
binding(accepted_stats)
assert blob(ACT, accepted_stats['path']) == blob(BASE, accepted_stats['path'])
assert len(registration['records']) == len(controls) == 6
control_checks = []
for record, control in zip(registration['records'], controls):
    assert record['id'] == control['id']
    for name in ['whole_original_object_binding', 'whole_approved_acceptance_binding', 'whole_original_object_sha256', 'whole_acceptance_object_sha256', 'complete_current_control_fields']:
        assert record[name] == control[name]
    for kind, object_key, hash_key in [('whole_original_object_binding', 'whole_original_object', 'whole_original_object_sha256'), ('whole_approved_acceptance_binding', 'whole_approved_acceptance_object', 'whole_acceptance_object_sha256')]:
        b = control[kind]
        binding(b)
        value = pointer(load(b['commit'], b['path']), b['pointer'])
        assert value == control[object_key] and canonical(value) == record[hash_key]
    assert record['accepted_contributors'] == control['accepted_contributors']
    assert record['remaining_contributors'] == control['pending_contributors']
    assert record['canonical_state'] == 'OPEN' and record['final_closure'] is False
    assert record['current_status'] == 'INTEGRATED_PENDING_EXACT_ACTUAL; NOT_ACCEPTED'
    assert record['actual_full_and_affected_receipts'] == 'PENDING_NEW_EXACT_ACTUAL_FULL_B07_B09_B10'
    for locator in record['current_formal_locators']:
        assert blob(CAND, locator['path']) == blob(ACT, locator['path'])
    control_checks.append(dict(id=record['id'], primary_owner=record['primary_owner'], primary=record['primary'],
                               registration_pointer='/records/' + str(len(control_checks)),
                               complete_control=record['complete_qualified_control_binding'],
                               original=record['whole_original_object_binding'], acceptance=record['whole_approved_acceptance_binding'],
                               full_objects_and_current_fields_equal=True, accepted_contributors=record['accepted_contributors'],
                               remaining_contributors=record['remaining_contributors'], current_locators_same_bytes=True))

public_checks = []
for filename in ['approval-ledger.tsv', 'traceability-successor.tsv']:
    path = ROOT + filename
    before, after = blob(BASE, path), blob(ACT, path)
    assert after.startswith(before)
    old = list(csv.DictReader(io.StringIO(before.decode()), delimiter='\t'))
    rows = list(csv.DictReader(io.StringIO(after.decode()), delimiter='\t'))
    assert len(old) == 201 and len(rows) == 207 and rows[:201] == old
    for row, control in zip(rows[201:], controls):
        assert row['finding_id'] == control['id'] and row['canonical_state'] == 'OPEN'
        assert row['candidate_commit'] == CAND
        obligations = json.loads(row['remaining_obligations'])
        assert obligations['accepted_contributors'] == control['accepted_contributors']
        assert obligations['remaining_contributors'] == control['pending_contributors']
        assert obligations['actual_review'] == 'PENDING_NEW_EXACT_ACTUAL_FULL_B07_B09_B10'
        assert obligations['canonical_final_closure'] == 'NOT_PERFORMED'
        if filename == 'approval-ledger.tsv':
            assert row['integration_verdict'] == 'INTEGRATED_PENDING_ALL_EXACT_ACTUAL_GATES'
            assert row['integration_review_commit'] == ''
            assert 'B11_C_PENDING' in row['downstream_gate']
        else:
            assert row['accepted_candidate_contribution'] == 'B11_CANDIDATE_LOCAL_PASS_NOT_ACTUAL_ACCEPTED'
            assert json.loads(row['remaining_batches']) == control['pending_contributors']
    public_checks.append(dict(path=path, before=identity(BASE, path), after=identity(ACT, path),
                              complete_201_raw_prefix_preserved=True, accepted_rows=201, physical_rows=207,
                              six_new_rows=rows[201:]))
canon_path = ROOT + 'finding-ledger.tsv'
assert blob(BASE, canon_path) == blob(ACT, canon_path)
canon_rows = list(csv.DictReader(io.StringIO(blob(ACT, canon_path).decode()), delimiter='\t'))
assert len(canon_rows) == 229 and all(r['canonical_state'] == 'OPEN' for r in canon_rows)
assert blob(ACT, ROOT + 'final-integration-review.md').endswith(blob(BASE, ROOT + 'final-integration-review.md'))
deps_path = ROOT + 'batches/B10/acceptance-stage-1/downstream-parallel-dispatch-1/remaining-dependencies.json'
assert blob(ADMIN, deps_path) == blob(ACT, deps_path)
deps = load(ACT, deps_path)
assert len(deps['accepted_batches']) == 11 and 'B11' not in deps['accepted_batches']
by_batch = {r['batch']: r for r in deps['remaining']}
assert 'B11' in by_batch['B12']['pending_dependencies'] and 'B11' in by_batch['B21']['pending_dependencies']
b15_paths = text('ls-tree', '-r', '--name-only', ACT, '--', ROOT + 'batches/B15/').splitlines()
assert all(p in source_blobs[ADMIN] and blob(ACT, p) == blob(ADMIN, p) for p in b15_paths)

owner_checks = {}
range_checks = {}
for role in ['B07', 'B09', 'B10']:
    old_log = load(OWN, B11 + f'affected-{role}-review-round-1/reading-log.json')
    ranges = []
    for entry in old_log['new_targeted_project_reads']:
        p = entry['path']
        assert blob(CAND, p) == blob(ACT, p)
        lines = blob(ACT, p).splitlines(keepends=True)
        for r in entry['ranges']:
            assert digest(b''.join(lines[r['line_start']-1:r['line_end']])) == r['sha256']
        ranges.append(dict(actual=identity(ACT, p), ranges=entry['ranges'], prior_candidate_bytes_equal=True))
    range_checks[role] = ranges
    checks = load(OWN, B11 + f'affected-{role}-review-round-1/static-checks.json')
    results = []
    for record in checks['accepted_owner_preservation']:
        p = record['path']
        prior = record.get('accepted_actual', record['BASE'])
        current, old = blob(ACT, p), blob(prior['commit'], p)
        if role == 'B10' and '/test-catalog/pokemon-rules-wp43-44-46-48-50.md' in p:
            assert current.startswith(old) and blob(BASE, p) == old
            kind = 'ENTIRE_ACCEPTED_PREFIX_RAW_ROW_SEQUENCE_MULTIPLICITY'
        elif record.get('accepted_owner_sections'):
            assert current == blob(BASE, p) == blob(CAND, p)
            for section in record['accepted_owner_sections']:
                prefix = section['heading'].encode()
                def extract(data):
                    lines = data.splitlines(keepends=True)
                    start = next(i for i, line in enumerate(lines) if line.startswith(prefix))
                    end = next((i for i in range(start + 1, len(lines)) if lines[i].startswith(b'## ')), len(lines))
                    return b''.join(lines[start:end])
                assert extract(current) == extract(old)
                assert digest(extract(current)) == section['sha256']
            kind = 'EXACT_ACCEPTED_BC_SW_SECTIONS_B10_P_SECTION_ALREADY_IN_BASE'
        elif record['preservation'] == 'complete file byte identity':
            assert current == old, (role, p)
            kind = 'COMPLETE_ACCEPTED_FILE_IDENTITY'
        else:
            assert current == blob(CAND, p)
            kind = 'EXACT_CANDIDATE_SCOPED_ACCEPTED_SECTION_REUSE'
        results.append(dict(path=p, accepted_source=prior, actual=identity(ACT, p), protection=kind))
    owner_checks[role] = results
catalogs = []
for p in [formal[5], formal[6], formal[7]]:
    old, current = blob(BASE, p), blob(ACT, p)
    assert current.startswith(old)
    old_rows = [l for l in old.splitlines(keepends=True) if l.startswith(b'|')]
    prefix_rows = [l for l in current[:len(old)].splitlines(keepends=True) if l.startswith(b'|')]
    assert prefix_rows == old_rows and collections.Counter(prefix_rows) == collections.Counter(old_rows)
    catalogs.append(dict(path=p, before=identity(BASE, p), actual=identity(ACT, p),
                         protected_bytes=len(old), old_lines=len(old.splitlines()), raw_table_rows=len(old_rows),
                         appended_bytes=len(current)-len(old), exact_prefix_and_order_and_multiplicity=True))

recounts = []
for final_path, original_path, expected in [(formal[2], 'specs/pokemon-rules/wp48-ability-calculation-modifiers.md', 148), (formal[3], 'specs/pokemon-rules/wp50-held-item-effect-coverage.md', 196)]:
    final_pairs, original_pairs = [], []
    families, labels = {}, {}
    for line in blob(ACT, final_path).decode().splitlines():
        cells = [c.strip() for c in line.split('|')[1:-1]]
        if not cells:
            continue
        match = re.fullmatch(r'([A-Za-z0-9]+)（(\d+)）', cells[0])
        if match:
            family, label = match.group(1), int(match.group(2))
            ids = re.findall(r'\b[A-Z][A-Z0-9]*\b', cells[1])
            assert len(ids) == len(set(ids)) == label
            families[family] = ids
            labels[family] = label
            final_pairs.extend((family, name) for name in ids)
    declared_empty = ['CertainSwitching'] if expected == 148 else ['CriticalCalcFromTarget', 'TrappingByTarget']
    empty_declaration = 'CertainSwitching 为空' if expected == 148 else 'CriticalCalcFromTarget／TrappingByTarget 为空'
    assert empty_declaration in blob(ACT, final_path).decode()
    for family in declared_empty:
        assert family not in families
        families[family] = []
        labels[family] = 0
    assert len(families) == (27 if expected == 148 else 32)
    direct = copies_count = copied_new = 0
    for line in blob(ACT, original_path).decode().splitlines():
        cells = [c.strip() for c in line.split('|')[1:-1]]
        if len(cells) < 3 or cells[0] not in families or cells[1] not in ['add', 'copy']:
            continue
        ids = re.findall(r'\b[A-Z][A-Z0-9]*\b', cells[2])
        if cells[1] == 'copy':
            assert (cells[0], ids[0]) in original_pairs
            copies_count += 1
            copied_new += len(ids) - 1
            ids = ids[1:]
        else:
            direct += len(ids)
        original_pairs.extend((cells[0], name) for name in ids)
    assert collections.Counter(original_pairs) == collections.Counter(final_pairs)
    assert len(final_pairs) == len(set(final_pairs)) == expected
    recounts.append(dict(final=identity(ACT, final_path), original=identity(ACT, original_path),
                         family_count=len(families), pair_count=expected, direct=direct,
                         copy_statements=copies_count, new_copy_pairs=copied_new, labels=labels,
                         explicit_empty_families=declared_empty,
                         exact_original_final_pair_multiset=True, identities_not_behavior_coverage=True))

result = dict(schema='new-independent-bounded-actual-static-metadata-v1', reviewed_sha=ACT,
              reviewed_tree=text('rev-parse', ACT + '^{tree}'), accepted_predecessor=BASE, candidate=CAND,
              management_packet_not_reviewed=PACKET, complete_unfiltered_flows=flows,
              ten_formal_identity_checks=formal_checks, eighty_four_exact_copies=copy_checks,
              own_candidate_report_exact_reuse=own_report_checks, complete_registration_control_checks=control_checks,
              public_pending_checks=public_checks, canonical_ledger=identity(ACT, canon_path),
              accepted_statistics_exact_preservation=identity(ACT, accepted_stats['path']),
              accepted_batches=11, accepted_contributions=201, canonical_OPEN=229, canonical_CLOSED=0,
              downstream_dependencies=identity(ACT, deps_path), B12_B21_wait_B11_C=True,
              B15_refreeze_files_preserved_and_candidate_absent=len(b15_paths),
              exact_owner_preservation=owner_checks, current_role_ranges=range_checks,
              catalog_prefix_checks=catalogs, new_opaque_identity_recounts=recounts,
              reference_execution=0, historical_program_execution=0, behavior_vector_execution=0)
pathlib.Path(OUT + 'static-checks.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
print(json.dumps(dict(status='PASS_STATIC_METADATA', flows=[{k:v for k,v in f.items() if k != 'complete_path_inventory'} for f in flows],
                      formal_paths=10, preserved_candidate_report_files=len(own_report_checks),
                      owner_files={r:len(v) for r,v in owner_checks.items()},
                      counts=[{k:v for k,v in c.items() if k not in ['final','original','labels']} for c in recounts]), ensure_ascii=False))
