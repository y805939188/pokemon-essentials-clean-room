# 自身核对方法的修正记录

这些是本轮自编元数据核对的错误，不是候选／实际缺陷；不得把初次未通过计数写成被审失败。所有行为判断来自直接静态阅读，不来自这些脚本。

1. 初次程序在固定原 findings 输入处中止：自己把明确绑定 O 的历史读者错误强制绑定到 T，导致路径不存在。原登记实际上明确携带 O。修正为显式历史commit优先，只有实际 binding 才用T；未更改被审登记。
2. 随后26项初次完整结果为23通过／3未通过，已保留于 `initial-metadata-check-attempt.json`：目录 ID 正则漏了 E07b/E08b/E09b 三个原合法设计；整节切片漏了下一heading之前的末尾换行；把原 findings 的语义状态错误当作 canonical OPEN统计。修正为保留b后缀、准确包括章节换行，以及从固定原 `root/remediation-index.tsv` 直接读取229个 `OPEN_NOT_EDITED_IN_THIS_REVIEW` 行。当前对象语义状态与规范关闭状态分开。
3. 修正后26项全部通过。随后新增实际公共叙述／18行快照／依赖集合运算／残余门／O01保持核对，再独立重构批准的30条原稿替换，最终32项通过／0失败，见 `metadata-check-results.json`。12个阶段JSON内1,069明确身份绑定均通过；669唯一commit/path不等于全部历史内容语义已审。

源定位检索两次猜测的Trainer路径不存在，随后 `rg --files` 定位到 `Data/Scripts/015_Trainers and player/001_Trainer.rb` 并读取161–168；未读失败路径不在源阅读记录。原稿提案路径也通过实际阶段identity解析到 `scope-proposal-1/original-sync-proposal.json`，未使用不存在的candidate-1同名路径。未执行作者或历史审者程序。

`metadata-audit.py`仅运行自编Git、JSON、TSV、文本与哈希核对。源码日志哈希完整文本只用于身份，所列行范围才是本轮新语义阅读范围；未列范围不宣称已读。没有参考行为执行、转译模型、求解器或自动测试向量。
