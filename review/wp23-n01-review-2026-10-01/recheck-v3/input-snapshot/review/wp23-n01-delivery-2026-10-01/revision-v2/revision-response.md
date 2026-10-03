# WP23-N01 有限修订 v2 回应（WP23-N01-R01／WP23-N01-C01）

2026-10-01；规格提取方。依据独立复审 [report.md](../../../wp23-n01-review-2026-10-01/report.md) 与 [revision-prompt.md](../../../wp23-n01-review-2026-10-01/revision-prompt.md)。两项均**接受并回源核实后修订**；不重开 WP23 旧 R01～R03、原三包 14 项或 CLOSURE-R01；N01 首版材料（`review/wp23-n01-delivery-2026-10-01/` 根目录 response／checks／diff-bindings／n01-diffs）已被本轮快照固定，留作 v1 历史、不回写。

## WP23-N01-R01 — 接受（外层选人返回门）

- **回源**：`016_UI/017_UI_PokemonStorage.rb:1964–2022` 外层选人循环：`pbSelectBox` 返回后先取 `@storage[selected]`——**成员为空 → `next` 继续选人循环**（无菜单、无公开返回、无放置调用）；有成员 → 显示 Select／Summary／Withdraw／Item／Mark／Cancel 菜单，**仅 Select 赋返回值并退出**；BACK → `pbConfirm("Continue Box operations?")`（Yes 继续、No／取消确认退出并返回 nil）；Close Box → `pbConfirm("Exit from the Box?")`（确认后返回 nil）。`:837–891` 的切盒即时写入与 `:1705–1723` 的取出实际写入核对「此前操作不回滚」前提。
- **修订（WP23 主稿）**：
  - §8.1 操作表行：Select 才返回位置、确认中选 Yes 均继续选人、「队伍」按钮先经外层成员门。
  - §8.1 三层合同 v2：层次一改为公开返回的产生点（Select／BACK 确认／Close Box 确认分列）＋**空返回不回滚此前已完成的存取／标记／当前盒变化**；层次二改为外层成员门（格空 → 继续选人循环；有成员 → 先显菜单、选 Select 才返回）；「空源位置 → 放置 false」限定为**绕过选择器的直接调用**前提；「选择并暂持」明确为当前正常输入未发出的备用命令分支。
  - W34 改为三层对照 v2：(a) 格空 → 继续选人循环、不返回、不进放置；格有 X → 先显菜单、选 Select 才返回并可放置 X 删该格；(b) 直接调用（同前，无最后可战斗门、非 UI 可达示例）；(c) 切盒后退出（或先取出再取消）→ 返回 nil 但当前盒新值／已完成的取出**不回滚**。
  - 头部状态与尾注记 v2；N01 首版被审稿 `e7765dac…`／45,274 留史。
- **保留**（复审 §4 确认的正确结论）：取出模式启动、负位置非队伍语义、默认基础储存对该位置的读取／写入／删除指向同一盒格、合格非空成员经 Select 返回并满足放置条件后可入室内并删源盒格、替换原始值相等门、直接提供有效队伍位置时缺最后可战斗守卫。

## WP23-N01-C01 — 接受（摘要两项当前身份）

- **事实**：`delivery-summary.md` §3 的 self-checks／boundary-checks 引用未随第七十轮级联。已从磁盘**程序化实测**更正为 `c406e6445f67a79439fd192655f6b228462ea805ab1eeba39042cbd39e29fdca`／35,439 与 `bb766c24baa044bb354fe90e34c368ff3b8178b5f2b1015bbc2f098c6a599985`／22,843（没有凭前缀补写后缀）。旧 revision-v2／旧 validation-results 保持历史角色，不冒充本次 N01 最终检查；CLOSURE-R01 不重开（不同待办）。
- 本轮 §3 摘要相关历史行同步留史；新版进入新历史。

## 当前身份（v2，2026-10-01 实测）

| 文件 | 完整 SHA-256 | 字节 |
| --- | --- | ---: |
| `specs/pokemon-rules/wp23-shadow-hyper-and-purification.md` | `cda848c3172f63d213a64674d7d39662e3c332018e6bb414bda54450a4ad655b` | 47,455 |
| `specs/pokemon-rules/wp32-contextual-trade-and-post-battle-evolution.md`（仅 WP23 身份行） | `06d990a7ae652d0f656131ac3ef5f7555a0124ae2304c34e5ed33467d47aff4d` | 30,435 |
| `planning/feature-matrix.md` | `49e3423610675b8a0f5d4c96dbbf3b8a10af9371631db12a2d7b65c0d04fe5d4` | 57,703 |

被审链：回填版 `6343cfea`／41,529 → N01 v1 `e7765dac`／45,274（被审）→ N01 v2（本轮）。差异相对 `wp23-n01-review-2026-10-01/input-snapshot`，见 [diff-bindings.json](diff-bindings.json)。

状态：**N01 REVISED_PENDING_REVIEW（有限修订 v2）**，待定点复审；其余范围维持原审批状态。不进入 GR 修订或其它包。
