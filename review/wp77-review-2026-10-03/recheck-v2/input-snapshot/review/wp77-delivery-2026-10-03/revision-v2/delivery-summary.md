# WP77 首审修订 v2 交付摘要（首审 9 项：7 P2＋2 P3）

2026-10-03；规格提取方。依据 `review/wp77-review-2026-10-03/`（首审 **REQUIRES_REVISION：9 OPEN（7 P2＋2 P3）**；v2 修订提示）。**本轮只修 9 项同根问题**，完成送 v2 有界复审；通过后再由审查明确后续全局一致性/覆盖审查范围，本轮不进入 WP78/79/80。

- **主稿**：[wp77-demo-evidence-and-capability-coverage.md](../../../specs/demo/wp77-demo-evidence-and-capability-coverage.md)，v1 被审 `db304223`／29,990 → v2 当前 `40f21b99`／41,773（258 行；磁盘程序化实测）。**v2 证据覆盖附表**：[evidence-coverage-table.md](evidence-coverage-table.md) `95d38a6c`／7,628（四组 **5／3／5／3＝16 行**结构法实测；档位列实测①15 行、②11 行）。**v2 缺口表**：[gap-register.md](gap-register.md) `891793eb`／4,454（**12 条候选链 G01–G12，与主稿同组**）。两份 diff 分别相对首审冻结 v1（主稿 7 hunks、附表 1 hunks）、patch 精确重建（[diff-bindings.json](diff-bindings.json)、[revision-diffs/](revision-diffs/)）。
- **逐项回应**：[revision-response.md](revision-response.md)（9 项：v1 残留／回源／修订位置／静态对照；无新增编号）。
- **自检**：[checks.json](checks.json)——9 项验收向量（含固定算术：偏移 ≤0 → 夹到 1、> 上限 → 夹到上限；①15/②11 档位列复算；8 检查＋1 汇总口径）、16 场景唯一性与逐行复核（本轮修订 9 行：M02/M03/M04/M05/M07/M08/M11/M12/M16）、全文残留扫描、附表实测计数（16）、diff 重建、链接解析、来源完备声明、上游保护。
- **来源身份**：[source-identities.json](source-identities.json)——本轮**新增定点阅读 5 处**（Metadata 属性、StartGame、RegionMap 开关读取、DungeonParameters 回退、RandomDungeons 默认与生成入口）＋WP61/WP14 已批准合同行定点复核＋Gen 5–8 备份存在性核验（仅身份，未全文阅读）；开工登记基线复测一致。
- **修订主题速览**：**R01** Home 更正为失败回程/Teleport 家地点回退（非新游戏起点证据）——系统起始位置来自缺失的 System.rxdata，Home 已知、起始位置未知。**R02** 连接补 Route 8(69)↔Lappet(2) 直连；19 条规范化连接表逐项不重不漏。**R03** 区域地图分 6 条飞行记录与 5 个不同目的地（Essen＝18 普通＋6 飞行＋2 开关）；飞行—治疗点完全匹配更正为 4 个（Cedolan 7＠(47,11) ≠ map 009 的 8＠(17,11)）。**R04** 岛屿开关 51/52 的读取消费者已存在（未置位时隐藏信息/目的地）——继续待证的是置位/解锁事件。**R05** Dungeon 标记只启用生成；参数选择经区域（默认 none）/版本（默认 0）回退到默认参数（5×5）——cave/0 才选到 5×4 样本；cave 通道随机偏移开启、forest 省略未开启。**R06** 等级缩放补夹限：偏移后夹到 [1, 最大等级] 再赋级。**R07** 遭遇计数分槽位与不同标识（Safari 内区陆遇 12 条/11 种、水/钓 14 条/12 种；Tiall＝6 条 _1＋2 条无后缀）；Gen 备份仅身份登记。**R08** Default 通用 Intro 5 条、时段 Intro 3 条分开；注释 Poké Center 条目 3 个与 HealingSpot 字段 6 处分开。**R09** 计数口径统一（①15/②11；G01–G12 十二组；8 检查＋1 汇总；③④继续为 0，不为凑数字提升档位）。
- **场景**：M01–M16 保留共 16 行唯一；本轮修订 9 行、无新增/删除。
- **保持**：v1 交付材料、首审原件与快照字节未改；全部既有具名批准（WP01～WP76、B 整合收口）保持；reference 固定 `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`、Git 清洁；未创建任务／Agent、未发跨会话消息、未提交／推送；未运行游戏/编译器/生成器/反序列化/参考行为模拟器；不使用 WP79/WP80 占位文件。
- **状态**：**ReviewPending（首审修订 v2，待有界复审）**；作者状态 REVISED_PENDING_REVIEW——不自行关闭 9 项、不自行 Reviewed、不宣称通过；③已证事件链与④运行观察继续为 0。

## 停止点

9 项修订完成并备齐材料，停止送 WP77 v2 有界复审；通过后由审查明确后续全局一致性/覆盖审查所采用的范围；不自行宣布全项目完成或进入 WP78/79/80。
