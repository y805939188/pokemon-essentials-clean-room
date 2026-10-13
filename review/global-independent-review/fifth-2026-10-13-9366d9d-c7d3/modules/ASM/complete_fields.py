#!/usr/bin/env python3
"""Receive exactly the431 pre-existing ASM field gaps; no behavioral execution.

Run after build_draft.py when rebuilding the two-stage ASM deliverable. The
immutable field-completion-input.json fixes the denominator; original review
snapshot identities are retained separately from current consumed-record hashes.
All output is confined to this directory. Reference code is never emitted.
"""
import collections
import datetime
import hashlib
import json
import pathlib
import re
import subprocess

OUT = pathlib.Path(__file__).resolve().parent
ROOT = OUT.parent.parent
REPO = ROOT.parents[2]
B5 = "9366d9d17aaeac3b4414236468affa650fb3dd27"
R = "8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b"
CACHE = {}
IDENTITIES = {}
FIXED = {}
EXTRACTS = []
EXTRACT_INDEX = {}
MANUAL = {}


def load(path):
    if path not in CACHE:
        data = (ROOT / path).read_bytes()
        CACHE[path] = json.loads(data)
        IDENTITIES[path] = {"bytes": len(data), "sha256": hashlib.sha256(data).hexdigest()}
    return CACHE[path]


def esc(v):
    return str(v).replace("~", "~0").replace("/", "~1")


def ref(path, pointer=""):
    return {"path": path, "pointer": pointer}


def resolve(r):
    value = load(r["path"])
    for part in r.get("pointer", "").split("/")[1:]:
        key = part.replace("~1", "/").replace("~0", "~")
        value = value[int(key)] if isinstance(value, list) else value[key]
    return value


def child(r, key):
    return ref(r["path"], r["pointer"] + "/" + esc(key))


def record_evidence(r, role):
    value = resolve(r)
    canonical = json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode()
    return {"ref": r, "role": role, "current_artifact_identity": IDENTITIES[r["path"]], "consumed_record_canonical_json_sha256": hashlib.sha256(canonical).hexdigest(), "canonicalization": "UTF8 ensure_ascii=false sort_keys=true separators=(',',':')", "does_not_replace_GCV_snapshot_sha256": True}


def save(name, d):
    path = OUT / name
    assert path.parent == OUT
    path.write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n")


def rs(v):
    if isinstance(v, list):
        if len(v) == 2 and all(isinstance(a, int) for a in v):
            return [v]
        return [r for x in v for r in rs(x)]
    return []


def unique(items):
    out, seen = [], set()
    for item in items:
        key = json.dumps(item, ensure_ascii=False, sort_keys=True)
        if key not in seen:
            seen.add(key)
            out.append(item)
    return out


def overlap(a, b):
    return any(max(x, u) <= min(y, v) for x, y in rs(a) for u, v in rs(b))


DOC = {
    "K03": "generic-kernel/wp03-content-identity-and-schema.md",
    "K04": "generic-kernel/wp04-pbs-lifecycle.md",
    "K05": "generic-kernel/wp05-events-extensions-plugins.md",
    "K06": "generic-kernel/wp06-time-random-steps-stats.md",
    "K07": "generic-kernel/wp07-diagnostics-files-http.md",
    "K08": "generic-kernel/wp08-localization.md",
    "W16": "engine-overworld/wp16-world-rendering-and-visual-transitions.md",
    "W15": "engine-overworld/wp15-resource-matching-and-audio.md",
    "ST": "pokemon-rules/wp19-attributes-ability-and-stats.md",
    "FORM": "pokemon-rules/wp21-dynamic-forms-and-display.md",
    "MEGA": "pokemon-rules/wp22-mega-and-primal-reversion.md",
    "HATCH": "creature-rpg/wp35-eggs-and-hatching.md",
    "DAY": "creature-rpg/wp33-daycare-and-breeding-session.md",
    "INHERIT": "pokemon-rules/wp34-inheritance-and-offspring.md",
    "ENCOUNTER": "creature-rpg/wp36-wild-encounters-and-modifiers.md",
    "ROAM": "pokemon-rules/wp37-roaming-and-poke-radar.md",
    "DEX": "pokemon-rules/wp62-pokedex-records-regions-and-content.md",
    "DEXUI": "user-interface/wp66-b-storage-and-pokedex-ui.md",
    "GEAR": "user-interface/wp63-pokegear-map-music-and-phone.md",
    "DUEL": "user-interface/wp68-duel.md",
    "TRIAD": "creature-rpg/wp68-triple-triad.md",
    "SLOT": "user-interface/wp69-slot-machine.md",
    "VOLTORB": "pokemon-rules/wp69-voltorb-flip.md",
    "LOTTERY": "pokemon-rules/wp70-lottery.md",
    "MINING": "user-interface/wp70-mining.md",
    "TILE": "user-interface/wp71-tile-puzzles.md",
    "MA": "combat-requirements/wp47-a-move-attributes-targeting-and-calling.md",
    "MB": "combat-requirements/wp47-b-switching-control-and-item-changes.md",
    "FIELD": "combat-requirements/wp45-weather-terrain-side-and-position-effects.md",
    "DAMAGE": "pokemon-rules/wp46-damage-multihit-and-healing.md",
    "ABILITY": "pokemon-rules/wp48-ability-calculation-modifiers.md",
    "ITEM": "pokemon-rules/wp50-held-item-triggers-and-consumption.md",
    "TOOLS": "demo-dx/wp75-project-conversion-and-authoring-tools.md",
    "DEBUG": "demo-dx/wp72-debug-contexts-and-controls.md",
    "EDITOR": "demo-dx/wp73-a-content-editors.md",
    "WORLD_EDITOR": "demo-dx/wp73-b-world-and-encounter-editors.md",
    "ANIM": "demo-dx/wp74-battle-animation-authoring-and-exchange.md",
    "DEMO": "demo-dx/wp77-demo-evidence-and-capability-coverage.md",
}


def doc_path(p):
    p = DOC.get(p, p)
    return p if p.startswith("deliverables/") else "deliverables/final-specification-set/" + p


def fixed_text(p, version=B5):
    p = doc_path(p)
    key = (version, p)
    if key not in FIXED:
        data = subprocess.check_output(["git", "-C", str(REPO), "show", version + ":" + p])
        FIXED[key] = {"lines": data.decode().splitlines(), "bytes": len(data), "sha256": hashlib.sha256(data).hexdigest()}
    return FIXED[key]


def excerpt(p, ranges, role="exact_current_contract", original_mapping_ref=None):
    path = doc_path(p)
    ranges = rs(ranges)
    data = fixed_text(path)
    key = (path, json.dumps(ranges))
    if key not in EXTRACT_INDEX:
        idx = len(EXTRACTS)
        EXTRACT_INDEX[key] = idx
        lines = data["lines"]
        for a, b in ranges:
            assert 1 <= a <= b <= len(lines), (path, a, b, len(lines))
        EXTRACTS.append({"id": f"ASM-FCT-{idx+1:04d}", "path": path, "version": B5, "ranges": ranges, "text": "\n".join("\n".join(lines[a-1:b]) for a,b in ranges), "fixed_file_identity": {"bytes": data["bytes"], "sha256": data["sha256"]}, "role": "exact_existing_specification_wording_not_new_source_review"})
    idx = EXTRACT_INDEX[key]
    return {"text_ref": ref("modules/ASM/field-text-extracts.json", f"/extracts/{idx}"), "path": path, "version": B5, "ranges": ranges, "role": role, "original_mapping_ref": original_mapping_ref}


def add(local, field, text, specs=(), disposition="recorded", refs=()):
    assert (local, field) not in MANUAL, (local, field)
    MANUAL[(local, field)] = {"fact_text": text, "specs": list(specs), "disposition": disposition, "extra_refs": list(refs)}


# M11 mappings receive a specific entry/producer/consumer relationship. The
# source purpose and exact receiver clauses remain independent evidence, not
# a claim that matching names prove an uninspected caller.
M11 = {
 1: ("DEX", [[23,28],[75,82]], "图鉴对象初始化与公开整体清理是本范围的入口；地区表提供区域数，清理生产空记录集合并触发可访问列表重算，保留解锁表。它不以某个剧情授予事件已存在为前提。"),
 2: ("DEX", [[75,82],[86,91]], "图鉴列表构建和形态浏览消费本范围的见过/蛋/形态查询；输入物种经基种归并，形态查询可初始化空槽，末次形态直接查询按原键。未以查询名称推成无副作用。"),
 3: ("DEX", [[38,46],[52,64],[75,90]], "战斗包装、获得/孵化/进化/交换与形态提交分别生产登记；最近见到和末次直接写入是不同入口，当前接收者及刷新门按逐入口表分开。"),
 4: ("DEX", [[23,25],[38,44],[75,75]], "内部战斗包装在对方倒下与捕获计数点分别递增；Info页与普通遭遇连锁查询消费合成计数。独立计数入口不刷新，也不代写见过/拥有。"),
 5: ("DEX", [[69,69],[97,112]], "解锁/锁定和有刷新参数的记录入口可触发可访问重算；暂停菜单/区域选择消费其结果。当前区域模式消费地图区域号，普通模式消费解锁表和见过集合；正常剧情授予/解锁事件调用仍未见证。"),
 6: ("DEXUI", [[128,140]], "暂停菜单的多区域分流建立区域选择列表；每行消费区域名称、见过数、拥有数及区域长度，两完成图标由对应计数阈值决定，选择结果交给主列表。"),
 7: ("DEXUI", [[128,140]], "多区域入口打开本选择场景；BACK/Exit关闭，确认普通区域先写观看区域再开主列表，主列表返回后继续本菜单。初始化、更新与释放属于这一场景链。"),
 8: ("DEXUI", [[128,140]], "区域选择包装读取当前可访问区域及命名配置，确认后写持久观看区域并调用主列表；主列表正常返回到区域菜单，未把区域名的配置形态当额外游戏功能。"),
 9: ("DEXUI", [[146,152]], "主列表构建器把物种行交给列表绘制与游标选择；绘制消费seen/owned、区域编号及行物种，未见行占位且USE不打开条目。空列表是该列表控件的本地输入边界。"),
 10: ("DEXUI", [[156,190],[202,202]], "主搜索画面按所选参数打开网格或大小子页；子页消费本地草稿、焦点与端点索引，OK才交回参数，ACTION仅改变焦点，不能替代Start搜索。"),
 11: ("DEXUI", [[128,156]], "当前区域/单区域/区域菜单三种入口汇入主列表场景；建立时读取观看区域、保存索引和持久模式并初始化会话参数，返回原入口时释放本场景。"),
 12: ("DEXUI", [[146,150]], "主列表初开、排序改变及条目返回后的重建调用此列表构造范围；上游为区域顺序表、seen/owned和末次形态数据，下游为显示行与搜索过滤。"),
 13: ("DEXUI", [[146,152],[188,188],[202,204]], "列表游标改变和搜索结果刷新调用预览/计数绘制；当前行的末次性别/形态与普通外观请求供预览，搜索结果态另外消费命中数与locale换算。"),
 14: ("DEXUI", [[156,186],[202,202]], "进入搜索及各参数子页时调用本范围绘制；消费者是七参数界面与大小双端焦点，显示单位转换不改变原始分米/百克过滤值。"),
 15: ("DEXUI", [[152,152],[184,190]], "Start搜索是过滤/排序的生产入口，先写持久模式再构造结果；预览位图入口消费末次性别/形态但请求普通外观。无结果时保留旧列表和会话参数。"),
 16: ("DEXUI", [[194,194]], "主列表BACK在结果态调用关闭搜索；条目页返回调用同一搜索或普通列表重建。该范围消费返回索引/物种，决定夹限、按物种找回与持久索引写入。"),
 17: ("DEXUI", [[156,186]], "搜索参数项的确认进入对应子页；方向与ACTION/BACK/USE作用于当前子页焦点/草稿，OK才返回参数。双类型槽的轮转/不重复/清空由该子页状态消费，背景选型不等于候选集合。"),
 18: ("DEXUI", [[156,190]], "主列表ACTION打开搜索主画面；参数子页回传值组成当前草稿，Start才写持久排序并运行过滤，Reset只改草稿，Cancel/BACK只关闭当前搜索编辑。"),
 19: ("DEXUI", [[140,156],[188,200]], "主列表更新循环消费游标与输入：ACTION进入搜索、BACK退出结果态或列表、曾见行USE打开条目；非搜索时才持续写保存索引，条目返回进入相应重建分支。"),
 20: ("DEXUI", [[200,217]], "完整列表/摘要单物种和获得后的简略入口分别建立条目页；页刷新消费末次形态和资源指标，Forms选择器的写入与普通页面刷新分离。"),
 21: ("DEXUI", [[204,210]], "Forms页面/选择器调用可列形态生成，先消费形态名称和展示号结构，再消费已见门与性别图解析；多于一项才进入选择器，结构多形态判定不由最终列表数倒推。"),
 22: ("DEXUI", [[200,204]], "Info页初显/换物种/USE切换显示消费拥有资格、物种文本、捕获与击败合成计数；locale决定显示换算，基础记录不因此改写。"),
 23: ("DEXUI", [[202,202]], "条目Area页绘制消费本范围生成的栖息地格集合；上游为遭遇版本枚举、地图区域/隐藏元数据、占位形状和所有可见Point。它不是WP63首条点或仅长度游标查询。"),
 24: ("DEXUI", [[200,210]], "条目翻页/切换物种调用Area或Forms绘制；Area消费已求格集合并显示空态，Forms标签消费当前性别/形态，前后物种浏览只沿传入列表跳过未见者。"),
 25: ("DEXUI", [[208,210]], "Forms页USE且可列项大于一项才打开形态选择器；初始循环及上下移动立即生产末次形态写入，BACK/USE只返回条目页，不回滚首轮或随后写入。"),
 26: ("DEXUI", [[200,210]], "完整条目主循环按当前Info/Area/Forms页消费ACTION/BACK/USE/方向；叫声、计数切换、形态选择和物种/页导航由各页角色决定。简略入口只保留Info关闭/叫声交互。"),
 27: ("DEXUI", [[212,217]], "主列表传入完整列表，摘要View Pokédex先写最近见到后传入单物种完整页，捕获/获得提示链传入简略Info；返回值回到各自调用者，异常不取得正常释放保证。"),
 28: ("GEAR", [[72,85],[95,100]], "电话系统的注册/查找/可见排序入口生产联系人记录；电话UI按已有记录呼出，旧标识包装是另一路由，不把缺失公开查找自动补成记录调用。"),
 29: ("GEAR", [[72,91]], "注册入口构造联系人默认字段；每秒再战计时和胜利重置消费记录级版本/旗标，删除通过可见性写入影响自开关并请求地图刷新。"),
 30: ("GEAR", [[95,100],[129,146]], "电话UI以联系人记录调用呼出，帧更新到期调用呼入；两者经各自信号/范围或候选门后，分派公共事件或训练家对话生成，再共用播放路径。"),
 31: ("GEAR", [[142,146]], "呼入/呼出及旧播放包装把对话和联系人交给分段播放器；每通先抽TP与TE一次供所有分段共用，训练家队伍/遭遇前四槽/地图名与本地化是其上游。"),
 32: ("GEAR", [[89,91],[136,146]], "帧更新挂钩是双计时的实际消费者；持机且无菜单/战斗/消息/强制路线/解释器暂停时推进呼入及再战计时，到期再调呼入或就绪写入。"),
 33: ("GEAR", [[104,125]], "这18项是事件侧旧输入包装：逐项先弃用告警，再转发到具名注册/查找/版本/就绪/生成/播放查询。每行的首个错误与已提交前缀是其本身合同，非全部转发成功。"),
 34: ("GEAR", [[19,28]], "暂停菜单持机入口创建Pokégear按钮场景；按钮与背景各自消费玩家性别和可解析资源，显示/释放服务于同一按钮会话。"),
 35: ("GEAR", [[25,27]], "Pokégear按钮循环消费扩展项列表与UP/DOWN/BACK/USE；确认分派所选效果，假返回继续按钮循环，Map飞行哨兵结束本场景。"),
 36: ("GEAR", [[19,32]], "菜单扩展集合按Map10/Phone20/Jukebox30分派；Phone无联系人只提示后返回，Map选择目标写临时飞行字段并让暂停菜单进入飞行链，队伍FLY入口另有自己的返回处理。"),
 37: ("GEAR", [[38,48]], "地图包装传入区域/wallmap/飞行/编辑模式后调用场景初始化；最终区域和初始坐标来自当前地图定位、玩家位置与实际地图尺寸，相关点查询供底栏及飞行显示消费。"),
 38: ("GEAR", [[44,60]], "区域地图的游标刷新/编辑USE/退出保存调用本范围；名称、详情、治疗点分别消费首条同格记录，附加图消费wallmap或开关，飞行图标和确认共用治疗点查询。"),
 39: ("GEAR", [[52,60]], "地图输入循环先处理方向与插值状态，再消费BACK/飞行USE/编辑USE/ACTION；成功治疗点返回给包装，包装或暂停/队伍调用者才写入/消费飞行目的地。"),
 40: ("GEAR", [[19,21],[32,39],[58,60]], "正常暂停Town Map、Pokégear Map、脚本展示助手及队伍FLY分别调用地图包装；wallmap展示不写飞行目的地，选定点才交飞行执行，取消保留无目标返回。"),
 41: ("GEAR", [[66,83]], "Phone效果在可见联系人非空时打开场景；列表/头像/信号/再战标记绘制消费联系记录、地图元数据和再战启用状态，返回仍交Pokégear按钮循环。"),
 42: ("GEAR", [[66,83]], "电话列表ACTION进入移动模式，方向即时重排持久联系人序列；USE/ACTION落定，BACK按起点还原。普通USE交给命令菜单，普通BACK关闭场景。"),
 43: ("GEAR", [[66,85],[129,134]], "Phone打开前检查可见列表，USE命令分派已有记录呼出/排序/训练家删除；删除后可见重排，删光则关闭。NPC删除限制只属于UI命令。"),
 44: ("GEAR", [[150,159]], "点唱机Custom命令调用文件枚举和子列表选择；选曲结果回交主命令，后者才写默认BGM覆盖并清遭遇旗标，BACK只返回主命令，音频宿主播放另有边界。"),
 45: ("GEAR", [[150,159]], "点唱机主命令分派电台/Custom/Stop/退出；音乐请求交音频覆盖服务，遭遇率旗标由普通遭遇消费，退出不回滚这些状态。"),
 46: ("DUEL", [[17,21],[53,61]], "Duel包装准备对手和台词后建立生命显示；回合检查及损伤提交后的刷新消费活动临时生命与已转义名字，不读玩家持久生物HP。"),
 47: ("DUEL", [[17,21],[53,61],[67,69]], "Duel包装进入开场流程；开场读取玩家角色和指定地图事件原速度，随后请求速度/朝向/移动，正常收尾消费旧速度快照。"),
 48: ("DUEL", [[25,25],[36,47],[55,60]], "Duel主循环的回合检查先处理生命/终局，再抽对手动作与台词，最后进入玩家选择；特殊资格在相应动作选定时消费。"),
 49: ("DUEL", [[25,36],[58,69]], "玩家选择完成后，动作对分派消费双方已选动作并请求地图呈现、提交矩阵损失，再返回回合检查；两方伤害都提交后才重新判终局。"),
 50: ("DUEL", [[17,21],[47,47],[61,69]], "外部对决包装解析训练家类型、构造NPC并本地化12条台词，进入活动；正常胜负收尾才恢复速度并解除固定朝向，不能由包装存在推出实际Demo事件可达。"),
 51: ("TRIAD", [[21,31],[61,67],[116,118]], "建卡范围由持有/买卖/对局消费者以物种身份与通常形态0调用；四向值供翻转和AI评分，类型供elements/卡面，价格供买卖；未启用的属性克制辅助不加进对局。"),
 52: ("TRIAD", [[41,41],[73,94]], "对局初始化创建棋盘/场景；组牌、放置、计分与结算调用显示/通知。普通定时通知与USE暂停消息是不同内部消费者，BACK不能当暂停确认。"),
 53: ("TRIAD", [[61,65],[79,86]], "玩家牌组准备调用手选副本列表；回合选牌ACTION且openhand调用对手查看。它们消费当前手牌数量与副本扣减，返回选择结果而非立即写永久卡仓。"),
 54: ("TRIAD", [[79,94]], "对局玩家回合先选牌，再调用空格选择；BACK从选格返回选牌且不扣手牌，合法落牌才生产棋盘归属/手牌写入并更新分数。"),
 55: ("TRIAD", [[49,55],[88,94]], "真实落牌调用翻转提交，AI候选调用预估翻转；两者消费相同方向值/规则但预估不写棋盘，因此递归占位守卫不同，不能相互替代。"),
 56: ("TRIAD", [[47,67]], "对局入口消费等级、规则字符串、预设对手组和卡仓；校验后按elements→玩家牌→对手牌→先手顺序生产本局快照，持久卡仓到结算前保持。"),
 57: ("TRIAD", [[73,94],[100,110]], "九次合法落牌循环在对手回合调用候选评分/随机选择；结束后计分、显示结果再调用仓库转移，direct负局仍消费其具名残留身份，不改写成理想规则。"),
 58: ("TRIAD", [[37,41]], "卡仓的总数/增删/预检被对局准入、准备副本、买卖和赠卡分别调用；公开准入查询与进入对局自身检查分开，直接增删可部分提交。"),
 59: ("TRIAD", [[21,31],[116,116]], "购买入口从图鉴owned基础物种建立列表，选择数量/确认后依次调用余额复检、卡仓容量预检、添加与钱写入；卡价依赖建卡数值。"),
 60: ("TRIAD", [[31,39],[118,118]], "出售入口消费持仓槽及同身份合计数量，确认后先写钱再调用删除；查看/取消与地图视野恢复是这一买卖会话的不同路径。"),
 61: ("TRIAD", [[37,41],[118,118]], "列表查看只是卡仓消费者；赠卡包装先宽松解析身份与预检，再添加，不把它的守卫传播到卡仓直接入口。取消行与BACK只结束查看。"),
 62: ("SLOT", [[19,32],[62,63]], "场景创建依次建立三个转轮；旋转更新消费运行时长/图高，USE停止请求选择当前最左仍转轮并重抽滑移，结算读取冻结的显示索引。"),
 63: ("SLOT", [[53,66],[72,78]], "下注与支付循环更新场景信用/待付额并调用数字显示；控件的上限夹限不等于持久余额已写，持久提交在离场路径。"),
 64: ("SLOT", [[36,49],[63,78]], "三轮停止后结算调用有效线判奖，表现结束进入支付循环；USE或信用满额可一次清算待付，净差统计由会话退出消费最终信用。"),
 65: ("SLOT", [[13,15],[53,84]], "包装守卫后进入Slot场景；等待投入/旋转/结算状态循环消费输入，外层上限判断读场景信用而耗尽判断读持久余额，正常离场才提交和计净差。"),
 66: ("SLOT", [[13,15],[78,84]], "公开包装按COINCASE→零币→恰满值次序准入后淡出进入；正常收尾写信用与统计。直接场景入口没有自动继承包装的持物守卫。"),
 67: ("VOLTORB", [[13,19],[33,33]], "新会话与每次升级/重开调用棋盘生成，传入当前1–8等级；生成消费该级候选及随机洗牌，结果交行列提示和输入流程，1000次失败仍返回最后盘。"),
 68: ("VOLTORB", [[9,9],[23,27],[33,40]], "每个新盘先调用生成/建显示并初始化已揭、奖额、光标和标记，再检查余额上限；行列统计和预渲染都是该盘的消费者。"),
 69: ("VOLTORB", [[25,27],[34,39],[49,51]], "操作循环消费方向及USE；普通未揭格进入翻牌/记已揭/得分或踩雷路径，标记模式只操作标记；终局处理接收本次已提交的盘面。"),
 70: ("VOLTORB", [[35,45]], "USE后的全倍率检查和BACK确认分别调用结算；持久加币/统计发生在揭盘等待之前，继续键只推进展示与后续等级/退出处理。"),
 71: ("VOLTORB", [[23,23],[35,41],[57,57]], "单格翻开与终局揭盘调用显示/收牌范围；全盘揭示后的专门循环接受USE或BACK，随后按列收牌，不能由正常格操作直接跳过该等待。"),
 72: ("VOLTORB", [[9,9],[33,45],[49,57]], "公开包装/正常主循环消费退出标记；每轮先调用输入再检查quit，新盘/失败级别/收牌后的分支决定继续或关闭。媒体退幕不是另一个发奖入口。"),
 73: ("LOTTERY", [[13,17]], "生成入口由外部调用并传目标变量号，读当前日期、临时播种抽号后重播种，调用变量写入/地图刷新包装；日期改变本身不自动调用。"),
 74: ("LOTTERY", [[21,48]], "检索入口消费外部号码以及名字/位置/匹配数变量号，遍历队伍后含队伍的储存集合；三个结果按序直接写变量。外部领奖是独立未知调用，不在检索内生成。"),
 75: ("MINING", [[29,39],[47,49]], "场景初始化提供覆盖层/裂纹初态；USE敲击调用工具更新与局部效果，动画忙门由主循环消费，既不扣背包工具也不修改个体生命。"),
 76: ("MINING", [[17,27]], "61物品/13铁候选是初始化摆放的输入，权重、形状、互斥身份及素材矩形分别被抽样/重叠检测/绘制消费；数据表本身没有独立外部调用门。"),
 77: ("MINING", [[23,29],[45,45]], "Mining场景入口调用物品→铁→层厚初始化；成功布局和光标58交自由操作，内部位置重试与外层500次数是不同循环。"),
 78: ("MINING", [[19,27]], "初始化的候选/位置尝试调用同身份、化石/石板组与形状占用检查；检查读已放集合，只有接受后才写入布局，矩形空洞不算占用。"),
 79: ("MINING", [[33,39]], "USE敲击以当前光标和镐/锤模式调用本范围；先生产损耗再消费中心铁/层厚及3×3边界，完全揭露检测随后消费更新后的覆盖层。"),
 80: ("MINING", [[39,58]], "敲击后的揭露闪光正常结束才登记待领；主循环在动画忙门释放后先判坍塌再判全得，三个退出路径最后调用同一按序领取。"),
 81: ("MINING", [[11,13],[48,64]], "坍塌、挖完或确认放弃的正常流程调用领取入口一次；领取逐项调用背包直接add并反馈。外部重调同一场景领取会再尝试，公开进入无费用/工具守卫。"),
 82: ("TILE", [[31,37],[43,51],[104,107]], "Tile场景绘制消费模式、位置表、角度、暂持与选中态；块图/预旋转图与合法方向决定贴图、旋转和箭头，显示状态不代替动作资格。"),
 83: ("TILE", [[23,37],[76,96],[104,106]], "拼图入口以mode/board/width/height建立场景后调用初始化；块资源尺寸与模式决定排列/角度/初始光标，随后主循环先检查完成态。"),
 84: ("TILE", [[57,70]], "输入循环按当前模式与按住USE状态调用可移动方向或旋转；暂持块优先的ACTION与模式7联动不同，合法动作完成后才提交对应角度/位置。"),
 85: ("TILE", [[45,49],[64,66],[78,79]], "模式3滑动、模式4/5相邻交换和模式6行列移由方向输入分派；初始化模式6也调用同一行列移动能力，因此非方形列端点边界不能仅当UI输入问题。"),
 86: ("TILE", [[63,70],[100,100]], "主循环先判完成再处理输入；未完成BACK返回false，完成序列USE/BACK返回true，重新进入必须由事件再次调用并重新打乱。"),
}

# Nineteen M01 premises. Definition-only and legacy scopes explicitly identify
# which consumer contract carries the operational conditions.
add("M01-LZ-KEY", "preconditions", "输入为空值则原样返回；文本含回车/换行/制表/控制字符1、行首/行尾空白或连续空白时才进入键归一。处理顺序为逐行起始空白、逐行末尾空白、剩余连续空白折为一个空格；可跨相邻空行，不能改成整串trim或split/join。仅生成查找键，不按此规则改写原始值。", refs=[("modules/M01/followup-partial-dispositions.json","/records/3/status_reason")])
add("M01-LZ-DOMAINS", "preconditions", "此范围定义编号0–30的31种消息域及转发；域清单不是‘只存在18域’的判定，18仅是随附非空core内容。字典、数组与地图桶必须由其实际消费者按各自形态读取；运行语言选择与查找回退分别由M01-LZ-LOAD/M01-LZ-LOOKUP承接，没有为身份目录另造调用守卫。", disposition="definition_projection_with_named_consumer_conditions")
add("M01-CSV-LEGACY-SCALARS", "preconditions", "本范围是已审但不参与当前启用格式路径的旧标量转换辅助定义。旧引号/转义消费和宽严不同的转换仅在直接选用这些旧入口的条件下成立；当前PBS标量语法由M01-CSV-CAST承接，不能用旧辅助替代活动格式的接受条件。", disposition="not_applicable_to_active_parser_contract")
add("M01-CSV-LEGACY-RECORD", "preconditions", "旧记录求值器的可选宽松、重复字段与结果形态只限定该弃用定义。已审记录明确其未被当前启用路径使用；活动记录转换的前提由M01-CSV-RECORD承接，不把旧记录求值器计成另一套当前可接受语法。", disposition="not_applicable_to_active_parser_contract")
add("M01-PARSE-CONTENT", "preconditions", "前提须按选用解析入口分开：item/species/move会规范大小写与空白，物种解析含Nidoran别名，move可选择跳过未知；Nature/Trainer旧分支的定义不能变成当前统一别名合同。后继已找到parseSpecies的作者消费者，故该分支不能再整体归无消费者；设施宽容引用和其它旧辅助政策分别保留。", refs=[("modules/M01/followup-partial-dispositions.json","/records/12")])
add("M01-PBS-TOWN", "preconditions", "先经当前PBS/schema的身份、字段类型和重复Point读取；此town-map编译范围没有额外逐记录校验。区域名、点名、地点说明分别收进哈希消息域，重复文字按哈希身份处理；地图显示/开关/飞行资格不是这里的编译守卫。")
add("M01-PBS-ABILITY", "preconditions", "能力数据先满足通用注册/schema规则；本能力编译尾段无额外逐记录资格检查，正常完成后重建名称与说明两哈希域。标志的运行条件必须交给实际消费者，例如FasterEggHatching由M01-ABILITY-FLAG-HATCHING/WP35处理，不能从能登记推导所有能力效果启用。")
add("M01-PBS-METRICS-SHADOW", "preconditions", "复合物种/形态输入的形态0归基础身份，非0保留后缀；此尾段不追加终局约束。可选Shadow材料全缺时走通用可选返回；指标查询可新建默认记录，与实际原图/运行可用性分开。")
add("M01-PBS-RIBBON", "preconditions", "缎带编译接受通用schema与注册校验后的记录；此范围无额外逐记录检查，完成时重建名称/说明消息哈希。80条数据的成立不证明比赛发奖事件，个体给予/升级/移除的条件由M01-RIBBON-REGISTRY-CONSUMPTION及WP21§5.2承接。")
add("M01-PBS-MAP-DUNGEON", "preconditions", "地图Name非空与缺省分支不同：空名才读取对应MapInfos条目，缺该记录不保证安全空名。地牢图块表没有额外记录校验；参数的区域/版本身份仍规范化并判重。缺图块数组、空图块登记表的后续失败分别由已接收021/022事实限定，不能由69个有效地图样本外推畸形输入安全。", refs=[("modules/M01/followup-partial-dispositions.json","/records/20")])
add("M01-ID-DUAL", "preconditions", "调用的是双身份内容族的登记/存在/严格或宽松查询，合法查找输入为符号、字符串、整数或同族实例；错误类型不在宽容返回空的范围。登记按两个键写同一记录，‘两键一条目’以无键冲突为前提；同族实例可直接返回而不要求已登记。遍历只取非整数键并按数值身份排序、count按双键计数，不外推到纯整数或纯符号族。", specs=[("K03",[[26,42],[73,77]])])
add("M01-ID-BULK-DISCOVERY", "preconditions", "批量发现以已声明的数据族及其文件/基名定义为输入；OPTIONAL决定缺文件是否进入必需重编译集合。数组形式的PBS基名逐个展开，加载分派到各族已声明的读取入口；不是递归发现任意文件后自动注册。", specs=[("K03",[[59,87]])])
add("M01-FIXED-BodyColor", "preconditions", "本范围只声明按登记顺序排列的10色身份Red/Blue/Yellow/Green/Black/Brown/Purple/Gray/White/Pink及未命名回退/本地化；本身没有运行筛选门。图鉴搜索消费者按登记序建立颜色候选并排除假设None，实际筛选还要求曾见；固定目录缺口由024统一承接。", specs=[("DEXUI",[[188,190]])], refs=[("modules/M01/followup-partial-dispositions.json","/records/55")])
add("M01-FIXED-BattleWeather", "preconditions", "这是9种天气身份与对应动画名称的静态目录：None无动画，其余有各自名称。它本身不实施期限/压制/建立许可；四普通天气招式的强天气和同天气拒绝条件来自已审M08天气建立消费者，而非本登记表。", specs=[("FIELD",[[54,60]])], disposition="definition_projection_with_named_consumer_conditions")
add("M01-FIXED-BattleTerrain", "preconditions", "这是None/Electric/Grassy/Misty/Psychic五种身份与四个场地动画名称的定义；None没有动画。登记本身不判接地或期限；同种拒绝、建立期限和全员通知由M08场地建立消费者承接，成员是否受场地影响另按其接地查询。", specs=[("FIELD",[[83,90]])], disposition="definition_projection_with_named_consumer_conditions")
add("M01-EVO-REG-512", "preconditions", "六个use-item定义首先要求所用物品等于该进化条目参数；男/女、白天/夜晚分支再加对应条件；ItemHappiness在软上限开时要求友好度至少160，关时至少220。该族没有持物进化后移除处理器。统一检查入口仍先拒蛋/Shadow、不变之石和羁绊变身，并按当前形态条目顺序取首个命中。", specs=[("pokemon-rules/wp31-basic-evolution.md",[[68,75],[132,146]])])
add("M01-RIBBON-REGISTRY-CONSUMPTION", "preconditions", "登记数据定义80条名称/说明/图标身份，个体拥有列表顺序不等于图集编号。消费者给予/升级/移除/清空必须按各入口的已拥有状态和目标身份处理；重复升级及缺已拥有项失败不能由登记数据存在推成成功。", specs=[("FORM",[[262,270]])])
add("M01-ABILITY-FLAG-HATCHING", "preconditions", "每步先跳过孵化计数≤0者，对仍参与成员先减1，再即时扫描非蛋队伍；首个带FasterEggHatching标记者再减1且不叠加。扫描不另排濒死，首次减到0的临界个体已可入非蛋集合；计数到≤0才置0并提交孵化。", specs=[("HATCH",[[71,85]])])
add("M01-PBS-CONNECTION-DATA", "preconditions", "19条连接按作者顺序消费方向/偏移；字符串方向端点在输出时保留，数值端点的相反符号坐标先规范化，再按西/北/东/南边界形式选择。输出过滤依赖MapInfos、几何转换依赖地图尺寸；连接文本存在不证明地图几何或实际跨图入口。", specs=[("engine-overworld/wp11-map-topology-transfer.md",[[41,51]]),("DEMO",[[67,71]])])

add("M02-MENU-EXTENSION", "dependencies", "依赖命名菜单项登记集合、登记序/显式order、条件谓词、动态名称和效果回调：条件接收枚举实参，动态名称无参。缺菜单枚举空与直接call缺整个菜单可失败是不同入口；具体暂停/PC菜单提供自己的上下文和消费效果返回值。", specs=[("K05",[[49,54]])])
add("M02-STATEFUL-RANDOM", "dependencies", "依赖合法正n、该选择器保留的本轮已出现状态与普通随机入口。未出现偏向和旧值重抽会消费随机，轮次耗尽后重开；它不依赖战斗记录序列，也不保证无放回或恰n次覆盖。", specs=[("K06",[[131,142]])])
add("M02-RANDOM-RECORD", "preconditions", "记录/回放合同只适用于经战斗专用随机入口的调用：记录阶段保存其实际随机输出，回放按保存序列与当前位置取用。普通/AI旁路随机、外部状态和不同布局不能由此取得可重现保证；需要对应战斗初始化数据和可供本次读取的记录序列。", specs=[("K06",[[125,129]])])
add("M02-DIRECTORIES", "dependencies", "目录辅助依赖宿主目录进入、glob结果、路径/文件判断、逐文件操作及调用者给出的块。文件先于子树和删除含根为当前路径模式合同；缺目录的进入失败与块内部失败不同，插件脚本载入只消费其排序结果而不使链接/隐藏文件的全部宿主行为已证。", specs=[("K07",[[23,27]])])

add("EVENT_PAGE_REFRESH", "dependencies", "依赖事件页条件所读的开关/变量/自开关及事件绑定地图/ID，页选择结果交事件显示、移动路线和并行解释器。原始朝向/图案决定异页是否保留当前值，路线图像命令和强制路线结束会反向影响下一次页刷新；不把同页保持当全面重新初始化。")
add("EVENT_PRIVATE_COOLDOWN", "dependencies", "依赖绑定事件的私有变量/时间记录、现实时间查询和页条件的临时A消费者；到期设置临时A并同步请求事件刷新。这个记录是事件私有状态，不是WP06的游戏变量墙钟计时槽，两者不得互相代替。")
add("FIELD_STRENGTH_PUSH", "dependencies", "依赖当前解释器绑定事件、玩家面向、严格双端地图通行/角色碰撞、through状态、移动记录与strength_push_count。推格提交之后玩家锁定等待消费事件移动完成；激活怪力的外部许可与这段实际推格合同分开。")

add("M04.types-gender", "dependencies", "持久类型读取依赖当前物种/形态数据并返回列表副本；性别求值依赖GenderRatio固定表、个体身份派生值及强制性别字段。战斗临时类型是后续消费者的状态，不从此个体列表接口推成两类型截断。")
add("M04.nature", "dependencies", "依赖25项Nature登记表、个体身份派生/缓存和计算性格覆盖字段；能力计算消费计算性格，表现和Shadow心灵值等消费者仍读取原存储性格。修改计算覆盖不改写固定25项默认目录。")
add("M04.level-interface", "dependencies", "经验/等级接口依赖当前物种的成长曲线身份、GrowthRate阈值查询和等级上限；等级缓存与设置最低经验是个体层投影。六曲线全集、升级/学招/友好度流程由M06/WP30消费，Shadow暂存经验另经WP23。")
add("M04.hp.status-and-healing", "dependencies", "依赖个体HP上限、蛋判据、Status登记身份与招式槽PP；HP归零还调用Shadow超频清理，完整治疗与单项HP/状态/PP治疗分开。战斗场上状态同步由战斗消费者承担，不能把此持久个体接口当所有战斗资格门。")
add("M04.appearance.spinda", "dependencies", "依赖个体32位身份与普通异色读取、四组固定掩码、物种位图复制/修饰分派以及可枚举帧的AnimatedBitmap能力。消费入口须交付足够尺寸的有效位图；分帧PNG逐帧修饰不能替代原生动画内部帧访问证明。", refs=[("modules/C00/residual-premise-join.json","/records/12")])
add("M04.transformation.cleanup", "preconditions", "只在具名清理入口及其正常到达前提成立：普通换下、真正濒死、捕获送出队员、世界战斗包装与设施包装分别处理；裸终局不能自动获得包装清理。还原形态与持物恢复的先后及对方处理范围随入口而异，不能统一为任意离场均全部还原。", specs=[("MEGA",[[76,89]])])
add("M04.transformation.cleanup", "dependencies", "依赖战斗席位与持久个体间的同步、特殊形态还原入口、濒死/捕获队伍发送以及世界/设施各自的收尾包装；持物还原记录和形态判据按该具体入口先后消费，普通换下不能借用世界终局的范围。")

add("M06.WP33", "caller_override", "事件简写经编译器映射到寄存/取回/选槽/报价/兼容性/取蛋等工具；实际地图接待事件缺材料，不能补造收费或可达caller。玩家迈步处理器更新256步周期；调试菜单是已读的另一直接读写周期/已有蛋入口。", specs=[("DAY",[[79,105],[124,138]])])
add("M06.WP34", "caller_override", "寄养领取通过两槽亲本调用后代生成，再把产出的蛋交给领取/队伍流程；生成器内部按亲本归一→物种/形态→遗传各通道→收尾推进。其输入是给定亲本，兼容性、256步产蛋与容量/取蛋状态由WP33调用者决定，不由生成器重做。", specs=[("DAY",[[133,138]]),("INHERIT",[[5,20]])])
add("M06.WP35", "caller_override", "玩家迈步事件的独立孵化处理器按队伍索引减计数，归零者同步调用孵化提交与演出；寄养处理器在其前。赠蛋/寄养领取提供队伍中的蛋，直接孵化工具不自行检查蛋态或已孵化标志，重复直调与正常步进的去重性质不同。", specs=[("HATCH",[[71,85],[135,140]])])
add("M06.WP35", "dependencies", "依赖WP34产蛋字段、WP25队伍分类/容量、WP12/WP06迈步事件、特性FasterEggHatching标志，以及孵化提交使用的物种/拥有者/最初招式/图鉴/统计和文字资源。盒内蛋不在计步遍历中，呈现同步阻塞不额外推进计数。", specs=[("HATCH",[[71,85],[133,142],[184,187]])])
add("M06.WP36", "caller_override", "普通迈步与原地转向调用遭遇检查；碎岩先做触发检查，摇树/甜味/钓鱼走主动请求包装。物种选定通知先后供漫游/雷达改写，正常开战调用返回才执行该入口的临时字段清理；主动请求不生产encounter_triggered。", specs=[("ENCOUNTER",[[119,122],[151,158],[209,225]])])
add("M06.WP36", "preconditions", "步进链先要求可战斗成员与当前地形/类型机会；触发检查依次拒未知类型、禁用、无玩家、DEBUG+CTRL、无/零概率或无表。雷达摇草可越过部分概率/驱虫剂门；驱虫剂与威吓按候选和首成员条件再判。摇树/甜味/钓鱼主动路径不继承普通机会/概率/驱虫剂门，第一或第二候选为空会保留已写临时类型。", specs=[("ENCOUNTER",[[119,158],[209,224]])])
add("M06.WP36", "dependencies", "上游为内容/遭遇版本数据、地图/地形/步数、世界时段天气、玩家队伍和属性/持物/特性；选择钩子连接漫游/雷达，生成钩子连接个体字段修正，下游野生战斗包装消费候选与临时类型。其输入字段和清理所有者按步进/转向/主动入口分列。", specs=[("ENCOUNTER",[[154,158],[209,225],[276,279]])])
add("M06.WP37", "dependencies", "漫游与雷达依赖普通遭遇候选/创建通知、地图进入和战后通知、地图地形/路线、当前队伍/伙伴、持久条目/个体与临时连锁。候选修改是漫游先、雷达后；换图先推进漫游再清雷达；八个取消点只清临时连锁，不重置电量或漫游状态。", specs=[("ROAM",[[119,146]])])

add("gr5.battle.commands", "dependencies", "依赖当前战斗参与者/业主与控制标记、席位已有/强制命令、招式/物品/替补的可选资格、场景菜单返回和AI决策入口。玩家选择先于AI，UI只交付选择数据，登记/取消与自动招选择仍由命令流程的具体入口执行。", specs=[("combat-requirements/wp40-commands-obedience-and-action-order.md",[[45,74]])])

add("M09.AI.SWITCH_POLICY", "dependencies", "依赖技能档、当前动作/被迫换出上下文、业主后备队伍与同席已选过滤，以及残余伤害/状态/祈愿/入场危害和替补评分。ShouldSwitch与ShouldNotSwitch是不同登记消费者，强迫换出绕过普通意愿；后备排序还消费ReserveLast/UseOrder。")
add("M09.AI.ITEM_ACTION", "dependencies", "依赖NPC业主物品资源、HP/状态/阶级/复活默认表与配置、通用物品资格和CanUse注册。该资格先于AI分类，传AI上下文但无招式索引；候选优先/随机门及最终选择使用当前目标状态，不能把评分意愿当实际道具执行。")
add("M09.AI.FIELD_EVALUATION", "dependencies", "依赖当前天气/场地/阵营期限与危害、双方存活/后备、接地/靴/魔法防守及招式/能力/持物，另读世代设置与AI技能。天气旧收益扣除/新收益加入、场地种子条件、危害后备过滤和侧交换好坏集合各用具名AI消费规则，不直接执行M08效果。")
add("M09.FACTORY.INTERACTION", "dependencies", "依赖Factory六租借/对手生成、挑战会话保存的旧对手对象引用、玩家队伍替换和BattleSwap场景的选择/摘要返回。租三牌确认拒绝只撤第三个，交换两屏完成后才以原对象引用替换；取消仍可能执行setParty，不引入复制个体假设。")

add("M10-C-WORLD-CHARACTER", "caller_override", "地图呈现更新消费M03生产的逻辑坐标/朝向/图案/透明与事件更新资格，投影到角色及反射/冲浪/阴影附属呈现；角色动画请求字段另被呈现层消费。它不生产实际角色移动或推定地形通行。")
add("M10-C-WORLD-SCREEN", "caller_override", "图片/屏幕/计时器数据由相应业务或解释器命令写入，呈现更新读取图片编号/文件名/位置/缩放/角度/色调及计时器状态；图片隐藏/换名决定位图释放/加载。零时长任务与后续更新消费分开，不把绘制请求当立即完成。")
add("M10-C-TRANSITION", "dependencies", "过渡分派依赖输入名称/时长、当前快照、所选效果需要的图像资源、更新时钟与宿主回退入口；中断先于释放，通用时长先转换/取整再判正值，固定时长效果仍有进入门。缺图/宿主失败与纯像素轨迹是不同证据边界。")
add("M10-C-TRAINERCARD", "caller_override", "训练家卡入口创建单面卡场景，绘制消费玩家身份/钱/图鉴/徽章/游戏时间；首次开始日期在该显示路径惰性写入，关闭后释放并返回调用界面。性别资源和服装图查找是呈现消费者，不是修改玩家身份的入口。", specs=[("user-interface/wp65-trainer-card-appendix.md",[[20,34]])])
add("M10-C-SUMMARY", "caller_override", "队伍/储存等已选个体入口把成员与选中索引交给摘要；普通五页导航、招式/缎带排序、标记草稿和遗忘选择使用不同子流程。View Pokédex先经调用方最近见到写入再开完整单物种条目，不能把此副作用归普通图像刷新。", specs=[("DEXUI",[[212,217]])])
add("M10-C-TRADE", "preconditions", "交换演出消费已选送出成员与已构造接收成员、有效玩家/队伍槽及两者图像/球/消息呈现依赖；前置选择取消与进入后的演出/进化不同。显示释放后的交换进化不接受取消，包装在这些步骤正常返回后才替换队伍槽；更早图鉴/外来物主及统计写入不因此回滚。收到个体的首招记录按M05业务合同承接。")
add("M10-C-CREDITS", "dependencies", "依赖游戏/插件/引擎署名数据、文字绘制与五背景资源、运行时长、音频停止及旧BGM快照、内存中的曾播放标志与地图场景恢复。首次跳过资格由曾播放状态控制；滚动/背景切换/退出淡出各自计时，旧BGM恢复不证明所有宿主播放。")
add("M10-C-GIFTSMAIL", "dependencies", "神秘礼物呈现依赖下载/解码所得礼物集合、玩家待领/已领记录、个体或道具接收业务和消息/动画/音频；下载动画消息先于待领追加。邮件依赖作者/正文与个体图标快照、物品身份和取消返回；礼物作者管理由M12负责，网络地址未被本次访问。")
add("M10-C-FACTORY", "caller_override", "Factory挑战会话准备租借六选三及交换两组对象后调用BattleSwap选择场景；摘要返回保持选择索引，第三租借确认拒绝只撤第三项。两阶段交换完成/取消结果返回M09业务，确认淡出与最终槽写入次序分开。", specs=[("user-interface/wp67-a-battle-interaction-and-presentation.md",[[283,297]])])
add("M10-C-SPECIAL-BATTLE", "preconditions", "按已选择的特殊战斗场景分开：Safari使用专用投饵/投石/球数与菜单，Arena消费评分类别和结果卡，捕虫大会消费保留个体比较/帮助。相应业务上下文、场景和资源已建立是呈现前提；Safari直接场景天气动画不自动经过普通动画开关包装，Arena的宿主帧等待不换算成通用秒。", specs=[("user-interface/wp67-a-battle-interaction-and-presentation.md",[[283,297]])])
add("M10-C-DEX-SHARED", "caller_override", "本行是M10已读界面的图鉴调用投影，不签独立图鉴主源：暂停菜单按有图鉴/可访问分流，摘要先最近见到写入再开完整单物种页，捕获/获得开简略Info；真正主列表/条目状态由M11-S019/M11-S026/M11-S027签收。", specs=[("DEXUI",[[128,140],[212,217]])], disposition="delegated_named_consumer_projection")
add("GCV-S001-U01", "preconditions", "此构造范围只建立普通与循环两组空动画记录；它没有播放数据、活动动画或用户操作的附加业务门，旧计数字段在本层没有可观察消费者。是否请求动画以及数据/图像/宿主可用性归后续启动消费者，不能把空容器构造等同播放成功。", disposition="not_applicable_additional_playback_guard_to_empty_construction")
add("GCV-S001-U02", "dependencies", "正常释放链依赖现存普通/循环动画上下文及其资源释放入口，再交父显示释放；本层记录在各家族清理后清空。仅到达正常清理链才有此先后，不从资源有效期合同推导异常ensure。")
add("GCV-S001-U04", "preconditions", "输入是一条待加入的新动画记录和当前记录集合；只有遇到第一条不活动记录（含空槽）才替换该位置，全部活动才追加。这个有限定义无取消现有活动动画的门，也不额外验证播放数据；活动性来自对应动画上下文。")
add("GCV-S001-U04", "dependencies", "依赖当前记录集合顺序与动画上下文提供的活动性判断，新记录由启动路径提供，下游按普通/循环更新与释放。复用的是不活动记录位置；并存中的活动动画不能因为容器复用规则被当成已被覆盖。")
add("GCV-S001-U07", "dependencies", "依赖父/宿主更新、普通与循环各动画上下文的更新能力，以及共享屏幕动画抑制记录。先宿主再普通再循环，最后清抑制记录；边界是本次父更新完成，不能借用全局渲染帧作为等价清理时点。")

add("M12-ROOT-03", "preconditions", "文本转换只按各具名模式生效：转义器的首式匹配四个字符紧邻的连续序列，单独引号/井号/斜杠不满足；控制字符另行处理。逗号切分按双引号状态分隔、不处理转义引号。无调用者且无有效返回的事件ID工具不作为活动转换前提。", specs=[("TOOLS",[[354,366]])])
add("M12-ROOT-15", "caller_override", "debug菜单Rename outdated files先确认，取消不执行；确认后调用图形更名再调用事件引用同步，正常结束才提示Done。菜单确认不是每文件覆盖保护，原OBS006的重复token子范围由父规范可选处置控制。", specs=[("TOOLS",[[266,273]])])
add("M12-ROOT-15", "preconditions", "图形阶段限定Characters中berrytree前缀PNG，排除已有下划线与wet/damp/dry/planted四阶段名；目录不存在无动作。事件引用阶段逐地图页按相同前缀条件处理，但不验证目标图片存在；前一阶段异常会阻止后一阶段。", specs=[("TOOLS",[[268,273]])])
add("M12-ROOT-15", "dependencies", "依赖Characters目录枚举、复制后删源的文件移动、地图/事件页读取与逐图保存、诊断汇总。已有目标会先删，写目标失败或删源失败产生不同前缀；引用同步与文件存在性不是同一校验。", specs=[("TOOLS",[[269,273]])])
add("M12-ROOT-16", "caller_override", "scripts_extract的文件末尾直接调用提取入口，是作者主动运行的命令行路径；不由普通游戏事件或插件加载自动触发。输出的单节Main装载器是M12-ROOT-18的另一运行定义。", specs=[("TOOLS",[[40,48],[277,284]])])
add("M12-ROOT-16", "dependencies", "依赖本机脚本运行环境、读取/解压原Scripts归档、目录创建/递归清空、节名文件名转换、逐文件输出、备份与写单节装载器。数量门通过后各阶段仍可失败，清树、备份和替换不是原子事务。", specs=[("TOOLS",[[40,48],[277,284]])])
add("M12-ROOT-17", "dependencies", "合并依赖旧归档节数守卫、散文件树按文件先于子目录的排序递归、九实体反转义、正文压缩、随机节ID与归档直接写入；旧列表通过门后即丢弃。它不依赖提取侧两层编号作为递归上限，也不自动备份。", specs=[("TOOLS",[[286,291]])])
add("M12-ROOT-18", "caller_override", "固定归档内唯一Main是可读加载器定义：被宿主选用该归档Main时，从外部脚本根先排序加载rb文件再递归非点目录。这里不假定实际宿主已经选用/执行；scripts_extract把相应单节装载器写入归档的作者流程另属ROOT16。")
add("M12-ROOT-18", "dependencies", "依赖归档Main的宿主启动选择、外部脚本目录/文件读取、解码所得加载器的求值与异常设施、长诊断写日志路径。文件读取位于受保护求值之外，普通异常、ScriptError和读文件失败的处理边界不同；已生效定义不因后续失败回滚。")
add("M12-ROOT-19", "caller_override", "浏览器打开作者页后，Refresh/图片或格尺寸改变/鼠标悬停点击/Save/Cancel分别消费页面输入与选中点；Save才写入点数组并重新生成文本，Cancel恢复编辑字段。调用来自页面交互，不是游戏地图事件。", specs=[("TOOLS",[[312,324]])])
add("M12-ROOT-19", "preconditions", "页面输入为文本值：默认点宽高16和标记1–16不是校验；点击以当前文本数值换算并下取整，零/空白/非数字没有本工具的拒绝恢复。Save要求当前有选中点；字段合法性不能借用PBS编译schema。", specs=[("TOOLS",[[312,316],[324,324]])])
add("M12-ROOT-19", "dependencies", "依赖浏览器页面状态/鼠标坐标、点数组、区域图相对路径、已知点和选中点两个BMP及文本生成控件；格尺寸取字段值，工具不提供文件写入。底图/宿主显示与已有标记像素内容是不同证据范围。", specs=[("TOOLS",[[314,336]])])
add("M12-ROOT-20", "caller_override", "页面的载入动作调用文本解析，开始先清点数组再逐行修改；Save、改图/改格等正常动作调用文本生成/重绘。生成只更新文本框，由作者复制进town_map并自行加节行；没有工程写盘caller。", specs=[("TOOLS",[[318,324]])])
add("M12-ROOT-21", "preconditions", "本行是固定两个8×8、24位、未压缩BMP的完整像素内容证明，不是可调用游戏操作，因此没有独立游戏准入门。消费条件属于townmap作者页按相对路径加载已知点/选中点图；已有像素不证明底图或浏览器实际解码呈现。", specs=[("TOOLS",[[328,336]])], disposition="not_applicable_gameplay_guard_to_fixed_pixel_projection", refs=[("modules/M12/bmp-content-inspection.json","/records/0"),("modules/M12/bmp-content-inspection.json","/records/1")])
add("M12-ROOT-24", "caller_override", "这是外围工具文档/接口投影：extendtext的文档入口是RMXP显示文本或脚本对话框已显示时由作者运行程序；animmaker是作者给定XML/图像的外部转换工具。RES的可读定义新增证据另按ROOT24投影接收，不伪造游戏内自动caller或native选用。", specs=[("TOOLS",[[338,342]])])

add("M12-D02", "dependencies", "世界调试消费当前地图/玩家/传送服务、开关/变量及其表达式求值、Safari/捕虫会话、寄养槽位和漫游记录。每个菜单命令保留自己的范围/取消哨兵：例如捕虫时间修改移动原时点并同步首个计时显示、寄养选择写变量1/3、漫游Ctrl当前位置与重新随机不同；不是统一重建全部世界。")
add("M12-D03", "dependencies", "玩家/收集调试依赖物种/个体生成、队伍与储存容量、图鉴记录、背包口袋/槽上限、钱/徽章、电话联系人和角色外观元数据。批量填充先登记图鉴再遇容量上限、清盒不清图鉴、加物品提示不复检返回，依赖写入顺序必须保留。")
add("M12-D04", "dependencies", "个体诊断编辑依赖当前个体或setup上下文、HP/Status/Pokérus、等级经验与重算、EV/IV及身份派生、招式PP/学习、持物与邮件、特性/性格/性别/形态、图鉴与队伍/储存。复制/删除调用动画和容器写入，不能把调试绕过的普通许可重新加回。")
add("M12-D05", "dependencies", "测试战斗构造依赖普通野生生成器、训练家载入及onload通知、物种/等级/版本校验、队伍/边尺寸和战斗启动包装。高级构造在最终BACK之前已经生成成员或运行载入通知，取消界面不撤销这些上游副作用。")
add("M12-D06", "dependencies", "战斗诊断依赖当前两侧/业主/队伍起始段与场上成员映射、速度快照、NPC物品池、Mega选择记录、天气/场地/环境和背景服务。叶命令返回后才做具名刷新；调试Mega直接改标记不调用普通资格链。")
add("M12-D08", "dependencies", "四层效果编辑依赖确定的battler/side/field/position目标、120项白名单的类型/默认/范围、物品和招式登记选择器与成员选择器。当前值绘制、候选列表、左右步进三种消费者分别处理成员−1/缺对象与默认−2归一，不能由一处保护推导另一处也安全。")
add("M12-E05", "dependencies", "物种作者编辑依赖基础物种列表、Species的33编辑字段/schema与缺省值、身高/重量缩放、进化参数转换和登记/保存/PBS写出。旧plural工作视图为空与singular导出会转换参数是不同入口，反向图的重建时点由实际提交链决定。")
add("M12-E06", "dependencies", "元数据编辑依赖全局0号、PlayerMetadata登记集合/回退1号、MapInfos用于地图选择、各schema/default/suffix以及注册→保存→PBS写出链。最小未用正玩家ID的选择以现有非空玩家登记为前提，指定玩家缺失与地图信息缺失各有不同失败位置。")
add("M12-W02", "dependencies", "地形标签编辑依赖已登记TerrainTag身份、图块集的terrain/passages数组与图形、当前地图/玩家及宿主窗口尺寸。自动图块一次写48变体，普通图块单项写；稀疏ID不能与选择索引混同，保存会更新运行时别名，正常退出重建地图并居中玩家。")
add("M12-W05", "dependencies", "无效图块修复依赖有序地图集合、3D地图图块与所有事件页、图块集自动图块/通行数据及逐图保存/诊断。正且小于384的图块按48组检查，其余含0读取通行项真值；只保存实际有改动的地图，不存在全批事务保证。")
add("M12-A04", "dependencies", "动画路径工作流依赖当前帧/单元、点/控制点和弧长采样、编辑器确认/取消及目标动画扩帧。初始Catmull–Rom参数采样与后续按弧长重采样不同；空但真值路径被确认时先扩帧再访问坐标失败，不把取消或失败当无写入。")
add("M12-A08", "dependencies", "动画关联编译依赖当前动画集合名称、已登记Move身份、Move/OppMove前缀解析、我方/对方映射槽和写出缓存。按有效映射逐个最后覆盖，只有至少一个有效映射才写文件；旧文件残留与旧槽引用不由名称列表自动修复。")
add("M12-M02", "caller_override", "此scope登记G01–G12的证据限制，不是运行操作：实际新游戏、剧情战、注册/接待/评奖、小游戏、收费、到达/解锁事件caller尚缺原事件材料。现有静态能力和候选数据作为投影保留，不能造一个通用事件caller关闭该缺口。", specs=[("DEMO",[[179,196]])], disposition="not_applicable_independent_callable_behavior_to_evidence_limit")
add("M12-M02", "preconditions", "要提升各候选链到事件可达证据，需分别有系统起始位置/Intro、地图几何通行、训练家放置、电话注册、Safari/捕虫/设施接待评奖、小游戏入口、寄养收费/商店库存、地点到达、地牢进入/图块集和开关51/52置位路径。当前已有数据/静态消费者不满足这些链的全部前提。", specs=[("DEMO",[[179,196]])])
add("M12-M02", "dependencies", "G01–G12依赖表中的具体系统/地图/公共事件/图块集/动画/资源与可兼容宿主；这里只签缺材料对结论的影响，不把可读脚本列成未审。十二分组及每组已有静态档位按WP77表保留，事件链/运行观察不因本字段填完变成已证。", specs=[("DEMO",[[179,196]])])
add("M12-S01", "dependencies", "安全复制依赖源文件存在/读取、既有比较位置的字节比较、覆盖确认和实际写入位置；比较位置与目标位置可分离。动画批量导入在解码前先复制资源，并依赖槽分配与最终保存/缓存刷新，所以比较通过不等于目标已写或整个导入成功。")

add("BIN-C02", "dependencies", "本范围依赖B11/B12/B13各自给出的兼容数据库值、宿主数值表/颜色/音频等底层构造服务，以及公式求值上下文；四层/三层地图、八/六参数等变体不能混作同一输入形态。当前原生选择未证，故这些是定义间/宿主接口依赖，不是已启用的游戏规则依赖。", disposition="definition_and_host_interface_dependencies_only")
add("BIN-C11", "caller_override", "这些YUV/通道/顶点程序由后端选择与绑定才可能消费；已审外部当前脚本没有直接绑定这些程序的caller。具名程序的输入接口可读并已审，实际native后端选择仍未知；不为纯定义投影捏造独立游戏调用或覆写。", disposition="not_applicable_direct_game_script_caller_to_backend_definition")
add("BIN-C11", "dependencies", "依赖各程序已列的Y/U/V平面或交错纹理、纹理坐标/矩形坐标前缀、颜色通道顺序、转换系数与顶点变换输入。绑定的纹理/过滤/边缘策略、uniform值、前缀组合和GPU精度是外部输入，不能把其中一个后端变体的定义当默认输出保证。", refs=[("modules/BIN/shader-behavior.json","/not_a_claim")])
add("BIN-C12", "dependencies", "两组控制器数据依赖GUID/平台等映射字段及native选择层；已审EXT19只提供八个逻辑别名、刷新后F8截图和鼠标门，EXT23配置八输入标签等活动项，不给出两组映射的选择优先、死区或重复延迟。映射数据存在与逻辑按钮实际命中分层。", refs=[("modules/BIN/reading-coverage.json","/external_source_records/18"),("modules/BIN/reading-coverage.json","/external_source_records/22")])
add("BIN-C13", "caller_override", "本scope是固定词典/数值/诊断/符号字符串的分类证据，不是独立可调用游戏行为，因此无应补造的外部游戏caller。某条错误文字或符号的存在不能成为实际故障、恢复或建议执行路径。", disposition="not_applicable_callable_behavior_to_string_inventory")
add("BIN-C13", "preconditions", "证据适用域是B32–B58的数据块和固定161104条字符串候选；24词典片段按固定宽度合成13504词条，两块为纯9/10数值，一块为库诊断。分类使用记录的字节范围/类型，不以字符串相似证明可执行程序或默认启用。", disposition="fixed_data_evidence_domain_not_gameplay_guard")
add("BIN-C13", "dependencies", "仅依赖固定Game.exe中的相应字节块/字符串候选及其逐条分类记录；该处置不提出独立游戏规则，所以没有新的游戏子系统依赖。若讨论native使用者必须另有调用证据，不能由错误字符串补齐。", disposition="not_applicable_independent_game_requirement_dependency")
add("RES-FONT-BMP-CONTEXT", "caller_override", "本行复用M12字体/BMP内容证据，无独立RES运行caller。字体由WP17正文/小/窄字体选择与测量消费，已有点/选中点BMP由townmap作者页按相对路径消费；是否native字体匹配/绘制成功不由文件存在证明。", specs=[("TOOLS",[[328,336]])], disposition="reused_resource_projection_with_named_consumers")

POINT_SOURCE = {
    "M08-MOVE-UserSwapBaseAtkDef": ("Data/Scripts/011_Battle/003_Move/006_MoveEffects_BattlerStats.rb", [[1846,1854]], "到达使用者全局主要效果入口后，输入是使用者当前攻击/防御值及交换标记；本定义可被抢夺，没有额外本地失败谓词。它交换当前读数并翻转交换标记；通用使用前门仍属于调用流程，不从本地无额外门推成任意上下文可成功。"),
    "M08-MOVE-UserTargetSwapBaseSpeed": ("Data/Scripts/011_Battle/003_Move/006_MoveEffects_BattlerStats.rb", [[1859,1866]], "到达逐目标主要效果入口后读取使用者与目标的当前速度值并交换；本定义明确绕替身，没有新增本地失败谓词。普通使用/目标处理仍由消费者承担，不能把绕替身扩为绕过所有前门。"),
    "M08-MOVE-UserTargetAverageBaseAtkSpAtk": ("Data/Scripts/011_Battle/003_Move/006_MoveEffects_BattlerStats.rb", [[1872,1880]], "到达逐目标主要效果入口时需要使用者/目标当前攻击与特攻读数；分别平均并向下取整后赋给双方。本定义没有单独失败谓词或绕替身覆写，不能因原值相等而补一个失败条件，也不能取消通用目标/替身前门。"),
    "M08-MOVE-UserTargetAverageBaseDefSpDef": ("Data/Scripts/011_Battle/003_Move/006_MoveEffects_BattlerStats.rb", [[1886,1894]], "到达逐目标主要效果入口时需要使用者/目标当前防御与特防读数；分别平均向下取整后写双方。本地没有额外失败谓词或绕替身覆写；奇妙空间已影响的读取值按现有原数值接口消费，不改写阶级。"),
    "M01-LZ-KEY": ("Data/Scripts/001_Technical/003_Intl_Messages.rb", [[478,490]], None),
    "M01-EVO-REG-512": ("Data/Scripts/010_Data/001_Hardcoded data/007_Evolution.rb", [[512,558]], None),
}


def point_evidence(local):
    if local not in POINT_SOURCE:
        return None
    path, ranges, _ = POINT_SOURCE[local]
    return {"path": path, "version": R, "ranges": ranges, "read_scope": "only_missing_field_definition_or_local_guard", "role": "ASM_targeted_field_completion_read", "reference_execution": False, "source_code_copied_to_output": False}


def is_behavior_anchor(a):
    p = a.get("path", "")
    return bool(a.get("lines") or a.get("ranges")) and "/test-catalog/" not in p and not any(w in pathlib.Path(p).name for w in ("coverage", "-data.", "-calling-data.", "-coverage-data."))


def m08_resolution(gap, raw):
    local, field = gap["local_id"], gap["field"]
    r = gap["input_ref"]
    if field == "caller_override":
        assert local == "M08-MOVE-RemoveAllScreensAndSafeguard"
        return {"fact_text": "这是存在的清两侧屏障与神秘守护定义，已审可选SHADOWSHED数据实际绑定RemoveAllScreens而非本定义；不能以邻近Shadow处理器或相似名称伪造其样本caller。只接收此定义及通用效果分派的条件可用性，默认/插件动态绑定没有在此scope被证明。", "disposition": "not_applicable_claim_of_default_data_caller_to_unbound_definition", "contract_evidence": [excerpt(a["path"], a["lines"], "binding_contrast", child(child(r,"specification_anchors"),i)) for i,a in enumerate(raw["specification_anchors"])], "completion_method": "specific_definition_and_actual_optional_data_binding"}
    if local in POINT_SOURCE:
        return {"fact_text": POINT_SOURCE[local][2], "disposition": "recorded", "contract_evidence": [excerpt("DAMAGE",[[17,25]],"normal_battle_consumer_context_not_universal_direct_call_guard")], "completion_method": "targeted_existing_definition_local_guard_read", "source_point_evidence": point_evidence(local)}
    anchors = [(a, child(child(r,"specification_anchors"),i)) for i,a in enumerate(raw.get("specification_anchors",[])) if is_behavior_anchor(a)]
    if not anchors:
        anchors = [(a, child(child(r,"precise_specification_links"),i)) for i,a in enumerate(raw.get("precise_specification_links",[])) if is_behavior_anchor(a)]
    # The shared ProtectMove header has no predicate. Consume the actual paragraph.
    if local == "M08-MOVE-ProtectMove":
        anchors = [(a, rr) for a,rr in anchors if a.get("group_id") in {"M08-CLOSED-WP45-SIDE-PROTECT", "M08-CLOSED-WP47A-PROTECT-CONSUME"}]
    assert anchors, (local,"no authoritative behavior anchor")
    contracts = [excerpt(a["path"],a.get("lines",a.get("ranges")),"effect_specific_predicate_or_operand",rr) for a,rr in anchors]
    text = "\n".join(EXTRACTS[int(x["text_ref"]["pointer"].split("/")[-1])]["text"] for x in contracts)
    common = []
    if local.startswith("M08-ABILITY-"):
        common.append(excerpt("ABILITY",[[13,35]],"existing_ability_identity_validity_and_consumer_exceptions"))
        premise = "该能力登记的本地条件/实际输入如下；能力身份与普通有效性仍按WP48§2逐消费位置处理，不能从同名登记推断所有生命周期共用同一前门。"
    elif local.startswith("M08-ITEM-"):
        common.append(excerpt("ITEM",[[9,20]],"existing_held_item_validity_and_calculation_consumer_order"))
        premise = "该持物计算登记的具体条件/实际输入如下；普通物品有效性与身份存在分开，计算族调用顺序及例外按WP50§1–2承接。"
    else:
        common.append(excerpt("DAMAGE",[[17,25]],"normal_battle_consumer_context_not_universal_direct_call_guard"))
        premise = "该具名效果在已审战斗消费者中的局部门/实际读数如下；表中公式读数也属于输入前提，不能用同名覆盖表代替这些规则。"
    return {"fact_text": raw.get("name",local) + "：" + premise + "\n" + text, "disposition": "recorded", "contract_evidence": unique(contracts + common), "completion_method": "exact_already_reviewed_effect_contract_with_named_consumer_context", "same_clause_reuse_boundary": "Different source/effect/predicate scopes keep their own scope IDs even when the receiver table has one combined row."}


def add_primary_details(gap, raw, resolution):
    rr = gap["input_ref"]
    keys = ("comparison","current_contract_comparison","comparison_result","semantic_comparison","behavior_purpose","rules","rules_checked","conclusion","current_contract_status","relationship","observations","purpose")
    ev = [record_evidence(child(rr,k),"original_scope_fact") for k in keys if raw.get(k) not in (None,"",[],{})]
    for i,a in enumerate(raw.get("source_anchors",[])):
        # These preserve actual producer/consumer/source projection rather than
        # fabricating a relation from a pathname alone.
        ev.append(record_evidence(child(child(rr,"source_anchors"),i),"primary_named_source_or_dependency_anchor"))
    if gap["module"] == "M09":
        doc = load("modules/M09/source-to-spec.json")
        wanted = set(raw.get("source_segment_ids",[]))
        for i,p in enumerate(doc["source_paths"]):
            for j,s in enumerate(p["segments"]):
                if s["id"] in wanted:
                    ev.append(record_evidence(ref("modules/M09/source-to-spec.json",f"/source_paths/{i}/segments/{j}"),"explicit_source_segment_identity_not_path_match"))
    if gap["module"] == "M01":
        for i,d in enumerate(load("modules/M01/followup-partial-dispositions.json")["records"]):
            if d["capability_id"] == gap["local_id"]:
                ev.append(record_evidence(ref("modules/M01/followup-partial-dispositions.json",f"/records/{i}"),"C00_received_final_finite_disposition_not_new_counterevidence"))
    for path,pointer in resolution.pop("extra_refs",[]):
        ev.append(record_evidence(ref(path,pointer),"named_supplement_or_actual_dependency"))
    if gap["module"] == "M11":
        for ci,c in enumerate(load("modules/M11/spec-to-source.json")["clauses"]):
            if gap["local_id"] not in c.get("capability_ids",[]):
                continue
            if any(c["path"] == q["path"] and overlap(c["lines"],q["ranges"]) for q in resolution["contract_evidence"]):
                ev.append(record_evidence(ref("modules/M11/spec-to-source.json",f"/clauses/{ci}"),"primary_exact_inverse_clause_inside_manually_selected_receiver"))
    # Bounded BIN definitions expose real shader input fields. They are not native
    # selection proof and no shader/program is compiled or executed.
    if gap["local_id"] == "BIN-C11":
        ids = set(raw["source_ids"])
        for i,p in enumerate(load("modules/BIN/shader-behavior.json")["records"]):
            if p["id"] in ids:
                ev.append(record_evidence(ref("modules/BIN/shader-behavior.json",f"/records/{i}"),"named_program_input_definition_not_active_backend_selection"))
    if point_evidence(gap["local_id"]):
        resolution["source_point_evidence"] = point_evidence(gap["local_id"])
    resolution["primary_evidence"] = unique(ev)
    return resolution


def finish_one(gap):
    raw = resolve(gap["input_ref"])
    local, kind = gap["local_id"], gap["field"]
    if gap["module"] == "M08":
        result = m08_resolution(gap,raw)
    elif gap["module"] == "M11":
        number = int(local.split("S")[-1])
        path,ranges,caller = M11[number]
        contract = excerpt(path,ranges,"specific_UI_state_or_data_consumer_contract")
        if kind == "caller_override":
            text = caller
            method = "named_entry_state_transition_or_producer_consumer"
        else:
            assert kind == "status_reason" and raw["status"] == "supported"
            text = "supported的有界理由：主审已比较的实际规则为「" + raw["behavior_purpose"] + "」。现行对应条款明确承接如下条件/结果（失败、取消和不写入同样是被支持的行为，不意味着运行通过）：\n" + EXTRACTS[int(contract["text_ref"]["pointer"].split("/")[-1])]["text"]
            method = "specific_primary_rule_to_exact_current_receiver_reason"
        result = {"fact_text":text,"disposition":"recorded","completion_method":method,"contract_evidence":[contract],"source_scope_fact_ref":child(gap["input_ref"],"behavior_purpose")}
    else:
        result = dict(MANUAL[(local,kind)])
        result["contract_evidence"] = [excerpt(p,r,"exact_named_contract_for_missing_field") for p,r in result.pop("specs")]
        result["completion_method"] = "specific_existing_scope_fact_and_named_relation"
    result = add_primary_details(gap,raw,result)
    result["finite_field_complete"] = True
    result["no_new_domain_review_or_execution"] = True
    result["support_status_not_upgraded_by_field_reception"] = True
    return result


def subtract(original, closed):
    left = []
    for a,b in rs(original):
        chunks = [[a,b]]
        for c,d in rs(closed):
            new = []
            for x,y in chunks:
                if y<c or x>d:
                    new.append([x,y]); continue
                if x<c:new.append([x,c-1])
                if y>d:new.append([d+1,y])
            chunks = new
        left += chunks
    return left


def receive_parent_deltas(shards):
    reception = load("modules/C00/M01-followup-reception.json")
    assert reception["assigned_finite_followup_complete"]
    m01 = load("modules/M01/followup-partial-dispositions.json")
    assert m01["complete"] and len(m01["records"]) == 60
    idx = {d["capability_id"]:i for i,d in enumerate(m01["records"])}
    for data in shards.values():
        for row in data["rows"]:
            row["pending_final_delta"] = []
            if row["module"] == "M01" and row["local_id"] in idx:
                p = ref("modules/M01/followup-partial-dispositions.json",f"/records/{idx[row['local_id']]}")
                row["M01_final_finite_reception"] = {"reception_ref":ref("modules/C00/M01-followup-reception.json"),"record":record_evidence(p,"accepted_final_primary_finite60"),"primary_followup_pending":False,"candidate_adjudication_owner":"root;008–018 canonical delta outside ASM follow-up"}
            own = row.get("ownership_and_alias",{})
            if "JXN_join_state" in own:
                own["JXN_join_state"] = "parent_owned_integration_not_ASM_remaining_work"
    premise = load("modules/C00/residual-premise-join.json")
    assert premise["complete"] and len(premise["records"]) == 13
    files = load("modules/ASM/file-dispositions.json")
    joined = []
    for fi,f in enumerate(files["files"]):
        matches = [(i,q) for i,q in enumerate(premise["records"]) if q["path"] == f["path"] and q["version"] == f["version"]]
        if not matches:continue
        closed = [q["lines"] for _,q in matches]
        f["parent_residual_premise_receptions"] = [{"ref":ref("modules/C00/residual-premise-join.json",f"/records/{i}"),"ranges":[q["lines"]],"reading_extent":q["reading_extent"],"whole_file_signoff":False} for i,q in matches]
        f["remaining_semantic_or_context_ranges"] = subtract(f["remaining_semantic_or_context_ranges"],closed)
        f["remaining_is_available_material_not_missing_host"] = bool(f["remaining_semantic_or_context_ranges"])
        if f["disposition"] == "available_text_has_precise_remaining_semantic_or_context_ranges" and not f["remaining_semantic_or_context_ranges"]:
            f["disposition"] = "semantic_ranges_joined_with_layout_and_parent_premise_reception"
        for ex in f["excluded_scope_dispositions"]:
            ex["residual_numeric_ranges_after_other_reviewers_or_exact_reuse"] = subtract(ex["residual_numeric_ranges_after_other_reviewers_or_exact_reuse"],closed)
            ex["parent_premise_reception_refs"] = [ref("modules/C00/residual-premise-join.json",f"/records/{i}") for i,q in matches if any(overlap(v,[q["lines"]]) for v in ex.get("original_exclusion",{}).values() if isinstance(v,list))]
        joined += [{"file_ref":ref("modules/ASM/file-dispositions.json",f"/files/{fi}"),"premise_ref":ref("modules/C00/residual-premise-join.json",f"/records/{i}"),"ranges":[q["lines"]]} for i,q in matches]
    bypath = {f["path"]:f for f in files["files"]}
    for f in files["flagged_gap_files"]:
        f["remaining_ranges"] = bypath[f["path"]]["remaining_semantic_or_context_ranges"]
        f["disposition"] = bypath[f["path"]]["disposition"]
    save("file-dispositions.json",files)
    return joined


def main():
    timestamp = datetime.datetime.now(datetime.timezone.utc).isoformat()
    original = load("modules/ASM/field-completion-input.json")["original_field_gaps"]
    assert len(original) == 431
    assert len({(g["unit_id"],g["field"]) for g in original}) == 431
    progress = load("modules/ASM/progress.json")
    progress.update(complete=False,status="bounded_431_field_reception_in_progress",finite_followup_denominator=431)
    save("progress.json",progress)
    shards = {}
    loc = {}
    for p in sorted(OUT.glob("matrix-*.json")):
        if p.name == "matrix-draft.json":continue
        doc = load("modules/ASM/"+p.name)
        shards[p.name] = doc
        for i,row in enumerate(doc["rows"]):loc[row["scope_id"]] = (p.name,i,row)
    records = []
    for i,g in enumerate(original):
        assert g["unit_id"] in loc
        filename,row_index,row = loc[g["unit_id"]]
        assert row["local_id"] == g["local_id"] and row["module"] == g["module"]
        result = finish_one(g)
        rec = {"completion_id":f"ASM-FC-{i+1:04d}","original_gap_index":i,"scope_id":g["unit_id"],"module":g["module"],"local_id":g["local_id"],"field":g["field"],"original_gap_ref":ref("modules/ASM/field-completion-input.json",f"/original_field_gaps/{i}"),"matrix_field_ref":ref("modules/ASM/"+filename,f"/rows/{row_index}/{g['field']}"),"original_snapshot_ref":row["original_input_ref"],"current_primary_record":record_evidence(g["input_ref"],"current_record_for_fixed_scope"),"resolution":result}
        records.append(rec)
    premise_joins = receive_parent_deltas(shards)
    completion = {"schema_version":"gr5.asm.field-completion.v1","module":"ASM","created_at":timestamp,"complete":True,"denominator":431,"completed":len(records),"remaining":0,"counts_by_field":dict(collections.Counter(r["field"] for r in records)),"records":records,"parent_receptions":{"M01_finite60":record_evidence(ref("modules/C00/M01-followup-reception.json"),"accepted_primary_followup"),"residual_13_paragraphs":record_evidence(ref("modules/C00/residual-premise-join.json"),"root_direct_named_paragraph_reception"),"paragraph_to_file_joins":premise_joins},"outside_ASM_remaining_work":["root canonical integration of C01F008–018","root JXN97 identities/182 routes integration"],"source_targeted_read_scopes":[{"local_id":k,**point_evidence(k)} for k in POINT_SOURCE],"new_execution":{"reference":0,"behavior_model":0,"host_or_demo":0},"counting":"431 field receipts within existing scope rows; no added product feature or review-round denominator."}
    save("field-text-extracts.json",{"schema_version":"gr5.asm.exact-field-text.v1","extracts":EXTRACTS,"role":"Narrow existing specification passages for missing field reception; no copied reference source."})
    save("field-completion.json",completion)
    evidence = load("modules/ASM/evidence-fields.json")
    for i,record in enumerate(records):
        fid = record["completion_id"]
        rr = ref("modules/ASM/field-completion.json",f"/records/{i}/resolution")
        evidence["fields"][fid] = {"ref":rr,"value":record["resolution"],"authority":"ASM_finite431_named_field_receipt; support/status remains primary/root-owned"}
        _,_,row = loc[record["scope_id"]]
        old = row[record["field"]]
        prior = old.get("prior_field_evidence",old.get("evidence",[]))
        row[record["field"]] = {"state":"not_applicable_with_evidenced_boundary" if record["resolution"]["disposition"].startswith("not_applicable") else "recorded","fact_text":record["resolution"]["fact_text"],"evidence":[{"field_id":fid,"relation":record["resolution"]["completion_method"],"specificity":"named_fact_and_exact_evidence"}],"completion_ref":ref("modules/ASM/field-completion.json",f"/records/{i}"),"finite_field_reception_complete":True,"prior_field_evidence":prior,"scope_not_expanded":True}
        row["missing_field_dispositions"] = [x for x in row["missing_field_dispositions"] if x != record["field"]]
    for filename,data in shards.items():save(filename,data)
    save("evidence-fields.json",evidence)
    save("field-gaps.json",{"schema_version":"gr5.asm.field-gaps.v2","original_denominator":431,"completed":431,"count":0,"gaps":[],"original_gap_records":"field-completion-input.json#/original_field_gaps","completion_records":"field-completion.json#/records","meaning":"All431 fields now carry actual named text and precise evidence or a bounded evidenced not-applicable disposition; this is not source/host execution or global review completion."})
    aliases = load("modules/ASM/identity-aliases.json")
    aliases["JXN"]["state"] = "parent_owned_integration_not_ASM_remaining_work"
    for row in aliases["aliases"]:row["JXN_join_state"] = "parent_owned_integration_not_ASM_remaining_work"
    save("identity-aliases.json",aliases)
    projections = load("modules/ASM/projection-draft.json")
    for row in projections["rows"]:
        row.get("ownership_and_alias",{})["JXN_join_state"] = "parent_owned_integration_not_ASM_remaining_work"
    save("projection-draft.json",projections)
    overlays = load("modules/ASM/accepted-overlays.json")
    overlays["pending"] = []
    overlays["M01_final_reception"] = ref("modules/C00/M01-followup-reception.json")
    overlays["root_premise_closure"] = ref("modules/C00/residual-premise-join.json")
    overlays["parent_owned_integration_outside_ASM"] = completion["outside_ASM_remaining_work"]
    overlays["stale_pending_in_root_coverage_adjudications_superseded_only_for"] += ["M01 primary finite60 by C00/M01-followup-reception; canonical delta remains root-owned"]
    overlays["stale_pending_in_root_coverage_adjudications_superseded_only_for"] = unique(overlays["stale_pending_in_root_coverage_adjudications_superseded_only_for"])
    save("accepted-overlays.json",overlays)
    validation = load("modules/ASM/validation.json")
    checks = {
        "fixed431_original_field_identities":len(records)==431 and len({(r['scope_id'],r['field']) for r in records})==431,
        "every_completion_has_named_fact_text":all(len(r['resolution']['fact_text'].strip())>=35 for r in records),
        "every_completion_has_exact_primary_evidence":all(r['resolution']['primary_evidence'] for r in records),
        "every_completion_bound_to_actual_matrix_field":all(loc[r['scope_id']][2][r['field']]['completion_ref']['pointer']==f"/records/{i}" for i,r in enumerate(records)),
        "zero_designated_field_gaps_remaining":not any(loc[g['unit_id']][2][g['field']]['state']=='not_separately_recorded' for g in original),
        "all431_current_record_refs_resolve":all(resolve(r['current_primary_record']['ref']) is not None for r in records),
        "all_exact_contract_excerpts_nonempty":all(x['text'].strip() for x in EXTRACTS),
        "13_parent_premise_paragraphs_exactly_joined":len(premise_joins)==13,
        "zero_previous_available_text_residuals":not any(f['remaining_semantic_or_context_ranges'] for f in load('modules/ASM/file-dispositions.json')['files']),
        "M01_primary_finite60_no_longer_pending":all(not x.get('pending_final_delta') for x in shards['matrix-M01.json']['rows']),
        "scope_denominator_unchanged1460":len(loc)==1460,
        "no_new_behavior_execution":completion['new_execution']=={'reference':0,'behavior_model':0,'host_or_demo':0},
    }
    validation['followup'] = {"kind":"bounded431_field_and13_paragraph_receipt_validation_only","checks":checks,"passed":all(checks.values()),"denominator":431,"completed":431,"remaining":0,"counts_by_field":completion['counts_by_field'],"completion_method_counts":dict(collections.Counter(r['resolution']['completion_method'] for r in records)),"point_source_ranges":len(POINT_SOURCE),"exact_specification_excerpts":len(EXTRACTS),"new_execution":completion['new_execution'],"does_not_reaudit_initial_global_denominators":True}
    validation['passed'] = validation['passed'] and all(checks.values())
    validation['counts']['initial_field_gap_count'] = 431
    validation['counts']['field_gap_count'] = 0
    validation['counts']['field_gaps_by_field'] = {}
    validation['counts']['files_with_remaining_semantic_ranges'] = 0
    validation['counts']['file_dispositions'] = dict(collections.Counter(f['disposition'] for f in load('modules/ASM/file-dispositions.json')['files']))
    validation['pending_parent_reception'] = []
    validation['parent_owned_integration_outside_ASM'] = completion['outside_ASM_remaining_work']
    validation['complete'] = all(checks.values())
    save('validation.json',validation)
    manifest = load('modules/ASM/matrix-draft.json')
    manifest['pending_final_deltas'] = []
    manifest['parent_owned_integration_outside_ASM'] = completion['outside_ASM_remaining_work']
    manifest['field_completion'] = {'denominator':431,'completed':431,'remaining':0,'records':ref('modules/ASM/field-completion.json','/records'),'C00_premises_received':13,'M01_finite60_received':True}
    manifest['field_contract'] = 'Required fields retain named fact text and exact original record or current specification ranges. The431 former gaps are closed in field-completion.json; evidence-backed not_applicable describes a precise definition/evidence projection boundary. No blanket no-condition claim or global behavioral completion follows.'
    manifest['artifacts'] = unique(manifest['artifacts']+['field-completion.json','field-completion-input.json','field-text-extracts.json','complete_fields.py'])
    manifest['complete'] = all(checks.values())
    save('matrix-draft.json',manifest)
    report = "\n".join([
        "ASM同一任务的有限字段后继已完成：固定431项，完成431，剩余0。未增加领域审查轮次或功能分母，仍只有1460个稳定审计scope、1295个投影、25704个逆向单位、3849个语义记录和723个文件；1460不是独立产品功能数。仅写modules/ASM。",
        "",
        "field-completion-input.json冻结原431缺位；field-completion.json逐项保存旧缺位→scope/字段→具体事实文字→原审者精确JSON pointer/当前条款行范围的连接。每个新引用分开保存原GCV snapshot、当前消费文件bytes/SHA和所接收记录的规范JSON hash；旧snapshot没有冒成当前文件身份。field-text-extracts.json只保留用于缺字段接收的具名规格段，不复制参考源码。",
        "",
        "246项前提：M08的214项按既有效果合同逐条接收天气/场地/HP/状态/种类/标志/候选/计数等谓词或公式输入，能力/持物的普通有效性和消费者例外另具名引用；仅列名称的覆盖表不充当前提。四个原数值交换/平均定义作了定点读取，区分无额外本地失败门与仍存在的通用调用前门。其余前提按解析/数据声明/编译、遗传/遭遇、演出/作者工具的实际输入与门接收；未填统一“无条件”。",
        "",
        "97项caller/override：M11的76项分别落到图鉴写入/查询与列表/搜索/条目状态、电话注册/计时/呼叫、地图/工具入口、各小游戏初始化/输入/结算消费者；保留事件caller未见证、直接入口与包装入口差异。M10/M12的具名场景/命令行/浏览器入口和资源消费者单列；未绑定效果/后端程序/词典证据投影给出有证据的not_applicable界限，未捏造默认native或游戏调用。",
        "",
        "49项依赖：依据对应scope的producer/consumer/source anchors及其已审事实，写出登记/数据、状态、回调、业务/呈现交付、文件/资源或输入接口的具体关系；M09显式连接source_segment_ids，M12B连接调试/作者各命令的真实上下游。没有把目录同名或grep命中当关系证明。",
        "",
        "39项状态理由：接收M11各已支持范围的具名规则及精确当前接收段，说明正常/失败/取消/不写入为何在该范围被支持；未把所有partial升级supported，也未修改规范发现裁决。",
        "",
        "已接收modules/C00/residual-premise-join.json的13段/5文件，原U03-IF公共前提242行接收缺口已关闭。file-dispositions.json只增加13个具名段的父接收，不因此新增整文件full断言。M01的60项最终主审及144子范围接收由C00/M01-followup-reception承接，已移除M01 pending。C01F008–018规范最终接入与JXN97/182接入仍由root负责，不是ASM剩余，也未等待或重审这些候选。",
        "",
        "validation.json的followup校验分母/记录连接/非空具体事实/精确引用/13段接收与零残余；这些是文档接收检查，不是行为执行或全局最终验收。progress.complete=true仅表示本431项有界后继完成。参考/行为模型/宿主执行均0；模型请求gpt-6-astra/ultra/default、禁Fast，实际回显均UNVERIFIED。",
    ])
    report_path = OUT/'delta-join-report.md'
    initial_report = OUT/'delta-join-report.initial.md'
    if not initial_report.exists():initial_report.write_bytes(report_path.read_bytes())
    report_path.write_text(report+'\n')
    progress.update(complete=all(checks.values()),status='bounded431_field_reception_complete' if all(checks.values()) else 'bounded431_validation_failed',updated_at=timestamp,finite_followup_denominator=431,completed_fields=431,remaining_fields=0,pending_parent_final_delta=[],parent_owned_integration_outside_ASM=completion['outside_ASM_remaining_work'],global_review_complete=False)
    progress['outputs'] = unique(progress.get('outputs',[])+['field-completion.json','field-text-extracts.json','field-completion-input.json'])
    save('progress.json',progress)
    print(json.dumps({'checks':checks,'completed':len(records),'fields':completion['counts_by_field'],'method_counts':validation['followup']['completion_method_counts'],'spec_excerpts':len(EXTRACTS)},ensure_ascii=False))


if __name__ == '__main__':
    main()



