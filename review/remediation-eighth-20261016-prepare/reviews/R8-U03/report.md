# R8-U03 独立候选复审

结论：**candidate PASS（有限静态范围）**。唯一必修 `GR8-PBSW-001` 的无依据多数表述已被准确的五个具名样本替换；没有发现本次修订引入的新矛盾或候选阻塞项。**actual integrated review = NOT_STARTED；ACCEPTED = false；CLOSED = false。** 本报告不宣称正式接受，也不验收同提交中的 R8-U02。

## 固定输入与独立性

| 输入 | 固定身份 |
| --- | --- |
| 候选 commit | `8b69bca8bf9141276425a963f350b19048bb2b51` |
| 候选 workspace tree | `98c3f3ad5d091c4fc9980ffe9f8375a7e3a51156` |
| 原审查基线／候选唯一父提交 | `4575e80d041ab0c74a42e2e36399d05791dbaa5b` |
| 基线 tree | `e8fb0884694afee309c57504babf9f849a5f1498` |
| B8 | `fd1df570cad987dc3852a3b958f03916e317f7fe` |
| 原版 R／tree | `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`／`7589c800b61ba13a13040ed0d686979b80a84fd0` |
| R8 语义 core | `2460370f1e410bd49cc29e377b89662838aed2b3` |

候选镜像：`review/remediation-eighth-20261016-prepare/candidates/R8-U03/mirror/deliverables/final-specification-set/pokemon-rules/wp60-berry-plants.md`；mode `100644`，blob `43e55f00e3c3c6215e9a0ad50e953a7fdedf3ae1`，22,638 B，SHA256 `376f8c943441efeebfa4073b2c6e862e7d2c9eb0644db4b828f4781cff4035f2`。

本 reviewer 是本次单独委派的非作者 context，逻辑入口 `R8-R-R8-U03`；未写作者候选、正式规格或公共台账。作者来源线程为候选 change-record 中的 `01a13f49-a154-7054-9b04-ce31f924d01c`。用户明确本云任务创建请求已选择 `gpt-6.1-sol / ultra / default`；未获权威运行时逐字段 echo，actual model/effort/tier/speed/Fast 均保留 `UNVERIFIED_NOT_EXPOSED`，没有重复 CLI 配置探针。

并行只读核对使用两个真实独立助手入口 `/root/berry_source_countercheck`、`/root/u03_contract_history_countercheck`，创建参数均显式为 `gpt-6.1-sol / ultra`。它们未替根 reviewer 签整批结论；同一结论不按两个助手累加独立验收票。根 reviewer 自行接收完整本批合同、镜像整文件、源证据和保留范围。

## 逐项证据、最强反方与判定

| 检查 | 原版／候选定位与独立证据 | 最强反方及处理 | 判定 |
| --- | --- | --- | --- |
| GR8-PBSW-001：去除多数 | R `PBS/berry_plants.txt` 全部 336 行／67 唯一完整记录，仅 CHERIBERRY、CHESTOBERRY、PECHABERRY、RAWSTBERRY、ASPEARBERRY 匹配 3h/15/2..5，各在 3、8、13、18、23 行开始。镜像 WP60 §3.3 L45 明列五个简称，三元组正确。 | “样本”可能只指任意例子；但旧文没有可支持多数的小分母。候选消除了频数断言。合同允许仅列具名样本，无须把整套统计搬进正文。 | PASS |
| 完整分母与反例 | 独立遍历全部五份 PBS：默认及 Gen6/7/8 为 5/67，Gen5 为 5/64。每条三字段均显式存在，无重复 ID/字段。五份 RAZZBERRY L78–81 均为 2h/35/2..10；默认 13 组组合详见 verification.stdout.json。 | 单个 RAZZ 不能反证“多数”；否证依据是完整计数。备份文件不是五次运行样本，也不证明世代配置自动切换。 | PASS |
| 缺字段、缺记录与格式 | R `010_Data/002_PBS data/007_BerryPlant.rb` L13–17、28–34；`010_Data/001_GameData.rb` L99–105。镜像 L45 的字段域、L48 构造 3/15/2,5 缺省及倒序交换、L49 未知 ID 报错、L177 明确“缺省”均原样。 | 真实构造缺省不能证明现有 PBS 多数；具名样本也不改变缺字段规则或提供未知 ID 查询兜底。 | PASS |
| CHERI 与干涸边界 | R `012_Overworld/006_Overworld_BerryPlants.rb` L21–49、83–165；镜像 §5.2、§7；目录 BP02/BP05。初种新机制、水100、无覆盖物/浇水、正常结算6h：阶段3、水10、惩罚0。第7小时到−5且惩罚0，第8小时才惩罚1；10h 为阶段4/−5/3。 | 不能据无覆盖物向量外推旧机制、覆盖物、重植或真实会话；本报告均维持明确前提。Python只做独立算术，不执行原版。 | PASS |
| 累计回归保留 | 镜像 §1–13 共199行全文与基线对照，只有 L45 一次文字替换，其余字节完全相同。目录 BP01–20、R5-BP01–04 共24个原 ID 和整文件字节均与基线/B8一致。 | 字节相同本身不证明正确，因此另核构造、时间/产量、取消与采摘源码及24条本批场景；没有发现与本次澄清冲突。 | PASS |
| 取消／部分提交／采摘等待 | R 同脚本 L308–471；镜像 §6.2–6.4、§8–9。未选覆盖物即取消不消耗；已施肥后取消保留地块覆盖物且不回滚库存。采摘先取定qty，容量门前不提交；成功统计→加入→消息→A→返回真→外层reset；等待可推进时间，拒摘/满包不撤回已完成更新，直接工具不reset。 | 不能把“保持不变”扩大为等待中植物绝不变化；原 R5-BP01–04 前提和异常前缀仍保留，没有因样本改名改写。 | PASS |
| 覆盖物、旧机制与数学 | 镜像 §5.1–5.4、§7；R update、water、yield、显示调用者完整单位。DAMPMULCH 的15→7/14→7/1→0，15h成熟向量、旧对象显式结算门、雨浇水、重植清零、两套产量式全部保留。 | 不把原注释的旧机制装图更新当作实际调用保证；不把非负干燥值数学除法误换成7.5或水分夹零。 | PASS |
| 引用与去向 | 镜像章节、现有相对链接、测试 ID 全不变；链接按正式目标目录解析有效。`audit/source-traceability.md` T-WP60-01（L755–766）、`planning/feature-matrix.md` F14-03（L235）仍指向树果 Pokémon Rules／WP60-B。WP02 §6.2/§7 的备份手动启用与组合未验证范围保持。 | mirror 是部分镜像，不能要求其物理目录含全部相对引用目标；检查的是实际目标去向。频数澄清没有创造新框架归属，`full_tagging_performed:false` 仍真实；本报告不给全量去向打标通过。 | PASS |
| 修改边界与证据资格 | 基线→候选只有 U02 两文件、U03 两文件及协调证据共5项新增；AGENTS、原报告、specs、planning、audit与全部正式 deliverables 未改。U03 的全部候选库存仅镜像及 change-record 两文件。三阶段正式树均为 `f292698cdd4a8e725525a9be6dc34b75faaf151e`。 | 同 commit 有 U02 不能视为本批接收；协调 checks 也不是独立语义证明。作者 broad_companion_reception 的待核说明由本次实读接收，不据此追授作者全域 FULL。 | PASS |

## 完整合同与历史资格

已接收 AGENTS、review-SKILL、两份完整批次 prompt、完整 readset 导航、assignment U03、`contracts.zh.json#/records/7` 全七组，以及 accepted-facts/history/policy 三份完整伴件。`review-SKILL.md` 明确不用于评审报告；本次仅据它检查候选原位修正、保留正确范围，未使用它修改规格。

最终 prompt 中嵌入的 assignment 与完整合同逐对象与正式 handoff 完全一致。原 5caff 恢复合同的 `seven_groups` 与最终合同业务意义相同；差异是冻结/历史接收状态及关闭门后继。保留 original 5caff 身份与 C35 recovered_at 双身份，没有把原裁决一律改称 C35 首次产生。`findings.json` 的 U03 完整根记录及 `root-final-history-and-canonical-reception.v1.json` 对应 canonical 记录确认 required/P3、无语义前驱、`DISTINCT_WITHIN_RECEIVED_SET`；不据此宣称全历史首次新根。

accepted-facts 的 false/nil 持物、mail、pinch berry facet 不在本批树果种植频数修订中采用，故不拉入外域12源单位作为本批新义务。history 中 R7 的42任务ID/12实际审者及 WP39 多阶段身份资格、policy 中未选 optional/视觉政策、14有限 NO_REQUIRED 与4 binary负例均原样，不转授成本批或全局 PASS。旧 PBS 摘要 alias 未决仍保留原非阻塞资格；本次新静态解析有自己的工具记录，未补写旧过程的 I/O 或身份。

## 范围、执行与后续依赖

本次语义范围是 U03 全合同、完整受影响 WP60、全部相关树果源/数据与24条保留向量。跨WP测试目录以 BP、R5-BP 为本次语义验收单位，其余工作包只有导航/身份或上下文信用；旧审者 FULL 不转授。本批无 optional，也无必须先完成的其他语义编辑。

`verify.py` 已实际执行 exit0；真实 argv、UTC、exit、stdout/stderr 分别保存在 verification.operation.json、verification.stdout.json、verification.stderr.txt。它只读取固定 git 对象、解析文本、核验身份/字节及计算有界独立算术。没有执行 Ruby、游戏、编译、宿主或真实存档/媒体观察；静态频数、算术向量、工具校验分别记账。

剩余候选修正项：**无**。剩余正式门：R8-INTEGRATOR 冻结实际整合 commit/tree；真实非作者重新全文接收实际 WP60 及累计保留/必要公共贡献；之后由父任务/主审登记 ACCEPTED/CLOSED。公共索引是否登记本次贡献由整合者依实际发布约定处理；章节/引用/归属本身没有必须修改的结构变化。

输出分支 `codex/review-r8-u03-20261017-8b69`，仅增加本目录的复审证据，普通提交和 push；输出 commit 由最终交付消息与 git 历史给出，避免报告自引用未来 SHA。整合协调任务 `01a14a04-b178-7567-a4eb-0f0bfac9a0d9` 由父任务传递结果。
