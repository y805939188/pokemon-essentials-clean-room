# B14 候选二：B03 独立受影响复审

**PASS_SCOPED。** 固定候选 `af39efbf32549be964cb083bd49bed6d1d5c0d2a` 在本 B03 受影响接口范围内承接了三项首轮修订：FLY 正常/异常尾部及地点提示门、树果公共时间戳顺序、WP16 水花重置/普通更新。未发现新的本范围阻塞项。此结论不批准全部 B14 24 贡献/19 主责、B04 全域、B09 业务域或实际 integration。

## 身份、范围及完整差异

| 输入 | 精确身份 |
| --- | --- |
| 候选二 | `af39efbf32549be964cb083bd49bed6d1d5c0d2a`，tree `932ffac11a2701ddb432516e7bd07aa990fd326f` |
| 候选一 | `47f7514765f8569ae9172bb06a2cd615e2b83b8a` |
| 已接受 B09-C | `1e6b11a47370f1c7c4659a32443fc1afda597bac` |
| 只读独立参考 | `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`，tree `7589c800b61ba13a13040ed0d686979b80a84fd0` |
| B03 首轮报告 | `06dd362d2eb2674453646c899c9fd76af0841c8e`，仍 REQUEST_CHANGES |
| full R14 首轮报告 | `0579404a69952d24e9901664a611f5a05a01877e`，仍 REQUEST_CHANGES |
| B04 首轮报告 | `3aa4c41de2f58bd65405bc0855a7f45155a878c2`，仍 REQUEST_CHANGES |

两段完整无排除差异均独立生成并检查实际修改：

| 完整差异 | 路径/字节 | SHA256 |
| --- | --- | --- |
| B09→候选二 | 46 / 690132 | `64fa7af7383bbc0ab03e56eadff84d1b79a8854463b0d99dce3c38a139099af9` |
| 候选一→二 | 22 / 135924 | `cc70984763bc52d8825cea6d394171a1cb1dcc3051a26903488de1aec44558a3` |

方法为 Git binary/full-index/no-renames/no-ext-diff/no-textconv/no-color diff，无路径过滤。累计 12 正式路径（5 原文/7 最终），另 34 新 B14 范围/作者/候选证据；增量为 8 正式修改和 14 新候选二证据。原四原文批准 `b37533ef1cfc7808ed41d64215647a78d165ada4` 及候选一 20 项证据全部保留。获父任务追加批准的 berry§5.2、原/最终 WP16 单水花句及同范围 FLY 前提修订逐一核 before/after/补丁散列；追加范围不是正确性批准。

四个 B03 stale reader 及补充 WP61/WP16/原文依赖重新绑定。72 计划输入、6 原写入输入、14 额外输入按各自固定版本核身份；在候选树外的原审/规划对象仍绑定其独立 commit，不能误当 B09 树内文件。两个完整目录锁、B03 actual/旧独立 report 及 B04/B08 依赖版本保存；这只是身份核对，没有声明重新语义批准全部输入域。完整字段、所有路径/blob/SHA256/字节见 [input-identity-manifest.json](input-identity-manifest.json)。

## 三个首轮观察的独立二轮判断

| 原观察 ID | 原级别 | 本候选处置 | 本次边界 |
| --- | --- | --- | --- |
| B14-AFFECTED-B03-001 | P2 | PASS_SCOPED | FLY 可选回调/尾部与 B03 地点提示飞行门 |
| R-B14-1-001 | P3 | PASS_SCOPED | 树果共同时间戳及旧雨读取的相邻顺序 |
| B14-B04-R1-01 | P2 | PASS_SCOPED | 单水花句与 WP59/WT31 的相邻天气状态 |

三份首轮 report/finding 对象和原严重度不改写，不将这些本候选观察判定转成 full R14 或 B04 独立 receipt；不闭 canonical finding，不重复登记新根因。逐项前提、正/反例、剩余、验收及原/最终/源固定证据见 [findings.json](findings.json)。

FLY：[原/最终 §5.7 成对对照](https://github.com/y805939188/pokemon-essentials-clean-room/blob/af39efbf32549be964cb083bd49bed6d1d5c0d2a/deliverables/final-specification-set/engine-overworld/wp59-world-time-weather-field-moves.md#L260)、WT28/WT39/WT40 明确无回调或回调正常返回且不写相关状态，并固定后续等待/演出边界/记录清理正常。有效 D=(M,7,5)、个体、非空 E、统计 N 和正常前缀时，[固定工具](https://github.com/Maruno17/pokemon-essentials/blob/8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b/Data/Scripts/012_Overworld/004_Overworld_FieldMoves.rb#L471) 先提交 N+1、朝下目标落位及 BGM/刷新，再调用可选回调。[fade 清理](https://github.com/Maruno17/pokemon-essentials/blob/8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b/Data/Scripts/007_Objects%20and%20windows/002_MessageConfig.rb#L559) 不吞回调异常或清 E/D。WT39 回调不写状态却抛普通异常：0.25 秒等待未请求，E/D清理与正常 true 未达，记录保留；WT40 无回调/正常回调则按完整尾序列先清E再清D并true。两正文 §§5.3/5.4/5.7/7 与追加追溯同步，外层忽略结果仅指工具正常返回，不补造异常时外层true。

地点窗只在另行合法安排未处置 update 时比较：[飞行门](https://github.com/Maruno17/pokemon-essentials/blob/8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b/Data/Scripts/012_Overworld/001_Overworld%20visuals/002_Overworld_Overlays.rb#L28) 先于 delayed计时重置、消息/换图处置。D保留则早退；D清除后曾延迟者才重设计时。没有宣称未处理异常后游戏继续，固定普通菜单/道具搜索未找到传block，插件/真实事件到达未证。MP27、WT36及原地点条合同保存；不是全宿主异常合同或全部旅行能力批准。

树果：[两正文 §5.2 公共顺序及 BP18](https://github.com/y805939188/pokemon-essentials-clean-room/blob/af39efbf32549be964cb083bd49bed6d1d5c0d2a/deliverables/final-specification-set/pokemon-rules/wp60-berry-plants.md#L80) 与 [固定结算源](https://github.com/Maruno17/pokemon-essentials/blob/8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b/Data/Scripts/012_Overworld/006_Overworld_BerryPlants.rb#L97) 一致：覆盖物修正先于机制分支；共同存活时长、阶段、时间戳写入后，才旧阶段浇水/雨读取或新干涸。旧已种植对象、基础3h/GROWTHMULCH、原时长0/阶段1/原戳T−32400、本次取整T、有效Rain天气、无重植/其它相关写入且后续正常，按序得到32400→阶段5→戳T再旧分支。未种植/时差≤0在共同写前返回；无覆盖物9h为阶段4；重植上限reset/return另列；普通旧显示不结算。不推导旧UI施肥或默认故障到达。若另显式给后置分支人工失败，已提交的公共戳不能被倒推为未写；未执行或新增强制运行设计。本修订处理已接受B09残留断言，不计作B14新引入回归，也不批准完整C100/树果域。

水花：[原/最终 WP16 的唯一同步句](https://github.com/y805939188/pokemon-essentials-clean-room/blob/af39efbf32549be964cb083bd49bed6d1d5c0d2a/deliverables/final-specification-set/engine-overworld/wp16-world-rendering-and-visual-transitions.md#L162) 与 WP59§4.1/WT31及 C092 当前限定一致。[固定选择/重置/更新](https://github.com/Maruno17/pokemon-essentials/blob/8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b/Data/Scripts/012_Overworld/001_Overworld%20visuals/001_Overworld_Weather.rb#L210) 表明默认雨类四图下，从0起奇数1取末张水花，偶数0为雨滴；有效可见水花到期重置寿命0.40时为255并同次返回，普通未重置更新剩余0.30→0、0.19→255，水花不沿雨滴速度漂移。没有通过改WT31或退回正确WP59来迎合旧句。两WP16仅这一行改变，其它资源/速度/色调/渐变/Snow/Sun/Storm/地点提示字节保留；只判断状态，未观察屏幕帧。此为既有B04依赖残留的有界承接，其自身candidate/actual gate仍独立。

## 六个原控制及 B03 回归

所有当前限定、有效二审/root裁决/完整扩展及最低验收按固定全对象绑定，历史raw摘要不覆盖最终限定；范围见 [qualified-control-bindings.json](qualified-control-bindings.json)。

| 原 ID | 本次处置 | 独立来源/反向判断及剩余 |
| --- | --- | --- |
| GIR-FD82-002 | PASS_SCOPED | FLY异常/正常尾部、飞行门优先及delayed时点相符；同名/禁配对保存。B21等覆盖层其它责任仍OPEN。 |
| GIR-FD82-C003 | PASS_SCOPED | B03子型/行字面保存；WT28/39/40及BP18唯一前提/先后承接；其它工具/战斗/编辑器贡献未关闭。 |
| GIR-FD82-C007 | PASS_SCOPED | 命令45正常求值后的三条准确行首前缀保留，前置空白/大小写反向仍不同；67表承诺条件式，未全表重新交付。 |
| GIR-FD82-C094 | PASS_SCOPED | 连接越界、不再移动、有效目标：enter天气0→容器20；显示类型差异/进行中守卫。有效显式每图重建没有20尾写；20不等20秒。 |
| GIR-FD82-C095 | PASS_SCOPED | 朝上+瀑布/顶启动；向右menu效果true无启动；朝上顶direct启动/menu拒绝/交互描述。WP12逐步离地形/DEBUG CTRL恢复保留。 |
| WP80-INTAKE-R01 | PASS_SCOPED | ASCII Weather U+003D与UFF1D反向门及B03 s:/size/视线/路线字面保持；其它输入域仍OPEN。 |

C094复读 MapFactory/SceneMap/Overworld/GameScreen/GlobalSprites/Weather 时，区分每图重建与仍继续驱动的全局天气对象，不声称显式转移重建全部显示。同图/同天气类型跳过、新类型但进行中拒绝的相邻对照保持。瀑布启动置统计/标志/through而不即刻位移，后续推进清理仍引用WP12。

C103/C104只审通知合流：正常地图场景、非冰滑/瀑布、玩家实际平移完成、无中断/转移且后续WAIT维持强制路线，角色完成先发通用通知，玩家步后入口再次通用通知并早退，全球步数/玩家周期不增。两层煤灰、持袋、初值≤9997可擦两层、资源/统计+2；普通玩家、NPC、直接步后入口、已结束路线和自动移动门不同。FP01/02/33、原/最终WP61仍一致；没有重新批准整WP61。逐ID evidence/remaining/acceptance见 [affected-dispositions.json](affected-dispositions.json)。

两个目录480→503→505：全部旧ID顺序/数量保留，候选一503中只改WT28和BP18，其它501行字节不变，新增WT39/40。对B09旧480则仍19改写/461不变、新25行。全部B03 MP/MV/EV/FW/IM/MR/DG的251行、B04-R28、BP01–17含GR012及engine目录H段前整体字节保存。13个B03正式owner文件除共享目录外12完整文件不变。以上是保存性证据，未替代新调用条件复读，也没有批准不相关WT/FS/BP/FP语义。详见 [catalog-preservation.json](catalog-preservation.json)。

## 顺序、校验、发布及下一 gate

独立首判在 2026-10-05 15:40:16 UTC 保存 PASS_SCOPED，SHA256 `77d46cf6f31abe3090185b607561fd26df34621e143539ded8a32338f7946057`；先读三个不可改首轮问题、实际修订、源/反例及scope/identity，再读取候选二fix-response及作者validation自证。此前scope/identity元数据已读，不声称全程盲审。作者后置对照与追加六ID追溯和限定一致，未作为独立receipt；详见 [independent-first-judgment.json](independent-first-judgment.json)、[author-comparison.json](author-comparison.json)、[independent-final-judgment.json](independent-final-judgment.json)。

本人新写Git/text/JSON/hash/文档ID检查最终通过 1411 项，另有 111 项新报告身份/一致性检查通过；语义PASS_SCOPED来自独立文字/调用条件判断，未执行任何505静态设计。原始完整diff-check分别返回2，有80/23条警告，全部是保留的证据patch容器；两段正式/非patch证据检查均通过，不能写成原始整体检查通过。本人扩展依赖核验时初用B09版本读取树外固定原审失败，已改为各记录固定commit；这是本人导航错误，不是候选缺文件或行为问题。详见 [independent-validation.json](independent-validation.json)、[review-document-validation.json](review-document-validation.json)、[command-log.md](command-log.md)。

父任务曾报告executor断开；随后成功git/JSON读取与checkpoint写入核工具可用，继续同一worktree/任务，无重复派发或重新登录。保留当时恢复点 [recovery-checkpoint.json](recovery-checkpoint.json)。本报告仅新增此目录，普通提交/推送 `remediation/20261003-prepare/review-B14-affected-B03-2`，提交后独立回读远端完整report SHA；自身commit身份外部交接，不混作被审候选，不自引用。

参考独立Git在主Git外复用本人原获取记录，HEAD/tree/clean/connectivity已核；仅源文本读取，范围不是分支覆盖。U01–U10/G01–G12/AX01–AX20及具名未读保留：二进制/序列化地图事件、媒体、宿主/可执行程序、杯赛/metrics样本、backup/gen、插件/动态分发/别名/EventScene/dynamic shadow/真实Demo及未列范围未证。参考/游戏/Ruby/编译/转换/生成/反序列化/模拟器/求解器/行为向量执行0，运行观察0，已证Demo链0；canonical229OPEN/0CLOSED。配置gpt-6.1-sol/Ultra/继承Standard，实际UNVERIFIED（已接受PlanA），不降档/加速/派生、无child task或配置/额度探针。详见 [source-reading-log.json](source-reading-log.json)、[execution-request-receipt.json](execution-request-receipt.json)。

本候选PASS_SCOPED完成后停等父任务提供新的实际integration精确SHA；仍需新鲜完整差异和独立affected actual review。没有实际整合输入，不预支actual PASS，full R14及其它受影响owner gate也不由本报告替代，未派发B10或更改公共注册。
