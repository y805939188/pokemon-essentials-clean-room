# A-B02 作者候选

状态：**READY_FOR_REVIEW**。本候选覆盖 WP06–10 的七份许可正式路径、9 个主责 ID / 12 个局部贡献 ID；没有自批、关闭 finding 或自行整合。所有静态向量未执行。

输入父 SHA：`0a12de641542f9a59909d2a950c1de8df17ca09d`。它继承被审 B01 整合 `93d0714ddfdb4900e946c0acd1cc80cf6431f0a0` 的正式内容，独立 Ultra 报告提交 `8a1fdfb2b582df4cefb408b56eea144a2e53dcfe` 为 PASS_SCOPED；报告/接受登记后继没有替换正式字节。批准计划 `41fffb540c6483f5296ea0d33b789b75180d27ed` 原字节保留；原全局review取自 `93e10babe0b9c9ef8b3f5277754541b447beeeb4`，原被审基线 `e1e01bb18d824931e54f182dd61af5a9f908ba85`。

候选身份以包含本文件的本批 Git 提交解析；正式父提交固定为上述交接 SHA。作者完成一次普通 commit/push 后另在工作区 `/workspace/b02-publication-receipt.json` 记录具体候选 SHA、父 SHA、远端核验。不存在把候选自身哈希嵌入自身内容的循环；独立复审必须用最终回复/发布回执的精确 SHA 冻结。

- [逐ID作者回应](author-response.md)：修订、前提、最小反例/反向对照、原/净化/附表/测试/登记映射及剩余。
- [机器可读回应](finding-responses.json)、[静态向量](static-vectors.json)：保留严重度/全部 raw_id 别名；状态仅本批候选。
- [原有效finding输入](effective-finding-inputs.json)、[批准验收输入](acceptance-inputs.json)：保留有效二审与全部扩展，不从旧摘要推断。
- [写范围及独立性](scope.json)、[冻结输入身份](input-manifest.json)、[源静态读取](source-reading-log.json)：身份核验不冒充全文语义复核。
- [原路径最小范围建议](scope-conflicts.md)、[A-REG登记建议](registry-proposals.json)：**没有写授权即未应用**，公共表保持原字节。
- [文本/身份/差异自检](validation-results.json)、[正式差异](formal-diff.json)、[候选文件身份](candidate-manifest.json)：自检不是独立批准。
- [模型请求记录](execution-request-receipt.json)：请求 gpt-6.1-sol / Max / Standard(default)，实际生效 UNVERIFIED；无不支持Max证据，未降档。

原规格存在错误的六个路径已经逐条上报父统筹；本批未获得精确扩围，因此本候选保留这些待同步项，不宣称完整根因关闭。A017八处公共导航实际改写仍属唯一A-REG；C003除WP06缓存前提的其他扩展、C081的WP36下游及A015的WP65交界由相应批次处理。

独立参考 Git 在 `/workspace/pokemon-essentials-reference-b02`，固定 SHA `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`、tree `7589c800b61ba13a13040ed0d686979b80a84fd0`，干净只读。参考游戏/Ruby、编译/转换/生成、二进制反序列化、模拟器及求解器均未运行；未放入主 Git，未改 ignore，未向参考上游推送。

U01–U10 / G01–G12 / AX01–AX20、未读未知保持。运行观察0、真实Demo链0、静态向量执行0。B01的EP01–EP21完整保留。B02/B05独立，未消费彼此未批准候选；作者不释放后继，完成后停止等待父统筹派独立Ultra。
