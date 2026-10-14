# R6-U13-R 历史资格与载荷独立审读

被审冻结候选：`00b45de642f07cee9953e42f04cce9c35d77346f`，tree `6708f580d5a02f874a1a24a95d7c0649b10c393b`。本报告仅裁历史资格、受影响旧控制、载荷与工具边界；八 ID 的源行为细审由父审的 facility、variants、recording_save 负责，不能把本报告当这些分项的第二次完整独立终裁。实际写入只在本 history-payload 目录；未改候选、formal、参考、分支或 tag，未提交，未执行作者脚本、参考定义、宿主、保存器或真实保存。

**结论：候选包 FAIL。** S001 的正常回归控制丢失与历史获取说明错误必须修复；两项均归既有 S001／证据包条件，不增加规范 required ID。其余本文所核历史资格与精确字节保留范围支持静态通过，但不转移旧 PASS、不授整合 PASS、正式接受或 CLOSED。model／effort／tier／speed／平台 UUID 均 `UNVERIFIED`：请求 gpt-6.1-sol/ultra/default/普速没有有效运行回显，协作工具公开 metadata 仅列 priority 且无 default tier 选择参数。辅助文本核验不能视为满足指定配置资格。

| 项目 | 裁定 | 准确位置与最小修订 |
| --- | --- | --- |
| 原正常保存/载入及无格式迁移控制 | **FAIL，必改** | fixed main 的 pokemon 测试目录 `SF30` 第40行原 b 为正常结束后保存→载入、未开始/已结束会话及统计持久，c 为无 Safari/捕虫相关转换、普通载入无格式迁移。候选同第40行把两项替换为活动菜单门，SF36–40只新增活动保存/拒绝/失败前缀，未承接原 b/c。WP53正文246–248保留事实，不能替代测试目录正常对照。恢复在 SF30 同一行的独立正常结束→保存→载入与无转换子例，并保留计时基准未知及新菜单四组合；仍40条，不增加ID。 |
| R5原路径获取说明 | **FAIL，必改** | `historical-regression.json /R5_exact_scopes_read/0..2/retrieval_note` 及 `bind_history.py` 的 r5 构造处（第65行）称“Original contract path was not present at declared f49d object”。独立远端与当前本地 fixed f49d 的准确 root-M07/root-JXN path 均实际存在且 bytes/SHA/blob相等。把说明改成当时本地读取失败／诊断未证的准确范围；保留旧失败原记录及后继成功恢复，不把缺本地对象改写成固定提交无路径。不可仅在报告解释而继续由脚本生成错误字面。 |
| 作者唯一性自检 | **FAIL（工具证明能力），实际目录独立 PASS** | `verify_candidate.py:122–123` 先用ID作字典键去重，再比较 `len(newrows)` 与 `len(set(newrows))`，不能查重复；SF132–135同样先去重且未独立检查唯一性。原始行独立重数为QC49/49、WS36/36、PA32/32、RC29/29、SF40/40，无重复。最小修订是先保留原始ID序列并查总行数/唯一数/重复差集，再建索引，勿把无效断言冒称唯一性证明。 |
| SF30例外盲点 | **FAIL（回归充分性）** | `verify_candidate.py:135` 将SF01/SF30排除逐字保留，`tool-validation.json /preservation/4/changed_original_rows` 仅列变化允许集；因此其PASS不能证明变动行仍保留正确旧子例。`historical-regression.json /author_static_check` 的 COMPLETE 强度超过S001实际目录。新验收须逐子例核保留，恢复SF30后对新hash重审。 |
| 整数算术证据 | 限定通过 | `verify_candidate.py:147` 的1×100//205与3×100//205确是独立整数计算；h24_m0_factor/h24_m1_factor的30是直接字面，并未独立计算概率因子。工具证据只能分别记整数计算与预期常量，不能用常量填值证明新Palace语义。 |

历史资格实际按以下有限接点审读，而非将74导航记录变成74新语义 PASS：

- R1保持原WP限定，没有自造总数。SF30正常子例就是本批必须保留的旧正确控制，不能因新S001缺口修订而删除。
- R2精确B12/B13贡献五元组读集是 legacy `/contributions/231..239/historical_identity_scope_reuse`；B13实际 `d81562...` 原文件 `/controls/0..7/complete_current_control_fields`，B12为 legacy `/controls/84/historical_identity_scope_reuse`。B13第一条只投影相交的源组织扩展、明确边界，不授整个003根因或全部贡献通过。229控制/21批/341贡献仍分列。
- B003/B010/B025的条款键、原定义与最终加载目标门、q30/r19/r20冰目标对照、灭亡歌保存来源，QC-Q41/Q43/Q44/Q47保留。新人数门不改变这些旧控制。
- B027的nil取消不提交、空数组提交且另判长度保留；新读取人数0不能放宽最终min1/max0。B028的count≥3后连续3/4/5轮裁判、mind/skill/starthp和开场提示不因补位重置，PA-P20/P28原行保留；回复期例不重置周期。
- B029记录非随机属主询问的完整生产消费链、攻击阶段BatonPass记录1/回放消费1，Roar随机及Arena不可选对照仍受原门；新准备后属性捕获仍在初次入场/首命令前，不挪换人消费。RC-W16/W24/W25/W26及WP58§5.2保留。B018原W22b仍存在；新目录数量独立重数通过，数量不推出完整行为。
- B12-B026的缩队一员不等于大会接管：伙伴/双候选走普通2v2、去伙伴或force-single才可单候选大会覆盖，预算/K/通知边界不变。SF35原行保持；新活动保存的serializer单员不得推导为大会战斗接管。
- R3/R4完整读14条具名原scope（historical JSON的 `/R3_R4_exact_scopes_read`），其与本批只按共享WP40／非SF测试后缀有限关联。WP40去掉唯一Arena新增句后完整旧字节相等；BP/FP/PD/VF/LT后缀完整相等。GR3-M08原NaturalGift首次错误与GR4-J08限定后继不被Arena目标完成说明替代。R3 23/76、M09 optional/U08旧未启动/M02 NO_REQUIRED；R4当前17/76和B5旧16/75保持。
- R5完整读M07-001、M07-002、JXN-002的精确资格字段。bbdee081的findings0/1与7b21312的findings1原blob独立恢复且投影相等。回复期门只在更早门通过后终止并保留失败假；资格拒绝先命中仍真，PP不扣，完整正常尾部且存活才复制/消费。Metronome只按实际到更新点和最近身份，成功不是额外门。JXN-ERR01仍要求普通1v1排除设施变体、两次优先序和资格、诊断/裁判/重排/清理正常等全部前提，不能将其扩成Arena重试保证。第五唯一92 CLOSED/51P2/41P3、optional7/no-required7/policy6/limits13及410/568/158分母未被重开或扩大。

消费接点新核：WP09§5.1的全部持久值校验、打开文件前类型异常与IO仅回退计数；WP65§4/§6的退出前保存忽略布尔、Save可见门与两专用退出项；WP17§3.3.1/§7的忙暂停与地图微更新前提；WP66-A§4.6第132行仍无条件写达到规则人数即限制Entry/焦点，须由唯一整合者接收正读取人数限定后，绑定实际整合版本独立复验。WP65旧“进程结束”字样不授真实宿主进程结束观察，本文只核脚本场景置空与正常返回前缀。recording_save的新源链复核与本文恢复旧B12/B13资格是具名peer接点，不是继承作者阅读。

载荷／工具层证据：辅助 bytes-audit 对23文件（8mirror+15evidence）逐载荷fixed/worktree path/mode/type/bytes/SHA/blob全核相等；8份prepare469a原mirror与main8ea原formal相等；72 contract payload、36 required source/formal及七反证声明身份核相等；79阅读账本记录每段git entry/返回bytes/hash与36必读全文覆盖机械核齐；37 changed spans精确重建。上述完整身份检查不证明作者实际理解每行、提示初期UTC或宿主执行。common-structure-audit.json完整解析14共同JSON的1435结构节点、无重复JSON键；common-frozen-identities.json核432R+131formal字节身份全部相等，但没有把563次hash读取算成563份语义全文。

新审中保留了本地历史对象缺失、MCP legacy大载荷传输关闭、远端blob缓存运输多一LF以及相应后继恢复。两R5缓存精确bytes分别58751/162386，hash/blob与原声明严格相等，运输extraLF的初次不匹配和纠正独立保存于blob-recovery-receipt.json。恢复成功不能倒补旧UTC、配置回显、原失败原因或实际源运行。全文／结构／字段投影／本人／辅助阅读在reading-ledger.jsonl和bytes-audit账本分别标示；不把结构投影冒称全部旧报告的游戏语义新审。

最低后继动作：修复SF30原正常子例、R5三说明与生成脚本；更新候选及证据冻结身份，对新载荷复审S001和两项包证据。此后仍须R6-I共享文件接收（尤其WP66-A）、实际整合后全文/接合/历史回归、非作者独立验收和关闭依赖。当前不授CANDIDATE_PASS／INTEGRATED_PASS／正式接受／CLOSED；无新reference/host/real-save运行，配置要求仍未核定。

最终恢复补核（2026-10-14，实际收据 `bytes-audit/historical-final-summary.json`）：fixed c0ff 三原文件 exact commit/path/mode/type/bytes/SHA/blob 全匹配；74导航所有record/scope指针、canonical hash、scope_keys及归属元组全部核实。legacy25个control用原primary_owner，其余49用batch_owner，按显式归一化核对，没有扩大原owner。14 R3/R4投影、9 R2贡献、B12 controls84、8 B13有界投影、3 R5 findings与原声明均匹配。legacy BODY_PENDING已解除；没有额外复制28 MB正文。原77项本地缺对象失败和MCP Transport closed在 `bytes-audit/object-recovery-transition.json` 与 `c0ff-remote-payload-receipt.json` 保留，后继历史核验错误0不覆盖失败。当前没有剩余对象恢复blocker；SF30与R5获取说明两项FAIL及配置UNVERIFIED仍在。
