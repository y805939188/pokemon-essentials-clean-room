# WP23-N01 有限修订 v3 回应（WP23-N01-R01 剩余一句／WP23-N01-C01 最终同步）

2026-10-01；规格提取方。依据定点复审 [report.md](../../wp23-n01-review-2026-10-01/recheck-v2/report.md) 与 [revision-prompt.md](../../wp23-n01-review-2026-10-01/recheck-v2/revision-prompt.md)（recheck-v2：REQUEST_CHANGES，仅剩两处小项）。两项均**接受并回源核实后修订**；不重开 WP23 旧 R01～R03、原三包 14 项或 CLOSURE-R01；v1 材料（`review/wp23-n01-delivery-2026-10-01/` 根目录）与 v2 材料（`revision-v2/`）保持历史、不回写。

## WP23-N01-R01（剩余一句）— 接受（操作表确认规则按入口分列）

- **回源**：`016_UI/017_UI_PokemonStorage.rb:1964–1981` 外层选人循环的两处退出确认方向相反——BACK（`selected.nil?`）为 `next if pbConfirm("Continue Box operations?")`，**Yes 继续选人、No／取消确认退出**；Close Box（`selected[0]==-3`）为 `if pbConfirm("Exit from the Box?")` 播放 PC close 音效后 `break`，**Yes 退出、No／取消确认继续选人**；两条退出路径都返回 nil（不给位置）。
- **修订（WP23 主稿，仅一处行为文字）**：§8.1 操作表「空位置从储存选择」行删去错误的统一括注「确认中选 Yes 均继续选人」，改为按入口分列：BACK 在「Continue Box operations?」中选 Yes 继续选人、选 No／取消确认退出；Close Box 在「Exit from the Box?」中选 Yes 退出、选 No／取消确认继续选人；**退出才返回 nil**。
- **纠正 v2 回应**：`revision-v2/revision-response.md` 的 R01 修订条目重复了「确认中选 Yes 均继续选人」的统一表述，与三层合同（§8.1 层次一：BACK Yes 继续／Close Box Yes 退出）相反，本回应明确纠正；该 v2 回应按历史保留、不回写。三层合同正文、W34、10 条 v2 场景核对与其它 WP23 规则**未重写**——它们在 v2 已正确，本轮仅对齐操作表那一句。
- **保留**（recheck-v2 §2 已核实部分）：空映射盒格留在储存选人循环；有成员先显菜单、Select 才公开返回；空源直接调用与正常 UI 分开；空返回不回滚已完成的存取／标记／换盒；备用暂持分支不作为正常按钮路径。
- **同步**：头部状态与尾注记 v3；N01 v2 被审稿 `cda848c3172f63d213a64674d7d39662e3c332018e6bb414bda54450a4ad655b`／47,455 留史。WP32 仅 WP23 身份行级联（行为未改）；矩阵仅 F06-08 的 N01 待审版本；wp23-fixed／wp32-fixed／self-checks／boundary-checks 与 wp66bc-wp71 new-observations 按 v3 状态同步，new-observations 链接本轮材料、不自行 CLOSED。

## WP23-N01-C01 — 接受（最终测量后同步摘要两条当前引用）

- **顺序**：主稿与 WP32 身份行定稿 → 四份 JSON 与 N01 状态同步完毕并停止改动 → 从磁盘**程序化实测**最终 self-checks／boundary-checks 完整 SHA-256 与字节 → 更新 `delivery-summary.md` §3 两条当前引用 → 最后运行只读 `check-summary-final.py`（已先读源码确认只检查这两条引用、不写任何文件）。
- **结果**：self-checks.json `f68541a8570340091ad1b224357d37ba59a56586089f8e00d8cd0e55c560cf1f`／35,453，boundary-checks.json `441247366f4e46b045813ef86198d08b8cb56268c8ddf5566fccd1796140af9d`／22,854；校验脚本返回 **all_match=true、退出码 0**。未复用 v1 的 `c406e644…`／`bb766c24…`，也未把 recheck-v2 报告中的 v2 值当作固定目标；完整值一律实测，不凭前缀补写后缀。

## 当前身份（v3，2026-10-01 实测）

| 文件 | 完整 SHA-256 | 字节 |
| --- | --- | ---: |
| `specs/pokemon-rules/wp23-shadow-hyper-and-purification.md` | `4b58ebf0edea557875eaf51c81320fa781672509a91262c0fcdb8a6ca3777dac` | 48,379 |
| `specs/pokemon-rules/wp32-contextual-trade-and-post-battle-evolution.md`（仅 WP23 身份行） | `0fe64ae24d8d871c2f9547990bcff6f58da7d3b27e8c350983baa664550af216` | 30,435 |
| `planning/feature-matrix.md` | `8f668f98dd8adabbcb5c26c547d8b38552920d4ca41da2b00fda165fb29ee341` | 57,762 |
| `review/wp22-wp23-wp32-delivery-2026-09-30/delivery-summary.md` | `8cd0b6092a7dab2bd00f6a0f0d9e91592a8b7677adb813de0ffa26c844c562e1` | 6,302 |

被审链：回填版 `6343cfea`／41,529 → N01 v1 `e7765dac`／45,274（被审）→ N01 v2 `cda848c3`／47,455（被审）→ N01 v3（本轮）。差异相对 `wp23-n01-review-2026-10-01/recheck-v2/input-snapshot`（1120 项固定输入）生成，9/9 patch 重建逐字节匹配当前文件，见 [diff-bindings.json](diff-bindings.json)。

## 最终检查（三条最小验收）

1. **确认规则一致**：BACK Yes＝继续选人、Close Box Yes＝退出，在操作表（第 134 行）、三层合同正文（第 145 行）与本回应中一致；主稿已无「均继续」残留；见 [checks.json](checks.json) 的 v3-C1～C4。
2. **身份一致**：self／boundary 最终磁盘身份与摘要 §3 引用一致（`check-summary-final.py` all_match=true、退出码 0）；摘要最终身份 `8cd0b609`／6,302 与主 TSV v47／manifest 第七十二轮当前行一致（登记后复核，见下）。
3. **范围未外溢**：WP23 仅头部状态／第 134 行／尾注三处；W01～W46 连续唯一；WP32 仅第 214 行；矩阵仅 F06-08；摘要仅第 11、13、29～30、42 行；v1／v2 材料、reviewer 原件与全部冻结快照未改（预检 1120 输入、5 外部快照、17 份 reviewer 原件全部复测一致；reference 固定 commit、Git 清洁）。

**检查分段**：checks.json 为阶段一（登记前）；登记完成后做阶段二——全量当前登记对磁盘复测、摘要最终身份对 TSV／manifest 当前行、并重跑 `check-summary-final.py`，结果写入 `registration-final-checks.json`。按 revision-prompt，该最终 manifest／TSV 检查文件**不登记进 manifest／TSV 自身**，避免目标身份循环。

状态：**N01 REVISED_PENDING_REVIEW（有限修订 v3）**，待定点复审；其余范围维持原审批状态。不进入 GR-011／GR-013 修订或其它包；不创建任务／Agent、不发其它会话消息、不提交／推送。
