# 本轮统一发现台账（进行中）

这是审查检查点，不是全量结论。各组原始报告保持原样；同根归并、优先级调整和第二审查者依据在 findings.json 中分列。未裁决候选不当作已确认缺陷。

| 全局 ID | 当前级别 | 标题 | 当前处置 | 原始 ID |
| --- | --- | --- | --- | --- |
| WP80-INTAKE-R01 | P2 | 必要输入语法全角化 | OPEN_PENDING_FINAL_ADJUDICATION | RUN-C-001 |
| WP80-INTAKE-R02 | P2 | 原输入批准与净化输出待审混淆 | OPEN_PENDING_FINAL_ADJUDICATION | ROOT/intake |
| WP80-INTAKE-C01 | P3 | 作者报告分域和测试族统计错误 | OPEN_PENDING_FINAL_ADJUDICATION | ROOT/intake |
| WP80-B02-R01 | P2 | 来源结构与取证统计进入净化正文 | PARTIALLY_ADDRESSED_RESIDUAL_OPEN | RUN-A-007 |
| WP80-B02-R02 | P2 | 批准身份和条款去向声明不准确 | PARTIALLY_ADDRESSED_RESIDUAL_OPEN | RUN-A-008 |
| GIR-FD82-001 | P3 | 全集范围声明与导航仍停留在旧交付阶段 | CONFIRMED_REQUIRED_REVISION | RUN-A-005,RUN-D-001 |
| GIR-FD82-002 | P2 | 旧不适用判定遗漏图片、计时器及地图覆盖层的可观察合同 | OPEN_PENDING_PEER | ROOT/intake |
| GIR-FD82-A001 | P2 | 奇数引号合并耗尽输入时，KL10 错误预期去除包围标记 | OPEN_PENDING_ADJUDICATION | RUN-A-001 |
| GIR-FD82-A002 | P2 | PBS 新鲜度判定遗漏整数秒取整 | OPEN_PENDING_ADJUDICATION | RUN-A-002 |
| GIR-FD82-A003 | P2 | 净化将 Scripts 的假值检查写成空列表检查 | OPEN_PENDING_ADJUDICATION | RUN-A-003 |
| GIR-FD82-A004 | P2 | 插件自动发现遗漏路径子串规则及显式 Scripts 顺序 | OPEN_PENDING_ADJUDICATION | RUN-A-004 |
| GIR-FD82-A006 | P2 | 把调试菜单的翻译导出语言选择误当作游戏语言切换 | OPEN_PENDING_ADJUDICATION | RUN-A-006 |
| GIR-FD82-A009 | P3 | EP08 无条件要求更新链接但未提供 Link 前提 | OPEN_PENDING_ADJUDICATION | RUN-A-009 |
| GIR-FD82-A010 | P2 | TM09 把单株采摘果实数误写成株数 | OPEN_PENDING_ADJUDICATION | RUN-A-010 |
| GIR-FD82-A011 | P2 | 交换统计并非仅在交换完成后增加 | OPEN_PENDING_ADJUDICATION | RUN-A-011 |
| GIR-FD82-A012 | P2 | 目录删除合同遗漏目标目录本身也被删除 | OPEN_PENDING_ADJUDICATION | RUN-A-012 |
| GIR-FD82-A013 | P2 | 翻译节编号不是严格数字校验且零号数字节被拒绝 | OPEN_PENDING_ADJUDICATION | RUN-A-013 |
| GIR-FD82-A014 | P2 | 地图事件集合缺失被净化为事件集合为空 | OPEN_PENDING_ADJUDICATION | RUN-A-014 |
| GIR-FD82-A015 | P2 | SV02 丢失无存档前提却固定预期新游戏 | OPEN_PENDING_ADJUDICATION | RUN-A-015,RUN-D-014 |
| GIR-FD82-A016 | P2 | 旧帧数迁移缺少实际帧率除数与零值回退 | OPEN_PENDING_ADJUDICATION | RUN-A-016 |
| GIR-FD82-A017 | P3 | 游戏时间锚点清空的审计路径指向不存在目录 | OPEN_PENDING_ADJUDICATION | RUN-A-017 |
| GIR-FD82-A018 | P3 | LZ08–LZ10 省略决定预期的非地图节身份 | OPEN_PENDING_ADJUDICATION | RUN-A-018 |
| GIR-FD82-A019 | P3 | 弃用附表末节仍把当前状态写为待复审 | OPEN_PENDING_ADJUDICATION | RUN-A-019 |
| GIR-FD82-A020 | P2 | 缺少性格身份到增减能力项的固定映射 | CONFIRMED_REQUIRED_REVISION | RUN-A-020,RUN-D-019 |
| GIR-FD82-A021 | P3 | 物种记录的其余默认值并非全为空 | CONFIRMED_REQUIRED_REVISION | RUN-A-021 |
| GIR-FD82-A022 | P2 | 创建仅两类随机来源未排除创建形态回调 | CONFIRMED_REQUIRED_REVISION | RUN-A-022,RUN-D-009 |
| GIR-FD82-A023 | P2 | 四槽容量未区分学习工具与直接整表写入 | CONFIRMED_REQUIRED_REVISION | RUN-A-023 |
| GIR-FD82-A024 | P3 | 重学配置的蛋招式表述应限定为已记录的最初招式 | CONFIRMED_REQUIRED_REVISION | RUN-A-024 |
| GIR-FD82-A025 | P3 | 按索引遗忘遗漏负索引从末尾计数的边界 | CONFIRMED_REQUIRED_REVISION | RUN-A-025 |
| GIR-FD82-B001 | P2 | 特殊调用前置失败时，最近招式清除范围写错 | CONFIRMED_REQUIRED_REVISION | RUN-B-001 |
| GIR-FD82-B002 | P2 | 无可战斗成员的队伍先失败于计数/业主校验，未到已声明消息 | CONFIRMED_REQUIRED_REVISION | RUN-B-002 |
| GIR-FD82-B003 | P2 | 战斗条款字面键被截短，设置路径也被过度概括 | CONFIRMED_REQUIRED_REVISION | RUN-B-003 |
| GIR-FD82-003 | P2 | 净化正文仍承载非必要源对象、槽位与类组织约束 | CONFIRMED_REQUIRED_REVISION | RUN-B-004,RUN-C-006 |
| GIR-FD82-B005 | P2 | CP、BC、CM 多个静态测试缺少决定结果的前提 | CONFIRMED_REQUIRED_REVISION | RUN-B-005 |
| GIR-FD82-B006 | P2 | 高等级不服从默认值误写为按世代配置 | CONFIRMED_REQUIRED_REVISION | RUN-B-006 |
| GIR-FD82-B007 | P2 | 沉重球缺少当前有效重量与单位的输入合同 | CONFIRMED_REQUIRED_REVISION | RUN-B-007 |
| GIR-FD82-B008 | P2 | 物品选择期误把效果处理器存在检查推广到全部家族 | CONFIRMED_REQUIRED_REVISION | RUN-B-008 |
| GIR-FD82-B009 | P2 | 对视合并把事件触发类型2误写为优先级 | CONFIRMED_REQUIRED_REVISION | RUN-B-009 |
| GIR-FD82-B010 | P2 | 冰一击必杀摘要未承接条款加载后的实际目标资格 | CONFIRMED_REQUIRED_REVISION | RUN-B-010,RUN-D-013 |
| GIR-FD82-B011 | P2 | 灭亡歌全灭早退向量错误保留已由濒死清除的畏缩 | CONFIRMED_REQUIRED_REVISION | RUN-B-011 |
| GIR-FD82-B012 | P2 | Shift把连斩连续计数误写为反击计数清除 | CONFIRMED_REQUIRED_REVISION | RUN-B-012 |
| GIR-FD82-B013 | P2 | 伙伴参战时满队捕获替换仍可对送盒旧成员错误还原持物 | CONFIRMED_REQUIRED_REVISION | RUN-B-013 |
| GIR-FD82-B014 | P2 | 伤害型换出把成功命中数误设为实际伤害前提 | CONFIRMED_REQUIRED_REVISION | RUN-B-014 |
| GIR-FD82-B015 | P2 | 离场来源的未来攻击会先清他者指向原席位的交叉状态 | CONFIRMED_REQUIRED_REVISION | RUN-B-015 |
| GIR-FD82-B016 | P2 | 净化阶级附表把独立参数和次序退化为源名称解码 | OPEN_PENDING_ADJUDICATION | RUN-B-016 |
| GIR-FD82-B017 | P2 | HP平均从WP44移交后未进入任何实际执行合同 | OPEN_PENDING_ADJUDICATION | RUN-B-017 |
| GIR-FD82-B018 | P3 | 净化附表的分组计数与实际身份集合冲突 | OPEN_PENDING_ADJUDICATION | RUN-B-018,RUN-D-010 |
| GIR-FD82-C002 | P2 | 表达式开关“翻转后显示不变”缺少表达式独立于该开关的前提 | OPEN_PENDING_ADJUDICATION | RUN-C-002 |
| GIR-FD82-C003 | P2 | CE-M02 净化丢失数值和布尔子型，取消预期不再唯一 | OPEN_PENDING_ADJUDICATION | RUN-C-003 |
| GIR-FD82-C004 | P2 | 遭遇步数率 0 在反写后重编译变回默认值的语义损失未登记 | OPEN_PENDING_ADJUDICATION | RUN-C-004 |
| GIR-FD82-C005 | P2 | 遭遇编辑/编译后的注册数据与当前地图快照未在生效合同中分层 | OPEN_PENDING_ADJUDICATION | RUN-C-005 |
| GIR-FD82-C007 | P2 | 120 项战斗效果白名单的具体合同仍留在历史交付附件 | OPEN_PENDING_ADJUDICATION | RUN-C-007,RUN-D-016 |
| GIR-FD82-C008 | P2 | 完整调试菜单的 Use PC 入口没有规格或测试承接 | OPEN_PENDING_ADJUDICATION | RUN-C-008 |
| GIR-FD82-C009 | P2 | 寄养与遗迹石选人取消仍覆盖固定事件变量 | OPEN_PENDING_ADJUDICATION | RUN-C-009 |
| GIR-FD82-C010 | P2 | 示例队伍缺少固定物种顺序与逐物种招式映射 | OPEN_PENDING_ADJUDICATION | RUN-C-010 |
| GIR-FD82-C011 | P2 | 奇妙空间中防御/特防编辑的显示与生效方向未定义 | OPEN_PENDING_ADJUDICATION | RUN-C-011 |
| GIR-FD82-C012 | P2 | 战斗调试 Teach 绕过普通学招的 Shadow 拒绝门 | OPEN_PENDING_ADJUDICATION | RUN-C-012 |
| GIR-FD82-C013 | P2 | 只有一个玩家角色时并非只有提示：延后执行的退出分支会失败 | DISPUTED_LOADING_CONTEXT_PENDING_PEER | RUN-C-013 |
| GIR-FD82-C014 | P3 | 普通随机 EV 总额的上界是否可取未明确 | OPEN_PENDING_ADJUDICATION | RUN-C-014 |
| GIR-FD82-C015 | P3 | 战斗背景及底座名称输入的100字符上限未记录 | OPEN_PENDING_ADJUDICATION | RUN-C-015 |
| GIR-FD82-C016 | P2 | 指标反写路径只由非零形态驱动，基础记录保存不保证更新PBS | OPEN_PENDING_ADJUDICATION | RUN-C-016 |
| GIR-FD82-C017 | P2 | 物种招式选择器的默认招式预选错位未承接 | OPEN_PENDING_ADJUDICATION | RUN-C-017 |
| GIR-FD82-C018 | P2 | 字符串/进化子编辑确认原值会自匹配删项，字符串ESC也可到达 | OPEN_PENDING_ADJUDICATION | RUN-C-018 |
| GIR-FD82-C019 | P2 | 天气属性取消的结果取决于停在哪个输入阶段 | OPEN_PENDING_ADJUDICATION | RUN-C-019 |
| GIR-FD82-C020 | P2 | 共享文件列表缺目录/图形载入失败不都回落为空白 | OPEN_PENDING_ADJUDICATION | RUN-C-020 |
| GIR-FD82-C021 | P2 | 无询问复合子页返回会把未指定IV/EV归零，并可建立零宽地图尺寸 | OPEN_PENDING_ADJUDICATION | RUN-C-021 |
| GIR-FD82-C022 | P2 | 物种编辑读取旧进化字段名，保存可清空现有进化；参数转文本时点也被误述 | OPEN_PENDING_ADJUDICATION | RUN-C-022 |
| GIR-FD82-C023 | P2 | 空训练家个体槽尚未选物种时，打开招式选择会失败 | OPEN_PENDING_ADJUDICATION | RUN-C-023 |
| GIR-FD82-D002 | P2 | 独立读者问题 RUN-D-002: test-oracle contradiction | OPEN_PENDING_ADJUDICATION | RUN-D-002 |
| GIR-FD82-D003 | P2 | 独立读者问题 RUN-D-003: undefined numerical rounding | OPEN_PENDING_ADJUDICATION | RUN-D-003 |
| GIR-FD82-D004 | P2 | 独立读者问题 RUN-D-004: ambiguous input grammar | OPEN_PENDING_ADJUDICATION | RUN-D-004 |
| GIR-FD82-D005 | P2 | 独立读者问题 RUN-D-005: test precondition insufficient | OPEN_PENDING_ADJUDICATION | RUN-D-005 |
| GIR-FD82-D006 | P2 | 独立读者问题 RUN-D-006: test-oracle overgeneralization | OPEN_PENDING_ADJUDICATION | RUN-D-006 |
| GIR-FD82-D007 | P2 | 独立读者问题 RUN-D-007: test precondition insufficient | OPEN_PENDING_ADJUDICATION | RUN-D-007 |
| GIR-FD82-D008 | P2 | 独立读者问题 RUN-D-008: cross-spec invariant contradiction | OPEN_PENDING_ADJUDICATION | RUN-D-008 |
| GIR-FD82-D011 | P2 | 独立读者问题 RUN-D-011: parameter/condition contradiction | OPEN_PENDING_ADJUDICATION | RUN-D-011 |
| GIR-FD82-D012 | P2 | 独立读者问题 RUN-D-012: test-oracle arithmetic contradiction | OPEN_PENDING_ADJUDICATION | RUN-D-012 |
| GIR-FD82-D015 | P2 | 独立读者问题 RUN-D-015: fixed arithmetic contradicts initialization reachability | OPEN_PENDING_ADJUDICATION | RUN-D-015 |
| GIR-FD82-D017 | P2 | 独立读者问题 RUN-D-017: missing deterministic target-order data | OPEN_PENDING_ADJUDICATION | RUN-D-017 |
| GIR-FD82-D018 | P2 | 独立读者问题 RUN-D-018: source-dependent automatic reposition predicate | OPEN_PENDING_ADJUDICATION | RUN-D-018 |
| GIR-FD82-D020 | P2 | 独立读者问题 RUN-D-020: missing form-to-move behavioral data | OPEN_PENDING_ADJUDICATION | RUN-D-020 |
| GIR-FD82-D021 | P2 | 独立读者问题 RUN-D-021: quantitative party test fixtures lack decisive constraints | OPEN_PENDING_ADJUDICATION | RUN-D-021 |
| GIR-FD82-D022 | P2 | 独立读者问题 RUN-D-022: test dispatch discriminants omitted | OPEN_PENDING_ADJUDICATION | RUN-D-022 |
| GIR-FD82-D023 | P2 | 独立读者问题 RUN-D-023: display formula missing quantity multiplier | OPEN_PENDING_ADJUDICATION | RUN-D-023 |
| GIR-FD82-D024 | P2 | 独立读者问题 RUN-D-024: path resampling grid/count undefined or contradictory | OPEN_PENDING_ADJUDICATION | RUN-D-024 |
| GIR-FD82-D025 | P2 | 独立读者问题 RUN-D-025: contradictory variable ACTION transition | OPEN_PENDING_ADJUDICATION | RUN-D-025 |
| GIR-FD82-004 | P2 | 盒子成功交换后的暂持状态在同稿中相互矛盾 | OPEN_PENDING_SECOND_REVIEW | ROOT/intake |

本检查点汇集 91 条原始发现，归并为 87 个全局候选（含初始项与总审独立项）。计数随剩余批次推进；不据此推算工作包或规则覆盖率。

固定输入：项目 e1e01bb18d824931e54f182dd61af5a9f908ba85；参考 8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b。来源定位均为静态证据，运行观察和已证 demo 事件链仍为 0。
