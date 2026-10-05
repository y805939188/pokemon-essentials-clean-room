"""Prepare exact text-only original synchronization; never writes specs/.

Own document/identity bookkeeping, not a reference behavior simulator.
"""
import difflib
import hashlib
import json
import pathlib
import subprocess

ROOT = pathlib.Path(__file__).resolve().parents[6]
OUT = pathlib.Path(__file__).resolve().parent
BASE = "407536adb682a04161d3e9c82f153a62b1becd97"
CONTRACT_PATH = "review/remediation/20261003-prepare/batches/B08/acceptance-stage-1/B09-downstream-contract.json"
CONTRACT = json.loads((ROOT / CONTRACT_PATH).read_text())
REF = "8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b"
changes = {}


def replace(path, ids, clause, old, new, evidence):
    entry = changes.setdefault(path, {"before": (ROOT / path).read_text(), "after": (ROOT / path).read_text(), "clauses": []})
    assert entry["after"].count(old) == 1, (path, clause, entry["after"].count(old))
    line = entry["before"].count("\n", 0, entry["before"].index(old)) + 1
    entry["after"] = entry["after"].replace(old, new, 1)
    entry["clauses"].append({"finding_ids": ids, "clause": clause, "before_lines": [line, line + old.count("\n")], "before_text": old, "intended_after_text": new, "source_evidence": [{"repository": "Maruno17/pokemon-essentials", "commit": REF, "path": p, "lines": lines} for p, lines in evidence]})


B = "Data/Scripts/011_Battle/001_Battle/"
T = "Data/Scripts/011_Battle/002_Battler/"
M = "Data/Scripts/011_Battle/003_Move/"
O = "Data/Scripts/011_Battle/007_Other battle code/"
S = "Data/Scripts/011_Battle/004_Scene/"
WORLD = "Data/Scripts/012_Overworld/002_Battle triggering/001_Overworld_BattleStarting.rb"
p39 = "specs/combat/wp39-battle-context-and-participants.md"
p40 = "specs/combat/wp40-commands-obedience-and-action-order.md"
p41 = "specs/combat/wp41-switching-positioning-and-escape.md"
p42 = "specs/combat/wp42-growth-end-of-round-and-battle-outcomes.md"
p38 = "specs/pokemon-rules/wp38-capture-and-receiving.md"

replace(p39, ["GIR-FD82-B009"], "§3.2 对视合并触发类型",
        "玩家触发的敌方（[2] 优先级）训练家事件",
        "事件接触触发类型 2 的训练家事件（不是显示层或渲染优先级；还须满足训练家标记、距离／可达、非跳跃、非覆盖触发等候选门）",
        [(WORLD, "458-476"), ("Data/Scripts/004_Game classes/008_Game_Player.rb", "284-297"), ("Data/Scripts/004_Game classes/007_Game_Event.rb", "142-162")])
replace(p39, ["GIR-FD82-B002"], "§4.3 首个失败与空计数边界",
        '3. **每训练家必需席位**：按业主映射统计该侧每位训练家"应占"席位；某训练家无任何席位 → 报错（玩家侧/对方侧各自具名）；必需 1 个而无 1 个可战斗成员 → 报错"…has no able Pokémon"。',
        '3. **每训练家必需席位与首个失败**：先比较需占位的业主范围与实际建立的可战斗计数范围，再逐业主比较席位需求。计数只在遇到可战斗成员时建立；缺失计数不自动规范化为 0。已有 NPC 对象的非空全濒死队伍可通过构造的非空门，但默认 1v1 中需求范围为 1、计数范围为空，先报 invalid-owner 错误，不到“has no able Pokémon”分支。若某个较早队伍段没有可战斗成员、较后段有，范围中间可为空值；范围长度门通过后，对空计数的数量比较可先失败，不能统一宣称消息分支可达。实际存在的计数项若无席位则有该侧具名错误；可比较的计数不足而必需席位为 1 时，才到“has no able Pokémon”分支。普通生成数据、已有对象与人为不完整段分别看待；不声称默认 PBS 一定提供异常队伍。训练家核心此前已触发开战记录并清创建期规则，失败不承诺回滚。',
        [(B + "001_Battle.rb", "98-103;365-380"), (B + "002_Battle_StartAndEnd.rb", "16-104"), (WORLD, "493-545")])
replace(p39, ["GIR-FD82-B003"], "§7.1 完整条款键及设置者边界",
        '**条款类键**（selfko/draw/modifiedselfdestruct/suddendeath/sleep/modifiedsleep/freeze/evasion/skillswap/sonicboom/ohko/selfdestruct/perishsong/souldew 等）由**设施规则对象在创建前直接写 `battle.rules`**（WP54–WP58 前向；`add_battle_rule` 不接受这些名字）',
        '**条款类键**使用完整兼容字面：selfkoclause、drawclause、modifiedselfdestructclause、suddendeath、sleepclause、modifiedsleepclause、freezeclause、evasionclause、skillswapclause、sonicboomclause、ohkoclause、selfdestructclause、perishsongclause、souldewclause（完整行为表见 WP54）。其中 drawclause、modifiedselfdestructclause、suddendeath 已有消费者，但固定设施设置文件没有对应设置包装；其余所列键有该文件的设置包装直接写入战斗内规则（WP54–WP58 前向；`add_battle_rule` 不接受这些名字）。sleep=true 不启用 sleepclause；skillswapclause 真时技能交换的目标门仍适用，不能被 WP47-B 的局部效果表取消',
        [(O + "006_Battle_Clauses.rb", "11-49;66-90;112-168;197-304"), ("Data/Scripts/018_Alternate battle modes/002_Battle Frontier rules/005_Challenge_BattleRules.rb", "1-103")])
replace(p39, ["GIR-FD82-B005"], "§12.2 伙伴·对手2个场景",
        "| 伙伴·对手 2 个 | 对手 2 | 伙伴参与；默认写 double |",
        "| 伙伴·对手 2 个 | 对手 2、已登记有效伙伴、noPartner 未开、无显式尺寸规则 | 伙伴参与；默认写 double；仅改为无伙伴或 noPartner 真则不参与，对手数量不创造伙伴 |",
        [(WORLD, "171-201")])
replace(p39, ["GIR-FD82-B015"], "§6.1 非正式上场的关系清理",
        "### 6.2 逐出与清除写入点",
        "未来攻击来源已离场但后备仍可战斗时，到期处理会先清当前存活成员指向来源保存席位的交叉关系，再读取来源个体的计算数据；这也可能解除现占位者建立的拘束，虽没有正式换入。来源仍在场时不发生这一次离场来源清理。具体黑色目光对照见 WP42 §5.1 延迟攻击及 R10，不要求未来实现采用临时对象构造。\n\n### 6.2 逐出与清除写入点",
        [(B + "011_Battle_EndOfRoundPhase.rb", "78-114"), (T + "002_Battler_Initialize.rb", "5-14;35-58;150-153;197-212;226-249;268-272")])

replace(p40, ["GIR-FD82-B001"], "§5.2 前置失败的两类历史",
        '清"最近招式"记录（特殊使用除外）、给',
        '无条件清“最近使用招式／类型”；仅普通使用同时清“最近常规招式／目标”，特殊使用保留这后一组；随后给',
        [(T + "007_Battler_UseMove.rb", "154-193"), (T + "009_Battler_UseMoveSuccessChecks.rb", "19-25;183-190")])
replace(p40, ["GIR-FD82-B008"], "§4.2 选择期效果存在门",
        '逐类型要求对应处理器存在且"可在战斗使用"通过',
        '类型 1／2 先要求对个体效果登记存在，类型 3 先要求对场上席位效果登记存在；类型 4／5 没有同样的效果存在门。各分支仍须取得有效个体并通过战斗资格判定；无战斗资格登记且未命中条件登记时默认允许（不是任意未知物品可用）',
        [(B + "009_Battle_CommandPhase.rb", "100-136"), (S + "003_Scene_ChooseCommands.rb", "208-230;260-314"), ("Data/Scripts/013_Items/001_Item_Utilities.rb", "96-114"), ("Data/Scripts/003_Game processing/005_Event_Handlers.rb", "154-160;192-195"), (B + "006_Battle_ActionUseItem.rb", "34-59;133-147")])
replace(p40, ["GIR-FD82-B006"], "§10 默认服从开关",
        '| `ANY_HIGH_LEVEL_POKEMON_CAN_DISOBEY` / `FOREIGN_HIGH_LEVEL_POKEMON_CAN_DISOBEY` | 按世代配置 | 服从门的触发集合 |',
        '| `ANY_HIGH_LEVEL_POKEMON_CAN_DISOBEY` / `FOREIGN_HIGH_LEVEL_POKEMON_CAN_DISOBEY` | 固定默认 false／true，各自可配置；不是世代推导值 | 任意高等级／仅外来高等级的触发集合 |',
        [("Data/Scripts/002_BattleSettings.rb", "13-19"), (T + "009_Battler_UseMoveSuccessChecks.rb", "107-126")])
replace(p40, ["GIR-FD82-B006"], "§12.2 高等级采样资格",
        '| 服从门·采样 | 等级 60、徽章 3（L=40，同上前提） | `a=⌊100×rand(256)/256⌋`；a≥40 即不服从 |',
        '| 服从门·采样 | 等级 60、徽章 3（L=40，同上前提）；个体外来且默认 ANY=false／FOREIGN=true，或显式 ANY=true | 抽样102／103分别得a39／40，高等级不服从门分别未命中／命中；命中不固定后续分支。仅改为当前玩家原拥有、默认开关时，不抽这一高等级随机并服从 |',
        [("Data/Scripts/002_BattleSettings.rb", "13-19"), (T + "009_Battler_UseMoveSuccessChecks.rb", "107-126")])
replace(p40, ["GIR-FD82-B005"], "§12.2 自伤先行入睡门",
        '| 不服从·自伤 | r−c<c 且非睡眠 | 混乱自伤伤害、终止 |',
        '| 不服从·自伤 | 已进入不服从第三分支、c=20、非睡眠；较早的入睡门未命中，例如可睡眠而r=20 | r−c=0<c，混乱自伤并终止；仅改r=0且可睡眠时，较早入睡门先命中，自我入睡并终止，不自伤 |',
        [(T + "009_Battler_UseMoveSuccessChecks.rb", "129-166")])
replace(p40, ["GIR-FD82-B005"], "§12.2 戏法空间比较前提",
        '| 戏法空间 | 开启、速度 100 vs 50 | 慢者（50）先；平局序不重抽 |',
        '| 戏法空间 | 开启、速度100与50；招式优先级与最终子优先级分别相同 | 慢者50先；非全量重排不重抽平局序。仅改速度100者招式优先级+1、速度50者0时，100者先 |',
        [(B + "004_Battle_ActionAttacksPriority.rb", "235-250")])
replace(p40, ["GIR-FD82-B005"], "§12.2 Primal资格",
        '| Primal | 无环无登记 | 可执行且无次数限制；不写 mega 槽 |',
        '| Primal | 存活、有合法Primal形态、尚未Primal；无环无登记 | 可执行且不受Mega次数登记门，不写mega槽；仅改为无可用Primal形态则拒绝，不执行 |',
        [(B + "008_Battle_ActionOther.rb", "180-199")])
replace(p40, ["GIR-FD82-005"], "§4.3 NearAlly选择登记与执行",
        '近身友→近身存活的友；',
        '近身友正常初选存在具名异常：固定3v3、使用者0、中央盟友2已倒下无后备、远盟友4存活时，初选4，成员／数据框可高亮4，但4的类别文本为空且按钮不呈选中态；不移动光标直接确认仍登记4。布局及存活条件保持、执行正常到目标解析时，远4被邻近门拒绝且无近侧存活盟友兜底。仅改为2存活时初选2且执行可接受；无存活非己同侧成员时回自身是另一分支，不概括为“无存活相邻即回自身”；',
        [(S + "003_Scene_ChooseCommands.rb", "333-439"), (B + "001_Battle.rb", "458-471;553-576"), (S + "005_Battle_Scene_Menus.rb", "60-65;514-535"), (B + "009_Battle_CommandPhase.rb", "60-97"), (T + "008_Battler_UseMoveTargeting.rb", "36-45;173-190")])
replace(p40, ["GIR-FD82-B001", "GIR-FD82-B008"], "§12.2 成对补充场景",
        '| 抢夺·接管 | 合格者标记 2/4；另有 0 与天空摔投者 |',
        '| 前置拒绝·历史 | 非濒死、非多回合，最近使用A／类型T、最近常规B／目标有效；治疗招受回复封锁，PP5；普通／特殊使用对照 | 两者A／T均清空、PP均5；普通同时清B／目标，特殊保留B／目标 |\n| 道具·空效果配置 | 合法注册I，类型5、可消耗、非重要非球、背包1；普通内部战斗、玩家存活可行动；无效果／资格／条件登记、无插件或中途变更 | 正常背包显示Use，默认资格允许，登记库存1→0；执行空效果但清物品选择、不退款。仅改类型1或3且对应效果缺失时，选择期拒绝、库存仍1 |\n| 抢夺·接管 | 合格者标记 2/4；另有 0 与天空摔投者 |',
        [(T + "007_Battler_UseMove.rb", "154-193"), (T + "009_Battler_UseMoveSuccessChecks.rb", "19-25;183-190"), (B + "009_Battle_CommandPhase.rb", "100-136"), (B + "006_Battle_ActionUseItem.rb", "34-59;133-147"), ("Data/Scripts/013_Items/001_Item_Utilities.rb", "96-114")])

replace(p41, ["GIR-FD82-B012"], "§6 Shift计数种类",
        '显式取消多回合与反击计数',
        '显式取消多回合与连斩连续使用计数；不清反击伤害量，反击目标只按位置交换重映射，正常回合末尾清理才另清反击记录',
        [(T + "007_Battler_UseMove.rb", "17-40;61-95"), (B + "001_Battle.rb", "602-634"), (B + "011_Battle_EndOfRoundPhase.rb", "713-735")])
replace(p41, ["GIR-FD82-B014"], "§8 用户伤害型换出",
        '在"已造成伤害、未濒死、对侧未全灭、目标未因其它原因换出、有可换入者"前提下执行同一末段',
        '在“实计成功击数>0、用户未濒死、对侧未全灭、至少一个目标未因其它原因换出、有合法后备”前提下执行同一末段。成功击数与实际HP损失分开，结冻头吸收可令实际HP损失0、实计击数1而仍通过换出门（中间伤害计算值1不等于损失1）',
        [(M + "013_MoveEffects_SwitchingActing.rb", "64-84"), (T + "007_Battler_UseMove.rb", "403-428;499-505;583-637;752-760"), (T + "010_Battler_UseMoveTriggerEffects.rb", "154-166"), (M + "002_Move_Usage.rb", "163-194;328-345"), (M + "003_Move_UsageCalculations.rb", "239-243")])
replace(p41, ["GIR-FD82-B005"], "§12.2 单打替补提示场景",
        '| 回合末·单打对侧替换 | 玩家侧可用、未濒死 | 出示提示；确认先换玩家席 |',
        '| 回合末·单打对侧替换 | 内部训练家战、玩家侧1席、switchStyle=true；对侧濒死且有合法替补；玩家存活、本轮未换、有合法后备、无暴走效果；无其它阻断 | 出示提示；确认并选择合法后备才先换玩家席。仅改switchStyle=false时不提示，其余对侧替补继续 |',
        [(B + "005_Battle_ActionSwitching.rb", "145-174")])
replace(p41, ["GIR-FD82-B012", "GIR-FD82-B014"], "§12.2 计数与零HP换出对照",
        '| Shift·目标指向 | 交换前着迷指向 A |',
        '| Shift·计数对照 | 合法3席、同业主0与2可换；U连斩计数2、反击伤害20、反击来源为未交换的敌席1；无其它清理 | Shift后连斩0、反击伤害20／来源1保留、U已行动；真正到达正常尾部才把反击记录置未设 |\n| 用户换出·结冻头 | 物理U-turn全前门及命中通过，T为EISCUE形态0／ICEFACE、无替身、模式破坏者假；双方存活，U有合法后备，对侧仍有可战斗成员，无其它换出／反伤／持物副作用 | 结冻头吸收，本击实际HP损失0、目标变形、实计击数1，后段允许U选择替换；仅改本击未命中且无成功击时不换出 |\n| Shift·目标指向 | 交换前着迷指向 A |',
        [(T + "007_Battler_UseMove.rb", "17-40;61-95;403-428;752-760"), (B + "001_Battle.rb", "602-634"), (B + "011_Battle_EndOfRoundPhase.rb", "713-735"), (M + "013_MoveEffects_SwitchingActing.rb", "64-84"), (M + "002_Move_Usage.rb", "163-194;328-345"), (M + "003_Move_UsageCalculations.rb", "239-243")])

replace(p42, ["GIR-FD82-B015"], "§5.1 延迟攻击关系副作用",
        '按位置下标扫描，计时／来源解析／实际调用；可嵌套招式、成长、裁判。计时到0后早退的辅助残留依WP45，不统一全清',
        '按位置下标扫描、递减计时；到0且目标存在存活时，先在当前存活同侧成员中按来源队伍身份查找。来源在场则复用，不发生离场来源的额外交叉清理；来源离场但后备可战斗时，先清当前存活成员指向保存来源席位的着迷、锁定、黑色目光、下颚锁、章鱼桶锁、天空摔投及束缚等初始化交叉关系，再读来源个体计算数据并实际攻击。此清理不是正式换入，仍可解除现占位者的关系；来源数据不带入其特性、道具与招式组。可嵌套招式、成长、裁判；计时到0后早退的辅助残留依WP45，不统一全清',
        [(B + "011_Battle_EndOfRoundPhase.rb", "78-114"), (T + "002_Battler_Initialize.rb", "5-14;35-58;150-153;197-212;226-249;268-272")])
replace(p42, ["GIR-FD82-D018"], "§5.1 远位自动调整完整判据",
        '当双方无近邻可交手时，在最多3席布局内寻找同一业主的空位／中央位；涉及两个侧的双席候选时按源排除相应交换。使用WP41交换合同，无完整再入场通知',
        '在最多3席的非单打布局，按§5.4先根据调整前分布收集所有侧的交换候选，再按同一计划执行；两席侧在全计划多于1项时跳过该侧候选，三席侧不套此门。使用WP41位置交换合同，无完整再入场通知',
        [(B + "011_Battle_EndOfRoundPhase.rb", "542-591"), (B + "001_Battle.rb", "458-471;553-576;602-634")])
replace(p42, ["GIR-FD82-D018"], "新增§5.4 全局计划及端点边界",
        '## 6. 正常战斗终局（WP42-D）',
        '### 5.4 远位自动调整的计划与执行\n\n只在阶段23实际到达且布局非1v1时处理。先以调整前的当前存活集合按侧0、侧1收集候选；本侧尺寸1跳过。对尺寸2／3的一侧，只要其任一存活成员与任一存活对侧成员邻近，就终止整个候选收集；此前候选不撤销。没有邻近对时，本侧每名存活成员的目标位置为：双席0↔2、1↔3；三席移到本侧中央2／3。仅来源与目标归同一业主才纳入计划，不另加目标必须有存活个体的门。\n\n候选全部收集后按计划顺序执行；候选总数大于1时，来源侧尺寸2的候选不执行，尺寸3的候选继续。实际交换仍要求两端席位已建立且同侧同业主；端点不存在则这一项失败且无移动消息，其余项继续。成功后显示横移／移到中央；不重新判邻近来取消后续已计划交换，不产生手动Shift的行动代价或完整入场通知，目标指向按WP41交换合同处理。\n\n3v3六席均已建立、每侧单业主、仅0／1存活、2／3中央已濒死无后备时，计划0↔2及1↔3并依序都成功，最终存活位置2／3；不能在先移一侧后停止。3v2五席已建立、同样仅0／1存活且各侧单业主时，计划仍含0↔2与1↔3，但双席侧那一项因总数2跳过，最终2／1。若3v3中0与2归不同业主、1与3同业主，则只有1↔3进入计划，最终0／3；原分布已经有近邻对时计划为空。所有例均为静态设计，不作实况证明。\n\n## 6. 正常战斗终局（WP42-D）',
        [(B + "011_Battle_EndOfRoundPhase.rb", "542-591"), (B + "001_Battle.rb", "458-471;553-576;602-634")])
replace(p42, ["GIR-FD82-B011"], "§9 R04正常灭亡歌链",
        '| R04 | 灭亡歌使双方全灭，同侧来源检查点及drawclause已将决定写2，反射壁1、畏缩真 | 阶段14调用成长后退出，反射壁仍1、尾畏缩未清、正在回合末标记可仍真；正常终局随后按结果处理 |',
        '| R04 | 普通1v1各侧唯一存活非蛋成员、歌声计数1且来源同为玩家侧；己方畏缩真、反射壁1、drawclause真；无改变该链的能力／物品／特殊模式 | 阶段13歌声归0→HP0→逐只正式濒死，畏缩已清假；检查点写2，阶段14成长后退出，反射壁仍1、正在回合末仍真。尾阶段未到不意味着更早清理回滚；对照两侧仍可战斗、无歌声归零、决定0且正常尾部到达时，反射壁1→0、回合末标记假 |',
        [(B + "011_Battle_EndOfRoundPhase.rb", "368-390;671-676;713-780"), (T + "003_Battler_ChangeSelf.rb", "64-100"), (T + "002_Battler_Initialize.rb", "128-178"), (O + "006_Battle_Clauses.rb", "25-37")])
partner = '伙伴实际参战时，玩家当前队伍与原合并参与集合的成员顺序可分离：满队接收移除玩家成员并左移玩家六格还原记录，合并参与集合仍保留旧成员身份。正常终局仍遍历该合并集合并按同一索引读已移位记录，因此送盒旧成员仍可被写入后继成员的物品，留队成员也可被写错。无伙伴路径的参与集合随玩家队伍同步，才有送盒成员退出这次循环的结论；仅有伙伴登记而未实际参战不构成此反例。还原先于外层伙伴治疗和世界拾取／采蜜，后续按当时实际当前持物消费；不把它等同每个成员自身原物品。'
replace(p42, ["GIR-FD82-B013"], "§6 接收后终局集合／记录不一致",
        '接收可能将成员放入／替换队伍并同步相关记录；',
        '接收可能将成员放入／替换队伍并左移相关记录，但不保证与伙伴合并参与集合保持身份对应。' + partner,
        [(WORLD, "182-201;388-394"), (B + "001_Battle.rb", "119-159;303-305"), (O + "005_Battle_CatchAndStoreMixin.rb", "15-79"), (O + "004_Battle_Peers.rb", "5-24"), ("Data/Scripts/014_Pokemon/001_Pokemon-related/004_PokemonStorage.rb", "38-44;170-175;231-249"), (B + "002_Battle_StartAndEnd.rb", "479-511")])
replace(p42, ["GIR-FD82-B015", "GIR-FD82-D018", "GIR-FD82-B013"], "§9 新增固定静态对照保留全部旧ID",
        '| E01 | 野生结束时旧决定1且捕获队列非空 |',
        '| R09 | §5.4的3v3／3v2固定分布，各席均已建立、每侧单业主、仅0／1存活且无后备 | 3v3计划两项并都执行，最终2／3；3v2双席侧项跳过，最终2／1；不在首项后重判近邻 |\n| R10 | 普通1v1，A从席0对T席1设Future Sight后换下到可战斗后备，B占0并在到期轮以黑色目光锁T；计数1，T非幽灵且攻击后仍存活，无其它解除关系副作用 | 来源A离场时，到期先清T指向0的黑色目光，再攻击，B未离场仍失去该拘束。对照A仍在场且T指向0时不发生这次清理 |\n| E14 | 满队A..F、A当前／还原X、B当前／还原Y、其余无物，X／Y合法且无本场被动效果；伙伴实际参战，双野生先倒一只再捕获最后一只，捕获者无物，询问档0送盒A、有盒空位，无额外成员／持物回调 | 接收后玩家B..F,捕获者，合并集合仍A..F,伙伴；玩家六格还原记录Y,空,空,空,空,空。正常终局盒中A改Y、留队B改空；无伙伴对照盒中A保留X、留队B还原Y。任意中间成员替换的映射见WP38 |\n| E01 | 野生结束时旧决定1且捕获队列非空 |',
        [(B + "011_Battle_EndOfRoundPhase.rb", "78-114;542-591"), (T + "002_Battler_Initialize.rb", "5-14;197-212"), (M + "013_MoveEffects_SwitchingActing.rb", "316-343"), (M + "005_MoveEffects_Misc.rb", "631-637"), (WORLD, "182-201"), (O + "005_Battle_CatchAndStoreMixin.rb", "15-79"), (B + "002_Battle_StartAndEnd.rb", "479-511")])

replace(p38, ["GIR-FD82-B007"], "§4 沉重球输入单位及有效重量",
        '| 沉重球 | 新档：',
        '| 沉重球 | 输入为**当前有效战斗重量，单位0.1kg**（先个体当前形态重量＋临时变化、下限1，再有效重量特性及道具修正，最终下限1；特性受模式破坏者抑制、道具按有效性门；引用WP48／WP50，不用物种基重替代）。新档：',
        [(O + "010_Battle_PokeBallEffects.rb", "125-147"), (T + "001_Battle_Battler.rb", "277-287"), ("Data/Scripts/014_Pokemon/001_Pokemon.rb", "903-905"), (O + "008_Battle_AbilityEffects.rb", "351-360"), (O + "009_Battle_ItemEffects.rb", "253-256")])
replace(p38, ["GIR-FD82-B013"], "§5 送盒退出还原的条件",
        '满队替换时换出到盒子的成员按**当前持物**送盒、退出结束时的还原循环（§6具名）。',
        '满队替换时换出到盒子的成员先按**当前持物**送盒；是否退出终局还原取决于参与集合与玩家队伍是否同步。伙伴实际参战的合并集合可继续保留该身份并用移位后的记录写错物品（§6具名），不能无条件承诺送盒成员退出。',
        [(WORLD, "182-201"), (O + "005_Battle_CatchAndStoreMixin.rb", "15-79"), (O + "004_Battle_Peers.rb", "5-24"), (B + "002_Battle_StartAndEnd.rb", "479-511")])
replace(p38, ["GIR-FD82-B013"], "§6 无伙伴／实际伙伴成员映射",
        '被送盒成员的还原记录随移位／删除不再作用于它：结束时的持物还原循环只对**届时仍留在队伍**的成员按还原记录恢复。两条结果分列（WP20明确交给本包的对照）：“还原记录X、当前持物已为nil”的合法暂时移除状态（暂时打落路径）——留队→结束还原X；**先送盒→保持nil**、退出还原循环。永久消耗可能连还原记录一起清（记录也nil时两路径都为nil）；不用普通消耗冒充该前提。',
        '无伙伴实际参战时，参与集合随玩家队伍同步，送盒成员退出正常终局还原；“还原记录X、当前物品空”的合法暂时移除状态（暂时打落路径）下，留队→正常终局还原X，先送盒→保持空。合法打落场景可限定为持抢夺机器的Shadow训练家捕获路径；不把野生对手／伙伴AI打落己方当默认已证路径。永久消耗可能连还原记录一起清，不用普通消耗冒充该前提。' + partner,
        [(WORLD, "182-201;388-394"), (O + "005_Battle_CatchAndStoreMixin.rb", "15-79"), (O + "004_Battle_Peers.rb", "5-24"), ("Data/Scripts/014_Pokemon/001_Pokemon-related/004_PokemonStorage.rb", "38-44;170-175;231-249"), (B + "002_Battle_StartAndEnd.rb", "479-511")])
replace(p38, ["GIR-FD82-B005"], "§9 W01普通捕获分支",
        '| W01 | A=100,B=100,率45,无状态 |',
        '| W01 | A=100,B=100,率45,普通非必捕球、非异兽、无状态、无调试；暴击捕获关闭或入口未命中 |',
        [(O + "005_Battle_CatchAndStoreMixin.rb", "229-260")])
replace(p38, ["GIR-FD82-B007"], "§9 W10阈值单位",
        '沉重球（率45基准）：2999／3000界、999／1000界、1999／2000界；率0',
        '沉重球新档（率45基准），下列均为当前有效战斗重量、单位0.1kg：2999／3000界、999／1000界、1999／2000界；率0',
        [(O + "010_Battle_PokeBallEffects.rb", "125-147"), (T + "001_Battle_Battler.rb", "277-287")])
replace(p38, ["GIR-FD82-B013", "GIR-FD82-B007", "GIR-FD82-B005"], "§9 W20限定与新增成对向量",
        '| W20 | 满队换出：被换成员还原记录X、当前持物nil（暂时打落的合法状态） | 留队成员→结束时还原X；被换出送盒成员→保持nil、退出还原循环；永久消耗且记录也nil时两路径都为nil（不用普通消耗冒充前提） |',
        '| W20 | 无伙伴实际参战、参与集合随玩家队伍同步、正常终局；满队换出成员还原X、当前持物空，合法暂时打落的Shadow训练家抢夺捕获路径，盒有空位、无其它持物回调 | 留队成员→结束还原X；被送盒成员→保持空、退出还原循环；永久消耗且记录也空时两路径都空。伙伴反例另见W21／W22，不把打落归默认野生或伙伴AI路径 |\n| W21 | WP42 E14的满队／伙伴实际参战固定输入；A..F当前及还原依次X,Y,空,空,空,空，捕获者无物，送盒A | 接收后盒中A先X；原合并集合仍A..F,伙伴，玩家六格记录变Y,空,空,空,空,空；正常终局盒中A改Y、留队B改空。无伙伴对照盒中A保留X、B还原Y |\n| W22 | 同W21但送盒中间D，A..F初始／当前物品依次I_A..I_F，均合法无被动；捕获者无物，无其它回调 | 玩家队伍A,B,C,E,F,捕获者；玩家六格记录I_A,I_B,I_C,I_E,I_F,空。合并集合仍A..F,伙伴，终局D虽在盒仍被写I_E、留队E被写I_F、留队F被写空。一般送盒第k名时，k以前记录不移，旧第k至倒数第二身份被写后继记录，旧末名被写空；无伙伴对照留队身份正确对应、送盒D保留I_D |\n| W23 | 1180（118kg）基底、临时变化0、有效LIGHTMETAL、无重量道具、模式破坏者假；非异兽、沉重球新档、基础率45、HP100／100、无状态／调试、暴击关 | 当前有效重量590（59kg）→率25→x8；仅改为该特性被抑制／无效时重量1180→率45→x15。无修正的300kg应输入3000并得+30，不能按300误判−20 |\n| W24 | W01同血量率状态，暴击开、拥有31种无护符、256域固定0、65536域固定0 | x15、y38527、c1；命中暴击并捕获，只需一次65536判定，不能要求四次普通通过 |',
        [(WORLD, "182-201"), (O + "005_Battle_CatchAndStoreMixin.rb", "15-79;229-260"), (B + "002_Battle_StartAndEnd.rb", "479-511"), (O + "010_Battle_PokeBallEffects.rb", "125-147"), (T + "001_Battle_Battler.rb", "277-287"), (O + "008_Battle_AbilityEffects.rb", "351-360")])


def identity(data):
    return {"git_blob": hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest(), "sha256": hashlib.sha256(data).hexdigest(), "bytes": len(data)}


manifest = {"run_id": "20261003-prepare", "batch": "B09", "role": "A-B09", "stage": "PREPARED_BEFORE_ORIGINAL_WRITE_SCOPE_REQUEST", "baseline_commit": BASE, "contract_path": CONTRACT_PATH, "original_write_authorized": False, "original_writes_performed": 0, "requested_authorization": "Authorize only the exact five original diffs bound below. The seven formal paths already authorized by the downstream contract remain the complete formal scope; no other originals, formal paths, public registries, history or reference changes are requested. If accepted, synchronize corresponding authorized final bodies/catalog cases in the complete later candidate.", "files": [], "static_cases_execution": 0, "runtime_observations": 0, "proven_demo_chains": 0, "source_execution": 0, "self_check_is_approval": False}
assert set(changes) == {x["original_path"] for x in CONTRACT["potential_original_sync_contract"]}
for path, entry in changes.items():
    before = entry["before"].encode(); after = entry["after"].encode()
    contract_before = next(x["original_input"] for x in CONTRACT["potential_original_sync_contract"] if x["original_path"] == path)
    assert all(identity(before)[k] == contract_before[k] for k in ["git_blob", "sha256", "bytes"])
    assert (ROOT / path).read_bytes() == before
    patch = ''.join(difflib.unified_diff(entry["before"].splitlines(keepends=True), entry["after"].splitlines(keepends=True), fromfile="a/"+path, tofile="b/"+path))
    patch_name = pathlib.Path(path).stem + ".patch"
    (OUT / patch_name).write_text(patch)
    manifest["files"].append({"path": path, "before": {"commit": BASE, **identity(before)}, "intended_after": identity(after), "complete_diff_path": str((OUT / patch_name).relative_to(ROOT)), "complete_diff_sha256": hashlib.sha256(patch.encode()).hexdigest(), "clauses": entry["clauses"], "approval_status": "PENDING_PARENT_SCOPE_AUTHORIZATION", "applied": False})
(OUT / "original-sync-proposal.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n")
print(json.dumps({"files": len(manifest["files"]), "clauses": sum(len(x["clauses"]) for x in manifest["files"]), "original_writes": 0, "diff_paths": [x["complete_diff_path"] for x in manifest["files"]]}, indent=2))
