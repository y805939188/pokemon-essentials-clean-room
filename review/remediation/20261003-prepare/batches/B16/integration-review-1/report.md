# B16 integration-review-1 — 原 FULL 角色独立 actual 复审

实际结论：**PASS_SCOPED，FULL24/20 通过**。24项贡献分别给出本角色精确ACT的PASS_SCOPED，20项主责分别满足当前限定最低验收；阻塞 **0**，本角色最小修复范围为空。该结论来自完整实际差异、登记/保护/范围/依赖与逐项质量判断，未自动转签候选PASS。

| 固定对象 | 完整身份 |
| --- | --- |
| reviewed ACT | `29b21fe188cce4e76f5a2f566f9144f1c3f53239` |
| reviewed ACT tree | `e05903a329f4a18370a17858f4653cbb1273b49e` |
| 正式接受前驱 C | `27185563f307e16d2612fa86e83b2c9bd772c79e` |
| 候选 NEW | `356b46b320884e57e71a1cab8413e13594524a7d` |
| 原候选独立 FULL 报告 | `da58ab3e8ce5e508b2ed55928c6f334cb64a2445` |
| actual派发包（只读入口） | `7372479c763b90271f0bf8fbab68a15862739ba0` |

目标为ACT，不是后来的管理包或moving branch。G的普通ACT提交以前驱行政scope4 `cc14f356dfc30eb7d27d4c5684f738867a64b0d5` 为父，但实际接受基线仍为上述C；两者未混用。报告分支为 `codex/cloud-dot-B16-actual-full-review-1-20261010`，写入仅本新目录。

请求配置保持gpt-6.1-sol / ultra / default（Standard）。无可信有效后端回显，按精确分派保留 effective_backend **UNVERIFIED**，不声称实际后端已验证；未probe、降级、fallback或创建子任务。

## 完整流与实际整合变化

两条完整未过滤流均独立重现、完整读取、逐顶层block/全部路径核验，所有差异中的JSON完整解析；没有截取11载荷来替代实际流。

| 流 | 文件 | 字节 | SHA256 |
| --- | ---: | ---: | --- |
| [C→ACT](complete-C-to-ACT.diff) | 238 | 36,030,263 | `495c8d8e900688901c17cb152e0a86f40bedc2012643024a75d0375c91b4c2aa` |
| [NEW→ACT](complete-NEW-to-ACT.diff) | 114 | 29,337,440 | `9b2b0dd682dfcad49e6fe4a0e41b0ce52f08f7e7ce132be94130c89bef8294b2` |

C→ACT改变14个既有路径：11个原净载荷，以及公共approval ledger、traceability successor、final integration review三个登记路径；另增224个资料路径。NEW→ACT仅改变上述3个公共路径，另增111个冻结/候选独立报告/行政准备/G证据路径；11载荷无语义或字节增量。

实际意义并非简单“复制后即可PASS”：G追加了24项带完整控制和前驱证据的pending登记，复制了候选作者和独立评审资料，并保留scope3/4和下游私有准备。逐项核对其角色、状态、指针、真实ACT绑定、主责最低条件及全部非局部义务，确认没有把候选结论或范围许可伪装成ACT/C，没有增加新的调用/数据行为合同或抹掉既有失败边界。

独立确认161份发布资料复制来源准确：113份NEW作者/候选资料、9份原FULL报告、39份affected候选资料，各整文件及mode匹配固定来源。14个候选affected回执准确对应NEW（9 PASS_SCOPED、5 NOT_AFFECTED）且无阻塞，只作为G整合的前提，不转成14个actual结论。B16控制包、scope3/4及B17/B18原行政准备按固定版本保持，后者正式释放仍待唯一B16 C。

## 公共pending登记与全部旧成果保护

两个公共表均是旧240条原始字节记录前缀加24条B16新记录，物理264条。每个新增ID/primary、候选SHA/报告、G记录pointer、完整控制绑定、全部贡献/已接受/待贡献、实际门和C/闭合状态一致。ACT内自引用字段为 `EXTERNAL_ACTUAL_FREEZE_REQUIRED`；派发包的逐项外部绑定解析到上述精确ACT/tree，不修改冻结ACT，也不签接受。

G的24项actual回执仍为空、B16已接受贡献0、canonical OPEN。公共记录明确 `PENDING_EXACT_ACTUAL_FULL_AND_AFFECTED`、C及最终闭合 `NOT_PERFORMED`。字段虽保留候选PASS及既有栏目名称，其明确值没有宣称B16实际接受。

- C既有36,350路径中，除上述14条授权变化外，36,336路径mode/type/blob保护。
- NEW既有36,463路径中，除三个公共登记外，36,460路径mode/type/blob保护；原共享目录与11载荷保持。
- 行政前驱全部既有成果除11载荷/三个授权公共登记外保护，含B17/B18原私有准备；没有提前改正式下游内容或释放作者。
- 接受统计整文件及240个唯一(batch, ID)已接受贡献的版本准确证明保持，不重授240项语义PASS，不递归重审其历史。
- 旧final integration review整正文原样为ACT后缀；完整canonical ledger字节保持，并独立解析为229 OPEN、0 CLOSED。正式接受仍15/21与240。
- 旧目录460行的ID/顺序/重数、451保护行、9本批必要修改和24新增行按已验证候选证据保持，当前完整目录同NEW字节；所有24新增静态设计仍进入本actual限定判断。

## 11载荷、原稿范围与C003/C120

六净稿、五原稿整文件均绑定C前值、NEW值和ACT值，ACT与NEW字节一致。当前原稿完整after分别对应scope3或storage一稿的scope3+scope4后继after；权限链与准确应用证明复用版本匹配的本角色独立证据。G没有重执行保存补丁程序、扩scope或借权限收据代替质量。当前作者trace、hunk、资料附表和目录证据准确复制，旧错误或partial/pending仅属明确冻结前驱。

C003/R-B16-F01在ACT目录590行仍正确：合法来源hp50/totalhp120、目标非蛋非来源hp30/totalhp50，资格/菜单门和正常资源成立。完整用量24先扣来源，来源26；目标夹限仅恢复20至50，不返还来源扣量。目标total120恢复24至54、total40恢复10至40，来源均26；来源hp≤24及自身/蛋/濒死/满血目标的拒绝分支保持。原净A§4.2、旧A23、当前纠正trace/hunk一致；A31/A33和其余非局部扩展保持，旧来源30错误未在ACT复发。

C120在ACT原净217行都保留实际条件，且已接受WP25整文件保持：

| 具名前提 / 静态反向 | ACT判断 |
| --- | --- |
| 默认16基础墙纸、零基盒5，整数16未解锁/已锁回，初始化与相应素材正常 | 实际不可用，显示及记录改5；盒2同前提改2，退出不回滚 |
| 可用3、已解锁16 | 保持原编号；不能把所有“非法”编号笼统归一 |
| 完整匹配旧 `box3`；锁定的旧 `box16` | 先转整数并写回，再按实际可用性；前者3保持，后者先16再5 |
| nil / 空串 | 默认显示5，背景记录仍原空值；不与不可用整数合并写回 |
| `box2`、后接LF、`prefix`+LF+`box2`；同一行 `box2x` 对照 | WP25首个完整匹配行兼容保持；非匹配文本不保证转换 |
| 既有/手工 `box3x` | 可用性数值比较失败早于默认背景写回、旧图处理与素材加载；不宣称正常游戏生成或Demo可达 |
| 默认16下既有/手工整数−1 | 实际可用性通过，无默认背景写回；对应素材存在/加载仍未证 |
| 背景读取缓存与当前记录真正相同 | 不重取；空值默认显示不等于空记录；已发生写入不因单纯退出撤销 |

这一实际限定不扩大source异常，也不规定未来沿用参考组织。Wallpaper操作、当前盒切换、旧正常目录B16-C120及共用搜索Start/Cancel、末次形态写回没有回归。C003/C120的源级条件由自己固定候选证据准确复用；本actual没有新的行为来源/调用数据变化需要重读参考。

## FULL24/20逐项实际结论

完整24原始/批准/当前控制、全部根/扩展/minimum/recheck和12 effective聚合与固定packet匹配；G嵌入值逐项全等，没有省掉四个共享贡献。每项本actual记录包含精确ACT/tree、完整控制绑定、合法前提、正例、最小反例、相邻反向、旧回归、原净/目录/追踪一致性、实际变化及有效证据复用理由、非局部义务、限制和阻塞列表，见 [review.json](review.json)。以下ID均有GIR-FD82-前缀。

| ID | 主责 | 本角色ACT结论 | 实际条件与复用理由 |
| --- | --- | --- | --- |
| 003 | 否 | PASS_SCOPED | 三模式/返回/几何与净化保持；全根扩展和非局部仍保留 |
| 004 | 是 | PASS_SCOPED | 持物交换后续状态、BACK和空格分叉保持 |
| 006 | 否 | PASS_SCOPED | 暂停/导航两个周期、绝对相位及首帧保持 |
| A015 | 是 | PASS_SCOPED | 已读数据分叉/三个入口及旧SV02/MG03保持 |
| A044 | 是 | PASS_SCOPED | 默认TR双入口教学/删除/重学及资源统计保持 |
| A048 | 是 | PASS_SCOPED | 合法空重学首绘失败与非空取消/教学对照保持 |
| A055 | 否 | PASS_SCOPED | 零结果Start/Cancel、结果BACK和持久模式写入保持 |
| A056 | 是 | PASS_SCOPED | 两计数及完成长度条件保持 |
| A058 | 是 | PASS_SCOPED | 方图/盒图表、多消费者周期/相位与缺图边界保持 |
| B035 | 是 | PASS_SCOPED | 有限双槽部分写入与真实回退/交易资源保持 |
| C003 | 否 | PASS_SCOPED | 完整扣24来源26、目标夹限20，修复不复发 |
| C058 | 是 | PASS_SCOPED | BGS记忆共享、二次SE缩放与副本对照保持 |
| C114 | 是 | PASS_SCOPED | 名义请求时序、输入次序及首绘保持 |
| C115 | 是 | PASS_SCOPED | 五档尺寸/负值/保存越界条件和宿主未证保持 |
| C117 | 是 | PASS_SCOPED | 排序取消恢复与存储索引保持 |
| C118 | 是 | PASS_SCOPED | 图标帧/偏移/HP档、消费者空返回保持 |
| C120 | 是 | PASS_SCOPED | 三路写回、匹配与失败前缀/−1/素材未证保持 |
| C121 | 是 | PASS_SCOPED | Info/搜索换算舍入及原值过滤保持 |
| C122 | 是 | PASS_SCOPED | 结构先于已见、性别/标签及末次形态写回保持 |
| C123 | 是 | PASS_SCOPED | 37+37离散表、焦点与搜索写入保持 |
| C124 | 是 | PASS_SCOPED | IV/PID决胜、30描述与隐藏门保持 |
| C125 | 是 | PASS_SCOPED | 正常背景前提下旧源索引部分写入/首绘失败保持 |
| C126 | 是 | PASS_SCOPED | 空招式多入口/教学与取消分叉保持 |
| D023 | 是 | PASS_SCOPED | 数量×半价显示/实际金额、奇数/零展示与旧C29保持 |

20项主责的 `actual_primary_minimum_satisfied` 均为true；四共享仍有独立ACT贡献判定，未借主责门替代FULL24。所有表述都是范围内静态质量结论，不是执行过的行为测试。

## 检查证据、限制与结束条件

[新元数据核验程序](verify-metadata.py) 得到 **972/972 PASS**，完整结果/两流全部路径与块/11实物/公共24登记/240旧成果/源身份见 [metadata-verification.json](metadata-verification.json)。只执行本次新Git/文本/JSON/TSV/散列检查和报告组装，没有运行保存的作者/reviewer/preparation程序；元数据通过不替代上面的actual质量判断。

[source-reading-log.json](source-reading-log.json) 明确区分：所有24项精确旧候选语义证据及实际复用理由、四份C003/C120固定来源blob/范围的本次身份读核、actual新项目/登记/保护阅读。**本actual新增语义参考读取0**；没有把散列读取冒充新源级语义审查或重跑旧来源结论。

[source-limits.json](source-limits.json) 保留完整候选与原FULL限制：U01–U10、G01–G12、AX01–AX20、完整具名未读、条件berry67、媒体/宿主/插件/样本/非局部与真实Demo未证。reference/game/Ruby/compiler/converter/generator/deserializer/行为向量及旧程序执行0，runtime observations0，proven Demo chains0；未把静态设计称运行测试，未做全历史或递归来源审计。

本FULL精确ACT结束条件为完整24/20及零本角色阻塞报告普通发布、自己的远端ref/tree/全部文件字节独立读回。必须另有独立exact ACT affected各owner结论；只有唯一登记者在两actual必需门全过后才可做范围内C。本报告不签affected或C、不接受24项、不关canonical。reviewed ACT仍15/21接受批次、240接受贡献、B16新24pending、229OPEN/0CLOSED；非局部贡献及最终global义务保持。

[artifact-manifest.json](artifact-manifest.json) 绑定首份报告文件。首份普通提交推送后，新增要求的publication-readback.json记录其完整远端读回，再普通提交推送；最终head/tree及包括回执的所有报告文件再独立整字节读取比较，完整最终reportSHA在委派返回给出，避免自身未来SHA循环绑定。
