# GR-007／GR-008／GR-009 有界整改回应

2026-10-01；规格提取方。依据 `review/gr004-gr006-review-2026-10-01/`（GR-004～006 通过报告、next-task-prompt、next-task-inputs.json）及全局 review 的三项完整 finding（含来源、最小输入、原批准范围与静态验收向量；外部原件只读，副本固定于 [input-snapshot/](input-snapshot/)，findings.json 身份 `ee7e9282d51221a5ad66999847a4a0d90f49c4fce3488e1fd8e41e1c1b60f95c`／129,975 与 next-task-inputs 登记一致）。三项全部接受并回源核对后修订，无反证项、无静默跳过。写入前已复测目标身份与 next-task-inputs 的 current_targets 及指定冻结快照（`review/wp58-wp62-wp38-review-2026-09-30/closure-review/input-snapshot/`）一致，无漂移；11 份来源与 2 份只读/最小传播依赖（WP18、WP08）身份实测亦与登记一致。

修订对象与当前身份（磁盘程序化实测）：

| 包 | 修订前（冻结基线） | 修订后（当前） |
| --- | --- | --- |
| WP15 `specs/overworld/wp15-resource-matching-and-audio.md` | `cb184c3d58a51fa86bc4bc89b5708dc61fa77ad33578709804846494fa7c6143`／21,219 | `4270e034868eca42646747286793669accf7d981611d26ddc5c68bf81c4d5fdf`／23,576 |
| WP20 `specs/creature-rpg/wp20-hp-status-moves-helditem.md` | `05a59789554a4824121a852f05bf643f799b6e52af6837eb966c19cbec678d3c`／35,076 | `9d688fd62df53bdffec6062c9c90d71664640c8ac1acf6ed243166dda245514e`／37,484 |
| WP24 `specs/creature-rpg/wp24-player-trainers-partners.md` | `325940946f7b120c4e484695dd35c5804c2baf9411798d95c22af2f944a2e7e5`／29,668 | `19a03575e87ee01b437c0a97bc5013b3652593964f77721f2c50b341bb3427af`／32,957 |
| WP18（GR-009 交界最小同步） `specs/creature-rpg/wp18-creature-identity-species-ownership.md` | `55fb5004ecf99272f2f88332d20bb076cce6ca5075f6ed546eb24e83df579791`／37,448 | `5207621025bb3198ae129d1fe1f575a761e67498caf403d541621dab4e8458f1`／37,854 |

三份目标规格状态均为 **Reviewed（原限定范围不变）＋ReviewPending（GR 有界修订，待有界复审）**；WP18 仅一行指引同步（无行为规则变化、不加 GR 状态记法）；提取方不自行关闭 GR 或宣称通过。差异相对冻结快照 4/4 patch 精确重建到当前字节，见 [diff-bindings.json](diff-bindings.json) 与 [revision-diffs/](revision-diffs/)。

## GR-007（WP15）— 地图 BGS 名称变化触发的是 BGM 淡出（接受）

- **原问题**：§6.3 传送淡出（原第 123 行）称"BGS 不同名同样淡出"，把背景音效差异自动等同于淡出背景音效；推得对 BGS 进行 0.8 秒淡出。
- **回源**：`003_Game processing/002_Scene_Map.rb:56–75`（autofade：BGM 名称含夜间变体比较分支与 **BGS 名称比较分支调用的都是 `pbBGMFade(0.8)`**）；`008_Audio/002_Audio_Play.rb:70–89`（`pbBGMFade`→`pbBGMStop`→`$game_system.bgm_fade` 包装链）；`004_Game classes/002_Game_System.rb:113–123`（`bgm_fade`：清 playing_bgm、非暂停时重置位置、无 defaultBGM 时向宿主请求 BGM 淡出 800 毫秒）、`207–228`（`bgs_fade` 为另一独立入口，本分支不调用；playing_bgs 保持）。
- **修订位置**：§6.3 传送淡出行（BGS 差异分支实际请求 BGM 淡出，作为参考快照行为如实登记）；§9.2 传送淡出场景拆为仅 BGM 变／仅 BGS 变／均不变三组对照，前提固定无 defaultBGM 覆盖、非暂停，观察点限定在 autofade 返回、后续地图 autoplay 之前；头部状态、§10 溯源与 §12 历史注记。6.2 通用淡出机制与 WP11 时机引用不变。
- **静态验收（与 finding 向量一致）**：
  | BGM 同名 | BGS 同名 | 预期 |
  | --- | --- | --- |
  | 是 | 否（目标 autoplay_bgs=true） | 一次 BGM 淡出请求；playing_bgm 清空，playing_bgs 保持 |
  | 否 | 是（目标 autoplay_bgm=true） | BGM 差异分支请求 BGM 淡出 |
  | 是 | 是 | 两个差异分支均不请求淡出 |
- **边界**：仅凭控制流与状态写入确认，无需实际音频资源或播放测试；800 毫秒为固定常数换算；参考缺陷保留（不改成 BGS 淡出）。

## GR-008（WP20）— 最初招式记录的不重复保证被扩大到整表记录入口（接受）

- **原问题**：§7 不变量 7（原第 205 行）称"重复项不入记录"，与 §5.2（原第 135 行）"当前全部招标识依序复制"矛盾——把 add_first_move 的去重守卫推广到了 record_first_moves 整表记录。
- **回源**：`014_Pokemon/001_Pokemon.rb:29–32`（moves/first_moves 字段语义）、`681–704`（`record_first_moves`：先清空再**无守卫**逐项 push 当前标识；`add_first_move`：仅当记录未含该标识才追加——只阻止追加、不消除已有重复）；`014_Pokemon/004_Pokemon_Move.rb:24–27`（招标识赋值入口：`id=` 经 GameData::Move.get 解析并**按新总 PP 钳制当前 PP**——可合法形成两个 TACKLE 槽）；`PBS/moves.txt:5326, 5961`（TACKLE/GROWL 具名存在）。
- **修订位置**：§7 不变量 7（"不重复"限定到逐项添加入口；整表记录保留当时列表的重复与顺序）；§5.2 两入口分列（整表入口不做去重；逐项添加不追加同标识但不修复已有重复；删除按标识删全部同标识项）；§11.2 增三组对照；头部状态、§12 溯源与 §14 历史注记。原正确 PP 钳制规则与 R01～R03 结论不变，不引入理想化去重。
- **静态验收（与 finding 向量一致）**：
  | 操作 | 输入 | 预期 |
  | --- | --- | --- |
  | 整表记录 | 当前 [TACKLE, TACKLE]（经 id= 入口形成） | [TACKLE, TACKLE] |
  | 逐项添加 TACKLE | 记录 [TACKLE] | [TACKLE]（不追加） |
  | 逐项添加 TACKLE | 记录 [TACKLE, TACKLE] | [TACKLE, TACKLE]（不追加，也不修复原有重复） |
- **边界**：不需无效对象或超过槽位上限；WP26/35/38 复制/记录首招、WP30 重学候选去重是各自另一步，不受影响。

## GR-009（WP24）— 训练家/拥有者语言来源被混同于游戏界面语言选择（接受）

- **原问题**：§3.1（原第 48 行）把语言来源写成"当前语言设置，WP08"，（原第 52 行）未区分宿主地区语言与 UI 选择——把训练家语言关联到界面选择，缺少宿主语言映射的来源规则。
- **回源**：`019_Utilities/001_Utilities.rb:49–61`（`pbGetLanguage`：读宿主 `System.user_language[0..1]`——ja→1、en→2、fr→3、it→4、de→5、es→7、ko→8、其余→2；**不读取 LANGUAGES 或 `$PokemonSystem.language`**）；`015_Trainers and player/001_Trainer.rb:169–175`（构造时 `@language = pbGetLanguage`）；`014_Pokemon/005_Pokemon_Owner.rb:30–42`（`Owner.new_from_trainer` 复制训练家 language；`new_foreign` 默认 2）；`003_Game processing/001_StartGame.rb:21–34` 与 `016_UI/013_UI_Load.rb:334–343`（UI 语言选择只写 `$PokemonSystem.language`、消息文件与存档 Hash，**不触碰已有训练家/Owner 字段**）。
- **修订位置**：§3.1 字段行与语言专条（宿主映射、与 WP08 界面语言选择索引是两种独立身份与读取时刻、UI 切换不回改）；§3.4 Owner 复制同源值；§10 依赖表引用修正；§11.2 增四组场景；头部状态、§12 溯源与 §14 历史注记。**WP18 最小同步**（§6.1 `language` 指引一行："见 WP08"更正为指向 WP24 §3.1 来源说明——确有同根因引用错误需直接同步，按提示仅一行最小调整）；WP08 已正确 UI 行为、经验/繁殖公式未动。
- **静态验收（与 finding 向量一致）**：
  | 宿主 | 界面 | 预期 |
  | --- | --- | --- |
  | ja-JP | English（索引 0） | 训练家 language=1；Owner 复制 1 |
  | en-US | French | 训练家 language=2 |
  | zh-CN | 任意 | 训练家 language=2（未映射回退） |
  | 仅切换 UI 语言 | — | 已构造训练家与 Owner 的 language 保持原值；新消息文件按 UI 索引选择 |
- **边界**：未读取真实主机语言、未操作 UI 或存档；WP30 经验/WP34 遗传比较持久 language 的既有结论正确、未动；WP30/WP34 尚未全文审，不据此给它们重复编号。

## 总体自检结果

- 四份修订 diff 对冻结快照 4/4 patch 精确重建到当前字节；变更仅在各 finding 批准的条款、场景与必要状态/历史注记内（WP15 §6.3 一行＋§9.2 三行；WP20 §5.2 两条、§7 一条、§11.2 三行；WP24 §3.1 两条、§3.4 一条、§10 一行、§11.2 四行；WP18 §6.1 一行指引＋§14 同步注记；各包头部状态、§12/§10、§14/§12）。
- 同根因旧表述全文扫描：WP15 无残留"BGS 不同名同样淡出"；WP20 无残留"重复项不入记录"（§14 注记为引用旧句说明更正，非当前规则）；WP24 无残留"来源为当前语言设置"。
- 既有 R01～R03（各包旧编号）、GR-001～006 CLOSED 结论、第一组三包 31 项通过结论、N01 已通过范围均未改动；GR-010～016 与 WP12 的 GR-011 未动。
- 矩阵记法：F05-02（WP15）、F06-06（WP20）、F07-03（WP24）各加 ReviewPending GR 修订记法。GR-009 归 F07-03 的口径：修订条款位于 WP24-A（身份、外观与标识：§3.1 训练家基础字段、§3.4 与 WP18 拥有者关系），其矩阵归属为 F07-03（玩家外观/身份）；F07-02 覆盖 NPC 训练家数据装载/伙伴（WP24-C/D），本批未改——按一 GR 一行先例不重复加注，具名提交 reviewer 裁定。
- 修订后状态：三包 **Reviewed（原范围）＋ReviewPending（GR 有界修订，待有界复审）**；WP18 保持 Reviewed（仅一行指引同步）；不自行关闭、不宣称通过。
