# B16 candidate-review-2 — 原 FULL 角色增量复核

当前明确结论：**PASS_SCOPED，FULL24/20 通过**。24 项贡献全部 PASS_SCOPED，20 项主责全部 PASS_SCOPED，剩余本角色 FULL 阻塞 **0**。原 R-B16-F01 已在本精确 NEW 解决；C120 按实际增量重新判断通过，未用 OLD 的 PASS 或 scope4 许可代替质量判断。

| 固定对象 | 完整 SHA / tree |
| --- | --- |
| reviewed NEW | `356b46b320884e57e71a1cab8413e13594524a7d` |
| NEW tree | `344b606d8368eb09dc9313e09fdda1fa227e6f39` |
| reviewed OLD | `ae223d7bfb9ff6ed8a1ac153debb986115345957` |
| OLD tree | `7b3a16f86aea8438eceb007436687b72aced8e74` |
| FIX_BASE B13-C | `27185563f307e16d2612fa86e83b2c9bd772c79e` |
| publication（只读入口） | `7585b16a65338392af8ff78e7d8a8cb23cd19901` |
| 本角色原完整报告 | `458f4f207266154021340c09d949f7863c358df2` |

评审目标是 NEW，publication 仅供读取精确分派、完整流和发布证据；作者 moving branch 不替代目标。报告分支 `codex/cloud-dot-B16-full-review-2-20261010`；写入仅限本新 candidate-review-2 目录。请求 gpt-6.1-sol / ultra / default（Standard）；会话无可信有效后端回显，按当前分派保留 effective_backend **UNVERIFIED**，未 probe、降级、fallback 或创建子任务。

## 完整流及真实影响

独立重现并完整读取两条未过滤流，全部顶层 diff block/路径进入核验；没有用三行 payload diff 替代完整输入：

| 流 | 字节 | 文件 | SHA256 |
| --- | ---: | ---: | --- |
| [OLD→NEW](complete-OLD-to-NEW.diff) | 4,453,488 | 49 | `b35f926522bbeefb7873a8cd10efacf9f6b83f858bb4faa3c7c2df24c86beb91` |
| [FIX_BASE→NEW](complete-FIX_BASE-to-NEW.diff) | 6,692,823 | 124 | `d2504fc7d646b54b38c913586b4de12a426e05c9cf4715c1dacb7b2b9b05293b` |

OLD→NEW 是三个既有文件各改一行，加46个本批作者/候选证据文件。实际行为约束只改奶招目录反向预期，以及原净墙纸条款的条件范围；其它新增证据包含中间部分状态、scope4提案/申请、应用回执、原发布入口、两修复的后继资料和当前完整 manifest/trace/hunk。历史 partial/pending 和旧错误文本保持冻结，当前完整 manifest、current original whole results、current clauses 和 corrected C003 evidence 精确覆盖它们；没有把历史状态当作当前阻塞或当前预期。

FIX_BASE→NEW 为11个既有输出修改（五原稿、六净稿）和113个本批新增证据。当前十一实物的完整 blob/SHA256/字节均独立核验；八个其它输出与 OLD 完全相同。所有 OLD 既有36,417路径中，仅三个授权输出变化，其余36,414路径 mode/type/blob一致；全部 BASE 既有路径除十一输出外也保持。已接受 WP25 整文件保持。

## C003 / R-B16-F01

当前目录 `deliverables/final-specification-set/test-catalog/user-interface-wp17-63-65-66-67-68-69-70-71.md:590` 只将“上限50对照实际20来源30目标50”改为“上限50对照实际20来源26目标50”。独立完整目录比较确认，仅这一处替换，其余目录字节全保持。

合法前提是可用奶招来源非蛋 hp50/totalhp120，目标非蛋、非来源、非濒死 hp30/totalhp50，菜单资格与正常资源成立。完整用量24先扣来源，来源50→**26**；目标缺口20，目标30→50。目标恢复夹限不会减少来源扣量。对照目标total120时恢复24→54、来源26；目标total40时恢复10→40、来源仍26。来源 hp≤24、目标自身/蛋/濒死/满血分别在守卫拒绝，不发生本次使用写入。

自己原 FULL 的固定 Party 1258–1281、Item Utilities 333–338 静态来源证据经整 blob 和范围身份重核后复用；原净 A§4.2 及旧 A23 正常例保持正确。当前 corrected C003 trace、catalog-row-edits、catalog-preservation 和当前完整 hunk 与修正行一致；旧30证据有明确冻结前驱与覆盖关系。A31互异三候选/交集去重、A33健康蛋拒绝/非蛋反向、旧回归及非局部8类扩展未被这一数字修改扩大或重签。

本角色结论：**R-B16-F01 RESOLVED_FOR_EXACT_NEW，C003 PASS_SCOPED**。

## C120 新条款及不回归

原稿 `specs/ui/wp66-b-storage-and-pokedex-ui.md:217` 与净稿 `deliverables/final-specification-set/user-interface/wp66-b-storage-and-pokedex-ui.md:217` 的新墙纸片段完全一致；搜索模式和末次形态写回前缀、盒5等正常例及其它入口尾部逐字保持。

独立有界回查固定参考 `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b` 的 UI Storage 378–397、Pokemon Storage 101–106，并读取已接受 WP25 §3.4/兼容附表75–98。正常显示结果要求基础储存、正常初始化、对应素材可用且无插件替换；既有/手工异常记录只是静态边界，不声明正常游戏写入者或 Demo 可达。

| 静态具名记录 / 前提 | 当前质量判断 |
| --- | --- |
| 零基盒5，整数16已锁/未解锁 | 实际不可用，显示和记录改5；盒2同前提改2 |
| 可用整数3；已解锁16 | 保持对应编号；不是任意“非法”编号均回写 |
| 旧 `box3` | 先写整数3，再按实际可用性决定是否默认；此例保持3 |
| 旧 `box16` 且16已锁 | 先写16，再因不可用写5；不省略先转换这一写入 |
| nil / 空串 | 默认显示5，背景记录保持原空值；不能与不可用整数合并回写 |
| `box2`、`box2`后接LF、`prefix`+LF+`box2` | WP25首个完整匹配行均识别并写整数2；同一行 `box2x` 不匹配 |
| 既有/手工非匹配 `box3x` | 数值比较先失败，早于默认背景回写、旧图处理与素材加载；不能宣称归一后成功显示 |
| 默认16下既有/手工整数−1 | 实际可用性通过，无默认背景回写；尝试对应素材，存在/加载结果仍未证 |
| 正常已发生读取写入后退出 | 不回滚；缓存与当前记录确实相同才跳过重取，空值默认显示不等于空记录 |

这分别保留可用性、旧格式匹配、背景记录写入、显示请求、失败前缀和未证素材边界，满足完整当前 C120 根/最低验收/effective 条件；未要求未来实现沿用参考组织。B16-C120旧正常目录行、Wallpaper命令、当前盒切换及B14/B15守卫保持。共用217行中的搜索Start/Cancel、末次形态写回描述保持，A055/C122/C123无回归。

scope4 `cc14f356dfc30eb7d27d4c5684f738867a64b0d5` 只授权一原稿、一控制、一条款；独立按完整文本补丁在内存应用一次，结果精确等于授权after和NEW。scope3其余27替换效果和其它原稿字节保持；未执行旧应用脚本。scope4是范围许可，不是本次质量通过依据。

本角色结论：**C120 FRESH FULL DELTA PASS_SCOPED**。这是本 FULL 对相关修复的独立质量判断；没有代签 B06 affected 或宣称其 NEW 门已经通过。

## FULL24/20 全量当前结论

完整24原始/批准/当前控制及12 effective聚合均与自己原FULL所用固定 packet `8e2753430ccb4bad8098048c814576aa386a09ef` 逐完整对象/全部字段/值身份匹配。根、扩展、最低修订、确定复核及全部贡献角色/非局部义务保持，不缩减为两个 finding。其它22项复用原完整合法前提、正反例、旧回归和一致性判断，但每项都有独立 actual-delta/protection 依据；共用B文件的当前整 blob 绑定也已更新。

所有 ID 均以 GIR-FD82- 为前缀；逐项完整前提、正例、最小反例、相邻反向、旧回归、原净/附表/目录/追踪一致性以及复用理由见 [review.json](review.json)。

| ID | 主责 | 当前判定 | 增量依据 |
| --- | --- | --- | --- |
| 003 | 否 | PASS_SCOPED | 新限定仍中立；模式、返回、几何与净化要求保持 |
| 004 | 是 | PASS_SCOPED | 持物交换/取消/空位条款及行保持 |
| 006 | 否 | PASS_SCOPED | 两图标周期、相位、首帧保持 |
| A015 | 是 | PASS_SCOPED | 启动守卫、SV02/MG03保持 |
| A044 | 是 | PASS_SCOPED | 双入口TR闭环保持 |
| A048 | 是 | PASS_SCOPED | 空重学首绘/非空对照保持 |
| A055 | 否 | PASS_SCOPED | 共用搜索写入前缀及持久模式分叉保持 |
| A056 | 是 | PASS_SCOPED | 区域两个计数保持 |
| A058 | 是 | PASS_SCOPED | 图标资源表/消费者/周期保持 |
| B035 | 是 | PASS_SCOPED | 袋部分加入回退及交易资源保持 |
| C003 | 否 | PASS_SCOPED | **新合法扣量判断及全部后继证据一致** |
| C058 | 是 | PASS_SCOPED | BGS共享记忆/二次缩放保持 |
| C114 | 是 | PASS_SCOPED | 标题/帮助名义请求及输入次序保持 |
| C115 | 是 | PASS_SCOPED | 五档尺寸和越界保存值保持 |
| C117 | 是 | PASS_SCOPED | 排序取消与存储索引保持 |
| C118 | 是 | PASS_SCOPED | 图标帧、偏移、空物品消费者保持 |
| C120 | 是 | PASS_SCOPED | **新条件及失败前缀独立重核，旧正常例保持** |
| C121 | 是 | PASS_SCOPED | 换算/舍入/原值过滤保持 |
| C122 | 是 | PASS_SCOPED | 结构/已见/标签及共用末次形态写入保持 |
| C123 | 是 | PASS_SCOPED | 37+37表、导航和共用搜索写入保持 |
| C124 | 是 | PASS_SCOPED | IV/PID/30描述保持 |
| C125 | 是 | PASS_SCOPED | 正常背景前提下旧索引部分写入/失败保持 |
| C126 | 是 | PASS_SCOPED | 空招式多入口分叉保持 |
| D023 | 是 | PASS_SCOPED | 数量展示/实际金额及C29保持 |

## 支持证据与保留门

[新元数据核验](verify-metadata.py) **339/339 PASS**，完整结果、49/124全路径及块、十一输出、24控制/12聚合、三行前后、240贡献保护和固定来源身份见 [metadata-verification.json](metadata-verification.json)。240个已接受贡献回执整文件及受保护既有资料保持；旧目录460行ID/顺序/重数保持，原451保护行、9必要修改与24新增行保持，当前只修B16-C003一处。该保护证明不重授240项语义通过、不替代 affected。

[source-supplement.json](source-supplement.json) 区分自己版本准确的C003来源复用和本次两个必要C120有界回查。原报告、来源证明与完整继承限制保持；未重审全历史或递归来源。U01–U10、G01–G12、AX01–AX20、条件berry67、完整具名未读、媒体/宿主/插件/真实Demo及非局部未证全部保留。runtime observations=0，proven Demo chains=0；未执行 reference/game/Ruby/compiler/converter/generator/deserializer/行为向量或历史程序。静态设计与元数据核验均不称运行测试。

本角色当前最小修复范围为空，剩余 FULL 阻塞0。仍须独立必要 affected 对精确NEW出结论；之后唯一G才可冻结ACT，ACT独立FULL及单独affected各自完整消费FIX_BASE→ACT和NEW→ACT两流，必需精确门通过后才由唯一C接受。canonical保持OPEN，非局部贡献及最终global闭合义务保留。没有代签其它角色、ACT/C或正式接收。

本目录 [artifact-manifest.json](artifact-manifest.json) 绑定第一份报告文件。普通提交推送后，新增 remote-readback-1.json 记录第一提交的独立远端ref/tree/全部文件字节读回；第二次普通报告提交推送后，最终ref/tree及包含回执的所有报告文件全部字节再独立读取比较，完整最终reportSHA在委派返回中给出，避免回执自绑定循环。
