"""Build a bounded handoff delta. Reads inputs; writes only this task directory.

No reference execution, Git mutation, publication, or remediation is performed.
"""
from pathlib import Path
import copy
import hashlib
import json
import re
import subprocess

TASK = Path(__file__).resolve().parent
RR = TASK.parent.parent
REPO = RR.parents[2]
OLD = RR / 'evidence/external-recovered/handoff_preparation_cloud/5caff3bd1a1b062b48b7eda46777a614921946f3'
OLD_COMMIT = '5caff3bd1a1b062b48b7eda46777a614921946f3'
B8 = 'fd1df570cad987dc3852a3b958f03916e317f7fe'
R = '8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
FORMAL = 'deliverables/final-specification-set/'
STATE = 'READY_PENDING_ROOT_CORE_FREEZE'

def read(path):
    return json.loads(path.read_text())

def dump(path, obj):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2) + '\n')

def identity(path, purpose):
    b = path.read_bytes()
    return {'repo': str(REPO), 'commit': None, 'tree': None,
            'commit_binding': 'PENDING_ACTUAL_ENCLOSING_ROOT_PUBLICATION; exact content identity below, not a future Git identity',
            'path': str(path.relative_to(REPO)), 'mode': '100644', 'bytes': len(b),
            'sha256': hashlib.sha256(b).hexdigest(),
            'blob': hashlib.sha1(b'blob ' + str(len(b)).encode() + b'\0' + b).hexdigest(),
            'purpose': purpose}

def ref(path):
    return str(path.relative_to(RR))

roots = read(RR / 'adjudication/root-decisions.partial.json')
old_records = read(OLD / 'handoff/contracts.zh.json')
old_batches = read(OLD / 'handoff/batch-assignment.json')['batches']
old_manifest = read(OLD / 'handoff/cloud-eighth-update-handoff-manifest.json')
assert len(roots['records']) == 38
assert roots['bounded_counts'] == {'required': 29, 'required_P2': 2, 'required_P3': 27, 'optional': 9}
assert [(x['id'], x['classification'], x.get('severity')) for x in roots['records'][:33]] == [
    (x['id'], x['classification'], x.get('severity')) for x in old_records]

root_names = [
    'root-wp31-unknown-note-reception.v1.json',
    'root-cp002-faint-audio-bounded-adjudication.v1.json',
    'root-shadow-type-legacy-optional-adjudication.v1.json',
    'root-cp01-end-mark-optional-adjudication.v1.json',
    'root-mg-name-escape-required-adjudication.v1.json',
]
new_ids = [x['id'] for x in roots['records'][33:]]
wp31, faint, shadow, endmark, mg = new_ids
wp67_path = FORMAL + 'user-interface/wp67-a-battle-interaction-and-presentation.md'
wp64_path = FORMAL + 'creature-rpg/wp64-mail-and-mystery-gift.md'
catalog_path = FORMAL + 'test-catalog/creature-rpg-wp35-36-57-64-68.md'
wp31_path = FORMAL + 'pokemon-rules/wp31-basic-evolution.md'
shadow_path = FORMAL + 'pokemon-rules/wp23-shadow-data-and-vectors.md'
primary = {faint: 'R8-U06', mg: 'R8-U09'}
optional_primary = {'GR8-UI-001': 'R8-U01', 'GR8-AI-002': 'R8-U06',
                    'GR8-HIST-U12-RECEIPT-SCOPE-001': 'R8-U07',
                    'GR8-UI-003': 'R8-U09', 'GR8-EXT-CD-004': 'R8-U09',
                    'GR8-EXT-CD-003': 'R8-U09', wp31: 'R8-U09', shadow: 'R8-U09', endmark: 'R8-U06'}
conditional_paths = {
    'GR8-UI-001': [FORMAL + 'user-interface/wp65-title-load-options-pause-and-pc.md'],
    'GR8-AI-002': [FORMAL + 'combat-requirements/wp52-a-generic-numerical-and-status-evaluation.md'],
    'GR8-HIST-U12-RECEIPT-SCOPE-001': ['review/remediation-eighth-20261016-prepare/navigation/current-r7-metadata-qualification.json'],
    'GR8-UI-003': [FORMAL + 'user-interface/wp66-a-party-and-summary-ui.md'],
    'GR8-EXT-CD-004': [FORMAL + 'pokemon-rules/wp34-inheritance-and-offspring.md'],
    'GR8-EXT-CD-003': [FORMAL + 'creature-rpg/wp26-acquisition-gifts-and-script-trade.md'],
    wp31: [wp31_path], shadow: [shadow_path], endmark: [wp67_path],
}

common_roles = {
    'author_requested': {'model': 'gpt-6.1-sol', 'effort': 'xhigh', 'tier': 'default', 'speed': 'normal', 'Fast': 'off'},
    'reviewer_requested': {'model': 'gpt-6.1-sol', 'effort': 'ultra', 'tier': 'default', 'speed': 'normal', 'Fast': 'off'},
    'actual': {k: 'UNVERIFIED' for k in ['model', 'effort', 'tier', 'speed', 'Fast']},
    'actual_author_and_reviewer_task_ids': 'NOT_STARTED',
    'independence': '后续实际非作者审查候选及最终整合受影响全文；逻辑角色改名不创造独立性。',
}
new_records = []
for i, name in enumerate(root_names):
    raw = read(RR / 'adjudication' / name)
    if 'record' in raw:
        contract = copy.deepcopy(raw['record']['complete_semantic_contract_received'])
    else:
        contract = copy.deepcopy(raw['complete_semantic_contract'])
    cur = roots['records'][33 + i]
    if cur['id'] == wp31:
        contract['minimal_revision_contract']['preserve'][0] = '固定R的64个独立注册身份、原52手工意义分组、五wrapper、None/prevo和首成功规则全部保留；52不是注册身份数量。'
    record = {
        'id': cur['id'], 'classification': cur['classification'], 'severity': cur.get('severity'),
        'classification_authority': {'path': 'adjudication/root-decisions.partial.json', 'pointer': f'/records/{33+i}'},
        'root_contract': identity(RR / 'adjudication' / name, '完整有限根裁决；保留原反证与历史链'),
        'complete_contract': contract,
        'operation': {
            'state': STATE, 'selected': cur['classification'] == 'required',
            'unique_primary_batch': primary.get(cur['id']),
            'conditional_batch_if_user_selects': optional_primary.get(cur['id']),
            'roles': copy.deepcopy(common_roles),
            'direct_semantic_required_ids': [], 'transitive_semantic_required_ids': [],
            'candidate_writer': primary.get(cur['id'], optional_primary.get(cur['id'])),
            'actual_target_writer': 'R8-INTEGRATOR',
            'release_gate': 'root core及全历史/接口接收冻结，后继真实enclosing commit与core绑定，再由用户手动启动；optional须另行选择。',
            'acceptance_gates': ['candidate PASS', 'actual integrated PASS', 'ACCEPTED', 'CLOSED'],
            'business_execution': 'NOT_EXECUTED', 'update_started': False,
        },
    }
    record['operation']['mandatory_target_write_set'] = {faint: [wp67_path], mg: [wp64_path, catalog_path]}.get(cur['id'], [])
    record['operation']['conditional_target_write_set'] = conditional_paths.get(cur['id'], [])
    record['operation']['candidate_mirror_prefix'] = 'review/remediation-eighth-20261016-prepare/candidates/' + record['operation']['candidate_writer'] + '/mirror/'
    new_records.append(record)
dump(TASK / 'handoff/contracts.delta.zh.json', {'schema': 'r8-five-complete-operative-contracts/v1',
     'status': STATE, 'WP31_count_qualification': identity(RR / 'adjudication/mandatory-wp31-registered-identity-count-qualification.v1.json', '原9102B合同保留；本有效合同已修正64身份/52意义分组'),
     'records': new_records, 'new_classification_votes': 0, 'update_started': False})

batches = copy.deepcopy(old_batches)
for batch in batches:
    bid = batch['id']
    for rid, pb in primary.items():
        if pb == bid:
            batch['required_ids'].append(rid)
    batch['optional_ids_if_later_selected'] = [rid for rid, pb in optional_primary.items() if pb == bid]
    batch['selected_optional_ids'] = []
    batch['conditional_target_write_set_by_id'] = {rid: conditional_paths[rid] for rid in batch['optional_ids_if_later_selected']}
    batch['inherited_complete_prompt'] = identity(OLD / f'handoff/batches/{bid}/prompt.md', '原批次全文固定保留；受本有效共同门与增量条款限定')
    batch['inherited_complete_readset'] = identity(OLD / f'handoff/batches/{bid}/readset.json', '原完整必要读集，不以本索引替代实读')
    batch['inherited_semantic_scope'] = '全部原required合同七组、反例、preserve、验收、回归及共同前提原文保留；旧33计数/core/pending状态由本补充和root最终事实取代。'
    batch['R8_core'] = STATE
    batch['input_contract_commit'] = None
    batch['input_commit_rule'] = '原40f45...仅为历史准备输入；执行前绑定实际包含本补充与根最终报告的enclosing commit，不伪造未来hash。'
    batch['state'] = 'PLANNED_NOT_STARTED'
    batch['current_launch_blocker'] = STATE + '; UPDATE_NOT_STARTED'
    batch['author']['actual_configuration'] = copy.deepcopy(common_roles['actual'])
    batch['reviewer']['actual_configuration'] = copy.deepcopy(common_roles['actual'])
    if bid == 'R8-U06':
        batch['title'] = '战斗主合同、成长/AI共享目录与固定濒死音频请求'
        batch['additional_contract_ids'] = [faint]
        batch['optional_additional_contract_ids'] = [endmark]
        batch['additional_read_requirement'] = '完整CP002根合同和exact-inputs所有必要完整定义/条款；WP67-A受影响全文、WP15音频/长度、WP16调度、WP74§1、BT K01–K59；CP01仅选择后接收其完整合同、K34与两胜利/失败控制。'
        batch['file_ownership_note'] = 'WP67-A整文件候选唯一writer R8-A-R8-U06，同时接收旧COM同步与新CP002；CP01可选仅用户选择后纳入，根因独立；固定视觉政策未选不纳入。'
    elif bid == 'R8-U09':
        batch['title'] = '固定蛋群作者接受域与CreatureE礼物命名输入'
        batch['additional_contract_ids'] = [mg]
        batch['optional_additional_contract_ids'] = [wp31, shadow]
        batch['actual_target_write_set'] += [wp64_path, catalog_path]
        batch['candidate_write_set'] += [batch['candidate_mirror_prefix'] + p for p in [wp64_path, catalog_path]]
        batch['additional_read_requirement'] = 'CreatureE子范围：完整MG根裁决/原候选/真实非作者反证/input ledger，WP64全文174、WP17全文319、共享Creature catalog全文183，MG25/MG29–32；MG Edit/Create/Manage/显示、自由文本/消息包装、TextEntry、debug真实入口完整具名单元；继承EggGroup全部共同前提和source4–68含方法结束。'
        batch['file_ownership_note'] = 'WP64整文件候选唯一writer R8-A-R8-U09。共享Creature catalog的EG/EN/FC/TT/MG、Factory/Triad/E贡献由R8-INTEGRATOR整文件唯一正式集成；本批只在独占mirror提供MG32局部贡献及累计preserve，保持32条计数/原ID/别名前缀。'
        batch['shared_receivers'] += ['CreatureE/Mail/MysteryGift', 'WP17正确输入只读', 'Factory/Triad/E共享catalog单集成者']
    else:
        batch['additional_contract_ids'] = []
        batch['optional_additional_contract_ids'] = []
        batch['additional_read_requirement'] = '继承原批全文和原readset；本批无新增必修行为范围。'
        batch['file_ownership_note'] = '原候选独占mirror及R8-INTEGRATOR唯一正式writer分工保留。'
    batch['additional_contract_pointer'] = 'handoff/contracts.delta.zh.json#/records'
dump(TASK / 'handoff/batch-assignment.json', {'schema': 'r8-nine-batches-root38/v1', 'batches': batches,
     'one_required_one_primary': True, 'status': STATE, 'update_started': False})

records_index = []
for i, rec in enumerate(roots['records']):
    if i < 33:
        loc = {'path': ref(OLD / 'handoff/contracts.zh.json'), 'pointer': '/' + str(i)}
        batch = old_records[i]['primary_batch']
    else:
        loc = {'path': ref(TASK / 'handoff/contracts.delta.zh.json'), 'pointer': '/records/' + str(i-33)}
        batch = primary.get(rec['id'])
    records_index.append({'id': rec['id'], 'classification': rec['classification'], 'severity': rec.get('severity'),
                          'full_contract': loc, 'root_pointer': '/records/' + str(i),
                          'required_primary_batch': batch,
                          'conditional_batch_if_user_selects': optional_primary.get(rec['id']),
                          'optional_selected': False if rec['classification'] == 'optional' else None})
dump(TASK / 'handoff/records-index.json', {'schema': 'r8-effective-38-contract-index/v1',
     'classification_authority': identity(RR / 'adjudication/root-decisions.partial.json', '仅当前38条分类、严重度、全局边界及政策分列；不是本任务重做裁决'),
     'records': records_index, 'bounded_counts': roots['bounded_counts'],
     'qualification': roots['counts_qualification'], 'status': STATE, 'update_started': False})

graph = copy.deepcopy(read(OLD / 'handoff/dependency-graph.json'))
graph['schema'] = 'r8-dependency-graph-root38/v1'
graph['required_nodes'] += [faint, mg]
graph['semantic_edit_edges'] = []
graph['transitive_closure_edit_edges'] = []
graph['common_release'] = 'root全局core/history/interfaces冻结并后继实际enclosing commit绑定；用户另行手动启动；不是当前HEAD或原准备commit。'
graph['additional_closure_edges'] = [
    {'from': mg, 'to': 'R8-INTEGRATOR', 'kind': 'MG32/shared-Creature-catalog-whole-file-reception',
     'blocking': 'MG实际整合/接受/关闭；不阻独立候选准备', 'preserve': 'Factory/Triad/E的EG/EN/FC/TT/MG、32计数/原ID/别名前缀'},
    {'from': faint, 'to': 'R8-INTEGRATOR', 'kind': 'WP67-A-whole-file-reception',
     'blocking': '该根实际整合/接受/关闭', 'preserve': '旧COM同步、CP01未选、视觉policy未选'},
]
graph['first_wave_after_common_release_count'] = 9
graph['currently_startable_count'] = 0
graph['currently_startable'] = []
graph['optional_selection'] = {rid: 'UNSELECTED; 未选择不阻required关闭' for rid in optional_primary}
graph['independent_policy'] = {'id': 'GR8-POL-FIXED-BATTLE-VISUAL-FIDELITY-001', 'selection': 'UNSELECTED', 'required_write_set': [], 'optional_counted_write_set': [], 'blocking': '仅将来实际选择并依赖该视觉精度的范围'}
dump(TASK / 'handoff/dependency-graph.json', graph)

conflicts = copy.deepcopy(read(OLD / 'handoff/file-conflict-graph.json'))
conflicts['schema'] = 'r8-file-conflicts-root38/v1'
wp67_existing = [x['id'] for x in old_records if wp67_path in x['seven_groups']['4_最小修订合同']['required_target_write_set']]
conflicts['new_record_edges'] = [
    {'from': rid, 'to': faint, 'paths': [wp67_path], 'resolution': 'U06整文件唯一候选writer；R8-INTEGRATOR唯一正式writer'} for rid in wp67_existing]
conflicts['new_record_edges'].append({'from': faint, 'to': endmark, 'paths': [wp67_path],
     'conditional': '仅CP01被用户选择时', 'resolution': '同U06单writer，根因独立，optional未选不得改'})
for p in [wp64_path, catalog_path]:
    conflicts['actual_file_writers'].append({'path': p, 'candidate_batch': 'R8-U09', 'actual_writer': 'R8-INTEGRATOR'})
conflicts['shared_Creature_catalog'] = {'path': catalog_path, 'actual_writer': 'R8-INTEGRATOR',
     'candidate_contribution_batch': 'R8-U09', 'producer_domains': ['CreatureE/Mail/MG', 'Factory', 'Triad', 'EG/EN/FC/TT existing owners'],
     'rules': '正式整文件唯一writer；贡献者不直接写target。MG32输入改为删空RETURN+确认，邻接已有非空名ESCAPE成功；保32条及原ID/别名前缀和其它域。无新required语义边。'}
conflicts['conditional_optional_writers'] = [
    {'id': rid, 'candidate_batch': optional_primary[rid], 'actual_writer': 'R8-INTEGRATOR', 'paths': paths, 'selection': 'UNSELECTED'}
    for rid, paths in conditional_paths.items()]
conflicts['fixed_visual_policy_write_set'] = []
dump(TASK / 'handoff/file-conflict-graph.json', conflicts)

policy_file = RR / 'adjudication/root-cp-ir012-visual-fidelity-policy-disposition.v1.json'
dump(TASK / 'handoff/policy-and-preservation.json', {
    'schema': 'r8-unselected-policy-and-preservation/v1',
    'independent_policy': {'id': 'GR8-POL-FIXED-BATTLE-VISUAL-FIDELITY-001', 'classification': 'independent_policy',
       'selection': 'UNSELECTED', 'root': identity(policy_file, '完整八节独立视觉精度政策；保持未选择'),
       'scope': '固定球/释放/捕获/派出/排列等可读参数已归真实有限接收；纯视觉精度由用户将来选择，现无formal写集。CP002有限音频required独立保留。',
       'required_count_contribution': 0, 'optional_count_contribution': 0, 'write_set': []},
    'separate_no_required': roots['separate_bounded_no_required_reception'],
    'inherited_eight_full_records': {'path': ref(OLD / 'handoff/cloud-eighth-update-handoff-manifest.json'), 'pointer': '/separate_no_required'},
    'additional_full_receipts': [identity(RR / 'adjudication' / n, '有限NO_REQUIRED；无整改batch，不升级全局NO_REQUIRED_UPDATE') for n in [
        'root-recorded-debug-skip-scope-no-required.v1.json', 'root-participation-update-scope-no-required.v1.json',
        'root-weather-expiry-message-order-no-required.v1.json', 'root-hist-c2-001-no-required.v1.json']],
    'additional_navigation_receptions': roots['additional_bounded_scope_no_required_receptions'],
    'binary_negative': {'path': ref(OLD / 'handoff/cloud-eighth-update-handoff-manifest.json'), 'pointer': '/separate_binary_negative', 'count': 4},
    'original_UI002': {'classification': 'REJECTED', 'write_set': [], 'meaning': '原nil &异常反例已撤，不计required/optional，不自动替换新finding。'},
    'evidence_corrections': {
        'WP31': '64独立注册身份；52只为手工意义分组；原9102B裁决原字节留存，实际执行用修正伴件。',
        'MG32': '仅MG31明确空文确认；MG32原只写命名取消。原候选不覆写，本必修精确澄清MG32输入；对象副作用预期仍保留。',
        'PC_F033': 'trigger true不自动reset；grace可能已经增加step_count，不能改写为两计数始终不改变。现WP36正确，非新finding。',
        'startup_impact': '原35项的20模块门/15精度追溯只限其原分母，不外推38；无全局架构clearance/TS授权。',
        'inherited': {'path': ref(OLD / 'handoff/cloud-eighth-update-handoff-manifest.json'), 'pointer': '/evidence_corrections'},
    }, 'L01_L14': '原范围按全局合同及最终root执行/材料台账接收；本任务新增业务运行0。可得未读不得标limit。',
    'status': STATE, 'update_started': False,
})

shared_text = f'''状态 {STATE}，UPDATE_NOT_STARTED，update_started:false。本提示词供用户在root实际冻结/后继发布绑定后手动派发；目前已启动整改0。B8={B8}，R={R}。项目 /workspace/pokemon-essentials-clean-room；R /workspace/pokemon-essentials 只读。

当前唯一分类依据是 adjudication/root-decisions.partial.json 的38条有限记录：29 required（2P2/27P3）与9 optional；另1独立视觉政策UNSELECTED，12有限NO_REQUIRED与4 binary负例分列，UI002原候选撤销。不是全轮最终总数。原33合同分类/严重度全保持；新5条见本包 contracts.delta.zh.json。全部9个optional保持未选择。旧合同中已解决的pending提案、33计数和WIP身份仅留历史，执行以本有效索引及root最终绑定为准。

完整读取 AGENTS.md、inputs/eighth-global-review-prompt.md、inputs/review-SKILL.md，以及本批固定引用的原prompt全文/原readset全部必要条款、对应contracts七组和新增根完整合同；精确重复内容可核等后关联去重，所有独有语义都须实读。索引、哈希、旧PASS和脚本不能代替实读。原包固定交付 {OLD_COMMIT}，恢复目录 {ref(OLD)}；原任务远端路径为该报告根/tasks/handoff_preparation_cloud/。原33全文不缩成摘要。

执行前，由root的真实后继发布入口提供最终语义core commit/tree、实际包含本补充和最终报告的enclosing commit以及逐文件身份。现有HEAD、旧40f45...、原准备5caff...都不是未来最终core；本包core/enclosing字段保持空。核对实际提供的commit、tree、path/mode/blob/bytes/SHA后才使用。共同门满足后9批隔离mirror可独立准备，9是逻辑批数，不代表slots；当前可启动0。

作者请求gpt-6.1-sol/xhigh，真实非作者reviewer请求gpt-6.1-sol/ultra；均default普速、normal、Fast off。actual model/effort/tier/speed/Fast无权威echo逐字段UNVERIFIED，实际作者/审者ID尚NOT_STARTED。CLI/Desktop启动方法未实际测试，UNVERIFIED；用户手动建立实际context并粘贴本批入口，不编造flags或任务ID。

候选作者只写本批mirror及独立证据，不直接写正式target。所有正式文件、公共planning/audit索引、共享目录及台账由R8-INTEGRATOR唯一写者逐贡献整合；仅同步实际受影响行，不扩大整表重写。候选PASS、actual整合PASS、ACCEPTED、CLOSED四门分列；最终actual审者须实际不同于作者、全文接收受影响结果与累计保留。文件冲突是写权/接收门，不自动变成根因语义先后依赖。

采用最终态文档修订：错误原位替换、必要缺项补齐、正确scope保留；原提案/反证/撤销按原字节留审计。不改R、不开发框架、不复制源码或Ruby架构、不选择未选optional/policy、不合并main。SOURCE_STATIC/DERIVED_VECTOR与TOOL_VALIDATION/真实执行分列，本准备新增业务/游戏/宿主/编译/行为模型/向量运行0，NOT_EXECUTED，不用运行未知豁免可得条款。
'''

delta_snippets = {
    'R8-U06': '''本批新增必修 GR8-UI-FAINT-AUDIO-001（alias GR8-EXTCP-002），WP67-A§9.3为唯一owner。完整合同见contracts.delta.zh.json#/records/1：固定正常前提下专用_faint优先（形态再基础），普通回退音高75且长度同音高，20调度单位/秒向上取整后+2；两资源都缺基础10再+2，仍有独立Pkmn faint音效。给定1秒静态夹具三分支22/29/12；已选资源0长为2。成员与框并发推进，聚合另次观察完成，数字不是墙钟或总阻塞时长。保effectsOff仍播、HP先写、异常无统一回滚。WP15/WP16正确通用规则只读，不强制新文件/ID；必要向量可用现有BT场景，若改catalog必须由唯一writer接收。

GR8-UI-BATTLE-END-MARK-001（CP01-C01）只在用户选择后纳入同一WP67-A writer；完整合同records/3。仅局部括号统一两胜利入口先置mark再BGM，普通失败/平局不置。胜利无输入等待，失败/平局全显后开始计时，首次正常访问elapsed>=3秒条件时关闭；不承诺精确墙钟3秒，不改正确§3.5/K34。该可选与CP002根因独立，固定视觉policy未选，无496字段/16RGB整表写集。''',
    'R8-U09': '''本批保原EggGroup固定15接受域合同及source4–68完整范围，新增CreatureE子范围 GR8-CRE-MG-NAME-CANCEL-001（MGE-CAND-NAME-ESCAPE），完整合同见contracts.delta.zh.json#/records/4。必改WP64§7相关句与共享Creature catalog MG32输入/邻近控制。

共同前提：固定R/B8、合法master G=[7,0,P,Gift]、有效非蛋PICHU、P.obtain_text=Mystery Gift、管理解码与在线空表正常、无插件/异常。主反例未Receive且P不与玩家共享。获得地先写Faraway place后，既有非空名Gift按ESCAPE返回原Gift并成功返回新tuple，Manage替换会话条目，无停止提示；Edit不写master/export/server。RETURN非空为普通成功；删空RETURN确认停止→nil/不替换但P已写保留，拒绝→重入；Create初空ESCAPE确认停止→nil；既有Gift删空再ESCAPE仍返回原Gift成功。各步骤按实际返回空/0决定停止确认，物理ESCAPE不是统一领域取消。

MG32原“命名取消”明确为删空RETURN+确认；同向量补非空原名ESCAPE成功对照。保MG25/MG29–32、副作用、32条计数、原ID和别名前缀；不新建测试ID。仅MG31原明确空文确认，原候选夸大MG32的证据更正不否定对象副作用。WP17公共输入正确只读；保获得地先写/不回滚、Receive别名、副本/会话/master/Export/在线四层、ID0哨兵/数量/异常范围。

共享Creature catalog全文包括EG/EN/FC/TT/MG及Factory/Triad/E贡献，R8-INTEGRATOR为整文件唯一正式集成者；本批在唯一mirror给MG32局部贡献，actual非作者全文接收累计结果，不因不同段落放开并发target写入。root-creature-e-task-final-acceptance.v1.json只表示有限审读完成，不授global freeze或B8合规。

可选WP31 unknown（records/0）及SHADOW legacy（records/2）均未选择。选择WP31才局部改两定位句，保64注册身份/52意义分组、Level/None/guard/首成功/BE01–37；未知作者枚举拒绝与绕编译坏数据可达查询分开。选择SHADOW才补可选Type样本特殊位，保默认未启用、逐招true物理/legacy false按有效SHADOW特殊及PP0，通用算法只读。原CD003/CD004/UI003可选同样须另行选择。''',
}

for batch in batches:
    bid = batch['id']
    original_prompt = batch['inherited_complete_prompt']
    original_readset = batch['inherited_complete_readset']
    text = f'# {bid} 完整有效派发入口\n\n' + shared_text
    text += '\n本批必修：' + '、'.join(batch['required_ids']) + '。\n'
    text += '\n固定保留全文：' + original_prompt['path'] + f"（{original_prompt['bytes']} bytes，SHA256 {original_prompt['sha256']}）。原完整读集：" + original_readset['path'] + f"（SHA256 {original_readset['sha256']}）。先读上述全文，再组合本入口及新增完整合同；任何引用材料缺失保持具体范围OPEN，不能将此入口单独当已完成阅读。\n"
    text += '\n' + delta_snippets.get(bid, '本批没有新增必修行为根。原完整逐项合同、普通/失败/取消/部分提交控制、preserve与验收原文继续有效；只更新共同分类、冻结/执行门和全局接收边界。') + '\n'
    text += '\n本批完整有效读写/角色/候选/actual分工：\n\n```json\n' + json.dumps(batch, ensure_ascii=False, indent=2) + '\n```\n\n'
    text += '输出候选变更、逐ID验收/回归与保留范围、精确输入与目标身份、实读台账、失败/未知边界、共享贡献接收状态；作者不得自签actual最终验收。UPDATE_NOT_STARTED。\n'
    p = TASK / f'handoff/batches/{bid}/prompt.md'
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text)

index_prompt = '# 第八轮38条有限裁定：完整有效人工整改handoff索引\n\n' + shared_text
index_prompt += '\n完整合同按records-index.json逐ID解析：原33条全文固定引用原contracts.zh.json对应对象，新5条全文位于contracts.delta.zh.json。逐项的source/spec完整身份、普通/最小反例、必要消费者、最小修订、read/write/preserve、验收、实际独立反证及历史链均按该全文接收；本索引不取代它们。\n\n'
index_prompt += '| ID | 当前分类 | 严重度 | 唯一必修批次／可选条件批次 |\n| --- | --- | --- | --- |\n'
for r in records_index:
    index_prompt += f"| {r['id']} | {r['classification']} | {r['severity'] or '原裁决未赋值'} | {r['required_primary_batch'] or r['conditional_batch_if_user_selects'] + '（未选）'} |\n"
index_prompt += '\n九批完整有效派发入口（共同release后候选第一波9，当前0）：\n\n'
for b in batches:
    index_prompt += f"- {b['id']}：{b['title']}；完整入口 handoff/batches/{b['id']}/prompt.md，原全文与原读集身份随入口固定。\n"
index_prompt += '\n'+delta_snippets['R8-U06']+'\n\n'+delta_snippets['R8-U09']+'\n'
index_prompt += '\n全局真实未封账项：root core/history/全域接口接收与全量分母；必须由root最终报告逐项签收。本准备只组合已裁38条，不产生新required/optional票，不能声明全轮PASS/全系统运行等价。独立视觉政策保持UNSELECTED，12有限NO_REQUIRED、4binary负例与UI002撤销分列在policy-and-preservation.json。旧35项startup-impact不自动外推38项、不构成TS授权。最终发布身份由外部后继实际commit绑定，无自身未来hash。\n\nUPDATE_NOT_STARTED\n'
(TASK / 'handoff/cloud-eighth-update-handoff-prompt.md').write_text(index_prompt)

# Prove repeated old prompt bodies are the exact serialized contract values already read.
master = (OLD / 'handoff/cloud-eighth-update-handoff-prompt.md').read_text()
section_matches = list(re.finditer(r'^## (GR8-[^\s]+) — .*$', master, re.M))
sections = {}
for i, m in enumerate(section_matches):
    stop = section_matches[i+1].start() if i+1 < len(section_matches) else len(master)
    candidate = master[m.start():stop]
    later = re.search(r'^## (?!GR8-)', candidate, re.M)
    if later:
        candidate = candidate[:later.start()]
    sections[m.group(1)] = candidate.strip()
prompt_proofs = []
for b in old_batches:
    body = (OLD / f"handoff/batches/{b['id']}/prompt.md").read_text()
    pos = body.index('\n## GR8-')
    dispatch = json.loads(body[:pos].split('## 本批独占合同\n\n', 1)[1])
    seen = body[pos:].removesuffix('\nUPDATE_NOT_STARTED\n').strip()
    expected = '\n\n'.join(sections[r['id']] for r in old_records if r['id'] in b['required_ids']).strip()
    # Exact whitespace can differ by one separator; compare each retained section independently.
    own_matches = list(re.finditer(r'^## (GR8-[^\s]+) — .*$', seen, re.M))
    equality = []
    for i, m in enumerate(own_matches):
        end = own_matches[i+1].start() if i+1 < len(own_matches) else len(seen)
        equality.append(seen[m.start():end].strip() == sections[m.group(1)])
    assert dispatch == b and all(equality) and len(equality) == len(b['required_ids'])
    prompt_proofs.append({'batch': b['id'], 'dispatch_exact_batch_assignment': True,
        'complete_required_contract_sections_exact_master': True, 'sections': len(equality),
        'only_batch_tail_addition': 'UPDATE_NOT_STARTED',
        'reading_qualification': '机械同文证明只支持去重定位；语义信用来自具名实际读者，非本校验生成。'})
dump(TASK / 'verification/original-prompt-dedup.json', {'schema': 'r8-inherited-prompt-exact-dedup/v1', 'proofs': prompt_proofs})

input_files = [RR/'inputs/eighth-global-review-prompt.md', RR/'inputs/review-SKILL.md', REPO/'AGENTS.md',
               RR/'adjudication/root-decisions.partial.json', policy_file,
               RR/'adjudication/mandatory-wp31-registered-identity-count-qualification.v1.json',
               RR/'adjudication/root-creature-e-task-final-acceptance.v1.json']
input_files += [RR/'adjudication'/n for n in root_names]
input_files += [RR/'delegation'/f'handoff-preparation-mandatory-supplement.v{i}.json' for i in range(1,5)]
input_files += [RR/'adjudication'/n for n in ['root-wp31-unknown-exact-inputs.v1.json', 'root-cp002-faint-audio-exact-inputs.v1.json',
    'root-recorded-debug-skip-scope-no-required.v1.json', 'root-participation-update-scope-no-required.v1.json',
    'root-weather-expiry-message-order-no-required.v1.json', 'root-hist-c2-001-no-required.v1.json',
    'root-encounter-counter-fact-clarification-reception.v1.json', 'ts-startup-impact-bounded.v1.md']]
input_files += [RR/'tasks/mg_name_escape_counterreview_cloud/input-read-ledger.json',
                RR/'tasks/mg_name_escape_counterreview_cloud/independent-counterreview.md',
                RR/'tasks/creature_e_mail_mystery_completion_cloud/mg-name-escape-candidate.v1.json',
                RR/'tasks/pbs_creature_current_cloud/shadow-type-legacy-flag-review-request.v1.json',
                RR/'tasks/creature_c_existing_crea/shadow-type-legacy-bounded-review.v1.json',
                RR/'tasks/pbs_creature_current_cloud/shadow-type-record-consumer.complete.v1.json',
                RR/'evidence/external-recovered/receive_external_combat_presentation/5ed44d1b3f0d024f1b6633348e1ea59ec488909d/integration/CP01-C01-counterreview.json']
input_files += [OLD/'handoff'/n for n in ['contracts.zh.json', 'cloud-eighth-update-handoff-prompt.md',
    'cloud-eighth-update-handoff-manifest.json', 'batch-assignment.json', 'dependency-graph.json', 'file-conflict-graph.json']]
input_files += list(sorted((OLD/'handoff/batches').glob('*/prompt.md'))) + list(sorted((OLD/'handoff/batches').glob('*/readset.json')))

# Bind finite source/spec input units without reproducing reference source.
units = []
def add_unit(info, ranges, owner, carrier):
    commit = info.get('commit')
    if commit not in [R, B8]:
        return
    path = info['path']
    repo = Path('/workspace/pokemon-essentials') if commit == R else REPO
    b = subprocess.check_output(['git', 'show', commit + ':' + path], cwd=repo)
    sha = hashlib.sha256(b).hexdigest()
    blob = hashlib.sha1(b'blob ' + str(len(b)).encode() + b'\0' + b).hexdigest()
    expected_sha = info.get('sha256', info.get('whole_blob_sha256'))
    expected_blob = info.get('blob', info.get('git_blob', info.get('content_git_blob')))
    if expected_sha:
        assert sha == expected_sha, (path, sha, expected_sha)
    if expected_blob:
        assert blob == expected_blob, (path, blob, expected_blob)
    units.append({'repo': str(repo), 'commit': commit,
        'tree': '7589c800b61ba13a13040ed0d686979b80a84fd0' if commit == R else '751dfde81048c81390f89a65ca1d1a565ba8e1ca',
        'path': path, 'mode': '100644', 'bytes': len(b), 'sha256': sha, 'blob': blob,
        'complete_unit_ranges_inclusive': ranges, 'contract_id': owner, 'identity_carrier': carrier,
        'current_task_credit': 'IDENTITY_BINDING_ONLY; future author/reviewer must actually read all required complete units and context; prior named-reader credit is not inherited'})

wp31_inputs = read(RR/'adjudication/root-wp31-unknown-exact-inputs.v1.json')
for k in ['all_eleven_contained_unit_integrity_only', 'extra_actual_root_reads']:
    for x in wp31_inputs[k]:
        add_unit(x, [x['range']], wp31, 'adjudication/root-wp31-unknown-exact-inputs.v1.json#/' + k)
for x in read(RR/'adjudication/root-cp002-faint-audio-exact-inputs.v1.json')['inputs']:
    add_unit(x, [[q['first'], q['last']] for q in x['ranges']], faint, 'adjudication/root-cp002-faint-audio-exact-inputs.v1.json#/inputs')
for x in read(RR/'tasks/mg_name_escape_counterreview_cloud/input-read-ledger.json')['entries']:
    add_unit(x, x['read_ranges_inclusive'], mg, 'tasks/mg_name_escape_counterreview_cloud/input-read-ledger.json#/entries')
shadow_inputs = read(RR/'tasks/pbs_creature_current_cloud/shadow-type-record-consumer.complete.v1.json')
for k in ['complete_source_units', 'complete_relevant_formal_units']:
    for x in shadow_inputs[k]:
        add_unit(x['identity'], [x['range']], shadow, 'tasks/pbs_creature_current_cloud/shadow-type-record-consumer.complete.v1.json#/' + k)
cp01_carrier = 'evidence/external-recovered/receive_external_combat_presentation/5ed44d1b3f0d024f1b6633348e1ea59ec488909d/integration/CP01-C01-counterreview.json'
for x in read(RR/cp01_carrier)['actual_independent_read_units']:
    add_unit(x, x['read_ranges'], endmark, cp01_carrier + '#/actual_independent_read_units')
add_unit({'commit': R, 'path': 'Data/Scripts/011_Battle/004_Scene/002_Scene_Initialize.rb'}, [[5,11]], endmark,
         'adjudication/root-cp01-end-mark-optional-adjudication.v1.json#/record/complete_semantic_contract_received/bidirectional_evidence/root_direct_whole_necessary_units')
dump(TASK/'handoff/source-spec-readset.delta.json', {'schema': 'r8-five-finite-source-spec-identities/v1',
     'units': units, 'source_code_copied': False, 'status': STATE,
     'future_read_rule': 'All complete units plus parent complete-contract readsets/context; source/unit identity does not grant this task source FULL_READ or renewed adjudication.',
     'inherited_33_complete_readsets': [b['inherited_complete_readset'] for b in batches], 'update_started': False})

manifest = {
    'schema': 'r8-complete-operative-handoff-root38-delta/v1', 'language': 'zh-CN', 'status': STATE,
    'B8': old_manifest['B8'], 'R': old_manifest['R'],
    'R8_core': {'status': 'OPEN_NOT_FROZEN', 'commit': None, 'tree': None},
    'enclosing_report_commit': None,
    'enclosing_commit_rule': 'root发布后继真实包含报告/本补充的commit；执行前外部绑定。禁止用观察HEAD/旧准备commit/自hash替代。',
    'observed_checkout_head_only': subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=REPO, text=True).strip(),
    'inherited_package': {'delivery_commit': OLD_COMMIT, 'recovered_root': ref(OLD),
       'original_task_path': ref(RR/'tasks/handoff_preparation_cloud'), 'files': 48, 'bytes': 12597957,
       'rule': '原48文件不可变；按精确身份引用全文/证据，无重复复制12MB。'},
    'classification_source': identity(RR/'adjudication/root-decisions.partial.json', '唯一当前分类依据'),
    'bounded_counts': roots['bounded_counts'], 'records': records_index,
    'policy_count': 1, 'policy_selection': 'UNSELECTED', 'optional_selected_count': 0,
    'full_contract_resolution': {'inherited_33': ref(OLD/'handoff/contracts.zh.json'), 'new_5': ref(TASK/'handoff/contracts.delta.zh.json')},
    'input_payloads': [identity(p, '固定输入/完整继承载荷/精确可恢复证据；读取信用见reading-ledger.json，身份不授阅读') for p in input_files],
    'new_source_spec_readset': 'handoff/source-spec-readset.delta.json',
    'dependency_graph': 'handoff/dependency-graph.json', 'file_conflict_graph': 'handoff/file-conflict-graph.json',
    'batch_assignment': 'handoff/batch-assignment.json', 'batch_count': 9,
    'first_wave_after_release_count': 9, 'currently_startable_count': 0,
    'common_roles': common_roles, 'all_actual_formal_writers': 'R8-INTEGRATOR',
    'semantic_edit_edges': [], 'transitive_semantic_edit_edges': [],
    'shared_catalog': {'path': catalog_path, 'writer': 'R8-INTEGRATOR', 'vector_count': 32,
       'preserve': '原32条计数、ID、别名前缀及EG/EN/FC/TT/MG和Factory/Triad/E其它域；MG32输入及邻近控制最小同步。'},
    'history_and_independence': '原33分类/严重度全保持；五根取root已有裁决与真实非提出者链，不新投票。全历史canonical/alias去重和全局接口/core由root最终封账。',
    'execution': {'new_business_runs': 0, 'reference_game': 'NOT_EXECUTED', 'host': 'NOT_EXECUTED',
       'compiler': 'NOT_EXECUTED', 'behavior_model': 'NOT_EXECUTED', 'vectors': 'NOT_EXECUTED',
       'package_tools': 'JSON/集合/精确同文/身份核验，只授TOOL_VALIDATION'},
    'protected': '仅tasks/handoff_final_five_root_deltas/写入；Git/index/source/formal/planning/audit/旧报告及其它任务不改。',
    'remaining': 'remaining.md', 'update_started': False, 'final_marker': 'UPDATE_NOT_STARTED',
}
dump(TASK / 'handoff/cloud-eighth-update-handoff-manifest.json', manifest)
print(json.dumps({'status': STATE, 'records': len(records_index), 'new_complete_contracts': len(new_records),
                  'counts': roots['bounded_counts'], 'batches': len(batches), 'original_prompt_dedup_proofs': len(prompt_proofs)}, ensure_ascii=False))
