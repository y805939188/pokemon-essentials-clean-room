# R6 最终实际合并独立审查：group-C

结论：**ACTUAL_PASS_SCOPED_STATIC，19/19；FAIL 0；最小实质整改 0。** 本结论只覆盖 U06 四项、U07 七项、U08 五项、U09 三项及它们必要的共享正文／消费者／历史回归。候选 PASS、本文实际范围 PASS、全局正式接受及 CLOSED 是不同阶段；本文不登记正式接受或 CLOSED，也不代签其它组。

绑定实际 commit **`86bbc99b28d93db4ed9d6897daf5f3725ccd1808`**，workspace tree **`67e8c55d520fa8cad2928cb4b95e24c3ed602d5a`**，formal tree **`ebbe29f2bc88cd17de7072bf440c6fa8c8c7089c`**。[最终输入](https://github.com/y805939188/pokemon-essentials-clean-room/blob/86bbc99b28d93db4ed9d6897daf5f3725ccd1808/review/remediation-sixth-20261014-prepare/integration/U01-U14-final-composite-20261014/actual-review-input.json) 为 152860 bytes／SHA256 `4671c1c31f18858a7719e88533029d746c62dfb77d4239cbb0cae633e79863da`／blob `ccf79b03165573f27070a417a2e3d986907f6623`。全部 53 份正式载荷身份独立核验；这只证明身份，不生成语义结论。此前实际输入 `9d5b4e99b617828690e6529b77a1e555d7c9eb1b` 不是本签名，未把其结果转签最终版本。

固定 preparation `469a268b92daed7b4d28d7fd0da75520cbb7228f`；正式 baseline `8ea169fbd0f33f378b5d732fd6bea59e854e04a6`；只读 reference `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`／tree `7589c800b61ba13a13040ed0d686979b80a84fd0`。适用根 AGENTS 完整阅读并核验，最终 bytes 6328／SHA256 `41cea9c6aa439dc70eaca2c26ce1f7967a887538c1aef25b9297c07b0437ff40`。只写本 `actual-reviews/group-C/`；候选、其它审者报告、公共 ledger、正式正文、Mac 和 main 均未修改。

独立审者为本次直接审查的 R6-U07-R／group-C；用户声明审者 thread `01a13acf-046d-764f-b8fb-1ea14dcf6002`，与候选作者不同。实际 runtime thread／模型回显不可得。请求 **gpt-6.1-sol / ultra / default tier / default 普速、fast=false**；实际模型／effort／tier／speed／任务 UUID 全部 **UNVERIFIED**。没有 CLI 配置探测，没有子代理。参考函数、行为模型、向量、编译器、编辑器、原生宿主、Demo、真实存档执行均为 **0**；本目录 Python 只处理 Git 字节、JSON、身份、范围和报告，不实现或执行参考行为。

逐 ID 完整合同、七组字段、原提案及非提出者反证已读；U06/U08/U09/U14 采用可重构的完整 JSON 精确值去重阅读，未省略任何原始键值。U07 复用同一直接审者此前完整 371765-byte prompt（SHA256 `d787ad55e3965afafb1332c7b085c2555dfd86e8fdfcd15607b309ce85cdd1df`、blob `f8b65f62b4101faf554f9898fbe014aaedb3950e`）、完整合同、七份全源文件 5130 行及原反证的确切阅读；七份 reference 字节重新核验相同。此前候选报告 `44e3b725850315c8f050fcdd8cb1e88d5bd5c5ec` 保留，其候选结论没有转为本次实际结论。

当前全文读集 13 份：WP27、WP72、WP73-A、WP73-B、WP74、WP75、WP03、WP04、WP08、WP62、DX 共用测试目录、内核测试目录、WP67-A。其中十一份当前完整正文按连续有界段阅读；DX 目录和 WP67-A 的每一行通过“此前本人完整读过的固定正文之精确相同连续段＋全部新增／改写段”重构为当前全文，重构断言等于全部当前字节，两个完整增量均已读。不能把完整读集变成其所有无关 ID 的新全局签名。WP12／WP17／WP29 的必要消费条款另作有界全文单元阅读。

| ID | 独立实际结论与决定性证据 |
| --- | --- |
| R6-B-001 | PASS。MapsAndEvents 348–400：表属性访问抛可捕获错误的诊断仅 tilesetID/mapID；非空 tile 的 passage 查询无结果才产生 map/x/y/一基层。WP75 §10/§15.1、CV-M24 准确分叉，合法查询及已写前图不回滚保留。 |
| R6-B-002 | PASS。生成列表免费为容量门→提示→接收，收费为资金／容量门→扣款→提示→接收。Interpreter 101 同步返回前不执行 355。钱1000/物0的首提示分别1000/0、800/0；继续接收的获得消息仍0，成功入包才1。拒绝／提示失败前缀、WP27 内部消息与 WP29 普通商店分开。 |
| R6-DX-E001 | PASS。Species.editor_properties 真正绑定一般 Types 池；三个不同类型及注册伪类型可提交，无双槽限。专门类型选择器排伪类型仍正确。Apply／父 Yes/No/Cancel、入口原地 uniq、所有实际池绑定、登记→dat→基础 PBS 和后段失败逐层保留。 |
| R6-DX-E002 | PASS。Writer 291–351 先用非零形态后缀选路径，再输出同后缀基础记录、仅对相等非零形态省节。仅基础／同后缀差异／同后缀相等／异后缀四例齐全；WE-M20 主体正确，旧 WP73-B §7.5 正确条件、查询副作用和布局边界未被误改。 |
| R6-DX-AN-001 | PASS。保护计数仅0–59；0/2两使用者可删0，2换60后只计1拒删，换回恢复。存储／Copy／TAB／锁定／Clear 当前帧守卫／常规播放范围分别保留。 |
| R6-DX-AN-002 | PASS。Delete→BACK 后集合成员B与画布A脱离，Focus写B、新增读A、保存／导出读B。普通同对象／取消／明确Load／缩容nil失败均保留；U09磁盘和缓存区分没有误设对象重新绑定。 |
| R6-DX-AN-003 | PASS。播放器构造时捕获中心；user槽0移至200后普通user-focus槽2仍请求128，预览264/192。target／Screen／已建立双方线／静止／显式球爆覆盖分别核。WP67-A §9.4和新准备背景接口不矛盾，正常恢复不扩大为异常确保。 |
| R6-DX-AN-004 | PASS。Batch11项各范围及独立初值逐项核，Opacity17只勾直接255、Zoom X100、Priority Front1，未勾／取消／空槽不写。GradientX550打开工作500、勾选确认500、取消保留550，合法20保留；即时钳制／nil参与门／共享属性不合并。 |
| R6-DX-AN-005 | PASS（具名覆盖补全）。类型正确 length1/frame0nil/graphic空/timing空可越过转换和槽替换，后续画布更新才在局部导入 rescue 外失败。旧槽不恢复、缓存别名可见、尚未保存／清理／BGM恢复；有效帧、错类型／编码及替换前失败分别保留。 |
| R6-DX-AN-006 | PASS。同窗P→重开Curve→尚无线BACK清显示点却保留P，随后OK可写旧P／先扩帧。首次nil不写、已显示线才换新P；外层取消不写。Freehand首阶段ESC换空对象，OK先扩帧再失败；记录阶段ESC保留。 |
| R6-DX-AN-007 | PASS，仅 required P3。自动中间点0.3333/0.6666请求约99.99/199.98，区别精确100/200；显式拖动四点N5的0/.3046875/4.375/9.1015625/11不被替换。一般N浮点端点独立 optional、宿主量化未知，不新增逐位兼容必修。 |
| R6-DX-DEBUG-001 | PASS。空请求2→入2/消息2；998请求2→入1/false/消息2；999请求1→入0/false/消息1。取消0、部分后消息失败、无限口袋、填包重要数量／容量边界和 U14 名称默认分别核。 |
| R6-DX-DEBUG-002 | PASS。warp两分支均在返回true前同步地图事件→公共事件刷新、清请求。独立Refresh map只直接置请求；其后消息微更新可消费，因此真实效果返回时仍true/计数旧的过强观察点不成立。当前 DG-U08-07 正确限定到消息尚未更新时；取消／后项失败保留前缀。 |
| R6-DX-DEBUG-003 | PASS。F9按住新登记受消息／解释器／冰滑上下瀑布及先键分支约束，行走可排队停后消费。旧请求消费不重检新门；WP12明确强制路线WAIT与三自动移动标记不同。debug假／暂停优先／清标记后失败均核。 |
| R6-DX-DEBUG-004 | PASS。PBDebug.log_score_change的0在所有输出门之前返回，已有缓冲保留。±1、两标志门、显式flush关标志仍清、文件失败前缀及独立异常打印核；AI评分和新Arena技槽不混同。 |
| R6-DX-DEBUG-005 | PASS。查询／传入性别但活动建议不消费；Ada Lovelace两性别均Ada，长度严格＜max，去尾数字／完整用户名capitalize截断／空用户名及拒默认名均核。keyboard min0 ESC空、cursor BACK删字，未读真实用户名、未改设施随机名。 |
| R6-DX-COMP-001 | PASS。运行中compile_all(true)与main启动检查分开；Status/Power40坏项之前types/abilities可已新保存，moves内存前缀／旧dat／未完成窗口释放正确。启动预删／诊断后删除仅尝试，Reset/SystemExit／早期无清单保留；007导入及全合法直接完成对照齐全。 |
| R6-DX-COMP-002 | PASS。预载区域A→合法B编译得到盘B/查A，反写PBS A/盘B；冷缓存及地区编辑Yes显式失效另列。动画集合／关联两缓存、零有效名不写、独立连接缓存和Game_Temp重建不等价，宿主reload_cache仅请求。 |
| R6-DX-COMP-003 | PASS。普通A已登记、B内缩进独立#行经prep变空后非法属性拒，B未登记／终检save未到。列首#／空物理行、首节前错误、专用trainers先prep略空、普通／q井号后缀、显式Flags=不同根均核。 |

逐 ID 全部冻结最小修订与验收条件、源上下文、当前条款／目录、89 个独立静态向量组（每组可有多个子例，**不是执行数**）、反向／取消／失败前缀详见 [per-id-review.json](per-id-review.json)。所有条件均有处置；DEBUG-002 的观察点按完整源和共享消息合同作上述限定，不以冻结过强表述否定正确参考事实或跳过验收。候选作者的工具检查／载荷读回数量均不替代本次语义审核。

U14 六个相关消费者已独立接合：收集slash+LF／运行slash+n与后置消息换行、指定UI图片语言身份、有限NamePlural／Type／Move默认、已有部分Metrics／整条缺失克隆、PBS Happiness256／UI255、Flags空属性[nil]／蛋先2→1再失败。这里只核 C 接口，不授 U14 六项整包实际签名。全部前提和未证边界见 [interfaces-and-regressions.json](interfaces-and-regressions.json)。

最终增量只改变八份正式文件，[final-formal-delta.patch](final-formal-delta.patch) 完整343行已逐段读完；13份C读集与9d全字节相同，仍重新审查相关消费者。Arena状态／技分与AI零差日志分开，世界准备在录制捕获之前／回放不再准备，Palace登记与动画缓存分开，普通QuitGame共享保存与专门Save可见／模式退出／调试计时分开。重载单调时钟未知仍保留。GR6-F-002 的WP66-A接收0/1/3、raw-negative／Standard-negative、首错／焦点／nil-vs-empty整组实际验收留其独立主责，C不代签。旧U13 FAIL `00b45de…`／`3ef4854…`与修复候选 `9971fe8…`／候选PASS复审 `411b563…`均保留，候选PASS不自动扩大为全局实际PASS。

必要历史按精确scope回归：R1原WP范围；R2 229/21/341不同分母、九个新增精确原始指针字段读回及既有U07精确动画记录；R3 23/76；R4 17/76与B5限定16/75、GR4-M10-004全部三条件；R5唯一最终92CLOSED/51P2/41P3及旧FAIL、MISMATCH、LF原误判与修正历史。当前实际保留 last-user／slot60／别名／共享层／N/N+2／取消写前缀、池排序／Metrics路径、35转换／治疗非终止／分页丢行／页条件、loader／六旧战斗族／门配方／Boolean累计等各自限定。未选历史记录只作NOT_AFFECTED／导航，未重开全局R1–R5，旧PASS不代新验收。完整记录与来源核验见 [history-qualified-input.json](history-qualified-input.json)、[history-origin-verification.json](history-origin-verification.json)、[interfaces-and-regressions.json](interfaces-and-regressions.json)。

两处机械新增行未逐字匹配只是WP04目录导航合并；实际303行同时有U09 KL37–50与U14 FLAGS，相关行为／案例完整。工具显示截断均用有界缺段回读补齐；日志请求跨度本身不等于完整阅读或PASS。错误路径／报告副本假设／脚本导入错误／一次exec transport中断已恢复，未隐藏成源FAIL。记录见 [execution-and-reading.json](execution-and-reading.json)。

签名范围内没有剩余实质阻塞。其它组独立实际审查、全局正式接受、行政同步及最后CLOSED仍是后续阶段；宿主／媒体／Demo／真实保存与兼容政策未知按原范围保留。本报告不新增行政要求或未来框架设计。发布固定commit/tree、有限载荷清单及完整远端读回记录见本目录 publication-receipt.json、payload-manifest.json、core-remote-readback.json；最终发布版本的全部新载荷再作独立远端全字节回读，固定入口由最终回执给出。
