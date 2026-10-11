# B20 独立 FULL 候选再审（cloud-2）

结论：**PASS_SCOPED_FULL_CANDIDATE_19_15；完整19项贡献/15项主责，剩余本FULL候选阻断问题0。** 五组修复按源文、当前正文/目录和51个后继静态子案例重新核对；另14项按上一轮固定完整裁决/源证据及本轮未变条款、案例和资格绑定核对。静态案例全部 **NOT_EXECUTED**，运行观察、行为向量执行和已证明Demo链均为0。这个结论不签ACT、不正式接受B20、不关闭canonical或其它owner义务，也不代签独立affected gate。

精确审查NEW2：`3f521e6dea0b442e4bb174a9715c458416386b37`，tree `49f406a6de8ca2786e5dda27abada19780fdfa05`。基线B19 C：`de1a1c28a4255ff1cfd59fb6fb96f9be2d6ece1f`，tree `88a400af08253bea8d97ee2ef2fa6636f0900f92`。修复BASE：`272885cca76c36cd04dde27b6be2c654759ec4c2`，tree `46969272b7387645bc97b91d227734e89a5f8a80`；上一轮审查NEW `1abaefb1db5818ff9404392143c476979d34c21a`、tree `2e40f9ad0e8fa40377d39e5a19eaa74cc2e05e85` 保留为历史。

审查入口：`81d3be653e87e6424d0d8cd38dab14a9aafc97a1` 的 `review/remediation/20261003-prepare/batches/B20/author-draft-1/candidate-review-2/FULL.md`；最终入口读回包 `dbfa219547690f06eac9180f3ecd9dd1091eb49f`，tree `59529b00d2a3704251f6622f3b1d7b55a186dfdc`。入口/repair-navigation在这两包逐字一致；final相对NEW2仅增加review元数据，所有NEW2已有路径未改。精确入口blob/SHA256/字节、导航与每个引用的验证结果见 [identity-and-preservation.json](identity-and-preservation.json)。

原合同仍是 `669997ac28258f26d0bafc81b1d081abb407a3a1:review/remediation/20261003-prepare/batches/B20/refreeze-after-B19-C-1/author-contract.json`。完整原始finding及已裁决接受对象仍从固定 `93e10babe0b9c9ef8b3f5277754541b447beeeb4` / `41fffb540c6483f5296ea0d33b789b75180d27ed` 取用；本轮19对象的hash/pointer及所有必需资格字段重新匹配，保留根裁决、扩展、前提、反例、最低修订、重查、证据限制和跨owner义务。没有以ID串、索引字段、作者完成状态或scope许可代替质量判断。

两原稿scope固定为 `924c7c3a7a5029b07ad18085cf2dadb594512186:review/remediation/20261003-prepare/batches/B20/candidate-fix-1-original-scope-grant-1/scope-receipt.json`。分别从BASE读取before，独立逐行重构获准WP75一hunk、WP77两hunk的完整after，再与NEW2整文件blob/SHA256/字节相等。Git显示上下文可以移动一行或附带函数上下文文字；重构按固定声明的原字面和位置验证，三处补丁hash均匹配。未把scope匹配当行为通过，未扩展为其它原稿或架构003清理许可。

两轮完整未过滤差异均重新以 `git diff --no-ext-diff --no-textconv --binary --full-index --no-renames BASE NEW` 在内存生成，逐字节核对发布对象；报告仅引用固定流，不另存流或递归复制旧控制/报告：

- C→旧NEW：`f325f625f879105f7811713d9a38cc58da875de2:review/remediation/20261003-prepare/batches/B20/author-draft-1/candidate-review-1/stream/C-to-NEW.full.diff`；blob `54c4dcf3be88f175fcceaca5c3642c29c532adfe`；SHA256 `0889ed6d2a4d300325c0fa5d319d9fd89b72bdaeec8e8a0401c7185a25f9eccb`；1,189,663字节。
- BASE→NEW2：`a9323ee064a4931fa8c218cfe24a060acc4c2e86:review/remediation/20261003-prepare/batches/B20/author-draft-1/candidate-review-2/stream/BASE-to-NEW2.full.diff`；blob `355aca2a456562a5e0799cf36957262ff84c88d9`；SHA256 `0096cacd3fefe3dcb85857300114224b6195deb3f536c22952c75a75845abc1c`；451,455字节。

五组中有6条历史问题，C029的FULL F03/affected AF01合并为一次语义复查。各历史问题的原验收条件、当前路径/行/哈希及逐个子案例核对见 [resolution-ledger.json](resolution-ledger.json)。以下结论均由独立静态阅读形成：

1. **C024 / FULL F01**：WP75正式§3.3第48行及§12.1第282行、原稿第304行、新B20-C024与12子案例一致。顺序为数量门→建/清树→全部目录/脚本输出→备份→loader；编号仅布局。9/10/11两个方向分别核对。清树后首文件打开失败时旧树已清、备份未到（已有B0不变/原无仍无）、原归档不变，无loader；后文件、清树、备份、loader失败保留各已发生前缀，无全局回滚或正常收尾必达承诺。源 `scripts_extract.rb:12–69,71–88,154–175`、`scripts_combine.rb:76–117`。
2. **INTAKE / FULL F02**：正式WP75第26行及B20-INTAKE-R01使用四个ASCII U+003A正向前缀，U+FF1A为负例。10子案例分离前缀大小写与仅换冒号；item/hiddenitem和Battle/Type的前缀大小写不敏感，注册ID/有效页/独立Name/Battle等门不混用。全角Type只是不提供类型，不能虚称其它合法块为空。历史CV-M07字节保留，当前本批规则明确。Move/Common、Trainer/SellItem/s:的其它精确门仍按原限定。源 `Compiler_MapsAndEvents.rb:479–492,510–562,776–791`。
3. **C029 / FULL F03＋AF01**：正式WP77第145–146行、原稿新增§6.4a第174–176行、目录与12子案例绑定只读WP21§6#2/WP18。forced含0最先返回；battle/storage任一真返回存储值；两者假才实际调用动态处理器，宝珠/旗标决定1/0、不同候选按主合同提交。存储0加宝珠/旗标在battle与storage分别仍0，存储1无二条件分别仍1；forced0与form_simple反例明确。原稿原局部正确处理器审计保留，Demo进入/变形未证。源 `Pokemon.rb:147–166`、`FormHandlers.rb:267–272`。
4. **C028 / AF02**：正式WP77第115–121行及原稿第139–145行、目录与14子案例一致。缺max版训练家资料TP空；遭遇请求版缺先退版本0，双版缺或Land/Cave/Water三表空TE空。训练家版本max与全局遭遇版本独立，联系人队伍/地图不替换成玩家队伍/当前图；成员按次数、首最多4槽均匀、重复不去重/第五槽排除/不按野生权重保留。start→TP一次→TE一次→地图名→各段→end，即使无占位符也取候选；空队伍、非法参数/物种按失败阶段限定，不声称同一空文字保护。只读WP63/PL16/PL17保全。源 `Item_Phone.rb:414–438,506–535`、`Encounter.rb:30–39`。
5. **C003 / AF03**：仅新增B20-C003第270行与后继3子案例修正CN为玩家coins代币窗，G为money金钱窗；37/1200与0/1200两对照一致，无金银铜层级。midi排除/mid先复制、坏anm不回滚前缀、CommonEvent独立/被吞/可达三组合及b/pg、标题实体合同保留。源 `Messages.rb:308–345,574–595`、`Player.rb:1–20`，与只读WP17第47行一致。

**上一轮局部判断更正**：我的旧报告对C028和C003的 `PASS_SCOPED_STATIC` 未正确处理缺记录回退与CN代币语义，这两个有限旧判断不能作为NEW2通过证据。本轮以固定源和新活跃案例独立重新判定。旧报告commit `2cf7346cecacb9fad22fe53ebd68e60807bde53d`（tree `09e82497a45e2daaddda861413c23911a4377d86`）及最终读回commit `df1539b67988d4f161b31935752a7f13aec8556b`（tree `0dfea6acf6a43a3070990eb11d2f21b43e5191d6`）保持原样；旧分支远端仍是该最终SHA，没有覆盖或回写旧报告。

| 贡献ID | 责任 | 本轮核对 | 有限条目结论 |
| --- | --- | --- | --- |
| GIR-FD82-003 | B21共享 | 固定证据＋未变增量核对 | PASS_SCOPED_STATIC |
| GIR-FD82-C003 | B21共享 | 五组新源复查 | PASS_SCOPED_STATIC |
| GIR-FD82-C007 | B21共享 | 固定证据＋未变增量核对 | PASS_SCOPED_STATIC |
| GIR-FD82-C020 | B20主责 | 固定证据＋未变增量核对 | PASS_SCOPED_STATIC |
| GIR-FD82-C024 | B20主责 | 五组新源复查 | PASS_SCOPED_STATIC |
| GIR-FD82-C025 | B20主责 | 固定证据＋未变增量核对 | PASS_SCOPED_STATIC |
| GIR-FD82-C026 | B20主责 | 固定证据＋未变增量核对 | PASS_SCOPED_STATIC |
| GIR-FD82-C027 | B20主责 | 固定证据＋未变增量核对 | PASS_SCOPED_STATIC |
| GIR-FD82-C028 | B20主责 | 五组新源复查 | PASS_SCOPED_STATIC |
| GIR-FD82-C029 | B20主责 | 五组新源复查 | PASS_SCOPED_STATIC |
| GIR-FD82-C030 | B20主责 | 固定证据＋未变增量核对 | PASS_SCOPED_STATIC |
| GIR-FD82-C031 | B20主责 | 固定证据＋未变增量核对 | PASS_SCOPED_STATIC |
| GIR-FD82-C032 | B20主责 | 固定证据＋未变增量核对 | PASS_SCOPED_STATIC |
| GIR-FD82-C033 | B20主责 | 固定证据＋未变增量核对 | PASS_SCOPED_STATIC |
| GIR-FD82-C034 | B20主责 | 固定证据＋未变增量核对 | PASS_SCOPED_STATIC |
| GIR-FD82-C051 | B20主责 | 固定证据＋未变增量核对 | PASS_SCOPED_STATIC |
| GIR-FD82-C083 | B20主责 | 固定证据＋未变增量核对 | PASS_SCOPED_STATIC |
| GIR-FD82-D024 | B20主责 | 固定证据＋未变增量核对 | PASS_SCOPED_STATIC |
| WP80-INTAKE-R01 | B21共享 | 五组新源复查 | PASS_SCOPED_STATIC |

每项完整限定、原始/已裁决对象hash/pointer、活跃案例身份和当前评估见 [per-ID-review.json](per-ID-review.json)。14项未变部分的再核对不是整仓重审：WP74整文件未变，WP75/WP77改变行均局限上列五组，补集逐字一致；14个目录行和14个原案例对象逐字一致，固定旧证据与全部资格绑定重新确认。静态例不能替代运行随机取样、脚本IO或Demo链证明。

旧内容保全：BASE有36903个tracked路径，本次仅五个既有payload修改、28个新增review文件，无删路；所有既有BASE路径除该五payload外逐字/模式不变，包括47个先前作者输出。C有36856个tracked路径，到NEW2仍仅原七个payload改变，此外所有既有C路径保全。旧195目录ID的顺序/重数保留，全部195行与旧NEW逐字一致；相对C的193行逐字一致，AN-M23/CV-M18保持先前限定修正。19个B20行仅五个修复行改变、其余14行逐字一致。323个已核对canonical/控制/B19/PA040/接受接口路径与C一致；已接受19批/308贡献及229 OPEN/0 CLOSED状态没有写入更改。

行为准确性与可独立实现性：修复明确了外层门、正常缺失回退、概率样本域、阶段失败及已发生状态，足以按可观察行为独立设计实现与后续测试；没有要求复制参考类结构、方法体或Marshal实现。只读参考固定commit `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`、tree `7589c800b61ba13a13040ed0d686979b80a84fd0`，本轮源读回身份见 [source-reading-log.json](source-reading-log.json)。未执行参考游戏、Ruby、编译器、转换器、反序列化器、行为向量或旧执行脚本；没有模型/额度审计或CLI后备。

报告仅写新分支 `codex/cloud-B20-independent-full-rereview-20261011` 的本目录。报告发布后的普通推送及独立新bare远端fetch、全部输出blob/SHA256/字节比对，记录于 `publication-readback.json`；`output-manifest.json`列出六个非manifest/receipt输出，manifest和receipt自身在最终独立读回时另核对，不产生自引用递归。

尚需原流程的独立affected候选结论、注册员唯一G/ACT冻结、精确ACT的FULL与affected actual两门及最终有限接受；本报告不代签这些门。**本FULL候选复审没有剩余阻断项。**
