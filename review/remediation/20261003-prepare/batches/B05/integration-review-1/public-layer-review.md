# B05 实际整合公共新字节独立验收

固定对象：`cc085d618ce8b5ebda82c28a3a1ac9a09dda9a85`。接受上游为B02-C `9576f00e7d3aeb96f7ca8c42caccfba8f808505e`。本轮独立判断 **PASS_SCOPED**；下表只验收本批新增公共层，不把旧候选通过扩为整仓通过。

| 实际改变的公共文件 | 独立语义验收与反向对照 |
| --- | --- |
| `audit/source-traceability.md` | 新B05后继区分候选/报告/实际整合，指向十五当前身份、原授权、逐ID登记及正确定位日志。旧B02/B01与审计正文后缀保持。明确S19正确为001_Utilities；没有说A-REG重读26源文件或运行参考。 |
| `deliverables/final-specification-set/README.md` | 当前入口绑定B02真实被审/Ultra报告/接受起点，以及B05完整候选/独立报告。B05当前仍是整合待审，未把候选或报告SHA冒充实际整合。原全集交付历史段保留；未宣称运行、关闭或下游自动开始。 |
| `deliverables/final-specification-set/scope-statement.md` | 最新状态区分已接受B02与本次B05待审；233规范对象/229必修OPEN/关闭0各有含义。U/G/AX、具名未知、demo/运行0保持；旧局部批准不能成为全集验收。 |
| `deliverables/final-specification-set/test-catalog/README.md` | 仅两个B05表项范围更新，随后追加当前登记；其余原文保留。当前164与213行，339→377，新增38、只改FM15/FM20/SH06、无删除。PT/PS/AQ/BR尾段、B01/B02的51/99行保持。行数是未执行静态清单。 |
| `planning/coverage.md` | 只加具名B05后继；原历史覆盖与Feature表保持。当前16贡献、15正式文件按受审限定登记；A020/A024/A026、A040、A044、C124/C126剩余批次明确。未把局部通过写为所有消费者通过。 |
| `planning/feature-matrix.md` | 与当前覆盖入口一致；原Feature/别名及历史正文保持。公开剩余B07/B16/B17，B03仍消费原B02冻结，不宣称其所有公共读入在新SHA不变。 |
| `review/remediation/20261003-prepare/approval-ledger.tsv` | 旧26行完整字节前缀保留，追加16个B05待审贡献，总42。候选结论PASS_SCOPED；实际整合判决和报告尚待，canonical均OPEN，下游BLOCKED。以finding+candidate区分贡献；A020/B01与A020/B05不能误计为两个规范finding。 |
| `review/remediation/20261003-prepare/traceability-successor.tsv` | 旧26行前缀保留，当前42贡献行。新增16条的原优先级/完整报告身份、作者映射、路径hash、测试ID及剩余批次均逐ID与冻结材料匹配。测试列明确未执行；不移除协作贡献或把B05变成整ID关闭。 |
| `review/remediation/20261003-prepare/final-integration-review.md` | 新B05送审前置段绑定真实merge父、B02接受和B05完整候选链；下方整个B02-C/B02-G/B01-C正文原样保持。新的公共登记需实际新SHA审查，仍要求父任务串行接受/冻结。 |
| `review/remediation/20261003-prepare/historical-errata.md` | 本次最小原稿授权、正确原Mega/Shadow/h255数据与旧批准身份分开；前轮S19和EOF错误以勘误/有界日志解释，未反写冻结首判。旧B02/B01勘误正文保持，未把修正前定位当正确来源。 |

全部35条current-hashes（15正式/10公共/10依赖）与实际Git字节一致；manifest的144个具名历史/当前身份也独立匹配。原完整finding和批准acceptance散列逐ID回算一致，当前登记继承既有独立16对象的每个字段，作者v2建议完整相等。

## 十个新增整合证据

本轮检查全部 `integration-stage-1/` 十文件：README、manifest、finding-registration、merge-independence、scope-counts、current-hashes、validation-results、两patch、diff-and-freeze。A-REG的结构自检不是独立Ultra证据，本轮自己的结果见 [独立验收](independent-validation.json)。

两patch确实是各自起点到payload `b82dde24ae1e0980fe442031e421ea4a709e0981` 的完整Git差异。最终被审提交再增加两patch及diff-and-freeze三文件，原payload字节保持。本轮另直接重建 **实际最终SHA** 的86/115路径，包含这三文件，不能用payload的83/112路径代替。完整路径、前后blob、全文diff的字节数/散列以及三新增证据路径见 [最终差异清单](complete-diff-manifest.json)。此有限链无需把自身patch或报告SHA递归写进自身。

## 回归与剩余边界

正常merge的两父为B02接受上游与B05独立报告；三来源提交的父/tree/全name-status均直接回查。B05完整66路径与B02接受链路径无交集；合并前后十五正式与51记录保持，全部其他上游既有路径受保护。公共新字节已在上表独立验收；没有只靠候选PASS或hash判断公共语义。

仍可直接读到WP28:213的“所有EV写入”量词。这是既有GIR-FD82-A040的B07欠项，与本批设施255/255反例明确并列保存，不能用本轮通过关闭；也不重开新ID。B16的Characteristic/零招UI责任、B17设施生成器责任均不在本轮正式可写范围。零招、负索引、ROTOM同值删空、数据缺失跳过与解析部分失败、h255/G0和起始Nature降量等带前提反例原字节保持。

目前未建立新的整合遗漏、回归或矛盾，新增缺陷0。规范229必修仍OPEN；父任务串行接受之前，公共冻结中B05下游BLOCKED的历史状态正确。后续可消费的有界前提及B06/B07额外依赖见 [依赖冻结建议](dependency-freeze.json)，本reviewer没有启动下游或改公共登记。
