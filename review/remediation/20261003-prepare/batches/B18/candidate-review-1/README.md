# B18 FULL 候选独立复审 1

结论：**PASS_SCOPED**。精确 NEW `ee552e1cde86ed1b9bf378bda40952b4c3e7bec3` 的 B18 完整本地八贡献／五主责候选静态范围通过，未发现阻塞性缺陷，作者最小返修范围为空。本报告只签 FULL candidate；必要 affected 候选、G、精确 ACT 的 FULL／affected、限定 C 和最终 global 门仍保留。

本角色从 publication `e032b6e9a5e07e75f821bc934bbfceedd20fc039` 建立独立分支 `codex/cloud-dot-B18-full-review-1-20261010`，只新增本目录。NEW tree 为 `2ccc051bc820307b6b0cbe3ebc9ec6e355f71458`；FIX_BASE 为 B17-C `b6d5a06ab86839e7a5743095153c1d4cf340d966`，tree `b4040126c92ca8807f36f23e3959cb9689dc2a11`。下游管理合同固定在 `466cc2b33d91de749ff844dd01bedb9fc8afb799` 的 `B18/refreeze-after-B17-C-1/`，没有把管理提交当作正式正文输入。

请求配置为父工具已配置的 gpt-6.1-sol／ultra／Standard／default。没有可信 effective 回显，记 **UNVERIFIED**，按已接受 PlanA 继续，不新增认证门；没有模型 CLI／原生 fallback、子 agent、回参或配额审计，也没有默降级。本轮只执行新 Git／JSON／hash／文本元数据核验和报告写入。

## 完整范围及独立核验

先读取根 AGENTS.md，检查当前提交的 `.agents/`／`.codex/` 及适用子目录指引，没有额外适用的仓库技能／AGENTS。随后读取 publication 的 review-dispatch、完整 candidate／output manifest、整个 control-bindings、全部八项 original／approved／current 控制与其 roots/extensions、六个整个 effective-case aggregate、refreeze 合同、原稿许可、来源限制、接口、输入／复用／批准／目录／后继证据。完整对象用不可变 commit/path/blob/SHA-256/pointer 绑定，不将标题或局部例子当控制全集。

独立无路径过滤重建 C→NEW：40 个差异路径、324,603 字节，SHA-256 为 `422aca527c0a9cc48dbd9528fe1ad09914812fb7d46833027128570190cbad7b`，与发布流逐字节一致。全部 40 个路径逐一处置，包括 13 个正式路径、2 份原稿、10 份继承作者证据和 15 份新作者证据。NEW→publication 只有发布流和 endpoint 两个新增路径，NEW 既有字节均未改。

完整流只引用已发布 [C-to-NEW.diff](https://github.com/y805939188/pokemon-essentials-clean-room/blob/e032b6e9a5e07e75f821bc934bbfceedd20fc039/review/remediation/20261003-prepare/batches/B18/author-draft-2/publication/C-to-NEW.diff)，blob `450a5fa6e296fe3c2c7582e9871b97d49d6be50f`。本报告没有另复制该流或递归复制历史大型 diff。路径清单和处置见 [stream-disposition.json](stream-disposition.json)，独立核验见 [checks.json](checks.json)，完整身份索引见 [evidence-index.json](evidence-index.json)。

54 项计划身份全部核验，52 项绑定当前 C、2 项绑定不可变原审查；51 项相对已完成切片输入不变，真实 B17 变化只在索引 17／21／53。实际读取三文件完整有界差异：demo 的 GN-M19／设施 EV 场景，UI 的 K08／K11／K42／L09 和 B17 新场景，以及原 WP67-B 的剪影／动画末轮 BACK 次序。它们没有改变五主责的 source/caller 前提。UI 消费已接受 B17 字节，demo 和 WP67-B 保持只读；未消费 B19 未接受输出。[input-consumption.json](input-consumption.json) 逐项区分当前核验、准确旧阅读复用、B16 切片刷新和本轮 B17 实际阅读；身份核验不冒充 54 份全文新读。

## 八贡献的最低限定裁决

全部案例是未执行静态设计，逐项完整前提、有序结果、邻近反向、旧回归及不可扩大的边界见 [review.json](review.json)。

| ID | 独立最低限定判断 | 当前对应 |
| --- | --- | --- |
| GIR-FD82-001 | 七个真实目录的三级审计引用都落根 audit；二级反向都落不存在的 deliverables/audit；既有 Layouts 正确导航及批次／来源分离保留 | 七正文头部、traceability navigation |
| GIR-FD82-C003 | T01 的空暂持及空格 0 分别为必要前提；两次互换后手空／目标 T 可唯一推出。T18 三列保留合法整序、全零角度、空暂持及等待后新确认 true | TP T01／T18，三个 B18-C003 邻近反向 |
| GIR-FD82-C127 | 合法永久 `[A1,A1,B3]` 依槽重填为副本 `[A2,B3]`，永久保持，手选同副本，首抽 A=1/2；满槽反向仍三槽，A=2/3 | TT §4／§8、原稿 after、TT-25 |
| GIR-FD82-C128 | 后手玩家 5／对手 4 的 ACTION→UP→DOWN→BACK 为高亮 0→空导航位 4→0→回选牌，不改局面；5／5 与关闭 openhand 反向保留 | TT §5／§8、原稿 after、TT-26；Duel 边界 |
| GIR-FD82-C129 | 默认 4×4 从整序／零角度起恰五步：模式 6 为奇排列，模式 7 的 W 和为奇，不能初始完成；可逆构造及模式 4 完成反向保留 | TP §5.1／§8／§9、原稿 after、T22／T23 |
| GIR-FD82-C130 | 暂持 T 目标空→占用→空，身份不变、普通→红→普通；4／5／6 的 USE 绘制门与合法方向分开，3 及 1／2／7 对照明确 | TP §4.2／§7、原稿 after、T24／T25 |
| GIR-FD82-C131 | 整数模式 0＋1×1 首轮先完成，等待后新 BACK／USE 返回 true 并经正常包装；0＋2×1 未完成新 BACK=false | TP §2.1／§9、原稿 after、T26 |
| WP80-INTAKE-R02 | 九旧输入批准逐文件对应旧快照和登记重映射；新净化／目录及原稿行为 after 不继承旧批准。冻结自检错误以明确后继说明处理 | 九正文／附表、三 catalog 及历史纠正／注册建议引用 |

C003 完整四 root、八扩展和 CE／D007／D021／D022 仍有约束，只裁决 B18 的 C-08 T01／T18。本报告不借其他 contributor PASS 自动通过本批，也不替 B21 或其他 owner 关闭 001／C003／INTAKE-R02。原全局范围维护与公共后继登记由其既定角色继续处理。

模式 7 的 W 证明逐一人工重核全部 16 个具名合法组：交数为前四个 1、后十二个 3；每格减 1 模 4，无论越零与否都翻奇偶，五步后 W 和奇，全零要求偶。模式 6 每步单个四循环符号 −1，五步积 −1，恒等完成要求 +1。与原 S 的全偶交数不变量相容；不是生成或试跑动作。T09 的合法组／非法单格、T19 末格漏扫、T20 单行、T21 非方形缺陷和宽 1 导航未证继续保留。没有把五步改四步，也未外推其他尺寸、完整可解性、最终分布或最短步数。

两个 C003 T01 反向分别从正常合法抓 U、合法放 U 于格 0 开始，足以独立推翻缺省空态下的旧结果；T18 的未完成反向返回 false。三列修复没有丢掉最终完成确认，也没有用“任意暂存列”伪造重复块的合法库存。TT-25／26、TP T22–26 在正文、原稿、目录和后继限定一致；TT 26、TP 26，三个 C003 反向另计，Duel 12。

## 保护及准确复用

三个完整 catalog 的 804 个既有身份行按全文件行／出现次序映射，重复身份保留；802 行原字节不变，仅 TP T01／T18 改动。新增 10 行为 TT 两行、TP 五行和 C003 三行。全部 UI 的 B16／B17 行精确 C 字节保持；不是只核 TP 切片。八个未改活动的数据／状态表字节、75 项 Voltorb 顺序、22 个转轮位置、Mining 重复候选和形状均保持。

17 批／276 旧接受贡献的精确 statistics blob 未变，276 键完整且唯一，含 B16 的 24 和 B17 的 12；135 个既有 acceptance-stage 路径及 335 个 B16／B17 证据路径没有改动。canonical 229 OPEN／0 CLOSED 不变，原接受事实未被重新裁决或反签。

两原稿完整 after 与管理 carried 许可、准备 proposed-after、切片 `3d730acb28dbf48704d365536c9ff4940965f53b` 精确同字节，C before 也符合许可。没有新原稿字节或扩大范围；旧 patch 没有再次作用于 after。十份 author-draft-1 继承证据逐字节等于切片，保留旧 B16 归属；26 个核心行为节与切片一致，当前增量只做合同允许的导航、批准后继和案例纳入／计数。

来源／caller 使用准备 `c1f1597ffbb92f2ef2000e04069cad93dd471256` 的精确 source-evidence，模式 7 数学使用固定全球 review 的 mode-7-proof，并独立人工复核。九旧输入的批准使用原首审、整合 recheck-v2 和 root 对应；当前 before 九份一致，其中两份原字节相同，七份仅 +41 字节登记路径重映射。历史 ReviewPending 保持，不升级新字节。本轮核验 253 个明确项目引用身份／pointer，零缺失或不匹配；这是精确引用检查，不宣称所有被引历史正文重新全文审阅。

## 剩余门与限制

本候选没有要求作者返修的阻塞项。必要 affected 候选门仍须父级／唯一登记者按既定接口安排；齐后仅唯一登记者串行 G、普通发布与远端读回、冻结 ACT。之后独立 FULL／affected ACT 必须针对精确 ACT，完整未过滤 C→ACT 与 NEW→ACT 各发布一次，并处置原稿、目录、公共、依赖和元数据变化；只能带实际 delta 理由复用本报告。ACT 门齐后才可唯一限定 C。公共后继勘误／登记、其他贡献、非本地和最终 global 门未在这里关闭。

U01–U10／G01–G12／AX01–AX20、具名前提下的完整树果 67、未读二进制／实际地图事件／插件动态调用／媒体字体／宿主配置容量／样例／backup/gen／非本地／Demo 限制完整继承。参考、游戏、Ruby、编译转换生成反序列化、历史脚本、行为模拟与向量执行均为 0；运行观察、已证 Demo 链为 0。固定数学论证和合法静态调用链不冒充实测或事件可达。

报告只写本目录，未改 formal／public／main／reference／原报告，未自开任务，未签 actual 或 C。报告普通提交的完整 SHA／tree、远端 ref 和全部报告读回结果在最终交回中提供；[report-manifest.json](report-manifest.json) 记录除自身外的报告文件身份，避免自引用哈希。
