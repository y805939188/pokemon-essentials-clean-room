# B21 九输入批准后继与历史保全独立静态复核

被审 NEW `5c3e19831e1e29450247fa6061f3c2feac2f893e` / tree `98062bf1205669936426ae870913e578528b740c`；对照 C `e9c140dc33de1cb0662521318b051174909e4509`，派发 D `eb1885265fcde2a52767077de3193862036c3a71`，发布入口 P `fa5e1d876c9082797d6eb71f1590f3d8d9a19b0a`。

结论：`PASS_STATIC_APPROVAL_AND_HISTORICAL_PRESERVATION_SUBSCOPE`。本子范围未发现候选阻塞。仅是批准链、历史勘误和身份保全的有界结论，不代表 FULL B21、actual、B21 接受、关闭或 FINAL 签名。

审查先读取固定 P 的 frozen-NEW/FULL/affected/dispatch，再读取 D 原完整合同及 overlay，继承原批准对象的全部限定。所有检查是文档/Git 对象静态核对；参考、Ruby、编译器、转换器、参考数据反序列化器、行为向量及旧脚本均未执行，运行观察和已证 Demo 链均为 0。

## 九输入逐字节重建

原快照身份逐项与 2026-09-30 独立批准报告中的 SHA256/bytes 交叉核验，2026-10-03 recheck-v2 保留原限定批准。下表是独立比较固定快照与 REVIEW_BASE 原稿所得；没有用作者计数作为依据。

| 原输入 | 旧快照 SHA256 | 比较结果 | 当前 C 原稿 SHA256 | 当前 C 最终正文 SHA256 |
| --- | --- | --- | --- | --- |
| specs/ui/wp68-duel.md | `6699589968fd4b8822f563f75c5b083cc89fda6fe23adefa04041ee895db2ede` | 只替换路径，+41 bytes | `ccda54e0fa9542e0678a02b62f6db75d067e0976de028ab74fe4c8d79aa4ee7d` | `fdd80183edf7d8f0479e1f071aee4edf1c16ad65721f1574058cfb83243663e2` |
| specs/creature-rpg/wp68-triple-triad.md | `1cb1ebf9da6989c3a0ab1edf26a7cf0157fc8c702c679ca17d245274fbb03adf` | 只替换路径，+41 bytes | `c55c769cfa1bf408e5134ec60e5ca5ccdeaa8c3edb263ea74a8dbb4e43851dd1` | `51eb9e360e99ece3623bf6bbd35e5376d9e82703efd1626e65df91a5c4d1bf15` |
| specs/ui/wp69-slot-machine.md | `ac2c0ad509b897f72287a9ee55c12930a8c7e6c0aa395b90f968a9c6a00d0fe6` | 只替换路径，+41 bytes | `2261c893b9628a2ff1b5058163bd05736fa719024bf23eeb2e9760f7e8e56bb4` | `dce442a55d319cc0893e93febce5e5c3dedd6a4c5dbf333730d0b42c4f7d81f9` |
| specs/pokemon-rules/wp69-voltorb-flip.md | `1708fbb07da943c13b6726ea2232f6eaa13b9906d77ccd39fa57b094c00eb60d` | 只替换路径，+41 bytes | `b22213bb54e48f0aa8e019b90ce5f39c5b110edcc53974658a0cc3132aa21528` | `f84e2e030a4ea70ee86b4da4295990aa80356f359d37ae2b0bf8726af6db054f` |
| specs/ui/wp69-slot-reels.md | `6065db8382d3cc0eba4f506c75e58194c04ece6747e1706bf539b09f106dc3b1` | 只替换路径，+41 bytes | `8cdf25ab7ea57ac271f3a16cabb2d54431d5609519b77e74b0fdbf04bc47b53c` | `aeef3712af8deaff89f6484e5aef36e01b9b5b70157844d3445e52f08019eb69` |
| specs/pokemon-rules/wp69-voltorb-layouts.md | `50d97a9f6a61c97087341a1b0c1f5551957a60ad62b46afe91ad1d4a1973ec97` | 同字节 | `50d97a9f6a61c97087341a1b0c1f5551957a60ad62b46afe91ad1d4a1973ec97` | `23c29f2d8bfa099f1d101bf989f157a309167c3a788b02d74ea7c64a0125513a` |
| specs/pokemon-rules/wp70-lottery.md | `f37d37df4c2992b81e8a6a38bd02570d0de4db927c3d0efd051fb6181a40f7ed` | 只替换路径，+41 bytes | `0374cb8ad9d9375743c3c13ca3f97c33a3074fad1fb2505819facf8fc35d67e9` | `eddd6303b5c298b2f6bf011b647e35e4bf7fe83c274577f21710eef7935e0552` |
| specs/ui/wp70-mining.md | `7c692fbbf9990dfb3b50a13e9e2773b00dc29b1bde4a60142714c15fe21e238a` | 只替换路径，+41 bytes | `417105aaa906e350dfe9bba44f8e99a227c8eaba9412a3a54e12bf7e3c152ec4` | `2c2c6e0a2c6ba4bcfe7ba2f1d33d5225c82ea03899030ca27b6d434bed0a13d2` |
| specs/ui/wp70-mining-data.md | `ddd6f46d30f61912fd052d22df3c90716799a820c8c6e6c1ad2135ac92fce9f9` | 同字节 | `ddd6f46d30f61912fd052d22df3c90716799a820c8c6e6c1ad2135ac92fce9f9` | `a8b0205fb0a862b2113861288f6bfefcde8c89ac94bd80ba225819a8257fd52b` |

7 份路径变化均且仅为 `delivery/` → `../../review/wp68-wp69-wp70-parallel-b-2026-09-30/`，每份恰好一次；Voltorb layouts 与 Mining data 两份同字节。原快照、原批准与旧 ReviewPending 原文保留。九份当前最终正文分别与精确 B18 ACT `c211767166b18799122c1e39b9f08afce6b0c92b` 原始 blob 相同，且 C→NEW 未变化；B18 R02 接受仅是共享本地贡献，`specific_minimum_satisfied=false`、B21 仍 pending、canonical OPEN。旧批准不转授当前新输出。

## 历史载体及全部 138 位置

R02 原控制 17 个旧位置组、C01 的旧完成报告 8–9/24、B02 两条去向及其审计位置、GIR-001 的 15 个位置全部有精确旧 SHA/行定位后继。R02/C01 的原 project_locations 与作者清单逐位置一致。逐位置旧内容已经阅读；旧 checks、处置、完成报告保持 C→NEW 同字节，中央当前载体的修订由正式历史勘误解释。B02 目标已实际打开：原 WP02 §4.3/附表 §7.4 是 16 开关候选使用点，原附表 §7.2 是 41文件/139行/0注释的审计统计；audit T-WP02-01/02/WP04 原节原字节保留，旧 GR-001 报告未动。

旧 158 是固定外部报告字段标签，不是实际数组长度。独立读取固定 `680e3988c4144db269e063971991134b8e0bd678` 的 `review/remediation/20261003-prepare/batches/B20/affected-review-cloud-20261011-1/b20-preservation.json`，SHA256 `5612de987509aebf71f432f69fc27a9c30c354adfeec5860a33442265d81da42`。逐位置重算原 findings 及 PLAN acceptance 规范对象哈希，并对应当前 C 本地接受记录；138/138 相符，各 owner 顺序完全相同。

| Owner | 实际数组位置数 | 原对象/批准对象/当前接受逐位置一致 |
| --- | ---: | --- |
| B10 | 7 | 是 |
| B11 | 6 | 是 |
| B12 | 9 | 是 |
| B13 | 8 | 是 |
| B14 | 24 | 是 |
| B15 | 16 | 是 |
| B16 | 24 | 是 |
| B17 | 12 | 是 |
| B18 | 8 | 是 |
| B19 | 24 | 是 |

固定 `7c5309763a6cf2e31564a1fe42786ebcbfecbef5` 的 `.../affected-review-cloud-20261011-2/b20-r2-preservation.json`，SHA256 `85ff5a7e8cbacbcadec2c88d2dc1f406d72800f97271b1d7471df93c5eead174` 保留原 158 标签；它只引用上述完整数组。当前 C 的 `batches/B20/acceptance-stage-1/historical-count-clarification.json`，SHA256 `21f54c07e7883890ccb77059c328822be196354caad70bd55ac544e0da445b94`，C→NEW 同字节。外部历史对象通过固定 Git 引用复用，不要求复制进候选，不递归复制。

日期 manifest 的 4,112 行旧前缀完整保留，只追加 15 行；正式历史勘误旧 119 行前缀保留，只追加 33 行。两个 TSV 的旧 327 数据行原始前缀保持，只追加 14 条 OPEN/待独立候选/未接受/无 actual 签名建议。B20 327 回执容器的原始 627,635 字节 C→NEW 同字节，SHA256 `d11d131dc64b399cda50b7518fffe8a812282c1b51436065647c1707c831d303`；完整 327 数组规范 SHA256 `ca73d8b68c03e80e40066acb4349683836f8165a4f2daa5935cfef8b852cd9fa`，327 个 batch/ID 键唯一。

当前固定树独立枚举为 111 正文＋17 测试族＋1索引＋2根文件＝131 Markdown；各域 11/11/15/27/23/17/7。这里只证明统计单位及目录身份，不能据数量判定行为完整或已接受。

## 有界裁决与剩余门

- `WP80-INTAKE-R02`：`PASS_STATIC_B21_APPROVAL_SUCCESSOR_SUBSCOPE`。Old exact approval snapshots and reports verified; nine inputs reconstructed as 2 same and 7 sole +41 path remap; all present final files equal exact B18 ACT and C/N unchanged; current scoped acceptance and B21 pending distinct; 17 original carrier positions covered and old review material unchanged.
- `WP80-INTAKE-C01`：`PASS_STATIC_B21_COUNT_HISTORY_SUBSCOPE`。Independent current fixed tree enumeration gives seven body domains 11/11/15/27/23/17/7 =111, test17+index1, roots2, total131; old erroneous report8/9/24 explicitly corrected by successor and raw history retained.
- `WP80-B02-R02`：`PASS_STATIC_B21_HISTORICAL_SUCCESSOR_SUBSCOPE`。Historical disposition14/81 fixed and unchanged; exact original WP02 §4.3 and appendix §7.2/§7.4 inspected, audit T-WP02-01/02 section bytes retained; 16 switches and 41/139/0 are indexed evidence, not transferred final-body statistics; original GR-001 reports preserved.
- `GIR-FD82-001`：`PASS_STATIC_HISTORICAL_CARRIER_MAPPING_ONLY`。All 15 listed historical locations retained in successor with fixed old SHA and line locators; current wrappers distinguish old status/history from B21 candidate. Full navigation/link semantics owned by parent navigation review.

剩余门：完整 B21 候选独立复审 → 唯一登记员整合 → 原 R-B21 精确 actual 与全部 affected 接口复审 → B21 C → 原 FINAL-1 → 有证据的唯一登记员关闭/最终 SHA → FINAL-2。U01–U10/G01–G12/AX01–AX20、样本/媒体/宿主/插件/配置与真实 Demo 范围继续保留。

完整逐位置身份、sha256、规范对象哈希及核验布尔值见同名 JSON；JSON 仅记录固定引用和派生证据，不复制完整差异或原证据整包。

审计过程说明：整理临时输出的辅助脚本曾因路径变量复用，短暂误写工作树 `batches/B01/author/historical-errata.md`。该工作树副本立即用固定 C 原始 3,003 bytes 恢复，SHA256 `bafff7cd954b8150456518ad407b9768559cceeb407bfe619cc1e62088cbf624`，当前 git status 该路径为空；未提交或发布误写。全部实质审查读取固定 Git 对象，Git 历史、候选和正式证据对象均未改变。
