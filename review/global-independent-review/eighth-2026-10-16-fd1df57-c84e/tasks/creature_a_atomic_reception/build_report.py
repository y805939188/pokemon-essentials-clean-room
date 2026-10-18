"""Static audit record assembly only. Never imports or executes reference code.

The hand-authored children below are bounded decompositions of original source
facts. They are deliberately NOT a claim to exhaust each whole formal clause.
"""
from pathlib import Path
import datetime
import hashlib
import json

OUT = Path(__file__).resolve().parent
BASE = OUT.parent.parent
RS = json.loads((BASE / "tasks/coverage_acceptance_incremental/dispatch/creature_a_atomic_reception.readset.json").read_text())
NOW = datetime.datetime.now(datetime.timezone.utc).isoformat()
READER = "/root/creature_a_atomic_reception"

# Every item was split by meaning, not by punctuation, method count or line count.
CHILDREN = {
1: ["个体物种内容查询使用个体基物种身份", "该查询使用简单形态而不直接调用动态形态读取"],
2: ["设置物种先严格解析目标记录", "目标基身份相同则在任何后继变更之前返回"],
3: ["异基物种写目标基身份", "有非负默认形态时优先采用", "否则目标自身正形态被采用", "两者均无则原存储形态保留"],
4: ["异基物种清强制形态", "新物种单性别时清性别缓存", "异基物种清等级缓存", "异基物种清特性解析缓存", "特性索引未在此清除", "最后请求能力重算，失败不撤销此前字段"],
5: ["forced_form非nil时普通形态直接返回它，包括0"],
6: ["战斗守卫为真时返回存储形态", "仓库守卫为真时返回存储形态", "上述守卫分支不请求getForm处理器"],
7: ["非守卫分支请求动态处理器", "结果为nil/false不提交", "结果与存储值相等不提交", "不同truthy结果经提交型form入口写回"],
8: ["显式form提交无同值早退"],
9: ["显式form先写形态并清特性缓存", "随后处理器正常返回才重算", "重算正常返回后条件向全局玩家图鉴登记"],
10: ["setForm先写存储形态", "让出点之前已经清特性缓存", "给定block在onSetForm之前执行，异常可阻止后段"],
11: ["simple形态写入存储形态", "simple形态写请求重算", "本入口不显式清特性缓存", "本入口不调用形态处理器或图鉴登记"],
12: ["等级缓存缺失时按当前经验与成长曲线求值", "求得等级被缓存，已缓存值直接返回"],
13: ["合法可比较等级超出1..上限时抛参数错误", "该越界失败先于经验和等级字段写入"],
14: ["普通非Shadow经验裸写保留请求值", "经验写入清等级缓存而不主动重算能力"],
15: ["正孵化步数判为蛋，零及负数不满足本谓词"],
16: ["等级达到上限时经验进度直接为0.0"],
17: ["HP设置把请求值夹到0..当前已计算上限"],
18: ["HP结果0请求异常治疗", "异常治疗对蛋早退，故蛋旧状态与计数可保留", "HP结果0清进化准备，不分蛋与否"],
19: ["异常设置先检查个体可用性", "不可用时即使非法输入也在解析前返回"],
20: ["合法异常设置只写规范状态身份，不改关联计数"],
21: ["可用要求非蛋且HP正", "濒死要求非蛋且HP非正，蛋不属于任一谓词"],
22: ["HP治疗对蛋早退", "异常治疗对蛋早退", "PP治疗对蛋早退", "完整治疗对蛋早退"],
23: ["非蛋HP治疗直接写满HP", "该单项治疗不经过HP归零清理路径"],
24: ["非蛋异常治疗把状态设NONE", "同次异常治疗把计数设0，濒死亦可到达"],
25: ["非负治疗索引直接访问所给槽", "不存在槽可在PP写入之前失败，不另作越界恢复"],
26: ["类型读取复制外层列表", "改返回列表的结构不改变存储类型列表"],
27: ["兼容第一类型读首项", "兼容第二类型缺失时回首项，入口发弃用提示"],
28: ["比例性别读取PID低8位", "低8位严格小于female_chance才为女", "首次结果写性别缓存"],
29: ["单性别或无性别物种设置性别时直接返回"],
30: ["普通异色仅在nil缓存时求PID与Owner ID异或判定", "普通结果独立缓存，不填超级缓存"],
31: ["超级异色仅在nil缓存时求同一异或两半再异或", "结果等于0才为超级，独立缓存不填普通缓存"],
32: ["超级异色setter写其缓存", "所写真值才强制普通异色真，假不清普通缓存"],
33: ["未缓存特性索引取PID最低位", "显式索引写入保留该输入", "索引写入清特性解析缓存"],
34: ["隐藏索引缺槽时局部解析回PID自然槽", "保存的隐藏索引不因此改变", "隐藏判定仍按保存索引>=2"],
35: ["合法已登记显式特性可写为覆盖", "不检查其是否在该物种候选表"],
36: ["自然候选枚举保留原位置", "隐藏候选枚举原位置加2", "空项跳过而不压缩索引，重合索引不合并"],
37: ["未缓存性格按PID模当前登记数量取登记键", "固定默认25键时才可把除数写为25", "结果写表现性格缓存"],
38: ["有计算性格覆盖时合法表现性格设置仍可改表现缓存", "该分支不请求能力重算"],
39: ["合法计算性格覆盖设置或清除后均请求重算"],
40: ["无参hasNature只检查当前表现缓存", "该查询不请求派生，不记录曾求值历史"],
41: ["未登记的非空合法类型道具身份在个体setter被忽略", "忽略分支保持原持物字段"],
42: ["邮件getter发现邮件无item或与现持物不匹配时清本方邮件引用", "读取本身可有写入副作用"],
43: ["默认招式只取等级可达条目", "重复身份保留最后出现位置", "仅取末尾至多四项", "每项新建招式对象而非复用旧PP"],
44: ["静默学习已有招式时移动原对象到末尾", "当前PP与提升计数随原对象保留"],
45: ["新身份静默学习先追加新对象", "超四时只移除首项一次，不循环截断异常长列表"],
46: ["首招整表记录先清旧表", "随后逐当前槽写身份，保留重复与顺序"],
47: ["逐项首招添加只对已登记身份处理", "已含同身份则不追加", "该守卫不清理原表已有重复"],
48: ["兼容检查教学表", "兼容检查等级表", "兼容检查可回溯蛋招表", "三者任一命中即真，未知招式假"],
49: ["个体可重学先拒蛋及Shadow", "存在当前等级可达且未掌握等级招则真", "首招记录中有未掌握身份亦真", "本谓词不读界面的更多招式配置"],
50: ["Owner setter先检查类别再替换引用", "替换不清普通或超级异色等派生缓存"],
51: ["Owner ID不同即外来", "Owner名字不同亦外来", "性别语言差异不参与该谓词"],
52: ["获得时间setter调用输入to_i保存整数秒", "getter从存值构建Time，不是返回原时间对象"],
53: ["孵化时间setter也调用to_i", "getter只有方式1才访问所存孵化秒数", "其它方式读nil而不检查所存时间"],
54: ["nil或空文本昵称清为空", "与当前物种名相等也清为空", "其余文本原样保存，本setter不截10字符"],
55: ["height读简单形态物种的0.1m值", "weight读简单形态物种的0.1kg值"],
56: ["有效IV对每一主能力读取强化标记", "标记truthy取31，否则原始IV", "不因此改原始IV容器"],
57: ["基础HP为1先返回1", "该特例先于禁用IV/EV配置处理"],
58: ["重算先计算六项再写新HP上限", "当前HP正时按上限差调整且至少1", "HP再经自身setter夹到新上限"],
59: ["当前HP零且上限增加时才写增量HP", "上限不增则该分支不写HP，保持濒死"],
60: ["普通clone新建IV容器并复制六主能力值", "普通clone新建ivMaxed容器并复制六键值", "普通clone新建EV容器并复制六主能力值", "两个对象后续对这些容器的原位写不互传，但重算须各自到达"],
61: ["普通clone未新建markings数组", "普通clone未新建mail对象", "普通clone未克隆fused所指个体", "共享对象的原位突变与仅替换本方引用是不同后继"],
62: ["创建直接赋物种happiness", "本入口无额外0..255夹制，仍要求其余创建依赖成功"],
63: ["普通创建末尾请求重算", "重算读取计算用性格，默认无覆盖时填表现性格缓存", "后续callback不清它时创建返回已缓存"],
64: ["只有初始存储形态0才进入创建复检", "recheck_form还必须为真"],
65: ["创建handler返回数字0仍为truthy", "因而也经form提交并按withMoves条件重建招式"],
66: ["Owner构造先建立以实参值为键的校验Hash", "相等键由后项条件保留", "名字0与后项gender0碰撞可遮蔽String条件", "仅与前项ID同值不能据此豁免后项String条件", "通过校验后才依次赋四字段"],
67: ["训练家转Owner复制现有language", "该转换不重读宿主语言"],
68: ["外来Owner省略language取2", "外来构造本身默认gender2，外来赠送包装默认gender0另算"],
69: ["非蛋队伍查询过滤nil与蛋并保序", "可用队伍再过滤濒死", "结果列表与原party成员共享对象身份"],
70: ["移除先拒越界索引", "必须有其它索引的可用个体才删除", "允许删除后数组压缩并返回true"],
71: ["Trainer构造在ID写入后读宿主语言前两字符", "固定七种映射及其它成功前缀回2", "语言读取异常先于party初始化且不回滚先写ID"],
72: ["Player钱包创建直接取Metadata.start_money", "该路径不调用money=夹制"],
73: ["同值角色编号或套装早退", "不同值先写字段", "随后地图角色存在才刷新，异常不保证撤销字段"],
74: ["四资源显式写先校验Integer", "合法整数各夹0..各自上限", "类型失败先于对应资源赋值"],
75: ["Pokedex.clear清各记录字段", "clear不重建解锁表", "清理后刷新可访问列表，失败不撤销已清字段"],
76: ["set_seen先归并有效基种并置true", "should_refresh=false只抑制刷新，不抑制该记录写入"],
77: ["合法物种的seen_form查询可懒建空表", "查询不是在全部状态下纯读"],
78: ["形态计数用两性别数组各2异色槽的长度作循环上界", "实际仅检查形态索引0及1", "高形态已见可被精确查询却不计入该数"],
79: ["直接末次形态写入不归并原键", "保留输入性别及形态异色三元组", "同一基种键仍会覆盖register所用同表槽"],
80: ["register输入为Pokemon时读取其gender和普通shiny", "性别>=2归0后写形态表"],
81: ["register只有last缺失或空列表才初始化末次三元组", "已有非空末次保持"],
82: ["最近见到入口总覆盖末次三元组", "保留个体原性别不把2归0"],
83: ["lock和unlock对任何负整数转全国槽", "超上界整数也转全国槽", "两入口写后刷新"],
84: ["当前地区模式刷新只检查该地区seen_any", "此分支不读取unlock位"],
85: ["清空长度零盒的非空计数为0", "empty为真且full也为真"],
86: ["容量先判box>=盒数返回0", "其它负盒号返回队伍上限，不验证该负地址存在"],
87: ["成员寻址只有-1代表队伍", "其它负盒号沿盒数组负索引寻址", "容量查询与成员寻址不能合并"],
88: ["复制到队伍先守满队", "成功追加源同一对象到队尾", "之后compact空项，显式目标索引不决定位置"],
89: ["基础storage.move在copy失败时不删源", "copy成功后才delete源，后段失败无事务保证"],
90: ["捕获存储可先治疗并恢复ready标记", "随后全满返回-1时治疗已经发生"],
91: ["RegionalStorage.move转调copy", "因此成功后源与目标均可持同一对象"],
92: ["RegionalStorage.delete引用未定义pkmn", "无外部定义时在实际删除之前名称解析失败"],
93: ["旧背景匹配使用原字面行锚正则", "首个匹配行数字转整数并先写背景", "随后才检查可用性，不可用又写默认", "匹配整行不等于整个多行文本只能含该行"],
94: ["进入storage screen先写in_storage真", "仅正常尾部清false，异常无全局ensure清理保证"],
95: ["取出先做满队守卫", "场景动画正常返回后才移动领域成员", "动画失败不保证尚未到达的数据移动"],
96: ["拿起先守最后可用成员", "场景动作正常后才保存held引用", "随后删源，队伍删源压缩"],
97: ["放下要求目标为空", "邮件与cannot_store拒绝只限盒子目标", "放回队伍空格不套这两门"],
98: ["释放确认默认No", "未通过前置蛋/邮件/cannot_release门时不开该确认", "同意后的动画/删除/消息仍有先后"],
99: ["个性描述只读六原始IV", "PID模6决定HP攻防速特攻特防环扫起点", "严格更大才替换，故并列首个保持", "获选IV模5决定对应语义，不用强化IV或计算能力"],
100: ["摘要先全国解锁时用全国号", "否则首个已解锁地区查号后立即停止", "该地区无号不继续后续已解锁地区"],
101: ["摘要图鉴选项先register_last_seen", "然后才打开完整单种场景", "后续BACK不撤销先写末次"],
102: ["尺寸辅助只读原始IV低4位", "PID只取低两字节", "高度取简单形态内容值", "两阶段整数数学分开，不抽随机或写个体", "固定*.rb只有定义命中，不据此排除地图或动态调用"]
}

def dump(name, obj):
    (OUT / name).write_text(json.dumps(obj, ensure_ascii=False, indent=2) + "\n")

def identity(path):
    data = path.read_bytes()
    return {"path": str(path.relative_to(BASE)), "bytes": len(data), "sha256": hashlib.sha256(data).hexdigest(), "blob": hashlib.sha1(("blob " + str(len(data)) + "\0").encode() + data).hexdigest()}

def consumer_for(n):
    if n <= 11:
        return {"local": ["Pokemon.species_data/form/species=/calc_stats", "Player::Pokedex.register"], "received": ["UI:X16", "CORE:CAR-CRE-F01", "CORE:CAR-CAA-J04", "KERNEL:SP01..SP13"], "open": ["all concrete MultipleForms callbacks/default+backup form records", "all actual form invocation paths"]}
    if n <= 16:
        return {"local": ["Pokemon.initialize/calc_stats/exp_fraction", "Trainer.pokemon_party/able_party"], "received": ["UI:S05/S06/S07", "CORE:CAR-CRE-F09"], "open": ["GrowthRate all complete definitions/curve records", "Shadow exp override and full growth consumers"]}
    if n <= 25:
        return {"local": ["Trainer.heal_party", "PokemonStorage.pbCopy/pbStoreCaught", "Battle::Peer.pbStorePokemon"], "received": ["CORE:CAR-CRE-F01..F03/F06/F07/F11", "UI:P02/P10/S04/S07/B08/B10"], "open": ["Shadow hp/heal overrides complete source", "all active item recovery handlers/interpreter/daycare/contest/facility callers"]}
    if n <= 40:
        return {"local": ["Pokemon.calc_stats/initialize/species_data"], "received": ["UI:S05/S06/S07/X25/X26", "CORE:CAR-CRE-F01/F09"], "open": ["full Nature/GenderRatio/Ability/Type records and concrete ability-changing callers", "wild/offspring mutations and default+backup content"]}
    if n <= 49:
        return {"local": ["Pokemon.initialize/reset_moves/learn_move/clone", "Utilities record-first before store", "CatchAndStore success first_moves"], "received": ["UI:P05/P07/P11/S07/S08/S09/S12/S13/X17/DATA01..DATA10", "CORE:CAR-CRE-F04/F05"], "open": ["all machine/Tutor/relearner handlers and teaching statistics", "Mail internal mutators/full WP64", "all move display hooks/PP effect consumers"]}
    if n <= 55:
        return {"local": ["Pokemon.initialize", "Owner.new_from_trainer/new_foreign", "Utilities foreign gift", "CatchAndStore snag-only Owner mutation"], "received": ["UI:S05/S06/S12/E03/E06", "CORE:CAR-CRE-F09/CAR-CAA-J02", "KERNEL:VAL01..VAL03/LANG01..LANG03"], "open": ["trade/hatch/MysteryGift complete producers", "all obedience/foreign language consumers", "malformed Owner downstream consumers"]}
    if n <= 65:
        return {"local": ["Pokemon.calcIV/calc_stats/clone/initialize", "Pokemon move PP setters", "PokemonStorage shared-object copy/healing"], "received": ["UI:S06/S09/S10/S11/B08/X24", "CORE:CAR-CRE-F08/F09", "KERNEL:SAVE01..SAVE07"], "open": ["native serialization alias/cycle behavior and real reload", "Shadow clone/saved_ev override", "mail/fused internal mutation chains", "all item/EV/wild/trainer/offspring writer composition"]}
    if n <= 74:
        return {"local": ["Owner/Trainer/Player complete constructors and setters", "Utilities foreign gift", "Player party/Pokedex"], "received": ["KERNEL:VAL01..VAL03/LANG01..LANG03/EVT04/EVT05", "UI:P03/P06/P11/S05", "CORE:CAR-CAA-J02/J03"], "open": ["Trainer GameData.to_trainer field override/full records", "movement charset/initial naming/shops/ash/resource consumers", "all license flag actual event writers"]}
    if n <= 84:
        return {"local": ["Player::Pokedex complete record APIs", "Pokemon.form=", "Utilities obtain paths", "CatchAndStore queue direct registration"], "received": ["UI:D01..D10/E01..E06/S05/S12/X15/X18/X29", "KERNEL:SAVE01..SAVE07", "CORE:CAR-CAA-J02/J03"], "open": ["regional helper/cache/compiler complete lifecycle", "actual regional/default species/form/map/encounter records", "all egg/evolution/shadow/recording writers"]}
    if n <= 92:
        return {"local": ["PokemonStorage and RegionalStorage complete definitions", "Utilities.pbStorePokemon", "Battle::Peer.pbStorePokemon", "CatchAndStore queue/old-member transfer"], "received": ["UI:B01..B12/X08/X18", "KERNEL:SAVE01..SAVE07", "CORE:CAR-CAA-J03"], "open": ["regional actual runtime selection/default registration", "complete daycare/purify/facility callers", "native alias preservation and real reload"]}
    if n <= 98:
        return {"local": ["PokemonStorage actual member/container receiver", "Pokemon setters/heal"], "received": ["UI:B01..B12/X08/X18", "KERNEL:SAVE01..SAVE07"], "open": ["full special-position downstream purify operations", "actual media/host output", "native serialization/reload"]}
    if n <= 101:
        return {"local": ["Pokemon raw IV/PID/Owner/name/height data", "Player::Pokedex register_last_seen"], "received": ["UI:S02/S05/S06/S12/E01..E06", "KERNEL:SAVE01..SAVE07"], "open": ["all actual species/region/showNature predicates from Shadow complete source", "native rendering/translation/real reload"]}
    return {"local": ["Utilities.pbSize complete mathematical definition", "Pokemon.height/iv/personalID getters"], "received": ["KERNEL:SP01..SP03"], "open": ["map/demo/plugin/dynamic callers", "actual target invocation; NOT_EXECUTED"]}

def main():
    assert set(CHILDREN) == set(range(1, 103))
    snapshots = json.loads((OUT / "received-snapshots/identities.json").read_text())
    packages = {p.name: json.loads(p.read_text()) for p in (OUT / "received-snapshots").glob("*.json") if p.name != "identities.json"}
    receptions = []
    for name in ["creature-save-events-contribution.json", "creature-species-compiler-contribution.json", "creature-validation-language-contribution.json"]:
        p = packages[name]
        receptions.append({"package": name, "original_reader": p["actual_reader"], "receiver": READER, "adopted_complete_fact_ids": [x["id"] for x in p["facts"]], "received_complete_semantic_payload": p, "receipt": "ACTUALLY_READ_COMPLETE_FACTS_AND_COMMON_PREMISES", "own_source_full_read_granted": False})
    receptions.append({"package": "creature-species-compiler-catalog-correction.json", "receipt": "ACTUALLY_READ_FULL_CORRECTION", "adopted": packages["creature-species-compiler-catalog-correction.json"], "effect": "SP14 Habitat exact sequence includes Mountain at index6; original frozen typo is not a formal defect"})
    ui = packages["creature-a-ui-package.v1.json"]
    receptions.append({"package": "creature-a-ui-package.v1.json", "reader": "/root/ui_wp66 for 73 source units; /root/ui_full for 5 parent units and exact wallpaper note", "intermediate_receiver": "/root/ui_full", "receiver": READER, "complete_source_unit_ids": [x["id"] for x in ui["complete_wp66_units"]], "complete_parent_unit_ids": [x["id"] for x in ui["complete_parent_units"]], "meaningful_payload_receipt": "ALL_73_PLUS_5_FULL_OBJECTS_AND_ALL_PREMISES_FACTS_ACTUALLY_READ", "identity_fields": "STRUCTURE_PARSED_AND_FIXED_PATH_HASH_VERIFIED; no source reading credit", "own_source_full_read_granted": False, "open": ui["not_granted"], "interfaces": ui["interfaces"], "note": "DATA01..10 only explicit finite fact meanings adopted; their assertion 'all fields read' does not transfer omitted raw fields as accepted values"})
    core = packages["creature-forward.v1.json"]
    receptions.append({"package": "creature-forward.v1.json", "original_reader": core["reader"], "receiver": READER, "adopted_complete_fact_ids": [x["id"] for x in core["rows"]], "received_complete_rows": core["rows"], "adopted_complete_joins": [x for x in core["bounded_joins"] if x["id"] in ["CAR-J04", "CAR-J05"]], "not_fully_received": [x["id"] for x in core["complete_manual_atoms"]], "reason": "Combined atom output was truncated in the middle; no aggregate46-atom credit. CAR-J01/02/03 reference those atoms and are not treated as received complete contributions.", "own_source_full_read_granted": False})
    receptions.append({"package": "creature-forward-supplement.v1.json", "original_reader": "/root/core_atomic_reception", "receiver": READER, "receipt": "ALL_FOUR_COMPLETE_FINITE_JOINS_ACTUALLY_READ", "payload": packages["creature-forward-supplement.v1.json"], "own_source_full_read_granted": False})
    atoms = []
    fact_rows = []
    for f in RS["full_original_source_fact_records"]:
        n = int(f["id"].rsplit("F", 1)[1]); cons = consumer_for(n)
        for idx, text in enumerate(CHILDREN[n], 1):
            atoms.append({"id": f"CAA-SF{n:03d}-A{idx:02d}", "parent_original_fact": f["id"], "formal": f["formal"], "assertion": text, "source_complete_unit": f["source"], "original_fact_full_record_read": True, "source_credit": "NAMED_COMPLETE_UI_RECEPTION" if 93 <= n <= 101 else "OWN_FULL_SOURCE_FILE_READ", "premises": f["premises"], "additional_bounded_premise": "Fixed standard definitions, valid conventional inputs except explicitly named counterexamples; normal dependencies until identified failure; no plugin/concurrent override.", "consumer_reception": cons, "support": "SUPPORTED_LOCAL_STATIC_MEANING; FULL_FORMAL_PARENT_NOT_EXHAUSTED", "persist_reload": "KERNEL SAVE04 top-level object graph received; Marshal alias/cycle/actual readback unproven; no blanket roundtrip claim", "normal_cancel_failure": "See complete original source unit, full formal context and consumer joins; early cancellation prevents only unreached writes; earlier reached writes have no inferred rollback.", "primary": f["formal"]["path"], "receiver": READER, "runtime": "NOT_EXECUTED"})
        fact_rows.append({"id": f["id"], "original_complete_record": f, "source_support": "SUPPORTED_BOUNDED_STATIC_AFTER_OWN_SOURCE_READ" if not 93 <= n <= 101 else "SUPPORTED_BOUNDED_STATIC_COMPLETE_UI_CONTRIBUTION", "child_ids": [f"CAA-SF{n:03d}-A{i:02d}" for i in range(1, len(CHILDREN[n]) + 1)], "sourcefact_decomposition": "MANUAL_SOURCE_FACT_CHILDREN_FROZEN", "whole_formal_clause_decomposition": "OPEN_NOT_GRANTED_BY_FACT_INDEX", "premise_status": "LOCAL_PREMISES_RECONSTRUCTED; TRANSITIVE_OPEN_LIST_RETAINED", "consumers": cons, "consumer_completeness": "OPEN_EXPLICIT_FINITE_RECEIPTS; DYNAMIC_DENOMINATOR_NOT_FROZEN", "business_execution": "NOT_EXECUTED"})
    # Three specifically named old table locators are independently exhausted.
    wp18 = RS["primary_formal_paths"][0]
    special = {
        107: [("species字段返回基物种身份", [7, 7]), ("公开species只有读取器，无同名直接accessor写入", [7, 7]), ("受控设置入口可切换物种并按§3.4副作用处理", [123, 138])],
        111: [("iv登记六主能力原始个体值", [45, 46]), ("iv getter提供可变容器且可整体替换", [45, 46]), ("ivMaxed登记计算上限覆盖标记", [47, 50]), ("ivMaxed容器可原位写或整体替换", [47, 50]), ("ev登记六主能力努力值", [51, 52]), ("ev容器可原位写或整体替换", [51, 52])],
        112: [(f"{a}为已计算能力的公开只读值", [53, 54]) for a in ["totalhp", "attack", "defense", "spatk", "spdef", "speed"]] + [(f"{a}在重算中写为当前计算结果", [1099, 1127]) for a in ["totalhp", "attack", "defense", "spatk", "spdef", "speed"]]
    }
    special_ids = {}
    for line, items in special.items():
        ids = []
        for idx, (meaning, source_lines) in enumerate(items, 1):
            aid = f"CAA-WP18-L{line}-A{idx:02d}"; ids.append(aid)
            atoms.append({"id": aid, "old_locator": f"CRE-LOC:{wp18}:L{line}", "formal_path": wp18, "line": line, "assertion": meaning, "source": {"path": "Data/Scripts/014_Pokemon/001_Pokemon.rb", "lines": source_lines}, "complete_source_file_read": True, "consumer": consumer_for(60 if line == 111 else 58 if line == 112 else 2), "support": "SUPPORTED_STATIC", "scope": "Normal fixed public field API and six-main-stat domain. Reflective/plugin mutation is not forbidden by the readonly wording.", "parent_decomposition": "MANUAL_EXHAUSTED_BOUNDED_TABLE_ROW", "consumer_closure": "OPEN_TRANSITIVE", "business": "NOT_EXECUTED"})
        special_ids[line] = ids
    # Consumer counterexamples are separate semantic observations, not new findings.
    atoms += [
        {"id": "CAA-COPY-MUTATE-01", "assertion": "普通clone之后直接向共享markings容器追加，来源与副本都可见；该能力由可变容器访问定义支持，固定脚本没有默认caller不移出分母", "source": "Pokemon accessors43–44/clone1135–1151", "consumer": "CI-11 direct-container vector", "support": "SUPPORTED_STATIC", "runtime": "NOT_EXECUTED"},
        {"id": "CAA-COPY-MUTATE-02", "assertion": "正常Summary Mark先克隆本地编辑表，确认时整体替换本方markings；它可拆开原先共享引用，不能把直接append示例当该UI的原位写效果", "source": "UI:S11 full facts and common premise; provider /root/ui_wp66", "consumer": "WP18 clone→Summary normal Mark→member field replacement", "support": "RECEIVED_BOUNDED_STATIC", "runtime": "NOT_EXECUTED"},
        {"id": "CAA-COPY-MUTATE-03", "assertion": "Storage Mark同样本地副本编辑、OK整体赋值；BACK不提交本次编辑而不回滚此前集合操作", "source": "UI:B08 full unit", "support": "RECEIVED_BOUNDED_STATIC", "runtime": "NOT_EXECUTED"},
        {"id": "CAA-COPY-MUTATE-04", "assertion": "PokemonStorage复制与Pokemon.clone是不同能力；前者复用同一整个Pokemon，治疗或能力变化可由另一容器地址看见", "source": "PokemonStorage178–204 and Pokemon heal/calc_stats complete files", "support": "SUPPORTED_STATIC", "runtime": "NOT_EXECUTED"},
        {"id": "CAA-COPY-MUTATE-05", "assertion": "Player/Storage分别作为顶层SaveData值进入保存并按顺序加载；不能仅由源内引用关系推导跨顶层序列化的别名、循环或真实重载保持", "source": "KERNEL SAVE01..SAVE07 received in full", "support": "BOUNDED_RECEIVED_WITH_EXPLICIT_OPEN", "runtime": "NOT_EXECUTED"}
    ]
    old = []
    for loc in RS["all_old_locators_exact"]:
        row = dict(loc); line = loc["range"][0]
        hit = loc["path"] == wp18 and line in special_ids
        row.update({"actual_receiver": READER, "formal_context": "FULL_READ_BY_SELF", "manual_children": special_ids[line] if hit else [], "decomposition": "MANUAL_EXHAUSTED_BOUNDED_TABLE_ROW" if hit else "OPEN_MANUAL_WHOLE_CLAUSE_DECOMPOSITION", "source_support": "CHILDREN_SUPPORTED_STATIC" if hit else "OPEN_WHOLE_CLAUSE_MAPPING; LOCAL_FACT_INDEX_IS_NOT_SUPPORT", "premise": "LOCAL_SOURCE_AND_EXACT_RECEIPTS_AVAILABLE; TRANSITIVE_OPEN", "consumer": "OPEN_EXPLICIT_SOURCEFACT_AND_INTERFACE_LISTS", "accepted": False})
        old.append(row)
    dump("manual-atomic-clauses.json", {"schema": "gr8-cre-a-manual-atoms/v1", "recorded_utc": NOW, "reader": READER, "atomic_denominator_frozen": False, "sourcefact_children_frozen_count": sum(map(len, CHILDREN.values())), "table_row_children": sum(map(len, special.values())), "consumer_observations": 5, "atoms": atoms, "warning": "Source-fact children are NOT exhaustive formal children; only named three old table locators have exhausted manual decomposition. No heading/line/semicolon count is an atomic denominator.", "business": "NOT_EXECUTED"})
    dump("sourcefact-consumer-receptions.json", {"schema": "gr8-cre-a-fact-reception/v1", "recorded_utc": NOW, "reader": READER, "original_facts_read": 102, "facts": fact_rows, "named_contributions": receptions, "snapshot_identities": snapshots, "all_original_empty_consumers_replaced_with_explicit_local_received_open": True, "all_consumers_closed": False, "no_whole_domain_pass": True, "business": "NOT_EXECUTED", "update": "UPDATE_NOT_STARTED"})
    dump("old-locator-disposition.json", {"schema": "gr8-cre-a-old-locator-disposition/v1", "exact_denominator": len(old), "manually_exhausted_locators": 3, "not_manually_exhausted_locators": len(old) - 3, "fully_accepted_locators": 0, "rows": old})
    print(json.dumps({"atoms": len(atoms), "sourcefact_children": sum(map(len, CHILDREN.values())), "whole_old_locator_decompositions": 3, "whole_old_locator_accepted": 0, "old_open": len(old) - 3, "facts_with_explicit_disposition": len(fact_rows)}, ensure_ascii=False))

if __name__ == "__main__":
    main()
