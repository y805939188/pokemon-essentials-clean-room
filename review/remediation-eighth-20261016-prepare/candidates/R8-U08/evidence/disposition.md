# R8-U08 修订处置

输入 `4575e80d041ab0c74a42e2e36399d05791dbaa5b`；B8 `fd1df570cad987dc3852a3b958f03916e317f7fe`；只读 R `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`。本记录为作者修订证据，不是正式 review 或接受回执。三个完整候选及原/新字节身份见 [candidate-manifest.json](candidate-manifest.json)。

## GR8-ELR-001

处置：本批唯一 required/P3 已形成候选，待实际非作者复审。沿用 canonical `R6-D-LZ-002`，本项是新增 Slot consumer precision facet；`GR5-M11-004` 及原四组消费者的已关闭资格不变，不另立通用语言资源根。

原证据：完整固定源 `Data/Scripts/017_Minigames/003_Minigame_SlotMachine.rb` 的七角色/八处查找（30、206、209、264、303、327、365、371）；语言文件完整装载/域24哈希/查找/脚本包装见 `Data/Scripts/001_Technical/003_Intl_Messages.rb`。完整 `007_BitmapSprite.rb`、`008_AnimatedBitmap.rb`、`002_RubyUtilities.rb` 区分提示图空译与直接转轮空译，另完整读缓存、文件解析和宿主兼容声明。源只读且未执行。10个合同source/spec及3个补充源文件实读身份和范围见 [reading-ledger.json](reading-ledger.json)。

原规格缺项：WP08 §5.1.1 明示仅覆盖指定调用者，消费者表列控制帮助、战斗菜单、训练家卡、翻牌四组；WP15 §3.2 重复该集合；WP69 主文及22位置附表没有 Slot 图像语言接点。通用哈希查找正确，但不能唯一决定这七个图像请求应先查语言。

修改位置（以下路径均相对于 `mirror/deliverables/final-specification-set/`）：

| 候选 | 章节/锚点 | 最终行为 |
| --- | --- | --- |
| `generic-kernel/wp08-localization.md` | §5.1.1 / `511-指定-ui-图像身份的语言选择` | 消费者表补 Slot 七角色和固定资源，链接 WP69 状态表；保留四组及所有通用查找/工作流字节。 |
| `engine-overworld/wp15-resource-matching-and-audio.md` | §3.2 / `32-与内容身份的衔接` | 同步有限消费者导航，固定资源按各自表划分，避免把翻牌的可译背景误作固定背景。 |
| 同上 | §5.1 / `51-位图访问的分入口失败` | 新增图标空身份清图、直接动画空身份文件名求值早失败两行；不改变普通非空/帧前缀路径。 |
| `user-interface/wp69-slot-machine.md` | 新§2.2 / `22-图像身份与当前语言` | 七角色逐状态查找时点，game→core→A，A/B/C有限对照、固定图、布局/高度前提；不改随机/时间/奖项。 |
| 同上 | 新§6.1 / `61-图像选择加载失败与已完成前缀` | 提示空译清图/转轮空译早失败；普通捕获尝试空白/帧前缀边界，无A重试；准入、BACK、初始化/中奖/财务前缀。 |

区分正误的场景：有效当前语言已成功加载；正常准入、前序构造正常；A/B/C为非空普通非前缀、同高度同布局可加载位图。game域24将转轮图A→B、core缺键且A仍可用时，三个转轮分别请求B。保持A的实现不符合此合同。两层缺键请求A、仅core命中请求C、两层同键取game B；给固定背景映射仍请求原背景。六提示图只在表列状态请求，未到状态不预查。空译及失败/取消前缀另见 [static-vectors.json](static-vectors.json)。所有行为向量为 DERIVED_VECTOR / NOT_EXECUTED，观察点为资源身份交付，非最终像素。

相关完整引用：报告根 `review/global-independent-review/eighth-2026-10-16-fd1df57-c84e/` 下现行 `handoff/contracts.zh.json#/records/27`、`handoff/batches/R8-U08/prompt.md`、`readset.json`、`handoff/batch-assignment.json#/batches/7`；原提案 `evidence/adjudication-inputs/b1ec9b4abad50d2bade2e8694e23a58eea29732aa38b841075831b55ff8cbb7d.json`；完整实际非提出者反证 `evidence/adjudication-inputs/ac3ebbb490bffe1d8c717c26e6adf3a85cfa13aa8544e41602c98df27696c516.json`；`adjudication/root-elr001-counter-reception.v1.json`、`root-elr001-fixed-input-checks.v1.json`；当前 `findings.json#/records/27` 与 `adjudication/root-final-history-and-canonical-reception.v1.json#/canonical_records/27`。早期记录的 pending 只保其生成时点，当前根资格由最终 authority 接合。

原合同来源为 `5caff3bd1a1b062b48b7eda46777a614921946f3` 的 `review/global-independent-review/eighth-2026-10-16-fd1df57-c84e/tasks/handoff_preparation_cloud/handoff/contracts.zh.json#/27`。C35 `2460370f1e410bd49cc29e377b89662838aed2b3` 恢复入口为该报告根下 `evidence/external-recovered/handoff_preparation_cloud/5caff3bd1a1b062b48b7eda46777a614921946f3/handoff/contracts.zh.json#/27`（blob `829d3fed5b738e379c88e66c8a514795b0c92dbb`）。原来源与恢复位置分别保留，不能把原历史结论全改称C35提出。

保留核对：WP08 原四行、空译/参数/作者工作流不变；WP15 原有普通非空与帧前缀边界不变；WP69原全文逐字为新全文有序保留子序列，仅新增两个独立小节。22位置附表、LZ39–41、SL系列均未写；高度H/滑移/随机/有效线/重玩/净币额统计原字节保留。机械依据见 [validation.json](validation.json)，不转为游戏执行信用。

未决依赖：无其它必改的语义前置。候选非作者复审、协调者实际整合、实际整合全文/累计保留的独立复审及 ACCEPTED/CLOSED 分开，均未由作者签署。媒体、实际语言加载、宿主像素/声音/真实保存均未运行；不阻有限静态修订。未来是否采用异常兼容政策仍由对应决策负责，不在本批选择视觉 policy。

去向影响：R8-INTEGRATOR 只将清单中三份mirror映射到正式目标；按本项精确贡献同步必要公共追溯/索引，不由本作者写公共层。打标任务据 [tagging-handoff.md](tagging-handoff.md) 定位，本批未重复全面打标。

## 可选处置

最新用户已覆盖旧提示中“一律未选”的限制。R8-U08没有归属自己的可选项，本批选入0项，也不代其它批作否决。全部10项归属和转交理由逐项列于 [optional-disposition.json](optional-disposition.json)。本批新增有限对照和失败边界均属于 GR8-ELR-001 完整性要求，未借可选授权扩大写集；纯美化未纳入。
