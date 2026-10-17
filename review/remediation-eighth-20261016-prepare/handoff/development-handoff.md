# 第八轮开发交接（最终独立验收输入）

29必改、10选入可选和9批已接受。最终打标分类与累计来源校准已获独立PASS并按固定载荷整合；整轮最终独立验收尚未完成，CLOSED=0。本交接供最终审者及后续开发定位材料，不启动Ruby参考执行、Showdown原型或新框架实现。

## 规格与接收链

累计正式源为 `5f87743293290de2e219ecdd6c19e88280f60c9a`，formal tree为 `93dc967b4cdb653359afc123d3b8b318d6475fdd`。原R8交付 `4575e80d041ab0c74a42e2e36399d05791dbaa5b`、历史main/B8 `fd1df570cad987dc3852a3b958f03916e317f7fe`、只读参考 `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b` 均保留。

从[九批累计入口](../accepted-cumulative/README.md)、[九批回执](../accepted-cumulative/batch-receipts.json)和[39项状态链](../accepted-cumulative/issue-status.json)定位原合同、正确行为、修订位置、正反场景、候选/实际独立报告及验证资格。131文件中38变化/93保持；历史2,683标题至当前2,704，新增21、删除0。实际6份条件扩展文档已接收；U07只修历史资格overlay，无玩法正文delta。UI65保留U01历史贡献及U04最后两行修复，最终接收由U04真实回执绑定。

## 去向与当前章节

从[去向整合入口](../../../planning/implementation-routing/README.md)、[当前2,704标题覆盖](../../../planning/implementation-routing/r8-20261017/current-coverage.md)、[机器清单](../../../planning/implementation-routing/r8-20261017/routing-manifest.json)及[整合回执](../acceptance/tagging-cumulative/receipt.json)进入。固定候选为 `7ed3e0554ac24339a7e61cab152f628037111644`，独立报告为 `1baee5d7346592478b72d8983b0109e1b2a5e2d9`，正文只取最终5f，不使用候选分支保留的B8工作树覆盖它。

131文档、87WP、736活跃/33完整退役/33元数据、9接受事件/230绑定，pending与partial均0。分类及累计校准PASS只接收粗标和来源同步；框架307、Showdown74、协作130、MZ225、排除0，所有736去向仍待验证、阶段待定/未批准、未实现/未验收。先前R3两P3/七case的原FAIL及后继七case PASS完整保留；原作者候选README的待审文字按其原时点读取，当前状态由本交接与协调回执说明。

## 开发使用方式

先读取源行为的前提、状态与失败前缀，再结合经过校准的去向/依赖拆分工作。Showdown替代方向不撤销本轮原版行为修正。捕获、背包战斗道具、逃跑、战中成长四类协作边界要另固定目标版本/格式并验证；这不是本轮粗标通过的前置原型任务。

[详细与简版路线](../../../planning/framework-roadmap/README.md)按用户原文保存并已获独立忠实性PASS；不等于架构、目标版本、原型或实现验收。用户范围/首版细项、XP工程/旧格式和特殊玩法按既定路线再决定，待定不自动排除。

所有本轮业务向量仍为SOURCE_STATIC/DERIVED_VECTOR/NOT_EXECUTED。此次9项集成命令仅为Markdown/JSON/Python/Git工具验证；原独立候选检查与历史隔离执行保持各自版本、process及有限范围。参考游戏、Ruby、宿主音画、保存回放、Showdown和框架执行均无本轮新增信用。详见[限制与资格](known-limits.md)。

## 最终门与发布交接

当前整体内容等待非作者gpt-6.1-sol ultra/default独立验收；输入绑定必须由后继manifest指向真实既有artifact。通过后协调者才登记整轮接受/CLOSED，再按授权核漂移、保护、必需检查并正常合并main，随后执行已证明可恢复的清理。请求/创建/admission与未暴露runtime echo分别登记，不转授辅助context档位或增加票数。

收尾材料见[只读盘点入口](../cleanup-preflight/README.md)及[最终输入引用补充](../cleanup-preflight/final-input-ref-status.json)。合并SHA、最终main、清理和CI结果尚待实际操作后登记。用户本地的私有归档及同步由父任务单独执行，本云工作区不代表用户本地同步状态。
