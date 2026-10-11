# B21 精确 ACT 独立 affected 子审：B15–B20 与 B03/B14/B19 接口

结论：**PASS_SCOPED_EXACT_ACT_AFFECTED_B15_B20_AND_NAMED_B03_B14_B19_INTERFACES**。本次实际检查未发现本子审范围内的 affected actual blocker。该签名绑定 ACT `d7b9f0882ce873eade1e57bf2a4aa76f7b329b0e` / tree `aed1622a540c3fb9c898e1c7b94741be319f7a83`，不是候选 PASS 的自动转授，也不签 FULL、B21 C、canonical 关闭或 FINAL。

固定管理包 `b49aa3c2c1aa6992539b06a555477db33b75c0a4` / tree `72fdb37b03fdf59caa522f262becd85f25fac7c7`；正式基线 C `e9c140dc33de1cb0662521318b051174909e4509`；已审 NEW2 `e58486178e746273fb6fab55df00722807f1dc44`。先读管理包 `review/remediation/20261003-prepare/batches/B21/actual-freeze-1/affected-actual-dispatch.md`、完整结构派发、两流 manifest 和 owner entrypoints，再检查实际对象与实际管理差异。

语义复用只归属于固定先前独立报告 `53a14af81c1c139da047c51450a84aa7bee9b225:review/remediation/20261003-prepare/batches/B21/affected-review-cloud-20261011-2/b15-b20-and-route-review.json`，blob `b49e5debf7b5c922cd48eab922d3a9c5fc035866`，SHA256 `5020436545d9061370ed984ec8a2bcb467b1c459999dc1c2d04e297cc9ca14a8`。其 `/independent_route_semantic_review`、`/conversion_healing_extraction_compilation_boundary_review`、`/owner_preservation/0` 至 `/owner_preservation/5` 保留原限定。本审另外验证 ACT 的真实字节、当前消费者及 G 登记，不用旧 B20 接受覆盖新段落。

## 完整差异、许可和实际字节

两个未过滤完整流均以新只读 Git 元数据代码独立重建，与固定管理包完整字节一致；不将完整流再次复制到报告。

| 流 | 固定管理包内路径 | blob | SHA256 | 字节 |
| --- | --- | --- | --- | --- |
| C→ACT | `review/remediation/20261003-prepare/batches/B21/actual-freeze-1/complete-C-to-ACT.diff` | `ea8912a48c1a1771176361218bad0beb6a6de449` | `7c293d12cae6badaa58f9361c607811f273830a63653815ef0b6cce3621fcd48` | 2297767 |
| NEW2→ACT | `review/remediation/20261003-prepare/batches/B21/actual-freeze-1/complete-NEW2-to-ACT.diff` | `aa769a802b884cdf0615646d01f4a79c514d0f95` | `7dce7af42a9ea2fee958d981a896463d896d78dca85a8b7c62cdbef4a4d5c995` | 4520793 |

全路径身份清单以 `--no-renames` 独立核为 52/62；默认相似度 rename 表示会将两组删增配成两个 rename，因此 NEW2→ACT 可显示 60 个记录。这是显示规则差异，完整流的字节身份已经独立匹配。

精确许可固定在 `aa57e293bf3a0a77fa42f1f42777df88cbd2fbe8:review/remediation/20261003-prepare/batches/B21/original-scope-grant-R-B21-006-1/scope-grant.json`，SHA256 `a768aff855c04e0be4754270a68500fd7b2d5b715cf90c86657ebbfa9a60b3bd`。独立核其三份 before/after 与 ACT：两 WP75 仅各一段替换，原稿257行、最终稿235行；目录只插入243–248行，即五案例及空行。所有 hunk 外字节与 C 相同，scope 是许可依据，质量另由本次实际审查判断。

| ACT 真正新字节载体 | blob | SHA256 |
| --- | --- | --- |
| `specs/demo/wp75-project-conversion-and-authoring-tools.md` | `3d8b2744c200484fc4a5dcdac2b6fb38542a6a19` | `0db98a17ecd51cc69e7ccc307a97e103d5211585016902f669e226a5f6e7ec75` |
| `deliverables/final-specification-set/demo-dx/wp75-project-conversion-and-authoring-tools.md` | `b2221b3a1793a579cdfbfc74f4bc1e8ea54e23d0` | `2968e3946a4ab751fcdb3d2dda241b3e94f6c4e49c04fe07b0494a5d6c9631a5` |
| `deliverables/final-specification-set/test-catalog/engine-overworld-wp11-15-59-60.md` | `90d0b2513cbcde582ad62189efae93153ccbeab1` | `328093fecfc874cab446a8b969ca8e78889842643fb5859edb2ddea7dcfd17fc` |

独立核全部 22 ACT payload 与 NEW2 的完整字节一致；28 个本范围当前具名消费者的 blob/SHA/长度逐一与先前固定独立证据一致；两 WP13 原/最终全文与 C 字节相同。结论使用这些身份来限定语义复用范围，再审实际管理整合，不以作者的数量或 PASS 字段本身作通过依据。

## B20 新字节与 B03 路线回归

实际阅读两份 §8.6 和 MR18–MR22：先整个求值正常返回，再按原文本任一行行首的三个大小写准确前缀判帧门；命中推进后结束当前帧，没有命中推进后同帧继续。前导空白、接收者、大小写变体仅拒绝该行，其他行仍可能命中；长后缀没有名称结束边界，但仍须整个求值正常返回。求值异常早于谓词和分派器推进，不声称先前脚本副作用回滚，不为任意带前缀字符串承诺可执行。

这与固定独立来源 SRC-040 的源范围427–549、669–699和原批准的先求值/三字面前缀合同一致。来源证据只归属既有固定 SHA `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`，`Data/Scripts/004_Game classes/006_Game_Character.rb`，SHA256 `48496384805d3d5b67c6ba990486de4d53f60cfb7a09e4fc81a3a8350a18d871`；不把本次身份复用写成新运行观察。

MR18/19 保持同一正常返回前提，对比后来行准确前缀与一个 ASCII 前导空格；MR20 明示有效上下文和整个正常返回，接收者行未匹配，不能推广到任意调用；MR21 用较长后缀赋值隔离字面前缀与真实随机移动；MR22 明示无外部提供者的名称失败，另一匹配行不能越过整体求值成功门。全部静态案例执行0。逐行核 MR01–MR17（包括 MR08）与 C 的行字节、顺序、身份完全保全，MR18–MR22 与已审 NEW2 完全一致；删除仅243–248六行可恢复整个 C 目录。

四份实际条款范围哈希和22案例行哈希见伴随 JSON。WP13 的原接受只适用于旧固定内容；两份 WP75 新段落在本 ACT 单独判定为合格，未由旧 B20 PASS 接受。

## B14/B19 转换、治疗、提取、编译方向

两份 WP75 的 35 有序 literal 替换、两条后续文本规则、ASCII门、资源复制后验证、CommonEvent路径和提取方向条件的 hunk 外完整字节不变。固定先前 SRC-314 静态证据为 `Data/Scripts/021_Compiler/004_Compiler_MapsAndEvents.rb`，SHA256 `3fd9c8c754f3af9bb6204b2492d266fb252cbcd8771593a6650f70601b9b13cc`。仍保留治疗首字符预检查→续行无分隔拼接→删除空白→精确整体文本匹配，旧末条残留/单行增长及可能不终止、前期已写文件不回滚；转换顺序和部分写入不因 G 登记改变。

提取仍按方向区分清树/前缀写入/备份/loader、反向合并门、重建抛弃旧列表与不备份，不声称等价、事务化或自动执行。编辑器可达、archive/PBS、compile、当前地图/cache/snapshot 分层保留；调试治疗不同于正常 domain，120效果白名单/默认范围和动态激活限定仍在，菜单可达不等于工具完成。

ACT G7-4/G8-2/G8-3 位于 `review/remediation/20261003-prepare/wp78-junction-successor.tsv` data rows43/46/47；整个文件与 NEW2 相同且逐对象哈希匹配。两 SRC-040/SRC-314 的 `/rows/39/new_qualified_route_bridge`、`/rows/313/new_qualified_route_bridge` 当前 ACT 对象哈希均 `2257c908c4383049f3a89662c744add0646f3486026ec71af35fd193404dbb49`，正确消费本 ACT 相同 after 字节。CHAIN-6 是固定 NEW2 `author-draft-1/eight-chains.json#/chains/5` 对象 `b91d1c0966726b899c99a913f619cf1cee62d824265eba655b21e9546bf4deaf` 的归属复用，不将 ACT 缺少的作者目录当成本地可读副本。新桥只声明条件文本消费，不制造编译自动化、运行路线或演示链完成。

WP59 时间/色调实际消费者保持 C 全字节：四通道逐小时插值、06:30整数亮度138、30秒单调刷新与calendar value区分、禁用时缓存及地图/户外门都未被路线桥或 G 登记改写。GIR003扩展4/9/10仍指向真正的 WP67-A/76、WP60/61/63/65、WP66-A/67-B 消费者；C029仍接 WP21/18/77与旧 B20 trace318。实际消费者全字节及旧 trace 前缀重新核，没有导航回退。

## 六 owner 的精确 actual 处置

六个 owner 的历史证据子树 mode/type/blob 由完整 Git subtree 身份核与 C 一致；其 acceptance 全字节不改。旧 FULL 精确 SHA/路径、先前语义范围、全部103回执的 item 指针和对象哈希均在伴随 JSON `/owners/0` 至 `/owners/5`，无旧语义范围扩张。

| owner | ACT 处置 | 原接受贡献 | 实际影响与保留的限定 |
| --- | --- | --- | --- |
| B15 | PASS_SCOPED_EXACT_ACT_AFFECTED | 16 | WP62登记/搜索退出、礼物取消前写入、18电话 ASCII参数与异常、地图取整及第一重叠记录、Jukebox map/global门全字节一致；新路线谓词和管理登记不消费这些状态，不新增成功/回滚条件。 |
| B16 | PASS_SCOPED_EXACT_ACT_AFFECTED | 24 | Party/背包/仓库swap/BACK、邮件/BoxLink部分写入、商店非事务、选项/BGS记忆及返回值仍按旧限定；WP66-A/WP67-B导航实接正确域，新中央资格没有提升为全部 UI 激活。 |
| B17 | PASS_SCOPED_EXACT_ACT_AFFECTED | 12 | 战斗距离/BACK、Mega真正变形、进化update→BACK→finished、EV重复槽、曲目/intro独立副作用与位置前态保留；WP67-A/WP76真实caller保留，未报声音/宿主时序运行。 |
| B18 | PASS_SCOPED_EXACT_ACT_AFFECTED | 8 | 卡片hand/destination/input门、duplicate与uniform前提、puzzle奇偶/合法逆构造及旧九输入批准未改变；G9-3实际管理层与旧具体receipt另核，注册不转成接受或关闭。 |
| B19 | PASS_SCOPED_EXACT_ACT_AFFECTED | 24 | 编辑器ASCII/异常、BREAK局部失败、numeric/nullable/parent取消、120成员域、archive→PBS→compile→snapshot/cache与治疗分层保留；新路线桥不吞异常、不刷新地图或隐式编译。 |
| B20 | PASS_SCOPED_EXACT_ACT_NEW_WP75_AND_OLD_B20_INTERFACES | 19 | 旧19只归属 before/未改接口；本 ACT 两§8.6及五case另审，35替换/ASCII、提取方向、动画及真实工具缺陷保留；C029的物种/helditem/forced0、battle/storage、普通/simple和反向case未改。 |

这些结果是本 ACT 的限定 affected 处置，不重签旧 owner 的原始 FULL 或接受回执。

## 327旧接受、14待接受和公共 G

独立重新取得 ACT `review/remediation/20261003-prepare/batches/B20/acceptance-stage-1/completion-statistics-successor.json`，blob `78fe0ad495e2b8734b5cc16788988a97e84c277f`，SHA256 `d11d131dc64b399cda50b7518fffe8a812282c1b51436065647c1707c831d303`。整个文件与 C 完全相同；327对象逐一重建并匹配固定先前独立哈希，其中本范围103项按原对象指针验证。

同327对象 sorted-key compact JSON 数组哈希仍 `ca73d8b68c03e80e40066acb4349683836f8165a4f2daa5935cfef8b852cd9fa`；G 使用保持键序 compact 得 `a265c9218a0a39996ef8c543a01e16f5a9a1e0d1be5e46c741b9055859c3db43`。两者序列化约定不同，数据对象相同。GIR003 accepted_contributors 按批次排序，集合/唯一性与12个旧接受owner一致；旧回执和旧公共行未重新排序。

实际两个公共 TSV 的 C 全字节是 ACT 不变前缀，327旧接受字段/签名均保留。只后14行由 author proposal 转 G registration：各 ID/remaining contributors/B21_C/closure/FINAL 独立解析，仍只剩 B21 待接受，canonical仍OPEN；新14不得计入327接受。外部管理包 `public-registration-actual-binding.json` 精确绑定三文件、14条 G 对象指针及 ACT/tree，解析公共占位符仅属冻结绑定，不是实际质量签名。

三实际公共文件身份：

| 路径（均在 `review/remediation/20261003-prepare/`） | blob | SHA256 |
| --- | --- | --- |
| `approval-ledger.tsv` | `bb3b9c0403e2d7065adebbf2e1cdab85b62cdfbe` | `401fa6e8984c8b75acd382cd5a0f47a8671bce7fb27d4040cdb8cf8f0b9768fc` |
| `traceability-successor.tsv` | `43a24e7fd40f7948af8fbf95c57d9cd7585dac92` | `da1e2003ae43264233b2e2f8d64f9a8d7ef8913e87fd9eea698ea81f33048a6a` |
| `final-integration-review.md` | `b09fe13c24e01b1bc18ef02a77601c6c218e4264` | `0cebc77c6580f2d871437ba41aed89dc47d4fe43454d47855649d7bfd2959979` |

实际 final-integration-review 保持整个 NEW2 为字节前缀，仅追加 G 层。G层明确 20/21、327 accepted、14 pending，B20/B03/B14/B19仍需实际复审；不抹除以前时点的 author pending/head 或旧批准。G formal-copy-identities 的32作者证据固定 N 引用逐一核 blob/SHA/长度，不因 ACT未复制作者材料导致旧固定证据失去归属。

G9-3 actual data row51 的五具名管理范围重新核哈希，fixed旧snapshot只用于这些不变范围；audit整文件曾附加更新，不能声称其旧整文件就是 ACT。其旧 B01 receipt0/trace1、B18 GIR001 receipt276/trace277、B18 R02 receipt283/trace284 均与 ACT旧公共行/327对象精确相同。原批准、当前字节、候选签名、actual签名、接受和关闭分层仍成立。

## 限制与验收条件

本次只执行新 Git/UTF8/JSON/hash 元数据核查；未执行参考游戏、Ruby、编译器、转换器、反序列化器、行为向量、案例或旧脚本。没有新运行观察/真实Demo链。没有修改仓库正文、参考、旧报告、main或旧证据；输出仅 `/tmp` 新独立子审文件供主审普通发布及独立远端读回。

本 PASS 限于上列 ACT/tree、scope三份 after 和全部具名接口：保留整个正常求值/调用机会、准确字面前缀、失败与部分写入、静态输入前提、旧具体接受作用域及 source/config/UI/未读/激活限制。如果这些实际身份或条件再改，需要相应新的精确审查。当前327接受/14pending/229OPEN/0CLOSED不由本报告改变；主审须完成其余 affected owner及导航/资格范围，FULL由原独立角色处理，B21 C/关闭/FINAL由另门协调。本子审无剩余 blocker。
