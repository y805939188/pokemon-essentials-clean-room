# WP72＋WP73-A＋WP73-B v4 有限复审（2026-10-02）

**结论：行为规格已通过本批静态复审；整体暂为REQUEST_CHANGES，仅剩BATCH-R02一项P3记录更正。累计36/37 CLOSED，本轮五项行为残留全部关闭，没有新增问题编号。** 正式进入WP74＋WP75＋WP76前，只需完成一次记录更正核验，不再改行为正文。

## 已通过与保持

| 本轮问题 | 结论 |
| --- | --- |
| WP73A-R01 | CLOSED：154已改为取消不撤回嵌套类型/PBS已写变化，原无条件保证消除。 |
| WP73A-R04 | CLOSED：81/82与池专行已同时说明No不接收新集合但原数组规范化保留。 |
| WP73B-R02 | CLOSED：M05-a正确包含过滤旧边、重新生成A—B、保留C—D而不生成A—C。 |
| WP73B-R06 | CLOSED：81、M09-a与表24已区分Save No下Exit No/Yes两个结果。 |
| WP73B-R08 | CLOSED：129限定全量对应x/y，150区分预览回落与单体自动定位失败。 |

WP72的14项、WP73-A的11项、WP73-B的9项行为问题现均闭环；BATCH-R01净化、BATCH-R03状态记法保持闭环。当前三主稿、三入口表及120项目录均保持字节，下一轮不需要主稿/附表差分，也不需要重新阅读或提取参考实现。

四份diff严格从recheck-v3冻结v3重建当前v4，3＋2、5＋2个hunk全部字节一致。manifest115轮1,318条完整身份＋2旧无哈希行，TSV v90共1,223条，唯一且对磁盘零偏差；历史§2/§3/§4仅插入。上轮136份审查材料、v1/v2/v3作者材料、50份不可变依赖、16份批准与WP72保持对象全部稳定；reference固定HEAD且Git清洁。

本轮审查当前活动12份文本：WP72把更正回应/摘要合为一份note，按等效内容核验，不要求补文件凑数。净化检查通过，静态行为与元数据检查分开。未运行参考代码、游戏、编辑器、编译或行为模拟器。

## 唯一剩余项：BATCH-R02 [P3] 当轮记录仍错位

WP73-A v4回应第12/32/41行、摘要第8/13行、checks的当轮案例清单和阶段末检，仍声称v4实际修改M15/M20。与recheck-v3冻结前态逐行比较后，**v4的20条案例全部相同，M15/M20均字节未变**。这两项改动发生在v3，不是v4；同一回应还写M20不动，内部也不一致。

| 包 | v4相对v3实际改动案例 | 相对v1累计改动 | 新增/删除案例 |
| --- | --- | ---: | --- |
| WP72 | 无 | 9 | 无 |
| WP73-A | 无 | 9 | 无 |
| WP73-B | M05、M09 | 8 | 无 |

另将WP73-B附表版本链完整写出，避免省略“v3修订的前态”而把旧文件误称为v3表自身。已绑定的diff是正确的：

| 附表版本 | SHA-256前8位 | 字节 |
| --- | --- | ---: |
| v2 | `069f97b6` | 9,317 |
| v3 | `91f4a26f` | 9,680 |
| v4 | `51386600` | 9,785 |

最小修订为新增一份统一记录更正说明及实测checks，明确取代v4的错误统计/版本简称。当前主稿中的带日期v4工作量注记作为历史留存，用新更正记录澄清，不再修改主稿。旧v4作者文件同样不覆盖；无需复制整套行为回应或生成空diff。

## 当前通过的文件身份

| 文件 | SHA-256前8位 | 字节 |
| --- | --- | ---: |
| `specs/demo/wp72-debug-contexts-and-controls.md` | `d6ee4e2d` | 88,617 |
| `review/wp72-delivery-2026-10-02/revision-v3/entry-coverage-table.md` | `c9492b08` | 25,856 |
| `review/wp72-delivery-2026-10-02/revision-v2/battle-effects-catalog.md` | `6bba8070` | 11,204 |
| `specs/demo/wp73-a-content-editors.md` | `69053cf2` | 51,685 |
| `specs/demo/wp73-b-world-editors.md` | `e4c9543d` | 47,985 |
| `review/wp73a-delivery-2026-10-02/revision-v4/entry-coverage-table.md` | `48a6fc8c` | 12,511 |
| `review/wp73b-delivery-2026-10-02/revision-v4/entry-coverage-table.md` | `51386600` | 9,785 |

WP61（11/11）、WP53、WP37、WP65、WP67-A/B、GR-001～016、WP23-N01及全部旧批准保持。此次未改作者文件、登记或reference，未开始WP74～WP77、集中回填、B批整合、整体double review或WP80。

[仅记录更正的v5提示](next-task-prompt.md)；[37项状态](findings.json)；[当轮/累计计数证据](change-counts.json)；[登记与严格差分](registration-checks.json)；[检查记录](checks.json)；[最终保护核验](final-verification.json)。
