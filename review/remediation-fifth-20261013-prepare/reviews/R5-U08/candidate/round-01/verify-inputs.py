#!/usr/bin/env python3
"""Independent fixed-object checks. Document/tool validation only."""
import collections
import hashlib
import json
import pathlib
import posixpath
import re
import subprocess

ROOT = pathlib.Path(__file__).resolve().parents[6]
PREP = 'review/remediation-fifth-20261013-prepare'
INPUT = PREP + '/integration/R5-U08/candidate-01'
OUTPUT = PREP + '/reviews/R5-U08/candidate/round-01'
CANDIDATE = 'f623c2ecdd1c6a52d44145fdc7599624a8c64f7b'
LOCATOR = '9f19756ab9eb73d94ceb2707ea97bfe0986d43dd'
SUBJECT = 'e4ea8d03b0e2c7c20fc41fce92f0b2b7b7f02514'
FROZEN = '22fba7786b0090a1955ce6211315b0036cddfbcd'
READS = {}


def git(*args):
    return subprocess.check_output(['git', '-C', str(ROOT), *args])


def read(commit, path):
    data = git('show', commit + ':' + path)
    key = (commit, path)
    READS[key] = {'commit': commit, 'path': path, 'bytes': len(data),
                  'sha256': hashlib.sha256(data).hexdigest(),
                  'git_blob': hashlib.sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest(),
                  'read_kind': 'complete_byte_validation'}
    return data


def load(commit, path):
    return json.loads(read(commit, path))


def verify(identity):
    data = read(identity['commit'], identity['path'])
    result = READS[(identity['commit'], identity['path'])].copy()
    result['expected'] = {k: identity[k] for k in ('bytes', 'sha256', 'git_blob') if k in identity}
    result['result'] = 'PASS' if all(result[k] == v for k, v in result['expected'].items()) else 'FAIL'
    return result


def save(name, obj):
    path = ROOT / OUTPUT / name
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2) + '\n')


def main():
    locator = load(LOCATOR, INPUT + '/candidate-review-input.json')
    identities = []
    payloads = locator['full_core_inputs'] + [x['source'] for x in locator['six_proposed_admin_mirrors']]
    payloads += [locator[k] for k in ('author_manifest', 'candidate_patch', 'current_candidate_ledger')]
    publication = load(LOCATOR, INPUT + '/candidate-publication-readback.json')
    seen = {(x['commit'], x['path']) for x in payloads}
    payloads += [x for x in publication['rows'] if (x['commit'], x['path']) not in seen]
    identities.extend(verify(x) for x in payloads)
    identities.extend(verify(x) for x in (locator['U07_unique_acceptance'],))
    identities.extend(verify(x['base']) for x in locator['six_proposed_admin_mirrors'])
    frozen_paths = git('ls-tree', '-r', '--name-only', FROZEN, PREP + '/contracts').decode().splitlines()
    frozen_paths += [PREP + '/registration/initial-ledger.json']
    frozen_unchanged = []
    for path in frozen_paths:
        frozen_unchanged.append({'path': path, 'result': 'PASS' if read(FROZEN, path) == read(CANDIDATE, path) else 'FAIL'})
    matrix = load(CANDIDATE, INPUT + '/mandatory92-review-matrix.json')['findings']
    trace = load(CANDIDATE, INPUT + '/bidirectional-traceability.json')
    source_set = set()
    formal_set = set()
    for row in matrix:
        for anchor in row['source_anchors']:
            digest = hashlib.sha256(json.dumps(anchor, ensure_ascii=False, sort_keys=True, separators=(',', ':')).encode()).hexdigest()
            source_set.add((anchor['path'], row['id'], row['batch'], digest))
        for target in row['required_sync_targets']:
            formal_set.add((target['path'], row['id']))
            identities.append(verify({'commit': SUBJECT, 'path': target['path'], **target['current_identity']}))
    actual_source = {(row['path'], x['finding_id'], x['batch'], x['source_anchor_record_sha256'])
                     for row in trace['source_to_findings'] for x in row['uses']}
    actual_formal = {(row['path'], fid) for row in trace['formal_to_findings'] for fid in row['finding_ids']}
    save('traceability-results.json', {'schema': 'independent.r5.u08.traceability.v1', 'subject': SUBJECT,
         'result': 'PASS' if source_set == actual_source and formal_set == actual_formal else 'FAIL',
         'source_paths': len({x[0] for x in source_set}), 'formal_paths': len({x[0] for x in formal_set}),
         'source_relations': len(source_set), 'formal_relations': len(formal_set),
         'source_missing': sorted(source_set - actual_source), 'source_extra': sorted(actual_source - source_set),
         'formal_missing': sorted(formal_set - actual_formal), 'formal_extra': sorted(actual_formal - formal_set),
         'scope': 'Exact inverse of fixed required finding sources and mandatory sync targets; 568 qualifications remain separately in criterion-results.json.'})
    mirrors = []
    for item in locator['six_proposed_admin_mirrors']:
        old = read(SUBJECT, item['target_path'])
        new = read(CANDIDATE, item['source']['path'])
        added = new[len(old):].decode()
        links = []
        for destination in re.findall(r'\[[^\]]+\]\(([^)]+)\)', added):
            path = posixpath.normpath(posixpath.join(posixpath.dirname(item['target_path']), destination.split('#')[0]))
            exists = bool(git('ls-tree', '-r', '--name-only', CANDIDATE, '--', path).strip())
            links.append({'link': destination, 'resolved_at_target': path, 'result': 'PASS' if exists else 'FAIL'})
        table = re.findall(r'^\| (GR5-[^ |]+) \| (R5-U\d+) \| (\d+) \| 精确owner静态已接受 \| OPEN_REQUIRED \|$', added, re.M)
        expected = {(x['id'], x['batch'], str(len(x['static_criteria']))) for x in matrix}
        table_ok = not table or (len(table) == 92 and set(table) == expected)
        mirrors.append({'target_path': item['target_path'], 'candidate_identity': item['source'],
                        'result': 'PASS' if new.startswith(old) and table_ok and all(x['result'] == 'PASS' for x in links) else 'FAIL',
                        'old_prefix_exact': new.startswith(old), 'added_bytes': len(new)-len(old),
                        'links': links, 'finding_table_rows': len(table), 'table_92_exact': table_ok,
                        'semantic_judgment': 'Addition identifies current successor and historical timestamps; separates owner acceptance92, aggregate candidate/actual/formal/closure, static410/schema568, SC correction, finite historical qualified scopes and execution phases. Existing behavior stays exact prefix; only target-coordinate navigation is proposed.',
                        'actual_applied': False})
    save('mirror-results.json', {'schema': 'independent.r5.u08.mirrors.v1', 'candidate': CANDIDATE,
                               'result': 'PASS' if all(x['result']=='PASS' for x in mirrors) else 'FAIL', 'files': mirrors,
                               'count': 6, 'new_links': sum(len(x['links']) for x in mirrors), 'actual_integration': 'WAIT'})
    save('identity-results.json', {'schema': 'independent.r5.u08.identity.v1', 'candidate': CANDIDATE,
          'candidate_tree': git('rev-parse', CANDIDATE + '^{tree}').decode().strip(),
          'locator': LOCATOR, 'locator_tree': git('rev-parse', LOCATOR + '^{tree}').decode().strip(),
          'formal_subject': SUBJECT, 'formal_bytes_same_as_candidate': not bool(git('diff', '--name-only', SUBJECT, CANDIDATE, '--', 'deliverables/final-specification-set', 'planning', 'audit')),
          'frozen_inputs_unchanged': frozen_unchanged, 'new_candidate_payloads': len(payloads),
          'new_candidate_payload_bytes': sum(x['bytes'] for x in payloads),
          'checks': identities, 'identity_mismatches': [x for x in identities if x['result'] != 'PASS'],
          'execution_level': 'TOOL_VALIDATION_ONLY'})
    save('root-reading-log.json', {'schema': 'independent.r5.u08.root-byte-reading.v1', 'files': list(READS.values()),
                                 'scope': 'Complete byte comparisons. Semantic/full-text reading is separately recorded in supporting review logs.'})
    print(json.dumps({'payloads': len(payloads), 'payload_bytes': sum(x['bytes'] for x in payloads),
                      'identity_mismatches': sum(x['result']!='PASS' for x in identities),
                      'frozen_changes': sum(x['result']!='PASS' for x in frozen_unchanged),
                      'trace_exact': source_set == actual_source and formal_set == actual_formal,
                      'mirror_results': [x['result'] for x in mirrors]}, ensure_ascii=False))


if __name__ == '__main__':
    main()
