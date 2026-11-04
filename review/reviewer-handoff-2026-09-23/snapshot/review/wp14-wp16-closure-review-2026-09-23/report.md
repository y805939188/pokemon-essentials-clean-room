# WP14–WP16 v3 闭合复审

日期：2026-09-23（Asia/Shanghai）。独立 reviewer，Reference/Audit 侧材料，不是 WP80 sanitized 交付。S = `reference/pokemon-essentials/Data/Scripts/`。

**结论：WP14、WP15、WP16 分别 PASS_SCOPED，可以开始下一步 WP17。** 本轮关闭 WP14-R01、WP15-R01、WP16-R01；WP16-R02 继承 CLOSED。原四个行为问题已全部闭合，本轮修订及直接传播未发现阻塞回归。WP01–WP13 的既有限定通过不重开。

先由提取方将三包按下述范围回填 Reviewed、保留被审哈希及新哈希，即可在同一轮执行 WP17；不必为纯状态回填再等待一次行为复审。本 reviewer 不代改规格、矩阵或 manifest。

## 1. 固定版本与检查范围

| 对象 | 完整 SHA-256 | 字节数 |
| --- | --- | ---: |
| `specs/overworld/wp14-random-dungeons.md` v3 | `5ca2c044a47156b4b8a75a4d51e26a4ce90397b18f7df71f02ab60b8a5a91363` | 23596 |
| `specs/overworld/wp15-resource-matching-and-audio.md` v3 | `8e44c387811e325c78f39f341a3a7c208407ae9689af28c4afdd9b801970e95e` | 20631 |
| `specs/overworld/wp16-world-rendering-and-visual-transitions.md` v3 | `ccb7bb9ac4039d186cedcea4c5f0e35c03afdd562bc8e221a22f6f05cdd33563` | 21104 |
| `planning/feature-matrix.md` | `1dc4faf5efd4fc110637b64e16cb533d0f39a12fb373bebcc17a926a8dd2436d` | 35130 |
| `planning/review-manifest-2026-09-19.md` | `ce026a9179ea468be3b1e1468b065f4eae25720402d0c3b75e01407f5e9b967a` | 43696 |
| 提取侧 `review/wp14-wp16-recheck-2026-09-23/revision-response.md` | `92ebec7d281e86e497ae8ce63d0f32a8be23430de0b2ba284bbb3661a8691b45` | 5016 |

- 当前 manifest **85 条完整 SHA-256/字节数记录全部匹配**；本轮固定 93 项输入。两条“见原件”历史行不纳入完整哈希记录数。
- 对照 v2，既有输入变化仅三份规格、矩阵及 manifest；另有新回应和三个 diff。三个 diff 均能精确重建 v3 文本。上轮审查 artifacts 及固定快照均未改写。
- WP11 manifest 当前/历史条目继续与 v2 快照相同。WP01–WP13、AGENTS、overview、module-map 和 extraction-plan 保持既有字节版本。
- 参考 HEAD 为 `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`，describe 为 `v21.1-23-g8c5911e4`；普通状态为空，ignored 为 `.DS_Store`、`PBS/.DS_Store`。
- 本轮 7 个相关源码文件逐字节匹配固定提交。语义复核只覆盖原剩余问题及其直接调用链，具体片段见 `source-checks.json`；不冒称重新完成首轮整包提取或全部源码审查。

配套记录：`input-manifest.json`、`input-snapshot/`、`changes-from-v2.diff`、`source-checks.json`、`static-checks.json`。未运行游戏、参考 Ruby/表达式、生成器、解释器、编译器、转换器、插件或网络，未操作真实地图/存档。

## 2. 问题闭合证据

以下行号对应本轮固定规格。

| 原编号 | 结论 | 本轮核对 |
| --- | --- | --- |
| WP14-R01 | CLOSED | WP14:158–161、173、202–203、214 已区分空事件集合与含事件的最终异常结果，说明每轮重置标记、最后一轮决定最终抛错；与 `S/012_Overworld/008_Overworld_RandomDungeons.rb:379–380,428–434,1011–1014,1077–1105` 一致 |
| WP15-R01 | CLOSED | WP15:65、69、142、169–171 已区分形态键缺失但回退基础记录、查询整体 nil、文件候选全缺失；蛋通用候选也可 nil。对应 `S/010_Data/002_PBS data/008_Species.rb:154–163`、`009_Species_files.rb:37–63,113–120,144–169,183–191` 和 `S/001_Technical/002_Files/001_FileTests.rb:109–135` |
| WP16-R01 | CLOSED | WP16:100、170–172 恢复淡入中守卫、正/非正 duration 分支、旧粒子基础阶段 1–3、time_shift 与完成条件；在途过渡收到零 duration 新请求的场景正确。对应 `S/012_Overworld/001_Overworld visuals/001_Overworld_Weather.rb:11–23,66–95,425–428,446–477` |
| WP16-R02 | 继承 CLOSED | WP16:101、173 已明确对象稳定为 Rain 的前提；screen 上限变化不绕过调用者的类型差异判断。对应 `S/005_Sprites/006_Spriteset_Global.rb:33–38`、`S/004_Game classes/001_Game_Screen.rb:65–70` |

三个原剩余项的已接受主体、相关摘要及新增场景未出现相反的新规则。WP14 的无异常结论限定为已到达摆放阶段且先前操作正常完成，不扩大为整个地图建立过程不会抛错。WP15 的查询对照使用合法物种/整数形态输入；缺形态键与缺资源仍按不同条件处理。WP16 的零 duration 立即分支须满足同段明确列出的入口守卫；None 的 time_shift=2 与其他无叠层天气的 time_shift=1 是互斥选择。

## 3. 分包批准范围与保留限制

| 包 | 判定 | 本次闭合后的限定范围 |
| --- | --- | --- |
| WP14 | PASS_SCOPED | 继承首轮已接受的生成触发/输入、尺寸、布局/墙体/图块化与随机来源目录；闭合已述事件/玩家摆放及最终失败分支 |
| WP15 | PASS_SCOPED | 继承首轮已接受的资源路径、训练家/道具、缓存/音频等已述范围；闭合直接图像与专门入口的形态查询、候选回退及缺失结果 |
| WP16 | PASS_SCOPED | 继承首轮已接受的世界绘制与视觉入口范围；闭合天气调用条件、正/非正 duration、在途守卫及已述固定阶段；WP15 的未改资源子范围引用传播可接受 |

这是有限静态审查结论，不是所有参数组合、全部资源入口或整游戏的完备性保证。WP14 实际地图、最终可达性与跨实现种子复现；WP15 动画位图逐入口未决行为、实际媒体和宿主输出；WP16 动态阴影创建者、完整天气消费者及实际视觉效果，继续按各包未决项及前向依赖记录。U01–U10、WP78/79/80 出口不因本批闭合而自动完成。

## 4. 非阻塞维护与登记

**WP15-C01（非阻塞）**：WP15:168 的旧“全缺失”例仍简写“蛋类回退 000 图”。第 65、142、171 行已明确通用候选也可 nil，本轮按这些明确规则批准；可随 Reviewed 回填把该旧例收紧为“尝试相应通用候选，通用候选也缺失则 nil”，消除对文件存在性的暗示。无需因此新增一轮全文复审。

三包当前磁盘状态仍为 ReviewPending。提取方可依据本报告回填：WP14 对应 F04-06；WP15 对应 F02-04、F05-01、F05-02；WP16 对应 F05-03、F05-04。只将获批子范围登记 Reviewed，保留 Inventoried/未决前向范围。WP16 的依赖状态可同步为 WP15 限定 Reviewed，历史 `1aa30467` 来源记录保留。

回填后保留本报告的 v3 被审完整哈希、回填后完整哈希及实际 diff，不把新字节冒称本报告全文检查过的版本。纯管理性变化和上述维护可以与 WP17 同轮交付，不再等待单独确认。

## 5. 下一步

**可开始 WP17（消息、窗口与输入，F05-05/F05-06）。** 计划声明依赖 WP08、WP15 的相关限定范围已具备；对未闭合组合继续记录前向引用。按此前约定，本次只给 WP17 执行提示，不附带启动 WP18 或其他包。

可直接交给提取模型的任务见 [next-batch-prompt.md](/Users/dingshinn/Desktop/pokemon-framework-reference/review/wp14-wp16-closure-review-2026-09-23/next-batch-prompt.md)。本 reviewer 仅新建独立报告、检查、快照和提示词，未代做状态回填、未执行 WP17。最终输入稳定性和本轮产物哈希见 `final-checks.json`。
