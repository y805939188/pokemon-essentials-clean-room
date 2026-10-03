# WP75 v4：仅收尾两个P3

工作目录 `/Users/dingshinn/Desktop/pokemon-framework-reference`。遵守AGENTS.md、reference只读、clean-room与架构中立。v3有界复审为REQUEST_CHANGES：18 CLOSED、2 OPEN，均P3；所有P2已闭环，无新增编号。只收尾R11的M15场景前提与R12的C组小标题，送v4有界复审；通过后继续已授权WP76，不重复询问批次授权。

先读本目录report.md、findings.json、registration-checks.json、independent-checks.json和next-task-inputs.json。冻结v3主稿 `15ebcf2d9e30b2e394b94cab045974113610454f7f40104fa91259405998d285`／74,925字节；v3附表 `614a3db18532e1988a20beef4bee61d47500e55b5b67bf074fdce7f0f6c89b49`／10,505字节。

第123轮登记基线：manifest `6bc0769a`／1,049,511（1,370完整身份＋2历史行）；TSV v98 `739a5cb8`／177,814（1,275条）；矩阵 `4434d5ea`／67,759。完整身份见next-task-inputs。reference HEAD `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b` 且Git清洁。

## 两项精确修订

- **WP75-R11（P3）**：M15验证整个规范化流程时，分页后第5至8行的新窗口会继续处理，第9行本身就是后续文本命令。原始首行大于20字符、原第9行句号结尾、原文本之后无新文本命令，不足以排除新窗口的合并/断句。直接采用充分夹具：一个文本起始命令＋8条续行，每一行均为独立测试文本 `This sentence is longer than twenty characters.`，之后仅结束命令。这样每一行都大于20字符且句号结尾，无格式码/反斜杠/小于号，可得到3窗4/4/1。同步M15、回应、checks、摘要与本轮记录。正确的规则正文和已补好的M17保持，不继续扩写。
- **WP75-R12（P3）**：v3附表C组已正确恢复柜台能力，共9个数据行，但局部标题仍写8行。改为实测9行；无其它增删时总数仍44＝5/6/9/9/8/7。复核全部组标题与结构计数一致，柜台正文/场景/该数据行不重写。

报告提供满足v3旧前提却仍触发断句的反例。不要运行参考程序或参考行为模型；本轮只需定点阅读来源与文本静态核对，不扩读无关领域。

## 交付

主稿原位修订，M01–M30身份保留。正常更新§20当前修订版本/交付索引与v4记录；不自行Reviewed。v1/v2/v3作者材料、各轮review及快照全部保留原字节，18项闭环与WP74 18/18、WP72/73 37/37、全部旧批准保持。

新建 `review/wp75-delivery-2026-10-02/revision-v4/`，提交回应、自检、来源身份、摘要、新附表、diff-bindings及两份严格完整diff；阶段登记末检另存，不登记自身哈希。两份diff分别从本review的 `input-snapshot/specs/demo/wp75-project-conversion-and-authoring-tools.md` 和 `input-snapshot/review/wp75-delivery-2026-10-02/revision-v3/entry-coverage-table.md` 重建v4主稿与新表。绑定实测完整SHA-256/bytes/hunks，零模糊零偏移；不要求累计历史diff。

最终文本定稿后核验场景实际改动数、所有组标题/表行数、链接、来源身份、净化及当前断言一致性。SellItem等兼容输入数据仍允许；不得重新引入实现控制流原句。矩阵仅F18-04更新为v4待有界复审，旧通过行保持；manifest/TSV按真实身份登记，历史§2/§3/§4只追加，不集中回填。

两项完成后停止送v4有界复审，通过后恢复WP76。reference只读；不运行转换器、提取合并、浏览器页、游戏、反序列化或参考模型，不改工程/存档，不创建Agent/聊天、不跨会话发消息、不提交推送，不启动WP77、B批整合或整体double review。
