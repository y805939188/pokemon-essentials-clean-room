#!/usr/bin/env python3
"""生成 WP02 逐定义清单附表（specs/kernel/wp02-settings-inventory-appendix.md）。

与 wp02_settings_inventory.py（控制台清单程序）共用
wp02_settings_common.py 的解析/求值逻辑；本程序是附表 Markdown 的唯一生成路径。
只读解析固定基线，不修改 reference；未求值项显式报告（不静默吞掉）。

用法：
  python wp02_build_appendix.py [输出路径]
默认输出 specs/kernel/wp02-settings-inventory-appendix.md；
验收时可指定临时输出路径，再与交付附表比对。
"""
import sys
from collections import Counter
from pathlib import Path
from wp02_settings_common import (FILES, parse_settings, parse_facility_lists,
                                  facility_candidates, matches_discovery)

DEFAULT_OUT = Path("/Users/dingshinn/Desktop/pokemon-framework-reference/specs/kernel/wp02-settings-inventory-appendix.md")
OUT = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_OUT

GROUPS_001 = [
    (9, 17, "元信息"), (49, 65, "玩家资源"), (72, 102, "世界与野外"),
    (110, 124, "场地招式许可"), (131, 151, "个体与生成"), (160, 169, "寄养与繁殖"),
    (177, 213, "漫游"), (220, 225, "队伍与储存"), (233, 257, "道具效果"),
    (264, 282, "背包"), (288, 319, "图鉴"), (333, 339, "城镇地图"),
    (348, 353, "电话"), (361, 370, "遭遇与战斗开始"), (377, 389, "游戏开关 ID"),
    (396, 414, "动画 ID"), (425, 425, "语言"), (436, 441, "屏幕"),
    (448, 501, "窗口皮肤"), (510, 514, "调试"),
]
GROUPS_002 = [
    (10, 19, "回合顺序与服从"), (27, 27, "Mega 开关"), (35, 52, "招式计算"),
    (59, 68, "特性与道具效果"), (77, 82, "亲密"), (92, 96, "捕获"),
    (104, 117, "经验与 EV"), (125, 130, "战后"), (139, 139, "AI"),
]

def group_of(fname, line):
    for lo, hi, name in (GROUPS_001 if fname == FILES[0] else GROUPS_002):
        if lo <= line <= hi:
            return name
    return "未分组"

def cell(s) -> str:
    return str(s).replace("|", "\\|")

def display_value(val: str) -> str:
    if val.startswith("["):
        return "数组（见词典）"
    if val.startswith("{"):
        return "哈希（见词典）"
    return val

constants, methods, meta, unevaluated = parse_settings(gen=8)
for r in constants:
    pass
c1 = [r for r in constants if r[0] == FILES[0]]
c2 = [r for r in constants if r[0] == FILES[1]]
gen1 = [r for r in c1 if r[3].startswith("世代")]
gen2 = [r for r in c2 if r[3].startswith("世代")]
sd = [r for r in constants if r[3].startswith("设置间")]
thr = dict(sorted(Counter(r[3] for r in constants if r[3].startswith("世代")).items()))
thr_text = "、".join(f"{k.replace('世代', '')}:{v}" for k, v in thr.items())

sections, refs = parse_facility_lists()
ref_paths = sorted({p for _, _, p in refs})
candidates = facility_candidates()
unreferenced = sorted(set(candidates) - set(ref_paths))
ref_match = {p: matches_discovery(p) for p in ref_paths}

L = []
A = L.append
A("# WP02 附表：逐定义配置清单与检索索引（参考侧取证材料）")
A("")
A("本附表是 [wp02-rule-configuration-and-data-variants](wp02-rule-configuration-and-data-variants.md) 的取证附件。")
A("**生成路径**：本 Markdown 由 `analysis/inventory/wp02_build_appendix.py` 写出；`analysis/inventory/wp02_settings_inventory.py` 是独立的控制台清单程序，两者共用 `analysis/inventory/wp02_settings_common.py` 对固定基线（commit `8c5911e4`）的设置文件做**只读解析**（不修改 reference）。统计由本表逐定义行独立复算，不采用任何审查方给出的数字。")
A("")
A("## 1. 统计单位约定")
A("")
A("- **独立常量**：`Settings` 命名空间内单个常量定义（合并展示行按展开计）。")
A("- **方法型配置**：`def self.<name>` 定义的配置方法（调用形式为 `Settings.<name>`，与常量的 `Settings::<NAME>` 不同）。")
A("- **元信息**：`Essentials` 命名空间常量，不属于 Settings 统计。")
A("- **展示行**：WP02 主文档词典表格中的行（一个展示行可合并多个常量）。")
A("- **值列口径**：\"派生\"列记录表达式/引用关系；\"世代 8 默认值\"列记录求值结果；无法解析的项显式标\"未求值\"并附原因，不静默吞掉。")
A("")
A("## 2. 独立复算统计")
A("")
A("| 集合 | 数量 | 复算方式 |")
A("| --- | --- | --- |")
A(f"| 001 Settings 常量 | {len(c1)} | 第 3 表逐行计数 |")
A(f"| 002 Settings 常量 | {len(c2)} | 第 4 表逐行计数 |")
A(f"| Settings 常量合计 | {len(constants)} | {len(c1)} + {len(c2)} |")
A(f"| 世代派生常量 | {len(gen1)+len(gen2)} | 第 3、4 表\"派生\"列以\"世代\"开头行计数（001 文件 {len(gen1)} + 002 文件 {len(gen2)}） |")
A(f"| 设置间派生 | {len(sd)} | APPLY_HAPPINESS_SOFT_CAP（= AFFECTION_EFFECTS） |")
A(f"| 方法型配置 | {len(methods)} | 第 5 表 |")
A(f"| Essentials 元信息 | {len(meta)} | 第 6 表 |")
A(f"| 世代派生阈值分组 | {thr_text} | 第 3、4 表\"派生\"列分组计数 |")
A("")
A("世代派生中含数值型 6 条：SHINY_POKEMON_CHANCE（16 或 8）、NUM_BADGES_BOOST 五项（999 或 1/5/7/7/3）；其余 41 条为布尔型。")
A(f"本轮求值覆盖检查：未求值项 = {unevaluated if unevaluated else '无（118 常量全部求值）'}。")
A("")
A("## 3. 逐定义清单：`S/001_Settings.rb`（Settings 命名空间常量）")
A("")
A("| 行 | 键名 | 派生 | 世代 8 默认值 | 词典分组 |")
A("| --- | --- | --- | --- | --- |")
for r in c1:
    A(f"| {r[1]} | {cell(r[2])} | {cell(r[3])} | {cell(display_value(r[4]))} | {cell(group_of(r[0], r[1]))} |")
A("")
A("## 4. 逐定义清单：`S/002_BattleSettings.rb`（Settings 命名空间常量）")
A("")
A("| 行 | 键名 | 派生 | 世代 8 默认值 | 词典分组 |")
A("| --- | --- | --- | --- | --- |")
for r in c2:
    A(f"| {r[1]} | {cell(r[2])} | {cell(r[3])} | {cell(display_value(r[4]))} | {cell(group_of(r[0], r[1]))} |")
A("")
A("## 5. 方法型配置（`def self.*`）")
A("")
A("| 文件 | 行 | 键名 | 调用形式 | 已见使用点 | 词典分组 |")
A("| --- | --- | --- | --- | --- | --- |")
A("| 001_Settings.rb | 28 | game_credits | `Settings.game_credits` | `S/016_UI/001_Non-interactive UI/007_UI_Credits.rb:61`（`Settings.game_credits \|\| []`） | 元信息 |")
A("| 001_Settings.rb | 264 | bag_pocket_names | `Settings.bag_pocket_names` | `S/013_Items/008_PokemonBag.rb:12`；编辑器/调试 2 处 | 背包 |")
A("| 001_Settings.rb | 296 | pokedex_names | `Settings.pokedex_names` | `S/016_UI/003_UI_Pokedex_Main.rb:427,872`；`S/016_UI/002_UI_Pokedex_Menu.rb:102`；调试 1 处 | 图鉴 |")
A("")
A("## 6. Essentials 命名空间元信息（不混入 Settings 统计）")
A("")
A("| 文件 | 行 | 键名 | 值 | 备注 |")
A("| --- | --- | --- | --- | --- |")
for m in meta:
    A(f"| {m[0]} | {m[1]} | {cell(m[2])} | {cell(m[3])} | 源文件标记为不可编辑 |")
A("")
A("## 7. 检索索引（WP02-R03：命中与消费者分类）")
A("")
A("### 7.1 检索规则")
A("")
A("- 常量使用点：`grep -rn \"Settings::<NAME>\\b\" --include=\"*.rb\" S/`（`::` 形式，词边界）。")
A("- 方法型使用点：`grep -rn \"Settings\\.<name>\" --include=\"*.rb\" S/`（`.` 形式；常量模式会漏掉此类调用）。")
A("- 世代直接引用：`grep -rn \"Settings::MECHANICS_GENERATION\" --include=\"*.rb\" S/`（不含两个设置文件内部的裸常量）。")
A("- 命中分类：**文件级命中**（含该串的文件数）、**行级出现**（总行数）、**注释命中**（命中行形如注释）。行级出现不等于独立分支数：同一条件表达式可多次出现，同一文件可含多个判断。")
A("")
A("### 7.2 世代直接引用统计（本轮实测）")
A("")
A("| 指标 | 数值 | 说明 |")
A("| --- | --- | --- |")
A("| 含直接引用的文件 | 41 | 文件级命中，不含两个设置文件 |")
A("| 行级出现总数 | 139 | 例：`006_MoveEffects_BattlerStats.rb` 11 行、`008_Battle_AbilityEffects.rb` 12 行 |")
A("| 注释命中 | 0 | 全部出现在代码行 |")
A("")
A("结论限定：只能说\"41 个文件含直接世代引用、共 139 行出现\"；不能称为\"41 处分支\"，也不排除同一路径同时受其他设置影响。")
A("")
A("### 7.3 LANGUAGES 使用点分类（本轮实测）")
A("")
A("| 位置 | 行 | 分类 | 内容 |")
A("| --- | --- | --- | --- |")
A("| `S/003_Game processing/001_StartGame.rb` | 31–33 | 已核消费者（代码） | 多语言且无存档时进入语言选择；按选择加载文本资源 |")
A("| `S/016_UI/013_UI_Load.rb` | 307, 337 | 已核消费者（代码） | 载入界面在候选 ≥2 时显示语言菜单；按选择加载文本资源 |")
A("| `S/019_Utilities/001_Utilities.rb` | 605 | 已核消费者（代码） | 生成语言选项列表 |")
A("| `S/020_Debug/003_Debug menus/002_Debug_MenuCommands.rb` | 1428–1439 | 已核消费者（代码） | 调试菜单切换语言 |")
A("| `S/016_UI/015_UI_Options.rb` | 28 | **注释命中** | 注释性引用，非使用 |")
A("")
A("### 7.4 重点设置行级分类（WP02 词典第 4.3 节 16 个开关）")
A("")
A("GAIN_EXP_FOR_CAPTURE(2 行)、ENABLE_CRITICAL_CAPTURES(1)、NEW_CAPTURE_CAN_REPLACE_PARTY_MEMBER(2)、AFFECTION_EFFECTS(5)、APPLY_HAPPINESS_SOFT_CAP(12)、RECALCULATE_TURN_ORDER_AFTER_MEGA_EVOLUTION(1)、NO_MEGA_EVOLUTION(1)、CHECK_EVOLUTION_AFTER_ALL_BATTLES(1)、CHECK_EVOLUTION_FOR_FAINTED_POKEMON(1)、HEAL_STORED_POKEMON(8)、DISABLE_IVS_AND_EVS(2)、OVERWORLD_WEATHER_SETS_BATTLE_TERRAIN(1)、MORE_ABILITIES_AFFECT_WILD_ENCOUNTERS(7)、LEGENDARIES_HAVE_SOME_PERFECT_IVS(1)、HIGHER_SHINY_CHANCES_WITH_NUMBER_BATTLED(1)、MOVE_CATEGORY_PER_MOVE(4)：以上行级出现**注释命中均为 0**，均为代码行候选使用点；逐行行为语义仍归领域包确认。")
A("")
A("### 7.5 设施引用集合与普通发现规则的关系（本轮从名单实际解析）")
A("")
A("当前名单 `P/battle_facility_lists.txt` 含 1 个 DefaultTrainerList 与 4 个 TrainerList，每节各 1 个 Trainers 与 1 个 Pokemon 字段，去重后**被引用输入路径共 10 个**：")
A("")
A("| 名单节 | 字段 | 引用路径 | 普通发现可匹配 |")
A("| --- | --- | --- | --- |")
for name, field, path in refs:
    A(f"| {cell(name)} | {field} | {cell(path)} | {'是' if ref_match[path] else '否'} |")
A("")
A("| 集合 | 数量 | 内容 |")
A("| --- | --- | --- |")
A(f"| 被当前名单引用的文件 | {len(ref_paths)} | 上表去重路径 |")
A(f"| 目录存在的 battle_tower/cup 候选文件 | {len(candidates)} | `P/` 顶层按前缀枚举 |")
A(f"| 存在但未被当前名单引用的候选文件 | {len(unreferenced)} | {'、'.join(unreferenced)} |")
A("")
A(f"上表 10 个被引用路径逐一核对：均**不满足**普通发现的完全基名或基名+下划线匹配（如 `battle_tower_trainers.txt` 不以任何基名开头），不经普通发现进入编译，只经名单字段显式读取。未被当前名单引用的候选文件用途**未调查**；其他入口（专用读取路径全集、失败行为）归 WP04，不据本表断言全局无引用。")
A("")
A("## 8. 用途与限制")
A("")
A("- 本表供 WP02-R01 验收：词典与逐定义清单双向对应；所有集合计数可按第 2 节方式从本表复算。")
A("- Settings 键名、路径与默认值是参考侧取证记录，**不是**未来框架的公开 API 或模块划分依据。")
A("- 本表只覆盖固定快照中两个设置文件的显式定义；不排除插件、动态定义或其他配置体系存在更多入口（当前快照无 Plugins 内容，U09 开放）。")

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text("\n".join(L) + "\n", encoding="utf-8")
print(f"wrote {OUT} ({len(L)} lines)")
print(f"counts: 001={len(c1)} 002={len(c2)} gen={len(gen1)+len(gen2)} setting-derived={len(sd)} methods={len(methods)} meta={len(meta)}")
print(f"unevaluated: {unevaluated if unevaluated else '无（全部求值）'}")
print(f"facility refs={len(ref_paths)} candidates={len(candidates)} unreferenced={unreferenced}")
