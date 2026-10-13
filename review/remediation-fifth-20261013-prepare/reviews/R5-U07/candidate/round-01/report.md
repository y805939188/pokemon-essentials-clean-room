# R5-U07 非作者独立候选复审（round-01）

固定候选的七项、三十三条必修静态标准已逐项核对：三十二条限定静态通过；002/C01 为带审查前提纠正的限定静态通过。六个 ID 可签各自候选局部范围，002 可签来源一致的更窄范围。没有要求作者制造“捕获体跨 LF”的错误规格。全部七个 required ID 保留，实际整合、正式接受及 CLOSED 均未签署。

| ID | 标准数 | 独立候选裁决与实核范围 | 剩余门 |
| --- | ---: | --- | --- |
| GR5-M12-001 | 3 | PASS_SCOPED_STATIC：实际 Main 安全解码身份、文件/目录顺序、隐藏项、899/900、错误分层和已加载前缀 | U01/U03/U06、实际字节复审 WAIT |
| GR5-M12-002 | 3 | PASS_SCOPED_STATIC_WITH_REVIEW_PREMISE_CORRECTION：六族行门、整字段丢文、旧18参数/规则与 trainer-only 重访；捕获体不跨 LF | SC-U07-001 登记者处理；依赖/实际复审 WAIT |
| GR5-M12-003 | 4 | PASS_SCOPED_STATIC：两页门的全部方向/音效/2/6/8/等待路线/透明/原目的地，独立转移80/100及失败前缀 | 依赖/实际复审 WAIT |
| GR5-M12-004 | 2 | PASS_SCOPED_STATIC：两布尔族各真→假/假→真/全假/下一事件重置；首页和再战消费、采集/解析支门 | 依赖/实际复审 WAIT |
| GR5-M12-101 | 11 | PASS_SCOPED_STATIC：新建类型/道具原文与 ID/提示/显示/档案/PBS差异，已有训练家败词父 Yes/No 与外层 Yes/No，嵌套写入和重载三层 | 依赖/实际复审 WAIT |
| GR5-M12-102 | 5 | PASS_SCOPED_STATIC：REPEL工作/登记/档案/PBS四阶段、BP1→0、两份量 nil/空串/???、SellPrice半价反例与实际库存/覆盖消费门 | 依赖/实际复审 WAIT |
| GR5-M12-103 | 5 | PASS_SCOPED_STATIC：后置显式门与普通底层登记分开，在场写穿/场下简化、seen/seen_forms与首写末次、BACK/同值限定、非自动存档 | U03/U06旧Summary C01残余与实际依赖 WAIT |

## 冻结身份及独立性

- 合同/入口：`22fba7786b0090a1955ce6211315b0036cddfbcd`，tree `21f3484d167d8cab7a288e0204c72f275414d52e`；入口 `contracts/R5-U07/reviewer-entry.md`。本次与作者证据中的合同七文件全字节相同。
- 候选：`367827c70622071bdbbd1db91111bc8e208a946f`，tree `25d8cfe853347d7afa5dbf1f7ec1097e48862491`。
- 作者证据：`70d1d4773af04fab74cdf3a91fbb0d4ecff924f1`，tree `afe9e4a48739d33f90b8f59c93a1b0ff9640ce6e`，分支 `r5-u07-author-20261013`。
- B5：`9366d9d17aaeac3b4414236468affa650fb3dd27`，正式子树 `d5a462b4c6f8b78c3264a25d6b5495230fa265e2`；R：`Maruno17/pokemon-essentials@8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`，tree `7589c800b61ba13a13040ed0d686979b80a84fd0`。

本次委派任务未参与此前候选创作；可见任务标识 `/root`，三个独立只读子任务为 conversion_semantics/editor_semantics/form_regression。平台全局任务 UUID 未回显，记 UNVERIFIED；来源线程只记为委派来源，不冒充审者身份。Git 提交账号不作为作者/审者任务同一性证据。请求参数 gpt-6.1-sol / ultra / default / 普速 / 禁Fast，实际模型、推理、档位、速度回显全部 UNVERIFIED，未审计额度或认证。

已读仓库 AGENTS；环境 `.agents`/`.codex` 为空，B5/冻结/证据树无 `.agents/skills` 或仓库 SKILL.md。仅写本独立 review 域；没有修改参考、作者、正式正文、公共登记或冻结历史，没有 merge main 或操作 Mac。

## SC-U07-001 可审计裁定

裁定为 **纠正审查前提，保留 002 必修，并签更窄的来源一致范围**；没有作者语义返修要求。固定转换器六个识别点在1000/1016/1034/1053/1075/1100行，捕获体使用排除 LF 的点匹配且无 m 或局部跨行选项。Ruby 2.6 与 3.1 官方文档均分别定义点字符、m及包含LF的空白字符。因此“调用外围空白跨行”“合法调用独立行前后可有其它普通行”与“括号捕获体跨 LF”是不同条件。[Ruby 2.6 Regexp](https://docs.ruby-lang.org/en/2.6.0/Regexp.html)、[Ruby 3.1 Regexp](https://docs.ruby-lang.org/en/3.1/Regexp.html)。

原审 `root-M12/canonical-findings.json /findings/1/expected_reference_behavior/facts/0`、boundary及failure边界将第三个条件混入。原 `GR5-EXEC-REF-001` 六输入只测试单野外独立前/后行、同一行前/后缀、空括号与单行正例；没有体内 LF 样本，不能替错误前提提供执行证据。原 `GR5-EXEC-REF-002` 十八旧输入两遍仅证明有限结构观察；六族全参数/源门另由静态实读对照。

来源一致的最小对照：有合法完整调用行时，其前后独立普通行仍可被整字段替换丢失；唯一调用的括号体包含 LF 且没有另一个合法调用行时，不满足此识别门；外围空白的LF仍另行可匹配。同一行无关前后缀、错误大小写、空括号及不同家族优先次序均保留具体前提。

作者 WP75 §8.2、U07-C02及scope-conflicts作了正确选择。`finding-responses.json /findings/1/failure_cancel_partial_submit` 仍继承冻结“捕获体可跨行”错误句：该句明确排除出本次签名，不能作为当前规格/执行事实再发布。登记者应在单独裁定回执/后继证据中处理这句及原前提，保留 required ID 和行门/丢文根因。本任务没有自行删除必修、改合同或改公共台账；也没有签任意畸形输入、全部Ruby实现或运行通过。

## 候选、共享提案与旧回归

从固定Git对象完整读取候选新增16载荷与作者证据17载荷；作者manifest中的15项受校验载荷共384560字节，manifest自身与publication证据另按固定Git对象核身份。四份B5目标、十三个片段的唯一替换锚/原行坐标/字节偏移/长度/hash独立核对并重建；在scratch用固定补丁进行 `git apply --check`、实际重放，四份结果与独立重建及proposed身份逐字节相同。没有运行作者verify脚本或写正式路径。prepare相对任务freeze只多既有preparation-publication-receipt，合同身份未漂移。

四份受审拟整合字节身份详见 [independent-validation.json](independent-validation.json)；共有WP72/WP73-A/测试提案仍交 R5-I 唯一写入。AUTHOR-CONVERSION-OUTPUT、CONTENT-REGISTRATION-PERSISTENCE、CREATURE-FORM-LIFECYCLE、KERNEL-EXTERNAL-LOADER的准确主owner及必要原生命周期/交界已定向读取；局部producer→write→consumer→display→persistence明确区分内存、顺序dat/PBS、UI/缓存、玩家存档和失败前缀。局部候选签名不签整个共享主条款。

旧回归按准确owner/scope定向核对：B20/C024（方向/门/分阶段写入），B20/C034（十八参数与规则顺序，野外重访无退出），B03+B20/C051（原跟随/开关前缀），B20/C030（页面条件继承），B19/C021（IV/EV缺项0与地图宽0），101归并M05-005三消费者及A-R01/C022/B21有限补充。GR4-M04-001旧owner为R4-U03，仅C01–C05；Summary C01现行残余仍留U03/GR5-M04-002，不能因103通过将旧整ID转签。未变正文/测试按精确字节复用，旧PASS没有转作本轮证据。[完整限定回归](regression-results.json)。

原C12菜单323–366锚是构造测试入口，不能用于类型/道具编辑caller；本次101/102另实读1181–1188/1208–1215。此读取锚纠正及所有实际范围/文件身份见 [source-reading-log.json](source-reading-log.json)，未改冻结证据。

## 执行、依赖与登记限制

R4历史隔离参考执行 **4**、R5原review隔离参考执行 **4**、本update新增参考/行为模型/宿主/Demo执行 **0** 分列。前两者只复用准确有限原观察；001六输入、002十八两遍不称完整转换器或战斗运行。安全zlib解码、JSON/hash与补丁/字节重放、普通推送和完整读回属于TOOL_VALIDATION。全部新行为向量仍DERIVED_VECTOR/NOT_EXECUTED。

完整地图/事件、Graphics/Audio、原生宿主、真实UI/存档及任意组合的原缺口保持。optional7、no-required7、政策6及M11-005 optional方面没有纳入。

U01/U03/U06准确实际贡献及接受回执未提供，依赖门全部 WAIT。之后须 R5-I整合 → 冻结实际commit/tree及共享正文 → 非作者按actual-reviewer-entry定向复审 → 唯一登记。候选PASS不转到实际字节；本次正式接受0、CLOSED0。SC-U07-001供登记者处理，不另开全局review。

全部逐标准理由、范围排除与阻塞见 [criterion-results.json](criterion-results.json)；普通推送/新载荷完整读回的后继回执见 [review-manifest.json](review-manifest.json)。
