# C01 归档纠正记录（WP80-B01-C01；2026-10-03）

依据 `review/wp80-batch-01-review-2026-10-03/recheck-v3/findings.md`（C01 非阻塞归档整理）执行。本记录说明版本归位，**不改写 v2/v3 既有检查记录来伪装覆盖从未发生**。

## 事实

- WP80 批次 1 v3 修订期间，条款处置表的 v3 同步版被误写回 `revision-v2/clause-disposition.md`（原位覆盖）——v2 作者材料「字节保持」声明对该文件一度不成立。
- 原 v2 完整字节一直在独立冻结快照中（`review/wp80-batch-01-review-2026-10-03/recheck-v2/input-snapshot/`），当前 v3 内容也已冻结锁定，**无历史证据丢失**。

## 归位（按 findings.md 顺序执行并程序化核验）

| 步骤 | 结果 |
| --- | --- |
| 1. 当前已接受 v3 内容保存至 `review/wp80-delivery-2026-10-03/revision-v3/clause-disposition.md` | 完整 SHA-256 `78b4f5041d9048efe2d461f45cb2edb08173145f24a0dacd3b812c88206cbf80`／10,029 字节——与冻结锁定身份**一致** |
| 2. 从只读冻结对象恢复 `review/wp80-delivery-2026-10-03/revision-v2/clause-disposition.md` | 完整 SHA-256 `a69348ffa1be227687ecbfc2856fa73aab41c5a239008716c9522e31224f046b`／8,732 字节——原 v2 身份**一致** |
| 3. 有效引用指向 | v2 回应内相对链接仍解析至恢复后的 v2 原件（历史一致）；v3 材料对处置表的提及为纯文本（无链接）；**当前有效处置表＝`revision-v3/clause-disposition.md`**；后续批次引用一律指向 v3 |

## 登记

第 153 轮：manifest §1 该 v2 行恢复原 v2 身份（v3 同步误写期身份 `78b4f504`／10,029 留史见§3）；新增 `revision-v3/clause-disposition.md` 行；§3 追加本纠正历史；本记录单独保存。**行为验收不受影响**（批次 1 PASS_SCOPED 保持，R01–R03 保持关闭）。
