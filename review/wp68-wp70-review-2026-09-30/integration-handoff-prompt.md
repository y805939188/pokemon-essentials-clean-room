# 单一整合者交接：WP68／WP69／WP70批次B已限定通过

本提示供后续明确负责整合的会话使用；当前review会话没有执行整合、没有创建任务或发送跨会话消息。不要因为读到本文件就替代主线A的工作或自动启动WP71。

先完整读取独立审查报告：

`/Users/dingshinn/Desktop/pokemon-spec-parallel-minigames/review/wp68-wp70-review-2026-09-30/report.md`

**审查结论：WP68／WP69／WP70全部PASS_SCOPED，限六活动的具名静态范围及三份附表，无必修返工项。** 来源异常已由reviewer独立核实，不应擅自修成理想规则。运行、事件、媒体、概率分布和阶段出口仍保留。

## 1. 复核输入与并行适用性

- 独立交付根：`/Users/dingshinn/Desktop/pokemon-spec-parallel-minigames/`。
- 主工作区：`/Users/dingshinn/Desktop/pokemon-framework-reference/`。
- reference全程只读，commit固定 `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`；不运行任何参考代码、玩法、生成器、解释器或真实网络。
- 对照独立报告§1、review的`input-manifest.json`／`current-hashes.tsv`，复算9份规格／附表和待导入材料的完整SHA-256及字节。原被审版本为B-v1，不能仅用前缀验证。
- 原交付摘要：`53af402e567def39288b12c098603ec044c18b5e0b1d66b2d5e06a0fcb73ee7b`／7,311字节。
- 原整合提案：`c4c4c6ea6e56547b9f15320066b6f8696095f71453a40a265f63c0747df089cd`／19,820字节。

读取主库根及适用AGENTS、当前矩阵／manifest／主TSV。逐项检查新目标是否存在，核对实际采用的WP06／17／19／24／25／27冻结身份与当前主库适用性。主线A正常推进不是错误；不要求主库整个历史快照不变，不回滚A，也不把冻结规划文件覆盖回去。

若目标已有不同字节，明确比较来源／审查身份与差异，不自动覆盖；若依赖改变，只审其对本批合同的实际影响，不重做已通过基础包。没有冲突且适用性成立时，在整合任务授权内继续。

## 2. 精确导入范围

使用 `delivery/integration-proposal.json` 的25项`new_artifacts`和完全相同的白名单，按各自`suggested_main_relative_path`导入：9份新规格／附表，16份提取侧交付／证据材料。逐文件验证完整身份，不复制整个独立工作区。

必须排除：

- 20份冻结上下文的原路径，包括旧specs、AGENTS、规划／manifest和基线权威材料；不能覆盖主库已有文件。
- 独立工作区的`delivery/current-hashes.tsv`，不能用它替换主TSV。
- 提案本身与提取侧`final-checks.json`是运输控制材料，不是旧白名单payload；如需留档，另放明确的证据路径，不能把自检文件当审查通过报告。

reviewer原件是另一组材料，不能覆盖提取侧同名文件。按本review目录`final-checks.json`的artifacts清单另列精确归档映射，例如导入主库新的 `review/wp68-wp70-review-2026-09-30/`。需要一起归档输入快照时，按review的`input-manifest.json`逐文件列入该审查目录的`input-snapshot/`；它们只是审查证据副本，绝不能映射到主库原specs／planning路径。保留原件字节及审查／自检角色区分。

## 3. 外审登记与管理性回填

通过范围逐项登记：

| 包 | Feature与限定范围 |
| --- | --- |
| WP68 | F17-01：Duel D-A～E；F17-02：Triple Triad T-A～G |
| WP69 | F17-03：Slot Machine S-A～F与有序转轮附表；F17-04：Voltorb Flip V-A～E与候选附表 |
| WP70 | F17-05：Lottery L-A～E；F17-06：Mining M-A～F与候选／铁形状附表 |

允许按报告把主稿／附表及六条矩阵对应子范围回填 **Reviewed（限定静态范围，2026-09-30独立批次B首审PASS_SCOPED；管理性回填）**，保留前向Inventoried。不得改F17-07或把所有小游戏、Demo、运行、全项目写成已通过。

原交付文件头部仍为ReviewPending，是被审身份的一部分。可以先原样导入并登记外审依据，再回填；也可同一串行整合中完成。两种方式都必须保留报告固定的B-v1哈希、实际回填后完整哈希／字节及管理差异，不冒充reviewer审过修改后的字节。

同轮只允许必要状态、引用／路径、审查依据和身份登记变化。若改变规则、场景期望、常数或失败行为，单列行为差异和理由，另行复审，不借本次PASS_SCOPED自动通过。参考本身的direct错扣、支付tick、倒置夹限、不终止条件等，不在整合中修复或删除。

逐行应用六条矩阵提案到**当前主库**，不要使用冻结整份矩阵覆盖。按主库既有manifest §1／§2.1／§3／§4及主TSV串行登记，实际轮次／版本从当前主库续接，不采用独立B目录的局部版本号。提取自检与reviewer材料分别登记，避免自哈希循环。

## 4. 整合后验证与停止

复核导入／回填目标、哈希／字节／短标签、未覆盖文件集合、引用依赖、JSON、主稿与附表链接、68／69／70对应场景和有序表。审计文字中的`delivery/`身份表路径在新位置需有明确映射；如调整链接或路径，记录字节差异并重测。

保持冻结输入／独立被审产物／reviewer原件可追溯。不得运行自检工具中的任何未经阅读代码；优先用安全自有文本／哈希／集合／固定算术检查，不执行参考或编写玩法模拟器。源commit保持固定，禁止fetch／checkout／修参考。

完成本批导入、限定Reviewed回填、登记和检查后停止并交付整合报告，说明旧被审身份、新回填身份、改动范围和剩余限制。**不启动WP71或第四包，不创建Agent／任务，不向其它会话发消息，不提交／推送。** 不改主线A的行为产物；Demo／宿主／媒体／插件、U01–U10、WP77和WP78→WP79→WP80继续保留。
