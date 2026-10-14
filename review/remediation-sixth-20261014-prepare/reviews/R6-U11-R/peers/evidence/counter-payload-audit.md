# R6-U11 反证原载荷静态子审计

9 个 `counter_evidence_ids` 原载荷均已独立完整语义读完，bytes/SHA256/Git blob 全部匹配 expected，且与冻结 HEAD `e93d0e56750a6a16cc50cc68b2c97f11ea255153` 对象同字节。原处置表与候选语义提交 `54af598ca85211641348e6057ed0c348044787fe` 同字节。此结论只覆盖原载荷身份、读取和应用；不自签候选行为 PASS、正式接受或 CLOSED。

## 读集与边界

先全文读适用 `AGENTS.md`（297 行），确认 `/workspace/AGENTS.md`、`/workspace/.agents/skills` 与仓库 `.agents/skills` 缺失。合同 `contracts/R6-U11.json` 全 2016 行按连续 1–350、351–700、701–1050、1051–1400、1401–1750、1751–2016 读完；首个组合输出截断不计合同全读，后续完整分块补齐。原作者 `counterevidence-dispositions.json` 全 159 行、`author-report.md` 和 `early-reading-and-attempts.json` 亦全文读完。完整身份和范围见 JSON 的 `prerequisite_full_read_set`。

大型导入文件不是只读相关节点：完整 320 对象按原序 0–39、40–79、80–119、120–159、160–199、200–239、240–279、280–319 展示并读取，每对象所有键和值均保留，仅折叠空白。全部 8627 行对应的语义内容已覆盖；逐对象原行范围/身份见 JSON 的 320 条读集记录。其 77 条 party、120 条 storage、123 条 Bag/Mart 全部原 `source_read_credit_to_K=0`，本次阅读不把导入信用变为 K 的新源读取。

`/workspace/pokemon-essentials-reference-r6` 在本执行环境不存在；未 fetch、checkout、运行参考或作者脚本。Encounter 的固定 `8c5911...` 源对象可从 clean-room 对象库只读取得，完整读日志源行重建为 2267 字节，SHA256 与日志 envelope 及固定源对象同字节。`main` 命名 ref 不存在，固定 `8ea169...` commit 可解析。expected 中 `5210b009...` 历史 recovery commit 在本库 `git show` 为 128，故只声称本地载荷匹配绑定指纹，不声称此环境重新取回历史提交。

## 全部九份载荷

### EV-0ef3145857f02a64

`review/remediation-sixth-20261014-prepare/inputs/evidence/tasks/R6-F/countercheck-ui-entry-stale-command.json` — 完整 19 行，2442 字节；SHA256 `320b742ad5bd6f804610535ee08e8de2747a524799ba2bcf98647feaf2b990c0`；Git blob `6a2ecc27f138a1471e768d128363d6c6f097d7b5`。

对象：R6-UI-PARTY-004；GR6-F002 (fifth falsification attempt context)。R6-F独立负证据：同物种二人确认被拒后选择循环继续，BACK为nil且summary_calls为空；成功A1/B和人数不足控制也保留。局部command在Ruby loop块每次调用重新初始化，既往Entry0不留存的隔离观察反驳旧静态假设。

- **UI-ST-001**：不涉及储存队伍末按钮几何。
- **UI-ST-003**：不涉及图鉴形态循环或末次记录。
- **UI-ST-005**：不涉及储存选择器；不能由Party旧command撤销推广储存输入阶段。

保留范围：原NEGATIVE_ISOLATED_EVIDENCE_PENDING_ROOT_I_HOST_LANGUAGE_SCOPE_DECISION和root主机语言范围待裁字段不覆盖。 原Ruby2.6.10p210隔离执行为历史记录，本审计不重跑、不计新执行。 无whole host/UI或真实Summary证明；上游count0 Entry-cap差异独立。 与EV-41c7...PARTY-004旧肯定同时保存，不复活已撤销提案。

### EV-1561728b1e620c9b

`review/remediation-sixth-20261014-prepare/inputs/evidence/tasks/R6-K/imported-ui-party-storage-bag-facts.json` — 完整 8627 行，309853 字节；SHA256 `a6d7cec2f4626c28bfa2c4547e7af6ec0a01519d8a3a74c16f090b75bb61a437`；Git blob `c0c9ae765f2f21d09d6ed85597e04c00d826fa80`。

对象：77 party facts；120 storage facts；123 Bag/Mart facts。完整320对象：Party/P001–P048覆盖面板、方向/输入、消息、换位、多选资格、道具/邮件及事件变量；Summary/S001–S029覆盖页面、标记草稿、招式/缎带、Shadow绘图请求与遗忘/查看边界。Storage120对象覆盖图形/导航/选择/切盒、集合操作前缀、Mark/摘要/道具/选择模式与名义素材范围。Bag/Mart123对象含27聚合事实和96拆分单元，覆盖浏览/过滤/排序、数量/消息、普通Bag和PC丢弃次序、买卖钱包/统计/回滚及菜单尾清理。

- **UI-ST-001**：/140 UI-ST-S-0811给末按钮UP最后槽/DOWN首槽；/139、/143、/144、/172保留双列坐标及整理/存入返回区别。
- **UI-ST-003**：没有Pokedex源事实；不能把本导入载荷算作形态资格/回绕/末次写入的独立源证据。
- **UI-ST-005**：/136普通命令BACK>USE；/141盒两阶段、/143队伍两阶段、/165标记方向后BACK>USE、/172和/193上层消费/退出；/146–148切盒与当前盒写入上下文。完整源仍需另读核Input.update，导入概要不能替代。

保留范围：所有320 source_read_credit_to_K均为0，IMPORTED_SOURCE_STATIC不变。 CONFLICT、COVERAGE_GAP_PENDING、OVERBROAD_CLAUSE_PENDING、PRESENTATION_RESERVED、STRUCTURAL_ONLY/STRUCTURE_ONLY、INVENTORY_ONLY、null均为原记录状态，不升成本批裁决。 /149、/154、/169的像素化/预览疑义属于UI-ST-002可选澄清，不进三ID必修。 /28多选旧CONFLICT不得覆盖R6-F后继反证/撤销；/58 Shadow、/69 ACTION缺槽等仍各属party范围。 数据/资源/主机/插件/事件/真实save未执行，不将路径定位算真实像素。

### EV-b27d920efd83c7f2

`review/remediation-sixth-20261014-prepare/inputs/evidence/tasks/R6-UI/bag/counterreview-R6-UI-002.json` — 完整 406 行，22504 字节；SHA256 `17de0fae3e5e45c70cdeae2af2f440be49bd5fd92879b8c020118eef1c885e18`；Git blob `805df95e4e6f6bae9bf8f7f112de0f889dcd5118`。

对象：R6-UI-002 (Safari capacity)。Safari Ball三分容量反证：party1/fullboxes允许且先减球再refresh/throw；party6/fullboxes拒且不减球不投不结算该轮；party6/boxspace允许。核Safari入口/默认Peer/基础存储/正常准备与呈现消费者，反驳先填满六人或另有boxes-only门。

- **UI-ST-001**：只出现默认队伍上限6的独立Safari前提，不能证明储存导航。
- **UI-ST-003**：不涉及图鉴形态。
- **UI-ST-005**：是Safari Ball命令容量裁决，不能迁移其拒绝/消费次序到储存两阶段。

保留范围：SUPPORT与PENDING_EXTERNAL_GLOBAL_ROOT_ADJUDICATION并存，不自签最终。 收编/捕获成功为条件；真实Demo gate/像素/媒体/宿主仍未执行。 允许Ball先减的异常前缀无通用退款；拒绝消息失败无必然重开菜单。 不改上游正确WP53或普通K17/K49，不要求永久兼容源缺陷。

### EV-0ee010f7c2e5072b

`review/remediation-sixth-20261014-prepare/inputs/evidence/tasks/R6-UI/bag/counterreview.json` — 完整 207 行，7790 字节；SHA256 `2330acac3cea7d81b9e53df98411c31fb0ff2a786d553985f342efd5e428fd8c`；Git blob `71062aff787921854d7a5b8638424dd3a5eba031`。

对象：GR6-K-001；GR6-K-002。两个有界静态反证：K001旧记忆口袋字段复制后保留，旧版本上下文重复单项转换可覆盖当前游标；普通正常load版本标记更新后不会自然重复。K002构造器等值Hash键折叠可掩盖name的String验证，数值name0能进入；独立name setter仍拒，现有Owner对象个体构造分支不深度重验。

- **UI-ST-001**：无储存几何证据。
- **UI-ST-003**：无图鉴形态或Pokedex末次字段证据。
- **UI-ST-005**：只涉及Bag口袋迁移/Owner构造，不能外推储存当前盒或输入快照。

保留范围：旧root required/open read只是历史状态，本新countercheck不替root处置。 K001必须保旧提供版本上下文重复选择前提；registeredItems/registeredIndex和choices清理正确保持。 K002有效类型期待String及setter拒绝保持。 reviewer未新运行probe、save、native或UI；future compatibility NOT_MANDATORY。

### EV-8b91c7b176e6f8ee

`review/remediation-sixth-20261014-prepare/inputs/evidence/tasks/R6-UI/root/counterreview-bag.json` — 完整 73 行，3347 字节；SHA256 `ec1a6befe199d202f3ab1e25a28f70f8da3a7b5f9914c034f771338205e18610`；Git blob `11c2d4b96dce096f110e7ea0e57fadc100336d04`。

对象：GR6-UI-BAG-001；GR6-UI-BAG-002。BP普通自定义问候替代默认双欢迎，省略/nil才双欢迎；退出两告别和正常尾clear保持。普通Bag丢3时success消息入口仍5、返回后2，PC独立丢3先删至2再消息；终态相同不能替代阶段对照，0/No取消不删。

- **UI-ST-001**：不涉及储存队伍面板。
- **UI-ST-003**：不涉及形态列表。
- **UI-ST-005**：其Bag/PC消息边界不能代储存方向/动作优先；仅作为共享UI禁止全域推广的范围约束。

保留范围：C12为合并终态行，未升格成明确先删强冲突。 GLOBAL_ROOT_REQUIRED待最终分类保持。 源事实补记不等未来维持缺陷。 proposer probe只佐证，本原reviewer/root无新BP窗口/host执行，本审计也无执行。

### EV-d4c77e20723ddeb8

`review/remediation-sixth-20261014-prepare/inputs/evidence/tasks/R6-UI/root/counterreview-storage.json` — 完整 118 行，5290 字节；SHA256 `3e7ac15d249c99d4c397b951dd26488c462b1ebc133b30b3f6f00a1ef5fa9ca3`；Git blob `2a8ce3fcc03767d2deff80fd37f1fd2dbef936b8`。

对象：UI-ST-001；UI-ST-002；UI-ST-003；UI-ST-005。唯一直接包含本批三ID的非提出者root反证：末Close6 UP5/DOWN0，空槽不跳过；形态可列>1门、UP/DOWN取模回绕且下一轮先写last、BACK不撤，端点箭头隐藏不阻输入；储存方向覆盖UP>LEFT>RIGHT>DOWN后独立按钮，RIGHT+USE选新格，JUMPDOWN胜BACK且分支内Input更新后不落BACK。另UI-ST-002无条件矛盾被反驳，建议只作可选澄清。

- **UI-ST-001**：直接支持缺专门转移；普通WP17窗口或队伍不足6均不能反驳末按钮规则。
- **UI-ST-003**：直接支持本地覆盖缺口，不能改判原正文明确要求不回绕；物种/页/形态三类入口分开。
- **UI-ST-005**：直接支持本地两阶段缺口；方向切盒辅助尾Input.update排除整轮固定快照，JUMP分支不继续同轮BACK。

保留范围：原三SUPPORTED_*为SOURCE/FORMAL fresh static支持，final_adjudication仍PENDING_EXTERNAL_GLOBAL_ROOT历史生成时点。 UI-ST-002 optional不升必修。 原counterreviewer reference/model未执行，hostDemo UNKNOWN。 no_old_PASS_used不等本次新回源验收；本载荷完整读不替候选源/正文独立复核。

### EV-a2277b389acfafc6

`review/remediation-sixth-20261014-prepare/inputs/evidence/tasks/R6-UI/storage/counterreview-R6-UI-001.json` — 完整 310 行，14535 字节；SHA256 `604c1b46bae8f0f1a2f730d623161bf4cb4b9e15a67f663219ceccda3d5b9017`；Git blob `744db6e6d6657dfaea4f9051a24cceca8bff4aa5`。

对象：R6-UI-001 (ordinary battle full-party capture replacement)。正常满队替换成功链：选旧成员A仍在队伍时默认Peer存同一A入盒，返回后删玩家A，送盒暂停内party5/A入盒/N未入队/四记忆未移；暂停正常返回才左移记忆并收N。选人取消/Send-to-Box/档2及存盒失败与消息内失败前缀分开。

- **UI-ST-001**：不决定储存导航末按钮。
- **UI-ST-003**：不决定形态选择及末次记录。
- **UI-ST-005**：战斗pause同步边界不决定储存输入两阶段；只保“取消不通用回滚”的原有有界原则。

保留范围：CONFIRM_STATIC_LOCAL_ORDER_CONFLICT与PENDING_GLOBAL_ROOT并存。 存盒成功并返回前提必保；全满默认Peer兜底错误早于队伍删除。 媒体依赖正常前序才到特定pause；异常无通用恢复/清理。 默认/no-plugin链可静态到达，不是实际hostDemo；未重审全战斗/伙伴/任意Peer。

### EV-41c7e7b577ea4ede

`review/remediation-sixth-20261014-prepare/inputs/evidence/tasks/R6-UI/storage/counterreview-party.json` — 完整 1102 行，52837 字节；SHA256 `89cdac7bda7fdd79cde4c66c2cf05f51583babafe7e3bc0880e7184f2b74806f`；Git blob `36b257d38ceeef94f737db3862d40aa3ad0c7488`。

对象：R6-UI-PARTY-001；R6-UI-PARTY-002；R6-UI-PARTY-003；R6-UI-PARTY-004。四旧静态counterreviews：Summary Mark默认[]显示缺槽0不填齐，独立ACTION比较nil失败，而Storage Mark无ACTION不能推广；重学最初记录只把未会且不在等级候选项前置，非首位GROWL重叠能区分错误排序；Shadow改经验文本仍低于上限请求条，非零Exp需在makeShadow前建立，真实像素未知；旧PARTY-004静态局部command持久假设声称拒非法二人后空Summary失败。

- **UI-ST-001**：Party普通/多选按钮几何不能代储存末按钮。
- **UI-ST-003**：Summary/重学/Shadow与Pokedex形态不同入口，不能替形态回绕证据。
- **UI-ST-005**：PARTY001明确Storage Mark只方向/BACK/USE，无ACTION清零，须保此界限；旧PARTY004局部变量假设已被EV-0ef...隔离负证据反驳，不能迁移储存输入逻辑。

保留范围：四verdict及各PENDING_GLOBAL_ROOT作为旧记录保留，不删除冲突。 PARTY004旧肯定被后继负证据/撤销限制，不能重登记必修；本审计不裁主机Ruby语义。 其他三个仅各自限定静态事实/请求，不升像素、Demo或源缺陷永久兼容。 全部reference/model执行NOT_EXECUTED，host/physical/sound UNKNOWN。

### EV-6f7e577895cef574

`review/remediation-sixth-20261014-prepare/inputs/evidence/tasks/R6-UI/storage/read-logs/reference__pokemon-essentials__Data__Scripts__010_Data__002_PBS data__013_Encounter.rb.1-71.txt` — 完整 72 行，2913 字节；SHA256 `8a5ccb0cc0d46d659859fce7f5d19339dd03ac716d9a4edb806f1269349347fe`；Git blob `829f50d1aa1d42a1ce02726d5a608601c0ef5a0e`。

对象：Encounter data source read-log, not a UI finding verdict。原Envelope及冻结Encounter1–71全部源行：按map/version字符串身份查询，get首选具体版本否则0；each按map/version序；each_of_version选当前版本并对[map,version]键存在性检查决定版本0记录是否追加，记录map/version/step_chances/types/PBS suffix。其查询键表示是否一致不在本子任务新裁。此载荷是带原源文本的阅读交付，不含UI结论。

- **UI-ST-001**：无储存导航关系。
- **UI-ST-003**：无图鉴可列形态/末次记录关系。
- **UI-ST-005**：无储存输入阶段关系；读日志交付状态不等语义PASS。

保留范围：original stage delivered_for_semantic_read不是审查PASS。 不以读取该文本重开Encounter版本/键类型新根因或扩张R6-U11。 71源行重建2267字节，SHA256与envelope一致且和clean-room库固定8c5911对象同字节；参考未checkout未执行。

## 本批三个 ID 的应用结论

| ID | 直接相关原证据 | 保留前提与范围 |
|---|---|---|
| UI-ST-001 | EV-d4c77 根反证；EV-156 的 /140 与返回入口上下文 | 默认上限 6 时 Close6 UP5/DOWN0，末按钮与普通成员 ±2 分开；空槽不跳过；整理收面板/存入关闭确认分开；配置表达不等任意非默认布局可用。 |
| UI-ST-003 | EV-d4c77 根反证直接支持 | 可列 >1；形态取模回绕、下一循环先写末次再受理 BACK/USE且不撤销；不同于物种端点停住与页夹限。EV-156 没有图鉴形态事实，不能凭导入给它增加源信用。 |
| UI-ST-005 | EV-d4c77 根反证；EV-156 的 /136、/141、/143、/165 与切盒/上层消费上下文 | 方向 repeat 覆盖优先后独立动作；服务布尔条件限定各查询阶段；方向切盒尾 Input.update 不能被固定快照概括抹掉；动作 JUMP 分支不再落同轮 BACK；持握禁退及已切盒不回滚保持。 |

读取这九份原载荷未发现推翻上述三条合同的原载荷内容；这不是对候选新增正文/向量的新回源验收，后者由父审计完成。

## 精确问题与后继处理

**CP-01：作者读取范围不能冒充九份全读。** 处置表第 35 行明确大型载荷只读 11 个节点，第 52/69/86/137/154 行对五份只登记身份校验。作者报告也坦诚具名节点处置。保留这些真实历史，不倒补作者信用；本独立读集已经补齐当前审查的九份全文语义读取。该记录问题本身没有证明新增规格行为错误。

**CP-02：复用处置文字缺精确对象。** 第 18/120 行混用“撤销 PARTY-004/捕获 R6-UI-001”，实际上前者载荷只含 PARTY-004 负证据，后者只含捕获；第 52 行具体为 Safari R6-UI-002，第 69 行具体为 K001/K002。后继证据处置应沿本报告逐份对象及三 ID 应用标注，不能因共享反证 ID 列表就把所有混合对象算作每条行为支持。

**CP-03：历史 recovery 限制。** 九份精确载荷身份及 e93 字节均已验证；本库缺历史 5210b009 commit 不宜写成“已重新取回该历史提交”。这是恢复链核验限制，不是载荷字节不匹配。

## 旧 FAIL、撤销与执行信用

这九份载荷没有终态旧 FAIL 门报告：存在静态 failure 提案、CONFLICT、PENDING、SUPPORT 等不同字段。不能用本子审计声称任何旧 FAIL 已消除或历史资格重新验收。PARTY-004 的旧肯定与 R6-F 后继否定均全文保留，撤销不复活；原 Ruby/host 范围限定也保留。UI-ST-002 仍只可选澄清，不升本批必修。早期作者截断、对象缺失、超长区间断言失败及修正、18 次 Ruby 历史尝试分母与 INC-R6-001 均不删除、不重跑、不重计。

本次源执行、独立行为模型执行、作者脚本执行均为 0；host/Demo/物理输入/真实 save/媒体为未验证。只写本 md/json；候选、formal、public、main 均未修改。合同请求模型 gpt-6.1-sol、effort ultra、tier/speed default；实际模型/effort/tier/speed/平台 UUID 没有回显，全部 UNVERIFIED，路由 task 不是平台 UUID。

没有本子任务读取或交付阻塞。父审计仍需完成候选源/正式正文及历史资格/接口复核。
