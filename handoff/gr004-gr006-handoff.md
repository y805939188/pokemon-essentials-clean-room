# 交接：下一批 GR 有界整改（GR-004／GR-005／GR-006）

你是 Pokémon Essentials 行为规格提取项目的**主线规格提取模型**（不是独立 reviewer）。本提示交给你的是一个有界整改任务：**GR-004（WP12）、GR-005（WP13）、GR-006（WP14）三项已知全局问题的有界修订**，修完登记后停止送有界复审。读完本提示与指定材料、完成固定预检后直接开工。

## 1. 项目背景速览

- 主工作区：`/Users/dingshinn/Desktop/pokemon-framework-reference/`。
- 项目把 Pokémon Essentials 当作**只读行为参考**，提取可观察行为、规则、状态转移、数学、输入输出、失败／取消与用户流程，供后续独立 clean-room 实现。**当前不是实现阶段**：不写框架代码、不逐行翻译 Ruby、不复制源码结构、不设计 TypeScript API；正文按行为组织，源路径／行号只用于审计（traceability）。
- `reference/pokemon-essentials/` 严格只读，固定 commit `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`。不切换基线、不联网换版本、不改 reference、不运行游戏／参考表达式／事件解释器／生成器／编译转换器／翻译器／真实网络，不操作真实地图／存档／输入。
- 先读根目录 `AGENTS.md`（工作区根），它规定了严格的源码分离、clean-room 输出、架构中立与分类规则，全部适用。
- 计划共 87 个可执行包。执行策略见 `planning/extraction-plan.md` §2.2（用户澄清版）：**某次 review 发现的问题必须先修订并复审通过，再推进下一包／批**；全部内容包处理完后再做整体 double review，最后 WP80 净化交付。

## 2. 当前进度（已完成，不要重做）

- 主线 62 包＋独立 B 批 3 包（WP68/69/70，位于 `/Users/dingshinn/Desktop/pokemon-spec-parallel-minigames/`，只读引用，不整合）有通过记录；全局复核另有 16 项 P2 待修（GR-001～016），本批处理前三项之后的第 4～6 项。
- WP23-N01（净化室选择可达性）已闭环通过（recheck-v3 PASS_SCOPED），管理性回填留待集中收尾。
- 第一组三包（WP66-A 队伍摘要、WP63 Pokégear/地图/电话、WP64 邮件/神秘礼物）：提取→两次进度复审 29 项 findings→v2 修订→v2 复审 19 关/10 残留→v3 补修→v3 复审通过→GROUP1-C02 元数据收尾→**31 项全部 CLOSED，限定通过**。三包当前为 ReviewPending（修订 v3），管理性回填另记。
- **GR-001（WP04 分词包围标记末字段位置条件）／GR-002（WP08 导入形态首条数字判别）／GR-003（WP10 寄养迁移场景跳过对象）已全部 CLOSED**（GR-001 经一次字面样例 U+0060→U+0022 补修后定点复审 PASS_SCOPED）。

## 3. 当前登记状态（以磁盘实测为准复核，不要照抄本提示哈希）

- manifest `planning/review-manifest-2026-09-19.md`：**第八十二轮**，§1 共 **1,070 条**带完整身份条目（另 2 条无哈希「见原件」行）；最终身份 `18c1ba841cc8a41b2d8eea76870ee2fda03fe17f60d9c0853f25ca510f4b624f`／645,944。
- 主 TSV `review/wp18-wp20-delivery-2026-09-26/current-hashes.tsv`：**v57**，**975 条**；最终身份 `bfa1dd6f630a4e8ed8df5211d8d8f11e49ffe8a021be9da5801cb63d42fabc64`／135,897。
- 矩阵 `planning/feature-matrix.md`：`1103abf69ae6626a91dcccda502c458fd76b3028f8a1ac22211e6352f15dc004`／60,341。
- reference HEAD 必须为 `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b` 且 `git status --porcelain` 为空。
- **主 TSV 覆盖惯例**：只登记 WP17 及以后批次的规格与交付材料；WP04／08／10／12／13／14 等早期规格身份只登记 manifest §1，不为它们向主 TSV 加行。

## 4. 工作纪律（全部硬性）

- **完整哈希与字节一律从磁盘程序化测量**；绝不凭前缀或记忆补写后缀（本项目 CLOSURE-R01 教训）。发现与旧记录冲突时先查是否既有编号，不重复报新问题、不默改旧规格、不宣称任何既有编号关闭。
- 状态词汇：Drafted（提取与自检完成）／ReviewPending（已送审待结论／已修订待复审）／Reviewed（限定范围经独立 review 通过）／Partial／Blocked。**提取方不自行 Reviewed、不自行关闭任何问题、不宣称通过**。
- reviewer 原件、全部 input-snapshot 快照、旧交付材料、旧 revision 目录一律只读留史，不回写。
- 每轮交付：上游主稿先定稿 → 测量下游引用（摘要/fixed/绑定）→ 最后登记（manifest §1 就地更新变更行＋追加新材料行、§2.2 轮次叙述、§3 历史行、§4 轮次摘要；主 TSV 头部与行）。**最终登记检查独立保存（registration-final-checks.json），不登记进其描述的 manifest／TSV**，避免自引用循环。
- 差异（diff）相对指定冻结快照生成，必须 patch 精确重建到当前字节才算成立。
- 不创建任务／Agent、不向其它会话发消息、不提交／推送。只做静态规格与自有文本／哈希／JSON／差异／字面集合／固定算术。

## 5. 本批任务：GR-004／GR-005／GR-006

权威材料（先读）：

1. 根 `AGENTS.md`、`planning/extraction-plan.md` §2.2。
2. 通过报告与执行提示：`review/gr001-gr003-review-2026-10-01/recheck-v2/report.md`、`recheck-v2/next-task-prompt.md`、**`recheck-v2/next-task-inputs.json`**（含三个目标当前身份、8 份来源身份、三项完整 finding）。
3. 全局 review：`/Users/dingshinn/Desktop/pokemon-completed-scope-review/report.md` 与 `findings.json` 的 GR-004～006（外部只读；如需使用请先复制进工作区再读副本）。
4. 三个目标规格的当前稿（见下表）与 next-task-inputs 列出的来源文件。

三个目标（写入前从磁盘复测身份，与 next-task-inputs 的 current_targets 一致才动手；出现漂移先记录差异、保留他人工作）：

| 目标 | 当前身份（预检以磁盘实测核对） |
| --- | --- |
| `specs/overworld/wp12-terrain-movement-vehicles.md` | `8187e7deb59950301a12a6518a3c81a1e2a3aebabc347f7fa388e02364e8b280`／32,153 |
| `specs/overworld/wp13-map-events-npc-followers.md` | `0b9bbd02e9b6032690967549f62d0f5024c0a8bf6ad541e0f7b94b7a09d242d8`／28,571 |
| `specs/overworld/wp14-random-dungeons.md` | `cb4edd9caac4109baa392b1792c4a52f6c00afb210e63afbf7aa019276ee96f7`／24,017 |

逐项范围（按 next-task-prompt 与 finding 执行，不扩不缩）：

1. **GR-004／WP12**：在 `wp12-terrain-movement-vehicles.md` 补**非玩家角色被玩家阻挡时的「玩家非 through」前提**，并区分**移动角色自身 through** 与玩家 through。按 finding 固定其余位置、通行和碰撞条件，补仅改变玩家 through 真假的一对静态场景。保留既有地图边界、双向图块和事件碰撞规则。来源含 `004_Game classes/006_Game_Character.rb`、`004_Game_Map.rb`（身份见 next-task-inputs）。
2. **GR-005／WP13**：在 `wp13-map-events-npc-followers.md` 补**上一次成功更新状态的优先许可**及其与清除／重设顺序的关系：同一实例持续获得调用时，成功更新后会继续放行，不再落到屏幕范围门；须区分地图层菜单暂停调用、从未获准的屏外实例，以及重建／外部改写边界。补**已更新后屏外、尚无许可屏外、菜单阻止调用**三组对照，保留自动／并行等例外。来源含 `004_Game classes/007_Game_Event.rb`、`005_Sprites/003_Sprite_Character.rb`、`012_Overworld/004_Overworld_FieldMoves.rb`（身份见 next-task-inputs）。
3. **GR-006／WP14**：在 `wp14-random-dungeons.md` 区分**奇数尺寸调整意图**与**标准参数对象下的实际失败**：奇数单元宽／高、奇数通道的写回入口缺失，首次写回即报错；不得写成自动调整后正常生成。补**奇数宽、奇数高、奇数通道、全偶数**四组对照，说明失败发生在**待播种子消费／播种和地图重写之前**。不得执行参考生成器补证，也不修改 reference 使它「正常」。来源含 `010_Data/002_PBS data/020_DungeonParameters.rb`（身份见 next-task-inputs）。

通用要求：每项按原 ID 回源核对定义、调用者与必要配置；不逐行翻译源码；规格只写行为、状态、前提、失败与测试输入输出。反证须具名提交 reviewer 裁定，不能静默跳过。**不要用新增正确段落掩盖同根因旧矛盾句**——正文、场景和当前活动材料要一致（全文核对同根旧表述已删除或限定）。

## 6. 交付与登记

1. 新建 `review/gr004-gr006-revision-2026-10-01/`：固定输入与实测、实际来源读段、三项逐 ID 回应（原问题／修订位置／来源／场景预期／自检）、相对指定快照的精确 diff（patch 重建验证）、静态正常／边界场景、自检 checks.json、当前完整身份与必要交界同步清单、不登记的 registration-final-checks.json。
2. 规格头尾加 GR 修订记法（Reviewed 原范围＋ReviewPending GR 修订待复审；被审身份留史写法沿用既有格式）；矩阵 F04-03（WP12）、F04-05（WP13）、F04-04（WP14，如行内归属如此，以矩阵实际行为准）加 ReviewPending GR 修订记法（参考上一批 F02-02／F02-05／F03-02 的写法）。
3. 登记新一轮（manifest 第八十三轮／主 TSV v58）：三份规格行就地更新（注意：这三个规格早于主 TSV 覆盖起点，身份只登记 manifest §1）、矩阵行就地更新、revision 材料追加；§2.2／§3／§4 续写；完整哈希与字节从磁盘生成，历史身份留史，当前引用与历史角色分开。
4. 全量复测：TSV 全部行与 manifest §1 全部带哈希行对磁盘 0 偏差、无重复路径；reference HEAD 与清洁复核。

## 7. 停止点与后续（本批不做）

- **三项完成后停止并送有界复审**；不自行关闭 GR、不宣称通过。复审通过后再按安排处理 GR-007～016。
- WP12 另有 GR-011（转向遭遇标记）、WP41/42/58 另有 GR-013（参战标记索引），**本批不宣称 WP12 全部问题已解决**，也不提前执行 GR-011／GR-013。
- 不启动 WP65／WP67-A／WP67-B 等新包提取；N01 已通过范围不重开；第一组 31 项通过结论与三包 v3 正文不动；N01 与第一组的管理性回填、B 批整合留待集中收尾；WP63-64-O01（载入画面礼物接收对载入缓存玩家的修改）留给 WP65 时代处理。
- 后续大阶段（本批之后的总路线）：GR-007～016 全部整改完毕→整体 double review（额外遗漏）→统一修订／补漏／复核→WP80 净化交付。
