# WP77修订v2：关闭首审9项再申请后续阶段

工作目录 `/Users/dingshinn/Desktop/pokemon-framework-reference`。本轮WP77首审REQUIRES_REVISION：WP77-R01～R09共9项，7项P2＋2项P3。先完整读取本目录report.md/findings.json/independent-counts.json/literal-reference-checks.json/source-read-log.json/input-manifest.json及AGENTS.md、extraction-plan §2.2。不因材料缺失把可静态确认的事实继续放成未知。

## 修订范围

仅修改 `specs/demo/wp77-demo-evidence-and-capability-coverage.md`；新增 `review/wp77-delivery-2026-10-03/revision-v2/`。旧首版表、缺口表、摘要、自检、来源身份、末检以及本review/快照保持原字节。既有WP01～WP76及B整合的行为产物/批准保持，不重开或改写。

1. R01：Home是回程家地点回退，不能作为新游戏起始地图证据。起始位置来自当前缺失的系统数据，Home值、初始金钱、PC存放、系统起始位置分开。
2. R02：连接图补上69↔2直连。用19条具名记录核验完整映射，不只校验端点ID存在。
3. R03：区域地图区分6条飞行点记录与5个不同目的地；Essen26条分组可为18普通＋6飞行＋2开关。飞行与HealingSpot匹配4个，不是2个，按报告列出的坐标核对。
4. R04：开关51/52的读取消费者已经存在于区域地图查询；未知的是解锁/写入事件，不能把两者都写成消费者未见。沿WP63和实际读取条件分开普通图/墙图。
5. R05：Dungeon字段只启用生成；cave/forest选择来自区域/版本状态，当前未证写入事件。补默认参数回退、tileset依赖与两套ShiftCorridors差异。
6. R06：等级缩放先计算偏移，再夹到1和成长上限，随后重算能力/重置招式。补上下界固定向量。
7. R07：Safari内陆遇12条/11种、水钓14条/12种；Tiall8条为6条_1后缀＋2条无后缀。数量按槽位/不同标识分开；当前PBS根集与四个Gen备份同名表的选择边界明确，未读备份不冒充全文。
8. R08：Default通用Intro5条，时段早午晚各1共3条；Poké Center注释条目3个，HealingSpot字段6处，不能混成实际游戏设施总数。注释标题与Name字段分清。
9. R09：证据标签、候选链和跨表核对建立稳定行ID，按最终表复算。冻结稿实际①15/②11；主稿12条缺口链与缺口表11组不一致；跨表实际8检查＋1汇总。不能凑数字提升证据档位；③已证事件与④运行保持0。

逐项同步正文、M场景、覆盖表、缺口表、摘要、自检和真实来源阅读范围。原正确配置和静态消费事实保持，修订不能只改标题数字。缺事件不意味着没有能力，配置/注释/入口存在不意味着已部署或可达；不从外部版本补未知数据，不运行或反序列化reference。

## 交付与登记

新增逐项回应、修订版证据表/缺口表、摘要、自检、来源完整身份及严格diff。以本review/input-snapshot中的首版为差异基线，固定输入/定点阅读/仅身份核验分别记账。当前登记第131轮、TSV v106，完整身份见本轮冻结输入；续接轮次/版本以开工实测为准（通常132/v107）。只更新F18-06/F18-07的WP77修订待审子范围及必要manifest/TSV，保持WP01已通过基线与demo Provisional/Partial边界，历史只追加。末检独立保存避免自哈希。

完成后停止送9项有界复审，不自行CLOSED/Reviewed，不进入WP78/79/80。保持reference HEAD 8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b且只读；不运行游戏/生成器/编译器/反序列化/参考行为模拟器，不写新框架，不创建聊天/Agent、不跨会话发消息、不提交推送。
