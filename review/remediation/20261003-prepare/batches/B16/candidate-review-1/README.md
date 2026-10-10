# B16 candidate-review-1 — independent FULL24/20

判定：**FAIL**。24 项贡献中 23 项 PASS_SCOPED、1 项 FAIL；20 项主责控制全部 PASS_SCOPED。非主责的 GIR-FD82-C003 仍是 mandatory FULL 对象，因此不能以主责全部通过替代 FULL24 通过。

只评审固定 candidate `ae223d7bfb9ff6ed8a1ac153debb986115345957`，tree `7b3a16f86aea8438eceb007436687b72aced8e74`。FIX_BASE 为 B13-C `27185563f307e16d2612fa86e83b2c9bd772c79e`，tree `e44ed01586846bb42b03105dcc575d463df4ef49`。publication `5c70c6945ede498f1d7d59592da1d37a96c07a98` 仅供读取精确分派和发布回执，未作为评审后继。报告分支为 `codex/cloud-dot-B16-full-review-1-20261010`；写入仅限本新目录。

请求配置为 gpt-6.1-sol / ultra / default（Standard）。本委派会话未提供可信的有效后端回显，按当前合同记录 effective_backend **UNVERIFIED**；未使用降级、CLI/native fallback 或嵌套子任务。不声称已验证实际模型或服务档位。

## 阻塞 R-B16-F01（P2，GIR-FD82-C003）

固定 candidate 的 `deliverables/final-specification-set/test-catalog/user-interface-wp17-63-65-66-67-68-69-70-71.md:590`，B16-C003 新行写为：

> 上限50对照实际20来源30目标50

该行给定来源 hp50/totalhp120、目标非蛋非来源 hp30/totalhp50，并声明资格门成立。完整用量为 max(floor(120/5),1) = 24；来源先扣完整用量，得到 **26**；目标按缺口恢复 20，得到 50。因此正确静态预期为“上限50对照实际20来源26目标50”。目标恢复夹限不会把来源扣量缩为 20。

独立有界来源复核固定在参考 commit `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`：`Data/Scripts/016_UI/005_UI_Party.rb:1258–1281` 确认先扣来源完整用量；`Data/Scripts/013_Items/001_Item_Utilities.rb:333–338` 确认恢复只夹限目标。原稿 `specs/ui/wp66-a-party-and-summary-ui.md:78`、净稿 `deliverables/final-specification-set/user-interface/wp66-a-party-and-summary-ui.md:82` 以及旧 A23 正常例一致且正确。上述依据为静态源文本审查，没有执行参考程序或行为向量。

错误还存在于固定作者证据的 trace、catalog-preservation、catalog-row-edits、formal-clause-edits 和完整旧 payload diff 拷贝中；精确路径与 JSON pointer 见 [review.json](review.json) 的 blockers[0].secondary_loci。拷贝一致不构成独立质量通过。

最小修复范围：只将新目录 B16-C003 这一反向的来源 HP **30→26**；保留目标恢复 20、目标 50 及该行其它 A31/A33 分支。发布一致的新作者/候选后继证据，更新对应行、追踪、保全、hunk 拷贝及身份、完整 diff、精确分派。旧报告保持冻结。五份 scope3 原稿及原净 A§4.2 无需为此扩修；修复后的新精确候选仍须独立 FULL 和必要 affected。

## 完整验收矩阵

各项完整的合法前提、正常静态正例、最小反例、相邻反向、旧回归、原净正文/资料附表/目录/追踪一致性及非局部义务列于 [review.json](review.json) 的 per_ID_results。下表是索引，所有 ID 均以 GIR-FD82- 为前缀。

| ID | 主责 | 判定 | 独立验收要点 |
| --- | --- | --- | --- |
| 003 | 否 | PASS_SCOPED | 净化组织限制；三模式输入、返回和六面板几何保留 |
| 004 | 是 | PASS_SCOPED | 持物交换后仍持目标物；BACK 拒绝及空格放置分开 |
| 006 | 否 | PASS_SCOPED | 暂停与导航图标各自周期、绝对相位和首帧 |
| A015 | 是 | PASS_SCOPED | 已读数据为空/非空的三个入口守卫及旧 SV02/MG03 |
| A044 | 是 | PASS_SCOPED | 默认 TM57 的 TR、兼容性、双入口教学/删除/重学闭环 |
| A048 | 是 | PASS_SCOPED | 合法空重学首绘失败时点与非空取消/教学对照 |
| A055 | 否 | PASS_SCOPED | 零结果 Start/Cancel 与结果页 BACK 的持久模式写入 |
| A056 | 是 | PASS_SCOPED | 两个可见计数与完成图标的长度比较 |
| A058 | 是 | PASS_SCOPED | 128 方图与单行盒图、多消费者相位及资源失败边界 |
| B035 | 是 | PASS_SCOPED | 双槽部分加入失败后的真实回退、数量和交易资源 |
| C003 | 否 | **FAIL** | 奶招上限反向错误；A31/A33 其它修复有效 |
| C058 | 是 | PASS_SCOPED | 共享记忆 BGS 的二次 SE 缩放与查询副本对照 |
| C114 | 是 | PASS_SCOPED | 启动/标题/帮助淡入淡出名义请求、次序及首绘 |
| C115 | 是 | PASS_SCOPED | 五档尺寸映射、首次初始化、越界保存值与宿主边界 |
| C117 | 是 | PASS_SCOPED | 排序取消恢复次序/当前项，保留此前存储索引 |
| C118 | 是 | PASS_SCOPED | 个体/物种/物品图标帧、偏移、HP 档及空物品消费者 |
| C120 | 是 | PASS_SCOPED | 盒背景存储/显示两口径、锁定、缓存及退出不回滚 |
| C121 | 是 | PASS_SCOPED | en_US 身高体重换算、两页面舍入及原始筛选值 |
| C122 | 是 | PASS_SCOPED | 结构可用先于已见、形态1性别三例、排序与标签 |
| C123 | 是 | PASS_SCOPED | 完整37+37离散刻度、上下界状态和确认焦点 |
| C124 | 是 | PASS_SCOPED | 六 IV 顺序、PID 同最大决胜、30 性格描述和隐藏门 |
| C125 | 是 | PASS_SCOPED | Box Link 后旧源索引造成部分写入及首绘失败；取消对照 |
| C126 | 是 | PASS_SCOPED | 空招式普通页/详情/遗忘/事件入口分叉和通用教学对照 |
| D023 | 是 | PASS_SCOPED | 展示数量×半价与真实交易金额；奇数及零展示反向 |

完整控制入口来自固定 packet `8e2753430ccb4bad8098048c814576aa386a09ef`：完整 downstream contract、original-and-acceptance-controls 及 effective-case-constraints。24 份完整原始 finding、24 份完整已批准 acceptance、当前根/扩展/最低验收/全部贡献角色和 12 份 effective 聚合均已读取，逐对象身份、完整值和字段关系独立核验。scope3 `bd14b2170085fdb491c01f633c9e9d794c723c3c` 仅授予五原稿有限替换范围，不能代替本次五原稿和六净稿的质量判定。

## 完整差异与保护核验

新元数据核验 [verify-metadata.py](verify-metadata.py) 得到 **586/586 PASS**，完整结果见 [metadata-verification.json](metadata-verification.json)。该程序只检查 git 对象、文本、JSON、身份、范围和保护关系；未执行旧作者/reviewer/preparation 脚本或参考程序。

- [complete-FIX_BASE-to-candidate.diff](complete-FIX_BASE-to-candidate.diff) 是无路径过滤的完整 `git diff --binary FIX_BASE candidate`：2,248,505 字节，SHA256 `f8012172e5751ba620d9ddd37793382f9128973ba2331fef187575adbbf7fd7b`。完整流为 78 个文件：11 个既有输出修改（五原稿、六净稿）和 67 个新增本批作者/候选证据；已逐文件核验完整块及身份。
- scope3 的五文件、20 个唯一控制、21 个 ID/文件组和 28 条有限替换均精确匹配；独立按完整文本补丁一次应用后的结果等于 candidate。没有执行旧补丁脚本。
- 六净输出与固定先前作者版本相同；既有64个作者物理产物及23个 BASE B16行政文件均保持；除授权11输出外所有 BASE 既有文件逐 blob 保持。正式/public/main/reference/旧报告未改。
- BASE 的240个已接受唯一(batch, ID)贡献回执完整枚举并保持字节，及其既有输出保护独立核验。这是版本准确的保护证明，不重授240项语义 PASS，也不代替其它 affected 角色。
- 旧目录460行的 ID、顺序、重数保持；451行字节保持，9行仅本批分派必要修改；24个新增行均进入完整质量判断，发现 C003 阻塞。旧 C29 等邻近回归未被改写。
- 固定先前33份参考文本/范围证据的身份独立复核；只增加10个必要有界来源/条件复核，见 [source-supplement.json](source-supplement.json)。未进行全历史或递归来源审计。

## 保留限制与后续门

继承 U01–U10、G01–G12、AX01–AX20、条件 berry67 以及完整 named-unread 清单，未扩大豁免。二进制/序列化资料、宿主及媒体资源、真实地图事件、插件/动态分派、完整 Demo 链等仍未证明；完整继承值在 review.json 中保留。runtime observations = 0，proven Demo chains = 0。静态设计、来源审查与元数据核验均不称为运行测试。

本报告只签本精确 candidate 的 FULL。未签 affected、G、ACT、C 或正式接收；canonical 保持 OPEN。有限修复和精确 refreeze 后仍需 mandatory candidate FULL 与独立必要 affected；之后才由唯一 G 登记，ACT 的 FULL/affected 各自完整消费 FIX_BASE→ACT 与 candidate→ACT 两流，最后由唯一 C 在所有必需门通过后判断。非局部贡献和全局闭合义务保留。

## 报告发布证明

本目录文件身份收录于 [artifact-manifest.json](artifact-manifest.json)。普通报告提交推送后，独立读取远端 ref、tree 及全部报告文件字节；第一份提交的回执收录于后继新增 remote-readback-1.json。最终远端 head、tree 和包含回执的全部报告字节再独立读回，完整最终报告 SHA 在委派返回中给出。回执自身的提交身份不写入自身，避免循环绑定。
