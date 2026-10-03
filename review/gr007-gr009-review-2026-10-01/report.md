# GR-007～009 有界复审（2026-10-01）

**结论：REQUEST_CHANGES。GR-008 CLOSED；GR-007与GR-009仍为OPEN_PARTIAL，暂不进入GR-010～012。** 两项核心反例已修正，剩余是触发前提与语言来源适用范围需要收紧；保留原ID，不新增问题编号。

## 被审对象与范围

| 包 | 完整SHA-256 | 字节 |
| --- | --- | ---: |
| specs/overworld/wp15-resource-matching-and-audio.md | `4270e034868eca42646747286793669accf7d981611d26ddc5c68bf81c4d5fdf` | 23,576 |
| specs/creature-rpg/wp20-hp-status-moves-helditem.md | `9d688fd62df53bdffec6062c9c90d71664640c8ac1acf6ed243166dda245514e` | 37,484 |
| specs/creature-rpg/wp24-player-trainers-partners.md | `19a03575e87ee01b437c0a97bc5013b3652593964f77721f2c50b341bb3427af` | 32,957 |
| specs/creature-rpg/wp18-creature-identity-species-ownership.md | `5207621025bb3198ae129d1fe1f575a761e67498caf403d541621dab4e8458f1` | 37,854 |

四份diff均从与交接身份一致的冻结快照严格重建，4/4字节一致；WP18变更为一条语言指引及相应历史注记。manifest §1 **1,083条**、主TSV v59 **988条**全部与磁盘一致且无重复，阶段最终身份正确。只改变四份规格、矩阵和两份行政清单，WP08、先前GR-001～006及第一组31项通过材料未动。

## GR-007：补齐淡出触发门

**已正确**：仅BGS名称变化的既定正例确实请求BGM淡出800ms，清空playing_bgm，不调用BGS淡出，playing_bgs保持。默认BGM覆盖与观察点已有说明。

**仍需修订**：WP15第123行将名称差异直接写成触发条件；第177行“仅BGM变化”场景未给出目标autoplay_bgm开启。实际比较前还各有门：BGM分支需要已有BGM播放记录且目标autoplay_bgm=true；BGS分支需要已有BGS播放记录且目标autoplay_bgs=true。

反例（系统对象存在、非暂停、无默认覆盖，白天或无夜间变体，观察在autofade返回且autoplay之前）：

- 正在播放A／Rain，目标B／Rain，但目标autoplay_bgm=false：没有淡出，BGM仍A、BGS仍Rain。当前第177行所列条件不能排除该输入，却要求一次淡出。
- 正在播放A／Rain，目标A／Wind，但目标autoplay_bgs=false：同样没有淡出。BGS名称差异本身不足以触发。

请在规则和正例中补完整前提，并补关闭目标开关的对照。比较的是当前播放登记与目标地图解析后的曲名；BGS分支虽然淡出BGM，但不额外要求BGM分支也成立。来源：`003_Game processing/002_Scene_Map.rb:56–69`，音频包装与系统状态写入见[source-checks.json](source-checks.json)。

## GR-008：CLOSED

WP20§5.2和不变量7已准确限定：整表记录先清空后按序复制，保留重复；逐项添加只阻止再次追加同标识，不修复既有重复。两个合法招式对象经标识赋值形成两TACKLE槽、保持PP钳制的前提成立，三组对照与来源一致。该修订可关闭，WP20无需继续改动。

## GR-009：收窄WP18新增的来源概括

**已正确**：WP24的训练家构造读取宿主语言映射，和UI选择索引分开；从训练家构造Owner时复制字段值；单纯UI切换不回改已有字段。四组原反例均成立。

**仍需修订**：WP18第203行新增“language来源为宿主语言映射”未限定构造路径；第360行同步注记也沿用该概括。Owner自身并非一律读取宿主。正常无插件、其余参数有效时：

- 宿主ja-JP，外来Owner构造省略language：得到**2**，不是宿主映射的1。
- 显式构造Owner传入language=3：得到**3**。
- 训练家字段从默认1显式改成7后再复制Owner：得到**7**，不会重新读取宿主。

来源：`014_Pokemon/005_Pokemon_Owner.rb:19–41,62–66`；`015_Trainers and player/001_Trainer.rb:4–9,169–175`。请把指引改为“训练家默认初始化来源见WP24；Owner取值由构造入参或训练家现有字段提供，外来构造默认2”，保留已有正确外来默认值和UI独立性。主规则已正确，不需要重写WP24的宿主映射或WP08的UI行为。

## 矩阵裁定与下一步

**接受F07-03作为GR-009本次主登记行**：修订归WP24-A身份／语言来源，F07-03已有该身份范围登记，NPC装载与伙伴流程未改。WP18属于直接引用同步，不要求重复开GR编号；这不构成“一GR永远只能登记一行”的通用限制。

仅按[有限补修提示](next-task-prompt.md)处理上述两项边界，保持GR-008、GR-001～006和第一组31项通过结论，完成后再送定点复审。GR-010～016与WP65等新包不启动。

本次只新增审查目录，未修改被审文件或外部review原件。来源按固定commit静态核对，未执行参考代码、播放音频、读取真实主机语言或操作UI／存档；未创建任务／Agent、未发跨会话消息、未提交／推送。

[逐项结论与反例](findings.json) · [登记与差异核验](registration-checks.json) · [矩阵差异](feature-matrix.diff) · [最终检查](final-checks.json)
