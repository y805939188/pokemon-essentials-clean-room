# GR-013／GR-014／GR-015／GR-016 有界整改回应

2026-10-01；规格提取方。依据 `review/gr010-gr012-review-2026-10-01/recheck-v2/`（GR-011／012 通过报告、next-task-prompt、next-task-inputs.json）及全局 review 的四项完整 finding（含来源、最小输入、原批准范围与静态验收向量；外部原件只读，副本固定于 [input-snapshot/](input-snapshot/)，findings.json 身份 `ee7e9282d51221a5ad66999847a4a0d90f49c4fce3488e1fd8e41e1c1b60f95c`／129,975 与 next-task-inputs 登记一致）。按 GR-013→014→015→016 串行回源核对后修订，四项全部接受，无反证项、无静默跳过。写入前已复测七份编辑对象与 next-task-input-snapshot 逐项一致，六份只读支持稿（WP21/WP49/WP50/WP43/WP55/WP57）身份一致且未改；28 份去重来源身份实测与登记一致；reference 固定 commit、Git 清洁。

修订对象与当前身份（磁盘程序化实测）：

| 包 | 修订前（冻结基线） | 修订后（当前） |
| --- | --- | --- |
| WP41 `specs/combat/wp41-switching-positioning-and-escape.md` | `a5232a1ed18dc24257748c34b2ec83eca9730e2c8ef077c7be638ff3b4d38036`／33,281 | `c456e49407c54a9f5dbae206698dd67af9e60894f2a05705abdfa11f9f2780bb`／35,065 |
| WP42 `specs/combat/wp42-growth-end-of-round-and-battle-outcomes.md` | `126e2612e2776c41557475a98cd97b8ef40a0a7f02fd95f16c434de49855a3eb`／41,759 | `f6e5d683fc18a5d3d7d28b255cc3bd5acafd98dba7fae35fc09b755ce0ab72fe`／44,526 |
| WP58 `specs/combat/wp58-battle-recording-and-playback.md` | `61853e136fc3716f8a3072a60142ee8e797b3c41b8bf6011ddb2d9dbded71a7c`／30,501 | `74a2077b517a10051a3edaf5b178986f0e4510d5f891726b3ed32601f212b995`／32,625 |
| WP47-B `specs/combat/wp47-b-switching-control-and-item-changes.md` | `007699019544203b9b5f4c42f18db8eb91711d2d96f6fa8afdf047d44b16e778`／39,000 | `00409b29ded9dbd29d29e1a9384b9bc365c4da1e55f6b70326e05cc01d10866e`／43,261 |
| WP52-A `specs/combat/wp52-a-generic-numerical-and-status-evaluation.md` | `388b5fce672b8d88cb08e309827154c35e44f68cbe4fd07b62c2f66e3701f26b`／50,104 | `42138911ff6ec27780170f10c630c0e9e4eacae1f59e4f36d6658b6e5022cc67`／52,988 |
| WP52-B `specs/combat/wp52-b-field-damage-healing-and-target-evaluation.md` | `73fa6ffa2096cea14354faca92e63439c9db7698541536212901050f65baf759`／45,342 | `15e28d3975d69eb5735004c38297f2dcee34d6617bbc1bbc20f8258d304c66c5`／47,142 |
| WP19 `specs/pokemon-rules/wp19-attributes-ability-and-stats.md` | `cd3dcf4bf8e7dbea0a45d4abb30540fe2c28406a614590ac1a198a622930055f`／36,492 | `f5611332759af16658dce669552a04764672449e5e6aae73c2af5c61657c6f41`／40,355 |

七份修订后规格状态均为 **Reviewed（原限定范围不变）＋ReviewPending（GR 有界修订，待有界复审）**；提取方不自行关闭 GR 或宣称通过。差异相对冻结基线 7/7 patch 精确重建到当前字节，见 [diff-bindings.json](diff-bindings.json) 与 [revision-diffs/](revision-diffs/)。

## GR-013（WP41＋WP42＋WP58）— 参战标记写入与终局读取口径不同（接受）

- **原问题**：WP41 只写派出时标记已使用于战斗，WP42 只写逐玩家侧个体执行离场回调——缺少写入/读取的实际索引差异；把"使用过"当可靠个体参战事实，结合 WP21 会推得确曾参战的后备 BURMY 在洞穴终战变形。
- **回源**：`011_Battle/001_Battle/001_Battle.rb:151–159`（usedInBattle 按队伍长度初建全假）；`005_Battle_ActionSwitching.rb:274–296`（`pbSendOut` 写入 `@usedInBattle[侧][席位换算]`——**按派出席位定位，不用个体队伍下标**；同一席位两次派入只写同一记录位）；`002_Battle_StartAndEnd.rb:235–240, 500–511`（正常终局 `pbParty(0).each_with_index` **按队伍下标逐个读取**并传给离场处理）；`004_Battle_Peers.rb:53–58`（标志传入形态处理器）；`FormHandlers.rb:189–199`（BURMY：终战且参战真才按环境变形）；`005_RecordedBattle.rb:147–180, 246–256`（回放继承普通派出/终战链）。
- **修订位置**：WP41 §4.1 派出行（写入定位按"侧＋侧内场上位置"）；WP42 §6 共同次序（终局按当前队伍下标读取、两端口径不同）＋§9 E07/E08/E09 三组对照；WP58 §6.2 具名反例收紧（须实际传入标志为真）＋§8 W22b 反例。参考真实缺陷如实登记、不修 reference；WP21 处理器"标志由调用者给出"合同与 WP62 形态登记门不变。
- **静态验收（与 finding 向量一致）**：
  | 输入 | 预期 |
  | --- | --- |
  | 下标 0=PIKACHU、下标 1=BURMY；先派 0 到席位 0，再把 1 换入同一席位 0；正常终局 | 记录 [true,false]；BURMY 读得 false、形态保持 0，不新增形态 1 图鉴记录 |
  | BURMY 为下标 0 且首发席位 0 | 记录位 0 真；终局传真、形态 0→1 并经形态提交登记图鉴 |
  | 直接给离场处理器"参战真、终战真" | 按 WP21 原合同变为洞穴形态 1（处理器规则未改） |
  | 两组队伍次序分别用于正常单打回放（副本形态 0、Cave、实时图鉴未记形态 1） | 下标 0 首发且标志真者终战写形态 1 到实时图鉴；下标 1 换入者保持 0 |
- **边界**：不扩展多席位/接收换队的完整目录；回放结论收紧为具名正例，不扩大为所有回放或所有后备保证。

## GR-014（WP47-B）— 投掷前序自耗后的首次失败与已提交状态（接受）

- **原问题**：§5.3（原第 130 行）以"在到达该后段时还为树果"概括吃果记录并描述正常后置消费，未列前序自耗使当前持物为空时的首次失败——会错误当成可安全略过的正常路径。
- **回源**：`011_MoveEffects_Items.rb:403–470`（FLING：目标主要效果按 U 当前物品分派，尾部 `target.setBelched if user.item.is_berry?` **无空值守卫**）；`007_Battler_UseMove.rb:660–707`（每击顺序：伤害→接触反应（INNARDSOUT）→HP 物品检查（ORAN 自耗）→正式濒死→主要效果）；`008_Battle_AbilityEffects.rb:1853–1868`（INNARDSOUT 允许濒死时反伤同值间接伤害）；`006_Battler_AbilityAndItem.rb:212–242, 272–323`（半血门、pbConsumeItem 的回收/拾取/Belch/移除）；`009_Battle_ItemEffects.rb:364–385`（ORANBERRY HPHeal）；`002_Battle_StartAndEnd.rb:334–346`、`001_PBDebug.rb:4–17`（阶段外层 logonerr 捕获并记录一般异常、不中止不回滚）。
- **修订位置**：§5.3 投掷行补空持物首次失败（含失败前已提交状态不回滚、不回绑最初抛出物、外层诊断边界）；§7 增 I13（完整自耗链）、I14（无自耗）、I15（高于半血门）三组对照；§8 注记与 §9 溯源。WP49 每击次序、WP50 自耗合同、WP42 诊断边界与通用物品 helper 均未改；不给 reference 补守卫。
- **静态验收（与 finding 向量一致）**：
  | 输入 | 预期 |
  | --- | --- |
  | U26/50 STATIC 持 ORAN 用 FLING，T10HP INNARDSOUT，命中致倒下 | U26→16→26；ORAN 已自耗（C/I 清、R/P 记 ORAN、Belch 真）；T 已倒下；主要效果在空持物树果判断首次失败；此前状态保留，后段 Belch 标记与使用结束消费未发生 |
  | 同上但 T 无 INNARDSOUT 且无其它 U 失物/受伤反应 | U 仍持 ORAN 到主要效果，无此失败；按正常后置消费 |
  | T 仍有该特性，U 初始 40/50，损 10 后 30＞25 | ORAN 不触发，无 nil 失败；后段消费按原合同 |
- **边界**：局部失败为 NoMethodError 类；普通阶段外层诊断可捕获该一般异常，不夸大为必然进程崩溃。

## GR-015（WP52-A＋WP52-B）— 旧会心表长度与 AI 局部评分消费者（接受）

- **原问题**：WP52-A（原第 70 行）给旧表写成 16/8/4/3/2/1（截尾分母 1），（原第 72 行）把负下标末项普遍称 1——实际共用旧表只有五档，磨砺评分在旧配置下被误判无用。
- **回源**：`001_Battle_Move.rb:21`（共享表：旧 `[16,8,4,3,2]`、新 `[24,8,2,1]`）；`011_AIMove.rb:500–540`（粗会心级累计、按表长截尾；负值返回）；`004_AI_MoveEffects_MoveAttributes.rb:441–470`（磨砺：分母==1 判无用，否则有非必会心伤害招 +15）；`008_Battle_AbilityEffects.rb:1639–1642`（SUPERLUCK +1）；`009_Battle_ItemEffects.rb:1246–1252`（SCOPELENS +1）；`003_Item_BattleEffects.rb:282–287, 708–712`（DIREHIT3 合法入口置 FocusEnergy=3）。
- **修订位置**：WP52-A §3.1 粗会心级旧表删末项 1、粗伤负下标按新 1／旧 2 分列（两档 ≤2 在粗伤近似中仍视为会心，AI 近似缺陷保留）；§8 增 N02b/N02c/N02d 三组向量。WP52-B §2 磨砺段补同算法的旧/新配置对照（算法不改）；§8 增 B12b。WP43 正确常量、N02 新表结论、粗伤近似与命中 96 等已批准结论不变；不重写 WP51 候选选择或评分算法。
- **静态验收（与 finding 向量一致）**：
  | 输入 | 预期 |
  | --- | --- |
  | 旧配置、累计 1+1+3=5、输入分 100、有合格伤害招 | 截到索引 4、分母 2；局部分 115 |
  | 仅切换新配置 | 截到索引 3、分母 1；局部分 60 |
  | 粗会心返回 −1，旧/新对照 | 取末项 2／1；两者在粗伤 ≤2 判断仍近似会心，非实效必会心保证 |
- **边界**：只修正共享常量与负下标说明；真实会心规则不受 AI 近似影响。

## GR-016（WP19）— 正常设施创建的 255 EV 例外（接受）

- **原问题**：WP19（原第 145/224 行）宣称单项 EV≤252 是写入者保证的不变量，（原第 237 行）又排除正常入口产生超域值——遵守该规格会限制或拒绝 SUNKERN 的两项 255。
- **回源**：`PBS/battle_tower_pokemon.txt:3`（SUNKERN：努力项只有 HP,SA）、`:117`（DROWZEE：HP,ATK,SA 具名三项对照）；`PBS/battle_facility_lists.txt:1–25`（默认列表）；`002_Challenge_Data.rb:113–138, 201–217`（模板解析；创建时 `pkmn.ev[stat] = EV_LIMIT(510) ÷ ev.length` 逐项写入后重算——**无 252 夹限**）；`003_Challenge_ChooseFoes.rb:59–80, 144–164`（对手/Factory 候选直接消费者）；`001_Pokemon.rb:89–93`（EV_LIMIT/EV_STAT_LIMIT 常量）、`1086–1126`（计算入口；DISABLE_IVS_AND_EVS 只影响计算、不改存储）。
- **修订位置**：§4.4 域与上限、存储、写入者目录及 §5 不变量 5 限定为培养/增量写入者的保证＋设施例外；§6 边界"正常入口不产生超域值"同步限定；§9.2 增三组向量；§9.1 溯源与 §11 注记。普通培养/增量上限、存储不钳位与计算公式保持；WP55/57 行为不改为 252；WP19-R03 闭合结论不变。
- **静态验收（与 finding 向量一致）**：
  | 输入 | 预期 |
  | --- | --- |
  | 默认 SUNKERN 双努力项 HP/SA，EV_LIMIT 510 | 两项 255、其余 0、合计 510；不夹 252；⌊255/4⌋=63 与 252 相同 |
  | 具名三项模板 DROWZEE（HP/ATK/SA） | 各 170、合计 510；不是全部模板都超单项上限 |
  | 双项模板＋禁用 IV/EV 计算开 | 存储仍 255/255，计算视为 0；不能借配置规范化存储 |
- **边界**：差异首先是存储状态/总量与后续培养额度；不展开 WP23/73 内部。

## 总体自检结果

- 七份修订 diff 对冻结基线 7/7 patch 精确重建到当前字节；变更仅在各 finding 批准的条款、场景与必要状态/历史注记内。
- 同根因旧表述全文扫描：WP41 无"派出标记即个体参战事实"表述；WP42 无无条件"逐个参与个体"读取口径；WP58 无"使用过即变形"前提；WP47-B 无"安全略过空持物"路径；WP52-A 无 16/8/4/3/2/1 与"负下标末项 1"全称；WP19 无"所有写入者保证 252"全称。
- 既有 R01～R03（各包旧编号）、GR-001～012 CLOSED 结论、第一组三包 31 项通过结论、N01 已通过范围均未改动；六份只读支持稿（WP21/WP49/WP50/WP43/WP55/WP57）未改；WP62 形态登记门未改。
- 矩阵记法：F11-05（WP41／GR-013）、F11-07（WP42／GR-013）、F13-06（WP58／GR-013）、F12-05（WP47-B／GR-014）、F12-08（WP52-A＋WP52-B／GR-015，同一功能行覆盖两包）、F06-04（WP19／GR-016）。**GR-013 跨三包分记三行、GR-015 合一行**——沿用 GR-011 跨包分记已获接受的先例，同一问题不重复计数，具名提交 reviewer 裁定。
- 修订后状态：七包 **Reviewed（原范围）＋ReviewPending（GR 有界修订，待有界复审）**；不自行关闭、不宣称通过。
