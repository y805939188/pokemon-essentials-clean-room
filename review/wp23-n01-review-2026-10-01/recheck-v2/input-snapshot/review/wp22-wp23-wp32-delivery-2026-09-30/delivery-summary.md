# WP22／WP32限定回填与WP23三项修订 — 有限复审材料 v3（WP23限定Reviewed管理性回填同步）

2026-09-30；规格提取方。独立首审结论：**WP22／WP32 PASS_SCOPED，WP23 REQUEST_CHANGES**；独立有限复审结论：**WP23 PASS_SCOPED（R01～R03全部CLOSED）**。本次已按有限复审报告§4将WP23主附表头尾与F06-08的WP23子范围管理性回填为限定Reviewed，并同步WP32及本目录活动材料中WP23的当前状态／完整身份。净化、Hyper、N01行为未改；N02宿主行为保留；不进入主线下一批。

## 1. 当前主稿／附表身份

| 包／文件 | 状态 | 完整SHA-256 | 字节 | 场景 |
| --- | --- | --- | ---: | ---: |
| WP22 [wp22-mega-and-primal-reversion.md](../../specs/pokemon-rules/wp22-mega-and-primal-reversion.md) | Reviewed（限定范围） | `894fa8e0d18dc7a5823e8c51b85cefd23f9f955b08fde6a7621533a48b8302f3` | 25,402 | 25 |
| WP22 [wp22-transformation-data.md](../../specs/pokemon-rules/wp22-transformation-data.md) | Reviewed（限定范围） | `310956bf2c308626f3035b86fd256e35e68fdc58d340c3d941e07f8cdc9a03e3` | 6,410 | — |
| WP23 [wp23-shadow-hyper-and-purification.md](../../specs/pokemon-rules/wp23-shadow-hyper-and-purification.md) | Reviewed（限定范围，管理性回填）＋ReviewPending（N01 子项修订 v2，2026-10-01 待定点复审） | `cda848c3172f63d213a64674d7d39662e3c332018e6bb414bda54450a4ad655b` | 47,455 | 46 |
| WP23 [wp23-shadow-data-and-vectors.md](../../specs/pokemon-rules/wp23-shadow-data-and-vectors.md) | Reviewed（限定范围，管理性回填） | `20a561cb27c6b6d164ad3f6814aa0d926ea0ba1389cfc85a7118a097170b7457` | 13,995 | — |
| WP32 [wp32-contextual-trade-and-post-battle-evolution.md](../../specs/pokemon-rules/wp32-contextual-trade-and-post-battle-evolution.md) | Reviewed（限定范围） | `06d990a7ae652d0f656131ac3ef5f7555a0124ae2304c34e5ed33467d47aff4d` | 30,435 | 38 |
| WP32 [wp32-context-inputs-and-scenarios.md](../../specs/pokemon-rules/wp32-context-inputs-and-scenarios.md) | Reviewed（限定范围） | `5ae30fa1105776063a7455ff41ffbecc41a984a0a9482a5a6970f190063d8ca0` | 10,203 | — |

六份被审v1完整身份保留在首审报告§1、各主附表尾注、wp*-fixed的review_history与本轮input-snapshot；WP23被审v2完整身份另保留在有限复审报告§1与wp23-fixed.json的review_history。当前字节不冒充被审对象。场景25／46／38，共109条，均为静态预期，不是运行测试。

## 2. 修订与确认范围

- R01：净化室跨级恢复的首个能力窗口缺更新回调；明确E1000／S416→目标1332，但失败时已写1331，未到学招／进化／昵称／存放／清中心。补同等级S0、遗迹石对照，并限定O03到达前提。
- R02：替换比较原始Shadow查询结果，nil／false不归一；补三组返回值对照，蛋替换例要求原始值匹配。
- R03：普通默认Battle M4000／G0写存储Hyper真并请求进入提示，有效查询仍假且同前提可重复；不扩到插件、小量表或回放。
- N01：已按独立确认有限同步WP31旧第114行摘要及完整身份引用；N02维持静态双调用／宿主未决，WP26未改。

WP62回填和WP38／C03同步已获本轮受理，本次不再修改它们；WP22／WP32只回填状态、N01同步状态和必要依赖身份，不改变其它已接受行为。

## 3. 核对与材料

- [self-checks.json](self-checks.json)：逐包自检与当前身份；`c406e6445f67a79439fd192655f6b228462ea805ab1eeba39042cbd39e29fdca`，35,439字节。
- [boundary-checks.json](boundary-checks.json)：六组交界／46条完整绑定；`bb766c24baa044bb354fe90e34c368ff3b8178b5f2b1015bbc2f098c6a599985`，22,843字节。
- [new-observations.md](new-observations.md)：九项观察的独立判定与处理；`34e5049496914d11ee17944757fc4358d0eaae834c80a093a409654e92bf6089`，5,415字节。
- [source-identities.json](source-identities.json)：66条来源文件身份；仅具名段语义核对；`778703d7535a5a1389ce834901dbd9a8396a72c18630d6d3204506a7f1334918`，46,521字节。
- [revision-v2/preflight-checks.json](revision-v2/preflight-checks.json)：13项与876输入／快照及12轮历史预检；`8d896471cbd43e4caa5f5d78089162474d43348b467fb9e83eef4ad1cc9ff38e`，7,904字节。
- [revision-v2/targeted-checks.json](revision-v2/targeted-checks.json)：固定算术与调用者／原始返回值／G0边界核对；`4f56c49e7c81eb52ba63b2c3c9d125af23aeb3c3d5664b2cf0fbb5a69a6026ed`，2,557字节。

逐项回应及本轮差异见[revision-response](../wp22-wp23-wp32-review-2026-09-30/revision-response.md)与[revision-diffs](../wp22-wp23-wp32-review-2026-09-30/revision-diffs/)；本轮所有差异从**本轮首审input-snapshot**重建至当前目标，不复用更早闭合轮作为新差异基线。旧backfill-response／六份backfill-diff／diff-bindings为第六十三轮历史，保持原件，其目标由本轮快照核对。

当前最终只读登记／哈希／JSON／链接／差异／白名单结果见[validation-results.json](validation-results.json)。本轮仅运行审查过写入范围的自有文本／哈希／固定算术检查，没有运行旧交付生成／登记脚本或参考模型。

## 4. 登记与停止

现有manifest续**第七十一轮**、主TSV续**v46**，保留旧行与历史链；F06-08分别为WP22、WP23限定Reviewed（WP23 另有 N01 净化室选择可达性子项 2026-10-01 修订 v2 待定点复审，见 `review/wp23-n01-delivery-2026-10-01/`），F09-04为WP32限定Reviewed，前向范围保留。限定通过集合＝WP01–WP36、WP38–WP52（47=A/B，52=A/B/C）、WP54–WP60、WP62；仅各包具名静态范围，不是整个游戏运行通过。

备妥有限复审后停止，不启动主线下一批，不接管用户另行安排的独立工作；未创建任务／Agent、未发其它会话消息、未提交／推送。Demo、宿主、媒体、插件、U01–U10与WP78→WP79→WP80保留。

首稿摘要历史：`b2d16704d7ef0990eab88860c51ccb9c36a088663dd3e3e45604ec0e38808921`，5,299字节；v2摘要历史：`055425c0f344492a62230d6a8dd5d8b44c0f8e825f88929b11a5b175b84e2f13`，5,696字节；原“三包ReviewPending／105场景”与“WP23 ReviewPending”属于各自送审时点，不覆盖本轮状态。
