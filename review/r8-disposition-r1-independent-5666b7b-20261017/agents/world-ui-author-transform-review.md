# 作者转换、policy与接受回填的独立只读校对

固定受审候选为 `5666b7b912e2fb79b5119283ee6a37401a7071db`。本次补充结论为 **限定PASS：未发现仍以关键词自动重分去向、非历史policy显式行动与主清单不一致，或U02/U03接受被扩大**。主审中 `WORLD-CATALOG-F01` 的反向目录串域问题仍为FAIL；本补充没有推翻语义审查或宣称整个候选通过。

完整机器结果及逐736 ID、47新增、32退役的一致性核对见 [world-ui-author-transform-review.json](world-ui-author-transform-review.json)。本次只写这两份新review文件；未运行、导入三份作者脚本，也未执行任何mutator、游戏、业务向量或原型。

## 实际阅读与输入身份

已完整阅读固定候选中的三份脚本，共1,247行，工作区字节均等于固定Git对象：

| 文件（均在 `revisions/r1/`） | 完整新读范围 | SHA256 |
| --- | --- | --- |
| `revise-data.py` | L1–929 | `70f19b658dcc8b45f231135e0d04a70614252cc821e46b2780489b752f7b4ea2` |
| `report-revision.py` | L1–221 | `abfde490e648bc8dd862afaefef0f10cf1aaa424066e40994203fdb42d376ece` |
| `tools/backfill-u02-u03.py` | L1–97 | `f661b503f9ae4e4686d01f5c6509bd8c3d4db5797d95c088de3676ebe60305fe` |

`routing-policy.json` 的8个非legacy顶层字段全部解析、逐字段遍历并与完整脚本文字和主清单对照。其2.68MB显式行动表有736个ID、6,623条行动；重复记录按395个完整语义载荷去重检查：184个显式修订载荷、173个直接引用载荷、38个拆分载荷。其中181种显式reason字符串全部为已完整阅读脚本中的文字常量。没有把重复模板的解析或源定位清点冒称新的正式正文全文阅读。

本次另读了 `routing.py` 的初始化、标题解析、seed拒绝和CLI分派相关范围；完整读取正式U02/U03回执，并独立核对B8→908的完整正式子树差分。正式正文语义沿用已完成的分域独立复核，本补充没有重新声称全正文阅读。

## 分类与policy关系

`revise-data.py` L46–65为旧行补当前有效范围、直接引用和职责字段，保留原去向；L68–185的edit/add/child/retire辅助只落实传入的显式决定。L187–849的实际修订按具名ID、具体源节、字面职责和范围表选择目标。`startswith`用于解析明确文档别名或取来源摘录，正则用于标题定位；这些路径没有用目的/术语等关键词重新决定功能去向。

`routing.py` L148–149直接拒绝seed；CLI读取主清单及章节覆盖，代码没有加载routing-policy。policy的实际作用是记录显式行动和解释来源；`legacy_initial_policy_snapshot`只保历史算法，不是现行重建权威。`revise-data.py` L22–23还明确拒绝在接受事件存在后重跑旧迁移，避免覆盖当前适用快照。

全量独立核对得到：

- 736个policy ID与活跃主清单集合相同；6,390条直接引用的逐ID去重集合与主清单完全相同。
- 所有旧ID的policy行动列表与feature-resolution行动列表一致；每个最后生效的非模板rationale与当前future_plan一致。
- 38处父子拆分的ID、源范围和excluded_child_refs一致；47个新增单元的文档、source/scope范围及reason一致，未复用旧ID。
- 32个policy退役与主清单退役原因、元数据ID、替代关系和finding关系一致；退役去掉retirement后等于d62完整旧行。
- policy新增/退役表与new-and-retired-units逐字段一致。上述错误均为0。

这些检查证明显式记录与固定产物一致，不能代替依赖必要性和职责语义裁定。通用职责模板也不会自动产生独立验收信用。

## 报告与接受回填

`report-revision.py`生成作者问题映射、元数据/依赖/阅读/合理PASS传播台账和R1 README；没有写主清单、policy或正式规格。42组手工说明与2组root工具问题分别保留作者待独立复审状态，没有把作者计数/assert变成PASS或CLOSED。阅读台账明确否认全正式clause与目标兼容通过。

两份历史作者脚本从 `/tmp/r8-disposition-review-a0352c7` 读旧报告，没有自行对这个临时目录作Git哈希断言。本次没有依赖该临时目录：直接从固定 `a0352c7fba38391afc535525988245701d5ce202` 比对全部721条旧verdict、reason和finding_refs，错误0；全部721个immutable source与d62相同。

`backfill-u02-u03.py`固定回执提交 `861f7a44a6f763c265a11761ab17a8ec3b55f304` 与路径，核验batch集合恰为U02/U03、ACCEPTED与actual_integrated_PASS真、CLOSED假；核验共同payload和两份文件完整身份，要求正式差分路径恰等于这两份接受文档。

对受审产物重新核对131份当前文档身份和736条活跃当前locator/状态：恰17条位于接受文档，实际功能文本变化仅 `FR-000403/588`。191条批次绑定中174条继续pending。全体去向仍待验证、阶段待定/未批准、未实现、未验收。所有文档/locator指向908是后继观察快照更新；源接受只给两份文档，没有扩为其余批次、CLOSED或实现验收。身份、locator、状态范围错误0。

两处实际正式差分分别为WP04 §5.2移除特定改写提示承诺、WP60树果§3.3把“多数”改为五果具名样本；没有额外正式文件变化。32个退役完整旧行没有被回填改写。

## 保留问题与限制

`revise-data.py` L907–916的apply_catalog_corrections只对三份明确目录作子体系排除，漏掉反向Pokemon目录。故已确认的 `/sections/2277–2292` Fishing/Slot/Mining误消费者（含新增728/730）仍存在。这是显式消费者决定覆盖不全，归既有WORLD-CATALOG-F01同根问题；本补充不重复计新根。

本次静态检查最初把审者额外计算的line_count与作者五字段identity整对象比较，产生131个审者检查假差异；已按commit/path/bytes/sha256/git_blob五字段纠正，131份均匹配。该诊断过程保存在JSON中，未改候选，不计候选finding。

实际model、thinking、service tier、speed、Fast与云任务UUID继续逐字段UNVERIFIED。没有新增正式整改、业务运行或原型验证信用；剩余语义阻塞仍以主分域报告和root整合裁定为准。
