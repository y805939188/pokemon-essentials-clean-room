# M08 第五轮全局独立审查

**M08 原静态语义审查及本次 GCV-E001 有界原稿比较均已完成，产物校验通过；`progress.json.complete=true`。** 能力缺口是审查结果，不等于未审材料。三项 P2 候选均保留 `candidate_pending_independent_counterevidence` / `unresolved`，本模块不自行签署最终必修。

固定 B5：`9366d9d17aaeac3b4414236468affa650fb3dd27`；正式子树 `d5a462b4c6f8b78c3264a25d6b5495230fa265e2`。固定 R：`8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`；tree `7589c800b61ba13a13040ed0d686979b80a84fd0`。参考根为 `/Users/dingshinn/Desktop/pokemon-framework-reference/reference/pokemon-essentials`，保持只读；身份沿父会话核定，未重复行政审计。

请求模型为 `gpt-6-astra / ultra / service_tier=default`，实际参数回显 **UNVERIFIED**。没有替换模型、创建子 agent 或调查额度、认证、私有会话、后端。

## 已完成的有限范围

- 全部 13 个 Move 文件、10 个 Battler 文件，以及 Effects、ActiveField、DamageState、AbilityEffects、ItemEffects，共 28 个指定主责文件、21,586 行均已全文逐段分析；每个现存效果定义、注册、复制、分支、默认值和必要异常均实质比较，未用代表性效果替代全集。
- 目录外的条款覆写、Shadow 战斗覆写及四个独立效果已补入。共登记 447 个招式效果/共享基础定义的有限范围；其中包含共用辅助规则，**不是 447 个独立产品功能**。别名、覆写、数据绑定和跨模块消费者只作为唯一规则的投影。
- WP43–WP50 所分配的 14 份正文、coverage、data，及 4 份测试文件中的全部 M08 范围，合计 **1,906 条段落、表行或向量**，均已有精确来源及比较结论。所有向量只作静态推导，未运行。
- 必要消费者包括天气/场地及回合末局部、入场/位置/危害、优先级与换逃保证、正常终局持物/能力、Mega 能力后置、调试退出、注册默认、捕获重量和主动 SITRUS 对照。完整 M07 阶段/命令/顺序/终局、M09 AI、M04 Shadow/个体生命周期不在本模块签署范围。

逐源的实际行范围、入口、字段、证据层级、whole-file `review_extent` 与剩余区间在 [reading-coverage.json](reading-coverage.json)。共享文件仍可保持 `partial`，其尚未审核的整文件区间明确属于其它责任域；没有把局部投影提升为外域全文通过。缺少引擎、序列化 demo 地图/事件和媒体不阻止本轮可得材料的静态审查，亦未被计作运行证据。

## 候选与反证状态

| ID | P 级 | 结论与边界 | 独立反证状态 |
| --- | --- | --- | --- |
| GR5-M08-001 | P2 | 原能力值四效果，以及 WP23 外委派的四个 Shadow 专属效果，缺少实际接收合同。原值/阶级、奇数舍入、对象和提交顺序必须分开；Shadow 定义存在不等于可选样本已启用。按同一委派根因合并。 | 母会话已独立确认原能力值四项及后补 Shadow 四项；采用其共享绕过条件、力量戏法恢复条件及 Shadow 参数纠正，不重复反证。 |
| GR5-M08-002 | P2 | 鸟嘴加热反灼在攻击者自身替身条件下，可于 HP/记录已提交后触发缺失招式查询方法的局部异常；目标替身不是本项前提。现有正常资格/一般异常条款未具名接收该输入。 | 母会话已独立确认原范围；规范整合仍由母会话裁决。不宣称进程崩溃或宿主必能继续。 |
| GR5-M08-003 | P2 | 合法但无实现的效果：变化招在整招门失败，伤害招继续普通合同。缺省/`nil` 归 `None`，**空字符串不在该保证内**。可选 SHADOWSHED 的 `RemoveAllScreens` 绑定为另一个真实数据投影；不能替换为不同的双侧清屏障定义。 | 母会话已独立确认原回退范围及可选 SHADOWSHED 投影；保留 nil/空字符串限定，不冒充默认 740 招式缺坏或运行可达。 |

每项完整前提、最小反例、正常/失败对照、反证实读范围、影响、拟修订、静态验收与排除声明见 [findings.json](findings.json)。母会话证据只读引用 `counterevidence/root-M08/resolution.json` 及其 `report.md:11–13` 后补裁决，外部推荐与本模块最终签署分开记录。ShadowHalf/ShadowEnd 的 false 参数控制动画，伤害登记仍为默认真；正损失会登记本轮受伤、本轮招式伤害，并可设置跨半标记。此纠正优先于保留的旧候选材料中相反表述，各 JSON 的 `effective_parent_corrections` 或发现后补裁决字段已接入。

精神香草的定身身份残留不另立必修：当前 WP50 §4 / HI10 已明确只清计数、保留身份。设施条款的自爆假返回、DAMP 跳过、同命默认逐目标门等亦有当前 WP54 接收，不重复立项。

## 数据、数学与当前补充

普通及特殊公式已按整数/浮点、round/floor/ceil、随机闭区间、上下界和实际短路对照。包括命中整数阈值、四倍率舍入、满 HP 耐受、HP 最小请求、原能力值读取、火海双递减、场地清除/默认恢复、每击与整招消费时点。

[数据证据](data-audit.json) 区分以下有限层次：

- 740 个默认招式的战斗参数/标志/效果绑定；67 个 NaturalGift 和 578 个 Fling 字段与附表逐项一致；9 份调用/控制名单完整常量及条件分支已读后对照。
- 267 个默认能力身份及 693 个默认物品身份/相关谓词标志投影。12 个 IconMail、67 个 Berry、18 个 TypeGem 的谓词含义与实际消费者核对；名称/描述、经济、孵化及完整编译不充当战斗规则证据。注册别名 STICK 无默认物品记录，保留为条件化注册行为，不立默认损坏缺陷。
- 18 个可选 Shadow 招式及其类型样本全文读过。ShadowRush 的说明文字不覆盖其 `None` 绑定；SHADOWSHED 与 `RemoveAllScreensAndSafeguard` 明确分离。未安装、编译或运行可选数据。
- WP48 的 148 个（族，能力）身份与 WP50 的 196 个（族，物品）身份，经原稿表、现行表和本轮源索引三方字面对照一致。**数量/身份匹配不是语义审核或执行证明。**

当前 U04 的相关实质补充已跟读并重新与源及现行正文核对；自然之恩和投掷的空持物失败及先写前缀不回滚保留。历史 PASS 不作本轮证据，R4 隔离执行不计本轮执行；GR3-M09-001 暂缓及 GR3-M02-003 NO_REQUIRED 均未重开。

## GCV-E001 有界原稿事实承接比较

本次只补 14 份固定 B5 `specs/` 原稿。先复核已有 actual-read 证据：此前 WP48/WP50 roster 核对仅证明身份/登记投影，WP44 旧锚点仅作导航，均没有被冒充为全行或全文原稿比较。935 行与已完成现行范围完全相同字节的内容按精确成对范围复用；其余 2919 行均实际阅读并作事实处置。全部 3854 行现已闭合，未因同名文件或现行已读跳过。

| 原稿 | 总行数 | 精确复用 | 本次实读差异 |
| --- | ---: | ---: | ---: |
| wp45-weather-terrain-side-and-position-effects.md | 265 | 92 | 173 |
| wp47-a-attributes-targeting-calling-data.md | 281 | 27 | 254 |
| wp47-a-move-attributes-targeting-and-calling.md | 214 | 83 | 131 |
| wp47-b-control-items-coverage-data.md | 172 | 58 | 114 |
| wp47-b-switching-control-and-item-changes.md | 238 | 84 | 154 |
| wp49-ability-phase-triggers.md | 427 | 115 | 312 |
| wp43-types-accuracy-and-damage.md | 241 | 100 | 141 |
| wp44-effect-coverage.md | 215 | 29 | 186 |
| wp44-statuses-stat-stages-and-immunities.md | 285 | 81 | 204 |
| wp46-damage-healing-coverage.md | 304 | 15 | 289 |
| wp46-damage-multihit-and-healing.md | 345 | 111 | 234 |
| wp48-ability-calculation-modifiers.md | 403 | 74 | 329 |
| wp50-held-item-effect-coverage.md | 245 | 12 | 233 |
| wp50-held-item-triggers-and-consumption.md | 219 | 54 | 165 |
| 合计 | 3854 | 935 | 2919 |

逐段/逐表行的前提、数值、提交顺序、异常、依赖、默认身份与类型映射均已比较。向量搬移逐条对应；源定位、实现登记方式、旧哈希和批准回填等行政沿革正确净化。WP48 的重量单位、自然之恩 U04 等现行补强不作为原稿事实遗失。原稿已涉及的既有委派缺口仍归 001 等既有发现。

2919 个差异行的互斥记账为：863 行已接收；1943 行混合行为接收与源/行政净化；98 行纯源或实现信息排除；7 行既有已确认缺口；7 行版式/空行；1 行历史或被替换表述。**这些是导航行数，包含版式，不是事实、能力或新覆盖计数。** 未发现新的正确事实遗失，未新增 004+ 候选。

[original-comparison.json](original-comparison.json) 记录每段处置、当前接收锚点、原稿→现行/既有来源组及其逆向对应；[reading-coverage.json](reading-coverage.json) 的 `original_specification_comparison` 精确区分本次实读与逐字节复用。双向图仅追加独立原稿比较层，原主责源 28 份/21,586 行、现行 18 份/1,906 条、852 条唯一规则记录及既有来源组全部保持。原稿行不新增能力，历史 PASS 不替代本次语义判断。

校验见 [original-comparison-validation.json](original-comparison-validation.json)：核对范围无重叠/无遗漏、原/现行哈希及复用字节、双向关系、现行组引用和既有审查核心未改变。此校验不读取或执行参考行为；本次没有因原稿比较扩大源审查。

## 交接与执行边界

[source-to-spec.json](source-to-spec.json) 和 [spec-to-source.json](spec-to-source.json) 提供双向条款/唯一规则索引；[shared-interfaces.json](shared-interfaces.json) 给出消费者及责任边界；[progress.json](progress.json) 保留完成度、外域精确剩余区间和反证交接。

可得且已分配的静态源、合同、附表及向量没有剩余未审项。下一责任是母会话的规范整合；原 001–003 与后补 Shadow 独立反证均沿已完成裁决，不重开相同范围。正式全局 Feature Matrix 由母会话整合本模块投影，本会话没有改共享产物。

参考、Ruby、游戏、编译器、反序列化、行为模型及行为向量执行次数均为 **0**。只运行只读文本辅助解析、模块证据整理和产物结构校验；没有修改正式规格、reference、历史证据、共享报告，没有提交、推送、update、安装工具或修改配置。所有写入限于分配的 M08 目录。

校验限定：六项 JSON 的 schema、必需字段、唯一身份、精确锚点行界、双向组引用、1906 条范围完成标记及零执行记录通过；见 [artifact-validation.json](artifact-validation.json)。该校验没有执行行为，也不以结构正确代替前述逐段语义审查。
