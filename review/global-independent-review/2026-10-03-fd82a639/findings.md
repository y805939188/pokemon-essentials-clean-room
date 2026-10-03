# 本轮统一发现台账（进行中）

这是审查检查点，不是全量结论。各组原始报告保持原样；同根归并、优先级调整和第二审查者依据在 findings.json 中分列。未裁决候选不当作已确认缺陷。

| 全局 ID | 当前级别 | 标题 | 当前处置 | 原始 ID |
| --- | --- | --- | --- | --- |
| WP80-INTAKE-R01 | P2 | 必要输入语法全角化 | CONFIRMED_REQUIRED_REVISION | RUN-C-001 |
| WP80-INTAKE-R02 | P2 | 原输入批准与净化输出待审混淆 | OPEN_PENDING_FINAL_ADJUDICATION | ROOT/intake |
| WP80-INTAKE-C01 | P3 | 作者报告分域和测试族统计错误 | OPEN_PENDING_FINAL_ADJUDICATION | ROOT/intake |
| WP80-B02-R01 | P3 | 来源结构与取证统计进入净化正文 | PARTIALLY_ADDRESSED_RESIDUAL_OPEN | RUN-A-007 |
| WP80-B02-R02 | P3 | 批准身份和条款去向声明不准确 | PARTIALLY_ADDRESSED_RESIDUAL_OPEN | RUN-A-008 |
| GIR-FD82-001 | P3 | 全集范围声明与导航仍停留在旧交付阶段 | CONFIRMED_REQUIRED_REVISION | RUN-A-005,RUN-D-001 |
| GIR-FD82-002 | P2 | 旧不适用判定遗漏图片、计时器及地图覆盖层的可观察合同 | OPEN_PENDING_PEER | ROOT/intake |
| GIR-FD82-A001 | P2 | 奇数引号合并耗尽输入时，KL10 错误预期去除包围标记 | CONFIRMED_REQUIRED_REVISION | RUN-A-001 |
| GIR-FD82-A002 | P2 | PBS 新鲜度判定遗漏整数秒取整 | CONFIRMED_REQUIRED_REVISION | RUN-A-002 |
| GIR-FD82-A003 | P2 | 净化将 Scripts 的假值检查写成空列表检查 | CONFIRMED_REQUIRED_REVISION | RUN-A-003 |
| GIR-FD82-A004 | P2 | 插件自动发现遗漏路径子串规则及显式 Scripts 顺序 | CONFIRMED_REQUIRED_REVISION | RUN-A-004 |
| GIR-FD82-A006 | P2 | 把调试菜单的翻译导出语言选择误当作游戏语言切换 | CONFIRMED_REQUIRED_REVISION | RUN-A-006 |
| GIR-FD82-A009 | P3 | EP08 无条件要求更新链接但未提供 Link 前提 | CONFIRMED_REQUIRED_REVISION | RUN-A-009 |
| GIR-FD82-A010 | P2 | TM09 把单株采摘果实数误写成株数 | CONFIRMED_REQUIRED_REVISION | RUN-A-010 |
| GIR-FD82-A011 | P2 | 交换统计并非仅在交换完成后增加 | CONFIRMED_REQUIRED_REVISION | RUN-A-011 |
| GIR-FD82-A012 | P2 | 目录删除合同遗漏目标目录本身也被删除 | CONFIRMED_REQUIRED_REVISION | RUN-A-012 |
| GIR-FD82-A013 | P2 | 翻译节编号不是严格数字校验且零号数字节被拒绝 | CONFIRMED_REQUIRED_REVISION | RUN-A-013 |
| GIR-FD82-A014 | P2 | 地图事件集合缺失被净化为事件集合为空 | CONFIRMED_REQUIRED_REVISION | RUN-A-014 |
| GIR-FD82-A015 | P2 | SV02 丢失无存档前提却固定预期新游戏 | CONFIRMED_REQUIRED_REVISION | RUN-A-015,RUN-D-014 |
| GIR-FD82-A016 | P2 | 旧帧数迁移缺少实际帧率除数与零值回退 | CONFIRMED_REQUIRED_REVISION | RUN-A-016 |
| GIR-FD82-A017 | P3 | 游戏时间锚点清空的审计路径指向不存在目录 | CONFIRMED_REQUIRED_REVISION | RUN-A-017 |
| GIR-FD82-A018 | P3 | LZ08–LZ10 省略决定预期的非地图节身份 | CONFIRMED_REQUIRED_REVISION | RUN-A-018 |
| GIR-FD82-A019 | P3 | 弃用附表末节仍把当前状态写为待复审 | NOT_REQUIRED_HISTORICAL_CONTEXT | RUN-A-019 |
| GIR-FD82-A020 | P2 | 缺少性格身份到增减能力项的固定映射 | CONFIRMED_REQUIRED_REVISION | RUN-A-020,RUN-D-019 |
| GIR-FD82-A021 | P3 | 物种记录的其余默认值并非全为空 | CONFIRMED_REQUIRED_REVISION | RUN-A-021 |
| GIR-FD82-A022 | P2 | 创建仅两类随机来源未排除创建形态回调 | CONFIRMED_REQUIRED_REVISION | RUN-A-022,RUN-D-009 |
| GIR-FD82-A023 | P2 | 四槽容量未区分学习工具与直接整表写入 | CONFIRMED_REQUIRED_REVISION | RUN-A-023 |
| GIR-FD82-A024 | P3 | 重学配置的蛋招式表述应限定为已记录的最初招式 | CONFIRMED_REQUIRED_REVISION | RUN-A-024 |
| GIR-FD82-A025 | P3 | 按索引遗忘遗漏负索引从末尾计数的边界 | CONFIRMED_REQUIRED_REVISION | RUN-A-025 |
| GIR-FD82-A026 | P2 | 提交与战斗改招缺少形态到具名招式的固定对应 | CONFIRMED_REQUIRED_REVISION | RUN-A-026,RUN-D-020 |
| GIR-FD82-A027 | P2 | ROTOM 已掌握目标招时删除旧招的分支与空招式边界未登记 | CONFIRMED_REQUIRED_REVISION | RUN-A-027 |
| GIR-FD82-A028 | P2 | BANETTE 的 Mega 石身份被净化改写 | CONFIRMED_REQUIRED_REVISION | RUN-A-028 |
| GIR-FD82-A029 | P2 | 香类无效条件从友好度255误变为心阶段5 | CONFIRMED_REQUIRED_REVISION | RUN-A-029 |
| GIR-FD82-A030 | P2 | 可选 Shadow 表的 GROWLITHE 与 SNORUNT 首招被改写 | CONFIRMED_REQUIRED_REVISION | RUN-A-030 |
| GIR-FD82-A031 | P3 | SH06 的90点香下降缺少储存性格前提 | CONFIRMED_REQUIRED_REVISION | RUN-A-031 |
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
| GIR-FD82-B016 | P2 | 净化阶级附表把独立参数和次序退化为源名称解码 | CONFIRMED_REQUIRED_REVISION | RUN-B-016 |
| GIR-FD82-B017 | P2 | HP平均从WP44移交后未进入任何实际执行合同 | CONFIRMED_REQUIRED_REVISION | RUN-B-017 |
| GIR-FD82-B018 | P3 | 净化附表的分组计数与实际身份集合冲突 | CONFIRMED_REQUIRED_REVISION | RUN-B-018,RUN-D-010 |
| GIR-FD82-B019 | P2 | 重定向资格误用原始目标数据，遗漏幽灵诅咒的动态目标 | CONFIRMED_REQUIRED_REVISION | RUN-B-019 |
| GIR-FD82-B020 | P2 | AI 道具资格扫描遗漏混入选招道具时整段选择失败的合同 | OPEN_PENDING_ADJUDICATION | RUN-B-020 |
| GIR-FD82-B021 | P2 | AI 回合末近似漏写逐项最低量，改变低总 HP 换人意愿 | OPEN_PENDING_ADJUDICATION | RUN-B-021 |
| GIR-FD82-C002 | P2 | 表达式开关“翻转后显示不变”缺少表达式独立于该开关的前提 | CONFIRMED_REQUIRED_REVISION | RUN-C-002 |
| GIR-FD82-C003 | P2 | CE-M02 净化丢失数值和布尔子型，取消预期不再唯一 | CONFIRMED_REQUIRED_REVISION | RUN-C-003 |
| GIR-FD82-C004 | P2 | 遭遇步数率 0 在反写后重编译变回默认值的语义损失未登记 | CONFIRMED_REQUIRED_REVISION | RUN-C-004 |
| GIR-FD82-C005 | P2 | 遭遇编辑/编译后的注册数据与当前地图快照未在生效合同中分层 | CONFIRMED_REQUIRED_REVISION | RUN-C-005 |
| GIR-FD82-C007 | P2 | 120 项战斗效果白名单的具体合同仍留在历史交付附件 | CONFIRMED_REQUIRED_REVISION | RUN-C-007,RUN-D-016 |
| GIR-FD82-C008 | P2 | 完整调试菜单的 Use PC 入口没有规格或测试承接 | CONFIRMED_REQUIRED_REVISION | RUN-C-008 |
| GIR-FD82-C009 | P2 | 寄养与遗迹石选人取消仍覆盖固定事件变量 | CONFIRMED_REQUIRED_REVISION | RUN-C-009 |
| GIR-FD82-C010 | P2 | 示例队伍缺少固定物种顺序与逐物种招式映射 | CONFIRMED_REQUIRED_REVISION | RUN-C-010 |
| GIR-FD82-C011 | P2 | 奇妙空间中防御/特防编辑的显示与生效方向未定义 | CONFIRMED_REQUIRED_REVISION | RUN-C-011 |
| GIR-FD82-C012 | P2 | 战斗调试 Teach 绕过普通学招的 Shadow 拒绝门 | CONFIRMED_REQUIRED_REVISION | RUN-C-012 |
| GIR-FD82-C013 | P2 | 只有一个玩家角色时并非只有提示：延后执行的退出分支会失败 | CONFIRMED_REQUIRED_REVISION | RUN-C-013 |
| GIR-FD82-C014 | P2 | 普通随机 EV 总额的上界是否可取未明确 | CONFIRMED_REQUIRED_REVISION | RUN-C-014 |
| GIR-FD82-C015 | P3 | 战斗背景及底座名称输入的100字符上限未记录 | CONFIRMED_REQUIRED_REVISION | RUN-C-015 |
| GIR-FD82-C016 | P2 | 指标反写路径只由非零形态驱动，基础记录保存不保证更新PBS | CONFIRMED_REQUIRED_REVISION | RUN-C-016 |
| GIR-FD82-C017 | P2 | 物种招式选择器的默认招式预选错位未承接 | CONFIRMED_REQUIRED_REVISION | RUN-C-017 |
| GIR-FD82-C018 | P2 | 字符串/进化子编辑确认原值会自匹配删项，字符串ESC也可到达 | CONFIRMED_REQUIRED_REVISION | RUN-C-018 |
| GIR-FD82-C019 | P2 | 天气属性取消的结果取决于停在哪个输入阶段 | CONFIRMED_REQUIRED_REVISION | RUN-C-019 |
| GIR-FD82-C020 | P2 | 共享文件列表缺目录/图形载入失败不都回落为空白 | CONFIRMED_REQUIRED_REVISION | RUN-C-020 |
| GIR-FD82-C021 | P2 | 无询问复合子页返回会把未指定IV/EV归零，并可建立零宽地图尺寸 | CONFIRMED_REQUIRED_REVISION | RUN-C-021 |
| GIR-FD82-C022 | P2 | 物种编辑读取旧进化字段名，保存可清空现有进化；参数转文本时点也被误述 | CONFIRMED_REQUIRED_REVISION | RUN-C-022 |
| GIR-FD82-C023 | P2 | 空训练家个体槽尚未选物种时，打开招式选择会失败 | CONFIRMED_REQUIRED_REVISION | RUN-C-023 |
| GIR-FD82-C024 | P2 | 净化稿把提取脚本与合并脚本的活动入口写反 | OPEN_PENDING_ADJUDICATION | RUN-C-024 |
| GIR-FD82-C025 | P2 | 第60号单元槽在复制、清空和格式转换中的差异未承接 | OPEN_PENDING_ADJUDICATION | RUN-C-025 |
| GIR-FD82-C026 | P2 | 动画渐变被概括成普通插值，漏掉坐标符号、零时长和重叠旧值 | OPEN_PENDING_ADJUDICATION | RUN-C-026 |
| GIR-FD82-C027 | P2 | 分页与断句组合可丢失原第5至9行，规格未记录 | OPEN_PENDING_ADJUDICATION | RUN-C-027 |
| GIR-FD82-C028 | P2 | 电话占位符被误述为类型与金钱 | OPEN_PENDING_ADJUDICATION | RUN-C-028 |
| GIR-FD82-C029 | P2 | 扭曲世界形态规则丢失限定物种与道具身份 | OPEN_PENDING_ADJUDICATION | RUN-C-029 |
| GIR-FD82-C030 | P2 | 训练家转换产物未说明原页面条件会继续限制所有基础页 | OPEN_PENDING_ADJUDICATION | RUN-C-030 |
| GIR-FD82-C031 | P2 | 组织器的保存询问初始选中Yes，被写成默认Cancel | OPEN_PENDING_ADJUDICATION | RUN-C-031 |
| GIR-FD82-C032 | P2 | 定义路径的坐标基准与控制点钳制未定义 | OPEN_PENDING_ADJUDICATION | RUN-C-032 |
| GIR-FD82-C033 | P2 | ALT透明像素命中不考虑旋转，规格未保留这个限制 | OPEN_PENDING_ADJUDICATION | RUN-C-033 |
| GIR-FD82-C034 | P2 | 旧战斗转换把参数数列为固定值，未承接省略可选尾参 | OPEN_PENDING_ADJUDICATION | RUN-C-034 |
| GIR-FD82-C035 | P2 | 骑行取消条件被双重否定写成相反方向 | OPEN_PENDING_ADJUDICATION | RUN-C-035 |
| GIR-FD82-C036 | P2 | 非玩家水域与冰面规则遗漏双向调用的另一端 | OPEN_PENDING_ADJUDICATION | RUN-C-036 |
| GIR-FD82-C037 | P2 | 普通事件传送保留游泳，被泛化为显式传送默认取消 | OPEN_PENDING_ADJUDICATION | RUN-C-037 |
| GIR-FD82-C038 | P2 | IM01的空操作区间误含有治疗效果的314 | OPEN_PENDING_ADJUDICATION | RUN-C-038,RUN-D-002 |
| GIR-FD82-C039 | P2 | 循环末尾的文本预读可在显示消息前失败 | OPEN_PENDING_ADJUDICATION | RUN-C-039 |
| GIR-FD82-C040 | P2 | 脚本条件得到nil时并不会进入Else | OPEN_PENDING_ADJUDICATION | RUN-C-040 |
| GIR-FD82-C041 | P2 | 两类等待命令缺少20单位每秒的参数换算 | OPEN_PENDING_ADJUDICATION | RUN-C-041 |
| GIR-FD82-C042 | P2 | 251被写成按名称停止指定音效 | OPEN_PENDING_ADJUDICATION | RUN-C-042 |
| GIR-FD82-C043 | P2 | 额外连接数不保证新增同数目的不同连接 | OPEN_PENDING_ADJUDICATION | RUN-C-043 |
| GIR-FD82-C044 | P2 | 空可访问节点集会在房间退化之前失败 | OPEN_PENDING_ADJUDICATION | RUN-C-044 |
| GIR-FD82-C045 | P2 | 摆放候选房间与最终地面不等价：退化不登记，重绘不清旧记录 | OPEN_PENDING_ADJUDICATION | RUN-C-045 |
| GIR-FD82-C046 | P2 | 摆放间隔需明确为切比雪夫距离而非两个方向都至少2 | OPEN_PENDING_ADJUDICATION | RUN-C-046 |
| GIR-FD82-C047 | P2 | 装饰密度0可编译通过并在启用对应装饰时除零 | OPEN_PENDING_ADJUDICATION | RUN-C-047 |
| GIR-FD82-C048 | P2 | 地牢图样、数量和图块映射仍不足以独立形成测试判据 | OPEN_PENDING_ADJUDICATION | RUN-C-048,RUN-D-003 |
| GIR-FD82-C049 | P2 | 对角移动和NPC趋避策略仍指回来源而无独立行为合同 | OPEN_PENDING_ADJUDICATION | RUN-C-049 |
| GIR-FD82-C050 | P2 | 冰滑在冰面前方受阻时即清状态，退出条件被漏写 | OPEN_PENDING_ADJUDICATION | RUN-C-050 |
| GIR-FD82-C051 | P2 | 门口跟随者编排有实际转换调用，却没有独立效果合同 | OPEN_PENDING_ADJUDICATION | RUN-C-051 |
| GIR-FD82-C052 | P2 | 边缘跨图只查目标全阻挡，未承接其与普通双向通行的差异 | OPEN_PENDING_ADJUDICATION | RUN-C-052 |
| GIR-FD82-C053 | P2 | 连续选择组的合并和选项变换未被命令矩阵承接 | OPEN_PENDING_ADJUDICATION | RUN-C-053 |
| GIR-FD82-C054 | P2 | 换向先转身与75毫秒门遗漏上一帧已移动的直接移动分支 | OPEN_PENDING_ADJUDICATION | RUN-C-054 |
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
| GIR-FD82-D021 | P2 | 独立读者问题 RUN-D-021: quantitative party test fixtures lack decisive constraints | OPEN_PENDING_ADJUDICATION | RUN-D-021 |
| GIR-FD82-D022 | P2 | 独立读者问题 RUN-D-022: test dispatch discriminants omitted | OPEN_PENDING_ADJUDICATION | RUN-D-022 |
| GIR-FD82-D023 | P2 | 独立读者问题 RUN-D-023: display formula missing quantity multiplier | OPEN_PENDING_ADJUDICATION | RUN-D-023 |
| GIR-FD82-D024 | P2 | 独立读者问题 RUN-D-024: path resampling grid/count undefined or contradictory | OPEN_PENDING_ADJUDICATION | RUN-D-024 |
| GIR-FD82-D025 | P2 | 独立读者问题 RUN-D-025: contradictory variable ACTION transition | CONFIRMED_REQUIRED_REVISION | RUN-D-025 |
| GIR-FD82-004 | P2 | 盒子成功交换后的暂持状态在同稿中相互矛盾 | OPEN_PENDING_SECOND_REVIEW | ROOT/intake |

本检查点汇集 131 条原始发现，归并为 124 个全局候选（含初始项与总审独立项）。计数随剩余批次推进；不据此推算工作包或规则覆盖率。

固定输入：项目 e1e01bb18d824931e54f182dd61af5a9f908ba85；参考 8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b。来源定位均为静态证据，运行观察和已证 demo 事件链仍为 0。
