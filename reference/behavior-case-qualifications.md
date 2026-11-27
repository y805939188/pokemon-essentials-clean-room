# 跨功能案例与适用条件

这些输入、顺序和结果来自固定参考版本的静态行为推导。读取每个样例的前提、预期和反向条件。时间和绘制值表示逻辑请求，像素、声音、机器容量与墙钟耗时需要另行观察。不同样例可使用同一测试 ID，从不同入口检验其前提；每份 JSON 内的顺序只用于查找。字段名和叙述中的旧入口名称用于辨认参考行为，独立实现可自行组织状态和调用。

<a id="content-io"></a>

## 内容与读写

编译输入与异常恢复需要分别检验文件状态和返回值。删除空目录时父目录保留；提取翻译时，覆盖既有译文与递归删除目录是不同入口。

- [PBS 生命周期](../spec/core/pbs-lifecycle.md)
- [诊断、文件与 HTTP](../spec/core/diagnostics-files-http.md)
- [本地化](../spec/core/localization.md)
- [迁移、失败与恢复](../spec/core/migration-failure-recovery.md)
- [文件系统、翻译和存档迁移的输入与预期](../vectors/qualified/content-io.json)

<a id="world-and-events"></a>

## 地图与事件

地图变更、有效目标、方向、地形与解释器状态决定完整结果。事件传送 201 先排队；同图刷新与跨图重建应分开核对。等待参数 1 对应 0.05 秒，完成等待仍需一次更新机会。

- [地图拓扑与转移](../spec/world/map-topology-transfer.md)
- [地形、运动与载具](../spec/world/terrain-movement-vehicles.md)
- [解释器命令兼容矩阵](../spec/world/interpreter-command-matrix.md)
- [随机地牢](../spec/world/random-dungeons.md)
- [边缘跨图、场地技和时间环境](../vectors/qualified/map-movement-and-time.json)

<a id="presentation"></a>

## 资源与呈现

对自动图块的同一张 192×128 输入，2048 容量条件下展开为 64×1536，第一次播放计数为 2；1024 容量条件下折叠为 128×768，第一次播放计数为 4。无额外强制重算时，经过 0.5 秒分别请求帧 0 的 x=0 与帧 2 的 x=128。越界请求的最终像素未验证。空名图像、非空缺图的直接入口、有外部错误处理的动画入口各有其结果。

- [资源匹配、资源访问及声音](../spec/world/resource-matching-and-audio.md)
- [世界绘制与视觉过渡](../spec/world/world-rendering-and-visual-transitions.md)
- [消息、窗口与输入行为规格](../spec/ui/messages-windows-input.md)
- [天气、色调与绘制条件](../vectors/qualified/weather-and-presentation.json)
- [战斗音频、提示、输入与结算顺序](../vectors/qualified/battle-presentation.json)

<a id="creature-identity"></a>

## 个体、队伍与玩家

建议名候选要非空且长度严格小于上限。上限为 10 时，abcdefghi1 移除尾部数字后得到 Abcdefghi；abcdefgh1 可直接得到 Abcdefgh1。仅浏览盒子也可写回已归一的墙纸。伙伴开启雷达的资格与随后遇敌处理清链的条件分开。

- [生物身份、物种记录、来源与拥有者行为规格](../spec/creatures/creature-identity-species-ownership.md)
- [玩家、NPC 训练家与伙伴行为规格](../spec/creatures/player-trainers-partners.md)
- [队伍、盒子与成员移动行为规格](../spec/creatures/party-and-storage.md)
- [背包、物品储存与快捷登记行为规格](../spec/creatures/bag-and-item-storage.md)
- [玩家和步数副作用](../vectors/qualified/player-and-step-effects.json)

<a id="items-and-growth"></a>

## 使用物品与成长

糖果已进入满级进化演出时，正常取消可保留物种与等级、增加取消统计，并在演出正常返回后消费一份。选择物品前取消和演出异常有不同提交边界。

- [主动道具与培养/教学行为规格](../spec/creatures/item-use-and-training.md)
- [买卖与 BP 商店行为规格](../spec/creatures/shops-and-exchanges.md)
- [成长、学习替换与友好行为规格](../spec/creatures/growth-learning-and-friendship.md)
- [基础进化](../spec/creatures/basic-evolution.md)
- [使用、数量、学习、取消与呈现](../vectors/qualified/items-and-presentation.json)
- [成长、感染、步行与物品结果](../vectors/qualified/growth-and-field-effects.json)

<a id="encounters"></a>

## 遭遇与培育

检查当前地图的遭遇快照和注册表、步数回绕与强度改变、伙伴参加条件，以及已存在的漫游个体。给定个体和由物种／等级生成个体可产生不同的生成通知数。

- [寄养会话与兼容性行为规格](../spec/creatures/daycare-and-breeding-session.md)
- [蛋状态与孵化行为规格](../spec/creatures/eggs-and-hatching.md)
- [普通遭遇、触发与修正行为规格](../spec/world/wild-encounters-and-modifiers.md)
- [漫游与 Poké Radar](../spec/world/roaming-and-poke-radar.md)
- [漫游、伙伴与战斗进入](../vectors/qualified/encounter-to-battle.json)
- [表选择、遭遇时机与场地](../vectors/qualified/encounter-and-field-effects.json)

<a id="battle"></a>

## 战斗与奖励

真实参战伙伴与满队替换同时存在时，送盒的 A 保留共享身份。以 A、B 原持 X、Y，其余空为前提，玩家队伍和还原记录发生位移，一次正常终局写回后盒中 A=Y，留队 B=空。仅登记伙伴或无伙伴时，盒中 A 保持 X，B=Y。变更当前持物与永久消耗须分别设定。

- [战斗上下文与参与者行为规格](../spec/battle/battle-context-and-participants.md)
- [命令、特殊行动、服从性与行动顺序行为规格](../spec/battle/commands-obedience-and-action-order.md)
- [换人、替补、场上位置移动与逃跑行为规格](../spec/battle/switching-positioning-and-escape.md)
- [战斗成长交界、回合末与终局行为规格](../spec/battle/growth-end-of-round-and-battle-outcomes.md)
- [捕获判定与接收策略](../spec/creatures/capture-and-receiving.md)
- [命令、服从、经验、捕获、持物与终局](../vectors/qualified/battle-and-rewards.json)
- [行动顺序、拒绝、失败与近邻对照](../vectors/qualified/battle-order-and-failures.json)
- [战斗结果交还地图的跨域案例](../vectors/qualified/battle-and-field-effects.json)

<a id="field"></a>

## 场地、时间与步行

同一时刻可以独立观察地图色调与战斗时段。钓鱼、攀瀑、浇水、蓝黑画面转场与回程各有自己的检查时点。公共入口返回成功时，实际移动、资源写入或完整播放仍依赖后续前提。

- [世界时间、天气与场地能力](../spec/world/world-time-weather-field-moves.md)
- [钓鱼](../spec/world/fishing.md)
- [树果种植](../spec/world/berry-plants.md)
- [野外被动变化与失败回程](../spec/world/field-passive-effects-and-blackout.md)
- [场地时间与配置交叉](../vectors/qualified/world-time-and-state.json)
- [时间边界、转移、回收与反向输入](../vectors/qualified/map-timing-and-recovery.json)

<a id="limits"></a>

## 未验证范围

本组早期静态样本中，8 个杯赛引用清单与 pokemon_metrics.txt 的具体样本、备份和生成目录的完整内容、实际地图事件链、动态分派、插件组合、弃用别名和真实地图的动态阴影可达性仍有未验证范围。二进制、宿主配置、媒体与字体的最终输出、损坏媒体解码和宿主容量不能从静态输入直接推定。较晚的[具名材料观察](observation-limits.md)与[旧世代备份的字段与启用条件](generation-data-compatibility.md)各自说明了实际读过的输入。自动图块 1024/2048 仅为条件输入，缺图异常以宿主确实抛出普通加载错误为前提。

当前行为采用场景中具名条件。配置和编辑器入口、同地图与连接跨图、普通战斗与接管路径、合法与异常输入均需分别核对。每组正反例只确认其明示的状态、顺序及返回边界。
