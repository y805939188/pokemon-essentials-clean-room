# 新会话：接手 Pokémon Essentials 独立行为规格 Review

你是本项目的**独立 reviewer，不是提取模型**。请先完整读取：

`/Users/dingshinn/Desktop/pokemon-framework-reference/review/reviewer-handoff-2026-09-23/handoff.md`

再读根目录及适用 AGENTS.md、当前 manifest，以及：

- `review/wp17-recheck-2026-09-23/report.md`
- `review/wp17-recheck-2026-09-23/revision-prompt.md`
- `review/wp17-recheck-2026-09-23/revision-response.md`
- 同目录 `revision-diffs/`；旧被审版本在 `input-snapshot/`。
- 当前 `specs/ui/wp17-messages-windows-input.md` 与 `specs/ui/wp17-draw-text-tags.md`。

工作区 `/Users/dingshinn/Desktop/pokemon-framework-reference/`；参考固定 commit `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`，reference 只读。

当前状态：WP01–WP16 各自限定通过且已登记 Reviewed。WP17 最新完成审查只检查了主文档 v2/附表首版，结论 REQUEST_CHANGES；R02～R05/C01 已关闭，**仅剩 R01 新附表两处：c 清阴影、单独/文尾图像消费边界；C02 为非阻塞场景记法维护。**

提取方已交付 WP17 主文档 v3、附表 v2，声称剩余项已修。交接会话按用户要求只整理材料，没有 review 这批新稿。**本新会话请直接固定新版本并做原问题及直接回归复审，无需再问是否继续。** 不重做首审、不重开 R02～R05/C01，也不要把本交接或提取方回应当外审通过。

交接时实测版本：

| 对象 | SHA-256 | 字节数 |
| --- | --- | ---: |
| WP17 主文档 v3 | `6010f40b2f00feb1643b7da215ea4ccac1be3e0af429de57a9efaf400c16c4c9` | 29193 |
| 绘制附表 v2 | `e01466ef9f45f661c57f2bb7e53adaa7504d4bafa7e25308f3cb41950a9a24d0` | 7129 |
| feature-matrix | `5aecfd3979c85a572d1256c04802a7263930eefbe088295e6d289ab9772e571e` | 35698 |
| manifest | `d3bef5803ae34a7769b45a111fbb4a0184d2d1d1574f057efbaa66dd8d8d8063` | 53195 |
| 最新提取侧回应 | `01632506f5fc23773fab5db7a522b5503d5e24e8c299bec2756aa0f29964b418` | 3229 |

先复算实际完整哈希和差异；交接后可能继续更新。辅助锚点在本交接目录的 `workspace-checks.json`、`current-hashes.tsv`、`snapshot/` 和 `changes-since-last-review.diff`。98 条 manifest 哈希匹配只表示字节对应，不表示 v3 已审。

此次有限复审：

1. c/c3 嵌套场景：`<c3=FFFFFF,000000>A<c=FF0000>B</c>C</c3>D` 中 B 无阴影，C 恢复外层组合。查 `Data/Scripts/007_Objects and windows/010_DrawText.rb:248–266,437–461,622–633,940–965`。
2. 直接格式化入口：单独 img/icon、最后文字后的图像，与图像后仍有普通字符的输入分别核对；不要扩大成所有消息文尾图像无效。查同文件 `360–393,423–432,519–538,627–658,1003–1007`。
3. C02：空选项/默认选择的命名输入条件、setter 场景 `[1,9]`、总览按入口更新次序。只做维护差异确认，不重开已关闭行为。

默认只读源码、规格、计划和旧审查；仅在 review 下新建独立报告、检查、快照和提示词，不覆盖原件，不代提取方改规格/矩阵/manifest。禁止运行游戏、参考 Ruby/表达式、解释器/事件脚本、生成器、编译器、转换器、插件或真实网络，不操作真实地图/存档/输入，不设计新框架，不自动创建其他任务/并行 Agent。可用安全的自有只读文本/哈希/集合/独立算术检查，不执行参考代码。

真实剩余问题给稳定编号、被审完整哈希/行号、源码证据、影响、最小修订和静态验收；继承已通过范围，不为措辞偏好无限复审。区分本轮新证据、旧审查记录、提取方声明和运行未决。

完成后交付新独立报告＋可直接给提取模型的提示词：若 WP17 限定通过，给 WP17 Reviewed 管理性回填及 **WP18→WP19→WP20 三包**执行提示（按计划依赖、逐包自检、批末统一送审）；否则只给有限修订提示。本会话不代执行下一批。Demo、宿主、媒体、插件、U01–U10 及 WP78/79/80 阶段出口继续保留。
