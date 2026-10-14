# Group D：R6-U12 实际整合后独立复审

**GR6-UI-BAG-001 与 GR6-UI-BAG-002 均 ACTUAL_PASS，限定新静态内容；最小必需修订 0。** 两项裁决按原合同七组直接重验当前正式文本、正常对照、最小反例和实际消费者链。新参考执行、行为模型、原生 UI／宿主／Demo、真实保存均为 0；不是运行通过。候选 PASS、实际静态 PASS、正式接受和 CLOSED 分开；本报告没有登记后两项。

本人签核范围是 U12 两项。Group D 的输入身份／组合核验覆盖 U10、U11、U12 三批九项、11 个实际文件共 576898 bytes；其余七项语义由本轮指定审者负责。文件名 U01-U12-U14 表示累计 U01 至 U12 加 U14 的 13 批 48 项／47 个实际文件，不是 Group D 范围。U01、U09、U14 只作相关共享接口背景。

## 固定身份与读集

当前 branch 为 `codex/remediation-sixth-actual-d-20261014`；实际 commit `9d5b4e99b617828690e6529b77a1e555d7c9eb1b`，workspace tree `faae3b9a22c37a2e2e994553f59e7099c6394db0`，formal tree `74dccc64506d008d50cf1cdfd906f701931020cc`。固定 main 为 `8ea169fbd0f33f378b5d732fd6bea59e854e04a6`。参考 `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`／tree `7589c800b61ba13a13040ed0d686979b80a84fd0` 仅在 clean-room Git 对象库只读，不 checkout、不 source、不运行 Ruby 或作者程序。

实际 input 全部 2661 行新读，124082 bytes、SHA256 `7b63483a915792c077b2f8cf84208e9f5a7ac94e55ce93cfc8bbde718bf6d9aa`、blob `f7f220a4ee7c4b2ff6dc94b799fe54b13879b6c8`；分段 1–440、441–920、921–1410、1411–1910、1911–2390、2391–2661。U12 合同全部 1288 行、63698 bytes 新读，SHA256 `a6495dcc42d58188354488cc60a3272b596e3429efbe4b96e02500b00529555e`、blob `f9e14c8ba48fc4627eaefee0ff9b7730d55e72a4`。U12 候选 `caa090d8e396c08b09fb2d4d5067aa00f4d6c3cb`，tree `8f29be65173bb29d160aed74dbb6f7378fa81c2a`，mirror tree `6de96e3b11c39a1f7ee5531d2629532cee00ce90`；原独立复审 `d7460b2a689245671e1b4f9c00da8d930113218d` 的 `reviews/R6-U12-R/report.md` 55 行全文新读，11671 bytes、SHA256 `c20a528397fa7e56f5c2a11bc307cc3222154adf4db595687b241800506e3997`、blob `822e323e013f7244ae16bbccbaf8736d91db393a`。原候选 PASS 仅作来源，没有替代新实际裁决。

根 AGENTS 在同会话前一任务已完整读取，本次固定字节复核一致；相关 `.agents/skills` 缺失已检查，无可用本地技能。请求配置 gpt-6.1-sol／ultra／default tier／普速；有效 model、effort、tier、speed、Fast、平台 UUID 均无回显，全部 **UNVERIFIED**，未 CLI 配置探测，未另 spawn。

| 当前实际全文 | 行数 | bytes | SHA256 | Git blob |
| --- | ---: | ---: | --- | --- |
| WP27 | 223 | 25470 | `10c14321e5ba28a2992bcd255cd9f3c6face23cb892115d01f5ce34a7757fe1b` | `1a231d8373ba8f9d7903f5d234b4e47cac99529c` |
| WP29 | 212 | 19150 | `564fea440a6dd7fe177098bdfab4f7b3cbff4e6fa674ea29acf5b879da1ed90f` | `76d5db6ceba8689f300f723e08261181c00c7b81` |
| WP66-C | 210 | 29800 | `6b2b6137af53472b31580137ffdcfb4daec71a821f4d0f489d12e4b9d681939f` | `418dcd5a6fb29e3c20a7bcf87e61ba9363ff7061` |
| UI catalogue（个人部分新读，团队全文另汇） | 1026 | 170395 | `b4edb87c39ad8f9ec9f0572b55464d3f46f3d1da755ee578d33e2cef4ae546e5` | `4bc6fcda1473e6d31870dff079ba111bee97567b` |

前三份实际全文已新读。WP27 初按候选 221 行读取，实际新增两行后为 223 行，尾 222–223 单独补齐，不留下假全文信用。UI 本人新读 1–243、319–358、629–644、699–709、743–765、831–840、1012–1026；原前缀虽逐字一致，仍从当前固定实际 blob 新读，没有把旧签名迁来。Root 汇合本轮团队剩余段的完整 1026 行语义收据；本人的整文件字节读取不等同个人全文语义阅读。

新回源全文：BPShop525、Bag704、ItemStorage376、Bag／PC 容器助手301 行。新必要消费者／接口：AdvancedText114–619、Messages687–701、Game_Temp88–94、MessageConfig188–193／484–511、PC入口1–53、Item1–206、实际 WP17 59–160。身份、范围、逐段 SHA、Git argv、cwd、UTC、exit、stderr 见 [read-ledger.jsonl](read-ledger.jsonl)。初始未同步仪表化的读取不补造命令／UTC，见 [supplemental-read-receipt.json](supplemental-read-receipt.json)。

## GR6-UI-BAG-001：ACTUAL_PASS

1. **身份与原裁决。** canonical／root cause 同 ID，无 alias，required/P3 保持；历史生成时点 PENDING 不撤销合同现有已裁必修事实。
2. **双向证据。** BPShop511–525 在任一问候前，先对调用方同一 stock 列表过滤已持重要物品。`text.nil?` 选择互斥默认两请求／非 nil 普通自定义一请求；buyScreen 正常返回后共同两请求告别及清价格。Messages687–701 是实际请求消费者，Game_Temp88–94 定义覆盖清除。当前反向定位 WP29:88、WP66-C:120–121、UI:1018–1021。
3. **前提与最小反例。** 固定参考，有效空库存或可成功过滤的库存，消息／场景正常，普通有界自定义文本。省略或空值给默认2条；独立同态 Custom welcome 替换为1条，两默认介绍不再请求。两正常返回分支仍共同2条告别和清覆盖。立即购买列表取消不恢复已过滤同列表。首问候或画面异常只保已经到达的前缀，无 ensure，不能保证尾部告别／清覆盖／外层恢复。
4. **最小规则。** 实际正文、WP29 同步入口及 BP01–04 齐备条件、替换、正常共同尾。没有改变全价实扣／半价显示、退款统计、资源与容量回退、同列表再次过滤；没有授予媒体或地图实际可达。
5. **新验收与旧回归。** BP01 默认2、自定 BP02 为1、BP03 首问候前列表已变、BP04 两个独立异常分支均无正常尾保证，逐行按新读源重推。C20/C29/C30/C31/C32、B16-B035/D023 保留原字节与原序；20×3 显示30实扣60、21×3 显示30实扣63、先加失败后的局部回退形状与统计保持。旧资格只按下节精确范围使用。
6. **独立反证。** 检验“正文只指省略”“自定追加默认”“自定应改告别”“请求就是原生输出”四种解释：显式登记参数、互斥 nil 门、共同后继和请求证据层分别排除。裁决来自新源／实际文本，不由作者脚本或自报 PASS 代审。
7. **依赖与接收。** WP29／WP17 请求消费与正常尾是具名依赖。共享内容与本组别项独立保留；R6-I 负责之后公共同步、正式接受和 CLOSED。本人的实际通过只涵盖该 ID 新静态内容。

## GR6-UI-BAG-002：ACTUAL_PASS

1. **身份与原裁决。** 同 ID，无 alias，required/P3 保持。C12 旧聚合最终数量2正确，问题是提示中间阶段覆盖缺口，不把其逗号升级成已经证明反序。
2. **双向证据。** Bag522–535 数量／确认后先成功提示，再在正常返回后 `qty.times` 默认删1且不检查返回，最后刷新。PC673–704 先 checked 整批 remove(qty)、刷新，再成功提示。两个 scene 代理实际进入 ItemStorage200–216／241–274 的共享显示／确认；PC1–53 接正确 Toss 场景。容器103–108／226–229／284–301 给单件参数、整批参数、partial删除，因此 checked 不等于 atomic。AdvancedText 初始化／尺寸重排／busy／pause／resume／update 与 MessageConfig 更新链实际新读。当前条款 WP27:121／125，WP66-C:64／84／90／157–158／184，C12:334、C36:358，TS01–05:1022–1026。
3. **前提与最小反例。** 普通非调试 Bag，有效非重要 X×5，选3／Yes，依赖正常且无竞争库存写入。Bag 成功提示入口仍5，提示正常返回后删1三次到2再刷新；独立 PC 同态先删3检查并刷新，提示入口已2。正常最终均2。数量 BACK0／确认No 均不删且无成功提示；重要物品默认 Bag 无 Toss，PC 直接拒绝且不进入数量／确认。提示有界错误使 Bag 保5、后删及刷新未到；PC 保2及已刷新；两者正常结束未到，外层恢复／回滚不保证。
4. **最小规则。** 两主规格、状态分层表、失败段、C12/C36 及 TS01–05 一致。TS05 限真实 A/B/C 三行、最终两行、逐字、持续正常更新、无外部 resume／改文本。普通显示仅 USE／brief、短确认 Yes／BACK No 与商店可恢复门保留不同局部前提。
5. **新验收与旧回归。** TS01/02 正常阶段差异，TS03 提示错误下各自前缀，TS04 取消与重要守卫，TS05 忙暂停均新人工推导。最终尺寸重排引入第三行前中间 pause；AdvancedText 保持 busy，而共享恢复／退出门要求 `!busy`，因此 USE/BACK/brief 不能使这段返回。Bag 仍5；PC 已2并刷新。既有 U06-M10-001-A..E、QN、CM/NM 原字节保持；确认尚未删除、取出已转移、净化前缀不抹掉；不推广到战斗列表或其它商店。
6. **独立反证。** 终态相同、display 非阻塞、普通 BACK 退出、checked 删必原子、busy 自动变假、借商店恢复门六种反解，与实际新读控制顺序、共享 loop、重排／update 或 partial helper 前提不符。旧 toss-order probe 的两个协调器／三个替身仅 Bag正常、Bag显示失败、PC正常；它未执行真实 UIHelper／容器／busy，且无 PC显示失败向量。本轮未重跑；PC显示失败及三行暂停只给新静态推导信用。
7. **依赖与接收。** 当前 WP17 59–160 及 U06／QN／CM/NM 依赖新读。WP27 与 U14 新名称接口直接回源：Name 与 NamePlural 各自省略默认，份名缺席分别回普通名；重要／ShowQuantity 只影响显示门，不改变 Toss 库存写入时间。U01 为背景，不并入本组三批九项签核。U13 域目录及 WP66-A/WP54 联合接收接口明确排除。

## 共享组合、原行与反证资格

WP29／WP66-C 实际 bytes 等于已审 U12 mirror，但仍重新读实际全文和源消费链。WP27 相比 U12 mirror 仅新增 U14 名称独立省略默认两行（实际61–62）：Review 不导出 Reviews，独立省略 NamePlural 原值 Unnamed；不同语言域／份名空译限定保留。Item1–206 新读支持该共享接口，无 U12 Toss／数量冲突。

UI 的完整组成是 baseline914 + U11 中间31 + U10 EOF64 + U12 EOF17 =1026。完整独立字节核验确认 U11 实际287–317、U10 实际946–1009、U12 实际1010–1026 三贡献块各与原候选全块原字节相等。两个 EOF 块完整并存，不能以只剩一个尾块签核。U12 的 C12、C36 **有意替换** 为实际334、358，与已审候选修订全字节一致；旧723表格行里其余721原字节保持且有序，数字含表头／separator，不是业务向量或执行数。不能将旧U11的“931行逐字节保留”概括给当前不同输入。当前9个新增 BP01–04／TS01–05 唯一、全为 NOT_EXECUTED_THIS_UPDATE。详见 [group-and-table-bindings.json](group-and-table-bindings.json)、[static-checks.json](static-checks.json)。

九个共同 counter_evidence 原载荷本次全部独立读 bytes／核身份，均等于同会话先前非作者 peer 的完整语义读取对象，原 receipt 固定在 `2b6832d1049650e08a071dccabce23326cc2c9ef`、SHA256 `97b2f97c165fbf237f00d22e334adb19444640cb0cc305c194fd666f33e06f8a`、blob `a652a0fc03aa985c3cdfc2430d90fa737113eca5`。这项资格复用与个人新阅读分列：本轮 root/counterreview-bag 全73行及 imported /205、/210、/251、/257 全节点新读；不会声称个人本轮重新语义读完全部320记录。K 阅读信用仍0。九身份、各适用范围、先前全载荷 receipt 与新相关读取见逐ID JSON；无外域旧 FAIL 被过滤掉。

## 历史范围、限制与余下门

原固定独立 U12 report 全文读取记录了 R1 WP27登记／预检／partial、WP29资源／覆盖／交易、WP66-C A–E/R01–03 的局部资格；R2 精确 B06/A038、B07/D023、B16/B035/C117/D023 与229控制／21批／341五元组，两个 owner D023 分列；R3 M10-002/003 的23/76；R4 M10-001/003 的17/76与B5 16/75分列。R5 原 U06 M10-001 的 packet/findings0、selected13f/records67、独立044、activation12df 所授92CLOSED/OPEN0仅原selected92（51P2/41P3），不让当前 R6 自己的两必修免新验收。7optional／7no-required、6policy／13limits保持独立资格。

本轮相关当前实际 span、源入口／消费者与上述旧行均独立新核，旧 PASS 不替新实际验收。额外尝试重取原 c0ff R2/R3/R4 固定 Git tree 失败（指定路径 git show exit128，ls-tree 报 not a tree）；这项本地历史访问缺口保留，只沿用固定非作者原审的精确资格，不冒称本轮新原历史全文读取。当前新源推导与实际内容通过不依赖作者历史自检。旧 G03/G09 FAIL、U03 FAIL／定向修复、两 advisory SHA MISMATCH、SC-U07-001 体内 LF 错误和纠正仍保留。

U13 原 FAIL 与修订 `9971fe84896786645cdcda3ab45e5caf7785cabc` 尚待原审且未接收，facilities 域目录及 WP66-A/WP54 联合接口不在本报告签核中。input 中隔离接收条款不使 U13 通过。任意未来 changed blob 必须重验。Root 仍汇合本组其他 peer 的语义签名与 UI 当前团队全文收据；公共同步在 R6-I 后做。对 U12 已完成内容没有必需修订；有效运行配置、原生宿主／媒体／物理输入／地图可达、真实存档、任意插件组合与外层异常恢复继续未知。

交付 [report.json](report.json) 含逐 ID 七组、实际身份／47载荷完整核验、11本组路径绑定、九向量独立预期、旧行资格与精确限制。仅写本 peer 目录；无 candidate/formal/public/旧review 修改，无 git提交／切 branch／push／force／删除／Mac 操作。读取与静态辅助脚本均为本审者独立实现，未执行作者 validation。完成后固定本目录文件，供 root 发布和完整 readback。
