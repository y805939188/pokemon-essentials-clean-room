# WP04–WP07 v3 复审：三包通过，WP06 统计附表待修

日期：2026-09-19。Reference/Audit 侧独立 reviewer。R = `reference/pokemon-essentials/`；S = `R/Data/Scripts/`。本报告为内部审查材料，不是 WP80 sanitized 产物。

**批次结论：PARTIAL。WP04、WP05、WP07 为 PASS_SCOPED；WP06 为 REQUEST_CHANGES，仅原 WP06-R03 的新增附表内容尚未闭合。**

上轮六个未关闭编号中的五项已关闭。WP06 的 74 字段集合覆盖也已通过，剩余问题是局部数值含义与证据定位；不再要求重建统计目录或重审其他三个包。

## 1. 实际对象与基线

工作区 `/Users/dingshinn/Desktop/pokemon-framework-reference/`。参考 HEAD 实测仍为 `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`，describe 为 `v21.1-23-g8c5911e4`。

| 对象 | SHA-256 | 字节数 |
| --- | --- | ---: |
| WP04 v3 | `0df88787a53863e2ee6d521c45e0b5c9e297d18670b4e263bdb084aaf1d37028` | 22748 |
| WP05 v3 | `aae49934ce2f557af8d49cf6d8822fd5670e9162f592359d78331abe818ab46c` | 18157 |
| WP06 v3 | `09e01e07f48bda95f7f0b1644aa0d13482d004c7f0dd9d392b43dbee99a5ff1f` | 19824 |
| WP06 统计目录附表 | `0ea55ff18aedfef58dbe47df3da226b4fb89fb66fead78760200effb518b0882` | 13543 |
| WP07 v3 | `101577efd4304b59cbbd3cf20bad24766db318579799337ba206024805837727` | 17049 |
| manifest | `344cb4f210433cd55783a31a9ea29191f49798b0fff4ceeb0b9574d9d1c58b30` | 13669 |

规格均位于 `specs/kernel/`；下文“附表”指 `wp06-stats-directory.md@0ea55ff1`，“主文档”指 `wp06-time-random-steps-stats.md@09e01e07`。

固定输入 32 项；当前 manifest **28 项完整哈希和字节数全部匹配**。上轮报告及提示词原件与其最终检查记录一致。WP01–WP03、矩阵和原计划未修改。四包实际差异与新增附表已固定，见 [input-manifest.json](/Users/dingshinn/Desktop/pokemon-framework-reference/review/wp04-wp07-recheck-v3-2026-09-19/input-manifest.json)、[changes-from-v2.diff](/Users/dingshinn/Desktop/pokemon-framework-reference/review/wp04-wp07-recheck-v3-2026-09-19/changes-from-v2.diff)。

## 2. 已执行检查与限制

- 逐项对照上轮六项与实际修改；重读普通/重复属性、新身份登记、BerryPlant/Metadata 引用、Scripts 缺省、trigger 首参、HTTP 返回及插件异常分支。
- 独立提取 GameStats 的声明集合并与附表首列核对：**74 个声明、74 个不同条目，无遗漏、额外项或重复**。对各字段建立 `$stats.<字段>` 文字引用索引，并对新增附表中的计量、更新定位及未证分类追踪实际消费者。机械覆盖不等于全部运行语义验证。见 [stats-field-check.json](/Users/dingshinn/Desktop/pokemon-framework-reference/review/wp04-wp07-recheck-v3-2026-09-19/stats-field-check.json)。
- 上轮 79 个源文件哈希未变；加上本轮统计引用所在文件，共 109 项 Git blob 与固定提交一致。此项包含索引完整性检查，不表示全文语义重读 109 文件。Git 只读查询退出码均为 0，普通状态为空，ignored 仍有 `.DS_Store`、`PBS/.DS_Store`。见 [source-checks.json](/Users/dingshinn/Desktop/pokemon-framework-reference/review/wp04-wp07-recheck-v3-2026-09-19/source-checks.json)。
- **未运行游戏、Ruby、编译器、参考表达式、插件或网络请求**。下列向量均是静态推导，不是运行通过。只写本轮 review 目录，未改提取方文档或旧报告。

## 3. 原问题处置与逐包结论

| 编号 | 处置 | 依据 |
| --- | --- | --- |
| WP04-R02 | 关闭 | 属性重复/未知属性、新身份与未知引用分别说明；错误的 BerryPlant Item 枚举及 Trainer→Metadata 链已撤回并按实际引用拆分，补有静态场景。 |
| WP05-R02 | 关闭 | Scripts 默认数组、自动收集、省略行与解析后值的差别已写清；空脚本条目与整个产物为空分开。 |
| WP05-R03 | 关闭 | trigger 首参已改为归一化后的键，不保证 Symbol，并补字符串触发场景。 |
| WP06-R03 | 部分关闭 | 74 字段目录、Safari/BugContest 与 waterfalls_descended 的覆盖通过；附表的计量与个别来源断言需 §4 修正。 |
| WP07-R01 | 关闭 | HTTP 汇总表与基础/便利入口一致，不再把请求异常说成可由空结果区分。 |
| WP07-R03 | 关闭 | Reset/SystemExit 限定于具体包装/编译分支，插件执行的捕获路径已区分。 |

更早关闭的 WP04-R01/R03、WP05-R01、WP06-R01/R02、WP07-R02、BATCH-C01/C02 继续关闭。本轮没有与旧审查无关的新范围要求。

**限定通过范围**：

- **WP04**：固定基线的 PBS 输入发现、已述解析/校验及依赖边界、触发、写回/反写和失败副作用的静态规格范围。各领域字段语义、完整编辑器/事件转换流程及组合兼容继续按既有前向引用处理。
- **WP05**：通知/菜单机制、插件元数据/依赖与发现—编译—产物消费的静态约束范围；不代表真实插件组合运行有效。
- **WP07**：已述文件/HTTP 包装与诊断分层、失败前提的静态规格范围；不代表宿主协议/归档行为、外部服务及所有业务恢复已验证。

## 4. 唯一未关闭编号：WP06-R03 [P2]

本项从“目录缺失”收敛为下列有定位的附表修正。主文档中的统计摘要、未决分类和交付说明应同步，其他正确条目保留。

### 4.1 计量类别与单位

**位置**：附表第 48、96–97 行。

| 字段 | 当前附表 | 实际行为与证据 |
| --- | --- | --- |
| max_yield_berry_plants | “最大值／单株最高产量更新” | 是符合产量条件的**采摘次数计数器**。`S/012_Overworld/006_Overworld_BerryPlants.rb:437–454` 中，确认且背包允许添加后，采摘量达到或超过该树果的 maximum_yield 时加 1；不保存最大产量。 |
| mart_items_bought | 单位“次数” | 累计购买的**物品数量**。普通商店 `S/016_UI/020_UI_PokeMart.rb:636–644`、BP 商店 `021_UI_BattlePointShop.rb:484–492` 在完整购买成功后增加 quantity，不是每笔交易固定加 1。 |
| premier_balls_earned | 单位“次数” | 累计实际获得的**纪念球个数**。普通商店 647–661 行增加实际添加的球数，或在单球奖励分支增加 1；不是奖励事件次数。 |

**影响**：会产生错误的统计数值和测试预期；这是本包字段目录的事实问题，不是 WP60/WP29 后续玩法细节。

**最小修订与静态验收**：

- 将 max_yield_berry_plants 改为达到/超过最高产量条件的采摘次数。以原计数 2、配置 maximum_yield=10、确认采摘且背包可接收为前提：qty=8 后仍为 2；qty=10 后为 3；qty=12 后也为 3。三例独立起始，不能写成最大值变成 10/12。取消或容量不足在这些累加之前返回。
- 一笔成功购买 3 件物品，mart_items_bought 增加 3；一次实际添加 2 个纪念球，premier_balls_earned 增加 2。改用“件／个的累计数量”等无歧义单位，不展开全部商店规则。

### 4.2 名人堂时间：赋值方法与 UI 读取必须分开

**位置**：附表第 111、114 行；主文档第 92–93、183 行的静态/待证分组。

附表把 `set_time_to_hall_of_fame` 的写入定位到 `UI_HallOfFame.rb`，但该 UI 的第 246 行是**读取** `time_to_enter_hall_of_fame`。实际赋值方法在 `S/004_Game classes/012_Game_Stats.rb:169–170`：当前值为 0 时赋当前 play_time。

当前固定脚本检索能找到该方法定义和初始化注释，但未定位到其调用；初始化注释第 139 行称由名人堂事件设置。相邻 `set_time_to_badge` 也有可读赋值方法（165–166），其事件调用同样待证。

**最小修订**：写入证据改指 GameStats；UI 单列为展示读取。对这两个方法型字段分别保留“赋值机制静态已知”和“实际触发/事件调用未证”，不要用“有方法定义”冒充“调用链已确认”，也不要因为调用事件缺失而把赋值方法本身归为未知。同步主文档“仅这 10 个字段有事件限制，其余均明确”的绝对分组；不以固定数量作为分类目标。

**静态验收**：能在表中分别找到方法定义、赋值条件、已定位调用者或未定位说明、UI 读取者。无需恢复缺失事件，也不要求运行名人堂画面。

### 4.3 BP 获得统计的未知原因不能写成已经确认的缺失事件

**位置**：附表第 102、139 行；主文档第 93 行。

附表称 battle_points_won 的写入来自“缺失设施发奖事件”，并将整组归为“代码注释声明更新方式”。实际当前可定位内容为 `012_Game_Stats.rb:49,131` 的声明与初始化；这两处没有所述设施发奖事件注释。本轮按字段名检索固定脚本/PBS/文档未找到该写入依据。

**最小修订及验收**：若有其他真实证据，补其定位；否则改为“当前未定位到更新入口，写入来源待查”，将“可能位于缺失事件”标为推断/待证，交 WP55/WP77 等适用范围核实。不得从搜索未命中推出一定由某缺失事件写入，也不宣称没有此功能。它可以保持未决，不要求为关闭 WP06 虚构答案。

## 5. 状态登记与后续

提取方可根据本报告做管理性回填：

| 包/Feature | 可登记范围 |
| --- | --- |
| WP04；F02-02 的 WP04 子范围 | Reviewed（§3 所述静态范围）；编辑器/转换全集及其他未决不随之升级 |
| WP05；F01-03/F01-04 的 WP05 子范围 | Reviewed（通知/菜单与插件机制范围）；业务语义及真实组合继续原状态 |
| WP07；F01-06/F01-07 的 WP07 子范围 | Reviewed（已述通用 I/O/诊断范围）；宿主、外部服务和业务失败范围继续原状态 |
| WP06 与统计目录 | 继续待修订复审，不整包升级 Reviewed；字段集合覆盖通过可记录，但不替代语义修正 |

保留本轮被审哈希与状态回填后新哈希，只记管理性差异，不改旧报告。WP01–WP03 的限定 Reviewed 不变。U01–U10 保持各自证据边界；通过不等于运行通过或 WP80 清理通过。

下一次只需处理 WP06-R03 的上述局部内容与三包状态登记，保留 74 字段的完整集合，提交实际 diff 和静态场景后复审。**WP08 的声明依赖 WP03/WP04 已通过，具备单独启动条件；WP09/WP10 涉及 WP06，不能把整批的完成前置都算作已闭合。** 本轮提供的执行提示词聚焦完成当前修订；未自行启动新包。

材料：[修订与状态回填提示词](/Users/dingshinn/Desktop/pokemon-framework-reference/review/wp04-wp07-recheck-v3-2026-09-19/revision-prompt.md)、[最终一致性与交付哈希](/Users/dingshinn/Desktop/pokemon-framework-reference/review/wp04-wp07-recheck-v3-2026-09-19/final-checks.json)。本轮到报告与提示词交付为止。
