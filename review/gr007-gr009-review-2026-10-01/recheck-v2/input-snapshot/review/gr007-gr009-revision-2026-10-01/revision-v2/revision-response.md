# GR-007／GR-009 剩余边界补修（revision v2）

2026-10-01；规格提取方。依据有界复审 [report.md](../../gr007-gr009-review-2026-10-01/report.md) 与 [next-task-prompt.md](../../gr007-gr009-review-2026-10-01/next-task-prompt.md)：**GR-008 已 CLOSED（WP20 当前字节 `9d688fd6`／37,484 保持不变）；GR-007 淡出目标与 GR-009 训练家默认宿主映射的核心修订已正确，仅各剩一项边界收紧**。本目录只处理这两项；v1 回应／checks／diff 留史于 `../` 根目录，不改写。写入前已复测：三包与 WP20 当前字节同复审 input-snapshot 逐项一致（WP15 `4270e034`／23,576、WP18 `52076210`／37,854、WP24 `19a03575`／32,957、WP20 `9d688fd6`／37,484）；Owner/Trainer 来源段（`005_Pokemon_Owner.rb:19–41,62–66`、`001_Trainer.rb:4–9,169–175`）与 `002_Scene_Map.rb:56–69` 已按补修范围重核；reference 固定 commit、Git 清洁。

修订对象与当前身份（磁盘程序化实测）：

| 包 | v1 被审（复审快照冻结） | v2 当前 |
| --- | --- | --- |
| WP15 `specs/overworld/wp15-resource-matching-and-audio.md` | `4270e034868eca42646747286793669accf7d981611d26ddc5c68bf81c4d5fdf`／23,576 | `de45aaf9e80032d5d2b00d829aeb0e0b679e70b4beb6ab1c89d934846601d7a9`／25,152 |
| WP18 `specs/creature-rpg/wp18-creature-identity-species-ownership.md` | `5207621025bb3198ae129d1fe1f575a761e67498caf403d541621dab4e8458f1`／37,854 | `8ddf97ff2d0a3bc22ddb7c25bf2423778425e4f697df94c4101442fd365dfdde`／39,278 |
| WP24 `specs/creature-rpg/wp24-player-trainers-partners.md` | `19a03575e87ee01b437c0a97bc5013b3652593964f77721f2c50b341bb3427af`／32,957 | `3298577e6067554be22e7ece0bd0b39506d615cdc02a1677d8ffb9825f59945f`／33,326 |

差异相对复审 input-snapshot 3/3 patch 精确重建到当前字节，见 [diff-bindings.json](diff-bindings.json) 与 [revision-diffs/](revision-diffs/)。

## GR-007（WP15）— 补齐淡出触发门（接受）

- **剩余问题**：v1 §6.3 把名称差异直接写成触发条件；§9.2"仅 BGM 变"正例未给出播放登记与目标 autoplay_bgm=true 前提。复审反例：目标 autoplay_bgm=false（或 autoplay_bgs=false）时名称不同也不淡出。
- **回源**：`002_Scene_Map.rb:56–69`——两通道均无播放登记则整体返回；BGM 分支门：`playingBGM` 存在 且 `map.autoplay_bgm` 且登记名 ≠ 目标解析名（含夜间变体）；BGS 分支门：`playingBGS` 存在 且 `map.autoplay_bgs` 且 BGS 名不同 → 仍调 `pbBGMFade(0.8)`（BGM 淡出），不额外要求 BGM 分支成立。
- **补修位置**：§6.3 两条分支补齐三门（相应通道已有播放登记、目标对应 autoplay 开关开启、名称不同），明确"仅名称不同不足以触发"与"BGS 分支不额外要求 BGM 分支成立"；§9.2"仅 BGM 变"正例补齐前提，新增目标 BGM 开关关闭、目标 BGS 开关关闭两组对照；§12 注记续写 v2。v1 已正确的 BGS→BGM 淡出更正、均不变对照与观察点限定未改。
- **静态验收（与复审反例一致）**：
  | 情形 | 预期 |
  | --- | --- |
  | A／Rain 播放中，目标 B／Rain 且 autoplay_bgm=true | 一次 BGM 淡出；playing_bgm 清空、playing_bgs 保持 |
  | A／Rain 播放中，目标 B／Rain 但 autoplay_bgm=false | 不请求淡出；playing_bgm 仍 A、playing_bgs 仍 Rain |
  | A／Rain 播放中，目标 A／Wind 但 autoplay_bgs=false | 不请求淡出；两通道登记均保持 |
  | A／Rain 播放中，目标 A／Wind 且 autoplay_bgs=true | BGS 分支请求 BGM 淡出（v1 已确认，保持） |
  | 两通道均无播放登记 | 预淡出整体直接返回 |
- **边界**：仍不播放真实音频、不执行参考方法；defaultBGM 覆盖与非暂停语义沿用 6.2/§6.3 已述前提。

## GR-009（WP18＋WP24 限定）— Owner 语言来源按构造路径分列（接受）

- **剩余问题**：v1 WP18 §6.1 新增指引把 `language` 来源概括为"宿主语言映射"未限定构造路径；§14 注记沿用同一概括。复审反例：宿主 ja-JP 下外来构造省略 language 得 2（非 1）；显式构造传 3 得 3；训练家字段改 7 后复制得 7（不重读宿主）。
- **回源**：`005_Pokemon_Owner.rb:19–41`（`initialize` 采用传入整数；`new_from_trainer` 复制训练家现有字段；`new_foreign(name="", gender=2, language=2)` 省略默认 2）、`62–66`（`language=` setter 采用显式整数）；`001_Trainer.rb:4–9`（`language` 为 attr_accessor 可写字段）、`169–175`（构造时 `pbGetLanguage` 仅为训练家默认初始化来源）。
- **补修位置**：WP18 §6.1 指引改为按构造路径分列（直接构造采用入参；`new_from_trainer` 复制训练家**现有**字段值；`new_foreign` 省略默认 2；setter 采用显式值；训练家默认初始化来源才是宿主映射，见 WP24 §3.1），保留与 WP08 界面选择索引分开、不随 UI 切换回改的正确结论；§11.2 增三组对照；§14 注记改写并标明 v1 被审身份留史。WP24 §3.4 同义概括限定为"复制训练家**现有**字段值（默认初始化为宿主映射；改写后复制改写值）"；§14 续写 v2——**WP24 已正确的宿主映射规则与 §11.2 四组场景一律未改**。
- **静态验收（与复审反例一致）**：
  | 构造路径 | 预期 |
  | --- | --- |
  | 宿主 ja-JP，`new_foreign` 省略 language | 2（参数默认，非宿主映射 1） |
  | 宿主 ja-JP，显式构造传 language=3 | 3（采用入参） |
  | 宿主 ja-JP，训练家字段 1→7 后 `new_from_trainer` | 7（复制现有字段值，不重读宿主） |
  | 训练家默认构造（v1 已确认，保持） | 宿主映射（ja→1 等）；UI 切换不回改 |
- **边界**：WP08 已正确 UI 行为、经验/繁殖公式未动；F07-03 矩阵归属已经本次复审裁定接受，不挪行；未读取真实主机语言。

## 总体自检结果

- 三份 v2 diff 对复审 input-snapshot 3/3 patch 精确重建；变更仅在补修提示批准的位置（WP15 §6.3 一段、§9.2 三行改/两行增、§12 注记；WP18 §6.1 一条、§11.2 三行、§14 注记；WP24 §3.4 一句、§14 注记）。
- 残留扫描：WP15 无"名称不同即淡出"无门表述；WP18 无当前结论层面的"来源为宿主语言映射"概括（§14 注记为已限定历史记录，标明 v1 身份与收窄原因）；WP24 无"复制即宿主编号"概括。
- WP20（GR-008 CLOSED）字节未动；GR-001～006、第一组 31 项、N01 已通过范围未动；GR-010～016 与 WP12 的 GR-011 未动。
- 修订后状态：WP15／WP24 保持 **Reviewed（原范围）＋ReviewPending（GR 有界修订 v2，待定点复审）**；WP18 保持 Reviewed（交界同步 v2）；不自行关闭、不宣称通过。
