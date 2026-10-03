# WP77 首审修订 v3 回应（复审残留 2 项 P2＋本轮补充 1 项 P3，共 3 项）

2026-10-03；规格提取方。依据 [report.md](../../wp77-review-2026-10-03/recheck-v2/report.md)（v2 复审：**7 项 CLOSED，R03／R07 仍 OPEN，新增 N01（P3）**）与 [next-task-prompt.md](../../wp77-review-2026-10-03/recheck-v2/next-task-prompt.md)：**3 项按原编号原位修订**（N01 为本轮审查补充发现，不伪称原 9 项之一），无新增自编 ID。v1／v2 交付材料、首审与复审原件、各级快照保持原字节。reference 固定 commit `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`、Git 清洁。

修订对象与当前身份（磁盘程序化实测）：

| 文件 | v2 被复审（recheck-v2 input-snapshot 冻结） | v3 当前 |
| --- | --- | --- |
| `specs/demo/wp77-demo-evidence-and-capability-coverage.md` | `40f21b99acec8571df27447b281529d9463dffbc0a3b6c4f182e42cb8d431cee`／41,773 | 见 [diff-bindings.json](diff-bindings.json) 与登记 |
| `review/wp77-delivery-2026-10-03/revision-v2/evidence-coverage-table.md`（v2 附表） | `95d38a6c905df41112f132c02bc4990e0e5e147a5dd9bbf337bb4329f252c234`／7,628 | **本轮无变更**——行为无变化，按 v3 提示保持并引用已核身份，不为增加 diff 制造变更 |
| `review/wp77-delivery-2026-10-03/revision-v2/gap-register.md`（v2 缺口表） | `891793ebf6dbb609743b8d0782200b9f76a2e32c345bdf80ff0de635587aecee`／4,454 | **本轮无变更**——同上 |

一份 diff 相对复审冻结 v2 生成（主稿 **4 hunks**）、patch 精确重建到当前字节，见 [diff-bindings.json](diff-bindings.json) 与 [revision-diffs/](revision-diffs/)。附表与缺口表行为不变，沿用 v2 已核身份。场景 M01–M16 保留（**本轮无场景行变更**——M05／M12 已核对无同类错误；无新增/删除）。作者状态：**REVISED_PENDING_REVIEW**——不自行 CLOSED、不自行 Reviewed。

## R03（P2）普通点枚举仍含带飞行目的地的 Cedolan 第二点（已修）

- **v2 已接受**：6 条飞行记录对 5 个不同目的地（Cedolan 两条共用）、Essen 26＝18 普通＋6 飞行＋2 开关、飞行—治疗点完全匹配 4 个——复审已关闭该部分。
- **残留**：§4.4 普通点 18 条的枚举示例仍把带飞行目的地的 Cedolan 第二点位（(14,10)）列入普通组，与「互斥类别分组」自述冲突。
- **回源**：`PBS/town_map.txt:8–9`（本轮复核——(13,10) 与 (14,10) 两条 Cedolan 记录**均带飞行目的地 7＠(47,11)**）。
- **修订位置**：§4.4（普通点 18 条枚举删去 Cedolan 第二点位，补记「**两个 Cedolan 点均带飞行目的地、只归飞行记录组，普通组不含任何 Cedolan 记录**」）；主稿修订记录 v3；checks R03。
- **对照**：26＝18＋6＋2、5 个不同目的地、4 个治疗点匹配、Cedolan 7＠(47,11) ≠ map 009 的 8＠(17,11) 与 Tiall 1 条／总数 27 全部保持不变。

## R07（P2）Safari 水/钓表误写 FEEBAS 重复（已修）

- **v2 已接受**：陆遇 12 条／11 种、水/钓 14 条／12 种（槽位记录数与不同物种数分开）——复审已关闭该部分。
- **残留**：§5.1 写「MAGIKARP 与 FEEBAS 各重复槽位」——FEEBAS 实际仅一条，不存在重复。
- **回源**：`PBS/encounters.txt:245–262`（本轮复核——[068] 水/钓块：**MAGIKARP 三条**＝OldRod 两条（第 251–252 行）＋GoodRod 一条（第 254 行）；**FEEBAS 仅 GoodRod 一条**（第 255 行））。
- **修订位置**：§5.1（更正为「重复者为 MAGIKARP 三条（OldRod 两条、GoodRod 一条）；FEEBAS 仅 GoodRod 一条」）；主稿修订记录 v3；checks R07。
- **对照**：水/钓 14 条／12 种、陆遇 12 条／11 种、Tiall 6 条 _1 后缀＋2 条无后缀、数量限根目录当前表与 Gen 5–8 备份身份登记全部保持不变。

## N01（P3，本轮补充发现）地图 045 误归 Route 5（已修）

- **说明**：本项为 v2 复审在 R01–R09 之外的补充发现，按审查给的 N01 编号处理，不伪称原 9 项之一。
- **残留**：§4.2 户外图清单把 map 045 与 041 并列为 Route 5；实际 045 源注释与 Name 均属 Route 6。
- **回源**：`PBS/map_metadata.txt:200–221`（本轮复核——`[041] # Route 5`／Name Route 5；`[044] # Route 6`／Name Route 6；`[045] # Route 6 Cycling Road`／**Name＝Route 6**）。
- **修订位置**：§4.2（清单更正为 **Route 5(041)、Route 6(044/045——045 为 Route 6 自行车道，源注释与 Name 均属 Route 6)**）；主稿修订记录 v3；checks N01。
- **对照**：已正确的 041↔045 连接条目（§4.3 规范化表 (41,45)）不改；69 节登记、19 连接、户外图 MapPosition 结论不变。

## 已关闭 7 项保持

R01（Home 回程≠新游戏起点）、R02（Route 8↔Lappet 直连）、R04（岛屿开关读取消费者）、R05（Dungeon 标记与参数回退）、R06（等级缩放夹限）、R08（时段 Intro 与中心条目计数）、R09（计数口径统一）经复审 **CLOSED**，本轮未改动其结论；v3 仅修订上述 3 项及其直接交叉引用。

## 总体自检结果（全文口径）

- 一份 diff 对复审冻结 v2 patch 精确重建（主稿 **4 hunks**——见 [diff-bindings.json](diff-bindings.json)）；变更覆盖 3 项位置及修订记录；v2 已接受的全部结论（E34 九份身份、69 节/19 连接/19 遭遇节/20 训练家节/15 注册类型、6 飞行记录/5 目的地/4 匹配、开关读取消费、参数回退、夹限规则、档位计数）保持。
- **残留扫描覆盖最终主稿与本目录新材料**：3 项同根残留逐一命名核对（普通组含 Cedolan、FEEBAS 重复、045 归 Route 5 三处旧断言已全部原位消除）；带日期的 v1／v2 修订记录留史、由 v3 记录接续更正。
- 场景编号：M01–M16 共 16 个定义行，全文唯一、交叉引用可解析；**本轮无场景行变更**、无新增/删除。
- 链接解析：v3 新材料全部本地链接经脚本解析存在（见 [checks.json](checks.json)）。
- 来源身份：本轮**无新增源码阅读**——为同 HEAD 既有阅读复核（`town_map.txt:8–9`、`encounters.txt:245–262`、`map_metadata.txt:200–221` 三段定点）；全文/定点/继承/仅身份分开登记，不把身份核验当阅读。
- 净化：v3 新写文字扩展模式扫描 **0 命中**；审计名仅作标识。
- 未改写 v1／v2 交付材料、reviewer 原件与各级快照；全部既有具名批准（WP01～WP76、WP68–70 整合收口）保持；reference 只读；未运行游戏/编译器/生成器/反序列化/参考行为模拟器。
- 修订后状态：WP77 保持 **ReviewPending（首审修订 v3，待短复审）**——不自行关闭 3 项、不自行 Reviewed、不宣称通过；③已证事件链与④运行观察继续为 0。
