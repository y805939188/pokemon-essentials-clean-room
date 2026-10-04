# 范围与未验证声明（WP80 净化规格集；2026-10-03）

## 当前B04-G状态（实际整合待Ultra）

接受基线 `6452c0e03025605222f3de9a272221e2b82eeda4` 为 B01/B02/B03/B05/B06 五批。B04完整候选 `50f9ca2506bf0de21c33c644569c9987f84b80a3`、作者交接 `5da06e2baf0879978a871c6952fab1105909b511`、第二轮独立报告 `c500ed089fd1192409c1c77a7a91e093c59a8a45` 为35贡献／23主责 PASS_SCOPED；13份正式文件原字节整合。本次实际新SHA及全部公共／依赖登记待同一 R-B04 Ultra，未接受 B04。规范必修229 OPEN／0 CLOSED。

[当前交接](../../review/remediation/20261003-prepare/final-integration-review.md)、[逐ID与范围登记](../../review/remediation/20261003-prepare/batches/B04/integration-stage-1/finding-registration.json)、[返修历史](../../review/remediation/20261003-prepare/batches/B04/integration-stage-1/historical-repair-registration.json)、[候选报告](../../review/remediation/20261003-prepare/batches/B04/review-round-2/report.md)、[五读者接口](../../review/remediation/20261003-prepare/batches/B04/integration-stage-1/downstream-handshake.json)。ROOT002仅34具名静态场景（地点条10／灯光5／黑暗6／图片8／计时器5）限定后继；旧WP79 source-judgments NA/EXCLUDE原字节保留，未作实际事件／素材／文件全覆盖推断。C003仅本批C-04扩展，原根与全部八扩展及其他责任保持；C061/C062两P2返修归原根，不新增ID。

五批已接受主责52，具体原修订51满足／1缺具体消费／0证据不足，严格全贡献47／5；79已接受贡献记录／76触及ID保持原口径。差别A017、A034、C053、WP80-B02-R02保留，A024仍等B07；本批候选23主责及35条新候选记录不混入接受分母。

B07四计划读＋原WP17消息＝5，B06四计划读＋原WP15音频＝5均重冻结。B04→B07必须串行，actual Ultra及父任务C接受后才以精确后继重冻结B07；B07后续WP28/WP30反向变更必须受影响B04复核。B06 WP24§5.4/PT41–63六逻辑请求与引子记忆字节不变，伙伴／雷达及其余贡献不获额外接受。未派发任务。 参考程序、运行观察、已证Demo链、行为向量执行均0；容量1024/2048为条件夹具，缺文件抛错为具名宿主前提。以下旧层按各自冻结版本保留，旧批准不转授新字节。

## 当前 B06-G 状态（实际整合待 Ultra）

已接受上游为 B01/B02/B03/B05，固定 `1fd612d47dcda164de61ab2d25a1cb5e0fbde085`。B06完整十项候选 `4076a3fbbf6fe355b73f3fe2229d1f981fe735d2`、作者交接 `ee7461e90ad5e0943e39c56c22a080f761f4e1c0`、独立Ultra报告 `70babef632539c952aa988e7762d0c2aa19cfeb3`为本批10贡献／7主责 PASS_SCOPED；八份原／净化／目录字节原样整合，本次实际新SHA及公共登记待 R-B06 Ultra。规范必修229 OPEN／0 CLOSED。

当前入口：[整合交接](../../review/remediation/20261003-prepare/final-integration-review.md)、[B06具体登记](../../review/remediation/20261003-prepare/batches/B06/integration-stage-1/finding-registration.json)、[候选复审](../../review/remediation/20261003-prepare/batches/B06/review-full-round-1/report.md)、[下游合同](../../review/remediation/20261003-prepare/batches/B06/integration-stage-1/downstream-handshake.json)。A034/B08、A059/B04/B09/B17/B21、C103/B14、C120/B16继续OPEN；候选PASS与旧批准均不代替本次实际受影响复审。参考程序／运行观察／已证Demo链／行为向量执行均0。

以下既有正文和旧公共状态按其冻结版本保留；当前状态以本层及中央后继为准。

本声明约束整个 `deliverables/final-specification-set/` 的解释方式。**使用本集前必读。**

## 1. 覆盖范围

- 本集已完成批次 1–15 的全集作者交付，对应 WP01–WP79 的 113 份静态输入（含 4 份补提取附表）。旧 WP78/WP79 的局部通过与关闭记录仅绑定各自固定被审版本；它们不代替后续最终全局审查或当前整改验收。
- 历史行为覆盖统计（WP79 v6 原被审版本）：312 个参考脚本路径中 **291 已覆盖＋4 补提取＋17 不适用（具名理由）**；33 个顶层数据文件按机制/样本/启用分层在案；113 个 Feature 全部被 84 个内容包认领。
- 当前正文为**批次 1–15 的全集作者交付**。最终全局独立审查已经完成，原报告 233 项中 229 项要求修订；这 229 项当前全部 OPEN，全集整改验收尚未完成。
- B01/B02/B05有界实际整合已接受，最新基线 `ae230e76e9c041f39c28948321d0960804c02388`；B03候选27贡献/19主责PASS_SCOPED及十三正式字节已整合，本次公共层/索引/实际新SHA仍待R-B03 Ultra。规范229必修仍OPEN、关闭0；候选局部结论不作全集、运行或跨批验收。

## 2. 未验证保留项（全部继续有效，不因净化升级）

| 保留项 | 内容 | 口径 |
| --- | --- | --- |
| U01（demo 材料缺失） | `Data/Map*.rxdata`、`MapInfos/CommonEvents/System/Tilesets/Animations.rxdata`、`Graphics/`、`Audio/`、`Plugins/`、`Game.ini`、`Game.rxproj` 缺失——**全部 demo 事件链不可验证**，不补造事件演示 | 已证 demo 事件链＝**0** |
| G01–G12（12 条 demo 候选链） | 起始/玩家元数据、地图登记、户外图清单、飞行点、训练家配置、水/钓遭遇、陆地遭遇、地牢参数、点唱机/电话、候选引用链等——仅能静态核对数据与机制，**运行表现待证** | 运行观察＝**0**（④ 级证据为零） |
| 素材与媒体 | 一切实际视觉/音频结果、动画时序、帧率与墙钟耗时、宿主 Graphics/Audio 输出 | 未运行验证 |
| 配置与备份 | Gen 5–8 backup 与 Shadow Pokémon backup 仅存在性登记（启用 U03/U06 待证）；WP02-E 未验证组合表保留；跨系统随机 U05 待证 | 存在性≠支持 |
| 插件组合 | 插件机制已静态覆盖（三阶段）；**真实第三方插件组合缺材料**（快照无 Plugins/ 目录，P05） | 机制≠组合兼容 |
| 工具/编辑器运行 | 调试菜单、编辑器、动画工具、转换/生成器的**运行与素材**（Inventoried） | 静态合同在案，运行未证 |
| 20 项来源异常（AX） | WP78 登记的 20 项参考异常事实（反直觉但有静态证据的行为） | 保留为事实，不自动修成「合理行为」 |
| 具名样本限定 | 8 个杯赛名单引用文件与 `pokemon_metrics.txt` 数据样本未读（名单引用为文件名级证据）；备份目录未全文阅读 | 不以机制冒充已读 |
| 局部未穷尽 | 动态阴影全部创建者、EventScene 实际调用者、deprecated_method_alias 登记调用点等具名未定位项 | 保留待证，不推成「不存在」 |

## 3. 证据层级口径

- **全部内容为静态证据**：已定位／静态确认／数据样本确认；**无运行确认**。
- 三类统计分别命名、不互相替代：字符串匹配（候选引用证据）≠ 阅读统计 ≠ 行为覆盖统计。
- 场景/向量（含测试目录条目）均为**静态推导预期**（输入 → 推导预期），未在任何引擎上执行；不得伪装为已执行测试。

## 4. 净化纪律（本集正文的写法约束）

- 正文只表达独立行为：目的、输入输出、条件、状态变化、数学规则、失败边界、场景与依赖；必要的兼容性事实保留行为意义。
- 参考实现的方法名、源文件路径、宿主专有对象关系与历史修订叙述**不在正文出现**，统一移至 `audit/source-traceability.md`；配置/数据/资源/命令/登记项的身份名称属于数据标识，随正文保留。
- 不把参考类层级或调用组织改写为新框架结构；不补造素材、demo 链、运行结果或插件兼容性；发现新实质行为问题时返回有界提取/复审，不在净化中夹带语义变更。

## 5. 完成度声明

- WP79 静态覆盖审查已经独立复审通过（PASS_SCOPED，2026-10-03）——这是**静态规格阶段的覆盖结论**，不是运行能力声明。
- **本集不声明完整游戏运行能力已验证**：素材、demo 事件链、运行观察、宿主输出与插件组合均按第 2 节保留。后续实现方的运行验证应以上述保留项为独立验证目标。
- WP80 全集作者交付与最终全局独立 review 已完成；当前处于 229 项必修整改的候选／整合复审阶段。B01 有界候选通过不等于全部贡献完成，最终整改关闭仍须各贡献验收及最终独立 Ultra。

当前整改身份、逐ID欠项和门禁见 [B03-G交接](../../review/remediation/20261003-prepare/final-integration-review.md)、[B03登记](../../review/remediation/20261003-prepare/batches/B03/integration-stage-1/finding-registration.json)与 [已接受主责逐ID统计](../../review/remediation/20261003-prepare/batches/B03/integration-stage-1/accepted-primary-completion.json)；原全局报告固定为 [93e10ba](https://github.com/y805939188/pokemon-essentials-clean-room/blob/93e10babe0b9c9ef8b3f5277754541b447beeeb4/review/global-independent-review/2026-10-03-fd82a639/final-report.md)。U01–U10/G01–G12/AX01–AX20与具名未知继续有效，运行观察/真实Demo链仍0。
