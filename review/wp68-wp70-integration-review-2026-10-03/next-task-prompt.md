# 整合批次管理收尾：B-INTEGRATION-R01/R02两项P3

工作目录 `/Users/dingshinn/Desktop/pokemon-framework-reference`。独立审查确认WP68–70导入、原件归档、路径重映射、依赖适用性及具名批准范围正确，没有行为返工；整批因2项管理同步问题仍为REQUIRES_REVISION。先读本目录report.md、findings.json、matrix-change-inventory.json、current-index-status-residuals.json、approval-authorities.json、registration-checks.json及AGENTS.md/extraction-plan §2.2。

## 允许范围与基线

当前登记第129轮、TSV v104，完整身份见报告和input-manifest。先实测当前文件，不硬套旧数。WP68–70九份规格的路径重映射版及全部原字节导入/归档保持，不重新导入；WP76及其它已审行为稿/附表同样保持。

新收尾材料放 `review/wp68-wp70-integration-and-status-reconciliation-2026-10-02/revision-v2/`。旧整合v1报告、回填表、自检、映射、管理diff与本review及快照全部留史；不要改写其旧计数以伪装首次就正确。

## R01：统一数量口径

实测是41处状态标注回填（B6＋主线/N01/WP76共16＋GR19），另5处已有规格链接状态附注，总计46。另有6条B新增规格链接，Notes列总共11行变化；矩阵状态列40行变化，因为F04-03含两项GR。按单位分别报告，修正“46＋5”。新报告、回填依据、自检与新增登记摘要一致；第129轮历史中的旧数字通过新轮勘误说明纠正，不回写历史。

## R02：同步中央当前审查状态

以current-index-status-residuals.json的35条当前specs记录为范围，逐项查最新具名批准（approval-authorities.json给出入口，仍需按实际范围核对），将manifest §1的当前审查注记与Feature Matrix一致。保留当前规格哈希/字节；原送审状态若有审计价值，明确标为“历史提交状态”，再追加当前限定通过结论和批准报告路径。不要全局替换旧交付/历史ReviewPending。

报告/回填依据及manifest矩阵汇总中，F17-07应明确“WP71 A～F静态范围已通过保持，事件奖励/媒体/全尺寸可解性和分布等未验证子范围保留”；F18-06和F18-07 Demo保持实际Provisional。矩阵本身已经正确，不为这次文字修正重新改其状态或行为。旧问题台账、review原件、冻结快照不覆盖。

## 交付与停止

提供两项回应、修订版整合报告、按单位列出的回填依据、35条当前记录同步清单（最新批准/范围/未变身份）、相对本review冻结当前manifest的严格管理diff、身份及自检。manifest §2.2/§3/§4只追加；通常续第130轮与TSV v105，但以开工真实现状为准。主TSV仅登记本轮新增/变更管理材料；不得把reviewer原件当提取侧自检或修改旧批准。

核验完整哈希/字节/路径唯一、旧文件允许变更集合、历史追加、所有批准范围与链接；末检单独保存避免自哈希。完成后停止送两项短复核，不自行标本批通过，也不启动WP77。通过后按顺序WP77→WP78→WP79→WP80推进。

reference只读，HEAD固定8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b；不运行参考/游戏/编译器/反序列化/行为模拟器，不写新框架，不创建聊天/Agent、不跨会话发消息、不提交推送。
