"""Read-only Markdown/JSON/Git checks; review outputs stay in this agent namespace."""
from pathlib import Path
import collections
import hashlib
import json
import re
import subprocess
import unicodedata

ROOT = Path(__file__).resolve().parents[3]
OUT = Path(__file__).resolve().parent
CANDIDATE = "d62b41f4d620e50bb04c80a7505374bd284d8210"
SOURCE = "fd1df570cad987dc3852a3b958f03916e317f7fe"
DELIVERY = "4575e80d041ab0c74a42e2e36399d05791dbaa5b"
P = ROOT / "planning/implementation-routing/r8-20261017"

def sha(b):
    return hashlib.sha256(b).hexdigest()

def git(*args):
    return subprocess.check_output(["git", *args], cwd=ROOT)

manifest_bytes = (P / "routing-manifest.json").read_bytes()
manifest = json.loads(manifest_bytes)
sections = json.loads((P / "section-coverage.json").read_bytes())["sections"]
all_features = [f for f in manifest["features"] if "/combat-requirements/" in f["source"]["document"]]
features = [f for f in all_features if not re.match(r"wp5[12]", Path(f["source"]["document"]).name)]
paths = sorted({f["source"]["document"] for f in features})
independent_tree_paths = sorted(git('ls-tree','-r','--name-only',CANDIDATE,'deliverables/final-specification-set/combat-requirements').decode().splitlines())
independent_assigned_paths = [p for p in independent_tree_paths if not re.match(r'wp5[12]', Path(p).name)]
raw_manifest_lines = manifest_bytes.decode().splitlines()
view_lines = (P / "views/combat-requirements.md").read_text().splitlines()

# Judgments below were written after full literal reading of every one of these 15 documents.
reasons = {
1:"包装生成、对象复用、伙伴编组和世界入口跨边界，协作候选合理；未把返回真当胜利。",
2:"布局/所有者与持久参与成员接入相关，协作候选合理；保留合法三打显示秩异常。",
3:"席位—所有者—玩家/伙伴段映射与参与记录需共同约定，粗标协作可接受。",
4:"本节不仅建立临时席位，还逐字段写穿持有物/等级/形态/HP/真实异常，并从持久个体回读；单一Showdown承担遗漏明确持久提交边界。",
5:"创建规则/世界环境映射的协作候选合理，但同一行并入7.5整套选曲请求、预置和播放交付，遗漏表现职责独立边界。",
6:"规则/不变量约束入口和双方模型，作为已有功能的共同验收约束可接受；不视为额外已实现功能。",
7:"入口报错、skip和包装返回边界横跨世界与战斗，协作候选合理。",
8:"配置变体对创建、捕获/伙伴等组合有直接行为影响，粗标协作合理；未批准首版。",
9:"玩家命令、AI控制和即时逃跑/背包登记是共同输入协议，协作候选合理。",
10:"物品4.2已拆，但4.2.1退款残留身份/正常终局/次轮命令消费者仍留本Showdown父行；4.3目标光标到确认亦含表现边界。",
11:"去向和PROTO-BATTLE-ITEM合理，但范围只97–105，未关联106–115退款整链，且缺背包WP27/28与终局WP42必要依赖。",
12:"攻击全序调用物品、Mega、成长、诊断和普通招式，协作粗标可接受；通用待验证不能代表通过。",
13:"优先级、子优先级、速度/同速、增量重排属于战斗内部规则，Showdown承载候选合理。",
14:"Mega资源/次数与个体变形、Shadow Call及Shift接入有不同领域，协作候选合理。",
15:"登记/执行、退款、PP与控制权的不变量供本篇共同验收，协作候选合理。",
16:"终止、失败/消耗与特殊模式边界是共享观察结果，协作粗标合理。",
17:"徽章/Shadow/环物品和战斗配置有真实领域消费者，协作候选合理。",
18:"换入/换出战斗资格可调查引擎，但3.4独立队伍界面canCancel/按钮/摘要/登记正交流程未从Showdown承担拆出。",
19:"出入场顺序及同席位临时效果属于引擎候选，持久个体来源已有上下文映射；可接受粗标但需继续校准R8缺秩整改。",
20:"替补循环含野生拒下一只的即时逃跑与决定3后继续扫描；与FR22/PROTO-ESCAPE缺少显式关联，需纳入同一协作原型。",
21:"Shift重映射十项/例外、选择交换、行动代价是战斗内部状态，Showdown候选合理；立绘消费由表现域接。",
22:"三种入口、计数/随机、决定3与世界终局为协作原型，去向合理，但依赖只WP27/40，未列明确终局WP42。",
23:"招式逃离/替补/后备交互与决定3交界，协作粗标合理。",
24:"换人与Shift/拖出/逃跑不变量关联本篇，协作粗标合理。",
25:"取消、无替补、目标变化及结果消费者跨输入和战斗，协作候选合理。",
26:"玩家系统switchStyle及接力/多打配置有双方消费者，粗标协作合理。",
27:"持久个体、临时场上副本、捕获队列与世界状态分层明确，协作候选合理。",
28:"主循环/裁判内部顺序可调查引擎承担，捕获/逃跑结果仍按已有跨域行输入，未声称兼容。",
29:"成长立即提交、逐级/学招等待、场上回读以协作+原型登记正确；缺WP19/20等明示持久能力/招式依赖。",
30:"完整回合末顺序/早退、缓存与重读为引擎候选，成长/替补通过已独立合同交接，粗标可接受。",
31:"终局退款、捕获接收、病毒、可变还原记录与双方资源清理确属协作，粗标合理。",
32:"世界善后/队伍治疗、进化、拾取/采蜜与包装返回由框架编排合理；音频/过渡的消费还应关联表现域。",
33:"skip/中止/一般异常有不同内外层出口，协作候选合理，未补造finally或已校准。",
34:"配置和跨阶段不变量是该合同验收约束，协作粗标合理。",
35:"天气/场地/侧/位置域状态模型是战斗内部状态，Showdown候选合理。",
36:"规则和世界天气的创建瞬间映射需共同输入协议，单独协作行拆分适当。",
37:"天气覆盖/压制/期限/原始来源和ShadowSky明确战斗内生命周期，Showdown候选合理；Shadow范围待决策另行保留。",
38:"场地接地查询与自然到期/直接移除通知属战斗引擎候选，不把数值相同当行为通过。",
39:"44项作用域目录是行为数据，独立按全场/侧/位置生命周期承载可接受。",
40:"火海双递减、侧保护最后行动和13项换场/清除是战斗内部规则，Showdown候选合理。",
41:"危害资格顺序/实际伤害/吸收属战斗引擎候选，持久HP交接需沿共享写回合同。",
42:"祈愿/延迟来源/位置交换的生命周期和组合规则为引擎候选，可保留合并粗标。",
43:"七调用入口的完整排除名单与世代增量是行为数据，可与引擎承载候选对应。",
44:"17/17/4持物改类型映射是规则数据，Showdown候选合理，不据数据一致宣告支持。",
45:"自然之恩67条默认内容及缺标志边界为规则数据，Showdown候选合理。",
46:"本节仅列59身份→已有主合同位置，属覆盖/追溯索引，独立待实现功能行重复制造实现承诺。",
47:"本节只划WP45/46/44/47B等已有域外责任，无独立实现行为，应该关联已有行作元数据。",
48:"当前类型与四种原能力数值只改场上副本，持久不变边界明确，Showdown候选合理。",
49:"类型/环境/每击当前持物读取及异常前缀为引擎规则候选；不把自然之恩等同背包主动道具。",
50:"命中/保护/时机和具名例外属于引擎规则，Showdown候选合理。",
51:"执行期动态目标构造、重定向/反射属于战斗引擎规则，Showdown候选合理。",
52:"调用/模仿属引擎，但6.3写生先写持久招式再写场上槽与新PP，整体Showdown承担漏持久学习提交边界。",
53:"号令32项/安可常6增6排除表是引擎行为数据，Showdown候选合理。",
54:"不可移物物种/原能力组合及邮件/Mega限制数据是战斗规则数据，Showdown候选合理。",
55:"578条投掷默认威力仅内容数据，Showdown候选合理，未把静态数据登记当运行。",
56:"60项身份→主合同位置只是覆盖索引，应作来源元数据关联行为行。",
57:"已有/共享域外归属主要说明WP44/45/46/47A责任保留，不应成为独立实现功能。",
58:"招式逃离、强制替补和玩家中途选择具有决定3与等待接缝，整体Showdown且无逃跑/替补原型关联不足。",
59:"拘束/代价/行动推进、号令记录恢复属于引擎规则，Showdown候选合理。",
60:"PP减少通过真实招/变身身份同步条件明列，战斗规则候选合理，需沿WP20共享写回合同。",
61:"当前持物写穿、I/R/P/Belch、野生永久转移/终局还原不是单纯临时计算，整体Showdown缺持久物权协作职责；并漏WP42/49/50依赖。",
62:"能力只改场上、浮空/变身临时复制边界明确，Showdown候选合理。",
63:"本节为N01/N02已批准同步和CLOSED事实，只有历史/审计责任，不构成新待实现功能。",
64:"能力身份/有效性与失去获得顺序是引擎候选，持久与场上字段差异已作为输入合同保留。",
65:"入场反应/威吓/天气场地与能力获取全序为引擎候选，Showdown粗标合理。",
66:"离场恢复真实异常/HP、濒死友好和图鉴等跨持久域，整体Showdown缺框架提交与终局层次的职责说明。",
67:"HP跨半、状态/阶级/失败回调规则属引擎候选，持久字段写回仍需共享提交合同。",
68:"每击时序虽为引擎，MAGICIAN/PICKPOCKET转当前物与还原记录并立即触发，跨物权状态协作边界未细分。",
69:"回合末普通规则可引擎承担，但BALLFETCH/HARVEST/PICKUP获得物、还原和消费跨持久物权；整体Showdown缺协作接点。",
70:"MIMICRY场上类型和通知顺序为引擎规则，Showdown候选合理。",
71:"9.2通用形态提交个体/图鉴、9.3共生当前物转移与还原记录差异跨持久层，整体Showdown不足。",
72:"本节混合不变量/失败/配置和依赖，有实际回调约束，可关联本篇作为验收合同；不解释为完成实现。",
114:"资格/组合由框架筛选合理；2.3独立多选界面的次序、按钮/焦点/取消/摘要与提交流程未拆出MZ表现责任。",
115:"赛前成员/队伍约束和数据缓存为框架领域合同，归属合理。",
116:"临调经验/HP、两侧按索引还原、异常前缀和战斗调用跨层，协作候选合理。",
117:"规则组合含报名、临调和战斗条款，协作候选合理，保留直接样本/工厂/模式差异。",
118:"14条款键的设置与实际战斗消费者有共同接入职责，协作候选合理。",
119:"工厂组合数据含领域资格、临调与战斗条款，协作候选合理。",
120:"直接样本/模式转换数据需框架装配并交战斗，协作粗标合理。",
121:"固定资格限制数据与框架资格筛选相同责任，整篇套协作缺为何与FR115框架实现不同的依据，待确认。",
122:"明确56个来源定义身份/主合同定位只是审计索引，独立协作功能行不当。",
123:"条款设置与真实消费接缝有直接行为数据，协作候选合理。",
124:"会话存档、原队伍引用、暂停继续/位置恢复、内容生成全塞协作；未拆框架会话与战斗对局接点，缺WP09/10保存及队伍必要依赖。",
125:"单场包装的经验/物品调整还原与结果回传为协作边界，粗标合理。",
126:"失败/取消主要会话/生成/保存与单场异常混合；框架职责和协作故障接点未区分，待确认。",
127:"配置/内容资源/消息/地图坐标与依赖清单是来源数据合同，协作粗标可接受但资源呈现需关联MZ。",
128:"特殊模式保留用户范围决定正确；自动命令取代正常选招、AI换人/随机域与引擎交接未在框架实现建议中说明，待查。",
129:"Arena同时规定引擎成功状态机/裁判持久HP与非战斗裁判画面，单一框架实现缺逻辑/战斗/MZ独立边界。",
130:"普通/Palace/Arena差异是验证矩阵，可关联功能，但单一框架建议未解释引擎改造或协作方案，待查。",
131:"仅声明回放/内容生成/事件/宿主/运行保留，应作范围元数据，不应成为独立框架实现功能。",
132:"导出临时记录和全局上次战斗的生命周期跨战斗输出/保存，协作候选合理。",
133:"18初始条件与布局/未录选项差异需框架与引擎共同冻结，协作候选合理。",
134:"登记钩子/撤销残留/记录槽与实际命令分层需共同协议，协作候选合理。",
135:"三随机域和询问式替补/回放序列交界清楚，协作候选合理。",
136:"回放副本仍扣实时背包/写实时图鉴的协作候选合理，但6.4消息自动/选靶/中止表现未拆，且未列实时WP09/38/62等关键依赖。",
}

finding_defs = [
 {"id":"COMBAT-01","severity":"P2","title":"退款后续消费者落回Showdown父行，物品原型范围不完整","feature_numbers":[10,11],"source_evidence":[["wp40-commands-obedience-and-action-order.md",97,115]],"explanation":"4.2.1实际是H3，与4.2同Markdown层级，但其具名行为显然是同一背包物品退款链；FR10范围含106–123，FR11只97–105。退款后身份残留决定终局二次退款/次轮清身份/失能清身份；不能仅把首次选择和执行分类为协作。","required_change":"把106–115纳入FR11，或追加保留稳定ID继承的协作子行，绑定PROTO-BATTLE-ITEM及FR31/背包合同；从父行排除同范围并重新生成映射/view。"},
 {"id":"COMBAT-02","severity":"P2","title":"持久写回、学习和物权边界被整体Showdown标签掩盖","feature_numbers":[4,52,61,66,68,69,71],"source_evidence":[["wp39-battle-context-and-participants.md",207,226],["wp47-a-move-attributes-targeting-and-calling.md",201,211],["wp47-b-switching-control-and-item-changes.md",116,159],["wp49-ability-phase-triggers.md",84,101],["wp49-ability-phase-triggers.md",171,210],["wp49-ability-phase-triggers.md",226,256]],"explanation":"正文明确区分临时能力与持久HP/状态/形态/招式/当前物及可变还原记录。候选只给Showdown通用行为比对问题，没有框架持久写回、索引/身份、事件提交与异常前缀的责任分配；partners中列框架不代替五去向分类和验收边界。","required_change":"对纯引擎部分保留粗行；把持久提交/回读/学习/物权子节拆成协作边界或将整个真实混合单元标协作，并明确哪个方拥有与提交持久记录；新增原型问题而非宣告Showdown不支持。"},
 {"id":"COMBAT-03","severity":"P2","title":"独立音频、队伍选择与裁判/回放交互未拆表现边界","feature_numbers":[5,10,18,114,129,136],"source_evidence":[["wp39-battle-context-and-participants.md",260,278],["wp40-commands-obedience-and-action-order.md",116,123],["wp41-switching-positioning-and-escape.md",65,71],["wp54-entry-eligibility-level-adjustment-and-clauses.md",42,50],["wp56-palace-and-arena-variants.md",102,112],["wp58-battle-recording-and-playback.md",160,165]],"explanation":"这些不是单个战斗消息，而是完整音频候选/交付、队伍多选/焦点/摘要/取消、目标光标可视状态、裁判屏幕和回放等待/中止流程，具有与逻辑判定不同的MZ接入与表现验收边界。整行Showdown/框架/双方协作都未描述MZ。","required_change":"按现有子章节拆出MZ表现/输入消费行或明确关联已登记表现功能，并从父行排除对应独立验收范围；逻辑资格/状态写入继续保持相应逻辑去向。"},
 {"id":"COMBAT-04","severity":"P3","title":"覆盖、域外归属和历史保留被制造成独立实现功能","feature_numbers":[46,47,56,57,63,122,131],"source_evidence":[["wp47-a-attributes-targeting-calling-data.md",202,214],["wp47-b-control-items-coverage-data.md",95,105],["wp47-b-switching-control-and-item-changes.md",186,195],["wp54-entry-rules-and-cup-data.md",66,87],["wp56-palace-and-arena-variants.md",139,141]],"explanation":"正文主要列来源效果身份→已有主合同、域外责任、旧N01/N02批准同步/CLOSED或未决保留，没有该行独立的新功能。候选把它们全部作为behavior-unit/待实现待验收功能，重复实现计数并把审计事实混入计划。","required_change":"保留永久ID历史导航，明确这些行是来源元数据/不单计实现单元，并关联已存在行为行；不得删除历史ID来重建编号，不得用不纳入目标回避元数据归属。"},
 {"id":"COMBAT-05","severity":"P2","title":"文档模板依赖漏掉直接背包、成长、终局、保存和图鉴消费者","feature_numbers":[11,22,29,61,124,136],"source_evidence":[["wp40-commands-obedience-and-action-order.md",97,115],["wp41-switching-positioning-and-escape.md",172,175],["wp42-growth-end-of-round-and-battle-outcomes.md",59,95],["wp47-b-switching-control-and-item-changes.md",116,159],["wp55-facility-session-and-restoration.md",62,69],["wp58-battle-recording-and-playback.md",144,155]],"explanation":"每文档全部行复制同一小组WP依赖，feature_refs全空。例如FR11没有WP27/28/42，FR22没有WP42，FR29没有WP19/20，FR61没有WP42/49/50，FR124没有WP09/10/25，FR136没有WP62/09。它们均由正文直接规定，关系不是可选远期猜测。","required_change":"补真实输入、提交和消费者依赖；允许WP级粗标但须纳入必要合同或具体feature引用，并区分来源叙述关联和未来实现依赖，重新检查图与view。"},
 {"id":"COMBAT-06","severity":"P2","title":"替补/招式逃离的协作原型只覆盖一个标题","feature_numbers":[20,58],"source_evidence":[["wp41-switching-positioning-and-escape.md",114,128],["wp47-b-switching-control-and-item-changes.md",19,47]],"explanation":"FR20包含野生拒下一只→替补逃跑决定3→同次扫描继续提示/绑定的完整非致死链；FR58含可逃查询/决定3和玩家不可取消中途替补等待。它们均为Showdown且未关联FR22/PROTO-ESCAPE，只有通用行为比对问题，遗漏实际入口及调用者消费。","required_change":"将相关子边界标为协作或明确待原型裁决，关联逃跑/替补协议与世界终局；保留普通战斗内部状态机的粗粒度，勿把所有换人统一改成同一资格。"},
]

feature_findings = collections.defaultdict(list)
for fd in finding_defs:
    fd["feature_ids"] = [f"FR-{n:06d}" for n in fd.pop("feature_numbers")]
    for fid in fd["feature_ids"]:
        feature_findings[fid].append(fd["id"])

pending = {121,126,128,130}
ledger = []
structural_errors = []
for path in paths:
    b = (ROOT / path).read_bytes()
    lines = b.decode().splitlines()
    headings = []
    anchor_counts = collections.Counter()
    fence = None
    for i,line in enumerate(lines,1):
        fm = re.match(r"^ {0,3}(`{3,}|~{3,})",line)
        if fm:
            if fence is None: fence = fm.group(1)[0]
            elif fm.group(1)[0] == fence: fence = None
            continue
        if fence: continue
        hm = re.match(r"^ {0,3}(#{1,6})\s+(.+?)\s*#*\s*$",line)
        if not hm: continue
        title = hm.group(2)
        base = ''.join(ch for ch in title.lower() if ch in '-_ ' or unicodedata.category(ch)[0] in 'LN').replace(' ','-')
        occurrence = anchor_counts[base]
        anchor_counts[base] += 1
        anchor = base + (f"-{occurrence}" if occurrence else "")
        headings.append({"line":i,"level":len(hm.group(1)),"title":title,"anchor":anchor})
    mapped = [s for s in sections if s["path"]==path]
    actual_pairs = {(x["line"],x["level"],x["title"]) for x in headings}
    map_pairs = {(x["line_start"],x["level"],x["title"]) for x in mapped}
    issues = []
    if actual_pairs != map_pairs: issues.append("heading mapping set mismatch")
    if b != git('show',f'{CANDIDATE}:{path}'): issues.append("working bytes differ from fixed candidate")
    if b != git('show',f'{SOURCE}:{path}') or b != git('show',f'{DELIVERY}:{path}'): issues.append("formal body changed")
    for s in mapped:
        h = next(x for x in headings if x['line']==s['line_start'])
        if h['anchor']!=s['anchor']:issues.append(f"anchor mismatch at {h['line']}")
    structural_errors.extend({"path":path,"error":x} for x in issues)
    ledger.append({"path":path,"bytes":len(b),"line_count":len(lines),"sha256":sha(b),"git_blob":git('hash-object','--stdin').decode().strip() if False else git('rev-parse',f'{CANDIDATE}:{path}').decode().strip(),"literal_read_ranges":[[1,len(lines)]],"literal_read_status":"FULL_TEXT_READ_BY_COMBAT_PARENT","heading_count":len(headings),"mapped_heading_count":len(mapped),"structural_status":"PASS" if not issues else "FAIL","headings":headings})

results=[]
for f in features:
    fid=f['feature_id']; n=int(fid[3:]); p=f['source']['document']; lines=(ROOT/p).read_text().splitlines()
    relevant=[s for s in sections if s['path']==p and fid in s['feature_refs']]
    v=next(((i+1,line) for i,line in enumerate(view_lines) if line.startswith('| '+fid+' / ')),None)
    raw_lines=(ROOT/p).read_text().splitlines(keepends=True)
    unit=''.join(''.join(raw_lines[a-1:z]) for a,z in f['source']['line_ranges'])
    # Preserve each selected raw line's original LF, including range ends.
    identity_ok=sha((ROOT/p).read_bytes())==f['source']['file_sha256'] and sha(unit.encode())==f['source']['unit_sha256']
    identity_ok &= f['source']['heading']==lines[f['source']['line_ranges'][0][0]-1].lstrip('#').strip()
    identity_ok &= f['source']['commit']==SOURCE
    view_ok=bool(v) and f['future_plan']['destination'] in v[1] and all(t in v[1] for t in [f['source']['anchor'],f['current_applicability']['status'],f['destination_verification']['status'],f['future_plan']['stage'],f['implementation']['status'],f['implementation']['acceptance_status']])
    fs=feature_findings[fid]
    verdict='FAIL' if fs or not identity_ok or not view_ok else '待查' if n in pending else 'PASS'
    results.append({"feature_id":fid,"source_document":p,"source_heading":f['source']['heading'],"source_line_ranges":f['source']['line_ranges'],"candidate_manifest_line":next(i+1 for i,x in enumerate(raw_manifest_lines) if '"feature_id": "'+fid+'"' in x),"candidate_view_line":v[0] if v else None,"plan_destination":f['future_plan']['destination'],"verdict":verdict,"reason":reasons[n],"finding_refs":fs,"identity":"PASS" if identity_ok else 'FAIL',"generated_key_fields":"PASS" if view_ok else 'FAIL',"mapped_heading_lines":[s['line_start'] for s in relevant],"upstream":f['upstream']})

counts=collections.Counter(x['verdict'] for x in results)
output={"schema":"r8-disposition-combat-independent-review.v1","candidate_commit":CANDIDATE,"source_commit":SOURCE,"delivery_commit":DELIVERY,"formal_tree":git('rev-parse',f'{CANDIDATE}:deliverables/final-specification-set').decode().strip(),"role":"INDEPENDENT_SUBREVIEW; no author artifact mutation","configuration":{"requested_parent_task":"gpt-6.1-sol / ultra / default","actual_model":"UNVERIFIED","actual_effort":"UNVERIFIED","actual_service_tier":"UNVERIFIED","authoritative_execution_echo":"NOT_AVAILABLE"},"conclusion":"FAIL_FIXED_COARSE_CANDIDATE_IN_THIS_SCOPE","counts":{"literal_documents":len(paths),"literal_lines":sum(x['line_count'] for x in ledger),"literal_bytes":sum(x['bytes'] for x in ledger),"headings":sum(x['heading_count'] for x in ledger),"feature_rows":len(results),"feature_verdicts":dict(counts),"combat_all_feature_rows":len(all_features)},"reading_ledger":ledger,"feature_results":results,"findings":finding_defs,"structural_errors":structural_errors,"scope_limits":["WP51/WP52 eight documents and the AB/AI catalog are reviewed by child combat_ai, not reread in this parent context; merge its separate evidence.","Three remaining combat test catalogs have no literal-reading credit in this parent context; parent root assigned a later independent context.","View all 95 feature rows were parsed and compared for key fields; source and unique per-row plans were semantically read. The 210596-byte repetitive rendered view was not separately claimed as visual full-text reading.","No Showdown prototype, Ruby/game/native host/business vector or runtime equivalence was executed.","Schema/validator global audit belongs to root; this script is independent source/heading/row evidence, not substitute semantic review.","R8-U06 write set/required IDs and source readset index were examined for routing association; the 29-item remediation source-code readsets were not executed or fully semantically reread, because this is not that remediation review."],"upstream_calibration":"AWAITING_UPSTREAM_CALIBRATION; no accepted events, no final R8 acceptance","input_hashes":{str(p.relative_to(ROOT)):sha(p.read_bytes()) for p in [ROOT/'AGENTS.md',P/'README.md',P/'review-prompt.md',P/'routing-manifest.json',P/'section-coverage.json',P/'views/combat-requirements.md',ROOT/'review/global-independent-review/eighth-2026-10-16-fd1df57-c84e/handoff/batch-assignment.json',ROOT/'review/global-independent-review/eighth-2026-10-16-fd1df57-c84e/handoff/batches/R8-U06/readset.json']}}
output['independent_tree_scope']={'combat_documents':len(independent_tree_paths),'assigned_documents':len(independent_assigned_paths),'assigned_set_matches_manifest':set(independent_assigned_paths)==set(paths),'paths':independent_assigned_paths}
batch_data=json.loads((ROOT/'review/global-independent-review/eighth-2026-10-16-fd1df57-c84e/handoff/batch-assignment.json').read_bytes())
u06=next(b for b in batch_data['batches'] if b['id']=='R8-U06')
binding_errors=[]
for f in results:
    expected=f['source_document'] in u06['actual_target_write_set']
    actual='R8-U06' in f['upstream']['batches']
    if expected!=actual or expected and (f['upstream']['status']!='待整改后核对' or set(f['upstream']['required_ids'])!=set(u06['required_ids']) or f['upstream']['accepted_events']):
        binding_errors.append(f['feature_id'])
output['u06_conservative_binding_check']={'status':'FAIL' if binding_errors else 'PASS','error_ids':binding_errors,'required_ids':u06['required_ids']}
if (OUT/'combat-ai-report.json').exists():
    ai=json.loads((OUT/'combat-ai-report.json').read_bytes())
    output['child_review']={'path':str((OUT/'combat-ai-report.json').relative_to(ROOT)),'sha256':sha((OUT/'combat-ai-report.json').read_bytes()),'source_documents':8,'source_lines':1523,'source_headings':101,'catalog_lines':349,'catalog_headings':8,'feature_rows':41,'feature_verdicts':{'FAIL':19,'待查':22},'all_combat_source_rollup':{'documents':23,'lines':4736,'headings':419,'feature_rows':136,'PASS':65,'FAIL':45,'待查':26}}
(OUT/'combat-results.json').write_text(json.dumps(output,ensure_ascii=False,indent=2)+'\n')
report=['# Combat 固定基线独立语义复审','',f'受审候选 `{CANDIDATE}`；来源 `{SOURCE}`；交付 `{DELIVERY}`。本域结论 **FAIL**，不足以授予“固定基线粗标限定通过”；更不构成最终R8整改/验收。', '',f'本上下文实际全文阅读15篇、{output["counts"]["literal_lines"]}行、{output["counts"]["literal_bytes"]}字节；独立核对{output["counts"]["headings"]}个标题及95条feature（PASS {counts["PASS"]} / FAIL {counts["FAIL"]} / 待查 {counts["待查"]}）。WP51/52另8篇及AB/AI catalog由独立子上下文combat_ai完整阅读，证据见其报告；其余3篇catalog由root后继补审，本报告不计为已读。', '', '本报告未应用clean-document-revision重写规格；该技能明确排除审计报告。根AGENTS、README、review-prompt、DELIVERY、review-SKILL、handoff入口相关内容及U06实际写集/读集索引已读；长handoff首次工具输出存在截断，本报告不主张其全合同/全原始读集已经全文读完。真实执行配置没有权威echo，model/effort/tier逐项UNVERIFIED。', '', '## 固定输入与机械核对', '',f'正式子树 `{output["formal_tree"]}`。15篇工作字节逐篇与受审候选、历史来源、固定交付相同；来源文件/unit哈希、有效标题、锚点及映射集合独立核对结果见JSON。结构错误数 {len(structural_errors)}。稳定ID未改写或重建。', '', '生成view的95行已逐行解析并核对来源锚点、去向、四组状态及相应行位置；唯一字段和来源正文已做语义审查。未把重复的210596字节view另称为人工视觉全文阅读。Schema/验证器与远端保全由root汇总，不在此子报告重复授予通过。', '', 'U06正式写集覆盖WP39/40/41/42及WP52-A主稿、相关成长/属性/catalog/UI；本域四篇各行保守绑定R8-U06和11 required ID、状态待整改后核对，接受事件空。其余combat正文未因未选optional F05/AI002自动绑定为已接受或排除。保守整文件绑定是允许的初版口径；仍须未来精确受影响章节差分。', '', '## 逐项问题', '']
for fd in finding_defs:
    report += [f'### {fd["id"]} {fd["severity"]} — {fd["title"]}', '', '功能ID：'+', '.join(fd['feature_ids'])+'。', '', fd['explanation'], '', '证据：'+'；'.join(f'`deliverables/final-specification-set/combat-requirements/{p}` L{a}–{z}' for p,a,z in fd['source_evidence'])+'。', '', '必要修正：'+fd['required_change'], '']
report += ['## 每文档完整阅读与固定身份','','| 文档 | 完整实读 | 标题 | SHA256 |','| --- | --- | ---: | --- |']
for d in ledger: report.append(f'| {Path(d["path"]).name} | L1–L{d["line_count"]} | {d["heading_count"]} | `{d["sha256"]}` |')
report += ['', '## 95行逐项裁定','','PASS只表示该固定粗标的分类/粒度可接受，不代表目标支持、实现或验收已完成。FAIL行依据正文与候选实际字段；待查是已全文阅读后仍缺具体职责依据，不能计作PASS。','','| ID | 结果 | 语义理由 |','| --- | --- | --- |']
for r in results:report.append(f'| {r["feature_id"]} | {r["verdict"]} | {r["reason"]} |')
report += ['', '## 限定与后继','','捕获/背包道具/逃跑/战中成长原型均未运行；相关行未把来源规格当兼容证明、阶段待定且未批准、实现未实现、验收未验收，状态诚实是保留项。去向合理性仍必须修正上述缺陷。未知原型不阻止接受合理粗标，但不豁免本次语义判断。', '', 'Palace/Arena范围及框架如何接管引擎调度、纯框架会话/数据为何被套协作等4行已列待查。既有异常仍按来源事实保留，未来是否兼容应由用户/原型决定，不能通过改正式正文消除问题。当前未批准“不纳入目标”行0，本域未发现暗中排除。', '', '本代理只写本独占review/agents/combat-*，未切分支、未提交、未改作者工件/正式规格/reference/main。后继必须绑定新的精确commit，保留本失败证据，针对变更影响重新核验；正式整改完成后再接受协调任务的固定新基线、回填并独立验收。']
(OUT/'combat-report.md').write_text('\n'.join(report)+'\n')
print(json.dumps({'output':'combat-results.json / combat-report.md','counts':output['counts'],'structural_errors':structural_errors,'identity_failures':[x['feature_id'] for x in results if x['identity']!='PASS'],'view_failures':[x['feature_id'] for x in results if x['generated_key_fields']!='PASS']},ensure_ascii=False,indent=2))
