# R8-U08 独立候选复审

结论：**candidate PASS（有限静态规格复审）**。GR8-ELR-001 的七个 Slot 图像角色接点已实质补齐；WP08、WP15、WP69 的新增文字与固定参考证据一致。没有阻塞本候选的未修语义项。非阻塞精度说明 N01 见下文。此结论不等于实际整合 PASS、ACCEPTED 或 CLOSED，也不认证 Ruby、游戏、宿主、媒体或业务向量执行。

## 1. 固定输入与独立性

- 仓库：`y805939188/pokemon-essentials-clean-room`。
- 本次唯一待审候选：`960862ac156d9871e5f05037231cba12754b213e`；workspace tree `74fe34400f9a582a76ca8fe65fadef090d16c549`；作者分支 `revision/r8-u08-20261017` 回读时仍指此 SHA。
- 原基线：`4575e80d041ab0c74a42e2e36399d05791dbaa5b`；B8：`fd1df570cad987dc3852a3b958f03916e317f7fe`；正式子树：`f292698cdd4a8e725525a9be6dc34b75faaf151e`。
- 只读参考仓库：`y805939188/pokemon-essentials`，R：`8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`，tree：`7589c800b61ba13a13040ed0d686979b80a84fd0`。
- 语义 core：`2460370f1e410bd49cc29e377b89662838aed2b3`。原合同来源 `5caff3bd1a1b062b48b7eda46777a614921946f3` 与 C35 恢复路径各保原身份；没有把 C35 改称原结论提出点。
- 本审者为本次新委派的非作者上下文 `/root`，逻辑入口 `R8-R-R8-U08`；未参与候选编写。父来源线程 `01a13f49-a154-7054-9b04-ce31f924d01c` 是授权来源，不冒作本审者平台 ID。本审者 opaque 平台 ID 未暴露，登记 UNVERIFIED。
- 用户指定/请求配置：gpt-6.1-sol、ultra、default、normal/Fast off。实际 model/effort/tier/speed/Fast 无权威 echo，逐项 UNVERIFIED；未做 CLI 或换模型探测。
- 辅助上下文为 `/root/source_semantics`、`/root/provenance_scope`、`/root/readset_audit`；其工作是辅助核验，不另计同一 finding 的新根或多票。

执行环境创建失败（container_creation / container_service_failed），本审查改用已连接 GitHub 工具读取固定 commit/path/blob，并在 functions.exec 的 JavaScript 环境核字节、逆变换与链接。未执行本地 shell 命令、Python 作者校验器或 Ruby。工具读取与字节校验均不授业务执行信用。逐类实读、精确去重和辅助范围见 [reading-ledger.json](reading-ledger.json)；核验结果见 [verification.json](verification.json)。

## 2. 候选身份与最小改动

所有候选均为 mode 100644，三个完整镜像全文已由本审者实际阅读。下列 bytes/SHA256/Git blob 由本审者独立计算，并与固定 Git 树及作者清单逐项相符：

| 镜像对应正式相对路径（deliverables/final-specification-set/） | bytes | SHA256 | Git blob |
| --- | ---: | --- | --- |
| engine-overworld/wp15-resource-matching-and-audio.md | 27316 | a2c64f174a79089499e77aa321ca0ae3f5332d211392aeb48d37e0a24d8921d6 | 0c5932b12b9ccf1f18c02ca28f6a537c5b728ac7 |
| generic-kernel/wp08-localization.md | 30907 | fd12d77fd07ec26c13769985f73baebe800505025995fe63f9e801a06fe49e3a | 8167755e68acd3c5f3873208879f90fd062954ba |
| user-interface/wp69-slot-machine.md | 15326 | 35b518f2677a7433a645c24cb930cc502dd691f2d5bada496d1b77152441473f | 4498ff990d62b43dbdc2080fb9656a95600685ee |

基线至候选 compare 为 ahead 2 / behind 0，仅新增本批 19 文件（3 mirror、16 evidence），正式规格、planning/audit 与其它批未改。作者先提交 `ab336ac28b5d47e6be8a967eeea68ef557974c08` 的18文件，再以固定候选提交新增发布回执；回执明确描述前一已发布提交，不包含自身未来 hash。该18文件的回读身份与本审者从固定候选重新取得的字节一致。

独立逆变换结果：WP08 只删 Slot 新表行即逐字等于原文件；WP15 只恢复指定 UI 段并删除两个空身份表行即逐字相等；WP69 只删新 §2.2 与 §6.1 即逐字相等。四条新增链接的目标与锚点在“固定输入由三个候选覆盖”的虚拟整合视图全部存在。该检查不构成实际正式整合。

## 3. GR8-ELR-001 逐项语义裁决

以下候选行号均指固定 mirror；源行号均指固定 R。路径缩写：Slot 为 `Data/Scripts/017_Minigames/003_Minigame_SlotMachine.rb`，Intl 为 `Data/Scripts/001_Technical/003_Intl_Messages.rb`，BitmapSprite、AnimatedBitmap 位于 `Data/Scripts/007_Objects and windows/`，RubyUtilities 位于 `Data/Scripts/001_Technical/`。引用仅定位源证据，不复制实现。

| 验收项 | 本审者证据与最强反方 | 裁决 |
| --- | --- | --- |
| ELR-A01：缺项与当前有限义务 | 基线完整 WP08 §5.1.1 限定“指定调用者”，四组表没有 Slot；WP15 §3.2 重复同一集合，基线 WP69 主文/附表没有此接点。最强反方为“通用字符串查找已经足够”。但通用规则只决定被调用后的查找结果，不能识别哪些图像角色先查语言；固定背景对照也阻止扩大为所有图像。本候选 WP08 L66、WP15 L34、WP69 L48–64 明确接齐，未重写通用算法。 | PASS |
| ELR-A02：七角色、优先级与固定对照 | Slot L30、206、209、264、303、327、365、371 是七角色/八处调用；Intl L511–529、600–610、703、774–784 支持成功载入的当前语言域24、game→core→A。候选 WP69 L50–64 分别给缺译A、game B、core C、game优先、A仍可用及固定背景控制。A/B/C 普通非前缀、同布局同高度、前序正常的前提明确。 | PASS |
| ELR-A03：空译/普通失败/前缀 | BitmapSprite L176–195 支持六提示空译清旧图；RubyUtilities L31 与 AnimatedBitmap L5–18 支持直接转轮空串在文件名求值先失败。AnimatedBitmap L43–69 与 L141–151 区分帧前缀和普通加载捕获。候选 WP15 L113–115、WP69 L120–122 正确保留空译有效命中、普通32×32仅尝试、后继仍可能失败、前缀独立边界及不重试A。 | PASS |
| ELR-A03：准入、取消和已达前缀 | Slot L442–455 三拒绝先于图像初始化；L400–414 未下注BACK正常退出仍依序写币额与净差统计。L15–32 的对象/状态/起始随机先于符号图；L147–209 的奖额/重玩/待付显示及可能音效先于中奖图；L432–435 无本地整体收尾保证。候选 WP69 L116、124 区分未达财务尾与已写币额后统计失败，不承诺统一回滚。 | PASS |
| ELR-A04：累计保留及运行资格 | 本审者全文核固定源与候选，逆变换证明原 WP69 §2/2.1、§3–§5 全部原字节保留；原四family及 WP08 其余规则保留。22位置附表与目录未改；LZ39–41 仍专属控制帮助，S01–S16 原前提/预期保留。H/时间区间/冻结顶部/滑移随机/有效线/重玩/币额/净差统计均未扩改。 | PASS_STATIC；NOT_EXECUTED |

### 七角色的实际到达时点

| 角色 | 固定源定位 | 有限时点 |
| --- | --- | --- |
| 转轮符号图 | Slot L30，L280–282 | 三轮初始化分别查找，非全局一次替代 |
| 中奖提示 | L195–206 | 有奖额或重玩，中奖循环每次实际请求 |
| 大奖提示 | L208–210 | 中奖循环且大奖级别大于0 |
| 未中提示 | L258–265 | 无奖额且无重玩，未中循环每次请求 |
| 投入提示 | L303、365–367 | 场景初始化一次；每次进入等待投入分支再请求，后一请求在内层等待循环之前 |
| 停止提示 | L326–329 | 进入旋转处理分支时请求 |
| 按键提示 | L367–372 | 等待投入内层循环，已有下注时请求 |

背景、遮罩、按钮、线、灯、数字由 Slot L31、115、279、285、291–299 支持固定身份。候选没有新增玩家语言选择或保存写入；未到状态不预查其它角色。

**N01（非阻塞精度说明）**：WP69 L58 的“等待投入表现循环中的每次请求”可能被误读为每次迭代重查投入图。源的准确位置为上述 L365，位于内层 loop L367 之前。最强 FAIL 反方是增加查找/加载频率会改变行为；但候选 L50 已以“每次到达相应图像请求时”限定，D06 亦为“按实际请求查”，均未写每帧或每次迭代查找，故没有足以判 FAIL 的强制频率矛盾。本报告记录精确定位，固定候选未改。

## 4. 向量逐项接收

[作者 static-vectors.json](../../candidates/R8-U08/evidence/static-vectors.json) 的共同前提与15条输入/预期已完整阅读，并与固定源逐项核对。下表 PASS 仅表示静态合同吻合，全部业务向量仍 **DERIVED_VECTOR / NOT_EXECUTED**。

| 向量 | 独立语义核对 | 判定 |
| --- | --- | --- |
| D01 | 两语言层缺键，三轮分别交A | PASS_STATIC |
| D02 | game A→B、core缺键、A仍可用，三轮各交B | PASS_STATIC |
| D03 | 仅core A→C，交C | PASS_STATIC |
| D04 | game B与core C并存，交B | PASS_STATIC |
| D05 | 固定背景/遮罩/按钮/线/灯/数字不因语言映射变为可译 | PASS_STATIC |
| D06 | 七角色仅在实际请求位置查；投入时点按N01精确定位 | PASS_STATIC |
| D07 | 六提示空译清旧图、不进动画加载；后继不保证安全 | PASS_STATIC |
| D08 | 转轮空译在文件名求值阶段失败，早于普通加载捕获 | PASS_STATIC |
| D09 | 普通非空加载的可捕获错误后尝试空白；不重试A | PASS_STATIC |
| D10 | 合法数字前缀的加载/校验/分配独立于普通捕获 | PASS_STATIC |
| D11 | 包装三拒绝均先于初始化；不扩成底层共有守卫 | PASS_STATIC |
| D12 | 未下注BACK且开转分支未接管，正常离场提交币额和净差统计 | PASS_STATIC |
| D13 | 初始化已建状态/随机前缀保留，未达财务尾不提交该尾 | PASS_STATIC |
| D14 | 中奖图失败保奖额/重玩/待付及已达音效前缀；币额后统计失败可留币额 | PASS_STATIC |
| D15 | 原玩法、22位置、旧LZ39–41与四family保留；文本验证不冒业务执行 | PASS_STATIC |

作者 `validation.json` 的47项通过及 `validation-command.json` 的 Python exit0 已作为作者 TOOL_VALIDATION 证据阅读；本审者没有重跑该过程，也没有把关键词/哈希通过当语义裁决。独立字节与链接结果、原93条 commands.jsonl 的字段核对及重复原文精确去重见 verification.json；复审使用的 JavaScript 字节算法与逆变换见 [verifier.js.txt](verifier.js.txt)。

## 5. 历史、跨批与未改范围

现行 `handoff/contracts.zh.json#/records/27` 与 reviewer prompt 的完整合同逐值相等；assignment 的 R8-U08 完整对象亦相等。旧原七组合同与当前变化限定在 canonical/facet、最终历史接收及发布/关闭门；旧 OPEN 按生成时点保留。当前 `findings.json#/records/27/canonical_and_history` 与 `adjudication/root-final-history-and-canonical-reception.v1.json#/canonical_records/27` 相合。

`tasks/reference_metadata_completion/slot-history-final-join/finite-comparison.json` 的 R6-D-LZ-002 比较明确：原四family能力已关闭，48材料不认证所有48调用链，本项是新增七个 Slot 消费者精度义务。GR5-M11-004 的H/停止/22位置和旧有限过程资格独立保留。没有新增第二个通用语言资源根，没有重开旧关闭范围。该完整20项历史比较由辅助审者全文读取；本审者另实读父根/时间项及当前最终authority对应完整记录，不冒充重新完成全部历史底层审查。

当前 assignment / conflict graph 中 WP08、WP15、WP69 候选仅属U08，正式writer均为R8-INTEGRATOR；跨批实际路径冲突为空，直接/传递语义编辑前置均0。U06 对B8 WP15 L131–190的音频/长度是只读接点，原文已被本批逆变换保留，不能因新行号偏移误作丢失。U02/U05没有新增WP08/WP15写边。U01未来对同一generic-kernel目录的独立贡献由整合者保全LZ39–41；本批没有写该目录。

R8-INTEGRATOR 只映射本批三个镜像到正式目标；必要时按本项精确贡献同步 `audit/source-traceability.md`、`planning/feature-matrix.md`，并接收 [tagging-handoff.md](../../candidates/R8-U08/evidence/tagging-handoff.md) 的有限新增/受影响位置。本审者不写公共层，不预签该接收。U08无归属可选，0选入不等于全局否决其它批10可选；独立视觉policy没有在本批选入。CREB身份/mail/berry强制伴件已按条件读，其facet未被本候选采用，不扩本批源/写集。

## 6. 门状态及协调交接

| 门 | 本次状态 |
| --- | --- |
| 固定候选独立复审 | **PASS_STATIC_SCOPED**，仅 `960862ac156d9871e5f05037231cba12754b213e` |
| actual integrated PASS | **PENDING**：未提供/未形成供本审者冻结接收的实际整合提交 |
| ACCEPTED | **PENDING**：由唯一正式接收者另行登记 |
| CLOSED | **PENDING**：实际整合全文、累计保留、共享/公共贡献接收后独立关闭 |
| Ruby/游戏/原生/真实语言载入/媒体/像素/声音/保存回放 | **NOT_EXECUTED，新增执行0** |
| 业务向量 | **NOT_EXECUTED** |

候选结论无未决必修语义项；N01非阻塞。后续真实整合必须另冻结commit/tree/path/bytes/SHA/blob，非作者完整读取受影响正式整文件及累计保留，复查链接和公共/打标贡献。候选PASS不得替代该门。父任务按授权交协调 `01a14a04-b178-7567-a4eb-0f0bfac9a0d9` 处理。

本报告及伴件仅写独占 `review/remediation-eighth-20261016-prepare/reviews/R8-U08/`，以独立分支普通提交发布。其实际发布commit/tree及完整远端回读由后继 publication-receipt 与最终回复绑定，不在正文预测自身未来hash。
