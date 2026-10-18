"""Serialize the actual root reader's bounded semantic decisions; no business code."""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
OUT = Path(__file__).resolve().parent
BASE = ROOT / 'review/remediation-eighth-20261016-prepare'
ARTIFACT = 'fd414a2c6ec0a0f746b48e0924e5692221ea5d5a'
BINDING = '8ab43a609e60430492b219f0dce14ef4fdb8e47f'

def load(p):
    return json.loads(p.read_text())

def save(name, value):
    (OUT / name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')

# These are manual conclusions after the root's actual reading, not generated
# from a previous PASS flag, hash, keyword, title or helper semantic verdict.
# Each tuple: final locations, source/consumer reasoning, distinguishing control.
D = {
'GR8-KER-001': ('WP10 §5; WP09 §5; kernel catalog deletion group', '删除按P→单个P.bak执行，前一失败截断后继；递归备份读取不扩张删除深度。两个UI调用者在错误处理后分别返回标题或继续重置，未补事务回滚。', '主档删成、备份删除失败：孤立备份保留，下次主档存在门为假，不自动扫描它；取消/首删失败/均不存在/全成功五控制分立。'),
'GR8-KER-002': ('WP09 §4.1/4.1.1; final UI65 startup; kernel catalog startup group', '成功读取和旧序列适配后的结果空性决定启动初始化或装载；启动仅五个bootup登记值取默认，17为全部登记人口。后续有效性、备份、删档同意/拒绝和语言门独立。', '可读旧序列适配为空表→初始化分支；非空有效表→装载。BACK哨兵0继续等待，不产生默认选项返回。解码异常不冒称空表。'),
'GR8-KER-003': ('WP04 §5.2 L196', '默认formatter只构造特定提示字符串，调用者不交付该字符串；去掉这句输出承诺，同时保留真实属性更名、覆盖写入及独立进度/完成输出。', '旧属性匹配时重写但无该特定提示；已用新拼写时不重写。第二文件失败不撤回第一文件，已打开覆盖可留部分写。'),
'GR8-CRE-001': ('WP19 §5.3; WP30 §4.4; WP42 §4.2; EV/ST static groups', '255/255模板存储与重算保持，普通非Shadow成长首先计算HP单项余量−3，早于总量夹限及本接收者EV/经验写入；更早非内部战斗门与先前受领者前缀独立。', 'HP/ATK各255总510，产出1或0均在HP首门失败；每项≤252但总520则可先过单项门、再在总量门失败；不将两种越额混同。'),
'GR8-COM-001': ('WP40 §6.1', 'STALL参与排序，TRUANT的后段行动拒绝不等于排序特性。原速度、平局及配置顺序保持。', '同速度对照分别仅有STALL、仅TRUANT和均无；不能由之后无法行动倒推先后排序。'),
'GR8-COM-002': ('WP39 §4.3.1; WP67-A §3.2/§12; Z01–05', '零可战侧的计数键缺项不等于0；输入映射依原序保留，首失败前的peer/seen/初始化前缀与后来形态/UI阶段分开。玩家skip、NPC及蛋/伙伴各依本身门。', '默认1v1零可战输入先失败，2v1、NPC、玩家skip、蛋和不等布局不能合并成统一健康队列，也不推自动胜利或完整UI。'),
'GR8-COM-003': ('WP39 §4.3.1; WP40 §6.1; WP67-A; M01–04', '混合映射保原序：实际席位0/1/3与配置行动序0/1不同，AI登记不补priority调度；早peer/seen与晚形态/命令/UI消费者均保持。', '混合顺序及其反序、双健康、3v1控制分别按前提判断；登记Q不推出Q必执行，不自动压缩真实参与者索引。'),
'GR8-PBSW-001': ('WP60 §3.3 L45', '五个具名样本准确替代无依据多数；显式数据与构造缺字段默认、未知ID错误、世代备份人工启用分别处理。共享世界目录整篇保留。', '默认67记录只有五果3h/15/2..5，Gen5为5/64，RAZZ为2h/35/2..10；CHERI六小时阶段3/水10/惩罚0，不扩成所有配置运行。'),
'GR8-PBSW-002': ('WP11 L37; WP14 L48/L284; world catalog R8-PBS01', '051文本明确Dungeon=true，模式及条件查询可读；资源、tileset/area/event实体、装载和进入生成仍是不同证据层。', 'PBS有标记而Map051实体未证时，只接受文本配置，不能把材料未知写成字段未知或已运行成功。'),
'GR8-UI-001': ('final UI65 §4.1 L88/L90', '普通No只限定不调用持久层保存；首次信息窗此前已展开共享地图名的前缀不回滚。未新建命名规则。', '首次打开信息窗后No：可已有共享名称变化、返回false和选择音，但未调用持久保存；已展开名称对照不再产生同一展开。'),
'GR8-WORLD-001': ('WP11 §4 neighbor placement; world catalog NP01–05', '进入摆放后首异常且未达正常收尾时，外层捕获继续的同实例保抑制状态；合法重建/帮助缓存清理不独立复位。', '失败前已加入/偏移前缀保留；同实例后继请求受抑制，新容器在成功建立及依赖正常时不继承旧抑制，不称永久软锁。'),
'GR8-WORLD-002': ('WP11 §4/§6; world catalog MP13/RP01–08', '有连接分支最终过滤包含当前图，驻留容器与global当前图可分离；保存类型门、load预取图及继续预览没有被空容器结论覆盖。', 'speed0单轮100格两图均出3328界得空表而global仍旧A；26格删A留B。条件直接保存可过类型门，后继load/预览先取图失败；不称保存必失败。'),
'GR8-AI-001': ('WP52-A §6; AI catalog T02/CV01–05', '原始类型候选发现与计算类型伤害匹配分层，PP过滤仅在后者有限总PP门；直接查询只加14一次，普通User/0不消费该逐目标贡献。', 'PP0仍可参与候选类型发现，但有限总PP下不能贡献匹配；直接查询+14与普通整条行动总分不等价，不能推总分固定100。'),
'GR8-AI-002': ('WP52-A §6 count sentence', '20直接登记+5复制目标=25，只更正计数，不改行为表、默认、拼写或资格。', '按直接20与复制5分别计数，不能把23当缺少两项实现或新增必修根。'),
'GR8-HIST-001': ('current-r7-metadata-qualification.json /stage_counts', '旧3项/2批及其它0限定历史投影，当前27项/13批四门接原最终ledger/public/closure；未倒填字段生成UTC。', 'completion已完成但旧semantic counters仍3/2时，进度取后继27/13，旧值可恢复，42任务ID不当42独立context。'),
'GR8-HIST-R2-BINDING-001': ('overlay /candidate_r2_bindings', 'U03/U07/U10逐真实r2结果接r2审者，直接旧ID/prompt保为r1派发；原WAIT、helper披露与原关闭保持。', 'a8a65→01a1401b-538b，1bd079→01a1401b-7752，d7337→01a1401b-a243；原r1 ID不能与现r2 result直接联结。'),
'GR8-HIST-U06-CONTINUATION-001': ('overlay /u06_continuation', '历史启动WAIT、16:11程序不授PASS、18:41新签内容及19:22parent接收分层；同context续turn+0。', '程序允许继续不等于内容PASS；55a843的新内容裁决方可接收，84dd旧WAIT和程序违例保持。'),
'GR8-HIST-U12-RECEIPT-SCOPE-001': ('overlay /u12_input_receipt_scope', '旧15:43输入UTC/两WAIT限定初次输入与发布；fd112431两有限PASS、parent和eligibility才是后继内容范围。', '旧输入UTC不重命名为完成UTC；38ea初次WAIT与fd112431同context新内容分开，不撤销已有合格有限结果。'),
'GR8-WORLD-003': ('WP12 §7.2; WP13 event L131; final UI65 L152/L210; JT01–06', '普通移动/碰撞计时与跳跃独立。合格普通更新可在活动零跳中登记/消费ACTION/SPECIAL；消息早退、微更新、新请求与已有请求门分层。final UI65两行已接正确WP12。', '无普通移动计时、活动零跳、其余门合格时可进入菜单/快捷；已有debug请求不受全部新登记门重审。先清请求/置菜单中的失败前缀不保证UI或跳跃恢复。'),
'GR8-WORLD-INT-001': ('WP13 event §4; command117; CE01–05', '117携父事件号但子绑定创建时当前图，父保原图；私有变量键与普通角色/自开关/解锁的当前图规则分立。', '父A/7、当前B→子[B,7]与父[A,7]分立；同图后写覆盖，失联后编号0仍分图；缺记录继续，深度101另门。'),
'GR8-WORLD-INT-002': ('WP13 command119; event §7; LB01–05', '已分派119从头找首同名118但不搜最后保留项；缺目标返回继续、位置不变，外层物理下一项。终端先结束和101预读另判。', '命中跳转对照A OFF/B ON，缺标签A/B ON；已写A不因后继B失败回滚，不推无界终止或坏结构安全恢复。'),
'GR8-UI-003': ('WP66-A L145', '非蛋INFO普通与Shadow未满级都按当前普通exp请求128基准偶数舍入底条；saved_exp与心量/数值区独立。保原alias链。', '普通/Shadow当前exp对应宽64或0，满级均不请求；不能从Shadow心量文字替代推出底条消失，也无像素运行信用。'),
'GR8-WORLD-004': ('WP61 §3.3 L56; WP36 §4.3 consumer', '默认Repel比较首非蛋，允许濒死；替代才首可战。nil→雷达→Repel→能力顺序及严格低于/清累积保持。', '濒死L50+健康L10、野生L20：默认拒绝清0，替代放行；相等不拒绝，nil仍先于雷达拒绝。'),
'GR8-COM-004': ('WP39 §3.4', '同一参数分支既有消息差异也有结果差异；修复括注不否定原结果行/BC09。', '两参数控制分别比较消息与返回结果，不能仅因文本不同就宣称结果相同。'),
'GR8-COM-005': ('WP39 §7.4; WP42 §7.1', '正常返回、外层善后及结束通知后复位行走动画/转向预锁；这一步不写方向，不承诺整场方向不变。', '尾动作前方向已被其它阶段改动可保持该值；尾动作自身不提供默认朝向写入。'),
'GR8-COM-006': ('WP40 §5.2 step14', '火药使原行动失败；附加自损同时要求有效天气非雨/大雨及可承间接伤害，早PP/历史前缀保持。', '晴/普通+可承伤自损，与雨/大雨或不可承间伤对照；阻自损不恢复原行动成功。'),
'GR8-COM-007': ('WP40 §10', '王者盾牌接触反制使用正确的配置世代分支；原独立HYPERCUTTER资格与其它保护效果不被合并。', '切换具名配置按各世代降幅；不能以同一接触事件取代能力/保护的独立门。'),
'GR8-ELR-001': ('WP08 §5.1.1; WP15 §3/§5; WP69 §2.2/§6.1', '七角色/八调用先查当前语言SCRIPT_TEXTS，game→core→原键，固定背景等不查；实际高度、空提示清图、转轮空名早失败、普通/帧前缀和已达对象/随机/音效/财务前缀分开。', '两语言缺键A、gameB优于coreC、空译不重试A；投入图只在实际L365请求，不承诺内层每帧查找；未下注BACK正常财务尾与异常未达尾分开。'),
'GR8-COM-008': ('WP41 §9 step4', '换人席位可选增量重算发生在完整速度入场前；配置false、缓存/平局以及startup另路不改。', '开关true/false对照分别观察换人增量与后继完整入场，不能从完整排序存在抹去此前增量步骤。'),
'GR8-EXT-CD-004': ('WP34 L158 → BR23', '只把末次换号/Owner后读的导航接BR23，亲本与生成、随机次数和缓存读取算法不改。', 'BR23 N2末次PID后Owner首次读取；BR24首轮成功/N0不读不清，各自原控制保持。'),
'GR8-EXT-CD-002': ('WP36 §4.2 L132', '作者步骤概率接受整数前缀而无非负门，累加器整除向下；负输入沿原算法、不钳零。正概率样本与负样本宽限前提分别保留。', '−1/200整数商−1；负前缀宽限八次后失败累积−1/−2，正21独立状态不得套同一宽限八次。编译器槽权重正数校验不施加到步骤值。'),
'GR8-EXT-CD-003': ('WP26 L138; WP58 §6.2–6.4', '空收服存储归记录战斗；回放保副本与实时背包等依赖、正常终局和中止分层，不新增捕获可达或全隔离。', '记录存储空操作不能阻止回放合法玩家消耗品扣实时背包，正常终局也不等于中止路径。'),
'GR8-PBS-EGGGROUP-DOMAIN-001': ('WP03 §6.2/L313–339/§metadata; WP18 §3.1', '15精确作者身份只在WP03单一目录，WP18引用；严格枚举拒绝在当前species/form登记前，基础默认/形态克隆及先前登记前缀保持。', 'Humanlike/Field有效，HumanShape/UnknownGroup拒绝；DITTO+PICHU先被Undiscovered门拒绝，不从通用交集推可配。未扩Nature/Shape/Color/Habitat。'),
'GR8-CRE-WP31-UNKNOWN-001': ('WP31 L247/L266; WP03/04 enum contract', '未知作者进化方法在当前记录登记前拒绝；绕编译数据只在实际严格查找到达时报错。五类检查guard和先成功可避坏后项，不扩到after-evolution内部动作。', 'egg/Shadow/Everstone/BattleBond早门与先成功都可避后坏条；action_after_evolution本身直接扫描，不能套五检查统一guard。'),
'GR8-UI-FAINT-AUDIO-001': ('WP67-A §9.3; preserved WP15 audio consumer', '倒下鸣叫入口、音高回退和长度等待有界，数据框消失并行；HP、Off和独立音效不混算。新的Slot语言图像没有改这些音频合同。', '100/d22、75/d29、双缺d12、零长d2及同后缀形态回退控制；SOURCE_STATIC不授发声、像素或墙钟观察。'),
'GR8-PBS-SHADOW-TYPE-LEGACY-001': ('WP23 appendix L228', '原可选SHADOW显式special=true；有效装入原SHADOWRUSH且类型有效时逐招开关true物理/false特殊；Power55/PP0与默认未启用分开。', 'PP0不禁止直接分类查询；未知Type只在实际查询到达失败，不能把省略默认false套到本显式样本。'),
'GR8-UI-BATTLE-END-MARK-001': ('WP67-A §9.1', '两胜利入口先置结束标记后请求BGM；败/平普通scene对照与消息计时原规则保持。', '胜利BGM请求失败仍可留下先置标记；不能把所有结束分支均解释为音乐开始后才置标记。'),
'GR8-CRE-MG-NAME-CANCEL-001': ('WP64 L127–128; shared Creature catalog MG32', '命名按返回文本空性判断，非空原Gift的ESCAPE返回原名可成功；只有空返回且同意停止才nil。共享obtain_text早前缀和三层不写分开。', '原非空名ESCAPE、先删空再ESCAPE均返回旧非空名；删空RETURN+Yes停止，No重入；Create初空/Manage替换/Receive三控制保持。'),
'GR8-COM-RECORD-DEBUG-RNG-001': ('WP58 §5.1; unchanged WP76/RC29 consumer', '调试helper返回选择与实际AI主路径分开，局部归因澄清不改记录流或选择算法，不重写WP76。', '主AI路径不因直接helper选择有返回就记入随机流；直接helper的失败与真实AI的约束按各自入口。'),
}

def main():
    contracts_path = ROOT / 'review/global-independent-review/eighth-2026-10-16-fd1df57-c84e/handoff/contracts.zh.json'
    contracts = load(contracts_path)['records']
    provenance = load(OUT / 'provenance-reading-sources.json')['batch_reader_config_create_report_entries']
    bybatch = {v['batch']: v for v in provenance}
    assert set(D) == {v['id'] for v in contracts}
    old = {}
    for f in ['reviews/actual-U01-U04-U05-U07-U08-U09/r1/per-id.json', 'reviews/actual-U04/r2/verdict.json', 'reviews/actual-U06/r1/continuation-results.json']:
        for i, v in enumerate(load(BASE / f)['records']):
            old[v['id']] = {'path': str((BASE/f).relative_to(ROOT)), 'pointer': '/records/'+str(i), 'record': v}
    for i, v in enumerate(load(BASE / 'reviews/actual-U02-U03/r1/review-result.json')['batches']):
        old[v['required_id']] = {'path': str((BASE/'reviews/actual-U02-U03/r1/review-result.json').relative_to(ROOT)), 'pointer': '/batches/'+str(i), 'record': v}
    records=[]
    for i,c in enumerate(contracts):
        ident=c['id']; batch=c.get('required_primary_batch') or c['conditional_batch_if_user_selects']; b=bybatch[batch]
        loc, reason, control=D[ident]
        record={'id':ident,'classification':c['classification'],'severity':c.get('severity'),'batch':batch,
            'actual_integrated_verdict':'PASS','final_artifact':ARTIFACT,'final_locations':loc,
            'root_semantic_reasoning':reason,'discriminating_static_control':control,
            'contract':{'commit':BINDING,'path':str(contracts_path.relative_to(ROOT)),'pointer':'/records/'+str(i),'canonical_root':c.get('canonical_root'),'canonical_typed_sha256':hashlib.sha256(json.dumps(c,ensure_ascii=False,separators=(',',':')).encode()).hexdigest()},
            'candidate_entry':b['candidate_entry'],'candidate_independent_report':b['candidate_independent_entry'],
            'prior_actual_independent':{'commit':b['actual_independent_entry']['commit'],'path':old[ident]['path'],'pointer':old[ident]['pointer'],'qualification':'Named original scope preserved; not root newly reading every underlying source or tool log.'},
            'accepted_receipt':b['accepted_entry'],'unresolved_blocking_dependencies':[],
            'evidence_types':['SOURCE_STATIC','DERIVED_VECTOR_NOT_EXECUTED','TOOL_VALIDATION_SEPARATE'],
            'reading_basis':'All final affected files whole received by root:25 current direct,12 own priorU06,1 own priorWP61 exact-byte same-purpose. Original candidate and actual source qualifications received from named reports; current cumulative joins manually reassessed.',
            'ACCEPTED_registered_by_this_reviewer':False,'CLOSED_registered_by_this_reviewer':False}
        if c['classification']=='optional':
            o=next(v for v in load(BASE/'coordination/optional-disposition.json')['records'] if v['id']==ident)
            record['optional_disposition']={'selection':'SELECTED','reason_received':o['current_reason'],'root_judgment':'Local low-risk understanding/verification benefit accepted; no mandatory root inflation','original_UNSELECTED_time_scope_preserved':True}
        records.append(record)
    assert sum(v['classification']=='required' for v in records)==29
    assert sum(v['classification']=='optional' for v in records)==10
    assert sum(v['severity']=='P2' for v in records)==2
    save('per-id.json',{'schema':'r8-final-root-39-actual-decisions/v1','input_binding':BINDING,'artifact':ARTIFACT,'manual_root_semantic_decisions':True,'required':29,'required_P2':2,'required_P3':27,'selected_optional':10,'records':records,'global_gate':'Consolidated overall result issued separately after protection checks','business_execution':'NOT_EXECUTED'})

if __name__=='__main__':
    main()
