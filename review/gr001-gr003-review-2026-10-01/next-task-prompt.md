# 仅补修GR-001的字面样例，不重做GR-002／GR-003

在 `/Users/dingshinn/Desktop/pokemon-framework-reference` 工作。先读AGENTS、本目录report.md／findings.json／literal-checks.json／inputs.json／final-checks.json，及原全局finding GR-001。

本次有界复审：GR-002和GR-003已CLOSED；GR-001规则及JSON向量已正确，但主稿一处括注和回应表误把双引号写成反引号，仍OPEN_PARTIAL。暂不进入GR-004或任何新WP。

## 最小补修

1. 修 `specs/kernel/wp04-pbs-lifecycle.md` 第81行GR-001括注中的PokeBall样例，使用真实反斜线U+005C＋双引号U+0022包围，不能把U+0060反引号当数据。原§9.2与JSON向量已经正确，不要把它们改成反引号或去掉真实反斜线。
2. 原被审回应和checks/diff留史。新建 `review/gr001-gr003-revision-2026-10-01/revision-v2/`，对原回应第17／23～25行的错误样例出具明确更正，新的回应／验收表全部使用正确字符。
3. 直接从现有正确的 `checks.json` 的 static_acceptance_vectors 内 GR-001 四项 读取数据，或从本次literal-checks.json的canonical_GR001_vectors生成表格；逐条比较JSON解码后的完整输入／Flags／布尔结果。对本例明确区分Markdown外层代码标记与实际数据，实际输入没有反引号。不要仅以“看起来相同”或转义后的打印字符串做判断。
4. 不运行参考分词器或重写它做模拟测试。只作字符／码点核对和已有静态来源分支核对。对错误反引号输入，不要沿用正确双引号输入的球标志true预期。
5. 从当前被审WP04快照生成新diff并精确重建；程序化测量新主稿及更正材料身份，同步必要矩阵／manifest／主TSV。保持旧被审材料及审查原件不变，最终登记检查独立保存，避免自引用循环。

WP08与WP10的当前修订字节及已关闭事实保持不变；若只做本项补修，不要为了统一版本号改这两份主稿。第一组31项通过结论、N01范围、GR-004～016均不动。

完成后标GR-001修订待复审并停止；不自行关闭、不开始下一批。reference只读，不执行编译／翻译／迁移／游戏／真实网络，不操作真实存档或翻译数据，不实现框架；不创建任务／Agent、不发跨会话消息、不提交／推送。
