# U06 实际整合冻结与独立复审入口

已形成实际提交 `266539d5db6d84116a355f503df8830d309c7937` / tree `d4efb94a34fd5fc5d3c3eb66bf861782c23cbbcc`。3个正式文件逐字等于冻结作者 `c9d6e3c81c88c778abf2f822977275d0e632581e` 的独立PASS候选；仅增加2个必要当前公共承接，4份管理记录。其他128正式、旧review/229/341、参考与main保持；U01/U03未通过或未完成的候选没有混入。

候选独立报告 `471c63bb7585c44d08571e7d09631694eea57632` 只签候选。actual独立复审、正式接受、最终CLOSED均未完成；2/23实际字节已整合、0/23正式接受、0/23关闭；六主题批中1批actual payload已冻结，U07未完成。U06没有旁批前置。

[实际复审输入](actual-review-input.json) / [同独立reviewer任务](actual-review-task.md) / [单份完整实际差异](actual.patch)。actual.patch明确from `d0371f693f4a0dc713ee5cc6e43a20ff465269a8` to `266539d5db6d84116a355f503df8830d309c7937`，所有9个变化文件已在临时base副本重建逐字匹配。复审应绑定该actual，而包提交只承载冻结任务；包发布commit/tree由外部最终回执提供，不自嵌循环。

[integration-state.json](integration-state.json)仅登记分层状态；[source-successor.json](source-successor.json)绑定新事实与来源，公共新增字节待本次review；[protection-check.json](protection-check.json)记录128文件保护；[input-verification.json](input-verification.json)记录实际读取的作者10文件/候选review6文件身份。
