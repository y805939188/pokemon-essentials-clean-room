# 第二轮命令与发布记录

所有项目操作在 `/workspace/pokemon-essentials-clean-room`，参考在主Git外 `/workspace/reference-b03`。参考仅git rev-parse/status、rg和原文本sed只读；Python只用于项目Git/Markdown/JSON元数据、哈希与字节核验，无参考解释器/向量/公式执行。

1. 重读AGENTS；本地无适用.agents/.codex skill。先核旧review分支4706/clean；fetch主项目作者普通分支，ls-remote确认105a。
2. 在105a新建 `remediation/20261003-prepare/review-B03-2`；核新候选3c572/tree6933及参考固定SHA/tree/clean，检查完整53路径和旧候选增量9正式路径。
3. 独立读场景、Metadata、Messages、Interpreter_Commands、Character、Player原文本；审三个反例/近邻和原26项影响范围。比较13正式payload/handoff及全部235旧行字节；先保存 preliminary-static-audit 与 independent-first-judgment。
4. 首判后再读author-v3响应、自检/结果、追溯、建议、来源日志及范围/冻结证据；读取作者自检源而未执行。运行本目录verify-inputs.py，仅做独立身份/字节/文档结构检查；通过后不扩大到运行或模拟。
5. 报告字段、逐ID、链接、JSON与只新增review-round-2范围复核；git diff --check通过；再核固定参考clean。

发布使用普通命令：

- `git add -- review/remediation/20261003-prepare/batches/B03/review-round-2`
- `git commit -m "review(B03): independently accept scoped second-round candidate"`
- `git push origin HEAD:refs/heads/remediation/20261003-prepare/review-B03-2`
- `git rev-parse HEAD`、`git ls-remote origin refs/heads/remediation/20261003-prepare/review-B03-2` 核完整发布SHA相等，再核工作区clean及第一轮远端4706不变。

本文件不写自己的未来commit SHA。最终普通发布返回SHA由交付响应单列，候选/交接/报告身份分开，无自引用。第一轮报告保持在其独立分支，没有合入作者正式输入。没有main/force/reference upstream/public registry操作。
