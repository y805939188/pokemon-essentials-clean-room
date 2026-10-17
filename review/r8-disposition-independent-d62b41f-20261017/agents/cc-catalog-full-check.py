#!/usr/bin/env python3
"""Independent static evidence collector for the fixed six-catalog review only."""
import hashlib
import json
import re
import subprocess
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path('/workspace/pokemon-essentials-clean-room')
OUT = ROOT / 'review/r8-disposition-independent-d62b41f-20261017/agents'
CANDIDATE = 'd62b41f4d620e50bb04c80a7505374bd284d8210'
SOURCE = '4575e80d041ab0c74a42e2e36399d05791dbaa5b'
B8 = 'fd1df570cad987dc3852a3b958f03916e317f7fe'
ROUTING = 'planning/implementation-routing/r8-20261017/'
FORMAL = 'deliverables/final-specification-set/'
CAT = FORMAL + 'test-catalog/'
HANDOFF = 'review/global-independent-review/eighth-2026-10-16-fd1df57-c84e/handoff/'
FILES = [
    'creature-rpg-wp18-20-24-25-26.md',
    'creature-rpg-wp27-28-29-30-33.md',
    'creature-rpg-wp35-36-57-64-68.md',
    'combat-requirements-wp39-40-41-42-45.md',
    'combat-requirements-wp47-ab.md',
    'combat-requirements-wp54-55-56-58.md',
]
READ_CHUNKS = [
    [[1, 110], [111, 220], [219, 331]],
    [[1, 115], [116, 220], [221, 326]],
    [[1, 100], [101, 183]],
    [[1, 105], [106, 210], [211, 297]],
    [[1, 90], [91, 165]],
    [[1, 100], [101, 190]],
]
commands = []


def utc():
    return datetime.now(timezone.utc).isoformat()


def git(*args, binary=False):
    argv = ['git', *args]
    start = utc()
    p = subprocess.run(argv, cwd=ROOT, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    commands.append({'argv': argv, 'started_utc': start, 'finished_utc': utc(),
                     'exit_code': p.returncode, 'stderr': p.stderr.decode(),
                     'stdout_sha256': hashlib.sha256(p.stdout).hexdigest(),
                     'stdout_bytes': len(p.stdout),
                     'stdout': None if binary else p.stdout.decode()})
    p.check_returncode()
    return p.stdout if binary else p.stdout.decode().strip()


def at_commit(path, commit=CANDIDATE):
    return git('show', f'{commit}:{path}', binary=True)


def sha(data):
    return hashlib.sha256(data).hexdigest()


def independent_headings(data):
    lines = data.decode().splitlines()
    hs = []
    fence = None
    for line_number, line in enumerate(lines, 1):
        stripped = line.lstrip()
        fm = re.match(r'^(`{3,}|~{3,})', stripped)
        if fm:
            token = fm.group(1)[0]
            if fence is None:
                fence = token
            elif fence == token:
                fence = None
            continue
        if fence:
            continue
        m = re.match(r'^(#{1,6})[ \t]+(.+?)\s*$', line)
        if m:
            title = re.sub(r'[ \t]+#+[ \t]*$', '', m.group(2))
            hs.append({'level': len(m.group(1)), 'title': title, 'line_start': line_number})
    for i, h in enumerate(hs):
        h['line_end'] = next((n['line_start'] - 1 for n in hs[i + 1:]
                              if n['level'] <= h['level']), len(lines))
    return hs


# Hand-authored semantic observations follow actual complete reads in the tool transcript.
# Each list is in source heading order, including the H1 and all H3/history sections.
OBSERVATIONS = [
    [
        ('137-176', '整篇登记CI/HP/PT/PS/AQ及历史追加静态设计；对应五篇主规格的宽导航合理。'),
        ('137-144', '物种默认、创建形态/缓存、复制、拥有者/来源及失败前缀均由WP18消费。'),
        ('140,143', 'Owner构造同值遮蔽与单字段校验明确限定入口，属于拥有者与失败边界。'),
        ('145-151', 'HP/状态、超四招存储、TR首招记录、持物还原与PP写穿由WP20主合同承接。'),
        ('152-161', '资源/装载/伙伴为WP24；PT41-63音频请求有独立FR155，参与/战后有FR157/158，未把请求当发声。'),
        ('162-170', '集合别名、复制追加、守卫、治疗及墙纸内存写回由WP25承接；UI拆行FR163/165可导航。'),
        ('171-176', '赠送/静默/外来/蛋/交换及等待重检前缀属于WP26；入队/送箱引用保持领域边界。'),
        ('141', '尺寸辅助是WP18来源记录章节内已有§7.4数学；合法输入域、默认消费者未知均保留。'),
        ('141', '全15分段两端为同一尺寸辅助测试设计，不需要新建15个实现功能。'),
        ('153,154,162,164', 'StartMoney/免费购买交界由WP24资源承接；负地址容量由WP25承接，NPC默认覆盖由WP24装载承接。跨商店仍有正文前向引用。'),
        ('137,138', '作者Happiness256/255/省略/0分别检查物种输入与创建直写，由WP18主规格承接；普通变化不提前夹限。'),
    ],
    [
        ('177-217', '整篇BG/IU/SH/GR/DC和R4/R5/R6追加设计由五篇主规格承接，未独立登记测试为实现。'),
        ('177-182', '槽容量、直接部分提交、预检、快捷登记、旧档转换和菜单给予资格均有WP27归属。'),
        ('183-195', '道具效果/培养/教学与场外场内差异由WP28承接；FR186/187/190/191/192分出战斗库存/效果交界。'),
        ('186,191', 'PP补给HP0在场外/战斗的不同资格、登记扣减、选招取消、回满封顶由WP28§5.2及3.5承接。'),
        ('196-202', '购买/售出/BP半价显示与实际扣减、免费钱包写回、价格覆盖由WP29承接。'),
        ('203-211', '经验步进取整、EV先写、学习取消/重学候选与友好规则由WP30；战中成长/学习有FR204/207原型候选。'),
        ('212-217', '寄养槽、兼容先门、周期/直接领取差异、满队先生成和供方槽序由WP33承接。'),
        ('184,185', 'Itemfinder的矩形范围、Manhattan排序、同距枚举、方向锁定和统计前缀由WP28专门FR185承接。'),
        ('205,208', '经验设置先提示后提交、同值早退、钳制后差量及友好变化由WP30经验辅助承接。'),
        ('177,179,183,184,188,189,196,199', '历史综合向量含钱包/商店、形态道具回调、融合嵌套缩队、培养和选择工具；本篇WP28主流与WP27/WP29状态交界可消费，外部WP21形态主规则不被声称重新验证。'),
        ('208', '作者友好初值与正常walking夹限是WP30§7.1-7.2同一规则的入口对照。'),
    ],
    [
        ('218-252', '本篇五组是蛋/遭遇/Factory/邮件礼物/Triple Triad，B18后继资格限定旧字节；不含Duel动作对决。'),
        ('218-225', '蛋每步/同轮加速、提交前缀、演出动态形态/图鉴与命名由WP35承接。'),
        ('226-233', '遭遇输入、机会/候选/允许门、步进/转向/主动包装、雷达/伙伴与大会分流由WP36承接。'),
        ('234-238', 'Factory租借池、上端越界、整体重试、对象交换与取消提交由WP57承接。'),
        ('239-246', '邮件快照/自清错误、礼物下载/同ID队列/领取/编辑别名由WP64承接；MG31/32仍须U09修正输入精度。'),
        ('247-252', '卡片价格、槽概率、翻牌、终局转移与openhand导航均为WP68 Triple Triad，没有Duel生命/动作矩阵。'),
        ('250,252', '局部通知1.5秒与结果消息USE/BACK是Triad会话/交互的消费者，不能关联Duel不可取消动作。'),
        ('239,240', 'PC Give失败前缀、盒子Summary写信快照与取消保留属于WP64邮件与流转。'),
    ],
    [
        ('1-42', '整篇战斗入口/命令/换人逃跑/成长终局/天气域的静态验收源，五篇宽导航可接受。'),
        ('1-8', 'BC覆盖入口生成/覆盖、训练家布局、业主范围、音乐请求与对位查询/投球前缀，由WP39主规格消费。'),
        ('9-17', '命令/服从/顺序、物品Direct5、特殊调用、目标选择和PP前缀由WP40主规格消费。'),
        ('18-26', '换人准入、追击、Shift、逃跑概率和扫描内写3后继续替补由WP41主规格消费，FR22保逃跑原型。'),
        ('29', 'EV先写、逐级反馈、取消学招、持久/场上回读由WP42成长交界消费，FR29保战中成长原型。'),
        ('28,30', 'EOR缓存序、阶段到达、灭亡歌检查点、自动中央化与延迟攻击交叉清理由WP42消费。'),
        ('31-33', '旧/新决定、奖金/治疗、BURMY按席记录错配、显式中止/退款及伙伴对象别名由正常终局/世界交接消费。'),
        ('36,37', '世界映射/默认/存储与有效天气、压制和原始天气结束由WP45消费。'),
        ('38', '青草恢复先到期、默认场地恢复与直接清除不同，由WP45场地消费。'),
        ('39,40', '全场重力/空间、旧新玩水及通知差异由WP45有界全场/清理消费。'),
        ('39,40', '屏障、火海双递减、换场、回声和保护最后行动门由WP45阵营合同消费。'),
        ('41', '撒菱/岩钉/毒菱吸收/黏网不同输入、整数阶段与免疫由WP45入场危害消费。'),
        ('42', '祈愿、治愈之愿、Shift与延迟攻击清来源关系由WP45位置与延迟执行消费。'),
        ('40', '除雾的具名清理范围及不因闪避封顶失败由WP45清场合同消费。'),
        ('11,31', '双POTION资格失败退款残留与同轮再次撤销由WP40库存选择和WP42终局消费，均保持未运行。'),
        ('3,12,13,30,33', '历史FH/MET/RANK/ERR保失败/计数/显示秩/局部错误后调度，分别可导航WP39-42；未将诊断捕获等同恢复。'),
    ],
    [
        ('43-63', 'WP47-A/B正文及数据附页的静态设计，不制造独立功能/执行结果。'),
        ('43-52', '类型/环境、保护、目标重定向、复制调用与完整排除数据由WP47-A消费。'),
        ('53-63', '换人接力、束缚/代价、号令/PP、C/I/R/P物品关系和能力/变身由WP47-B消费。'),
        ('51,58,62', 'CURSE动态目标、EXPANDINGFORCE类别、Ice Face成功击与精确skillswapclause消费者属于WP47-A/B。'),
        ('45,49', '自然之恩自耗后续击空身份访问有WP47-A主合同与默认数据行；WP46/50交界保正文引用，AI不被套用异常。'),
        ('58,59,62', '原能力值读写与WonderRoom、Shadow实效/命名绑定、BEAKBLAST替身局部失败由WP47-B承接，未签运行。'),
        ('51', 'PROTEAN后期CURSE目标重建与先前FOLLOWME不同，WP47-A目标行承接；PP/类型/诅咒前缀不回滚。'),
    ],
    [
        ('114-136', '资格/临调、会话、Palace/Arena与记录回放四组静态案例，原W编号按系列保留。'),
        ('114-123', '四类资格、数量输入、临调位置还原、条款真实键/消费者由WP54正文及数据附页承接。'),
        ('124-127', 'WS有放回生成/短名单、快照/报名别名、保存失败及取消/结束差异由WP55会话合同承接。'),
        ('125,126', '零候选与缺模板导致不同治疗/构造前缀由WP55单场交界与失败合同消费，未误推自动补齐。'),
        ('128-131', 'Palace性格/AI和Arena累计不复位、结算时机/持久HP与回复期边界，由WP56变体承接且范围待决。'),
        ('132-136', 'RC记录时点、Mega漏记、布局不还原、全局图鉴/背包写入、换人序列与随机域由WP58承接；非真实回放执行。'),
    ],
]


def ids(spec):
    result = []
    for token in spec.split(','):
        if '-' in token:
            a, b = map(int, token.split('-'))
            result.extend(f'FR-{x:06d}' for x in range(a, b + 1))
        else:
            result.append(f'FR-{int(token):06d}')
    return result


started = utc()
manifest = json.loads(at_commit(ROUTING + 'routing-manifest.json'))
coverage = json.loads(at_commit(ROUTING + 'section-coverage.json'))
file_manifest = json.loads(at_commit(ROUTING + 'candidate-file-manifest.json'))
batches = json.loads(at_commit(HANDOFF + 'batch-assignment.json', SOURCE))['batches']
feature_by_id = {x['feature_id']: x for x in manifest['features']}
trees = {c: git('rev-parse', f'{c}:{FORMAL.rstrip("/")}') for c in [CANDIDATE, SOURCE, B8]}
candidate_file_checks = []
for f in file_manifest['files']:
    data = at_commit(f['path'])
    tree_line = git('ls-tree', CANDIDATE, '--', f['path'])
    mode, _, blob_and_path = tree_line.split(' ', 2)
    blob, _ = blob_and_path.split('\t', 1)
    candidate_file_checks.append({'path': f['path'], 'bytes': len(data), 'sha256': sha(data),
        'git_blob': blob, 'git_mode': mode,
        'manifest_matches': (len(data), sha(data), blob, mode) ==
                            (f['bytes'], f['sha256'], f['git_blob'], f['git_mode']),
        'workspace_matches_fixed_candidate': (ROOT / f['path']).read_bytes() == data})

documents = []
section_results = []
for file_index, name in enumerate(FILES):
    path = CAT + name
    data = at_commit(path)
    source_data = at_commit(path, SOURCE)
    b8_data = at_commit(path, B8)
    hs = independent_headings(data)
    indexed = [(i, s) for i, s in enumerate(coverage['sections']) if s['path'] == path]
    doc_index, doc = next((i, d) for i, d in enumerate(manifest['documents']) if d['source']['path'] == path)
    assert len(hs) == len(indexed) == len(OBSERVATIONS[file_index]), name
    mapping_checks = []
    for h, (section_index, s), (primary_refs, reason) in zip(hs, indexed, OBSERVATIONS[file_index]):
        loc_ok = all(h[k] == s[k] for k in ['level', 'title', 'line_start', 'line_end'])
        primary = ids(primary_refs)
        primary_present = set(primary).issubset(s['feature_refs'])
        mapping_checks.append(loc_ok and primary_present)
        bad = [f for f in s['feature_refs'] if feature_by_id[f]['source']['document'] == FORMAL + 'user-interface/wp68-duel.md']
        section_results.append({'source_document': path, **h,
            'coverage_pointer': f'/sections/{section_index}', 'anchor': s['anchor'],
            'mapping_kind': s['mapping_kind'], 'related_wp_refs': s['related_wp_refs'],
            'actual_feature_refs': s['feature_refs'], 'semantically_relevant_primary_refs': primary,
            'locator_and_primary_link_check': loc_ok and primary_present,
            'status': 'FAIL' if bad else 'PASS',
            'reason': reason + (' 但同WP号连接还加入四条Duel专属功能，见CC-CATALOG-F01。' if bad else ' 同篇广绑作为静态导航可接受，不声称每条关联逐case适用。'),
            'unrelated_feature_refs': bad, 'finding_refs': ['CC-CATALOG-F01'] if bad else []})
    documents.append({'path': path, 'document_id': doc['document_id'],
        'manifest_document_pointer': f'/documents/{doc_index}', 'bytes': len(data),
        'sha256': sha(data), 'git_blob': git('rev-parse', f'{CANDIDATE}:{path}'),
        'line_count': len(data.decode().splitlines()), 'heading_count': len(hs),
        'semantic_read_status': 'FULL_READ', 'semantic_read_ranges_inclusive': [[1, len(data.decode().splitlines())]],
        'actual_untruncated_read_chunks_inclusive': READ_CHUNKS[file_index],
        'missing_or_unread_lines': [], 'source_delivery_identical': data == source_data,
        'b8_identical': data == b8_data, 'workspace_identical': data == (ROOT / path).read_bytes(),
        'source_manifest_identity_matches': (len(data), sha(data)) == (doc['source']['bytes'], doc['source']['sha256']),
        'all_headings_located_and_primary_links_present': all(mapping_checks),
        'all_sections_metadata': all(s['mapping_kind'] == 'section-metadata' for _, s in indexed),
        'catalog_feature_ids': doc['feature_ids'], 'upstream': doc['upstream'],
        'mapped_feature_count': len({f for _, s in indexed for f in s['feature_refs']}),
        'status': 'FAIL' if file_index == 2 else 'PASS'})

referenced_ids = sorted({f for s in section_results for f in s['actual_feature_refs']})
feature_checks = []
for fid in referenced_ids:
    f = feature_by_id[fid]
    expected_batches = sorted(b['id'] for b in batches if f['source']['document'] in b['actual_target_write_set'])
    expected_required = sorted({x for b in batches if b['id'] in expected_batches for x in b['required_ids']})
    feature_checks.append({'feature_id': fid, 'source_document': f['source']['document'],
        'source_heading': f['source']['heading'], 'future_destination': f['future_plan']['destination'],
        'stage': f['future_plan']['stage'], 'stage_approval': f['future_plan']['stage_approval'],
        'destination_verification_status': f['destination_verification']['status'],
        'implementation_status': f['implementation']['status'], 'acceptance_status': f['implementation']['acceptance_status'],
        'compatibility_evidence': f['destination_verification']['evidence'],
        'source_only_is_compatibility_evidence': f['destination_verification']['source_only_is_compatibility_evidence'],
        'prototype_refs': f['future_plan']['prototype_refs'], 'decision_refs': f['decision_refs'],
        'upstream': f['upstream'], 'expected_document_write_set_batches': expected_batches,
        'upstream_batch_and_required_ids_match': f['upstream']['batches'] == expected_batches and
                                                 f['upstream']['required_ids'] == expected_required,
        'no_acceptance_promotion': f['destination_verification']['status'] == '待验证' and
                                  f['implementation']['status'] == '未实现' and
                                  f['implementation']['acceptance_status'] == '未验收' and
                                  f['future_plan']['stage'] == '待定' and
                                  f['future_plan']['stage_approval'] == '未批准' and
                                  not f['destination_verification']['evidence'] and
                                  not f['upstream']['accepted_events'] and
                                  not f['destination_verification']['source_only_is_compatibility_evidence']})

finding = {
    'id': 'CC-CATALOG-F01', 'severity': 'P3', 'status': 'FAIL',
    'title': 'WP68编号碰撞把Triad静态目录错误关联到Duel动作对决',
    'candidate_commit': CANDIDATE,
    'candidate_path': ROUTING + 'section-coverage.json',
    'source_path': CAT + FILES[2], 'source_lines': [[1, 5], [129, 167]],
    'affected_section_pointers': [f'/sections/{i}' for i in range(2156, 2164)],
    'exact_unrelated_ref_pointers': [f'/sections/{i}/feature_refs/{j}' for i in range(2156, 2164) for j in range(35, 39)],
    'unrelated_feature_ids': ['FR-000695', 'FR-000696', 'FR-000697', 'FR-000698'],
    'feature_pointers': [f'/features/{i}' for i in range(694, 698)],
    'unrelated_source_document': FORMAL + 'user-interface/wp68-duel.md',
    'unrelated_source_lines': [[5, 13], [23, 88]],
    'generator_path': ROUTING + 'routing.py', 'generator_lines': [[271, 276]],
    'reason': '目录明确只收录WP35/WP36/WP57/WP64及WP68 Triple Triad；全部案例/历史段无Duel四动作、两项临时生命或角色地图对决。Duel正文L13明确两者使用独立规则；当前生成器按document_wp_refs交集，仅共同WP68便把Duel四行加入全部8个元数据章节，造成32条错误关联。',
    'why_not_overgranularity': '允许保留本篇35条真实主规格功能的宽导航，也不要求每个case拥有功能ID；错误是跨独立子体系关系，不是章节粗标本身。',
    'necessary_fix': '保留稳定功能ID及正式正文，使用显式源文档/子体系资格或等效限定规则生成catalog元数据关联；从本篇8项feature_refs排除FR-000695..FR-000698，再重生成、静态校验并固定新候选复核。保留Triple Triad的FR-000247..252和其它四组主规格关联。',
    'runtime_or_upstream_acceptance_inferred': False,
}

result = {
    'schema': 'r8-independent-six-catalog-full-review/v1', 'reviewer': '/root/creature_combat_catalog_full_review',
    'platform_task_id': 'UNVERIFIED', 'candidate_commit': CANDIDATE, 'source_delivery_commit': SOURCE,
    'historical_source_commit': B8, 'formal_trees': trees, 'all_three_formal_trees_equal': len(set(trees.values())) == 1,
    'requested_configuration_from_delegation': {'model': 'gpt-6.1-sol', 'effort': 'ultra', 'service_tier': 'default'},
    'effective_configuration_echo': {k: 'UNVERIFIED' for k in ['model', 'effort', 'tier', 'speed', 'Fast']},
    'configuration_boundary': '请求由父任务给定；本context没有可核验的执行telemetry或default tier创建回显，不把继承/名称视为有效配置证明。',
    'started_collection_utc': started, 'finished_collection_utc': utc(),
    'scope': {'catalog_documents': 6, 'catalog_bytes': sum(d['bytes'] for d in documents),
              'catalog_lines': sum(d['line_count'] for d in documents), 'headings': len(section_results),
              'distinct_related_feature_ids': len(referenced_ids), 'distinct_intended_related_feature_ids': len(referenced_ids) - 4,
              'catalog_created_feature_rows': 0, 'section_status_counts': dict(Counter(s['status'] for s in section_results)),
              'case_execution_count': 0, 'reference_execution_count': 0, 'framework_execution_count': 0, 'prototype_runs': 0},
    'documents': documents, 'section_results': section_results, 'feature_state_and_binding_checks': feature_checks,
    'candidate_file_identity_checks': candidate_file_checks,
    'candidate_manifest_files_all_match': all(x['manifest_matches'] and x['workspace_matches_fixed_candidate'] for x in candidate_file_checks),
    'all_mapped_feature_state_checks_pass': all(x['no_acceptance_promotion'] for x in feature_checks),
    'all_mapped_feature_document_batch_bindings_pass': all(x['upstream_batch_and_required_ids_match'] for x in feature_checks),
    'findings': [finding],
    'upstream_observations': [
        'DOC-0098 combat主目录整体绑定R8-U06，DOC-0104 Creature9c整体绑定R8-U09；写集保守绑定不声称每个必修ID均修改所有案例。',
        'WP36相关FR226..233依R8-U05；WP30相关FR203..211依R8-U06；WP18相关FR137..144和WP64相关FR239..246依R8-U09，全部待整改后核对。',
        'R8-U07写集是navigation/current-r7-metadata-qualification.json，没有本六目录写集；Creature9c L5 B18旧字节静态资格不向本候选转授。全局上游门仍未接受。',
        'MG31/32命名取消/空文输入精度是U09待整改事项，来源仍固定旧字节，不以静态例或粗标证明修复。',
        'WP58 attribution可选项GR8-COM-RECORD-DEBUG-RNG-001未选，RC-W11静态正确控制不自动产生U06必修绑定。',
    ],
    'reading_boundary': {
        'full_catalogs': '六份全部正文、表行、共同前提、历史与补充层；工具分块正文输出无截断。',
        'prerequisites': ['AGENTS.md全文', ROUTING + 'README.md全文', ROUTING + 'review-prompt.md全文',
                          HANDOFF.replace('handoff/', '') + 'DELIVERY.md全文',
                          HANDOFF.replace('handoff/', '') + 'inputs/review-SKILL.md全文（只读规则，不用于审计报告写作）',
                          HANDOFF + 'cloud-eighth-update-handoff-prompt.md全文（首输出截断部分由后继分块补读）'],
        'related_indices': 'batch-assignment.json中U05/U06/U07/U09的完整required/optional/actual_target_write_set范围投影；不是全部39规范合同全文。',
        'candidate_projections': '全部59个section-coverage对象；全部206关联feature的身份/源章节/去向/阶段/验证/实现/验收/批次状态投影，敏感边界另读完整对象。',
        'supporting_source_reads': [{'path': FORMAL + 'user-interface/wp68-duel.md', 'lines': [[1, 88]], 'status': 'PARTIAL_SUPPORTING_READ'}],
        'not_claimed': ['其余11个catalog全文（含combat AI catalog）', '全部正式正文全文', '全部主清单/schema/工具/生成视图全文',
                        '全部R8合同及reference源单位全文', '任意业务向量执行或原型运行', '全项目最终验收'],
        'truncation_handling': '初次宽投影输出曾截断；59个章节及所有关联功能身份/状态均已用精简投影或独立检查补齐。未把截断批次readset大输出记为完整读取。',
    },
    'command_receipts': commands,
    'prior_tool_transcript_observations': [
        '全部六catalog语义读取使用nl -ba与sed指定连续区间，stdout完整可见，所有调用exit0；区间逐文档记录于documents。',
        '一次文档索引投影误用documents[].path导致KeyError:path（exit1），随后改用documents[].source.path重读，未影响候选。',
        '早期rg/readset宽输出有截断，不作完整readset信用；本报告只登记实际补读范围。',
    ],
    'conclusion': 'FAIL_FIXED_CANDIDATE_METADATA_RELATIONSHIP; 六目录已全文阅读，1项P3确定问题待修；其余51章通过本范围静态关联/证据状态核对。最终上游校准、用户范围决定和原型仍待办。',
}
OUT.mkdir(parents=True, exist_ok=True)
(OUT / 'cc-catalog-full-results.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({'candidate': CANDIDATE, 'formal_tree': next(iter(trees.values())), 'scope': result['scope'],
                  'identity_match': result['candidate_manifest_files_all_match'],
                  'state_checks': result['all_mapped_feature_state_checks_pass'],
                  'binding_checks': result['all_mapped_feature_document_batch_bindings_pass'],
                  'findings': [{'id': finding['id'], 'severity': finding['severity']}],
                  'results': str(OUT / 'cc-catalog-full-results.json')}, ensure_ascii=False, indent=2))
