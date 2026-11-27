# 跨功能规则与失败顺序

同一操作可能跨越两个或更多功能。每一项给出调用前提、写入顺序，以及失败、取消或换入口时的差异。兼容参考行为时按具体入口处理部分写入。以下为静态行为，未执行；真实演示事件链未验证。适用边界沿用 U01–U10、G01–G12 与 AX01–AX20。

<a id="g1-1"></a>
### G1-1 普通 PBS 发现机制

**接口** 只发现顶层小写后缀文本候选；发现、读取、校验与产物消费为不同状态。

**边界** 子目录备份不由普通发现入口自动纳入；被发现文件仍可能编译失败。

**相关规格** [规则配置档案与数据变体](../spec/core/rule-configuration-and-data-variants.md)、[PBS 生命周期](../spec/core/pbs-lifecycle.md)

<a id="g1-2"></a>
### G1-2 候选变体材料（备份目录）

**接口** Gen5–8 四目录各九份文本，在早期清单中仅按身份登记；WP23主文/附表§3/§3.1/§3.2提供字面字段与样本目录，131量表/招式样本全集可查。两类都不构成自动切换/编译/启用合同。

**边界** Shadow样本内容可支持BUTTERFREE量表4000与招式顺序SHADOWRUSH/SHADOWMIST；不能降为仅存在性。Gen5–8 仅给目录的输入不能推导字段值，后来实读的字段见[旧世代备份的字段与启用条件](generation-data-compatibility.md)，Shadow实际启用仍U06未知。

**相关规格** [心量表数据、可选内容与固定向量](../spec/creatures/shadow-data-and-vectors.md) §3、§3.1、§3.2

**静态场景** [SHADOW-CONTENT-P](../vectors/cross-domain-contrasts.md#shadow-content-p)、[SHADOW-ACTIVATION-N](../vectors/cross-domain-contrasts.md#shadow-activation-n)

<a id="g1-3"></a>
### G1-3 设施名单专用显式入口

**接口** 设施名单由显式名单文件字段加载；普通PBS发现与专用名单入口分开。

**边界** 无引用的非single fancy两个文件只登记存在，不假定消费者。

**相关规格** [PBS 生命周期](../spec/core/pbs-lifecycle.md)、[设施内容生成与模拟（挑战生成器——候选构造／合法性筛选／去重／评估与写出）行为规格](../spec/authoring/facility-content-generation-and-simulation.md)、[参赛资格、队伍子集、等级调整与杯赛条款行为规格](../spec/battle/entry-eligibility-level-adjustment-and-clauses.md)、[默认杯赛、条款与资格目录附表](../spec/battle/entry-rules-and-cup-data.md)

<a id="g1-4"></a>
### G1-4 注册表默认契约与按类例外

**接口** 通用身份查询默认与Encounter版本回退、Trainer三元身份和Phone三入口各自例外分列。

**边界** 遭遇缺请求表与缺步进表不同，不能把某类回退泛化到所有注册表。

**相关规格** [内容身份、注册与 schema](../spec/core/content-identity-and-schema.md)、[普通遭遇、触发与修正行为规格](../spec/world/wild-encounters-and-modifiers.md)、[玩家、NPC 训练家与伙伴行为规格](../spec/creatures/player-trainers-partners.md)、[Pokégear、区域地图、点唱机与电话行为规格](../spec/ui/pokegear-map-music-and-phone.md)

<a id="g1-5"></a>
### G1-5 编译消费边界 vs 数据包编译声明

**接口** 未知属性不自动消费；同图/版本组合重复为编译错误。设施生成写出先产物后交错文本，失败保留已写。

**边界** 版本枚举错键仍保留同图重复/无法匹配异常；已登记规则不重新生成；注释示例不是默认规则。

**相关规格** [PBS 生命周期](../spec/core/pbs-lifecycle.md)、[普通遭遇、触发与修正行为规格](../spec/world/wild-encounters-and-modifiers.md)、[设施内容生成与模拟（挑战生成器——候选构造／合法性筛选／去重／评估与写出）行为规格](../spec/authoring/facility-content-generation-and-simulation.md)、[参赛资格、队伍子集、等级调整与杯赛条款行为规格](../spec/battle/entry-eligibility-level-adjustment-and-clauses.md)、[默认杯赛、条款与资格目录附表](../spec/battle/entry-rules-and-cup-data.md)

<a id="g2-1"></a>
### G2-1 计时来源

**接口** 宿主日期钟、累计游戏时间与运行时长分别消费；读档后的离线时间按消费者定义。

**边界** 日期变化不等于帧循环推进；动画相位不得统一重置为场景打开时零。

**相关规格** [统计字段目录](../spec/core/stats-directory.md)、[时间、随机、计步与统计](../spec/core/time-random-steps-stats.md)、[世界时间、天气与场地能力](../spec/world/world-time-weather-field-moves.md)、[钓鱼](../spec/world/fishing.md)、[树果种植](../spec/world/berry-plants.md)、[Pokégear、区域地图、点唱机与电话行为规格](../spec/ui/pokegear-map-music-and-phone.md)、[Lottery](../spec/ui/lottery.md)、[Mining 候选与形状数据附表](../spec/ui/mining-data.md)、[Mining 行为规格](../spec/ui/mining.md)

<a id="g2-2"></a>
### G2-2 离线追赶语义

**接口** 树果按小时追赶生长/耗水/重植；电话按刷新秒去重，期限到零重设20–39分钟且当次仍减一。

**边界** 单株六小时与多株采摘统计不混同；电话菜单暂停和离线重设不同。

**相关规格** [钓鱼](../spec/world/fishing.md)、[树果种植](../spec/world/berry-plants.md)、[Pokégear、区域地图、点唱机与电话行为规格](../spec/ui/pokegear-map-music-and-phone.md)、[统计字段目录](../spec/core/stats-directory.md)、[时间、随机、计步与统计](../spec/core/time-random-steps-stats.md)

<a id="g2-3"></a>
### G2-3 步进入口与计数

**接口** 普通玩家、强制玩家、NPC及主动请求分入口；全局计步31位回绕，寄养256与友好128各有周期。

**边界** 强制玩家一步的通用通知两次不能套给NPC/普通玩家；主动遭遇不等于步进机会检查。

**相关规格** [野外被动变化与失败回程](../spec/world/field-passive-effects-and-blackout.md)、[统计字段目录](../spec/core/stats-directory.md)、[时间、随机、计步与统计](../spec/core/time-random-steps-stats.md)、[寄养会话与兼容性行为规格](../spec/creatures/daycare-and-breeding-session.md)、[蛋状态与孵化行为规格](../spec/creatures/eggs-and-hatching.md)、[普通遭遇、触发与修正行为规格](../spec/world/wild-encounters-and-modifiers.md)

<a id="g2-4"></a>
### G2-4 行走友好度

**接口** 普通步进累计达到或超过128周期→按队伍顺序逐个非空/非蛋/未濒死成员独立1/2抽样（0..1为0命中）→命中才消费成长规则基础2/2/1、正修正/封顶与Shadow阶段门→循环后计数归0。

**边界** 127到128、两名合格成员独立抽样0/1仅第一名变化，1/0仅第二名变化；不采用共同概率门。空/全不合资格仍归0；Shadow阶段≥4即使命中也不增友好。

**相关规格** [野外被动变化与失败回程](../spec/world/field-passive-effects-and-blackout.md) §4.1 （FP03）、[成长、学习替换与友好行为规格](../spec/creatures/growth-learning-and-friendship.md) §8

**静态场景** [FRIEND-P](../vectors/cross-domain-contrasts.md#friend-p)、[FRIEND-N](../vectors/cross-domain-contrasts.md#friend-n)、[FRIEND-SHADOW-N](../vectors/cross-domain-contrasts.md#friend-shadow-n)

<a id="g2-5"></a>
### G2-5 显式种子与有限可重现

**接口** 普通随机、显式播种和记录随机序列分别描述；录像读取按录制顺序。

**边界** 挖矿播种后不恢复调用前序列；未规定跨实现相同随机发生器。

**相关规格** [统计字段目录](../spec/core/stats-directory.md)、[时间、随机、计步与统计](../spec/core/time-random-steps-stats.md)、[随机地牢](../spec/world/random-dungeons.md)、[Lottery](../spec/ui/lottery.md)、[Mining 候选与形状数据附表](../spec/ui/mining-data.md)、[Mining 行为规格](../spec/ui/mining.md)、[战斗记录与回放行为规格](../spec/battle/battle-recording-and-playback.md)

<a id="g2-6"></a>
### G2-6 读档/暂停推进

**接口** 帧消费者须实际得到更新机会；菜单/战斗/消息/强制路线/解释器的电话守卫分别暂停倒计时。

**边界** 宿主日期继续变化不自动推进所有帧驱动业务；捕虫期限独立。

**相关规格** [统计字段目录](../spec/core/stats-directory.md)、[时间、随机、计步与统计](../spec/core/time-random-steps-stats.md)、[Pokégear、区域地图、点唱机与电话行为规格](../spec/ui/pokegear-map-music-and-phone.md)、[Safari 与捕虫大会](../spec/battle/safari-and-bug-catching-contest.md)

<a id="g2-7"></a>
### G2-7 漫游/雷达随机

**接口** 默认漫游十键各九邻接；额外1/32从全十键抽，允许当前图；KYOGRE专属四键邻接另列。

**边界** 雷达草丛闪光、生成个体异色、连锁继续三判断分开，不用全局图替代专属图。

**相关规格** [统计字段目录](../spec/core/stats-directory.md)、[时间、随机、计步与统计](../spec/core/time-random-steps-stats.md)、[漫游与 Poké Radar](../spec/world/roaming-and-poke-radar.md)

<a id="g2-8"></a>
### G2-8 世界天气显示管线

**接口** 世界天气意图、显示粒子/渐变/色调/闪光与战斗天气身份分层；进入通知先要求旧图存在且异图→按元数据/概率求新类型（缺字段/失败为None）→同类型跳过、仅类型改变局部写power9/duration0。合法连接边缘在进入通知后独立写duration20；显式转移重建无此连接后写。

**边界** Rain/duration7异图又得Rain：显式重建保留7，合法连接才后写20；同图/旧图0不重掷。类型变更无连接局部0，有连接最终20；正在渐变守卫不打断，类型同仅强度改不刷新。20是名义单位、正值只选择固定渐变，不是20秒；TIME_SHADING/户外门不扩到outdoorlight。

**相关规格** [世界时间、天气与场地能力](../spec/world/world-time-weather-field-moves.md) §4.3、§4.5 （WT07）、[地图拓扑与转移](../spec/world/map-topology-transfer.md) §5

**静态场景** [WEATHER-SAME-P](../vectors/cross-domain-contrasts.md#weather-same-p)、[WEATHER-TYPE-P](../vectors/cross-domain-contrasts.md#weather-type-p)、[WEATHER-GATES-N](../vectors/cross-domain-contrasts.md#weather-gates-n)

<a id="g3-1"></a>
### G3-1 捕获唯一主规格

**接口** 投球登记扣减先于动作；捕获成功更新图鉴/拥有/接收；满队选择替换和送盒分别处理。

**边界** 登记后失败不退球；全满兜底在消息缺陷处失败，不保证撤销已提交字段。

**相关规格** [捕获判定与接收策略](../spec/creatures/capture-and-receiving.md)、[队伍、盒子与成员移动行为规格](../spec/creatures/party-and-storage.md)、[图鉴记录、区域与内容规则](../spec/creatures/pokedex-records-regions-and-content.md)、[背包、物品储存与快捷登记行为规格](../spec/creatures/bag-and-item-storage.md)、[HP、异常状态、已知招式与持有状态行为规格](../spec/creatures/hp-status-moves-helditem.md)

<a id="g3-2"></a>
### G3-2 容量与部分写入

**接口** 容量预检与实际添加分开；背包有限槽部分添加保留，生物队伍/盒子各自检查。

**边界** 预检成功不使后段成为事务；盒子游标无下界检查的实际异常保留。

**相关规格** [队伍、盒子与成员移动行为规格](../spec/creatures/party-and-storage.md)、[背包、物品储存与快捷登记行为规格](../spec/creatures/bag-and-item-storage.md)、[获得、赠送与脚本交换行为规格](../spec/creatures/acquisition-gifts-and-script-trade.md)、[捕获判定与接收策略](../spec/creatures/capture-and-receiving.md)

<a id="g3-3"></a>
### G3-3 租借个体所有权

**接口** 租借创建默认拥有者记录为有效编号0/空名/性别2/语言2；交换计数仅确认加一。

**边界** 取消不加计数但提交仍可能执行；生成无迭代上限不改成必然成功。

**相关规格** [Factory 租借与换队行为规格](../spec/battle/factory-rentals-and-swaps.md)、[设施基础会话行为规格](../spec/battle/facility-session-and-restoration.md)、[参赛资格、队伍子集、等级调整与杯赛条款行为规格](../spec/battle/entry-eligibility-level-adjustment-and-clauses.md)、[默认杯赛、条款与资格目录附表](../spec/battle/entry-rules-and-cup-data.md)、[队伍、盒子与成员移动行为规格](../spec/creatures/party-and-storage.md)

<a id="g3-4"></a>
### G3-4 图鉴写入门与公开清理

**接口** 战斗侧仅捕获写拥有，获得侧九入口分别写；静默入队可只写拥有。整体清理清记录后刷新，保留区域解锁。

**边界** 击倒不写拥有；最近见到覆盖与禁止刷新参数是独立入口。

**相关规格** [图鉴记录、区域与内容规则](../spec/creatures/pokedex-records-regions-and-content.md)、[捕获判定与接收策略](../spec/creatures/capture-and-receiving.md)、[蛋状态与孵化行为规格](../spec/creatures/eggs-and-hatching.md)、[获得、赠送与脚本交换行为规格](../spec/creatures/acquisition-gifts-and-script-trade.md)、[Factory 租借与换队行为规格](../spec/battle/factory-rentals-and-swaps.md)

<a id="g3-5"></a>
### G3-5 给予链部分提交

**接口** 持物/邮件给予先完成对应容量检查及已提交入库/清空，再进入后续选择。

**边界** 后续取消/失败不回滚先前邮件入库和清空；交换取消保持各自先写的实际结果。

**相关规格** [邮件与神秘礼物行为规格](../spec/creatures/mail-and-mystery-gift.md)、[队伍与摘要界面（查看／选择／成员操作与真实写入）行为规格](../spec/ui/party-and-summary-ui.md)、[生物盒子与图鉴界面（整理、检索与收集信息浏览）行为规格](../spec/ui/storage-and-pokedex-ui.md)、[背包、物品储存与商店界面（数量／目标选择与交易反馈）行为规格](../spec/ui/bag-item-storage-and-shop-ui.md)、[背包、物品储存与快捷登记行为规格](../spec/creatures/bag-and-item-storage.md)、[队伍、盒子与成员移动行为规格](../spec/creatures/party-and-storage.md)

<a id="g3-6"></a>
### G3-6 拥有者/外来判定结构

**接口** 拥有者编号/名称/性别/语言与玩家ID、宿主语言和界面语言各有角色；获得入口写属主。

**边界** 默认拥有者不是不存在；外来资格不能仅由对象包装结构推断。

**相关规格** [生物身份、物种记录、来源与拥有者行为规格](../spec/creatures/creature-identity-species-ownership.md)、[玩家、NPC 训练家与伙伴行为规格](../spec/creatures/player-trainers-partners.md)、[获得、赠送与脚本交换行为规格](../spec/creatures/acquisition-gifts-and-script-trade.md)、[捕获判定与接收策略](../spec/creatures/capture-and-receiving.md)、[Factory 租借与换队行为规格](../spec/battle/factory-rentals-and-swaps.md)

<a id="g4-1"></a>
### G4-1 临时等级与还原

**接口** 调整前保存两侧完整经验，调整后存物品；正常恢复按届时位置索引，等级相同保留级内经验。

**边界** 重排/替换不自动按原身份复原；非法等级已写成员后失败无本层整体回滚。

**相关规格** [参赛资格、队伍子集、等级调整与杯赛条款行为规格](../spec/battle/entry-eligibility-level-adjustment-and-clauses.md)、[默认杯赛、条款与资格目录附表](../spec/battle/entry-rules-and-cup-data.md)、[设施基础会话行为规格](../spec/battle/facility-session-and-restoration.md)、[Palace 与 Arena 变体行为规格](../spec/battle/palace-and-arena-variants.md)

<a id="g4-2"></a>
### G4-2 会话状态机与队伍引用

**接口** 原队伍快照字段仅开始时按引用写入；玩家队伍引用四入口为进行中报名/租借提交、开始有报名引用（含空列表）时替换、取消存在快照时恢复、结束无条件写原字段后才判断进行中。暂停保留进行中；开始/暂停/继续决定0仍保存，结束仅进行中且决定非0保存。

**边界** 进行中显式空列表同时写报名/玩家队伍并返回假；nil取消不提交且不覆盖旧报名。取消恢复后重置但不保存/不刷图；结束无条件恢复（字段空则玩家队伍空），非进行中到此返回，进行中才重置/刷图，决定0不保存。正常UI空列表可达未证。

**相关规格** [设施基础会话行为规格](../spec/battle/facility-session-and-restoration.md) §2.2、§2.3、§2.4

**静态场景** [FACILITY-INPROGRESS-P](../vectors/cross-domain-contrasts.md#facility-inprogress-p)、[FACILITY-START-P](../vectors/cross-domain-contrasts.md#facility-start-p)、[FACILITY-CANCEL-N](../vectors/cross-domain-contrasts.md#facility-cancel-n)、[FACILITY-END-P](../vectors/cross-domain-contrasts.md#facility-end-p)

<a id="g4-3"></a>
### G4-3 Mega/Primal 分入口还原

**接口** 普通换下及裸战斗正常终局不统一解除；濒死、捕获及世界返回/设施包装分别按其序列解除。

**边界** 世界返回玩家/伙伴全队与裸回放不同；设施正常恢复治疗不等于HP/PP快照恢复。

**相关规格** [Mega、Primal 与显式还原](../spec/creatures/mega-and-primal-reversion.md)、[默认特殊形态资格数据](../spec/creatures/transformation-data.md)、[命令、特殊行动、服从性与行动顺序行为规格](../spec/battle/commands-obedience-and-action-order.md)、[换人、替补、场上位置移动与逃跑行为规格](../spec/battle/switching-positioning-and-escape.md)、[捕获判定与接收策略](../spec/creatures/capture-and-receiving.md)、[战斗成长交界、回合末与终局行为规格](../spec/battle/growth-end-of-round-and-battle-outcomes.md)、[参赛资格、队伍子集、等级调整与杯赛条款行为规格](../spec/battle/entry-eligibility-level-adjustment-and-clauses.md)、[默认杯赛、条款与资格目录附表](../spec/battle/entry-rules-and-cup-data.md)、[设施基础会话行为规格](../spec/battle/facility-session-and-restoration.md)、[战斗记录与回放行为规格](../spec/battle/battle-recording-and-playback.md)

<a id="g4-4"></a>
### G4-4 Shadow 状态

**接口** Shadow标志、量表、Hyper和暂存状态独立；量表0仍Shadow，HP到0清Hyper，净化按入口恢复。

**边界** 再次建立Shadow不是幂等；可选Shadow备份启用仍U06，不能变成默认行为。

**相关规格** [心量表数据、可选内容与固定向量](../spec/creatures/shadow-data-and-vectors.md)、[Shadow、Hyper、成长暂存与净化生命周期](../spec/creatures/shadow-hyper-and-purification.md)、[捕获判定与接收策略](../spec/creatures/capture-and-receiving.md)、[野外被动变化与失败回程](../spec/world/field-passive-effects-and-blackout.md)、[图鉴记录、区域与内容规则](../spec/creatures/pokedex-records-regions-and-content.md)

<a id="g4-5"></a>
### G4-5 参战标记下标口径（真实参考缺陷）

**接口** 参战写入按侧内位置、终局读按队伍下标，实际口径不一致保留。

**边界** BURMY回放变更须参战标志实际真；正确身份重排推断不能修掉来源异常。

**相关规格** [换人、替补、场上位置移动与逃跑行为规格](../spec/battle/switching-positioning-and-escape.md)、[战斗成长交界、回合末与终局行为规格](../spec/battle/growth-end-of-round-and-battle-outcomes.md)、[战斗记录与回放行为规格](../spec/battle/battle-recording-and-playback.md)

<a id="g4-6"></a>
### G4-6 参战者初始化与持久字段

**接口** 战斗临时值与生物持久值隔离；初始化、换下、濒死、捕获的指定写回分别定义。

**边界** 两组规则键集合不同；空对手拒绝仍存在，但不要求源类、固定槽或容器结构。

**相关规格** [战斗上下文与参与者行为规格](../spec/battle/battle-context-and-participants.md)、[HP、异常状态、已知招式与持有状态行为规格](../spec/creatures/hp-status-moves-helditem.md)、[命令、特殊行动、服从性与行动顺序行为规格](../spec/battle/commands-obedience-and-action-order.md)、[换人、替补、场上位置移动与逃跑行为规格](../spec/battle/switching-positioning-and-escape.md)、[战斗成长交界、回合末与终局行为规格](../spec/battle/growth-end-of-round-and-battle-outcomes.md)

<a id="g4-7"></a>
### G4-7 异常/阶级的持久与临时层

**接口** 持久异常与混乱/着迷/畏缩/瞌睡/剧毒累计等临时状态各有期限；七阶级归战斗层。

**边界** 查询、施加、治愈与写回不互换；失败后持久值变化按具体入口。

**相关规格** [有界效果归属与数据对应](../spec/battle/status-effects-coverage.md)、[异常状态、能力阶级与免疫](../spec/battle/statuses-stat-stages-and-immunities.md)、[HP、异常状态、已知招式与持有状态行为规格](../spec/creatures/hp-status-moves-helditem.md)、[战斗成长交界、回合末与终局行为规格](../spec/battle/growth-end-of-round-and-battle-outcomes.md)、[战斗天气、场地、阵营与位置效果行为规格](../spec/battle/weather-terrain-side-and-position-effects.md)

<a id="g4-8"></a>
### G4-8 形态提交副作用链

**接口** 正常形态提交写形态→清缓存→处理器→重算→有玩家登记；带提示入口在写入后让出；简单写入省略处理器/缓存/登记。

**边界** 学习放弃/蛋或Shadow拒绝不回滚形态；同形态ROTOM已有唯一目标招仍可能删到0；战斗专招PP按新总PP夹限。

**相关规格** [动态形态与展示属性](../spec/creatures/dynamic-forms-and-display.md)、[生物身份、物种记录、来源与拥有者行为规格](../spec/creatures/creature-identity-species-ownership.md)、[属性派生、特性选择与六项能力](../spec/creatures/attributes-ability-and-stats.md)、[图鉴记录、区域与内容规则](../spec/creatures/pokedex-records-regions-and-content.md)、[HP、异常状态、已知招式与持有状态行为规格](../spec/creatures/hp-status-moves-helditem.md)、[成长、学习替换与友好行为规格](../spec/creatures/growth-learning-and-friendship.md)

<a id="g4-9"></a>
### G4-9 伤害核心数值输入与效果族修正管道

**接口** 当前能力/速度/重量含已审修正；伤害P/A/D/F分别在指定节点取整，能力→使用方物品→目标物品→后置顺序。

**边界** 非法相性重叠优先克制再抗性再免疫；CHOICESCARF倍率与讲究选择锁不同，未知处理器不是倍率1。

**相关规格** [战斗类型、命中与伤害计算](../spec/battle/types-accuracy-and-damage.md)、[属性派生、特性选择与六项能力](../spec/creatures/attributes-ability-and-stats.md)、[多次攻击、特殊伤害与恢复——有界效果覆盖](../spec/battle/damage-healing-coverage.md)、[多次攻击、特殊伤害与恢复](../spec/battle/damage-multihit-and-healing.md)、[特性参与计算、免疫与有效性](../spec/battle/ability-calculation-modifiers.md)、[持物效果有界覆盖](../spec/battle/held-item-effect-coverage.md)、[持有物计算、触发与消耗](../spec/battle/held-item-triggers-and-consumption.md)、[命令、特殊行动、服从性与行动顺序行为规格](../spec/battle/commands-obedience-and-action-order.md)

<a id="g5-1"></a>
### G5-1 战斗成长调用与门

**接口** 非内部战斗或经验关闭先退出；对手须有参战记录且濒死/临时捕获。玩家本人可战队伍先EV后经验，最后清对手记录。

**边界** 伙伴计入继续战斗资格但不进普通经验接收循环；早退不清参与记录。

**相关规格** [战斗成长交界、回合末与终局行为规格](../spec/battle/growth-end-of-round-and-battle-outcomes.md)、[成长、学习替换与友好行为规格](../spec/creatures/growth-learning-and-friendship.md)、[属性派生、特性选择与六项能力](../spec/creatures/attributes-ability-and-stats.md)、[有界效果归属与数据对应](../spec/battle/status-effects-coverage.md)、[异常状态、能力阶级与免疫](../spec/battle/statuses-stat-stages-and-immunities.md)、[战斗天气、场地、阵营与位置效果行为规格](../spec/battle/weather-terrain-side-and-position-effects.md)

<a id="g5-2"></a>
### G5-2 战后进化时序

**接口** 战后T1–T7及L0/K/D临时记录分别定义；扫描一次，不对新结果连锁重查。

**边界** 取消不留下成功记录；NINCADA附加个体不继承该记录。

**相关规格** [情境输入、默认数据与前后状态](../spec/creatures/context-inputs-and-scenarios.md)、[情境、交换、战后成就与事件进化](../spec/creatures/contextual-trade-and-post-battle-evolution.md)、[战斗成长交界、回合末与终局行为规格](../spec/battle/growth-end-of-round-and-battle-outcomes.md)、[基础进化](../spec/creatures/basic-evolution.md)、[战斗交互与呈现行为规格](../spec/ui/battle-interaction-and-presentation.md)、[生命周期演出与历程展示行为规格](../spec/ui/lifecycle-presentations-and-history.md)

<a id="g5-3"></a>
### G5-3 进化提交主流程

**接口** 阻止、取消、成功三路；成功按统计及身份/能力/图鉴/招式/收尾固定序列交接呈现。

**边界** 呈现失败不自动把先前提交改成事务；兼容物种/道具身份不能净化成泛称。

**相关规格** [基础进化](../spec/creatures/basic-evolution.md)、[主动道具与培养/教学行为规格](../spec/creatures/item-use-and-training.md)、[情境输入、默认数据与前后状态](../spec/creatures/context-inputs-and-scenarios.md)、[情境、交换、战后成就与事件进化](../spec/creatures/contextual-trade-and-post-battle-evolution.md)、[战斗交互与呈现行为规格](../spec/ui/battle-interaction-and-presentation.md)、[生命周期演出与历程展示行为规格](../spec/ui/lifecycle-presentations-and-history.md)、[图鉴记录、区域与内容规则](../spec/creatures/pokedex-records-regions-and-content.md)

<a id="g5-4"></a>
### G5-4 孵化提交

**接口** 队伍孵化先核心写入后演出；图鉴写入及动态形态读取各有门，多蛋按队伍顺序。

**边界** 演出动态形态读取可有提交副作用；未执行演出不意味着核心孵化未发生。

**相关规格** [蛋状态与孵化行为规格](../spec/creatures/eggs-and-hatching.md)、[遗传与后代生成](../spec/creatures/inheritance-and-offspring.md)、[寄养会话与兼容性行为规格](../spec/creatures/daycare-and-breeding-session.md)、[图鉴记录、区域与内容规则](../spec/creatures/pokedex-records-regions-and-content.md)、[战斗交互与呈现行为规格](../spec/ui/battle-interaction-and-presentation.md)、[生命周期演出与历程展示行为规格](../spec/ui/lifecycle-presentations-and-history.md)

<a id="g5-5"></a>
### G5-5 寄养蛋三具名入口

**接口** 寄养周期只置已有蛋标记；领取守卫只槽数2，生成及随机/感染副作用先于队伍容量，再入队与复位。

**边界** 满队失败保留生成副作用和旧标记，重试重新生成；不把生成移到周期，也不证明接待事件守卫。

**相关规格** [寄养会话与兼容性行为规格](../spec/creatures/daycare-and-breeding-session.md)、[遗传与后代生成](../spec/creatures/inheritance-and-offspring.md)、[蛋状态与孵化行为规格](../spec/creatures/eggs-and-hatching.md)、[队伍、盒子与成员移动行为规格](../spec/creatures/party-and-storage.md)

<a id="g5-6"></a>
### G5-6 继承通道的随机与顺序

**接口** 领取生成时执行IV三/五项及力量道具通道、去重/互斥/顺序，异色重掷按实际返回门。

**边界** 派生域归属性规格；不要求源数组/类；周期标记不是遗传结果实体。

**相关规格** [遗传与后代生成](../spec/creatures/inheritance-and-offspring.md)、[属性派生、特性选择与六项能力](../spec/creatures/attributes-ability-and-stats.md)、[寄养会话与兼容性行为规格](../spec/creatures/daycare-and-breeding-session.md)

<a id="g6-1"></a>
### G6-1 资源域与交易层

**接口** 资源写入按金钱/BP/硬币各自夹限，商店资格、支付和赠品由交易入口定义。

**边界** BP商店不套普通赠品；有限2槽P999/997买3失败回退总量可保留997/999槽分布。

**相关规格** [玩家、NPC 训练家与伙伴行为规格](../spec/creatures/player-trainers-partners.md)、[买卖与 BP 商店行为规格](../spec/creatures/shops-and-exchanges.md)、[背包、物品储存与快捷登记行为规格](../spec/creatures/bag-and-item-storage.md)

<a id="g6-2"></a>
### G6-2 扣除与不退

**接口** 消耗登记/资格/效果/返回分层；道具使用过一件后再取消目标可返回0而保留效果与扣减。

**边界** 不能由返回0推成未使用；投球登记即扣减，与普通道具消费门不同。

**相关规格** [捕获判定与接收策略](../spec/creatures/capture-and-receiving.md)、[主动道具与培养/教学行为规格](../spec/creatures/item-use-and-training.md)、[背包、物品储存与快捷登记行为规格](../spec/creatures/bag-and-item-storage.md)、[队伍与摘要界面（查看／选择／成员操作与真实写入）行为规格](../spec/ui/party-and-summary-ui.md)、[生物盒子与图鉴界面（整理、检索与收集信息浏览）行为规格](../spec/ui/storage-and-pokedex-ui.md)、[背包、物品储存与商店界面（数量／目标选择与交易反馈）行为规格](../spec/ui/bag-item-storage-and-shop-ui.md)

<a id="g6-3"></a>
### G6-3 持物消费与还原

**接口** 持物身份、有效性、触发记录、消费和正常恢复分别记账；普通恢复遍历届时留队列表。

**边界** 伙伴普通2v1/满队有盒位/receive正常主夹具：送盒A获得Y、留队B空；仅一次终局恢复，不再给移位玩家额外遍历。

**相关规格** [持物效果有界覆盖](../spec/battle/held-item-effect-coverage.md)、[持有物计算、触发与消耗](../spec/battle/held-item-triggers-and-consumption.md)、[战斗成长交界、回合末与终局行为规格](../spec/battle/growth-end-of-round-and-battle-outcomes.md)、[参赛资格、队伍子集、等级调整与杯赛条款行为规格](../spec/battle/entry-eligibility-level-adjustment-and-clauses.md)、[默认杯赛、条款与资格目录附表](../spec/battle/entry-rules-and-cup-data.md)、[捕获判定与接收策略](../spec/creatures/capture-and-receiving.md)、[玩家、NPC 训练家与伙伴行为规格](../spec/creatures/player-trainers-partners.md)

<a id="g6-4"></a>
### G6-4 小游戏支付/结算与代币

**接口** 卡片买先余额/容量/添加后扣款，卖先加钱后删卡；老虎机场景信用额到结算写回；挖矿逐件入包；拼图返回布尔。

**边界** 加钱夹满仍删卡；挖矿工具不扣背包；拼图奖励属于缺失外部事件，不能推有奖励。

**相关规格** [Triple Triad 行为规格](../spec/ui/triple-triad.md)、[Duel 行为规格](../spec/ui/duel.md)、[Voltorb Flip](../spec/ui/voltorb-flip.md)、[Voltorb Flip 级别候选数据](../spec/ui/voltorb-layouts.md)、[Slot Machine 行为规格](../spec/ui/slot-machine.md)、[Slot Machine 有序转轮数据附表](../spec/ui/slot-reels.md)、[Lottery](../spec/ui/lottery.md)、[Mining 候选与形状数据附表](../spec/ui/mining-data.md)、[Mining 行为规格](../spec/ui/mining.md)、[Tile Puzzles（板块拼图小游戏）行为规格](../spec/ui/tile-puzzles.md)、[玩家、NPC 训练家与伙伴行为规格](../spec/creatures/player-trainers-partners.md)、[背包、物品储存与快捷登记行为规格](../spec/creatures/bag-and-item-storage.md)、[统计字段目录](../spec/core/stats-directory.md)、[时间、随机、计步与统计](../spec/core/time-random-steps-stats.md)

<a id="g6-5"></a>
### G6-5 树果产量与背包容积

**接口** 树果水分可负；干小时惩罚累计，潮湿覆盖折半向下；采摘确认且可入包后更新单株产量计数。

**边界** 单株qty8/10/12对应计数2/3/3，取消/容量不足不加；不保存最大产量值。

**相关规格** [钓鱼](../spec/world/fishing.md)、[树果种植](../spec/world/berry-plants.md)、[背包、物品储存与快捷登记行为规格](../spec/creatures/bag-and-item-storage.md)、[统计字段目录](../spec/core/stats-directory.md)、[时间、随机、计步与统计](../spec/core/time-random-steps-stats.md)

<a id="g7-1"></a>
### G7-1 交互入口及其调用者

**接口** 消息/选项/数量/按键由主规格定义，集合内4及外5消费者分别引用；取消负值/零/正数各有含义。

**边界** 空数组与nil不同；取消不能统一为false，暂停符与本地化占位符不同。

**相关规格** [附表：绘制文本标记目录](../spec/ui/draw-text-tags.md)、[消息、窗口与输入行为规格](../spec/ui/messages-windows-input.md)、[队伍与摘要界面（查看／选择／成员操作与真实写入）行为规格](../spec/ui/party-and-summary-ui.md)、[生物盒子与图鉴界面（整理、检索与收集信息浏览）行为规格](../spec/ui/storage-and-pokedex-ui.md)、[背包、物品储存与商店界面（数量／目标选择与交易反馈）行为规格](../spec/ui/bag-item-storage-and-shop-ui.md)、[附：控制帮助（Controls help）四页场景合同](../spec/ui/controls-help-appendix.md)、[标题、载入、选项、暂停与 PC（主导航）行为规格](../spec/ui/title-load-options-pause-and-pc.md)、[附：训练家卡（Trainer Card）场景合同](../spec/ui/trainer-card-appendix.md)、[解释器命令兼容矩阵](../spec/world/interpreter-command-matrix.md)、[地图事件、NPC 与跟随](../spec/world/map-events-npc-followers.md)、[移动路线命令矩阵](../spec/world/move-route-matrix.md)、[主动道具与培养/教学行为规格](../spec/creatures/item-use-and-training.md)、[买卖与 BP 商店行为规格](../spec/creatures/shops-and-exchanges.md)、[Safari 与捕虫大会](../spec/battle/safari-and-bug-catching-contest.md)、[战斗交互与呈现行为规格](../spec/ui/battle-interaction-and-presentation.md)、[生命周期演出与历程展示行为规格](../spec/ui/lifecycle-presentations-and-history.md)

<a id="g7-2"></a>
### G7-2 主导航状态分层

**接口** 界面即时修改、游戏状态和持久写盘分开；可见候选排序后逐项评估，保存/退出分别处理。

**边界** 退出前保存被拒仍可终止；子画面返回父级与回地图不混同，选项取消不恢复即时值。

**相关规格** [附：控制帮助（Controls help）四页场景合同](../spec/ui/controls-help-appendix.md)、[标题、载入、选项、暂停与 PC（主导航）行为规格](../spec/ui/title-load-options-pause-and-pc.md)、[附：训练家卡（Trainer Card）场景合同](../spec/ui/trainer-card-appendix.md)、[队伍与摘要界面（查看／选择／成员操作与真实写入）行为规格](../spec/ui/party-and-summary-ui.md)、[生物盒子与图鉴界面（整理、检索与收集信息浏览）行为规格](../spec/ui/storage-and-pokedex-ui.md)、[背包、物品储存与商店界面（数量／目标选择与交易反馈）行为规格](../spec/ui/bag-item-storage-and-shop-ui.md)、[战斗交互与呈现行为规格](../spec/ui/battle-interaction-and-presentation.md)、[生命周期演出与历程展示行为规格](../spec/ui/lifecycle-presentations-and-history.md)

<a id="g7-3"></a>
### G7-3 领域守卫与 UI 消费

**接口** PC整队入口门与界面逐目标门分别检验，容量预检先于实际提交。

**边界** BoxLink缩队后旧索引可部分写入再失败；空重学初绘可失败，不能统一为正常空提示。

**相关规格** [队伍、盒子与成员移动行为规格](../spec/creatures/party-and-storage.md)、[队伍与摘要界面（查看／选择／成员操作与真实写入）行为规格](../spec/ui/party-and-summary-ui.md)、[生物盒子与图鉴界面（整理、检索与收集信息浏览）行为规格](../spec/ui/storage-and-pokedex-ui.md)、[背包、物品储存与商店界面（数量／目标选择与交易反馈）行为规格](../spec/ui/bag-item-storage-and-shop-ui.md)、[主动道具与培养/教学行为规格](../spec/creatures/item-use-and-training.md)

<a id="g7-4"></a>
### G7-4 错误阶段与失败分层

**接口** 下载、文件、编辑器校验、资源选择、编译、插件及转换按入口各自定义异常阶段。

**边界** 阶段1失败阻止阶段2，但不撤销已写文件；没有执行下载/编译/转换或宿主异常画面。 整个路线脚本求值异常先于任何行首判定/索引推进；其它行有前缀不抵消异常。

**相关规格** [弃用告警机制](../spec/core/deprecation-appendix.md)、[诊断、文件与 HTTP](../spec/core/diagnostics-files-http.md)、[邮件与神秘礼物行为规格](../spec/creatures/mail-and-mystery-gift.md)、[内容编辑器（物种/道具/训练家/元数据/图鉴列表）行为规格](../spec/authoring/content-editors.md)、[世界编辑器（地图连接/地图元数据/地形标签/遭遇/指标）行为规格](../spec/authoring/world-editors.md)、[project-conversion-and-authoring-tools](../spec/authoring/project-conversion-and-authoring-tools.md) §8.6、[PBS 生命周期](../spec/core/pbs-lifecycle.md)、[通知、扩展与插件](../spec/core/events-extensions-plugins.md)、[资源匹配、资源访问及声音](../spec/world/resource-matching-and-audio.md)

**静态场景** MR18–MR22（移动路线矩阵与转换文本）

<a id="g7-5"></a>
### G7-5 战斗命令 UI 与选择期合法性

**接口** 命令导航/选择/登记/撤销和执行资格分层；登记消耗物品的扣减时点保留。

**边界** NearAlly正常三席：user0/near2濒死无reserve/far4存活可初选登记4，但布局/存活不变到执行拒绝4；无非自身同侧存活才回自身。

**相关规格** [命令、特殊行动、服从性与行动顺序行为规格](../spec/battle/commands-obedience-and-action-order.md)、[战斗交互与呈现行为规格](../spec/ui/battle-interaction-and-presentation.md)、[生命周期演出与历程展示行为规格](../spec/ui/lifecycle-presentations-and-history.md)、[战斗上下文与参与者行为规格](../spec/battle/battle-context-and-participants.md)

<a id="g8-1"></a>
### G8-1 插件注册、扩展入口及调用条件

**接口** 插件早于编译检查；编译检查调试门不阻止发布消费预编译插件。候选物种通知与生成完成通知分开。

**边界** 普通步进候选通知早于允许遭遇门；主动请求通知后仍可空候选退出。WP21自身形态登记不当作WP05事件消费；真实插件组合仍未知。

**相关规格** [通知、扩展与插件](../spec/core/events-extensions-plugins.md)、[PBS 生命周期](../spec/core/pbs-lifecycle.md)、[野外被动变化与失败回程](../spec/world/field-passive-effects-and-blackout.md)、[普通遭遇、触发与修正行为规格](../spec/world/wild-encounters-and-modifiers.md)、[统计字段目录](../spec/core/stats-directory.md)、[时间、随机、计步与统计](../spec/core/time-random-steps-stats.md)、[附：控制帮助（Controls help）四页场景合同](../spec/ui/controls-help-appendix.md)、[标题、载入、选项、暂停与 PC（主导航）行为规格](../spec/ui/title-load-options-pause-and-pc.md)、[附：训练家卡（Trainer Card）场景合同](../spec/ui/trainer-card-appendix.md)、[调试情境与控制行为规格](../spec/authoring/debug-contexts-and-controls.md)、[动态形态与展示属性](../spec/creatures/dynamic-forms-and-display.md)

<a id="g8-2"></a>
### G8-2 编译/反写/编辑器/生成器时序（按具名入口，非自动链）

**接口** 编辑登记、archive、文本、编译产物和当前地图快照分层；同版本早退保留；生成写出后不自动编译。 转换文本消费边界：整个求值正常后检任一行的三个准确前缀；命中推进并结束帧，无命中推进同帧继续。

**边界** 0率archive→文本省略→重编译Land默认21；父No不把复数Evolutions数值转文本，真正单数写出转换另列；break局部失败不借return推理。

**相关规格** [PBS 生命周期](../spec/core/pbs-lifecycle.md)、[内容编辑器（物种/道具/训练家/元数据/图鉴列表）行为规格](../spec/authoring/content-editors.md)、[世界编辑器（地图连接/地图元数据/地形标签/遭遇/指标）行为规格](../spec/authoring/world-editors.md)、[project-conversion-and-authoring-tools](../spec/authoring/project-conversion-and-authoring-tools.md) §8.6、[设施内容生成与模拟（挑战生成器——候选构造／合法性筛选／去重／评估与写出）行为规格](../spec/authoring/facility-content-generation-and-simulation.md)、[普通遭遇、触发与修正行为规格](../spec/world/wild-encounters-and-modifiers.md)

**静态场景** MR18–MR22（移动路线矩阵与转换文本）

<a id="g8-3"></a>
### G8-3 作者入口 vs 玩家事件入口

**接口** 作者调试/工具/浏览器入口与玩家事件入口分别登记；静态可达工具不是真实玩家演示。

**边界** 地图/公共事件材料缺失，已证事件链0；工具运行、素材和插件组合仍未知。

**相关规格** [调试情境与控制行为规格](../spec/authoring/debug-contexts-and-controls.md)、[内容编辑器（物种/道具/训练家/元数据/图鉴列表）行为规格](../spec/authoring/content-editors.md)、[世界编辑器（地图连接/地图元数据/地形标签/遭遇/指标）行为规格](../spec/authoring/world-editors.md)、[战斗动画制作与交换（动画编辑器／组织器／单项与批量导入导出）行为规格](../spec/authoring/battle-animation-authoring-and-exchange.md)、[project-conversion-and-authoring-tools](../spec/authoring/project-conversion-and-authoring-tools.md) §8.6、[设施内容生成与模拟（挑战生成器——候选构造／合法性筛选／去重／评估与写出）行为规格](../spec/authoring/facility-content-generation-and-simulation.md)、[示例工程证据与能力覆盖](../spec/authoring/demo-evidence-and-capability-coverage.md)

**静态场景** MR18–MR22（移动路线矩阵与转换文本）

<a id="g8-4"></a>
### G8-4 调试直接写入 vs 领域所有权

**接口** 调试直接写入按非默认入口描述；原状态、即时刷新请求与持久保存的先后保留。

**边界** 表达式语法失败可能发生在翻槽后/刷新前；不把调试行为当普通领域守卫或推宿主最终收口。

**相关规格** [调试情境与控制行为规格](../spec/authoring/debug-contexts-and-controls.md)、[野外被动变化与失败回程](../spec/world/field-passive-effects-and-blackout.md)、[保存、启动、新游戏与继续](../spec/core/save-startup-continue.md)

<a id="g9-1"></a>
### G9-1 材料定位、样本与运行证据

**接口** 材料定位、内容样本、静态推导、事件链和运行观察可以指向同一功能。每项结论依赖各自检查过的输入。

**边界** 只定位文件不支持配置值，静态合同不是运行确认；待验证可与已确认局部事实并存。

**相关规格** [示例工程证据与能力覆盖](../spec/authoring/demo-evidence-and-capability-coverage.md)

<a id="g9-2"></a>
### G9-2 WP77 引用合同 vs WP11–17/WP36/WP61/WP63/WP64 当前声明

**接口** Demo配置引用当前主合同；Home是失败回程而非系统起始点；开关51/52读取已存在，置位事件未知。

**边界** 平衡等级消费有界先求平衡级再−4加0–4夹限；配置样本不证明实际地图事件启用。

**相关规格** [示例工程证据与能力覆盖](../spec/authoring/demo-evidence-and-capability-coverage.md)、[地图拓扑与转移](../spec/world/map-topology-transfer.md)、[随机地牢](../spec/world/random-dungeons.md)、[普通遭遇、触发与修正行为规格](../spec/world/wild-encounters-and-modifiers.md)、[野外被动变化与失败回程](../spec/world/field-passive-effects-and-blackout.md)、[Pokégear、区域地图、点唱机与电话行为规格](../spec/ui/pokegear-map-music-and-phone.md)、[邮件与神秘礼物行为规格](../spec/creatures/mail-and-mystery-gift.md)

<a id="g9-3"></a>
### 静态证据的适用单位

证据限于其检查过的输入、版本和范围。同一条旧结论不能自动适用于改变后的内容。

<a id="g9-4"></a>
### G9-4 缺失素材与资源回退

**接口** 缺Graphics/Audio/Plugins目录与资源缺失归一/匹配规则是不同事实；各入口回退条件独立。

**边界** 文件导航或请求曲目不证明真实像素/发声，素材未知继续保留。

**相关规格** [示例工程证据与能力覆盖](../spec/authoring/demo-evidence-and-capability-coverage.md)、[资源匹配、资源访问及声音](../spec/world/resource-matching-and-audio.md)

<a id="g9-5"></a>
### G9-5 场地能力资格 vs 地形/通行

**接口** 场地技能徽章/功能/队伍招式及朝向/地形/载具资格分门，效果与取消各自定义。

**边界** FLY成功前提和SPLASH句保留；直接FLASH效果与外层资格不同，不泛化所有地形行为。

**相关规格** [世界时间、天气与场地能力](../spec/world/world-time-weather-field-moves.md)、[地形、运动与载具](../spec/world/terrain-movement-vehicles.md)、[玩家、NPC 训练家与伙伴行为规格](../spec/creatures/player-trainers-partners.md)、[HP、异常状态、已知招式与持有状态行为规格](../spec/creatures/hp-status-moves-helditem.md)

<a id="g9-6"></a>
### G9-6 保存 UI 交接 vs 存档机制

**接口** 保存UI可用门、确认、反馈与实际存档/迁移机制分工；普通、事件、退出前、紧急入口分别交接。

**边界** 无效档/备份与删除双确认不统一。

**相关规格** [附：控制帮助（Controls help）四页场景合同](../spec/ui/controls-help-appendix.md)、[标题、载入、选项、暂停与 PC（主导航）行为规格](../spec/ui/title-load-options-pause-and-pc.md)、[附：训练家卡（Trainer Card）场景合同](../spec/ui/trainer-card-appendix.md)、[保存、启动、新游戏与继续](../spec/core/save-startup-continue.md)、[迁移、失败与恢复](../spec/core/migration-failure-recovery.md)
