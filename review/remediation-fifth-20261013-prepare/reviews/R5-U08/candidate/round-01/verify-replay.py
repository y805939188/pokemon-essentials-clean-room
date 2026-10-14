#!/usr/bin/env python3
"""Independent R5-U08 document-byte replay. No reference/model/host execution.

Run from any directory: python verify-replay.py --repo /workspace/r5-u08-independent
All projections are private temporary directories under /tmp. Only the four
review output files next to this script are written; no git mutation is used.
"""
import argparse
import collections
import difflib
import hashlib
import json
import pathlib
import subprocess
import tempfile

B5 = '9366d9d17aaeac3b4414236468affa650fb3dd27'
FREEZE = '22fba7786b0090a1955ce6211315b0036cddfbcd'
SUBJECT = 'e4ea8d03b0e2c7c20fc41fce92f0b2b7b7f02514'
CORE = 'f623c2ecdd1c6a52d44145fdc7599624a8c64f7b'
LOCATOR = '9f19756ab9eb73d94ceb2707ea97bfe0986d43dd'
ROOT = 'review/remediation-fifth-20261013-prepare'
INPUT = ROOT + '/integration/R5-U08/candidate-01'
FORMAL = 'deliverables/final-specification-set'
SUPPORT = ['planning/feature-matrix.md', 'planning/coverage.md', 'audit/source-traceability.md']
STAGES = [
    ('R5-U01', 'd4f06b3b4eb7905d019d2c037b2642103c91972e', 'actual-01'),
    ('R5-U02', '05f63178be9b751ee6512d4cda5464e3e1d239c4', 'actual-01'),
    ('R5-U03', '8b25b16c531d454588b0ba190f3602a840f4e9ff', 'actual-01'),
    ('R5-U03-revision-in-operation49', 'df2c338ca3aff4c0b0bf4087442215877a5df597', 'actual-02'),
    ('R5-U04', '15bda43997b6b8d294f997dc4620f2359b4c8dfc', 'actual-01'),
    ('R5-U05', 'effb28783bb5ee953ba19499ee74f64323b5c15e', 'actual-01'),
    ('R5-U06', 'd73d8d633441336fbd587608c3909414a2737a75', 'actual-01'),
    ('R5-U07', 'c4925526acf0aa54dd14390636cf368b40f6d233', 'actual-01'),
]
RECEIPTS = {
    'R5-U01': '20261013-u01-formal-acceptance/U01-formal-acceptance.json',
    'R5-U02': '20261013-u02-acceptance-u03-limited-repair/U02-formal-acceptance.json',
    'R5-U03': '20261013-u03-formal-acceptance/U03-formal-acceptance.json',
    'R5-U04': '20261013-u04-formal-acceptance/U04-formal-acceptance.json',
    'R5-U05': '20261013-u05-formal-acceptance/U05-formal-acceptance.json',
    'R5-U06': '20261014-u06-formal-acceptance/U06-formal-acceptance.json',
    'R5-U07': '20261014-u07-formal-acceptance/U07-formal-acceptance.json',
}


def identity(data):
    return {'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest(),
            'git_blob': hashlib.sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest()}


def canonical_sha(value):
    return hashlib.sha256(json.dumps(value, ensure_ascii=False, sort_keys=True,
                                     separators=(',', ':')).encode()).hexdigest()


def pointer(value, coordinate):
    for part in coordinate.strip('/').split('/'):
        if part:
            part = part.replace('~1', '/').replace('~0', '~')
            value = value[int(part)] if isinstance(value, list) else value[part]
    return value


class Git:
    def __init__(self, repo):
        self.repo = repo
        self.proc = subprocess.Popen(['git', 'cat-file', '--batch'], cwd=repo,
                                     stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        self.cache = {}
        self.reads = {}

    def cmd(self, *args):
        return subprocess.check_output(['git', *args], cwd=self.repo)

    def get(self, commit, path, purpose='document identity and mechanical replay'):
        key = commit + ':' + path
        if key not in self.cache:
            self.proc.stdin.write(key.encode() + b'\n')
            self.proc.stdin.flush()
            header = self.proc.stdout.readline().decode().strip().split()
            if len(header) != 3:
                raise ValueError('Missing pinned Git object: ' + key)
            oid, typ, length = header
            if typ != 'blob':
                raise ValueError('Expected a blob: ' + key)
            data = self.proc.stdout.read(int(length))
            if self.proc.stdout.read(1) != b'\n':
                raise ValueError('Invalid cat-file framing')
            if identity(data)['git_blob'] != oid:
                raise ValueError('Git object identity mismatch: ' + key)
            self.cache[key] = data
            self.reads[key] = {'commit': commit, 'path': path, **identity(data),
                               'full_blob_read': True, 'purposes': set()}
        self.reads[key]['purposes'].add(purpose)
        return self.cache[key]

    def load(self, commit, path, purpose='pinned JSON schema and byte identity'):
        return json.loads(self.get(commit, path, purpose))

    def tree(self, commit, root=FORMAL):
        return self.cmd('rev-parse', commit + ':' + root).decode().strip()

    def files(self, commit, root=FORMAL):
        rows = self.cmd('ls-tree', '-rz', '--full-tree', commit, '--', root).split(b'\0')
        result = {}
        for row in rows:
            if row:
                meta, path = row.split(b'\t', 1)
                mode, typ, oid = meta.decode().split()
                result[path.decode()] = {'mode': mode, 'type': typ, 'git_blob': oid}
        return result


def run(repo, out):
    git = Git(repo)
    failures = []
    notes = []

    def check(ok, what, details=None):
        if not ok:
            failures.append({'check': what, 'details': details})
        return bool(ok)

    def matches(data, declared, what):
        got = identity(data)
        ok = all(got[k] == declared[k] for k in ['bytes', 'sha256', 'git_blob'] if k in declared)
        check(ok, what, {'computed': got, 'declared': declared})
        return ok

    def ref_record(ref):
        obj = git.load(ref['commit'], ref['path'], 'frozen author operation/fragment record')
        return pointer(obj, ref.get('pointer', ''))

    def normalized_author(op, batch):
        path = op.get('target_path', op.get('target'))
        kind = op.get('kind', op.get('operation'))
        if batch == 'R5-U01':
            before, payload = op['b5_anchor'], op['payload']
        elif batch == 'R5-U02':
            before, payload = op['before'], op['after']
        elif batch == 'R5-U03':
            before, payload = op.get('old_text', ''), op['new_text']
        elif batch == 'R5-U04':
            before, payload = op.get('B5_anchor', ''), op['replacement']
        elif batch == 'R5-U06':
            before, payload = op['before'], op['after']
        else:
            raise ValueError(batch)
        return path, kind, before.encode(), payload.encode()

    def apply_author(state, path, kind, before, payload, batch):
        data = state[path]
        if kind == 'append':
            if batch == 'R5-U04':
                # Reproduce the author's exact documented separator convention.
                rewritten = data.rstrip() + b'\n\n' + payload.strip() + b'\n'
                offset = len(data.rstrip()) + 2
            else:
                offset, rewritten = len(data), data + payload
        else:
            check(data.count(before) == 1, batch + ' unique approved anchor', {'path': path})
            if data.count(before) != 1:
                raise ValueError('Nonunique author anchor: ' + path)
            offset = data.index(before)
            after = payload + before if kind == 'insert_before' else payload
            rewritten = data[:offset] + after + data[offset + len(before):]
        state[path] = rewritten
        return offset

    subject_desc = git.load(CORE, INPUT + '/current-formal131-identities.json')
    plan = git.load(CORE, INPUT + '/mechanical-replay.json')
    owners_desc = git.load(CORE, INPUT + '/sole-writer85.json')
    owners_frozen = git.load(FREEZE, ROOT + '/frozen-input/shared-file-owners.json')
    matches(git.get(FREEZE, ROOT + '/frozen-input/shared-file-owners.json'),
            owners_desc['frozen_source'], 'sole-writer frozen-source bytes/SHA/blob')
    locator = git.load(LOCATOR, INPUT + '/candidate-review-input.json')
    git.get(CORE, 'AGENTS.md', 'workspace instructions')
    git.get(CORE, INPUT + '/reviewer-entry.md', 'scope/identity/stage requirements')
    git.get(CORE, INPUT + '/acceptance-checklist.json', 'G01/G03/G05/G06/G11 applicable requirements')
    expected_trees = {LOCATOR: '89976655b95e4faa04e7ff0bd8cfd597579961c3',
                      CORE: 'dcab935559e54f7a454fd9b86fd3bc25c0372182',
                      SUBJECT: '4cb802d1f7114ac4d0d2dbacfa0be58586e3ed8c'}
    for commit, tree in expected_trees.items():
        check(git.cmd('rev-parse', commit + '^{tree}').decode().strip() == tree,
              'pinned commit tree', {'commit': commit, 'tree': tree})
    check(plan['from_B5'] == B5 and plan['current_base'] == SUBJECT, 'replay endpoints pinned')
    file_index = git.files(B5)
    paths = sorted(file_index)
    check(len(paths) == 131, 'B5 independently enumerated formal131', len(paths))
    check(set(paths) == {x['path'] for x in subject_desc['files']}, 'descriptor formal131 exact set')
    frozen_by_path = {x['path']: x for x in owners_frozen['files']}
    owners_by_path = {x['path']: x for x in owners_desc['files']}
    check(len(frozen_by_path) == len(owners_frozen['files']) == 85, 'frozen unique85')
    check(set(frozen_by_path) == set(owners_by_path), 'candidate owner set matches frozen85')
    shared = {p for p, x in frozen_by_path.items() if x['writer'] == 'R5-I'}
    check(len(shared) == 21, 'frozen shared21')
    check(len(frozen_by_path) - len(shared) == 64, 'frozen nonshared64')
    state = {p: git.get(B5, p) for p in paths}
    b5_state = state.copy()
    receipts = {}
    receipt_refs = {}
    review_bindings = {}
    contracts = {}
    for batch, suffix in RECEIPTS.items():
        contracts[batch] = git.load(FREEZE, ROOT + '/contracts/' + batch + '/contract.json',
                                    'frozen per-finding formal permissions and sole semantic owner')
        git.get(FREEZE, ROOT + '/contracts/' + batch + '/author-entry.md',
                'owner mirror/shared write boundary; mechanical R5-I reception permission')
        path = ROOT + '/registration/successors/' + suffix
        raw = git.get(SUBJECT, path, 'unique accepted owner-scope receipt')
        receipt = json.loads(raw)
        receipts[batch] = receipt
        receipt_refs[batch] = {'commit': SUBJECT, 'path': path, **identity(raw)}
        review = receipt['independent_review']
        check(git.cmd('rev-parse', review['commit'] + '^{tree}').decode().strip() == review['tree'],
              batch + ' independent actual review tree')
        files = []
        for value in review.values():
            if isinstance(value, dict) and 'path' in value:
                rcommit = value.get('commit', review['commit'])
                review_raw = git.get(rcommit, value['path'], 'exact prior independent actual review record, no semantic transfer')
                matches(review_raw, value, batch + ' prior independent review byte identity')
                files.append({'commit': rcommit, 'path': value['path'], **identity(review_raw)})
        review_bindings[batch] = {'commit': review['commit'], 'tree': review['tree'], 'files': files}

    stages = []
    all_operations = []
    contributions = collections.defaultdict(list)
    previous = B5
    op49_revision = {}
    with tempfile.TemporaryDirectory(prefix='r5-u08-independent-replay-', dir='/tmp') as temp:
        temp = pathlib.Path(temp)
        patch_root = temp / 'accepted-replay'
        patch_root.mkdir()
        for p, data in state.items():
            target = patch_root / p
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(data)
        for ix, (stage, actual, round_id) in enumerate(STAGES):
            batch = 'R5-U03' if 'revision' in stage else stage
            mapping_path = ROOT + '/integration/' + batch + '/' + round_id + '/candidate-to-actual.json'
            mapping_raw = git.get(actual, mapping_path, 'actual-to-frozen-author byte mapping independently checked')
            mapping = json.loads(mapping_raw)
            declared_stage = plan['steps'][ix]
            check(declared_stage['stage'] == stage and declared_stage['actual_commit'] == actual,
                  'frozen replay step identity', {'stage': stage})
            matches(mapping_raw, declared_stage['mapping'], stage + ' mapping bytes/SHA/blob')
            check(git.cmd('rev-parse', actual + '^{tree}').decode().strip() == declared_stage['actual_tree'],
                  stage + ' actual tree')
            check(git.tree(actual) == declared_stage['formal_tree'], stage + ' formal tree')
            actual_file_index = git.files(actual)
            check(set(actual_file_index) == set(paths), stage + ' independently enumerated formal131 set')
            before_state = state.copy()
            operations = []
            mirror_checks = []
            fragment_checks = []
            if 'revision' in stage:
                candidate = mapping['candidate']['commit']
                old_candidate = 'd84bf0dd0eac4605c98d8ba4ae3f8502117fc5a7'
                author_root = ROOT + '/candidates/R5-U03/author/'
                old_ops = git.load(old_candidate, author_root + 'operations.json')['operations']
                new_ops = git.load(candidate, author_root + 'operations.json')['operations']
                old_vec = git.load(old_candidate, author_root + 'static-vectors.json')['vectors']
                new_vec = git.load(candidate, author_root + 'static-vectors.json')['vectors']
                check(len(old_ops) == len(new_ops) == 52, 'U03 retains52 canonical operations')
                check([j for j in range(52) if old_ops[j] != new_ops[j]] == [49], 'U03 only operation49 revised')
                check([k for k in old_ops[49] if old_ops[49][k] != new_ops[49][k]] == ['new_text'],
                      'U03 op49 only new_text revised')
                check(len(old_vec) == len(new_vec) == 69, 'U03 retains69 vector records')
                check([j for j in range(69) if old_vec[j] != new_vec[j]] == [45], 'U03 only vector45 revised')
                check([k for k in old_vec[45] if old_vec[45][k] != new_vec[45][k]] == ['input'],
                      'U03 only vector45 input revised')
                row = mapping['one_row']
                path = mapping['changed_formal_file']['path']
                offset = row['utf8_byte_offset']
                old_row = state[path][offset:offset + row['old_identity']['bytes']]
                new_row = row['new_row'].encode()
                def vector_row(v):
                    return ('| ' + v['id'] + ' | ' + v['premises'] + ' | ' + v['input'] + ' | ' + v['expected'] + ' |\n').encode()
                check(old_row == vector_row(old_vec[45]), 'U03 old failed catalog row equals original vector45')
                check(new_row == vector_row(new_vec[45]), 'U03 revised catalog row equals author vector45')
                matches(old_row, row['old_identity'], 'U03 exact old failed row')
                matches(new_row, row['new_identity'], 'U03 exact approved repaired row')
                check(old_ops[49]['new_text'].encode().replace(old_row, new_row, 1) == new_ops[49]['new_text'].encode(),
                      'U03 old op49 payload differs by exactly repaired row')
                check(old_ops[49]['new_text'].encode().count(old_row) == 1, 'U03 unique old row in operation49')
                check(new_ops[49]['new_text'].encode().count(new_row) == 1, 'U03 unique new row in operation49')
                check(canonical_sha(old_ops[49]) == row['prior_operation_record_sha256'], 'U03 prior op49 record identity')
                check(canonical_sha(new_ops[49]) == row['approved_operation_record_sha256'], 'U03 approved op49 record identity')
                state[path] = state[path][:offset] + new_row + state[path][offset + len(old_row):]
                mirror = git.get(candidate, mapping['changed_formal_file']['candidate_mirror_path'],
                                 'original author repaired nonshared mirror')
                check(state[path] == mirror, 'U03 original-author repaired mirror exact')
                for side in ['before', 'after']:
                    matches(before_state[path] if side == 'before' else state[path],
                            mapping['changed_formal_file'][side], 'U03 revised file ' + side)
                response = git.load(candidate, mapping['candidate']['author_response'], 'original author limited repair provenance')
                prior_checks = []
                prior_path = ROOT + '/reviews/R5-U03/actual/round-01/criterion-results.json'
                prior_criteria = git.load('1eda123e3bcd4b1aa99e2ba57c6de02d56414716', prior_path,
                                          'exact preserved59 prior qualified static record identities; no new signature')
                check(len(response['unchanged_prior_static_PASS']) == 59, 'U03 exactly59 prior static qualified records')
                for prior in response['unchanged_prior_static_PASS']:
                    old_record = pointer(prior_criteria, prior['pointer'])
                    record_sha = canonical_sha(old_record)
                    ok = check(record_sha == prior['frozen_record_sha256'], 'U03 prior59 exact record identity',
                               {'criterion_id': prior['criterion_id'], 'pointer': prior['pointer']})
                    prior_checks.append({'criterion_id': prior['criterion_id'], 'review_commit': prior['review_commit'],
                                         'path': prior_path, 'pointer': prior['pointer'], 'record_sha256': record_sha,
                                         'result': 'PASS_EXACT_UNCHANGED_SCOPE_IDENTITY' if ok else 'FAIL',
                                         'new_semantic_signature': False})
                mirror_root = author_root + 'formal'
                fragment_root = author_root + 'fragments'
                candidate_document_deltas = git.cmd('diff', '--name-only', old_candidate, candidate, '--',
                                                    mirror_root, fragment_root).decode().splitlines()
                check(candidate_document_deltas == [mapping['changed_formal_file']['candidate_mirror_path']],
                      'U03 only approved catalog mirror changes; all other mirrors/fragments exact', candidate_document_deltas)
                check(git.get(old_candidate, author_root + 'fragment-manifest.json') ==
                      git.get(candidate, author_root + 'fragment-manifest.json'), 'U03 all31 original fragment records unchanged')
                check(response['author_base']['commit'] == old_candidate and response['scope'] == 'GR5-M05-004/static/04',
                      'U03 author limited response exact original base and qualification')
                gate = mapping['independent_candidate_review']
                git.get(gate['commit'], gate['report'], 'original nonauthor independent one-row candidate gate')
                git.get('1eda123e3bcd4b1aa99e2ba57c6de02d56414716',
                        ROOT + '/reviews/R5-U03/actual/round-01/report.md', 'preserved original actual01 FAIL')
                op49_revision = {'verdict': 'PASS_DOCUMENT_IDENTITY_AND_QUALIFIED_ELIGIBILITY',
                    'original_actual01': previous, 'original_actual01_status': 'FAIL_RETAINED_NOT_ACCEPTED',
                    'original_author_candidate': candidate, 'actual02': actual,
                    'candidate_review': gate['commit'], 'actual_review': review_bindings[batch],
                    'accepted_receipt': receipt_refs[batch], 'target_path': path,
                    'operation_index': 49, 'vector_index': 45, 'changed_operation_field': 'new_text',
                    'changed_vector_field': 'input', 'old_row_identity': identity(old_row),
                    'new_row_identity': identity(new_row), 'canonical_operation_count_remains': 52,
                    'new_canonical_contribution_count': 0, 'revision_event_count': 1,
                    'original_author_response_schema': response.get('schema'),
                    'original_author_response': {'commit': candidate, 'path': mapping['candidate']['author_response'],
                                                 **identity(git.get(candidate, mapping['candidate']['author_response']))},
                    'prior59_qualified_record_identity_results': prior_checks,
                    'candidate_document_changed_paths': candidate_document_deltas,
                    'qualification': 'Only GR5-M05-004/static/04, R5U03-M05-004-02 consumption prerequisite; prior59 exact scopes reused. No full-ID or behavior-execution promotion.'}
                operations.append({'operation_id': 'R5-U03/operation/49/revision-event', 'target_path': path,
                                   'source_record_sha256': canonical_sha(new_ops[49]),
                                   'approved_payload_identity': identity(new_row), 'pre_operation_utf8_byte_offset': offset,
                                   'source': {'commit': candidate, 'path': author_root + 'operations.json',
                                              'pointer': '/operations/49/new_text'}, 'canonical_contribution': False,
                                   'result': 'PASS'})
            elif batch == 'R5-U05':
                candidate = mapping['candidate']['commit']
                for transfer in mapping['files']:
                    source = transfer['approved_mirror']
                    data = git.get(source['commit'], source['path'], 'approved direct whole-mirror transfer')
                    matches(data, source, batch + ' direct mirror source identity')
                    mrecord = ref_record(transfer['source_fragment_manifest'])
                    check(canonical_sha(mrecord) == transfer['source_fragment_manifest']['record_sha256'],
                          batch + ' frozen mirror transfer record identity')
                    path = transfer['target_path']
                    state[path] = data
                    matches(data, transfer['actual_after'], batch + ' mapped actual mirror identity')
                    operations.append({'operation_id': transfer['transfer_id'], 'target_path': path,
                                       'source': source, 'source_record_sha256': canonical_sha(mrecord),
                                       'approved_payload_identity': identity(data), 'canonical_contribution': True,
                                       'result': 'PASS'})
            elif batch == 'R5-U07':
                candidate = mapping['candidate']['commit']
                for fragment in mapping['shared_fragment_records']:
                    source = fragment['source_manifest']
                    authored = ref_record(source)
                    check(canonical_sha(authored) == source['record_sha256'], batch + ' source fragment record SHA')
                    payload_path = ROOT + '/candidates/R5-U07/author/' + authored['payload_file']
                    payload_file = git.get(candidate, payload_path, 'frozen shared fragment payload bytes')
                    start, size = authored['payload_byte_offset'], authored['payload_bytes']
                    payload = payload_file[start:start + size]
                    check(hashlib.sha256(payload).hexdigest() == authored['payload_sha256'], batch + ' source fragment payload SHA')
                    matches(payload, fragment['source_payload'], batch + ' mapped source payload identity')
                    check(payload == fragment['approved_payload'].encode(), batch + ' integrator incoming payload unchanged')
                    path = authored['target_path']
                    before = authored['base_text'].encode()
                    check(before == fragment['base_text'].encode(), batch + ' incoming anchor unchanged')
                    kind = authored['operation']
                    if kind in ['replace_exact', 'replace_exact_anchor']:
                        kind = 'replace'
                    offset = apply_author(state, path, kind, before, payload, batch)
                    check(offset == fragment['current_before_utf8_byte_offset'], batch + ' fragment current byte offset')
                    operations.append({'operation_id': authored['id'], 'target_path': path, 'source': source,
                                       'source_record_sha256': canonical_sha(authored), 'approved_payload_identity': identity(payload),
                                       'pre_operation_utf8_byte_offset': offset, 'canonical_contribution': True, 'result': 'PASS'})
                transfer = mapping['nonshared_mirror_transfer']
                source = transfer['source']
                data = git.get(source['commit'], source['path'], 'approved U07 nonshared direct mirror')
                state[transfer['target']] = data
                operations.append({'operation_id': 'R5-U07/direct-mirror/00', 'target_path': transfer['target'],
                                   'source': source, 'approved_payload_identity': identity(data),
                                   'canonical_contribution': True, 'result': 'PASS'})
            else:
                c = mapping['candidate']
                candidate = c['commit'] if isinstance(c, dict) else c
                for mapped in mapping['operations']:
                    source = mapped.get('source', mapped.get('candidate_source', mapped.get('source_candidate')))
                    authored = ref_record(source)
                    author_sha = canonical_sha(authored)
                    declared_sha = mapped.get('operation_record_sha256', mapped.get('source_record_sha256', source.get('record_sha256')))
                    check(author_sha == declared_sha, batch + ' frozen author operation record SHA')
                    path, kind, before, payload = normalized_author(authored, batch)
                    check(path == mapped.get('target_path', mapped.get('target')), batch + ' incoming target unchanged')
                    if batch == 'R5-U01':
                        check(kind == mapped['kind'], batch + ' incoming operation kind unchanged')
                        check(identity(before)['sha256'] == mapped['anchor_sha256'], batch + ' approved anchor SHA')
                        check(identity(payload)['sha256'] == mapped['payload_sha256'], batch + ' approved payload SHA')
                    else:
                        before_field = mapped.get('before', '')
                        after_field = mapped.get('approved_after', mapped.get('approved_payload', mapped.get('after', '')))
                        if kind != 'append':
                            check(before == before_field.encode(), batch + ' approved source anchor unchanged')
                        check(payload == after_field.encode(), batch + ' approved source payload unchanged')
                    offset = apply_author(state, path, kind, before, payload, batch)
                    declared_offset = mapped.get('pre_operation_byte_offset', mapped.get('current_pre_operation_byte_offset',
                                      mapped.get('pre_operation_utf8_byte_offset', mapped.get('current_pre_operation_utf8_byte_offset'))))
                    # U04 append maps the terminal separator replacement, not the inserted section start.
                    if kind != 'append' or batch != 'R5-U04':
                        check(offset == declared_offset, batch + ' operation byte offset', {'path': path, 'id': mapped.get('operation_id', mapped.get('id', mapped.get('edit_id')))})
                    operations.append({'operation_id': mapped.get('operation_id', mapped.get('id', mapped.get('edit_id'))),
                                       'target_path': path, 'source': source, 'source_record_sha256': author_sha,
                                       'approved_payload_identity': identity(payload), 'pre_operation_utf8_byte_offset': offset,
                                       'canonical_contribution': True, 'result': 'PASS'})
            touched = sorted(p for p in paths if state[p] != before_state[p])
            if 'revision' not in stage and batch != 'R5-U05':
                manifest_path = ROOT + '/candidates/' + batch + '/author/fragment-manifest.json'
                fragment_manifest = git.load(candidate, manifest_path, 'all approved shared fragment payload associations')
                for findex, fragment in enumerate(fragment_manifest['fragments']):
                    path = fragment.get('target_path', fragment.get('target'))
                    check(path in shared, batch + ' fragment only addresses frozen shared path', {'path': path})
                    if batch == 'R5-U01':
                        payload_path = fragment['payload_path']
                        raw = git.get(candidate, payload_path, 'exact frozen shared fragment file')
                        start, size = fragment['payload_start_byte'], fragment['payload_bytes']
                        payload = raw[start:start + size]
                        check(identity(payload)['sha256'] == fragment['payload_sha256'], batch + ' shared fragment slab SHA')
                    elif batch == 'R5-U02':
                        payload_path = fragment['payload_path']
                        raw = git.get(candidate, payload_path, 'exact frozen shared fragment file')
                        op = next(o for o in operations if o['operation_id'] == fragment['fragment_id'])
                        authored = ref_record(op['source'])
                        payload = authored['after'].encode()
                        check(len(payload) == fragment['replacement_bytes'] and identity(payload)['sha256'] == fragment['replacement_sha256'],
                              batch + ' fragment declared source replacement identity')
                        check(payload in raw, batch + ' exact approved payload occurs in frozen fragment file')
                    elif batch == 'R5-U03':
                        payload_path = ROOT + '/candidates/' + batch + '/author/' + fragment['fragment_file']
                        raw = git.get(candidate, payload_path, 'exact frozen shared fragment file')
                        payload = fragment['new_text'].encode()
                        check(payload in raw, batch + ' exact approved payload occurs in frozen fragment file')
                    elif batch == 'R5-U04':
                        payload_path = fragment['fragment_path']
                        raw = git.get(candidate, payload_path, 'exact frozen shared fragment file')
                        payload = fragment['replacement'].encode()
                        check(payload in raw, batch + ' exact approved payload occurs in frozen fragment file')
                    elif batch == 'R5-U06':
                        payload_path = fragment['candidate_path']
                        raw = git.get(candidate, payload_path, 'exact frozen shared fragment file')
                        payload = fragment['after'].encode()
                        check(payload in raw, batch + ' exact approved payload occurs in frozen fragment file')
                    else:
                        payload_path = ROOT + '/candidates/' + batch + '/author/' + fragment['payload_file']
                        raw = git.get(candidate, payload_path, 'exact frozen shared fragment file')
                        start, size = fragment['payload_byte_offset'], fragment['payload_bytes']
                        payload = raw[start:start + size]
                        check(identity(payload)['sha256'] == fragment['payload_sha256'], batch + ' shared fragment slab SHA')
                    matches_ops = [o for o in operations if o['target_path'] == path and
                                   o['approved_payload_identity'] == identity(payload)]
                    check(len(matches_ops) == 1, batch + ' shared fragment associated with one exact canonical author operation',
                          {'path': path, 'fragment_index': findex, 'matches': len(matches_ops)})
                    fragment_checks.append({'manifest': {'commit': candidate, 'path': manifest_path,
                                                         'pointer': '/fragments/' + str(findex), 'record_sha256': canonical_sha(fragment)},
                                            'target_path': path, 'payload_file': {'commit': candidate, 'path': payload_path, **identity(raw)},
                                            'payload_identity': identity(payload), 'operation_ids': [o['operation_id'] for o in matches_ops],
                                            'result': 'PASS' if len(matches_ops) == 1 else 'FAIL'})
            if 'revision' not in stage:
                permissions = contracts[batch]['per_finding_formal_permissions']
                for op in operations:
                    source = op['source']
                    check(source['commit'] == candidate, batch + ' operation bound to exact approved candidate')
                    check(source['path'].startswith(ROOT + '/candidates/' + batch + '/author/'),
                          batch + ' operation source belongs to sole semantic author')
                    path = op['target_path']
                    check(batch in frozen_by_path[path]['contributing_batches'], batch + ' approved contributor for target')
                    source_record = ref_record(source) if 'pointer' in source and '/direct-mirror/' not in op['operation_id'] else None
                    if source_record is not None:
                        for fid in source_record.get('finding_ids', []):
                            check(fid in permissions and path in permissions[fid],
                                  batch + ' source finding/target within frozen permission', {'finding_id': fid, 'path': path})
            map_paths = {f.get('path', f.get('target_path')) for f in mapping.get('files', [])}
            if 'revision' in stage:
                map_paths = {mapping['changed_formal_file']['path']}
            check(set(touched) == map_paths, stage + ' only mapped formal paths changed', {'touched': touched, 'mapped': sorted(map_paths)})
            check(set(touched) <= set(frozen_by_path), stage + ' no normative path outside frozen85 modified')
            derived_patch = git.cmd('diff', previous, actual, '--', FORMAL)
            if batch == 'R5-U01':
                patch, patch_source = derived_patch, {'kind': 'independently regenerated Git incremental document diff'}
            else:
                patch_path = ROOT + '/integration/' + batch + '/' + round_id + '/current-to-actual.patch'
                patch = git.get(actual, patch_path, 'fixed unified-diff byte identity plus independent private application')
                patch_source = {'commit': actual, 'path': patch_path}
            matches(patch, declared_stage['patch_identity'], stage + ' fixed incremental patch bytes/SHA/blob')
            patch_check = subprocess.run(['git', 'apply', '--check', '-'], input=patch, cwd=patch_root,
                                         stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            check(patch_check.returncode == 0, stage + ' private patch apply check', patch_check.stderr.decode())
            patch_apply = subprocess.run(['git', 'apply', '-'], input=patch, cwd=patch_root,
                                         stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            check(patch_apply.returncode == 0, stage + ' private patch apply', patch_apply.stderr.decode())
            check({str(p.relative_to(patch_root)) for p in patch_root.rglob('*') if p.is_file()} == set(paths),
                  stage + ' private replay creates no extra files')
            file_results = []
            for p in paths:
                actual_bytes = git.get(actual, p, 'full formal131 byte identity at each independent replay step')
                patch_bytes = (patch_root / p).read_bytes()
                ok = check(state[p] == actual_bytes == patch_bytes, stage + ' source/patch/actual bytes exact', {'path': p})
                check(identity(actual_bytes)['git_blob'] == actual_file_index[p]['git_blob'], stage + ' actual blob tree alignment', {'path': p})
                file_results.append({'path': p, 'bytes_sha_blob': identity(actual_bytes),
                                     'independently_rebuilt_identity': identity(state[p]),
                                     'private_patch_replay_identity': identity(patch_bytes),
                                     'source_replay_bytes_equal': state[p] == actual_bytes,
                                     'patch_replay_bytes_equal': patch_bytes == actual_bytes,
                                     'changed_in_stage': p in touched, 'result': 'PASS' if ok else 'FAIL'})
            for f in mapping.get('files', []):
                path = f.get('path', f.get('target_path'))
                if path not in shared:
                    source = f.get('approved_mirror', f.get('candidate_source', f.get('source')))
                    if source is None:
                        source = {'commit': candidate, 'path': ROOT + '/candidates/' + batch + '/author/formal/' + path}
                    mirror = git.get(source['commit'], source['path'], 'approved nonshared mirror identity comparison')
                    ok = check(mirror == state[path], batch + ' nonshared actual equals approved author mirror', {'path': path})
                    mirror_checks.append({'path': path, 'source': source, **identity(mirror), 'actual_byte_equal': ok})
                contributions[path].append({'batch': batch, 'actual_commit': actual,
                                            'receipt': receipt_refs[batch], 'independent_actual_review': review_bindings[batch],
                                            'operation_ids': [o['operation_id'] for o in operations if o['target_path'] == path],
                                            'scope': 'exact incoming owner fragment only' if path in shared else 'exact approved nonshared mirror'})
            if 'revision' not in stage:
                check(receipts[batch]['actual']['commit'] == (actual if batch != 'R5-U03' else STAGES[3][1]),
                      batch + ' unique accepted actual binding (U03 uses corrected actual02)')
            all_operations.extend(operations)
            stages.append({'stage': stage, 'actual_commit': actual, 'actual_tree': declared_stage['actual_tree'],
                           'formal_tree': git.tree(actual), 'previous_document_subject': previous,
                           'mapping': {'commit': actual, 'path': mapping_path, **identity(mapping_raw)},
                           'fixed_incremental_patch_source': patch_source,
                           'fixed_incremental_patch_identity': identity(patch),
                           'independently_regenerated_git_diff_identity': identity(derived_patch),
                           'patch_serializations_need_not_match': True, 'changed_paths': touched,
                           'source_operation_results': operations, 'nonshared_mirror_results': mirror_checks,
                           'shared_fragment_author_identity_results': fragment_checks,
                           'formal131_results': file_results, 'formal_files_checked': len(file_results)})
            previous = actual

        final_results = []
        desc_by_path = {x['path']: x for x in subject_desc['files']}
        for p in paths:
            data = git.get(SUBJECT, p, 'current accepted formal131 exact final subject')
            matches(data, desc_by_path[p], 'current131 descriptor bytes/SHA/blob')
            matches(b5_state[p], desc_by_path[p]['B5_identity'], 'current131 independently read B5 identity')
            check(state[p] == data, 'final8 source replay equals current formal subject', {'path': p})
            changed = data != b5_state[p]
            check(changed == desc_by_path[p]['changed_from_B5'], 'current131 B5 delta classification', {'path': p})
            final_results.append({'path': p, 'B5_identity': identity(b5_state[p]), 'current_identity': identity(data),
                                  'changed_from_B5': changed, 'final_source_replay_byte_equal': state[p] == data,
                                  'descriptor_bytes_sha_blob_equal': True})
        changed79 = {x['path'] for x in final_results if x['changed_from_B5']}
        check(len(changed79) == 79, 'current formal accepted79 changed')
        check(git.tree(SUBJECT) == '145e0f253be5233a114966bda684ac2a07b35d4e', 'current final formal tree pinned')
        candidate_root = temp / 'candidate-only-projection'
        candidate_root.mkdir()
        mirrors = locator['six_proposed_admin_mirrors']
        mirror_manifest_ref = locator['author_manifest']
        mirror_manifest_raw = git.get(mirror_manifest_ref['commit'], mirror_manifest_ref['path'],
                                      'six proposed mirror manifest exact pinned identity')
        matches(mirror_manifest_raw, mirror_manifest_ref, 'six mirror manifest bytes/SHA/blob')
        mirror_manifest = json.loads(mirror_manifest_raw)
        manifest_by_target = {x['target_path']: x for x in mirror_manifest['files']}
        check(len(manifest_by_target) == len(mirror_manifest['files']) == 6, 'six mirror manifest unique targets')
        check(set(manifest_by_target) == {x['target_path'] for x in mirrors}, 'six manifest matches locator target set')
        candidate_results = []
        for row in mirrors:
            path = row['target_path']
            source = row['source']
            old = git.get(SUBJECT, path, 'six candidate live old bytes; projection only')
            new = git.get(source['commit'], source['path'], 'six candidate proposed mirror full byte identity')
            matches(old, row['base'], 'six candidate base bytes/SHA/blob')
            matches(new, source, 'six candidate source bytes/SHA/blob')
            manifest_row = manifest_by_target[path]
            check(manifest_row['candidate_path'] == source['path'], 'six mirror manifest exact source coordinate')
            matches(old, manifest_row['base'], 'six mirror manifest base bytes/SHA/blob')
            matches(new, manifest_row['candidate_identity'], 'six mirror manifest candidate bytes/SHA/blob')
            appendix = new[manifest_row['appendix_utf8_byte_offset']:]
            matches(appendix, manifest_row['appendix_identity'], 'six mirror appended scope bytes/SHA/blob')
            regenerated = ''.join(difflib.unified_diff(old.decode().splitlines(keepends=True),
                                                       new.decode().splitlines(keepends=True),
                                                       fromfile='a/' + path, tofile='b/' + path)).encode()
            matches(regenerated, manifest_row['diff_identity'], 'six independently regenerated unified diff identity')
            check(new.startswith(old), 'six candidate exact old prefix retained', {'path': path})
            check(git.get(CORE, path) == old and git.get(LOCATOR, path) == old, 'six candidate live targets untouched at core and locator', {'path': path})
            target = candidate_root / path
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(old)
            candidate_results.append({'path': path, 'source': source, 'base_identity': identity(old),
                                      'candidate_identity': identity(new), 'old_prefix_exact': new.startswith(old),
                                      'appendix_identity': identity(appendix),
                                      'independently_regenerated_diff_identity': identity(regenerated),
                                      'appended_bytes': len(new) - len(old), 'live_target_unchanged': True,
                                      'projection_only': True, 'result': 'PASS'})
        candidate_patch_path = ROOT + '/candidates/R5-U08/author/navigation-support.patch'
        candidate_patch = git.get(CORE, candidate_patch_path, 'six-candidate private projection patch')
        matches(candidate_patch, locator['candidate_patch'], 'six candidate fixed patch bytes/SHA/blob')
        r = subprocess.run(['git', 'apply', '--check', '-'], input=candidate_patch, cwd=candidate_root,
                           stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        check(r.returncode == 0, 'six-candidate private patch check', r.stderr.decode())
        r = subprocess.run(['git', 'apply', '-'], input=candidate_patch, cwd=candidate_root,
                           stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        check(r.returncode == 0, 'six-candidate private patch application', r.stderr.decode())
        check({str(p.relative_to(candidate_root)) for p in candidate_root.rglob('*') if p.is_file()} ==
              {row['target_path'] for row in mirrors}, 'six private projection has only expected target paths')
        for row, result in zip(mirrors, candidate_results):
            projected = (candidate_root / row['target_path']).read_bytes()
            check(projected == git.get(row['source']['commit'], row['source']['path']), 'six private projected mirrors exact')
            result['private_patch_projection_identity'] = identity(projected)
        check(set(m['target_path'] for m in mirrors) == set(frozen_by_path) - changed79,
              '79 accepted plus6 candidate is exact frozen85')

    # Verify the accepted operation bindings without treating them as new semantic signatures.
    accepted_binding_results = []
    spans_keys = {'R5-U01': 'accepted_operations_scope', 'R5-U02': 'accepted_operation_spans',
                  'R5-U03': 'accepted_actual_operation_spans', 'R5-U04': 'accepted_actual_operation_byte_bindings'}
    operation_by_id = {x['operation_id']: x for x in all_operations if x.get('canonical_contribution')}
    for batch, receipt in receipts.items():
        actual = receipt['actual']['commit']
        results = []
        if batch in spans_keys:
            for row in receipt[spans_keys[batch]]:
                oid = row['operation_id']
                source_op = operation_by_id[oid]
                p = row.get('target_path', row.get('target', row.get('path')))
                offset = row.get('actual_payload_offset', row.get('utf8_byte_offset', row.get('actual_payload_utf8_byte_offset')))
                declared = row.get('span_identity', row.get('identity', row.get('actual_payload_identity')))
                if declared is None:
                    declared = {'bytes': row['actual_payload_bytes'], 'sha256': row['payload_sha256']}
                data = git.get(actual, p)
                span = data[offset:offset + declared['bytes']]
                matches(span, declared, batch + ' accepted receipt exact span identity')
                if batch == 'R5-U03' and oid == 'R5-U03/operation/49':
                    ref = row['source_candidate']
                    auth = ref_record(ref)
                    check(canonical_sha(auth) == ref['record_sha256'], 'U03 accepted revised op49 source identity')
                elif 'source_candidate_record_sha256' in row:
                    check(source_op['source_record_sha256'] == row['source_candidate_record_sha256'], batch + ' accepted operation frozen record association')
                results.append({'operation_id': oid, 'path': p, 'utf8_byte_offset': offset,
                                'accepted_span_identity': identity(span), 'result': 'PASS'})
        elif batch == 'R5-U05':
            for row in receipt['accepted_authored_transfer_operations']:
                data = git.get(row['approved_mirror']['commit'], row['approved_mirror']['path'])
                check(data == git.get(actual, row['target_path']), 'U05 receipt exact approved mirror transfer')
                results.append({'operation_id': row['transfer_id'], 'path': row['target_path'],
                                'accepted_mirror_identity': identity(data), 'result': 'PASS'})
        elif batch == 'R5-U06':
            for row in receipt['accepted_source_operation_associations']:
                op = operation_by_id[row['edit_id']]
                check(row['source_record_sha256'] == op['source_record_sha256'], 'U06 accepted source record identity')
                check(row['approved_after_identity'] == op['approved_payload_identity'], 'U06 accepted source payload identity')
                results.append({'operation_id': row['edit_id'], 'path': row['target'],
                                'accepted_payload_identity': row['approved_after_identity'], 'result': 'PASS'})
        else:
            ref = receipt['approved_operation_mapping']
            matches(git.get(ref['commit'], ref['path']), ref, 'U07 receipt exact14-operation mapping identity')
            results = [{'operation_id': o['operation_id'], 'path': o['target_path'],
                        'accepted_payload_identity': o['approved_payload_identity'], 'result': 'PASS'}
                       for o in stages[-1]['source_operation_results']]
        accepted_binding_results.append({'batch': batch, 'actual_commit': actual, 'receipt': receipt_refs[batch],
                                         'prior_actual_review': review_bindings[batch], 'operation_binding_results': results,
                                         'count': len(results), 'semantic_signatures_transferred': False})
    check(sum(x['count'] for x in accepted_binding_results) == 262, 'accepted262 exact operation associations')
    canonical_ops = [x for x in all_operations if x.get('canonical_contribution')]
    check(len(canonical_ops) == 262, 'independently reconstructed262 canonical contributions')
    check(len({x['operation_id'] for x in canonical_ops}) == 262, '262 unique canonical operation identities')
    direct = [x for x in canonical_ops if '/direct-mirror/' in x['operation_id']]
    check(len(direct) == 3, 'three authored direct mirror transfers')
    check(len(canonical_ops) - len(direct) == 259, '259 explicit frozen author edits')
    shared_fragment_count = sum(len(s['shared_fragment_author_identity_results']) for s in stages)
    check(shared_fragment_count == 103, 'all103 approved shared fragment payload associations')
    all_changed = git.cmd('diff', '--name-only', B5, SUBJECT).decode().splitlines()
    nonadmin = [p for p in all_changed if not p.startswith(ROOT + '/')]
    check(set(nonadmin) == changed79, 'all nonadministrative changes exact accepted79')
    protected = [p for p in all_changed if not p.startswith(ROOT + '/') and p not in frozen_by_path]
    check(not protected, 'no package-external normative/reference/source/history path changes', protected)
    for p in SUPPORT:
        check(git.get(B5, p) == git.get(SUBJECT, p), 'support live untouched B5 to subject', {'path': p})
    check(not git.cmd('diff', '--name-only', SUBJECT, CORE, '--', FORMAL, *SUPPORT), 'core live formal/support unchanged')
    check(not git.cmd('diff', '--name-only', CORE, LOCATOR, '--', FORMAL, *SUPPORT), 'locator live formal/support unchanged')
    sole_results = []
    for p in sorted(frozen_by_path):
        frozen, candidate = frozen_by_path[p], owners_by_path[p]
        expected_writer = frozen['writer']
        checks = []
        checks.append(check(candidate['sole_actual_writer'] == expected_writer, 'sole writer matches frozen owner', {'path': p}))
        checks.append(check(candidate['contributing_batches'] == frozen['contributing_batches'], 'sole contributor batches exact', {'path': p}))
        checks.append(check(candidate['finding_ids'] == frozen['findings'], 'sole owner findings exact', {'path': p}))
        checks.append(check(frozen['historical_files_writable'] is False and candidate['historical_files_writable'] is False,
                            'sole-writer historical documents remain readonly', {'path': p}))
        checks.append(check(candidate['current_whole_file_signature'] == 'WAIT_U08_INDEPENDENT',
                            'sole-writer input has no premature whole-file signature', {'path': p}))
        actual_batches = sorted({x['batch'] for x in contributions[p]})
        if p in changed79:
            checks.append(check(actual_batches == sorted(frozen['contributing_batches']), 'all and only required batch contributions accepted', {'path': p, 'actual_batches': actual_batches}))
            current = git.get(SUBJECT, p)
            checks.append(matches(current, candidate['current_identity'], 'sole-writer current formal identity'))
            phase = 'ACCEPTED_FORMAL_OWNER_CONTRIBUTIONS'
        else:
            checks.append(check(frozen['contributing_batches'] == ['R5-U08'] and expected_writer == 'R5-U08', 'six candidate U08 sole owner', {'path': p}))
            current = git.get(SUBJECT, p)
            checks.append(matches(current, candidate['current_identity'], 'candidate-only owner table live base identity'))
            checks.append(check(not actual_batches, 'six candidate have no actual accepted contributions', {'path': p}))
            phase = 'CANDIDATE_ONLY_NOT_ACTUAL_NOT_ACCEPTED'
        if expected_writer != 'R5-I':
            checks.append(check(len(frozen['contributing_batches']) == 1 and frozen['contributing_batches'][0] == expected_writer,
                                'nonshared sole semantic owner', {'path': p}))
        sole_results.append({'path': p, 'result': 'PASS' if all(checks) else 'FAIL',
                             'frozen_owner_writer': expected_writer, 'shared': p in shared,
                             'semantic_owner_batches': frozen['contributing_batches'], 'finding_ids': frozen['findings'],
                             'current_live_identity': identity(current), 'phase': phase,
                             'accepted_contribution_bindings': contributions[p],
                             'mechanical_integrator_authors_new_semantics': False,
                             'qualification': 'Shared R5-I writes only exact approved owner payloads; nonshared owner retains sole semantic authorship while R5-I may mechanically transport approved mirror bytes.'})
    notes.append('U05/U07 transport maps call R5-I actual_writer for nonshared mechanical mirror reception. Frozen sole-writer table retains R5-U05/R5-U07 as sole semantic owners; contract author-entry explicitly authorizes R5-I exact-byte transport. This is a label distinction, not evidence of another semantic author.')
    notes.append('The six U08 table rows have empty finding_ids; all_required_owner_contributions_accepted=true is vacuous for that empty required-finding set. It does not constitute actual integration, a mirror acceptance receipt, or CLOSED.')
    verdict = 'PASS_DOCUMENT_MECHANICAL_REPLAY' if not failures else 'FAIL_DOCUMENT_MECHANICAL_REPLAY'
    common = {'reviewer_task_path': '/root/replay', 'opaque_platform_task_id': 'UNVERIFIED',
              'requested_parameters': {'model': 'gpt-6.1-sol', 'reasoning_effort': 'ultra', 'service_tier': 'default', 'Fast': False},
              'actual_parameter_echo': {'model': 'UNVERIFIED', 'reasoning_effort': 'UNVERIFIED', 'service_tier': 'UNVERIFIED'},
              'subject': {'locator_commit': LOCATOR, 'candidate_core_commit': CORE, 'current_formal_commit': SUBJECT,
                          'B5_commit': B5, 'freeze_commit': FREEZE},
              'evidence_level': 'INDEPENDENT_DOCUMENT_BYTES_AND_RECORD_IDENTITY_ONLY',
              'reference_behavior_execution': 0, 'behavior_model_execution': 0, 'host_engine_execution': 0,
              'new_semantic_signature': False, 'actual_U08_integration': False,
              'formal_U08_acceptance': False, 'CLOSED': 0}
    replay = {'schema': 'r5.u08.independent.replay-results.v1', **common, 'verdict': verdict,
              'method': 'Pinned Git blobs, frozen-author operations, a separate private git-apply projection, and every131 actual file at each8 step. Author all131 status booleans are never used as decision inputs.',
              'counts': {'stages': 8, 'formal_files_per_stage': 131, 'stage_file_comparisons': 1048,
                         'canonical_contributions': len(canonical_ops), 'explicit_author_edits': len(canonical_ops) - len(direct),
                         'direct_mirror_transfers': len(direct), 'U03_in_place_revision_events': 1,
                         'shared_fragment_source_associations': shared_fragment_count,
                         'final_formal_files': 131, 'accepted_changed_formal_paths': len(changed79),
                         'unchanged_formal_paths': len(paths) - len(changed79), 'candidate_private_mirrors': len(mirrors)},
              'stages': stages, 'current_formal131_results': final_results,
              'accepted_operation_identity_results': accepted_binding_results,
              'U03_original_author_operation49_revision': op49_revision,
              'six_private_candidate_projection_results': candidate_results,
              'protected_paths': {'outside_frozen85_normative_changes': protected,
                                  'administrative_changed_paths_count': len(all_changed) - len(nonadmin),
                                  'all_nonadministrative_changed_paths': nonadmin}, 'failures': failures, 'notes': notes}
    sole = {'schema': 'r5.u08.independent.sole-writer-results.v1', **common,
            'verdict': 'PASS_DOCUMENT_OWNER_AND_WRITER_BINDINGS' if not failures else 'FAIL_DOCUMENT_OWNER_AND_WRITER_BINDINGS',
            'frozen_owner_table_identity': {'commit': FREEZE, 'path': ROOT + '/frozen-input/shared-file-owners.json',
                                          **identity(git.get(FREEZE, ROOT + '/frozen-input/shared-file-owners.json'))},
            'counts': {'paths': len(sole_results), 'shared_R5_I': len(shared), 'nonshared_sole_semantic_owner': len(sole_results) - len(shared),
                       'accepted_formal': len(changed79), 'U08_candidate_only': len(mirrors)},
            'results': sole_results, 'U03_operation49_qualification': op49_revision,
            'outside_package_normative_changes': protected, 'notes': notes, 'failures': failures}
    reading_rows = []
    for key in sorted(git.reads):
        entry = git.reads[key].copy()
        entry['purposes'] = sorted(entry['purposes'])
        entry['semantic_source_behavior_review_claimed'] = False
        reading_rows.append(entry)
    reading = {'schema': 'r5.u08.independent.replay-reading-log.v1', **common,
               'meaning': 'Full document blobs read for byte replay and identity inspection; not source behavior execution and not a claim to semantic rereview of all document prose.',
               'unique_commit_path_reads': len(reading_rows), 'entries': reading_rows}
    out.mkdir(parents=True, exist_ok=True)
    for name, value in [('replay-results.json', replay), ('sole-writer-results.json', sole), ('replay-reading-log.json', reading)]:
        (out / name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')
    report = [f'# R5-U08 独立文档重放与 sole-writer 复核\n\n裁决：`{verdict}`。',
              f'固定当前正式主体 `{SUBJECT}` / formal tree `145e0f253be5233a114966bda684ac2a07b35d4e`；候选 core `{CORE}`，定位 `{LOCATOR}`。',
              f'独立读取 B5 和冻结作者操作，逐八步重建，同时在 `/tmp` 对另一路副本执行增量文档 patch 重放。每步131文件均核原始 bytes、SHA-256 和 Git blob，共1048次逐文件对齐。当前131最终映射也逐份复核，79变化、52未变。',
              '独立追溯262规范贡献＝259显式作者编辑＋3直接镜像转移；七份唯一接受回执与其原 actual 独审报告/检查文件精确身份已核。回执及作者结果不转为本次语义签名。',
              'U03 旧 actual01 FAIL 保留。原作者新固定候选仅操作索引49的 new_text、向量索引45的 input 变化；只替换一个消费前提行，52规范操作不增项，另计1限修事件。其它mirror/fragment文档未改，31片段记录精确未变，59原限定static记录hash独立核对。限修 candidate/actual/唯一接受准确绑定；不扩大为整旧ID签名。',
              '85路径与冻结集合逐项相等；21共享唯R5-I按已审原owner载荷接入，64非共享唯语义owner。79正式已接＋6 U08候选。非共享的机械镜像运输由R5-I执行仍不产生另一语义owner；U05/U07 actual_writer 字段使用的是运输执行者名称。',
              '导航3/support3只在 `/tmp` 独立投影：六原文精确前缀、源身份与 patch 结果吻合，core/定位的live目标仍旧字节。当前B5→正式差异无85集合外规范、source、reference、历史路径变化；222项行政差异限于本轮prepare目录。',
              '本结果只裁决文档重放、身份及写者资格。新reference/model/host行为执行均0；U08 actual/正式接受/CLOSED均未发生。真实任务路径 `/root/replay`；模型、effort、tier与opaque UUID回显缺失均记UNVERIFIED。',
              f'失败项数：{len(failures)}。可重跑：`python {out / "verify-replay.py"} --repo {repo}`。']
    if failures:
        report.append('失败详见 replay-results.json 的 failures；本报告不授权修正式字节或接受/关闭。')
    (out / 'replay-review.md').write_text('\n\n'.join(report) + '\n')
    print(json.dumps({'verdict': verdict, 'failure_count': len(failures), 'counts': replay['counts'],
                      'read_count': len(reading_rows), 'output_directory': str(out)}, ensure_ascii=False))
    if failures:
        print(json.dumps(failures[:10], ensure_ascii=False, indent=2))
    git.proc.stdin.close()
    git.proc.wait()
    return int(bool(failures))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo', type=pathlib.Path, default=pathlib.Path('/workspace/r5-u08-independent'))
    args = parser.parse_args()
    destination = pathlib.Path(__file__).resolve().parent
    raise SystemExit(run(args.repo.resolve(), destination))
