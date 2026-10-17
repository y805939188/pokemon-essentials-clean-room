#!/usr/bin/env python3
"""Describe explicit R2 author changes and preserve prior review verdict identities."""
import copy
import hashlib
import json
import subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
REPO = ROOT.parents[2]
BASE = '5666b7b912e2fb79b5119283ee6a37401a7071db'
REVIEW = '8c8b46e919e0a15aaaf204f16df5b4ad3c9888b8'
SOURCE = 'fd1df570cad987dc3852a3b958f03916e317f7fe'
INPUT = Path('/tmp/r8-disposition-r1-review-8c8b46e')
PREFIX = str(ROOT.relative_to(REPO))


def read(path):
    return json.loads(path.read_text())


def write(name, value):
    if (HERE / 'pre-calibration-binding.json').exists():
        value['author_semantic_snapshot_binding'] = read(HERE / 'pre-calibration-binding.json')
    if name == 'finding-resolution.json' and (HERE / name).exists():
        prior = json.loads((HERE / name).read_text())
        if 'final_author_tool_evidence' in prior:
            value['final_author_tool_evidence'] = prior['final_author_tool_evidence']
    (HERE / name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')


def fixed(name):
    return json.loads(subprocess.check_output(['git', 'show', f'{BASE}:{PREFIX}/{name}'], cwd=REPO))


assert hashlib.sha256((ROOT / 'routing-manifest.json').read_bytes()).hexdigest() == 'f7e6ee69c5f58c3f5dab89d39a0df7e4c5f1041ba4998dabe9a19879cdd428fc', 'R2 semantic snapshot changed (including accepted backfill); refuse historical evidence regeneration'
manifest = read(ROOT / 'routing-manifest.json')
before = fixed('routing-manifest.json')
f = {x['feature_id']: x for x in manifest['features']}
r = {x['feature_id']: x for x in manifest['retired_features']}
oldf = {x['feature_id']: x for x in before['features']}
oldr = {x['feature_id']: x for x in before['retired_features']}
m = {x['metadata_id']: x for x in manifest['metadata_records']}
oldm = {x['metadata_id']: x for x in before['metadata_records']}
decisions = read(HERE / 'explicit-decisions.json')['items']
consumer_rows = read(HERE / 'consumer-mappings.json')['relationships']
results = read(INPUT / 'feature-results.json')
reviews = read(INPUT / 'findings.json')['findings']


def root_ids(ref):
    return [d['finding_id'] for d in decisions if ref in d['affected_refs']]


def details(ref):
    if ref in f:
        now = f[ref]
        return {'current_disposition': 'ACTIVE', 'current_source': now['source'],
                'current_scope': now['functional_scope'], 'responsibilities': now['future_plan']['responsibilities'],
                'direct_refs': now['dependencies']['direct_refs'], 'feature_refs': now['dependencies']['feature_refs'],
                'specific_repair': [d['description'] for d in decisions if ref in d['affected_refs']]}
    old = r[ref]
    meta = m[old['retirement']['metadata_record_id']]
    return {'current_disposition': 'RETIRED_METADATA', 'metadata_id': meta['metadata_id'],
            'current_consumer_refs': meta['feature_refs'], 'retirement': old['retirement'],
            'specific_consumer_groups': [x for x in consumer_rows if x['metadata_id'] == meta['metadata_id']],
            'historical_body_preservation': 'EXACT_D62_ORIGINAL_EXCEPT_RETIREMENT'}


old_rows = []
for x in results['old_feature_results']:
    ref = x['feature_id']
    old = oldf.get(ref, oldr.get(ref))
    now = f.get(ref, r.get(ref))
    row = {'feature_id': ref, 'fixed_review_verdict': x['verdict'], 'fixed_review_reason': x['reason'],
           'fixed_review_commit': REVIEW, 'review_finding_refs': x.get('finding_refs', []),
           'source_identity_unchanged': old['source'] == now['source']}
    if x['verdict'] == 'PASS':
        row.update({'author_disposition': 'PRIOR_PASS_PRESERVED',
                    'entire_record_equal_to_r1': now == old,
                    'same_root_check': '本行具体责任/分类与不可变来源保留；本次共享状态六行、元数据十组和目录同号引用的完整显式修正另列，不将旧PASS自动授给新769。'})
    else:
        row.update({'author_disposition': 'AUTHOR_REVISED_AWAITING_INDEPENDENT_REVIEW', **details(ref)})
    old_rows.append(row)
assert len(old_rows) == 721
assert sum(x['fixed_review_verdict'] == 'FAIL' for x in old_rows) == 28
assert all(x['source_identity_unchanged'] for x in old_rows)
assert all(x['entire_record_equal_to_r1'] for x in old_rows if x['fixed_review_verdict'] == 'PASS')
active_fails = [{'feature_id': x['feature_id'], 'review_reason': x['reason'], 'review_finding_refs': x.get('finding_refs', []),
                 'author_disposition': 'AUTHOR_REVISED_AWAITING_INDEPENDENT_REVIEW', **details(x['feature_id'])}
                for x in results['active_feature_results'] if x['verdict'] == 'FAIL']
meta_fails = [{'metadata_id': x['metadata_id'], 'review_reason': x['reason'], 'review_finding_refs': x.get('finding_refs', []),
               'source_identity_unchanged': m[x['metadata_id']]['source'] == oldm[x['metadata_id']]['source'],
               'current_consumer_refs': m[x['metadata_id']]['feature_refs'],
               'specific_source_groups': [z for z in consumer_rows if z['metadata_id'] == x['metadata_id']],
               'author_disposition': 'AUTHOR_REVISED_AWAITING_INDEPENDENT_REVIEW'}
              for x in results['retired_metadata_results'] if x['verdict'] == 'FAIL']
write('feature-resolution.json', {'schema_version': 'routing-r2-feature-resolution.v1', 'previous_candidate': BASE,
      'fixed_review_commit': REVIEW, 'status': 'AUTHOR_REPAIRS_NOT_INDEPENDENT_VERDICTS',
      'old_rows': old_rows, 'active_fail_rows': active_fails, 'metadata_fail_rows': meta_fails,
      'coverage': {'old_rows': 721, 'old_fail_specific_dispositions': len([x for x in old_rows if x['fixed_review_verdict'] == 'FAIL']),
                   'old_pass_preserved': len([x for x in old_rows if x['fixed_review_verdict'] == 'PASS']),
                   'active_fail_specific_dispositions': len(active_fails), 'metadata_fail_specific_dispositions': len(meta_fails),
                   'unhandled': 0}})

finding_rows = []
for x in reviews:
    key = x['id']
    if key == 'ROOT-R1-VIEW-01':
        finding_rows.append({'finding_id': key, 'review_severity': x['severity'], 'author_disposition': 'AUTHOR_TOOL_REVISED_AWAITING_INDEPENDENT_REVIEW',
                             'specific_action': '父任务修复父行显式excluded_child_refs子ID导航及被引用子行锚点；重生全部视图并检查实际全部拆分。',
                             'evidence': 'tools/root-tool-resolution.json', 'execution': 'tools/actual-command-io.json'})
    else:
        d = next(d for d in decisions if d['finding_id'] == key)
        finding_rows.append({'finding_id': key, 'review_severity': x['severity'], **d,
                             'data_diff': 'data-diff.json', 'semantic_basis': 'source-reading-scope.json',
                             'consumer_mapping': 'consumer-mappings.json' if key in ['DS-R1-001', 'R1-KF-001', 'R1-CATALOG-WP-COLLISION'] else None})
assert len(finding_rows) == 12
write('finding-resolution.json', {'schema_version': 'routing-r2-finding-resolution.v1', 'previous_candidate': BASE, 'fixed_review_commit': REVIEW,
      'status': 'R2_AUTHOR_REVISED_AWAITING_PARENT_ULTRA_DEFAULT_REVIEW',
      'review_inputs': 'tools/review-input-ledger.json', 'findings': finding_rows,
      'counts': {'findings': 12, 'P2': 2, 'P3': 10, 'semantic_data_repairs': 11, 'tool_repairs': 1, 'unhandled': 0}})

groups = read(INPUT / 'finding-results.json')['finding_results']
group_rows = []
for g in groups:
    cases = g.get('original_cases', g.get('all_original_cases', g.get('case_results', [])))
    cases = cases if isinstance(cases, list) else []
    propagation = g.get('propagation_cases', [])
    propagation = propagation if isinstance(propagation, list) else []
    fail_cases = [x for x in cases + propagation if isinstance(x, dict) and x.get('verdict') == 'FAIL']
    feature_refs = sorted({x.get('feature_id', x.get('old_feature_id')) for x in fail_cases if x.get('feature_id', x.get('old_feature_id'))})
    related = set()
    for x in results['old_feature_results']:
        if x['feature_id'] in feature_refs:
            related.update(x.get('finding_refs', []))
    group_rows.append({'original_finding_id': g['finding_id'], 'r1_verdict': g['verdict'],
                       'action': 'PRESERVE_PRIOR_PASS_NO_RECLASSIFICATION' if g['verdict'] == 'PASS' else 'PRECISE_R2_REPAIR_AWAITING_REVIEW',
                       'r1_failed_cases': fail_cases, 'r2_finding_refs': sorted(related),
                       'specific_case_dispositions': [{'feature_id': ref, 'resolution': f'feature-resolution.json#old_rows/{next(i for i,x in enumerate(old_rows) if x["feature_id"] == ref)}'} for ref in feature_refs if any(x['feature_id'] == ref for x in old_rows)],
                       'scope': '独立R1报告的35个PASS组结论仍属于其固定5666字节；R2保留其正确内容，具体修复不升级为作者验收。'})
for row in group_rows:
    if row['original_finding_id'] == 'WORLD-CATALOG-F01':
        row['r2_finding_refs'] = ['R1-CATALOG-WP-COLLISION']
        row['specific_case_dispositions'] = [
            {'document': z['document'], 'anchor': z['anchor'], 'removed_wrong_document_feature_refs': z['removed'],
             'source_basis': '本目录L3仅对应Safari/BerryPlant/FieldPassive/Pokedex/Voltorb/Lottery六篇；按固定正文身份移除Fishing/Slot/Mining同号错误关系，保留真实共享消费者。',
             'section_diff': 'data-diff.json#coverage_changed', 'detailed_evidence': 'consumer-mappings.json#collision_removals'}
            for z in read(HERE / 'consumer-mappings.json')['collision_removals']]

write('retained-pass-propagation.json', {'previous_candidate': BASE, 'fixed_review_commit': REVIEW,
      'original_groups': group_rows, 'r1_pass_groups_preserved': sum(x['r1_verdict'] == 'PASS' for x in group_rows),
      'r1_failed_groups_targeted': sum(x['r1_verdict'] == 'FAIL' for x in group_rows),
      'old_pass_records_equal': sum(x.get('entire_record_equal_to_r1', False) for x in old_rows),
      'r1_new_47_records_exactly_equal': all(f[x['feature_id']] == x for x in before['features'] if int(x['feature_id'][3:]) > 721),
      'r1_pass_metadata_22_exactly_equal': all(m[x['metadata_id']] == oldm[x['metadata_id']] for x in results['retired_metadata_results'] if x['verdict'] == 'PASS'),
      'new_child_769_requires_independent_classification_review': True,
      'catalog_collision_propagation': '所有该16节中确属Fishing/Slot/Mining正文的错误关系均移除，包含新增728/730；同WP编号仍保留为原始导航字段，未以它证明依赖。',
      'shared_ai_propagation': '六个被裁定受影响行共同采用R2-AI-PREPARATION具体字段/异常合同；不改其它通过的评分策略分类。',
      'scope': '作者保全/传播证据，不是新独立复审。'})

# Explicit reading scope, keeping semantic reading apart from JSON/AST consumption.
docs = {Path(d['source']['path']).name: d['source']['path'] for d in manifest['documents']}
spans = {
    'wp49-ability-phase-triggers.md': [[100, 123]],
    'wp51-ai-action-selection-and-skill.md': [[132, 151]],
    'wp52-a-generic-numerical-and-status-evaluation.md': [[9, 111]],
    'wp52-a-evaluation-coverage-and-data.md': [[237, 255]],
    'wp52-b-field-damage-healing-and-target-evaluation.md': [[23, 114]],
    'wp52-c-items-calling-and-control-evaluation.md': [[106, 133]],
    'wp72-debug-contexts-and-controls.md': [[196, 217], [307, 451]],
    'wp73-a-content-editors.md': [[193, 198]],
    'wp77-demo-evidence-and-capability-coverage.md': [[49, 197]],
    'wp24-player-trainers-partners.md': [[173, 229]],
    'wp28-item-use-and-training.md': [[112, 122], [174, 226], [276, 294]],
    'wp02-rule-configuration-and-data-variants.md': [[246, 256]],
    'wp03-content-identity-and-schema.md': [[313, 359]],
    'wp04-pbs-lifecycle.md': [[286, 296]],
    'wp06-stats-directory.md': [[73, 87]],
    'wp22-mega-and-primal-reversion.md': [[37, 60]],
    'wp07-diagnostics-files-http.md': [[155, 168]],
    'wp15-resource-matching-and-audio.md': [[130, 165]],
    'wp67-a-battle-interaction-and-presentation.md': [[132, 163]],
    'wp42-growth-end-of-round-and-battle-outcomes.md': [[203, 230]],
    'demo-dx-wp72-73-74-75-76-77.md': [[285, 294], [319, 344]],
    'pokemon-rules-wp43-44-46-48-50.md': [[270, 285]],
    'pokemon-rules-wp53-60-61-62-69-70.md': [[1, 25]],
    'generic-kernel-wp02-03-04.md': [[5, 89], [90, 198], [200, 236]],
    'generic-kernel-wp05-06-07-08-09-10.md': [[265, 288]]}
reading = []
for name, ranges in spans.items():
    data = subprocess.check_output(['git', 'show', f'{SOURCE}:{docs[name]}'], cwd=REPO)
    reading.append({'commit': SOURCE, 'document': docs[name], 'file_sha256': hashlib.sha256(data).hexdigest(),
                    'semantic_scope': 'TARGETED_SOURCE_CHAPTER_OR_TABLE_EXCERPTS', 'line_ranges': ranges,
                    'does_not_claim_all_document_clauses_read': True})
write('source-reading-scope.json', {'status': 'AUTHOR_REPAIR_READING_NOT_INDEPENDENT_REVIEW', 'fixed_review_commit': REVIEW,
      'review_outputs': {'all_73_identity_loaded_and_parsed': True, 'author_consumption_evidence': 'tools/review-input-ledger.json',
                         'semantic_text': ['REPORT.md', 'REVIEW-CONTRACT.md', 'all domain reports', 'all findings', 'all 28 old FAIL / 18 active FAIL / 10 metadata FAIL reasons and consumer audits'],
                         'machine_derived_scope': 'JSON/JSONL parsed, Python AST parsed without execution; byte loading alone is not semantic full reading.'},
      'source_reading': reading, 'headings': '全集2683标题/来源身份由工具机械核对，不能替代语义阅读。',
      'qualification': '具名目录只读取相关章节/表格；碰撞目录以L3明确对应六正文的文档身份排除错误引用，不冒称全文317行逐条语义审查。部分长输出分段补读，阅读范围是定向而非全部正式全文。',
      'destination_validation': 'ALL_UNVERIFIED; NO_PROTOTYPE_EXECUTION', 'reference_or_business_execution': 0})
print(json.dumps({'old_rows': len(old_rows), 'old_fail': len([x for x in old_rows if x['fixed_review_verdict'] == 'FAIL']), 'active_fail': len(active_fails), 'metadata_fail': len(meta_fails), 'findings': len(finding_rows), 'original_groups': len(group_rows)}, ensure_ascii=False))
