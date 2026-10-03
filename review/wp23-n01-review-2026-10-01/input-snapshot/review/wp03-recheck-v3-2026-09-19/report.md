# WP03 v3 独立复审

日期：2026-09-19。本报告属于 Reference/Audit 内部审查材料，不是 WP80 sanitized 产物。

**结论：REQUEST_CHANGES，仅剩 WP03-R01 的枚举存在条件需要收紧。R02、R04、R05、C04 关闭；R03、C01–C03 保持关闭。**

本轮修订已处理上轮主要反例。剩余项可以通过修正一句行为定义及对应交付说明、补一组有界静态场景闭合，不要求重写规格或重新提取。

## 1. 实际对象与变更范围

工作区为 `/Users/dingshinn/Desktop/pokemon-framework-reference/`。参考 HEAD 实测仍为 `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`，describe 为 `v21.1-23-g8c5911e4`。未变更参考基线。

| 对象 | SHA-256 | 字节数 |
| --- | --- | ---: |
| `specs/kernel/wp03-content-identity-and-schema.md` v3 | `f1d8a763301385496754b93cef621fdd2abfca088f8268ad07913bed358090f4` | 29897 |
| `planning/review-manifest-2026-09-19.md` | `41ac47ad0be2f4966d9da0f75c94f70b42578129167c696bf362d6e05e947518` | 见固定清单 |
| 上轮 `review/wp03-recheck-2026-09-19/report.md` 原件 | `799f7c0dfb8fe49add0c3a43659901b55821694d91338cfb6ce70a5ec906296d` | 14947 |

22 个输入文件已固定到本目录 `input-snapshot/`。当前 manifest 的 **20 项完整哈希和字节数全部一致**。与上轮输入快照比较，已有文件中仅 WP03 主文档和 manifest 发生变化；矩阵、WP01/WP02、附表、工具、总控文档与旧报告均未变。

记录见 [input-manifest.json](/Users/dingshinn/Desktop/pokemon-framework-reference/review/wp03-recheck-v3-2026-09-19/input-manifest.json) 和 [changes-from-v2.diff](/Users/dingshinn/Desktop/pokemon-framework-reference/review/wp03-recheck-v3-2026-09-19/changes-from-v2.diff)。manifest 自身哈希由 reviewer 固定，不要求提取方做自引用。

## 2. 已执行检查与未执行检查

- 阅读实际修订 diff、相关正文及静态场景，按上轮报告四组剩余项和 C04 逐项复核；核对计划中的 WP03 完成标准及涉及的领域责任。
- 重新读取电话编译/存在性探测/消费入口、遭遇版本枚举和图鉴消费者、槽权重合并/节身份重复拒绝、move2anim 读取分支。源码路径均位于固定参考目录，已确认可读取。
- 复算上轮 55 个相关源文件的哈希与 Git blob，均未变化且与固定提交一致。该项是完整性核对，不等于再次全文审查 55 个文件。只读 Git 查询均退出 0；普通状态为空，ignored 仍有 `.DS_Store`、`PBS/.DS_Store`。详见 [source-checks.json](/Users/dingshinn/Desktop/pokemon-framework-reference/review/wp03-recheck-v3-2026-09-19/source-checks.json)。
- 按未变化的声明索引检查第 7 节作者类行，**19/19 均存在**；检查上轮七处责任错配的实际修订。见 [field-catalog-check.json](/Users/dingshinn/Desktop/pokemon-framework-reference/review/wp03-recheck-v3-2026-09-19/field-catalog-check.json)。未将类行覆盖率解释为全部字段语义已提取。
- 未运行游戏、Ruby、编译器、WP02 生成器或参考表达式；未进行全仓重新盘点。下文结果均为源码静态核对及推导，不是运行观察。仅写本轮独立 review 目录。

## 3. 原问题处置

以下 WP03 行号均针对 `f1d8a763`。

| 编号 | 处置 | 本轮证据与边界 |
| --- | --- | --- |
| WP03-R01 | 部分关闭，仅余 §4 | 第 71、263 行已正确区分电话默认字符串键登记、符号键探测与消费者直取；第 233 行已限定默认严格查询。第 72 行已识别数组/符号键不匹配，但将枚举结果写成无条件同时存在两个版本。 |
| WP03-R02 | 关闭 | 第 152–153 行已区分槽合并累加权重与地图/版本节重复拒绝；证据为编译器 695–708、712–725、743–757 行。同物种和等级范围的权重 20、30 合并为 50；不同等级范围不按该条件合并。 |
| WP03-R04 | 关闭 | 第 89 行已限定“读取返回 nil/false”，将文件缺失及宿主失败留为未验证；与 `001_MiscPBSData.rb:47–52` 一致。 |
| WP03-R05 | 关闭（当前责任目录范围） | 第 195–196 行补回 Type、Ability；孵化交界、Mega 数值引用、Move 优先级/反向引用、Item 数量呈现、遭遇时间与 MapMetadata 引用均按上轮要求修正。具体领域语义仍归后续包。 |
| WP03-C04 | 关闭 | manifest 对首轮 WP03 review 原件记录为 18612 字节；实际哈希仍为 `6f5bd583ee53b017828f3f3060682b31cf99eb82b5f6a82c6bc74a7eadd88846`。上轮复检原件也正确登记为 14947 字节。 |
| WP03-R03、C01–C03 | 保持关闭 | 没有相关行为回归证据，不重开。 |

## 4. 唯一剩余项：WP03-R01 [P2] 枚举不会生成不存在的版本条目

**被审位置**：`specs/kernel/wp03-content-identity-and-schema.md@f1d8a763:72`；同一表述还出现在 `planning/review-manifest-2026-09-19.md@41ac47ad` 的第七轮 R01 记录及交付摘要。

**问题**：“目标版本号 > 0 时总是同时产出版本 0 与目标版本条目”缺少条目存在前提。数组键探测在正常编译的符号键表中无法命中，这一判断正确；但它只使**已有的版本 0 条目**不再被排除，不能生成缺失的版本 0 或目标版本记录。

**证据**：`reference/pokemon-essentials/Data/Scripts/010_Data/002_PBS data/013_Encounter.rb:39–59` 的枚举从当前数据表已有记录出发，分别筛选目标版本和版本 0，没有创建记录的步骤。正常符号键来源为 `Data/Scripts/021_Compiler/002_Compiler_CompilePBS.rb:713–725`。

**影响**：仅有版本 0 时，按现文的无条件结论会预期还产出不存在的目标版本。这是本轮修订后的边界错误，不是新增领域调查要求；上轮 §4.1 验收本已包含“只存在版本 0”的情况。

**最小修订**：将第 72 行及对应交付记录收紧为：

> 在正常编译的符号键表中，目标版本 v > 0 时，枚举所有已存在的版本 v 条目；同时枚举所有已存在的版本 0 条目，不论同地图是否已有版本 v。不会生成缺失版本的记录。目标版本为 0 时，仅枚举已存在的版本 0 条目。

这段行为描述不规定未来 API，也不要求修改参考源码。对手动注入数组键或其他动态表形态不外推。

**静态验收向量**：以单一地图、正常编译的符号键表为前提，列出枚举目标版本 2 的结果。

| 表中已有版本 | 产出的版本 | 表内容是否改变 |
| --- | --- | --- |
| 0、2 | 0、2 | 不改变 |
| 仅 0 | 仅 0 | 不改变 |
| 仅 2 | 仅 2 | 不改变 |
| 两者均无 | 无 | 不改变 |

补入或明确引用这组静态预期即可；无需运行游戏或编译器。保留 `get` 的版本回退与 `exists?` 的精确组合检查，不把它们与枚举混为一个入口。

## 5. 保留未知、状态与下一步

本轮无新增独立阻塞项，也无新增非阻塞建议；剩余项仍归原 R01。U01–U10 及全部既有材料/运行限制继续保留，图鉴实际显示和宿主读取失败表现未验证。

WP01/WP02 的限定 Reviewed 继续有效。WP03 暂不升级 Reviewed，F01-02/F02-01 中 WP03 子范围仍待本项闭合，字段语义范围仍 Inventoried。R02/R04/R05/C04 的关闭结论可直接继承到下一轮，不要求重新提交同类修订。

下一步仅修正 §4 的存在条件、同步记录并给出上述静态场景，再提交实际版本差异。闭合后可按既有计划启动 WP04；本轮不启动该包，也不替提取方修改规格或状态。

交付前输入与源码一致性、报告哈希见 [final-checks.json](/Users/dingshinn/Desktop/pokemon-framework-reference/review/wp03-recheck-v3-2026-09-19/final-checks.json)。本轮到提交报告为止。
