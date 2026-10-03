# WP67-B 首审修订 v2 交付摘要（R01–R15／C01）

2026-10-02；规格提取方。依据 `review/wp67b-review-2026-10-02/`（REQUEST_CHANGES：15 P2＋1 P3；v2 修订提示）。**本轮只修订 WP67-B 首版 16 项**，完成送复审，不启动 WP37。

- **主稿**：`specs/ui/wp67-b-lifecycle-presentations-and-history.md`，v1 被审 `03b7146c`／45,009 → v2 当前 `de32309ac0bf9cf58f843583bb0b35d5cd8de26072d22cee0eaee81f6db35f11`／60,068（磁盘程序化实测）。**v2 入口附表**：[entry-coverage-table.md](entry-coverage-table.md) `d782efb11a2279d4f509bef7f05024ef0664b5bcb885fa05b53712bf5d351427`／12,410。两份 diff 分别相对各自冻结快照（主稿 10 hunks、附表 4 hunks）、patch 精确重建（[diff-bindings.json](diff-bindings.json)）。
- **状态**：**ReviewPending（v2，R01–R15／C01 已修订待复审）**；作者状态 REVISED_PENDING_REVIEW——不自行关闭、不自行 Reviewed。
- **场景**：L01–L28 保留（7 行修订）＋新增 L29–L34 对照，共 34 个定义行、全文唯一。
- **入口附表**：自 v1 的 28 行出发修订受影响行；**v2 七组数据行机械实测 8／5／3／10／4／2／2＝34 行**（C01；首版摘要"24 行"之误在此更正，v1 实际为 28 行，v1 材料留史不回写）。
- **逐项回应**：[revision-response.md](revision-response.md)（16 项：原错误／回源路径行段／修订位置／静态对照／附表行）。
- **自检**：[checks.json](checks.json)——逐项验收向量、34 场景唯一性、全文残留扫描（16 项同根旧句全部为空）、附表实测计数、上游保护、源码分离（R15 更正如实登记，不沿用不真实合规声明）。
- **来源身份**：[source-identities.json](source-identities.json)——基线 63/63 复核不变＋v2 新增 2 份定点来源（019_Utilities、018_UI_ItemStorage）磁盘实测身份。
- **上游保护**：WP23／WP23-N01／WP32-N02 已通过边界原样继承、字节未改；WP67-A、WP65、GR-001～016 及其他批准结论保持；reference 固定 `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`，Git 清洁。

## 修订主题速览

- **进化/图鉴/命名**（R01–R04）：满级糖默认开启、独立入口、取消仍消费；三类图鉴页后续分列（进化待学列表空/非空、交换 WP32-N02、孵化无提前收尾）；命名按光标/键盘模式分列、空文本清昵称；直接孵化与仅演出分列。
- **交换/净化室**（R05–R09、R13）：首卡 2.5 秒自然推进、USE/BACK 提前推进；净化室取消五层；REPLACE 原始值门（空值≠假值）与蛋例外；WITHDRAW 双满拒绝/盒有位/盒满队伍有位失败仍清源；迈步提示的入口前提；中心独存 SUMMARY 不开摘要。
- **遗迹石/道具**（R10–R12）：外层三层分开（无可战斗门、整队标注、Lugia 例外；选人包装写结果变量）；包装返回透传收尾结果非成功布尔；TIMEFLUTE 无净化提交仍消费；香类消息按实际变化三分支。
- **名人堂/片尾/clean-room**（R14、R15）：上限 0 仍增编号、PC 可见后成员创建处失败；三处源码赋值改行为表述并修正自检声明。
- **C01**：附表行数按机械实测登记（v2＝34 行）。

## 停止点

16 项修订完成并备齐材料，停止送复审；不自行关闭 16 项、不自行 Reviewed；不启动 WP37／WP53／WP61、集中回填、B 批整合或整体 double review；未创建任务／Agent、未发跨会话消息、未提交／推送。
