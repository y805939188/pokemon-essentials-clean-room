# 已批准范围的独立全局复核

**REQUEST_CHANGES。** 已完成 **59／59 个工作包、75／75 份冻结主稿与附表、10／10 条跨模块检查链**。确认 **16 项P2问题，影响18包**；其余41包在本次已批准范围内为PASS_SCOPED。没有未审包或待核实的批准版本缺口。

本结论绑定2026-09-30交接白名单和不可变快照，reference commit为 `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`。旧通过结论保留其历史意义；本轮只要求修订有新证据支持的具体合同。最新闭合批准的WP62 v3纳入，头部ReviewPending不改变该受理事实。

**范围与方法**

- 七组均完成正文与附表全文阅读、批准范围／版本替代链核查和逐包判断。完整身份、受理报告、纳入条款和排除项见[scope-audit.json](/Users/dingshinn/Desktop/pokemon-completed-scope-review/scope-audit.json)。
- [package-review.md](/Users/dingshinn/Desktop/pokemon-completed-scope-review/package-review.md)逐包列结果；[cross-module-review.json](/Users/dingshinn/Desktop/pokemon-completed-scope-review/cross-module-review.json)记录46组“输入→读取／写入→消费者／结果”，不是仅链接或术语扫描。
- 本轮实际回读147个来源路径：52个全文、95个片段；另列313个文本检索／身份扫描路径，两类集合有重叠，不相加为行为审查覆盖量。高风险合同和全部确认反例独立回源；其余正确旧目录／向量明确继承独立证据。
- 全程静态。未运行游戏、参考Ruby／表达式、生成器、编译器、解释器、插件、网络或行为模拟器；未操作真实地图／存档／输入。自有工具只处理文本、身份、集合、差异和具名固定算术。

**确认问题（按影响性质排列；稳定编号不变）**

| 编号 | 受影响包 | 需要修正的行为合同 |
| --- | --- | --- |
| GR-014 | WP47-B | 投掷持物在每击反应中先自耗后，主要效果可在空持物处失败 |
| GR-006 | WP14 | 大网格奇数尺寸被写成自动调整，实际在不存在的写入入口失败 |
| GR-013 | WP41, WP42, WP58 | 参战标记写入与终战读取的不同下标口径未被交界合同记录 |
| GR-016 | WP19 | 正常设施创建可写单项255 EV，否定WP19的全写入者252上限保证 |
| GR-012 | WP60 | 潮湿覆盖物的整数干燥折半未进入规格 |
| GR-015 | WP52-A | AI主规格给旧会心表添加了不存在的必会心末档 |
| GR-010 | WP26 | 蛋入口无图鉴写入的保证漏掉创建形态复检 |
| GR-009 | WP24 | 训练家/拥有者语言来源被混同于游戏界面语言选择 |
| GR-011 | WP12, WP36 | 转向遭遇的标记未接回同次普通移动的抑制门 |
| GR-004 | WP12 | 非玩家角色被玩家阻挡的合同漏掉玩家through条件 |
| GR-005 | WP13 | 事件屏外更新合同遗漏成功更新后持续放行条件 |
| GR-007 | WP15 | 地图BGS名称变化触发的是BGM淡出 |
| GR-001 | WP04 | CSV 包围标记去除漏记末字段位置条件 |
| GR-002 | WP08 | 翻译导入未注明由首行数字决定数组/哈希形态及其失败 |
| GR-008 | WP20 | 最初招式记录的不重复保证被扩大到整表记录入口 |
| GR-003 | WP10 | 寄养迁移场景残留按旧输入跳过的相反结论 |

逐项最小输入、当前结果与参考结果的差异、完整文件哈希／字节／行号、调用链、首次失败前提交、历史关系、最小修订和正反验收见[findings.md](/Users/dingshinn/Desktop/pokemon-completed-scope-review/findings.md)及[findings.json](/Users/dingshinn/Desktop/pokemon-completed-scope-review/findings.json)。GR-011、GR-013分别合并跨包同根因；GR-016由已批准设施消费者反证上游全称保证。未把这些参考缺陷本身当作修代码任务。

**跨模块结果**

| 检查链 | 完成结果 |
| --- | --- |
| X1 配置/数据→消费者→保存恢复 | 配置、内容身份与保存时序已区分；GR-001/002涉及文本输入消费，GR-009涉及语言来源，GR-015涉及旧配置共享常量。 |
| X2 个体生成/形态/所有者→缓存与持久状态 | 构造、派生缓存与持久写入已核；GR-008修记录去重范围，GR-013修位置/队伍下标，GR-016修EV上限的正常创建例外。 |
| X3 获得/交换/捕获→队伍/盒子→图鉴 | 获得、捕获、替换与图鉴接收者/门/先后已核；GR-010补蛋构造间接写图鉴。 |
| X4 背包/使用/商店/持有物 | 容器部分写入、商店回退、登记扣减和持物还原分层成立；GR-014补投掷中先自耗后的失败。 |
| X5 成长/学习/基础进化/繁殖/孵化 | 经验/EV/HP/学招、进化提交、寄养遗传和孵化时序已核；GR-003/008/009/016为相关有限修订。 |
| X6 战斗命令→执行→效果→回合末→终局 | 命令、执行、每击反应、回合末、正常终局与中止分层已核；GR-013/014为已证交界缺口。 |
| X7 AI预测与真实规则 | 预测候选、独立评分、近似/错误与真实效果保持区分；GR-015修旧表，不把AI改成实效。 |
| X8 时间/步数/随机→世界活动 | 时钟、帧等待、距离与普通步数不同来源已核；GR-011/012分别为转向抑制和整数水分反例。 |
| X9 设施/租借/回放→普通战斗与保存 | 报名原引用、单场按索引还原、租借、保存返回/异常、记录缺口及回放全局写入已核；GR-013/016收紧相关上游保证。 |
| X10 UI守卫与领域底层入口 | 菜单预检、确认、底层提交和查看写状态逐入口区分；没有把未完成完整UI包纳入。 |

**完整性与限制**

最终复测75份规格＋6份上下文＋3份权威材料全部匹配交接完整哈希和字节；5份交接文件未变。59包映射与安排集合一致。实际回读来源和文本扫描身份均匹配固定commit；315条相对文件链接存在，25个显式锚点存在。问题证据坐标和完整身份校验无错误。详见[integrity-checks.json](/Users/dingshinn/Desktop/pokemon-completed-scope-review/integrity-checks.json)、[source-checks.json](/Users/dingshinn/Desktop/pokemon-completed-scope-review/source-checks.json)、[completion-checks.json](/Users/dingshinn/Desktop/pokemon-completed-scope-review/completion-checks.json)和[final-checks.json](/Users/dingshinn/Desktop/pokemon-completed-scope-review/final-checks.json)。这些机械结果不证明行为正确。

有界目录的身份／数量检查、固定算术与行为判断分账；没有声称逐行重读全部参考源，也没有证明所有扩展组合、动态调用或跨版本回放等价。UO-002仍未证实可观察影响，单列为非必修；M-001及最新闭合C03已知维护不计入16项。

排除WP22／23／32／37／53／61、WP63–80及其子包；正在进行的WP22→23→32和WP68→69→70均跳过。Demo／媒体／宿主／插件及U01–U10保持。主库实时合法变化不与冻结快照作错误比较。

**交付与停止**

有限修订任务见[revision-prompt.md](/Users/dingshinn/Desktop/pokemon-completed-scope-review/revision-prompt.md)。本会话的所有写入都在独立输出目录；未修改主库规格、矩阵、manifest、主TSV、reference或历史审查原件，未创建任务／Agent、发消息、提交或推送。

本次阶段性复核不替代WP78／WP79／WP80，不批准整个项目进入实现阶段。报告及证据台账完成后停止，不代执行修订。
