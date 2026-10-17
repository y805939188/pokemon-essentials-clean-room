# 正式规格去向清单

本清单为未来实现分工提供章节级候选。固定来源是 `fd1df570cad987dc3852a3b958f03916e317f7fe`，交付输入是 `4575e80d041ab0c74a42e2e36399d05791dbaa5b`；两者正式规格子树均为 `f292698cdd4a8e725525a9be6dc34b75faaf151e`。正式规格正文保持原字节。

## 阅读入口

- [集中机器清单](routing-manifest.json)：稳定功能ID、来源事实、当前适用定位、未来计划、去向验证、实现与验收、依赖、决策和整改关联。
- 可读明细：[通用内核](views/generic-kernel.md)、[生物领域](views/creature-rpg.md)、[宝可梦规则](views/pokemon-rules.md)、[战斗需求](views/combat-requirements.md)、[引擎与世界](views/engine-overworld.md)、[界面](views/user-interface.md)、[制作与示例](views/demo-dx.md)。每行分别列来源事实和未来计划，链接固定提交/行范围，并保留章节锚点。
- [文档覆盖视图](coverage.md)、[全部标题映射](section-coverage.json)、[覆盖口径](coverage-summary.json)。治理、术语、依赖和测试章节作为元数据关联功能；测试目录中的静态案例不另计已实现功能。
- [Schema](routing-manifest.schema.json)、[验证与生成工具](routing.py)、[初始去向规则](routing-policy.json)、[工具校验结果](validation-result.json)、[非法输入拒绝检查](validator-negative-checks.json)。
- [状态与交接](handoff.json)、[上游接受回填](accepted-source-updates.json)、[回填合同](backfill-contract.json)、[独立复审入口](review-prompt.md)、[候选文件身份](candidate-file-manifest.json)。

## 使用规则

五类去向为框架实现、Showdown承担、框架与Showdown协作、MZ接入与表现重建、不纳入目标。当前所有功能的去向均待验证，阶段均待定，实现均未实现，验收均未验收；这四组状态独立。去向名称表示承载假设，不能据此推断Showdown已经支持该功能。

`source`固定保存原始来源提交、文档、章节、行范围和哈希；`current_applicability`记录当前适用版本。接受后继时保留历史来源定位，通过接受事件追加新定位和差分。`FR-000001`这类ID在首次登记后永久保留，改标题、移动章节或更新来源不重新编号；拆分时追加ID并登记继承关系，合并时保留旧ID导航。

功能按二级章节归组，去向或验收边界不同的子章节单独登记。父行的`line_ranges`排除被拆出的子节，避免重叠计数。所有实际Markdown标题都进入覆盖映射；无二级章节的数据附页按整篇登记。当前分母由固定索引与实际Git树计算，历史131文档、87WP用于核对；新索引变化须显式评估，不能以旧数字拒绝新增正式规格。

捕获、背包战斗道具、逃跑和战中升级分别绑定四个原型门。其问题覆盖许可、资源来源与扣减、随机消费、场上/持久状态同步、取消、暂停、异常前缀、终局与世界交接。同公式或数值一致不证明这些行为已覆盖。原型均未运行，Showdown版本、规则世代与格式仍待固定。

特殊玩法、Shadow、调试/编辑工具以及XP工程/旧格式迁移的范围保持待用户决策。只有带明确用户范围决定的记录才能使用“不纳入目标”；首版未选或暂缓也不自动排除。来源规格的“非目标”仅说明原篇责任边界，不能转成未来项目排除决定。

正在整改的正式文档先以批次写集保守绑定整篇功能行，状态为待整改后核对。此绑定不声称批内每个必修ID均修改了本行，也不代替精确受影响章节差分。上游候选、实际整合、正式接受和关闭分开；独立复审及上游接受校准完成前，这里保持候选状态。

## 核验口径

标题清点与源身份覆盖为全集机械核对。正文阅读为入口和行为章节抽读，混合边界定向阅读；本候选不声称逐条全文语义审查。去向验证和原型执行为零。工具校验只验证JSON结构、来源身份、覆盖、ID引用和状态约束，不执行Ruby、游戏、宿主、业务向量或框架实现。

根AGENTS与用户的[clean-document-revision技能](../../../review/global-independent-review/eighth-2026-10-16-fd1df57-c84e/inputs/review-SKILL.md)适用：正文按最终态组织，配置、执行证据和待处理事项在交接文件中登记。实际请求配置与有效执行回显逐字段分开；创建参数不作为执行遥测。

## 命令

从仓库根执行，需Python和`jsonschema`：

```bash
python planning/implementation-routing/r8-20261017/routing.py validate
python planning/implementation-routing/r8-20261017/routing.py check-generated
python planning/implementation-routing/r8-20261017/routing.py self-test
python planning/implementation-routing/r8-20261017/routing.py render
python planning/implementation-routing/r8-20261017/routing.py assess-current --commit <精确提交>
```

`validate`和`assess-current`只读；`check-generated`在临时目录重建并逐字节比较视图和汇总，拒绝过时产物；`render`重建可读视图和汇总；`self-test`只写工具负例结果。`seed`只用于首次登记，清单已存在时拒绝重建ID。接受新来源前先运行差分评估，再按回填合同更新当前适用定位和精确接受记录；不能重新运行`seed`替换旧来源历史。
