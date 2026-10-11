# B21 NEW2 独立 affected 子审：B15–B20 与路线交界

结论：**PASS_SCOPED**。独立核得两份 WP75 §8.6 新字节、MR18–MR22 和 G7-4/G8-2/G8-3、CHAIN-6、SRC-040/SRC-314 的新路线桥与固定来源/已接受消费者一致；B15–B20 原接受贡献、旧证据和非新段落接口保全。没有本子审质量阻塞。scope 许可仅证明可修改的固定字节范围，本结论来自以下静态核查。

被审 NEW2 `e58486178e746273fb6fab55df00722807f1dc44` / tree `1dbe28a733bfde428129ed662d7e0d66243978c4`；C `e9c140dc33de1cb0662521318b051174909e4509`；派发 D `eb1885265fcde2a52767077de3193862036c3a71`；scope grant `aa57e293bf3a0a77fa42f1f42777df88cbd2fbe8`；freeze/publication `9b6d16e34daf59e205f8a3df20e24930175064ed`。原 affected `7db07543137cc11ef76b725e0a3c8975796bc7b0` 只在其旧限范围内复用，不把旧 B20 PASS 转授新段落。

## 许可、实际字节与固定旧证据

独立核 grant 中三个 before/after blob、SHA256、字节数与 NEW2 实际对象相同。两份 WP75 各只替换 §8.6 一段：原稿257、最终稿235；目录只在旧 MR17 后插入五新行及空行（243–248）。各 hunk 外逐字节不变；原/最终 WP13 两个移动路线矩阵保持 C 全字节，全部旧目录行（包括 MR01–MR17/MR08）的字节、次数和顺序保全。

| 当前实际输出 | blob | SHA256 |
| --- | --- | --- |
| `specs/demo/wp75-project-conversion-and-authoring-tools.md` | `3d8b2744c200484fc4a5dcdac2b6fb38542a6a19` | `0db98a17ecd51cc69e7ccc307a97e103d5211585016902f669e226a5f6e7ec75` |
| `deliverables/final-specification-set/demo-dx/wp75-project-conversion-and-authoring-tools.md` | `b2221b3a1793a579cdfbfc74f4bc1e8ea54e23d0` | `2968e3946a4ab751fcdb3d2dda241b3e94f6c4e49c04fe07b0494a5d6c9631a5` |
| `deliverables/final-specification-set/test-catalog/engine-overworld-wp11-15-59-60.md` | `90d0b2513cbcde582ad62189efae93153ccbeab1` | `328093fecfc874cab446a8b969ca8e78889842643fb5859edb2ddea7dcfd17fc` |

原固定批准 `41fffb540c6483f5296ea0d33b789b75180d27ed:review/remediation-20261003-prepare/finding-acceptance.json#/GIR-FD82-C007/extension_decisions/1` 仍要求先求值再按三个准确行首前缀判帧门，必要输入身份不能用语义等价移动或未来方法模板代替。批准文件 SHA256 `54e4c86be3db493a5463ce4bcdef81c7184f1a1d89e6b3bbea358f14cc347225`；extension1 对象 SHA256 `d97a3540871e46dd19d5c84cce11509b35358e4bc34cc5dd58f535500cf316db`。完整限定 overlay 位于 D `control-and-acceptance-overlay.json#/complete_control_records/8`。C007 当前限定还明确67树果完整表属条件建议，不能据机制/样本扩成无条件67行义务；120效果成员与18电话兼容各自保留原完整要求。

固定原子审 `7db07543137cc11ef76b725e0a3c8975796bc7b0:review/remediation/20261003-prepare/batches/B21/affected-review-cloud-20261011-1/owners-b15-b20.json`，blob `3081e38395aed64a92b268f90889818a6036bddd`，SHA256 `27fd383dd853adc46a4ac745f1989469ccc3e0256711c7c820dcba3a63683dfd`。六 owner exact acceptance/FULL/103 receipt 的身份、item指针与范围重新核到 NEW2；26旧证据解析无错误。327旧receipt逐对象静态重建 SHA256 以及整数组 canonical SHA256 `ca73d8b68c03e80e40066acb4349683836f8165a4f2daa5935cfef8b852cd9fa` 与作者登记相同，但它只证明身份保全，不替代语义判断。旧 approval-ledger/traceability-successor 的 C 全字节仍为 NEW2 的不变前缀。

## 独立来源与控制流程

仅静态阅读参考固定 SHA `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`，没有执行：

- SRC-040：`Data/Scripts/004_Game classes/006_Game_Character.rb`，blob `9de49c288ec6c5d8c962b14f1b959ad90ae3d662`，SHA256 `48496384805d3d5b67c6ba990486de4d53f60cfb7a09e4fc81a3a8350a18d871`；读取范围 427–549, 669–699。
- SRC-314：`Data/Scripts/021_Compiler/004_Compiler_MapsAndEvents.rb`，blob `cb302adb0c236984c0b4acc5ea61d31c7048dcca`，SHA256 `3fd9c8c754f3af9bb6204b2492d266fb252cbcd8771593a6650f70601b9b13cc`；读取范围 1–38, 951–974, 1135–1191, 1571–1575, 1683–1750。

SRC040 的路线分派先拒绝 moving/jumping 和 size≤1，然后进入有界循环。代码45的求值在540；三次大小写准确的行首文本检查在541–543；命中在544加索引、545立即返回；不命中到548加索引后继续本循环。因此后来行命中也会结束本次调用；空白/接收者/大小写改变只使该行不命中，别的行仍可命中；较长后缀没有名字终止边界。求值异常先于判定和分派器推进，本层没有 rescue。这里只说分派器不到后续推进点，不把脚本已经造成的副作用回滚。

三个准确前缀为 `move_random_range`、`move_random_UD`、`move_random_LR`。新两段文字要求整个求值正常返回，以文本行首判帧门；不承诺任意有前缀字符串可执行。WP13 §1 lines17–18与matrix45 line71已有同一合同，本次只消除 WP75 旧“字符0”缩窄。有效角色/列表/字符串、当前更新机会与足够后续循环机会是分派前提；不以工具入口可达代替实际调用。

## 五个新增静态案例

所有案例执行数为0。它们是明确输入前提下对固定代码分支的静态推导：

- MR18：Explicit two-line valid local-assignment normal-return premise. Only second line starts range_extra; line anchor still matches. Advance then return postpones27. This is a static input design, not a run.
- MR19：Same normal-return premise as18, one leading ASCII space on the sole candidate line, no other matching line. Predicate false reaches548 then current loop processes27. Whitespace is a literal gate rather than a guarantee about arbitrary Ruby text.
- MR20：Receiver line self.move_random_range(2) has an explicitly given valid context/whole-evaluation normal return. It does not begin with a literal. No other match, so dispatcher continues to27; no claim all contexts allow receiver calls.
- MR21：Earlier whitespace/receiver lines do not match, later exact UD_extra or LR_extra assignment does. Whole-evaluation normal return is explicit. Long suffix has no end boundary and assignment need not cause movement; isolates prefix identity from movement semantics.
- MR22：One line is assumed to encounter an undefined-name error with no external provider, while another line has an exact prefix. The exception leaves code540 before any prefix inspection/dispatcher advance and before27. Caller presentation remains unverified.

MR18/19构成同一正常求值前提下的后续行/前导空格反向；MR20只在给定可正常返回的接收者上下文判未匹配，不推广到任意调用；MR21的长后缀赋值隔离字面身份和随机移动效果；MR22证明别行匹配文本不能免除求值成功门。旧 MR08 已分别列三个 literal 与后续27，MR13–MR16的空白/receiver/长suffix/异常对照均未改。

## 转换、治疗、提取与编译回归

Independently read source SCRIPT_REPLACEMENTS1–38 and replace_scripts951–956; compared every ordered literal pair to final WP75 lines149–183, all exact and ordered. Two following regex substitutions retain variable-read negative-following-character restriction and party(pbGet) form; no lexical boundaries/string/comment protection or AST conversion is added. NEW2 only §8.6 differs in both WP75 copies.

SRC3141135–1171 checks first-character f/p/K before concatenating all consecutive655 text without separators then deleting all whitespace. 1173–1191 requires exact two normalized whole-text forms. Deletion count lastScript−i retains the final old command; with one original355 the zero-delete insertion places output before unchanged input, and1572 increments back to that input, so repeated growth/possible nontermination remains. No rollback or semantic-equivalence guarantee is introduced. Source driver1713–1715 runs naming then text replacements before fix_event_use, so Kernel removal can precede the healing precheck.

SRC3141683–1750 source text retains sorted map traversal; trainer→item→name→script replacement→fix use, then counter handling/save only for changed map. CommonEvent path subsequently runs fix_event_use only. New route bridge does not make these tools run, does not turn saved PBS into an automatic compile, and does not erase previously written maps on a later exception.

Current final WP75 §12.1/12.2 preserves accepted archive-count direction gates9/10/11, clear tree→write prefixes→backup→loader ordering, partial writes, opposite merge guard, rebuild discard of old archive list and no merge backup. Source/serializer for these unchanged clauses was not executed or rerun; exact accepted old B20 C024 and related controls/FULL evidence remain the reuse basis.

WP59 §3.5 unchanged: independent four-channel hourly interpolation, actual brightness integer138 at06:30, 30-second monotonic refresh versus calendar value time, disabled switch retaining cache and map/outdoor apply gate. The new route line predicate does not alter time/tone inputs or cache. Named B14 old caller conditions and sample/activation limits remain; no new shading/host observation.

WP72§6.1/8.3 and full effect table, WP73-A/B source-form/archive/PBS/current-snapshot distinctions remain. Tool menu availability is separate from tool completion. Land archive0→PBS omission→recompile21 versus OldRod0, same-version early return, metric nonzero-form path and no live layout auto-refresh, pluralEvolutions parentNo versus singular-write conversion, and BREAK LocalJumpError are not overridden by the route bridge.

G7-4 新异常补充不吞异常也不回滚早期文件；G8-2 新路线桥明确整个正常求值→任一行三准确前缀→命中结束/不命中继续，仍保持登记/archive/PBS/compile/当前snapshot分层；G8-3仍区分作者工具可达与玩家事件演示。CHAIN-6新桥明确只是文本消费条件，不保证转换自动执行路线或自动编译链；复数Evolutions、单数写出转换与 BREAK 局部失败仍分列。两 SOURCE bridge 绑定真实 NEW2 WP75 identity、旧 WP13 clauses 与五静态行，固定 source blob 不变；本审另作了实际 plain-text 语义阅读，不把作者 false semantic_read 标志改成运行证明。

| 新交界/桥 | 固定路径/指针 | 独立对象哈希 |
| --- | --- | --- |
| G7-4 | `review/remediation/20261003-prepare/wp78-junction-successor.tsv` data row 43 | `c0a20dec715d60eecc9ac8fcf81ee99360333f10ffbebb2705f92250bbafa2eb` |
| G8-2 | `review/remediation/20261003-prepare/wp78-junction-successor.tsv` data row 46 | `a6f2ba51b898a907adf286d33924c4222612884c52a7e7d76125e6d355a6b643` |
| G8-3 | `review/remediation/20261003-prepare/wp78-junction-successor.tsv` data row 47 | `19ec01181147c058641a425479f5c4c2537100629db55d78edd235e2b0785776` |
| CHAIN-6 | `review/remediation/20261003-prepare/batches/B21/author-draft-1/eight-chains.json#/chains/5` | `b91d1c0966726b899c99a913f619cf1cee62d824265eba655b21e9546bf4deaf` |
| SRC-040 | `review/remediation/20261003-prepare/wp79-source-successor.json#/rows/39/new_qualified_route_bridge` | `2257c908c4383049f3a89662c744add0646f3486026ec71af35fd193404dbb49` |
| SRC-314 | `review/remediation/20261003-prepare/wp79-source-successor.json#/rows/313/new_qualified_route_bridge` | `2257c908c4383049f3a89662c744add0646f3486026ec71af35fd193404dbb49` |

## 逐 owner 判定

### B15

PASS_SCOPED。旧16项 exact acceptance/FULL/历史子树重新核到NEW2。WP62 ordinary登记/last_seen、搜索mode4与result退出、礼物共享P取消前写入、电话18 ASCII参数/输入形态/异常、TP/TE版本与首4均匀/单次抽样、地图ceil/floor/第一重叠记录和Jukebox map/global门仍用固定已接受消费者。NEW2路线文本只影响B20↔B03分派说明，不为地图/礼物/电话添加入口、成功、回滚或状态写入。GIR003扩展9现在接到WP60/61/63/65及B14/B15/B16原trace，不再用错误域覆盖。

C接受 `review/remediation/20261003-prepare/batches/B15/acceptance-stage-1/contribution-acceptance.json`，SHA256 `f823a2cc752fed9e3101e2ca75167c7a651e54fe93498e76cc0803e5db1d651f`；旧FULL `4b3ff8dff1733aa8249c75a8b494e87ad93fc472:review/remediation/20261003-prepare/batches/B15/integration-review-1/findings.json`，SHA256 `bf7e70963cfdad57d931e794f9501bbe9232bb63adf072f7d15a884ffb6640aa`。对应所有 /records/i 与旧FULL项指针见 JSON，仅在原限定局部范围复用，不重签旧owner。

### B16

PASS_SCOPED。旧24项 fixed controls/FULL和消费者字节重新核。仓库swap暂持/BACK门、背包TR与Party Item Use的初始moves/stat写入差异、空重学先ArgumentError、邮件/BoxLink部分写入与NoMethodError、shop槽位非事务、BGS共享记忆和option/background异常边界保持。SRC066/068/230当前资格限暂停/导航绝对相位及训练家/盒名预览实际caller，未转为全部UI运行。扩展10新导航准确接WP66-A/WP67-B及B16/B17，原源组织中立化与必要返回值均保存；WP75路线谓词不消费这些UI状态。

C接受 `review/remediation/20261003-prepare/batches/B16/acceptance-stage-1/contribution-acceptance.json`，SHA256 `4f3df8260649c8dd40407e6a7e64936aa215cdf7a3f13ff1a3235dcf4fe99394`；旧FULL `191e669c72282e0c11217df2e7f80ed5c377dbd7:review/remediation/20261003-prepare/batches/B16/integration-review-1/review.json`，SHA256 `0b13cd526c90e23490c805ac728d5401364ba288acc416c0a202e11452580a1a`。对应所有 /records/i 与旧FULL项指针见 JSON，仅在原限定局部范围复用，不重签旧owner。

### B17

PASS_SCOPED。旧12项精确范围仍在NEW2。NearAlly位置0/2/4、far确认登记后执行拒绝、自身反例、Fight/Encore/type4 BACK、Mega可达与真正变形、进化update→BACK→finished、EV重复槽及no-scene singular move失败、六选曲/独立nextbattle/intro记忆副作用、前态双shift计划都未被新中央资格混层。SRC290与SRC026限具名静态消费者和清时间锚点，不报声音或宿主时序。GIR003扩展4现在为WP67-A/WP76、正确B17 trace265及逐clause/case，WP39只供领域上下文，不替代UI。

C接受 `review/remediation/20261003-prepare/batches/B17/acceptance-stage-1/contribution-acceptance.json`，SHA256 `2482d5b8fab7b9375dd15e4ac047e73f513b7a9aa8ce41931dd5953586375703`；旧FULL `6d5fb7f267b65f2aba01837ce0f87488b0723220:review/remediation/20261003-prepare/batches/B17/integration-review-1/contribution-review.json`，SHA256 `b34f4b2e3c70569582812c3a9a4b5d67c3f155326395480413fc8a975dd677db`。对应所有 /records/i 与旧FULL项指针见 JSON，仅在原限定局部范围复用，不重签旧owner。

### B18

PASS_SCOPED。旧8项 exact acceptance/FULL和WP68/WP71/各旧目录字节不变。hand/destination门、完成后freshinput、duplicate slot与uniform概率前提、openhand空导航但无board写入、puzzle奇偶与合法逆构造、redcursor/mode/USE门、旧九输入批准身份与current字节质量分开仍成立。NEW2仅新增移动路线静态case，与这些玩法输入/存储/返回无共用修改入口；未新增demo可玩或solver运行证明。

C接受 `review/remediation/20261003-prepare/batches/B18/acceptance-stage-1/contribution-acceptance.json`，SHA256 `94e78a0ffeebb2c15ca66628b4fee50222b4d4c1e2e4df4ed655f971bcb8b5e5`；旧FULL `fd0a6d7556839ab1daa8ca6c64a12ead833de13f:review/remediation/20261003-prepare/batches/B18/integration-review-1/review.json`，SHA256 `2d5c43dbce33c7ed1636593a5e05ba74a19dc0a60a94929c4ce152bf5bef1dd8`。对应所有 /records/i 与旧FULL项指针见 JSON，仅在原限定局部范围复用，不重签旧owner。

### B19

PASS_SCOPED。旧24项限范围复用，重新核NEW2消费者及G7-4/G8-2/G8-3/CHAIN6。ASCII s: vs全角、SyntaxError与StandardError差别、BREAK真实LocalJumpError、numeric/nullable与parent取消、120成员域/默认范围、六内容editor、archive→PBS→compile→current-map/cache顺序、调试治疗与正常domain差别不变。新增route bridge是条件文本消费者，不触PBS编译/治疗入口，不吞已写文件前缀或刷新缓存；具体源序与实际newWP75 identity单独核了。

C接受 `review/remediation/20261003-prepare/batches/B19/acceptance-stage-1/contribution-acceptance.json`，SHA256 `6a1e5a20e1cc8f1924a3ac8e413a084e0954687b6cc623ab3617f962364c9377`；旧FULL `9dfbf89aba953a872a2680ff22946464a89d9861:review/remediation/20261003-prepare/batches/B19/actual-full-review-20261010-1/contribution-review.json`，SHA256 `a11326754de17fee44e8d8b3d9f429cdbcf50de7f08c65c51eaeb66004482585`。对应所有 /records/i 与旧FULL项指针见 JSON，仅在原限定局部范围复用，不重签旧owner。

### B20

PASS_SCOPED旧19项保全＋PASS_SCOPED_NEW2_NEW_BYTES。旧接受只用于固定before与未改§3.1/8.1/8.4/10/12.1/12.2等部分；§8.6两新字节由本次source/control/case独立判断。35有序literal/两regex、必要ASCII、资源copy→validation、CommonEvent可达chunk、提取merge阶段/方向、动画slot/frame/shared base及真实converter缺陷、电话C028条件均保持。C029当前WP77 145–146主体GIRATINA/GRISEOUSORB及forced0、battle/storage、普通/simple、other-species反向仍同C字节；新map39/trace9明确接WP21/WP18/WP77和B20-C029目录278，旧trace318/receipt317保全。

C接受 `review/remediation/20261003-prepare/batches/B20/acceptance-stage-1/contribution-acceptance.json`，SHA256 `10d1d555d045fa853c8b7f975f80ec4ea17d2c515f4a67066ea8ba9c484da08a`；旧FULL `3fef0d8982b01f26fe52c0345a9f4d82419c63dd:review/remediation/20261003-prepare/batches/B20/independent-full-actual-review-cloud-1/per-ID-actual-review.json`，SHA256 `b30c3e9dba797f78156a7a4a7e820ae089ee9bf8b369406f3ffbe640889b4f3e`。对应所有 /records/i 与旧FULL项指针见 JSON，仅在原限定局部范围复用，不重签旧owner。

## 原导航阻塞的本范围复核

原 GIR003 extension4/9/10 和 C029 精确导航缺口在 NEW2 分别修到 WP67-A/76（B17 trace265）、WP60/61/63/65（B14/B15/B16）、WP66-A/67-B（B16/B17）、WP21/18/77（B20 trace318与case278）。当前consumer实际 blob/哈希、命名clause范围哈希与静态case行哈希重新核过；没有用一个无关B09/B19 trace或same-ID整体对象代替本扩展的owner证据。原BODY/反例与界面层次并未被撤销。

## 验收条件、限制与未完成门

- This PASS_SCOPED binds only exact NEW2 e58486178e746273fb6fab55df00722807f1dc44/tree1dbe28a733bfde428129ed662d7e0d66243978c4, the granted two §8.6 paragraphs and MR18–MR22 bytes, unchanged old B15–B20 scopes, and named B03/B14/B19 route/conversion interfaces. A changed before/patch/after identity requires new exact review and, if outside current permission, its precise successor scope.
- Root must complete its independent FULL and other affected-owner/whole-junction/navigation/qualification findings. This delegated report supplies no actual, registrar B21 acceptance, closure, FINAL1 or FINAL2 signature.
- The later actual integration must be frozen separately and independently rechecked on exact actual bytes and interfaces. Neither historical B20 PASS, scope grant, NEW2 candidate review nor author counts/identity checks automatically transfer quality to that version.
- Retain327 accepted receipt objects and old signatures by attribution, immutable controls and canonical OPEN/remaining gates. Keep evaluation normal-return and caller/update conditions, ordered failure/partial writes, named literals, line prefixes and reverse cases. Runtime/behavior vector/real demo chain execution remains0.

本子审无剩余质量阻塞。全部执行0：参考游戏、Ruby、编译器、转换器、反序列化、行为向量、旧执行脚本；只进行新 JSON/TSV/plain-text/Git 元数据阅读分析。没有修改仓库、原/净正文、参考、旧报告或 main。完整C→NEW2差异由根独立重建，本报告只引用 publication `9b6d16e34daf59e205f8a3df20e24930175064ed` 的 `review/remediation/20261003-prepare/batches/B21/author-draft-1/freeze-2/complete-C-to-NEW2.diff`，SHA256 `0213e85fbe687500343f9e3848b49650bafdb7a726cac8beb54f083ee7e41b15`，不再复制完整包。

本报告是 NEW2 的限定候选affected结论，主审仍负责其余 FULL/affected 范围以及普通发布和独立远端读回；未来 exact ACT、登记B21接受、FINAL-1、关闭与 FINAL-2 均尚不由本报告签署。
