# R5-U03 WING 消费前提限修 01

本候选仅修 `GR5-M05-004/static/04` 的 `R5U03-M05-004-02` 输入前提：合法作者 WING 记录须为非重要物品，且有效消费为真（Consumable 省略或 true）。目标前提与 EV+1、扣1、重算预期均保持；69 条向量和 11 项必修分母保持。

固定作者基线为 `d84bf0dd0eac4605c98d8ba4ae3f8502117fc5a7` / tree `c1b9497fc9d571b738ccbad3eaaf3a6584b98f41`。限修提案为 `9fab9d7d2995cf0402920f3bf94d8473579e31b8` / tree `6fe336abffd610702d9b02bd6d409c8f881d0ff1`；失败实际报告为 `1eda123e3bcd4b1aa99e2ba57c6de02d56414716` / tree `1a5751e2198717ddf95a3322815fd8a43e46deef`。新候选与证据同 commit，最终 commit/tree 由外部发布回执绑定，避免自哈希。

限修同步载荷是 `static-vectors.json /vectors/45/input`、`operations.json /operations/49/new_text`、专属测试目录镜像第294行、完整 B5 `formal-diff.patch` 及当前 manifest。此目录的 [一行增量补丁](formal-diff.patch) 与提案补丁逐字节相同。[逐项响应与验收映射](response.json)、[读取记录](source-reading-log.json) 和 [结构验证](validation.json) 给出精确身份与限制。

`Consumable=false` 的合法非重要 WING 可仍成功增加 EV 并重算，但外层不扣库存；绑定复制不会改变数据消费位。重要物品有效消费也为假。新前提排除这些不消费记录，符合 WP27 §2.1–§2.2、WP28 §5.3/§6；O025 的显式 false 经导出/重编译保留规则保持。以上均是静态规则推导，未执行参考、模型或宿主行为。

与 d84 相比，其余68向量对象、51操作对象、80目录行、15正文投影、31共享片段及28既有载荷文件逐字节保持；包括旧 v2 证据、fragment-manifest、两个导航 MISMATCH。旧 v2 验证只绑定 d84，不能当当前消费前提的验证。实际报告中另10项 PASS、另59条静态 PASS 仅以固定记录身份复用；旧候选 PASS 与实际 FAIL 均原样保留，此作者不签新独立 PASS。

复现：在包含固定输入 Git 对象的本仓库运行 `python review/remediation-fifth-20261013-prepare/candidates/R5-U03/author/limited-wing-01/verify.py`。该脚本只核文档差异、身份和补丁回放，输出 TOOL_VALIDATION；不实现或执行引擎规则。

原审者入口：仅定向复验 `004-02/static/04`、WP27/28 外层消费矩阵及 O025 消費位反写，核新固定 candidate commit/tree 和增量载荷；其余精确未变资格按 response.json 绑定复用。原审者由父任务安排。U01 上游门已由实际报告确认在 `7bd8102f0ecf147b58b652e5dbb425c69847e144` 的独占贡献范围满足。候选复验仍 WAIT；通过后才由 R5-I 机械接入精确一行、冻结 actual-02，再由原审者核实际字节。当前 actual-02 未创建，整8共享文件/U08/关闭仍 WAIT，正式接受、公共登记和 CLOSED 均为0。

候选分支 `codex/r5-u03-author-20261013`；只写原 U03 author 域。未改 live formal、main、其他作者、Mac 或不可变历史。R4历史隔离4与R5复审隔离4分别保留，本次新行为执行0。实际模型回显 UNVERIFIED，未切换模型/使用Fast/审计额度。宿主、媒体、完整Demo、真实存档及动态扩展等限制保持；optional与兼容政策不扩张。
