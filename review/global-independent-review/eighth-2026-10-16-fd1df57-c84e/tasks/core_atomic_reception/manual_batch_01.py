"""Manually authored semantic children for the first fifty old locators.

This file is review data authoring, not a splitter or business model.
"""
import datetime
import json
import pathlib

P = pathlib.Path(__file__).resolve().parent
NOW = datetime.datetime.now(datetime.timezone.utc).isoformat()
LAYOUT = {
    1: "Classification and independent-contract designation; administrative type only.",
    3: "Scope declaration lists the subjects of the document; no operational totality claim accepted.",
    4: "Scope index entry: battle entry.",
    5: "Scope index entry: initialization/layout.",
    6: "Scope index entry: ownership/party segments.",
    7: "Scope index entry: Battler responsibilities.",
    8: "Scope index entry: rules/environment/hooks.",
    9: "Explicit subject exclusions and cross-document routing, not a completed receiver assertion.",
    10: "Explicit UI/facility exclusions and implementation-independence statement.",
    11: "Terminology table column headings.",
    26: "Core steps introduction.",
    34: "Timeline introduction and presentation instruction.",
    41: "Trainer wrapper subsection introduction.",
    46: "Wild-input scan subsection introduction.",
}

# Each list was authored by reading the complete text and actual reached source.
CHILDREN = {
 2: [
  "正文声称由批准WP39转写；批准和历史来源须由root历史接收证明。",
  "本正文不列源路径、类名、行号或证据URL；审计登记转交指定索引。",
  "保留字段名、配置键和身份名作为数据标识。",
  "保留标识不要求未来实现采用同名结构或接口。",
  "全部证据限定静态；没有游戏运行确认。",
 ],
 12: [
  "战斗上下文包含双方参与个体和训练家身份。",
  "战斗上下文包含双方侧尺寸。",
  "战斗上下文包含场地、侧和位置效果。",
  "战斗上下文包含场上席位。",
  "战斗上下文包含回合计数。",
  "战斗上下文包含当前决定码。",
  "战斗上下文包含本次战斗临时规则。",
  "这些行为状态不强制容器、构造顺序或类组织。",
 ],
 13: [
  "野生包装可先调用覆写钩子并按非nil截断值返回。",
  "野生包装核心正常返回后可调事后钩子。",
  "训练家包装可保存并合并待战训练家。",
  "野生和训练家包装使用各自结果归一条件。",
  "核心在创建前先执行skip查询。",
  "未skip核心调开始记录、创建并进入呈现包装。",
  "战斗正常返回后核心按顺序调用善后和结果写入。",
 ],
 14: [
  "player可战计数查询结果为0时skip查询真。",
  "仅DEBUG真且Ctrl按下时额外skip查询真。",
  "skip成立时核心返回skip helper结果，未到战斗构造和开始。",
  "本术语指未实际开战的取消路径；不覆盖后文skip helper可能写1的具体结果码。",
 ],
 15: [
  "创建前规则在game_temp.battle_rules累积。",
  "Battle构造建立独立rules字典。",
  "prepare按具体键写战斗属性或内部rules，随后清创建规则。",
  "两个字典的键和消费者须逐键核对，不能因同名规则概念合并。",
 ],
 16: [
  "交付战斗的成员集合保持输入和拼接顺序。",
  "实际伙伴参战时玩家和伙伴成员分别记录起点。",
  "对方为按训练家段拼接的集合或野生对象集合。",
  "集合包含同一Pokemon对象引用，字段变更可共享。",
  "伙伴参战时参与集合为新拼接数组，可与后续当前player.party顺序分离。",
  "行为合同不强制使用数组实现。",
 ],
 17: [
  "每位训练家的队伍段在交付集合中连续。",
  "各段用起始索引划分，尾端由下一起点或集合长度确定。",
 ],
 18: [
  "参战者对应场上席位索引。",
  "偶数席位属玩家侧。",
  "奇数席位属对方侧。",
  "每个初始化参战者保存Pokemon引用及参与队伍内索引。",
 ],
 19: [
  "席位所有者从侧内训练家及所属段/位置计算。",
  "可控制者包含玩家、伙伴或对方训练家。",
  "玩家拥有的查询只认可玩家本人，伙伴不因此成为玩家拥有。",
 ],
 20: [
  "决定0表示未决或中止。", "决定1表示胜。", "决定2表示负。",
  "决定3表示逃跑或弃权。", "决定4表示捕获。", "决定5表示平局。",
  "普通外层最终调用set_outcome把结果写入所选游戏变量。",
 ],
 21: [
  "伙伴可在创建期条件通过时作为玩家侧额外训练家。",
  "伙伴登记提供类型、名称、身份标识和成员集合。",
  "伙伴参战者由AI正常分支控制，controlPlayer等独立规则仍须保留。",
  "伙伴登记的写入、清除与身份版本读取属于WP24的独立接收。",
 ],
 22: [
  "野生包装接受分隔物种与等级参数。",
  "野生包装接受单参数物种/等级数组。",
  "野生包装接受已有Pokemon对象。",
  "can_override关键字默认false。",
 ],
 23: [
  "包装先调用generate_foes生成有序对手集合。",
  "分隔式和数组式新物种通过pbGenerateWildPokemon构造并进入生成修正链。",
  "已有Pokemon参数直接复用引用，不在此重构造。",
  "恰一个对手且can_override真才调on_calling_wild_battle。",
  "钩子收到原对手对象和初值[nil]的可变截断容器。",
  "截断容器首项非nil时直接返回该值，包括false，不进入核心。",
  "漫游、狩猎、捕虫等具体覆写接收者另需各具名完整合同。",
 ],
 24: [
  "未截断时包装把生成集合按对象参数传入核心。",
  "核心正常返回后仍以恰一个对手且can_override真为事后钩子门。",
  "事后钩子参数是当时对手species、level和原始outcome。",
  "雷达连锁怎样消费事后钩子仍属具名接收者。",
 ],
 25: [
  "野生包装对结果2返回false。",
  "野生包装对结果5返回false。",
  "野生包装其余结果返回true；此布尔不等于仅胜利。",
  "覆写钩子提前返回分支绕过本归一。",
 ],
 27: [
  "野生核心读取outcomeVar；nil或false时用1。",
  "野生核心读取canLose；nil或false时用false。",
 ],
 28: [
  "核心在开始记录和对象解析之前执行skip查询。",
  "查询真时直接调用skip helper并返回其结果。",
 ],
 29: [
  "未skip时核心先触发on_start_battle。",
  "当前登记的开始处理器记录全队战前等级。",
  "开始处理器清本轮相关计数；每个实际处理器的字段需独立核。",
 ],
 30: [
  "核心再调用generate_foes逐参数解析。",
  "对象分支直接加入原对象引用。",
  "包装传入这些对象，因此构造修正不因核心再解析重复。",
  "覆写钩子对对象的早先修改由同一引用带入核心。",
  "直接核心传物种/等级时在核心解析点首次构造。",
 ],
 31: [
  "核心调用set_up_player_trainers取得训练家、道具、成员和段起点。",
  "生成场景后把这些实际集合交Battle。",
  "把玩家侧段起点及伙伴道具赋给battle。",
  "尺寸规则为nil时设对手个数NvN；已有非nil规则不覆盖。",
 ],
 32: [
  "prepare_battle先应用创建规则。",
  "规则应用正常返回才清创建规则字典。",
  "动画包装内standby执行pbStartBattle。",
  "pbStartBattle正常返回才在同一动画块调用after_battle。",
  "动画包装正常返回后执行Input.update。",
  "随后set_outcome写变量并按结果处理统计。",
  "任一后段失败不意味着未到的善后/写结果仍执行，也不回滚已到前缀。",
 ],
 33: ["核心返回原始outcome，包装随后才作各自布尔归一。"],
 35: [
  "野生包装构造/修正发生在可选覆写检查之前。",
  "覆写未截断才进入核心skip。",
  "所以调试skip时包装已生成个体。",
  "未skip才调开始记录，并把同一批个体对象交战斗。",
 ],
 36: [
  "直接核心先skip。", "未skip才开始记录。",
  "开始记录之后才解析/生成。", "直接核心skip路径尚未生成输入个体。",
 ],
 37: [
  "合并探测条件成立时包装先解析训练家输入A。",
  "数据参数解析成功后触发A的on_trainer_load。",
  "合格单一A及其事件id存为waiting_trainer并返回false。",
  "第二事件传B正常进核心时先skip、开始记录，再解析B。",
  "B数据路径触发B的load钩子。",
  "waiting A以已有对象追加，直接复用而不再装载/触发load。",
  "A首次load钩子对对象的已提交修改保留。",
 ],
 38: [
  "探测中已解析但不满足单一训练家及队伍上限时不保存waiting。",
  "包装继续用原输入调用核心。",
  "核心不skip且原输入仍数据参数时可再次装载并触发load。",
  "该路径与已保存waiting对象复用的路径分开，不能统一一次装载。",
 ],
 39: [
  "普通训练家核心先skip，再on_start_battle。",
  "随后解析训练家输入。", "数据输入装载成功后触发load钩子。",
  "对象输入直接复用。", "解析及创建正常后才进入战斗。",
 ],
 40: [
  "已有NPCTrainer对象输入直接加入训练家集合。",
  "对象分支复用items和party成员，不调用pbLoadTrainer。",
  "对象分支不触发on_trainer_load。",
 ],
 42: [
  "合并探测要求无waiting、地图解释器运行且可双打三个条件同时成立。",
  "当前事件从地图解释器get_self取得。",
  "候选从pbTriggeredTrainerEvents([2],false,true)取得，2是事件接触触发类型。",
  "候选finder还须核训练家标记、距离/可达、非跳跃和非覆盖触发等实际门。",
  "包装排除当前自身事件。", "包装排除A自开关已真事件。",
  "恰一个其它候选才解析本次训练家输入。",
  "解析恰一个训练家且其party长度不超MAX_PARTY_SIZE才保存对象和当前事件id。",
  "保存后立即false返回，本事件不发起战斗。",
 ],
 43: [
  "已有waiting时把保存对象追加至本次输入。", "随后调用核心。",
  "本次数据参数按需装载，保存对象复用不重触load。",
  "核心outcome==1才设置waiting事件A开关。",
  "该分支正常完成后清waiting；中途异常无ensure保证清理。",
  "无waiting时直接以原输入调用核心。",
 ],
 44: ["训练家包装outcome==1返回true。", "其余结果返回false。"],
 45: [
  "训练家核心按解析结果保存对方训练家、items及段起点。",
  "Battle输入包含对方训练家集合。",
  "无尺寸规则时用训练家个数NvN。",
  "动画类型按实际battle.singleBattle?选1，否则3。",
  "set_outcome显式传trainer_battle=true，走训练家统计分支。",
 ],
 47: [
  "遇Pokemon对象且当前无待配等级物种时直接加入原引用。",
  "遇Pokemon对象但仍有待配等级物种时先抛缺等级错误。",
 ],
 48: [
  "遇数组且无待配物种时以Species.get(arg[0]).id校验/规范物种。",
  "数组把arg[1]直接交pbGenerateWildPokemon；不在本分支套分隔式整数范围校验。",
  "生成正常返回才把对象加入结果。",
 ],
 49: [
  "非对象/数组且没有待配物种时经Species.exists?判断物种，再暂存输入身份。",
  "有待配物种时下一值必须Integer。", "该等级必须在1..GrowthRate.max_level两端包含。",
  "非整数或越界先报等级错误，未构造这一个对象。",
  "合法等级生成正常后加入并清暂存物种。",
 ],
 50: ["无待配物种且Species.exists?为false时抛不存在物种错误。"],
}

# Exact pending receiver names reflect the assertion, not every foreign domain.
OPEN = {
 2: ["ROOT_CURRENT_HISTORY_AND_APPROVAL_TRACE"],
 13: ["WORLD concrete override and end-hook receivers", "UI animation/scene callback"],
 14: ["CRE actual player.able_pokemon_count receiver", "HOST Input press observation NOT_EXECUTED"],
 20: ["KERNEL pbSet game variable receiver"],
 21: ["CRE WP24 partner register/version/write-clear", "AI actual ordinary partner command selection"],
 23: ["CRE/WORLD pbGenerateWildPokemon complete producer", "WORLD concrete override handlers"],
 24: ["WORLD radar on_wild_battle_end receiver"],
 29: ["Complete actual on_start_battle handler records"],
 30: ["CRE/WORLD pbGenerateWildPokemon complete producer"],
 31: ["UI create_battle_scene constructor"],
 32: ["UI BattleAnimation/standby/Input receiver", "KERNEL game-variable/stat receiver"],
 35: ["CRE/WORLD pbGenerateWildPokemon complete producer", "WORLD actual override receiver"],
 36: ["CRE/WORLD pbGenerateWildPokemon complete producer"],
 37: ["CRE pbLoadTrainer actual receiver", "WORLD on_trainer_load concrete callbacks"],
 38: ["CRE pbLoadTrainer actual receiver", "WORLD on_trainer_load concrete callbacks"],
 39: ["CRE pbLoadTrainer actual receiver", "WORLD on_trainer_load concrete callbacks"],
 42: ["WORLD actual trainer-event finder and map interpreter receiver", "CRE trainer load"],
 43: ["WORLD map interpreter self-switch mutation", "CRE trainer load"],
 45: ["UI animation receiver", "KERNEL outcome/stat receiver"],
 48: ["CRE/WORLD pbGenerateWildPokemon complete producer", "DATA Species.get actual registry"],
 49: ["CRE/WORLD pbGenerateWildPokemon complete producer", "DATA Species/GrowthRate registry"],
 50: ["DATA Species.exists? registry"],
}

def source_for(number):
    path = "Data/Scripts/012_Overworld/002_Battle triggering/001_Overworld_BattleStarting.rb"
    if number == 2:
        return []
    if number == 12:
        return [{"path": "Data/Scripts/011_Battle/001_Battle/001_Battle.rb", "range": [93, 181]}]
    if 15 <= number <= 19:
        return [
            {"path": path, "range": [14, 68] if number == 15 else [171, 201]},
            {"path": "Data/Scripts/011_Battle/001_Battle/001_Battle.rb", "range": [215, 399]},
            {"path": "Data/Scripts/011_Battle/002_Battler/002_Battler_Initialize.rb", "range": [66, 91]},
        ]
    if number == 14:
        return [{"path": path, "range": [142, 168]}]
    if number == 20:
        return [{"path": path, "range": [338, 350]}, {"path": "Data/Scripts/011_Battle/001_Battle/002_Battle_StartAndEnd.rb", "range": [405, 568]}]
    if number == 21:
        return [{"path": path, "range": [171, 201]}, {"path": "Data/Scripts/011_Battle/001_Battle/009_Battle_CommandPhase.rb", "range": [187, 265]}]
    if 22 <= number <= 40:
        return [{"path": path, "range": [354, 440]}, {"path": path, "range": [451, 602]}]
    if 42 <= number <= 45:
        return [{"path": path, "range": [451, 602]}]
    return [{"path": path, "range": [411, 440]}]

manual = json.loads((P / "manual-atomic-clauses.json").read_text())
old = json.loads((P / "old-locator-disposition.json").read_text())
by_id = {row["id"]: row for row in old["rows"]}
existing = {row["id"] for row in manual["rows"]}
for number, texts in CHILDREN.items():
    locator = f"CORE-C{number:04d}"
    original = by_id[locator]
    ids = []
    for index, assertion in enumerate(texts, 1):
        ident = f"CAR-C{number:04d}-{index:02d}"
        ids.append(ident)
        if ident in existing:
            continue
        sources = source_for(number)
        for unit in sources:
            unit.update({"actual_reader": "/root/core_atomic_reception", "reading": "FULL_SOURCE_READ"})
        manual["rows"].append({
            "id": ident, "old_locator": locator,
            "spec": {"path": original["original"]["path"], "range": original["original"]["range"]},
            "assertion": assertion, "source_units": sources,
            "premise": "Fixed R ordinary definitions; actual parameter shape and reached earlier branches; callback normal completion only for later-step claims.",
            "producer_write_consumer_chain": "Actual BattleStarting entry branch and methods cited; identities and receiver names retained in the assertion, no method-list coverage credit.",
            "support": "SUPPORTED_BOUNDED_SOURCE_STATIC" if number != 2 else "ADMINISTRATIVE_STATIC_OR_HISTORY_OPEN",
            "pending_consumers": OPEN.get(number, []),
            "cancel": "Explicit skip/override/waiting and dialog cancellation remain separate branches; this atom does not promise later entry after early return.",
            "exception_partial_commit": "No enclosing transaction/ensure is inferred. An exception preserves already reached writes and may bypass later hooks, cleanup, result writes or waiting clear.",
            "persistence_reload": "Creation collections and battle rules are current-session references; any global field/variable save and reload receiver is independent. This atom makes no runtime roundtrip assurance.",
            "evidence": "SOURCE_STATIC", "business_execution": "NOT_EXECUTED", "manual_authored_utc": NOW,
        })
    original["manual_atom_ids"] = ids
    original["decomposition"] = "MANUAL_BY_ACTUAL_SEMANTIC_CHILDREN"
    original["all_children_received"] = not OPEN.get(number)
    original["status"] = "RECEIVED_BOUNDED_SOURCE_STATIC" if not OPEN.get(number) else "OPEN_EXACT_FOREIGN_RECEIVER"
    original["missing_action"] = OPEN.get(number, [])
for number, reason in LAYOUT.items():
    row = by_id[f"CORE-C{number:04d}"]
    row["decomposition"] = "MANUAL_NONBEHAVIOR_TYPE_DISPOSITION"
    row["all_children_received"] = True
    row["status"] = "LAYOUT_SCOPE_OR_NAVIGATION_ONLY"
    row["manual_type_reason"] = reason
    row["missing_action"] = []
manual["updated_utc"] = NOW
manual["frozen_subset"] = len(manual["rows"])
manual["global_atomic_denominator"] = "NOT_FROZEN"
(P / "manual-atomic-clauses.json").write_text(json.dumps(manual, ensure_ascii=False, indent=2) + "\n")
(P / "old-locator-disposition.json").write_text(json.dumps(old, ensure_ascii=False, indent=2) + "\n")
progress = json.loads((P / "progress.json").read_text())
progress.update({"updated_utc": NOW, "manual_atomic_frozen_subset": len(manual["rows"]), "manual_locator_frozen_subset": sum(bool(x["manual_atom_ids"]) for x in old["rows"]), "old_layout_disposed": sum(x["status"] == "LAYOUT_SCOPE_OR_NAVIGATION_ONLY" for x in old["rows"]), "old_bounded_source_received": sum(x["status"] == "RECEIVED_BOUNDED_SOURCE_STATIC" for x in old["rows"]), "old_locators_complete": sum(x["all_children_received"] for x in old["rows"]), "global_atomic_denominator": "NOT_FROZEN"})
(P / "progress.json").write_text(json.dumps(progress, ensure_ascii=False, indent=2) + "\n")
print(json.dumps({"utc": NOW, "manual_atoms": len(manual["rows"]), "manual_locators": progress["manual_locator_frozen_subset"], "layout": progress["old_layout_disposed"], "bounded_source_rows": progress["old_bounded_source_received"], "all_remaining_open": True}))
