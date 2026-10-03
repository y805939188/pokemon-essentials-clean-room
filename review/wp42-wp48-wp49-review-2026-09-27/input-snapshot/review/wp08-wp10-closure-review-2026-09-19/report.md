# WP08–WP10 闭合复审

日期：2026-09-19。Reference/Audit 侧独立 reviewer。本报告和快照是内部审查材料，不是 WP80 sanitized 产物。

**结论：PASS_SCOPED。WP08-R01、WP10-R05 已闭合；WP09 状态回填和 BATCH-C02/C03 维护通过。WP08–WP10 的当前限定范围均已通过，可开始下一批 WP11–WP13。**

本轮没有剩余阻塞项。§4 记录一处时序措辞维护，可随状态回填处理，不要求再次全包送审。

## 1. 实际对象与基线

工作区 `/Users/dingshinn/Desktop/pokemon-framework-reference/`。参考 HEAD 实测仍为 `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`，describe 为 `v21.1-23-g8c5911e4`；默认机制世代 8。

| 对象 | 被审 SHA-256 | 字节数 |
| --- | --- | ---: |
| WP08 v3 | `65a79ab5fd52e6f5e7989af2c5423083953807263baab97523b99c25088948b2` | 17796 |
| WP09 状态/维护版 | `76450356b03f11abc59808e84c7c07e0f69c3f6543aaafc9b1856b3cdf2de4e6` | 18087 |
| WP10 v3 | `d50edf924e43179ef1f191e5e37a07639f11fbc68be343129c120edcf64cabde` | 22199 |
| manifest | `5834ef418232cc18c9c7d1e9fdadebfdc8c706b79c659d6160cd54c21160c5d7` | 16106 |

本轮固定 41 项输入。manifest **39 项完整哈希和字节数全部匹配**，上轮报告和提示词原件未变。见 [input-manifest.json](/Users/dingshinn/Desktop/pokemon-framework-reference/review/wp08-wp10-closure-review-2026-09-19/input-manifest.json)。

WP09 实际变化为头尾状态登记及缺键类型约束的限定；矩阵只回填 F03-01/F03-03 的已审子范围。WP08 改动为两处旧总结修正；WP10 为三行转换描述及拒绝删除的控制流说明。没有夹带其他包行为变化。见 [changes-from-v2.diff](/Users/dingshinn/Desktop/pokemon-framework-reference/review/wp08-wp10-closure-review-2026-09-19/changes-from-v2.diff)。

## 2. 执行检查与旧问题处置

重新核对实际 diff 和上轮剩余项，阅读对应消息查找、转换赋值/清理、默认类型校验及退出分支。此前 115 个相关源文件的哈希未变，Git blob 均匹配固定提交；这不表示本轮全文重读 115 文件。Git 只读查询退出码均为 0，普通状态为空，ignored 仍为 `.DS_Store`、`PBS/.DS_Store`。见 [source-checks.json](/Users/dingshinn/Desktop/pokemon-framework-reference/review/wp08-wp10-closure-review-2026-09-19/source-checks.json)。

| 项目 | 结论与证据 |
| --- | --- |
| WP08-R01 | 关闭。第 7/8 节旧总结已按入口分层：默认材料缺失不覆盖当前语言命中，数组未中为空串，哈希/地图未中回输入原文。与 `Data/Scripts/001_Technical/003_Intl_Messages.rb:589–631` 一致。 |
| WP10-R05：树果 | 关闭。符号条件控制字段填充，非符号不意味着跳过整个替换；单项转换与完整链上游归一化已区分。源码 `Data/Scripts/002_Save data/005_Game_SaveConversions.rb:109–136`；实际操作时序按 §4 精确表述。 |
| WP10-R05：跟随者 | 关闭。重建 followers 受旧列表非空条件控制；dependentEvents 置 nil 在条件外，空数组也清理。源码同文件 152–163。 |
| WP10-R05：已有寄养槽 | 关闭。新槽 `[C, 空]`、旧 A/B 得到 `[C, A]`；已占用的新槽被跳过，旧字段清理仍执行。源码同文件 174–199。 |
| BATCH-C02 | 关闭。WP09 缺键结论限定到当前默认 17 项的类型约束，不外推未绑定类型的扩展。源码 `002_SaveData_Value.rb:31–33,210–212`。 |
| BATCH-C03 | 关闭。拒绝删除明确为 exit/SystemExit、退出当前执行，不删除且不返回菜单。源码 `013_UI_Load.rb:244–248` 及 `003_Errors.rb:81–84`。 |

其余已关闭的 WP08–WP10 问题继续关闭。WP01–WP07 的限定通过范围不重开。

**未运行游戏、Ruby、参考表达式、编译/转换器、插件或网络请求，未操作真实存档。** 所有向量均为静态核对；未开始下一批提取。只写本轮独立 review 目录。

## 3. 通过范围、未知与状态建议

- **WP08**：固定基线的文本域与已述身份形态、默认/当前语言消息分层、主动/延迟载入、查找/空译/异常边界、占位格式化、提取/编译/直写工作流及适用静态场景。
- **WP09**：继承上轮对默认 17 项持久状态、启动/新游戏/继续、地图恢复分流、保存前后内存/磁盘边界的限定通过；本轮登记和限定维护有效。
- **WP10**：固定默认转换登记、版本筛选/顺序、旧格式入口边界、备份与写回路径、已述恢复/紧急保存/地图失败分支、转换目录及已记录参考快照反例。

通过不证明任意旧档兼容、真实存档转换结果、真实插件组合、宿主落盘/重启行为或完整 Demo 可达。U01–U10 与已登记的运行/材料限制保持；源码中的已知异常结果也不会因通过而变成目标框架必须照搬的设计。

可据本报告登记 WP08、WP10 为 **Reviewed（上述限定范围）**，同步 F02-05 的 WP08 子范围及 F03-02/F03-04 的 WP10 子范围。其他文本呈现、领域语义、旧档样本、宿主与完整组合范围保持原状态。保留本轮被审哈希、状态/维护后的新哈希与 diff，不把新字节冒充本轮原对象，也不改写 review 原件。

## 4. 非阻塞维护 BATCH-C04：树果转换时序措辞

WP10@d50edf92:106 将“新建并替换”合写在前，随后说“再进一步填充”，容易被误读成先替换旧记录、后填字段。

本轮按源码核对的精确顺序是：**先构造新对象，按条件填充字段，正常到达分支末尾时才替换旧条目**。非符号输入跳过的是条件填充，仍可到达末尾替换；若填充阶段抛错，则尚未执行该条目的末尾替换（`005_Game_SaveConversions.rb:110–122,124–136`）。

建议在状态回填时将该行改为上述顺序。此处是避免措辞歧义，不改变原定点验收中的正常完成结果，不重开 R05，也不阻塞下一批；保留维护 diff 即可。

## 5. 下一批：WP11–WP13

当前计划仍为 87 个可执行包。下一批建议先做三个紧密关联的包；WP13 的解释器命令全集工作量较大，因此本批不追加 WP14。

| 包 | 内容 | 依赖安排 |
| --- | --- | --- |
| WP11 | 地图拓扑与转移，F04-01 | WP03、WP05 已通过 |
| WP12 | 地形、运动、载具，F04-02/F04-03 | 先取得本批 WP11 的相关自检版本，另引用已通过的 WP02/WP06 |
| WP13 | 地图事件、NPC、跟随，F04-04/F04-05 | 使用本批 WP11/WP12 的相关自检版本与已通过的 WP05 |

具体依赖核对见 [next-batch-dependencies.json](/Users/dingshinn/Desktop/pokemon-framework-reference/review/wp08-wp10-closure-review-2026-09-19/next-batch-dependencies.json)。批内可逐包自检后继续，批末统一送审；不把自检当 Reviewed。WP14 保留原计划与编号，后续单独安排或并入适合的批次。

使用 [WP11–WP13 执行提示词](/Users/dingshinn/Desktop/pokemon-framework-reference/review/wp08-wp10-closure-review-2026-09-19/next-batch-prompt.md)。本轮停止于报告及提示词交付，未代提取方回填状态、未提取 WP11。最终一致性和交付哈希见 [final-checks.json](/Users/dingshinn/Desktop/pokemon-framework-reference/review/wp08-wp10-closure-review-2026-09-19/final-checks.json)。
