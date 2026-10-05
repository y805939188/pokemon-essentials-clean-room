# R-B02 执行记录

只用 Git acquisition/read/show/diff/hash、rg、sed/nl、JSON及自写文本账本。源码静态阅读见 source-reading.json；不记录为运行观察、Demo链或行为向量执行。

1. 当前AGENTS与本地技能路径检索；独立review分支固定candidate2。第一次fetch尚未完成即尝试switch时报 unable to read tree，等待fetch完成后正确switch，失败尝试没有修改正式内容。
2. 主项目candidate2普通fetch；独立参考clone到主Git外、固定HEAD/tree/origin/detached/clean。环境恢复后再次核主项目分支/HEAD/仅本目录未跟踪，以及参考仍固定且clean。
3. `git ls-remote --heads origin '*B14*'`精确读back batch-B14为af39efbf32549be964cb083bd49bed6d1d5c0d2a。
4. 完整前驱→candidate2及candidate1→candidate2差异；累积12正式文件改变句子、共享目录整段和相关当前接口。输出较长的阅读随后按窄区间补读，不据输出截断声称全文核完。
5. 固定原finding/acceptance、B09合同/锁、B02既有12对象重读；原全局报告不在当前tree，按合同明示历史93e10ba引用，不错误用当前路径替代。
6. Reviewer-owned `audit.py`最初将两个历史输入误当当前路径，随后按其固定commit纠正；初EP检索误用engine目录，定位真实generic目录后纠正。首次计数正则漏28个连字符B04-R ID，已明确补记并拓展为完整ID。均为账本脚本问题，不当作候选行为缺陷；最终全部核验通过。
7. 独立静态先行判断写入后，才读候选2作者响应/身份/自检/补丁。普通fetch六个他审输入所属三个精确报告commit，仅用于核作者证据身份；不运行他审程序。
8. 自写audit最终核72输入/6原写基线、完整46/22路径、12/8正式路径、两目录480旧ID及当前505、B02全部13正式路径、EP01–21、12完整对象/acceptance/C0034根8扩展、6当前管理文件、12文档身份、5intended/application身份、6补丁 `git apply --reverse --check`。补丁只检查，不应用。全累积正式 `git diff --check`通过。
9. `finalize-metadata.py`只写本review目录身份/记录。引用失配或猜测路径的ENOENT阅读已用rg实际定位或Git历史引用纠正；没有据错误路径宣称无行为。
10. 所有待commit内容限定本目录；普通commit及明确review分支push，随后 `ls-remote`和FETCH_HEAD核报告SHA。发布SHA在外部回执交付，报告正文不自引用。没有main/force/public/reference写入。

静态行为向量执行0、参考程序执行0、历史验证器执行0、runtime0、Demo链0、子任务0。自写程序执行只做Git/hash/text/JSON账本，代码可审阅。未来actual由父任务新exact SHA另派，不自动传递候选PASS。
