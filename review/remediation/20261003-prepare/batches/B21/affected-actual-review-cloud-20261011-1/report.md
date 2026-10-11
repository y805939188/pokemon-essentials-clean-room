# B21 精确 ACT 独立 affected B01–B20 复审

结论：**PASS_SCOPED_EXACT_ACTUAL_AFFECTED_B01_B20**。本报告独立签署以下精确 ACT 的全部 B01–B20 支持消费接口及间接影响。完整 C→ACT、NEW2→ACT 差异、三路径 scope 实际落地、B20 新字节与 B03/B14/B19 回归、公共 G 登记/实际绑定、327 旧接受及历史证据保全均通过限定静态复核；无剩余 affected actual blocker。

本次是新的 AFFECTED_ACTUAL 判决。相同 NEW2 字节的原有效证据按固定身份和资格归属复用，候选 PASS、scope 许可、作者或登记员数量/断言没有替代本 actual 判断。此报告不签 FULL actual、B21 C、canonical 关闭、FINAL-1/FINAL-2 或 main 合入。

| 固定角色 | commit | tree |
| --- | --- | --- |
| 被审 ACT | `d7b9f0882ce873eade1e57bf2a4aa76f7b329b0e` | `aed1622a540c3fb9c898e1c7b94741be319f7a83` |
| 唯一 G / ACT 唯一父提交 | `d13eedb893abaf39322a022beba1d0a24f43b8aa` | `10b08e7ce7f461d8a351f6f02734ed5e60029bfd` |
| 固定管理包 M，ACT 后继 | `b49aa3c2c1aa6992539b06a555477db33b75c0a4` | `72fdb37b03fdf59caa522f262becd85f25fac7c7` |
| 已审 NEW2 | `e58486178e746273fb6fab55df00722807f1dc44` | `1dbe28a733bfde428129ed662d7e0d66243978c4` |
| 原 affected NEW2 报告 R | `53a14af81c1c139da047c51450a84aa7bee9b225` | `baa164d68c76bc82d4fbaf11e018554073aa3f57` |
| B20 C 基线 | `e9c140dc33de1cb0662521318b051174909e4509` | `5baa01c8a604400b73f560bb06fa5d770089502a` |
| 原完整派发 D | `eb1885265fcde2a52767077de3193862036c3a71` | `c85948f536d7444bfe83d3c323ea6a48ba15d143` |
| 三路径精确 scope SG | `aa57e293bf3a0a77fa42f1f42777df88cbd2fbe8` | `d1333b17eb6987d51dac40988d7d0e744b2ed677` |

## 固定入口、完整差异与实际范围

先读 M 的 `review/remediation/20261003-prepare/batches/B21/actual-freeze-1/affected-actual-dispatch.md` 与结构化派发，随后读取两份完整差异、冻结身份、全部 20 owner 入口及 G/actual 绑定。原 D 的完整合同、229 义务、20 依赖和 SG 精确许可继续有效。M 是晚于 ACT 的管理发布，不冒充被审 ACT。以下简称 B 根目录为 `review/remediation/20261003-prepare/`。

在内存独立重建未过滤的 `git diff --no-ext-diff --binary --full-index C ACT` 和 `NEW2 ACT`，完整字节与 M 发布版本一致；逐差异路径判定正文、管理、证据位置和保护范围。完整差异只引用固定身份，不在本报告目录再复制。

| M 中固定路径（B 根目录下） | Git blob | SHA256 | bytes |
| --- | --- | --- | ---: |
| `batches/B21/actual-freeze-1/complete-C-to-ACT.diff` | `ea8912a48c1a1771176361218bad0beb6a6de449` | `7c293d12cae6badaa58f9361c607811f273830a63653815ef0b6cce3621fcd48` | 2,297,767 |
| `batches/B21/actual-freeze-1/complete-NEW2-to-ACT.diff` | `aa769a802b884cdf0615646d01f4a79c514d0f95` | `7dce7af42a9ea2fee958d981a896463d896d78dca85a8b7c62cdbef4a4d5c995` | 4,520,793 |

C→ACT 展开为 52 路径事件：25 正式输出加 27 管理文件。NEW2→ACT 展开为 62 事件：三公共管理文件修改、32 作者证据仅在固定 NEW2 保留、27 管理文件新增。Git 默认识别两组重命名，第二份完整展示为 60 差异块；展开的增加/删除是同一完整比较，没有过滤或遗漏。27 管理文件为原 D 包13、SG包5和G材料9；精确分组和全部路径见 [静态审计](static-audit.json)。

原22写路径加精确获准3路径仍是25正式输出。G→ACT仅复制22个 NEW2 payload：原22中除三公共管理路径的19项，加 scope3。这22项逐完整字节同 NEW2；三公共管理项由唯一 G 另行登记，ACT 同 G，不能用 NEW2 比对自动签其新字节。原 D/SG 管理材料在 ACT 与其固定发布逐字节一致。

scope3 after 与 SG 指定 blob/hash/bytes完全一致，独立逐行比较仍只有：WP75 原稿257行、最终稿235行各一段替换，engine目录243–248行五案例及空行插入。所有 hunk 外字节同 C。scope 的 SHA256 为 `a768aff855c04e0be4754270a68500fd7b2d5b715cf90c86657ebbfa9a60b3bd`；它只证明写权限，质量由本次接口复核判断。

## 公共 G、资格及 actual 导航

三公共管理文件的 actual 身份如下，全部同 G；两个 TSV 的 C 旧327行原始字节前缀均保留，最终整合说明完整 C/NEW2层继续保留，再追加 unique G 后继：

| B 根目录路径 | ACT blob | SHA256 |
| --- | --- | --- |
| `approval-ledger.tsv` | `bb3b9c0403e2d7065adebbf2e1cdab85b62cdfbe` | `401fa6e8984c8b75acd382cd5a0f47a8671bce7fb27d4040cdb8cf8f0b9768fc` |
| `traceability-successor.tsv` | `43a24e7fd40f7948af8fbf95c57d9cd7585dac92` | `da1e2003ae43264233b2e2f8d64f9a8d7ef8913e87fd9eea698ea81f33048a6a` |
| `final-integration-review.md` | `b09fe13c24e01b1bc18ef02a77601c6c218e4264` | `0cebc77c6580f2d871437ba41aed89dc47d4fe43454d47855649d7bfd2959979` |

新14 G记录的完整 original/approved 对象、完整 qualified control、主责和各 contributor 集合与原 D/批准合同及固定独立报告吻合。新行328–341仅登记 NEW2 候选门；actual review 是 PENDING/NOT_PERFORMED，B21 C/关闭/FINAL均未执行。管理 M 的 `actual-freeze-1/public-registration-actual-binding.json`，blob `d0e709cfb0e858fbcc3b90e0a7b8242fb58b21ba`、SHA256 `1d0a3d8891653b8049fb2699114ec9178e895ab9d3e8940fb69e503e71e66a8d`，逐行把 G 与精确 ACT/tree 绑定。`EXTERNAL_ACT_FREEZE_REQUIRED` 因此有外部精确冻结，未写成自引用或伪 actual PASS，也未改旧327的实际绑定。

G9-3五管理限定、九原输入批准与 B01/B18 真实 scoped receipt/trace 保持，且本次另读新增 G 管理层。B01 GIR001 receipt0/trace1、B18 GIR001 receipt276/trace277、B18 R02 receipt283/trace284不转授 B21；九原输入资格不自动接受 WP75 新字节。GIR003 已接受 contributor 在新 G 中按批次排序，旧签名对象及 TSV行仍全字节不变，集合与原12 owner一致；没有重签或减少旧贡献。

原 NAV-001/NAV-002、C029 勘误及九修复涉及的真实消费桥未回退：FD003 root与ext4/9/10分别关联真实编辑、战斗/槽、场地/菜单、队伍/生命周期域；CFG25/26、SRC392/393保持机制/样本/内容/启用分层；C029仅旧B20接受贡献，B05机制与B19编辑是另具名消费者复用。54交界/8链及432 source、35 config/17 UI后继全字节同 NEW2；当前111具名消费者与 ACT 对应，原47批准scope与14项原对象/资格未变。

ACT 本树不含32个 author-draft-1 证据文件。正式22输出中14个 author 命名空间引用均能由管理包固定 NEW2 inventory 或固定 P2 freeze完整归属消费，未映射为0；公共 trace 新行亦固定 whole_author_trace/nine_repairs 的 commit/hash，G固定 dependency-refresh。**此为外部固定证据导航，不是 ACT 本树相对链接存在的声明。** 本合同允许固定外部证据，不要求无变化作者整包递归物化；其缺席不等于 C旧证据被删除。旧scope/旧案例指针保持各自固定快照的行号，范围同字节复用不冒称整个当前文件未变。

详细当前资格、14 G记录、导航字段映射与限定理由见 [导航与公共G独立子审](navigation-and-public-G-review.md)、[机器证据](navigation-and-public-G-review.json)。

## B20 新字节与 B03/B14/B19 actual 回归

本次核的是 ACT 实际 after：两 WP75 §8.6 和 MR18–MR22及其消费桥，与已审 NEW2完整字节一致，但新段落仍独立复核 actual 条件；没有把 B20历史 PASS扩大到新段落。固定旧 NEW2 的 [独立路线判断](https://github.com/y805939188/pokemon-essentials-clean-room/blob/53a14af81c1c139da047c51450a84aa7bee9b225/review/remediation/20261003-prepare/batches/B21/affected-review-cloud-20261011-2/b15-b20-and-route-review.json)，blob `b49e5debf7b5c922cd48eab922d3a9c5fc035866`、SHA256 `5020436545d9061370ed984ec8a2bcb467b1c459999dc1c2d04e297cc9ca14a8`，仅作为同字节、同资格语义来源，不代签 ACT。

WP75 当前限定仍是：整个求值正常返回后，检查任一行行首三个精确大小写字面；命中推进后结束帧，无命中推进后同帧继续；异常先于分派器判定和后续推进，不承诺回滚先前脚本副作用。空白/接收者/大小写变体只拒绝该行，其他行仍可命中；长后缀是字面前缀匹配，不保证方法签名或任意字符串求值成功。有效角色/列表/文本、正常返回/异常和后续循环机会仍为未执行静态前提。

WP13 原/最终全字节同 C；最终稿 blob `b79888af1ce084dc0441b0688661b5c4511f029c`、SHA256 `8eca09260fa1ab57791542cfc250ae51ea0e13dab7456d85c3e0a1d5704ef5aa`。目录删除唯一新增段可还原全部 C 旧字节；MR01–MR17完整行/顺序/次数保持，特别 MR08。MR18–MR22覆盖后续行、ASCII空格、接收者、UD/LR长后缀及整体异常，未执行任何案例。

两WP75 ACT blob分别为 `3d8b2744c200484fc4a5dcdac2b6fb38542a6a19` / `b2221b3a1793a579cdfbfc74f4bc1e8ea54e23d0`，SHA256分别为 `0db98a17ecd51cc69e7ccc307a97e103d5211585016902f669e226a5f6e7ec75` / `2968e3946a4ab751fcdb3d2dda241b3e94f6c4e49c04fe07b0494a5d6c9631a5`；engine目录 blob `90d0b2513cbcde582ad62189efae93153ccbeab1`、SHA256 `328093fecfc874cab446a8b969ca8e78889842643fb5859edb2ddea7dcfd17fc`。

B14时间/色调、B19编辑白名单与转换/治疗/提取/编译方向边界未扩张。35转换字面及 ASCII/原顺序保留；治疗首字符预检、续行拼接、删空白、精确匹配，以及原少删1/单行不终止/部分输出限定均未因路线摘要成为执行保证。G7-4/G8-2/G8-3、CHAIN-6、SRC040/314当前桥指向 ACT 实际 after；新 G只登记，未引入调用/异常/激活新行为。参考静态来源仍固定 `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`，同字节旧 source 证据归属复用，不重新执行或泛读整库。

详见 [B15–B20与重点接口 actual 子审](b15-b20-interface-review.md)、[机器证据](b15-b20-interface-review.json)。

## 全部20 owner的 actual 处置与保全

每行均为本次精确 ACT 的限定 affected PASS，不是重签旧贡献。未受影响依据是完整差异、具名读写/调用/异常条件、同字节对应和有效旧资格共同成立；单独 same-ID、same-blob 或 old-PASS 不构成通过理由。当前公共 G 对这些域只更新状态/固定证据绑定，未改变其调用条件；支持范围在中央后继中未扩张。

| owner | 旧贡献/primary | 本 actual 的具体处置依据 |
| --- | ---: | --- |
| B01 | 14/7 | 配置/PBS机制、样本、启用分层不变；Shadow已读与未读资格、CFG真消费者保留；G9-3及新公共G另核，无混签。 |
| B02 | 12/9 | 日期/uptime/游戏秒、保存/迁移/语言条件和部分失败未受G登记影响；统计不冒充关闭。 |
| B03 | 27/19 | WP13原/最终与旧案例保全；ACT WP75/MR18–22及天气局部/连接后写门另核。 |
| B04 | 35/23 | 世界显示、资源/音频/命名资格保持；天气意图/显示与单强度/渐变守卫未扩张，新目录行另核。 |
| B05 | 16/10 | Shadow已读样本/启用未知、形态/PP/学习/友好阶段门保持；C029仅B20贡献，B05机制复用分列。 |
| B06 | 10/7 | 对象、容量、接收/背包预检与提交条件不改，取消/部分失败的旧限定有效。 |
| B07 | 19/12 | G2-4周期后逐成员独立1/2与归0同已审条件；成长/学习/进化及部分提交没有新的G执行保证。 |
| B08 | 17/9 | 繁殖/孵化与OldRod/漫游/雷达旧接口保持，CFG/L09仍指真实WP35生命周期消费者。 |
| B09 | 20/13 | 伙伴移位、注册/执行/音频限定不改；FD003呈现由真实B17域承接，A059原row155保留。 |
| B10 | 7/2 | OHKO资格、HP/参数/伤害入口及反向前提不改，中央设施摘要不扩大异常或数学支持。 |
| B11 | 6/3 | 几何/near-neighbor及特性/持物阶段、具名调用者与部分失败限定保持。 |
| B12 | 9/6 | AI上下文/评分/特殊战不改；收获机制/UI关联保持，没有新增最佳策略保证。 |
| B13 | 8/5 | 快照仅begin写、玩家队伍四入口、nil/[]、取消/结束保存及经验/物品顺序保持。 |
| B14 | 24/19 | 时间四通道、色调/场地条件保持；ACT工具消费方向及G7/8/CHAIN6回归另核，FD003 ext9真域保持。 |
| B15 | 16/10 | 电话/地图/邮件/礼物共享状态不改，FD003 ext9实际owner和限定导航保持。 |
| B16 | 24/20 | 容量/BoxLink/队伍/命名及部分写入保持，FD003 ext9/10和真实row241分层有效。 |
| B17 | 12/7 | WP67呈现/交互/生命周期及WP76槽序/失败不改，ext4/10和真实row265有效。 |
| B18 | 8/5 | 九原输入限定批准与小游戏前提保留；B01/B18管理贡献、新G登记和actual门分层另核。 |
| B19 | 24/19 | 120参数/编辑白名单与治疗/提取/编译边界保持；ACT路线消费桥、FD003 root和scope资格另核。 |
| B20 | 19/15 | 两WP75新段另判ACT；35转换/ASCII、三个精确字面、WP77/C029及Demo限定保持。 |

[全部owner处置](owner-dispositions.json)记录20精确actual处置、各旧receipt计数、B01–B14的106个当前consumer身份及固定旧证据归属；B15–B20详尽证据在子审索引。B01–B14有效旧语义来源固定 R 的 `b01-b14-fixed-evidence-reuse.json`，blob `53145141791a405e6d3bb2929e4940c0c0fd3288`、SHA256 `be76022e4f87cd11943b73ef22e6267805abc2f2e07308fe3f343a62cceef697`，按 `/owners/0` 至 `/owners/13` 复用，不复制旧报告整包。

327旧receipt逐对象规范化hash同原独立证据，C统计全字节同ACT；sorted-key compact数组 SHA256 `ca73d8b68c03e80e40066acb4349683836f8165a4f2daa5935cfef8b852cd9fa`。G的 `a265c9218a0a39996ef8c543a01e16f5a9a1e0d1be5e46c741b9055859c3db43` 是保留对象键序 compact JSON 的同数组身份，两个序列化规则不同，未误判为对象变动。所有20 owner回执与原D完整accepted dependency严格对应。

36,837受保护路径 mode/type/blob同 C；其中2,828旧批次证据不变。参考、AGENTS、旧接受、本体及除scope3外的原稿/案例均保全。229finding ID/顺序/OPEN保留，未分配215行不变，分配14只追加原closure_gate限定；旧中央Markdown字节层和JSON字段保留。历史138实际数组及158原标签继续固定归属，不覆盖原签名。

独立导出的当前统计为20接受批、327贡献、228触及ID、220主责最低、215整项严格、14待B21贡献/9主责、229 OPEN/0 CLOSED；21/341是未来投影，不是本次接受或关闭。1092项根元数据检查无错误，仅说明身份/范围/保全方法，不代替上述语义判决。新 [审计源码](static-audit.py)只运行Git/UTF-8 JSON/TSV/hash处理；原旧脚本未执行。

## 执行边界与后继验收

参考游戏、Ruby、编译器、转换器、参考反序列化器、行为向量、旧脚本执行均0；静态案例执行0、运行观察0、真实Demo链0。U01–U10/G01–G12/AX01–AX20、未读/备份/资源/宿主/插件/动态调用/缓存/激活及原异常资格全部继承，67树果完整目录仍条件性。模型参数按协议接纳，不做模型/额度审计或CLI替代。

本 affected actual 门已满足：全20 owner精确actual处置、327旧接受保全、scope3与全部支持接口回归通过，公共G与冻结ACT消费层无剩余阻塞。FULL actual须由其原独立角色另行协调；两actual门及各发布/读回证据齐备后，唯一登记员才可执行B21 scoped14接受。其后仍须原FINAL-1、有证据的逐canonical关闭/最终冻结、FINAL-2，不能从本报告转授。

报告分支只新增本目录，正文/main/参考/旧报告/旧证据没有改写。输出身份清单记录本次payload；普通发布后的独立远端回执记录首轮全部输出，最终提交的全部输出（含回执自身）再独立远端完整读回并在交接提供精确report commit/tree。回执不递归自嵌所在提交身份。
