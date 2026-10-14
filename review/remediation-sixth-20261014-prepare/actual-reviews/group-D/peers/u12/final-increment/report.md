# U12：最终 86bbc 输入的增量独立复审

**GR6-UI-BAG-001、GR6-UI-BAG-002 均 ACTUAL_PASS，限最终输入下具名静态内容；必要修订 0。** 本次明确重绑最终身份、读取全部新增／改变记录、核验未变内容与新增接口范围。旧 9d 报告保持原样；本结论不签其余七个 Group D ID、U13 八项或全部56项，不登记正式接受／CLOSED。

最终 commit `86bbc99b28d93db4ed9d6897daf5f3725ccd1808`、workspace tree `67e8c55d520fa8cad2928cb4b95e24c3ed602d5a`、formal tree `ebbe29f2bc88cd17de7072bf440c6fa8c8c7089c`。最终 `integration/U01-U14-final-composite-20261014/actual-review-input.json` 为152860 bytes／3243行，SHA256 `4671c1c31f18858a7719e88533029d746c62dfb77d4239cbb0cae633e79863da`、blob `ccf79b03165573f27070a417a2e3d986907f6623`。累计14批56项／53正式文件；Group D 仍 U10/U11/U12 三批九项、11个实际文件，当前579648 bytes（原576898加domain目录2750），不能把旧总量用于最终版。

## 完整增量读集与独立字节核验

先前实际 input 全2661行语义阅读及身份仍固定于9d；本次完整读取13个新增／改变 root 字段，新增 `/batches/13` U13全记录，22个新增／改变 `/files` 记录的完整变化字段（其中6个全新完整记录），以及 `delta_from_prior_actual` 全部字段：8组 before/after、45个未变路径、原 C/D 实际审查身份及共享接口条件。其余13批记录与复用字段逐对象精确相等。将全部增量接回旧全文对象后，与最终原 JSON 完全相等。这是完整新增／改变记录阅读，不冒称新输出3243行逐行全文，更不是56项内容审查。逐指针与工具输出收据见 [final-read-receipt.json](final-read-receipt.json)、[semantic-input-delta.json](semantic-input-delta.json)。

独立 Git diff 确认9d→final只有8个正式路径修改：WP40、WP54、WP55、WP56、WP58、WP53、combat设施目录、pokemon规则目录，均没有新增／删除正式路径。每个 before／after 的完整 bytes、SHA256、Git blob 对 input 都匹配；全部53个最终实际文件的 path/mode/type/bytes/SHA256/blob 也逐一匹配。字节身份不授予其它文件的语义全文或接口签名，详见 [final-static-checks.json](final-static-checks.json)。一次合并8路径 diff 输出发生截断，明确不给全8 patch语义阅读信用；相应实际全文由各指定审者读取，未以截断输出充当完整阅读。

| U12 实际全文／共享目录 | 最终 bytes | 最终 SHA256 | 最终 Git blob | 与9d关系 |
| --- | ---: | --- | --- | --- |
| WP27 | 25470 | `10c14321e5ba28a2992bcd255cd9f3c6face23cb892115d01f5ce34a7757fe1b` | `1a231d8373ba8f9d7903f5d234b4e47cac99529c` | 全字节相等，223行旧新实际全文阅读资格复用 |
| WP29 | 19150 | `564fea440a6dd7fe177098bdfab4f7b3cbff4e6fa674ea29acf5b879da1ed90f` | `76d5db6ceba8689f300f723e08261181c00c7b81` | 全字节相等，212行实际全文资格复用 |
| WP66-C | 29800 | `6b2b6137af53472b31580137ffdcfb4daec71a821f4d0f489d12e4b9d681939f` | `418dcd5a6fb29e3c20a7bcf87e61ba9363ff7061` | 全字节相等，210行实际全文资格复用 |
| UI catalogue | 170395 | `b4edb87c39ad8f9ec9f0572b55464d3f46f3d1da755ee578d33e2cef4ae546e5` | `4bc6fcda1473e6d31870dff079ba111bee97567b` | 全字节相等，1026行；只复用本人原登记片段，团队全文由root汇合 |

最终U12合同、WP17、九个原反证完整载荷也与9d全字节相等；固定R commit/tree不变。旧源实读的 BPShop525、Bag704、ItemStorage376、容器301及实际代理／AdvancedText／尺寸／update／Messages／GameTemp等消费者范围准确复用，不增加新执行或新全文信用。旧报告 [report.md](../report.md)、[report.json](../report.json) 的逐ID七组和 [supplemental-read-receipt.json](../supplemental-read-receipt.json) 有明确冻结范围；本次另作最终有界裁决，不能把未变身份本身当自动迁签。

## U13 producer 修复的身份与限制

新producer候选 `9971fe84896786645cdcda3ab45e5caf7785cabc`，tree `93ebe95d038954fd0dfb14fd07ac2f95a2485baf`，mirror tree `13d502e4131ace3e8fe2e59ce07a338b98ff7967`；独立修复复审 `411b563309a4e642e628dcf8289e36c6fe3fd37f`，tree `c34fc75d13828a49322203455073d475431395bc`，repair报告目录 tree `9c654f8b8cd59c427989bea23958bdd360dcee1c`。其 `repair-01/review-report.md` **完整新读**，11273 bytes、SHA256 `1445036698ffb92561fd87c121310ee65dac157f038b7ab098e5ccb21710970a`、blob `04df5bf6c83056ed44697f379a306ed5f3476d32`；上述对象及8镜像身份均独立匹配final input。U13合同370944 bytes仅身份核验，不给本人U13七组语义审查信用。

独立比较旧FAIL候选00b45de与9971：candidate目录18条A/M变化，没有该范围删除；8镜像中7份完整不变，唯一pokemon测试目录第40行SF30变化577 bytes。新SF30完整原行实读，d正常结束→保存→普通载入保留持久统计，运行／单调时钟未知，未执行真实保存／载入；e固定默认转换集合无Safari／捕虫专用转换，不外推插件、版本或整个存档没有迁移。原d/e正常对照恢复、a/b/c门保留，行ID未增长。修复报告明确旧候选 `00b45de642f07cee9953e42f04cce9c35d77346f`／独立审 `3ef4854ef43eac92fd1dc57350e4cf6aa160082b` 的 **FAIL仍保留**；两对象均可读，修复不回写它们。

旧9d报告的“U13未接收”是当时事实；本次独立PASS来源已经接收，只在此新增记录更新当前状态。候选PASS不等于U13实际producer/receiver接口通过：WP66-A在9d已接收且最终字节未变，但新WP54/QC、0/1/3、raw/Standard negative、focus、first-error、nil/empty接口仍须storage/root实际新核；新domain/WP53全文由pokedex负责。本人没有替其签核。U13修复审及本审的有效model/effort/tier/speed/UUID均UNVERIFIED，源定义／作者脚本／行为模型／宿主／真实保存执行0。

## 两项最终七组裁决与接口判断

**BAG-001。** 身份、required/P3、无别名和原裁决不变；最终正文及双向定位 WP29:88、WP66-C:120–121、BP01–04:1018–1021 字节不变。固定BPShop先同列表过滤、nil默认2／普通自定义1替换、buy正常返回共同2告别清覆盖链仍成立。省略／Custom welcome正常对照、同列表提前提交及首问候／购买错误无ensure尾的反例重新按最终输入域确认。原价格20×3显示30实扣60、21×3显示30实扣63、退款／统计／容量partial范围保留；新增U13队伍、保存或战斗变体条款没有改动这些正文与固定消费者，也不授新的尾部恢复或宿主结果。原独立反证、九载荷范围与历史资格继续限定；本ID最终 **ACTUAL_PASS**，必要修订0。

**BAG-002。** 身份、required/P3与C12“原终态2正确但提示阶段缺失”的裁决保持。最终 WP27:121/125、WP66-C:64/84/90/157–158/184、C12:334、C36:358、TS01–05:1022–1026 全字节相同。普通Bag有效5选3/Yes显示入口仍5、正常返回三次删1后2/刷新；PC先整批删除check到2/刷新再提示；数量BACK0、No与重要守卫不变。提示错误分别保Bag5未删与PC2已刷新；真实三行／最终两行／逐字／持续正常更新／无外部恢复的busy限定仍只有静态推导。新增U13规则不触及该库存时点、partial容器形状或WP17局部恢复门；普通显示、短确认、商店及战斗列表的不同域保持，不把相同终态或checked删除推广为同步／原子／回滚。最终 **ACTUAL_PASS**，必要修订0。

逐ID七组当前记录见 [report.json](report.json)，与冻结旧七组通过精确身份／读集衔接。UI完整三贡献块、两个EOF块、C12/C36有意替换和其余721旧表行资格都因整个1026行blob完全相等而保持；721含表结构行，不是新执行测试。九个U12向量均NOT_EXECUTED，旧有限probe运行信用不移入本轮。

## 恢复后的历史原节点新读

父方后来成功取回 `c0ff33024aea424c68d29f9778fe7c8e807d21e8`，本次在final-increment独立完整读取9个精确原 `historical_identity_scope_reuse` 节点：R4 M10-001/003、R3 M10-002/003、R2 B06/A038、B07/D023、B16/B035/C117/D023。三份完整大原载荷 bytes/SHA256/blob/mode独立核验，全部9节点的UTF-8 `sort_keys=True`／compact JSON SHA256都与原绑定相等，原身份tuple和pointer完整保留。[recovered-history-nodes.json](recovered-history-nodes.json) 保留全部选中原节点，[recovered-history-read-receipt.json](recovered-history-read-receipt.json) 记录范围与身份。

新读只给这9个完整资格节点信用，不冒称3大原报告全部语义阅读，亦不授旧PASS迁签。B07是deferred partial，B16只assigned local UI，B06原局部贡献；两owner的D023独立，不合并。R3三数量入口与战斗列表busy域、R4数字／命令和测量折行域均保原前提，不外推物理输入、字体或所有长字符串。旧9d记录的c0ff缺失／exit128失败时点保持原样，此处列“恢复后新读”，不倒补当时成功。R1原WP和R5 selected92／51P2/41P3等精确资格沿原独立范围保留，G03/G09 FAIL、U03 FAIL修复、两advisory mismatch、SC-U07-001 LF错误／纠正不抹掉。

当前U12没有内容阻塞。余下Group D其它项和新producer/receiver联合接口由本轮指定审者汇合；公共同步R6-I、正式接受、CLOSED分开。请求gpt-6.1-sol／ultra／default普速无有效回显，全部UNVERIFIED；无CLI配置probe、spawn、作者代码、参考Ruby/model执行。只写本final-increment目录，没有修改旧9d报告或candidate/formal/public，没有提交／切branch／push；共享HEAD由父方切至最终审查branch，本审只读取固定Git对象。
