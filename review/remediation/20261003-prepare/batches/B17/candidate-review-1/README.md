# B17 candidate-review-1：独立 FULL 复审

结论：**REQUEST_CHANGES**。完整 12 贡献／7 主责已复审；7 项主责局部最低验收静态满足，11 项局部贡献静态满足，GIR-FD82-003 因旧必要数据回归失败。合法写入、原稿授权及目录字节保护均不能替代质量通过。

| 身份 | 精确值 |
| --- | --- |
| reviewedSHA | `86bcafffbb2127c66b8636d10943cf702c18a557` |
| reviewed tree | `8626342ceeba125603aca6cac5b86b4e454a8ba0` |
| FIX_BASE B16-C | `f66366b2bbe5c3e1cdd39459f80be672173e7f94` |
| publication envelope | `d0effbf6e7cddb88482658f8c1b7616a9d5b4091` |
| dispatch contract | `82a824483b8abb165b67c275e500e332fd91344d` |
| 独立报告分支 | `codex/cloud-dot-B17-full-review-1-20261010` |

请求配置为 gpt-6.1-sol／ultra／default／Standard；无可信运行回显，按已批准 Plan A 记为 UNVERIFIED。未请求降级、fallback 或元数据／配额探针。未开额外任务。

## 阻塞与最小返修

1. **B17-R1，P2：WP76 §7.2 第165行把 `PLAYER1/PLAYER2` 改成 `PLAYE/PLAYE`。** B16-C 和固定参考 BattleSim 第382–383行分别保留两个完整名字；改写截断并合并了必要数据身份。恢复正式 WP76 的两个原名字，保留其它中立改写。
2. **B17-R2，P2：WP76 §7.4 第185行把固定算例 `双方 R1500/D350、σ＝0.9` 改成 `双方 /D350、σ＝0.9`。** 算例自己的评级输入被删除，而既有预期数值仍在。恢复双方评级1500的显式前提；可用独立文字，不需改变公式或重算向量。此处判前提丢失，未声称数值已运行验证。

两处均违反 003 净化时保留必要行为／输入的资格；与泛删 `R` 后数字的改写相符仅为 diff 推断。完整定位与 commit/path/blob/SHA256/字节身份见 [findings.json](findings.json)。获准 WP67-A/B 原稿已精确等于批准 after，不需因这两项返修修改原稿。作者应同步修订证据、冻结新候选和唯一完整流后再交复审。

## 全限定贡献判定

| 控制 | B17主责 | 局部静态结论 | 核心资格 |
| --- | --- | --- | --- |
| 003 | 否，B21 | FAIL | 非必要组织可移除；必要身份、固定输入、返回／共享副作用／失败必须保留 |
| 005 | 是 | 满足 | 合法3v3默认远4／近2／自身0；UI、登记与执行拒绝分层 |
| A040 | 否，B07 | 满足 | 默认合法双EV255/255、重复分母、正常培养252/510门分别保持 |
| A050 | 否，B07 | 满足 | 准备隐藏、首更新零缩放、52单位白剪影、成功闪光才恢复常色 |
| A059 | 是 | 满足 | 完整选择族、nil/空串、数组末非nil、引子记忆／计时器副作用 |
| B031 | 是 | 满足 | 手动Fight、有效Encore自动Fight、道具type4的BACK调用者分层 |
| B032 | 是 | 满足 | 可达Mega石或MegaMove；CTRL不绕前三门，实际进化在攻击阶段 |
| B033 | 是 | 满足 | 无活非自身同侧者才自身；确认可登记，执行再拒绝 |
| B034 | 是 | 满足 | 直接辅助访问失败与普通设施AI路径分开，概率／返回／校验保留 |
| C003 | 否，B21 | 满足 | 仅L09第三输入b→c，与正确原稿及三个期望一致 |
| C119 | 是 | 满足 | 动画更新→BACK→finished，同末帧仍可取消 |
| D018 | 否，B09 | 满足 | 前态收集、两计划顺序执行、双槽限制／同属主／早期终结完整 |

[contribution-review.json](contribution-review.json) 每项绑定完整原始、批准、当前根／扩展／资格／最低验收，不以标题或40个设计代替控制。所有非本批义务及 canonical OPEN 保留，局部静态满足不等于 C 接受。

## 独立保护与证据

完整未筛选 C→候选流由本次独立 `git diff --no-ext-diff --no-textconv --binary --full-index C candidate` 重建，逐字节等于封套唯一流：369630字节，20文件（5正式＋2原稿＋13作者证据）。封套另有4文件，无额外实质变化。流不复制到本报告。

不可变流引用：commit `d0effbf6e7cddb88482658f8c1b7616a9d5b4091`；path `review/remediation/20261003-prepare/batches/B17/candidate-1/C-to-candidate.full.diff`；blob `fa1d7c2d4255e005b285977e33421903085ee782`；SHA256 `a84c956e06b387ff163cefb8e52459883828336fe0c7f7e6ae98703b30d80343`。完整库存、端点及复建结果见 [metadata-verification.json](metadata-verification.json)。

85项机械检查全部通过，123个直接不可变项目引用独立核验；69个计划输入身份（67当前C＋2不可变原稿）、两份原稿整文件批准 after 都准确。36594个其它路径 mode/blob 保持；264项旧贡献／191触达／16已接受批次的统计和记录保持，229 OPEN／0 CLOSED。两本目录175／484个旧行的顺序、数量与其它属主字节保持；仅GN-M19、K08/K11/K42/L09允许旧行改变，反转这些改动并去B17新节可精确重建旧整目录。新增3＋37行和40设计逐条对齐，B16新增24行全部保持。**这些字节结果不消除 WP76 两项语义回归。**

40项为未执行静态设计。复审核对合法正例、相邻反例和旧回归；P003保留必要身份／旧行为的设计在当前正文未满足，见 [static-case-review.json](static-case-review.json)。没有 reference/game/Ruby、行为向量、生成器、旧脚本执行；无运行观察或真实Demo证明。

[affected-interface-assessment.json](affected-interface-assessment.json) 独立核对15个导航接口：B04/B05/B06/B07/B09/B16仍需各自候选 affected 门，后续 actual门独立；其余有具名NOT_AFFECTED理由。此FULL报告不代签其它角色、G、ACT或C。B18 FULL继续按合同等待B17 C远端读回。

27个精确固定参考文件字节身份及本次实际静态阅读范围见 [source-reading-log.json](source-reading-log.json)；既有否定检索按不可变证据复用，不冒称新遍历所有脚本／插件。完整U01–U10、G01–G12、AX01–AX20、conditional berry67及媒体／宿主／样本／Demo限制见 [source-limits.json](source-limits.json)。目录／原净一致性与旧贡献保护汇总见 [protection-and-consistency.json](protection-and-consistency.json)。

本目录仅签独立候选FULL结论。普通独立分支发布后须核对远端ref、commit tree和全部报告文件字节，最终交接返回实际reportSHA；[report-manifest.json](report-manifest.json) 列出报告文件字节身份，不自引用包含它的提交。
