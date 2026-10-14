# R6-U12-A 候选交付

从固定准备提交 `469a268b92daed7b4d28d7fd0da75520cbb7228f` 创建作者分支 `codex/remediation-sixth-r6-u12-author-20261014`，只修本批四份镜像，另写本批 evidence。正式 main 输入为 `8ea169fbd0f33f378b5d732fd6bea59e854e04a6`，参考为 `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`。全部源与旧报告保持只读。

| ID | 实际修订与作者静态结果 | 新向量 |
| --- | --- | --- |
| GR6-UI-BAG-001 | WP66-C §6.1、WP29 §4明确默认问候2条／提供普通文本时1条替换；两分支正常返回后共同2条告别及清覆盖。进入过滤早于问候，取消不恢复列表；失败不补收尾保证。所列有效前提下静态自检通过。 | R6-U12-BP01–04 |
| GR6-UI-BAG-002 | WP66-C §4/5/6.4/8、WP27 §4.2、C12/C36明确Bag成功提示→正常返回后逐件不检查删除→刷新；PC检查整批删除→刷新→成功提示。数量5丢3的提示边界分别5/2，正常终态均2；显示失败及条件忙暂停保留各自前缀。所列有效前提下静态自检通过。 | R6-U12-TS01–05 |

原C12终态不是错误，修订补提示阶段；C36仍是checked整批删除且无容量预检。现有数量取消、确认No、重要物品及调试门、过滤同列表所有权、购买统计／全价实扣／半价显示、回退与登记等范围保留。其余721行既有表格记录逐字保留，新增9行向量全部是未执行设计。

已分段完整读固定提示2720行及合同1288行；提示中的合同与独立合同字节完全相同，该重复区由独立全文读取覆盖。指定源 Bag704、ItemStorage376、BPShop525行和四份正式全文1554行均新读；必要容器、显示/更新消费者与WP17共享合同另有具名范围。完整阅读与源身份见 [semantic-reading-ledger.json](semantic-reading-ledger.json)、[prompt-contract-reading.json](prompt-contract-reading.json)、[read-segments.jsonl](read-segments.jsonl)。输入摘要或旧PASS未被当作新语义验收。

逐ID七组实际记录见 [author-findings.json](author-findings.json)。原反证身份及有效本批两项完整root反证入口见 [original-evidence-identities.json](original-evidence-identities.json)；混合UI反证列表中无关对象只核身份，不冒充本人全领域阅读。完整原提案已在固定合同中阅读，原历史PENDING字段保留。

历史回归见 [historical-regression.json](historical-regression.json)、[historical-qualified-inputs.json](historical-qualified-inputs.json)、[r5-exact-binding.json](r5-exact-binding.json)：只回归本批当前受影响条款/接口，保留R1原WP范围、R2精确贡献五元组、R3/R4资格及已激活R5精确scope。旧失败／MISMATCH／LF纠正与optional/policy/limits不重写、不重开、不扩批。文档、身份、保留行、差集、allowlist及实际改动检查见 [tool-validation.json](tool-validation.json)。初期读取范围和验证schema错误按 [pre-capture-attempts.json](pre-capture-attempts.json) 保留，不倒补未捕获时间或退出。

本作者新增证据分为SOURCE_STATIC、DERIVED_VECTOR和TOOL_VALIDATION；新增原参考执行、完整行为模型、宿主／Demo、物理输入／图形音频及真实save均0。原3向量隔离探针只是历史证据，本作者未重新执行、未继承为新运行。实际模型／effort／tier／speed／平台UUID未有有效回显，按 [provenance.json](provenance.json) 记UNVERIFIED；依用户指令没有运行CLI或额外代理证明配置。

状态是**作者候选完成，待父线程安排独立非作者审查**。未自签CANDIDATE_PASS，未写正式接受或CLOSED。R6-I仍是唯一正式文件接收者；WP27与U01/U14、UI测试目录与U10/U11的共享写入须按本批精确diff合并，不用此baseline镜像覆盖别批改动。随后需要候选非作者审查、实际整合、共享全文/接口/历史独立复验和正式接受。宿主未执行与配置未回显继续如实保留。

候选commit/tree及最终发布对象由外部发布回执/最终响应绑定；manifest不递归自哈希。
