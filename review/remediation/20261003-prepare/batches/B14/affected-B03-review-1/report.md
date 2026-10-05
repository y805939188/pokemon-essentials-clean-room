# B14 候选对 B03 已接受接口的独立受影响复审

**最终结论：REQUEST_CHANGES，1 项 P2：B14-AFFECTED-B03-001。** 新增 FLY 成功尾序列及 WT28 没有明确要求可选回调正常返回。回调不改位置/领域状态却抛异常时，地图已经正常转移，后续等待及两个记录清理仍不会到达；这影响 B03 地点提示的飞行目的地守卫承接。天气、瀑布、实际强制路线一步的两次通用通知保持下述 PASS_SCOPED。

本报告只批准或请求修改 B03 已接受贡献的受影响接口。没有批准全部 B14、B04、WP59–61、B09-C 业务域或实际 integration。原 B03 27 条贡献/19 主责的已接受记录不被撤销；共享 root002/C003/C007/INTAKE 等及其它责任批次仍 OPEN。

## 固定输入和身份

- 候选：`47f7514765f8569ae9172bb06a2cd615e2b83b8a`；tree：`d1203c2c6a0177fb66b89acf5c7ba1cfbc511aeb`。
- 已接受 B09-C 前件：`1e6b11a47370f1c7c4659a32443fc1afda597bac`；tree：`18433d8e75ec0cddbd3227ae7e63c9d49590e375`。
- 只读独立参考：`8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`；tree：`7589c800b61ba13a13040ed0d686979b80a84fd0`。复用本人前轮独立准备的主 Git 外参考，核对远端 provenance、HEAD/tree/clean 和 connectivity；没有新 clone 的声明。
- 完整前件→候选差异，无路径排除：30 路径、577145 字节、SHA256 `2dbbb69a545b3ab0e02b897b590297d774fa89727d98feb8cfdc2dacdd41d834`。10 项正式修改为 6 最终材料和获准的 4 原文同步，另有 20 新候选/范围证据。四个原文补丁与范围批准 checkpoint `b37533ef1cfc7808ed41d64215647a78d165ada4` 对应字节一致；范围批准没有被当作正确性批准。
- B03 package 的完整 contract gate 与前件 B09-C 已接受 downstream contract 一致。四个已声明 stale reader 全部重新绑定；补读 WP61 原文/最终文中的实际通知合流。全部 6 原 ID 的当前限定、有效二审/根裁决、扩展及最低验收完整绑定在 [qualified-control-bindings.json](qualified-control-bindings.json)，不使用历史 raw 摘要覆盖最终范围。
- B03 既有 actual `e24f2ac6f43642ea0e68bd9aa21fb2c313d6ebdf`、独立 actual 报告 `dea9d118d7ed3b7ddb57b1c4e7bd40db8dd06497` 作为继承记录；本候选的新 exact actual gate 尚未提供。

完整路径/blob/SHA256/字节及旧控制对象身份见 [input-identity-manifest.json](input-identity-manifest.json)。候选 SHA 与将来外部交接的本报告 commit SHA 分开，文件不自引用自己的报告 commit。

## 原 ID 的本次限定处置

| 原 ID | 结论 | 本接口证据及剩余 |
| --- | --- | --- |
| GIR-FD82-002 | REQUEST_CHANGES | 原 MP24–27 与 WT36 的同名抑制、飞行门优先、delayed 重置保持；新 FLY/WT28 尾部前提需修订。请求只限下述新观察，其它 B21 等共享贡献未关闭。 |
| GIR-FD82-C003 | PASS_SCOPED | B03 已接受输入子型及 251 行逐行保存；天气/瀑布/通知限定案例可唯一判定。新 FLY 前提问题交叉链接，父任务决定归并；不验其它工具/战斗/编辑器。 |
| GIR-FD82-C007 | PASS_SCOPED | 三条路线前缀字面保留；67 树果表仍是有条件承诺，未宣称本轮全表读取/交付。雨类消费者仅接口复读。 |
| GIR-FD82-C094 | PASS_SCOPED | 连接跨图 enter0→容器20 与显式重建转移0、类型差异/进行中显示守卫一致；非完整天气渲染器验收。 |
| GIR-FD82-C095 | PASS_SCOPED | 朝向/瀑布顶/direct/menu/普通交互及 true 但未启动差别保持；既有 WP12 后续推进/状态恢复保留。 |
| WP80-INTAKE-R01 | PASS_SCOPED | Weather 用 ASCII U+003D；原正确形式及 B03 s:/size/route 字面保持。全域字符输入其它责任未关闭。 |

逐 ID 控制对象散列、原严重度、理由、证据、剩余、验收见 [affected-dispositions.json](affected-dispositions.json)。相邻 C103/C104 的通用通知/煤灰合流为接口 PASS_SCOPED；C088 只审 FLY 回调/清理组合并请求修改，未批准完整 C088。

## 独立来源与成对静态判断

连接跨图以玩家不再移动、已越当前边界、有效连接图为前提：enter 通知写雨强度 60/时长 0，地图容器随后写时长 20。显示消费者在天气类型不同才请求淡变，正在淡变可以拒绝，20 是正时长的固定淡变选择，不能译为 20 秒。合法显式重建转移没有连接尾写，仍为 0；同图不触发 enter、同类不改类型/强度但连接调用者仍能写 20 的对照保留。固定 MapFactory/SceneMap/Overworld/GameScreen/GlobalSprites/Weather 分支与 WT07/WT09、WP11§4 一致。

瀑布启动要求朝上且面对瀑布或瀑布顶，置 ascending/through、增加统计，启动本身不立即迈步。向右面向瀑布满足菜单资格/效果返回真却不启动；向上瀑布顶的直接确认入口可启动，菜单拒绝、普通交互只描述。WT33 与 MV64–66 和 WP12 后续离开地形/DEBUG CTRL 恢复规则相承接。没有把真实地图或媒体未读提升为运行成功/失败事实。

正常主场景、非冰滑/瀑布、实际玩家平移完成、无中断/转移且后续 WAIT 使路线仍强制时：位移完成一次通用通知；玩家随后步后入口再次通用通知，并在仍强制路线或解释器门早退。全局步数/玩家周期不增。两层煤灰、持袋及初值≤9997可分别擦除并资源/统计增 2；普通玩家、NPC、直接调用步后入口、已结束路线或自动移动门是相邻不同输入。新 FP01/FP02/FP33、原/最终 WP61§2/3.1 保留这些前提，没有把所有一次实际移动统一成双通知。

三条兼容路线字面 `move_random_range`、`move_random_UD`、`move_random_LR` 及大小写保持；命令45求值与字面分支顺序保留。树果读取天气意图的 Rain 类别而非可见粒子，Storm 也属 Rain；只核这个既有读者接口，未重新审全树果状态机。Compiler 只作为文本核对 ASCII 字段分隔符，未运行编译器。导航范围/完整参考 blob 身份见 [source-reading-log.json](source-reading-log.json)，范围不是分支覆盖证明。

## 新 P2：FLY 可选回调异常切断尾部

定位：[最终 WP59 表及前提](https://github.com/y805939188/pokemon-essentials-clean-room/blob/47f7514765f8569ae9172bb06a2cd615e2b83b8a/deliverables/final-specification-set/engine-overworld/wp59-world-time-weather-field-moves.md#L251)、[原 WP59 同步位置](https://github.com/y805939188/pokemon-essentials-clean-room/blob/47f7514765f8569ae9172bb06a2cd615e2b83b8a/specs/overworld/wp59-world-time-weather-field-moves.md#L274)、[WT28](https://github.com/y805939188/pokemon-essentials-clean-room/blob/47f7514765f8569ae9172bb06a2cd615e2b83b8a/deliverables/final-specification-set/test-catalog/engine-overworld-wp11-15-59-60.md#L347)。正文要求目标有效、转移正常返回、回调不改位置/状态；WT28 只限定回调不改位置，却都把回调后的等待、清逃脱点、清飞行目的地作为完整预期。

固定参考 [FLY 工具](https://github.com/Maruno17/pokemon-essentials/blob/8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b/Data/Scripts/012_Overworld/004_Overworld_FieldMoves.rb#L471) 在转移、自动地图 BGM 和刷新后调用可选回调；它随后才等待，退出淡变块后才清两个记录。[fade 包装器](https://github.com/Maruno17/pokemon-essentials/blob/8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b/Data/Scripts/007_Objects%20and%20windows/002_MessageConfig.rb#L559) 的 ensure 恢复淡变/释放视口，没有吞异常或执行 FLY 两个记录清理。[地点提示 update](https://github.com/Maruno17/pokemon-essentials/blob/8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b/Data/Scripts/012_Overworld/001_Overworld%20visuals/002_Overworld_Overlays.rb#L28) 又先检查 fly_destination，之后才重置 delayed 计时并检查消息/地图变更。

反例是直接工具的明确可选参数，未执行：合法目标/个体及正常场景资源，非空逃脱点；演出、地图转移、BGM、刷新正常返回；回调不写位置或领域状态，只在调用处抛普通异常，fade ensure 的宿主更新/清理正常返回。地图和统计前缀已提交，而 0.25 秒等待未请求、两个记录清理及正常 true 返回未到达。这个输入满足“地图转移正常返回、回调不改位置/状态”，不满足尚未写出的“回调正常返回”。若再有合法安排的地点提示更新机会，保留的 fly_destination 仍使飞行门先返回；此处没有声称未处理异常后默认游戏会继续运行。

成对正向对照：可选回调不存在或正常返回，且不写位置/相关领域状态，后续等待/淡变清理/记录清理正常时，完整成功尾序列成立。表头“成功转移能力”不能替代 WT28 中具体地图转移与整个工具正常返回的区分。

最低修改是在原文、最终文、WT28 及作者追溯中补相同的正常回调/相关状态前提，增加上述异常切点静态对照，保存已提交前缀和未达尾部、条件式地点提示守卫结果。无需新增回滚实现、参考执行或全宿主异常合同。固定 Scripts 普通调用点搜索没有找到传可选 block 的调用者；默认菜单/插件/真实事件可达未证，这个限制必须保留。详见 [findings.json](findings.json)。

## 保存性、审查顺序与边界

两目录静态设计合计从 480 到 503：旧 480 中 19 行改写、461 行字节不变，23 行新增；B03 MP/MV/EV/FW/IM/MR/DG 共 251 行全部字节/顺序保留，B04-R 28 行及树果 BP01–17 含 GR-012 保存。原 B03 正式 13 文件除共享 engine catalogue 外均不变。这是回归证据，未替代调用者/条件复读，未给予不相关新 WT/FS/BP/FP 全域语义批准。详见 [catalog-preservation.json](catalog-preservation.json)。

[独立首判](independent-first-judgment.json) 于 2026-10-05 14:29:13 UTC 保存 PASS_SCOPED，SHA256 `018879c0d76a1a0a47ef495347dd1d35c565c420d837456d5fddc649092a747f`，在读取候选 contributions/AREG/validation 自证前作出。首判范围覆盖核心天气/瀑布/双通知/兼容和保存性，保持原字节。随后对照作者说明并独立挑战相邻 FLY 可选回调切点，发现新反例，最终改为 REQUEST_CHANGES；不以首判历史覆盖最终结论。[author-comparison.md](author-comparison.md) 与 [independent-final-judgment.json](independent-final-judgment.json) 明确这个变化。

本人新写文档/身份核验通过 685 项，另有 57 项新报告身份/一致性核验通过；这些结果仅为 Git/文档库存及报告一致性 PASS，语义结论另行 REQUEST_CHANGES。完整差异原始 `git diff --check` 返回 2，57 条警告全部在四份按批准字节保留的原文 patch 文件；正式材料/其余证据单独检查通过，不能称原始检查整体通过。没有执行作者或旧 reviewer verifier，也没有执行任何静态行为向量。见 [independent-validation.json](independent-validation.json)、[review-document-validation.json](review-document-validation.json)、[command-log.md](command-log.md)。

保留 U01–U10/G01–G12/AX01–AX20：二进制/序列化地图事件、宿主/可执行程序、媒体、八杯赛表/metrics 样本、backup/gen、实际插件/动态分发/弃用别名/EventScene/dynamic shadow/真实 Demo 未证；其它未列范围未读。运行观察 0，已证 Demo 链 0，参考/游戏/Ruby/编译/转换/生成/反序列化/模拟器/求解器执行 0，行为向量执行 0。canonical 229 OPEN / 0 CLOSED，不自行关闭 finding。

请求配置 gpt-6.1-sol / Ultra / Standard(default)，按已接受方案 A 保留实际配置 UNVERIFIED；无降档/加速/派生、配置探针/额度检查及 child task 均 0。只新增本报告目录，普通提交到 `remediation/20261003-prepare/review-B14-affected-B03-1`，核远端 SHA。候选整改后还需固定新候选复审；本轮完成后停等父任务实际 integration 新 SHA，不能移植旧 PASS 或预支 actual 核验。完整执行边界见 [execution-request-receipt.json](execution-request-receipt.json)。
