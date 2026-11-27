# 跨领域的异常、未验证项与案例范围

## 已登记的参考异常

以下 20 项来自参考 R 的静态异常登记，各行按对应功能章节所列输入与版本解释。表内的记录位置和旧数据名称用于识别兼容行为。独立实现采用其他结果时可在自己的模式中另列。

| 编号 | 交界 | 参考结果 | 具体条件 |
| --- | --- | --- | --- |
| AX01 | G3-2 | 背包 add 空间不足返回 false 但此前已写入的槽位保留（部分添加） | [WP27](../spec/creatures/bag-and-item-storage.md) |
| AX02 | G3-2 | 背包游标设置无下界检查（负值可被保存） | [WP27](../spec/creatures/bag-and-item-storage.md) |
| AX03 | G3-1 | 球登记即消耗，之后任何失败（目标丢失/挡球/摇晃不足）不退回 | [WP38](../spec/creatures/capture-and-receiving.md) |
| AX04 | G3-1 | 捕获全满兜底在未定义消息方法处失败；此前已提交的图鉴/昵称/治疗/离场状态不回滚 | [WP38](../spec/creatures/capture-and-receiving.md) |
| AX05 | G3-3 | Factory 战后交换取消不计数但提交仍执行 | [WP57](../spec/battle/factory-rentals-and-swaps.md) |
| AX06 | G3-3 | Factory 候选生成无迭代上限（整体校验不过则无限重试） | [WP57](../spec/battle/factory-rentals-and-swaps.md) |
| AX07 | G4-1 | 临时等级调整中非法等级被 setter 拒绝时，已经写过的前面成员没有本层事务还原 | [WP54](../spec/battle/entry-eligibility-level-adjustment-and-clauses.md) |
| AX08 | G4-2 | 帐篷档（60）在 set 路径不可达（模式计算只产出开放档或普通档） | [WP55](../spec/battle/facility-session-and-restoration.md) |
| AX09 | G4-4 | Shadow S01 重新建立无守卫、非幂等（丢弃旧暂存与旧恢复目标） | [WP23](../spec/creatures/shadow-hyper-and-purification.md) |
| AX10 | G4-5 | 参战标记写入按「侧＋侧内场上位置」、终局读取按「队伍下标」——两端口径不同的真实参考缺陷（GR-013） | [换人](../spec/battle/switching-positioning-and-escape.md)、[终局](../spec/battle/growth-end-of-round-and-battle-outcomes.md)、[回放](../spec/battle/battle-recording-and-playback.md) |
| AX11 | G2-5 | 彩票生成后无参重播种不恢复调用前随机序列（其它普通随机消费者可能受影响） | [WP70](../spec/ui/lottery.md) |
| AX12 | G3-5 | 邮件/持物给予链非全有全无事务：先取邮件再给予时，后续取消/失败不回滚先前信箱入库与成员清空 | [WP64](../spec/creatures/mail-and-mystery-gift.md) |
| AX13 | G8-2 | 训练家战斗新建流程嵌套例外：外层 No 只重载 .dat、不回滚已写 PBS（可带出先前内存编辑） | [WP73-A](../spec/authoring/content-editors.md) |
| AX14 | G8-2 | WP76 写出：先保存 .dat 再截断总 PBS 交错写——后续失败不自动撤销先前数据 | [WP76](../spec/authoring/facility-content-generation-and-simulation.md) |
| AX15 | G1-5 | 遭遇枚举 each_of_version 使用错误形状的键（数组 vs 符号）：正常编译数据下该检查永不命中，同地图已有版本 v 时枚举仍先产出版本 0（同一地图出现两次，不修参考） | [WP36](../spec/world/wild-encounters-and-modifiers.md) |
| AX16 | G6-4 | 卡片出售先加钱并更新显示再删牌（删除返回不检查）；达到金钱上限仍可卖——牌照删、显示报价不代表实际到账差额 | [WP68](../spec/ui/triple-triad.md) |
| AX17 | G2-7 | 默认全局路线图的漫游推进 1/32 额外随机候选从全部 10 个键中取——可能抽中当前图 | [WP37](../spec/world/roaming-and-poke-radar.md) |
| AX18 | G4-9 | 类型相性冲突数据优先克制、再抗性、再免疫——不按免疫优先修复非法重叠数据 | [WP43](../spec/battle/types-accuracy-and-damage.md) |
| AX19 | G4-8 | 形态处理器内交互学习被放弃、或被蛋/Shadow 拒绝时不回滚形态——形态已处于提交链中，招式保持不变 | [WP21](../spec/creatures/dynamic-forms-and-display.md) |
| AX20 | G6-5 | 树果水分允许为负（逐小时干涸不夹零）；惩罚只在水分 ≤0 的小时 +1 | [WP60](../spec/world/berry-plants.md) |

## 基线未验证项

U01–U10 按首次登记的提问范围解释。后续完成的局部静态核对由相应正文给出。U02 的进化参数已单独比较发行版与参考 R；版本等价性仍须逐功能判断。U07 的取消、失败与部分写入须分别查看具体入口。

| 编号 | 最初待验证的范围 | 原材料允许的结论 |
| --- | --- | --- |
| U01 | 完整 demo 的地图/公共事件/资源 | 当前明确缺失；影响事件收费、授予能力、奖励和可达性验证 |
| U02 | 参考快照与基准发行版的行为差异 | 初次取样固定了版本，尚未比对发行版；不能把设置注释当一致性证明 |
| U03 | 世代开关和 PBS 备份的组合边界 | 默认机制为 8，编译不自动遍历备份目录；需分别记录配置和数据集 |
| U04 | 数据存在与完整功能存在的区别 | 有华丽大赛属性，但未建立完整华丽大赛流程证据；关键词搜索未找到 Dynamax/Z-Move/Terastal 或网络对战入口 |
| U05 | 随机数、时间、录像确定性 | 普通随机、地牢种子、战斗录像三类证据共存，未验证跨系统一致性 |
| U06 | Shadow 数据与脚本的启用条件 | 核心脚本与训练家标记存在；可选 PBS 在备份目录 |
| U07 | 取消/失败时的跨域状态一致性 | 捕获、赠送、交易、道具和商店有分散的容量检查；当时未逐分支验证 |
| U08 | RMXP 命令兼容范围 | 事件解释器中部分标准 RPG 命令明确为空操作；不能声称完整 RMXP 行为兼容 |
| U09 | 插件实际组合及外部服务行为 | 无 Plugins 内容；神秘礼物有下载入口但未联网测试 |
| U10 | 战斗效果、AI 判断与版本差异覆盖 | 初次取样仅定位机制族及其主要连接，后续逐入口的条件见[战斗规格](../spec/battle/README.md) |

G01–G12 分别记录 12 条示例候选链的已知数据、缺失材料和受影响结论。完整逐项表见[示例工程的证据与能力](../spec/authoring/demo-evidence-and-capability-coverage.md#9-缺口与影响g01g12)。

## 条件测试的读法

- 地点条 10 例、灯光 5 例、黑暗 6 例、图片 8 例和计时器 5 例合计 34 例（ROOT002）。各例按给定资源、画面和宿主条件核对，未证明实际事件布置或素材全集。见[世界绘制与过渡](../vectors/world-rendering-and-transitions.md)。
- UI 的 NV 和 TP 两个案例族各有 T01–T21，T06b、T25b、T34b 是独立行。用案例族与 ID 一起定位，保留顺序和重复次数。见[菜单、演出与小游戏](../vectors/menus-presentations-and-minigames.md)。
- 早期局部静态材料覆盖 312 条参考路径（291 覆盖、4 补提取、17 具名不适用）、33 个顶层数据文件、84 个内容包认领 113 个功能。此计数只说明该批有限输入。432 个来源导航、35 条作者配置、17 类 UI 场景、54 个交界和 8 条链各有自己的计量和证据范围。
- 名人堂登记、剧本道馆/发奖、寄养收费等示例分别需要真实事件材料。完整 67 种树果组合、未读杯赛名单、备份启用、字体、音频和真实插件均保留各自前提。1024、2048 等容量与缺图时抛错属于具名宿主测试条件。

旧值、回调与温度换算等六种旧输入的可选行为见[旧输入兼容范围](legacy-compatibility-choices.md)。资源与工具的有限参考行为、条件化 AI 评分及测试输入见[条件化兼容资料](conditional-behavior-profiles.md)。资料证据分层见[适用范围与证据等级](scope-and-evidence.md)。
