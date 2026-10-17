# 给打标任务的有限变更清单

本清单只交接 R8-U08 的新增/受影响位置，不重复全面打标。候选路径均为本批 `mirror/` 下正式相对路径；最终接收前先以 `candidate-manifest.json` 核字节。

| 正式相对路径（均在 deliverables/final-specification-set/） | 章节/锚点 | 变更行为与证据等级 |
| --- | --- | --- |
| `generic-kernel/wp08-localization.md` | §5.1.1 / `511-指定-ui-图像身份的语言选择`，Slot Machine新表行 | SOURCE_STATIC：七角色接入当前语言查找；固定背景/遮罩/按钮/线/灯/数字；引用WP69§2.2。原四行不变。 |
| `engine-overworld/wp15-resource-matching-and-audio.md` | §3.2 / `32-与内容身份的衔接`，指定UI段 | SOURCE_STATIC：有限消费者增加Slot；固定资源按WP08各行划分，保翻牌可译背景。 |
| 同上 | §5.1 / `51-位图访问的分入口失败`，两个新表行 | SOURCE_STATIC／DERIVED_VECTOR：图标空串清图；直接动画空串文件名求值失败，早于普通加载捕获。未执行。 |
| `user-interface/wp69-slot-machine.md` | 新§2.2 / `22-图像身份与当前语言`，首段及七行表 | SOURCE_STATIC：状态到达才查七角色、三轮分别查，game→core→A；查找不新增选语言/写存档。 |
| 同上 | 新§2.2后两段 | SOURCE_STATIC：固定资源、布局和H；DERIVED_VECTOR：缺译A、game B、core C、优先级/背景对照，全部NOT_EXECUTED。 |
| 同上 | 新§6.1 / `61-图像选择加载失败与已完成前缀`，三段 | SOURCE_STATIC／DERIVED_VECTOR：空译分入口、普通非空捕获/帧前缀边界、不重试A；准入/BACK及初始化、中奖、财务已达前缀。全部未运行。 |

现有WP69§2/§2.1、§3–§5全文、22位置附表、LZ39–41、SL系列均未改；不能因候选新增文字把原静态向量改标执行通过。宿主/像素/媒体/声音/真实语言加载/存档回放证据为0。新§2.2的“语言成功加载/资源可用”是向量输入前提，不是本次发生过的观察。

canonical关系保持 `R6-D-LZ-002` / facet `GR8-ELR-001`，保 `GR5-M11-004` 与旧四family关闭；不要新增第二个语言资源根或替本作者签独立接受。无本批可选项；所有跨批可选转交见optional-disposition.json。
