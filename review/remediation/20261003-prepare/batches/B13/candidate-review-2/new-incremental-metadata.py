"""New R-B13 incremental Git/JSON/hash/text checks; executes no repository code."""
import difflib
import hashlib
import json
import re
import subprocess
from pathlib import Path

BASE = '8e67f780c204d593d89f364f585d2c6c2fe74631'
OLD = '5845e8084ced280e51c51a4081ec8583a9c2ca39'
NEW = 'db9e6ed1997efe5bf94dac952aad44fd3b9ebd21'
PUB = 'dbabf68ec00e7e368d594dfb49497ba5a9cbf578'
SCOPE = '231c9f25df4dd64961fb9290ff52302782a9fdb8'
PRIOR = 'e03b7c2824105c5925cb9d64079bf653b03a41f4'
PREFIX = 'review/remediation/20261003-prepare/batches/B13/'
A = PREFIX + 'author-draft-1/'
CURRENT = A + 'two-findings-scope-applied-1/'
REPAIR = A + 'two-findings-repair-1/'
OUT = Path(PREFIX + 'candidate-review-2')
OUT.mkdir(parents=True, exist_ok=True)

def git(*args):
    return subprocess.check_output(['git', *args])

def content(ref, path):
    return git('show', ref + ':' + path)

def obj(ref, path):
    return json.loads(content(ref, path))

def identity(ref, path):
    b = content(ref, path)
    return {'commit': ref, 'path': path,
            'git_blob': git('rev-parse', ref + ':' + path).decode().strip(),
            'sha256': hashlib.sha256(b).hexdigest(), 'bytes': len(b)}

def binding(r):
    got = identity(r['commit'], r['path'])
    return {'binding': r, 'actual': got,
            'matched': all(got[k] == r[k] for k in ['git_blob', 'sha256', 'bytes'])}

def tree(ref):
    result = {}
    for item in git('ls-tree', '-rz', '--full-tree', ref).split(b'\0'):
        if item:
            meta, p = item.split(b'\t', 1)
            result[p.decode()] = meta.decode()
    return result

old_tree, new_tree, base_tree = tree(OLD), tree(NEW), tree(BASE)
changed = sorted(p for p in old_tree.keys() | new_tree.keys() if old_tree.get(p) != new_tree.get(p))
full = git('diff', '--binary', '--no-ext-diff', '--no-textconv', OLD, NEW)
(OUT / 'OLD-to-NEW.full.patch').write_bytes(full)
aggregate = git('diff', '--binary', '--no-ext-diff', '--no-textconv', BASE, NEW)
(OUT / 'FIX_BASE-to-NEW.full.patch').write_bytes(aggregate)
full_diff = {'argv': ['git', 'diff', '--binary', '--no-ext-diff', '--no-textconv', OLD, NEW],
             'bytes': len(full), 'sha256': hashlib.sha256(full).hexdigest(),
             'author_publication_full_patch_equal': full == content(PUB, PREFIX + 'candidate-1/two-findings-scope-applied-1/OLD-to-NEW.full.patch'),
             'unfiltered': True, 'changed_path_count': len(changed)}
inventory = obj(NEW, CURRENT + 'all-11-formal-output-identities.json')
formal_paths = [r['path'] for r in inventory['outputs']]
formal_changed = [p for p in changed if p in formal_paths]
unexpected = [p for p in changed if p not in formal_paths and not p.startswith(REPAIR)
              and not p.startswith(CURRENT) and not p.startswith(PREFIX + 'candidate-1/')]
formal = []
for r in inventory['outputs']:
    ident = identity(NEW, r['path'])
    formal.append({'path': r['path'], 'FIX_BASE': identity(BASE, r['path']),
                   'OLD': identity(OLD, r['path']), 'NEW': ident,
                   'unchanged_since_OLD': old_tree[r['path']] == new_tree[r['path']],
                   'author_output_matched': all(ident[k] == r['output'][k] for k in ['git_blob', 'sha256', 'bytes']),
                   'publication_same_bytes': content(PUB, r['path']) == content(NEW, r['path'])})
protected = [p for p in old_tree if p not in formal_changed]
protected_changed = [p for p in protected if old_tree[p] != new_tree.get(p)]
previous_metadata = obj(PRIOR, PREFIX + 'candidate-review-1/independent-metadata.json')
previous_coverage = obj(PRIOR, PREFIX + 'candidate-review-1/control-coverage.json')
old_dispositions = obj(OLD, A + 'scope-applied-1/finding-dispositions-successor.json')
new_dispositions = obj(NEW, CURRENT + 'finding-dispositions-successor.json')
controls = obj(NEW, A + 'original-and-acceptance-controls.json')
control_reuse = []
required = ['whole_control', 'original_required_fields', 'current_required_fields',
            'whole_extensions_and_root_adjudications', 'approved_acceptance_gate']
for i, c in enumerate(controls['controls']):
    a, b = old_dispositions['controls'][i], new_dispositions['controls'][i]
    control_reuse.append({'id': c['id'], 'primary': c['primary'],
                         'accepted_contributors': c['accepted_contributors'],
                         'exact_complete_control_file_unchanged': content(OLD, A + 'original-and-acceptance-controls.json') == content(NEW, A + 'original-and-acceptance-controls.json'),
                         'required_control_fields_equal': {k: a[k] == b[k] for k in required},
                         'prior_whole_object_and_binding_checks': previous_metadata['control_bindings'][i],
                         'prior_semantic_review_identity': identity(PRIOR, PREFIX + 'candidate-review-1/control-coverage.json'),
                         'prior_semantic_review_pointer': '/records/' + str(i),
                         'prior_semantic_review_ID_matched': previous_coverage['records'][i]['id'] == c['id'],
                         'current_disposition': b['local_disposition']})
planned = obj(NEW, A + 'planned-inputs-52.json')
planned_checks = [binding(r['input']) for r in planned['records']]
peer = obj(NEW, REPAIR + 'review-input-bindings.json')
peer_checks = []
for r in peer['inputs']:
    check = binding(r)
    check['frozen_copy_equal'] = content(NEW, r['copy']) == content(r['commit'], r['path'])
    peer_checks.append(check)
index_checks = [binding(r) for r in obj(NEW, CURRENT + 'current-evidence-index.json')['references']]
scope = obj(SCOPE, PREFIX + 'scope-amendment-2/scope-amendment.json')
scope_record = scope['records'][0]
scope_inputs = []
for r in obj(NEW, CURRENT + 'scope-application-receipt.json')['scope_inputs']:
    check = binding(r)
    check['copy_equal'] = content(NEW, r['frozen_read_only_copy']) == content(r['commit'], r['path'])
    scope_inputs.append(check)
original = scope_record['path']
before = content(OLD, original).decode()
after = content(NEW, original).decode()
patch = ''.join(difflib.unified_diff(before.splitlines(True), after.splitlines(True),
                                  fromfile='a/' + original, tofile='b/' + original)).encode()
def outside_section(text):
    a = text.index('### 5.2 ')
    z = text.index('### 5.3 ', a)
    return text[:a], text[z:]
scope_check = {'scope_commit': SCOPE, 'scope_inputs': scope_inputs,
               'before_matches_bound_whole_file': content(OLD, original) == content(scope_record['before']['commit'], scope_record['before']['path']),
               'after_matches_bound_whole_file': content(NEW, original) == content(scope_record['after_to_apply']['commit'], scope_record['after_to_apply']['path']),
               'whole_patch_identity': binding(scope['source_whole_patch']),
               'independent_whole_patch_sha256': hashlib.sha256(patch).hexdigest(),
               'independent_whole_patch_bytes': len(patch),
               'exact_whole_patch_equal': patch == content(scope['source_whole_patch']['commit'], scope['source_whole_patch']['path']),
               'outside_5_2_byte_equal': outside_section(before) == outside_section(after),
               'quality_not_inferred_from_scope': True}
def rows(text):
    group = ''
    result = []
    for line in text.splitlines():
        match = re.match(r'^##\s+([A-Z]+)', line)
        if match:
            group = match.group(1)
        match = re.match(r'^\|\s*((?:Q|W|P)\d{2}[a-z]?|(?:EG|EN|FC|MG|TT)-\d+)\s*\|', line)
        if match:
            result.append({'group': group, 'id': match.group(1), 'row': line})
    return result
catalogs = []
for path in formal_paths:
    if '/test-catalog/' not in path:
        continue
    a, b = rows(content(OLD, path).decode()), rows(content(NEW, path).decode())
    key = lambda r: (r['group'], r['id'])
    amap, bmap = {key(r): r for r in a}, {key(r): r for r in b}
    catalogs.append({'path': path, 'OLD_count': len(a), 'NEW_count': len(b),
                     'old_order_and_multiplicity_preserved': [key(r) for r in a] == [key(r) for r in b if key(r) in amap],
                     'missing_old': [k for k in amap if k not in bmap],
                     'changed_old_rows': [{'group': r['group'], 'id': r['id'], 'before': r['row'], 'after': bmap[key(r)]['row']} for r in a if r['row'] != bmap[key(r)]['row']],
                     'added_rows': [r for r in b if key(r) not in amap],
                     'counts': {g: sum(r['group'] == g for r in b) for g in dict.fromkeys(r['group'] for r in b)},
                     'STATIC_UNEXECUTED': True})
interfaces = []
for r in obj(NEW, CURRENT + 'affected-interface-navigation-successor.json')['current_read_only_interfaces']:
    got = identity(NEW, r['path'])
    interfaces.append({'path': r['path'], 'NEW': got,
                       'binding_matched': all(got[k] == r['identity'][k] for k in ['git_blob', 'sha256', 'bytes']),
                       'OLD_NEW_byte_equal': content(OLD, r['path']) == content(NEW, r['path']),
                       'BASE_NEW_byte_equal': content(BASE, r['path']) == content(NEW, r['path'])})
new_json = []
for path in changed:
    if path.endswith('.json'):
        obj(NEW, path)
        new_json.append(identity(NEW, path))
evidence = {'kind': 'NEW_INCREMENTAL_GIT_JSON_HASH_TEXT_METADATA_ONLY',
            'reviewed_OLD': OLD, 'reviewed_NEW': NEW,
            'reviewed_NEW_tree': git('rev-parse', NEW + '^{tree}').decode().strip(),
            'formal_FIX_BASE': BASE, 'publication_navigation_only': PUB,
            'complete_unfiltered_OLD_NEW': full_diff,
            'complete_unfiltered_FIX_BASE_NEW': {'bytes': len(aggregate), 'sha256': hashlib.sha256(aggregate).hexdigest(), 'unfiltered': True},
            'all_changed_paths': changed, 'formal_changed_paths': formal_changed, 'unexpected_changed_paths': unexpected,
            'all_11_outputs': formal, 'complete8_5_controls_reuse': control_reuse,
            'all_52_input_bindings': planned_checks, 'prior_peer_inputs_immutable': peer_checks,
            'current_evidence_index_bindings': index_checks, 'scope2': scope_check,
            'all_OLD_existing_paths_except_3_formal_unchanged': {'checked': len(protected), 'changed': protected_changed},
            'previous_BASE_to_OLD_reviewed_protection_reused': previous_metadata['whole_preexisting_path_protection'],
            'catalogs': catalogs, 'current_read_only_interfaces': interfaces,
            'added_JSON_parsed_and_hashed': new_json,
            'publication_delta': git('diff', '--name-status', NEW, PUB).decode().splitlines(),
            'reference_Ruby_game_vectors_historical_programs_executed': 0,
            'metadata_success_not_quality_verdict': True}
(OUT / 'independent-metadata.json').write_text(json.dumps(evidence, ensure_ascii=False, indent=2) + '\n')
assert not unexpected and not protected_changed
assert len(formal) == 11 and len(formal_changed) == 3
assert sum(c['primary'] for c in control_reuse) == 5 and len(control_reuse) == 8
assert all(c['exact_complete_control_file_unchanged'] and all(c['required_control_fields_equal'].values()) for c in control_reuse)
assert all(r['matched'] for r in planned_checks + index_checks)
assert all(r['matched'] and r['frozen_copy_equal'] for r in peer_checks)
assert all(r['author_output_matched'] and r['publication_same_bytes'] for r in formal)
assert scope_check['exact_whole_patch_equal'] and scope_check['outside_5_2_byte_equal']
assert scope_check['before_matches_bound_whole_file'] and scope_check['after_matches_bound_whole_file']
assert all(r['matched'] and r['copy_equal'] for r in scope_inputs)
assert full_diff['author_publication_full_patch_equal']
assert all(r['old_order_and_multiplicity_preserved'] and not r['missing_old'] for r in catalogs)
assert all(r['binding_matched'] and r['OLD_NEW_byte_equal'] and r['BASE_NEW_byte_equal'] for r in interfaces)
print(json.dumps({'complete_diff': full_diff, 'formal_changed': formal_changed,
                  'protected_existing_paths': len(protected), 'controls8_5_exact_reused': True,
                  'all11_52_peer_index_bindings_match': True, 'scope2_exact_patch': scope_check['exact_whole_patch_equal'],
                  'catalogs': [{'OLD': r['OLD_count'], 'NEW': r['NEW_count'], 'changed_old': [(x['group'], x['id']) for x in r['changed_old_rows']], 'added': [(x['group'], x['id']) for x in r['added_rows']]} for r in catalogs]}, ensure_ascii=False))
