# 作者数据的读取范围与启用条件

各行描述该组早期静态取样。较晚的定点核对见[旧世代备份的字段与启用条件](generation-data-compatibility.md)和[材料与运行观察](observation-limits.md)。

对照下表时，分别核对格式机制、已知样本以及加载条件。仅在文件名出现在一份名单时，只能证明该引用存在。内容身份、调用条件是兼容对象，内部容器和类型组织由实现选择。

<a id="cfg-01"></a>
### CFG-01 · abilities.txt

**机制** WP48（特性能力计算：速度/重量/行动顺序、类型/命中/会心、伤害倍率）＋WP49（特性阶段触发：入场/离场、HP/状态/阶级、每击与整招、回合末四族）＋WP19 §3.4（特性派生选择）＋WP44（异常/阶级状态交界）

**已读样本与限制** WP34/WP35 孵化加速三个特性样本（abilities.txt:162,199,976——FastEggHatching 三特性）；不标「数据内容已读全覆盖」

**启用条件** 实际启用按 WP04 编译生命周期与 WP02 §6/§7（候选数据与未验证组合）保留，不据本表断言运行启用

**相关规格** [特性参与计算、免疫与有效性](../spec/battle/ability-calculation-modifiers.md)、[特性阶段触发、反应与连锁行为规格](../spec/battle/ability-phase-triggers.md)、[属性派生、特性选择与六项能力](../spec/creatures/attributes-ability-and-stats.md)、[有界效果归属与数据对应](../spec/battle/status-effects-coverage.md)、[异常状态、能力阶级与免疫](../spec/battle/statuses-stat-stages-and-immunities.md)

<a id="cfg-02"></a>
### CFG-02 · battle_facility_lists.txt

**机制** WP76（写出顺序与失败残留、编译边界）＋WP55（全 5 节消费）＋WP02 §6（名单引用关系）

**已读样本与限制** WP76（25 行全文）＋WP77 §4/§5（E34 全文 25 行）

**启用条件** 实际启用按 WP04 编译生命周期与 WP02 §6/§7（候选数据与未验证组合）保留，不据本表断言运行启用

**相关规格** [设施内容生成与模拟（挑战生成器——候选构造／合法性筛选／去重／评估与写出）行为规格](../spec/authoring/facility-content-generation-and-simulation.md)、[设施基础会话行为规格](../spec/battle/facility-session-and-restoration.md)、[规则配置档案与数据变体](../spec/core/rule-configuration-and-data-variants.md)

<a id="cfg-03"></a>
### CFG-03 · battle_tower_pokemon.txt

**机制** WP55（设施会话消费）＋WP76（候选个体生成机制）＋[设施名单的显式输入](generation-settings.md#设施名单的显式输入)（名单引用关系——不经普通发现，只经名单字段显式读取）

**已读样本与限制** WP76/WP55 头部格式样本（不声称全量逐条读取）

**启用条件** 实际启用按 WP04 编译生命周期与 WP02 §6/§7（候选数据与未验证组合）保留，不据本表断言运行启用

**相关规格** [设施基础会话行为规格](../spec/battle/facility-session-and-restoration.md)、[设施内容生成与模拟（挑战生成器——候选构造／合法性筛选／去重／评估与写出）行为规格](../spec/authoring/facility-content-generation-and-simulation.md)、[规则配置档案与数据变体](../spec/core/rule-configuration-and-data-variants.md)

<a id="cfg-04"></a>
### CFG-04 · battle_tower_trainers.txt

**机制** WP55（设施会话消费）＋WP76（训练家池机制）＋[设施名单的显式输入](generation-settings.md#设施名单的显式输入)（名单引用关系）

**已读样本与限制** WP76/WP55 头部格式样本（不声称全量逐条读取）

**启用条件** 实际启用按 WP04 编译生命周期与 WP02 §6/§7（候选数据与未验证组合）保留，不据本表断言运行启用

**相关规格** [设施基础会话行为规格](../spec/battle/facility-session-and-restoration.md)、[设施内容生成与模拟（挑战生成器——候选构造／合法性筛选／去重／评估与写出）行为规格](../spec/authoring/facility-content-generation-and-simulation.md)、[规则配置档案与数据变体](../spec/core/rule-configuration-and-data-variants.md)

<a id="cfg-05"></a>
### CFG-05 · berry_plants.txt

**机制** [树果种植](../spec/world/berry-plants.md)（种植/生长/收获机制）

**已读样本与限制** wp60（berry_plants.txt 多段样本）

**启用条件** 实际启用按 WP04 编译生命周期与 WP02 §6/§7（候选数据与未验证组合）保留，不据本表断言运行启用

**相关规格** [树果种植](../spec/world/berry-plants.md)

<a id="cfg-06"></a>
### CFG-06 · cup_fancy_pkmn.txt

**机制** 已查的默认名单与具名脚本未引用本文件。fancy 杯单双打均引用 _single 变体，其他引用未验证

**已读样本与限制** 早期清单仅核验文件存在，未读取其实际数据样本

**启用条件** 当前所查默认名单未选择本文件。全局用途及其他配置中的启用待证，见[设施名单的显式输入](generation-settings.md#设施名单的显式输入)。

**相关规格** [设施内容生成与模拟（挑战生成器——候选构造／合法性筛选／去重／评估与写出）行为规格](../spec/authoring/facility-content-generation-and-simulation.md)、[示例工程证据与能力覆盖](../spec/authoring/demo-evidence-and-capability-coverage.md)

<a id="cfg-07"></a>
### CFG-07 · cup_fancy_pkmn_single.txt

**机制** WP76/WP77（杯赛列表机制：名单查询/编译/反写/杯赛规则族——fancycup 节 Pokemon 字段引用本文件）

**已读样本与限制** 未读——[设施名单的显式输入](generation-settings.md#设施名单的显式输入)对应条目是名单引用的文件名行，不是本文件实际数据样本的阅读证据；保持样本阅读的真实限定

**启用条件** 实际启用按 WP04 编译生命周期与 WP02 §6/§7（候选数据与未验证组合）保留，不据本表断言运行启用

**相关规格** [设施内容生成与模拟（挑战生成器——候选构造／合法性筛选／去重／评估与写出）行为规格](../spec/authoring/facility-content-generation-and-simulation.md)、[示例工程证据与能力覆盖](../spec/authoring/demo-evidence-and-capability-coverage.md)

<a id="cfg-08"></a>
### CFG-08 · cup_fancy_trainers.txt

**机制** 已查的默认名单与具名脚本未引用本文件。fancy 杯单双打均引用 _single 变体，其他引用未验证

**已读样本与限制** 早期清单仅核验文件存在，未读取其实际数据样本

**启用条件** 当前所查默认名单未选择本文件。全局用途及其他配置中的启用待证，见[设施名单的显式输入](generation-settings.md#设施名单的显式输入)。

**相关规格** [设施内容生成与模拟（挑战生成器——候选构造／合法性筛选／去重／评估与写出）行为规格](../spec/authoring/facility-content-generation-and-simulation.md)、[示例工程证据与能力覆盖](../spec/authoring/demo-evidence-and-capability-coverage.md)

<a id="cfg-09"></a>
### CFG-09 · cup_fancy_trainers_single.txt

**机制** WP76/WP77（杯赛列表机制——fancycup 节 Trainers 字段引用本文件）

**已读样本与限制** 未读——[设施名单的显式输入](generation-settings.md#设施名单的显式输入)对应条目是名单引用的文件名行，非数据样本阅读证据；保持真实限定

**启用条件** 实际启用按 WP04 编译生命周期与 WP02 §6/§7（候选数据与未验证组合）保留，不据本表断言运行启用

**相关规格** [设施内容生成与模拟（挑战生成器——候选构造／合法性筛选／去重／评估与写出）行为规格](../spec/authoring/facility-content-generation-and-simulation.md)、[示例工程证据与能力覆盖](../spec/authoring/demo-evidence-and-capability-coverage.md)

<a id="cfg-10"></a>
### CFG-10 · cup_little_pkmn.txt

**机制** WP76/WP77（杯赛列表机制——littlecup 节 Pokemon 字段引用本文件）

**已读样本与限制** 未读——[设施名单的显式输入](generation-settings.md#设施名单的显式输入)对应条目是名单引用的文件名行，非数据样本阅读证据；保持真实限定

**启用条件** 实际启用按 WP04 编译生命周期与 WP02 §6/§7（候选数据与未验证组合）保留，不据本表断言运行启用

**相关规格** [设施内容生成与模拟（挑战生成器——候选构造／合法性筛选／去重／评估与写出）行为规格](../spec/authoring/facility-content-generation-and-simulation.md)、[示例工程证据与能力覆盖](../spec/authoring/demo-evidence-and-capability-coverage.md)

<a id="cfg-11"></a>
### CFG-11 · cup_little_trainers.txt

**机制** WP76/WP77（杯赛列表机制——littlecup 节 Trainers 字段引用本文件）

**已读样本与限制** 未读（名单只引用文件名，未提供实际样本）

**启用条件** 实际启用按 WP04 编译生命周期与 WP02 §6/§7（候选数据与未验证组合）保留，不据本表断言运行启用

**相关规格** [设施内容生成与模拟（挑战生成器——候选构造／合法性筛选／去重／评估与写出）行为规格](../spec/authoring/facility-content-generation-and-simulation.md)、[示例工程证据与能力覆盖](../spec/authoring/demo-evidence-and-capability-coverage.md)

<a id="cfg-12"></a>
### CFG-12 · cup_pika_pkmn.txt

**机制** WP76/WP77（杯赛列表机制——pikacup 节 Pokemon 字段引用本文件）

**已读样本与限制** 未读（名单只引用文件名，未提供实际样本）

**启用条件** 实际启用按 WP04 编译生命周期与 WP02 §6/§7（候选数据与未验证组合）保留，不据本表断言运行启用

**相关规格** [设施内容生成与模拟（挑战生成器——候选构造／合法性筛选／去重／评估与写出）行为规格](../spec/authoring/facility-content-generation-and-simulation.md)、[示例工程证据与能力覆盖](../spec/authoring/demo-evidence-and-capability-coverage.md)

<a id="cfg-13"></a>
### CFG-13 · cup_pika_trainers.txt

**机制** WP76/WP77（杯赛列表机制——pikacup 节 Trainers 字段引用本文件）

**已读样本与限制** 未读（名单只引用文件名，未提供实际样本）

**启用条件** 实际启用按 WP04 编译生命周期与 WP02 §6/§7（候选数据与未验证组合）保留，不据本表断言运行启用

**相关规格** [设施内容生成与模拟（挑战生成器——候选构造／合法性筛选／去重／评估与写出）行为规格](../spec/authoring/facility-content-generation-and-simulation.md)、[示例工程证据与能力覆盖](../spec/authoring/demo-evidence-and-capability-coverage.md)

<a id="cfg-14"></a>
### CFG-14 · cup_poke_pkmn.txt

**机制** WP76/WP77（杯赛列表机制——pokecup 节 Pokemon 字段引用本文件）

**已读样本与限制** 未读（名单只引用文件名，未提供实际样本）

**启用条件** 实际启用按 WP04 编译生命周期与 WP02 §6/§7（候选数据与未验证组合）保留，不据本表断言运行启用

**相关规格** [设施内容生成与模拟（挑战生成器——候选构造／合法性筛选／去重／评估与写出）行为规格](../spec/authoring/facility-content-generation-and-simulation.md)、[示例工程证据与能力覆盖](../spec/authoring/demo-evidence-and-capability-coverage.md)

<a id="cfg-15"></a>
### CFG-15 · cup_poke_trainers.txt

**机制** WP76/WP77（杯赛列表机制——pokecup 节 Trainers 字段引用本文件）

**已读样本与限制** 未读（名单只引用文件名，未提供实际样本）

**启用条件** 实际启用按 WP04 编译生命周期与 WP02 §6/§7（候选数据与未验证组合）保留，不据本表断言运行启用

**相关规格** [设施内容生成与模拟（挑战生成器——候选构造／合法性筛选／去重／评估与写出）行为规格](../spec/authoring/facility-content-generation-and-simulation.md)、[示例工程证据与能力覆盖](../spec/authoring/demo-evidence-and-capability-coverage.md)

<a id="cfg-16"></a>
### CFG-16 · dungeon_parameters.txt

**机制** [随机地牢](../spec/world/random-dungeons.md)（地牢生成机制）＋WP77 §4.5（demo 登记）

**已读样本与限制** WP77（E34 全文 30 行）＋wp14（[cave]/[forest] 样本）

**启用条件** 实际启用按 WP04 编译生命周期与 WP02 §6/§7（候选数据与未验证组合）保留，不据本表断言运行启用

**相关规格** [随机地牢](../spec/world/random-dungeons.md)、[示例工程证据与能力覆盖](../spec/authoring/demo-evidence-and-capability-coverage.md)

<a id="cfg-17"></a>
### CFG-17 · dungeon_tilesets.txt

**机制** [随机地牢](../spec/world/random-dungeons.md)（地牢图块机制）

**已读样本与限制** wp14（[7]/[23] 样本）

**启用条件** 实际启用按 WP04 编译生命周期与 WP02 §6/§7（候选数据与未验证组合）保留，不据本表断言运行启用

**相关规格** [随机地牢](../spec/world/random-dungeons.md)

<a id="cfg-18"></a>
### CFG-18 · encounters.txt

**机制** [普通遭遇、触发与修正行为规格](../spec/world/wild-encounters-and-modifiers.md)（遭遇数据/触发机制）＋[漫游与 Poké Radar](../spec/world/roaming-and-poke-radar.md)（雷达段消费）＋WP72（编辑器机制）

**已读样本与限制** WP77（E34 全文 311 行）＋wp36（[002] 水系钓竿段、[005]/[005,1] 陆地/夜间/雷达段）

**启用条件** 实际启用按 WP04 编译生命周期与 WP02 §6/§7（候选数据与未验证组合）保留，不据本表断言运行启用

**相关规格** [普通遭遇、触发与修正行为规格](../spec/world/wild-encounters-and-modifiers.md)、[漫游与 Poké Radar](../spec/world/roaming-and-poke-radar.md)、[调试情境与控制行为规格](../spec/authoring/debug-contexts-and-controls.md)

<a id="cfg-19"></a>
### CFG-19 · items.txt

**机制** [招式属性、目标与复制调用行为规格](../spec/battle/move-attributes-targeting-and-calling.md)＋wp47-b（物品效果/控制合同）＋wp42（终局消费）

**已读样本与限制** WP47-A（自然之恩 Flags 数据读取）＋WP76（25 个不同身份的章节标识检索——不称已读物品效果全文）；不声称全量逐条读取

**启用条件** 实际启用按 WP04 编译生命周期与 WP02 §6/§7（候选数据与未验证组合）保留，不据本表断言运行启用

**相关规格** [招式属性、目标与复制调用行为规格](../spec/battle/move-attributes-targeting-and-calling.md)

<a id="cfg-20"></a>
### CFG-20 · map_connections.txt

**机制** [地图拓扑与转移](../spec/world/map-topology-transfer.md)（地图拓扑/传送机制）＋WP72/WP73-B（连接编辑器机制）

**已读样本与限制** WP77（E34 全文 40 行）＋wp11（作者内容样本）

**启用条件** 实际启用按 WP04 编译生命周期与 WP02 §6/§7（候选数据与未验证组合）保留，不据本表断言运行启用

**相关规格** [地图拓扑与转移](../spec/world/map-topology-transfer.md)、[调试情境与控制行为规格](../spec/authoring/debug-contexts-and-controls.md)、[内容编辑器（物种/道具/训练家/元数据/图鉴列表）行为规格](../spec/authoring/content-editors.md)、[世界编辑器（地图连接/地图元数据/地形标签/遭遇/指标）行为规格](../spec/authoring/world-editors.md)

<a id="cfg-21"></a>
### CFG-21 · map_metadata.txt

**机制** [世界时间、天气与场地能力](../spec/world/world-time-weather-field-moves.md)（天气/场地消费）＋WP72/WP73-B（元数据编辑器机制）

**已读样本与限制** WP77（E34 全文 398 行、69 节）＋wp59（Weather 行三例样本）

**启用条件** 实际启用按 WP04 编译生命周期与 WP02 §6/§7（候选数据与未验证组合）保留，不据本表断言运行启用

**相关规格** [世界时间、天气与场地能力](../spec/world/world-time-weather-field-moves.md)、[调试情境与控制行为规格](../spec/authoring/debug-contexts-and-controls.md)、[内容编辑器（物种/道具/训练家/元数据/图鉴列表）行为规格](../spec/authoring/content-editors.md)、[世界编辑器（地图连接/地图元数据/地形标签/遭遇/指标）行为规格](../spec/authoring/world-editors.md)

<a id="cfg-22"></a>
### CFG-22 · metadata.txt

**机制** WP77 §4.1（起始与玩家元数据——四类事实分开）＋WP72/WP73-A（元数据编辑器机制）

**已读样本与限制** WP77（E34 全文 33 行）

**启用条件** 实际启用按 WP04 编译生命周期与 WP02 §6/§7（候选数据与未验证组合）保留，不据本表断言运行启用

**相关规格** [示例工程证据与能力覆盖](../spec/authoring/demo-evidence-and-capability-coverage.md)、[调试情境与控制行为规格](../spec/authoring/debug-contexts-and-controls.md)、[内容编辑器（物种/道具/训练家/元数据/图鉴列表）行为规格](../spec/authoring/content-editors.md)、[世界编辑器（地图连接/地图元数据/地形标签/遭遇/指标）行为规格](../spec/authoring/world-editors.md)

<a id="cfg-23"></a>
### CFG-23 · moves.txt

**机制** [招式属性、目标与复制调用行为规格](../spec/battle/move-attributes-targeting-and-calling.md)＋wp47-b（招式属性/控制合同）＋wp54（入场资格/条款）＋wp20（招式槽消费）

**已读样本与限制** WP76（AERIALACE/SWIFT/SKETCH 三段）＋WP47-A（SWORDSDANCE :6541–6550 目标数据审计）；不声称全量逐条读取

**启用条件** 实际启用按 WP04 编译生命周期与 WP02 §6/§7（候选数据与未验证组合）保留，不据本表断言运行启用

**相关规格** [招式属性、目标与复制调用行为规格](../spec/battle/move-attributes-targeting-and-calling.md)

<a id="cfg-24"></a>
### CFG-24 · phone.txt

**机制** [Pokégear、区域地图、点唱机与电话行为规格](../spec/ui/pokegear-map-music-and-phone.md)（电话数据/联系人/呼叫/对话机制）

**已读样本与限制** WP77（E34 全文 48 行）＋wp63（顶层首 40 行结构样本）

**启用条件** 实际启用按 WP04 编译生命周期与 WP02 §6/§7（候选数据与未验证组合）保留，不据本表断言运行启用

**相关规格** [Pokégear、区域地图、点唱机与电话行为规格](../spec/ui/pokegear-map-music-and-phone.md)

<a id="cfg-25"></a>
### CFG-25 · pokemon.txt

**机制** wp31（进化机制）＋wp33/wp35（寄养/繁殖/孵化消费）＋wp55（设施消费）＋wp47-b（交换/控制消费）

**已读样本与限制** wp31（NINCADA/EEVEE/TYROGUE/WURMPLE/KIRLIA 等进化样本群）＋WP76（SMEARGLE :6189–6205）；不声称全量逐条读取

**启用条件** 实际启用按 WP04 编译生命周期与 WP02 §6/§7（候选数据与未验证组合）保留，不据本表断言运行启用

**相关规格** [基础进化](../spec/creatures/basic-evolution.md) §2、§3.1、§3.5、§9、[寄养会话与兼容性行为规格](../spec/creatures/daycare-and-breeding-session.md) §5.1、§5.4、[蛋状态与孵化行为规格](../spec/creatures/eggs-and-hatching.md) §3.1、§3.2、[设施基础会话行为规格](../spec/battle/facility-session-and-restoration.md) §2.5、[有界覆盖与默认数据附表](../spec/battle/control-items-coverage-data.md) §2、[招式换人、行动控制与物品变化行为规格](../spec/battle/switching-control-and-item-changes.md) §5.1、[设施内容生成与模拟（挑战生成器——候选构造／合法性筛选／去重／评估与写出）行为规格](../spec/authoring/facility-content-generation-and-simulation.md) §5.5、§5.6

<a id="cfg-26"></a>
### CFG-26 · pokemon_forms.txt

**机制** wp22（Mega/原始回归机制）＋wp31/wp32（进化条件与情境输入）

**已读样本与限制** wp22（48 个 Mega 目标字段、KYOGRE/GROUDON 形态 1）＋wp31（RUNERIGUS 事件编号 2）；不声称全量逐条读取

**启用条件** 实际启用按 WP04 编译生命周期与 WP02 §6/§7（候选数据与未验证组合）保留，不据本表断言运行启用

**相关规格** [Mega、Primal 与显式还原](../spec/creatures/mega-and-primal-reversion.md) §2、§3、§5、[默认特殊形态资格数据](../spec/creatures/transformation-data.md) §1、§2、[基础进化](../spec/creatures/basic-evolution.md) §3.5、§9、[情境、交换、战后成就与事件进化](../spec/creatures/contextual-trade-and-post-battle-evolution.md) §2、§7、[情境输入、默认数据与前后状态](../spec/creatures/context-inputs-and-scenarios.md) §2

<a id="cfg-27"></a>
### CFG-27 · pokemon_metrics.txt

**机制** WP73-B（指标编辑器：保存/丢弃/全量自动定位算法）＋WP72（调试菜单入口）

**已读样本与限制** 未读——未见本文件数据样本阅读登记；保持真实限定，不因机制在案声称内容已读

**启用条件** 实际启用按 WP04 编译生命周期与 WP02 §6/§7（候选数据与未验证组合）保留，不据本表断言运行启用

**相关规格** [内容编辑器（物种/道具/训练家/元数据/图鉴列表）行为规格](../spec/authoring/content-editors.md)、[世界编辑器（地图连接/地图元数据/地形标签/遭遇/指标）行为规格](../spec/authoring/world-editors.md)、[调试情境与控制行为规格](../spec/authoring/debug-contexts-and-controls.md)

<a id="cfg-28"></a>
### CFG-28 · regional_dexes.txt

**机制** [图鉴记录、区域与内容规则](../spec/creatures/pokedex-records-regions-and-content.md)（区域图鉴机制）＋WP72（编辑器机制）

**已读样本与限制** wp62（两节 212 行结构样本；不声称逐条读取全部物种链）

**启用条件** 实际启用按 WP04 编译生命周期与 WP02 §6/§7（候选数据与未验证组合）保留，不据本表断言运行启用

**相关规格** [图鉴记录、区域与内容规则](../spec/creatures/pokedex-records-regions-and-content.md)、[调试情境与控制行为规格](../spec/authoring/debug-contexts-and-controls.md)

<a id="cfg-29"></a>
### CFG-29 · ribbons.txt

**机制** WP21 §5.2（缎带存储、给予/升级/移除接口与异常路径（含 [B,B] 替换与移除失败静态异常路径）、摘要展示（每页 12 个可滚动偏移））

**已读样本与限制** schema 字段目录已读（标识/名称/图标位置/描述/标记；「图标位置只用于裁切非排序依据」）；不标数据内容已读全覆盖

**启用条件** 实际启用按 WP04 编译生命周期与 WP02 §6/§7（候选数据与未验证组合）保留，不据本表断言运行启用

**相关规格** [动态形态与展示属性](../spec/creatures/dynamic-forms-and-display.md)

<a id="cfg-30"></a>
### CFG-30 · town_map.txt

**机制** [Pokégear、区域地图、点唱机与电话行为规格](../spec/ui/pokegear-map-music-and-phone.md)（区域地图机制）＋WP75（转换工具）＋WP77 §4.4（飞行点登记）

**已读样本与限制** WP77（E34 全文 36 行）＋wp63（顶层首 30 行结构样本）

**启用条件** 实际启用按 WP04 编译生命周期与 WP02 §6/§7（候选数据与未验证组合）保留，不据本表断言运行启用

**相关规格** [Pokégear、区域地图、点唱机与电话行为规格](../spec/ui/pokegear-map-music-and-phone.md)、[project-conversion-and-authoring-tools](../spec/authoring/project-conversion-and-authoring-tools.md)、[示例工程证据与能力覆盖](../spec/authoring/demo-evidence-and-capability-coverage.md)

<a id="cfg-31"></a>
### CFG-31 · trainer_types.txt

**机制** wp51（技能值消费）＋WP72（编辑器机制）＋WP76/WP77（设施与 demo 消费）

**已读样本与限制** WP76（189–196 YOUNGSTER）＋wp51（技能样本）

**启用条件** 实际启用按 WP04 编译生命周期与 WP02 §6/§7（候选数据与未验证组合）保留，不据本表断言运行启用

**相关规格** [调试情境与控制行为规格](../spec/authoring/debug-contexts-and-controls.md)、[设施内容生成与模拟（挑战生成器——候选构造／合法性筛选／去重／评估与写出）行为规格](../spec/authoring/facility-content-generation-and-simulation.md)、[示例工程证据与能力覆盖](../spec/authoring/demo-evidence-and-capability-coverage.md)

<a id="cfg-32"></a>
### CFG-32 · trainers.txt

**机制** WP55（设施会话）＋WP72/WP73-A（训练家战斗编辑器机制）＋WP76（设施生成）＋WP77 §5.2（训练家配置——20 节）

**已读样本与限制** WP77（E34 全文 118 行、20 节）

**启用条件** 实际启用按 WP04 编译生命周期与 WP02 §6/§7（候选数据与未验证组合）保留，不据本表断言运行启用

**相关规格** [设施基础会话行为规格](../spec/battle/facility-session-and-restoration.md)、[调试情境与控制行为规格](../spec/authoring/debug-contexts-and-controls.md)、[内容编辑器（物种/道具/训练家/元数据/图鉴列表）行为规格](../spec/authoring/content-editors.md)、[世界编辑器（地图连接/地图元数据/地形标签/遭遇/指标）行为规格](../spec/authoring/world-editors.md)、[设施内容生成与模拟（挑战生成器——候选构造／合法性筛选／去重／评估与写出）行为规格](../spec/authoring/facility-content-generation-and-simulation.md)、[示例工程证据与能力覆盖](../spec/authoring/demo-evidence-and-capability-coverage.md)

<a id="cfg-33"></a>
### CFG-33 · types.txt

**机制** wp47-a（类型相性/目标合同）＋wp51（AI 相性消费）＋wp68-triad（卡牌消费）＋WP72（编辑器机制）

**已读样本与限制** WP47-A（默认身份/图标具名数据读取）；不声称全量字段逐条读取

**启用条件** 实际启用按 WP04 编译生命周期与 WP02 §6/§7（候选数据与未验证组合）保留，不据本表断言运行启用

**相关规格** [调试情境与控制行为规格](../spec/authoring/debug-contexts-and-controls.md)

<a id="cfg-34"></a>
### CFG-34 · Gen 5–8 backup/ (9 texts each)

**机制** WP02 §6.2（候选变体材料登记——存在性证据，非支持结论）：普通发现不扫描、无自动切换

**已读样本与限制** 早期清单只核验文件身份。后来对四代备份进行了字段与样本核对，详见[旧世代备份的字段与启用条件](generation-data-compatibility.md)。

**启用条件** 普通发现不自动加载备份。仅凭清单不能证明切换、成功编译或运行启用。

**相关规格** [规则配置档案与数据变体](../spec/core/rule-configuration-and-data-variants.md)

<a id="cfg-35"></a>
### CFG-35 · Shadow Pokémon backup/ (4 texts)

**机制** WP23主规则与数据附表§3/§3.1/§3.2；WP02 的存在性定位与 WP23 的具体样本分别适用。

**已读样本与限制** WP23记录四文本的字面字段与样本目录：shadow_pokemon131节/525行、moves18节/213行、items4节/42行、types1节/7行；量表/招式样本全集及招式/物品数据在§3.1/§3.2。数据提取不证明启用、编译或运行组合。

**启用条件** U06实际启用未知；顶层无对应Shadow专用节/文件，未提供可验证编译产物；不自动切换备份。

**相关规格** [心量表数据、可选内容与固定向量](../spec/creatures/shadow-data-and-vectors.md) §3、§3.1、§3.2、[Shadow、Hyper、成长暂存与净化生命周期](../spec/creatures/shadow-hyper-and-purification.md) §2
