#!/usr/bin/env python3
"""R2 explicit author edits to fixed R1; no classification seeding or runtime execution."""
import copy
import hashlib
import json
import subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
REPO = ROOT.parents[2]
BASE = '5666b7b912e2fb79b5119283ee6a37401a7071db'
D62 = 'd62b41f4d620e50bb04c80a7505374bd284d8210'
SOURCE = 'fd1df570cad987dc3852a3b958f03916e317f7fe'
CURRENT = '908273093e1f6b27fc58249417675dd62d146224'
REVIEW = '8c8b46e919e0a15aaaf204f16df5b4ad3c9888b8'
PREFIX = str(ROOT.relative_to(REPO))


def git_bytes(commit, path):
    return subprocess.check_output(['git', 'show', f'{commit}:{path}'], cwd=REPO)


def load_baseline(name):
    value = git_bytes(BASE, f'{PREFIX}/{name}')
    assert (ROOT / name).read_bytes() == value, f'{name} changed; refuse overwrite'
    return json.loads(value)


def save(name, value):
    (ROOT / name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')


manifest = load_baseline('routing-manifest.json')
coverage = load_baseline('section-coverage.json')
original = copy.deepcopy(manifest)
old_coverage = copy.deepcopy(coverage)
features = {f['feature_id']: f for f in manifest['features']}
metadata = {x['metadata_id']: x for x in manifest['metadata_records']}
retired = {f['feature_id']: f for f in manifest['retired_features']}
sections = coverage['sections']
docs = {Path(d['source']['path']).name: d for d in manifest['documents']}
decisions = []
consumption = []


def fid(n):
    return f'FR-{n:06d}'


def ids(numbers):
    return sorted({fid(n) for n in numbers})


def section(name, start):
    return next(s for s in sections if Path(s['path']).name == name and s['line_start'] == start)


def ref(number, reason):
    f = features[fid(number)]
    return {'document': f['source']['document'], 'anchor': f['source']['anchor'], 'reason': reason}


def setdeps(number, links, reason):
    f = features[fid(number)]
    f['dependencies']['feature_refs'] = ids(links)
    f['dependencies']['direct_refs'] = [ref(n, why) for n, why in links.items()]
    f['differences'].append(f'R2：{reason}；来源与去向验证状态不变。')


def roles(number, scopes):
    f = features[fid(number)]
    assert set(scopes) == set(f['future_plan']['partners'])
    f['future_plan']['responsibilities'] = [{'party': k, 'scope': v} for k, v in scopes.items()]


def decision(root, description, affected, evidence, operations):
    decisions.append({'finding_id': root, 'status': 'AUTHOR_REVISED_AWAITING_INDEPENDENT_REVIEW',
                      'description': description, 'affected_refs': affected,
                      'source_basis': evidence, 'operations': operations})


def meta_rows(number, rows):
    meta = metadata[f'META-{number:06d}']
    union = ids(n for line, label, ns in rows for n in ns)
    meta['feature_refs'] = union
    meta['reason'] += ' R2按下列实际源表行逐组重新核对消费者；逐行依据见revisions/r2/consumer-mappings.json。'
    for old_id in meta['retired_feature_ids']:
        retired[old_id]['retirement']['replacement_feature_refs'] = union
    for s in sections:
        if meta['metadata_id'] in s['metadata_refs']:
            s['feature_refs'] = sorted(set(s['feature_refs']) - set(metadata_before[meta['metadata_id']]['feature_refs']) | set(union))
    for line, label, ns in rows:
        consumption.append({'metadata_id': meta['metadata_id'], 'source_commit': SOURCE,
                            'document': meta['source']['document'], 'lines': line,
                            'source_group': label, 'feature_refs': ids(ns),
                            'relationship': 'SOURCE_RESPONSIBILITY_OR_EVIDENCE_CONSUMER_ONLY',
                            'basis': '按具名字段、消费者或缺证据链定位现有行为行；不是以同WP编号或邻近ID认定依赖，未授实现/运行结论。'})


metadata_before = copy.deepcopy(metadata)

# COMBAT-R1-01: one genuinely distinct asynchronous exit/owner-choice boundary.
parent = features[fid(67)]
child = copy.deepcopy(parent)
child['feature_id'] = fid(769)
child['name'] = '跨半退出能力的可逃决定、业主替补与世界结果交接'
path = parent['source']['document']
data = git_bytes(SOURCE, path)
lines = data.decode().splitlines()
h = section(Path(path).name, 102)
source = copy.deepcopy(parent['source'])
source.update({'heading': h['title'], 'anchor': h['anchor'], 'heading_level': h['level'],
               'heading_sha256': h['heading_sha256'], 'line_ranges': [[106, 106]],
               'unit_sha256': hashlib.sha256(('\n'.join(lines[105:106]) + '\n').encode()).hexdigest(),
               'fact_excerpt': lines[105]})
child['source'] = source
child['current_applicability']['locator'] = {k: copy.deepcopy(v) for k, v in source.items()
                                           if k not in ('commit', 'document', 'fact_excerpt', 'evidence_type')}
# The document classification stays identical; the distinct behavior is in scope/plan.
child['future_plan'].update({'destination': '框架与Showdown协作', 'partners': ['框架', 'Showdown', 'MZ'],
                            'rationale': 'WP49 §5.1 L106实际写决定3或等待业主替补；规则资格、交互暂停与世界结果分别需要具名责任。',
                            'prototype_refs': ['PROTO-ESCAPE'],
                            'questions': ['验证野生可逃门与决定3、训练家非回合末业主等待/负下标失败、回合末分支及重入；不由HP数值一致推出行为覆盖。']})
child['future_plan']['responsibilities'] = [
    {'party': 'Showdown', 'scope': '候选承担跨半退出能力的触发/可逃/替补资格及分支，写本战决定3或请求合法替补；保留负选择失败与回合末差异。'},
    {'party': '框架', 'scope': '协调等待与恢复；经WP42接收决定3并进行外层结果/世界善后，保持选中成员归属与一次提交，不将成功判定当世界结果已提交。'},
    {'party': 'MZ', 'scope': '呈现非回合末业主替补选择、等待和返回；沿WP41取消/摘要合同交回选择，不替引擎决定可逃。'}]
child['dependencies']['feature_refs'] = ids([20, 22, 31, 32, 734])
child['dependencies']['direct_refs'] = [ref(22, '野生可逃及决定3的实际规则消费者。'), ref(734, '训练家非回合末等待业主选择及负选择/取消返回。'), ref(20, '回合末替补与通常替补时机分开。'), ref(31, '战斗终局消费决定3。'), ref(32, '外层善后和世界交接接收终局。')]
child['functional_scope'] = {'line_ranges': [[106, 106]], 'excluded_child_refs': [], 'reason': '此行完整描述EMERGENCYEXIT/WIMPOUT跨半退出算法，具有异步业主选择和终局交接。'}
child['differences'] = ['R2 COMBAT-R1-01：从FR-000067不可变源范围内拆出L106；不修改来源行为，全部计划待验证。']
parent['functional_scope'] = {'line_ranges': [[100, 105], [107, 123]], 'excluded_child_refs': [fid(769)], 'reason': '普通HP/状态/阶级反应保留父行；L106逃跑决定与业主替补交互由新协作子行承担。'}
parent['current_applicability']['locator']['line_ranges'] = copy.deepcopy(parent['functional_scope']['line_ranges'])
parent['current_applicability']['locator']['unit_sha256'] = hashlib.sha256(('\n'.join(lines[99:105]) + '\n' + '\n'.join(lines[106:123]) + '\n').encode()).hexdigest()
parent['future_plan']['rationale'] += ' R2有效行为范围排除FR-000769的具名退出/业主选择边界。'
features[fid(769)] = child
manifest['features'].append(child)
next(d for d in manifest['documents'] if d['document_id'] == child['document_id'])['feature_ids'].append(fid(769))
for s in sections:
    if s['path'] == path and s['line_start'] <= 106 <= s['line_end'] and fid(67) in s['feature_refs']:
        s['feature_refs'] = sorted(set(s['feature_refs']) | {fid(769)})
decision('COMBAT-R1-01', '保留纯反应父行，拆出具名退出协作边界。', ids([67, 769]), [{'document': path, 'line_ranges': [[100, 123]], 'key_lines': [106]}], ['ADD_CHILD', 'SUBTRACT_PARENT_SCOPE', 'EXPLICIT_EXIT_RESPONSIBILITIES'])

# DS-R1-003: §13 is exclusively current battle four-layer effects.
roles(261, {'框架': '协调调试授权、层级/目标选择和类型化编辑请求，保持直接调试写入与正常招式/特性流程分离；本表不读写原个体/持久层，不自动触发普通效果后续链。',
            'Showdown': '候选承担当前战斗的全场/阵营/位置/在场成员四层效果的查询与允许直接写入；逐项核对120项映射、上下限及重置，不自动同步原个体、不伪装正常招式/特性执行。',
            'MZ': '按四层呈现120项调试按钮、类型化选值、默认与边界反馈；只是当前战斗直接编辑，不提供原个体或持久层编辑入口。'})
setdeps(261, {4: '当前在场成员/效果初始化与重置的上下文，非原个体写回。', 35: '全场/阵营/位置四层状态域定义。', 39: '当前战斗有界效果目录及作用域。', 40: '普通阶段建立/清理作为对照；调试写入不自动调用该正常链。'}, '删除错误原个体PP/持物接收者147/148；按WP72 §7.5与§13限定当前四层')
features[fid(261)]['future_plan']['questions'] = ['固定目标版本后逐项核对120项当前战斗效果的读写/重置与四层作用域；验证不会修改原个体或触发普通招式/特性后续链。']
features[fid(261)]['future_plan']['prototype_refs'] = []
decision('DS-R1-003', '纠正四层战斗调试与原个体持久写入的错误等同。', ids([261]), [{'document': features[fid(261)]['source']['document'], 'line_ranges': [[212, 217], [307, 451]]}], ['REWRITE_RESPONSIBILITIES', 'CORRECT_RECEIVER_REFS'])

# CAI-R1-01: source records real preparation mutation; no universal rollback promise.
ai = {76: '逐招式/逐目标准备计算类型及global moldBreaker；评分结束清除moldBreaker，再按原槽登记选择。',
      88: '每目标从原招式重建评估对象，处理Copycat/NaturePower/MirrorMove替换后准备共享类型/忽略特性上下文。',
      89: '优先度查询可写Prankster并显式清除；宝石判定写GemConsumed后显式清除，类别函数可真实prepare，读取damageState。',
      98: '伤害粗估前可写共享类型/忽略特性；NaturalGift缺持物错误可在这些写入之后发生，初始100不等于真实HP提交。',
      99: '粗估伤害/恢复查询消费已准备上下文；BeatUp零分母可在共享写入之后失败，非宝石夹具不凭空清GemConsumed。',
      111: '调用替换后沿共同准备合同；SecretPower真实prepare写入效果代码，再由AI自身坏映射评价。'}
shared = {'contract_id': 'R2-AI-PREPARATION', 'status': 'CANDIDATE_UNVERIFIED', 'feature_refs': ids(ai),
          'framework': '拥有评分策略和逐目标原评估对象重建，协调准备→规则查询→源中明确的清理→评分/登记顺序；不把预测变真实HP/PP/持物消耗。',
          'showdown': '候选拥有供评估共享的战斗查询/准备状态及源中具名写入和正常显式清理；类型、忽略特性、Prankster、GemConsumed、类别/SecretPower效果必须逐项映射。',
          'failure': '源中有写入后异常且未见统一回滚，不承诺pure、通用finally清理或失败后无残留。具体源码/目标引擎兼容未验证。',
          'per_feature': [{'feature_id': fid(n), 'source_fact': detail} for n, detail in ai.items()]}
for n, fact in ai.items():
    f = features[fid(n)]
    roles(n, {'框架': f['future_plan']['responsibilities'][0]['scope'] + ' 共享准备责任R2-AI-PREPARATION：评分策略和每目标评估对象重建归框架；协调具名准备/查询/正常清理顺序，不把预测当真实HP/PP提交。',
              'Showdown': '候选拥有共享战斗查询/准备状态及具名正常写入/清理。' + fact + ' 不假设查询纯函数或异常统一回滚；完整共享合同见revisions/r2/shared-ai-preparation.json。'})
    f['future_plan']['questions'].append('验证R2-AI-PREPARATION所列共享写入/清理状态与目标引擎映射；异常前缀不自动回滚，未运行原型。')
    f['dependencies']['direct_refs'].extend([ref(76, 'WP51 §5的共享准备/评分后moldBreaker清理顺序。'), ref(88, 'WP52-A §2每目标评估对象重建与准备。'), ref(89, 'WP52-A §3的Prankster/GemConsumed显式清理及类别prepare；非纯查询合同。')])
decision('CAI-R1-01', '给六行共享准备写入和具名清理明确候选责任，保留异常残留事实。', ids(ai), [{'document': features[fid(n)]['source']['document'], 'line_ranges': features[fid(n)]['source']['line_ranges']} for n in ai], ['EXPLICIT_SHARED_STATE_OWNERSHIP', 'PRESERVE_FAILURE_PREFIX'])

# CAI-R1-02: preserve the exact d62 original as a retired historical identity.
f86 = features.pop(fid(86))
d62 = json.loads(git_bytes(D62, f'{PREFIX}/routing-manifest.json'))
old86 = copy.deepcopy(next(f for f in d62['features'] if f['feature_id'] == fid(86)))
replacement86 = ids([74, 80, 94, 95, 98, 99, 100, 101, 102, 103, 104, 105, 109, 110, 111, 112, 113])
old86['retirement'] = {'reason': 'WP52-A数据§5是已有/前向登记的历史责任索引，不产生独立执行行为。', 'review_finding_refs': ['CAI-R1-02'], 'metadata_record_id': 'META-000033', 'replacement_feature_refs': replacement86}
manifest['features'] = [f for f in manifest['features'] if f['feature_id'] != fid(86)]
manifest['retired_features'].append(old86)
newmeta = {'metadata_id': 'META-000033', 'document_id': f86['document_id'], 'source': copy.deepcopy(f86['source']), 'kind': '评估效果已有与前向归属索引', 'reason': old86['retirement']['reason'], 'feature_refs': replacement86, 'retired_feature_ids': [fid(86)]}
manifest['metadata_records'].append(newmeta)
d = next(d for d in manifest['documents'] if d['document_id'] == f86['document_id'])
d['feature_ids'].remove(fid(86)); d['retired_feature_ids'].append(fid(86))
propagation86 = []
for f in manifest['features']:
    if fid(86) in f['dependencies']['feature_refs']:
        f['dependencies']['feature_refs'] = sorted(set(f['dependencies']['feature_refs']) - {fid(86)} | set(replacement86))
        propagation86.append(f['feature_id'])
for s in sections:
    if fid(86) in s['feature_refs']:
        s['feature_refs'] = sorted(set(s['feature_refs']) - {fid(86)} | set(replacement86))
        if s['path'] == f86['source']['document'] and s['line_start'] <= 237 <= s['line_end']:
            s['metadata_refs'] = sorted(set(s['metadata_refs']) | {'META-000033'})
            s['retired_feature_refs'] = sorted(set(s['retired_feature_refs']) | {fid(86)})
decision('CAI-R1-02', '原ID86完整退役为META33；实际评估功能继续由既有活跃合同承接。', [fid(86), 'META-000033'], [{'document': f86['source']['document'], 'line_ranges': [[237, 255]]}], ['RETIRE_EXACT_D62_ROW', 'REPLACE_ACTIVE_REFERENCES'])

# DS-R1-001: source-row ownership, not WP family coincidence or nearby numbers.
meta_rows(11, [([193, 198], 'WP73-A依赖PBS生命周期、WP73-B地图元数据/遭遇、WP74组织器、WP75编译转换', [270, 272, 286, 294, 301, 401, 402, 403])])
meta_rows(12, [([51, 56], '初始钱包/PC种子、双外观、Home回程与逻辑音频；Home不证明新游戏起点', [152, 153, 178, 355, 600]),
               ([58, 65], '地图元数据、治疗/天气/地形旗标', [324, 325, 326, 329, 331, 372, 600]),
               ([67, 71], '已登记地图连接不证明可通行', [323]),
               ([73, 79], '区域地图、飞行与开关读取消费；事件解锁未证', [633, 374, 600]),
               ([81, 87], 'Dungeon启动、区域/版本参数与布局/图块/摆放；赋值事件未证', [346, 347, 348, 349])])
meta_rows(13, [([91, 98], '遭遇版本/类型/原槽与野外等级/生成', list(range(226, 234))),
               ([100, 105], 'NPC类型、队伍配置与版本装载', [154]),
               ([107, 111], '联系人默认消息/再战版对应', [634]),
               ([113, 121], 'TP/TE一次计算、前四槽/版本回退和失败前缀', [635, 154, 226])])
meta_rows(14, [([125, 134], 'Safari和捕虫会话/接待未证', [580, 581, 582, 583, 584]),
               ([136, 140], '四设施、杯赛和列表作者工具', [114, 117, 119, 124, 128, 129, 234, 235, 236, 308, 309, 310, 311, 312, 313, 314, 315, 316]),
               ([142, 144], '六活动与拼图静态依赖，场所不证明可玩', [247, 248, 249, 250, 251, 252, 609, 615, 616, 617, 695, 699, 708, 714, 725]),
               ([145, 147], 'GIRATINA读取门/动态提交与野外缩放，不由旗标证明实际变形', [461, 463, 466, 229, 346]),
               ([149, 152], 'LocationFlag当前地图求值', [490])])
meta_rows(15, [([154, 157], '区域地图/飞行及电话；作者工具入口与Demo事件分开', [633, 634, 635, 253, 262, 263, 264, 265, 269, 270, 271, 272, 273, 274, 277, 294, 301, 308]),
               ([159, 163], '平衡级唯一WP36数学入口供野外缩放消费', [229])])
meta_rows(16, [([169, 169], 'C1连接到地图登记', [323]), ([170, 170], 'C2遭遇节到地图登记', [226, 324]),
               ([171, 171], 'C3训练家类型注册', [154, 394]), ([172, 172], 'C4联系人到训练家版本', [634, 154]),
               ([173, 173], 'C5飞行记录到目的地/治疗点', [633, 600, 324]), ([174, 174], 'C6地点进化旗标链', [490]),
               ([175, 175], 'C7杯赛ID到设施列表', [114, 117, 119, 124, 309]), ([176, 176], 'C8BugContest类型注册', [226])])
meta_rows(17, [([183, 183], 'G01新游戏起点缺证，不用Home补齐', [445, 642, 152, 153, 178, 600]),
               ([184, 184], 'G02遇敌/钓/碎岩/撞树/雷达缺几何与通行', [226, 227, 229, 374, 376, 379, 380, 520, 521]),
               ([185, 185], 'G03剧情训练家缺放置事件', [154, 1]), ([186, 186], 'G04电话再战缺注册', [634, 635]),
               ([187, 187], 'G05Safari缺接待事件', [580, 581]), ([188, 188], 'G06捕虫缺接待评奖', [582, 583, 584]),
               ([189, 189], 'G07设施杯赛缺接待/租赁/评级链', [114, 124, 128, 129, 234, 235, 236]),
               ([190, 190], 'G08六小游戏/拼图缺事件入口', [247, 609, 615, 695, 699, 708, 714]),
               ([191, 191], 'G09寄养/商店/百货缺库存收费事件', [177, 196, 197, 212, 213, 214, 674]),
               ([192, 192], 'G10地点进化缺地图到达', [490]), ([193, 193], 'G11地牢/动态形态缺图块/参数赋值与进入', [346, 347, 348, 349, 229, 466]),
               ([194, 194], 'G12飞行岛屿缺开关置位/访问', [633, 374])])
decision('DS-R1-001', '七项Demo/作者元数据按实际源组重新绑定，清除错误孵化/HP/设施EV等同号引用。', [f'META-{n:06d}' for n in range(11, 18)], [{'document': metadata[f'META-{n:06d}']['source']['document'], 'line_ranges': metadata[f'META-{n:06d}']['source']['line_ranges']} for n in range(11, 18)], ['REBUILD_EXPLICIT_CONSUMER_RELATIONSHIPS', 'SYNC_RETIREMENT_AND_COVERAGE_REFS'])

def add_catalog(name, start, numbers, why):
    s = section(name, start)
    s['feature_refs'] = sorted(set(s['feature_refs']) | set(ids(numbers)))
    s['metadata_reason'] += ' R2：' + why + '；只是静态未执行目录关联。'

add_catalog('demo-dx-wp72-73-74-75-76-77.md', 285, [456], 'B17普通培养252/510与设施255/255对照需要WP19培养参数')
add_catalog('demo-dx-wp72-73-74-75-76-77.md', 319, [635, 466], 'B20-C028电话TP/TE和C029形态读取门分别消费WP63§5与WP21§6')
decision('DS-R1-002', '补两个具名后继目录漏接的真实消费者，保留旧目录广义导航。', ['DOC-0105'], [{'document': docs['demo-dx-wp72-73-74-75-76-77.md']['source']['path'], 'line_ranges': [[285, 294], [319, 344]]}], ['ADD_CATALOG_REFS_456_635_466'])
add_catalog('pokemon-rules-wp43-44-46-48-50.md', 270, [724], '合法未知效果回退唯一合同WP43§2.1')
decision('POK-R1-CATALOG-001', 'R5-U04目录接到未知效果真实回退行724。', ['DOC-0112', fid(724)], [{'document': docs['pokemon-rules-wp43-44-46-48-50.md']['source']['path'], 'line_ranges': [[270, 285]]}], ['ADD_CATALOG_REF_724'])

collision_paths = {docs[x]['source']['path'] for x in ['wp60-fishing.md', 'wp69-slot-machine.md', 'wp69-slot-reels.md', 'wp70-mining.md', 'wp70-mining-data.md']}
collision_removed = []
for s in sections:
    if Path(s['path']).name == 'pokemon-rules-wp53-60-61-62-69-70.md':
        wrong = [x for x in s['feature_refs'] if features[x]['source']['document'] in collision_paths]
        s['feature_refs'] = [x for x in s['feature_refs'] if x not in wrong]
        if wrong:
            collision_removed.append({'document': s['path'], 'anchor': s['anchor'], 'removed': wrong})
            s['metadata_reason'] += ' R2：按本目录L3明列的六篇源文件消除同WP号Fishing/Slot/Mining误连；消息/地图等真实共享导航保留。'
decision('R1-CATALOG-WP-COLLISION', '按固定文档身份移除16目录节的Fishing/Slot/Mining同号误连。', ['DOC-0113'], [{'document': docs['pokemon-rules-wp53-60-61-62-69-70.md']['source']['path'], 'line_ranges': [[1, 317]], 'key_lines': [3]}], ['REMOVE_EXPLICIT_WRONG_DOCUMENT_LINKS'])

# R1-CRE-DEP-001: seven failing rows, each evaluated by actual source purpose.
deps = {
    155: {355: 'WP24§5.4选曲/引子先交WP15播放、音量与暂停恢复，逻辑请求不等于发声。', 726: 'WP16战前包装读取/恢复音乐记忆并清下一战预置。', 733: 'WP39音频请求与过渡/胜利/捕获交付边界。', 682: 'WP67-A捕获成功音频等待；不是伙伴登记或换人。'},
    157: {1: '伙伴是否参与的谓词为战斗创建输入。', 2: '参与时玩家侧第二训练家/队伍追加及布局归WP39。', 3: '记录伙伴队伍段、所有者与道具再次读取，非WP10标记迁移。'},
    158: {32: '伙伴在场的双方全队治疗/解除变身与可失败败北平局分支是外层善后，未参战仍可触发。', 464: '伙伴在战斗中也沿普通形态进入/离开门。', 473: '伙伴战后解除Mega/Primal的生命周期交界。'},
    186: {11: 'WP40物品选择库存预扣、执行复检与退款；不能由普通背包消耗推断战斗成功。', 32: '战后退款/终局外层善后接收。', 679: 'WP67-A物品/目标/招式选择和取消返回的实际交互。', 525: '球在战斗用物分流后交捕获许可与接收，保留抓球/物品区分。'},
    190: {145: '治疗/复活最终HP与濒死门，战斗与非战斗分流。', 11: '战斗治疗登记、执行复检与消耗/退款。', 32: '战斗结束的治疗/退款善后边界。', 679: '战斗治疗选择目标与取消。', 656: 'MILKDRINK/SOFTBOILED队伍菜单扣使用者HP并治疗目标的实际入口。', 576: '与自动持物HP恢复比较，主动治疗不因此触发持物链。'},
    191: {147: '持久招式槽/PP/PP成长状态与战斗实例同步须分别核对。', 11: '战斗用ETHER等的登记、执行与复检退款。', 679: 'WP67-A§5目标/招式槽选择及取消返回。', 576: 'LEPPABERRY主动用物与自动持物PP恢复不合并；没有香类净化依赖。'},
    192: {11: 'X道具等战斗用物沿WP40登记/执行/消耗。', 679: '实际战斗物品选择目标/取消反馈。', 546: 'X道具阶级资格与提交。', 40: 'GuardSpec的Mist阵营建立及期限。', 22: 'POKEDOLL等走战斗逃跑/拘束交界。', 525: '球类交捕获许可。', 463: '指定特殊道具的形态改变交真实形态提交；不是教学/香/邮件合同。'}
}
for n, links in deps.items():
    setdeps(n, links, '按本源节真实行为重建直接依赖；原document_wp_refs/wp_refs仍保留来源历史前置，不把它们当本行直接依赖')
decision('R1-CRE-DEP-001', '逐七行真实目的纠正伙伴/音频/治疗/PP/战斗特殊物品依赖。', ids(deps), [{'document': features[fid(n)]['source']['document'], 'line_ranges': features[fid(n)]['source']['line_ranges']} for n in deps], ['REPLACE_WRONG_PURPOSE_DIRECT_REFS', 'ADD_ACTUAL_BATTLE_UI_AND_AFTERCARE'])

# R1-KF-001: complete named field/group mappings; no generic WP-number matching.
meta_rows(19, [([250, 250], '世代基准与备选数据集/编译完整性', [388, 391, 401, 402]),
               ([251, 251], '世代基准与逐条覆盖的一致性由具体领域核对', [389, 390, 393, 454, 532, 537]),
               ([252, 252], '亲密与软上限、进化与战斗亲密效果', [208, 490, 501, 28, 532, 533, 534, 535]),
               ([253, 253], '徽章许可的编号/数量两模式', [374, 375]),
               ([254, 254], '配置与插件依赖/载入边界', [411, 412, 413]),
               ([255, 255], 'Shadow开关与捕获/成长/净化', [483, 484, 487, 488, 530, 204, 402])])
field_rows = [
    (319, 'Species身份/形态/来源', [137, 140, 141, 461, 463]), (320, '基础能力IV/EV', [454, 456, 457]),
    (321, '学习表及战斗生效', [206, 207, 147, 29]), (322, '进化方法参数/前后关系', [490, 491, 493, 501, 503]),
    (323, '蛋群/熏香/后代及孵化', [212, 214, 508, 509, 510, 511, 512, 513, 219]),
    (324, '野生持物/遭遇修正', [229]), (325, 'Mega/Primal资格与时机', [469, 470, 471, 472, 14]),
    (326, '图鉴文本/分类/展示及资源/本地化', [604, 606, 608, 438, 440, 353, 465]),
    (327, '特性选择/计算与阶段触发', [454, 562, 563, 564, 565, 566, 567, 568, 569, 64, 65, 66, 67, 68, 69, 70, 71, 769]),
    (328, '性别比例/成长曲线', [454, 203, 137]), (329, 'SpeciesMetrics资源尺寸/阴影位置', [353, 364]),
    (330, 'SpeciesMetrics战斗放置/指标编辑', [683, 273, 353]), (331, 'Type相克/属性/图标', [532, 454, 353]),
    (332, 'Ability文字标志/计算触发与AI引用', [438, 440, 562, 65, 66, 67, 68, 69, 70, 76, 88, 769]),
    (333, 'Shadow全部字段及抢夺/呼唤/成长', [483, 484, 485, 486, 487, 488, 489, 530, 14, 204]),
    (334, 'Move数值分类目标', [532, 533, 535, 454]), (335, 'Move优先级', [13]),
    (336, 'Move效果代码/效果率/AI消费者', [543, 544, 545, 546, 547, 548, 555, 556, 557, 558, 559, 560, 48, 49, 50, 51, 52, 53, 54, 55, 58, 59, 60, 61, 62, 76, 88, 98, 111]),
    (337, '反向机器/学习关联，不是Move自身字段', [188, 189, 206]),
    (338, 'Item口袋/价格/BP价/交易反馈', [177, 196, 197, 198, 153, 674]),
    (339, 'Item使用上下文与机器教学', [183, 184, 186, 188, 189, 206, 525, 11]),
    (340, 'Item持有物状态及触发', [148, 574, 575, 576, 577, 578, 579]),
    (341, 'Item球/邮件/重要物品标志', [188, 525, 527, 239, 240]),
    (342, 'BerryPlant完整生命周期', [588, 589, 590, 591, 592, 177, 425]),
    (343, 'Ribbon展示及演出', [465, 747]), (344, 'Encounter版本/类型/修正与漫游雷达', [226, 227, 228, 229, 230, 517, 518, 519, 520, 521]),
    (345, 'TrainerType资源/电话类型', [154, 155, 353, 634]), (346, 'Trainer身份队伍/再战推进', [154, 1, 634]),
    (347, 'Trainer成员配置', [138, 454, 456, 154, 1]), (348, 'PhoneMessage完整联系人/呈现消费', [634, 635, 625]),
    (349, 'MapMetadata世界/天气/地形/地牢/遭遇', [323, 324, 329, 331, 372, 374, 346, 226]),
    (350, 'MapMetadata治疗点/地图位置尺寸', [324, 600, 633, 353]),
    (351, 'MapMetadata战斗背景/音乐/环境', [353, 355, 726, 683, 733, 5]),
    (352, 'TownMap区域地图及资源', [633, 353]), (353, 'Metadata初始资源/全局默认', [445, 153, 178]),
    (354, 'PlayerMetadata外观/Home/初始位置', [152, 445, 353, 600]),
    (355, 'DungeonTileset全部字段/图块供给', [346, 348]), (356, 'DungeonParameters全部字段/随机种子', [346, 347, 427]),
    (357, '17类固定规则的领域消费者', [203, 137, 454, 508, 490, 501, 145, 146, 543, 329, 226, 372, 35, 532]),
    (358, '区域图鉴/连接/设施名单/战斗动画/MapInfos等非类产物', [607, 323, 114, 124, 309, 683, 277, 289, 403])]
meta_rows(20, [([line, line], label, ns) for line, label, ns in field_rows])
meta_rows(21, [([290, 290], '本地化/文本收集与PBS产物', [438, 440, 441]),
               ([291, 291], '数据/世界编辑器读写编译产物', [262, 263, 264, 265, 269, 270, 271, 272, 273, 274]),
               ([292, 292], '事件转换与编译驱动', [294, 295, 296, 297, 298, 299, 300, 301]),
               ([293, 293], '资源/指标/动画映射消费者', [352, 353, 354, 683, 289]),
               ([294, 294], '内容身份与schema定义', [394, 395, 396, 397]),
               ([295, 295], '候选数据集手动选择', [391])])
kc = 'generic-kernel-wp02-03-04.md'
for start, nums, why in [(5, [374, 375, 439, 441, 642, 644], 'KC03徽章许可、KC05/06语言选择与提取取消'),
                         (16, [454, 456], 'KR13固定Nature顺序与能力结果依赖WP19'),
                         (37, [323, 269, 272, 273], 'KL18/22/23–26/44连接、遭遇编辑与指标读写消费者'),
                         (97, [346, 347, 348, 349, 323, 269], 'U01-M01-021/022地牢类型供给，027连接解析及编辑'),
                         (181, [219, 273], 'FLAGS04每步减步后查询失败与部分指标编辑'),
                         (200, [346, 347, 348, 349, 273], 'J01-V01–06/V11地牢；V12指标编辑No/Yes分层')]:
    add_catalog(kc, start, nums, why)
add_catalog('generic-kernel-wp05-06-07-08-09-10.md', 277, [352, 353, 639], 'LZ39–41指定键图身份交WP15资源与WP65控制帮助页消费')
decision('R1-KF-001', '三个内核元数据按全部字段责任组重绑，补具名目录跨域消费者；移除Fishing邻号误连。', ['META-000019', 'META-000020', 'META-000021', 'DOC-0108', 'DOC-0109'], [{'document': metadata[f'META-{n:06d}']['source']['document'], 'line_ranges': metadata[f'META-{n:06d}']['source']['line_ranges']} for n in [19, 20, 21]], ['EXPLICIT_FIELD_GROUP_MAPPING', 'ADD_NAMED_CATALOG_CONSUMERS'])

features[fid(420)]['dependencies']['feature_refs'] = sorted(set(features[fid(420)]['dependencies']['feature_refs']) | {fid(471)})
features[fid(420)]['dependencies']['direct_refs'].append(ref(471, 'mega_evolution_count仅玩家自己拥有者的Mega实际执行增加，写入在消息/变形之前；异常可保留计数，不由终局或捕获计数替代此生产点。'))
setdeps(436, {406: 'WP04启动/直接编译不同异常层的诊断、清理尝试与异常转换；错误定位可能先发生，非本地化集合。',
              413: 'WP05插件元数据/依赖/加载错误的诊断后终止边界。',
              448: 'WP09主循环普通异常/特殊异常及Hangup紧急保存进入条件，未假设原子回滚。',
              451: 'WP10载入失败/回退/恢复与紧急保存条件；不能把所有诊断都当语言状态。',
              432: '弃用告警的沉默/输出条件与致命异常层分开。'}, '纠正复制而来的本地化用途，改为每个真实失败/恢复层用途')
decision('R1-KF-002', '统计补Mega实际生产点；失败层依赖逐条纠正为编译/插件/主循环/恢复用途。', ids([420, 436]), [{'document': features[fid(420)]['source']['document'], 'line_ranges': [[73, 87]]}, {'document': features[fid(471)]['source']['document'], 'line_ranges': [[56, 60]]}, {'document': features[fid(436)]['source']['document'], 'line_ranges': [[155, 168]]}], ['ADD_ACTUAL_STAT_PRODUCER', 'REWRITE_WRONG_LOCALIZATION_REASONS'])

# Archive identity invariants and fixed accepted overlay are checked before any write.
now = {f['feature_id']: f for f in manifest['features']}
for f in original['features']:
    if f['feature_id'] != fid(86):
        assert now[f['feature_id']]['source'] == f['source']
        if f['feature_id'] != fid(67):
            assert now[f['feature_id']]['current_applicability'] == f['current_applicability']
for f in original['retired_features']:
    assert {k: v for k, v in retired[f['feature_id']].items() if k != 'retirement'} == {k: v for k, v in f.items() if k != 'retirement'}
assert manifest['current_snapshot'] == original['current_snapshot']
assert manifest['source_baseline'] == original['source_baseline']
assert manifest['decisions'] == original['decisions']
assert manifest['prototypes'] == original['prototypes']
assert len(manifest['features']) == len(original['features'])
save('routing-manifest.json', manifest)
save('section-coverage.json', coverage)
save('revisions/r2/explicit-decisions.json', {'schema_version': 'routing-author-r2-decisions.v1', 'input_candidate': BASE, 'review_commit': REVIEW, 'status': 'AUTHOR_REVISED_AWAITING_ULTRA_DEFAULT_REVIEW', 'items': decisions, 'tool_finding': 'ROOT-R1-VIEW-01由父任务单独修复；结果引用tools证据，不自行作PASS结论。'})
save('revisions/r2/consumer-mappings.json', {'schema_version': 'routing-consumer-mappings.v1', 'input_candidate': BASE, 'review_commit': REVIEW, 'relationships': consumption, 'fr86_reference_propagation': propagation86, 'collision_removals': collision_removed, 'limitation': '显式源组消费定位；来源事实不证明Showdown支持、实现、Demo可达或原型通过。'})
save('revisions/r2/shared-ai-preparation.json', shared)

def delta_rows(old, new, key):
    a = {x[key]: x for x in old}; b = {x[key]: x for x in new}
    return {'added': sorted(b.keys() - a.keys()), 'removed': sorted(a.keys() - b.keys()),
            'changed': [{'id': k, 'fields': [f for f in sorted(set(a[k]) | set(b[k])) if a[k].get(f) != b[k].get(f)]} for k in sorted(a.keys() & b.keys()) if a[k] != b[k]]}

save('revisions/r2/data-diff.json', {'input_candidate': BASE, 'features': delta_rows(original['features'], manifest['features'], 'feature_id'), 'retired': delta_rows(original['retired_features'], manifest['retired_features'], 'feature_id'), 'metadata': delta_rows(original['metadata_records'], manifest['metadata_records'], 'metadata_id'), 'coverage_changed': [{'path': a['path'], 'anchor': a['anchor'], 'fields': [k for k in a if a[k] != b[k]]} for a, b in zip(old_coverage['sections'], sections) if a != b], 'invariants': {'all_existing_source_objects_unchanged': True, 'old_retired_original_fields_unchanged': True, 'accepted_current_snapshot_unchanged': True, 'prototypes_and_decisions_unchanged': True}, 'status': 'AUTHOR_DIFF_NOT_INDEPENDENT_ACCEPTANCE'})
print(json.dumps({'active': len(manifest['features']), 'retired': len(manifest['retired_features']), 'metadata': len(manifest['metadata_records']), 'new_ids': [fid(769)], 'retired_this_revision': [fid(86)], 'semantic_findings': len(decisions)}, ensure_ascii=False))
