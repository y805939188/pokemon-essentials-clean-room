#!/usr/bin/env python3
"""Apply the bounded R3 narrative repair to the exact c0f62d9 candidate."""
import argparse
import ast
import copy
import datetime
import hashlib
import json
from pathlib import Path
import subprocess
import sys

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
INV = HERE.parents[1]
ROOT = INV.parents[2]
BASE = 'c0f62d973180679134f2eb1a488c1dc359c8658f'
REVIEW = '34202eb7accfee48bb8761db88b340bd77f54a42'
SOURCE = '5f87743293290de2e219ecdd6c19e88280f60c9a'
REVIEW_DIR = 'review/r8-disposition-r3-independent-c0f62d9-20261017/'
R3 = INV / 'revisions/r3'
FACTS = {
    'FR-000029': '普通非Shadow成长按WP19的正常模板HP255/攻击255（总量510）对照，在HP单项余量252−255=−3的首项反向区间失败，尚未到总量夹限及本接收者EV/经验写入或后续刷新；此前受领者与回调前缀不保证回滚，默认非内部设施仍在更早成长门返回。',
    'FR-000032': '正常核心返回并完成外层善后及结束通知后，复位玩家行走动画状态与转向预锁记录；此处不写面向方向。',
    'FR-000173': '记录战斗的收服存储为空操作；回放另按WP58 §6.2–6.4的副本、实时依赖及正常结束/中止分层合同，不能由记录战斗存储空操作推定回放隔离。',
    'FR-000204': '普通非Shadow战斗成长消费正常设施模板HP255/攻击255（总量510）时，先在HP单项余量252−255=−3的夹限失败，尚未到总量夹限和本接收者EV/经验写入或后续重算；先前前缀与默认非内部设施的更早成长门分别保留。',
    'FR-000227': '接受的负步骤概率前缀沿同一算法处理，累加器及整数商可为负；累加器除以200的整数商向下取整，不钳零。',
    'FR-000456': '正常设施模板HP/攻击各255、其余0，总量510符合总量上限而超过单项252；属性重算保留存储值，普通非Shadow成长先在HP单项负余量夹限失败，未到总量夹限及本接收者写入。',
    'FR-000596': 'Repel遭遇允许门默认比较首个非蛋成员（含濒死），替代配置才取首位可战成员；野生等级低于所选成员等级时拒绝并清累积，计步与遭遇判定仍分别归现有消费者。',
}
FILE_FACTS = {
    'wp42-growth-end-of-round-and-battle-outcomes.md': FACTS['FR-000029'] + FACTS['FR-000032'],
    'wp26-acquisition-gifts-and-script-trade.md': FACTS['FR-000173'],
    'wp30-growth-learning-and-friendship.md': FACTS['FR-000204'],
    'wp36-wild-encounters-and-modifiers.md': FACTS['FR-000227'],
    'wp19-attributes-ability-and-stats.md': FACTS['FR-000456'],
    'wp61-field-passive-effects-and-blackout.md': FACTS['FR-000596'],
}
BOUNDARIES = {
    'wp42-growth-end-of-round-and-battle-outcomes.md': '成长持久写入与战斗调用继续为协作候选；单项余量与总量余量按先后门分别验证，外层行走动画/转向预锁复位归世界交接，异常前缀和表现尾仍待验证。',
    'wp26-acquisition-gifts-and-script-trade.md': '既有获得/存储与记录/回放交界分责保持；目标须分别验证记录战斗存储空操作、回放副本和实时依赖以及正常终局/中止，不把记录存储合同扩成回放整体隔离。',
    'wp30-growth-learning-and-friendship.md': '成长协作候选保持；分别验证单项/总量夹限的实际首失败位置、本接收者未写状态、此前受领者前缀及非内部设施早退，不扩张到Shadow/道具。',
    'wp36-wild-encounters-and-modifiers.md': '既有框架遭遇触发候选保持；验证接受负概率、负累加器的向下取整及不钳零，不改变原有Repel比较成员规则。',
    'wp19-attributes-ability-and-stats.md': '属性领域与战斗成长交接类别保持；区分总量510但单项255越252的模板、重算不归一化、单项/总量实际失败顺序及设施internalBattle更早门。',
    'wp61-field-passive-effects-and-blackout.md': '既有框架野外被动/计步和遭遇消费者分责保持；验证Repel默认首非蛋（含濒死）与替代首可战的配置差别，不以概率取整替代成员选择合同。',
}


def git(*args):
    return subprocess.check_output(['git', *args], cwd=ROOT)


def sha(data):
    return hashlib.sha256(data).hexdigest()


def load(path):
    return json.loads(path.read_bytes())


def save(path, value):
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--apply', action='store_true')
    args = p.parse_args()
    assert args.apply, 'Explicit --apply required; this writer is for the exact fixed candidate only.'
    assert git('rev-parse', 'HEAD').decode().strip() == BASE
    path = INV / 'routing-manifest.json'
    before_bytes = path.read_bytes()
    assert sha(before_bytes) == 'ee46bb7278bb21311115a62e93bd93770a205dc691a01a48f45c22b6c09b4f71'
    manifest = json.loads(before_bytes)
    old = copy.deepcopy(manifest)
    findings = json.loads(git('show', REVIEW + ':' + REVIEW_DIR + 'findings.json'))
    cases = {c['feature_id']: (f['id'], c) for f in findings['findings'] for c in f['cases']}
    assert set(cases) == set(FACTS)
    records = []
    fs = {f['feature_id']: f for f in manifest['features']}
    for fid, fact in FACTS.items():
        issue, case = cases[fid]
        row = fs[fid]
        assert row['differences'][1] == case['candidate_claim']
        row['differences'][1] = fact + ' 目标去向、时序与失败前缀仍待验证。 R3逐行证据：revisions/r3/feature-source-deltas.json#' + fid + '（final5f与不可变B8来源分别登记）。'
        records.append({'feature_id': fid, 'finding_id': issue, 'pointer': case['candidate_pointer'],
                        'before': case['candidate_claim'], 'after': row['differences'][1],
                        'fixed_source': {'commit': SOURCE, 'document': case['current_source_document'],
                                         **case['source_identity']},
                        'author_status': 'CORRECTED_AWAITING_INDEPENDENT_REVIEW',
                        'preserved_facets': case['preserved_facets']})
    expected = copy.deepcopy(old)
    for row in expected['features']:
        if row['feature_id'] in FACTS:
            row['differences'][1] = fs[row['feature_id']]['differences'][1]
    assert expected == manifest
    save(path, manifest)
    delta_path = R3 / 'feature-source-deltas.json'
    delta = load(delta_path)
    for row in delta['records']:
        if row['feature_id'] in FACTS:
            row['source_fact_delta'] = FACTS[row['feature_id']]
            row['future_boundary_reassessment'] = BOUNDARIES[Path(row['current_source']['document']).name]
    save(delta_path, delta)
    file_path = R3 / 'source-file-reassessment.json'
    files = load(file_path)
    for row in files['records']:
        name = Path(row['document']).name
        if name in FILE_FACTS:
            row['source_fact_reassessment'] = FILE_FACTS[name]
            row['future_plan_reassessment'] = BOUNDARIES[name]
    save(file_path, files)
    patch_path = R3 / 'source-refinement-patch.json'
    patch = load(patch_path)
    for row in patch['records']:
        if row['feature_id'] in FACTS:
            change = next(c for c in row['field_changes'] if c['pointer'] == '/differences')
            assert change['after'][1] == cases[row['feature_id']][1]['candidate_claim']
            change['after'] = copy.deepcopy(fs[row['feature_id']]['differences'])
    save(patch_path, patch)
    # Synchronize reusable source strings without changing the historical writer guard.
    generator = R3 / 'build-author-evidence.py'
    text = generator.read_text()
    tree = ast.parse(text)
    assignment = next(n for n in tree.body if isinstance(n, ast.Assign)
                      and any(isinstance(t, ast.Name) and t.id == 'manual' for t in n.targets))
    manual = ast.literal_eval(assignment.value)
    for name in FILE_FACTS:
        a, b = manual[name]
        literal = repr(name) + ':(' + repr(a) + ',' + repr(b) + ')'
        assert text.count(literal) == 1
        text = text.replace(literal, repr(name) + ':(' + repr(FILE_FACTS[name]) + ',' + repr(BOUNDARIES[name]) + ')')
    text = text.replace("fr=[]\n", "fr=[]\nunit_narratives=" + repr({k: FACTS[k] for k in ['FR-000029', 'FR-000032']}) + '\n')
    text = text.replace("'source_fact_delta':d['source_fact_reassessment']", "'source_fact_delta':unit_narratives.get(i,d['source_fact_reassessment'])")
    assert 'unit_narratives=' in text and 'Historical R3 author step refuses changed/final manifest' in text
    ast.parse(text)
    generator.write_text(text)
    receipt = {'schema_version': 'routing-r3-seven-narrative-repair.v1',
               'role': 'AUTHOR_REPAIR_ONLY_NOT_INDEPENDENT_ACCEPTANCE',
               'utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
               'fixed_candidate': BASE, 'fixed_review': REVIEW, 'current_source': SOURCE,
               'manifest_before_sha256': sha(before_bytes), 'manifest_after_sha256': sha(path.read_bytes()),
               'updated_consolidated_patch_sha256': sha(patch_path.read_bytes()),
               'roots': sorted({x['finding_id'] for x in records}), 'records': records,
               'only_manifest_changes': 'Exactly the seven listed /features/N/differences/1 strings; all other JSON values equal c0f62d9.',
               'historical_application_receipts_preserved': ['revisions/r3/author-refinement-application.json', 'revisions/r3/source-narrative-correction.json'],
               'archive_preserved': 'revisions/r3/tools/post-source-pre-semantic-35175c7094b0.json.gz',
               'runtime_configuration': {'requested': 'gpt-6.1-sol / xhigh / default', 'actual_model': 'UNVERIFIED', 'actual_effort': 'UNVERIFIED', 'actual_tier': 'UNVERIFIED'},
               'business_or_prototype_execution': False}
    save(HERE / 'correction-record.json', receipt)
    for name, key in [('facet-inheritance.json', 'records'), ('feature-resolution.json', 'active_feature_results')]:
        target = R3 / name
        value = load(target)
        for row in value[key]:
            if row['feature_id'] in FACTS:
                row['current_calibration_repair'] = {
                    'fixed_review': REVIEW, 'received_facet_verdict': 'FAIL',
                    'received_other_four_facets': 'PASS',
                    'finding_id': cases[row['feature_id']][0],
                    'author_status': 'CORRECTED_AWAITING_INDEPENDENT_REVIEW',
                    'evidence': '../r3-calibration-repair/correction-record.json#' + row['feature_id']}
        save(target, value)
    print(json.dumps({'corrected_features': list(FACTS), 'manifest_sha256': receipt['manifest_after_sha256'],
                      'patch_sha256': receipt['updated_consolidated_patch_sha256']}, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
