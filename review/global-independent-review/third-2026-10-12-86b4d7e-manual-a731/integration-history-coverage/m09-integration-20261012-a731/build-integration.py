"""Finite metadata/semantic join serializer. Never executes reference behavior."""
import collections
import csv
import json
import pathlib
import re

ROOT = pathlib.Path('/Users/dingshinn/Desktop/pokemon-framework-reference')
BASE = ROOT / 'review/global-independent-review/third-2026-10-12-86b4d7e-manual-a731'
OUT = pathlib.Path(__file__).parent
OLD = ROOT / 'review/remediation/20261003-prepare/FINAL-1/independent-review-cloud-20261011-1'
FINAL_COMMIT = 'c2bc1a341ba6acdf7c8c111dc88d39a162a093d6'
CURRENT_SPEC = '167296dbe9e2384627b0ed696e87aeb01f211252'

def jread(p):
    return json.loads(p.read_text())

def tread(p):
    with p.open(newline='') as f:
        return list(csv.DictReader(f, delimiter='\t'))

def write(name, obj):
    (OUT / name).write_text(json.dumps(obj, ensure_ascii=False, indent=2) + '\n')

def rel(p):
    return str(p.relative_to(ROOT))

def rows_from(d):
    if isinstance(d, list):
        return d, ''
    for k in ['records', 'historical_controls_consumed', 'controls']:
        if isinstance(d.get(k), list):
            return d[k], '/' + k
    raise ValueError('No record array')

def paths_from(obj):
    """Navigation paths only; no inferred semantic support from path matching."""
    s = json.dumps(obj, ensure_ascii=False)
    return sorted(set(re.findall(r'(?:deliverables/final-specification-set|specs|review|audit)/[^\s\"\|;]+?\.(?:md|tsv|json)', s)))

modules = {}
control_pool = collections.defaultdict(list)
cap_index = {}
source_pool = collections.defaultdict(list)
spec_pool = collections.defaultdict(list)
assigned_spec_owners = collections.defaultdict(set)
results = {r['module']: r for r in jread(BASE / 'module-results.json')}
for n in range(1, 13):
    m = f'M{n:02}'
    p = BASE / m
    reg, regprefix = rows_from(jread(p / 'regression-review.json'))
    caps, files, specs = (tread(p / f'{k}-coverage.tsv') for k in ['capability', 'file', 'spec'])
    for i, r in enumerate(reg):
        control_pool[r['id']].append((m, i, regprefix, r))
    for i, r in enumerate(caps):
        cap_index[r['capability_id']] = {'module': m, 'row_1based': i + 1, **r}
    for i, r in enumerate(files):
        key = r['source_path'].removeprefix('reference/pokemon-essentials/')
        source_pool[key].append({'module': m, 'row_1based': i + 1, **r})
    for i, r in enumerate(specs):
        spec_pool[r['spec_path']].append({'module': m, 'row_1based': i + 1, **r})
    for r in jread(p / 'assigned-specs.json'):
        assigned_spec_owners[r['path']].add(m)
    modules[m] = {'reg': reg, 'regprefix': regprefix, 'caps': caps, 'files': files,
                  'specs': specs, 'junction': (p / 'junction-review.md').read_text(),
                  'assigned_junctions': tread(p / 'assigned-junctions.tsv'),
                  'task': results.get(m, {}).get('task', m)}

for r in jread(BASE / 'root-assigned-specs.json'):
    assigned_spec_owners[r['path']].add('ROOT')
for i, r in enumerate(tread(BASE / 'root-spec-coverage.tsv')):
    spec_pool[r['spec_path']].append({'module': 'ROOT', 'row_1based': i + 1, **r})
unique_module_control_ids = len(control_pool)

identity_checks = jread(BASE / 'regression-identity-checks.json')
regnav = tread(BASE / 'regression-229.tsv')
oldregs, _ = rows_from(jread(OLD / 'all229-dispositions.json'))
old_by_id = {r['id']: (i, r) for i, r in enumerate(oldregs)}
accepted = jread(BASE / 'accepted-341-scope.json')['full_mapping']
oldjunction = jread(OLD / 'junction-chain-review.json')
canonical_junction_rows = tread(ROOT / 'review/remediation/20261003-prepare/wp78-junction-successor.tsv')
canonical_junction_by_id = {r['junction_id']: r for r in canonical_junction_rows}
formal = jread(BASE / 'formal-spec-identities.json')
formal_by_path = {r['path']: r for r in formal}
reference = tread(BASE / 'reference-file-inventory.tsv')

common = {
    'reviewer_task': '/root/m09_ai_facilities_v3',
    'integration_scope': 'Finite independent integration helper; root owns canonical adjudication. Original M09 products frozen.',
    'delivery': {'commit': '86b4d7e1d8645e75af91a215240f8786a5bb4ca8', 'tree': '42c29efb5422772a1d90f657f25983600f500f28'},
    'formal': {'commit': CURRENT_SPEC, 'tree': '33598d8a2a3acdd093cc4fe23f48eea8666100f3'},
    'reference': {'commit': '8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b', 'tree': '7589c800b61ba13a13040ed0d686979b80a84fd0'},
    'model_requested': 'gpt-6.1-sol/ultra/Standard(default)', 'effective_echo': 'UNVERIFIED',
    'identity_verification_reused': rel(BASE / 'regression-identity-checks.json'),
    'identity_is_not_semantic_pass': True,
    'execution': {'reference_runtime': 0, 'behavior_cases': 0, 'static_cases': 0, 'simulator': 0, 'deserialization': 0, 'demo': 0},
    'historical_state_unchanged': True, 'old_signature_transferred': False,
    'method': 'Read current reports/junctions/capability evidence and scoped regression fields; join exact original/approved/FINAL1 identities and exact batch/ID/candidate/ACT/reviewer tuples. Preserve source/spec row status and limits. No recursive historical re-review or whole-ID acceptance inferred from a receipt.'
}

ISSUES = {
 'IHC-001': {'kind': 'HISTORICAL_EVIDENCE_REUSE_CORRECTION', 'target': 'G2-5',
             'excluded': 'Mining explicitly reseeds', 'current': 'Lottery date seeding and dungeon generation reseeding are distinct. Mining/Tile ordinary randomness does not explicitly seed.',
             'evidence': 'M11-C79/C81/C85; M03 dungeon query family; M09 recording random channel; WP06/WP70/WP58.', 'new_formal_finding': False},
 'IHC-002': {'kind': 'HISTORICAL_EVIDENCE_REUSE_CORRECTION', 'target': 'G6-5;CHAIN-2',
             'excluded': 'single-plant qty8/10/12 gives statistical increments2/3/3',
             'current': 'Confirmed whole quantity/capacity then total plant harvest+1. Separate maximum-yield harvest+1 when qty>=that berry maximum. Ordinary plant yield does not exceed maximum; direct helper threshold remains >=.',
             'evidence': 'M11-C32; BerryPlants reference423–458, specifically450–452; WP60 berry plants §5–6.', 'new_formal_finding': False},
 'IHC-003': {'kind': 'HISTORICAL_EVIDENCE_REUSE_CORRECTION', 'target': 'GIR-FD82-A022;CHAIN-5',
             'excluded': 'FINAL1 neighboring_reverse withMoves=false skips creation form callback',
             'current': 'withMoves controls move initialization. Creation form callback is independently gated by recheck_form and initial zero form; false withMoves alone does not skip it.',
             'evidence': 'M04 regression-review explicit_reuse_exclusions/current WP18/WP21/CI03; root independent source recheck.', 'new_formal_finding': False},
 'IHC-004': {'kind': 'HISTORICAL_EVIDENCE_REUSE_CORRECTION', 'target': 'GIR-FD82-A059;CHAIN-8',
             'excluded': 'FINAL1 neighboring_reverse no remembered Q sets timer',
             'current': 'No remembered Q cancels an existing pending timer; it does not create the remembered-Q timed branch. Preserve selection/play/wait/clear separation.',
             'evidence': 'M05 regression-review explicit_reuse_exclusions; WP24/PT58; root exact consumer recheck.', 'new_formal_finding': False},
 'IHC-005': {'kind': 'JOIN_QUALIFICATION', 'target': 'G5-1',
             'current': 'Wild music gate is before internalBattle/experience early return. The later gate suppresses EV/EXP distribution, not that prior music side effect.',
             'evidence': 'M07 current junction/capability; M06 battle distribution handoff.', 'new_formal_finding': False},
 'IHC-006': {'kind': 'HISTORICAL_STAGE_QUALIFICATION', 'target': 'G9-3;GIR-FD82-001;WP80-INTAKE-C01',
             'current': 'FINAL1/old B21 prose at its frozen stage is not current canonical status; final closure is a separately identified event. Count111/18/2 and341/229 does not prove quality or runtime.',
             'evidence': 'Current root-spec-coverage; final-integration-review5/643; fixed closure identities.', 'new_formal_finding': False},
 'IHC-007': {'kind': 'NAVIGATION_OWNERSHIP_GAP_RESOLVED_WITH_FINITE_JOIN', 'target': 'WP80-INTAKE-C01',
             'current': 'Initial assigned_modules empty; no module regression row. Integration independently consumes complete effective FINAL1 statistical control and reads current errata/count statements; 131-file classified recount supplies current evidence.',
             'evidence': 'historical-errata126/145; original completion8–9/24 (historical errors retained); final-integration5/643; formal131 identities.', 'new_formal_finding': False},
 'IHC-008': {'kind': 'NAVIGATION_OWNERSHIP_GAP_RESOLVED_WITH_FINITE_JOIN', 'target': 'G9-3',
             'current': 'No assigned domain-junction row; ROOT management-stage scope explicitly joined here through root formal coverage, identity checks and separately frozen approval/ACT/closure states.',
             'evidence': 'root-spec-coverage; final-integration-review5/643; baseline/regression-identity-checks; exact FINAL1 and closure identities.', 'new_formal_finding': False}
}

# Independent current integration judgments. These are behavioral prose, not copied source.
# ID | normal | failure/boundary | relevant findings | qualifiers
FACTS_TEXT = '''
G1-1|顶层小写.txt按最长合法基名及下划线后缀发现；发现列表交给普通编译入口。|大写扩展名、子目录、备份目录不自动进入；发现成功不证明转换/编译成功。|GR3-M01-003|目录名单全量与内容语义/启用分开。
G1-2|Gen5–8四目录各九文本存在；Shadow四文本和131量表/招式样本已由M04全文对照。|可选备份没有实际启用证据；目录发现不等于生效或全变体内容审查。||U06及Gen5–8未读内容保留。
G1-3|显式名单字段选择Trainer/Pokemon/Challenges；默认及四杯单打名单有具名加载消费者。|Fancy两份non_single未引用；缺规则名单不能由文件存在推导加载成功。|GR3-M12-002|当前累计场次缺口在下游生成器，不抹掉名单资格数据。
G1-4|通用注册表、Encounter版本回退、Trainer三元身份与Phone默认/训练家/NPC入口分列。|Encounter存在性查询不等于get回退；PhoneDefault重复节后覆盖是通用重复拒绝例外。|GR3-M01-004|每种数据身份和失败阶段分别核。
G1-5|编译专用schema先完成输入层处理，再解析注册数据；生成名单使用显式文件。|未知属性忽略与重复map/version拒绝不同；PBS井号后缀先删，q内容保真须有该输入层前提；生成失败可保留前序文件。|GR3-M01-003|源/正式表族与整份文件数不等价。
G2-1|宿主日历钟、累计游戏时间、单调运行时钟按消费点分开。|离线日期改变不等于帧业务前进；动画初显/更新相位不能统一重置。||不推宿主钟精准度。
G2-2|树果按小时追赶生长、耗水、重植；电话去重墙钟刷新，到零重设20–39分后同次仍减1。|倒退/同秒树果不推进；电话菜单门暂停，不补算全部离线秒数。||普通植物量与统计字段分别。
G2-3|普通玩家一步回绕31位计数并通知；强制玩家实际一步有两次一般通知；寄养256/友好128另计。|NPC/转向不继承强制玩家语义；同步回调异常保留前写且阻断后回调/遭遇。|GR3-M02-001|只在各完整调用前提下判次数。
G2-4|128阈值后按队伍顺序逐合格成员独立1/2，命中再消费成长/Shadow门，最后计数0。|两成员抽样0/1与1/0分别只有首/次变化；空/全不合格也归0；Shadow阶段>=4命中仍不增。|GR3-M02-001|回调异常可能阻止后续及归零，正常完整循环前提保留。
G2-5|Lottery日期播种后无参重新播种；地牢生成显式种子；记录器独立采集随机抽样。|Mining/Tile普通随机不播种；无参重播种不恢复原序列；非驻留地图查询还可能触发地牢副作用。|GR3-M03-002|IHC-001；跨实现随机序列未知。
G2-6|帧消费者实际获得更新机会才推进；电话分别受菜单/战斗/消息/强制路线/解释器门控制。|日期钟继续不保证帧计时消费者更新；捕虫单调期限与消息暂停微更新各自独立。|GR3-M02-001|宿主未执行。
G2-7|Roamer邻接抽样和1/32全候选跳转分开；Radar草地/个体shiny与连锁续存门独立。|全候选可抽原位置；Kyogre特殊候选不泛化；候选通知先于最终许可。||完整地图事件未证。
G2-8|旧图存在且异图才求新天气，类型变更局部duration0；合法连接随后独立写20。|同Rain且旧duration7显式重建保7，连接才20；同图/旧图0不重掷；渐变中/仅强度变更不刷新显示。||20是选择渐变的名义值，非20秒；宿主媒体未证。
G3-1|投球登记先耗球，捕获图鉴/拥有/接收后按满队替换或送盒。|登记后捕获失败不退款；全满后异常不保证撤销先写记录；伙伴接收对象沿末尾恢复一次。|GR3-M07-001|退款新缺口是其它战斗物品执行/终局交界，不扩捕获旧控制。
G3-2|背包/储存容量预检与实际逐槽添加分开，正常接收按入口完成。|有限槽添加可能部分写；负box索引与低界缺失不变成全事务回滚。||默认无限容量不证明有限两槽行为。
G3-3|Factory租借候选、按数量确认、取消重选及换队候选各有入口。|取消后重新commit可保不同原状态；count确认不补资格复核；无限抽样不构造有限保证。||恢复治疗/物品与快照语义分开。
G3-4|捕获与九类获得入口分别登记拥有/见到；公开清理后刷新但保留区域解锁。|击倒不写拥有；静默入队可只写拥有；动态形态登记及图鉴Area消费者不等于拥有记录。|GR3-M11-001|新掩码缺口是不同消费者，不重开C110/C111。
G3-5|给予持物/邮件先容量与必要入库/清空，再交接选择界面。|后续取消不回滚先写；BoxLink嵌套取回可使Move缓存物品过期并重复提交。|GR3-M10-001|新当前正常可达重复，与C125旧索引缺陷分开。
G3-6|个体Owner四字段、玩家身份、宿主语言/UI语言分别消费；默认Owner存在。|来源记录与当前持有者/玩家可不同；同名不证明同Owner，语言不能泛化为唯一全局值。||宿主/外部来源未执行。
G4-1|设施准备先记录EXP再等级调整，战后物品恢复与位置EXP还原按独立阶段。|同级内EXP可保留；后位无效数据失败不撤销前位；物品在调整后的快照时点取得。||无真实接待事件证据。
G4-2|活动队伍[]覆盖实际队伍并令资格注册失败；nil保原队返回nil；正常start/rest/go/end按状态写入/恢复。|取消仅有original才恢复后reset；非活动end也可写旧nil；决策0不保存end结果而start/rest/go仍可保存。||恢复治疗不是通用快照撤销。
G4-3|Mega/Primal在濒死/捕获/世界/设施有各自回退和治疗入口。|普通交换/裸终局不能统一为必回退；回放不自动执行设施准备治疗。||録制重建边界保留B030非必修身份。
G4-4|Shadow标记、量表、Hyper与暂存独立；量表0仍Shadow；HP0清Hyper。|再次make不是幂等；可选Shadow备份启用未知，不把量表0当净化。||U06未证。
G4-5|环境使用标记写入侧按队伍/席位置消费，终局按队伍索引读取。|Burmy队伍Index1替席0虽出战，可因终局读取Index1未标记而不变；不能修成理想集合。||精确入口/索引前提保留。
G4-6|状态、阶段与场景临时信息的写入门分别定；持久数据只在具名门提交。|蛋/初始空敌方与不允许写回场景各自拒绝；调试直接写不能改成正常领域守卫。||类层级不是未来架构。
G4-7|五种持久状态与混乱/迷人/畏缩/瞌睡/毒计数/阶段暂态分别交接。|查询资格不等于应用/清除；局部清除不保证全治疗；状态消息失败的前写边界仍限定。||完整动作执行由M07/M08消费。
G4-8|形态提交先写→缓存/处理器→重算→登记，提示入口写后让出；简单写省略后项。|拒绝学习不回滚，Rotom同形态唯一目标招可删到0；SPINDA像素可得数学尚缺。|GR3-M04-001|IHC-003：withMoves不代替创建复检开关。
G4-9|伤害/属性/速度评估按正常阶段与修正优先序消费，AI静态预测和真实反应分开。|NaturalGift首击耗自身果后续击空持物查询失败，前写不回滚；AI有当前果资格门仍不模拟该反应。|GR3-M08-001|基数、失败门、位置/目标与handler族实际语义分别核。
G5-1|野生音乐门先行，之后internal/exp门才限制EV/EXP；可收获者EV在EXP前。|伙伴计入参加者不等于给伙伴发奖励；早退保参战记录；同级经验helper显式消息先提示后写。|GR3-M06-001|IHC-005；早退不能抹先行音乐门。
G5-2|演化条件消费已有记录，T1–T7/L0/K/D与终生记录门按条件分列，一次检查不串新物种。|取消不记进化成功；Nincada额外个体不继承全部状态；调用者门不抹辅助本身能力。||数据全名单/机制/启用分开。
G5-3|阻止、取消、成功三路；成功提交统计/身份/图鉴/招式后交接演出收尾。|演出/资料后失败保前序写；兼容身份不能净化成泛称；无资源不代表算法不存在。||宿主资源未证。
G5-4|队伍孵化核心写入先于演出；多个蛋按顺序，新孵化个体可影响后项加速门。|演出动态形态读可提交；取消/未执行演出不反证核心孵化；同轮后项不是旧队伍快照统一算。||实际事件/媒体未知。
G5-5|寄养周期只标蛋可领；原始领取两槽先生成、随机/感染，再查队伍容量。|满队保flag，再次领取可重生成；不能把容量预检挪到所有副作用前；不借模型理想化失败。||没有运行生成器。
G5-6|IV3/5、PowerItem、唯一父项与shiny重抽按有序独立门消费，蛋招表与祖先学习回溯分开。|不把父项拷贝/随机视为交换律；实际可选数据启用未证；空/不合格父项保入口失败边界。||全样本表语义与启用分别。
G6-1|钱/BP/coins各自夹限；商店添加成功才计数/支付/过滤，再按入口礼品。|有限两槽999/997买3失败回补总量但变997/999；BP无礼品；并发按键数量优先序与共享选择不同。|GR3-M10-002|默认容量与有限反例前提不混。
G6-2|物品执行成功/取消/已用一次后返回0分层，战斗登记消费先于执行。|执行失败退款未清身份，若同轮正常终局再次退款stock2→0→1→2；下一命令清身份/用方濒死反向保1。|GR3-M07-001|普通场内默认可达前提见完整finding，非自造异常。
G6-3|现持物、初始物、恢复记录、有效门、消费与末尾恢复分开；伙伴正常接收储存对象一次恢复。|Boxed对象/现场对象别名可不同；NaturalGift后续查询失败不自动恢复或无视先写；无额外玩家恢复循环。|GR3-M08-001|AI预测独立当前门，不签真实反应。
G6-4|卡牌买预检添加后付钱，卖先加钱再删；Slots局部信用离场才写回净差；挖矿逐件领；Tile布尔结果。|钱满仍删卡；挖矿tool不消费且重复直接领奖可重复；拼图奖励事件未知；Voltorb倒置clamp局部失败。||素材/奖励事件未证。
G6-5|采摘确认且整量容量过后总株计数+1，qty>=本果max则最大产量株另+1。|qty8/10/12各是单株，不按产量分档加2/3/3；拒绝/容量不足不加；直接查询不加统计。||IHC-002；正常株不超过max，直接helper保留>=。
G7-1|消息、选项、数量、按键主合同交给各消费者；nil/空数组、负/零/正值出口各有含义。|SPECIAL过场nil/[]门不同；战斗逐字busy只恢复而非普通paused跳字；数量同轮优先序不能统一。|GR3-M03-003,GR3-M10-002,GR3-M10-003|共享接口保消费者明确例外。
G7-2|UI记忆、游戏状态与磁盘分别写；退出确认可即使save失败仍离场；子页BACK返回父页。|Options取消不恢复即时配置；反馈文字不等于磁盘提交；当前M02-003由root裁NoRequired。||GR3-M02-003 NO_REQUIRED_REVISION保original_submission与裁决。
G7-3|PC外层队伍资格与物品逐目标门各自消费，正常嵌套交互保已写状态。|BoxLink缩队旧索引前写后失败；空重学初绘失败；Move缓存helditem在嵌套取走后仍提交导致复制。|GR3-M10-001|不将取消统一为事务rollback。
G7-4|下载/文件/编辑/资源/编译/插件/转换分别定义先后及可得失败阶段。|整个路线eval异常先于行首判断，其它行前缀不抵消异常；地图文本较早空桶可跳后非空输出；导入strip/hash缺合同。|GR3-M01-001,GR3-M01-002,GR3-M03-003|未下载、编译、工具或宿主执行。
G7-5|选目标UI登记与真实执行重新资格分开，近盟友几何按初选/存活门。|三席near2濒死无替补而far4存活可初选4登记、执行拒4；near2活先2，无其它活同侧回self；执行物品退款随后终局可再退款。|GR3-M07-001|NearAlly不是理想全局可达过滤。
G8-1|插件消费早于调试编译守卫；候选通知早于允许门，生成完成通知另发；形态回调不是同一通知。|同步回调异常保前写阻后项；持久值同ID双注册保存后项覆盖/读两次/撤销全删；发布可消费预编译插件。|GR3-M02-001,GR3-M02-002,GR3-M01-004|Plugins缺目录与实际启用未知。
G8-2|作者编辑、PBS编译、归档、当前缓存/地图重建按不同入口交接，不自动一条链。|Land0导出省略后重编译default21；同版本早退不刷新；metrics查询可创建项；PBS hash先删；非lambda break/route eval分层。|GR3-M01-003,GR3-M03-004|兼容文字和schema不是未来API要求。
G8-3|调试/编辑器/浏览工具能力与玩家地图事件调用分列，文本可核其合法输入/结果。|工具入口存在不证明实际接待/奖励/事件可达；缺Demo/媒体/宿主不抹掉可得数学。|GR3-M05-001,GR3-M12-001|Debug直写和正常领域门分开。
G8-4|调试直接状态写后求值/刷新请求/持久保存分开，按非默认入口给行为。|SyntaxError可保翻switch槽而阻后刷新；无自动disk保存；设施累计历史旧70+12应82。|GR3-M12-002|未执行eval/生成/模拟器。
G9-1|来源、行为族、正式条款/测试和独立批准多对多，每项保精确身份和作用范围。|同数量/hash/路径存在/方法数不证明语义覆盖；229/341/54/8/432/131各自分母，历史签名不转授。||IHC-007有限统计控制补join。
G9-2|配置样本引用当前主合同，HOME是失败回程；开关51/52读点已证，真实写事件未证。|未驻留查询可生成地牢/改seed和transfer-temp；平衡等级先求值再−4+0..4夹限；礼物编辑共享对象取消可已改。|GR3-M03-002|不将样本当真实Demo链。
G9-3|原批准、候选、ACT独立复审、当前字节、canonical关闭按冻结身份分别绑定；341 keyed范围保各local。|旧B21的229OPEN/327阶段不是现关闭状态；旧批准2同字节/7路径重映射不签新输出；88索引错按exact key消费。||IHC-006；只复用精确限定证据。
G9-4|Graphics/Audio/Plugins缺失与算法/查找/资源存在分别分类；knownpoint.bmp/selpoint.bmp根文件实存。|文件存在不证明绘制/声音/工具运行；Font/DLL/exe/归档只识别不反序列化；SPINDA可得数学不能因Graphics缺失略过。|GR3-M04-001,GR3-M12-001|二进制/宿主真实功能未知。
G9-5|徽章/功能/队伍招式与朝向/地形/载具资格分门，效果及取消分入口；镜头和探测仪有独立消费能力。|FLY/SPLASH、直接FLASH与outer门各自保留；SURF当前出边非仅朝向；镜头卷动/探测仪几何仍缺合同。|GR3-M03-001,GR3-M05-002|当前正式集合引用足以排除M11旧SURF候选。
G9-6|保存UI确认/反馈与迁移/写盘分层，普通/退出/事件/紧急入口有独立顺序。|读档两分支清事件变更记录、条件restore不是一直完整恢复；重复持久ID按后项保存、两次加载，不推全原状态。|GR3-M03-004,GR3-M02-002|GR3-M02-003已NoRequired，保原异议与裁决。
CHAIN-1|伙伴捕获正常接收同一对象送盒/替换，现持物与初始恢复记录在终局一次消费。|满队/箱边界保各先写及消息失败；不加无调用者额外恢复循环或理想全事务。||当前对象别名/owner/资格按本链前提。
CHAIN-2|交换/寄养/孵化/步进分别推进，强制玩家双一般通知，友好128逐成员1/2，植物成功一株总+1。|NPC/普通步不统一双发；回调异常阻后项；孵化核心先于演出/动态形态，新孵化可改后项加速；旧qty分档误句排除。|GR3-M02-001|IHC-002；时间源/离线/暂停独立。
CHAIN-3|有限槽失败回补总量而非原分布，邮件先取下入包后取消保前写，PC/物品/UI按各消费者门。|BoxLink缩队旧索引失败/空重学初绘/缓存helditem复制，数字同轮优先序差与同轮终局再退款保独立结果。|GR3-M10-001,GR3-M10-002,GR3-M07-001|不把有限两槽反例推广默认无限。
CHAIN-4|设施资格→EXP快照/等级调整→名单/租借选择→战斗→位置EXP/物品恢复→end保存按阶段。|nil/[]/取消/end非active区别明确；治疗不是快照回滚；录像重建不补准备地形/默认天气；旧70+12累计应82。|GR3-M12-002|B030非必修保持；规则文件/材料缺失分别。
CHAIN-5|形态先提交再交互，Shadow量表0不等净化，成长/学习/图鉴动态读按门依次消费。|ROTOM同形态唯一招可删空；withMoves=false不跳创建form复检；同级EXP差量提示先于写；SPINDA算法可得而合同缺。|GR3-M04-001,GR3-M06-001|IHC-003；Shadow备份启用/Gen内容未知。
CHAIN-6|编辑/PBS文本/编译/归档/当前缓存/地图重建分层，各明示refresh入口。|Land0写出省略再编译21；相同版本早退；原q文本先hash后转换；事件变更读档清空/restore条件保留。|GR3-M01-003,GR3-M03-004|不会执行编译或旧verifier。
CHAIN-7|Arena初次提示、前三轮判定后替补保count/mind/skill/startHP，随后第3/4/5连续；录制随机序列消费独立。|WP67-A现仍写更替提示/每3回合，与WP56/PA-P28冲突；回放随机超序/未录环境不补正常设施状态。|GR3-M10-004,GR3-M08-001|B028局部当前残留不重开旧CLOSED；NaturalGift实际续击失败需与AI预测界面分开。
CHAIN-8|世界显示/全局相位/计时输入/天气连接/战前音频/目标几何按真实消费者顺序。|零时长不撤在途任务；99998排序独立；near4可初登记后执行拒；SPECIAL过场/镜头卷动、battlebusy仅resume、eventrecord读档恢复有新缺口。|GR3-M03-001,GR3-M03-003,GR3-M03-004,GR3-M10-003|IHC-004；无记忆Q取消timer；媒介/宿主未证。
'''
facts = {}
for line in FACTS_TEXT.strip().splitlines():
    ident, normal, failure, findings, qualification = line.split('|')
    facts[ident] = {'normal': normal, 'failure_and_boundary': failure,
                    'related_new_findings': findings.split(',') if findings else [],
                    'qualification': qualification}

root_findings = jread(BASE / 'findings.json')
if isinstance(root_findings, dict):
    root_findings = root_findings.get('findings', root_findings.get('records', []))
new_findings = {x['id']: x for x in root_findings}
for m in modules:
    d = jread(BASE / m / 'findings.json')
    if isinstance(d, dict):
        d = d.get('findings', d.get('records', []))
    for x in d:
        new_findings.setdefault(x['id'], x)
new_findings['GR3-M02-003']['disposition'] = 'NO_REQUIRED_REVISION'

def finding_summary(fid):
    f = new_findings[fid]
    out = {'id': fid, 'severity': f.get('severity'), 'disposition': f.get('disposition'),
            'title': f.get('title'), 'original_submission_and_adjudication_retained': fid == 'GR3-M02-003'}
    if fid == 'GR3-M02-003':
        out['preserved_disagreement_and_resolution'] = {k: f[k] for k in ['original_submission', 'peer_counterevidence', 'root_adjudication'] if k in f}
    return out

def old_semantics(r):
    for k in ['normal_reverse_partial_failure_review', 'normal_reverse_partial_failure']:
        if k in r:
            return {'field': k, 'value': r[k]}
    return {'normal': r.get('normal_static_judgment'),
            'reverse': r.get('reverse_and_neighbor_static_judgment'),
            'partial_failure': r.get('partial_failure_and_specific_limits')}

def module_current_join(m, i, prefix, r):
    status = next((r[k] for k in ['status', 'local_status', 'review_status', 'judgment'] if k in r), 'UNSTANDARDIZED_SCOPED_RECORD')
    judgment = next((r[k] for k in ['current_semantic_judgment', 'current_judgment', 'current_independent_judgment', 'local_judgment', 'normal_reverse_partial_failure', 'historical_semantic_scope'] if k in r), None)
    if judgment is None and 'historical_semantic_basis' in r:
        judgment = {'current_source_read_scope': r.get('independent_source_scope'),
                    'attributed_semantic_basis_reused_by_module': r['historical_semantic_basis'],
                    'scope_rule': 'Module explicitly reads current source/spec/capability scope, while FINAL1 semantic material is attributed controlled reuse. No claim of a fresh all-owner judgment.'}
    fields = ['actual_read_scope', 'read_scope', 'effective_scope_preserved', 'scope_limits',
              'current_clauses', 'current_clauses_read', 'current_spec_clauses', 'current_spec_paths',
              'current_paths', 'current_spec_evidence', 'current_source_evidence', 'current_evidence',
              'current_capabilities', 'limitations', 'limits', 'explicit_reuse_exclusions',
              'effective_premises', 'effective_counterexample', 'minimum_revision_control', 'determinate_recheck_control',
              'effective_control', 'effective_input_fields', 'historical_semantic_scope',
              'minimum_revision_assessment', 'determinate_recheck_assessment', 'independent_source_scope',
              'historical_semantic_basis']
    refs = {k: r[k] for k in fields if k in r}
    return {'module': m, 'task': modules[m]['task'],
            'current_record': {'path': rel(BASE / m / 'regression-review.json'), 'pointer': prefix + '/' + str(i)},
            'status': status, 'judgment_at_recorded_scope': judgment,
            'scope_and_current_evidence': refs,
            'historical_reuse': next((r[k] for k in ['historical_evidence_reuse', 'identity_reuse', 'historical_reuse'] if k in r), None),
            'related_new_findings_at_module_record': next((r[k] for k in ['related_new_findings', 'new_findings', 'new_finding_relations', 'new_findings_relation'] if k in r), []),
            'does_not_sign_other_modules_or_whole_receipt': True}

def current_paths(r):
    return paths_from([r.get(k) for k in ['current_C_clause_data_case_files', 'current_primary_carriers', 'current_clause_evidence', 'current_required_input_identity_and_ACT_preservation']])

def formal_carrier_join(paths):
    out = []
    for p in paths:
        if p in formal_by_path:
            rs = spec_pool[p]
            out.append({'path': p, 'current_identity': formal_by_path[p],
                        'owners': sorted(assigned_spec_owners[p]),
                        'current_module_spec_rows': {m: [x['row_1based'] for x in rs if x['module'] == m] for m in sorted(set(x['module'] for x in rs))},
                        'row_status_counts': dict(collections.Counter(x['status'] for x in rs)),
                        'semantic_use': 'Read scope and relevant clause/case details remain in module tables; shared-file rows outside the control are not promoted to its acceptance.'})
        else:
            out.append({'path': p, 'classification': 'HISTORICAL_OR_AUXILIARY_CARRIER',
                        'semantic_use': 'Exact historical FINAL1 range/pointer only unless current scoped evidence explicitly reads it; not part of formal131.'})
    return out

regressions = []
for nav in regnav:
    ident = nav['original_id']
    i, r = old_by_id[ident]
    original = next(r[k] for k in ['whole_original_control_identity', 'whole_original_control', 'complete_original_control_identity'] if k in r)
    approved = next(r[k] for k in ['whole_approved_control_identity', 'whole_approved_control', 'complete_approved_control_identity'] if k in r)
    joins = [module_current_join(*item) for item in control_pool[ident]]
    exclusions = [k for k, issue in ISSUES.items() if ident in issue['target']]
    if ident == 'WP80-INTAKE-C01':
        counts = collections.Counter(pathlib.PurePosixPath(x['path']).parts[2] for x in formal)
        joins.append({'module': 'INTEGRATION', 'task': common['reviewer_task'], 'status': 'SUPPORTED_STATIC_STATISTICAL_SCOPE',
                      'current_record': 'this regression-229-joins.json#/records/' + str(len(regressions)),
                      'judgment_at_recorded_scope': 'Current successor corrects historical completion8–9/24 to engine11, pokemon27, test17+index1. Formal inventory independently classified111 body+18 test+2 root=131; no quantity-to-quality inference.',
                      'effective_control_consumed': r['qualified_control_consumption'],
                      'scope_and_current_evidence': {'counts': dict(counts), 'read_loci': ['review/wp80-delivery-2026-10-03/wp80-completion-report.md:8–9/24', 'review/remediation/20261003-prepare/historical-errata.md:126/145', 'review/remediation/20261003-prepare/final-integration-review.md:5/643'],
                                                    'normal': 'Seven domains11/15/27/23/11/17/7=111; test-catalog17+README1; root README/scope2.',
                                                    'reverse': '84packages/87plan/113inputs/113features/432source are separate counts;170/171 original stages preserved.',
                                                    'partial_failure': 'A correct recount does not certify semantics, canonical closure or runtime.'},
                      'historical_reuse': {'complete_identity_reused': True, 'semantic_scope': 'Complete qualified statistical control, normal/reverse/partial and current successor statements read here.'},
                      'does_not_sign_other_modules_or_whole_receipt': True})
    relations = sorted({fid for _, _, _, mr in control_pool[ident] for fid in re.findall(r'GR3-M\d\d-\d{3}', json.dumps(mr, ensure_ascii=False)) if fid in new_findings})
    if ident == 'GIR-FD82-B028':
        relations = sorted(set(relations + ['GR3-M10-004']))
    required = [fid for fid in relations if new_findings[fid].get('disposition') == 'REQUIRED_REVISION']
    status = 'CURRENT_SCOPED_JOIN_WITH_NEW_ISSUE' if required else 'CURRENT_SCOPED_JOIN_COMPLETE'
    if any('excluded' in ISSUES[k] for k in exclusions):
        status += '_HISTORICAL_EXCERPT_EXCLUDED'
    row = {'id': ident, 'approved_title': nav['approved_title'], 'status': status,
           'identity_join': {'original': {**original, 'whole_object_sha256': nav['original_object_sha256']},
                             'approved': {**approved, 'whole_object_sha256': nav['approved_object_sha256']},
                             'FINAL1': {'commit': FINAL_COMMIT, 'path': rel(OLD / 'all229-dispositions.json'), 'git_blob': '1f3d84998f8db23f24f944d31a41315b1526d9f1', 'pointer': '/records/' + str(i), 'whole_object_sha256': nav['FINAL1_object_sha256']},
                             'integrity_basis': rel(BASE / 'regression-identity-checks.json'), 'not_new_semantic_signature': True},
           'qualified_control': {k: r[k] for k in ['current_qualifications', 'qualification_precedence', 'adjudication_precedence', 'effective_qualified_fields', 'qualified_control_consumption', 'complete_qualification_binding', 'effective_cases_identity', 'root_and_extension_adjudications', 'minimum_revision', 'determinate_recheck', 'minimum_revision_and_determinate_recheck', 'minimum_and_determinate_recheck_judgment', 'minimum_revision_assessment', 'determinate_recheck_assessment'] if k in r},
           'FINAL1_attributed_semantics': old_semantics(r),
           'old_semantic_use': 'Only named original/approved qualified scope via current module reading or explicitly attributed FINAL1 fields; any listed exclusions override reuse. Historical PASS is not a new current behavioral verdict.',
           'reuse_exclusions_and_qualifiers': [dict(id=k, **ISSUES[k]) for k in exclusions],
           'current_module_joins': joins, 'initial_assigned_modules': nav['assigned_modules'].split(';') if nav['assigned_modules'] else [],
           'join_completion_vs_behavior_support': 'The finite identity/local-scope join is complete. Each module status and explicit limits below determine behavioral support; completion does not upgrade PARTIAL, unreviewed shared-family, missing material or host.',
           'current_formal_and_auxiliary_carriers': formal_carrier_join(current_paths(r)),
           'accepted_contribution_keys': nav['accepted_contribution_keys'].split(';'),
           'new_finding_relations': [finding_summary(fid) for fid in relations],
           'old_state': nav['old_state'], 'old_state_mutated': False,
           'current_scope_limit': 'A local PARTIAL/unreviewed shared family remains local even if another owner supports its own projection. Root final adjudication is separate; no old state reopen or signature transfer.',
           'executed': False}
    regressions.append(row)
regression_by_id = {r['id']: r for r in regressions}

def junction_excerpt(m, ident):
    text = modules[m]['junction']
    if m == 'M05':
        # Earlier tabular PENDING content was explicitly marked navigation by its author.
        tail = text[text.find('##'):] if '##' in text else text
        return {'path': rel(BASE / m / 'junction-review.md'), 'read_scope': 'Current substantive tail bullets plus actual capability/source/spec rows; initial PENDING table is navigation only.', 'text': tail}
    headings = list(re.finditer(r'^#{2,4} .*$', text, re.M))
    for x, h in enumerate(headings):
        if re.search(r'(?<![A-Z0-9-])' + re.escape(ident) + r'(?!\d)', h.group()):
            end = headings[x + 1].start() if x + 1 < len(headings) else len(text)
            return {'path': rel(BASE / m / 'junction-review.md'), 'read_scope': 'Current named section', 'text': text[h.start():end]}
    selected = [l for l in text.splitlines() if re.search(r'(?<![A-Z0-9-])' + re.escape(ident) + r'(?!\d)', l)]
    return {'path': rel(BASE / m / 'junction-review.md'),
            'read_scope': 'Current explicit named table row' if selected else 'Current substantive grouped-domain junction document; no per-ID heading. Relevant current capability rows identify the bounded family; initial assigned navigation is not acceptance.',
            'text': '\n'.join(selected) if selected else text,
            'individual_ID_heading_absent': not bool(selected)}

def capjoins_for(m, excerpt, specpaths):
    found_ids = set(re.findall(r'M\d\d-[A-Z]*\d+', excerpt))
    exact = [r for r in modules[m]['caps'] if r['capability_id'] in found_ids]
    candidates = [r for r in modules[m]['caps'] if any(p in r['spec_paths'] for p in specpaths)]
    chosen = exact or candidates
    return {'selection': 'Explicit capability IDs in current semantic section' if exact else 'Relevant shared spec-family navigation; each row limits its own actual read scope, not automatic acceptance of every claim.',
            'rows': [{'path': rel(BASE / m / 'capability-coverage.tsv'), 'row_1based': modules[m]['caps'].index(r) + 1, **r} for r in chosen]}

junctions = []
for chain, oldrows in [(False, oldjunction['per_junction_results']), (True, oldjunction['per_chain_results'])]:
    for i, old in enumerate(oldrows):
        ident = old['id']
        owners = [m for m, d in modules.items() if any(x['id'] == ident for x in d['assigned_junctions'])]
        specs = sorted({p for m in owners for x in modules[m]['assigned_junctions'] if x['id'] == ident for p in x['spec_paths'].split('|')})
        reads = []
        for m in owners:
            ex = junction_excerpt(m, ident)
            reads.append({'module': m, 'task': modules[m]['task'], 'current_semantic_reading': ex,
                          'current_capability_source_spec_family_joins': capjoins_for(m, ex['text'], specs)})
        if ident == 'G9-3':
            specs = sorted(p for p in formal_by_path if 'ROOT' in assigned_spec_owners[p])
            reads.append({'module': 'ROOT/INTEGRATION', 'task': '/root',
                          'current_semantic_reading': {'path': rel(BASE / 'root-spec-coverage.tsv'),
                            'read_scope': 'Root three formal metadata/navigation/scope files plus integration read of current historical-stage qualification and exact independent closure footer.',
                            'text': 'Current root metadata preserves historical author/B21 staging as attributed history. final-integration5 records its B21-stage counts;643 separately records exact FINAL1 and229 canonical closure. Immutable candidate/ACT/review tuple and original approval do not transfer signatures.'},
                          'current_capability_source_spec_family_joins': {'selection': 'Management metadata scope, no reference behavior inferred.', 'rows': []}})
        f = facts[ident]
        exclusions = [k for k, v in ISSUES.items() if ident in v['target'].split(';')]
        oldkey = 'per_chain_results' if chain else 'per_junction_results'
        identities = {k: old[k] for k in ['C_row', 'C_row_object_sha256', 'whole_chain_object_sha256', 'fixed_independent_actual_judgment', 'fixed_independent_NEW2_judgment', 'limits'] if k in old}
        current = {'id': ident, 'kind': 'chain' if chain else 'junction', 'theme': old.get('theme', old.get('title')),
                   'current_status': 'CURRENT_CROSS_DOMAIN_DEFECT_RETAINED' if any(new_findings[fid]['disposition'] == 'REQUIRED_REVISION' for fid in f['related_new_findings']) else 'CURRENT_FINITE_STATIC_JOIN_QUALIFIED',
                   'premises': {'original_minimum_and_determinate_recheck': old['original_minimum_acceptance'],
                                'current': 'All named data/caller/condition/consumer requirements must hold; default/failure/partial cases remain consumer-specific. Static/manual inference only; ' + f['qualification']},
                   'normal': f['normal'], 'failure_and_boundary': f['failure_and_boundary'],
                   'current_module_evidence': reads,
                   'current_formal_carriers': formal_carrier_join(specs),
                   'legal_historical_reuse': {'exact_FINAL1': {'commit': FINAL_COMMIT, 'path': rel(OLD / 'junction-chain-review.json'), 'pointer': '/' + oldkey + '/' + str(i)},
                                             'qualified_identity_and_judgments': identities,
                                             'attributed_normal': old.get('normal_order_and_handoff', old.get('current_order_and_normal_conditions')),
                                             'attributed_reverse_partial': old.get('neighboring_reverse_and_partial_failure', old.get('neighboring_reverse_partial_failure_and_reachability')),
                                             'use': 'Original scoped minimum/recheck and named attributed reasoning only, reconciled above to current module evidence; old PASS and numeric offsets are not a new signature.'},
                   'historical_excerpt_exclusions_and_current_qualifiers': [dict(id=k, **ISSUES[k]) for k in exclusions],
                   'related_new_findings': [finding_summary(fid) for fid in f['related_new_findings']],
                   'related_tasks': [modules[m]['task'] for m in owners] or ['/root', common['reviewer_task']],
                   'local_unknowns': sorted(set(r['limitations'] for read in reads for r in read['current_capability_source_spec_family_joins']['rows'] if r['limitations'])),
                   'root_canonical_adjudication_pending_separate': True,
                   'historical_states_mutated': False, 'execution': False}
        if not chain:
            current['canonical_54_navigation_row'] = canonical_junction_by_id[ident]
        junctions.append(current)

# Receipts resolve by the complete fixed tuple and semantic record_key, never array position.
contributor_by_key = {}
for ident, (i, r) in old_by_id.items():
    for n, c in enumerate(r['all_contributor_joins']):
        assert c['record_key'] not in contributor_by_key
        contributor_by_key[c['record_key']] = (ident, i, n, c)

accepted_joins = []
for a in accepted:
    ident, ri, ci, c = contributor_by_key[a['record_key']]
    reg = regression_by_id[ident]
    tuple_ref = a['exact_identity_key']
    carrier_paths = paths_from([c.get(k) for k in ['current_carrier_comparison_keys', 'precise_range_preservation', 'current_static_case_rows', 'current_static_cases', 'current_clause_range_checks', 'current_C_scoped_support']])
    applicable_formal = [p for p in carrier_paths if p in formal_by_path]
    if not carrier_paths:
        carrier_paths = [x['path'] for x in reg['current_formal_and_auxiliary_carriers']]
    scoped_evidence = {k: c[k] for k in ['qualified_attributed_actual_semantic_evidence', 'fixed_qualified_independent_semantic_basis', 'independent_actual_quality_fields_consumed', 'independent_actual_qualified_scope', 'independent_actual_qualified_quality', 'qualified_acceptance_scope', 'qualification', 'local_qualification', 'qualification_match', 'precise_range_preservation', 'current_clause_range_checks', 'current_static_case_rows', 'current_static_cases'] if k in c}
    old_report = {k: c[k] for k in ['actual_independent_report', 'independent_disposition', 'independent_actual_quality_material_identity', 'actual_disposition_object_sha256', 'independent_actual_report_commit'] if k in c}
    allowed_modules = []
    for q in reg['current_module_joins']:
        allowed_modules.append({'module': q['module'], 'task': q['task'], 'current_record': q['current_record'],
                                'status': q['status'], 'judgment_at_recorded_scope': q['judgment_at_recorded_scope'],
                                'read_scope_rule': 'Only the current record actual family/premises; whole parent-ID or all shared-carrier clauses are not granted by this receipt.'})
    ctuple = c.get('accepted_candidate_actual_report', c.get('receipt', {}))
    derived = {'candidate': c.get('candidate', c.get('author_candidate_commit', ctuple.get('candidate'))),
               'actual': c.get('actual', c.get('reviewed_actual_commit', ctuple.get('actual'))),
               'independent_report': c.get('independent_actual_report_commit', ctuple.get('report', c.get('actual_independent_report', {}).get('commit')))}
    assert all(derived[k] == tuple_ref[k] for k in derived), (a['record_key'], derived, tuple_ref)
    accepted_joins.append({'record_key': a['record_key'], 'parent_control_id': ident,
                           'status': 'EXACT_CONTRIBUTION_JOIN_QUALIFIED_WITH_CURRENT_SCOPE',
                           'exact_tuple': tuple_ref, 'tuple_resolved_in_FINAL1_contributor': derived, 'receipt_and_registry_identity': a,
                           'FINAL1_parent_record_and_contributor': {'commit': FINAL_COMMIT, 'path': rel(OLD / 'all229-dispositions.json'), 'parent_pointer': '/records/' + str(ri), 'pointer': '/records/' + str(ri) + '/all_contributor_joins/' + str(ci), 'parent_object_sha256': reg['identity_join']['FINAL1']['whole_object_sha256']},
                           'attributed_independent_ACT_evidence': old_report,
                           'qualified_local_semantic_scope_and_range_evidence': scoped_evidence,
                           'current_carrier_joins': formal_carrier_join(carrier_paths),
                           'current_module_local_projections': allowed_modules,
                           'normal_failure_boundary_example': reg['FINAL1_attributed_semantics'],
                           'example_role': 'Attributed parent-control normal/reverse/partial, not expansion of this contributor local scope; actual named contributor range above controls reuse.',
                           'reuse_exclusions_and_qualifiers': reg['reuse_exclusions_and_qualifiers'],
                           'new_finding_relations': reg['new_finding_relations'],
                           'old_signature_transferred': False, 'whole_ID_acceptance_inferred': False,
                           'current_state_mutation': False, 'executed': False})

def source_classification(path):
    if path.startswith('Data/Scripts/') and path.endswith('.rb'):
        return 'READABLE_REFERENCE_BEHAVIOR_OR_SUPPORT_SOURCE'
    if path.startswith('PBS/'):
        return 'PBS_DATA_TEXT_CONTENT_READ_SCOPE_AND_ACTIVATION_SEPARATE'
    if path.startswith('Text_english_core/'):
        return 'LOCALIZATION_CONTENT_CORPUS_SAMPLED_NOT_FULL_SEMANTIC_READ'
    if path in ['scripts_combine.rb', 'scripts_extract.rb', 'townmapgen.html']:
        return 'AUTHORING_TOOL_SOURCE_SCOPED_OR_NOT_REVIEWED_NOT_EXECUTED'
    if pathlib.PurePosixPath(path).suffix.lower() in ['.dll', '.exe', '.dat', '.rxdata', '.sf2', '.ttf', '.bmp', '.png', '.rgssad']:
        return 'BINARY_OR_MEDIA_IDENTITY_NOT_RUNTIME_OR_DECODED_BEHAVIOR'
    return 'HOST_TOOL_CONFIGURATION_DOCUMENT_OR_LICENSE_MATERIAL'

source_rows = []
for r in reference:
    p = r['path']
    readings = source_pool[p]
    primary = [x for x in readings if x['module'] == r['primary_module']]
    source_rows.append({'path': p, 'fixed_identity': r, 'primary_owner': r['primary_module'],
                        'classification': source_classification(p), 'current_readings': readings,
                        'status': 'CLASSIFIED_AND_OWNED_WITH_EXPLICIT_READ_SCOPE' if readings else 'NO_CURRENT_COVERAGE_ROW',
                        'primary_owner_has_row': bool(primary),
                        'primary_statuses': sorted(set(x['status'] for x in primary)),
                        'actual_scope_preserved': True,
                        'content_and_activation_and_host_rule': 'Current SUPPORTED_STATIC is the declared text/family scope, never full actual activation/runtime/binary semantics. PARTIAL/NOT_REVIEWED/N/A and sampled data remain explicit.'})

spec_rows = []
for r in formal:
    p = r['path']; rs = spec_pool[p]
    spec_rows.append({'path': p, 'fixed_identity': r, 'owners': sorted(assigned_spec_owners[p]),
                      'status': 'ASSIGNED_WITH_CURRENT_CLAUSE_ROWS' if rs else 'NO_CURRENT_CLAUSE_ROWS',
                      'current_row_status_counts': dict(collections.Counter(x['status'] for x in rs)),
                      'current_clause_readings': rs,
                      'status_scope': 'Per clause/table/test design row; no favorable-row promotion of unresolved/not-reviewed or outside-owner families.',
                      'runtime_test_status': 'NOT_EXECUTED'})

material_gaps = []
for m, d in modules.items():
    for i, r in enumerate(d['files']):
        if r['status'] in ['MISSING_MATERIAL', 'UNRESOLVED', 'NOT_REVIEWED']:
            material_gaps.append({'module': m, 'path': rel(BASE / m / 'file-coverage.tsv'), 'row_1based': i + 1, **r})
    for i, r in enumerate(d['caps']):
        if r['status'] in ['MISSING_MATERIAL', 'UNRESOLVED', 'NOT_REVIEWED', 'PARTIAL']:
            material_gaps.append({'module': m, 'path': rel(BASE / m / 'capability-coverage.tsv'), 'row_1based': i + 1, **r})

coverage = {**common, 'kind': 'FINITE_COVERAGE_CLASSIFICATION_NOT_SEMANTIC_OR_RUNTIME_PASS',
            'denominators': {'reference_files': 432, 'formal_files': 131},
            'unowned_reference_files': [r['path'] for r in source_rows if not r['primary_owner']],
            'reference_without_current_row': [r['path'] for r in source_rows if not r['current_readings']],
            'reference_without_primary_owner_row': [r['path'] for r in source_rows if not r['primary_owner_has_row']],
            'unowned_formal_files': [r['path'] for r in spec_rows if not r['owners']],
            'formal_without_current_clause_row': [r['path'] for r in spec_rows if not r['current_clause_readings']],
            'reference_files': source_rows, 'formal_files': spec_rows,
            'unread_partial_missing_and_external_scope_records': material_gaps,
            'data_material_scope': {'PBS_inventory': [r for r in source_rows if r['path'].startswith('PBS/')],
                                    'full_mechanism_vs_samples': 'Mechanism semantics, complete list/formatted-table reading, named samples, optional backup existence, actual enabled variant, binary content, actual host all remain separate per-module rows.',
                                    'shared_AI_test_boundary': 'M08 has217 NOT_REVIEWED AI row entries including4 headings. M09 independently reads213 actual AI/AE/BE/CE test rows plus headings; no conversion of headings into cases.',
                                    'missing_demo': 'No maps/MapInfos/Game.ini/Graphics/Audio/Plugins means actual reception/grant/cost/reward/phone registration/event unlock/media/configuration/host are not proven.'},
            'module_counts': {m: {'files': len(d['files']), 'capabilities': len(d['caps']), 'spec_rows': len(d['specs']), 'regression_rows': len(d['reg'])} for m, d in modules.items()},
            'navigation_corrections': list(ISSUES.values()), 'new_findings': [finding_summary(x) for x in sorted(new_findings)]}

assert len(reference) == len(source_rows) == 432
assert len(formal) == len(spec_rows) == 131
assert len(regressions) == len({r['id'] for r in regressions}) == 229
assert len(accepted_joins) == len({r['record_key'] for r in accepted_joins}) == 341
assert len(junctions) == 62 and len(facts) == 62
assert all(r['current_module_joins'] for r in regressions)
assert all(r['current_module_evidence'] for r in junctions)
assert set(a['record_key'] for a in accepted) == set(contributor_by_key)
assert not coverage['unowned_reference_files'] and not coverage['reference_without_current_row']
assert not coverage['unowned_formal_files'] and not coverage['formal_without_current_clause_row']

write('regression-229-joins.json', {**common, 'kind': 'ALL229_QUALIFIED_CURRENT_SCOPE_JOINS', 'count': 229, 'records': regressions,
                                   'original_nonrequired4': identity_checks['original_nonrequired4'], 'navigation_corrections': ISSUES})
write('accepted-341-joins.json', {**common, 'kind': 'ALL341_EXACT_KEYED_LOCAL_CONTRIBUTION_JOINS', 'count': 341, 'records': accepted_joins,
                                 'numeric_navigation_corrections_from_FINAL1': oldjunction['management_input_navigation_corrections'], 'correction_rule': '88 old offsets are navigation only; record_key and complete tuple resolve every contribution.'})
write('junction-54-and-chains-8.json', {**common, 'kind': 'CURRENT54_JUNCTIONS_AND8_CHAINS_FINITE_INDEPENDENT_INTEGRATION',
                                      'counts': {'junctions': 54, 'chains': 8}, 'records': junctions, 'navigation_corrections': ISSUES})
write('coverage-gaps.json', coverage)
summary = {'counts': {'junctions': 54, 'chains': 8, 'regressions': 229, 'contributions': 341, 'reference_files': 432, 'formal_files': 131},
           'unique_module_regression_ids': unique_module_control_ids, 'integration_statistical_control': 'WP80-INTAKE-C01',
           'findings_count': len(new_findings), 'findings_dispositions': dict(collections.Counter(f.get('disposition') for f in new_findings.values())),
           'reference_primary_missing': coverage['reference_without_primary_owner_row'],
           'unowned_or_missing_rows': {k: coverage[k] for k in ['unowned_reference_files', 'reference_without_current_row', 'unowned_formal_files', 'formal_without_current_clause_row']},
           'validation_scope': 'Serializer schema/count/key/referential validation only; not a game/static-behavior case execution.'}
write('serialization-checks.json', summary)
print(json.dumps(summary, ensure_ascii=False, indent=2))
