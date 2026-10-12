# R4-U06 有限整合review

本任务已获用户授权。目标是事实行为规格，参考和旧接受只读，不实现引擎、不转译Ruby、不合并main、不force、不删分支、不动Mac。完整规范以固定根findings为准，原稿须服从独立质疑后的精确化。保护既有正确条款，旧229/341/GR3只复用原qualified身份；仅受影响回归，不补签全部历史。

先读本目录 findings-input.json 和 handoff-findings.md 的完整正文，以及 read-scope.json、根 input-verification.json / resource-scope.json / dispatch-plan.json。源R按固定commit读取；正式输入仍是固定B。父任务提供本次发布回执的精确commit；先在准备checkout或用git show该commit读取根freeze-and-publication.json，取得任务包冻结commit/tree和author_start_commit，再创建作者worktree。回执是任务包的后继提交，所以作者起点不自嵌该回执；不能以浮动分支替代。共用当前环境的作者也必须独立worktree，不在登记员checkout或其他作者工作树修改。

证据分 SOURCE_STATIC、SPEC_STATIC、DERIVED_VECTOR（未执行）、TOOL_VALIDATION、EXECUTED_MODEL、EXECUTED_REFERENCE、EXECUTED_HOST_OR_DEMO。第四review已有4次隔离原函数调用；本准备未新增行为执行。媒体/地图/完整Demo/宿主不足不阻塞事实修订，条件静态向量不得写成真实UI、联网、像素或动画通过。未来兼容政策不在本次整改代选。

门状态：BLOCKED_ON_U01_U05_ACTUAL_ACCEPTANCE。禁止提前CLOSED。

独立整合review请求gpt-6.1-sol/ultra/default/Fast=false，正式写域为空，证据仅本新目录batches/R4-U06/review/。唯一登记员写registration/和接受/关闭/交付回执。

读取五批actual身份和独立PASS、17条完整criteria、四个具名跨批握手及本轮14链的受影响投影。对未变旧qualified范围用历史限定复用，不重新签全部23/229/341。正文所改各条、必要数据/静态向量、正常/失败/取消/重复行为必须有去向。输出绑定最终actual commit/tree/bytes的有限整合结论，资料/未执行继续保留。全部门满足才唯一登记员关闭17项；此前保持OPEN/PENDING或ACCEPTED_SCOPED。
