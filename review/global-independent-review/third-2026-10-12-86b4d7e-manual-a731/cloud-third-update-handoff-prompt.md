# 云端第三轮整体 update 接手提示词（完整可复制）

**只有用户日后把本提示词交给 dot，并明确指示开始 update，才启动以下工作。当前本地 review 已完成并发布；没有云端任务已被创建/唤醒，也没有今天的规格修订授权。**

你接续的是第三轮已经完成的有限独立评审，不从零重新安排一轮全局review。先完成只读身份/材料/权限预检，给READY／READY_WITH_LIMITS／BLOCKED；条件允许才在用户届时实际授权范围进行有限修订。不能用既有PASS、计数或本地路径想象材料已可得。

## 1. 项目和轮次

仓库：y805939188/pokemon-essentials-clean-room。目标是理解Pokémon Essentials所有可得功能、规则、数学、状态、正常/失败/取消/部分提交/边界和UX，形成可供以后从零开发现代TypeScript框架的净室行为合同。保持通用内核、Creature-RPG、Pokémon规则、Combat、Engine/Overworld、UI、Demo/DX及共享交界；未来架构可以重新设计。此update只修订规格/分析与获授权登记，不创建TypeScript包、战斗实现、MZ插件或生产adapter，不翻译Ruby、不复制源代码/源类/方法层次。参考只读。

第一轮：本地各WP边review边update建立规格。第二轮：原全局review＋B01–B21共21批整改、229必修关闭、FINAL-1/FINAL-2独立验收。第三轮：这次用户手动本地独立review＋用户之后另行交dot开展的云端整体update，属于同一轮的先review后update，不误写为第四轮。

## 2. 固定输入、可达快照和真实状态

本轮报告/manifest资料快照已实际发布在独立ref `refs/heads/codex/review-third-20261012-86b4d7e-a731`，commit **f5174841d7ec4e8c4a6565392bd22daffa22ed99**，tree **275c99dae845c23ced0c43639dc6b28f01d27f0f**。该SHA是评审产物身份，不是受审规格输入。Git远端ref已查、隔离临时Git实际fetch该commit后逐一读取200文件，bytes/SHA256/blob全部一致；总报告/findings/manifest3个HTTP raw body也一致。main实时仍86b4d7e，没有merge/force/history rewrite。

固定资料根：`review/global-independent-review/third-2026-10-12-86b4d7e-manual-a731/`。完整冻结manifest直接读取：[snapshot manifest](https://raw.githubusercontent.com/y805939188/pokemon-essentials-clean-room/f5174841d7ec4e8c4a6565392bd22daffa22ed99/review/global-independent-review/third-2026-10-12-86b4d7e-manual-a731/cloud-third-update-handoff-manifest.json)。它的publication:not_published是首快照生成时历史字段，本提示词在真实发布/readback后给出了上述实际结果；不可据历史字段声称当前未发布。最终manifest/提示词自身的后续发布SHA/hash在外部最终回执给出，避免自引用；**所有云端必需实质资料在本节固定A快照中已可取得**，无需依赖自己的浮动branch名。

本提示词自身的发布身份不嵌入自身；请同时使用用户交付的最终回执。最终manifest的canonical ID/处置与本提示词及A findings严格相同，后继变化只补发布/导航/结束状态。A快照没有本提示词文件是刻意的先冻结发布→后生成提示词顺序，不是未完成review。

固定交付D：commit `86b4d7e1d8645e75af91a215240f8786a5bb4ca8`，tree `42c29efb5422772a1d90f657f25983600f500f28`。正式实际S：commit `167296dbe9e2384627b0ed696e87aeb01f211252`，tree `33598d8a2a3acdd093cc4fe23f48eea8666100f3`。131个正式文件逐个工作字节/Git blob/SHA256/bytes与delivery/2026-10-11/baseline-identities.json及S一致，预检和最终保护核验均131/131 MATCH。D整仓tree因加入报告/导航而不同于S；不能要求两整仓tree相等。公共登记/历史输入的151/13/14/2/批准JSON和覆盖TSV也匹配，protected-input-check.json有实际结果。

参考R：Maruno17/pokemon-essentials，commit `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`，tree `7589c800b61ba13a13040ed0d686979b80a84fd0`，432跟踪文件工作字节一致/无tracked dirty；仅两.DS_Store忽略项。本地reference目录是独立ignored仓库，不在本报告Git树里。可从同一公开固定R取得：432文件元数据、README body、25保留finding所需64唯一source_evidence文件实际远端body已读回全部匹配（reference-critical-source-readback.json），其余432 body并未声称全部远端读过。云端仍须实际验证能取得必要R输入，拒绝浮动版本替代。

本轮开始local branch review/third-2026-10-11-86b4d7e、HEAD=D/treeD、main/origin-main缓存及live都D；staged/tracked dirty=0，untracked只有旧62停止候选。随后从固定D创建本轮分支codex/review-third-20261012-86b4d7e-a731。静态review结束至首发布时仍HEAD=D，无正式tracked改动，新报告只在新隔离根；首发布后HEAD=A/treeA，main仍D，原62仍未跟踪，新增发布回执会在后续提交。本轮最终local HEAD/tree/staged/tracked/untracked及最终ref由外部实际发布回执给出，不把生成时快照说成之后的终态。

旧STOPPED.md/stop-receipt.json记录M01、本地化补查、M03、M07、M08、M09 interrupted，七模块未启动；旧协调completed为已确认历史证据。实时旧接口有限UNVERIFIED、无具体活动冲突，不恢复旧任务。62候选逐路径/bytes/hash保全，不能PASS/正式接受/完整review。两个停止回执完整字节复制在新legacy-stop-evidence/并有原path/SHA provenance，其余60候选没有云端转移且不作当前结论前提；无须为update恢复它们。

原二次review233总项/229必修/4非必修；第二轮21/21接受、341 scoped贡献、229 CLOSED/0 OPEN与FINAL1/2 PASS仅其原有效范围。旧README/公共字段OPEN/PENDING、B14 9/21、B21候选和current-status.main_merge:false保原历史时点，不能代替实际Git/后继关闭身份。

完整历史输入导航如下，均可在固定D/A相同路径读字节；权威原身份仍以下commit/blob/hash，不把摘要/PASS取代完整资料：

| 用途/权威commit | 相对路径 | bytes | SHA256 | blob |
| --- | --- | ---: | --- | --- |
| 93e10babe0b9c9ef8b3f5277754541b447beeeb4 | review/global-independent-review/2026-10-03-fd82a639/final-report.md | 5472 | 1619c959b928507d4d8b6fa48059aa11861fd8ef4e061ca7247db6287d038a81 | 5159c124f95a84855da8ce8d3f2276e651e8e40e |
| 93e10babe0b9c9ef8b3f5277754541b447beeeb4 | review/global-independent-review/2026-10-03-fd82a639/findings.json | 3148505 | 7c2f0b9159f7be21d8ae9d647399521017500fe4c40ffed042c004492c6a242d | 6f3d96fd99b5a026bb88e463b3ad6e46658e3c01 |
| 41fffb540c6483f5296ea0d33b789b75180d27ed | review/remediation-20261003-prepare/finding-acceptance.json | 2329113 | 54e4c86be3db493a5463ce4bcdef81c7184f1a1d89e6b3bbea358f14cc347225 | e178e5706771f5f7465bcf3351b5c632a5d68bab |
| 41fffb540c6483f5296ea0d33b789b75180d27ed | review/remediation-20261003-prepare/finding-coverage.tsv | 83100 | 4cebdf3aa5aad39e6827a6c7b30f22d1f7b2c729e1fcfa1aefb73ffc7d4cec3f | c87a9c5f90059083fa2e6bd477bdabe6207b18ae |
| c2bc1a341ba6acdf7c8c111dc88d39a162a093d6 | review/remediation/20261003-prepare/FINAL-1/independent-review-cloud-20261011-1/all229-dispositions.json | 6287211 | d7ef9787c4db80bbe408657b693663b47769d19aca1fb3307cc8cd7f7dc64246 | 1f3d84998f8db23f24f944d31a41315b1526d9f1 |
| c2bc1a341ba6acdf7c8c111dc88d39a162a093d6 | review/remediation/20261003-prepare/FINAL-1/independent-review-cloud-20261011-1/findings.json | 4921 | e3fc936255e3dbce444b61881ab17ec8893c356b824f11a702bdd9b0cdb8dcac | 38810222fb2ecd1649dfc938b659dadb11159803 |
| c2bc1a341ba6acdf7c8c111dc88d39a162a093d6 | review/remediation/20261003-prepare/FINAL-1/independent-review-cloud-20261011-1/junction-chain-review.json | 2213588 | d4b2e8bc59c830d9eb3fed15e4c63fa853316ab43e94ae568ecc1e79c2f21b57 | 538b5709b3b435d6011f66f66d82f2b870abde4b |
| c2bc1a341ba6acdf7c8c111dc88d39a162a093d6 | review/remediation/20261003-prepare/FINAL-1/independent-review-cloud-20261011-1/navigation-and-limits.json | 1383781 | 508aa8ba3ad72f313c842af411b753cfd7b239e61b1c8e23f3d84dc54b83bc22 | c19cf107803013b6e534556fe603c3e899116aaf |
| c2bc1a341ba6acdf7c8c111dc88d39a162a093d6 | review/remediation/20261003-prepare/FINAL-1/independent-review-cloud-20261011-1/output-identities.json | 5386 | 29a18b02da7207cc32f121f0cfea54b2617a538190fcae7da81c1d844af71be1 | 853da5014f1c8b9abf5c9a87617af33901721dc0 |
| c2bc1a341ba6acdf7c8c111dc88d39a162a093d6 | review/remediation/20261003-prepare/FINAL-1/independent-review-cloud-20261011-1/public-registry-and-provenance.json | 7436108 | 56bef3922c6fe3061a6e34af5e7b662000f7d42cff8c48a6aa1a44f0651571bf | ba8a8bec3db9dc43dcbb3797bb54d60328df7f32 |
| c2bc1a341ba6acdf7c8c111dc88d39a162a093d6 | review/remediation/20261003-prepare/FINAL-1/independent-review-cloud-20261011-1/publication-readback.json | 4554 | 1f852e967fd81e8c49b1766ea27130cc04f143e819e08d86aeabb023095e855b | 7a3e08971a64c3cbf009c96547d14e0c344792fe |
| c2bc1a341ba6acdf7c8c111dc88d39a162a093d6 | review/remediation/20261003-prepare/FINAL-1/independent-review-cloud-20261011-1/report.md | 9193 | 6a4b77a7b7316023089c8aab8d8fd03b1a5ae8d0606b7179c2e0b03b3ab54e7c | aa827920a0133f6c2159a926e70df75154ad981f |
| ed9ff08085837960f1d940ae5d47faca385982c7 | review/remediation/20261003-prepare/FINAL-2/independent-review-cloud-20261011-1/closure-verification.json | 5191373 | 282049a2b14c9b1ef080cf1e45eb699e2e6a37c8f5495fd416703fb5243c7cbc | 50343f58428345944bc5bcb365bfc6929ecf896c |
| ed9ff08085837960f1d940ae5d47faca385982c7 | review/remediation/20261003-prepare/FINAL-2/independent-review-cloud-20261011-1/findings.json | 4454 | ab5022abca2feef230826f9468df07bcc12dab2c1e0e9a8a1c5d0010c5fed135 | d4ba1cd221dfffddee7c41273ea93be2349f8d25 |
| ed9ff08085837960f1d940ae5d47faca385982c7 | review/remediation/20261003-prepare/FINAL-2/independent-review-cloud-20261011-1/output-identities.json | 4226 | 6975bbb8ecfa9b3e750950d91020f2532491c74897bc34d6d3db67f07178b093 | fd5b6ac65a0884abf290a8aebef7627fb7986010 |
| ed9ff08085837960f1d940ae5d47faca385982c7 | review/remediation/20261003-prepare/FINAL-2/independent-review-cloud-20261011-1/preservation-and-limits.json | 873127 | ee8fc96de4490acfd7b30af6243ae0716550ed0545e17ab5711348169581863e | a3d6f4f387ba31a3fa4f29b6fe266e04ae4fe326 |
| ed9ff08085837960f1d940ae5d47faca385982c7 | review/remediation/20261003-prepare/FINAL-2/independent-review-cloud-20261011-1/publication-readback.json | 3831 | 74579261ec810dacf715698ae38fac611b43121e0ba01c6a20730414d5098a7c | 397238b7350f60c1114ba962aabe60ef6059cf49 |
| ed9ff08085837960f1d940ae5d47faca385982c7 | review/remediation/20261003-prepare/FINAL-2/independent-review-cloud-20261011-1/report.md | 7196 | 1d069ef0d4d4f0805530bdaca8fac227a4818f73783ff3144557188bfc0467bd | 5a4ec465d12e1466e0a1c19b12b1e701fb58056c |
| 167296dbe9e2384627b0ed696e87aeb01f211252 | review/remediation/20261003-prepare/FINAL-closure/registration-cloud-20261011-1/all229-closure-records.json | 632066 | 9445554a062c6d2f7554f91efd8ecabf1c49be93a7e23e36b96d9be29b391ead | a6fc735479505a7fba30bb13b5a825abb5b37bf1 |
| 167296dbe9e2384627b0ed696e87aeb01f211252 | review/remediation/20261003-prepare/FINAL-closure/registration-cloud-20261011-1/all341-public-source-map.json | 493104 | 9560e9e57646d8cd0a6ea4fd352bdf98cf97ce3199df0a2071c72b2b3c61c018 | 98f5286b95c421a13c11e886e6054d43629a8f72 |
| 167296dbe9e2384627b0ed696e87aeb01f211252 | review/remediation/20261003-prepare/FINAL-closure/registration-cloud-20261011-1/completion-statistics-successor.json | 654561 | b36e978c52e480c4c9af813edc8fff23344fa98ca78e1a6197653f062c5da681 | 6e84ba75022cb84453cce20bcc862898dcd9fcbd |
| 167296dbe9e2384627b0ed696e87aeb01f211252 | review/remediation/20261003-prepare/FINAL-closure/registration-cloud-20261011-1/final1-evidence-and-observations.json | 4436 | eddced1ed190425c7ddd3750997760d9a0cfa1d88884afa57c8714509d2beec1 | 982353bc188a65f916e36ccfe2892e250a259b4c |
| 167296dbe9e2384627b0ed696e87aeb01f211252 | review/remediation/20261003-prepare/FINAL-closure/registration-cloud-20261011-1/public-registration-delta.json | 2665 | 161e6647b0a0daf463ba727f7d8e673a6c3bf06466ec12de193b5de88b9450a8 | 19d334d4d07aada31ed2940a8f015964badfc2c6 |
| 167296dbe9e2384627b0ed696e87aeb01f211252 | review/remediation/20261003-prepare/FINAL-closure/registration-cloud-20261011-1/source-limits.json | 1568 | 48f04d1507edeb614bb9180e43a2ad8ff738bc30784c92938ff40d038fdfccdb | 737d2f63723ff68a11a4bd1cb211020240b9dffc |
| 167296dbe9e2384627b0ed696e87aeb01f211252 | review/remediation/20261003-prepare/FINAL-closure/registration-cloud-20261011-1/validation-results.json | 603 | e4167d23a82ca7058433cc232d711b3ab543f7052e0c231d44f7819c78f12bce | b44c988513a5ccef181e1195e01280a8d4791a50 |
| 167296dbe9e2384627b0ed696e87aeb01f211252 | review/remediation/20261003-prepare/FINAL-closure/registration-cloud-20261011-1/closure-summary.md | 887 | 6b4ff92640099f238c748b7920b96915f566ee3cbebaf809082df5764f93d5d0 | 4b4feb004800668b824701731439c89ff8b175a8 |
| 167296dbe9e2384627b0ed696e87aeb01f211252 | review/remediation/20261003-prepare/FINAL-closure/registration-cloud-20261011-1/output-manifest.json | 3878 | 4e2bcaa4fec5ea48f7efa2c104b25f8c60b3bd30f125e0838f05735f7a917996 | e4369ccdd8cce3802ff451b8d8f7fd9d106c999a |
| 167296dbe9e2384627b0ed696e87aeb01f211252 | review/remediation/20261003-prepare/finding-ledger.tsv | 71894 | 06d12c554158480172a8ab18ffa4c1fcff05a0fde0e35d0266ec16c13aba1a8e | 18dfad6c6e70187ff64ab1d6db9d560fb68f6c80 |
| 167296dbe9e2384627b0ed696e87aeb01f211252 | review/remediation/20261003-prepare/approval-ledger.tsv | 792579 | 1bc83944c21054e22c9853dbcfa8400d2f0206ddfd5c1a7cf0b76f61ba3ae137 | 2f0d2f34a48c8f04e78cadb863ffca7e8343615d |
| 167296dbe9e2384627b0ed696e87aeb01f211252 | review/remediation/20261003-prepare/traceability-successor.tsv | 1083545 | 4cc4cd0b42ea5f62b8b8c8ff72eed0cce5c2ac4105c7821c506c0cb5e973a320 | 1958da89a1f85f4388e5d642491450199971b706 |
| 167296dbe9e2384627b0ed696e87aeb01f211252 | review/remediation/20261003-prepare/final-integration-review.md | 106817 | 14f7b2f1885b267c5bd6a0f319a99b71b5f8b54341dd8170750951ffa9ac2ae2 | 9822b0a832b725d8354cf016cee9433d12f57eca |

FINAL1 tree `2a1c6b097c35bd3af07bf663bd9e852cd4cc5bca`；FINAL2 tree `c7b97d9013f9d5a370b5517892273a858d1775fd`。原批准控制41fffb、原全局93e10分别按上表；完整151冻结输入清单在固定delivery/baseline-identities和manifest reviewed_actual，不能用WP/Feature计数扩大批准范围。

## 3. 实际覆盖、独立角色和限制

12模块有限约定范围均COMPLETED；root独立于正式作者/登记，亲审M02/M04/M05及交界裁决；其余9个fresh可见subagent。实际task names/输入/输出/时间/模型和可见方式见progress/module-results；主入口codex://threads/01a12bbf-9300-7833-82d7-d392ae9fa731；subagent只在父会话呈现，没伪造独立Desktop URL。平台4槽含root分批，并非人为3任务上限；未来按真实能力并行或串行。

从原可得入口/调用者/配置/数据/UI/工具建立757分域行为族，含共享交界投影而非互斥Feature数量：601 SUPPORTED_STATIC、139 PARTIAL、7 UNRESOLVED、9 MISSING_MATERIAL、1 NOT_REVIEWED。432来源文件与131正式文件均有独立归属/真实状态；双向表15856条定位含标题/共享行，数量不签行为。不得称全源分支、全内容、全部可得视觉参数或真实运行完整覆盖。

运行观察/参考行为/行为及静态案例/模拟/反序列化/真实Demo链均0。Git/hash/JSON/TSV、PBS字段/Nature25/Mega48/Shadow131/其它有限参数比对、BMP头和HTTP body字节校验是数据或产物检查，不是游戏运行/案例PASS。

真正缺Audio/Graphics/Plugins/Game.ini/Game.rxproj、MapInfos/全部地图/System/Tilesets/CommonEvents/动画数据库及对应编译物/真实录像等；knownpoint.bmp/selpoint.bmp实际可得但区域底图缺，工具/宿主未运行。故事许可/接待/授予/收费奖励/电话登记/解锁/保存恢复/录制回放等真实事件未证。不能由缺资源推功能不存在。

可得却未全审另列：73PBS与18本地化语料全语义/引用闭包、全物种/forms/metrics与设施名单组合/备份启用；部分Transitions逐像素body/墙修复输出/图形helper消费者；完整皮肤字体长词矩阵/摘要坐标/各球粒子颜色曲线/所有反馈文本；二进制Fonts/SF2/exe/DLL/归档内部效果。这些不能用Graphics缺失一概隐藏，按limits审计的能力/文件/解除条件保留，未知不等于无问题。
## 4. 全部canonical findings与可执行结束条件

共25保留ID，23需修（19 P2/4 P3），1 P3可选导航，1 P3完整集合反证后NO_REQUIRED_REVISION；无P1。所有source均R/固定treeR，所有spec均S/固定treeS。下方每项保完整审查字段，支持为静态，不是已修改或已验收。source/spec路径为仓库相对精确路径；blob与条款可解引用。历史签名不迁移到新报告或将来改变的字节。

### GR3-M01-001｜P2｜REQUIRED_REVISION｜翻译文本导入的空白、行首注释和修剪规则未进入往返合同

模块/能力/类别：M01；M01-L05；Generic Kernel / Demo / Developer Experience。处置状态：CONFIRMED；实际reviewer：/root/m01_content_data_v3。
证据层级：SUPPORTED_STATIC; NOT_EXECUTED。
- 来源R：`Data/Scripts/021_Compiler/001_Compiler.rb`；blob `1dd5f374734935f15502f973e07d2a603a1477dd`；定位 154–181；翻译分节读取会跳过空白行与列首井号注释，并修剪保留行的首尾空白。
- 来源R：`Data/Scripts/001_Technical/003_Intl_Messages.rb`；blob `f6c27e5d6efacfa696cfcad018007e9ff1c0a072`；定位 214–240,350–371,397–467,589–611；导出可保留空串译文；转义不保护井号或普通端部空格；导入在分节读取得到内容后才判数组/哈希及行数；当前消息查找允许空译。
- 来源R：`Data/Scripts/001_Technical/003_Intl_Messages.rb`；blob `f6c27e5d6efacfa696cfcad018007e9ff1c0a072`；定位 376–389；完整导入在输入解析前打开并截断输出。
- 规格S：`deliverables/final-specification-set/generic-kernel/wp08-localization.md`；blob `1a206505be5f80375eab1f0a2c121d8368cc0878`；定位 59,80–92,99–100,114–117；已说明运行空译命中、三/两行格式、数字首键形态错误及截断，但没有行过滤与译文修剪的合同。
- 规格S：`deliverables/final-specification-set/test-catalog/generic-kernel-wp05-06-07-08-09-10.md`；blob `eb3d68cc09674cdcfbfa2a9a6b99d6a475a1c9fe`；定位 86,88–95；LZ03证明空译运行语义；LZ05–LZ11未覆盖导入空行/注释行过滤或译文边缘空白。

适用前提：使用成功的作者导出/导入调用；明确非地图 SCRIPT_TEXTS 节；原始键为非空非数字 K，原文有效且默认语料存在。；首例语言译文已为有效空字符串；完整导入另要求旧产物存在且输出成功以覆盖模式打开。；井号例译文首字符为 U+0023；空格例译文为前后各一个 ASCII 空格的非空词。
正常/失败/边界或最小反例：input：K 对应空字符串译文的单条哈希导出；expected：导出留下键行和空译行；导入丢弃空译行，得到奇数条内容并拒绝，旧输出已截断。；input：K 对应以井号起始的单条非空译文；expected：导入把译文行作为注释忽略，同样因奇数条内容拒绝。前置一个空格的井号行先被保留再修剪，是相邻反例。；input：K 对应端部含普通空格的非空译文；对照用受支持的制表符转义；expected：普通端部空格被修剪，导入值改变；控制字符经既有转义恢复，不可概括所有空白均丢失。
当前与应交付事实的差异：current：规格把空字符串描述为有效运行命中，导出/导入格式已分层，却未交代在行数与形态判断前的行删除和所有内容行修剪。；expected：明确消息查找与文本输入可表达集合不同；列出空译、行首井号和端部空格的确定静态结果及其副作用，保留既有数字首键与 Map 的判定优先级。
用户影响：独立实现若按现有两/三行合同完整保留空译或普通端部空格，会与参考作者导入产生不同结果，也会漏测先截断后的失败。；实现风险：兼容导入、提取往返与语言资源更新测试可能误认语料能完整保存空译。
跨模块消费者：作者翻译导出与编译菜单；当前语言脚本文本查找；地图文本与其他文本域（本 finding 的决定向量限定为非地图哈希节）
历史finding/旧候选/去重关系：与 GIR-FD82-A013/A018 的节名和数字首键问题相邻但不同根因；不重开 LZ08–LZ11 已明示失败。；alias：
具体建议（不是已经修复）：在 WP08 作者导入段补行过滤和修剪规则；增加三个具名前提向量，分别覆盖空译、井号及普通端部空格，并把运行空译与文本表达边界连结。
可验证完成标准：正文、测试目录和追溯一致；空译单条哈希先删除空行再因奇数拒绝，完整导入已截断输出。；井号列首与前置空格井号对照保留，普通端部空格与转义控制字符对照保留。；不将本轮静态推导标为已运行往返；保留原 LZ03、LZ08–LZ11 的有效前提与结果。
依赖：M02 文件枚举/诊断；M11 语言界面；M12 翻译菜单；未知/缺资料：真实宿主异常提示、文件系统失败及全量语料受影响数量未验证。
实际root裁决：reviewer：/root；decision：CONFIRMED_WITH_PREMISES_AND_LIMITS；basis：独立module完整领域报告 + root逐项前提/反例及关键source/spec定点复读；具体阅读范围见root-integration-reading-log.tsv。未移转旧审核签名，未运行。
兼容/重设计分类：HISTORICAL_ANOMALY_USER_CHOICE_FOR_FUTURE_IMPLEMENTATION; DOCUMENT_FACT_REQUIRED

### GR3-M01-002｜P2｜REQUIRED_REVISION｜合并地图文本导出可因较早空桶跳过所有较晚有效文本

模块/能力/类别：M01；M01-L04；Generic Kernel / Demo / Developer Experience。处置状态：CONFIRMED；实际reviewer：/root/m01_content_data_v3。
证据层级：SUPPORTED_STATIC; NOT_EXECUTED。
- 来源R：`Data/Scripts/001_Technical/003_Intl_Messages.rb`；blob `f6c27e5d6efacfa696cfcad018007e9ff1c0a072`；定位 299–328；逐地图导出跳过空桶后继续；合并导出检查在遇到首个缺席桶时停止，此前没有非空桶则跳过整个事件域。
- 来源R：`Data/Scripts/001_Technical/003_Intl_Messages.rb`；blob `f6c27e5d6efacfa696cfcad018007e9ff1c0a072`；定位 109–180,573–586；收集为地图编号桶，只在有地图文本时填该桶，可保留稀疏中间编号；共享桶可以为空。
- 来源R：`Data/Scripts/020_Debug/003_Debug menus/002_Debug_MenuCommands.rb`；blob `6dd0c35a31040174efadefa2ba24a1c85a2499f9`；定位 1444–1453；作者菜单确有合并文件与按地图文件选择，选择不同到达这两个分支。
- 规格S：`deliverables/final-specification-set/generic-kernel/wp08-localization.md`；blob `1a206505be5f80375eab1f0a2c121d8368cc0878`；定位 32,74,78–84,99；已描述按图分桶及导出分文件选项，但未记录稀疏桶使合并导出省略整个事件域的条件。

适用前提：默认 game 消息已有效载入，事件域按地图编号分桶；共享桶0为空，地图1桶缺席，地图5桶含一个非空哈希条目；不存在更早非空桶。；目标导出路径可写，默认语料及宿主调用正常；完整提取会先按既有确认流程清除旧文件。；逐地图导出对照另假定 MapInfos 可读；本轮快照没有真实地图，不假定该夹具默认启用。
正常/失败/边界或最小反例：input：选择一个合并地图文本文件；空桶0、缺桶1、非空桶5；expected：检查在桶1停止，未见非空文本，整个 EVENT_TEXTS 文件不生成；桶5文本丢出导出集合。；input：同一桶集合改选每图一个文件且 MapInfos 正常；expected：跳过空/缺桶后继续，可生成 Map005 文本文件。；input：同一合并导出再给桶0或桶1一个非空条目；expected：跳过整个域的条件不成立，随后写出遍历仍可写较晚桶5；不能概括为只导出连续地图编号。
当前与应交付事实的差异：current：分文件选择被列为作者选项，读者无法从规格唯一推出稀疏桶的两种不同输出。；expected：登记合并导出的早期空桶条件、按地图导出相邻对照和已有确认删除在前的部分状态。
用户影响：合法稀疏地图消息可在成功提示前被全部省略；独立实现和测试可能错误承诺两种导出只是排版差异。；实现风险：作者重建翻译材料时难以匹配参考对缺地图编号与空共享文本的输出。
跨模块消费者：M12 作者翻译菜单；M03 地图编号与事件语料；M11 地图事件翻译显示
历史finding/旧候选/去重关系：新能力分支，区别于 A006 导出目标语言和 A013/A018 导入节识别；无旧 ID 重开。；alias：
具体建议（不是已经修复）：WP08 加合并/逐图导出的稀疏桶状态表和三个静态向量；保留来源异常，勿修参考或把例子称已运行地图。
可验证完成标准：空0、缺1、有效5合并不产 EVENT_TEXTS，逐图对照可产 Map005，前置非空桶使合并写出较晚5。；确认覆盖后旧文件可能已删而新事件域未重建，保持先删除时序。；将默认实际数据是否满足前提和运行表现继续标为未知。
依赖：M03 地图材料缺席；M12 翻译导出菜单；未知/缺资料：随附编译默认消息未反序列化，无法判断实际内容是否满足；真实地图和宿主执行=0。
实际root裁决：reviewer：/root；decision：CONFIRMED_WITH_PREMISES_AND_LIMITS；basis：独立module完整领域报告 + root逐项前提/反例及关键source/spec定点复读；具体阅读范围见root-integration-reading-log.tsv。未移转旧审核签名，未运行。
兼容/重设计分类：HISTORICAL_ANOMALY_USER_CHOICE_FOR_FUTURE_IMPLEMENTATION; DOCUMENT_FACT_REQUIRED

### GR3-M01-003｜P2｜REQUIRED_REVISION｜PBS 值在 schema 转换前删去井号后缀，q 原样合同未限定输入层

模块/能力/类别：M01；M01-P03；Generic Kernel / Demo / Developer Experience。处置状态：CONFIRMED；实际reviewer：/root/m01_content_data_v3。
证据层级：SUPPORTED_STATIC; NOT_EXECUTED。
- 来源R：`Data/Scripts/021_Compiler/001_Compiler.rb`；blob `1dd5f374734935f15502f973e07d2a603a1477dd`；定位 72–76,95–129,197–246,690–737；活跃行读取先删第一个井号及其后缀并修剪，再分属性；q 只能保留该预处理后的属性值。
- 来源R：`Data/Scripts/010_Data/002_PBS data/008_Species.rb`；blob `1ce450615687be8ecba5dde48474dd745acda29d`；定位 58–60,91–98；名称和图鉴文本是不同模式，但共享前置行处理。
- 来源R：`Data/Scripts/021_Compiler/001_Compiler.rb`；blob `1dd5f374734935f15502f973e07d2a603a1477dd`；定位 79–86,742–836；普通文本写出只按逗号/引号作 CSV 包围，q 文本直接写；没有井号保护。
- 规格S：`deliverables/final-specification-set/generic-kernel/wp04-pbs-lifecycle.md`；blob `61144bb9750475f289ac85aab7544412b219db15`；定位 60–76,80–90,158；活跃解析段跳过前置注释处理，并将 q 说为整条原始记录原样取用；未说明注释删除不识别引号。
- 规格S：`deliverables/final-specification-set/generic-kernel/wp03-content-identity-and-schema.md`；blob `341b45b6a41a3c48aae82fea53bcc0e320b5aaa8`；定位 108；将 q 仅概括为非格式化文本，需与生命周期实际输入层一致。

适用前提：合法基础物种节，其他字段和宿主调用正常；Pokedex 属性为非空纯文本 Alpha#Beta；对照无井号 AlphaBeta。；普通文本 Name 属性也可给含井号的文本；只调查静态值处理，不据此指认全部随附内容含此字符。；反写对照从登记中已有含井号文本开始，写出与后续编译均成功；不假定其只能由 PBS 初次建立。
正常/失败/边界或最小反例：input：Pokedex 的输入值 Alpha#Beta；expected：先删井号及后缀，登记的图鉴文本为 Alpha；q 不恢复 Beta。；input：无井号的 AlphaBeta；expected：图鉴文本保持 AlphaBeta。；input：登记图鉴文本含井号，正式反写再成功编译；expected：文本输出存在井号，随后同一前置处理丢失后缀；CSV 引号不能保护其作为注释起点的行为。
当前与应交付事实的差异：current：q 的原样表述没有明确原样的起点，PBS 活跃解析也未列出引号无关的注释/空白预处理。；expected：先说明行/属性预处理，随后说明 q 只免除 CSV 值转换；增加普通文本、q、写出再读的边界。
用户影响：未来兼容解析器可能保留参考会丢弃的文本后缀；也会误设字符串无损往返测试。；实现风险：作者文本、电话台词、图鉴与名称值的输入/输出兼容可能分歧。
跨模块消费者：物种名称、图鉴描述；电话 q 台词；本地化默认文本收集；其他 PBS 文本模式字段
历史finding/旧候选/去重关系：与 A001 分词引号位置问题不同：本项发生在分词和 schema 求值之前；保留 KL07–KL10 的准确字符与前提。；alias：
具体建议（不是已经修复）：修订 WP04 活跃解析顺序和 q 原样的范围；增加井号前后缀与反写对照，不把常规 CSV 包围理解为注释保护。
可验证完成标准：明确前置删注释、修剪与 q 求值顺序，井号纯文本例唯一推得 Alpha。；说明存在引号也不保护井号，且写出再读不能承诺保真。；已登记分词、未知属性、重复身份等合同保持；仅静态，不新增来源修复。
依赖：M04 物种/图鉴文本；M11 电话消息；M12 内容作者工具；未知/缺资料：所有随附 PBS/备份语料的井号语义影响数量未完整调查；宿主编译未运行。
实际root裁决：reviewer：/root；decision：CONFIRMED_WITH_PREMISES_AND_LIMITS；basis：独立module完整领域报告 + root逐项前提/反例及关键source/spec定点复读；具体阅读范围见root-integration-reading-log.tsv。未移转旧审核签名，未运行。
兼容/重设计分类：BEHAVIOR_OR_DATA_CONTRACT; FUTURE_ARCHITECTURE_FREE

### GR3-M01-004｜P2｜REQUIRED_REVISION｜电话默认消息的重复节会后项覆盖，不遵守通用重复拒绝结论

模块/能力/类别：M01；M01-I04；Generic Kernel / Creature-RPG / User Interface。处置状态：CONFIRMED；实际reviewer：/root/m01_content_data_v3。
证据层级：SUPPORTED_STATIC; NOT_EXECUTED。
- 来源R：`Data/Scripts/021_Compiler/002_Compiler_CompilePBS.rb`；blob `48e8b782e7175b2631b05d801d6bdcc391b5ddbe`；定位 54–60,1237–1255；通用路径在条目转换后调用该类存在性探测，再决定是否登记；默认节转换为字符串default。
- 来源R：`Data/Scripts/010_Data/002_PBS data/021_PhoneMessage.rb`；blob `adb8856ffe961f8ab61c7eb1a61ecc2b542f2871`；定位 15–29,36–46；存在性探测对姓名空的输入改用类型符号键；不匹配默认节的字符串登记键。
- 来源R：`Data/Scripts/010_Data/001_GameData.rb`；blob `ccfd971a29b3bab107e2da6865ac0050ed3256b0`；定位 78–95；符号型直接登记按条目原身份键替换已有条目。
- 来源R：`Data/Scripts/013_Items/004_Item_Phone.rb`；blob `f98163636a7d6082c2e1a8875ecd6e3b9b8fb007`；定位 447–461；联系人消息缺失时消费默认字符串键；后一条默认记录决定后续台词候选。
- 规格S：`deliverables/final-specification-set/generic-kernel/wp03-content-identity-and-schema.md`；blob `341b45b6a41a3c48aae82fea53bcc0e320b5aaa8`；定位 49,125–127；默认编译/存在性/消费三入口已区分，但通用PBS重复节拒绝表没有电话默认节例外。
- 规格S：`deliverables/final-specification-set/generic-kernel/wp04-pbs-lifecycle.md`；blob `61144bb9750475f289ac85aab7544412b219db15`；定位 85–88；再次把同一身份第二个通用节概括为拒绝，未限定默认电话登记键。
- 规格S：`deliverables/final-specification-set/test-catalog/generic-kernel-wp02-03-04.md`；blob `0f7d359a6cecc3b887cde604461b43f85162e689`；定位 25–27,51–52；KR06只检查默认三入口；KL15和重复规则没有默认电话正反对照。

适用前提：当前固定类查询未被插件覆写；普通合法电话PBS输入经compile_phone进入通用路径；所有依赖与宿主调用正常。；同一输入给两个合法 Default 节，每节只含一条不同的非空 Intro 台词；没有其他登记或混合来源文件。；联系人重复对照另给已登记有效训练家类型、同姓名同版本和合法内容；不得借默认键失败泛化所有电话条目。
正常/失败/边界或最小反例：input：第一个Default消息含台词A；第二个Default消息含台词B；expected：两个默认节均通过重复探测；后节替换前节，最终默认记录只含B；终检文本收集以B为输入候选，后续默认台词消费者取B再按当前语言查找，最终显示文本由本地化命中决定。；input：两个合法电话联系人节具有相同类型、姓名、版本；expected：三元键探测命中，第二节在登记前拒绝；此前第一条登记不由该错误自动回滚。；input：两个合法同ID普通道具节；expected：正常通用存在性探测命中并拒绝，与默认电话入口形成邻近反例。
当前与应交付事实的差异：current：把通用PBS入口作为统一重复拒绝规则，同时只在身份例外处说明电话三个键入口不同，未写由这种差异产生的编译结果。；expected：重复规则必须明确电话默认节按字符串登记但探测不命中，因此后项覆盖；联系人三元键重复仍拒绝。
用户影响：独立兼容编译器和测试会错误拒绝参考可接受并覆盖的输入，或错误把所有电话重复都允许。；实现风险：电话默认台词候选、默认文本收集和多文件合并顺序结果不同。
跨模块消费者：电话消息默认回退与台词抽样；编译终检本地化默认文本收集；M11 联系人界面；M12 内容作者工作流
历史finding/旧候选/去重关系：与G1-4登记默认键/三入口交界有关，但新发现为该身份差异的实际重复编译消费结果；不把已关闭默认三入口历史裁决重开。；alias：
具体建议（不是已经修复）：WP03重复表及WP04新身份/重复身份段增加按类默认例外；测试补默认后项覆盖、同三元联系人拒绝与普通道具拒绝对照。
可验证完成标准：两Default节最终只保留后者；电话取值候选与本地化收集输入一致，不把取值候选直接等同于当前语言显示。；联系人重复仍在第二次登记前拒绝，普通道具重复拒绝不变。；保持当前默认三入口区别，不改变源实现或推为未来架构。；例子标为静态未执行，不声称当前随附phone.txt存在重复默认节。
依赖：M11 电话消息消费者；M12 作者编译与错误显示；未知/缺资料：两个默认节在同一路径的静态结果确定；实际随附编译、跨文件发现顺序与宿主错误画面未运行。
实际root裁决：reviewer：/root；decision：CONFIRMED_WITH_PREMISES_AND_LIMITS；basis：独立module完整领域报告 + root逐项前提/反例及关键source/spec定点复读；具体阅读范围见root-integration-reading-log.tsv。未移转旧审核签名，未运行。
兼容/重设计分类：HISTORICAL_ANOMALY_USER_CHOICE_FOR_FUTURE_IMPLEMENTATION; DOCUMENT_FACT_REQUIRED

### GR3-M02-001｜P2｜REQUIRED_REVISION｜通知回调抛错后的停止和部分状态未进入扩展合同

模块/能力/类别：M02；通知失败顺序；Generic Kernel。处置状态：CONFIRMED；实际reviewer：/root。
证据层级：SUPPORTED_STATIC / SOURCE_STATIC_DERIVATION; NOT_EXECUTED。
- 来源R：`Data/Scripts/003_Game processing/005_Event_Handlers.rb`；blob `8e6f098cca94ff0cc0eec730335a91295f4847be`；定位 40–58;88–90；回调按序直接调用，没有逐回调捕获或回滚
- 来源R：`Data/Scripts/003_Game processing/006_Event_HandlerCollections.rb`；blob `807311c0e0f6835ebce56c0006115392cab4658b`；定位 62–64；命名事件触发沿同一调用路径
- 来源R：`Data/Scripts/012_Overworld/001_Overworld.rb`；blob `e95754925d6eea2735a22e9dfe5a8414fc7e3ab6`；定位 202–218；普通步计数写入先于两个玩家步通知
- 规格S：`deliverables/final-specification-set/generic-kernel/wp05-events-extensions-plugins.md`；blob `cad8f67dfa267d3b082c58f31f823d862474b8c8`；定位 §3.1–3.2;§7；说明依次调用全部，失败表只列插件错误
- 规格S：`deliverables/final-specification-set/test-catalog/generic-kernel-wp05-06-07-08-09-10.md`；blob `eb3d68cc09674cdcfbfa2a9a6b99d6a475a1c9fe`；定位 EP01–EP05；没有回调中断/部分提交对照

适用前提：已登记回调顺序为 A、B、C，A 正常完成，B 抛出异常；无扩展为触发入口补捕获，无更早失败，不讨论并发增删订阅；消费者在触发前或 A 内已有状态写入
正常/失败/边界或最小反例：normal：A/B/C 均正常返回则按序全部执行。；failure：A 把可见状态从 0 写为 1，B 抛错：C 不执行；状态保留 1，异常传向触发调用者。普通迈步中的计数也已发生，不能当作未迈步。；boundary：B 位于首位时没有先前回调副作用；B 位于末位时所有前项已发生。调试主流程的外层诊断不是继续本次通知的保证。
当前与应交付事实的差异：current：泛称依次调用全部；没有异常导致剩余回调跳过、既有写入保留和触发方中断的合同。；expected：限定正常完成的全调用保证，并用独立行为文字说明异常传播/停止/无事务撤回及外层处理边界。
用户影响：扩展作者和实现团队可能隔离回调错误后继续执行，导致步数、遇敌、孵化或UI消费者顺序与参考不同。；实现风险：共享事件链的失败语义不确定，可能重复推进或在已失败的状态上继续推进。
跨模块消费者：M03 世界步进/转移；M06 步数/遭遇/孵化；M10 菜单扩展；M11 野外被动
历史finding/旧候选/去重关系：relation：NEW_SCOPE；notes：原事件参数/身份/插件控制保持原限定；不是据旧PASS重开原229。；alias：
具体建议（不是已经修复）：补通知正常/失败/边界合同及测试设计，保留消费者已提交状态；无需规定事件总线或语言异常类型。
可验证完成标准：仅凭最终集可确定 A正常、B失败、C被跳过的顺序与状态；说明普通步计数发生在回调异常前，外层捕获不恢复本次调用；新增首项/中项/末项异常与全正常对照；未执行标识保留
依赖：M03/M06/M11 通知消费者交界；未知/缺资料：回调在触发期间增删订阅的宿主细节未穷尽，不以此项补写无限事件变体。
实际root裁决：reviewer：/root；decision：Independent primary actual substantive module review; new formal gap only；basis：review/global-independent-review/third-2026-10-12-86b4d7e-manual-a731/M02/report.md
兼容/重设计分类：BEHAVIOR_OR_DATA_CONTRACT; FUTURE_ARCHITECTURE_FREE

### GR3-M02-002｜P2｜REQUIRED_REVISION｜持久值重复身份的保存、读取和撤销语义缺失

模块/能力/类别：M02；持久状态登记碰撞；Generic Kernel。处置状态：CONFIRMED；实际reviewer：/root。
证据层级：SUPPORTED_STATIC / SOURCE_STATIC_DERIVATION; NOT_EXECUTED。
- 来源R：`Data/Scripts/002_Save data/002_SaveData_Value.rb`；blob `e4391327e67163b38b90707528efc0243625a4dd`；定位 195–207;220–231;279–283；登记追加而不按ID替换；撤销移除所有同ID；保存后取值覆盖先值；读取依序调用各登记
- 规格S：`deliverables/final-specification-set/generic-kernel/wp09-save-startup-continue.md`；blob `504d45cd7ebcd40cf039568080acabc3d3a277fa`；定位 §3.1；只列单项配置与读值/加载标记，无碰撞行为
- 规格S：`deliverables/final-specification-set/test-catalog/generic-kernel-wp05-06-07-08-09-10.md`；blob `eb3d68cc09674cdcfbfa2a9a6b99d6a475a1c9fe`；定位 SV08–SV11；未给重复登记身份对照

适用前提：动态作者/插件登记两个合法持久值，身份相同，保存值依次为 10 和 20；两项类型约束相容且取值/加载回调均正常，无此前标记跳过；仅分析登记接口，不宣称现有17项默认登记存在重复或缺失插件组合已运行
正常/失败/边界或最小反例：normal：不同身份各自形成保存键并加载一次。；failure：若同身份两个约束不相容，数据有效性检查要求两者均通过；保存最后值不能自动证明同时满足前者。；boundary：相同身份两正常登记：保存取值两次、最终键值20；读回同一20时两项加载回调依次各执行一次；撤销该身份移除两项。不是同键后项替换前项的事件/内容登记规则。
当前与应交付事实的差异：current：可配置持久值目录没有说明身份碰撞、重复回调和撤销范围。；expected：给出可观测登记碰撞行为与默认唯一身份范围；独立框架可重设计组织，但兼容策略不得默默套用其它注册表的替换规则。
用户影响：插件作者或未来迁移实现可能只保留后项，改变取值副作用、加载先后、有效性判断及卸载结果。；实现风险：保存字面看似正常，加载却遗漏或重复处理状态；冲突约束可能使存档不可用。
跨模块消费者：M01 内容身份/注册查询；M02 保存/启动/迁移；M12 作者扩展工具
历史finding/旧候选/去重关系：relation：NEW_NONDEFAULT_REGISTRATION_SCOPE；notes：现有17默认登记及旧缺键/加载门控制未否定；独立新证据不扩大旧229接受范围。；alias：
具体建议（不是已经修复）：补架构中立的同身份登记/保存/读取/撤销正常、失败与边界规则；若未来选择拒绝重复身份，列为用户明确的兼容决策。
可验证完成标准：10/20同身份向量明确最后保存值、两次取值/加载顺序与撤销全移除；类型约束冲突与已加载门分开说明；不要求复制源容器/类结构，不宣称默认游戏存在重复身份
依赖：M01 登记机制比较；M12 动态扩展范围；未知/缺资料：真实插件如何重复登记未有样本。
实际root裁决：reviewer：/root；decision：Independent primary actual substantive module review; new formal gap only；basis：review/global-independent-review/third-2026-10-12-86b4d7e-manual-a731/M02/report.md
兼容/重设计分类：HISTORICAL_ANOMALY_USER_CHOICE_FOR_FUTURE_IMPLEMENTATION; DOCUMENT_FACT_REQUIRED

### GR3-M02-003｜P3｜NO_REQUIRED_REVISION｜无旧存档紧急保存的备份提示未与实际备份状态分开

模块/能力/类别：M02；紧急保存反馈；User Interface / Generic Kernel。处置状态：DISPUTED；实际reviewer：/root。
证据层级：SUPPORTED_STATIC / SOURCE_STATIC_DERIVATION; NOT_EXECUTED。
- 来源R：`Data/Scripts/016_UI/014_UI_Save.rb`；blob `62ba8dc5e9825531ebdc5d5a34f797281043d3ea`；定位 1–24；复制备份受旧存档门控制，但成功保存分支恒显示已备份提示
- 规格S：`deliverables/final-specification-set/generic-kernel/wp10-migration-failure-recovery.md`；blob `a2164b3e92587d3f3dd1d1748f4124f3f5f52bdd`；定位 §5.2 line127；仅说明旧档已备份在旧档实际存在时成立，没有明确同样提示仍出现
- 规格S：`deliverables/final-specification-set/test-catalog/generic-kernel-wp05-06-07-08-09-10.md`；blob `eb3d68cc09674cdcfbfa2a9a6b99d6a475a1c9fe`；定位 MG07；无旧存档前提未登记恒显示的反馈
- 规格S：`deliverables/final-specification-set/test-catalog/user-interface-wp17-63-65-66-67-68-69-70-71.md`；blob `2744e1010109bafd3e9314e41cea66ecd0d04140`；定位 T15；有旧档两提示已给，无旧档成功对照缺失

适用前提：脚本超时进入紧急保存，玩家可保存，开始时默认存档不存在；保存及两条消息调用成功，没有更早异常；无独立已有.bak输入
正常/失败/边界或最小反例：normal：有旧档则先复制备份，保存成功后显示已保存与已备份两提示。；failure：保存失败进入保存失败提示；未进入成功提示分支。；boundary：无旧档则跳过复制，保存成功仍显示已保存与已备份两提示；本次并未创建旧档备份。
当前与应交付事实的差异：current：完整允许材料已确定无旧档保存成功仍两提示，备份操作未执行。WP10单段可加强导航，但不是必需合同缺失。；expected：保持既有合同；未来若用户选择更明确例子或修正误导提示，作为可选/兼容决定。
用户影响：复刻UI、设计测试或解释灾难恢复时可能错误认为出现备份提示即证明备份存在。；实现风险：UI回执被用作文件状态证据，造成错误恢复承诺。
跨模块消费者：M10 保存UI；M02 超时/恢复
历史finding/旧候选/去重关系：relation：REFINES_EXISTING_MG07_SCOPE_WITH_NEW_UI_EVIDENCE；notes：保留MG07无旧档也可保存及实际备份门；不改变旧229关闭结论，追加此前未明示的反馈分支。；alias：
具体建议（不是已经修复）：不列本轮必修；可选加入无旧档双提示显式案例，未来提示修正仍由用户决定。
可验证完成标准：无旧档成功向量同时给出提示序列和备份操作未执行；不把提示视为备份存在证明；保留有旧档/保存失败/无玩家的分支与未运行限定
依赖：M10 保存UI合同；未知/缺资料：真实超时/宿主消息显示未运行。
保留原提交：status：CONFIRMED；disposition：REQUIRED_REVISION；current_vs_expected：current：规定备份事实成立的条件，但读者无法唯一确定无旧档成功时的实际提示。；expected：分别记录文件操作事实与恒显示提示；登记这是参考的误导反馈，未来修正与否待用户决定。；recommendation：补无旧档且保存成功的两提示与无新备份文件对照，明确未来是否修正提示为用户选择。
保留独立反证：reviewer：/root/m10_ui_contracts_v3；scope：WP65 §4.2 + WP10 §5.2 complete allowed formal set；decision：DISPUTED / OPTIONAL; no required new gap；reason：Existing-file gate binds copy only; success dual messages unconditionally stated; no-player direct return qualifies final restore. Complete set uniquely determines behavior.
实际root裁决：reviewer：/root；independent_peer：/root/m10_ui_contracts_v3；decision：NO_REQUIRED_REVISION; explicit added example OPTIONAL only；basis：Root重新读UI_Save1–24、WP65§4.2 line90、WP10§5.2 line127–128。旧档存在只约束复制，保存成功两消息在WP65已无条件陈述，WP10区别备份事实并限制恢复。完整131允许集合可唯一推无旧档成功两提示/未复制；原候选把WP10局部遗漏扩大为整集缺口。；preservation：原M02/findings.json与此original_submission/peer_counterevidence均保留，不删ID，不改旧229。；evidence_level：SUPPORTED_STATIC; NOT_EXECUTED
兼容/重设计分类：BEHAVIOR_OR_DATA_CONTRACT; FUTURE_ARCHITECTURE_FREE

### GR3-M03-001｜P2｜REQUIRED_REVISION｜地图镜头卷动的速度、钳边与脚本等待能力没有形成独立合同

模块/能力/类别：M03；M03-C04；Engine / Overworld Integration。处置状态：CONFIRMED；实际reviewer：/root/m03_world_maps_v3。
证据层级：SUPPORTED_STATIC; runtime=0。
- 来源R：`Data/Scripts/004_Game classes/004_Game_Map.rb`；blob `3fda78303080bf7be450d110ecaf9df834bec691`；定位 323–393;439–460;497–565；镜头位置钳边、方向/双轴卷动、以单调时钟按速度等级插值、即时及等待包装均可静态审查。
- 来源R：`Data/Scripts/010_Data/002_PBS data/018_MapMetadata.rb`；blob `0f9bd8a556d8f352148da0047e7d387c625a544c`；定位 15;46;105；SnapEdges是可配置布尔能力。
- 来源R：`Data/Scripts/016_UI/020_UI_PokeMart.rb`；blob `e91b66e29e0b26b691ec5b8f4c06d5902f4911e7`；定位 244;349;362；商店场景实际调用地图卷动包装；默认脚本文本消费者，不只是未启用定义。
- 规格S：`deliverables/final-specification-set/engine-overworld/wp16-world-rendering-and-visual-transitions.md`；blob `5da79732e7b8a42a052fb1a16833a8516768e51d`；定位 §3.1 L23–29;§6 L203–213；仅规定滚动输入与绘制量化，未定义镜头输入生成/速度/边界。
- 规格S：`deliverables/final-specification-set/engine-overworld/wp13-interpreter-command-matrix.md`；blob `0adc7b28608ba8010713be9d879d52bc41ac73a6`；定位 203行 L58；只承接已卷动等待和新卷动立即继续；方向/距离/速度未给可判据语义。
- 规格S：`deliverables/final-specification-set/test-catalog/engine-overworld-wp16.md`；blob `4fb56f7a4e0f6f84ee7ec4a9a11b37cf713c2c1f`；定位 WR01–WR04 L9–12；测试覆盖投影/量化/拼接，不覆盖卷动速度、SnapEdges或即时/阻塞包装。

适用前提：有效地图、系统与正常更新机会；无插件、额外镜头写入或地图切换；距离以格计、显示以128子像素/格计。；正常速度等级4；单调时间持续推进；先将SnapEdges关闭；另外用512×384屏幕和30×20地图开启SnapEdges作边界对照。
正常/失败/边界或最小反例：input：向右卷动1格，速度4，起点显示x=0；经过0.1/0.2秒获得地图更新。；reference_result：显示x分别64/128子像素，0.2秒此轴结束；事件203发起后不等待，但脚本卷动包装循环更新到结束。；current_spec_result：无法仅由正式合同计算0.1秒位置及结束点，也没有包装阻塞和即时速度0的判据。；input：开启SnapEdges，30×20地图、512×384屏幕，分别请求负显示坐标和超过远侧边界的坐标；对照小于屏幕的地图。；reference_result：每轴下界0，上界为剩余可视格数×128；负上界时仍归0。小地图不能按无限滚动处理。
当前与应交付事实的差异：current：已有绘制量化和事件启动门，但完整镜头能力的输入、速度、边界、即时/等待分流没有承接。；expected：补实现无关的镜头合同：每轴距离/速度等级对应名义秒数、双轴分别完成、合法方向、SnapEdges钳边、速度0即时、居中入口校验与包装等待；保持投影量化合同。
用户影响：另一个独立实现不能从正式材料确定镜头可达范围、商店进出卷动节拍及事件与脚本调用的继续时机。；实现风险：可能误套角色移动速度、把脚本包装当非阻塞、或允许SnapEdges地图越过可视边界。
跨模块消费者：M10商店/UI场景；M11纸牌场景；M01地图元数据编译
历史finding/旧候选/去重关系：本轮独立能力分母新增；非旧C049 NPC移动或C069具名视觉过渡，未使用旧PASS。；alias：
具体建议（不是已经修复）：补镜头行为族及静态案例；只修改规格/测试设计，不实现框架或修参考。
可验证完成标准：给出速度1–6一格名义时长1.6/0.8/0.4/0.2/0.1/0.05秒或等价数学规则，并区分角色移动速度表。；给出方向无效/双轴距离/各轴结束、SnapEdges正常和小地图钳边案例。；区分203立即继续、脚本包装等待、速度0即时；居中目标/速度校验失败应无卷动。；明确素材/地图缺失不阻止上述静态机制，而实际镜头画面仍未验证。
依赖：地图元数据SnapEdges；单调时钟与地图更新机会；显示坐标单位与量化；未知/缺资料：真实地图/素材与运行画面缺失；不证明演示事件可达。；未来是否选择同等镜头能力由后续架构决定，审查要求保留当前行为事实。
实际root裁决：reviewer：/root；decision：CONFIRMED_WITH_PREMISES_AND_LIMITS；basis：独立module完整领域报告 + root逐项前提/反例及关键source/spec定点复读；具体阅读范围见root-integration-reading-log.tsv。未移转旧审核签名，未运行。
兼容/重设计分类：BEHAVIOR_OR_DATA_CONTRACT; FUTURE_ARCHITECTURE_FREE

### GR3-M03-002｜P2｜REQUIRED_REVISION｜地牢建立通知也可由未驻留地图查询触发，边缘不重生成的陈述缺少前提

模块/能力/类别：M03；M03-C17；Engine / Overworld Integration。处置状态：CONFIRMED；实际reviewer：/root/m03_world_maps_v3。
证据层级：SUPPORTED_STATIC; runtime=0。
- 来源R：`Data/Scripts/004_Game classes/005_Game_MapFactory.rb`；blob `0657b0f2d3a35e68fe8d1add1b855a167c3f7575`；定位 54–92;157–169;203–206;307–309；未驻留地图查询仍建立临时地图；不加入集合只影响驻留，不跳过建立通知。
- 来源R：`Data/Scripts/004_Game classes/004_Game_Map.rb`；blob `3fda78303080bf7be450d110ecaf9df834bec691`；定位 45–68；地图建立通知在创建事件前触发。
- 来源R：`Data/Scripts/012_Overworld/008_Overworld_RandomDungeons.rb`；blob `f3fffad94dbe64af0dbf6033bc22e1735dde7ae8`；定位 428–450;1063–1116；任一对应建立通知均受地牢标记驱动；无正式传送标记/当前地图身份的额外守卫。生成重播随机并消费待播种子，成功玩家摆放写传送暂存。
- 规格S：`deliverables/final-specification-set/engine-overworld/wp14-random-dungeons.md`；blob `fbe44a380025e809085ed230b8aa32ea2bdd62ea`；定位 §3.1 L25–29;§3.5 L73–79；描述建立通知及副作用，但声称边缘切图不触发重新生成，未限定目标已驻留，也无查询临时建立的副作用。
- 规格S：`deliverables/final-specification-set/engine-overworld/wp11-map-topology-transfer.md`；blob `b84fff503062df6e26b2a8902b0e7ab5a7e85707`；定位 §3.1;§5.2 L77–82；按图ID建立/复用，未分清不加入集合的查询加载同样有建立通知。

适用前提：当前地图A和目标地图B都可正常读取；B不在已加载集合且元数据地牢标记为真；参数和图块集有效且生成与摆放正常完成；无插件。；先记录玩家当前地图A、待播种子S及旧传送暂存坐标；从A请求B的地形或连接目标通行查询，不排队正式传送。
正常/失败/边界或最小反例：input：连续两次对未驻留B查询地形；两次间B仍不在集合。；reference_result：每次查询都建立临时B并触发地牢生成；第一次清待播种子并重播全局随机，成功玩家摆放可写传送暂存；临时B没有因查询而驻留。第二次仍可再次生成。；current_spec_result：仅从列举的重建/进入流程及边缘不重新生成陈述，无法确定这种查询有生成与持久/暂存副作用。；input：合法连接跨缘通行预检查时B尚未驻留；反向对照B已驻留且无重建。；reference_result：未驻留B先经临时建立/生成；已驻留B复用，不触发新的建立通知。
当前与应交付事实的差异：current：把生成触发概括为地图建立，却将边缘链写成无重生成，并缺少临时查询入口及其副作用。；expected：区分已驻留复用与未驻留临时建立；每次实际建立都可触发生成，临时查询也可消费种子、影响全局随机及成功时写玩家传送暂存。
用户影响：独立实现可能把查询当纯读，生成次数、种子消费和随后传送坐标与参考不同。；实现风险：连接/地形消费者可能取得不同生成布局；失败阶段及随机服务污染被误删。
跨模块消费者：M02随机服务与步进消费者；M11场地地形查询；M01地图/元数据加载；M03边缘通行和地图地形查询
历史finding/旧候选/去重关系：新交界，旧C044/C045/C047仅为单次生成内部失败，不覆盖临时查询建立；原固定身份语义可以复用，但旧PASS不是此能力证据。；alias：
具体建议（不是已经修复）：记录静态历史行为及失败/正常前缀；未来是否保留这种查询副作用单独交用户决策，不修参考。
可验证完成标准：边缘无重新生成只绑定已加载目标复用条件。；新增查询未驻留地牢图与已驻留对照；确定待播种子/随机重播/暂存坐标观察点。；普通非地牢查询建立仅保留对应建立通知，不能泛化为所有查询都写暂存。；失败时按构造/生成/摆放阶段保留已提交前缀；实际默认地图标记与可达性保持MISSING_MATERIAL。
依赖：地图驻留与建立通知；地牢元数据门；全局随机服务；传送暂存字段；未知/缺资料：缺真实地图，无法证明Demo默认启用或查询链真实可达；运行=0。；未来是否复刻查询副作用属于USER_DECISION，当前规格事实补充为REQUIRED_REVISION。
实际root裁决：reviewer：/root；decision：CONFIRMED_WITH_PREMISES_AND_LIMITS；basis：独立module完整领域报告 + root逐项前提/反例及关键source/spec定点复读；具体阅读范围见root-integration-reading-log.tsv。未移转旧审核签名，未运行。
兼容/重设计分类：HISTORICAL_ANOMALY_USER_CHOICE_FOR_FUTURE_IMPLEMENTATION; DOCUMENT_FACT_REQUIRED

### GR3-M03-003｜P2｜REQUIRED_REVISION｜SPECIAL触发的具名过场跳过与事件重新启动能力未承接

模块/能力/类别：M03；M03-C15；Engine / Overworld Integration; User Interface。处置状态：CONFIRMED；实际reviewer：/root/m03_world_maps_v3。
证据层级：SUPPORTED_STATIC; runtime=0。
- 来源R：`Data/Scripts/004_Game classes/002_Game_System.rb`；blob `95c749329ff95b417f38e96c42ea0a1feb29dbe5`；定位 279–287；系统逐更新机会检查SPECIAL与当前地图事件注释；置自开关A、结束解释器并重新启动事件。
- 来源R：`Data/Scripts/007_Objects and windows/011_Messages.rb`；blob `91c985bd0fda9a2368c894dee0ebbc9a476e9886`；定位 26–50；注释入口接受108/408且完整文本严格相等；返回数组即使为空仍通过存在性门。须主解释器运行且可取当前事件。
- 来源R：`Data/Scripts/003_Game processing/003_Interpreter.rb`；blob `21666002e7f4038dd3763b632538becaae5f8d7d`；定位 323–330；自开关写入按解释器地图/事件身份；值变化才请求已加载地图刷新。
- 来源R：`Data/Scripts/003_Game processing/002_Scene_Map.rb`；blob `8be1640f36b293f44329a3bbe6ccf3e13fb0d825`；定位 121–133;165–178；正常和迷你地图更新都会调用系统更新；它早于末端快捷按键门。
- 规格S：`deliverables/final-specification-set/engine-overworld/wp13-map-events-npc-followers.md`；blob `919807ef81368d5a7198e63291680d07d253c04c`；定位 §3–4;§4.2 L66–72；已有一般启动和三类终止，但无具名过场跳过消费者。
- 规格S：`deliverables/final-specification-set/engine-overworld/wp12-terrain-movement-vehicles.md`；blob `53157503985f9200d321b0361c9de25cc21fa36f`；定位 §4.3 L148–154；SPECIAL末端快捷登记/消费并非系统更新中的过场跳过门。
- 规格S：`deliverables/final-specification-set/test-catalog/engine-overworld-wp11-15-59-60.md`；blob `90d0b2513cbcde582ad62189efae93153ccbeab1`；定位 EV01–39;MV55–56/MV68–77；无过场注释精确识别、A开关和终止后重新启动向量；不应由末端快捷规则替代。

适用前提：有效地图场景及运行中的主解释器，事件ID仍能解析到当前事件，当前事件命令列表含注释完整文本Cut Scene；SPECIAL为本次触发。；开关A初值假、事件列表非空且含正文命令；正常系统更新与所有被调用通知返回，未发生其它状态写入。
正常/失败/边界或最小反例：input：系统更新机会收到SPECIAL；注释合法，当前事件仍存在。；reference_result：先将该解释器身份的自开关A置真并请求刷新，再结束当前命令列表/跟随覆盖/有效主事件解锁，随后标记同事件待启动；并非只打开快捷菜单或从原索引继续。；input：只改注释为cut scene、Cut Scene尾随空格，或主解释器未运行/当前事件不存在。；reference_result：严格文本或上下文门不成立，无此过场跳过副作用。；input：完整注释为列表末端，后续一项不存在，注释读取结果为空数组。；reference_result：门仍视为存在；不要求数组必须含下一项参数。
当前与应交付事实的差异：current：规格仅定义一般解释器终止与地图末端SPECIAL快捷登记。；expected：补独立跳过合同：严格注释语法、上下文和输入门、写A→结束→重新启动顺序、刷新与下一页时机；空数组/空值分开。
用户影响：该可得功能无法被独立实现或测试设计发现；作者标注可跳过的事件会按普通快捷菜单处理或不能切到结束页。；实现风险：错误共享末端解释器阻塞门，会彻底禁用运行中事件的跳过；或误认为清解释器即可，不标记重启。
跨模块消费者：M10键输入/快捷菜单合同；M12事件作者工作流；M02系统更新/通知失败前缀
历史finding/旧候选/去重关系：独立分母发现，旧C039/C053只涵盖预读/选项，不覆盖系统更新消费者；空数组与nil区别与G7-1交界一致。；alias：
具体建议（不是已经修复）：提取用户可见过场跳过行为；不复制参考结构，不运行/修补参考。
可验证完成标准：正文给出严格Cut Scene全文兼容输入和108/408注释条件。；给出正常顺序、自开关已真/已假对照、有效/失联事件对照以及空数组门。；明确系统更新早于地图末端SPECIAL登记，因此不能套末端主解释器未运行门。；保留缺地图事件的实际启用/可达性未知和0运行。
依赖：主解释器当前事件上下文；SPECIAL触发输入；自开关刷新/事件页选择；地图系统更新；未知/缺资料：缺真实事件数据，不能证明Demo有可跳过事件或实际页切换结果。；输入消费后同轮快捷标记是否也产生须结合消费者门具体分析，不能声明独占输入。
实际root裁决：reviewer：/root；decision：CONFIRMED_WITH_PREMISES_AND_LIMITS；basis：独立module完整领域报告 + root逐项前提/反例及关键source/spec定点复读；具体阅读范围见root-integration-reading-log.tsv。未移转旧审核签名，未运行。
兼容/重设计分类：BEHAVIOR_OR_DATA_CONTRACT; FUTURE_ARCHITECTURE_FREE

### GR3-M03-004｜P2｜REQUIRED_REVISION｜地图事件变更记录的读档清空及条件恢复副作用未形成合同

模块/能力/类别：M03；M03-C47；Engine / Overworld Integration; Generic Kernel。处置状态：CONFIRMED；实际reviewer：/root/m03_world_maps_v3。
证据层级：SUPPORTED_STATIC; runtime=0。
- 来源R：`Data/Scripts/012_Overworld/002_Overworld_Metadata.rb`；blob `148211a6c6f94ed0219134f52dcfff817e6bd0fd`；定位 144–182；记录消去及移动位置/朝向/穿透；恢复的位置朝向受记录地图匹配门，真穿透写入在该门外，假值不写。
- 来源R：`Data/Scripts/003_Game processing/001_StartGame.rb`；blob `983349abcd8e66180ab173e949a738d0530d12d5`；定位 63–104；普通读档恢复图后更新图，再调用记录恢复辅助；两条地图恢复分支均发送进入通知。
- 来源R：`Data/Scripts/012_Overworld/001_Overworld.rb`；blob `e95754925d6eea2735a22e9dfe5a8414fc7e3ab6`；定位 224–237；进入通知第一消费者清全部局部地图记录。
- 来源R：`Data/Scripts/004_Game classes/005_Game_MapFactory.rb`；blob `0657b0f2d3a35e68fe8d1add1b855a167c3f7575`；定位 17–27;142–153；同ID实际重建在旧ID非零时仍发离开通知，非重建标记变更仅进入通知。
- 规格S：`deliverables/final-specification-set/engine-overworld/wp11-map-topology-transfer.md`；blob `b84fff503062df6e26b2a8902b0e7ab5a7e85707`；定位 §5.2;§6 L90–94;§4读档恢复行；只规定实例/临时自开关与持久状态，未交付局部消去/移动记录的清空和恢复链。
- 规格S：`deliverables/final-specification-set/generic-kernel/wp09-save-startup-continue.md`；blob `504d45cd7ebcd40cf039568080acabc3d3a277fa`；定位 map_metadata行 L59;§4.1 L78–79；保存单元与重建门存在，但对象字段语义明确交领域；本领域未承接记录清空及恢复顺序。
- 规格S：`deliverables/final-specification-set/engine-overworld/wp13-map-events-npc-followers.md`；blob `919807ef81368d5a7198e63291680d07d253c04c`；定位 §3.1;§4.2；消去/结束已有，未区分消去实例与记录状态、条件恢复辅助。

适用前提：正常Game.load、有效存档单元与地图、进入通知/图更新都正常返回，无插件或介入写入；原局部地图记录至少含一条移动/消去条目。；条件辅助反例另给：记录仍在（直接能力输入或进入清空之后显式追加），当前图B；唯一记录图A≠B、事件ID7、记录位置(8,8)、朝向下、穿透真；B有事件7原位(2,2)、朝向右、穿透假。此条件不宣称默认读档保留旧记录。
正常/失败/边界或最小反例：input：普通读档，标记一致且非安全保存；对照需要同ID重建的有效读档。；reference_result：两条路径都发进入通知并清局部地图记录；无后续新写入时恢复辅助看到空记录。已有加载实例可保留其状态；重建实例状态另由页数据建立，不能保证旧移动记录再次恢复。重建旧ID非零时会有离开通知，同ID非重建路径没有离开通知。；input：上述A记录/B事件7条件辅助调用；对照记录穿透假。；reference_result：位置/朝向因图不匹配保持B原状态，但记录穿透真仍将B事件7穿透置真；假记录不会清已有真穿透。；input：A≠B且记录穿透真，但B不存在事件7；对照同图记录且该事件缺失。；reference_result：异图绕过同图缺事件跳过门，真穿透写入尝试失败；同图缺事件先跳过整条，不到穿透写入。之前已恢复条目无回滚保证。
当前与应交付事实的差异：current：保存/恢复门与事件实例状态被描述，但局部变更记录的消费者顺序和不一致写入门没有可独立推导规则。；expected：补记录行为族：记录项/清空时机、普通读档先清空再恢复辅助、同ID重建离开/进入通知；条件辅助按字段分别界定地图门、假值保持及缺事件失败。
用户影响：实现者可能错误保证消去/移动记录读档后被统一恢复，或按图身份过滤全部字段并漏掉参考局部副作用/失败。；实现风险：错误恢复保证影响地图事件状态、碰撞与脚本继续；缺事件异常的先前状态提交可能被错误回滚。
跨模块消费者：M02保存/读档恢复链；M03事件消去/推动/移动与通行；M12地图事件作者
历史finding/旧候选/去重关系：旧C037/C039/C036分别为传送/预读/双向地形，不覆盖事件变更记录；固定源异常事实与未来复刻决定分层。；alias：
具体建议（不是已经修复）：记录正常清空链和条件辅助行为，明确该历史缺陷没有已证Demo运行路径；未来是否复刻单独交用户决定，不修改参考。
可验证完成标准：正常读档两图恢复分支均给出进入清空→图更新→恢复辅助顺序。；同ID实际重建旧ID非零会发离开；无重建仅标记变更不发离开。不能把同图显式传送无重建条款泛化。；给A≠B同ID穿透真、穿透假、当前缺事件三对照；保留位置/朝向门与穿透门差异。；已加载实例状态保留与记录已清分别描述，不据清记录声称所有事件状态丢失。；异常只记录静态阶段/已提交前缀；未来是否保留源缺陷为USER_DECISION，不作为修参考要求。
依赖：地图进入通知顺序；持久地图局部记录；事件实例/页初始化；读档重建门；未知/缺资料：缺地图/存档样本；实际默认消费者仅定位Game.load，记录存在条件的动态额外消费者未证。；未来是否复刻辅助字段门差异为USER_DECISION，当前规格事实补充为REQUIRED_REVISION。
实际root裁决：reviewer：/root；decision：CONFIRMED_WITH_PREMISES_AND_LIMITS；basis：独立module完整领域报告 + root逐项前提/反例及关键source/spec定点复读；具体阅读范围见root-integration-reading-log.tsv。未移转旧审核签名，未运行。
兼容/重设计分类：HISTORICAL_ANOMALY_USER_CHOICE_FOR_FUTURE_IMPLEMENTATION; DOCUMENT_FACT_REQUIRED

### GR3-M04-001｜P2｜REQUIRED_REVISION｜个体编号斑点图像修饰缺少可得的数学与默认形状合同

模块/能力/类别：M04；SPINDA个体化图像修饰；Pokémon Rules / Engine Integration。处置状态：CONFIRMED；实际reviewer：/root。
证据层级：SUPPORTED_STATIC / SOURCE_STATIC_DERIVATION; NO_PIXEL_RUNTIME。
- 来源R：`Data/Scripts/014_Pokemon/001_Pokemon-related/001_FormHandlers.rb`；blob `d643bcc5fc09d233880174bb2b7004c843d224ac`；定位 41–140;152–156；四个可得形状、编号八个4位组→锚点、2倍尺度、RGB夹限和2×2共享采样写入；SPINDA注册
- 来源R：`Data/Scripts/010_Data/002_PBS data/009_Species_files.rb`；blob `2a2e2fb92e7c05ec3b2f586edfda64cd4eeeaba3`；定位 92–109；非蛋前/后精灵先按资源取位图，再复制结果并逐帧调用个体修饰；按物种参数纯取图不经过同一入口
- 规格S：`deliverables/final-specification-set/pokemon-rules/wp21-dynamic-forms-and-display.md`；blob `2bb7cb94ea07111177674afa51e9082d933b4750`；定位 §3.2 E line101;§10；只有按个体标识绘斑点/资源交界，缺参数与默认形状
- 规格S：`deliverables/final-specification-set/engine-overworld/wp15-resource-matching-and-audio.md`；blob `23c487115d8b01638ed2db062546ef2a58abdc9f`；定位 物种图像消费者与依赖；全域检索未有斑点算法/形状表
- 规格S：`deliverables/final-specification-set/test-catalog/pokemon-rules-wp19-21-22-23-34.md`；blob `454953cbd8071d38fd5848cec665fa916e164faf`；定位 FM系列；没有编号/色彩/重叠/帧与入口对照

适用前提：非蛋SPINDA个体，从按个体取精灵入口取得有效位图或动画帧；位图尺寸足够涵盖给定斑点，不讨论越界宿主行为；指定个人编号和普通异色缓存，无插件改写修饰器或资源；只比较静态像素操作，不需本轮创建素材
正常/失败/边界或最小反例：normal：相同编号/异色/位图输入产生相同四组斑点位置与色彩处理；编号0与4294967295相比，四组位置均向右/下各移动30像素。每个被标记点输出2×2块，读取该块左上像素再复制变更后的颜色到四点，不能简单写成四点分别调色。；boundary：原左上RGB(200,200,200)：普通异色为假→(200,85,125)，真→(125,190,50)，通道夹0..255；重叠区域会再次处理。蛋入口在修饰前返回；按物种参数直接取图没有同一个体修饰；按个体取正/背面均可调用且逐动画帧处理。；failure：资源未匹配或加载失败的宿主结果和越界像素行为保留未知；本轮没有真实位图输出、游戏运行或Demo证据。
当前与应交付事实的差异：current：仅能力名和消费者归属；实现者不能从最终集决定四个形状、编号取位组、位置、尺度、普通/异色色彩和帧/入口门。；expected：以独立数学/数据形状与状态/入口说明交付可得静态核心，资源/宿主未证只限定其真实像素结果，不抹掉已有规则。
用户影响：同一编号可被任意画成不同斑点仍满足概述，个体化外观能力无法作为可验证行为合同实现。；实现风险：把只读资源缺失误当静态算法缺失；或把源数组/方法原样复制进新代码来补需求。
跨模块消费者：M03资源/绘制；M10摘要/战斗精灵；M01资源身份/物种图像入口
历史finding/旧候选/去重关系：relation：NEW_CAPABILITY_DETAIL_NOT_ORIGINAL229_REOPEN；notes：旧WP21注册/形态/展示与媒体未运行限定仍成立；本项针对可得SPINDA修饰规则而非要求补齐Graphics或复制源架构。；alias：
具体建议（不是已经修复）：补独立锚点/编号组规则、四个默认形状的无源码表达、2倍尺度/夹限/2×2采样及重叠/逐帧/入口边界和测试设计；未来可改素材/呈现设计，但参考能力层须准确且与目标差异明分。
可验证完成标准：只凭最终集可推出0与最大32位编号的30px位移对照；形状数据自足，RGB两组/夹限与2×2采样能唯一计算；列出重叠、蛋、正背/按物种入口和动画帧边界；不生成/修参考素材，不宣称真实像素或运行通过，不照搬源数组或类方法结构
依赖：M03物种资源消费；M10精灵演出输入；未知/缺资料：实际源精灵尺寸、图像效果与越界get/set像素宿主规则未运行。；未来目标外观是否要求保持默认图案还是重设计由用户决定。
实际root裁决：reviewer：/root；decision：Independent primary actual substantive module review; new formal gap only；basis：review/global-independent-review/third-2026-10-12-86b4d7e-manual-a731/M04/report.md
兼容/重设计分类：BEHAVIOR_OR_DATA_CONTRACT; FUTURE_ARCHITECTURE_FREE

### GR3-M05-001｜P3｜REQUIRED_REVISION｜可得个体尺寸辅助缺少独立毫米数学合同

模块/能力/类别：M05；个体尺寸数学辅助；Pokémon Rules / Demo-DX。处置状态：CONFIRMED；实际reviewer：/root。
证据层级：SUPPORTED_STATIC_SOURCE_AND_COMPLETE_SPEC_SET_REVIEW; NOT_EXECUTED。
- 来源R：`Data/Scripts/019_Utilities/002_Utilities_Pokemon.rb`；blob `15432c8183de4c75ab6fb4edce82baf7d919eb05`；定位 243–271；完整辅助数学已读；全432文件rg只有定义，无普通静态caller，不推出动态不存在
- 规格S：`deliverables/final-specification-set/creature-rpg/wp18-creature-identity-species-ownership.md`；blob `f03d080ec39973be1eeb3f85683be6f56d9e6a7b`；定位 §3.2 height/weight责任，line74；§6派生line275；只有物种0.1m/0.1kg字段，不是该个体毫米计算
- 规格S：`deliverables/final-specification-set/creature-rpg/wp24-player-trainers-partners.md`；blob `bb181b68d143f2a8bd09ba4e447a9867ed791336`；定位 §3.1 line54；派生查询未穷尽，完整131搜索未有该可得数学定义

适用前提：合法个体，物种height字段为7（0.7m）；六项原始IV均0，PID32位合法；只调用可得尺寸辅助，未运行游戏。；不把该入口当默认游戏/钓鱼使用，静态调用者未定位，真实Demo/外部调用未知。
正常/失败/边界或最小反例：normal：PID0给203mm；不抽随机、不改个体状态。；boundary：PID2304（低byte0、高byte9）给209mm，PID2560（高byte10）给210mm；分段10边界不同。；reverse：原始IV低4位和PID低两byte参与；EV/Nature/ivMaxed不是该规则输入。；execution：NOT_EXECUTED; manual fixed arithmetic only
当前与应交付事实的差异：current：只给物种高度/重量和未穷尽派生查询；不能从独立材料推导个体尺寸输出。；expected：给出独立单位、位字段输入及组合数学、全部分段边界/比例和整数阶段、正常/边界向量；与物种高度展示区别。
用户影响：从零实现会遗漏已可得数学辅助或用物种高度误当个体尺寸。；实现风险：单位、截断和阈值易产生不同结果；默认可达性未知，不夸大当前玩家受影响。
跨模块消费者：外部事件/开发者辅助潜在使用；当前固定脚本仅定义；WP18个体信息与WP77/DX能力分母
历史finding/旧候选/去重关系：原229查尺寸相关为地图词法/显示，未见同一个体辅助根因；不重开旧控制。；alias：
具体建议（不是已经修复）：在适当个体或开发者行为合同补独立数学/参数表，不复制源表达式或强制源helper接口；明确静态无消费者和未运行。
可验证完成标准：允许材料独立推导203/209/210mm三个输入及全部分段两端。；明确原始IV/PID位输入与物种height单位，整数阶段；未把潜在调用写成已启用。
依赖：M04 个体字段；M11/M12 外部/示例调用界限；未知/缺资料：地图/Demo/插件调用者未得；原作者用途与未来是否保留该辅助需用户范围决策；规则文档可先补，不强制现代API
实际root裁决：reviewer：/root；decision：Independent primary actual substantive module review; new formal gap only；basis：review/global-independent-review/third-2026-10-12-86b4d7e-manual-a731/M05/report.md
兼容/重设计分类：BEHAVIOR_OR_DATA_CONTRACT; FUTURE_ARCHITECTURE_FREE

### GR3-M05-002｜P2｜REQUIRED_REVISION｜探测仪只列功能名，缺少搜索、方向与响应合同

模块/能力/类别：M05；野外探测仪及隐藏道具响应；Creature-RPG / Engine-Overworld / UI / Demo-DX。处置状态：CONFIRMED；实际reviewer：/root。
证据层级：SUPPORTED_STATIC_SOURCE_AND_COMPLETE_SPEC_SET_REVIEW; NOT_EXECUTED。
- 来源R：`Data/Scripts/013_Items/001_Item_Utilities.rb`；blob `0ff6f88feb9e1b375027d907e03976d17b10d617`；定位 556–576；筛选同图事件、矩形排除/自开关A、Manhattan距离和平局
- 来源R：`Data/Scripts/013_Items/002_Item_Effects.rb`；blob `cad2fc8d57960b79088eb19e92ff97ae9203e6df`；定位 318–356；统计先增、音效请求、无结果/脚下/邻近三路、别名
- 规格S：`deliverables/final-specification-set/creature-rpg/wp28-item-use-and-training.md`；blob `bb7c344cfbb24b8f8eb3e8ed8bfea0be6e426580`；定位 §3.3 line84；§4目录line131；仅打开对应功能/登记身份，未定义可得算法和响应
- 规格S：`deliverables/final-specification-set/generic-kernel/wp06-stats-directory.md`；blob `919b76a1fbc6039f1cf77b66854feed96f47aaac`；定位 line40 itemfinder_count；只给次数来源，不是搜索/响应合同
- 规格S：`deliverables/final-specification-set/demo-dx/wp75-project-conversion-and-authoring-tools.md`；blob `b2221b3a1793a579cdfbfc74f4bc1e8ea54e23d0`；定位 §4 item/hiddenitem转换；作者生成事件是上游，未承接探测搜索/时序

适用前提：玩家/当前地图/事件集合/自开关有效；名称含hiddenitem不区分大小写；媒体/转向等待正常返回，无额外回调改变地图或玩家。；隐藏道具事件可以是合法作者夹具，真实地图缺失，不宣称默认Demo可达。
正常/失败/边界或最小反例：normal：玩家(5,5)，候选(7,5)与(5,7)均未拾、名称匹配；两者Manhattan2，按当前事件枚举先者选；水平距离与垂直距离相等时朝垂直方向。；failure：无候选或候选自开关A真：使用统计先+1，音效请求后无响应消息，效果仍真；不拾取任何物品、不写A。；boundary：dx绝对7/dy5可入，8/6排除；同格候选先每0.2秒右转90度共4次，再等0.3秒脚下消息；近处转向后等0.3秒两段消息。；execution：NOT_EXECUTED_STATIC_SCENARIOS
当前与应交付事实的差异：current：功能列名不能确定哪些道具能被探测、多个目标如何选择、失败是否成功使用、角色方向/统计先后。；expected：独立候选过滤/距离/平局、三路响应、请求和等待单位、统计与返回/消费交界，保持无实际拾取。
用户影响：开发者可能使探测全图/已拾取道具、随机选平局目标或失败不统计；玩家方向与消息行为不同。；实现风险：事件身份和编译简写的上游规则、响应下游等待/使用返回容易遗漏。
跨模块消费者：WP75隐藏道具事件生成；WP13事件/自开关与玩家转向；WP06次数统计；WP27/28快捷/背包使用；M10消息/等待，M11世界活动
历史finding/旧候选/去重关系：旧C103/C120为其它状态写入，未同根；旧候选不作为通过或新证据。；alias：
具体建议（不是已经修复）：补净室行为表/状态次序与具名正常、无目标、阈值、平局、脚下反例；保留资源/宿主未知。
可验证完成标准：上述候选窗口/已拾过滤/两距离及枚举平局可从最终合同唯一推出。；三路统计/返回/方向/时序及不自动拾取都明示；无真实运行签名。
依赖：M03地图事件/转向；M10消息/等待；M12隐藏道具作者转换；未知/缺资料：真实地图/媒体/时序运行未证；动态事件枚举实现组织自由，但平局外部次序须说明兼容策略
实际root裁决：reviewer：/root；decision：Independent primary actual substantive module review; new formal gap only；basis：review/global-independent-review/third-2026-10-12-86b4d7e-manual-a731/M05/report.md
兼容/重设计分类：BEHAVIOR_OR_DATA_CONTRACT; FUTURE_ARCHITECTURE_FREE

### GR3-M06-001｜P3｜REQUIRED_REVISION｜经验设置辅助遗漏同级变化的差量消息及先提示后写入的时点

模块/能力/类别：M06；M06-G09；User Interface。处置状态：CONFIRMED；实际reviewer：/root/m06_lifecycle_encounters_v3。
证据层级：SUPPORTED_STATIC。
- 来源R：`Data/Scripts/013_Items/001_Item_Utilities.rb`；blob `0ff6f88feb9e1b375027d907e03976d17b10d617`；定位 223–278；增减差量消息先于经验写入，同等级也提示；之后才按等级相等早退。
- 规格S：`deliverables/final-specification-set/creature-rpg/wp30-growth-learning-and-friendship.md`；blob `ea4ebda45c4827d31a4d0af9bcf4332313b64104`；定位 136–140；字段写入/同级早退被列出，未完整交付差量提示及其写入前时点。

适用前提：合法普通非蛋非Shadow CATERPIE，Medium曲线、L3、E27；合法玩家/地图/场景，无插件；提示/刷新正常返回。；独立反向输入E28请求27；同值对照；均不跨级。
正常/失败/边界或最小反例：input：E27→28；expected：先显示获得1经验，再写28、维生素友好变化、重算/刷新；仍L3，无升级窗/学招/进化。；execution：NOT_EXECUTED_STATIC_DESIGN；input：E28→27；expected：先显示失去1经验，再写27、重算/刷新；仍L3，无友好/升级窗/学招/进化。；execution：NOT_EXECUTED_STATIC_DESIGN；input：目标与当前相同；expected：显示经验未变化，原值保持并早退。；execution：NOT_EXECUTED_STATIC_DESIGN
当前与应交付事实的差异：current：§5.2给写入与同级早退，缺每次非零增减的差量输出和提示早于写入；允许读者将同级改经验实现为静默。；expected：钳制后比较；非同值先按差量和方向提示，再分别写入/重算/刷新，之后才看是否跨级。
用户影响：用户可见输出遗漏，提示与持久提交边界不能从正文唯一确定。；实现风险：只在跨级显示消息，或把消息移到经验写入之后。
跨模块消费者：M05道具/经验糖果；M12调试经验设置；成长呈现和进化调用
历史finding/旧候选/去重关系：kind：NEW_SCOPE_NOT_REOPENING；note：旧A047为战斗分配/截断/零份额；本项是经验设置辅助的消息，非重开。；root_independent_review：root消息确认独立读ItemUtilities223–327及WP30§5.2，支持P3 REQUIRED；不重复立M05 ID。；alias：
具体建议（不是已经修复）：在WP30§5.2列出两方向差量提示、先提示后写入，补同级增/同级减/同值三组未执行静态设计。
可验证完成标准：正文独立决定三组消息、时点、终值和跨级门。；差量按钳制后的目标与当前比较；提示先于写入。；同级增经验保维生素友好；下降无友好；两者无升级窗/学招/进化。
依赖：WP30§5.2；WP28经验道具；调试经验入口；未知/缺资料：未运行场景/提示；资源、宿主显示与异常会话不在证明内。
实际root裁决：reviewer：/root；decision：Independent primary actual substantive module review; new formal gap only；basis：review/global-independent-review/third-2026-10-12-86b4d7e-manual-a731/M06/report.md
兼容/重设计分类：BEHAVIOR_OR_DATA_CONTRACT; FUTURE_ARCHITECTURE_FREE

### GR3-M07-001｜P2｜REQUIRED_REVISION｜执行期退款未清消费身份，同轮正常终局可再次退款；交界缺少确定库存结果

模块/能力/类别：M07；M07-C12；Combat Requirements / Creature-RPG。处置状态：CONFIRMED；实际reviewer：task：/root/m07_battle_session_v3；independence：新的实质审查角色，未参与受审规格字节作者或登记；非旧停止任务续跑；model_requested：gpt-6.1-sol；reasoning_requested：ultra；speed_requested：Standard(default)；echo：UNVERIFIED。
证据层级：SUPPORTED_STATIC; reference/runtime/demo executions=0。
- 来源R：`Data/Scripts/011_Battle/001_Battle/006_Battle_ActionUseItem.rb`；blob `9fafeea89590e2ecdf7f438d8ea91188af8d7fe8`；定位 34–74,87–101,104–123,134–148；登记先扣减；家族1/2/3/5失败退款后没有清选择中的物品身份，成功分支才清；退款只查消耗属性及容量
- 来源R：`Data/Scripts/011_Battle/001_Battle/009_Battle_CommandPhase.rb`；blob `9f38551f88dfb95dc6c1a4e31e2ed968019032b6`；定位 5–22,174–195；下一命令阶段直接清选择；正常终局撤销选择则按仍记录的物品再退款
- 来源R：`Data/Scripts/011_Battle/001_Battle/010_Battle_AttackPhase.rb`；blob `a6e9a3cee5f168f149eed44265f22db445bc7b1c`；定位 69–89,176–201；物品依当前顺序处理，没有相同目标排斥；失败后招式/回合末仍可正常结束战斗
- 来源R：`Data/Scripts/011_Battle/001_Battle/002_Battle_StartAndEnd.rb`；blob `54d4f8d6a10df57937838b36ec145a96fdc7b91e`；定位 322–347,479–510；决定正值离开循环后正常共同收尾，逐场上对象撤销未清选择
- 来源R：`Data/Scripts/011_Battle/001_Battle/011_Battle_EndOfRoundPhase.rb`；blob `ec13760f83d203484a97c5884238b17ef99ed3d2`；定位 207–238,597–706；普通毒伤可使唯一野生失能；替补入口裁判后返回正常终局
- 来源R：`Data/Scripts/011_Battle/002_Battler/003_Battler_ChangeSelf.rb`；blob `a3c00d47e159924e49f83aad5485718381ebae33`；定位 64–99；本例两名退款玩家席位保持存活，其选择未被濒死清除
- 来源R：`Data/Scripts/013_Items/003_Item_BattleEffects.rb`；blob `4c522dd209fd27bc5b36f807961e69b3405f6cba`；定位 66–79,333–337；普通Potion资格要求可战斗且HP未满；效果补20，使1HP缺口满血
- 来源R：`Data/Scripts/011_Battle/004_Scene/003_Scene_ChooseCommands.rb`；blob `3b61c5afac5ab50c42026ff5bcafa4f3e03ca2ce`；定位 208–289；普通个体物品可选择同一后备；没有第二命令对同一治疗对象的排斥
- 来源R：`PBS/items.txt`；blob `f0d40d5e111b85a606185101c326e24c832348d9`；定位 2942–2950；默认Potion属OnPokemon，非重要物品，恢复20
- 来源R：`Data/Scripts/010_Data/002_PBS data/006_Item.rb`；blob `94ac69921fb4a3c22c730d5155d3a559a3d6afb5`；定位 123–142,166–202；默认非重要可消费；Potion非机器/关键物，数据没有Consumable时默认真
- 来源R：`Data/Scripts/013_Items/001_Item_Utilities.rb`；blob `0ff6f88feb9e1b375027d907e03976d17b10d617`；定位 333–362；非场上后备的治疗先按总HP截断持久写回；Potion20足以补1HP缺口
- 规格S：`deliverables/final-specification-set/combat-requirements/wp40-commands-obedience-and-action-order.md`；blob `1b562fcfcb8461e879bfb6a221283fce7c6838b3`；定位 §4.2 L99–103，尤其L102；§8第2条 L260；只列失败退回/通过清消费身份，未明确失败保留身份及晚终局的重复退款；当前测试无该组合
- 规格S：`deliverables/final-specification-set/combat-requirements/wp42-growth-end-of-round-and-battle-outcomes.md`；blob `d230a02a94951b074bfc94072c335678ba472f1a`；定位 §6共同次序 L177–181；§5.1阶段19–22 L125–128；正常终局撤销未用物品的消费者未说明已退款失败选择可再次退回
- 规格S：`deliverables/final-specification-set/creature-rpg/wp28-item-use-and-training.md`；blob `bb7c344cfbb24b8f8eb3e8ed8bfea0be6e426580`；定位 §3.5 line99; §6 lines240–244; §7 line258；对应物品合同没有保留消费身份与重复退款结果，需交界同步
- 规格S：`deliverables/final-specification-set/test-catalog/combat-requirements-wp39-40-41-42-45.md`；blob `a0b11926f6dcfc601004852b86adaa0c314be75e`；定位 CM-20 L58；E04 L148；无失败保留身份→晚终局再退款库存的组合设计；既有单阶段退款与正常终局设计不能区别一次与重复退款的整链输出

适用前提：普通内部野生2v1、无伙伴、两名玩家活跃成员可选物品且一直存活；同队非在场可战斗成员T的HP=总HP−1，无蛋/查封/超频；背包Potion恰2且可接收退款。；两名玩家分别正常登记Potion到同一T；所有登记资格通过；无插件、额外处理器、重入或取消。两者按物品阶段顺序执行，第一件把T治满，第二件资格失败。；唯一野生成员已普通中毒且当前HP1，原始状态毒计数0，无毒疗/魔法防守或其它治疗；本轮合法非伤害行动不伤玩家、不清毒、不改变背包；本轮回合末毒伤后正常终局。；保持第二件的玩家使用者存活、没有其换人/失能/选择撤销或新命令阶段；容量足够，普通诊断/演出正常返回。
正常/失败/边界或最小反例：kind：normal_late_terminal；steps：库存2→登记两件→0；T仍缺1HP；第一件补T至满HP并清其消费身份；第二件失败退款：库存0→1；消费身份仍存在；回合末唯一野生因毒伤倒下；裁判胜利，进入正常终局；撤销第二件的选择，再次退Potion：库存1→2；expected_reference_static：Potion_final：2；successful_healing_items：1；target_HP：full；decision：1；execution：NOT_EXECUTED；kind：continues_reverse；change：唯一野生能撑过回合末且没有其它终局源，进入下一命令阶段；expected_reference_static：库存保持1；新命令阶段直接清选择，不再退款；execution：NOT_EXECUTED；kind：faint_boundary；change：第二件使用者在终局前正式失能，其选择由濒死清除；expected_reference_static：本条重复退款消费者不再命中，不能统一称所有失败物品都重复退款；execution：NOT_EXECUTED
当前与应交付事实的差异：current：分散合同允许读者把失败退款视为已经完成消费清理；未明确失败选择仍持消费身份，也未给同轮正常终局的确定最终库存。；expected：以参考静态异常明示失败退款后的残留、下一命令阶段与正常终局两消费者的不同结果及边界；默认内容反例最终Potion2，继续战斗对照1。
用户影响：至少一种正常合法多席物品/终局链的库存结果不能由现文本唯一判断；一次实际治疗可能没有净消耗。；实现风险：独立实现若退款后立即清消费身份，或用幂等退款，产出Potion1；照参考保留身份时晚终局产出2。规范必须把源行为与未来修正裁决分开。
跨模块消费者：M05 WP28/WP27 背包与战斗主动使用；M07 WP40 物品阶段/选择清理；M07 WP42 正常终局；M10 WP67-A 背包与选择取消显示
历史finding/旧候选/去重关系：related_controls：GIR-FD82-B008；relation：NEW_EVIDENCE_ADJACENT_NOT_REOPEN；note：B008处理效果存在性/无效果但资格通过不退款；本条是资格失败后的残留消费身份与晚终局第二退款。保留旧关闭与既有前提。；alias：
具体建议（不是已经修复）：required_now：补写冻结参考的静态行为异常、必要前提、库存状态序列和正常继续/失能/容量反例；同步WP28/WP40/WP42及测试。；future_policy：未来独立实现是否保留此历史缺陷须由用户在独立兼容性/实现阶段决定；本轮不默认要求永久复刻，也不修改参考或实现新框架。
可验证完成标准：正式参考行为层明确资格失败退款后该消费身份仍保留。；静态整链向量能唯一推出本例终局Potion2，继续到下一命令期对照Potion1。；限定使用者存活、无中间清选择、正常终局和退款容量，失能反例不得误套。；WP28/WP40/WP42和对应测试一致；未来是否修正历史缺陷单列用户裁决。
依赖：M05背包容量/物品消费属性；M07正式濒死清选择；M07正常終局入口；未知/缺资料：未运行宿主/菜单/战斗；实际输入交互与演出资源未认证。；其它处理器重入/异常/满背包退款不纳入本例。
实际root裁决：reviewer：/root；evidence：Independent source read ActionUseItem34–148/CommandPhase5–22/AttackPhase69–89/StartAndEnd501–510; Potion资格66–79/效果333–337; WP40§4.2 and WP42共同收尾 read；decision：Reference double refund chain supported. Requirement gap is explicit residual item identity and final inventory outcome, rather than unbounded addition of every derivable example. Current term未使用 lacks an unambiguous linkage to already-refunded failed selections. Preserve prerequisite actors alive/capacity/normal terminal/no next command; future historical-bug policy USER_DECISION.
兼容/重设计分类：HISTORICAL_ANOMALY_USER_CHOICE_FOR_FUTURE_IMPLEMENTATION; DOCUMENT_FACT_REQUIRED

### GR3-M08-001｜P2｜REQUIRED_REVISION｜自然之恩续击在首击自耗树果后缺少空持物查询失败合同

模块/能力/类别：M08；M08-NG-LIVE-ITEM；Combat Requirements / Pokémon Rules。处置状态：CONFIRMED；实际reviewer：task：/root/m08_effects_items_v3；independence：New independent review role; no authorship or registration of audited formal bytes；model_requested：gpt-6.1-sol；reasoning_requested：ultra；speed_requested：Standard(default)；echo：UNVERIFIED。
证据层级：SOURCE_STATIC_DERIVATION。
- 来源R：`Data/Scripts/011_Battle/003_Move/008_MoveEffects_MoveAttributes.rb`；blob `2f6f5db5298d8c7ee8cd046d9b9124f895b41ab1`；定位 1338–1379; especially 1364–1369；起用有树果/有效/前缀资格；威力每次查询先取当时持物身份，空持物的身份访问早于数据获取及默认威力返回。
- 来源R：`Data/Scripts/011_Battle/003_Move/002_Move_Usage.rb`；blob `10b06a44eabef9cd87291712141e938872acff1c`；定位 45–54；亲子爱对该实际伤害非蓄力单目标招式计划两击；此族未覆盖击数。
- 来源R：`Data/Scripts/011_Battle/003_Move/003_Move_UsageCalculations.rb`；blob `342abdfb68fb2faec2e25ce803aca3dafbb07b4e`；定位 239–253；普通伤害每次先决定会心，然后求当前基底；排除画皮/冰脸提前吸收。
- 来源R：`Data/Scripts/011_Battle/002_Battler/007_Battler_UseMove.rb`；blob `b6aa0c7f4aafc8b99d80508978f5704bc51a5867`；定位 404–432; 583–646；首击通过后目标仍活、U活且未真睡/冻便继续；第二击重算普通伤害，没有重新检查自然之恩起用树果门。
- 来源R：`Data/Scripts/011_Battle/002_Battler/010_Battler_UseMoveTriggerEffects.rb`；blob `f35de8ff5fd94e46279a59e4355a8db26e0502b2`；定位 5–45；目标物品每击反应后，U失HP立即查恢复物品。
- 来源R：`Data/Scripts/011_Battle/007_Other battle code/009_Battle_ItemEffects.rb`；blob `240046fc93ac5221b2684601338a83603173eaab`；定位 364–387; 1311–1331；JABO物理反伤请求U总HP整除8，ORAN可治且半血门内恢复10，返回真。
- 来源R：`Data/Scripts/011_Battle/002_Battler/006_Battler_AbilityAndItem.rb`；blob `3e5005b540e7657e15e77133aaf4a551eac57835`；定位 217–243; 272–285; 315–323；半血资格与成功恢复后普通消费清当前物品；没有共生时保持空。
- 来源R：`Data/Scripts/011_Battle/002_Battler/001_Battle_Battler.rb`；blob `dfea2bb1c97725d8c01ec40fb34549539de04e23`；定位 81–89；空物品身份经try_get读取为缺失；赋值写穿关联个体。
- 来源R：`Data/Scripts/010_Data/001_GameData.rb`；blob `ccfd971a29b3bab107e2da6865ac0050ed3256b0`；定位 99–116；物品符号数据获取不是空值回退；try_get明确对空输入返回空。此场景先在空当前物品的身份访问失败，尚未进入get。
- 来源R：`PBS/moves.txt`；blob `fa5dbaf2739b6b6f55ba5cc5d7d599b4a15b68ca`；定位 5581–5592；默认NaturalGift为物理、单目标、威力由树果替代；不额外限制亲子爱。
- 来源R：`PBS/items.txt`；blob `f0d40d5e111b85a606185101c326e24c832348d9`；定位 5252–5260; 5721–5727；ORAN默认毒80，自耗10；JABO真实默认树果。
- 规格S：`deliverables/final-specification-set/combat-requirements/wp47-a-move-attributes-targeting-and-calling.md`；blob `977839d20748e302813f6fe55bf1ba6a08a01225`；定位 §3.1 TypeAndPowerDependOnUserBerry table row, line 45；明列当前查询及无完整标志威力1，但未区分续击空物品导致先行查询失败；§1一般无回滚不足以确定这一异常触发。
- 规格S：`deliverables/final-specification-set/pokemon-rules/wp46-damage-multihit-and-healing.md`；blob `86da3961aba6375142252e8fb3ade847e68f9115`；定位 §2.1; §3.1 ParentalBond row；给两击和重算共同合同，但未为本族的空当前物品基底边界补足结果。
- 规格S：`deliverables/final-specification-set/test-catalog/combat-requirements-wp47-ab.md`；blob `9a78c3b203e8758bad9ca67fd51ab0b5fe6ab90b`；定位 MA-A09 (line 17); MA-C series；没有此自耗续击对照。

适用前提：合法默认NaturalGift槽、PP正、可行动；实际伤害且单目标，U持有效ORAN、有效PARENTALBOND；没有抢夺、反射、压制、替身、画皮/冰脸、保护、其它免疫/失手/异常/共生。；该状态可由普通技能交换从盟友取得PARENTALBOND；不依赖执行参考或改参考字节。静态夹具只假定当前合法战斗状态，不声称已操作获得链。；U总HP160、当前81，目标持有效JABO、可食果且首击后仍存活；U可间伤/恢复；没有RIPEN/CHEEKPOUCH等额外改写；双方零阶，当前代。
正常/失败/边界或最小反例：name：self_consumption_then_second_hit；input：U H160/h81持ORAN；目标JABO且耐久足以生存首击；两击计划；expected_static：首击正常基底80，目标损失已提交。；目标JABO扣U20：81→61；U半血ORAN回复10：61→71并消费当前ORAN，C空，I若相同清，R/P写ORAN。；第二击普通基底查询遇空当前物品身份，产生NoMethodError类异常，尚未调用物品get或默认1分支；首击伤害/树果反应/持久写回不回滚。；execution：NOT_EXECUTED；name：no_self_consumption_boundary；input：仅将U当前HP改101，其余不变；expected_static：JABO扣20后81>80，ORAN不触发；第二击仍以ORAN基底80完成；正常后段才消费此时ORAN。；execution：NOT_EXECUTED；name：one_hit_control；input：仅移除有效PARENTALBOND，其余同主夹具；expected_static：首击仍自耗至71，计划单击不再访问基底；正常使用结束看到空物品，局部守卫跳消费。；execution：NOT_EXECUTED
当前与应交付事实的差异：current：给当前树果完整/不完整标志取值与正常末尾消费；未给合法首击反应导致续击空物品的失败结果。；expected：补明缺失当前物品与存在但无完整标志两个不同分支；前者在续击基底查询首次失败，已提交副作用保留。
用户影响：独立实现者可能安全回退威力1、锁定最初树果，或跳第二击；三种都会改变有限参考结果与失败边界。；实现风险：应先准确记录历史可验证行为；未来是否兼容该缺陷属于用户选择，不应在本轮规格审查默认复刻或修正。
跨模块消费者：WP46多击消费者；WP50每击反伤/恢复/消费；WP40/42一般动作异常诊断边界；WP52-C自然之恩预测（本轮尚未完整核）
历史finding/旧候选/去重关系：kind：NEW_SCOPE_RELATED_FAILURE_PATTERN；related：GR-014 Fling empty-held-item failure already documented in WP47-B §5.3；difference：本候选是NaturalGift第二击基底查询，失败早于物品get；不是Fling目标作用后的树果查询，且可由未倒下目标JABO触发。；legacy_pass_reused：False；alias：
具体建议（不是已经修复）：在WP47-A该行补空当前物品续击失败与已提交状态不回滚的精确静态合同。；补三组输入、局部失败点和正常对照，区分记录参考异常与未来兼容决定。
可验证完成标准：仅最终规格即可确定主夹具的首击提交、U71/160且空持物以及续击首次失败位置。；高HP对照和单击对照可分别推出正常第二击/没有再次基底访问。；不把失败写为必然进程崩溃，不声称运行验证，不把空持物送get后才失败。
依赖：WP46整击顺序；WP50反应与消费；WP40/42异常边界；未知/缺资料：外层诊断呈现及后续宿主恢复没有执行；不从局部异常保证继续/崩溃。；未来实现选择兼容异常或采取有记录的差异由用户决定。
实际root裁决：reviewer：/root；decision：CONFIRMED_WITH_PREMISES_AND_LIMITS；basis：独立module完整领域报告 + root逐项前提/反例及关键source/spec定点复读；具体阅读范围见root-integration-reading-log.tsv。未移转旧审核签名，未运行。
整合定位/资格纠正：ai_consumer_correction：实际AI当前ORAN资格与威力读取由M09审的WP52-B§2.1 line54 / WP52-A§3.2承接，不误指WP52-C；不把实际每击JABO反应链故障扩到AI当前预测。原模块消费者字段保留作为早期导航。；reviewer：/root with independent M09 evidence
兼容/重设计分类：HISTORICAL_ANOMALY_USER_CHOICE_FOR_FUTURE_IMPLEMENTATION; DOCUMENT_FACT_REQUIRED

### GR3-M09-001｜P3｜OPTIONAL｜WP51下游定位将录像主责任误指WP57

模块/能力/类别：M09；M09-104；Combat Requirements / Demo / Developer Experience。处置状态：CONFIRMED；实际reviewer：task：/root/m09_ai_facilities_v3；independence：New independent substantive reviewer; no authorship or registration of audited formal bytes；model_requested：gpt-6.1-sol；reasoning_requested：ultra；speed_requested：Standard(default)；echo：UNVERIFIED。
证据层级：SUPPORTED_STATIC。
- 来源R：`Data/Scripts/011_Battle/008_Other battle types/005_RecordedBattle.rb`；blob `cfb3579b91753865b0b86326e059fb482437ab97`；定位 47–71,139–223；记录和回放行为由这组模块消费者提供。
- 来源R：`Data/Scripts/018_Alternate battle modes/001_Battle Frontier/004_Challenge_Battles.rb`；blob `7b2a9514fbfc6ca650cba2052a7c5e663a0cbcb9`；定位 13–34,84–143；设施可记录三模式、正常转储及回放分派/提升入口。
- 规格S：`deliverables/final-specification-set/combat-requirements/wp51-ai-action-selection-and-skill.md`；blob `9741e2ada560dfc8012b1ec7068735b1fcd5ba22`；定位 §7 L155；下游条目把WP57/76括注为录像/模拟/生成器；录像编号误指WP57。
- 规格S：`deliverables/final-specification-set/combat-requirements/wp58-battle-recording-and-playback.md`；blob `aaac519562388914245899d5dd07462f754ae915`；定位 §1 L9–13；录像、转储、提升和回放的明确主合同为WP58。
- 规格S：`deliverables/final-specification-set/creature-rpg/wp57-factory-rentals-and-swaps.md`；blob `ca4bba144d0aadbf489b2a57e35aca838f313d90`；定位 §1.1–1.3 L9–22；WP57定义Factory租借交换，并把记录/回放排除到其它域。

适用前提：独立实现者从冻结WP51§7下游责任定位寻找记录/回放合同；按正常模块编号阅读WP57和WP76。；当前正式WP57为Factory租借交换，WP58为记录回放；并未更改这些范围。
正常/失败/边界或最小反例：name：recording_contract_navigation；input：读WP51下游录像责任编号；current：WP57/76不能定位到声明的录像主合同。；expected：录像定位WP58；Factory若需要列为下游则另按租借角色注明。；execution：NOT_EXECUTED
当前与应交付事实的差异：current：WP51§7下游括注录像却列WP57/76。；expected：下游录像责任应准确指WP58，模拟/生成器仍WP76。
用户影响：责任导航可能使后续独立实现者遗漏WP58，现有录像机制正文没有因此缺失。；实现风险：仅文档交接定位，不改变参考行为或新增实现要求。
跨模块消费者：WP51独立读者；WP58记录/回放实现与测试设计消费者；全局依赖导航
历史finding/旧候选/去重关系：kind：NEW_MINOR_NAVIGATION_MISMATCH；legacy_pass_reused：False；scope：与旧15控制的机制最低修订不同，不重新打开任何旧状态。；alias：
具体建议（不是已经修复）：把WP51§7录像责任编号改为WP58；Factory租借如保留则写明WP57角色。
可验证完成标准：只读WP51下游定位即可准确找到WP58记录/回放主合同。；WP51/57/58现有技能、租借及记录行为保持。
依赖：WP57；WP58；WP76；未知/缺资料：未验证外部自动化是否解析这处自然语言编号；不据此声称运行故障。
实际root裁决：reviewer：/root；decision：Independent primary actual substantive module review; new formal gap only；basis：review/global-independent-review/third-2026-10-12-86b4d7e-manual-a731/M09/report.md
兼容/重设计分类：BEHAVIOR_OR_DATA_CONTRACT; FUTURE_ARCHITECTURE_FREE

### GR3-M10-001｜P2｜REQUIRED_REVISION｜持物移位经Box Link取回来源物品后仍提交旧物品，重复计数未进入合同

模块/能力/类别：M10；M10-C14；User Interface / Creature-RPG。处置状态：CONFIRMED；实际reviewer：/root/m10_ui_contracts_v3。
证据层级：SUPPORTED_STATIC; reference/UI executions=0。
- 来源R：`Data/Scripts/016_UI/005_UI_Party.rb`；blob `3f874cd888d5d8bb7db62202922ff86f367e01cb`；定位 746–790;1204–1213;1425–1484；持物移位先固定来源个体与旧持物；普通目标选择保留SPECIAL盒子桥，返回后不重新读取来源持物。
- 来源R：`Data/Scripts/016_UI/017_UI_PokemonStorage.rb`；blob `5c4ac47664c7ceaeed3541438b74c6c6be7973cc`；定位 1500–1568;1902–1934；整理模式能打开队伍面板Item；取回成功先加入袋、再清来源持物。
- 规格S：`deliverables/final-specification-set/user-interface/wp66-a-party-and-summary-ui.md`；blob `e98f39d491a9d2f964d34b5c287e5a39973b0470`；定位 29;60;105;202–206;218–219；Box Link及已提交盒侧变更已登记；移位行仍概括为字段互换/单向移动，未承接旧物品快照。
- 规格S：`deliverables/final-specification-set/test-catalog/user-interface-wp17-63-65-66-67-68-69-70-71.md`；blob `2744e1010109bafd3e9314e41cea66ecd0d04140`；定位 PT A15/A16;B16-C125；旧移位三分支与旧索引交换反例没有此连续物品计数向量。

适用前提：正常队伍[A,B]，二者非蛋非Shadow，A索引0持POTION，B索引1无持物；均存活。；Box Link三门成立；普通菜单Item→Move来源A；背包POTION起始0且可添加1；正常资源/媒体/世界上下文、无插件改写。；目标选择中SPECIAL进入盒子整理，不移动队伍位置。在队伍面板选A→Item→确认取回；成功后正常离开盒子。
正常/失败/边界或最小反例：input：返回原移位目标选择后确认B索引1。；expected：背包POTION=1；A无持物；B持POTION。总POTION从1成为2。来源对象与队伍索引均没改变，故不依赖缩队/失效索引。；input：独立同初态，取回后返回原目标选择按BACK。；expected：背包POTION=1；A/B均无持物。取回不回滚，尚无旧物品提交。；input：独立同初态，不进入盒子，直接选B。；expected：背包POTION=0；A空；B持POTION，总量仍1。
当前与应交付事实的差异：current：移位合同只给当前来源与目标持物互换/单向移动，不能唯一推得来源已无持物时仍赋旧物品。；expected：追加连续交界：发起移位保留旧持物身份及来源个体，允许Box Link写入；后续成功使用旧身份而不重新核对来源，记录袋与双方最终计数。
用户影响：正常可达的嵌套界面改变库存与持物总量；用通用守恒或重新验证来源会失去参考兼容性。；实现风险：独立实现若按新状态重查或取消连续操作，会改变可观察结果。参考异常是否保留属于未来用户决定，不能在规格抽取中默默修复。
跨模块消费者：队伍主界面Item→Move；Box Link整理队伍面板Item；WP27容器计数/WP20持物字段
历史finding/旧候选/去重关系：related：GIR-FD82-C125；distinction：旧控制是菜单Switch保留来源索引，经缩队产生数组部分写入/空白面板失败。本例不缩队、不改索引，不走Switch，来源持物身份快照导致重复计数；不能以旧PASS覆盖。；alias：
具体建议（不是已经修复）：补净室状态表和三条静态对照，不修改参考；同步移位文字、测试与交界引用。是否未来修复重复计数另列用户决定。
可验证完成标准：固定初态与完整UI链可从正式正文独立推出袋1/A空/B持POTION。；相同取回后BACK不移位且保留取回，未嵌套对照维持总量1。；不把C125的旧索引失败前提套到本例；保留0运行、资源与Demo未证。
依赖：M05/WP20/WP25/WP27；G7-3领域守卫与UI消费；未知/缺资料：Graphics/Audio/宿主输入实际表现未观察；静态输入夹具不声称真实键盘同轮必能产生。
实际root裁决：reviewer：/root；decision：CONFIRMED_WITH_PREMISES_AND_LIMITS；basis：独立module完整领域报告 + root逐项前提/反例及关键source/spec定点复读；具体阅读范围见root-integration-reading-log.tsv。未移转旧审核签名，未运行。
兼容/重设计分类：HISTORICAL_ANOMALY_USER_CHOICE_FOR_FUTURE_IMPLEMENTATION; DOCUMENT_FACT_REQUIRED

### GR3-M10-002｜P3｜REQUIRED_REVISION｜共享数量选择与两种商店的同轮输入优先序不同，统一语义漏掉确定出口

模块/能力/类别：M10；M10-C21；User Interface。处置状态：CONFIRMED；实际reviewer：/root/m10_ui_contracts_v3。
证据层级：SUPPORTED_STATIC; reference/UI executions=0。
- 来源R：`Data/Scripts/016_UI/018_UI_ItemStorage.rb`；blob `1b8578c6d1cd260ff401030072ebf7c9c58a833e`；定位 276–338；共享数量输入先BACK、再USE、后UP/DOWN/LEFT/RIGHT。
- 来源R：`Data/Scripts/016_UI/020_UI_PokeMart.rb`；blob `e91b66e29e0b26b691ec5b8f4c06d5902f4911e7`；定位 477–539；金钱商店数量输入先LEFT/RIGHT/UP/DOWN，再USE，最后BACK。
- 来源R：`Data/Scripts/016_UI/021_UI_BattlePointShop.rb`；blob `1019a689f6aba97946cec7fc96119cd7a1b10897`；定位 332–394；BP数量输入采用与金钱商店相同的动作优先序。
- 规格S：`deliverables/final-specification-set/user-interface/wp66-c-bag-item-storage-and-shop-ui.md`；blob `af4dc0b6b6fd975d02b6dcc26a7a0fd763396fa2`；定位 78;98–110;138–146；数量选择三处同语义只给单键出口，未限定同轮竞争差异。
- 规格S：`deliverables/final-specification-set/test-catalog/user-interface-wp17-63-65-66-67-68-69-70-71.md`；blob `2744e1010109bafd3e9314e41cea66ecd0d04140`；定位 BG C31/C33/C34；数量上限、取消与单键向量未覆盖同轮竞争。

适用前提：三处数量窗口均已正常到达输入循环，初值1、上限20，资源/状态正常。；夹具显式令相应trigger/repeat查询在同一采样轮为真，不声称宿主实际能生成全部组合。
正常/失败/边界或最小反例：input：同轮USE和BACK触发，无方向重复。；expected：共享数量返回0；金钱/BP商店返回1。；input：同轮RIGHT重复与USE触发，其余假。；expected：共享数量直接返回1；金钱/BP商店将当前值改11并继续等待，本轮不返回。；input：仅USE／仅BACK作为两组独立对照。；expected：三处分别返回1／0，原单键合同保留。
当前与应交付事实的差异：current：三处使用同语义描述，仅有单键规则，不能从规格判定竞争轮的返回值或仍在窗口。；expected：按消费入口给动作优先序，或给以上两条成对向量，清楚分开值修改与确认/取消。
用户影响：相同采样输入在商店和PC物品操作有不同返回与确认时机，影响后续交易/转移选择。；实现风险：统一输入分派会改变参考窗口出口；可用行为表描述，无需沿用重复的源实现。
跨模块消费者：PC存取丢数量；背包丢弃数量；Party辅助数量；金钱商店买卖数量；BP购买数量
历史finding/旧候选/去重关系：related：GIR-FD82-C072/C119；distinction：旧控制已覆盖光标命名竞争与进化末轮BACK；未覆盖这三处数量窗口的不同优先序。；alias：
具体建议（不是已经修复）：补入口化竞争合同和最小静态对照；无需新的生产代码或运行参考。
可验证完成标准：同轮USE+BACK确定共享0/两商店1。；同轮RIGHT+USE确定共享立即1/商店11并留循环。；单键与1..上限原规则仍保留，来源/规格/测试一致。
依赖：WP17按键查询；WP29交易确认时点；未知/缺资料：Graphics/Audio/宿主输入实际表现未观察；静态输入夹具不声称真实键盘同轮必能产生。
实际root裁决：reviewer：/root；decision：CONFIRMED_WITH_PREMISES_AND_LIMITS；basis：独立module完整领域报告 + root逐项前提/反例及关键source/spec定点复读；具体阅读范围见root-integration-reading-log.tsv。未移转旧审核签名，未运行。
兼容/重设计分类：BEHAVIOR_OR_DATA_CONTRACT; FUTURE_ARCHITECTURE_FREE

### GR3-M10-003｜P2｜REQUIRED_REVISION｜战斗确认与命令列表逐字中按键仅恢复，正文却写快进

模块/能力/类别：M10；M10-C28；User Interface / Combat Requirements。处置状态：CONFIRMED；实际reviewer：/root/m10_ui_contracts_v3。
证据层级：SUPPORTED_STATIC; execution=0。
- 来源R：`Data/Scripts/011_Battle/004_Scene/001_Battle_Scene.rb`；blob `1b949814487382dac9d8ed2772b4fff65253f9d2`；定位 267–307;184–265；确认共用命令列表：busy期间调用resume；普通/暂停消息用skipAhead，两个不同效果。
- 来源R：`Data/Scripts/007_Objects and windows/005_SpriteWindow_text.rb`；blob `e8be64d69b3bcb02def7a0cc09c0a5d4027cc628`；定位 368–418;526–617；resume在非暂停busy只返回true，不改字符/计时/速度；skipAhead才立即推进到暂停/换行等边界。
- 规格S：`deliverables/final-specification-set/user-interface/wp67-a-battle-interaction-and-presentation.md`；blob `13eb8eef1ce1958f9c4a3c825d9d24a007f8809b`；定位 213–219 (§9.1)；命令列表明确写消息逐字中BACK/USE先快进；确认包装共享此路径。
- 规格S：`deliverables/final-specification-set/user-interface/wp17-messages-windows-input.md`；blob `81b14a0b09327bc030e5d9ef9f907089bd68cb82`；定位 65–74；共享组件已正确区分resume与另一个推进字符能力，但WP67把它应用错到列表。
- 规格S：`deliverables/final-specification-set/test-catalog/user-interface-wp17-63-65-66-67-68-69-70-71.md`；blob `2744e1010109bafd3e9314e41cea66ecd0d04140`；定位 BT K45–K46；全显后初始Yes及可中止不自动选项的正确测试不能验证逐字中快进行为。

适用前提：普通非可中止的战斗场景；消息窗口正常、textspeed为正；命令列表或其Yes/No确认包装已打开。；当前busy=true、pausing=false、无计时等待；本轮字符显示计时尚不足以新增下一字符。；USE触发，或取消值非负的命令列表中BACK触发；无其它输入或插件。
正常/失败/边界或最小反例：input：列表逐字中USE。；expected：仅恢复调用，无即时推进、无更改速度，不选择命令；后续文字继续依计时。；input：相同文字显示时点换成普通战斗消息，USE。；expected：skipAhead即时推进到下一个暂停/换行/末尾边界，与列表不同。；input：列表已全显，USE；另开同态取消值1，BACK。；expected：分别返回当前索引0/取消值1，原K45行为保持。；input：列表显式中间暂停时USE。；expected：解除暂停；不等于立即显完全文。
当前与应交付事实的差异：current：§9.1将命令列表逐字中输入称快进。；expected：把普通/暂停消息的字符推进与命令列表/确认的恢复区分；按非暂停、暂停、全显三态分别给结果。
用户影响：玩家按确认键时的文字速度与下一步确认时机不同；依据现稿实现会提前展示和确认。；实现风险：无需沿用源方法/API，只写可见字数/速度/出口状态；保持正常与可中止场景边界。
跨模块消费者：战斗Yes/No确认（换人提议、捕虫替换等）；满队捕获接收命令列表；其它战斗消息+命令列表
历史finding/旧候选/去重关系：related：WP17 MG02;旧确认初始索引修订R04；distinction：普通消息快进与列表resume的混同是新条款矛盾；旧初始下标/全显确认合同正确且保留。；alias：
具体建议（不是已经修复）：修正WP67-A§9.1列表逐字中动作，添加普通消息/确认列表的同初态成对向量。参考读值仅作审计。
可验证完成标准：列表busy非暂停USE/BACK的预期没有即时推进或速度变化。；中间暂停仅解除，全显才有命令选择/取消返回。；普通及暂停战斗消息继续按各自快进与1秒/3秒计时规则。
依赖：WP17文本四态；M07战斗交互消费者；未知/缺资料：实际图形/音效/输入宿主与逐帧呈现均未运行。
实际root裁决：reviewer：/root；decision：CONFIRMED_WITH_PREMISES_AND_LIMITS；basis：独立module完整领域报告 + root逐项前提/反例及关键source/spec定点复读；具体阅读范围见root-integration-reading-log.tsv。未移转旧审核签名，未运行。
兼容/重设计分类：BEHAVIOR_OR_DATA_CONTRACT; FUTURE_ARCHITECTURE_FREE

### GR3-M10-004｜P2｜REQUIRED_REVISION｜Arena UI覆写表仍称更替展示与每三回合判决，与已修正领域合同冲突

模块/能力/类别：M10；M10-C34；User Interface / Combat Requirements。处置状态：CONFIRMED；实际reviewer：/root/m10_ui_contracts_v3。
证据层级：SUPPORTED_STATIC; old qualified witness reused; execution=0。
- 来源R：`Data/Scripts/011_Battle/008_Other battle types/004_BattleArenaBattle.rb`；blob `0fc5a9d394f033a9313b78f22c91fbf3ab54cd85`；定位 43–98;116–209；开始标志只在开场/未接通辅助置真；正常补位不复位。命令阶段只在标志真时显示对阵，回合计数达到3后逐回合评判。
- 规格S：`deliverables/final-specification-set/user-interface/wp67-a-battle-interaction-and-presentation.md`；blob `13eb8eef1ce1958f9c4a3c825d9d24a007f8809b`；定位 253 (§10 Arena行)；仍写成员更替时先显示对阵窗、每3回合裁判。
- 规格S：`deliverables/final-specification-set/combat-requirements/wp56-palace-and-arena-variants.md`；blob `54778a4361e4c3b0c5fc0417840fe56275993a19`；定位 108–110;122;140；已经明确补位保留标志/累计/计数及连续评判，旧修订本地正确。
- 规格S：`deliverables/final-specification-set/test-catalog/combat-requirements-wp54-55-56-58.md`；blob `9174e629b481a49358329651f3e17bf3c488921f`；定位 PA-P28；保留完整3→4→5连续向量。

适用前提：普通合法单打Arena、双方三员、尚未终局。原控制B028的完整Pikachu/Eevee/Bulbasaur、Growl、无环境/额外伤害/改判、对应HP100/115/105、全部命中夹具及有效资格完整继承。；正常第3回合评判后双方首发倒下并顺序补位；不直接调用孤立复位辅助、不加插件。
正常/失败/边界或最小反例：input：原控制第3轮补Eevee后继续第4/5轮。；expected：无新对阵开始提示；count保持3后成为4/5，当轮均评判并补位/终局；不重开三个回合周期。；input：只观察首次开场至前3轮。；expected：开场对阵提示，前2轮不判、第3首判；K40这局部正确，不推成后续周期保证。
当前与应交付事实的差异：current：WP67-A表格的两项总括仍传播旧Arena生命周期；引用WP56同一套规格却与其明确结果相反。；expected：把UI对阵提示限定首次开场已置位流程，正常更替不重新提示；评判写至少3门及后续逐回合，引用PA-P28而非每3回合。
用户影响：独立实现按照UI表会多播更替提示并推迟第4/5回合裁判，改变战斗长度/HP与终局。；实现风险：不能因WP56已正确而抹掉同集WP67的相反陈述，也不要求源字段/类结构。
跨模块消费者：Arena命令对阵窗；Arena评判评分窗；WP58模式回放
历史finding/旧候选/去重关系：related：GIR-FD82-B028；reuse：原完整有效前提/反例/最低修订/确定复核及FINAL1受限状态保留；新ID仅登记当前WP67-A残留文字，不自动重开旧关闭状态。M09核WP56/58本地正确，已确认未重复提此新ID。；alias：
具体建议（不是已经修复）：同步修正WP67-A§10的UI时点并回指WP56/PA-P28，保留领域已修正确内容及零运行限定。
可验证完成标准：当前Arena UI表能唯一推出3/4/5连判，不再新建每三回合周期。；第3补位后不额外显示开场对阵窗，首次开场仍保留。；旧B028受限关闭不改，新局部发现独立追踪。
依赖：M09/WP56；CHAIN-7；GIR-FD82-B028；未知/缺资料：评分窗资源/真实宿主呈现仍未运行。
实际root裁决：reviewer：/root；decision：CONFIRMED_WITH_PREMISES_AND_LIMITS；basis：独立module完整领域报告 + root逐项前提/反例及关键source/spec定点复读；具体阅读范围见root-integration-reading-log.tsv。未移转旧审核签名，未运行。
兼容/重设计分类：HISTORICAL_ANOMALY_USER_CHOICE_FOR_FUTURE_IMPLEMENTATION; DOCUMENT_FACT_REQUIRED

### GR3-M11-001｜P2｜REQUIRED_REVISION｜图鉴栖息地多格掩码及同格可见点并集仍无可计算合同

模块/能力/类别：M11；M11-C52 栖息地投影；Pokémon Rules / User Interface。处置状态：CONFIRMED；实际reviewer：task_id：/root/m11_world_activities_v3；independence：全新独立review角色，未参与受审正式字节作者或登记；model_requested：gpt-6.1-sol；reasoning_requested：ultra；speed_requested：Standard(default)；effective_echo：UNVERIFIED；visibility：只在父会话可见，本平台不提供独立Desktop链接。
证据层级：STATIC_SOURCE_AND_FORMAL_CONTRACT_RECONCILIATION; NOT_EXECUTED。
- 来源R：`Data/Scripts/016_UI/004_UI_Pokedex_Entry.rb`；blob `c2b43b0ed024526681dc0ecd5d56dbaa8affd972`；定位 313–353；完整栖息地要点生成入口：可见点全集收集、逐形状字符筛选及基格平移
- 来源R：`Data/Scripts/010_Data/002_PBS data/018_MapMetadata.rb`；blob `0f9bd8a556d8f352148da0047e7d387c625a544c`；定位 42,55,86；MapPosition三非负值、MapSize非负宽加文本；属性提示说明占位字符
- 来源R：`Data/Scripts/016_UI/009_UI_RegionMap.rb`；blob `3749127d031f82b36044af6a4f4fc5d4d8cff4ce`；定位 173–252；区域地图名称/详情/治疗点按同格首条返回；不得把此规则移用给栖息地
- 规格S：`deliverables/final-specification-set/pokemon-rules/wp62-pokedex-records-regions-and-content.md`；blob `8dbc9d5c8d76fb94cb76f09f3e2049f863180fff`；定位 §5.3 第1项，行117；正文仅概述含多格形状折算，没有掩码/高度/尾格/并集判定
- 规格S：`deliverables/final-specification-set/user-interface/wp66-b-storage-and-pokedex-ui.md`；blob `b2b133dddb48c023f6c6d1856e8af3dc8ac49cf5`；定位 §7.1，行198；Area要点生成只反向引用WP62，不给独立规则
- 规格S：`deliverables/final-specification-set/user-interface/wp63-pokegear-map-music-and-phone.md`；blob `ea9949228095b575d789dfccd880ba430b721d85`；定位 §3.1 行39、§3.2 同格首条项；游标定位明确只用形状长度，点详情用首条；均不是栖息地规则
- 规格S：`deliverables/final-specification-set/test-catalog/pokemon-rules-wp53-60-61-62-69-70.md`；blob `cbde89cb410b6565042ad12e3970424494eb0daa`；定位 PD16；已有测试只承接版本/隐藏/区域门，没有形状投影或重复点对照

适用前提：合法区域0及物种X，当前遭遇版本0，该地图的有效遭遇表含X；无HideEncountersInPokedex，MapPosition为(0,13,12)。；MapSize为正宽3、字符文本10000；区域所有相关格都有可见点记录，合法图鉴场景/消息/资源/宿主依赖，无插件或额外改写。；仅静态检查要点集合，不调用生成器、不运行UI、不证明真实地图事件可达。
正常/失败/边界或最小反例：id：HAB-01；input：上述正常01形状10000；expected：高度2；仅(13,12)属于非零占位；其余四个0和不足最后一行的末格不点亮。WP63相同文本只取长度，可使玩家游标在(15,13)，两消费者不能合并。；id：HAB-02；input：同前仅把形状改为11111；expected：点亮(13,12)/(14,12)/(15,12)/(13,13)/(14,13)，未提供的末格(15,13)不点亮。；id：HAB-03；input：同前但省略MapSize或宽0；另把基础点开关关闭且没有同格其它可见点；expected：前者回退1×1、默认占位1；后者该点不点亮。地图隐藏旗标或区域不符也不点亮。；id：HAB-04；input：基础格两条Point，首条受关闭开关51控制，第二条同格无门；其它条件同HAB-01；expected：栖息地仍可点亮基础格，因为任一可见同格点进入集合即可；WP63名称/详情/治疗查询仍由隐藏首条决定为空。交换首后二者并非同一种变化。
当前与应交付事实的差异：current：独立读者只能得知要使用某种多格形状和可见开关，无法唯一确定具体点集；引用的区域地图恰好使用不同的长度和首条规则。；expected：定义默认1格、正宽启用与向上取整高度、行优先字符占位、非整行尾部、基格平移及可见点并集；按正常01字符串至少给出上述成对向量。
用户影响：栖息地会多亮/少亮格，尤其可错误把游标矩形当物种范围，或把隐藏首条扩为所有同格记录都不可见。；实现风险：后续独立实现无法仅凭正式集合决定显示点集，测试PD16也不能区分两种实现。
跨模块消费者：WP66-B Area页（M10）；图鉴栖息地地图高亮；MapSize/MapPosition内容作者（M03/M12）
历史finding/旧候选/去重关系：relation：NEW_BEHAVIORAL_DETAIL_NOT_DUPLICATE；related_controls：GIR-FD82-C110；GIR-FD82-C111；note：C110修的是区域地图游标长度折算，C111修的是名称/详情/治疗首条；本项是另一个消费者的掩码与可见点并集，不撤销旧条款。；alias：
具体建议（不是已经修复）：补WP62§5.3可计算的栖息地投影合同和成对测试，WP66-B保持正向引用；所有新增只写行为/数学/案例，不改参考。
可验证完成标准：仅凭正式正文可算HAB-01/02的1格/5格及缺失尾格。；HAB-03区分缺省/零宽、隐藏/区域/遭遇资格。；HAB-04明确栖息地并集与WP63首条规则并存，保留既有版本枚举缺陷和媒体未证。；新增测试记录NOT_EXECUTED，不升级静态集合为真实地图执行。
依赖：WP62域记录；WP66-B显示；WP63城镇点；MapMetadata schema；遭遇版本枚举；未知/缺资料：真实图鉴UI资源、地图及任一上述事件使用缺失。；非01字符的宿主转换及越界位置属于另行有界约束，不要求本项扩张到任意坏输入。
实际root裁决：reviewer：/root；independent_peers：/root/m11_world_activities_v3；/root/m10_ui_contracts_v3；decision：CONFIRMED_REQUIRED_REVISION；basis：root独立读PokedexEntry313–353、RegionMap173–206、WP62§5.3/相关WP63、WP66-B§7.1；可见点并集与游标只长度/首条不同；未运行。
兼容/重设计分类：BEHAVIOR_OR_DATA_CONTRACT; FUTURE_ARCHITECTURE_FREE

### GR3-M12-001｜P3｜REQUIRED_REVISION｜区域地图工具标记图被错误列为缺失

模块/能力/类别：M12；Town Map素材可得性；Demo / Developer Experience / Engine Integration。处置状态：CONFIRMED；实际reviewer：/root。
证据层级：SUPPORTED_STATIC_FILE_IDENTITY_AND_HEADER; NOT_RUNTIME。
- 来源R：`knownpoint.bmp`；blob `1fc5257737f4b8fddef34da3d473a1a3ba33b528`；定位 whole 246 bytes; BMP signature and 8×8 header；固定Git跟踪且工作字节可读，尺寸/身份核验，不是运行渲染
- 来源R：`selpoint.bmp`；blob `3ed4a0ec643fac61437a1374be00c715669d023b`；定位 whole 246 bytes; BMP signature and 8×8 header；固定Git跟踪且工作字节可读，尺寸/身份核验，不是运行渲染
- 来源R：`townmapgen.html`；blob `6bffe3fc62a739ac3fbe577b4f43f2d20a35fe50`；定位 269;274；页面分别直接相对引用根目录两个标记图
- 规格S：`deliverables/final-specification-set/demo-dx/wp75-project-conversion-and-authoring-tools.md`；blob `b2221b3a1793a579cdfbfc74f4bc1e8ea54e23d0`；定位 §13.2 line321;§16 item8 line367；把knownpoint/selpoint列为demo缺失，与固定树实际可得素材不符

适用前提：固定参考实际根目录及页面原相对路径；仅核文件存在、可读与身份，不推页面底图存在或完整工具可运行
正常/失败/边界或最小反例：normal：knownpoint与selpoint均可从页面同根目录定位到8×8 BMP文件。；failure：Graphics/UI/Town Map/mapRegion0.png底图与Graphics目录缺失，仍不能证明完整页面呈现。；boundary：两个标记图可得不解除区域底图/浏览器/交互运行未知；不创建或补修任何参考资源。
当前与应交付事实的差异：current：缺项说明把根目录两个标记图与缺失Graphics资源合并成均无。；expected：可得标记图与缺失区域底图分别列；标记图身份可追溯，渲染效果继续未验证。
用户影响：交接者会错误索取已有素材或把可读标记资源列入missing_transfer，歪曲静态覆盖边界。；实现风险：缺素材限制的分母与可得文件覆盖不一致，未来验证计划重复或误冻结可做范围。
跨模块消费者：M01资源身份；M03资源匹配；M12区域地图作者工具/缺项表
历史finding/旧候选/去重关系：relation：NEW_EXACT_AVAILABILITY_EVIDENCE_NOT_REOPEN；notes：保留旧宿主/Graphics/Demo未知；不由新存在性修正扩大旧FINAL范围或改写历史裁决。；alias：
具体建议（不是已经修复）：仅修本轮建议范围内的未来WP75素材缺项与相邻引用说明，注明两BMP可得而底图缺失；无需生成素材或运行工具。
可验证完成标准：可得表逐列记录两个固定BMP路径/身份；缺项表不再称它们均无；Graphics区域底图/宿主/实际运行未知继续保留且不宣称Demo通过
依赖：M01资源身份与M03实际资源缺项列表一致；未知/缺资料：真实浏览器渲染/图示外观未运行观察。
实际root裁决：reviewer：/root；decision：CONFIRMED_WITH_PREMISES_AND_LIMITS；basis：独立module完整领域报告 + root逐项前提/反例及关键source/spec定点复读；具体阅读范围见root-integration-reading-log.tsv。未移转旧审核签名，未运行。
兼容/重设计分类：BEHAVIOR_OR_DATA_CONTRACT; FUTURE_ARCHITECTURE_FREE

### GR3-M12-002｜P2｜REQUIRED_REVISION｜设施队伍结算把应累计的已结算场次误写为清空后的历史长度

模块/能力/类别：M12；生成器累计场次、低分替换与退休阈值；Demo / Developer Experience / Generic Kernel。处置状态：CONFIRMED；实际reviewer：/root/m12_developer_tools_v3。
证据层级：SUPPORTED_STATIC; NOT_EXECUTED。
- 来源R：`Data/Scripts/018_Alternate battle modes/003_Battle Frontier generator/004_ChallengeGenerator_BattleSim.rb`；blob `3d74238e2e7319ad487445b4e037a4167929456e`；定位 48–65;126–129；本reviewer实读全文件：可见累计含当前历史；成功结算累计增加结算前后历史长度之差，正常清空时增加结算前全部场次。
- 来源R：`Data/Scripts/018_Alternate battle modes/003_Battle Frontier generator/001_ChallengeGenerator_Data.rb`；blob `7fb8c0682643ae974d9071f576263ae7249ff519`；定位 196–215;247–252；80/250场阈值与结算后的检查点使用累计场次；新队伍才从零开始。
- 规格S：`deliverables/final-specification-set/demo-dx/wp76-facility-content-generation-and-simulation.md`；blob `cdbc2fa0ce47e2eb543426bbd28e49c360b60686`；定位 §7.4 line189;§6.4 line144；正文声称把刚清空的历史长度加入累计，正常清空后该长度为0；与源更新量及自身阈值消费相冲突。

适用前提：合法队伍、评级数据与有限历史；本次评级更新正常完成并清空历史；没有替换队伍、外部修改或异常；阈值对照保留之前各分支不命中条件
正常/失败/边界或最小反例：normal：已结算累计70、当前历史12：结算前可见82；成功结算后历史0、已结算累计82，可见仍82。；failure：评级更新抛错早于历史清空时，不承诺完成累计更新或评级全字段事务回滚；本发现只核场次正常结算。；boundary：空历史成功更新场次增量0；已累计238＋12后得250，若评分70、至少2成员、下标小于600且更早条件均不命中，下一轮退休门可命中。
当前与应交付事实的差异：current：清历史后累计清空后长度（0），可被独立实现为各轮累计不增长。；expected：先保留本次已结算历史场数，成功清空后把该已结算数量累计；可见累计在结算前后不减少。
用户影响：按正文实现可能使80场低分替换及250场退休永不从多轮积累触发，改变池回收、队伍寿命与检查点再开语义。；实现风险：评级公式虽正确，迭代消费者仍会因场次数丢失而改变生成内容。
跨模块消费者：WP76队伍更替五支；WP76检查点继续与队伍累计场次；GN-M14/GN-M20测试设计
历史finding/旧候选/去重关系：relation：NEW_CURRENT_CLAUSE_DEFECT；notes：41项M12历史控制无本场次累加争点；不是重复新开既有评级或退休分支裁决。 原非必修GIR-FD82-D012限定WP52-C降PP4早退/末尾−10与C41算术，和本累计场次前提不同；保持旧裁决、不重开。；alias：
具体建议（不是已经修复）：将line189改为累计本次实际已结算场数，补成功结算前后累计不变与跨轮达到80/250的静态向量；保持数学评级变体及异常边界。
可验证完成标准：70＋12正常结算后累计82、历史0、可见82；238＋12正常结算后累计250，具备此前分支不命中的退休向量；空历史增量0；不把异常更新描述为评级全字段事务回滚
依赖：WP76§6.4/§7.4与GN-M14/GN-M20一致；未知/缺资料：未运行参考或静态案例；实际评级异常与宿主表现未验证。
实际root裁决：reviewer：/root；decision：CONFIRMED_WITH_PREMISES_AND_LIMITS；basis：独立module完整领域报告 + root逐项前提/反例及关键source/spec定点复读；具体阅读范围见root-integration-reading-log.tsv。未移转旧审核签名，未运行。
兼容/重设计分类：BEHAVIOR_OR_DATA_CONTRACT; FUTURE_ARCHITECTURE_FREE

## 5. 原229/341、去重与交界

完整229原/批准完整对象、有效前提/反例/minimum/determinate/root和extensions、FINAL1对象及当前模块消费投影在固定A的regression-229.tsv及integration regression-229-joins.json，精确指针/对象SHA可解引用。原341 map和当前accepted-341-joins.json逐batch/ID/candidate/ACT/independent_report五元组保存local资格/条款/范围/当前关系；同ID多批记录不合并扩大，不因新finding自动重开或回写旧台账。下表完整列229 ID→本轮投影→原接受keys→新关系，每个key的完整341 tuple/scope在manifest及固定附件。

| 原ID | 本轮模块/有限消费 | 原scoped贡献keys | 新关联 |
| --- | --- | --- | --- |
| GIR-FD82-001 | M03;M11;M12；有限scope join完成/未执行 | B01/GIR-FD82-001;B18/GIR-FD82-001;B21/GIR-FD82-001 |  |
| GIR-FD82-002 | M03;M11；有限scope join完成/未执行 | B03/GIR-FD82-002;B04/GIR-FD82-002;B14/GIR-FD82-002;B21/GIR-FD82-002 |  |
| GIR-FD82-003 | M03;M06;M07;M08;M09;M10;M11;M12；有限scope join完成/未执行 | B04/GIR-FD82-003;B08/GIR-FD82-003;B09/GIR-FD82-003;B10/GIR-FD82-003;B12/GIR-FD82-003;B13/GIR-FD82-003;B14/GIR-FD82-003;B15/GIR-FD82-003;B16/GIR-FD82-003;B17/GIR-FD82-003;B19/GIR-FD82-003;B20/GIR-FD82-003;B21/GIR-FD82-003 | GR3-M08-001 |
| GIR-FD82-004 | M10；有限scope join完成/未执行 | B16/GIR-FD82-004 |  |
| GIR-FD82-005 | M07;M10；有限scope join完成/未执行 | B09/GIR-FD82-005;B17/GIR-FD82-005 |  |
| GIR-FD82-006 | M10；有限scope join完成/未执行 | B04/GIR-FD82-006;B16/GIR-FD82-006;B21/GIR-FD82-006 |  |
| GIR-FD82-A001 | M01；有限scope join完成/未执行 | B01/GIR-FD82-A001 |  |
| GIR-FD82-A002 | M01；有限scope join完成/未执行 | B01/GIR-FD82-A002 |  |
| GIR-FD82-A003 | M02；有限scope join完成/未执行 | B01/GIR-FD82-A003 |  |
| GIR-FD82-A004 | M02；有限scope join完成/未执行 | B01/GIR-FD82-A004 |  |
| GIR-FD82-A006 | M01；有限scope join完成/未执行 | B01/GIR-FD82-A006;B02/GIR-FD82-A006 |  |
| GIR-FD82-A009 | M02；有限scope join完成/未执行 | B01/GIR-FD82-A009 |  |
| GIR-FD82-A010 | M02；有限scope join完成/未执行 | B02/GIR-FD82-A010 |  |
| GIR-FD82-A011 | M02；有限scope join完成/未执行 | B02/GIR-FD82-A011 |  |
| GIR-FD82-A012 | M02；有限scope join完成/未执行 | B02/GIR-FD82-A012 |  |
| GIR-FD82-A013 | M01；有限scope join完成/未执行 | B02/GIR-FD82-A013 | GR3-M01-001 |
| GIR-FD82-A014 | M02；有限scope join完成/未执行 | B02/GIR-FD82-A014 |  |
| GIR-FD82-A015 | M02;M10；有限scope join完成/未执行 | B02/GIR-FD82-A015;B16/GIR-FD82-A015 |  |
| GIR-FD82-A016 | M02；有限scope join完成/未执行 | B02/GIR-FD82-A016 |  |
| GIR-FD82-A017 | M02；有限scope join完成/未执行 | B02/GIR-FD82-A017;B21/GIR-FD82-A017 |  |
| GIR-FD82-A018 | M01;M02；有限scope join完成/未执行 | B02/GIR-FD82-A018 | GR3-M01-001 |
| GIR-FD82-A020 | M01;M04;M05；有限scope join完成/未执行 | B01/GIR-FD82-A020;B05/GIR-FD82-A020;B07/GIR-FD82-A020 |  |
| GIR-FD82-A021 | M04；有限scope join完成/未执行 | B05/GIR-FD82-A021 |  |
| GIR-FD82-A022 | M04；有限scope join完成/未执行 | B05/GIR-FD82-A022 |  |
| GIR-FD82-A023 | M04；有限scope join完成/未执行 | B05/GIR-FD82-A023 |  |
| GIR-FD82-A024 | M04;M06；有限scope join完成/未执行 | B05/GIR-FD82-A024;B07/GIR-FD82-A024 |  |
| GIR-FD82-A025 | M04；有限scope join完成/未执行 | B05/GIR-FD82-A025 |  |
| GIR-FD82-A026 | M04;M05；有限scope join完成/未执行 | B05/GIR-FD82-A026;B07/GIR-FD82-A026 |  |
| GIR-FD82-A027 | M04；有限scope join完成/未执行 | B05/GIR-FD82-A027 |  |
| GIR-FD82-A028 | M04；有限scope join完成/未执行 | B05/GIR-FD82-A028 |  |
| GIR-FD82-A029 | M04；有限scope join完成/未执行 | B05/GIR-FD82-A029 |  |
| GIR-FD82-A030 | M04；有限scope join完成/未执行 | B05/GIR-FD82-A030 |  |
| GIR-FD82-A031 | M04；有限scope join完成/未执行 | B05/GIR-FD82-A031 |  |
| GIR-FD82-A032 | M05；有限scope join完成/未执行 | B06/GIR-FD82-A032 |  |
| GIR-FD82-A033 | M05；有限scope join完成/未执行 | B06/GIR-FD82-A033 |  |
| GIR-FD82-A034 | M05;M06；有限scope join完成/未执行 | B06/GIR-FD82-A034;B08/GIR-FD82-A034 |  |
| GIR-FD82-A035 | M05；有限scope join完成/未执行 | B06/GIR-FD82-A035 |  |
| GIR-FD82-A036 | M04;M05；有限scope join完成/未执行 | B06/GIR-FD82-A036 |  |
| GIR-FD82-A037 | M04;M05；有限scope join完成/未执行 | B06/GIR-FD82-A037 |  |
| GIR-FD82-A038 | M05；有限scope join完成/未执行 | B06/GIR-FD82-A038 |  |
| GIR-FD82-A039 | M05；有限scope join完成/未执行 | B07/GIR-FD82-A039 |  |
| GIR-FD82-A040 | M04;M05;M12；有限scope join完成/未执行 | B05/GIR-FD82-A040;B07/GIR-FD82-A040;B17/GIR-FD82-A040 |  |
| GIR-FD82-A041 | M05；有限scope join完成/未执行 | B07/GIR-FD82-A041 |  |
| GIR-FD82-A043 | M05；有限scope join完成/未执行 | B07/GIR-FD82-A043 |  |
| GIR-FD82-A044 | M04;M05;M06;M10；有限scope join完成/未执行 | B05/GIR-FD82-A044;B07/GIR-FD82-A044;B16/GIR-FD82-A044 |  |
| GIR-FD82-A045 | M05;M06；有限scope join完成/未执行 | B07/GIR-FD82-A045 |  |
| GIR-FD82-A046 | M05;M08;M09；有限scope join完成/未执行 | B07/GIR-FD82-A046;B11/GIR-FD82-A046;B12/GIR-FD82-A046 | GR3-M08-001 |
| GIR-FD82-A047 | M05;M06;M07；有限scope join完成/未执行 | B07/GIR-FD82-A047;B09/GIR-FD82-A047 | GR3-M06-001 |
| GIR-FD82-A048 | M06;M10；有限scope join完成/未执行 | B07/GIR-FD82-A048;B16/GIR-FD82-A048 |  |
| GIR-FD82-A049 | M06;M07；有限scope join完成/未执行 | B07/GIR-FD82-A049;B09/GIR-FD82-A049 |  |
| GIR-FD82-A050 | M06;M10；有限scope join完成/未执行 | B07/GIR-FD82-A050;B17/GIR-FD82-A050 |  |
| GIR-FD82-A051 | M06；有限scope join完成/未执行 | B07/GIR-FD82-A051 |  |
| GIR-FD82-A052 | M05;M06；有限scope join完成/未执行 | B08/GIR-FD82-A052 |  |
| GIR-FD82-A053 | M04;M06；有限scope join完成/未执行 | B08/GIR-FD82-A053 |  |
| GIR-FD82-A054 | M11；有限scope join完成/未执行 | B15/GIR-FD82-A054 |  |
| GIR-FD82-A055 | M10;M11；有限scope join完成/未执行 | B15/GIR-FD82-A055;B16/GIR-FD82-A055 |  |
| GIR-FD82-A056 | M10;M11；有限scope join完成/未执行 | B15/GIR-FD82-A056;B16/GIR-FD82-A056 |  |
| GIR-FD82-A057 | M06;M11；有限scope join完成/未执行 | B15/GIR-FD82-A057 |  |
| GIR-FD82-A058 | M03;M10；有限scope join完成/未执行 | B04/GIR-FD82-A058;B16/GIR-FD82-A058;B21/GIR-FD82-A058 |  |
| GIR-FD82-A059 | M03;M05;M07;M10；有限scope join完成/未执行 | B04/GIR-FD82-A059;B06/GIR-FD82-A059;B09/GIR-FD82-A059;B17/GIR-FD82-A059;B21/GIR-FD82-A059 |  |
| GIR-FD82-B001 | M07；有限scope join完成/未执行 | B09/GIR-FD82-B001 |  |
| GIR-FD82-B002 | M07；有限scope join完成/未执行 | B09/GIR-FD82-B002 |  |
| GIR-FD82-B003 | M07;M08;M09；有限scope join完成/未执行 | B09/GIR-FD82-B003;B11/GIR-FD82-B003;B13/GIR-FD82-B003 | GR3-M08-001 |
| GIR-FD82-B005 | M06;M07；有限scope join完成/未执行 | B09/GIR-FD82-B005 |  |
| GIR-FD82-B006 | M07；有限scope join完成/未执行 | B09/GIR-FD82-B006 |  |
| GIR-FD82-B007 | M06;M08；有限scope join完成/未执行 | B09/GIR-FD82-B007;B11/GIR-FD82-B007 | GR3-M08-001 |
| GIR-FD82-B008 | M05;M07；有限scope join完成/未执行 | B07/GIR-FD82-B008;B09/GIR-FD82-B008 | GR3-M07-001 |
| GIR-FD82-B009 | M07；有限scope join完成/未执行 | B09/GIR-FD82-B009 |  |
| GIR-FD82-B010 | M07;M08;M09；有限scope join完成/未执行 | B10/GIR-FD82-B010;B13/GIR-FD82-B010 | GR3-M08-001 |
| GIR-FD82-B011 | M07；有限scope join完成/未执行 | B09/GIR-FD82-B011 |  |
| GIR-FD82-B012 | M07；有限scope join完成/未执行 | B09/GIR-FD82-B012 |  |
| GIR-FD82-B013 | M04;M06;M07；有限scope join完成/未执行 | B07/GIR-FD82-B013;B09/GIR-FD82-B013 |  |
| GIR-FD82-B014 | M07;M08；有限scope join完成/未执行 | B09/GIR-FD82-B014;B11/GIR-FD82-B014 | GR3-M08-001 |
| GIR-FD82-B015 | M07;M08；有限scope join完成/未执行 | B09/GIR-FD82-B015;B10/GIR-FD82-B015 | GR3-M08-001 |
| GIR-FD82-B016 | M07；有限scope join完成/未执行 | B10/GIR-FD82-B016 |  |
| GIR-FD82-B017 | M07;M08;M09；有限scope join完成/未执行 | B10/GIR-FD82-B017;B12/GIR-FD82-B017 | GR3-M08-001 |
| GIR-FD82-B018 | M07;M08;M09；有限scope join完成/未执行 | B10/GIR-FD82-B018;B11/GIR-FD82-B018;B13/GIR-FD82-B018 | GR3-M08-001 |
| GIR-FD82-B019 | M08；有限scope join完成/未执行 | B11/GIR-FD82-B019 | GR3-M08-001 |
| GIR-FD82-B020 | M05;M08;M09；有限scope join完成/未执行 | B12/GIR-FD82-B020 | GR3-M08-001 |
| GIR-FD82-B021 | M08;M09；有限scope join完成/未执行 | B12/GIR-FD82-B021 | GR3-M08-001 |
| GIR-FD82-B022 | M08;M09；有限scope join完成/未执行 | B12/GIR-FD82-B022 | GR3-M08-001 |
| GIR-FD82-B023 | M08;M09；有限scope join完成/未执行 | B12/GIR-FD82-B023 | GR3-M08-001 |
| GIR-FD82-B024 | M08;M09；有限scope join完成/未执行 | B12/GIR-FD82-B024 | GR3-M08-001 |
| GIR-FD82-B025 | M07;M09；有限scope join完成/未执行 | B09/GIR-FD82-B025;B13/GIR-FD82-B025 |  |
| GIR-FD82-B026 | M06;M11；有限scope join完成/未执行 | B08/GIR-FD82-B026;B12/GIR-FD82-B026 |  |
| GIR-FD82-B027 | M09；有限scope join完成/未执行 | B13/GIR-FD82-B027 |  |
| GIR-FD82-B028 | M09;M10；有限scope join完成/未执行 | B13/GIR-FD82-B028 | GR3-M10-004 |
| GIR-FD82-B029 | M09；有限scope join完成/未执行 | B13/GIR-FD82-B029 |  |
| GIR-FD82-B031 | M10；有限scope join完成/未执行 | B17/GIR-FD82-B031 |  |
| GIR-FD82-B032 | M04;M07;M10；有限scope join完成/未执行 | B17/GIR-FD82-B032 |  |
| GIR-FD82-B033 | M10；有限scope join完成/未执行 | B17/GIR-FD82-B033 |  |
| GIR-FD82-B034 | M10;M12；有限scope join完成/未执行 | B17/GIR-FD82-B034 |  |
| GIR-FD82-B035 | M10；有限scope join完成/未执行 | B16/GIR-FD82-B035 |  |
| GIR-FD82-C002 | M12；有限scope join完成/未执行 | B19/GIR-FD82-C002 |  |
| GIR-FD82-C003 | M02;M03;M05;M06;M10;M11;M12；有限scope join完成/未执行 | B02/GIR-FD82-C003;B03/GIR-FD82-C003;B04/GIR-FD82-C003;B07/GIR-FD82-C003;B08/GIR-FD82-C003;B14/GIR-FD82-C003;B15/GIR-FD82-C003;B16/GIR-FD82-C003;B17/GIR-FD82-C003;B18/GIR-FD82-C003;B19/GIR-FD82-C003;B20/GIR-FD82-C003;B21/GIR-FD82-C003 | GR3-M02-003 |
| GIR-FD82-C004 | M01;M06;M12；有限scope join完成/未执行 | B01/GIR-FD82-C004;B08/GIR-FD82-C004;B19/GIR-FD82-C004 |  |
| GIR-FD82-C005 | M06;M12；有限scope join完成/未执行 | B08/GIR-FD82-C005;B19/GIR-FD82-C005 |  |
| GIR-FD82-C007 | M02;M03;M06;M11;M12；有限scope join完成/未执行 | B03/GIR-FD82-C007;B04/GIR-FD82-C007;B08/GIR-FD82-C007;B14/GIR-FD82-C007;B15/GIR-FD82-C007;B19/GIR-FD82-C007;B20/GIR-FD82-C007;B21/GIR-FD82-C007 |  |
| GIR-FD82-C008 | M12；有限scope join完成/未执行 | B19/GIR-FD82-C008 |  |
| GIR-FD82-C009 | M10;M12；有限scope join完成/未执行 | B19/GIR-FD82-C009 |  |
| GIR-FD82-C010 | M12；有限scope join完成/未执行 | B19/GIR-FD82-C010 |  |
| GIR-FD82-C011 | M07;M12；有限scope join完成/未执行 | B10/GIR-FD82-C011;B19/GIR-FD82-C011 |  |
| GIR-FD82-C012 | M12；有限scope join完成/未执行 | B19/GIR-FD82-C012 |  |
| GIR-FD82-C013 | M12；有限scope join完成/未执行 | B19/GIR-FD82-C013 |  |
| GIR-FD82-C014 | M12；有限scope join完成/未执行 | B19/GIR-FD82-C014 |  |
| GIR-FD82-C015 | M12；有限scope join完成/未执行 | B19/GIR-FD82-C015 |  |
| GIR-FD82-C016 | M01;M12；有限scope join完成/未执行 | B01/GIR-FD82-C016;B19/GIR-FD82-C016 |  |
| GIR-FD82-C017 | M12；有限scope join完成/未执行 | B19/GIR-FD82-C017 |  |
| GIR-FD82-C018 | M12；有限scope join完成/未执行 | B19/GIR-FD82-C018 |  |
| GIR-FD82-C019 | M12；有限scope join完成/未执行 | B19/GIR-FD82-C019 |  |
| GIR-FD82-C020 | M11;M12；有限scope join完成/未执行 | B15/GIR-FD82-C020;B19/GIR-FD82-C020;B20/GIR-FD82-C020 |  |
| GIR-FD82-C021 | M12；有限scope join完成/未执行 | B19/GIR-FD82-C021 |  |
| GIR-FD82-C022 | M01;M12；有限scope join完成/未执行 | B01/GIR-FD82-C022;B19/GIR-FD82-C022 |  |
| GIR-FD82-C023 | M12；有限scope join完成/未执行 | B19/GIR-FD82-C023 |  |
| GIR-FD82-C024 | M12；有限scope join完成/未执行 | B20/GIR-FD82-C024 |  |
| GIR-FD82-C025 | M12；有限scope join完成/未执行 | B20/GIR-FD82-C025 |  |
| GIR-FD82-C026 | M12；有限scope join完成/未执行 | B20/GIR-FD82-C026 |  |
| GIR-FD82-C027 | M12；有限scope join完成/未执行 | B20/GIR-FD82-C027 |  |
| GIR-FD82-C028 | M11;M12；有限scope join完成/未执行 | B20/GIR-FD82-C028 |  |
| GIR-FD82-C029 | M12；有限scope join完成/未执行 | B20/GIR-FD82-C029;B21/GIR-FD82-C029 |  |
| GIR-FD82-C030 | M12；有限scope join完成/未执行 | B20/GIR-FD82-C030 |  |
| GIR-FD82-C031 | M12；有限scope join完成/未执行 | B20/GIR-FD82-C031 |  |
| GIR-FD82-C032 | M12；有限scope join完成/未执行 | B20/GIR-FD82-C032 |  |
| GIR-FD82-C033 | M12；有限scope join完成/未执行 | B20/GIR-FD82-C033 |  |
| GIR-FD82-C034 | M12；有限scope join完成/未执行 | B20/GIR-FD82-C034 |  |
| GIR-FD82-C035 | M03；有限scope join完成/未执行 | B03/GIR-FD82-C035 |  |
| GIR-FD82-C036 | M03；有限scope join完成/未执行 | B03/GIR-FD82-C036 |  |
| GIR-FD82-C037 | M03；有限scope join完成/未执行 | B03/GIR-FD82-C037 |  |
| GIR-FD82-C038 | M03；有限scope join完成/未执行 | B03/GIR-FD82-C038 |  |
| GIR-FD82-C039 | M03；有限scope join完成/未执行 | B03/GIR-FD82-C039 |  |
| GIR-FD82-C040 | M03；有限scope join完成/未执行 | B03/GIR-FD82-C040 |  |
| GIR-FD82-C041 | M03；有限scope join完成/未执行 | B03/GIR-FD82-C041 |  |
| GIR-FD82-C042 | M03；有限scope join完成/未执行 | B03/GIR-FD82-C042 |  |
| GIR-FD82-C043 | M03；有限scope join完成/未执行 | B03/GIR-FD82-C043 |  |
| GIR-FD82-C044 | M03；有限scope join完成/未执行 | B03/GIR-FD82-C044 | GR3-M03-002 |
| GIR-FD82-C045 | M03；有限scope join完成/未执行 | B03/GIR-FD82-C045 | GR3-M03-002 |
| GIR-FD82-C046 | M03；有限scope join完成/未执行 | B03/GIR-FD82-C046 |  |
| GIR-FD82-C047 | M03；有限scope join完成/未执行 | B03/GIR-FD82-C047 | GR3-M03-002 |
| GIR-FD82-C048 | M03；有限scope join完成/未执行 | B03/GIR-FD82-C048 |  |
| GIR-FD82-C049 | M03；有限scope join完成/未执行 | B03/GIR-FD82-C049 |  |
| GIR-FD82-C050 | M03；有限scope join完成/未执行 | B03/GIR-FD82-C050 |  |
| GIR-FD82-C051 | M03;M12；有限scope join完成/未执行 | B03/GIR-FD82-C051;B20/GIR-FD82-C051 |  |
| GIR-FD82-C052 | M03；有限scope join完成/未执行 | B03/GIR-FD82-C052 |  |
| GIR-FD82-C053 | M03;M10；有限scope join完成/未执行 | B03/GIR-FD82-C053;B04/GIR-FD82-C053 |  |
| GIR-FD82-C054 | M03；有限scope join完成/未执行 | B03/GIR-FD82-C054 |  |
| GIR-FD82-C055 | M03；有限scope join完成/未执行 | B04/GIR-FD82-C055 |  |
| GIR-FD82-C056 | M03;M10；有限scope join完成/未执行 | B04/GIR-FD82-C056 |  |
| GIR-FD82-C057 | M03；有限scope join完成/未执行 | B04/GIR-FD82-C057 |  |
| GIR-FD82-C058 | M03;M10；有限scope join完成/未执行 | B04/GIR-FD82-C058;B16/GIR-FD82-C058 |  |
| GIR-FD82-C059 | M03；有限scope join完成/未执行 | B04/GIR-FD82-C059 |  |
| GIR-FD82-C060 | M03；有限scope join完成/未执行 | B04/GIR-FD82-C060 |  |
| GIR-FD82-C061 | M03;M10；有限scope join完成/未执行 | B04/GIR-FD82-C061 |  |
| GIR-FD82-C062 | M03；有限scope join完成/未执行 | B04/GIR-FD82-C062 |  |
| GIR-FD82-C063 | M03；有限scope join完成/未执行 | B04/GIR-FD82-C063 |  |
| GIR-FD82-C064 | M03；有限scope join完成/未执行 | B04/GIR-FD82-C064 |  |
| GIR-FD82-C065 | M03；有限scope join完成/未执行 | B04/GIR-FD82-C065 |  |
| GIR-FD82-C066 | M03；有限scope join完成/未执行 | B04/GIR-FD82-C066 |  |
| GIR-FD82-C067 | M03；有限scope join完成/未执行 | B03/GIR-FD82-C067;B04/GIR-FD82-C067 |  |
| GIR-FD82-C068 | M03；有限scope join完成/未执行 | B04/GIR-FD82-C068 |  |
| GIR-FD82-C069 | M03；有限scope join完成/未执行 | B04/GIR-FD82-C069 |  |
| GIR-FD82-C070 | M10；有限scope join完成/未执行 | B04/GIR-FD82-C070 |  |
| GIR-FD82-C071 | M10；有限scope join完成/未执行 | B04/GIR-FD82-C071 |  |
| GIR-FD82-C072 | M10；有限scope join完成/未执行 | B04/GIR-FD82-C072 |  |
| GIR-FD82-C073 | M10；有限scope join完成/未执行 | B04/GIR-FD82-C073 |  |
| GIR-FD82-C074 | M10；有限scope join完成/未执行 | B04/GIR-FD82-C074 |  |
| GIR-FD82-C075 | M10；有限scope join完成/未执行 | B04/GIR-FD82-C075 |  |
| GIR-FD82-C076 | M10；有限scope join完成/未执行 | B04/GIR-FD82-C076 |  |
| GIR-FD82-C077 | M03；有限scope join完成/未执行 | B04/GIR-FD82-C077 |  |
| GIR-FD82-C078 | M03；有限scope join完成/未执行 | B04/GIR-FD82-C078 |  |
| GIR-FD82-C079 | M06；有限scope join完成/未执行 | B08/GIR-FD82-C079 |  |
| GIR-FD82-C080 | M01;M06；有限scope join完成/未执行 | B01/GIR-FD82-C080;B08/GIR-FD82-C080 |  |
| GIR-FD82-C081 | M02;M06；有限scope join完成/未执行 | B02/GIR-FD82-C081;B08/GIR-FD82-C081 |  |
| GIR-FD82-C082 | M06；有限scope join完成/未执行 | B08/GIR-FD82-C082 |  |
| GIR-FD82-C083 | M06;M12；有限scope join完成/未执行 | B08/GIR-FD82-C083;B20/GIR-FD82-C083 |  |
| GIR-FD82-C084 | M06；有限scope join完成/未执行 | B08/GIR-FD82-C084 |  |
| GIR-FD82-C085 | M06；有限scope join完成/未执行 | B08/GIR-FD82-C085 |  |
| GIR-FD82-C086 | M11；有限scope join完成/未执行 | B14/GIR-FD82-C086 |  |
| GIR-FD82-C087 | M11；有限scope join完成/未执行 | B14/GIR-FD82-C087 |  |
| GIR-FD82-C088 | M11；有限scope join完成/未执行 | B14/GIR-FD82-C088 |  |
| GIR-FD82-C089 | M11；有限scope join完成/未执行 | B14/GIR-FD82-C089 |  |
| GIR-FD82-C091 | M11；有限scope join完成/未执行 | B14/GIR-FD82-C091 |  |
| GIR-FD82-C092 | M11；有限scope join完成/未执行 | B14/GIR-FD82-C092 |  |
| GIR-FD82-C093 | M03;M11；有限scope join完成/未执行 | B04/GIR-FD82-C093;B14/GIR-FD82-C093 |  |
| GIR-FD82-C094 | M03;M11；有限scope join完成/未执行 | B03/GIR-FD82-C094;B14/GIR-FD82-C094 |  |
| GIR-FD82-C095 | M03;M11；有限scope join完成/未执行 | B03/GIR-FD82-C095;B14/GIR-FD82-C095 |  |
| GIR-FD82-C096 | M06；有限scope join完成/未执行 | B08/GIR-FD82-C096 |  |
| GIR-FD82-C097 | M11；有限scope join完成/未执行 | B14/GIR-FD82-C097 |  |
| GIR-FD82-C098 | M03;M11；有限scope join完成/未执行 | B14/GIR-FD82-C098 |  |
| GIR-FD82-C099 | M03;M11；有限scope join完成/未执行 | B14/GIR-FD82-C099 |  |
| GIR-FD82-C100 | M11；有限scope join完成/未执行 | B14/GIR-FD82-C100 |  |
| GIR-FD82-C101 | M11；有限scope join完成/未执行 | B14/GIR-FD82-C101 |  |
| GIR-FD82-C102 | M11；有限scope join完成/未执行 | B14/GIR-FD82-C102 |  |
| GIR-FD82-C103 | M05;M11；有限scope join完成/未执行 | B06/GIR-FD82-C103;B14/GIR-FD82-C103 |  |
| GIR-FD82-C104 | M11；有限scope join完成/未执行 | B14/GIR-FD82-C104 |  |
| GIR-FD82-C105 | M11；有限scope join完成/未执行 | B14/GIR-FD82-C105 |  |
| GIR-FD82-C106 | M03;M11；有限scope join完成/未执行 | B04/GIR-FD82-C106;B14/GIR-FD82-C106 |  |
| GIR-FD82-C107 | M11；有限scope join完成/未执行 | B15/GIR-FD82-C107 |  |
| GIR-FD82-C108 | M11；有限scope join完成/未执行 | B15/GIR-FD82-C108 |  |
| GIR-FD82-C109 | M10;M11；有限scope join完成/未执行 | B15/GIR-FD82-C109 |  |
| GIR-FD82-C110 | M11；有限scope join完成/未执行 | B15/GIR-FD82-C110 | GR3-M11-001 |
| GIR-FD82-C111 | M11；有限scope join完成/未执行 | B15/GIR-FD82-C111 | GR3-M11-001 |
| GIR-FD82-C112 | M11；有限scope join完成/未执行 | B15/GIR-FD82-C112 |  |
| GIR-FD82-C113 | M10;M11；有限scope join完成/未执行 | B15/GIR-FD82-C113 |  |
| GIR-FD82-C114 | M10；有限scope join完成/未执行 | B16/GIR-FD82-C114 |  |
| GIR-FD82-C115 | M10；有限scope join完成/未执行 | B16/GIR-FD82-C115 |  |
| GIR-FD82-C117 | M10；有限scope join完成/未执行 | B16/GIR-FD82-C117 |  |
| GIR-FD82-C118 | M03;M10；有限scope join完成/未执行 | B04/GIR-FD82-C118;B16/GIR-FD82-C118 |  |
| GIR-FD82-C119 | M10；有限scope join完成/未执行 | B17/GIR-FD82-C119 |  |
| GIR-FD82-C120 | M05;M10；有限scope join完成/未执行 | B06/GIR-FD82-C120;B16/GIR-FD82-C120 |  |
| GIR-FD82-C121 | M10；有限scope join完成/未执行 | B16/GIR-FD82-C121 |  |
| GIR-FD82-C122 | M10;M11；有限scope join完成/未执行 | B15/GIR-FD82-C122;B16/GIR-FD82-C122 |  |
| GIR-FD82-C123 | M10；有限scope join完成/未执行 | B16/GIR-FD82-C123 |  |
| GIR-FD82-C124 | M04;M10；有限scope join完成/未执行 | B05/GIR-FD82-C124;B16/GIR-FD82-C124 |  |
| GIR-FD82-C125 | M10；有限scope join完成/未执行 | B16/GIR-FD82-C125 | GR3-M10-001 |
| GIR-FD82-C126 | M04;M10；有限scope join完成/未执行 | B05/GIR-FD82-C126;B16/GIR-FD82-C126 |  |
| GIR-FD82-C127 | M06;M11；有限scope join完成/未执行 | B18/GIR-FD82-C127 |  |
| GIR-FD82-C128 | M11；有限scope join完成/未执行 | B18/GIR-FD82-C128 |  |
| GIR-FD82-C129 | M11；有限scope join完成/未执行 | B18/GIR-FD82-C129 |  |
| GIR-FD82-C130 | M11；有限scope join完成/未执行 | B18/GIR-FD82-C130 |  |
| GIR-FD82-C131 | M11；有限scope join完成/未执行 | B18/GIR-FD82-C131 |  |
| GIR-FD82-D018 | M07;M10；有限scope join完成/未执行 | B09/GIR-FD82-D018;B17/GIR-FD82-D018 |  |
| GIR-FD82-D023 | M05;M10；有限scope join完成/未执行 | B07/GIR-FD82-D023;B16/GIR-FD82-D023 |  |
| GIR-FD82-D024 | M12；有限scope join完成/未执行 | B20/GIR-FD82-D024 |  |
| GIR-FD82-D025 | M12；有限scope join完成/未执行 | B19/GIR-FD82-D025 |  |
| WP80-B02-R01 | M01；有限scope join完成/未执行 | B01/WP80-B02-R01 |  |
| WP80-B02-R02 | M01；有限scope join完成/未执行 | B01/WP80-B02-R02;B21/WP80-B02-R02 |  |
| WP80-INTAKE-C01 | INTEGRATION；有限scope join完成/未执行 | B21/WP80-INTAKE-C01 |  |
| WP80-INTAKE-R01 | M03;M11;M12；有限scope join完成/未执行 | B03/WP80-INTAKE-R01;B14/WP80-INTAKE-R01;B19/WP80-INTAKE-R01;B20/WP80-INTAKE-R01;B21/WP80-INTAKE-R01 |  |
| WP80-INTAKE-R02 | M11；有限scope join完成/未执行 | B18/WP80-INTAKE-R02;B21/WP80-INTAKE-R02 |  |

原4非必修A019/B030/D012/D017保原完整裁决：历史阶段语句、录像联合默认恢复、AI PP分段早退、已有目标取序表均不能仅局部删文重开。GR3-M12-002与D012不是同根；GR3-M10-004是旧B028正确领域之外当前UI残留；GR3-M11-001不同于C110长度/C111首条消费者。M02-003原必修提交、M10完整集合反证、root NoRequired皆保留，不能删除异议或方便集成重新降/升级。精确重复新finding=0，同域/同carrier相关不是别名。dedup-aliases及每项historical_relation保全部关系。

可复用证据排除：FINAL1 A022邻接“withMoves=false跳创建form回调”与A059“无记忆Q设置timer”两句不再复用；当前source/formal分别是moves只关招式、取消已有timer，原件/CLOSED不改。G2-5挖矿播种、G6-5qty8/10/12统计2/3/3为旧导航误句；实际Lottery/地牢播种与成功一株总+1、qty≥max另+1。G5-1音乐在internal/EXP门前。M08 AI217导航含4标题，M09实际213设计行有限补读，仍NOT_EXECUTED。初始无分配的统计C01/G9-3管理接口由独立integration有界补，不增GR3义务/递归门。

54既有交界/8链与18新增链完整具体正常失败边界及当前source/spec/premise/未知在junction-results.json与junction-review.md。root实际逐62当前判据读完并裁决，独立integration也给记录。相关新finding有些是carrier联系，不自动证明每个接口新反例；旧CLOSED不改。下面列全部18新增链，必须共同修订/验收的消费与共享文件依赖不能漏：

- N01 内容文本→导出/导入→消费：GR3-M01-001,GR3-M01-002,GR3-M01-003,GR3-M01-004；空译/井号/端部空格与稀疏地图桶的准入和输出不同；默认电话第二节覆盖，联系人重复仍拒；先删除/截断可能已发生。
- N02 通知/步骤→持久状态：GR3-M02-001；计步/前处理器写入后中处理器异常，后订阅者/遭遇不能保证到达；正常顺序保持，异常不能自动作为隔离继续。
- N03 持久注册→保存/读取/撤销：GR3-M02-002；同ID双注册保两个回调；保存后项值覆盖，读取两次同终值，验证各自谓词，撤销同ID全部；有效默认17单元不变。
- N04 查询未驻留图→地牢随机/暂存：GR3-M03-002；临时建立也发生成通知，清待播种子/重播全局随机、成功摆放写transfer暂存；驻留复用不重建。默认地图缺失不证明可达。
- N05 读档→进入清记录→条件恢复：GR3-M03-004；两读档分支先清地图变更记录，正常恢复辅助可见空表；额外/直接剩余异图同事件ID穿透真写在地图门外，缺事件首次失败。
- N06 SPECIAL→过场A开关/结束/重启：GR3-M03-003；严格Cut Scene注释与主解释器/事件门；空数组存在；先A再结束再启动，同轮快捷消费另按实际门，不宣称输入独占。
- N07 镜头→商店等UI等待：GR3-M03-001；速度4一格0.2秒，0.1秒64子像素；203新滚动不等，脚本包装等完成；SnapEdges与小地图限制独立。
- N08 编号/形状→真实前背精灵：GR3-M04-001；非蛋个体前背位图逐帧经过斑点回调；默认形状/位输入/2×2采样/通道夹限可审但合同未自足；species-only/图标不套。
- N09 个体字段→尺寸辅助：GR3-M05-001；原始六IV低4位/PID两低byte与物种height生成毫米，纯查询无随机/状态写；当前仅定义无静态caller，不伪造钓鱼/Demo。
- N10 隐藏事件→探测转向/消息/统计：GR3-M05-002；hiddenitem名称/自开关A、dx<8/dy<6、Manhattan和枚举平局，脚下4右转，无结果仍统计+1/effect真；不拾物。
- N11 经验变化→消息→写入/成长：GR3-M06-001；同级+1/−1也先差量提示后写经验，增经验友好与下降无友好分开；同值只提示早退。
- N12 登记消费→失败退款→同轮终局：GR3-M07-001；POTION2→登记0→首成功次无效退1且旧消费身份尚在→NORMAL终局再退2；下一命令先清与使用者倒下是反向结果1。
- N13 每击反应→消费→续击/AI：GR3-M08-001；NaturalGift/PARENTALBOND，H160/h81 ORAN，目标JABO存活：反伤20/恢复10后71且空物，第二基底nil身份访问失败；H101/单击对照不同；AI当前ORAN资格不模拟此反应。
- N14 BoxLink嵌套→旧持物提交：GR3-M10-001；A持POTION→Move缓存→盒中取回袋1清A→原目标B空确认，袋1/B持POTION/A空，总1→2；BACK保取回但不复制，无嵌套总1。
- N15 数量/文本输入→提交：GR3-M10-002,GR3-M10-003；同轮USE+BACK共享0/商店1，RIGHT+USE共享即1/商店11留；战斗列表busy未暂停只resume，普通消息skipAhead，全显才选项。
- N16 Arena领域→UI/记录：GR3-M10-004；首次对阵提示、正常补位不复位累计，count3/4/5连续判；WP56/PA-P28正确，WP67-A残留需修；旧B028不重开。
- N17 MapSize/遭遇→Area与地图查询：GR3-M11-001；Area正宽3/10000只有基格、11111为5格而非6；可见Point并集不同于WP63首条/只长度游标；缺省/零宽与隐藏门独立。
- N18 工具资源/评级历史→输出与阈值：GR3-M12-001,GR3-M12-002；两246bytes/8×8 BMP可得但底图缺；结算70+12=82，238+12=250，历史0增0；异常不承诺评级全字段原子恢复。

## 6. 有限批次、安全并行、验收与关闭

建议U01–U06六主题批，U07整合/正式登记，U08只有用户未来纳入可选范围才执行。源码/正式/公共输入冻结；未来新分支以用户明确授权的固定基点建立，先保全任何未保存变化，不用reset/clean/restore覆盖。共享文件唯一写者/有序交接，不让多个写者覆盖；角色作者与独立reviewer分离，作者自检不能当独立验收。coding/修订作者gpt-6.1-sol/xhigh，独立reviewgpt-6.1-sol/ultra，Standard(default)不Fast/不降级/不隐蔽CLI；参数请求接纳足够，回显不足UNVERIFIED，不审后台/额度/凭据。按真实平台条件并行或串行，不人为3任务上限/不强制12个额外会话。

### GR3-U01

finding IDs：GR3-M01-001,GR3-M01-002,GR3-M01-003,GR3-M01-004,GR3-M02-001,GR3-M02-002。depends_on：无。
范围/输入：PBS/本地化两个输入层、电话默认节、通知异常、同ID保存单元；WP03/04/05/08/09及两内核测试目录；固定D交付/S正式131字节/R参考，完整本轮canonical及各批实际后继冻结字节；非浮动分支
作者/共享文件：Future kernel-spec author; shared kernel catalog unique writer。预期修改：独立输入/输出与先后表、空/注释/空桶/重复条目对照、已提交前缀；原合法/默认合同保持
必须回归/交界验收：每ID接受标准＋旧A009/电话三入口/PBS新鲜度/插件顺序/保存恢复相关229投影，正常失败边界；新修订真实整合字节的独立review
并行条件：可与U03、U06不共享文件部分并行；WP09交界的最后整合在U02前完成
独立review：gpt-6.1-sol/ultra/Standard(default), independent of this batch author and registrar。交付：候选修订与精确diff/身份；作者自检且不冒独立PASS；独立review报告与输入snapshot；整合验收及依赖状态；未来获授权正式登记。有限结束：有限finding IDs与必要相关回归已处置、独立整合审阅、依赖和未证边界明确；不得借update重新全局无界review
### GR3-U02

finding IDs：GR3-M03-001,GR3-M03-002,GR3-M03-003,GR3-M03-004。depends_on：GR3-U01。
范围/输入：镜头/临时地图建立/过场跳过/事件记录恢复；WP11/12/13/14/16、WP09跨域承接；固定D交付/S正式131字节/R参考，完整本轮canonical及各批实际后继冻结字节；非浮动分支
作者/共享文件：Future world-spec author; shared WP09 final write delegated to kernel/shared integrator。预期修改：名义秒数/双轴/钳边；驻留vs临时建立；严格注释和重启；普通读档清记录与条件辅助错误区别
必须回归/交界验收：地图/通行/解释器/地牢229相关投影，G2/G5/CHAIN2，素材/真实地图和宿主未证保持
并行条件：U01 shared WP09已交接；可与U03/U06及不触世界文档的U04部分并行
独立review：gpt-6.1-sol/ultra/Standard(default), independent of this batch author and registrar。交付：候选修订与精确diff/身份；作者自检且不冒独立PASS；独立review报告与输入snapshot；整合验收及依赖状态；未来获授权正式登记。有限结束：有限finding IDs与必要相关回归已处置、独立整合审阅、依赖和未证边界明确；不得借update重新全局无界review
### GR3-U03

finding IDs：GR3-M04-001,GR3-M05-001,GR3-M05-002,GR3-M06-001。depends_on：无。
范围/输入：SPINDA斑点、个体尺寸辅助、探测仪、经验提示顺序；WP18/21/24/28/30及对应数据/测试目录；固定D交付/S正式131字节/R参考，完整本轮canonical及各批实际后继冻结字节；非浮动分支
作者/共享文件：Future creature-rules spec author; WP28 unique owner until handover U04。预期修改：独立形状/数学/单位；尺寸无静态caller限定；探测过滤/转向/统计；经验差量先提示再写，未跨级也提示
必须回归/交界验收：各固定向量/输入边界、旧Nature/形态/HP/TR/糖果取消/EXP229消费和消费者链；不跑参考或宣称真实像素
并行条件：U01/U02/U06不同文件可并行；U04的WP28等待本批冻结交接
独立review：gpt-6.1-sol/ultra/Standard(default), independent of this batch author and registrar。交付：候选修订与精确diff/身份；作者自检且不冒独立PASS；独立review报告与输入snapshot；整合验收及依赖状态；未来获授权正式登记。有限结束：有限finding IDs与必要相关回归已处置、独立整合审阅、依赖和未证边界明确；不得借update重新全局无界review
### GR3-U04

finding IDs：GR3-M07-001,GR3-M08-001。depends_on：GR3-U03。
范围/输入：战斗退款→同轮终局与自然之恩首击自耗→续击失败；WP28/40/42/46/47-A/50，UI消费者交给U05；固定D交付/S正式131字节/R参考，完整本轮canonical及各批实际后继冻结字节；非浮动分支
作者/共享文件：Future combat-spec author; shared WP28 sequential handover and designated integrator。预期修改：失败退款仍保留物品身份的条件链；NaturalGift当前空物与存在但标志不完整分开；I/C/R/P与首击前缀保留
必须回归/交界验收：两个POTION/终局/继续下一轮/濒死清choice对照，H81/H101/单击对照，旧B008/B013/multihit/helditem与AI当前预测分工
并行条件：可在U03冻结后与U02/U06不同文件工作并行；WP67-A由U05唯一写者消费本批冻结结果
独立review：gpt-6.1-sol/ultra/Standard(default), independent of this batch author and registrar。交付：候选修订与精确diff/身份；作者自检且不冒独立PASS；独立review报告与输入snapshot；整合验收及依赖状态；未来获授权正式登记。有限结束：有限finding IDs与必要相关回归已处置、独立整合审阅、依赖和未证边界明确；不得借update重新全局无界review
### GR3-U05

finding IDs：GR3-M10-001,GR3-M10-002,GR3-M10-003,GR3-M10-004,GR3-M11-001。depends_on：GR3-U03,GR3-U04。
范围/输入：BoxLink持物旧快照、数量输入竞争、战斗消息恢复、Arena UI残留、图鉴Area投影；WP62/66-A/B/C/67-A及UI/图鉴测试；固定D交付/S正式131字节/R参考，完整本轮canonical及各批实际后继冻结字节；非浮动分支
作者/共享文件：Future UI-spec author; shared UI catalog and WP67-A unique writer。预期修改：袋/持物三个终值和取消对照；同轮顺序；busy/pause/full三态；连续3/4/5判；mask/尾格/可见点并集
必须回归/交界验收：M05容量/源对象、M07退款UI可达、M09 Arena PA-P28/M11区域图首条与掩码的相邻反例；原C125/C110/C111/B028等scope保留
并行条件：与U02/U06不同文件可并行；本批整合时消费U03/U04已冻结条款，不能提前最终关闭依赖项
独立review：gpt-6.1-sol/ultra/Standard(default), independent of this batch author and registrar。交付：候选修订与精确diff/身份；作者自检且不冒独立PASS；独立review报告与输入snapshot；整合验收及依赖状态；未来获授权正式登记。有限结束：有限finding IDs与必要相关回归已处置、独立整合审阅、依赖和未证边界明确；不得借update重新全局无界review
### GR3-U06

finding IDs：GR3-M12-001,GR3-M12-002。depends_on：无。
范围/输入：townmapgen两个可得BMP与底图缺项分列、设施评级累计已结算场次；WP75/76与DX测试；固定D交付/S正式131字节/R参考，完整本轮canonical及各批实际后继冻结字节；非浮动分支
作者/共享文件：Future developer-tools spec author。预期修改：可得资源身份表、仍缺底图/浏览器运行限制；成功结算已处理数量累计与空历史/80/250阈值对照
必须回归/交界验收：246bytes/8×8身份与工具引用；70+12=82、238+12=250、空历史，旧评级/生成阈值229相关scope；M09接口联验
并行条件：与U01/U02/U03/U04/U05不共享必需修改文件，可并行；公共记录只交唯一整合写者
独立review：gpt-6.1-sol/ultra/Standard(default), independent of this batch author and registrar。交付：候选修订与精确diff/身份；作者自检且不冒独立PASS；独立review报告与输入snapshot；整合验收及依赖状态；未来获授权正式登记。有限结束：有限finding IDs与必要相关回归已处置、独立整合审阅、依赖和未证边界明确；不得借update重新全局无界review
### GR3-U07

finding IDs：GR3-M01-001,GR3-M01-002,GR3-M01-003,GR3-M01-004,GR3-M02-001,GR3-M02-002,GR3-M03-001,GR3-M03-002,GR3-M03-003,GR3-M03-004,GR3-M04-001,GR3-M05-001,GR3-M05-002,GR3-M06-001,GR3-M07-001,GR3-M08-001,GR3-M10-001,GR3-M10-002,GR3-M10-003,GR3-M10-004,GR3-M11-001,GR3-M12-001,GR3-M12-002。depends_on：GR3-U01,GR3-U02,GR3-U03,GR3-U04,GR3-U05,GR3-U06。
范围/输入：共享引用/54既有交界/8链与新增链有限整合，正式接受与最终关闭按未来实际授权；固定D交付/S正式131字节/R参考，完整本轮canonical及各批实际后继冻结字节；非浮动分支
作者/共享文件：Future global-formal integrator/registrar; never substitute for independent reviewer。预期修改：逐条整合范围/输入/作者自检/独立PASS/整合验收/正式接受/最终关闭分层登记；原229不无证据重开
必须回归/交界验收：最终真实整合字节上独立review，所有23必修及跨批依赖满足且未知保留；修改字节/前提才定点重验，不递归全历史
并行条件：前六批局部独立合格不足以提前最终关闭跨批项目；公共Feature Matrix、traceability、approval-register、junction-register唯一写者顺序整合
独立review：gpt-6.1-sol/ultra/Standard(default), independent of this batch author and registrar。交付：候选修订与精确diff/身份；作者自检且不冒独立PASS；独立review报告与输入snapshot；整合验收及依赖状态；未来获授权正式登记。有限结束：有限finding IDs与必要相关回归已处置、独立整合审阅、依赖和未证边界明确；不得借update重新全局无界review
### GR3-U08

finding IDs：GR3-M09-001,GR3-M02-003。depends_on：无。
范围/输入：仅用户将来选择：录像责任导航修订、无旧档提示显式案例；后者已无必修缺口；固定D交付/S正式131字节/R参考，完整本轮canonical及各批实际后继冻结字节；非浮动分支
作者/共享文件：Future designated optional documentation author after user scope choice。预期修改：GR3-M09-001 WP51录像消费者从WP57指WP58；GR3-M02-003仅可选显式例，不篡改完整集合可推出的现状裁决
必须回归/交界验收：不把可选和NO_REQUIRED_REVISION合并成必修或重开；如果改变bug兼容选择先记录用户决策
并行条件：WP51独立文件可并行；紧急保存可选改同核/UI共享文件时等待U01/U05并顺序整合
独立review：gpt-6.1-sol/ultra/Standard(default), independent of this batch author and registrar。交付：候选修订与精确diff/身份；作者自检且不冒独立PASS；独立review报告与输入snapshot；整合验收及依赖状态；未来获授权正式登记。有限结束：有限finding IDs与必要相关回归已处置、独立整合审阅、依赖和未证边界明确；不得借update重新全局无界review

每批在相关正常/失败/边界/交界和实际整合字节的独立review后，才按未来用户实际授权正式接受。候选、作者自检、独立PASS、整合验收、正式接受、最终关闭分层记录；批次独立合格但后续依赖未满足不能最终关闭。缺资源/未执行测试保持实际层级，不能用STATIC或数目假造runtime PASS。

共同文件owner：kernel作者/共享整合者管WP03/04/05/08/09及kernel测试，U01后才交U02的WP09；creature作者管WP18/21/24/28/30，WP28 U03→U04顺序交接；UI作者唯一管WP62/66/67-A与UI目录，消费U03/U04冻结输出；DX作者管WP75/76与DX目录；公共Feature Matrix/source traceability/approval/junction registers由将来获授权global整合登记员唯一写，独立reviewer不同角色。shared-file-owners.json保全部表。

修订分母是这次明确23必修及必要相关回归，不能借update重新无界全仓review，也不削弱质量门槛。按精确SHA/path/blob/条款/前提/已核结果有限复用历史，不反复重读所有raw/ACT附件；只在相关字节/前提改变或新反例影响范围时定点重验。不递归加审核门。原229/341接受只其原scope，任何未来改变的字节需自己的作者/独立/整合/登记证据。

## 7. 文件导航、完整性与发布

所有下列资料位于固定A=f5174841d7ec4e8c4a6565392bd22daffa22ed99/tree=275c99dae845c23ced0c43639dc6b28f01d27f0f 的 `review/global-independent-review/third-2026-10-12-86b4d7e-manual-a731/`，文件名下路径可直接拼第2节raw前缀或Git fetch该固定SHA后读取。每条 bytes/SHA256 是实际远端200 body readback值，来源为本轮独立review、精确旧scope复用或明确静态停止证据；Python文件仅分析/完整性/发布辅助，无框架实现。manifest自身SHA在下面单独给首冻结snapshot值，未让manifest嵌入自身；完整199附件清单＋其自身可从固定manifest读取，以下列全部附件，非让接手者自行寻找。

| 本轮根相对路径 | bytes | SHA256 | 用途/来源层级 |
| --- | ---: | --- | --- |
| M01/assigned-files.json | 55399 | 29008102b073d3b43fefda2765b73456ecaa888f1b00db50ba3ce8f917ec353f | 身份已核导航/完整旧控制；不是当前通过结论 |
| M01/assigned-junctions.tsv | 8765 | 154d69b0d85e9cb6a875193e518ee840ccb729f14ca54a864d0945020a29f63c | 身份已核导航/完整旧控制；不是当前通过结论 |
| M01/assigned-specs.json | 1774 | cc95ae16a11c96a12100900a2fbba82ff93d4338feafc2b5351b9092a71c85c3 | 身份已核导航/完整旧控制；不是当前通过结论 |
| M01/capability-coverage.tsv | 25555 | 74d601209d80e0262ffd3be259c5d12731e7f6124610091f313e77aa33686026 | 实质报告/完整发现/覆盖/归属/限定证据 |
| M01/coverage-counts.json | 346 | 3386584af8fefbadd10530dc9253ede3675342715610b4427e796c867107592d | 实质报告/完整发现/覆盖/归属/限定证据 |
| M01/file-coverage.tsv | 60350 | 2a47272254567e57bf65d23409a15f0187a838e9eefb43ec36d0b894ea228647 | 实质报告/完整发现/覆盖/归属/限定证据 |
| M01/findings.json | 23541 | b45f534f6defb704c2619abd03af2c778bf5caf49eec55f18580b0fb1aeb4934 | 实质报告/完整发现/覆盖/归属/限定证据 |
| M01/identity-check.json | 2777 | cf965b6e023d5f2e6ef8ac1cfa6041ec28d493955eb938401006299d426a9061 | 实质报告/完整发现/覆盖/归属/限定证据 |
| M01/junction-review.md | 5516 | 8c03313561ca5f62d14054d785e678e96eb9c968715be9ea4be6c9531c396dd0 | 实质报告/完整发现/覆盖/归属/限定证据 |
| M01/regression-controls.json | 277160 | 7acd72edc650388cc4bcaea6836fac59abc1f594590386f660d28b182ebe7e5e | 身份已核导航/完整旧控制；不是当前通过结论 |
| M01/regression-review.json | 80680 | 7e7f3a0b1f5a51dc437d37a0bc8a5d0d0b16ab76ec2879dccc80c410e68573eb | 实质报告/完整发现/覆盖/归属/限定证据 |
| M01/report.md | 7229 | 258167a73511f77668ffc81c5eba0c0d5e2a1f7d7e9a025eb4dd8aae84ce9149 | 实质报告/完整发现/覆盖/归属/限定证据 |
| M01/spec-coverage.tsv | 296357 | 39df5dc4ff29c37248f9ad4497f7b892a86f982a2f979c5a684694458804af95 | 实质报告/完整发现/覆盖/归属/限定证据 |
| M01/spec-identities.json | 2237 | a8f2d17a73b3f9d9a923038cccfbee41e92465c1a4c4e8472ec732a08217935c | 实质报告/完整发现/覆盖/归属/限定证据 |
| M02/assigned-files.json | 11067 | f655806cbc595a5c788dd8f44196c8aae82efdffa3fc66a9080f321a3c10831a | 身份已核导航/完整旧控制；不是当前通过结论 |
| M02/assigned-junctions.tsv | 14189 | f45e3598da2956c8b52d5cfc1d6e82755126700fff853d87b0e5887febc605bf | 身份已核导航/完整旧控制；不是当前通过结论 |
| M02/assigned-specs.json | 2845 | 407501a5cf1007ad89d80e4e5b858f862b830d781bd54f5ac01c63f484016f98 | 身份已核导航/完整旧控制；不是当前通过结论 |
| M02/build-review-artifacts.py | 32349 | c6ba36cd04cf6e63555418db24c708b3dcaadf5b73e6fd808d866e6d490751d2 | 本轮数据/产物/发布辅助；不执行参考行为 |
| M02/capability-coverage.tsv | 24080 | b1918fede5b8f9bd4a5a4031cb624f440a454acb02eec5ac9a7896e715d60285 | 实质报告/完整发现/覆盖/归属/限定证据 |
| M02/file-coverage.tsv | 9911 | b4efff05b5268dd22d113705fd412da6844926bca3743cf2422398f30d993820 | 实质报告/完整发现/覆盖/归属/限定证据 |
| M02/findings.json | 13482 | f6f19f7bfcc445daa35c30236ea4cd4c2c85aab1b357ecbe4402f75452d34f04 | 实质报告/完整发现/覆盖/归属/限定证据 |
| M02/junction-review.md | 2218 | 3d3f8721d0a0725e461d6c949e6fa23bbdb30d8f349fb35990ebac3922b23715 | 实质报告/完整发现/覆盖/归属/限定证据 |
| M02/regression-controls.json | 490447 | 04be06a4496c7815a20c87404d2877258aa7e9b8ba1d6254fd667da670c402ae | 身份已核导航/完整旧控制；不是当前通过结论 |
| M02/regression-review.json | 30156 | 7f8178e84625e5c35042b91c6f2c3d8e7442120d18201195b8216aed7a26f201 | 实质报告/完整发现/覆盖/归属/限定证据 |
| M02/report.md | 2073 | e2157d6d50a65e7374df2e2671ff7a4e244f3128aef635917e8897c214b9f624 | 实质报告/完整发现/覆盖/归属/限定证据 |
| M02/spec-coverage.tsv | 422635 | 0a8e215724a0445c0fba1edf4ab764b4eecf3f2cba56363b20b9dc5390e6df17 | 实质报告/完整发现/覆盖/归属/限定证据 |
| M03/assigned-files.json | 16853 | 14a2f96fb001f7361dc7bdb3307f9eba105dcd079fce97aea3caab58de9a09c6 | 身份已核导航/完整旧控制；不是当前通过结论 |
| M03/assigned-junctions.tsv | 10685 | 96d556c18554d04d613a9f98522c19e7101cd062441bdc45ba22e4be550815fa | 身份已核导航/完整旧控制；不是当前通过结论 |
| M03/assigned-specs.json | 3935 | 5c91792cc5c3c82511c9fdb61aa4632cc928e6c7967e11c5a2d73e389c123062 | 身份已核导航/完整旧控制；不是当前通过结论 |
| M03/capability-coverage.tsv | 39928 | e6fe0e21e35759e182da545dd97db8e55412c110ef19cb8c4615a5248f3639e7 | 实质报告/完整发现/覆盖/归属/限定证据 |
| M03/file-coverage.tsv | 26933 | c7a81103240abe5118926cd220f9d0410333cdd2ea324a93e346756e9d67b391 | 实质报告/完整发现/覆盖/归属/限定证据 |
| M03/findings.json | 27548 | 5c6906d499cb1bf02aa7f4959bce1b9902c28dddeb48df34cb4bf07f76b159b8 | 实质报告/完整发现/覆盖/归属/限定证据 |
| M03/junction-review.md | 9772 | aad4ec30d9002e607faad03c5512202548972ee25c28c9b2a7632d22bcdb6383 | 实质报告/完整发现/覆盖/归属/限定证据 |
| M03/regression-controls.json | 1478012 | 12f65637091d6f884fde44bb1b5c69135749705a9b1e8e441066468c09ab0ab9 | 身份已核导航/完整旧控制；不是当前通过结论 |
| M03/regression-review.json | 252245 | 1b191978154f9e9ee66d2a99ce643bcf17a0e5727fb026390553d83358d199de | 实质报告/完整发现/覆盖/归属/限定证据 |
| M03/report.md | 7188 | 6ad7af819898ae61775320c1e753744146ed8097dff99695d3f4c0607b35de82 | 实质报告/完整发现/覆盖/归属/限定证据 |
| M03/spec-coverage.tsv | 1722984 | 7d1c07bb3ac861e493ead8805aba466413fb4a7c9ef69da31b5cedad6c54742f | 实质报告/完整发现/覆盖/归属/限定证据 |
| M04/assigned-files.json | 3831 | eca8ac56344aa8fc8dd3bf301f1c03f431b2422660c9a5ac3d17acac8f290130 | 身份已核导航/完整旧控制；不是当前通过结论 |
| M04/assigned-junctions.tsv | 15228 | 14e1130ad3072ec67fb4d45b5fe3e5b9b8ae2e189e848e5459d1941ece2905b6 | 身份已核导航/完整旧控制；不是当前通过结论 |
| M04/assigned-specs.json | 3575 | 6fb607252067e04b0af9283e483c6ce167f406e6caba2fa01b51ebe1600df638 | 身份已核导航/完整旧控制；不是当前通过结论 |
| M04/build-review-artifacts.py | 26852 | 9b859c6d4444f23475e3e90ca62de77cbe8ae0800995d6c056305358705dbff5 | 本轮数据/产物/发布辅助；不执行参考行为 |
| M04/capability-coverage.tsv | 24684 | 00a72b2625e42ff5f5cb5aa038b571adffca61912ed7c38b837282f1aac8d3c0 | 实质报告/完整发现/覆盖/归属/限定证据 |
| M04/data-audit.py | 4542 | 5c3ec886829ed35794f74d711b006096e72c89f96cca59976e6c5f7170874e5b | 本轮数据/产物/发布辅助；不执行参考行为 |
| M04/data-field-equivalence.json | 36308 | 2aea62cf019d6b78a88e147735ffc7a91ab74cc32a484f82b652be0270ac1987 | 实质报告/完整发现/覆盖/归属/限定证据 |
| M04/file-coverage.tsv | 9004 | 44ad2751db5ff3f1882ee61340d6d559e41c73092ee1faf4eddad002d8f3d713 | 实质报告/完整发现/覆盖/归属/限定证据 |
| M04/findings.json | 5945 | b0491dec374012afcaefc7173e82302ff354c6900efe62bdea865892bec8f416 | 实质报告/完整发现/覆盖/归属/限定证据 |
| M04/junction-review.md | 2401 | 554c3f72af034fc319194cc8da20ce9ce4c9bddd480706ce426ea3bac57caf12 | 实质报告/完整发现/覆盖/归属/限定证据 |
| M04/regression-controls.json | 552521 | 8e5ff449ec7aaa050498a1df909f3ca079010d1cb607b9dc4fa5576f4e60c29c | 身份已核导航/完整旧控制；不是当前通过结论 |
| M04/regression-review.json | 50659 | 102674c6c414c6c7fce0d32ebf57603c4607417a02abff45346736033528fcc3 | 实质报告/完整发现/覆盖/归属/限定证据 |
| M04/report.md | 2245 | c1a12da4e79b2f1c49ae9e0231bf29cd9cee429e5edb84c219d38f40f3edeecd | 实质报告/完整发现/覆盖/归属/限定证据 |
| M04/reuse-qualification-corrections.json | 1122 | 81c940cccd070ad149a4bd0f197e0284929d56a39de7c8888cd5220ea7ff148a | 实质报告/完整发现/覆盖/归属/限定证据 |
| M04/spec-coverage.tsv | 1162931 | a313290ca445607a5a6a1e3c5fd393c8fdf042ed8c7277862f0295d5a459f2a3 | 实质报告/完整发现/覆盖/归属/限定证据 |
| M05/assigned-files.json | 4203 | c928355d24e63c4279965cc98dc51277515839572793c49b050c9aed2bf4d0b0 | 身份已核导航/完整旧控制；不是当前通过结论 |
| M05/assigned-junctions.tsv | 24284 | ef945260050004ab46bc448c601f359fcc458a8416a68d6100b5cb05ffcf88ea | 身份已核导航/完整旧控制；不是当前通过结论 |
| M05/assigned-specs.json | 2479 | 68da448dfda35e2ba8c7db190b2e463fbadec741c1a7b842d5b90551faec3363 | 身份已核导航/完整旧控制；不是当前通过结论 |
| M05/build-review-artifacts.py | 32134 | c2157c1a2ca24bdd97e1cfc38ed2b110866cca037d1b1a4b55bfeddbf6e40caf | 本轮数据/产物/发布辅助；不执行参考行为 |
| M05/capability-coverage.tsv | 26118 | e3b8580398267a7a99864ae446f5988037132ba23ceaeefc7ca7785ba667bf47 | 实质报告/完整发现/覆盖/归属/限定证据 |
| M05/file-coverage.tsv | 5416 | cdb007aa3951b3dfd0eae1af18892003576abf8a183a8d6c1388310a42bf3bac | 实质报告/完整发现/覆盖/归属/限定证据 |
| M05/findings.json | 9555 | 9b10acb8878faeb532ce1a3789979a8dfcdec6b16d6bcdb28527686000a0085a | 实质报告/完整发现/覆盖/归属/限定证据 |
| M05/junction-review.md | 26488 | 6aa2ea2a1f06757bff23fb46f4642534d5fadacf9ec6ee67d379edd5f20883b6 | 实质报告/完整发现/覆盖/归属/限定证据 |
| M05/regression-controls.json | 807306 | cd9b139b89badf30c94e8c96292b21d0184b56708ba0e2b1a44772bb28e9e015 | 身份已核导航/完整旧控制；不是当前通过结论 |
| M05/regression-review.json | 54212 | 3903d8605ceb7c0f31a63ba27c5574037b86c40fbc5fb08d3b3f6eae6b6e87f4 | 实质报告/完整发现/覆盖/归属/限定证据 |
| M05/report.md | 2461 | 2c650281b0ad048157776ead0a1fdda63ec1ccecfad0036838ca9bf012e6df73 | 实质报告/完整发现/覆盖/归属/限定证据 |
| M05/reuse-qualification-corrections.json | 512 | d0f65b68c10858f2c6b66111dd77402ecf7ef04f7994d01b9224bae514d177dd | 实质报告/完整发现/覆盖/归属/限定证据 |
| M05/spec-coverage.tsv | 1066431 | d6e7686ca436432f45e53f1a5ea17437a7459cb1479c848d55e5e7d8c20a5fb0 | 实质报告/完整发现/覆盖/归属/限定证据 |
| M06/assigned-files.json | 3088 | 0a34cf47c916e4f47e55e886fbab383261c91bca252cb8c8b3660999ff00a3c7 | 身份已核导航/完整旧控制；不是当前通过结论 |
| M06/assigned-junctions.tsv | 30703 | 769e45812604bb40f5f0cd9c852a0a3688181c3d8652e6be2feb2ef3b0612859 | 身份已核导航/完整旧控制；不是当前通过结论 |
| M06/assigned-specs.json | 4283 | 02e5c03e8324236802e9fc20276f50d91a21af9d60bacd17f1a096fef874b3b8 | 身份已核导航/完整旧控制；不是当前通过结论 |
| M06/capability-coverage.tsv | 43675 | e54d4420c1bd841d40d3bfe3e7016abf1448febc12b35b0dc2afc2648d9dd92b | 实质报告/完整发现/覆盖/归属/限定证据 |
| M06/file-coverage.tsv | 28152 | 5bec254bfdda4e91c5ec09afbc5e48d3cb7700b0633cab5a704c3ac2e72aeed4 | 实质报告/完整发现/覆盖/归属/限定证据 |
| M06/findings.json | 3917 | 4eabdd6c7fc57dc2ff9c9bbc60f0eee3766f1bcdf8126fb802b435615e85c9a4 | 实质报告/完整发现/覆盖/归属/限定证据 |
| M06/junction-review.md | 5345 | 4c2dff598eb15e3f2dfafe125e039d747f1c49fb1069c76ead6596c71ea7e03d | 实质报告/完整发现/覆盖/归属/限定证据 |
| M06/regression-controls.json | 1114090 | 30ba94b9e7307cae61c6d417cc9dd02f19267b4933a2566b99a11a436dc01853 | 身份已核导航/完整旧控制；不是当前通过结论 |
| M06/regression-review.json | 988097 | a256c378e5a06b7e9779b13299fbda83b4ae175d673081df6688d7386eddda98 | 实质报告/完整发现/覆盖/归属/限定证据 |
| M06/report.md | 4536 | fbc4fa4d60612a462cfdbb4f08cdcb60e243036f3ccafe94025f1ffb97d376fc | 实质报告/完整发现/覆盖/归属/限定证据 |
| M06/spec-coverage.tsv | 2678254 | 5fc75d43851d77e01ec48bde06c8228d12fd859fec86a159a044b7aa1dce7894 | 实质报告/完整发现/覆盖/归属/限定证据 |
| M07/assigned-files.json | 13452 | f8502f288dab07b5590e992a62507887904e51c024bdab084ec81042ce16166e | 身份已核导航/完整旧控制；不是当前通过结论 |
| M07/assigned-junctions.tsv | 16715 | deee74b88df63cf00e7180960f7710218eaca447f30072f83f88143ddc67d3fc | 身份已核导航/完整旧控制；不是当前通过结论 |
| M07/assigned-specs.json | 3660 | 2be6044de9440abce38b79e1a659c08f275b2780adaeb53e72b9db66dafeb239 | 身份已核导航/完整旧控制；不是当前通过结论 |
| M07/capability-coverage.tsv | 53833 | 9809d2457d3e2e908e8a97d9350f6e3e9f4e7e854d203bef355d7a333cc334a0 | 实质报告/完整发现/覆盖/归属/限定证据 |
| M07/file-coverage.tsv | 21685 | 648e320a1d19878ff123e7bad493b964141e18734eb0503cfcdb96fd2c703adb | 实质报告/完整发现/覆盖/归属/限定证据 |
| M07/findings.json | 12829 | 98c1e523156571d26cfc22bd0a50a87016f29ffc016cb4f84a96f72152dade81 | 实质报告/完整发现/覆盖/归属/限定证据 |
| M07/input-identities.json | 11997 | ed6a8275bb306ca5de5e84e24db930926ef5eed7dfe72f40ae32436b1391c940 | 实质报告/完整发现/覆盖/归属/限定证据 |
| M07/junction-review.md | 9456 | ced5dc2432a50acc27810d1ef34d58adfe3cb61787cc38453cae4337b62ed614 | 实质报告/完整发现/覆盖/归属/限定证据 |
| M07/regression-controls.json | 824429 | 251d9c05aa660150c9152b23b20f79f92028f36f8c211a43643eb95363856034 | 身份已核导航/完整旧控制；不是当前通过结论 |
| M07/regression-review.json | 129063 | 6f4d62a13ec570e15563cca555bbf85f41a1b175361e66682241c81a2b0271f0 | 实质报告/完整发现/覆盖/归属/限定证据 |
| M07/report.md | 8310 | 9416a5f0de0487310e9d7e9ecd7f59ea1b9df1e8c27e2f51db7d4214f007ef42 | 实质报告/完整发现/覆盖/归属/限定证据 |
| M07/spec-coverage.tsv | 710454 | 230fa2d33a6f9c057b3cba1e19008e88cd93c08fa71b3ac59a51ae23fa8c02f7 | 实质报告/完整发现/覆盖/归属/限定证据 |
| M08/assigned-files.json | 4791 | 55d00d844c3682e2d782823600e320a779e8d5c1b796cb8ede3bde779063578d | 身份已核导航/完整旧控制；不是当前通过结论 |
| M08/assigned-junctions.tsv | 3910 | 09ca78180d5abb86f698316ccfa536c046000b62e5d268ac07f20862e40d4e5a | 身份已核导航/完整旧控制；不是当前通过结论 |
| M08/assigned-specs.json | 4360 | 5a06faead1d759921a78b3b98274ae15358b84e4a9045cc6d3baa7259afeebb7 | 身份已核导航/完整旧控制；不是当前通过结论 |
| M08/capability-coverage.tsv | 83721 | b0e4fec76d02f3401c12f8ea58683bf9e54457a2a8e927b73bf01849d0cd08d4 | 实质报告/完整发现/覆盖/归属/限定证据 |
| M08/file-coverage.tsv | 15541 | 6ab2f1ce98fa360a2e71041a531451e68b0face56f46bc07b6d548be694c9f85 | 实质报告/完整发现/覆盖/归属/限定证据 |
| M08/findings.json | 11427 | 3e6733f626f6ce85998f77cd5e325d20964fb7f205e1f65784700be0d78802f1 | 实质报告/完整发现/覆盖/归属/限定证据 |
| M08/junction-review.md | 8141 | 054ccaf13c5ab4aaedff9b7483ac2376365287356259fe76ca3dc28cdadf8617 | 实质报告/完整发现/覆盖/归属/限定证据 |
| M08/regression-controls.json | 580074 | c36fd0fde800dd3f04e870689f73ea747f14d73ea5b2134ab01059d619c0da1e | 身份已核导航/完整旧控制；不是当前通过结论 |
| M08/regression-review.json | 209738 | 0bc0793fadd479eb9cc32ace337ad59fdcb519b6351ee4c3dd83f92cb0ca3a25 | 实质报告/完整发现/覆盖/归属/限定证据 |
| M08/report.md | 7182 | a16769468246e32c99f098497244516c1d1df768993536edb719b2b65dc28952 | 实质报告/完整发现/覆盖/归属/限定证据 |
| M08/spec-coverage.tsv | 1630674 | 006332da569a3eae469b578ce3668d77ae5790dd9eacf709b2f8840d23694cde | 实质报告/完整发现/覆盖/归属/限定证据 |
| M09/assigned-files.json | 15024 | 43873a6eaeb3930b43ccda5cadedc4eff4fd15fdad129d3c50dfa2fb24a39263 | 身份已核导航/完整旧控制；不是当前通过结论 |
| M09/assigned-junctions.tsv | 14012 | 9ff63df9283d79f2d9d00504d97c7aa1baf5f686205762c4becc7b6642c76628 | 身份已核导航/完整旧控制；不是当前通过结论 |
| M09/assigned-specs.json | 5517 | 2361c8212fb71e7ce8ba37760af164358f73006512ce8d5c5111f895cdc86149 | 身份已核导航/完整旧控制；不是当前通过结论 |
| M09/build-review-artifacts.py | 60262 | 562f77fba2ca4acacd844aad5f4355a655c01fd27f08ad3026bf08a130c1db6a | 本轮数据/产物/发布辅助；不执行参考行为 |
| M09/capability-coverage.tsv | 63707 | 00868b01e9acfca276c7f2960e6093027239fd47c089b415d5795c1ec675ce07 | 实质报告/完整发现/覆盖/归属/限定证据 |
| M09/coverage-counts.json | 349 | e728590e7a1eebb2bb4c6512fd80805ea2753bc0802d7f343f42b7e8f26ee449 | 实质报告/完整发现/覆盖/归属/限定证据 |
| M09/file-coverage.tsv | 25924 | a0d881d05921bc9236e2c1040dc0facd9fccc99cb1bfa555c238c9cf9fb978e1 | 实质报告/完整发现/覆盖/归属/限定证据 |
| M09/findings.json | 4887 | a53653ce1d15896f300cffa19a17d8901ba5053ecf2bc984684a1fb484fd1ae9 | 实质报告/完整发现/覆盖/归属/限定证据 |
| M09/input-identities.json | 14240 | 9ef949d82e03e1806a6868aad1f7b28101365c07275ec2793a5d5b89cbd970c1 | 实质报告/完整发现/覆盖/归属/限定证据 |
| M09/junction-review.md | 9524 | ec5912eefb0f26e6ae28618ad673a3e8c15f522d6afdde572757ebc429f4dc02 | 实质报告/完整发现/覆盖/归属/限定证据 |
| M09/regression-controls.json | 601150 | 0873d84bdc4330b09c247e415cf05dcea7a2e4150e6552641d97d6853f30c027 | 身份已核导航/完整旧控制；不是当前通过结论 |
| M09/regression-review.json | 113808 | 5ce5ec9e06a0d9fb9b6b692578a53f1fc1fbbd78d98209bf3cd53b707d4f0fe9 | 实质报告/完整发现/覆盖/归属/限定证据 |
| M09/report.md | 8552 | 776e707f8e16d65af239e46555429e9826db8818292e50c65cc31dae6f8b6f74 | 实质报告/完整发现/覆盖/归属/限定证据 |
| M09/spec-coverage.tsv | 1106063 | cd4886e4a75d782e61a8cdf2889cac51a0ae1c25cdbd2d0c32c1b1f7d8efee56 | 实质报告/完整发现/覆盖/归属/限定证据 |
| M10/assigned-files.json | 21074 | 89924a6e92a74367bc8b38af0b425f91ef642bb07bcf75d80e6b11b9167affdb | 身份已核导航/完整旧控制；不是当前通过结论 |
| M10/assigned-junctions.tsv | 24435 | 60962cdcf1a0ae89774d2c681a4b1307d7b98bda93f900bcdc9fd4b2498b76cd | 身份已核导航/完整旧控制；不是当前通过结论 |
| M10/assigned-specs.json | 3960 | b50d2c42004d9b70e80bd1f25e6c98f43f58c7622100dc7b96755a8ae6beceb5 | 身份已核导航/完整旧控制；不是当前通过结论 |
| M10/capability-coverage.tsv | 29509 | 54ee916637faee89794fd64c19ce61933c5e13ec656324334440311d4501874a | 实质报告/完整发现/覆盖/归属/限定证据 |
| M10/file-coverage.tsv | 32332 | 7809b1fd7e55e919a3258ae7c6b02804e671acb494a9510d7c703b7f7f911a0b | 实质报告/完整发现/覆盖/归属/限定证据 |
| M10/findings.json | 21292 | bba6c1c8508a7ea42d129cc5b872c908f2086437c81e727c293b61e0d5f449bf | 实质报告/完整发现/覆盖/归属/限定证据 |
| M10/junction-review.md | 19087 | 27b23253c8d716afb7d2a4bb752e2854235113c179d2a41a597ae2072aa8ed0c | 实质报告/完整发现/覆盖/归属/限定证据 |
| M10/regression-controls.json | 1402478 | 28ccdd9bfffddcb9305c45226bfd413c44e9afe749e53e8f14003ca4aaefb05a | 身份已核导航/完整旧控制；不是当前通过结论 |
| M10/regression-review.json | 264981 | dc989194bc3f73a73aa35e347c6e5c00b346e03490ae8bba1d7a96fc1ba0564e | 实质报告/完整发现/覆盖/归属/限定证据 |
| M10/report.md | 4160 | d7f01e6ca567ca6dd502d846663e2c93db953ec01058e352631d160cea410a3e | 实质报告/完整发现/覆盖/归属/限定证据 |
| M10/spec-coverage.tsv | 807779 | e08ac00a3798c3227471d6509a639d109ace3384f395fe9d8a6ce8ddcd11344c | 实质报告/完整发现/覆盖/归属/限定证据 |
| M11/assigned-files.json | 9674 | 28dd171b549ee810c5b5732c7545a2e73a2048b1575bbd53c8c6f7c4a87aa690 | 身份已核导航/完整旧控制；不是当前通过结论 |
| M11/assigned-junctions.tsv | 31910 | 25a41bdf93774dc058eac127da464ae6b70e554c560864db8ad9106a1b74efc2 | 身份已核导航/完整旧控制；不是当前通过结论 |
| M11/assigned-specs.json | 6642 | 9fdf0c4a2d2d7cf4328600c7345c23602375f6447019c1d14dd1cc50166c6c6d | 身份已核导航/完整旧控制；不是当前通过结论 |
| M11/capability-coverage.tsv | 42178 | 97d5819364093df7d6740f0e960b96ce50e1fcf429e8dc5ae28e413f80df4e13 | 实质报告/完整发现/覆盖/归属/限定证据 |
| M11/file-coverage.tsv | 19045 | 3b30c99047480a8215bd74f6ddf6ee7d19d1a7dbe80e2350969e81f989f7412d | 实质报告/完整发现/覆盖/归属/限定证据 |
| M11/findings.json | 8236 | a74dde9e2c049083097f222dda5e7c5a6a5559cfef4d12d976c03a3b7e081299 | 实质报告/完整发现/覆盖/归属/限定证据 |
| M11/junction-review.md | 48585 | 1dc49175046101549caeb349f5dc74255b68e83e43c85873115aa2c59aa39f06 | 实质报告/完整发现/覆盖/归属/限定证据 |
| M11/regression-controls.json | 1452142 | 25d54589a2b047118a9fc38a179a576e11b75d2215844488c903fe2b2322e73d | 身份已核导航/完整旧控制；不是当前通过结论 |
| M11/regression-review.json | 344935 | 428f7ab095072edb3ff90809f7b4ab56ad8bd0c5d34619c8e8d16335dd021bcc | 实质报告/完整发现/覆盖/归属/限定证据 |
| M11/report.md | 5959 | 6cbee3909c4d569619b437a8bd7796ba8052ab2735322a1b9085f0cc0d986340 | 实质报告/完整发现/覆盖/归属/限定证据 |
| M11/spec-coverage.tsv | 713356 | 0f6cc898665085b2bce0746e3fd3d552f1191df35c79c2e3ed0aa2852a518ed6 | 实质报告/完整发现/覆盖/归属/限定证据 |
| M12/assigned-files.json | 22737 | c4ce0cb9df576b9369474255fe249da63fc2552b8a25a90687013a58e24249aa | 身份已核导航/完整旧控制；不是当前通过结论 |
| M12/assigned-junctions.tsv | 14689 | 23c9ca703e29b02e9baac159423f08923fb013eda883003a7e3e86064c6febf9 | 身份已核导航/完整旧控制；不是当前通过结论 |
| M12/assigned-specs.json | 2854 | 05096ce5e1aa9b3c06c8dac352f88fdb324bf82c1b65295985425ec82440e9aa | 身份已核导航/完整旧控制；不是当前通过结论 |
| M12/capability-coverage.tsv | 75235 | 30ddf695374324ce605cda73478d6caaae25c834cbe52119f5a4b52fdb36713c | 实质报告/完整发现/覆盖/归属/限定证据 |
| M12/file-coverage.tsv | 25413 | d2cd8801b7fba5b7b57b7e0f608b433adcc8c79bf39f16cf5257470a040287ac | 实质报告/完整发现/覆盖/归属/限定证据 |
| M12/findings.json | 8847 | e8d706b61e959203511b4e5af2e06dffdcdd07be2a98bd758b88d13cc40166cc | 实质报告/完整发现/覆盖/归属/限定证据 |
| M12/junction-review.md | 11535 | 91bfd2111bd5bb434a0a420f1466483f18adf21bd1dc0536ee8487d41fdf98e2 | 实质报告/完整发现/覆盖/归属/限定证据 |
| M12/regression-controls.json | 1267088 | e33247c55cba835a80ef1a7910ad27ff1f140f0e81eadea87d40cbf0313a6590 | 身份已核导航/完整旧控制；不是当前通过结论 |
| M12/regression-review.json | 228813 | 591a08c277fc378982165470d87914c64dfbc0ce8ed18d21afa47e9c2fde3f2a | 实质报告/完整发现/覆盖/归属/限定证据 |
| M12/report.md | 7936 | 83a12b10644ce3304218468ade2735d6ca33dbd833108e952873c38426456746 | 实质报告/完整发现/覆盖/归属/限定证据 |
| M12/root-preliminary-tools-review.md | 2000 | 0c8bf2dd71223d5a5610915e9d46a97b10bc11aba8e96b4ec7f0dbe1a2317f06 | 实质报告/完整发现/覆盖/归属/限定证据 |
| M12/spec-coverage.tsv | 878324 | 76093f43a7664faca29a1c1f47ed321c9651944e14df7e879ab84ccfeb40ddcc | 实质报告/完整发现/覆盖/归属/限定证据 |
| accepted-341-scope.json | 691320 | 37949af51030566fd95378ee392ddc7baf5e91feed18bbecb8ed55a69fed14e1 | 实质报告/完整发现/覆盖/归属/限定证据 |
| adjudications.json | 12988 | 611cf91e824762fa91bd28de32fe14dbc130b85d4ce583147eaff1ff0aa32ee1 | 实质报告/完整发现/覆盖/归属/限定证据 |
| assemble-global-review.py | 9144 | dd4c513b61f7126b7437007a79e7d0e73f79b05759fb42105177e955bbd5db44 | 本轮数据/产物/发布辅助；不执行参考行为 |
| baseline.json | 24170 | 1e025313d883160d708ea0f996b48672fa47dd5044f2190b97fdfa63784ced2f | 实质报告/完整发现/覆盖/归属/限定证据 |
| build-handoff-manifest.py | 13933 | 6d11868ef1775e634ea5f16606520c514c91a807e7ed9333964b34bd3cc2abfc | 本轮数据/产物/发布辅助；不执行参考行为 |
| capability-coverage.tsv | 565639 | dc9489d2401f050663692d7afd37d139e0eb77c56f6ad38edebd2f4425c4e50b | 实质报告/完整发现/覆盖/归属/限定证据 |
| cloud-third-update-handoff-manifest.json | 6246281 | 474cba2d12f2af1bff2e86ced2f6add9b3fb3fecfe92cf1805821fb13e669f27 | 实质报告/完整发现/覆盖/归属/限定证据 |
| coverage-summary.json | 5756 | 38fe04462fb55411cf670255eb421245a7991754ad1279060d6596600ad908e6 | 实质报告/完整发现/覆盖/归属/限定证据 |
| dedup-aliases.json | 2016 | d99d9872037cc2a299857cd3a0143f2380c01fc29eb2c100b27e9b399cc26a5d | 实质报告/完整发现/覆盖/归属/限定证据 |
| delivery-scope-audit/limits-audit.json | 3035408 | 6fd0b59515b3c44cd3e399e9909cb90763e98e579f8faf94979ec2b5542038d8 | 实质报告/完整发现/覆盖/归属/限定证据 |
| delivery-scope-audit/scope-audit.md | 12231 | 3b7c6d74c61c8bcf6440a8495c2a803b922deb701a9afeecde1c59b91a75bb23 | 实质报告/完整发现/覆盖/归属/限定证据 |
| execution-records.json | 2720 | 11c396d536fa365eb480297b60d57be6407ccd0dd80d66dc6c8c96ed11d2d116 | 实质报告/完整发现/覆盖/归属/限定证据 |
| file-read-observations.tsv | 301804 | 1640af78e05e065e5dc0f93d5b5e095d0e231e187c7c8a24f0263b5a9312afdc | 实质报告/完整发现/覆盖/归属/限定证据 |
| final-report.md | 10465 | 7cbed26274aa4bcdc33ce4ff794457218fdd7b392b677b15a6e0bd50f212e8ba | 实质报告/完整发现/覆盖/归属/限定证据 |
| finalize-global-review.py | 17346 | 09fe5c9b2c16261394bea5dbf7a60c5c06269cd3258d2ed2ed58f98ce887e2da | 本轮数据/产物/发布辅助；不执行参考行为 |
| findings.json | 165385 | 6d5695d3039b3d8d91cd267d70dae8bb1ba958e3ff07ca266b7d7a39c756c262 | 实质报告/完整发现/覆盖/归属/限定证据 |
| formal-spec-identities.json | 43031 | 63c384def9b109bf73d1ff8dd3fabd5cbc18a096318be8cf4f0e559e110ed8e1 | 实质报告/完整发现/覆盖/归属/限定证据 |
| formal131-reverse-index.tsv | 57313 | 1332690f07928496449d50b06b3dd1fbc9bca32d92193ed28baca40c7cce00d7 | 实质报告/完整发现/覆盖/归属/限定证据 |
| integration-history-coverage/m09-integration-20261012-a731/accepted-341-joins.json | 10145358 | a7dc820d628ded7407682b6a9495d3c829c456eb0077bc569b54ea8e1f6e06e3 | 实质报告/完整发现/覆盖/归属/限定证据 |
| integration-history-coverage/m09-integration-20261012-a731/build-integration.py | 56089 | 65f9b602b9e9dd1518a5633dd3c9f259815707dece2443df288abeb05e8c04b5 | 本轮数据/产物/发布辅助；不执行参考行为 |
| integration-history-coverage/m09-integration-20261012-a731/coverage-gaps.json | 18799629 | 195a4ffa02a75af1cd748cfa6e6b3b151dcb55cf1a298b8982d86c7202400cc6 | 实质报告/完整发现/覆盖/归属/限定证据 |
| integration-history-coverage/m09-integration-20261012-a731/integration-report.md | 9167 | e22de22e40f1f59618e5c5c2df4bfccdc554461d247c98c9be285a9aa8df5f8a | 实质报告/完整发现/覆盖/归属/限定证据 |
| integration-history-coverage/m09-integration-20261012-a731/junction-54-and-chains-8.json | 6280380 | 0cba2c892e11ebe3831a27327627cd6d6751fbe313fa4c7180062b0026c09ed3 | 实质报告/完整发现/覆盖/归属/限定证据 |
| integration-history-coverage/m09-integration-20261012-a731/regression-229-joins.json | 7348397 | a613eecd341b5ae817aa3ea1fa4b910893a44a6480da3d4d107c54719ab41c2d | 实质报告/完整发现/覆盖/归属/限定证据 |
| integration-history-coverage/m09-integration-20261012-a731/serialization-checks.json | 741 | 9d03a7f386e479a97dcf2d64fd18c209b979012b5f0640f9a4d3af6a405a8878 | 实质报告/完整发现/覆盖/归属/限定证据 |
| integration-results.json | 3188 | 37d798b122970139d60680637626d7fc264fbe5d720ec60a56755f0cc9e5763a | 实质报告/完整发现/覆盖/归属/限定证据 |
| junction-results.json | 6334335 | 4416eb76a513e42ea9be6857b4373b7ecb14bda7eb7d5ad32202dde0ec299e3e | 实质报告/完整发现/覆盖/归属/限定证据 |
| junction-review.md | 27234 | 0841310c4aa433949792805b3bf037278783ed0786d2f504ce51366f7d397677 | 实质报告/完整发现/覆盖/归属/限定证据 |
| legacy-stop-evidence/STOPPED.md | 1330 | 5a13a9d8758208a006aeb037c65dcd0ba73f3ecbe5a11e4b08b8e2e442a081a8 | 原停止回执精确静态副本；不采候选PASS |
| legacy-stop-evidence/copy-provenance.json | 1508 | 4fd07ea7821ce58fdebf629615c47fbbe32898c3d66314558d8816a9cfb730cc | 原停止回执精确静态副本；不采候选PASS |
| legacy-stop-evidence/stop-receipt.json | 5043 | c2d99ad65598b7b6987b1632a1ee9cb721a5e2c931e014d4949cfd3c04b4bf01 | 原停止回执精确静态副本；不采候选PASS |
| limits-and-missing-materials.md | 4444 | e880c242bfc8077e6c9b4348ea488041516ea689ceb71d424bbfc22eee363d11 | 实质报告/完整发现/覆盖/归属/限定证据 |
| module-results.json | 20272 | 21b17bb31a1782bd6f16c08d767d9a8a87e753da252abbe00389008429829458 | 实质报告/完整发现/覆盖/归属/限定证据 |
| progress.json | 24209 | 716333de6cc36a3eb007202fd907750d4fb353c949a0ba6071bdabac496dba2f | 实质报告/完整发现/覆盖/归属/限定证据 |
| proposed-batches.json | 12798 | 978da8325ae98eb14e562bf6431c40127e41a23415efdd7efec93c24e33da1ab | 实质报告/完整发现/覆盖/归属/限定证据 |
| protected-input-check.json | 10466 | 94be00b9d314fbf0e1d90dba322d7f1207118a2e9a71fa6e40ce38d7bffa6545 | 实质报告/完整发现/覆盖/归属/限定证据 |
| protected-input-check.py | 3771 | 34361116fe39f4f1fb4bde3e255ad1da161e5bb554dec5d28b109c1197503222 | 本轮数据/产物/发布辅助；不执行参考行为 |
| publish-review.py | 6009 | 589d1db98dc134582380d376fac82ebb9f024d2758d1ca5d936fc79373ea3113 | 本轮数据/产物/发布辅助；不执行参考行为 |
| reference-cloud-availability.json | 855 | 75c4b9fb729972394ece6b0a006a77046a85a31606db8cba1b1bc81ae8295fc3 | 实质报告/完整发现/覆盖/归属/限定证据 |
| reference-critical-source-readback.json | 30684 | 3b39e632af6b2d83eda269ed710465aca8d3bf293810918b60dfc70069068ebb | 实质报告/完整发现/覆盖/归属/限定证据 |
| reference-file-coverage.tsv | 302010 | 2fb3dde035fc9316f27a0a2591afed156d361ffb1c344528b73a26fd6ce660e6 | 实质报告/完整发现/覆盖/归属/限定证据 |
| reference-file-inventory.tsv | 77535 | bf151b7ef1bb45dedfbd23eb605555c00128acf9f92ddd201daa02a8528ee9d0 | 实质报告/完整发现/覆盖/归属/限定证据 |
| reference-readback.py | 2040 | bd084c16633992851013d5dd78658f281ebba9d2f1a33e0eb0c0cf7586a831b6 | 本轮数据/产物/发布辅助；不执行参考行为 |
| regression-229.tsv | 103963 | c199fcc53d3114eeb981c8e27ed7ec5d304e23cfc8fa6b8f956d8ef0490f70b8 | 实质报告/完整发现/覆盖/归属/限定证据 |
| regression-identity-checks.json | 2951 | fd45ca26900c0f1d74212ca112b1133bc95a05ce40225125e385fa094dacd87a | 实质报告/完整发现/覆盖/归属/限定证据 |
| remote-input-readback.json | 831 | 250c443b8488144bdebd978dd318ef9ff2b7876e5361f27bf12bc18551947172 | 实质报告/完整发现/覆盖/归属/限定证据 |
| reviewer-instructions.md | 3900 | 445cba0f5664e4aabb984b9e534b6f1d842b57d13c94ac417ec037e7b81b0438 | 实质报告/完整发现/覆盖/归属/限定证据 |
| root-assigned-specs.json | 895 | 470ffc004001eb10dc479205dff88c7fa8b970565c692e8447c238b0b050d412 | 身份已核导航/完整旧控制；不是当前通过结论 |
| root-integration-reading-log.tsv | 39311 | a422b09d795d3a97cad7c394fddd48e64666a517c658a9a54249ab1a2c379206 | 实质报告/完整发现/覆盖/归属/限定证据 |
| root-spec-coverage.tsv | 104707 | 01f1d8a82954ae612042c567496b8134bb8d0e056028f6f9e28c03853a3318eb | 实质报告/完整发现/覆盖/归属/限定证据 |
| scope-audit-resolution.json | 700 | d07ee67d7c150124e1aa713e81e94fa09c5a9a97d259527f6ca5cf510eb20e19 | 实质报告/完整发现/覆盖/归属/限定证据 |
| shared-file-owners.json | 1216 | 03b8389c5cedf99eb79bc1ee1db69377f53807d2f283833a41a39b9b7063aec1 | 实质报告/完整发现/覆盖/归属/限定证据 |
| spec-coverage.tsv | 13716338 | 1f8c5ccb5e2714d9e1b2b4a8c1847572e0eb88c6f93bb2cc14993532666038da | 实质报告/完整发现/覆盖/归属/限定证据 |

A之后生成的完整prompt及最终manifest/实际publication receipts/结束说明由本地review分支后继发布，用户最终回执给精确SHA/tree/path/hash。无需文件自嵌自己的发布SHA；本提示词已给全部必要A固定入口和完整findings。当前本地绝对路径仅用户查看便利，不当云端可达。公开R关键64 body证明亦在A；云端若某必需输入不能取得，列missing_transfer/受影响步骤和最少处理，不默用浮动分支或想象素材齐。

未转移的是原剩余60未完成候选（不依赖作结论，nonblocking保全）和不存在/未提供的游戏资源/宿主工程（阻止相应runtime结论）；reference独立ignored仓库须从固定R取得/验证，不是已打包。缺材料不阻止有源可审的有限静态修订，但不得关闭依赖该材料的运行/全启用保证。

本轮本地review报告/交接包提交推送早已获授权，已正常选择性暂存该隔离根并真实发布/读回；旧62原件/正式/参考/公共台账/原稿/旧完整证据/主ref均未改。不合并main、不force、不改历史、不删历史分支，没有不可恢复清理/扩大凭据。隔离临时Git读回目录保留并在receipt记录。未来update/正式接受与关闭登记仅依用户届时实际启动和授权，不能由当前出版授权自动扩大。

## 8. 未决决定与云端第一步

用户未决：对参考bug/异常选择精确兼容、兼容模式或记录现代差异；无静态caller尺寸辅助的产品范围、视觉/默认艺术是否精确复刻；可选M09导航/NoRequired M02显式例是否纳入；是否补工程资源、扩展可得未全审内容、开展真实运行。事实补文档与未来bug政策分开，不把unknown等于无问题、可选或已关闭。

云端第一步按下面顺序有限完成：

1. 确认用户现在明确指示update及实际修改/登记范围；没有启动指示则只保留这份移交，不运行任务。读根AGENTS及适用指令，managed cloud若有runtime skill先读其环境政策，不绕过权限/安全拒绝。
2. 读本完整提示词、manifest、final-report、findings、baseline、limits和相关批的模块/交界/回归附件。身份预检只核必要完整性/可读性，不要求先重审全部历史大文件。
3. 验repo/D/S、131逐字节清单、R关键source可得，A报告/manifest hashes/bytes及实际Git固定ref，核模型/独立角色/可见任务/未保存变化/共享writer/资源运行限制。main_merge等旧字段按历史，不替实际Git。
4. 给READY、READY_WITH_LIMITS或BLOCKED：具体证据、影响能力和最少事项。回显/并行/素材限制可READY_WITH_LIMITS；关键固定输入不符/必要source不可取/危险dirty/实际活动冲突/全部review角色条件不符才按受影响范围blocked，不自动reset/修环境或恢复旧任务。
5. 条件满足立即按用户授权有限U批修订，持续progress/findings/依赖台账。继承本次实质成果，只对变化身份/前提定点核，不从零全局review。每批真实整合状态独立验收、角色分离、正式接受/最终关闭分层；未满足跨批/共享/必要验证条件保持未最终关闭。

**今天没有dot接手、承诺或自动启动。只有用户将来交付并明确启动才开始；完成获授权有限修订后如实报告残余未知和用户决定，不无限扩张。**
