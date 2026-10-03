# 管理回填逐项依据（对象—原状态—最新具名批准—回填范围）

2026-10-02；单一整合者。本表逐项对应本轮 Feature Matrix 集中回填；每项均落到对应最新通过报告，不把历史问题台账的 OPEN 或旧规格头部当作当前未闭合结论。行为主稿/附表均未因回填改动字节（仅导入的 9 份 B 规格按交接做了 delivery/ 路径重映射，前后身份见 [import-mapping.json](import-mapping.json)）。

## A. B 导入 6 条（F17-01～06）

| 对象 | 原状态 | 最新具名批准 | 被审身份 → 当前身份 | 回填范围 |
| --- | --- | --- | --- | --- |
| F17-01 Duel | Inventoried | `review/wp68-wp70-review-2026-09-30/report.md`（2026-09-30 PASS_SCOPED） | `66995899`/9,133 → `ccda54e0`/9,174（路径重映射） | WP68 Duel D-A～E＋Inventoried（运行/事件/媒体/概率分布） |
| F17-02 Triple Triad | Inventoried | 同上 | `1cb1ebf9`/17,196 → `fae1ffc1`/17,237（重映射） | T-A～G＋Inventoried（最终分布等） |
| F17-03 Slot Machine | Inventoried | 同上 | `ac2c0ad5`/11,143 → `2261c893`/11,184（重映射） | S-A～F＋有序转轮附表（`6065db83`/1,945 → `8cdf25ab`/1,986 重映射）＋Inventoried |
| F17-04 Voltorb Flip | Inventoried | 同上 | `1708fbb0`/10,295 → `b22213bb`/10,336（重映射） | V-A～E＋候选附表（`50d97a9f`/4,053 原字节）＋Inventoried |
| F17-05 Lottery | Inventoried | 同上 | `f37d37df`/10,078 → `0374cb8a`/10,119（重映射） | L-A～E＋Inventoried（开奖/兑奖事件） |
| F17-06 Mining | Inventoried | 同上 | `7c692fbb`/12,474 → `417105aa`/12,515（重映射） | M-A～F＋数据附表（`ddd6f46d`/5,594 原字节）＋Inventoried |

## B. 主线已通过待回填条目

| 对象 | 原状态 | 最新具名批准 | 回填范围 |
| --- | --- | --- | --- |
| F18-05（WP76） | ReviewPending v4 待短复审 | `review/wp76-review-2026-10-02/recheck-v4/report.md`（PASS_SCOPED 20/20） | WP76 A～F 具名静态范围 Reviewed＋Inventoried（运行/素材/demo） |
| F10-03／F10-04（WP37） | ReviewPending v3 待定点复审 | `review/wp37-review-2026-10-02/recheck-v3/report.md`（PASS_SCOPED 15/15） | WP37 A～C／D～F 具名静态范围 Reviewed＋Inventoried |
| F13-01／F13-02（WP53） | ReviewPending v4 待短复审 | `review/wp53-review-2026-10-02/recheck-v4/report.md`（PASS_SCOPED 15/15） | WP53 A～B／C～F Reviewed＋Inventoried |
| F14-05（WP61） | ReviewPending v3 待复审 | `review/wp61-review-2026-10-02/recheck-v3/report.md`（PASS_SCOPED 11/11） | WP61 A～F Reviewed＋Inventoried |
| F16-01／F16-02（WP65） | ReviewPending v3 待定点复审 | `review/wp65-review-2026-10-01/recheck-v3/report.md`（PASS_SCOPED 8/8） | WP65 A～C／D～F Reviewed＋Inventoried |
| F16-05（WP67-A） | ReviewPending v3 待定点复审 | `review/wp67a-review-2026-10-01/recheck-v3/report.md`（PASS_SCOPED 17/17） | WP67-A A～G Reviewed＋Inventoried |
| F16-06（WP67-B） | ReviewPending v3 待复审 | `review/wp67b-review-2026-10-02/recheck-v3/report.md`（PASS_SCOPED 16/16） | WP67-B A～F Reviewed＋Inventoried |
| F15-02／F15-03（WP63） | ReviewPending v3（第一组 31 项全部通过、回填另记） | `review/wp66a-wp63-wp64-closure-review-2026-10-01/final-recheck/report.md`（PASS_SCOPED 31/31） | WP63 A～C／D～E Reviewed（管理性回填）＋Inventoried；规格链接状态附注同步 |
| F15-04／F15-05（WP64） | 同上 | 同上 | WP64 A～B／C～F Reviewed＋附注同步 |
| F16-03（WP66-A） | 同上 | 同上 | WP66-A A～F Reviewed＋附注同步（WP66-B 原限定 Reviewed 保持） |
| F06-08 N01 子项 | ReviewPending v3 待定点复审 | `review/wp23-n01-review-2026-10-01/recheck-v3/report.md`（PASS_SCOPED） | WP23-N01 净化室选择可达性子项 v3 Reviewed（管理性回填） |

## C. GR-001～016 附注（19 处）

| GR | 所在 Feature | 最新具名批准 | 回填 |
| --- | --- | --- | --- |
| GR-001 | F02-02 | `review/gr001-gr003-review-2026-10-01/recheck-v2/report.md` | Reviewed（定点复审 PASS_SCOPED；管理性回填） |
| GR-002 | F02-05 | 同上（保持 CLOSED 继承） | 同上 |
| GR-003 | F03-02 | 同上 | 同上 |
| GR-004 | F04-03 | `review/gr004-gr006-review-2026-10-01/report.md` | 同上 |
| GR-005 | F04-05 | 同上 | 同上 |
| GR-006 | F04-06 | 同上 | 同上 |
| GR-007 | F05-02 | `review/gr007-gr009-review-2026-10-01/recheck-v2/report.md` | 同上 |
| GR-008 | F06-06 | 同上（保持 CLOSED 继承） | 同上 |
| GR-009 | F07-03 | 同上 | 同上 |
| GR-010 | F10-05 | `review/gr010-gr012-review-2026-10-01/recheck-v2/report.md` | 同上（保持 CLOSED 继承） |
| GR-011 | F04-03、F10-02（两处） | 同上 | 同上 |
| GR-012 | F14-03 | 同上 | 同上 |
| GR-013 | F11-05、F11-07、F13-06（三处） | `review/gr013-gr016-review-2026-10-01/recheck-v2/report.md` | 同上 |
| GR-014 | F12-05 | 同上（保持 CLOSED 继承） | 同上 |
| GR-015 | F12-08 | 同上 | 同上 |
| GR-016 | F06-04 | 同上 | 同上 |

## 状态三分法复核

- **具名静态范围已通过**：上表全部 Reviewed 项。
- **运行/demo 未知**：各行 ＋Inventoried 子范围逐条保留（运行/事件/媒体/概率分布/demo 可达性）。
- **前向引用待后续包**：WP77（demo 事件可达性）、WP78/79（整体 double review）、WP80（净化交付）保持原任务编号，不在本轮范围。
- 未获批准范围未顺带标 Reviewed（F17-07、F18-06、F18-07 demo 范围等保持原行）。
