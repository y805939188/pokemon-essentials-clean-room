# B02-G 实际整合受影响核验交接

**INTEGRATED_PENDING_ULTRA**。此目录是 A-REG 公共登记的送审输入，不是独立核验报告。完整候选 `46cd726c35e9d754a8e42b32986313ce3d4d1782` 的 R-B02 候选判决为 PASS_SCOPED，报告提交 `94b012ee12d457aa4b99103477a0d35f083b1182`；实际 integration 冻结 SHA 另由最终 Git 发布交接提供，不把报告提交当被审 SHA。

## 输入与保留

接受起点 `0a12de641542f9a59909d2a950c1de8df17ca09d`；13 份正式文件（7 最终/测试＋6 已授权原规格）、30份作者材料和12份独立报告材料均完整整合并保留原字节。B05未审候选未消费。完整正式前后与公共/依赖身份见 [integration-manifest.json](integration-manifest.json)、[current-hashes.tsv](current-hashes.tsv)。原全局报告 `93e10babe0b9c9ef8b3f5277754541b447beeeb4`、批准计划 `41fffb540c6483f5296ea0d33b789b75180d27ed`、参考 `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`不变。

旧 B01 接受记录没有覆盖：中央规范ledger原229行不变，approval/trace旧14行不变，仅追加12条B02贡献，以 finding+candidate 区分贡献；中央交接的整个B01原文保留。B01原manifest/计数/模型/审查材料、历史dated清单/current-hashes不回填。共享目录仅新增/修订本批行，EP01–21和DP整段不变；WP02原文/设置附表/WP08原文的新hash由B02候选审查承接，不能借B01旧源hash作新批准。

## 本次公共新字节及未完成范围

audit当前层应用 [八个正确导航后继](a017-navigation-successor.json)，逐个核固定参考目标与原行范围；历史八错误行原字节保留，当前查阅须用新层。README/scope准确区分B01已接受与B02待核验；测试索引改TM14/IO15/LZ17/MG16；coverage/Feature和勘误仅添当前限定层。旧批准/原行为限定不移动到新字节。

[逐 ID 登记](finding-registration.json)保留8主责行为、A017原候选提案判断和3局部贡献的范围、严重度、全部别名、原有效限定/扩展。当前仅已整合待Ultra；229必修全OPEN、关闭0。A015主责B16/WP65；C003仅WP06缓存贡献，WR12/B04及全部有效原/八扩展责任仍开放；C081的WP36原/最终饱和冲突归B08；A017新公共层仍待B02-I及B21核验。B03/B06/B16/B18/B21等下游BLOCKED，本作业不启动任务。

当前共享静态目录99行，相对上游+12，12旧行修订，无删除；原WP07/08/10场景14/17/16，+2/+3/+4。这些是文本场景计数，未执行。详见 [scope-counts.json](scope-counts.json)。

## 完整差异与核验门

有限两提交：先冻结完整登记payload，再只新增两份完整patch和diff-and-freeze记录；patch覆盖 accepted-upstream→payload 与 candidate→payload 全部路径。证据提交仅增加可审证据，正式/公共内容与payload不变。最后 inclusion SHA 是本次实际整合核验目标，由最终普通push/远端核验给出。完整最终差异始终可用 `git diff 0a12de641542f9a59909d2a950c1de8df17ca09d <frozen-integration-SHA>` 与 `git diff 46cd726c35e9d754a8e42b32986313ce3d4d1782 <frozen-integration-SHA>`重建；最后3个证据新增路径另列，避免patch/commit自引用循环。

R-B02须核精确实际SHA的13正式字节、完整差异、当前八导航与保留原限定、受影响旧B01贡献、原/最终同步、索引计数/链接、当前/历史身份、中央台账229 OPEN及跨批剩余；不能仅看hash声称公共语义通过。[validation-results.json](validation-results.json)只是A-REG的有界结构/身份检查。

作者请求gpt-6.1-sol Max/Standard，复审要求Ultra/Standard；实际三项UNVERIFIED，未降级/改配置。参考只读，参考程序/运行观察/真实Demo/静态向量执行均0；U/G/AX及素材/宿主/插件未知保留。完成普通push及远端SHA核验后停止等待R-B02实际整合复审。
