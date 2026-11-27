# 参考材料的适用范围

这份索引限于形成各项静态规格时所查的入口、字段和样本。432 项材料中包括 312 个参考脚本、2 个根层工具和 33 个顶层作者文本。确认文件身份只说明当时能定位该材料，不能证明通读、运行或完整功能覆盖。U01–U10、G01–G12 和 AX01–AX20 的限制继续适用。

同一功能中，多份材料可能共同指向一组规格；分行列出的链接补充各自的适用范围。原版隔离执行及其环境见[有限运行观察](observation-limits.md)，独立实现的模式见[版本与兼容规则](versions-and-compatibility.md)。

## 数据、存档与基础服务

### 全游戏设置常量定义：键目录、默认值与注释说明

逐项配置按各调用方的规则解释。配置 §4.3 列候选使用点，§7 列未验证组合。

- <a id="src-004"></a>[规则配置档案与数据变体](../spec/core/rule-configuration-and-data-variants.md)

### 诊断与文件 §C（诊断面——控制台输出集合）＋调试操作 §F（调试日志）

- <a id="src-006"></a>[诊断、文件与 HTTP](../spec/core/diagnostics-files-http.md)、[弃用告警机制](../spec/core/deprecation-appendix.md)、[调试情境与控制](../spec/authoring/debug-contexts-and-controls.md)

### 诊断与文件 §C（诊断与错误反馈——异常格式化）

- <a id="src-007"></a>[调试情境与控制](../spec/authoring/debug-contexts-and-controls.md)、[世界编辑器（地图连接/地图元数据/地形标签/遭遇/指标）](../spec/authoring/world-editors.md)、[诊断、文件与 HTTP](../spec/core/diagnostics-files-http.md)、[迁移、失败与恢复](../spec/core/migration-failure-recovery.md)、[弃用告警机制](../spec/core/deprecation-appendix.md)

### 内容身份与字段 §3.1（参数验证错误边界）＋诊断与文件 §C（诊断面）

- <a id="src-008"></a>[内容身份、注册与 schema](../spec/core/content-identity-and-schema.md)、[弃用告警机制](../spec/core/deprecation-appendix.md)、[诊断、文件与 HTTP](../spec/core/diagnostics-files-http.md)

### 数据、存档与基础服务的场景与机制

- <a id="src-009"></a>[弃用告警机制](../spec/core/deprecation-appendix.md)

### 规则配置 §3＋内容身份与字段 §3

- <a id="src-010"></a>[消息、窗口与输入](../spec/ui/messages-windows-input.md)、[规则配置档案与数据变体](../spec/core/rule-configuration-and-data-variants.md)、[内容身份、注册与 schema](../spec/core/content-identity-and-schema.md)

### 诊断与文件 §A（文件访问层）

共同涉及 [弃用告警机制](../spec/core/deprecation-appendix.md)、[诊断、文件与 HTTP](../spec/core/diagnostics-files-http.md)。

- <a id="src-011"></a>[资源匹配、资源访问及声音](../spec/world/resource-matching-and-audio.md)、[野外被动变化与失败回程](../spec/world/field-passive-effects-and-blackout.md)
- <a id="src-013"></a>[邮件与神秘礼物](../spec/creatures/mail-and-mystery-gift.md)

### 辅助功能的适用范围

文件访问混入——诊断与文件 §A 文件访问层已覆盖。该材料的其他功能没有由本条整体验证。

- <a id="src-012"></a>限于上述适用范围。

精灵基类原语——资源与音频/世界绘制 已覆盖可观察行为。该材料的其他功能没有由本条整体验证。

- <a id="src-018"></a>限于上述适用范围。

该项所指的其他可观察要求未确定。

- <a id="src-054"></a><a id="src-057"></a><a id="src-060"></a><a id="src-070"></a>限于上述适用范围。

地图渲染辅助——世界绘制 §3 地图绘制已覆盖。该材料的其他功能没有由本条整体验证。

- <a id="src-059"></a>限于上述适用范围。

窗口精灵原语——消息与输入 消息/窗口合同已覆盖可观察行为。该材料的其他功能没有由本条整体验证。

- <a id="src-067"></a>限于上述适用范围。

道具精灵辅助——资源与音频 资源匹配已覆盖。该材料的其他功能没有由本条整体验证。

- <a id="src-217"></a>限于上述适用范围。

宝可梦精灵辅助——资源与音频 资源匹配已覆盖。该材料的其他功能没有由本条整体验证。

- <a id="src-221"></a>限于上述适用范围。

### 规则配置 §7（检索索引与消费者分类）＋各领域包消费者

- <a id="src-014"></a>[设施基础会话](../spec/battle/facility-session-and-restoration.md)、[工程转换与制作工具](../spec/authoring/project-conversion-and-authoring-tools.md)、[心量表数据、可选内容与固定向量](../spec/creatures/shadow-data-and-vectors.md)、[Shadow、Hyper、成长暂存与净化生命周期](../spec/creatures/shadow-hyper-and-purification.md)、[规则配置档案与数据变体](../spec/core/rule-configuration-and-data-variants.md)

### 本地化 §A–D（文本域与身份/语言配置/查找回退/作者翻译工作流）

- <a id="src-015"></a>[本地化](../spec/core/localization.md)、[Duel](../spec/ui/duel.md)

### 通知与插件 §C–D（插件元数据与载入三阶段）

- <a id="src-017"></a>[通知、扩展与插件](../spec/core/events-extensions-plugins.md)、[诊断、文件与 HTTP](../spec/core/diagnostics-files-http.md)

### 保存与启动 §3–6＋迁移恢复 §3–5

共同涉及 [保存、启动、新游戏与继续](../spec/core/save-startup-continue.md)、[迁移、失败与恢复](../spec/core/migration-failure-recovery.md)。

- <a id="src-020"></a><a id="src-021"></a>仅涉及上列规格。
- <a id="src-022"></a>仅涉及上列规格。
- <a id="src-023"></a>[战斗记录与回放](../spec/battle/battle-recording-and-playback.md)、[背包、物品储存与快捷登记](../spec/creatures/bag-and-item-storage.md)、[时间、随机、计步与统计](../spec/core/time-random-steps-stats.md)
- <a id="src-024"></a>[背包、物品储存与快捷登记](../spec/creatures/bag-and-item-storage.md)、[寄养会话与兼容性](../spec/creatures/daycare-and-breeding-session.md)、[动态形态与展示属性](../spec/creatures/dynamic-forms-and-display.md)

### 保存与启动 §B＋示例工程 §4.1

- <a id="src-025"></a>[设施基础会话](../spec/battle/facility-session-and-restoration.md)、[玩家、NPC 训练家与伙伴](../spec/creatures/player-trainers-partners.md)、[示例工程证据与能力覆盖](../spec/authoring/demo-evidence-and-capability-coverage.md)、[保存、启动、新游戏与继续](../spec/core/save-startup-continue.md)

### 返回标题时的游戏时钟

返回标题时清除游戏时间锚点。

- <a id="src-026"></a>[统计字段目录](../spec/core/stats-directory.md)、[时间、随机、计步与统计](../spec/core/time-random-steps-stats.md)、[附：控制帮助（Controls help）四页场景合同](../spec/ui/controls-help-appendix.md)、[标题、载入、选项、暂停与 PC（主导航）](../spec/ui/title-load-options-pause-and-pc.md)、[附：训练家卡（Trainer Card）场景合同](../spec/ui/trainer-card-appendix.md)

### 通知与插件 §A（通知机制）

共同涉及 [调试情境与控制](../spec/authoring/debug-contexts-and-controls.md)、[通知、扩展与插件](../spec/core/events-extensions-plugins.md)。

- <a id="src-029"></a>[AI 场域、伤害恢复与多目标评估](../spec/battle/field-damage-healing-and-target-evaluation.md)、[AI 物品、调用与行动控制评估](../spec/battle/items-calling-and-control-evaluation.md)
- <a id="src-030"></a>[Safari 与捕虫大会](../spec/battle/safari-and-bug-catching-contest.md)、[Pokégear、区域地图、点唱机与电话](../spec/ui/pokegear-map-music-and-phone.md)

### 保存与启动 §3–5

- <a id="src-036"></a>[资源匹配、资源访问及声音](../spec/world/resource-matching-and-audio.md)、[Pokégear、区域地图、点唱机与电话](../spec/ui/pokegear-map-music-and-phone.md)、[保存、启动、新游戏与继续](../spec/core/save-startup-continue.md)

### 计时与统计 §4＋保存与启动 §A

- <a id="src-046"></a>[买卖与 BP 商店](../spec/creatures/shops-and-exchanges.md)、[寄养会话与兼容性](../spec/creatures/daycare-and-breeding-session.md)、[蛋状态与孵化](../spec/creatures/eggs-and-hatching.md)、[统计字段目录](../spec/core/stats-directory.md)、[时间、随机、计步与统计](../spec/core/time-random-steps-stats.md)、[保存、启动、新游戏与继续](../spec/core/save-startup-continue.md)

### 内容身份与字段 §3.1–3.2（注册表默认契约与按类例外）＋附表

- <a id="src-078"></a>[AI 通用数值、状态与阶级评估](../spec/battle/generic-numerical-and-status-evaluation.md)、[内容编辑器（物种/道具/训练家/元数据/图鉴列表）](../spec/authoring/content-editors.md)、[战斗动画制作与交换（动画编辑器／组织器／单项与批量导入导出）](../spec/authoring/battle-animation-authoring-and-exchange.md)、[设施内容生成与模拟（挑战生成器——候选构造／合法性筛选／去重／评估与写出）](../spec/authoring/facility-content-generation-and-simulation.md)、[内容身份、注册与 schema](../spec/core/content-identity-and-schema.md)

### 内容身份与字段 §3.2/附表（按类例外与字段责任目录）＋个体身份/能力与属性/动态形态/野外遭遇/天气与场地/图鉴 对应字段语义

各类内容由相应领域规格解释。

- <a id="src-080"></a><a id="src-081"></a><a id="src-082"></a><a id="src-083"></a><a id="src-084"></a><a id="src-086"></a><a id="src-087"></a><a id="src-088"></a><a id="src-089"></a><a id="src-090"></a><a id="src-091"></a><a id="src-093"></a><a id="src-094"></a><a id="src-095"></a>[内容身份、注册与 schema](../spec/core/content-identity-and-schema.md)、[生物身份、物种记录、来源与拥有者](../spec/creatures/creature-identity-species-ownership.md)、[属性派生、特性选择与六项能力](../spec/creatures/attributes-ability-and-stats.md)、[动态形态与展示属性](../spec/creatures/dynamic-forms-and-display.md)、[普通遭遇、触发与修正](../spec/world/wild-encounters-and-modifiers.md)、[战斗天气、场地、阵营与位置效果](../spec/battle/weather-terrain-side-and-position-effects.md)、[图鉴记录、区域与内容规则](../spec/creatures/pokedex-records-regions-and-content.md)

### 内容身份与字段 §3.2/编译与加载 §4.2（schema 消费边界）＋各领域包字段语义

字段语义按各领域的消费者解释。

- <a id="src-096"></a><a id="src-097"></a><a id="src-098"></a><a id="src-099"></a><a id="src-100"></a><a id="src-101"></a><a id="src-102"></a><a id="src-103"></a><a id="src-104"></a><a id="src-105"></a><a id="src-106"></a><a id="src-107"></a><a id="src-108"></a><a id="src-109"></a><a id="src-110"></a><a id="src-111"></a><a id="src-112"></a><a id="src-113"></a><a id="src-114"></a><a id="src-115"></a><a id="src-116"></a>[内容身份、注册与 schema](../spec/core/content-identity-and-schema.md)、[PBS 生命周期](../spec/core/pbs-lifecycle.md)

### 编译与加载 §3–7＋工程转换 §3–10＋设施内容生成 §8

共同涉及 [工程转换与制作工具](../spec/authoring/project-conversion-and-authoring-tools.md)、[设施内容生成与模拟（挑战生成器——候选构造／合法性筛选／去重／评估与写出）](../spec/authoring/facility-content-generation-and-simulation.md)、[PBS 生命周期](../spec/core/pbs-lifecycle.md)。

- <a id="src-311"></a>[买卖与 BP 商店](../spec/creatures/shops-and-exchanges.md)
- <a id="src-312"></a>[设施基础会话](../spec/battle/facility-session-and-restoration.md)、[买卖与 BP 商店](../spec/creatures/shops-and-exchanges.md)、[普通遭遇、触发与修正](../spec/world/wild-encounters-and-modifiers.md)、[战斗动画制作与交换（动画编辑器／组织器／单项与批量导入导出）](../spec/authoring/battle-animation-authoring-and-exchange.md)
- <a id="src-313"></a>[设施基础会话](../spec/battle/facility-session-and-restoration.md)、[图鉴记录、区域与内容规则](../spec/creatures/pokedex-records-regions-and-content.md)

项目转换 §8.6；移动路线 §1、§2；静态场景 MR18、MR19、MR20、MR21、MR22。该转换与移动路线的衔接为静态预期。

- <a id="src-314"></a>[战斗记录与回放](../spec/battle/battle-recording-and-playback.md)、[寄养会话与兼容性](../spec/creatures/daycare-and-breeding-session.md)、[工程转换与制作工具](../spec/authoring/project-conversion-and-authoring-tools.md)、[PBS 生命周期](../spec/core/pbs-lifecycle.md)、[设施内容生成与模拟（挑战生成器——候选构造／合法性筛选／去重／评估与写出）](../spec/authoring/facility-content-generation-and-simulation.md)

### 保存与启动 §B（启动阶段与新游戏/继续）＋通知与插件 §6.3（启动顺序：核心消息→插件→编译检查→初始化）＋示例工程 §4.1（系统起始位置边界）

- <a id="src-315"></a>[调试情境与控制](../spec/authoring/debug-contexts-and-controls.md)、[内容身份、注册与 schema](../spec/core/content-identity-and-schema.md)、[PBS 生命周期](../spec/core/pbs-lifecycle.md)、[通知、扩展与插件](../spec/core/events-extensions-plugins.md)、[保存、启动、新游戏与继续](../spec/core/save-startup-continue.md)、[示例工程证据与能力覆盖](../spec/authoring/demo-evidence-and-capability-coverage.md)


## 地图、移动与场地

### 事件与路线 §B＋矩阵

- <a id="src-027"></a>[买卖与 BP 商店](../spec/creatures/shops-and-exchanges.md)、[工程转换与制作工具](../spec/authoring/project-conversion-and-authoring-tools.md)、[统计字段目录](../spec/core/stats-directory.md)、[解释器命令兼容矩阵](../spec/world/interpreter-command-matrix.md)、[地图事件、NPC 与跟随](../spec/world/map-events-npc-followers.md)、[移动路线命令矩阵](../spec/world/move-route-matrix.md)

### 事件与路线 矩阵

- <a id="src-028"></a>[普通遭遇、触发与修正](../spec/world/wild-encounters-and-modifiers.md)、[工程转换与制作工具](../spec/authoring/project-conversion-and-authoring-tools.md)、[规则配置档案与数据变体](../spec/core/rule-configuration-and-data-variants.md)、[解释器命令兼容矩阵](../spec/world/interpreter-command-matrix.md)、[地图事件、NPC 与跟随](../spec/world/map-events-npc-followers.md)、[移动路线命令矩阵](../spec/world/move-route-matrix.md)

### 世界绘制 §C/D（屏幕效果/场景刷新）＋世界时间与场地 §B（世界天气显示管线）

- <a id="src-031"></a>[世界绘制与视觉过渡](../spec/world/world-rendering-and-visual-transitions.md)、[世界时间、天气与场地能力](../spec/world/world-time-weather-field-moves.md)、[情境、交换、战后成就与事件进化](../spec/creatures/contextual-trade-and-post-battle-evolution.md)、[战前过渡](../spec/world/pre-battle-transitions.md)

### 事件与路线 §A（事件开关语义）＋保存与启动 §A（持久值登记）

- <a id="src-033"></a>[调试情境与控制](../spec/authoring/debug-contexts-and-controls.md)、[解释器命令兼容矩阵](../spec/world/interpreter-command-matrix.md)、[地图事件、NPC 与跟随](../spec/world/map-events-npc-followers.md)、[移动路线命令矩阵](../spec/world/move-route-matrix.md)、[保存、启动、新游戏与继续](../spec/core/save-startup-continue.md)

### 事件与路线 §A（事件变量语义）＋保存与启动 §A（持久值登记）

- <a id="src-034"></a>[调试情境与控制](../spec/authoring/debug-contexts-and-controls.md)、[Lottery](../spec/ui/lottery.md)、[解释器命令兼容矩阵](../spec/world/interpreter-command-matrix.md)、[地图事件、NPC 与跟随](../spec/world/map-events-npc-followers.md)、[移动路线命令矩阵](../spec/world/move-route-matrix.md)、[保存、启动、新游戏与继续](../spec/core/save-startup-continue.md)

### 事件与路线 §A（事件页与自开关语义）

- <a id="src-035"></a>[解释器命令兼容矩阵](../spec/world/interpreter-command-matrix.md)、[地图事件、NPC 与跟随](../spec/world/map-events-npc-followers.md)、[移动路线命令矩阵](../spec/world/move-route-matrix.md)

### 地图转移 §3–5

- <a id="src-038"></a>[获得、赠送与脚本交换](../spec/creatures/acquisition-gifts-and-script-trade.md)、[地图拓扑与转移](../spec/world/map-topology-transfer.md)、[地形、运动与载具](../spec/world/terrain-movement-vehicles.md)、[地图事件、NPC 与跟随](../spec/world/map-events-npc-followers.md)

### 地图转移 §5

- <a id="src-039"></a>[世界编辑器（地图连接/地图元数据/地形标签/遭遇/指标）](../spec/authoring/world-editors.md)、[地图拓扑与转移](../spec/world/map-topology-transfer.md)、[地形、运动与载具](../spec/world/terrain-movement-vehicles.md)、[Safari 与捕虫大会](../spec/battle/safari-and-bug-catching-contest.md)

### 地形与移动 §B

项目转换 §8.6；移动路线 §1、§2；静态场景 MR18、MR19、MR20、MR21、MR22。该转换与移动路线的衔接为静态预期。

- <a id="src-040"></a>[地图拓扑与转移](../spec/world/map-topology-transfer.md)、[地形、运动与载具](../spec/world/terrain-movement-vehicles.md)、[地图事件、NPC 与跟随](../spec/world/map-events-npc-followers.md)、[移动路线命令矩阵](../spec/world/move-route-matrix.md)、[工程转换与制作工具](../spec/authoring/project-conversion-and-authoring-tools.md)

### 事件与路线 §A

- <a id="src-041"></a>[地图拓扑与转移](../spec/world/map-topology-transfer.md)、[地图事件、NPC 与跟随](../spec/world/map-events-npc-followers.md)、[世界时间、天气与场地能力](../spec/world/world-time-weather-field-moves.md)、[解释器命令兼容矩阵](../spec/world/interpreter-command-matrix.md)、[移动路线命令矩阵](../spec/world/move-route-matrix.md)

### 地形与移动 §B–D

- <a id="src-042"></a>[玩家、NPC 训练家与伙伴](../spec/creatures/player-trainers-partners.md)、[普通遭遇、触发与修正](../spec/world/wild-encounters-and-modifiers.md)、[统计字段目录](../spec/core/stats-directory.md)、[时间、随机、计步与统计](../spec/core/time-random-steps-stats.md)、[地形、运动与载具](../spec/world/terrain-movement-vehicles.md)

### 事件与路线 §A–B

- <a id="src-043"></a>[获得、赠送与脚本交换](../spec/creatures/acquisition-gifts-and-script-trade.md)、[地图事件、NPC 与跟随](../spec/world/map-events-npc-followers.md)、[解释器命令兼容矩阵](../spec/world/interpreter-command-matrix.md)、[移动路线命令矩阵](../spec/world/move-route-matrix.md)

### 事件与路线 §D

共同涉及 [地图事件、NPC 与跟随](../spec/world/map-events-npc-followers.md)、[解释器命令兼容矩阵](../spec/world/interpreter-command-matrix.md)、[移动路线命令矩阵](../spec/world/move-route-matrix.md)。

- <a id="src-044"></a>[地形、运动与载具](../spec/world/terrain-movement-vehicles.md)
- <a id="src-045"></a>[野外被动变化与失败回程](../spec/world/field-passive-effects-and-blackout.md)

### 资源与音频 §A–C＋世界绘制 §3–6

4 个原语不适用。

- <a id="src-049"></a><a id="src-050"></a><a id="src-051"></a><a id="src-052"></a><a id="src-053"></a><a id="src-055"></a><a id="src-056"></a>[资源匹配、资源访问及声音](../spec/world/resource-matching-and-audio.md)、[战前过渡](../spec/world/pre-battle-transitions.md)、[世界绘制与视觉过渡](../spec/world/world-rendering-and-visual-transitions.md)

### 世界绘制 §3

2 个辅助不适用。

- <a id="src-058"></a><a id="src-061"></a>[战前过渡](../spec/world/pre-battle-transitions.md)、[世界绘制与视觉过渡](../spec/world/world-rendering-and-visual-transitions.md)

### 资源与音频 §D（音频行为）

共同涉及 [资源匹配、资源访问及声音](../spec/world/resource-matching-and-audio.md)。

- <a id="src-074"></a>仅涉及上列规格。
- <a id="src-075"></a>[Pokégear、区域地图、点唱机与电话](../spec/ui/pokegear-map-music-and-phone.md)

### 过渡效果引擎：入口与单位、特殊判定与分派、完成与阻塞、效果类固定目标时长、各效果逐帧绘制（1,929 行）

各效果的逐像素绘制算法、图像切分与插值轨迹不改变选择/时长/完成合同，按附表 §7 具名排除；实际视觉呈现未运行验证（G 系列限制）。

- <a id="src-076"></a>[世界绘制与视觉过渡](../spec/world/world-rendering-and-visual-transitions.md)、[战前过渡](../spec/world/pre-battle-transitions.md)、[附：控制帮助（Controls help）四页场景合同](../spec/ui/controls-help-appendix.md)

### 环境类别硬编码注册：id/名称/battle_base 基座名（131 行数据注册）

环境条目依内容登记规则读取；招式属性与目标 §3.3 列出各环境效果。

- <a id="src-092"></a>[战斗天气、场地、阵营与位置效果](../spec/battle/weather-terrain-side-and-position-effects.md)、[普通遭遇、触发与修正](../spec/world/wild-encounters-and-modifiers.md)、[世界时间、天气与场地能力](../spec/world/world-time-weather-field-moves.md)、[内容身份、注册与 schema](../spec/core/content-identity-and-schema.md)、[战斗上下文与参与者](../spec/battle/battle-context-and-participants.md)、[覆盖与默认数据附表](../spec/battle/attributes-targeting-calling-data.md)、[招式属性、目标与复制调用](../spec/battle/move-attributes-targeting-and-calling.md)、[有界覆盖与默认数据附表](../spec/battle/control-items-coverage-data.md)、[招式换人、行动控制与物品变化](../spec/battle/switching-control-and-item-changes.md)

### 世界绘制 §4＋世界时间与场地 §B

共同涉及 [世界绘制与视觉过渡](../spec/world/world-rendering-and-visual-transitions.md)、[世界时间、天气与场地能力](../spec/world/world-time-weather-field-moves.md)、[战前过渡](../spec/world/pre-battle-transitions.md)。

- <a id="src-195"></a>仅涉及上列规格。
- <a id="src-197"></a>[战斗成长交界、回合末与终局](../spec/battle/growth-end-of-round-and-battle-outcomes.md)、[统计字段目录](../spec/core/stats-directory.md)、[Safari 与捕虫大会](../spec/battle/safari-and-bug-catching-contest.md)、[野外被动变化与失败回程](../spec/world/field-passive-effects-and-blackout.md)

### 野外被动效果 §3–4＋野外遭遇 §3–4

- <a id="src-198"></a>[战斗上下文与参与者](../spec/battle/battle-context-and-participants.md)、[生物身份、物种记录、来源与拥有者](../spec/creatures/creature-identity-species-ownership.md)、[玩家、NPC 训练家与伙伴](../spec/creatures/player-trainers-partners.md)、[背包、物品储存与快捷登记](../spec/creatures/bag-and-item-storage.md)、[野外被动变化与失败回程](../spec/world/field-passive-effects-and-blackout.md)、[普通遭遇、触发与修正](../spec/world/wild-encounters-and-modifiers.md)

### 世界侧战前过渡：特殊过渡注册表与优先选择、资源条件、默认效果选择、演出阶段（前置闪屏/截图准备/主过渡/后置等待/黑屏交接）与正常返回清理（432 行）

附表 §7 排除逐像素坐标、图像切分与插值轨迹。素材缺失和实际帧呈现仍受 U01 与 G 系列限制。

- <a id="src-200"></a>[战斗成长交界、回合末与终局](../spec/battle/growth-end-of-round-and-battle-outcomes.md)、[钓鱼](../spec/world/fishing.md)、[战斗交互与呈现](../spec/ui/battle-interaction-and-presentation.md)、[树果种植](../spec/world/berry-plants.md)、[普通遭遇、触发与修正](../spec/world/wild-encounters-and-modifiers.md)

### 遭遇数据查询、机会判定与类型选择、触发概率、候选选择与等级、个体生成与修正（469 行）

- <a id="src-201"></a>[战斗上下文与参与者](../spec/battle/battle-context-and-participants.md)、[生物身份、物种记录、来源与拥有者](../spec/creatures/creature-identity-species-ownership.md)、[普通遭遇、触发与修正](../spec/world/wild-encounters-and-modifiers.md)、[规则配置档案与数据变体](../spec/core/rule-configuration-and-data-variants.md)、[漫游与 Poké Radar](../spec/world/roaming-and-poke-radar.md)、[野外被动变化与失败回程](../spec/world/field-passive-effects-and-blackout.md)

### 遭遇修正钩子：示例/默认修正（73 行）

- <a id="src-202"></a>[普通遭遇、触发与修正](../spec/world/wild-encounters-and-modifiers.md)、[示例工程证据与能力覆盖](../spec/authoring/demo-evidence-and-capability-coverage.md)、[规则配置档案与数据变体](../spec/core/rule-configuration-and-data-variants.md)、[通知、扩展与插件](../spec/core/events-extensions-plugins.md)、[漫游与 Poké Radar](../spec/world/roaming-and-poke-radar.md)

### 世界时间与场地 §3.1＋计时与统计 §3

- <a id="src-205"></a>[时间、随机、计步与统计](../spec/core/time-random-steps-stats.md)、[世界绘制与视觉过渡](../spec/world/world-rendering-and-visual-transitions.md)、[世界时间、天气与场地能力](../spec/world/world-time-weather-field-moves.md)、[动态形态与展示属性](../spec/creatures/dynamic-forms-and-display.md)、[统计字段目录](../spec/core/stats-directory.md)

### 世界时间与场地 §C/D

- <a id="src-206"></a>[主动道具与培养/教学](../spec/creatures/item-use-and-training.md)、[统计字段目录](../spec/core/stats-directory.md)、[地形、运动与载具](../spec/world/terrain-movement-vehicles.md)、[地图事件、NPC 与跟随](../spec/world/map-events-npc-followers.md)、[世界时间、天气与场地能力](../spec/world/world-time-weather-field-moves.md)

### 钓鱼与树果 §F1–F5

- <a id="src-207"></a>[统计字段目录](../spec/core/stats-directory.md)、[钓鱼](../spec/world/fishing.md)、[树果种植](../spec/world/berry-plants.md)

### 钓鱼与树果 §B1–B5

- <a id="src-208"></a>[统计字段目录](../spec/core/stats-directory.md)、[树果种植](../spec/world/berry-plants.md)、[钓鱼](../spec/world/fishing.md)

### 随机地牢 §3–6＋示例工程 §4.5

- <a id="src-210"></a>[示例工程证据与能力覆盖](../spec/authoring/demo-evidence-and-capability-coverage.md)、[时间、随机、计步与统计](../spec/core/time-random-steps-stats.md)、[随机地牢](../spec/world/random-dungeons.md)

### 事件与路线 §D（NPC/跟随引用）＋训练家与伙伴/捕获与接收（宝可梦工具函数）

- <a id="src-289"></a>[生物身份、物种记录、来源与拥有者](../spec/creatures/creature-identity-species-ownership.md)、[HP、异常状态、已知招式与持有状态](../spec/creatures/hp-status-moves-helditem.md)、[队伍、盒子与成员移动](../spec/creatures/party-and-storage.md)、[获得、赠送与脚本交换](../spec/creatures/acquisition-gifts-and-script-trade.md)、[解释器命令兼容矩阵](../spec/world/interpreter-command-matrix.md)、[地图事件、NPC 与跟随](../spec/world/map-events-npc-followers.md)、[移动路线命令矩阵](../spec/world/move-route-matrix.md)、[玩家、NPC 训练家与伙伴](../spec/creatures/player-trainers-partners.md)、[捕获判定与接收策略](../spec/creatures/capture-and-receiving.md)


## 个体、队伍与养成

### 能力与属性 §4（等级↔经验接口）＋成长与学招 §A（成长曲线）

- <a id="src-079"></a>[成长、学习替换与友好](../spec/creatures/growth-learning-and-friendship.md)、[属性派生、特性选择与六项能力](../spec/creatures/attributes-ability-and-stats.md)、[Shadow、Hyper、成长暂存与净化生命周期](../spec/creatures/shadow-hyper-and-purification.md)

### 基础进化 §3（条件族目录）＋情境进化 §2（情境输入）

- <a id="src-085"></a>[示例工程证据与能力覆盖](../spec/authoring/demo-evidence-and-capability-coverage.md)、[规则配置档案与数据变体](../spec/core/rule-configuration-and-data-variants.md)、[动态形态与展示属性](../spec/creatures/dynamic-forms-and-display.md)、[基础进化](../spec/creatures/basic-evolution.md)、[情境输入、默认数据与前后状态](../spec/creatures/context-inputs-and-scenarios.md)、[情境、交换、战后成就与事件进化](../spec/creatures/contextual-trade-and-post-battle-evolution.md)

### 寄养会话 §3–5＋遗传与后代 §2–3＋蛋与孵化 §B/C

- <a id="src-209"></a>[队伍、盒子与成员移动](../spec/creatures/party-and-storage.md)、[获得、赠送与脚本交换](../spec/creatures/acquisition-gifts-and-script-trade.md)、[寄养会话与兼容性](../spec/creatures/daycare-and-breeding-session.md)、[蛋状态与孵化](../spec/creatures/eggs-and-hatching.md)、[遗传与后代生成](../spec/creatures/inheritance-and-offspring.md)

### 背包与道具库 §3–5＋道具使用 §3–5＋商店与兑换 §3–4＋持物效果 §A–F＋钓鱼与树果 §B1–B5＋邮件与神秘礼物 §2–6＋捕获与接收 §2–6＋漫游与雷达 §D–E

共同涉及 [背包、物品储存与快捷登记](../spec/creatures/bag-and-item-storage.md)、[主动道具与培养/教学](../spec/creatures/item-use-and-training.md)、[买卖与 BP 商店](../spec/creatures/shops-and-exchanges.md)、[持物效果有界覆盖](../spec/battle/held-item-effect-coverage.md)、[持有物计算、触发与消耗](../spec/battle/held-item-triggers-and-consumption.md)、[钓鱼](../spec/world/fishing.md)、[树果种植](../spec/world/berry-plants.md)、[邮件与神秘礼物](../spec/creatures/mail-and-mystery-gift.md)、[捕获判定与接收策略](../spec/creatures/capture-and-receiving.md)、[漫游与 Poké Radar](../spec/world/roaming-and-poke-radar.md)。

- <a id="src-211"></a>[HP、异常状态、已知招式与持有状态](../spec/creatures/hp-status-moves-helditem.md)、[成长、学习替换与友好](../spec/creatures/growth-learning-and-friendship.md)
- <a id="src-212"></a>[HP、异常状态、已知招式与持有状态](../spec/creatures/hp-status-moves-helditem.md)、[成长、学习替换与友好](../spec/creatures/growth-learning-and-friendship.md)、[统计字段目录](../spec/core/stats-directory.md)
- <a id="src-213"></a>[AI 通用数值、状态与阶级评估](../spec/battle/generic-numerical-and-status-evaluation.md)、[AI 场域、伤害恢复与多目标评估](../spec/battle/field-damage-healing-and-target-evaluation.md)
- <a id="src-214"></a>[内容身份、注册与 schema](../spec/core/content-identity-and-schema.md)、[时间、随机、计步与统计](../spec/core/time-random-steps-stats.md)、[迁移、失败与恢复](../spec/core/migration-failure-recovery.md)、[野外被动变化与失败回程](../spec/world/field-passive-effects-and-blackout.md)
- <a id="src-215"></a>[规则配置档案与数据变体](../spec/core/rule-configuration-and-data-variants.md)、[统计字段目录](../spec/core/stats-directory.md)
- <a id="src-216"></a>[HP、异常状态、已知招式与持有状态](../spec/creatures/hp-status-moves-helditem.md)、[队伍与摘要界面（查看／选择／成员操作与真实写入）](../spec/ui/party-and-summary-ui.md)
- <a id="src-218"></a>[Triple Triad](../spec/ui/triple-triad.md)、[标题、载入、选项、暂停与 PC（主导航）](../spec/ui/title-load-options-pause-and-pc.md)

### 动态形态 §3–5＋遗传与后代 §2–3＋蛋与孵化 §B/C＋图鉴 §3

共同涉及 [动态形态与展示属性](../spec/creatures/dynamic-forms-and-display.md)、[遗传与后代生成](../spec/creatures/inheritance-and-offspring.md)、[蛋状态与孵化](../spec/creatures/eggs-and-hatching.md)、[图鉴记录、区域与内容规则](../spec/creatures/pokedex-records-regions-and-content.md)。

- <a id="src-219"></a>[战斗成长交界、回合末与终局](../spec/battle/growth-end-of-round-and-battle-outcomes.md)、[战斗记录与回放](../spec/battle/battle-recording-and-playback.md)、[获得、赠送与脚本交换](../spec/creatures/acquisition-gifts-and-script-trade.md)、[示例工程证据与能力覆盖](../spec/authoring/demo-evidence-and-capability-coverage.md)
- <a id="src-220"></a>[命令、特殊行动、服从性与行动顺序](../spec/battle/commands-obedience-and-action-order.md)、[统计字段目录](../spec/core/stats-directory.md)、[Shadow、Hyper、成长暂存与净化生命周期](../spec/creatures/shadow-hyper-and-purification.md)、[野外被动变化与失败回程](../spec/world/field-passive-effects-and-blackout.md)
- <a id="src-222"></a>[队伍、盒子与成员移动](../spec/creatures/party-and-storage.md)、[获得、赠送与脚本交换](../spec/creatures/acquisition-gifts-and-script-trade.md)、[规则配置档案与数据变体](../spec/core/rule-configuration-and-data-variants.md)、[Shadow、Hyper、成长暂存与净化生命周期](../spec/creatures/shadow-hyper-and-purification.md)

### 个体身份 §3–5＋能力与属性 §3–4＋个体状态 §3–5＋动态形态 §3–5

- <a id="src-223"></a>[战斗上下文与参与者](../spec/battle/battle-context-and-participants.md)、[战斗记录与回放](../spec/battle/battle-recording-and-playback.md)、[生物身份、物种记录、来源与拥有者](../spec/creatures/creature-identity-species-ownership.md)、[HP、异常状态、已知招式与持有状态](../spec/creatures/hp-status-moves-helditem.md)、[属性派生、特性选择与六项能力](../spec/creatures/attributes-ability-and-stats.md)、[动态形态与展示属性](../spec/creatures/dynamic-forms-and-display.md)

### Mega与Primal §3–6

- <a id="src-224"></a>[生物身份、物种记录、来源与拥有者](../spec/creatures/creature-identity-species-ownership.md)、[Mega、Primal 与显式还原](../spec/creatures/mega-and-primal-reversion.md)、[默认特殊形态资格数据](../spec/creatures/transformation-data.md)

### 暗影与净化 §2–9

- <a id="src-225"></a>[战斗成长交界、回合末与终局](../spec/battle/growth-end-of-round-and-battle-outcomes.md)、[成长、学习替换与友好](../spec/creatures/growth-learning-and-friendship.md)、[心量表数据、可选内容与固定向量](../spec/creatures/shadow-data-and-vectors.md)、[Shadow、Hyper、成长暂存与净化生命周期](../spec/creatures/shadow-hyper-and-purification.md)

### 个体状态 §5（已知招式、PP 与最初招式记录）＋成长与学招 §D（学习/替换/遗忘/重学）

- <a id="src-226"></a>[HP、异常状态、已知招式与持有状态](../spec/creatures/hp-status-moves-helditem.md)、[弃用告警机制](../spec/core/deprecation-appendix.md)、[成长、学习替换与友好](../spec/creatures/growth-learning-and-friendship.md)

### 个体身份 §D（来源与拥有者）＋训练家与伙伴 §A（拥有者 ID/语言）

- <a id="src-227"></a>[生物身份、物种记录、来源与拥有者](../spec/creatures/creature-identity-species-ownership.md)、[玩家、NPC 训练家与伙伴](../spec/creatures/player-trainers-partners.md)、[Lottery](../spec/ui/lottery.md)

### 训练家与伙伴 §3–6＋队伍与存储 §3–6＋图鉴 §3

共同涉及 [玩家、NPC 训练家与伙伴](../spec/creatures/player-trainers-partners.md)、[队伍、盒子与成员移动](../spec/creatures/party-and-storage.md)、[图鉴记录、区域与内容规则](../spec/creatures/pokedex-records-regions-and-content.md)。

- <a id="src-228"></a>[设施基础会话](../spec/battle/facility-session-and-restoration.md)、[生物身份、物种记录、来源与拥有者](../spec/creatures/creature-identity-species-ownership.md)
- <a id="src-229"></a>[内容编辑器（物种/道具/训练家/元数据/图鉴列表）](../spec/authoring/content-editors.md)、[工程转换与制作工具](../spec/authoring/project-conversion-and-authoring-tools.md)
- <a id="src-231"></a>[生物身份、物种记录、来源与拥有者](../spec/creatures/creature-identity-species-ownership.md)、[买卖与 BP 商店](../spec/creatures/shops-and-exchanges.md)、[邮件与神秘礼物](../spec/creatures/mail-and-mystery-gift.md)
- <a id="src-232"></a>[获得、赠送与脚本交换](../spec/creatures/acquisition-gifts-and-script-trade.md)、[蛋状态与孵化](../spec/creatures/eggs-and-hatching.md)、[Triple Triad](../spec/ui/triple-triad.md)


## 战斗、策略与设施

### 战斗设置常量定义（30 个常量）

战斗侧规则从参战者到录像回放各有适用条件。配置 §7 列未验证组合。

- <a id="src-019"></a>[规则配置档案与数据变体](../spec/core/rule-configuration-and-data-variants.md)

### 参战者 §7（临时规则字典 $game_temp.battle_rules）＋计时与统计/保存与启动（临时状态边界）

- <a id="src-032"></a>[战斗记录与回放](../spec/battle/battle-recording-and-playback.md)、[买卖与 BP 商店](../spec/creatures/shops-and-exchanges.md)、[标题、载入、选项、暂停与 PC（主导航）](../spec/ui/title-load-options-pause-and-pc.md)、[生物盒子与图鉴界面（整理、检索与收集信息浏览）](../spec/ui/storage-and-pokedex-ui.md)、[战斗上下文与参与者](../spec/battle/battle-context-and-participants.md)、[统计字段目录](../spec/core/stats-directory.md)、[时间、随机、计步与统计](../spec/core/time-random-steps-stats.md)、[保存、启动、新游戏与继续](../spec/core/save-startup-continue.md)

### 参战者 §3–6＋指令与顺序 §3–6＋换人与逃离 §3–6＋成长与终局 §3–7

共同涉及 [战斗上下文与参与者](../spec/battle/battle-context-and-participants.md)、[换人、替补、场上位置移动与逃跑](../spec/battle/switching-positioning-and-escape.md)、[战斗成长交界、回合末与终局](../spec/battle/growth-end-of-round-and-battle-outcomes.md)、[命令、特殊行动、服从性与行动顺序](../spec/battle/commands-obedience-and-action-order.md)。

- <a id="src-117"></a>[战斗天气、场地、阵营与位置效果](../spec/battle/weather-terrain-side-and-position-effects.md)
- <a id="src-118"></a>[招式换人、行动控制与物品变化](../spec/battle/switching-control-and-item-changes.md)
- <a id="src-119"></a>[成长、学习替换与友好](../spec/creatures/growth-learning-and-friendship.md)、[规则配置档案与数据变体](../spec/core/rule-configuration-and-data-variants.md)、[统计字段目录](../spec/core/stats-directory.md)
- <a id="src-120"></a>[招式属性、目标与复制调用](../spec/battle/move-attributes-targeting-and-calling.md)、[设施基础会话](../spec/battle/facility-session-and-restoration.md)
- <a id="src-121"></a>[战斗天气、场地、阵营与位置效果](../spec/battle/weather-terrain-side-and-position-effects.md)、[招式换人、行动控制与物品变化](../spec/battle/switching-control-and-item-changes.md)
- <a id="src-122"></a>[AI 总体决策、能力档与选择登记](../spec/battle/ai-action-selection-and-skill.md)、[战斗记录与回放](../spec/battle/battle-recording-and-playback.md)、[主动道具与培养/教学](../spec/creatures/item-use-and-training.md)
- <a id="src-123"></a>[战斗记录与回放](../spec/battle/battle-recording-and-playback.md)、[特性参与计算、免疫与有效性](../spec/battle/ability-calculation-modifiers.md)、[战斗交互与呈现](../spec/ui/battle-interaction-and-presentation.md)
- <a id="src-124"></a>[特性阶段触发、反应与连锁](../spec/battle/ability-phase-triggers.md)、[战斗记录与回放](../spec/battle/battle-recording-and-playback.md)
- <a id="src-125"></a>[特性阶段触发、反应与连锁](../spec/battle/ability-phase-triggers.md)、[AI 总体决策、能力档与选择登记](../spec/battle/ai-action-selection-and-skill.md)
- <a id="src-126"></a>[招式换人、行动控制与物品变化](../spec/battle/switching-control-and-item-changes.md)
- <a id="src-127"></a>[战斗天气、场地、阵营与位置效果](../spec/battle/weather-terrain-side-and-position-effects.md)、[招式换人、行动控制与物品变化](../spec/battle/switching-control-and-item-changes.md)、[特性阶段触发、反应与连锁](../spec/battle/ability-phase-triggers.md)

### 属性命中与伤害 §6＋异常与阶级 §2–4＋伤害与治疗 §2–6＋招式属性、目标与控制＋特性修正 §B–E＋特性触发 §2–6＋持物效果 §B–E＋个体状态 §3–5

共同涉及 [招式属性、目标与复制调用](../spec/battle/move-attributes-targeting-and-calling.md)、[招式换人、行动控制与物品变化](../spec/battle/switching-control-and-item-changes.md)、[战斗类型、命中与伤害计算](../spec/battle/types-accuracy-and-damage.md)、[有界效果归属与数据对应](../spec/battle/status-effects-coverage.md)、[异常状态、能力阶级与免疫](../spec/battle/statuses-stat-stages-and-immunities.md)、[多次攻击、特殊伤害与恢复——有界效果覆盖](../spec/battle/damage-healing-coverage.md)、[多次攻击、特殊伤害与恢复](../spec/battle/damage-multihit-and-healing.md)、[覆盖与默认数据附表](../spec/battle/attributes-targeting-calling-data.md)、[有界覆盖与默认数据附表](../spec/battle/control-items-coverage-data.md)、[特性参与计算、免疫与有效性](../spec/battle/ability-calculation-modifiers.md)、[特性阶段触发、反应与连锁](../spec/battle/ability-phase-triggers.md)、[持物效果有界覆盖](../spec/battle/held-item-effect-coverage.md)、[持有物计算、触发与消耗](../spec/battle/held-item-triggers-and-consumption.md)、[HP、异常状态、已知招式与持有状态](../spec/creatures/hp-status-moves-helditem.md)。

- <a id="src-128"></a>[战斗上下文与参与者](../spec/battle/battle-context-and-participants.md)、[战斗天气、场地、阵营与位置效果](../spec/battle/weather-terrain-side-and-position-effects.md)
- <a id="src-129"></a>[战斗上下文与参与者](../spec/battle/battle-context-and-participants.md)、[换人、替补、场上位置移动与逃跑](../spec/battle/switching-positioning-and-escape.md)、[战斗成长交界、回合末与终局](../spec/battle/growth-end-of-round-and-battle-outcomes.md)
- <a id="src-130"></a>[战斗上下文与参与者](../spec/battle/battle-context-and-participants.md)、[换人、替补、场上位置移动与逃跑](../spec/battle/switching-positioning-and-escape.md)、[战斗成长交界、回合末与终局](../spec/battle/growth-end-of-round-and-battle-outcomes.md)
- <a id="src-131"></a>[捕获判定与接收策略](../spec/creatures/capture-and-receiving.md)
- <a id="src-132"></a>仅涉及上列规格。
- <a id="src-133"></a>[动态形态与展示属性](../spec/creatures/dynamic-forms-and-display.md)
- <a id="src-134"></a>[命令、特殊行动、服从性与行动顺序](../spec/battle/commands-obedience-and-action-order.md)、[战斗成长交界、回合末与终局](../spec/battle/growth-end-of-round-and-battle-outcomes.md)、[战斗天气、场地、阵营与位置效果](../spec/battle/weather-terrain-side-and-position-effects.md)
- <a id="src-135"></a>[命令、特殊行动、服从性与行动顺序](../spec/battle/commands-obedience-and-action-order.md)
- <a id="src-136"></a>[命令、特殊行动、服从性与行动顺序](../spec/battle/commands-obedience-and-action-order.md)、[战斗天气、场地、阵营与位置效果](../spec/battle/weather-terrain-side-and-position-effects.md)
- <a id="src-137"></a>仅涉及上列规格。

### 属性命中与伤害 §3–6＋伤害与治疗 §2–6＋招式属性与目标 §2–6＋招式控制与道具 §2–5＋特性修正 §C–E＋持物效果 §B–F

共同涉及 [战斗类型、命中与伤害计算](../spec/battle/types-accuracy-and-damage.md)、[多次攻击、特殊伤害与恢复——有界效果覆盖](../spec/battle/damage-healing-coverage.md)、[多次攻击、特殊伤害与恢复](../spec/battle/damage-multihit-and-healing.md)、[覆盖与默认数据附表](../spec/battle/attributes-targeting-calling-data.md)、[招式属性、目标与复制调用](../spec/battle/move-attributes-targeting-and-calling.md)、[有界覆盖与默认数据附表](../spec/battle/control-items-coverage-data.md)、[招式换人、行动控制与物品变化](../spec/battle/switching-control-and-item-changes.md)、[特性参与计算、免疫与有效性](../spec/battle/ability-calculation-modifiers.md)、[持物效果有界覆盖](../spec/battle/held-item-effect-coverage.md)、[持有物计算、触发与消耗](../spec/battle/held-item-triggers-and-consumption.md)。

- <a id="src-138"></a>[AI 通用数值、状态与阶级评估](../spec/battle/generic-numerical-and-status-evaluation.md)、[AI 场域、伤害恢复与多目标评估](../spec/battle/field-damage-healing-and-target-evaluation.md)、[HP、异常状态、已知招式与持有状态](../spec/creatures/hp-status-moves-helditem.md)、[规则配置档案与数据变体](../spec/core/rule-configuration-and-data-variants.md)
- <a id="src-139"></a>[战斗天气、场地、阵营与位置效果](../spec/battle/weather-terrain-side-and-position-effects.md)、[特性阶段触发、反应与连锁](../spec/battle/ability-phase-triggers.md)、[规则配置档案与数据变体](../spec/core/rule-configuration-and-data-variants.md)
- <a id="src-140"></a>[命令、特殊行动、服从性与行动顺序](../spec/battle/commands-obedience-and-action-order.md)、[规则配置档案与数据变体](../spec/core/rule-configuration-and-data-variants.md)、[Shadow、Hyper、成长暂存与净化生命周期](../spec/creatures/shadow-hyper-and-purification.md)
- <a id="src-141"></a>[战斗天气、场地、阵营与位置效果](../spec/battle/weather-terrain-side-and-position-effects.md)
- <a id="src-142"></a><a id="src-144"></a><a id="src-149"></a>[战斗天气、场地、阵营与位置效果](../spec/battle/weather-terrain-side-and-position-effects.md)
- <a id="src-143"></a>[战斗天气、场地、阵营与位置效果](../spec/battle/weather-terrain-side-and-position-effects.md)、[有界效果归属与数据对应](../spec/battle/status-effects-coverage.md)
- <a id="src-145"></a>[战斗天气、场地、阵营与位置效果](../spec/battle/weather-terrain-side-and-position-effects.md)、[战斗记录与回放](../spec/battle/battle-recording-and-playback.md)
- <a id="src-146"></a>[AI 场域、伤害恢复与多目标评估](../spec/battle/field-damage-healing-and-target-evaluation.md)
- <a id="src-147"></a>[战斗天气、场地、阵营与位置效果](../spec/battle/weather-terrain-side-and-position-effects.md)、[异常状态、能力阶级与免疫](../spec/battle/statuses-stat-stages-and-immunities.md)
- <a id="src-148"></a>[战斗天气、场地、阵营与位置效果](../spec/battle/weather-terrain-side-and-position-effects.md)、[HP、异常状态、已知招式与持有状态](../spec/creatures/hp-status-moves-helditem.md)
- <a id="src-150"></a>[换人、替补、场上位置移动与逃跑](../spec/battle/switching-positioning-and-escape.md)、[战斗天气、场地、阵营与位置效果](../spec/battle/weather-terrain-side-and-position-effects.md)

### AI 决策主包装：基础选择次序（换出→主动道具→特殊模式截获→Mega 登记→招式/目标候选评分→最终选择）、异常记录包装、中途补位最佳替补请求

数组组织、遍历和分派的实现可自选。评分数值、条件、取整、排序和选择权重依所列规格。

- <a id="src-160"></a>[AI 总体决策、能力档与选择登记](../spec/battle/ai-action-selection-and-skill.md)、[决策默认数据与有界目录附表](../spec/battle/ai-decision-defaults.md)、[评估覆盖与默认数据附表](../spec/battle/evaluation-coverage-and-data.md)、[AI 通用数值、状态与阶级评估](../spec/battle/generic-numerical-and-status-evaluation.md)、[有界登记、覆盖与数据附表](../spec/battle/ai-effect-coverage.md)、[AI 场域、伤害恢复与多目标评估](../spec/battle/field-damage-healing-and-target-evaluation.md)、[有界登记、物品评级与条件数据附表](../spec/battle/item-control-coverage-and-data.md)、[AI 物品、调用与行动控制评估](../spec/battle/items-calling-and-control-evaluation.md)

### 换人意愿 11 项、否决 4 项、替补评分与回合末近似输入（:1–705 全文）

数组组织、遍历和分派的实现可自选。评分数值、条件、取整、排序和选择权重依所列规格。

- <a id="src-161"></a>[AI 总体决策、能力档与选择登记](../spec/battle/ai-action-selection-and-skill.md)、[决策默认数据与有界目录附表](../spec/battle/ai-decision-defaults.md)

### 主动道具决策：HP 治疗/状态/全阶级/X 道具/倒下复活五族（:1–220 全文）

数组组织、遍历和分派的实现可自选。评分数值、条件、取整、排序和选择权重依所列规格。

- <a id="src-162"></a>[AI 总体决策、能力档与选择登记](../spec/battle/ai-action-selection-and-skill.md)、[决策默认数据与有界目录附表](../spec/battle/ai-decision-defaults.md)

### Mega 意愿：资格为真即登记（:1–13 全文）

数组组织、遍历和分派的实现可自选。评分数值、条件、取整、排序和选择权重依所列规格。

- <a id="src-163"></a>[AI 总体决策、能力档与选择登记](../spec/battle/ai-action-selection-and-skill.md)、[决策默认数据与有界目录附表](../spec/battle/ai-decision-defaults.md)

### 招式/目标候选生成、评估替换、重定向近似、野生额外偏好、阈值系数与权重选取（:1–393 全文）

数组组织、遍历和分派的实现可自选。评分数值、条件、取整、排序和选择权重依所列规格。

- <a id="src-164"></a>[AI 总体决策、能力档与选择登记](../spec/battle/ai-action-selection-and-skill.md)、[决策默认数据与有界目录附表](../spec/battle/ai-decision-defaults.md)、[评估覆盖与默认数据附表](../spec/battle/evaluation-coverage-and-data.md)、[AI 通用数值、状态与阶级评估](../spec/battle/generic-numerical-and-status-evaluation.md)、[有界登记、覆盖与数据附表](../spec/battle/ai-effect-coverage.md)、[AI 场域、伤害恢复与多目标评估](../spec/battle/field-damage-healing-and-target-evaluation.md)、[有界登记、物品评级与条件数据附表](../spec/battle/item-control-coverage-and-data.md)、[AI 物品、调用与行动控制评估](../spec/battle/items-calling-and-control-evaluation.md)

### 通用效果评分：阶级升降 helper 与值得变化（:1–572）、天气/地形评分（:573–797）

数组组织、遍历和分派的实现可自选。评分数值、条件、取整、排序和选择权重依所列规格。

- <a id="src-165"></a>[评估覆盖与默认数据附表](../spec/battle/evaluation-coverage-and-data.md)、[AI 通用数值、状态与阶级评估](../spec/battle/generic-numerical-and-status-evaluation.md)、[有界登记、覆盖与数据附表](../spec/battle/ai-effect-coverage.md)、[AI 场域、伤害恢复与多目标评估](../spec/battle/field-damage-healing-and-target-evaluation.md)、[有界登记、物品评级与条件数据附表](../spec/battle/item-control-coverage-and-data.md)、[AI 物品、调用与行动控制评估](../spec/battle/items-calling-and-control-evaluation.md)

### 22 项通用修正（:1–517 全文）

数组组织、遍历和分派的实现可自选。评分数值、条件、取整、排序和选择权重依所列规格。

- <a id="src-166"></a>[评估覆盖与默认数据附表](../spec/battle/evaluation-coverage-and-data.md)、[AI 通用数值、状态与阶级评估](../spec/battle/generic-numerical-and-status-evaluation.md)、[有界登记、覆盖与数据附表](../spec/battle/ai-effect-coverage.md)、[AI 场域、伤害恢复与多目标评估](../spec/battle/field-damage-healing-and-target-evaluation.md)、[有界登记、物品评级与条件数据附表](../spec/battle/item-control-coverage-and-data.md)、[AI 物品、调用与行动控制评估](../spec/battle/items-calling-and-control-evaluation.md)

### 吸收/浮空/毒近似（:1–98）、基础能力数据（:101–159）与能力评级（:235–380）、基础物品与 ItemRanking（:387 起）（:1–599 已读）

数组组织、遍历和分派的实现可自选。评分数值、条件、取整、排序和选择权重依所列规格。

- <a id="src-167"></a>[AI 总体决策、能力档与选择登记](../spec/battle/ai-action-selection-and-skill.md)、[决策默认数据与有界目录附表](../spec/battle/ai-decision-defaults.md)、[评估覆盖与默认数据附表](../spec/battle/evaluation-coverage-and-data.md)、[AI 通用数值、状态与阶级评估](../spec/battle/generic-numerical-and-status-evaluation.md)、[有界登记、覆盖与数据附表](../spec/battle/ai-effect-coverage.md)、[AI 场域、伤害恢复与多目标评估](../spec/battle/field-damage-healing-and-target-evaluation.md)、[有界登记、物品评级与条件数据附表](../spec/battle/item-control-coverage-and-data.md)、[AI 物品、调用与行动控制评估](../spec/battle/items-calling-and-control-evaluation.md)

### 训练家技能值、标记与决策档（:1–100 全文）

数组组织、遍历和分派的实现可自选。评分数值、条件、取整、排序和选择权重依所列规格。

- <a id="src-168"></a>[AI 总体决策、能力档与选择登记](../spec/battle/ai-action-selection-and-skill.md)、[决策默认数据与有界目录附表](../spec/battle/ai-decision-defaults.md)

### 战斗者决策投影（:1–595）：决策语境读取、近似输入、物品价值/食用评分（:433–554）

数组组织、遍历和分派的实现可自选。评分数值、条件、取整、排序和选择权重依所列规格。

- <a id="src-169"></a>[AI 总体决策、能力档与选择登记](../spec/battle/ai-action-selection-and-skill.md)、[决策默认数据与有界目录附表](../spec/battle/ai-decision-defaults.md)、[评估覆盖与默认数据附表](../spec/battle/evaluation-coverage-and-data.md)、[AI 通用数值、状态与阶级评估](../spec/battle/generic-numerical-and-status-evaluation.md)、[有界登记、覆盖与数据附表](../spec/battle/ai-effect-coverage.md)、[AI 场域、伤害恢复与多目标评估](../spec/battle/field-damage-healing-and-target-evaluation.md)、[有界登记、物品评级与条件数据附表](../spec/battle/item-control-coverage-and-data.md)、[AI 物品、调用与行动控制评估](../spec/battle/items-calling-and-control-evaluation.md)

### 招式决策投影：数值、倍率、会心、命中与副作用（:1–563）

数组组织、遍历和分派的实现可自选。评分数值、条件、取整、排序和选择权重依所列规格。

- <a id="src-170"></a>[评估覆盖与默认数据附表](../spec/battle/evaluation-coverage-and-data.md)、[AI 通用数值、状态与阶级评估](../spec/battle/generic-numerical-and-status-evaluation.md)、[有界登记、覆盖与数据附表](../spec/battle/ai-effect-coverage.md)、[AI 场域、伤害恢复与多目标评估](../spec/battle/field-damage-healing-and-target-evaluation.md)、[有界登记、物品评级与条件数据附表](../spec/battle/item-control-coverage-and-data.md)、[AI 物品、调用与行动控制评估](../spec/battle/items-calling-and-control-evaluation.md)

### 杂项效果登记：失败/评分/基数注册（:1–168 正文；:169 起登记身份）

数组组织、遍历和分派的实现可自选。评分数值、条件、取整、排序和选择权重依所列规格。

- <a id="src-171"></a>[评估覆盖与默认数据附表](../spec/battle/evaluation-coverage-and-data.md)、[AI 通用数值、状态与阶级评估](../spec/battle/generic-numerical-and-status-evaluation.md)、[有界登记、覆盖与数据附表](../spec/battle/ai-effect-coverage.md)、[AI 场域、伤害恢复与多目标评估](../spec/battle/field-damage-healing-and-target-evaluation.md)、[有界登记、物品评级与条件数据附表](../spec/battle/item-control-coverage-and-data.md)、[AI 物品、调用与行动控制评估](../spec/battle/items-calling-and-control-evaluation.md)

### 阶级类效果登记（:1–1672 正文）

数组组织、遍历和分派的实现可自选。评分数值、条件、取整、排序和选择权重依所列规格。

- <a id="src-172"></a>[评估覆盖与默认数据附表](../spec/battle/evaluation-coverage-and-data.md)、[AI 通用数值、状态与阶级评估](../spec/battle/generic-numerical-and-status-evaluation.md)、[有界登记、覆盖与数据附表](../spec/battle/ai-effect-coverage.md)、[AI 场域、伤害恢复与多目标评估](../spec/battle/field-damage-healing-and-target-evaluation.md)、[有界登记、物品评级与条件数据附表](../spec/battle/item-control-coverage-and-data.md)、[AI 物品、调用与行动控制评估](../spec/battle/items-calling-and-control-evaluation.md)

### 战斗者其它效果登记（:1–1114 正文；后段浮空/变身登记）

数组组织、遍历和分派的实现可自选。评分数值、条件、取整、排序和选择权重依所列规格。

- <a id="src-173"></a>[评估覆盖与默认数据附表](../spec/battle/evaluation-coverage-and-data.md)、[AI 通用数值、状态与阶级评估](../spec/battle/generic-numerical-and-status-evaluation.md)、[有界登记、覆盖与数据附表](../spec/battle/ai-effect-coverage.md)、[AI 场域、伤害恢复与多目标评估](../spec/battle/field-damage-healing-and-target-evaluation.md)、[有界登记、物品评级与条件数据附表](../spec/battle/item-control-coverage-and-data.md)、[AI 物品、调用与行动控制评估](../spec/battle/items-calling-and-control-evaluation.md)

### 招式属性类效果登记（:1–1559 全文）

数组组织、遍历和分派的实现可自选。评分数值、条件、取整、排序和选择权重依所列规格。

- <a id="src-174"></a>[评估覆盖与默认数据附表](../spec/battle/evaluation-coverage-and-data.md)、[AI 通用数值、状态与阶级评估](../spec/battle/generic-numerical-and-status-evaluation.md)、[有界登记、覆盖与数据附表](../spec/battle/ai-effect-coverage.md)、[AI 场域、伤害恢复与多目标评估](../spec/battle/field-damage-healing-and-target-evaluation.md)、[有界登记、物品评级与条件数据附表](../spec/battle/item-control-coverage-and-data.md)、[AI 物品、调用与行动控制评估](../spec/battle/items-calling-and-control-evaluation.md)

### 多击类效果登记（:1–531 全文）

数组组织、遍历和分派的实现可自选。评分数值、条件、取整、排序和选择权重依所列规格。

- <a id="src-175"></a>[评估覆盖与默认数据附表](../spec/battle/evaluation-coverage-and-data.md)、[AI 通用数值、状态与阶级评估](../spec/battle/generic-numerical-and-status-evaluation.md)、[有界登记、覆盖与数据附表](../spec/battle/ai-effect-coverage.md)、[AI 场域、伤害恢复与多目标评估](../spec/battle/field-damage-healing-and-target-evaluation.md)、[有界登记、物品评级与条件数据附表](../spec/battle/item-control-coverage-and-data.md)、[AI 物品、调用与行动控制评估](../spec/battle/items-calling-and-control-evaluation.md)

### 治疗类效果登记（:1–683 全文）

数组组织、遍历和分派的实现可自选。评分数值、条件、取整、排序和选择权重依所列规格。

- <a id="src-176"></a>[评估覆盖与默认数据附表](../spec/battle/evaluation-coverage-and-data.md)、[AI 通用数值、状态与阶级评估](../spec/battle/generic-numerical-and-status-evaluation.md)、[有界登记、覆盖与数据附表](../spec/battle/ai-effect-coverage.md)、[AI 场域、伤害恢复与多目标评估](../spec/battle/field-damage-healing-and-target-evaluation.md)、[有界登记、物品评级与条件数据附表](../spec/battle/item-control-coverage-and-data.md)、[AI 物品、调用与行动控制评估](../spec/battle/items-calling-and-control-evaluation.md)

### 物品类效果登记（夺取/交换/移除/消耗/投掷五族注册）

数组组织、遍历和分派的实现可自选。评分数值、条件、取整、排序和选择权重依所列规格。

- <a id="src-177"></a>[评估覆盖与默认数据附表](../spec/battle/evaluation-coverage-and-data.md)、[AI 通用数值、状态与阶级评估](../spec/battle/generic-numerical-and-status-evaluation.md)、[有界登记、覆盖与数据附表](../spec/battle/ai-effect-coverage.md)、[AI 场域、伤害恢复与多目标评估](../spec/battle/field-damage-healing-and-target-evaluation.md)、[有界登记、物品评级与条件数据附表](../spec/battle/item-control-coverage-and-data.md)、[AI 物品、调用与行动控制评估](../spec/battle/items-calling-and-control-evaluation.md)

### 招式改变类效果登记（重定向/混合伤害/诅咒/反击/融合等注册）

数组组织、遍历和分派的实现可自选。评分数值、条件、取整、排序和选择权重依所列规格。

- <a id="src-178"></a>[评估覆盖与默认数据附表](../spec/battle/evaluation-coverage-and-data.md)、[AI 通用数值、状态与阶级评估](../spec/battle/generic-numerical-and-status-evaluation.md)、[有界登记、覆盖与数据附表](../spec/battle/ai-effect-coverage.md)、[AI 场域、伤害恢复与多目标评估](../spec/battle/field-damage-healing-and-target-evaluation.md)、[有界登记、物品评级与条件数据附表](../spec/battle/item-control-coverage-and-data.md)、[AI 物品、调用与行动控制评估](../spec/battle/items-calling-and-control-evaluation.md)

### 换人与行动控制类效果登记（逃跑/接力/拖出/拘束/先后/PP 限制等注册）

数组组织、遍历和分派的实现可自选。评分数值、条件、取整、排序和选择权重依所列规格。

- <a id="src-179"></a>[评估覆盖与默认数据附表](../spec/battle/evaluation-coverage-and-data.md)、[AI 通用数值、状态与阶级评估](../spec/battle/generic-numerical-and-status-evaluation.md)、[有界登记、覆盖与数据附表](../spec/battle/ai-effect-coverage.md)、[AI 场域、伤害恢复与多目标评估](../spec/battle/field-damage-healing-and-target-evaluation.md)、[有界登记、物品评级与条件数据附表](../spec/battle/item-control-coverage-and-data.md)、[AI 物品、调用与行动控制评估](../spec/battle/items-calling-and-control-evaluation.md)

### 成长与终局 §3–8＋天气与场地 §3–7＋持物效果 §E＋录像与回放 §2–6＋捕获与接收 §5–6

共同涉及 [战斗天气、场地、阵营与位置效果](../spec/battle/weather-terrain-side-and-position-effects.md)、[战斗成长交界、回合末与终局](../spec/battle/growth-end-of-round-and-battle-outcomes.md)、[持物效果有界覆盖](../spec/battle/held-item-effect-coverage.md)、[持有物计算、触发与消耗](../spec/battle/held-item-triggers-and-consumption.md)、[战斗记录与回放](../spec/battle/battle-recording-and-playback.md)、[捕获判定与接收策略](../spec/creatures/capture-and-receiving.md)。

- <a id="src-180"></a>仅涉及上列规格。
- <a id="src-181"></a>[战斗上下文与参与者](../spec/battle/battle-context-and-participants.md)
- <a id="src-182"></a>[战斗类型、命中与伤害计算](../spec/battle/types-accuracy-and-damage.md)、[多次攻击、特殊伤害与恢复](../spec/battle/damage-multihit-and-healing.md)
- <a id="src-183"></a>[战斗上下文与参与者](../spec/battle/battle-context-and-participants.md)、[换人、替补、场上位置移动与逃跑](../spec/battle/switching-positioning-and-escape.md)
- <a id="src-184"></a>[生物身份、物种记录、来源与拥有者](../spec/creatures/creature-identity-species-ownership.md)、[HP、异常状态、已知招式与持有状态](../spec/creatures/hp-status-moves-helditem.md)
- <a id="src-185"></a>[战斗上下文与参与者](../spec/battle/battle-context-and-participants.md)、[命令、特殊行动、服从性与行动顺序](../spec/battle/commands-obedience-and-action-order.md)、[参赛资格、队伍子集、等级调整与杯赛条款](../spec/battle/entry-eligibility-level-adjustment-and-clauses.md)
- <a id="src-186"></a>[战斗动画制作与交换（动画编辑器／组织器／单项与批量导入导出）](../spec/authoring/battle-animation-authoring-and-exchange.md)、[战斗交互与呈现](../spec/ui/battle-interaction-and-presentation.md)
- <a id="src-187"></a>[命令、特殊行动、服从性与行动顺序](../spec/battle/commands-obedience-and-action-order.md)、[招式换人、行动控制与物品变化](../spec/battle/switching-control-and-item-changes.md)、[特性阶段触发、反应与连锁](../spec/battle/ability-phase-triggers.md)
- <a id="src-188"></a>[招式换人、行动控制与物品变化](../spec/battle/switching-control-and-item-changes.md)、[AI 通用数值、状态与阶级评估](../spec/battle/generic-numerical-and-status-evaluation.md)、[AI 场域、伤害恢复与多目标评估](../spec/battle/field-damage-healing-and-target-evaluation.md)
- <a id="src-189"></a>[成长、学习替换与友好](../spec/creatures/growth-learning-and-friendship.md)、[规则配置档案与数据变体](../spec/core/rule-configuration-and-data-variants.md)、[统计字段目录](../spec/core/stats-directory.md)、[钓鱼](../spec/world/fishing.md)

### 狩猎与捕虫 §3–7＋设施会话 §2–4＋宫殿与竞技场 §2–4＋录像与回放 §2–6

共同涉及 [Safari 与捕虫大会](../spec/battle/safari-and-bug-catching-contest.md)、[战斗交互与呈现](../spec/ui/battle-interaction-and-presentation.md)、[设施基础会话](../spec/battle/facility-session-and-restoration.md)、[Palace 与 Arena 变体](../spec/battle/palace-and-arena-variants.md)、[战斗记录与回放](../spec/battle/battle-recording-and-playback.md)。

- <a id="src-190"></a><a id="src-191"></a>[获得、赠送与脚本交换](../spec/creatures/acquisition-gifts-and-script-trade.md)
- <a id="src-192"></a><a id="src-193"></a>仅涉及上列规格。
- <a id="src-194"></a>[时间、随机、计步与统计](../spec/core/time-random-steps-stats.md)

### 开战编排：野生/训练家包装与核心开战入口、输入校验、跳过与返回、环境输入、默认表/窗口/抽取（749 行）

- <a id="src-199"></a>[战斗上下文与参与者](../spec/battle/battle-context-and-participants.md)、[战斗成长交界、回合末与终局](../spec/battle/growth-end-of-round-and-battle-outcomes.md)、[战斗天气、场地、阵营与位置效果](../spec/battle/weather-terrain-side-and-position-effects.md)、[漫游与 Poké Radar](../spec/world/roaming-and-poke-radar.md)、[战斗交互与呈现](../spec/ui/battle-interaction-and-presentation.md)、[生命周期演出与历程展示](../spec/ui/lifecycle-presentations-and-history.md)、[钓鱼](../spec/world/fishing.md)、[树果种植](../spec/world/berry-plants.md)

### 漫游宝可梦：状态/路线/推进/重置/覆盖开战（228 行）

- <a id="src-203"></a>[漫游与 Poké Radar](../spec/world/roaming-and-poke-radar.md)、[普通遭遇、触发与修正](../spec/world/wild-encounters-and-modifiers.md)

### 狩猎与捕虫 §3–7＋设施资格 §2–6＋设施会话 §2–4＋宫殿与竞技场 §2–4＋租赁与交换 §2–4＋录像与回放 §2–6＋设施内容生成 §3–8

共同涉及 [设施基础会话](../spec/battle/facility-session-and-restoration.md)、[战斗记录与回放](../spec/battle/battle-recording-and-playback.md)、[Factory 租借与换队](../spec/battle/factory-rentals-and-swaps.md)、[设施内容生成与模拟（挑战生成器——候选构造／合法性筛选／去重／评估与写出）](../spec/authoring/facility-content-generation-and-simulation.md)、[Safari 与捕虫大会](../spec/battle/safari-and-bug-catching-contest.md)、[参赛资格、队伍子集、等级调整与杯赛条款](../spec/battle/entry-eligibility-level-adjustment-and-clauses.md)、[默认杯赛、条款与资格目录附表](../spec/battle/entry-rules-and-cup-data.md)、[Palace 与 Arena 变体](../spec/battle/palace-and-arena-variants.md)。

- <a id="src-272"></a>仅涉及上列规格。
- <a id="src-273"></a>[示例工程证据与能力覆盖](../spec/authoring/demo-evidence-and-capability-coverage.md)
- <a id="src-274"></a>[属性派生、特性选择与六项能力](../spec/creatures/attributes-ability-and-stats.md)
- <a id="src-275"></a>[统计字段目录](../spec/core/stats-directory.md)、[Mega、Primal 与显式还原](../spec/creatures/mega-and-primal-reversion.md)
- <a id="src-276"></a>仅涉及上列规格。
- <a id="src-277"></a>[示例工程证据与能力覆盖](../spec/authoring/demo-evidence-and-capability-coverage.md)、[统计字段目录](../spec/core/stats-directory.md)、[标题、载入、选项、暂停与 PC（主导航）](../spec/ui/title-load-options-pause-and-pc.md)
- <a id="src-278"></a>仅涉及上列规格。
- <a id="src-279"></a>仅涉及上列规格。
- <a id="src-280"></a><a id="src-281"></a>仅涉及上列规格。
- <a id="src-282"></a>[战斗上下文与参与者](../spec/battle/battle-context-and-participants.md)
- <a id="src-283"></a>[获得、赠送与脚本交换](../spec/creatures/acquisition-gifts-and-script-trade.md)、[统计字段目录](../spec/core/stats-directory.md)、[Mega、Primal 与显式还原](../spec/creatures/mega-and-primal-reversion.md)
- <a id="src-284"></a><a id="src-285"></a><a id="src-286"></a><a id="src-287"></a>仅涉及上列规格。


## 界面与演出

### 消息与输入 §D（按键与文字输入）＋规则配置 词典（输入相关设置）

- <a id="src-016"></a>[背包、物品储存与快捷登记](../spec/creatures/bag-and-item-storage.md)、[消息、窗口与输入](../spec/ui/messages-windows-input.md)、[标题、载入、选项、暂停与 PC（主导航）](../spec/ui/title-load-options-pause-and-pc.md)、[Slot Machine](../spec/ui/slot-machine.md)、[绘制文本标记目录](../spec/ui/draw-text-tags.md)、[规则配置档案与数据变体](../spec/core/rule-configuration-and-data-variants.md)

### 图片的持续命令

图片时长1单位=.05游戏秒；旋转按运行时长，速度1每秒20度。即时命令继续、编号偏移及show/erase状态保留；命令矩阵只承接入口，不能排除持续行为。

- <a id="src-037"></a>[解释器命令兼容矩阵](../spec/world/interpreter-command-matrix.md)、[地图事件、NPC 与跟随](../spec/world/map-events-npc-followers.md)、[移动路线命令矩阵](../spec/world/move-route-matrix.md)、[战前过渡](../spec/world/pre-battle-transitions.md)、[世界绘制与视觉过渡](../spec/world/world-rendering-and-visual-transitions.md)

### 普通与战斗图片的更新

图片有效显示、原点/缩放、按ID排序与业务推进区间分开；普通推进1–50/战斗51–100，不规定视口容器。

- <a id="src-047"></a>[战前过渡](../spec/world/pre-battle-transitions.md)、[世界绘制与视觉过渡](../spec/world/world-rendering-and-visual-transitions.md)

### 倒计时的显示与停止

有起点才显示；负业务值显示00:00且不写回业务值；停止清起点隐藏。层次99998、图片200、闪屏500各有独立资格。

- <a id="src-048"></a>[战前过渡](../spec/world/pre-battle-transitions.md)、[世界绘制与视觉过渡](../spec/world/world-rendering-and-visual-transitions.md)

### 消息与输入 §3–7＋资源与音频 §C

共同涉及 [资源匹配、资源访问及声音](../spec/world/resource-matching-and-audio.md)、[绘制文本标记目录](../spec/ui/draw-text-tags.md)、[消息、窗口与输入](../spec/ui/messages-windows-input.md)。

- <a id="src-062"></a>[战斗动画制作与交换（动画编辑器／组织器／单项与批量导入导出）](../spec/authoring/battle-animation-authoring-and-exchange.md)
- <a id="src-063"></a>[情境、交换、战后成就与事件进化](../spec/creatures/contextual-trade-and-post-battle-evolution.md)
- <a id="src-064"></a><a id="src-065"></a><a id="src-073"></a>仅涉及上列规格。
- <a id="src-069"></a>[战斗动画制作与交换（动画编辑器／组织器／单项与批量导入导出）](../spec/authoring/battle-animation-authoring-and-exchange.md)
- <a id="src-071"></a>[弃用告警机制](../spec/core/deprecation-appendix.md)
- <a id="src-072"></a>[获得、赠送与脚本交换](../spec/creatures/acquisition-gifts-and-script-trade.md)、[设施内容生成与模拟（挑战生成器——候选构造／合法性筛选／去重／评估与写出）](../spec/authoring/facility-content-generation-and-simulation.md)、[情境、交换、战后成就与事件进化](../spec/creatures/contextual-trade-and-post-battle-evolution.md)、[漫游与 Poké Radar](../spec/world/roaming-and-poke-radar.md)

### 消息暂停图标

暂停显示入口先指定帧0；消息更新消费4帧/.15秒的运行钟相位。只承接具名可观察消费者，不要求源窗口结构。

- <a id="src-066"></a>[绘制文本标记目录](../spec/ui/draw-text-tags.md)、[消息、窗口与输入](../spec/ui/messages-windows-input.md)

### 暂停和导航图标

暂停4帧每帧.15秒，导航8帧每帧.1秒；开始暂停先帧0，后更新取运行钟相位。不能以内部精灵原语整体排除。

- <a id="src-068"></a>[绘制文本标记目录](../spec/ui/draw-text-tags.md)、[消息、窗口与输入](../spec/ui/messages-windows-input.md)、[队伍与摘要界面（查看／选择／成员操作与真实写入）](../spec/ui/party-and-summary-ui.md)、[生物盒子与图鉴界面（整理、检索与收集信息浏览）](../spec/ui/storage-and-pokedex-ui.md)、[背包、物品储存与商店界面（数量／目标选择与交易反馈）](../spec/ui/bag-item-storage-and-shop-ui.md)

### UI 场景基类：输入事件分发（确认/返回/更新三类回调）、图片组合与页面生命周期、等待与场景驱动入口（192 行）

其他派生场景的行为见各自界面规格。

- <a id="src-077"></a>[地图事件、NPC 与跟随](../spec/world/map-events-npc-followers.md)、[附：控制帮助（Controls help）四页场景合同](../spec/ui/controls-help-appendix.md)

### 战斗交互与呈现 §3–10（战斗交互与呈现）

共同涉及 [战斗交互与呈现](../spec/ui/battle-interaction-and-presentation.md)、[生命周期演出与历程展示](../spec/ui/lifecycle-presentations-and-history.md)。

- <a id="src-151"></a>[战斗记录与回放](../spec/battle/battle-recording-and-playback.md)、[战斗动画制作与交换（动画编辑器／组织器／单项与批量导入导出）](../spec/authoring/battle-animation-authoring-and-exchange.md)
- <a id="src-152"></a>[战斗记录与回放](../spec/battle/battle-recording-and-playback.md)
- <a id="src-153"></a>[命令、特殊行动、服从性与行动顺序](../spec/battle/commands-obedience-and-action-order.md)、[换人、替补、场上位置移动与逃跑](../spec/battle/switching-positioning-and-escape.md)、[战斗成长交界、回合末与终局](../spec/battle/growth-end-of-round-and-battle-outcomes.md)、[战斗记录与回放](../spec/battle/battle-recording-and-playback.md)
- <a id="src-154"></a>[战斗成长交界、回合末与终局](../spec/battle/growth-end-of-round-and-battle-outcomes.md)、[战斗动画制作与交换（动画编辑器／组织器／单项与批量导入导出）](../spec/authoring/battle-animation-authoring-and-exchange.md)
- <a id="src-155"></a>[命令、特殊行动、服从性与行动顺序](../spec/battle/commands-obedience-and-action-order.md)
- <a id="src-156"></a>[内容身份、注册与 schema](../spec/core/content-identity-and-schema.md)
- <a id="src-157"></a>[捕获判定与接收策略](../spec/creatures/capture-and-receiving.md)
- <a id="src-158"></a>仅涉及上列规格。
- <a id="src-159"></a>[调试情境与控制](../spec/authoring/debug-contexts-and-controls.md)、[设施内容生成与模拟（挑战生成器——候选构造／合法性筛选／去重／评估与写出）](../spec/authoring/facility-content-generation-and-simulation.md)

### 地点提示与照明

地点条资格/同名抑制/飞行先于消息/0.4+1.6+0.4秒中断；light/outdoorlight名称及回退；暗图64/176与直接FLASH先写标志后演出保留。

- <a id="src-196"></a>[地图拓扑与转移](../spec/world/map-topology-transfer.md)、[战前过渡](../spec/world/pre-battle-transitions.md)、[世界绘制与视觉过渡](../spec/world/world-rendering-and-visual-transitions.md)、[世界时间、天气与场地能力](../spec/world/world-time-weather-field-moves.md)

### 玩家、训练家和盒子的命名

玩家/NPC命名两模式与载入：4×4首行四帧周期.5秒；盒名两模式：单行四帧周期.4秒；运行钟相位，载入缺图失败合同保持。

- <a id="src-230"></a>[绘制文本标记目录](../spec/ui/draw-text-tags.md)、[消息、窗口与输入](../spec/ui/messages-windows-input.md)、[附：控制帮助（Controls help）四页场景合同](../spec/ui/controls-help-appendix.md)、[标题、载入、选项、暂停与 PC（主导航）](../spec/ui/title-load-options-pause-and-pc.md)、[附：训练家卡（Trainer Card）场景合同](../spec/ui/trainer-card-appendix.md)

### 消息与输入 §3–7＋领航器 §2–6＋标题与主菜单 §3–8＋队伍、仓库与背包界面＋战斗与生命周期呈现

训练家卡和控制帮助的范围仅限所列附表。

- <a id="src-233"></a><a id="src-235"></a><a id="src-236"></a><a id="src-237"></a><a id="src-238"></a><a id="src-239"></a><a id="src-240"></a><a id="src-241"></a><a id="src-242"></a><a id="src-243"></a><a id="src-244"></a><a id="src-245"></a><a id="src-246"></a><a id="src-247"></a><a id="src-248"></a><a id="src-249"></a><a id="src-250"></a><a id="src-252"></a><a id="src-253"></a><a id="src-254"></a><a id="src-255"></a><a id="src-256"></a><a id="src-257"></a><a id="src-258"></a><a id="src-259"></a><a id="src-260"></a><a id="src-261"></a><a id="src-262"></a><a id="src-263"></a><a id="src-264"></a>[绘制文本标记目录](../spec/ui/draw-text-tags.md)、[消息、窗口与输入](../spec/ui/messages-windows-input.md)、[Pokégear、区域地图、点唱机与电话](../spec/ui/pokegear-map-music-and-phone.md)、[附：控制帮助（Controls help）四页场景合同](../spec/ui/controls-help-appendix.md)、[标题、载入、选项、暂停与 PC（主导航）](../spec/ui/title-load-options-pause-and-pc.md)、[附：训练家卡（Trainer Card）场景合同](../spec/ui/trainer-card-appendix.md)、[队伍与摘要界面（查看／选择／成员操作与真实写入）](../spec/ui/party-and-summary-ui.md)、[生物盒子与图鉴界面（整理、检索与收集信息浏览）](../spec/ui/storage-and-pokedex-ui.md)、[背包、物品储存与商店界面（数量／目标选择与交易反馈）](../spec/ui/bag-item-storage-and-shop-ui.md)、[战斗交互与呈现](../spec/ui/battle-interaction-and-presentation.md)、[生命周期演出与历程展示](../spec/ui/lifecycle-presentations-and-history.md)

### 界面与演出的场景与机制

- <a id="src-234"></a>[附：控制帮助（Controls help）四页场景合同](../spec/ui/controls-help-appendix.md)
- <a id="src-251"></a>[附：训练家卡（Trainer Card）场景合同](../spec/ui/trainer-card-appendix.md)

### 卡牌与决斗 §2–6＋卡牌与决斗 §T-A–G＋转轮与翻牌 §S-A–F＋转轮与翻牌 §V-A–E＋彩票与挖矿 §L-A–E＋彩票与挖矿 §M-A–F＋拼图 §2–6

共同涉及 [Duel](../spec/ui/duel.md)、[Triple Triad](../spec/ui/triple-triad.md)、[Voltorb Flip](../spec/ui/voltorb-flip.md)、[Voltorb Flip 级别候选数据](../spec/ui/voltorb-layouts.md)、[Slot Machine](../spec/ui/slot-machine.md)、[Slot Machine 有序转轮数据附表](../spec/ui/slot-reels.md)、[Lottery](../spec/ui/lottery.md)、[Mining 候选与形状数据附表](../spec/ui/mining-data.md)、[Mining](../spec/ui/mining.md)、[Tile Puzzles（板块拼图小游戏）](../spec/ui/tile-puzzles.md)。

- <a id="src-265"></a>仅涉及上列规格。
- <a id="src-266"></a>仅涉及上列规格。
- <a id="src-267"></a>[统计字段目录](../spec/core/stats-directory.md)
- <a id="src-268"></a>[统计字段目录](../spec/core/stats-directory.md)
- <a id="src-269"></a>[时间、随机、计步与统计](../spec/core/time-random-steps-stats.md)
- <a id="src-270"></a>仅涉及上列规格。
- <a id="src-271"></a>仅涉及上列规格。

### 战斗音乐的六个入口

六选曲入口、下一战独立预置、训练家有序覆盖/确存空串、地图→全局→默认及引子记忆分列。FromType无普通消费者只限固定脚本定位；真实发声未证。

- <a id="src-290"></a>[玩家、NPC 训练家与伙伴](../spec/creatures/player-trainers-partners.md)、[资源匹配、资源访问及声音](../spec/world/resource-matching-and-audio.md)、[战前过渡](../spec/world/pre-battle-transitions.md)、[世界绘制与视觉过渡](../spec/world/world-rendering-and-visual-transitions.md)、[战斗交互与呈现](../spec/ui/battle-interaction-and-presentation.md)、[生命周期演出与历程展示](../spec/ui/lifecycle-presentations-and-history.md)


## 作者工具与示例工程

### 调试操作 §F（PBDebug 日志模块与持久性边界）

- <a id="src-005"></a>[战斗成长交界、回合末与终局](../spec/battle/growth-end-of-round-and-battle-outcomes.md)、[招式换人、行动控制与物品变化](../spec/battle/switching-control-and-item-changes.md)、[调试情境与控制](../spec/authoring/debug-contexts-and-controls.md)、[诊断、文件与 HTTP](../spec/core/diagnostics-files-http.md)

### 示例工程 §4.2（地图登记与户外图清单）＋地图转移/地形与移动/野外遭遇/世界时间与场地（地图元数据消费）

- <a id="src-204"></a>[战斗记录与回放](../spec/battle/battle-recording-and-playback.md)、[寄养会话与兼容性](../spec/creatures/daycare-and-breeding-session.md)、[普通遭遇、触发与修正](../spec/world/wild-encounters-and-modifiers.md)、[邮件与神秘礼物](../spec/creatures/mail-and-mystery-gift.md)、[示例工程证据与能力覆盖](../spec/authoring/demo-evidence-and-capability-coverage.md)、[地图拓扑与转移](../spec/world/map-topology-transfer.md)、[地形、运动与载具](../spec/world/terrain-movement-vehicles.md)、[世界时间、天气与场地能力](../spec/world/world-time-weather-field-moves.md)

### 设施内容生成 §9（名称生成全段）＋资源与音频 §A（资源匹配引用）

- <a id="src-288"></a>[参赛资格、队伍子集、等级调整与杯赛条款](../spec/battle/entry-eligibility-level-adjustment-and-clauses.md)、[玩家、NPC 训练家与伙伴](../spec/creatures/player-trainers-partners.md)、[主动道具与培养/教学](../spec/creatures/item-use-and-training.md)、[设施内容生成与模拟（挑战生成器——候选构造／合法性筛选／去重／评估与写出）](../spec/authoring/facility-content-generation-and-simulation.md)、[资源匹配、资源访问及声音](../spec/world/resource-matching-and-audio.md)

### 调试操作 §3–9＋内容编辑 §3–6＋地图编辑 §3–8＋动画制作 §3–10＋工程转换 §3–10＋设施内容生成 §3–8

共同涉及 [内容编辑器（物种/道具/训练家/元数据/图鉴列表）](../spec/authoring/content-editors.md)、[世界编辑器（地图连接/地图元数据/地形标签/遭遇/指标）](../spec/authoring/world-editors.md)、[战斗动画制作与交换（动画编辑器／组织器／单项与批量导入导出）](../spec/authoring/battle-animation-authoring-and-exchange.md)、[调试情境与控制](../spec/authoring/debug-contexts-and-controls.md)、[工程转换与制作工具](../spec/authoring/project-conversion-and-authoring-tools.md)、[设施内容生成与模拟（挑战生成器——候选构造／合法性筛选／去重／评估与写出）](../spec/authoring/facility-content-generation-and-simulation.md)。

- <a id="src-291"></a>[世界时间、天气与场地能力](../spec/world/world-time-weather-field-moves.md)
- <a id="src-292"></a><a id="src-293"></a><a id="src-294"></a>仅涉及上列规格。
- <a id="src-295"></a>仅涉及上列规格。
- <a id="src-296"></a><a id="src-297"></a><a id="src-298"></a><a id="src-299"></a><a id="src-300"></a>仅涉及上列规格。
- <a id="src-301"></a>[世界时间、天气与场地能力](../spec/world/world-time-weather-field-moves.md)
- <a id="src-302"></a><a id="src-305"></a><a id="src-306"></a><a id="src-307"></a><a id="src-310"></a>仅涉及上列规格。
- <a id="src-303"></a>[获得、赠送与脚本交换](../spec/creatures/acquisition-gifts-and-script-trade.md)、[蛋状态与孵化](../spec/creatures/eggs-and-hatching.md)
- <a id="src-304"></a>[寄养会话与兼容性](../spec/creatures/daycare-and-breeding-session.md)
- <a id="src-308"></a>[生物身份、物种记录、来源与拥有者](../spec/creatures/creature-identity-species-ownership.md)、[获得、赠送与脚本交换](../spec/creatures/acquisition-gifts-and-script-trade.md)、[寄养会话与兼容性](../spec/creatures/daycare-and-breeding-session.md)、[蛋状态与孵化](../spec/creatures/eggs-and-hatching.md)
- <a id="src-309"></a>仅涉及上列规格。


## 作者数据的读取与启用

本节保留早期静态规格的样本范围。实际启用还取决于[编译与加载](../spec/core/pbs-lifecycle.md)和[候选配置及未验证组合](../spec/core/rule-configuration-and-data-variants.md)。后续对四代备份中部分字段的观察及其依赖见[旧世代资料的读取条件](generation-data-compatibility.md)和[备份字段](backup-author-fields.md)。

### 第五至第八世代的备份资料

早期只定位到第五至第八世代的四组备份，每组九份文本，当时未作全文检查。后续静态观察包括 3,940 个物种或形态输入、2,696 个显示输入和 76 个遭遇输入。其字段、样本及同世代读取前提见[备份作者字段](backup-author-fields.md)和[旧世代资料的读取条件](generation-data-compatibility.md)。仅有备份不触发切换；整套编译、运行结果和混合世代组合仍未验证。 [对应作者数据与启用条件](authoring-data-coverage.md#cfg-34)

- <a id="src-328"></a><a id="src-329"></a><a id="src-330"></a><a id="src-331"></a><a id="src-332"></a><a id="src-333"></a><a id="src-334"></a><a id="src-335"></a><a id="src-336"></a><a id="src-337"></a><a id="src-338"></a><a id="src-339"></a><a id="src-340"></a><a id="src-341"></a><a id="src-342"></a><a id="src-343"></a><a id="src-344"></a><a id="src-345"></a><a id="src-346"></a><a id="src-347"></a><a id="src-348"></a><a id="src-349"></a><a id="src-350"></a><a id="src-351"></a><a id="src-352"></a><a id="src-353"></a><a id="src-354"></a><a id="src-355"></a><a id="src-356"></a><a id="src-357"></a><a id="src-358"></a><a id="src-359"></a><a id="src-360"></a><a id="src-361"></a><a id="src-362"></a><a id="src-363"></a>[规则配置档案与数据变体](../spec/core/rule-configuration-and-data-variants.md)

### 暗影物种、招式、道具与属性资料

暗影规格记录四文本的字面字段与样本目录：shadow_pokemon131节/525行、moves18节/213行、items4节/42行、types1节/7行；量表/招式样本全集及招式/物品数据在§3.1/§3.2。数据提取不证明启用、编译或运行组合。U06实际启用未知；顶层无对应Shadow专用节/文件，未提供可验证编译产物；不自动切换备份。 [对应作者数据与启用条件](authoring-data-coverage.md#cfg-35)

- <a id="src-364"></a><a id="src-365"></a><a id="src-366"></a><a id="src-367"></a>[心量表数据、可选内容与固定向量](../spec/creatures/shadow-data-and-vectors.md)、[Shadow、Hyper、成长暂存与净化生命周期](../spec/creatures/shadow-hyper-and-purification.md)

### abilities.txt

遗传与后代/蛋与孵化 孵化加速三个特性样本（abilities.txt:162,199,976——FastEggHatching 三特性）；不标「数据内容已读全覆盖」。 [abilities.txt的机制、样本及启用条件](authoring-data-coverage.md#cfg-01)

- <a id="src-368"></a>[特性参与计算、免疫与有效性](../spec/battle/ability-calculation-modifiers.md)、[特性阶段触发、反应与连锁](../spec/battle/ability-phase-triggers.md)、[属性派生、特性选择与六项能力](../spec/creatures/attributes-ability-and-stats.md)、[有界效果归属与数据对应](../spec/battle/status-effects-coverage.md)、[异常状态、能力阶级与免疫](../spec/battle/statuses-stat-stages-and-immunities.md)

### battle_facility_lists.txt

设施内容生成（25 行全文）＋示例工程 §4/§5（E34 全文 25 行）。 [battle_facility_lists.txt的机制、样本及启用条件](authoring-data-coverage.md#cfg-02)

- <a id="src-369"></a>[设施内容生成与模拟（挑战生成器——候选构造／合法性筛选／去重／评估与写出）](../spec/authoring/facility-content-generation-and-simulation.md)、[设施基础会话](../spec/battle/facility-session-and-restoration.md)、[规则配置档案与数据变体](../spec/core/rule-configuration-and-data-variants.md)

### battle_tower_pokemon.txt

设施内容生成/设施会话 头部格式样本（不声称全量逐条读取）。 [battle_tower_pokemon.txt的机制、样本及启用条件](authoring-data-coverage.md#cfg-03)

- <a id="src-370"></a>[设施基础会话](../spec/battle/facility-session-and-restoration.md)、[设施内容生成与模拟（挑战生成器——候选构造／合法性筛选／去重／评估与写出）](../spec/authoring/facility-content-generation-and-simulation.md)、[规则配置档案与数据变体](../spec/core/rule-configuration-and-data-variants.md)

### battle_tower_trainers.txt

设施内容生成/设施会话 头部格式样本（不声称全量逐条读取）。 [battle_tower_trainers.txt的机制、样本及启用条件](authoring-data-coverage.md#cfg-04)

- <a id="src-371"></a>[设施基础会话](../spec/battle/facility-session-and-restoration.md)、[设施内容生成与模拟（挑战生成器——候选构造／合法性筛选／去重／评估与写出）](../spec/authoring/facility-content-generation-and-simulation.md)、[规则配置档案与数据变体](../spec/core/rule-configuration-and-data-variants.md)

### berry_plants.txt

钓鱼与树果（berry_plants.txt 多段样本）。 [berry_plants.txt的机制、样本及启用条件](authoring-data-coverage.md#cfg-05)

- <a id="src-372"></a>[树果种植](../spec/world/berry-plants.md)

### cup_fancy_pkmn.txt

早期仅确认文件存在；已查的默认设施名单与具名脚本没有引用该文件。其他用途、完整内容和运行时启用情况未验证。见[设施名单的显式输入](generation-settings.md#设施名单的显式输入)。 [cup_fancy_pkmn.txt的机制、样本及启用条件](authoring-data-coverage.md#cfg-06)

- <a id="src-373"></a>[设施内容生成与模拟（挑战生成器——候选构造／合法性筛选／去重／评估与写出）](../spec/authoring/facility-content-generation-and-simulation.md)、[示例工程证据与能力覆盖](../spec/authoring/demo-evidence-and-capability-coverage.md)

### cup_fancy_pkmn_single.txt

早期证据限于[设施名单的显式输入](generation-settings.md#设施名单的显式输入)中的文件名引用，未读取该文件的数据样本。 [cup_fancy_pkmn_single.txt的机制、样本及启用条件](authoring-data-coverage.md#cfg-07)

- <a id="src-374"></a>[设施内容生成与模拟（挑战生成器——候选构造／合法性筛选／去重／评估与写出）](../spec/authoring/facility-content-generation-and-simulation.md)、[示例工程证据与能力覆盖](../spec/authoring/demo-evidence-and-capability-coverage.md)

### cup_fancy_trainers.txt

早期仅确认文件存在；已查的默认设施名单与具名脚本没有引用该文件。其他用途、完整内容和运行时启用情况未验证。见[设施名单的显式输入](generation-settings.md#设施名单的显式输入)。 [cup_fancy_trainers.txt的机制、样本及启用条件](authoring-data-coverage.md#cfg-08)

- <a id="src-375"></a>[设施内容生成与模拟（挑战生成器——候选构造／合法性筛选／去重／评估与写出）](../spec/authoring/facility-content-generation-and-simulation.md)、[示例工程证据与能力覆盖](../spec/authoring/demo-evidence-and-capability-coverage.md)

### cup_fancy_trainers_single.txt

早期证据限于[设施名单的显式输入](generation-settings.md#设施名单的显式输入)中的文件名引用，未读取该文件的数据样本。 [cup_fancy_trainers_single.txt的机制、样本及启用条件](authoring-data-coverage.md#cfg-09)

- <a id="src-376"></a>[设施内容生成与模拟（挑战生成器——候选构造／合法性筛选／去重／评估与写出）](../spec/authoring/facility-content-generation-and-simulation.md)、[示例工程证据与能力覆盖](../spec/authoring/demo-evidence-and-capability-coverage.md)

### cup_little_pkmn.txt

早期证据限于[设施名单的显式输入](generation-settings.md#设施名单的显式输入)中的文件名引用，未读取该文件的数据样本。 [cup_little_pkmn.txt的机制、样本及启用条件](authoring-data-coverage.md#cfg-10)

- <a id="src-377"></a>[设施内容生成与模拟（挑战生成器——候选构造／合法性筛选／去重／评估与写出）](../spec/authoring/facility-content-generation-and-simulation.md)、[示例工程证据与能力覆盖](../spec/authoring/demo-evidence-and-capability-coverage.md)

### cup_little_trainers.txt

早期证据限于[设施名单的显式输入](generation-settings.md#设施名单的显式输入)中的文件名引用，未读取该文件的数据样本。 [cup_little_trainers.txt的机制、样本及启用条件](authoring-data-coverage.md#cfg-11)

- <a id="src-378"></a>[设施内容生成与模拟（挑战生成器——候选构造／合法性筛选／去重／评估与写出）](../spec/authoring/facility-content-generation-and-simulation.md)、[示例工程证据与能力覆盖](../spec/authoring/demo-evidence-and-capability-coverage.md)

### cup_pika_pkmn.txt

早期证据限于[设施名单的显式输入](generation-settings.md#设施名单的显式输入)中的文件名引用，未读取该文件的数据样本。 [cup_pika_pkmn.txt的机制、样本及启用条件](authoring-data-coverage.md#cfg-12)

- <a id="src-379"></a>[设施内容生成与模拟（挑战生成器——候选构造／合法性筛选／去重／评估与写出）](../spec/authoring/facility-content-generation-and-simulation.md)、[示例工程证据与能力覆盖](../spec/authoring/demo-evidence-and-capability-coverage.md)

### cup_pika_trainers.txt

早期证据限于[设施名单的显式输入](generation-settings.md#设施名单的显式输入)中的文件名引用，未读取该文件的数据样本。 [cup_pika_trainers.txt的机制、样本及启用条件](authoring-data-coverage.md#cfg-13)

- <a id="src-380"></a>[设施内容生成与模拟（挑战生成器——候选构造／合法性筛选／去重／评估与写出）](../spec/authoring/facility-content-generation-and-simulation.md)、[示例工程证据与能力覆盖](../spec/authoring/demo-evidence-and-capability-coverage.md)

### cup_poke_pkmn.txt

早期证据限于[设施名单的显式输入](generation-settings.md#设施名单的显式输入)中的文件名引用，未读取该文件的数据样本。 [cup_poke_pkmn.txt的机制、样本及启用条件](authoring-data-coverage.md#cfg-14)

- <a id="src-381"></a>[设施内容生成与模拟（挑战生成器——候选构造／合法性筛选／去重／评估与写出）](../spec/authoring/facility-content-generation-and-simulation.md)、[示例工程证据与能力覆盖](../spec/authoring/demo-evidence-and-capability-coverage.md)

### cup_poke_trainers.txt

早期证据限于[设施名单的显式输入](generation-settings.md#设施名单的显式输入)中的文件名引用，未读取该文件的数据样本。 [cup_poke_trainers.txt的机制、样本及启用条件](authoring-data-coverage.md#cfg-15)

- <a id="src-382"></a>[设施内容生成与模拟（挑战生成器——候选构造／合法性筛选／去重／评估与写出）](../spec/authoring/facility-content-generation-and-simulation.md)、[示例工程证据与能力覆盖](../spec/authoring/demo-evidence-and-capability-coverage.md)

### dungeon_parameters.txt

示例工程（E34 全文 30 行）＋随机地牢（[cave]/[forest] 样本）。 [dungeon_parameters.txt的机制、样本及启用条件](authoring-data-coverage.md#cfg-16)

- <a id="src-383"></a>[随机地牢](../spec/world/random-dungeons.md)、[示例工程证据与能力覆盖](../spec/authoring/demo-evidence-and-capability-coverage.md)

### dungeon_tilesets.txt

随机地牢（[7]/[23] 样本）。 [dungeon_tilesets.txt的机制、样本及启用条件](authoring-data-coverage.md#cfg-17)

- <a id="src-384"></a>[随机地牢](../spec/world/random-dungeons.md)

### encounters.txt

示例工程（E34 全文 311 行）＋野外遭遇（[002] 水系钓竿段、[005]/[005,1] 陆地/夜间/雷达段）。 [encounters.txt的机制、样本及启用条件](authoring-data-coverage.md#cfg-18)

- <a id="src-385"></a>[普通遭遇、触发与修正](../spec/world/wild-encounters-and-modifiers.md)、[漫游与 Poké Radar](../spec/world/roaming-and-poke-radar.md)、[调试情境与控制](../spec/authoring/debug-contexts-and-controls.md)

### items.txt

招式属性与目标（自然之恩 Flags 数据读取）＋设施内容生成（25 个不同身份的章节标识检索——不称已读物品效果全文）；不声称全量逐条读取。 [items.txt的机制、样本及启用条件](authoring-data-coverage.md#cfg-19)

- <a id="src-386"></a>[招式属性、目标与复制调用](../spec/battle/move-attributes-targeting-and-calling.md)

### map_connections.txt

示例工程（E34 全文 40 行）＋地图转移（作者内容样本）。 [map_connections.txt的机制、样本及启用条件](authoring-data-coverage.md#cfg-20)

- <a id="src-387"></a>[地图拓扑与转移](../spec/world/map-topology-transfer.md)、[调试情境与控制](../spec/authoring/debug-contexts-and-controls.md)、[内容编辑器（物种/道具/训练家/元数据/图鉴列表）](../spec/authoring/content-editors.md)、[世界编辑器（地图连接/地图元数据/地形标签/遭遇/指标）](../spec/authoring/world-editors.md)

### map_metadata.txt

示例工程（E34 全文 398 行、69 节）＋世界时间与场地（Weather 行三例样本）。 [map_metadata.txt的机制、样本及启用条件](authoring-data-coverage.md#cfg-21)

- <a id="src-388"></a>[世界时间、天气与场地能力](../spec/world/world-time-weather-field-moves.md)、[调试情境与控制](../spec/authoring/debug-contexts-and-controls.md)、[内容编辑器（物种/道具/训练家/元数据/图鉴列表）](../spec/authoring/content-editors.md)、[世界编辑器（地图连接/地图元数据/地形标签/遭遇/指标）](../spec/authoring/world-editors.md)

### metadata.txt

示例工程（E34 全文 33 行）。 [metadata.txt的机制、样本及启用条件](authoring-data-coverage.md#cfg-22)

- <a id="src-389"></a>[示例工程证据与能力覆盖](../spec/authoring/demo-evidence-and-capability-coverage.md)、[调试情境与控制](../spec/authoring/debug-contexts-and-controls.md)、[内容编辑器（物种/道具/训练家/元数据/图鉴列表）](../spec/authoring/content-editors.md)、[世界编辑器（地图连接/地图元数据/地形标签/遭遇/指标）](../spec/authoring/world-editors.md)

### moves.txt

设施内容生成（AERIALACE/SWIFT/SKETCH 三段）＋招式属性与目标（SWORDSDANCE :6541–6550 目标数据审计）；不声称全量逐条读取。 [moves.txt的机制、样本及启用条件](authoring-data-coverage.md#cfg-23)

- <a id="src-390"></a>[招式属性、目标与复制调用](../spec/battle/move-attributes-targeting-and-calling.md)

### phone.txt

示例工程（E34 全文 48 行）＋领航器（顶层首 40 行结构样本）。 [phone.txt的机制、样本及启用条件](authoring-data-coverage.md#cfg-24)

- <a id="src-391"></a>[Pokégear、区域地图、点唱机与电话](../spec/ui/pokegear-map-music-and-phone.md)

### pokemon.txt

基础进化（NINCADA/EEVEE/TYROGUE/WURMPLE/KIRLIA 等进化样本群）＋设施内容生成（SMEARGLE :6189–6205）；不声称全量逐条读取。 [pokemon.txt的机制、样本及启用条件](authoring-data-coverage.md#cfg-25)

- <a id="src-392"></a>[基础进化](../spec/creatures/basic-evolution.md)、[寄养会话与兼容性](../spec/creatures/daycare-and-breeding-session.md)、[蛋状态与孵化](../spec/creatures/eggs-and-hatching.md)、[设施基础会话](../spec/battle/facility-session-and-restoration.md)、[有界覆盖与默认数据附表](../spec/battle/control-items-coverage-data.md)、[招式换人、行动控制与物品变化](../spec/battle/switching-control-and-item-changes.md)、[设施内容生成与模拟（挑战生成器——候选构造／合法性筛选／去重／评估与写出）](../spec/authoring/facility-content-generation-and-simulation.md)

### pokemon_forms.txt

Mega与Primal（48 个 Mega 目标字段、KYOGRE/GROUDON 形态 1）＋基础进化（RUNERIGUS 事件编号 2）；不声称全量逐条读取。 [pokemon_forms.txt的机制、样本及启用条件](authoring-data-coverage.md#cfg-26)

- <a id="src-393"></a>[Mega、Primal 与显式还原](../spec/creatures/mega-and-primal-reversion.md)、[默认特殊形态资格数据](../spec/creatures/transformation-data.md)、[基础进化](../spec/creatures/basic-evolution.md)、[情境、交换、战后成就与事件进化](../spec/creatures/contextual-trade-and-post-battle-evolution.md)、[情境输入、默认数据与前后状态](../spec/creatures/context-inputs-and-scenarios.md)

### pokemon_metrics.txt

未读——未见本文件数据样本阅读登记，不因机制在案声称内容已读。 [pokemon_metrics.txt的机制、样本及启用条件](authoring-data-coverage.md#cfg-27)

- <a id="src-394"></a>[内容编辑器（物种/道具/训练家/元数据/图鉴列表）](../spec/authoring/content-editors.md)、[世界编辑器（地图连接/地图元数据/地形标签/遭遇/指标）](../spec/authoring/world-editors.md)、[调试情境与控制](../spec/authoring/debug-contexts-and-controls.md)

### regional_dexes.txt

图鉴（两节 212 行结构样本；不声称逐条读取全部物种链）。 [regional_dexes.txt的机制、样本及启用条件](authoring-data-coverage.md#cfg-28)

- <a id="src-395"></a>[图鉴记录、区域与内容规则](../spec/creatures/pokedex-records-regions-and-content.md)、[调试情境与控制](../spec/authoring/debug-contexts-and-controls.md)

### ribbons.txt

schema 字段目录已读（标识/名称/图标位置/描述/标记；「图标位置只用于裁切非排序依据」）；不标数据内容已读全覆盖。 [ribbons.txt的机制、样本及启用条件](authoring-data-coverage.md#cfg-29)

- <a id="src-396"></a>[动态形态与展示属性](../spec/creatures/dynamic-forms-and-display.md)

### town_map.txt

示例工程（E34 全文 36 行）＋领航器（顶层首 30 行结构样本）。 [town_map.txt的机制、样本及启用条件](authoring-data-coverage.md#cfg-30)

- <a id="src-397"></a>[Pokégear、区域地图、点唱机与电话](../spec/ui/pokegear-map-music-and-phone.md)、[工程转换与制作工具](../spec/authoring/project-conversion-and-authoring-tools.md)、[示例工程证据与能力覆盖](../spec/authoring/demo-evidence-and-capability-coverage.md)

### trainer_types.txt

设施内容生成（189–196 YOUNGSTER）＋AI行动选择（技能样本）。 [trainer_types.txt的机制、样本及启用条件](authoring-data-coverage.md#cfg-31)

- <a id="src-398"></a>[调试情境与控制](../spec/authoring/debug-contexts-and-controls.md)、[设施内容生成与模拟（挑战生成器——候选构造／合法性筛选／去重／评估与写出）](../spec/authoring/facility-content-generation-and-simulation.md)、[示例工程证据与能力覆盖](../spec/authoring/demo-evidence-and-capability-coverage.md)

### trainers.txt

示例工程（E34 全文 118 行、20 节）。 [trainers.txt的机制、样本及启用条件](authoring-data-coverage.md#cfg-32)

- <a id="src-399"></a>[设施基础会话](../spec/battle/facility-session-and-restoration.md)、[调试情境与控制](../spec/authoring/debug-contexts-and-controls.md)、[内容编辑器（物种/道具/训练家/元数据/图鉴列表）](../spec/authoring/content-editors.md)、[世界编辑器（地图连接/地图元数据/地形标签/遭遇/指标）](../spec/authoring/world-editors.md)、[设施内容生成与模拟（挑战生成器——候选构造／合法性筛选／去重／评估与写出）](../spec/authoring/facility-content-generation-and-simulation.md)、[示例工程证据与能力覆盖](../spec/authoring/demo-evidence-and-capability-coverage.md)

### types.txt

招式属性与目标（默认身份/图标具名数据读取）；不声称全量字段逐条读取。 [types.txt的机制、样本及启用条件](authoring-data-coverage.md#cfg-33)

- <a id="src-400"></a>[调试情境与控制](../spec/authoring/debug-contexts-and-controls.md)


## 只确认身份或静态入口的材料

本节分别列出早期取样和后来已有具体记录的观察。宿主与资源条件见[验证范围与缺口](verification-boundaries.md)。

### 早期只确认身份的材料

此组先前仅登记材料身份。后续使用受限解析器对 messages_core.dat 的 10,697 项键与正文及其文本结构作了全量比对。原生载入和各语言的翻译质量仍未验证。见[序列化内容的观察范围](observation-limits.md)。

- <a id="src-001"></a><a id="src-002"></a><a id="src-316"></a><a id="src-317"></a><a id="src-318"></a><a id="src-319"></a><a id="src-320"></a><a id="src-321"></a><a id="src-322"></a><a id="src-323"></a><a id="src-324"></a><a id="src-325"></a><a id="src-327"></a><a id="src-401"></a><a id="src-425"></a>限于上述适用范围。

### 早期未解码或运行的材料

早期资料只确认这些文件存在。后续已解码 Scripts.rxdata 的唯一 Main 并逐行检查全部 49 行，没有执行该脚本。两幅标记位图各为 8 × 8、各 64 像素，共 128 像素。音色库已解析 RIFF 与 hydra 结构，含 236 个预设、240 件乐器、505 个样本和 1,524 条链接。Game.exe、x64-msvcrt-ruby310.dll 与 zlib1.dll 已核对 PE 结构、接口或依赖；完整机器码行为和实际分派仍未验证。解析结果也未验证真实画面、声音或原生加载。见[参考材料与宿主的观察范围](observation-limits.md)。

- <a id="src-003"></a><a id="src-326"></a><a id="src-420"></a><a id="src-422"></a><a id="src-424"></a><a id="src-428"></a><a id="src-429"></a><a id="src-431"></a><a id="src-432"></a>限于上述适用范围。

### 本地化候选文本，仅确认身份；翻译全文与运行未验证

- <a id="src-402"></a><a id="src-403"></a><a id="src-404"></a><a id="src-405"></a><a id="src-406"></a><a id="src-407"></a><a id="src-408"></a><a id="src-409"></a><a id="src-410"></a><a id="src-411"></a><a id="src-412"></a><a id="src-413"></a><a id="src-414"></a><a id="src-415"></a><a id="src-416"></a><a id="src-417"></a><a id="src-418"></a><a id="src-419"></a>[本地化](../spec/core/localization.md)

### 作者工具的静态入口；工具执行、转换和往返结果未验证

- <a id="src-421"></a><a id="src-423"></a><a id="src-426"></a><a id="src-427"></a><a id="src-430"></a>[工程转换与制作工具](../spec/authoring/project-conversion-and-authoring-tools.md)
