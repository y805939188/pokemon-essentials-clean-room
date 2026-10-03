# WP26／WP27／WP30 闭合复审后回填回应（2026-09-26）

日期：2026-09-26（Asia/Shanghai）。提取侧回填记录；依据 `review/wp26-wp27-wp30-closure-review-2026-09-26/report.md`（`21712a5c8715b793e18f2426868685f6e83caccf4e3f59eee083daef7e6d6e29`，11,449 字节）与同目录 `next-batch-prompt.md`（`8091fed24599616048b6b2ac83b25fba4bebc0070b96eed18e1c79d319e58fda`，12,982 字节）。闭合复审结论：WP26/WP27/WP30 均 **PASS_SCOPED（限定静态范围）**；最后五项全部关闭、未发现直接回归；C03 记法维护随回填同步、无需再等短审。**本回应是回填索引与验收记录，不是外审通过依据。**

## 0. 回填前复算（六项固定对象）

修订前实测与报告 §1 及闭合轮 `input-snapshot/` **完全一致**（`shasum -a 256` + `stat -f "%z"` 实测）：

| 对象 | 完整 SHA-256 | 字节 |
| --- | --- | ---: |
| WP26 v3 | `afc7214aa636369021e2bb1d71daa536e78170c850d2a09e58a075367e13bbe9` | 35,387 |
| WP27 v3 | `969cb37c0d38cc27ad97c178f821debdef394a6e3fdf6492847a799faf914c67` | 27,166 |
| WP30 v3 | `41e71624796647479e6428a13f04838010bfb97e44cbb2316927cdc70a669117` | 36,040 |
| feature-matrix | `6b49c40b3508f8863500a8e36ca8ddf9960e3f411a42ed9f508007e9ceccdf0a` | 41,342 |
| manifest | `88af4e6d88306f6bcb913e66bfc0b7146dd5c75d77f0c9c9b836d65570ec4156` | 112,415 |
| 交付摘要 v3 | `df4926ae7007de65c6b4b4bcaa85b35956b9e065a6531710a5ec43f7aee11109` | 11,682 |

## 1. 回填后版本（管理性回填 → Reviewed（限定静态范围））

| 文件 | 被审 v3（保留历史） | 回填后完整 SHA-256 | 字节 |
| --- | --- | --- | ---: |
| `specs/creature-rpg/wp26-acquisition-gifts-and-script-trade.md` | `afc7214a` | `c87101adc78d2bf5d6c51fd6bb2f608fec0b2536da19d855f12cdaca79520f18` | 35,738 |
| `specs/creature-rpg/wp27-bag-and-item-storage.md` | `969cb37c` | `8064f17284c50a05420198f62340b4dfa48613c00898ca293a64e1fc42c58ea4` | 27,516 |
| `specs/creature-rpg/wp30-growth-learning-and-friendship.md` | `41e71624` | `6fbc5a201689d43706af806ba57922c319c0821b79ef7ee27abbd084e7505a79` | 36,970 |
| `planning/feature-matrix.md` | `6b49c40b` | `cbf671a81e2d783500d5018815312e6eb9f4a4c2a7f452f39ddf923633eb6824` | 42,243 |

- 回填范围（按报告 §4）：WP26＝已述六类获得/赠送/蛋/脚本交换入口、顺序、命名、容量、返回/失败与直接消费者交界；WP27＝背包/PC 容器及存取、纯预检/部分执行、游标、登记/取消/图标/快捷收集及已述入口对照；WP30＝已述曲线/换算边界、经验/EV 主规则、等级/经验辅助、学习/替换/重学、友好/亲密派生与直接写入交界。
- 矩阵在本轮先后更新两次：六行回填（中间版 `347dfff0684cade153128bbdad76636b2ade4c89d05f63e29352102a45e9407d`，41,242 字节）与三新包四行增量；上表为最终实测值。
- 头部（第 11 行"规格状态"）与尾节（WP26/WP27 §13、WP30 §15）登记 **Reviewed（限定静态范围，2026-09-26 闭合复审 PASS_SCOPED；管理性回填）**；被审 v3 保留历史；回填后版本不伪称为复审对象。
- 矩阵六行（F07-06、F10-05、F08-01、F08-02、F09-01、F09-02）→ Reviewed（对应子范围）＋前向 Inventoried，未整行笼统完成。
- **未借回填改已接受行为**；除 C03 记法与状态文字外无正文修改（差异见 `backfill-diffs/`，相对闭合轮 `input-snapshot/`）。

## 2. C03 记法维护（报告 §3，已同步）

1. **WP30 §12.2 战斗经验向量的锚定**：
   - 第 283–291 行的九条"同上"全部改为"**以'战斗经验·单参与'为基准；覆写：<本行点名的 ID/语言/参与人数/开关/物品前提>**"——各行不再继承上一行的语言差异；期望值与原主规则不变。
   - "Shadow 余量不足""Shadow 心阶段 >3"两行改为**承接"Shadow 提交"行前提**（Shadow、心阶段 2、当前经验 E、暂存 S、收益 121），分别**仅改最大经验余量=10 / 心阶段=4**；数值不变。
2. **笔误更正**：上一轮（recheck 轮）`review/wp26-wp27-wp30-recheck-2026-09-26/revision-response.md` 第 25 行的源码名 `004_PokemonBag.rb` 为 **`008_PokemonBag.rb`** 的笔误（实际核对文件为 `S/013_Items/008_PokemonBag.rb:245–280`）。**旧回应保留为历史原件、不改写**；本回应为更正记录。
3. **"8 项关闭"历史语境**：三包头部/尾节的计数为**整批**口径，回填改写为"**整批** 8 项关闭、本包仅剩具名项"，并并入修订链历史（避免读作单包计数）。

## 3. 必要状态引用同步（管理性级联）

以下已 Reviewed 规格中"WP26/WP30 完成时核对"的引用行改为"已触发（限定通过）；规则变化时复核"（被同步文件的实测哈希见本批交付摘要与 manifest §1/TSV v11）：

| 文件 | 同步位置 | 回填后完整 SHA-256 | 字节 |
| --- | --- | --- | ---: |
| `specs/creature-rpg/wp18-creature-identity-species-ownership.md` | §10 依赖表 WP26、WP30 两行 | `54b547433c0dc9101c585bbbf9f6d4e91be0c05d649b26827622aeb1b843cc42` | 37,399 |
| `specs/pokemon-rules/wp19-attributes-ability-and-stats.md` | §8 依赖表 WP30 行 | `1c4325f56d80bc23b54f168d606ca472a502475ccceb12d8a07ab8ce0b569408` | 36,443 |
| `specs/creature-rpg/wp20-hp-status-moves-helditem.md` | §10 依赖表 WP30 行 | `9a2ad1ab17e84393eeb99b9dbb2e07a558087aa30935a5f07ab8ca55cf6b1a26` | 35,027 |
| `specs/pokemon-rules/wp21-dynamic-forms-and-display.md` | §10 依赖表 WP30 行 | `b5eeb48e958d58eed9c3bf2048b507e969a81d854e5a24151f63cf718bbd3945` | 42,498 |
| `specs/creature-rpg/wp25-party-and-storage.md` | §10 依赖表 WP26 行 | `f505afd5d1dcbea666effadb5b304c7f384db07a9480637ac064d2a7b6334d17` | 27,107 |

## 4. 保留边界与停止点

- 被审 v3 哈希全部保留历史；回填后哈希/字节另记、不伪称为复审对象；manifest 保留 v1/v2/v3 链。
- 回填**无需再等短审**（报告明确允许），同会话继续执行授权批次 **WP31→WP28→WP29**（见 `delivery-summary.md`）。
- 未修改 `reference/`；未运行游戏/参考脚本/编译器/网络；未创建并行任务；未提交/推送。
- 差异基准：`review/wp26-wp27-wp30-closure-review-2026-09-26/input-snapshot/`（reviewer 快照未覆盖、未改写）。
