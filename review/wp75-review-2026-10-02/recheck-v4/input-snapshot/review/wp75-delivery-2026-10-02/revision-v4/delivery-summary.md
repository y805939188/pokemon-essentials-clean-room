# WP75 首审修订 v4 交付摘要（v3 有界复审剩余 2 项 P3）

2026-10-02；规格提取方。依据 `review/wp75-review-2026-10-02/recheck-v3/`（v3 有界复审 **REQUEST_CHANGES：18 项 CLOSED、2 项 OPEN（均 P3）**；v4 修订提示）。**本轮只修 R11／R12 两项 P3 残留**，完成送 v4 有界复审，通过后继续已授权的 WP76；本轮不开始 WP76。

- **主稿**：[wp75-project-conversion-and-authoring-tools.md](../../../specs/demo/wp75-project-conversion-and-authoring-tools.md)，v3 被复审 `15ebcf2d`／74,925 → v4 当前 `8a09d95c`／76,732（385 行；磁盘程序化实测）。**v4 入口附表**：[entry-coverage-table.md](entry-coverage-table.md) `2d0eb2da`／10,609（六组 **5／6／9／9／8／7＝44 行**结构法实测——仅 C 组小标题由 8 更正为实测 9，数据行无增删）。两份 diff 分别相对 recheck-v3 冻结 v3（主稿 3 hunks、附表 2 hunks）、patch 精确重建（[diff-bindings.json](diff-bindings.json)、[revision-diffs/](revision-diffs/)）。
- **逐项回应**：[revision-response.md](revision-response.md)（2 项：v3 已接受部分／残留／修订位置／来源／静态对照；18 项已闭环保持）。
- **自检**：[checks.json](checks.json)——2 项验收向量、30 场景唯一性与逐行比较（本轮修订 1 行：M15；无增删）、全文残留扫描（最终主稿＋v4 附表＋回应＋摘要；广谱模式实测 0 新增命中——`SellItem(...)` 注释数据格式等既有命中保持、按首审报告兼容输入数据判别）、附表实测计数（44＝5/6/9/9/8/7，全部组小标题与实测一致）、diff 重建、链接解析、来源完备声明、上游保护。
- **来源身份**：[source-identities.json](source-identities.json)——**本轮无新增源码文件阅读**：2 项证据沿用同 HEAD 既有阅读定点复核（文本子规则条件 `004_Compiler_MapsAndEvents.rb:1434–1498`；附表组标题结构核对）；开工登记基线复测一致。
- **修订主题速览**：**R11** M15 场景换成互不干扰的充分夹具——1 条文本起始命令＋8 条续行命令、之后仅结束命令，9 行每一行均为同一独立测试文本 `This sentence is longer than twenty characters.`（每行 >20 字符且句号结尾、无格式码／反斜杠／`<`）——初次分页后第 5–8 行新窗口的首行/末行相关条件同样全部被排除，稳定预期 3 窗 4/4/1；已正确的文本规则正文与 M17 不动。**R12** v4 附表 C 组小标题由 v3 的 8 行更正为实测 9 行（「柜台合并」数据行 v3 已恢复，本轮仅同步标题计数）；其余组不动，总数保持 44。版本化同步（不另立问题）：主稿 §20 交付索引更新为含 revision-v4 的实际索引（原仍列 v2），状态行与修订记录追加 v4 条目——v4 仅两项 P3 收尾，无行为规则变更。
- **场景**：M01–M30 保留共 30 行唯一；本轮实际修订 1 行（M15）、无新增/删除。
- **保持**：v1／v2／v3 交付材料、首审与各轮复审原件、快照字节未改；18 项已闭环不重开；WP74 18/18、WP72／WP73-A／WP73-B 的 37/37 闭环、WP61（11/11）、WP53、WP37、WP65、WP67-A/B、GR-001～016、WP23-N01 及所有旧批准保持；reference 固定 `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`、Git 清洁；未创建任务／Agent、未发跨会话消息、未提交／推送；未运行任何工具或参考行为。
- **状态**：**ReviewPending（首审修订 v4，待有界复审）**；作者状态 REVISED_PENDING_REVIEW——不自行关闭 2 项、不自行 Reviewed、不宣称通过。

## 停止点

2 项 P3 残留修订完成并备齐材料，停止送 WP75 v4 有界复审；通过后再继续 WP76；不开始 WP77/78/79/80、集中回填或 B 批整合。
