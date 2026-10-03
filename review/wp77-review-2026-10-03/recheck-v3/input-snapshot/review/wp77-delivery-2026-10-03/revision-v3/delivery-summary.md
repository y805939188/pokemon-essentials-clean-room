# WP77 首审修订 v3 交付摘要（复审残留 2 项 P2＋本轮补充 1 项 P3，共 3 项）

2026-10-03；规格提取方。依据 `review/wp77-review-2026-10-03/recheck-v2/`（v2 复审：**7 项 CLOSED，R03／R07 仍 OPEN，新增 N01（P3）**；v3 收尾修订提示）。**本轮只修 3 项**，完成送 v3 短复审；通过后接续 WP78／79／80 的审查安排，本轮不自行进入。

- **主稿**：[wp77-demo-evidence-and-capability-coverage.md](../../../specs/demo/wp77-demo-evidence-and-capability-coverage.md)，v2 被复审 `40f21b99`／41,773 → v3 当前 `6c961566`／43,396（259 行；磁盘程序化实测）。**附表与缺口表本轮无变更**——沿用 v2 已核身份：附表 `95d38a6c`／7,628（四组 5／3／5／3＝16 行；档位列①15 行、②11 行）、缺口表 `891793eb`／4,454（12 条候选链 G01–G12，与主稿同组），不为增加 diff 制造变更。一份 diff 相对复审冻结 v2（主稿 **4 hunks**）、patch 精确重建（[diff-bindings.json](diff-bindings.json)、[revision-diffs/](revision-diffs/)）。
- **逐项回应**：[revision-response.md](revision-response.md)（3 项：v2 已接受部分／残留／回源／修订位置／静态对照；N01 标明为本轮补充发现、不伪称原 9 项之一；已关闭 7 项保持）。
- **自检**：[checks.json](checks.json)——3 项验收向量（town_map 8–9 两 Cedolan 点均带目的地；encounters 245–262 MAGIKARP 三条／FEEBAS 一条；map_metadata 200–221 三节 Name 归属）、16 场景唯一性（本轮无场景行变更）、全文残留扫描、diff 重建、链接解析、来源完备声明、上游保护。
- **来源身份**：[source-identities.json](source-identities.json)——本轮**无新增源码阅读**，为同 HEAD 既有阅读三段定点复核（town_map 8–9／encounters 245–262／map_metadata 200–221）；开工登记基线复测一致。
- **修订主题速览**：**R03** §4.4 普通点 18 条枚举删去带飞行目的地的 Cedolan 第二点——两个 Cedolan 点均带 7＠(47,11) 目的地、只归飞行记录组，普通组不含任何 Cedolan 记录（26＝18＋6＋2 等口径不变）。**R07** §5.1 水/钓重复者更正为 MAGIKARP 三条（OldRod 两条、GoodRod 一条），FEEBAS 仅 GoodRod 一条（14 条／12 种等口径不变）。**N01** §4.2 map 045 更正归 Route 6——Route 5(041)、Route 6(044/045)；已正确的 041↔045 连接不改。
- **场景**：M01–M16 保留共 16 行唯一；本轮无场景行变更（M05／M12 已核对无同类错误）、无新增/删除。
- **保持**：v1／v2 交付材料、首审与复审原件、各级快照字节未改；全部既有具名批准（WP01～WP76、WP68–70 整合收口）保持；reference 固定 `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`、Git 清洁；未创建任务／Agent、未发跨会话消息、未提交／推送；未运行游戏/编译器/生成器/反序列化/参考行为模拟器；不使用 WP79/WP80 占位文件。
- **状态**：**ReviewPending（首审修订 v3，待短复审）**；作者状态 REVISED_PENDING_REVIEW——不自行关闭 3 项、不自行 Reviewed、不宣称通过；③已证事件链与④运行观察继续为 0。

## 停止点

3 项修订完成并备齐材料，停止送 WP77 v3 短复审；通过后由审查明确 WP78／79／80 的推进；不自行宣布全项目完成。
