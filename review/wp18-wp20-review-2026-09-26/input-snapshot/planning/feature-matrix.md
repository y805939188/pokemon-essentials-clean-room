# 初始 Feature Matrix

范围：18 个 major domains、113 个高层 feature groups。本表用于追踪后续行为提取；初始建立时没有任何条目完成详细规格（初始阶段说明；当前各条目状态以 Specification status 列为准，聚合规则见 [extraction-plan](extraction-plan.md) 第 2.1 节）。领域定义见 [module-map](module-map.md)；后续任务见 [extraction-plan](extraction-plan.md)。

Reference locations 中的 **E01–E34** 对应 [repository-overview 的证据索引](../analysis/repository-overview.md#7-证据索引供四份文档共同使用)，其中列明可展开的源路径和实际检查深度。每行的 E 编号是来源指针，不是对该来源全部行为的完成声明。Notes 中 WP 指向后续负责提取的包，U 指向总览的未知点。

状态：**Inventoried** = 已建立高层能力/来源；**Provisional** = 能力边界或启用/演示情况仍待材料或更深检查。进入详细提取后，Specification status 改用 [extraction-plan](extraction-plan.md) 第 2.1 节的最小状态集合（Drafted/ReviewPending/Reviewed/Partial/Blocked，始终附范围），并按承接包/子范围聚合表达；Inventoried/Provisional 仅用于尚未开始详细提取的条目或其未提取范围。置信度：**高** = 核心入口/状态行为与调用或数据相互支持；**中** = 入口或配置明确，但行为范围仅抽样；**低** = 主要为材料缺口下的演示线索。置信度仅针对本行简述，不针对数值正确性、运行可用性或完整覆盖。

证据状态另按总览记录为已定位、静态确认、数据样本确认、运行确认或待验证；它不替代 Specification status 或 Confidence。本轮没有运行确认。每域后续均需记录默认行为、支持的变体、配置关联和未验证组合。

Classification 使用一个主要类别；必要的跨域分类记入 Notes。可复用但非基础设施的玩法可附“可选通用玩法”标签，不新增第八类；D17 的 UI 分类主要标交互入口，玩法/胜负规则仍须在 D17 提取，不整体归入 UI 或 Generic Kernel。`Creature RPG` 对应 AGENTS 的 Creature-RPG，`Combat` 对应 Combat Requirements，`Engine/Overworld` 对应 Engine / Overworld Integration。

| Feature ID | Domain | Feature | Short description | Classification | Reference locations | Specification status | Confidence | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| F01-01 | D01 | 配置与机制选择 | 版本、容量、规则开关和表现参数共同影响行为 | Generic Kernel | E02 | Reviewed（WP02 词典/派生范围）＋Inventoried（各开关领域语义范围） | 高 | Pokémon 具体策略另列；WP02 配置档案见 [wp02-rule-configuration-and-data-variants](../specs/kernel/wp02-rule-configuration-and-data-variants.md)，2026-09-19 闭合复审通过；各开关在领域规则中的完整语义待相应领域包闭合 |
| F01-02 | D01 | 内容身份与注册查找 | 命名内容的注册、存在性检查、查找和枚举 | Generic Kernel | E04 | Reviewed（WP03 身份/注册查找/枚举/缺失值范围）＋Inventoried（各内容类字段语义范围） | 高 | 不预设未来 ID 类型；WP03 规格见 [wp03-content-identity-and-schema](../specs/kernel/wp03-content-identity-and-schema.md)，2026-09-19 闭合复审通过；字段语义按领域包闭合 |
| F01-03 | D01 | 事件与可扩展菜单 | 按世界/战斗通知及可用条件扩展行为和菜单 | Generic Kernel | E03、E18 | Reviewed（WP05 通知/菜单机制范围）＋Inventoried（各事件/菜单语义范围） | 高 | 与地图事件解释器分开；WP05 规格见 [wp05-events-extensions-plugins](../specs/kernel/wp05-events-extensions-plugins.md)，2026-09-19 v3 复审通过；各事件/菜单语义归领域包 |
| F01-04 | D01 | 插件依赖与载入 | 插件元数据、版本约束、冲突、循环依赖和顺序检查 | Generic Kernel | E03、E08 | Reviewed（WP05 元数据/依赖/载入机制范围）＋Provisional（真实插件组合范围） | 高 | 当前未提供插件实例；WP05 规格见 [wp05-events-extensions-plugins](../specs/kernel/wp05-events-extensions-plugins.md)，2026-09-19 v3 复审通过，U09 |
| F01-05 | D01 | 随机、时钟与计步依赖 | 随机选择、现实时间、运行时长与步数推动多个系统 | Generic Kernel | E08、E17–E19、E27–E29 | Reviewed（WP06 时间/随机/计步机制范围）＋Provisional（跨系统一致性 U05 与领域规则范围） | 中 | 不宣称已有统一随机服务；WP06 规格见 [wp06-time-random-steps-stats](../specs/kernel/wp06-time-random-steps-stats.md)，2026-09-19 批次闭合复审通过；领域规则归 WP14/WP33–37/WP58–61 |
| F01-06 | D01 | 诊断与错误反馈 | 调试信息、校验错误、异常记录和部分恢复路径 | Generic Kernel | E03、E05、E08、E33 | Reviewed（WP07 诊断面/失败层次范围）＋Inventoried（各业务失败语义范围） | 中 | 错误的用户反馈和副作用待分域核实；WP07 规格见 [wp07-diagnostics-files-http](../specs/kernel/wp07-diagnostics-files-http.md)，2026-09-19 v3 复审通过；业务失败归 WP04/WP05/WP15/WP64 |
| F01-07 | D01 | 文件与 HTTP 支持 | 资源/数据读取及远程内容下载等基础能力 | Generic Kernel | E01、E11、E30 | Reviewed（WP07 文件层/HTTP 包装范围）＋Provisional（HTTPS/归档模式/外部服务范围） | 中 | HTTP 路径还见 `S/001_Technical/002_Files/003_HTTP_Utilities.rb`；WP07 规格见 [wp07-diagnostics-files-http](../specs/kernel/wp07-diagnostics-files-http.md)，2026-09-19 v3 复审通过 |
| F02-01 | D02 | 内容目录与字段约束 | 物种、招式、道具、地图等内容具有结构及交叉引用 | Generic Kernel | E04、E34 | Reviewed（WP03 schema/已述校验边界/责任目录范围）＋Inventoried（字段语义全集范围） | 高 | 字段语义按领域提取；WP03 规格与字段责任目录见 [wp03-content-identity-and-schema](../specs/kernel/wp03-content-identity-and-schema.md) 第 5、7 节，2026-09-19 闭合复审通过 |
| F02-02 | D02 | PBS 编译与反写 | 校验内容、构建运行数据、导出及提供位置诊断 | Demo/Developer Experience | E05 | Reviewed（WP04 触发/解析/写回/失败范围）＋Inventoried（编辑器与转换规则全集范围） | 高 | 编译可能修改 PBS/地图，非只读；WP04 规格见 [wp04-pbs-lifecycle](../specs/kernel/wp04-pbs-lifecycle.md)，2026-09-19 v3 复审通过；编辑器与转换全集归 WP73/WP75 |
| F02-03 | D02 | 备选数据与机制兼容 | 各世代和 Shadow 备份内容与机制开关分别存在 | Pokémon Rules | E01、E02、E05、E34 | Reviewed（候选材料登记及已述发现边界范围）＋Provisional（切换、编译、兼容范围） | 中 | 子目录不自动启用，仅登记为候选变体材料（见 [wp02-rule-configuration-and-data-variants](../specs/kernel/wp02-rule-configuration-and-data-variants.md) 第 6 节），2026-09-19 闭合复审通过；组合兼容待核实；WP04，U03 |
| F02-04 | D02 | 内容到资源的匹配 | 物种/形态、训练家、道具等数据选择图像及声音 | Generic Kernel | E04、E11、E12 | Reviewed（WP15 变体选择/回退范围，2026-09-23 外审闭合 PASS_SCOPED；管理性回填）＋Inventoried（媒体实际存在范围） | 中 | 含参考项目特定资源命名约定；WP15 规格见 [wp15-resource-matching-and-audio](../specs/overworld/wp15-resource-matching-and-audio.md) |
| F02-05 | D02 | 文本与语言资源 | 核心、游戏、地图文本提取/编译与语言选择 | Generic Kernel | E06、E08 | Reviewed（WP08 文本域/语言/查找/工作流范围）＋Inventoried（消费者文本呈现范围） | 高 | 字体/文本展示另见 D05/D16；WP08 规格见 [wp08-localization](../specs/kernel/wp08-localization.md)，2026-09-19 闭合复审通过；文本呈现归 D05/D16 |
| F03-01 | D03 | 持久状态登记与保存 | 指定哪些状态保存、初始化或在启动阶段载入 | Generic Kernel | E07、E08 | Reviewed（WP09 持久值目录/机制范围）＋Inventoried（各值字段语义范围） | 高 | 不要求沿用当前存储格式；WP09 规格见 [wp09-save-startup-continue](../specs/kernel/wp09-save-startup-continue.md)，2026-09-19 v2 复审通过；字段语义归领域包 |
| F03-02 | D03 | 旧存档转换 | 根据引擎/游戏版本处理旧数据格式与状态转换 | Generic Kernel | E07 | Reviewed（WP10 转换机制/目录范围）＋Inventoried（旧档样本与宿主行为范围） | 中 | 备份/转换失败边界待细查；WP10 规格见 [wp10-migration-failure-recovery](../specs/kernel/wp10-migration-failure-recovery.md)，2026-09-19 闭合复审通过；不宣称任意旧档全兼容 |
| F03-03 | D03 | 启动、新游戏与继续 | 载入设置、建立新状态或恢复已有地图世界 | Engine/Overworld | E08、E31 | Reviewed（WP09 启动阶段/新游戏/继续范围）＋Inventoried（启动 UI 与失败恢复范围） | 高 | UI 选项可见性归 D16；WP09 规格见 [wp09-save-startup-continue](../specs/kernel/wp09-save-startup-continue.md)，2026-09-19 v2 复审通过；失败/迁移归 WP10 |
| F03-04 | D03 | 载入/保存异常及恢复 | 保存失败反馈、地图缺失/损坏处理及紧急保存入口 | Generic Kernel | E07、E08 | Reviewed（WP10 失败/备份/紧急保存范围）＋Inventoried（完整失败恢复路径范围） | 高 | 调试与普通运行不同；WP10 规格见 [wp10-migration-failure-recovery](../specs/kernel/wp10-migration-failure-recovery.md)，2026-09-19 闭合复审通过 |
| F03-05 | D03 | 游戏统计与历程 | 累计时间、会话、移动、战斗和交易等活动数据 | Creature RPG | E08、E13、E18、E31 | Reviewed（WP06 统计目录、已述更新与保存交界范围）＋Inventoried（统计全集与迁移范围） | 中 | 统计重置与存档边界是横切项；WP06 规格与目录附表见 [wp06-time-random-steps-stats](../specs/kernel/wp06-time-random-steps-stats.md) 第 4 节及 [wp06-stats-directory](../specs/kernel/wp06-stats-directory.md)，2026-09-19 批次闭合复审通过；迁移归 WP10 |
| F04-01 | D04 | 地图连接与转移 | 管理相邻地图关系、坐标位置及地图切换 | Engine/Overworld | E09、E34 | Reviewed（WP11 拓扑/连接/转移范围，2026-09-22 外审 PASS_SCOPED；管理性回填）＋Inventoried（元数据语义与可达范围） | 高 | 连接配置与实际地图尺寸须联验；WP11 规格见 [wp11-map-topology-transfer](../specs/overworld/wp11-map-topology-transfer.md)；可达性 U01 |
| F04-02 | D04 | 地形与通行 | 地形标记、碰撞与位置环境影响移动和事件判定 | Engine/Overworld | E09、E18 | Reviewed（WP12 地形能力/通行判定范围，2026-09-22 外审 PASS_SCOPED；管理性回填）＋Inventoried（真实地图通行流程范围） | 中 | 草、水、桥等会被遭遇/场地消费者读取；WP12 规格见 [wp12-terrain-movement-vehicles](../specs/overworld/wp12-terrain-movement-vehicles.md)；WP36/WP59 交界 |
| F04-03 | D04 | 玩家运动和载具 | 走跑、骑行、水上/水下运动及许可/外观切换 | Engine/Overworld | E09、E28、E34 | Reviewed（WP12 移动/运动状态/载具范围，2026-09-22 外审 PASS_SCOPED；管理性回填）＋Inventoried（场地招式与媒体结果范围） | 高 | 解锁许可涉及玩家和场地招式；WP12 规格见 [wp12-terrain-movement-vehicles](../specs/overworld/wp12-terrain-movement-vehicles.md)；WP24/WP59 交界 |
| F04-04 | D04 | 地图事件与状态控制 | 事件条件、开关变量、公共事件、互动及命令执行 | Engine/Overworld | E10、E05 | Reviewed（WP13 事件页/触发/解释器/命令矩阵范围，2026-09-23 外审闭合 PASS_SCOPED；管理性回填）＋Inventoried（Demo 事件与完整流程范围） | 高 | 标准 RMXP 命令中存在空操作（28 个 command_dummy）；WP13 规格与命令/移动路线矩阵见 [wp13-map-events-npc-followers](../specs/overworld/wp13-map-events-npc-followers.md)、[wp13-interpreter-command-matrix](../specs/overworld/wp13-interpreter-command-matrix.md) 及 [wp13-move-route-matrix](../specs/overworld/wp13-move-route-matrix.md)，U08 |
| F04-05 | D04 | NPC、训练家感知与跟随 | 事件角色移动、远距触发、跟随及地图转移约束 | Engine/Overworld | E09、E10、E18 | Reviewed（WP13 NPC/感知/跟随范围，2026-09-23 外审闭合 PASS_SCOPED；管理性回填）＋Inventoried（完整跟随系统范围） | 中 | 不能自动等同于完整跟随宝可梦系统；事件跟随机制已按源码提取（守卫仅适用特定入口）；WP13 规格见 [wp13-map-events-npc-followers](../specs/overworld/wp13-map-events-npc-followers.md)；WP24/WP63 交界 |
| F04-06 | D04 | 随机地牢 | 按参数生成布局、安排事件和玩家位置 | Engine/Overworld | E29、E34 | Reviewed（WP14 生成规则/摆放/失败范围，2026-09-23 外审闭合 PASS_SCOPED；管理性回填）＋Inventoried（真实地图可达性与种子复现范围） | 高 | 补充标签：可选通用玩法；布局不自动归 Kernel，未运行种子/可达性测试；WP14 规格见 [wp14-random-dungeons](../specs/overworld/wp14-random-dungeons.md) |
| F05-01 | D05 | 资源解析与生命周期 | 获取/缓存图像、解析资源变体及处理资源使用 | Engine/Overworld | E11、E12 | Reviewed（WP15 解析/缓存/缺失边界范围，2026-09-23 外审闭合 PASS_SCOPED；管理性回填）＋Inventoried（动画位图逐入口行为范围） | 中 | 仅提取可见要求及缺失资源行为；WP15 规格见 [wp15-resource-matching-and-audio](../specs/overworld/wp15-resource-matching-and-audio.md) |
| F05-02 | D05 | 声音与音乐 | BGM/BGS/SE/ME、切换恢复、菜单音和物种叫声 | Engine/Overworld | E11、E12、E18 | Reviewed（WP15 播放/切换/暂停恢复/叫声范围，2026-09-23 外审闭合 PASS_SCOPED；管理性回填）＋Inventoried（实际播放与战斗内音频范围） | 高 | 战斗/骑行/地图选择声音另有消费者；WP15 规格见 [wp15-resource-matching-and-audio](../specs/overworld/wp15-resource-matching-and-audio.md) |
| F05-03 | D05 | 地图绘制 | tileset、自动图块、地图位置与分层可视效果 | Engine/Overworld | E11、E09 | Reviewed（WP16 图块层/滚动/拼接/分层范围，2026-09-23 外审闭合 PASS_SCOPED；管理性回填）＋Inventoried（实际视觉结果范围） | 中 | 不保留渲染器架构；WP16 规格见 [wp16-world-rendering-and-visual-transitions](../specs/overworld/wp16-world-rendering-and-visual-transitions.md) |
| F05-04 | D05 | 精灵、天气与场景过渡 | 角色/物品精灵、反射阴影、天气叠层和转场动画 | Engine/Overworld | E11、E28、E31 | Reviewed（WP16 精灵/反射/天气/过渡范围，2026-09-23 外审闭合 PASS_SCOPED；管理性回填）＋Inventoried（动态阴影创建者与实际时序范围） | 中 | 资源缺失，视觉时序未运行验证；WP16 规格见 [wp16-world-rendering-and-visual-transitions](../specs/overworld/wp16-world-rendering-and-visual-transitions.md) |
| F05-05 | D05 | 消息与基础窗口 | 显示文本、选项、数量、提示及用户等待反馈 | UI | E11、E10 | Reviewed（WP17 消息/选项/数量/交界范围，2026-09-23 外审闭合 PASS_SCOPED；管理性回填）＋Inventoried（真实交互观察范围） | 高 | 文字格式、取消与输入上限已按源码提取；WP17 规格见 [wp17-messages-windows-input](../specs/ui/wp17-messages-windows-input.md) 及附表 [wp17-draw-text-tags](../specs/ui/wp17-draw-text-tags.md) |
| F05-06 | D05 | 输入与文字输入 | 操作键、鼠标坐标和文本输入支撑交互 | UI | E11、E31 | Reviewed（WP17 按键/文字输入/取消范围，2026-09-23 外审闭合 PASS_SCOPED；管理性回填）＋Inventoried（宿主输入与鼠标支持面范围） | 中 | 不推断所有 UI 支持鼠标；WP17 规格见 [wp17-messages-windows-input](../specs/ui/wp17-messages-windows-input.md) |
| F06-01 | D06 | 物种与形态内容 | 定义物种信息、形态差异、学习表及生命周期引用 | Creature RPG | E04、E12 | ReviewPending（WP18 物种/形态内容分层、查找身份与字段责任范围；批内自检完成、批末统一送审）＋Inventoried（动态形态触发/优先级范围） | 高 | Pokémon 特定字段单列；WP18 规格见 [wp18-creature-identity-species-ownership](../specs/creature-rpg/wp18-creature-identity-species-ownership.md)；动态形态语义 WP21 |
| F06-02 | D06 | 个体身份和来源 | 个体身份、名字、拥有者、获得方式及地点时间 | Creature RPG | E12、E13 | ReviewPending（WP18 个体生成/复制/来源记录范围；批内自检完成、批末统一送审）＋Inventoried（赠送/交换/捕获完整接收流程范围） | 高 | 赠送/交换/捕获修改来源；WP18 规格见 [wp18-creature-identity-species-ownership](../specs/creature-rpg/wp18-creature-identity-species-ownership.md)；完整流程 WP26/WP38 |
| F06-03 | D06 | Pokémon 属性和个体差异 | 类型、性别、异色、特性选择及个人差异 | Pokémon Rules | E04、E12 | ReviewPending（WP19 类型/性别/异色/特性/Nature 派生与缓存范围；批内自检完成、批末统一送审）＋Inventoried（派生结果在战斗/野外的完整消费范围） | 高 | 属性概念与 Pokémon 具体判定分开；派生/缓存规则已按源码提取；WP19 规格见 [wp19-attributes-ability-and-stats](../specs/pokemon-rules/wp19-attributes-ability-and-stats.md) |
| F06-04 | D06 | 六项能力与培养参数 | 基础能力、等级、IV、EV、Nature 等共同决定数值 | Pokémon Rules | E02、E04、E12 | ReviewPending（WP19 能力公式/IV/EV/Nature/重算与写回范围；批内自检完成、批末统一送审）＋Inventoried（Hyper 启用入口与成长流程范围） | 高 | 包括能力重算与 Hyper Training 标记（标记接口与生效方式已登记；正常启用入口未定位）；WP19 规格见 [wp19-attributes-ability-and-stats](../specs/pokemon-rules/wp19-attributes-ability-and-stats.md) |
| F06-05 | D06 | HP、状态与恢复 | 个体生命、异常状态、濒死及治疗的持久状态 | Creature RPG | E12、E14 | ReviewPending（WP20 HP/濒死/治疗入口/异常与计数范围；批内自检完成、批末统一送审）＋Inventoried（战斗内状态机制与资源实际表现范围） | 高 | 战斗内临时状态另列（写穿/快照还原已登记）；WP20 规格见 [wp20-hp-status-moves-helditem](../specs/creature-rpg/wp20-hp-status-moves-helditem.md) |
| F06-06 | D06 | 已知招式与 PP | 已知招式槽、最初招式记录、PP 及恢复的持久状态 | Pokémon Rules | E12、E14、E16 | ReviewPending（WP20 招式槽/PP/最初招式记录/重学接口范围；批内自检完成、批末统一送审）＋Inventoried（学习替换交互与重学 UI 范围） | 中 | 状态约束 WP20；学习/替换主规则 F09-01／WP30；WP20 规格见 [wp20-hp-status-moves-helditem](../specs/creature-rpg/wp20-hp-status-moves-helditem.md) |
| F06-07 | D06 | 动态形态和展示属性 | 形态可依情境改变；标记、缎带等记录可展示 | Pokémon Rules | E12、E04、E31 | Inventoried | 中 | 个体含华丽大赛属性不证明完整比赛；WP21，U04 |
| F06-08 | D06 | 特殊变身与 Shadow 状态 | Mega/Primal 各自形态变化；Shadow/Hyper、成长暂存、净化与招式/EV/经验恢复 | Pokémon Rules | E25、E21、E34 | Inventoried | 高 | WP22、WP23 分开；战斗资格/时机 WP40，成长规则 WP30，净化 UI WP67-B；U06 |
| F07-01 | D07 | 拥有者与外来个体 | 训练家身份、原拥有者与外来个体关系 | Creature RPG | E12、E13 | ReviewPending（WP18 拥有者结构/变更入口/外来判定范围；批内自检完成、批末统一送审）＋Inventoried（服从/繁殖/彩票等消费者范围） | 高 | 后续影响经验、服从、繁殖和彩票；WP18 规格见 [wp18-creature-identity-species-ownership](../specs/creature-rpg/wp18-creature-identity-species-ownership.md)；服从性 WP40 |
| F07-02 | D07 | NPC 训练家与伙伴 | 加载训练家变体、队伍、物品、技能和伙伴参与 | Creature RPG | E13、E18、E24、E34 | Inventoried | 高 | 行为技能档归战斗 AI；WP24 |
| F07-03 | D07 | 玩家资料、许可和货币 | 玩家外观/身份、徽章、功能解锁及多种资源额度 | Creature RPG | E13、E02 | Inventoried | 高 | 徽章等 Pokémon 特定规则分离；WP24 |
| F07-04 | D07 | 队伍与可用成员 | 队伍容量、顺序、蛋/可出战成员和相关限制 | Creature RPG | E13、E18、E31 | Inventoried | 高 | 不把默认队伍容量推广成通用规则；WP25 |
| F07-05 | D07 | 生物储存 | 多盒存取、容量、命名/背景及存放恢复行为 | Creature RPG | E13、E31、E20 | Inventoried | 高 | UI 对最后可用成员等限制需联查；WP25 |
| F07-06 | D07 | 脚本交换 | 将队伍成员交换为指定生物并更新来源和图鉴 | Creature RPG | E31、E12 | Inventoried | 高 | 不等于网络交换；WP26，U04 |
| F08-01 | D08 | 背包容量与数量 | 按口袋组织物品，添加/删除/替换与容量判断 | Creature RPG | E14、E02 | Inventoried | 高 | 部分成功与全有全无入口需区分；WP27 |
| F08-02 | D08 | 物品储存与快捷登记 | PC 物品存放、登记和野外快捷使用 | Creature RPG | E14、E31 | Inventoried | 中 | 具体 UI 流程归 D16；WP27 |
| F08-03 | D08 | 道具使用上下文 | 背包、野外、个体和战斗的使用资格、消耗与结果 | Creature RPG | E14、E21 | Inventoried | 高 | 通用资格/消耗 WP28；捕获判定引用 WP38，投球战斗合法性引用 WP40；具体效果另分类 |
| F08-04 | D08 | 治疗、培养和教学道具 | 治疗/复活、能力培养及机器/导师教学等效果 | Pokémon Rules | E14、E16、E02 | Inventoried | 中 | 进化条件归 D09；WP28 |
| F08-05 | D08 | 持有物与被动效果 | 携带物品在战斗和其他规则中产生作用并可消耗 | Pokémon Rules | E12、E14、E23 | ReviewPending（WP20 普通持有状态读取/变更/清除范围；批内自检完成、批末统一送审）＋Inventoried（触发/消耗/恢复效果与主动道具范围） | 高 | 普通持有状态在 WP20（含战斗快照还原边界）；触发/恢复规则 WP50；WP20 规格见 [wp20-hp-status-moves-helditem](../specs/creature-rpg/wp20-hp-status-moves-helditem.md) |
| F08-06 | D08 | 商店与资源交换 | 金钱买卖、价格覆盖、重要物品限制及 BP 兑换 | Creature RPG | E15、E13 | Inventoried | 高 | 事件定义库存/价格配置待 demo；WP29 |
| F09-01 | D09 | 经验、等级、EV 与招式学习/替换 | 成长、收益分配、学习/替换/放弃；结果可反馈仍在进行的战斗 | Pokémon Rules | E16、E12、E02 | Inventoried | 高 | 成长/学习唯一主规格 WP30；战斗中触发/能力和招式同步 WP42；Shadow 暂存 WP23 |
| F09-02 | D09 | 友好、亲密和相关培养 | 活动改变友好状态并被进化/战斗等读取 | Pokémon Rules | E12、E02、E28 | Inventoried | 中 | Pokémon 关系规则；WP30 |
| F09-03 | D09 | 升级及道具进化 | 根据个体条件/项目检查目标并完成永久变化 | Pokémon Rules | E16、E12、E14 | Inventoried | 高 | 包括阻止、取消和副作用；WP31 |
| F09-04 | D09 | 情境、交换与战后进化 | 以地点、时间、交换或战斗成就为输入判断进化 | Pokémon Rules | E16、E18、E31 | Inventoried | 高 | 跨模块状态/时序重点；WP32 |
| F09-05 | D09 | 寄养和繁殖资格 | 寄存、取回、费用、兼容性及生成蛋的周期 | Creature RPG | E17、E13 | Inventoried | 高 | 培育屋收费部分依赖 demo 事件；WP33，U01 |
| F09-06 | D09 | 后代与遗传规则 | 选择后代物种/形态并继承招式、Nature、IV 等 | Pokémon Rules | E17、E12、E02 | Inventoried | 高 | 内容/世代组合须有测试向量；WP34 |
| F09-07 | D09 | 蛋与孵化 | 孵化步数、状态转化、来源和命名/展示 | Creature RPG | E17、E28、E31 | Inventoried | 中 | Pokémon 加速条件另外注明；WP35 |
| F10-01 | D10 | 遭遇表与选择 | 根据地图、版本、方式及时段选择物种和等级 | Creature RPG | E18、E34 | Inventoried | 高 | 权重与等级区间待详细提取；WP36 |
| F10-02 | D10 | 遭遇触发和修正 | 步数、地形、驱赶、特性/道具等修改遭遇 | Pokémon Rules | E18、E02、E14 | Inventoried | 高 | 选择前后修改顺序待明确；WP36 |
| F10-03 | D10 | 漫游个体 | 漫游位置、遭遇替换、战斗结果及持续状态 | Pokémon Rules | E19、E18、E02 | Inventoried | 中 | 开关和路线为配置；WP37 |
| F10-04 | D10 | Poké Radar 连锁 | 摇动草丛、连锁、特殊遭遇与结果联动 | Pokémon Rules | E19、E18、E34 | Inventoried | 中 | 地图/移动失效条件待核实；WP37 |
| F10-05 | D10 | 赠送与获得入口 | 获得生物或蛋，处理容量、命名和收集登记 | Creature RPG | E13、E17、E30 | Inventoried | 高 | 不同入口并非一定共用同一失败行为；WP26 |
| F10-06 | D10 | 球捕获与接收结果 | 捕获判定/概率、特殊球/抢夺例外、强制入队等接收策略及登记/存放流程 | Pokémon Rules | E20、E13、E14、E21、E30 | Inventoried | 高 | 捕获唯一主规格 WP38；库存/动作/集合/图鉴分别引用 D08/D11/D07/D15，取消许可不归 UI 独立决定；U07 |
| F11-01 | D11 | 战斗创建上下文 | 野生/训练家入口、地图环境、临时规则和前后通知 | Combat | E18、E21 | Inventoried | 高 | 世界层准备与规则层输入分开；WP39 |
| F11-02 | D11 | 参战者与布局 | 多训练家、伙伴、单/双/三打及不对称双方人数 | Combat | E18、E21 | Inventoried | 高 | 不推断任意人数支持；WP39 |
| F11-03 | D11 | 命令、特殊动作与服从性 | 招式/物品/换人/逃跑、Shift/Call、投球条件与命令能否按意图执行 | Combat | E21、E22、E02、E25、E31 | Inventoried | 中 | WP40；服从性区别于 AI；Call 同时追踪 Shadow 和其他效果 |
| F11-04 | D11 | 优先级与行动顺序 | 优先级/速度安排与重排；Mega/Primal 各自触发、Mega 次数和顺序条件 | Combat | E21、E02、E23 | Inventoried | 中 | WP40；形态状态引用 WP22，数值/特性引用 D12；配置变体单列 |
| F11-05 | D11 | 换人、位置移动、逃跑与行动限制 | 进出场/替补/逃脱及场上 Shift 位置移动的状态变化 | Combat | E21、E22、E23 | Inventoried | 中 | WP41；区别替补换人与位置移动，多人布局/效果交叉核对 |
| F11-06 | D11 | 回合结束和状态期限 | 回合末伤害/恢复、计时效果、失效与替补需求 | Combat | E21、E23 | Inventoried | 中 | 先定义生命周期，再细分触发顺序；WP42 |
| F11-07 | D11 | 战斗中成长交界与终局结算 | 成长触发与当前参战状态反馈，以及胜败/逃脱/捕获/平局后的清理和返回 | Combat | E18、E21、E16、E20 | Inventoried | 高 | WP42；成长规则引用 WP30；持续战斗中的能力/招式同步与终局分别核对 |
| F12-01 | D12 | 属性、命中和伤害计算 | 类型效果、命中/闪避、会心、伤害和相关修正 | Pokémon Rules | E22、E23、E02 | Inventoried | 高 | 本轮不提取公式；WP43 |
| F12-02 | D12 | 异常、能力阶级和免疫 | 战斗状态变化、能力阶级、阻止/解除与免疫规则 | Pokémon Rules | E22、E23 | Inventoried | 中 | 暂时战斗状态与个体状态需区分；WP44 |
| F12-03 | D12 | 全场、阵营与位置效果 | 天气、场地、阵营及位置上的持续/延迟效果 | Pokémon Rules | E23、E21、E22 | Inventoried | 中 | 期限/换人/结束清理均需审查；WP45 |
| F12-04 | D12 | 招式效果：伤害与恢复 | 多次攻击、伤害特例、吸取/反伤和恢复效果族 | Pokémon Rules | E22 | Inventoried | 中 | 按行为族枚举，不能只查 PBS 名称；WP46 只映射本包伤害/恢复范围的效果，全局映射随各包累积、WP79 审查未归属项 |
| F12-05 | D12 | 招式效果：控制与变更 | 招式复制/调用、目标/行动变化、替换、物品影响等 | Pokémon Rules | E22、E23 | Inventoried | 中 | 边界复杂，必要时再按家族拆分；WP47 |
| F12-06 | D12 | 特性效果与触发阶段 | 特性参与计算及生命变化、入离场等阶段 | Pokémon Rules | E23、E22 | Inventoried | 高 | 计算修正 WP48；阶段触发 WP49 |
| F12-07 | D12 | AI 行动策略与能力档 | 技能值/标记影响换人、使用物品、变身和招式选择 | Combat | E24、E04 | Inventoried | 高 | WP51；观察选择策略，服从性仅引用 WP40；不复制评分架构 |
| F12-08 | D12 | AI 效果评估 | 按失败、目标、效果与局势评价候选行动 | Combat | E24、E22、E23 | Inventoried | 中 | 与实际效果可能有偏差，必须另审；WP52 |
| F13-01 | D13 | Safari 会话与捕获战斗 | 专用球、步数预算、模式动作及结束回程 | Pokémon Rules | E26、E34 | Inventoried | 高 | 接待费用/奖励事件未知；WP53 |
| F13-02 | D13 | 捕虫大会 | 限时参赛、保留捕获结果、对手生成及评判 | Pokémon Rules | E26、E18、E34 | Inventoried | 高 | 与一般华丽大赛不同；WP53 |
| F13-03 | D13 | 参赛规则与杯赛 | 个体/队伍资格、数量、等级调整和战斗条款 | Combat | E27、E23、E34 | Inventoried | 高 | Pokémon 特定资格另列；WP54 |
| F13-04 | D13 | 设施会话和特殊胜负 | 挑战进度、对手与胜场；Palace/Arena 改变行动或评判 | Combat | E27、E34 | Inventoried | 高 | 会话 WP55；特殊规则 WP56 |
| F13-05 | D13 | 租借与交换队伍 | Factory 选择租借成员并在挑战阶段交换 | Creature RPG | E27 | Inventoried | 中 | 原队伍隔离和恢复重点；WP57 |
| F13-06 | D13 | 战斗记录与回放 | 记录参战条件、选择及随机结果用于重播 | Combat | E27 | Inventoried | 高 | 未证明任意战斗/跨版本可重播；WP58，U05 |
| F14-01 | D14 | 世界时间、季节和天气 | 时段/日历/天气影响展示和世界规则 | Engine/Overworld | E28、E18、E34 | Inventoried | 中 | 宿主时钟与保存恢复要求 WP06；消费者 WP59 |
| F14-02 | D14 | 场地招式与旅行能力 | 检查徽章/成员/环境并执行砍树、冲浪、飞行等 | Pokémon Rules | E28、E09、E02 | Inventoried | 高 | 移动结果归引擎集成；WP59 |
| F14-03 | D14 | 树果种植 | 种植、浇水、成长、重植、产量及采摘 | Pokémon Rules | E28、E14、E34 | Inventoried | 高 | 时间/世代机制/背包满需联查；WP60 |
| F14-04 | D14 | 钓鱼交互 | 工具、环境和等待/输入过程触发对应遭遇 | Engine/Overworld | E19、E18、E02、E34 | Inventoried | 中 | 鱼种/概率归遭遇表；WP60 |
| F14-05 | D14 | 逐步效果、治疗与失败回程 | 野外状态变化、Pokérus、友好、治疗/逃脱点及全队失效处理 | Pokémon Rules | E28、E18、E12 | Inventoried | 中 | Pokémon 特例与世界转移分离；WP61 |
| F15-01 | D15 | Pokédex 收集记录 | 见过/拥有、形态、区域图鉴解锁和捕获/击败记录 | Pokémon Rules | E30、E20、E13、E34 | Inventoried | 高 | 展示排序/搜索等 UI 另查；WP62 |
| F15-02 | D15 | Pokégear、区域地图与音乐 | 工具入口、地点信息/旅行目标及音乐选择 | UI | E30、E34、E28 | Inventoried | 中 | 菜单许可与地图功能相连；WP63 |
| F15-03 | D15 | 电话、联系人和再战 | 登记联系人、来去电、文本选择及训练家版本推进 | Creature RPG | E30、E34、E13 | Inventoried | 高 | 公共事件电话/接待联动依赖缺失材料；WP63 |
| F15-04 | D15 | 游戏内邮件 | 写信、附在个体上、阅读及转入信箱 | Creature RPG | E15、E31、E12 | Inventoried | 中 | 与交换/持有物限制需联查；WP64 |
| F15-05 | D15 | 神秘礼物 | 下载候选、避免重复、暂存和领取物品/生物 | Creature RPG | E30、E13、E14 | Inventoried | 高 | 样例服务未访问；不推断通用联机功能；WP64，U09 |
| F16-01 | D16 | 标题、载入、选项和玩家设置 | 游戏入口、设置调整和保存/继续操作 | UI | E08、E31、E06 | Inventoried | 中 | 缺失资源下不声明视觉已验证；WP65 |
| F16-02 | D16 | 暂停、PC 与快捷菜单 | 按状态显示菜单并转入领域功能 | UI | E31、E03、E14 | Inventoried | 高 | 菜单扩展机制另列；WP65 |
| F16-03 | D16 | 队伍、摘要、图鉴与盒子界面 | 浏览/管理个体和记录，呈现招式查看与学习/替换选择 | UI | E31、E13、E30 | Inventoried | 中 | 领域许可/规则引用主规格；WP66，学招关联 WP30 |
| F16-04 | D16 | 背包、购物与数量选择 | 在资源变更前选择对象/数量、确认并反馈失败 | UI | E31、E15、E14 | Inventoried | 高 | 避免重复定义价格/容量；WP66 |
| F16-05 | D16 | 战斗命令和反馈 | 命令/目标/队伍/物品选择、战斗中学招和结果反馈 | UI | E31、E20、E21、E16 | Inventoried | 中 | WP67-A；取消/强制入队权限引用领域策略，学招交互与当前战斗更新联审 |
| F16-06 | D16 | 生命周期演出和历程展示 | 进化、孵化、交换、净化结果与命名、名人堂及片尾流程 | UI | E31、E16、E17、E25 | Inventoried | 中 | WP67-B；净化规则引用 WP23，追踪 UI 中的领域写入 |
| F17-01 | D17 | Duel | 玩家与事件对手参与独立对决活动 | UI | E32 | Inventoried | 中 | 可选通用玩法；UI 仅标交互主入口，独立对决规则仍由 D17／WP68 提取 |
| F17-02 | D17 | Triple Triad | 基于物种的卡片、卡牌对局和持有/买卖 | Creature RPG | E32、E04 | Inventoried | 中 | 可选通用玩法与物种卡面规则分别描述；不因可复用就归 Kernel；WP68 |
| F17-03 | D17 | Slot Machine | 代币准入、转轮操作与结算 | UI | E32、E13、E14 | Inventoried | 高 | 可选通用玩法；UI 不涵盖全部结算规则，概率/难度待分析；WP69 |
| F17-04 | D17 | Voltorb Flip | 棋盘推理、得分、等级和代币结算 | Pokémon Rules | E32、E13 | Inventoried | 中 | 仅确认入口/能力族；WP69 |
| F17-05 | D17 | Lottery | 按拥有者号码匹配队伍/盒子中的个体 | Pokémon Rules | E32、E13 | Inventoried | 高 | 外部事件如何发奖待验证；WP70 |
| F17-06 | D17 | Mining | 操作挖掘场景并揭露/领取物品 | UI | E32、E14 | Inventoried | 中 | 可选通用玩法；UI 不涵盖全部玩法/奖励规则，容量失败与离场待查；WP70 |
| F17-07 | D17 | Tile Puzzles | 不同拼图操作与成功/退出结果 | UI | E32 | Inventoried | 中 | 可选通用玩法；UI 不涵盖胜负规则，具体模式逐项提取；WP71 |
| F18-01 | D18 | 调试与情境构造 | 修改状态、创建队伍/战斗、操控地图与检查效果 | Demo/Developer Experience | E33、E21、E24 | Inventoried | 高 | 作为作者行为要求，不建议照搬调试实现；WP72 |
| F18-02 | D18 | 数据和世界编辑器 | 编辑训练家、物种、遭遇、地图连接、地形及指标 | Demo/Developer Experience | E33、E05、E04 | Inventoried | 高 | 保存/反写兼容是独立验收点；WP73 |
| F18-03 | D18 | 战斗动画制作 | 编辑/组织/导入/导出动画并关联表现资源 | Demo/Developer Experience | E33、E11 | Inventoried | 中 | 无动画资产和运行验证；WP74 |
| F18-04 | D18 | 工程转换与外围制作工具 | 事件简写转换、旧脚本用法转换、文件组织及辅助制作 | Demo/Developer Experience | E01、E05、E33 | Inventoried | 中 | 脚本工具本轮主要据 README；完整功能后查；WP75 |
| F18-05 | D18 | 挑战内容生成与评估 | 生成参赛生物/训练家池并筛选/模拟评估 | Demo/Developer Experience | E27 | Inventoried | 中 | 不将生成器当作普通游戏战斗；WP76 |
| F18-06 | D18 | demo 场景与能力示例 | 用地图、遭遇、训练家和设施配置建立演示覆盖候选 | Demo/Developer Experience | E34、E18、E26、E27 | Provisional | 中 | 有配置证据，未证实事件可达性；WP77 |
| F18-07 | D18 | 基线、缺失材料与兼容范围 | 明确当前快照实际包含什么、还需哪些演示/运行证据 | Demo/Developer Experience | E01、E02、E34 | Reviewed（WP01 基线范围）＋Provisional（WP77 Demo 范围） | 高 | 高置信度针对缺失事实；WP01 规格见 [wp01-baseline-and-evidence-scope](../specs/demo/wp01-baseline-and-evidence-scope.md)，2026-09-19 闭合复审通过；demo 实际流程仍未知，WP77 有事件证据后方可标记已演示 |

## 使用和维护规则

1. 当前 113 是**初始高层组数**，不是具体招式、物种、UI 页面或最终 requirement 数。无搜索命中项没有作为已存在功能计入。
2. 后续拆分保留父 Feature ID，新增子编号并记录父子覆盖，避免“改名即完成”。状态只有在详细输出和证据达到提取计划的共同完成标准后才能推进。
3. 每一包完成后更新相关条目、实际证据、配置范围、测试场景与未决问题；引用同一个 E 包不表示两条需求相同。维持 D → F → 规格/规则编号 → 证据与测试场景；每条规则唯一主规格，跨域只引用。
4. 所有 UI/Engine 条目的运行可用性目前未经确认。demo 可达性、插件组合、网络有效性等缺口应独立保留，不能用高静态置信度掩盖。
5. 最终覆盖审查另检查尚未识别的能力、未关联源文件、未消费配置、孤立入口与例外；本表不是“没有列出就不存在”的白名单。
6. Feature 状态按承接它的工作包/子范围聚合表达，同一条目可同时持有不同范围的不同状态（约定见 [extraction-plan](extraction-plan.md) 第 2.1 节）；一个工作包完成其声明范围，不等于该 Feature 的全部范围完成。
