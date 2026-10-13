# R5-U03 独立候选有限复验 — round-02

**固定v2候选：11项限定 PASS（M01-006定向复验通过，其余10项按精确未变贡献复用round-01签名）。候选必需返修为空。** 本轮没有重开全局review，也没有重复其余10项语义审查。

**R5-U01实际接受依赖仍WAIT；actual字节未审，正式接受/CLOSED未授予。** 共享整文件不因某个贡献通过而接受，后续仍须R5-I实际整合、原非作者审者核实际commit/tree与唯一登记。

候选/作者证据 `d84bf0dd0eac4605c98d8ba4ae3f8502117fc5a7` / tree `c1b9497fc9d571b738ccbad3eaaf3a6584b98f41`。复用基点为独立报告 `0fd3fe285f4c726d736a7281f9949a5f3c91e0e9` / tree `8830d80fd553f76720e2f9c31bf5e9066c7595b2`；其[round-01失败记录](../round-01/report.md)保持原字节，本后继说明唯一返修门的恢复。B5/R/合同冻结身份不变，见[manifest](review-manifest.json)。

| 必修 | round-02裁决 | 审查依据 |
| --- | --- | --- |
| GR5-JXN-003 | PASS | 原限定签名，规则/向量/证据贡献精确未变 |
| GR5-M01-005 | PASS | 原限定签名；共享测试目录旧全文前缀保持 |
| GR5-M01-006 | **PASS** | 恢复段与3新增静态对照直接反查固定R及必要消费者/回归 |
| GR5-M04-001 | PASS | 原限定签名与枚举/解析/消费者规则未变 |
| GR5-M04-002 | PASS | 原限定签名与读取/重入链及旧向量未变 |
| GR5-M05-001 | PASS | 原邮件失败链/同步贡献未变 |
| GR5-M05-002 | PASS | 原融合/删除守卫及取消/许可贡献未变 |
| GR5-M05-003 | PASS | 原caller索引/快照/显示贡献未变 |
| GR5-M05-004 | PASS | 原参数全集、资格/赋值及回归贡献未变 |
| GR5-M05-006 | PASS | 原定义/数量/图标门贡献未变 |
| GR5-M05-007 | PASS | 原选择/转换/返回/失败前缀贡献未变 |

## 定向006结论

直接读取v2[WP18片段](https://github.com/y805939188/pokemon-essentials-clean-room/blob/d84bf0dd0eac4605c98d8ba4ae3f8502117fc5a7/review/remediation-fifth-20261013-prepare/candidates/R5-U03/author/fragments/deliverables/final-specification-set/creature-rpg/wp18-creature-identity-species-ownership.md.md)第5行，实际恢复了原被删除绑定：

- 给定形态（包括0）采用简单存储写入；该次不调用形态处理器、不登记图鉴、不清特性缓存，仍重算。普通创建自身的先前回调、随后特性索引覆盖清缓存分别观察。
- 随后持物/招式；显式列表存在且非空时按给定顺序逐个静默学习，否则按当前等级可达学习表重建默认招式。WP20§5.1承接去重/移至末尾、首项移除、重建末尾至多4项及满PP等通用细节。

固定R Trainer129–141、Pokemon181–184/625–659/1159–1225、RATTATA数据469–495直接支持这些规则，WP24第15行的原委托可继续承接。新覆盖表、普通创建/cache、IV/EV、Nature、后续hook可覆写及失败保留已写前缀均保持，不扩为所有入口/设施行为。

三个新增向量逐项PASS，均为**DERIVED_VECTOR / NOT_EXECUTED**：08限定简单写入后、后续特性覆盖前的中段，明确0也通过提供值门；09默认RATTATA L5显式[TAILWHIP,TACKLE]仅逐序学习这两招；10省略与记录空列表两个独立输入都重建[TACKLE,TAILWHIP,QUICKATTACK]，不把任意空白PBS行当合法格式。没有把中段缓存保证推广到全装载最终状态。

## 未变复用与派生核验

实际normative变化仅2目标：WP18上述段落与同一测试目录追加3行。52操作仅indices13/48变，31共享片段仅index1变；B5补丁/操作重放、8镜像、8共享文件/31片段和16投影目标一致。原66条完整向量对象和目录旧全文前缀不变，共69条静态未执行向量。

其余10项原finding记录、规则/证据贡献、完整向量及原独立criterion签名指针经比对符合精确限定复用；不只采信作者表，不据共享文件总hash授整文件接受。[逐项签名和复用证明](criterion-results.json)、[独立工具核验](independent-validation.json)均绑定新固定候选。

本轮502项TOOL_VALIDATION全部PASS。它们是字节、hash、链接、结构与重放检查，不是行为执行。原round-01的2处冻结历史SHA导航仍为MISMATCH；作者后继导航说明绑定两实际文件bytes/SHA256/blob与4个原记录指针/hash，已直接核实。其余17记录只按固定独立报告复用，新增核验0；未改冻结原文、旧owner/scope或旧状态。详见[限定回归](regression-results.json)。

## 边界与发布

候选返修已满足，不再新增返修要求或无限复审。remaining blockers只在实际阶段：R5-U01实际接受WAIT，之后的R5-I整合、actual字节复审与登记仍未执行。上游若实质改变本scope，才定向重审相应受影响部分。

原非作者任务 `/root` 与原语义/工具子审完成此次有限复验；任务UUID平台未暴露，未拿源thread/环境ID代替。请求gpt-6.1-sol/ultra/default普速禁Fast，实际模型/推理/服务参数回显均UNVERIFIED，未审计额度/认证。R4历史隔离执行4、R5review隔离执行4分别复用且未重跑；**本update新增参考/模型/宿主/Demo行为执行0**。无宿主、像素、真实存档、完整Demo或无界组合运行PASS；可选/政策范围未扩为必修。

只新增round-02独立review域，冻结round-01/作者/正式/公共登记保持原字节，未merge/push main、未访问Mac。普通推送至 `codex/r5-u03-independent-review-20261013`，精确新增载荷读回由[后继发布回执](remote-readback.json)固定完整bytes/SHA256/blob；其自身份由最终commit/tree外部绑定。阅读用的候选指向d84bf0d Git对象，工作树作者仍为原字节。
