#!/usr/bin/env python3
"""Check every heading of the exact current source independently of old coverage."""
from pathlib import Path
import argparse
import copy
import importlib.util
import json
import sys
import functools

import jsonschema

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
INVENTORY = HERE.parents[2]
spec = importlib.util.spec_from_file_location('routing_current_coverage', INVENTORY / 'routing.py')
r = importlib.util.module_from_spec(spec)
spec.loader.exec_module(r)

GOVERNANCE_AUTHORITY = 'a32873d2860b15d9f5e27727db8f131f4ec433b6'
GOVERNANCE_PATHS = {r.FORMAL + name for name in [
    'README.md', 'scope-statement.md', 'test-catalog/README.md']}
GOVERNANCE_FIELDS = ['document_id', 'path', 'level', 'title', 'anchor', 'heading_sha256']


@functools.lru_cache(maxsize=1)
def governance_headings():
    """Fixed reviewed headings, never an exemption learned from editable input."""
    relative = str((INVENTORY / 'section-coverage.json').relative_to(r.ROOT))
    fixed = json.loads(r.blob(GOVERNANCE_AUTHORITY, relative))
    return {tuple(s[k] for k in GOVERNANCE_FIELDS) for s in fixed['sections']
            if s['path'] in GOVERNANCE_PATHS and s.get('coverage_scope') == 'ALL_FORMAL_FEATURES'}


def allowed_governance(section, snapshot_commit):
    if tuple(section[k] for k in GOVERNANCE_FIELDS) not in governance_headings():
        return False
    source = r.identity(r.B8, section['path'])
    current = r.identity(snapshot_commit, section['path'])
    return all(current[k] == source[k] for k in ['git_blob', 'sha256', 'bytes'])


def check(data, manifest, schema):
    errors = ['schema: ' + error.message for error in jsonschema.Draft202012Validator(schema).iter_errors(data)]
    if errors:
        return errors
    if data['snapshot'] != manifest['current_snapshot'] or data['source_baseline_commit'] != r.B8:
        errors.append('current coverage snapshot mismatch')
    expected = []
    docs = {d['document_id']: d for d in manifest['documents']}
    for d in manifest['documents']:
        hs, _ = r.headings(r.blob(data['snapshot']['commit'], d['source']['path']))
        for h in hs:
            expected.append({'document_id': d['document_id'], 'path': d['source']['path'],
                             **{k: h[k] for k in ['level', 'title', 'anchor', 'line_start', 'line_end', 'heading_sha256']}})
    fields = ['document_id', 'path', 'level', 'title', 'anchor', 'line_start', 'line_end', 'heading_sha256']
    actual = [{k: s[k] for k in fields} for s in data['sections']]
    if actual != expected:
        errors.append('complete current heading identity/order coverage mismatch')
    active = {f['feature_id'] for f in manifest['features']}
    metadata = {m['metadata_id'] for m in manifest['metadata_records']}
    historical = r.read_json(INVENTORY / 'section-coverage.json')
    old_keys = {(s['path'], s['anchor']) for s in historical['sections']}
    for section in data['sections']:
        label = section['path'] + '#' + section['anchor']
        if set(section['feature_refs']) - active or set(section['metadata_refs']) - metadata:
            errors.append(label + ': unresolved current consumer')
        global_scope = section['coverage_scope'] == 'ALL_FORMAL_FEATURES'
        exempt = global_scope and allowed_governance(section, data['snapshot']['commit'])
        if global_scope and not exempt:
            errors.append(label + ': ALL_FORMAL_FEATURES requires fixed governance heading and source identity')
        if not section['feature_refs'] and not section['metadata_refs'] and not exempt:
            errors.append(label + ': unmapped current heading')
        if section['accepted_events'] != docs[section['document_id']]['upstream']['accepted_events']:
            errors.append(label + ': current acceptance navigation mismatch')
        if (section['path'], section['anchor']) not in old_keys and section['mapping_basis'] != 'AUTHOR_EXPLICIT_NEW_HEADING_MAPPING; independent review pending':
            errors.append(label + ': new heading needs explicit author consumer mapping')
    return errors


def view(data, historical):
    old_counts = {}
    counts = {}
    for s in historical['sections']:
        old_counts[s['document_id']] = old_counts.get(s['document_id'], 0) + 1
    for s in data['sections']:
        counts.setdefault(s['document_id'], {'path': s['path'], 'headings': 0, 'events': s['accepted_events']})['headings'] += 1
    text = ['# 当前源章节覆盖', '',
            '此表由 current-section-coverage.json 生成；历史源定位完整保留在 section-coverage.json。章节导航与源规格接受不证明未来去向兼容、阶段批准或实现验收。', '',
            f"当前固定快照：`{data['snapshot']['commit']}`；当前标题 {len(data['sections'])}；历史标题 {len(historical['sections'])}。", '',
            '| 文档 | 历史标题 | 当前标题 | 新增标题 | 源接受事件 |', '| --- | --- | --- | --- | --- |']
    for did, row in counts.items():
        text.append('| ' + ' | '.join([row['path'], str(old_counts[did]), str(row['headings']),
                                      str(row['headings'] - old_counts[did]), ', '.join(row['events']) or '源字节未变；无新增接受事件']) + ' |')
    return '\n'.join(text) + '\n'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--render', action='store_true')
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    data = r.read_json(INVENTORY / 'current-section-coverage.json')
    manifest = r.read_json(INVENTORY / 'routing-manifest.json')
    schema = r.read_json(INVENTORY / 'current-section-coverage.schema.json')
    historical = r.read_json(INVENTORY / 'section-coverage.json')
    errors = check(data, manifest, schema)
    expected_view = view(data, historical)
    view_path = INVENTORY / 'current-coverage.md'
    if args.render and not errors:
        view_path.write_text(expected_view)
    if not view_path.exists() or view_path.read_text() != expected_view:
        errors.append('current coverage readable view stale')
    cases = []
    behavior_index = next(i for i, s in enumerate(data['sections'])
                          if s['path'] == r.FORMAL + 'combat-requirements/wp39-battle-context-and-participants.md'
                          and s['anchor'] == '4-战斗初始化与布局')
    for name, mutate, token in [
        ('drop current heading', lambda d: d['sections'].pop(), 'current heading identity'),
        ('alter current heading end', lambda d: d['sections'][0].update(line_end=999999), 'current heading identity'),
        ('erase current consumer mapping', lambda d: d['sections'][1].update(feature_refs=[], metadata_refs=[], coverage_scope='UNRESOLVED'), 'unmapped current heading'),
        ('ordinary behavior cannot claim global governance', lambda d: d['sections'][behavior_index].update(feature_refs=[], metadata_refs=[], coverage_scope='ALL_FORMAL_FEATURES'), 'requires fixed governance'),
    ]:
        mutated = copy.deepcopy(data)
        mutate(mutated)
        found = check(mutated, manifest, schema)
        cases.append({'case': name, 'rejected': any(token in e for e in found), 'errors': found})
    old_keys = {(s['path'], s['anchor']) for s in historical['sections']}
    result = {'schema_version': 'routing-current-heading-check.v1',
              'scope': 'AUTHOR_STATIC_CURRENT_SOURCE_COVERAGE_ONLY; no semantic, compatibility or whole-round approval',
              'snapshot': data['snapshot'], 'documents': len(manifest['documents']),
              'historical_headings': len(historical['sections']), 'current_headings': len(data['sections']),
              'new_current_headings': sum((s['path'], s['anchor']) not in old_keys for s in data['sections']),
              'coverage_sha256': r.digest((INVENTORY / 'current-section-coverage.json').read_bytes()),
              'errors': errors, 'negative_cases': cases, 'all_negative_cases_rejected': all(c['rejected'] for c in cases),
              'current_readable_view_fresh': view_path.exists() and view_path.read_text() == expected_view}
    result['result'] = 'PASS_CURRENT_HEADING_COVERAGE' if not errors and result['all_negative_cases_rejected'] else 'FAIL'
    r.save_json(args.output, result)
    summary = {k: v for k, v in result.items() if k not in ['errors', 'negative_cases']}
    summary['error_count'] = len(errors)
    summary['errors_sample'] = errors[:8]
    summary['negative_cases'] = [{k: v for k, v in case.items() if k != 'errors'} | {'error_count': len(case['errors'])}
                                 for case in cases]
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return int(result['result'] == 'FAIL')


if __name__ == '__main__':
    sys.exit(main())
