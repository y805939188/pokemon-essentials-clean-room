# 下一批：WP68–70成果整合＋已通过记录集中回填

工作目录 `/Users/dingshinn/Desktop/pokemon-framework-reference`。WP76 v4已由本目录report.md确认 **PASS_SCOPED，20/20 CLOSED**，可以接续此前已安排的整合与管理回填批次。不重做WP74/75/76提取，不重复询问是否允许继续。本批结束交付整合报告并送核验，不自动进入WP77或最终double review。

## 1. 开工核验与范围

先读本目录report.md、findings.json、next-task-inputs.json、registration-checks.json和AGENTS.md；再读当前extraction-plan §2.2、Feature Matrix、manifest和主TSV。reference只读，HEAD固定8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b，核验Git清洁。

起始登记第128轮：manifest c6fbac9631aa95d270a84c5ad8486bd408875fe6141c7180319bb884ca5526ab／1,098,623；TSV v103 2211e8ad9c418d02ffde174a09011e544ddfc2442efe8a58f9522ff8b106c298／183,000（1,312条）；矩阵91e58b77583fe9296dd82bc746d103d5de8147167eea897d777d51b3f20d06db／68,210。重新实测当前身份；若有独立准备材料，仅在审清其范围/身份后使用，不以其取代批准依据。

保持WP76当前主稿8c266c5bf5fcb660823adde73227a7d7ad0e4ba6875cce1b24f293d31d380ac3／65,374和v4附表7b811db7bcd14b652d79a793d0d9a967d0362adce2e2452b72366eb86e1206db／12,357，以及WP74/75和其它已批准行为产物原字节。中央管理记录承担本轮状态回填，不为更改头部待审字样批量重写已批准规格。

## 2. WP68–70导入：按已有交接精确整合

独立工作区 `/Users/dingshinn/Desktop/pokemon-spec-parallel-minigames/`。完整读其中：

- `review/wp68-wp70-review-2026-09-30/report.md`
- `review/wp68-wp70-review-2026-09-30/integration-handoff-prompt.md`
- `delivery/integration-proposal.json`及上述报告绑定的输入/最终检查材料。

按其原交接逐文件实测：9份已批准规格/附表、25项new_artifacts白名单及各自suggested_main_relative_path；20份冻结上下文不得覆盖当前主区，B的delivery/current-hashes.tsv不得替换主TSV。核对新目标是否存在，复查WP06/17/19/24/25/27当前已批准合同对本批的适用性；有变化只追踪实际影响，不能回滚主线或重做无关基础包。

提取材料与reviewer原件分开归档；审查原件按该review的final-checks artifacts清单建立精确映射，快照仅可进入审查档案子目录，不能覆盖主区原specs/planning。运输提案/自检不是独立批准。所有同名冲突先比对身份；任何行为变化另行说明并复审，不借原PASS_SCOPED覆盖。

推荐先原字节导入并记录映射，再作必要的本地引用/路径修正，记录原被审身份与修正后的新身份；正文行为不变。批准范围仅WP68 F17-01/02、WP69 F17-03/04、WP70 F17-05/06的具名静态范围及三份附表，保留运行、事件、媒体和概率分布未验证限制。

## 3. 管理记录集中回填

先建立“对象—当前状态—最新具名批准—被审版本/当前身份—拟回填范围”的核对表。可从WP75 v4交接的依赖/批准索引起查，但每项必须落到对应最新报告，不能把历史问题台账的OPEN或旧规格头部直接当成当前未闭合结论。

本轮覆盖已获批准但管理记录滞后的项目，包括B导入6条Feature、WP76 F18-05、此前已通过的GR修订/N01/第一组闭环及后续各包中实际仍待回填的条目。以现状为准，不对已同步项目制造无意义改动，也不把未获批准范围顺带标为Reviewed。

只对Feature Matrix、extraction-plan的当前进度说明、manifest当前登记与追加历史、主TSV作管理变更；行为主稿/附表尽量保持已审字节。历史review、旧issue-ledger和冻结快照保留原件；需要汇总当前问题状态时新建有出处的收口记录，不改写历史报告。尤其区分：具名静态范围已通过、运行/demo未知、前向引用待后续包这三类状态。

共享索引由一个写入流程串行更新；没有必要为本批创建并行Agent、聊天或跨会话消息。登记轮次/TSV版本从实际当前主区续接，不能使用B局部版本号；不要对已缺材料的demo虚报完成。

## 4. 交付与验收停止点

在主区新的 `review/wp68-wp70-integration-and-status-reconciliation-2026-10-02/` 交付整合报告、精确导入映射与完整身份、依赖适用性/冲突核对、管理回填逐项依据、严格管理diff及最终检查。若目标目录已存在，先核验其来源与状态，使用新版本子目录，不能覆盖既有证据。

核验所有导入文件/链接/表、旧批准身份、仅允许的管理差异、TSV/manifest全量完整哈希与字节、路径唯一、历史追加及reference HEAD。末检单独保存避免自哈希。报告明确原被审身份、整合后身份、状态范围、未验证限制和实际未完成事项。

本批完成后停止送整合与管理回填核验；发现行为冲突先处理并复审。WP77以及WP78→WP79→WP80继续按计划后续安排。只做规格与审计，不运行参考/游戏/生成器/编译器/反序列化/行为模拟器，不写新框架、不提交推送、不跨会话发消息。
