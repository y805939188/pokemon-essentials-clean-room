# 正式规格去向清单

当前为 **R3 累计来源校准及作者返修候选，等待真正非作者 ultra/default 独立复审**。9 批正式 ACCEPTED 来源已经应用到 `5f87743293290de2e219ecdd6c19e88280f60c9a`（正式树 `93dc967b4cdb653359afc123d3b8b318d6475fdd`）。131 份正式文档身份已核，当前 2704 个标题全部映射，含相对历史新增的 21 个标题；230 个整改绑定全部回填，待核与部分回填均为 0。39 项来源接受为 29 required＋10 optional，CLOSED 仍为 0。来源接收不代表目标去向、实现或全轮验收通过。

固定历史来源为 `fd1df570cad987dc3852a3b958f03916e317f7fe`，R8 交付为 `4575e80d041ab0c74a42e2e36399d05791dbaa5b`，两者正式子树均为 `f292698cdd4a8e725525a9be6dc34b75faaf151e`。本打标分支正式正文继续保持这份 B8 树；当前接受源码从固定 Git 对象读取，不能用工作区 B8 字节代替 current5f。不可变 `source`、全部稳定 ID、完整退役历史与历史 2683 标题覆盖保留。

## 明细与证据

- [机器主清单](routing-manifest.json)、[Schema](routing-manifest.schema.json)、[验证与生成器](routing.py)。五类去向是框架实现、Showdown承担、框架与Showdown协作、MZ接入与表现重建、不纳入目标。
- 逐行视图：[内核](views/generic-kernel.md)、[生物](views/creature-rpg.md)、[宝可梦](views/pokemon-rules.md)、[战斗](views/combat-requirements.md)、[世界](views/engine-overworld.md)、[界面](views/user-interface.md)、[制作/示例](views/demo-dx.md)、[元数据及旧 ID](views/metadata.md)。来源事实和未来方案分栏，包含具名职责、直接依赖、有效范围及父子导航。
- [历史章节覆盖](section-coverage.json)、[当前接受章节覆盖](current-section-coverage.json)、[当前可读覆盖](current-coverage.md)、[覆盖统计](coverage-summary.json)。历史与当前是分别保存的定位证据；131 文档、87 WP 只是当前索引观察值，不作为固定分母限制后续变化。
- [R3 交接](revisions/r3/README.md)、[7 项问题映射](revisions/r3/finding-resolution.json)、[28 行依赖逐边处置](revisions/r3/dependency-repairs.json)、[736 行处理](revisions/r3/feature-resolution.json)、[44 组历史信用与传播](revisions/r3/retained-pass-propagation.json)、[逐 facet 继承限制](revisions/r3/facet-inheritance.json)。
- [38 文件差异重估](revisions/r3/source-file-reassessment.json)、[51 个直接变源单元](revisions/r3/feature-source-deltas.json)、[21 新标题显式消费者](revisions/r3/new-heading-mappings.json)、[39 项源接收](revisions/r3/issue-source-reception.json)、[阅读范围](revisions/r3/source-reading-scope.json)、[94 份 R2 复审输入消费](revisions/r3/review-input-consumption.json)。
- [实际 10 命令 I/O](revisions/r3/tools/actual-command-io.json)、[最终 15 项校准证据](revisions/r3/tools/final-calibration-proof.json)、[接受事件](accepted-source-updates.json)、[回填合同](backfill-contract.json)、[交接状态](handoff.json)、[未决边界](unresolved-boundaries.json)、[新独立复审入口](review-prompt.md)、[候选文件身份](candidate-file-manifest.json)、[相对 R2 的精确文件差分](revisions/r3/changes-from-r2.json)。

## R3 具体变化

R2 固定候选 `a32873d2860b15d9f5e27727db8f131f4ec433b6` 的独立 FAIL 报告为 `0ef0b7ad5f9465cfe31da0d7a35f56b5ccba5add`。其 7 项问题由作者修正：4 组/28 行的依赖指向按实际有效源区间修复，3 项来源工具门补强。原分类/职责/范围 PASS 是有限历史信用，不能由字节保全推定错误依赖也有效。

接受来源另使 6 行职责/依赖精化：645/647 的普通移动与跳跃末端门、92 的纹理直调评分和普通 User/0 不消费、397 的蛋群固定目录及消费者、699/703 的语言图像身份/失败前缀。去向类别保持不变。51 个相对 B8 直接文本变化单元补独立来源差异证据；合并补丁涉及 78 行/162 字段，可由接受后归档与逐字段 before/after 重建整个主清单。修正脚本没有修改 source、current/upstream、类别、阶段或实现状态。

当前 736 活跃行、33 完整退役行与33 元数据；去向数量为框架 307、Showdown 74、协作 130、MZ 225、排除 0。全部736行去向待验证、阶段待定且未批准、未实现、未验收。纯责任表/来源/静态向量属于元数据，不构成待实现功能，也不塞入“不纳入目标”。

## 核验与限制

最终 `cumulative-source` 阶段10命令全部 exit0，17个登记输入哈希全程稳定：27结构负例、9自检、2导航负例、11生成物一致、19保全检查、5接受绑定负例、2704当前覆盖及4负例、4个来源门隔离夹具（覆盖3项工具问题）通过。显式导航为36父/39子/39边。58份R1/R2历史工件原字节保留。它们是作者静态检查，尚未给出独立语义复审 PASS。

首次累计应用沿当时旧代码后暴露1776个显式null理由，初次失败、原代码gzip及后续归一化均保留；现行工具在写核心/归档前验证完整prospective输出，并拒绝旧回执授权后继未接受字节、普通行为标题借治理标签逃过空消费者等输入。[工具逐项记录](revisions/r3/tool-finding-resolution.json)区分初次失败与最终通过。

标题/身份全集机械核对、完整差异阅读、源章实读与目标去向验证是不同口径。35份完整差异复用此前完整阅读并逐文件/补丁验证字节相等；重读U02/U03两处差异与UI65最终修订，另定向实读问题源与目标有效单元。没有声称本轮重新逐句全文审完131篇，也没有把解析JSON或列标题当语义全文阅读。

捕获、背包战斗道具、逃跑、战中成长仍为协作原型候选；先固定目标Showdown commit/格式，再分别核持久/战斗临时状态、随机/记录、UI/宿主和异常前缀。AI策略、实际查询、共享准备写入及登记不能互相代替。公式/数值一致、来源引文或源静态PASS都不能证明兼容。Ruby、参考游戏、业务向量、宿主、Showdown/框架原型均未运行，没有实现新框架。

Shadow、设施、独立玩法、调试/作者工具、XP工程/旧格式与首版/后续仍需用户范围决定。只有明确用户范围决定可支持排除；暂缓不等于不纳入。根AGENTS和用户[clean-document-revision技能](../../../review/global-independent-review/eighth-2026-10-16-fd1df57-c84e/inputs/review-SKILL.md)适用。xhigh/default主任务创建请求与原生子代理配置证据分层，无权威执行echo的model/effort/tier/speed/Fast仍逐字段UNVERIFIED。

## 静态入口

```bash
python planning/implementation-routing/r8-20261017/routing.py validate
python planning/implementation-routing/r8-20261017/routing.py check-generated
python planning/implementation-routing/r8-20261017/revisions/r3/tools/run-author-checks.py --phase cumulative-source
```

接受接收/prepare/apply入口为 `revisions/r3/tools/backfill-accepted-sources.py`；精确参数与真实输入见工具I/O。旧seed入口拒绝重建，R1/R2迁移脚本与旧阶段结果只作固定历史，不能重跑覆盖已累计接受状态。新候选由父线程给40位SHA，再另建真正非作者gpt-6.1-sol ultra/default累计复审。

21条新标题来源证据的标题hash保留`SHA256_UTF8_TITLE_ONLY`口径；current定位使用的原Markdown标题行hash单列保存。原映射字节与初sourceapply I/O匹配并已归档，初次口径探针与修正见[记录](revisions/r3/tools/new-heading-hash-convention.json)；这是证据口径显式化，不改标题/消费者或核心17输入。
