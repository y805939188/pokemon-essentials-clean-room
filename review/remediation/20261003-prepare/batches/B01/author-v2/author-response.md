# B01 v2 后继作者回应

本轮最小扩围仅同步四项原规格行为和验收场景；旧候选和历史批准原件保留。下表不构成独立复审判决，规范状态全为 OPEN。

| 原规范 ID | 本次新增同步位置 | 作者变更 | 当前状态 |
| --- | --- | --- | --- |
| GIR-FD82-A001 | specs/kernel/wp04-pbs-lifecycle.md §4.2/§9.2 | 既有最终WP04 §4.2与KL10字节不变；新增同步原WP04 §4.2/§9.2：合并耗尽保留标记、追加独立Other才去标记，原正确非末/末/普通场景逐字保留。 | OPEN／待Ultra |
| GIR-FD82-A002 | specs/kernel/wp04-pbs-lifecycle.md §3.1/§9.2 | 既有最终WP04 §3.1与KL19–21字节不变；新增同步原WP04 §3.1/§9.2：各文件先截整秒、各集合取最大值后>=比较，新增隔离前提及三条对照。 | OPEN／待Ultra |
| GIR-FD82-A004 | specs/kernel/wp05-events-extensions-plugins.md §5.1/§6.2/§6.3/§9.2 | 既有最终WP05与EP19–21字节不变；新增同步原WP05 §5.1/§6.2/§6.3/§9.2：完整路径区分大小写.rb子串、显式先行自动追加、相同路径首次去重及产物消费同序。 | OPEN／待Ultra |
| GIR-FD82-A009 | specs/kernel/wp05-events-extensions-plugins.md §5.2/§9.2 | 既有最终WP05 §5.2与EP08字节不变；新增同步原WP05 §5.2/§9.2：最低依赖版本不足两种Link前提均终止，更新链接仅来自已合法登记的有效Link。 | OPEN／待Ultra |

完整14个贡献的前提、最小反例、唯一静态结果、反向对照、固定源阅读、剩余范围与登记建议见 [finding-responses.json](finding-responses.json)，当前14对象继承原报告全部字段/有效限定，规范ID和优先级不变。四项响应已更新原规格同步状态；其他10对象按旧候选原响应保留，不因此扩大交付。

本增量新增原WP04三条新鲜度场景和原WP05三条路径/顺序场景；改写原WP04合并耗尽场景、原WP05有/无Link场景及两个省略Scripts场景的自动候选前提。原非末值、单值/末值、普通值三个引号对照字节保留；假值/空列表的正确防御语义、依赖与发布/编译门控、错误终止也保持。既有最终目录20个新增ID属于完整PRE0差异，本增量最终ID新增0。

新增原规格句与既有最终规格共用固定源证据和静态向量；不创建或执行示例脚本，不运行编译、消费或游戏来证明结果。完整八份正式文件及本次两份正式文件差异分别见 [formal-diff.patch](formal-diff.patch) 与 [incremental-formal-diff.patch](incremental-formal-diff.patch)。

两条写权限冲突已由 [范围修订01](../scope-amendment-01.md) 授权并形成作者候选；其他跨批同步仍见 [scope-conflicts.md](scope-conflicts.md)。这是范围阻塞解除，不是finding关闭。历史 Reviewed 只绑定旧被审版本，当前candidate必须由新独立 Ultra／Standard 复审。

PRE0、旧author记录、历史批准与报告、公共入口/追溯/索引、其他原规格及参考保持原字节。没有整合，没有finding关闭，没有下游任务启动。实际有效模型/推理/速度仍UNVERIFIED，明确请求 Max／Standard、未降级或改配置。
