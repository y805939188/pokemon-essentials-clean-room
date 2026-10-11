# B20 独立 AFFECTED_ACTUAL 复审（B01–B19）

**结论：PASS_SCOPED_AFFECTED_ACTUAL，剩余阻塞0。** 全部19个已接受 owner 的实际支持接口已在精确 ACT 独立判定；旧308贡献与原目录顺序/重复次数保持。该签署仅为本人的有界 affected actual 门，FULL actual、唯一登记者的正式 C 和 canonical关闭仍归各自流程。

## 固定对象与入口

- 被审 ACT：`6babcf657aef559dbf101aeb093a1beb730ab507`；tree `7f511347be10a55ed1341f4132e198ac6bdedede`。
- 管理发布包 M：`66ba31f7895067c9d925aba20ce3de046fbf60e7`；tree `2f30f3ae648c593a32c52e2598a968bf677317ea`。M只新增17份冻结管理文件，区别于被审 ACT。
- 正式基线 B19 C：`de1a1c28a4255ff1cfd59fb6fb96f9be2d6ece1f`；tree `88a400af08253bea8d97ee2ef2fa6636f0900f92`。
- 已审 NEW2：`3f521e6dea0b442e4bb174a9715c458416386b37`；tree `49f406a6de8ca2786e5dda27abada19780fdfa05`。
- 当前入口：[affected-actual-dispatch.json](https://github.com/y805939188/pokemon-essentials-clean-room/blob/66ba31f7895067c9d925aba20ce3de046fbf60e7/review/remediation/20261003-prepare/batches/B20/actual-freeze-1/affected-actual-dispatch.json)；blob `07dd910c0cde97e16a793707500329f16f7b6267`；SHA256 `1c149a9fe3a455dfa033418c85fc9d9f13e660dea383bd61ac6fcc2aa27b657a`；47861 bytes。
- 固定既审 affected 实质报告 `cecc826263aab5e11cb51d1653bfb191306332c8`，最终包 `7c5309763a6cf2e31564a1fe42786ebcbfecbef5` / tree `e15b4d6548b9e22975a38fa9b61f9056d585e04d`。旧入口/原稿范围与五组修复证据均按固定SHA/path/hash归因，不递归复制。

模型参数按现有接纳约定有效。本轮没有模型/额度审计，没有CLI模型替代。

## 完整差异、七 payload 与整合范围

主审独立重建并核对两条完整、未过滤仓库流，逐header/hunk按规格和管理/证据分类；与M唯一已发布流逐字节相同。没有复制流进本报告。精确命令、全部路径分类和每节hash在 [metadata-verification.json](metadata-verification.json)。

| 完整流 | bytes / 路径 | 固定 M 路径、blob、SHA256 |
| --- | --- | --- |
| C→ACT | 1258161 / 44（规格7，管理37） | [`complete-C-to-ACT.diff`](https://github.com/y805939188/pokemon-essentials-clean-room/blob/66ba31f7895067c9d925aba20ce3de046fbf60e7/review/remediation/20261003-prepare/batches/B20/actual-freeze-1/complete-C-to-ACT.diff)；`62a6b2d7fdda7ae9605ce0324227bbc4bf6bb60a`；`7f1821dcf2808beabe0e741ae38a1afae49774ccb421d2d8f4978f4da59052ba` |
| NEW2→ACT | 3943665 / 112（规格0，管理112） | [`complete-NEW2-to-ACT.diff`](https://github.com/y805939188/pokemon-essentials-clean-room/blob/66ba31f7895067c9d925aba20ce3de046fbf60e7/review/remediation/20261003-prepare/batches/B20/actual-freeze-1/complete-NEW2-to-ACT.diff)；`201dfa8ef07c0786041c9481f87997b64cc8cb95`；`65a35f252d23e08daa4db4702a8e08b603ad2735660c449f17e67a915c599376` |

G `405d7884058d30d94655be0b75f8f12eb07a15d9`→ACT恰七个规格路径。ACT七payload的mode/type/blob、SHA256、大小和全部字节均等于已审NEW2。身份相同支持复用固定语义证据，本报告另核实际caller/data/condition、整合管理增量和外部fixture绑定后作actual判断；candidate PASS和scope许可不作为质量通过依据。

| ACT路径 | blob | SHA256 / bytes |
| --- | --- | --- |
| `deliverables/final-specification-set/demo-dx/wp74-battle-animation-authoring-and-exchange.md` | `42b214af3267436755339815ced7d67f67a3add1` | `77b41705e61b2fbd0d468b833ab51b6bdfb87d2e36de130efe8dc7b28469ddbe` / 70641 |
| `deliverables/final-specification-set/demo-dx/wp75-project-conversion-and-authoring-tools.md` | `d29ea4f31cf0b076991bf2cfda391c7703cd3040` | `9778e9a4909b492812034b1c687e27360f18fd96052d87067ddf32d455d6b237` / 67289 |
| `deliverables/final-specification-set/demo-dx/wp77-demo-evidence-and-capability-coverage.md` | `e792348b0a7f35145736f7d595e86ec290b420b8` | `d1ba7c694f41ee5c3763a725467996632264e504563be74036c20d6ad5021ca6` / 29209 |
| `deliverables/final-specification-set/test-catalog/demo-dx-wp72-73-74-75-76-77.md` | `d77a72b65a44f8d91b62dd06f0b324e7bfac774a` | `603ee184ceaed66dc6d5f6010542fb84e6a7f4da5d326e61b1227c6ad8ca9eb1` / 102307 |
| `specs/demo/wp74-battle-animation-authoring-and-exchange.md` | `76400f81ab7735c7a633049b4b3cec2b9915f49b` | `8c032d7b6870032a8abbb5367a324ac08a9ef4fb7c4240a0cf1d6370fd20c7eb` / 88842 |
| `specs/demo/wp75-project-conversion-and-authoring-tools.md` | `3796ec9ff81a2b3d41fc42a952167c2925e0ca46` | `e4c9c56c7ddf3c80d69f2911c25d3bfb5e55510f1f6700dc1cd155ecf70ed820` / 86424 |
| `specs/demo/wp77-demo-evidence-and-capability-coverage.md` | `64fc5fcf9ace768deaa640cc7f9a4190473785ea` | `46a5e1883baa6c524779f080feb7bec0602f14c3b62b0ff7c2ae41bb4cbb7180` / 47756 |

NEW2→ACT移除75份B20作者候选证据，均不在旧C接受证据集；19案例和作者导航继续由固定外部提交/路径/指针/hash绑定。14旧案例在固定`005b747898137720f78548f0fb24bdf40f375232`，5修复案例在NEW2；19 case ID/目录ID匹配、pointer可解且均NOT_EXECUTED。51子例不替代完整19/15合同或14旧对象。没有把候选大包缺于ACT误报为旧308损失。

## scope 链与公共登记

初始六项管理范围被`669997ac28258f26d0bafc81b1d081abb407a3a1`完整19贡献/15主责refreeze明示替代；`d54fba72a75a3324d7a3daf8e02bc1ecf6c8beeb`只授权三原稿19hunk；`924c7c3a7a5029b07ad18085cf2dadb594512186`只追加WP75/WP77三个hunk。各after完整对象按授权精确落入ACT，无域外原稿修改。G→ACT无额外规格写入，ACT→M只17冻结文件。详见 [scope报告](b20-act-scope.md) 与 [scope数据](b20-act-scope.json)。

19项G登记保持完整原finding/qualified binding、accepted/pending contributor和所有effective case aggregates。旧308接受仍308；两公共TSV的327条记录（另有表头）中的新增19条均pending、canonical OPEN、C NOT_PERFORMED。M外部binding把pending登记绑定精确ACT，没有自签actual或正式接受。approval/traceability/final-review的旧C全字节为精确前缀；canonical ledger全blob不变。B21仍held，未合main。

## 全部 owner 的有界 actual 判断

以下19项均PASS_SCOPED_AFFECTED_ACTUAL、剩余阻塞0。完整旧accepted scope/qualified指针、限制、实际变化条款/调用者/数据/条件/间接route、candidate→actual保留、判定理由与验收条件见 [owner-judgments.json](owner-judgments.json) 及三组新独立支持报告。未受本增量影响的范围由完整文件/子树/接受容器身份和固定既审消费者证据共同支持；空route或owner正文不变不单独构成“不受影响”依据。

| owner | 旧贡献/主责 | 实际支持界面和继续保留的门 |
| --- | --- | --- |
| B01 | 14/7 | WP75工具IO/编译入口；清树→写出→备份分阶段。 |
| B02 | 12/9 | WP74目录枚举/资源选择器；文件保护与缺目录传播。 |
| B03 | 27/19 | WP75事件/路线、页条件和ASCII四前缀独立门。 |
| B04 | 35/23 | 消息/资源/音画；CN与G数据字段及失败前缀。 |
| B05 | 16/10 | WP77普通getter→WP21/WP18外层battle/storage/forced门。 |
| B06 | 10/7 | CN→WP24 coins；party数学与库存/存储写者边界。 |
| B07 | 19/12 | 每级LevelUp→Common精确名称/播放；成长提交次序。 |
| B08 | 17/9 | WP77缩放→WP36数学；电话TE资料均匀选择与实时遭遇。 |
| B09 | 20/13 | WP75六族输出→WP39创建规则；转换/启动/结果独立。 |
| B10 | 7/2 | WP46每击/恢复→WP74映射；HP提交和反应先后。 |
| B11 | 6/3 | WP47-A动态类型/环境/Ghost→动画名/偏移。 |
| B12 | 9/6 | WP51–53评分/绑定；有限静态佐证不证明动态无消费者。 |
| B13 | 8/5 | 编辑复制与WP58回放字段；设施挑战链未证。 |
| B14 | 24/19 | 精确治疗转换→Recover All 0→WP61配置/成员集合。 |
| B15 | 16/10 | WP77电话→WP63版本、抽样、次数与异常阶段。 |
| B16 | 24/20 | 编辑器集合/缓存/正常恢复→WP65存储倍率。 |
| B17 | 12/7 | WP74名称/映射/缓存→WP67-A真实播放器。 |
| B18 | 8/5 | WP77场所登记→WP68–71独立玩法/奖励门。 |
| B19 | 24/19 | 六真实输入、120效果、编辑/磁盘/快照及ASCII/资源复制。 |

支持报告：[B01–B06](b20-act-owners01-06.md)、[B07–B12](b20-act-owners07-12.md)、[B13–B19](b20-act-owners13-19.md)。尤其B05、B06、B11、B17纳入真实间接reader，B09纳入WP75六族实际输出消费者；B12有限静态检索的范围保持，未声称动态不存在证明。

## 旧接受、目录与已修问题

原PLAN全键集合：308个唯一(owner,ID) receipt、205 primary、216 touched IDs保留；19份完整接受容器及2757个旧owner路径逐mode/type/blob保持。根/扩展/前提/最低修订/确定复查/effective case/非局部义务与已知source limits仍完整绑定，未以本地例子代替。

目录C195→ACT214；195旧ID顺序/重复次数全保持，193旧行字节不动，AN-M23/CV-M18两已指派行保持NEW2值。B19 17行与PA040 3行含LF行hash保持；B19六真实输入、120效果表及83/22/13/2分类原资格保持。详见 [保留报告](b20-act-preservation.md) / [数据](b20-act-preservation.json)。

| 旧问题 | 在固定ACT的静态验收条件 | 当前判定 |
| --- | --- | --- |
| AF01 / C029 | forced包括0优先；无forced时battle/storage任真返回stored，只有两者皆假调用handler；仅候选不同按主规格提交，form_simple不调用handler。 | NEW2已修；ACT实际getter消费边界保持，B05阻塞0。 |
| AF02 / C028 | 缺训练家记录正常空文字；遭遇请求版缺回退0，双版缺/空表正常空文字；TP/TE单次、均匀且保留重复；空party/非法数据等真正异常保持阶段前缀及未保证清理。 | NEW2已修；ACT电话/遭遇消费者保持，B08/B15阻塞0。 |
| AF03 / C003 | CN读coins独立字段，G读money；两个数值独立变化，不引入金银铜面额层级；格式归WP17。 | NEW2已修；ACT消息/库存/编辑接口保持，B04/B06/B19阻塞0。 |

五组已修局部门继续保持：C024清树后首文件失败未到备份，后续IO允许部分写出；四事件前缀局部大小写无关仍仅ASCII字面，并保留注册/页/有效Battle独立门。以上是静态判定，不是运行测试。完整验收和source范围引用继续来自固定已审NEW2支持，不重复未变全库阅读。

非阻塞观察ACT-OBS-01：旧NEW2汇总将B10–B19 local-qualified hash数组总数说明写为158，实际按固定数组独立重计138（7+6+9+8+24+16+24+12+8+24）。十份完整接受容器和记录都保持，不存在20贡献丢失。新报告采用138并透明引用旧原件；旧报告未回写。证据与后续新汇总验收条件见 findings.json。

## 独立挑战、证据边界与发布

根另核M全部17文件身份、194个固定外部文件身份和79个pointer；对子报告引用重新核590个唯一固定文件、505个literal pointer及85个含LF条款范围hash，全部通过。[evidence-identities.json](evidence-identities.json)与metadata文件给出完整固定身份。

独立挑战核196个固定对象、467个pointer、38个完整原/批准对象hash及19个owner导航行hash通过；候选FULL四引用和19 per-ID pointer与固定`2d854ca5462876156d371554c56fd51b0003a472`匹配，但本报告不采用它来签FULL actual。详见 [挑战报告](b20-act-challenge.md) / [数据](b20-act-challenge.json)。

参考只读固定`8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b` / tree `7589c800b61ba13a13040ed0d686979b80a84fd0`。未执行参考游戏、Ruby、编译器、转换器、反序列化器、生成器、行为向量或历史脚本；仅新写Git/JSON/hash/text元数据核验。所有case仍NOT_EXECUTED，runtime观察0、已证Demo链0。旧U01–U10、G01–G12、AX01–AX20和全部旧局部/非局部限制保持。

本分支基于固定M，只新增本人actual报告目录；正文、原稿、旧证据、公共登记、参考、main均未修改。普通推送后从全新独立bare Git对象库远端fetch，逐文件取blob并比较完整字节、Git blob、SHA256和大小，包含所有manifest与publication输出。publication记录固定首份实质报告commit/tree，最终包commit/tree及全输出再读回由外部返回精确身份，避免自引用递归。实际读回结果见 [publication/report-readback.json](publication/report-readback.json)，完整新输出清单见 [output-manifest.json](output-manifest.json)。

剩余affected blocker、输入或工具阻塞均0。正式C须唯一登记者在两份精确actual门及已发布读回具备后独立处理；本报告不接受C、不关闭canonical、不签FULL或合main。
