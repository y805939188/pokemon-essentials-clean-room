# GR3-U06 独立候选复审 attempt-01

**GR3-M12-001：PASS；GR3-M12-002：PASS。** 仅签冻结作者候选的本批有限静态验收；未发现需 REQUEST_CHANGES 的缺口。所有行为／静态案例均 NOT_EXECUTED，运行观察、真实 Demo 链、参考／游戏／浏览器执行均 0。身份、头部、JSON、文字及补丁检查不作行为运行 PASS。

## 被审身份、角色与读取边界

- repo：`y805939188/pokemon-essentials-clean-room`。
- 被审作者交付：`c9d6e3c81c88c778abf2f822977275d0e632581e` / tree `f2b3297d49415baf95a29c28626a06c3788f4ad0`，branch `codex/gr3-u06-author-20261012`。清单的正文 payload 是其父提交 `b7cf57c4ea3b9072982722f08b4f462e976e0fe4` / tree `ab83f9495743f2def57c2315e904d39649f22917`；本审查绑定最终交付而非只绑定 payload 或浮动分支。
- 管理 `d0371f693f4a0dc713ee5cc6e43a20ff465269a8` / tree `0e217b059c1350b6c4ca93b29ad86fae75b48a54`；H `d5b6af3ebbabc57ed7fbdc2e1fb2c4736dbf9a65` / tree `c8a523150d75c8d1bede346857263ddd00ef0035`；正式 D `86b4d7e1d8645e75af91a215240f8786a5bb4ca8` / tree `42c29efb5422772a1d90f657f25983600f500f28`。
- 参考 R `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b` / tree `7589c800b61ba13a13040ed0d686979b80a84fd0`。本执行器新 clone 至 `/workspace/u06-review-reference` 并 detached checkout、核工作字节／Git 对象／clean status；未沿用任务书另一个环境的绝对路径假设，未改参考。
- reviewer 是本次独立委派 `/root`，父来源 thread `01a10d94-84b9-759e-aa1d-edb0d9b6d0e2`，执行环境及可见只读 helper task names 见 [input-snapshot.json](input-snapshot.json)。本 reviewer 未参与候选写作、正式写入或 U07 登记。作者逻辑角色／任务由管理版 `author-task.md`、candidate-paths 的 `U06 author` owner 与作者模型回执固定；作者平台 task ID 没有提供，记 NOT_SUPPLIED，不捏造平台身份。此项透明记录不改变已明确委派的不同角色或候选数学判据。
- 根 AGENTS 和完整本批独立任务书已读；环境／管理／H 无适用仓库 skills。相关 Library 技能对显式仓库路径使用本地工具，不创建 Library／Space 副本。模型请求 `gpt-6.1-sol / ultra / default` 接纳有效，实际 model／reasoning／speed echo 均 UNVERIFIED；不查额度，不用 CLI 模型或隐藏任务。

完整三镜像由独立团队读作上下文：WP75 1–392、WP76 1–279、DX 目录 1–287。语义裁决只覆盖改动条款、两个 finding 的完整前提／反例／验收、派发十控制和必要 M09 交界；不是全局规格或递归历史复审。冻结核心与模块文件的全字节身份校验不等于全内容语义重审。作者自检仅作导航，下面结论来自新参考、真实候选和独立对照。

## 镜像、补丁与保护核验

| 完整镜像 | candidate blob | SHA256 | bytes |
| --- | --- | --- | ---: |
| WP75 | `f87c6edf5b09c2ee43b51a514bb7ef81e55e4062` | `00fa71977b73afd7f788025db190de7ce90f9ff036cccc1b069cb37083f12545` | 69082 |
| WP76 | `12591bc5a9a2daab90b88aeb6818b79d62c59c0a` | `354028776cd47dfab5c12d5bf1b41ed0b65dec5c335b9a2b4b618b560ca3a75b` | 51589 |
| DX 目录 | `255464a58f8e45e30ca1807250926aa47e0791a6` | `54ad7bb556cad38e565fbe255defbb104360ef1dfd4ad725277b8cba5a9eccf8` | 104319 |

base 对应路径在 D/H/管理/作者提交中的正式字节相等；candidate-identities 的 base/new blob、SHA256、bytes 全匹配。47678 bytes 的 candidate.patch SHA256 为 `775eee686fa8bea2a1acd8b84ba2ffde0fba9ce272eb127c240a09f34344d869`。独立在临时 D 副本做适用性检查并重建，退出 0；重建三个文件逐字等于完整候选，无额外路径。没有 apply 到正式目录／参考。

作者相对管理提交的十个改动都在其本批允许路径；正式 131 文件 D→作者差异为空，此处仅核字节保护。目录 214 个具名案例 ID 不增删，只有 CV-M30、GN-M14、GN-M20 修改，其余 211 行逐字不变。独立行解析器起初漏掉九个多连字符 ID，修正后重新核到 214；这是检查器修正，候选没有因此改变，未执行任何案例。

## GR3-M12-001 — PASS

实际验收标准逐项满足：

| 冻结 acceptance criterion | 候选条款／静态设计 | 独立证据及前提 |
| --- | --- | --- |
| 可得表逐列记录两固定 BMP 路径／身份 | WP75 §13.3 lines324–334，尤其330–331；CV-M30 line173 | 新取 R 的根目录两文件均受 Git 跟踪、246 bytes、BM 签名与8×8头部，路径／SHA256逐列吻合。 |
| 缺项表不再称它们均无 | WP75 line321、§16-8 line379、§17 line384；CV-M30 line173 | 可得根目录标记与缺失默认区域底图分列，未把标记纳入 missing_transfer。 |
| 保留 Graphics 底图／宿主／实际运行未知，不宣称 Demo 通过 | WP75 lines326、332、334、379–380、390；CV-M30 | 固定 R 无 Graphics 条目，工作目录亦无；存在性与完整呈现明确分层。 |

`knownpoint.bmp`：blob `1fc5257737f4b8fddef34da3d473a1a3ba33b528`，SHA256 `313c3c8fb2a3e3b4b60eb0e0ff9700ed12b5d2c2858f9d79975cd999945a4ef2`。`selpoint.bmp`：blob `3ed4a0ec643fac61437a1374be00c715669d023b`，SHA256 `27ce6d6bcb9dca59a1c8993cf2bac1a9affcda6637f0040e9e810f4d1d5c3ed0`。R 的 townmapgen.html blob `6bffe3fc62a739ac3fbe577b4f43f2d20a35fe50`，lines269/274 按原相对路径引用两标记；默认底图39及相邻路径定位仍指向 `Graphics/UI/Town Map/mapRegion0.png`。

前提只限固定树、页面同根原路径、可读字节／头部。正常可定位标记；底图缺失仍不能证明完整页面；没有浏览器加载、解码、外观或交互观察。取消、载入失败／部分前缀保留、文本由用户复制等相邻正文不变。M01 report line19、M03 report line22、reference inventory lines425/429 和 limits lines5/22 的有限资源对照一致；旧 inventory 的 NOT_REVIEWED 是历史分类，未被改为新运行签名。修复标准是冻结三 AC，已满足；无修改请求。

## GR3-M12-002 — PASS

R 的 BattleSim 全文1–438已读，关键为1–65与101–129：可见计数包含已结算累计和当前历史；正常结算真正清空历史后，新增累计等于本次处理的原历史场数。Data 的有界120–310，关键196–215／247–252，核定有序五支、全员评级结算、排序、队伍库检查点及下一轮消费；未执行代码。

候选 WP76 §2 line38、§6.4 lines142–148、§7.4 lines190–191、§7.4a lines196–205 与 GN-M14 line194／GN-M20 line200 一致。独立状态／数学判断如下，全部 NOT_EXECUTED：

| 具名前提 | 唯一静态结果／边界 |
| --- | --- |
| 合法队伍、有效 C、有限 h；评级成功并清空；无替换／外部修改／新对局；C70+h12 | C82/h0/可见82，结算前后可见数守恒；再给同队12场且中途五支均不命中→C94/h0，不重复累以前12场。 |
| C238+h12；成功后给定评分70、成员≥2、排序后扫描下标<600；池补充／新队构造正常 | C250/h0/可见250；评分<65且≥80、成员不足、下标删除前三支均不命中，才退休：原成员回池后新队C/h从0开始。 |
| 相同250例评分50；或评分70但成员1；或评分70／≥2成员但下标600 | 依次先低分替换、成员替换、删除；均不作退休回池承诺。评分60/累计79、评分70/249、评分65/80分别保留阈值／严格评分边界。 |
| C70+h0，空历史成功，重复成功空更新 | 每次累计增量0，C70/h0/可见70；评级偏差仍可膨胀，不称全部状态不变。 |
| 有效C70+h12，评级在清历史前抛错，无外部修改 | 本次场次未结算，C70/h12/可见82；评级字段可能部分改变，不承诺全字段回滚、正常外层收束或下一检查点必达。 |
| 多队循环中后队异常／生成启动前取消／生成中中断 | 同队成功不变量不扩成全库事务；已结算的前队／已写前缀无统一回滚承诺。旧启动前取消与启动后无中途取消、检查点恢复未知保持。 |

评分是结算后给定，不能由12场或累计250推算。正常保存并读取同一队伍记录的检查点才承接累计，实际崩溃恢复粒度仍未证。候选有效累计前提不覆盖缺字段归零、无效数据或外部扰动，也未笼统承诺所有失败阶段都保持全评级状态。

三冻结 AC 分别对应：70＋12 的82/0/82（WP76 line190/200、GN-M20）；238＋12及前三支不命中的退休（line196/202–203、GN-M14）；空历史0增量和非事务异常边界（line188/190–191/204–205、GN-M20）。保持活动评级数学：D lines176–188与candidate177–189逐字相等，含LF SHA256 `313fc7d647e0c98f219f48186fd524f6ad174fdef9323185a113062547e3f5ae`。GN-M18／GN-M19及五抽末次／全库整数平均门保留。修复标准已满足；无修改请求。

## 必要旧 qualified 控制与 M09 交界

完整 regression-scope 十对象、全部 qualification/root/extension/最低修订／确定复核与十二个贡献 tuple 已消费。精确对象、原/批准/FINAL身份、qualified_scope、全部accepted_contributions、当前定位与行hash记录在 input-snapshot；不会把旧 PASS 移给新增条款、其它 owner 或整 ID。

| 控制 | 本次有界对照 | 处置 |
| --- | --- | --- |
| D024 | WP74:272–276；DX:286，三采样路径与N+2/前N/舍入限制 | 保留原资格，案例字节不变 |
| D025 | WP72:65；DX:17，0/空串有序转换 | 保留原资格，字节不变 |
| C008 | WP72:68–74；DX:245，Field PC父入口与直接盒子分离 | 保留原资格，range hash匹配 |
| C010 | WP72:111–120；DX:21，六物种/招式/初始记录与缺种 | 保留原资格，range hash匹配 |
| C013 | WP72:99–110；DX:249，单／双角色延后回调与取消异常 | 保留原资格，range hash匹配 |
| C025 | WP74:184–200、384；DX:274，槽60分域与编辑联动 | 保留原资格，字节不变 |
| C029 | WP77:145–146；DX:278，forced/stored/动态门分域 | B20/B21各自资格保留 |
| C030 | 候选WP75:89–95；DX:279，原页条件／变量／末页优先 | §5.5逐字不变 |
| C031 | WP74:350、408；DX:280，Yes/No/Cancel与失败收尾 | 保留原资格，字节不变 |
| C051 | 候选WP75:118–124、WP13:112–119；DX:284，快照跟随链/透明度/through/等待 | B03/B20各自资格保留，§7.2a逐字不变 |

D024/D025 scope 中row_sha256按不含LF，其余sha256_including_LF按含LF独立核对；附带其它owner行只核保留，不扩大签署。D012原非必修裁决、WP52-C:171与C41原字节保留；PP4早退/末尾−10前提与此次历史累计不同，不重开。复审次数、旧229/341数量不作为完成率／质量证明。

WP55 §2.1–2.2（lines21、35–36、46）、WP57 §1.3／§8／§9及租借／交换lines69、81、91保持正式H→作者字节不变：会话胜场／交换与生成器C+h不同；WP76只影响作者生成产物，未回写会话/工厂行为。M09 junction lines10、20、28仍保留M12独立责任。公开提案registration lines131、149–159及traceability165–177保持唯一登记员和阶段顺序，无提前写公共文件。

公共source-traceability line1484仍有原“区域地图生成素材缺失”泛称，作者已提供有界后继行提案；本review不改旧字节或代签。实际整合时应同时核该继承及Feature Matrix／资源身份列表相应承接，继续区分可得BMP、缺底图和未知运行。

## 结束、产物与后续门

本批两个ID及必要控制／交界均已有有限处置，新增 findings 为 `[]`，候选无未处置阻塞。本报告与六份指定产物仅写新 `U06/independent-review/attempt-01/`。正式／候选／旧报告／公共台账／reference／main均不由reviewer修改；不实现或自行修问题，不签正式接受或CLOSED。

下一步仍需唯一整合员核准确base并形成真实actual提交，再冻结actual commit/tree/changed-path identities，由另一个同等独立角色复审实际整合字节与公共承接；之后才依授权登记正式接受及依赖满足后的关闭。资源补交、宿主／真实运行、bug兼容、尺寸或视觉产品决策保持原未决，不增本批修复义务；U08不启动，M02-003不重开。

本报告自身commit/tree不嵌入自身；正常提交推送与远端实际读回的最终身份由外部交付回执返回。输出文件字节hash见 [output-identities.json](output-identities.json)，逐ID机器判定见 [per-id-verdicts.json](per-id-verdicts.json)。
