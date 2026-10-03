# WP43／WP44／WP45交付摘要 v2（WP43回填、N01同步与三项有限修订）

日期：2026-09-27（Asia/Shanghai）。提取方材料，非独立review、非WP80 sanitized产物。reference固定commit `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`，全程只读；未运行参考过程／游戏／真实网络。

**本轮依据**：[首审报告](../wp43-wp45-review-2026-09-27/report.md)与[权威有限修订提示](../wp43-wp45-review-2026-09-27/revision-prompt.md)。独立结论：批次REQUEST_CHANGES；**WP43本体PASS_SCOPED**；WP44-R01/R02、WP45-R01三项必修；N01反例CONFIRMED，要求定点同步WP40；C01两处维护。现已完成所列回填与有限修订，实际修订尚待复核，不进入下一批。

**版本记录**：v1为本批首稿与WP39–41管理回填交付，完整原声明留在本轮input-snapshot；其“覆盖齐全／自检通过”不代替复杂行为验收。v2更正上述三项、同步N01及C01，保留已支持范围、原114／31／23审计集合及67条普通参数数据。旧报告、回应、差异和快照不倒写。

## 1. 固定输入与历史回填

七件必检（四新产物、矩阵、manifest、摘要），另补WP40、WP41、self、boundary、主TSV，共十二件逐一实测完整SHA-256／字节并与本轮input-snapshot逐字节比较，全部MATCH。

此前WP39／40／41管理回填已被本轮独立接受，原12项与C03关闭保留；原回填回应和五份差异继续留史：[backfill-response.md](backfill-response.md)、[backfill-diffs](backfill-diffs/)。本轮WP40的N01是**证据导致的局部行为简写修订**，不能把它重新叫作纯管理回填；WP41仅同步其上游身份，不改行为。

当前限定通过集合为 **WP01–WP21、WP24–WP31、WP33–WP36、WP39–WP41、WP43、WP59–WP60**。WP40既有限定Reviewed保留，N01实际修订／传播另待本轮复核；WP44主稿／附表与WP45保持ReviewPending。

## 2. 本轮当前产物（全部实测）

| 产物 | 完整SHA-256 | 字节 | 身份与范围 |
| --- | --- | ---: | --- |
| `specs/combat/wp40-commands-obedience-and-action-order.md` | `ad4718722897ef448623fb2bdcd7e9e8ca9a51538a5015edc331fcae50516654` | 42,476 | 既有限定Reviewed保留；N01定点校准，实际差异待复核 |
| `specs/combat/wp41-switching-positioning-and-escape.md` | `42878fac04b7ba5e195663f183fb484489200bab8ef5dc17333b0c0525b14085` | 31,939 | 已限定通过；仅WP40完整哈希管理级联 |
| `specs/pokemon-rules/wp43-types-accuracy-and-damage.md` | `0cd9958c256ef2caf7d6f9933127f35e5644131a3a97ed79d46998c6bcc15688` | 30,543 | 首审A～F PASS_SCOPED后管理性回填；基础计算与已接受数值不重写 |
| `specs/pokemon-rules/wp44-statuses-stat-stages-and-immunities.md` | `85e17c6c15225040eb5dd5f38503bbcac6c8fd96916f40270e3c989e86559311` | 49,950 | ReviewPending，R01/R02与C01首审修订v2 |
| `specs/pokemon-rules/wp44-effect-coverage.md` | `47bd80e20c877e612bb99e6929cf46b2efe7d87d94862760e9871234eecac3ef` | 27,133 | ReviewPending，v2精确合同锚点／多项镜甲索引；集合保持 |
| `specs/combat/wp45-weather-terrain-side-and-position-effects.md` | `f92b0f3cfa807d0c9a069fb586cde3673f878d4762dbede3425b08b86f06f35b` | 35,823 | ReviewPending，R01与C01首审修订v2及上游级联 |

修订前／被审身份留史（不冒充当前稿）：

| 产物 | 完整SHA-256 | 字节 |
| --- | --- | ---: |
| wp40-commands-obedience-and-action-order | `07789951f9aaaa7cac82508218a3f58c76caa735e18e4fad9f9a2dcd123a80d3` | 40,547 |
| wp41-switching-positioning-and-escape | `e6b835af5db676a28b80e7fb1513cf379267b2cdab427c7e9cc916e8e8a4c234` | 31,897 |
| wp43-types-accuracy-and-damage | `6021d835ebd2b62eac63062c5475e53501b5e6d46ff94873f2284799cf11ef0e` | 29,511 |
| wp44-statuses-stat-stages-and-immunities | `b7eae260636adef8e1e301737765c5ab396216f481086aecaab0c42857a1cf67` | 35,014 |
| wp44-effect-coverage | `ea5237d3257e1326876d3aae8d36c9bac003eb9682ad7402b05bc02797b45e39` | 24,809 |
| wp45-weather-terrain-side-and-position-effects | `2fbe3b6586b41214f02a8e1ec59257dad5dd740f5ce882279497e388f7a8afab` | 34,109 |

级联顺序：WP40 N01→WP41必要引用同步→WP43回填及引用→WP44主稿／附表v2→WP45v2。当前10条受影响完整哈希绑定均实测匹配；WP43被审首版、回填后版本与WP44／45尚未外审修订稿明确分开。

## 3. 指定编号的实际修订

| 编号 | 回源后修订 | 静态验收／保留边界 |
| --- | --- | --- |
| BATCH-N01 | WP40§5.3去掉一方无防守即命中的保证；无防守／未来攻击／帮助只在该层放开相应半无敌，普通处理器门引用WP43。WP43改为本轮确认记录 | 普通q70、0阶，模式破坏者开且目标无防守：r69命中／r70失败；关则普通目标处理器可设基础命中0。旧两标志／PP合同与旧12项不重开 |
| WP44-R01 | 主文§7.1新增K01–K22完整参数／分支表；16泛化项、破壳与五集合族在附表逐项链接稳定锚点；67条普通参数保持 | 重力基底81→121先截断、青草61→31先四舍五入且无额外接地门；忽略替身降攻；破壳五项请求和次序；五集合族的对象、项目、量、部分成功及UserSide直接遍历 |
| WP44-R02 | 改写中央模式破坏者保证，新增§5.3区分普通多项／毒液陷阱招式预检与中央镜甲反射；索引与失败摘要同步 | 模式破坏开，来源攻特攻−6→多项预检放弃；来源0→目标−1／−1不反射；普通单项不带该预检。未给reference补不存在的门 |
| WP45-R01 | 目录、§7.2、失败摘要及S06/S07补最后行动检查与保护计数写入 | 世代8计数9且无其它未动UseMove／Shift：免抽签但失败、计数1、侧标记假；有合格者且其它门过：成功设真、9→27 |
| BATCH-C01 | WP44仅statusCount>0的剧毒递增Toxic；WP45取证尾数改为实际781 | 普通毒Toxic0保持0；已支持毒疗／魔法防守数值、44项范围和尾部生命周期不重开 |

详见本审查目录新增 [revision-response.md](../wp43-wp45-review-2026-09-27/revision-response.md) 与 [revision-diffs](../wp43-wp45-review-2026-09-27/revision-diffs/)（10份，以本轮快照为基准；含self／boundary）。

## 4. 自检与五组交界

[self-checks.json](self-checks.json)与[boundary-checks.json](boundary-checks.json)更新为v2，revision_history明确旧声明语境。本轮只定点回读13个源文件并核对固定commit字节；首稿44源数据身份／全文范围作为继承证据，不冒称本轮全文重读。

- 审计集合和起始行保持：114阶级项、31状态项、23前向项；67条普通参数的对象／量不变。22条精确合同锚点与三处多项预检链接已核对。
- 当前三新包有92条具名静态场景（WP43 21、WP44 40、WP45 31），另有WP40 N01两条对照；向量数不是行为审查通过数。
- 本轮3项新增独立算术实测：floor(81×3/2)=121、正值round(61/2)=31、9×3=27。没有运行或转译参考过程。
- 五组交界维持：计算与个体／阶段、状态与写回／计算、天气作用域与世界／位置、向WP42/46–50移交、追踪一致性。R01基底替代不改WP43公式，R02两层镜甲不合并，R01保护免抽签不合并为免失败。

全部修订自检为提取侧结果；WP43的Reviewed来自独立授权，WP44／45不得由自检升级。最终全量清单／链接／JSON／快照核验在登记完成后实测，由交付消息报告。

## 5. 矩阵与登记

F12-01仅WP43 A～F子范围回填Reviewed＋前向Inventoried；F12-02/03维持ReviewPending，具名登记R01/R02或R01已修订为v2、待复审。N01追踪说明同步；F11-06/07及其它Feature未动。

manifest第四十九轮更新§1／§2.1／§3／§4，补登本轮reviewer材料12份；主TSV沿用更新为v24，不丢原353条。新增本轮回应与10份差异，旧审查／回应／快照保留；预计增加23条，以最终实测为准。

## 6. 交付材料身份

| 材料 | 完整SHA-256 | 字节 |
| --- | --- | ---: |
| `planning/feature-matrix.md` | `b230d1d7840b31923c741d439c2344990c18e00108a45801fdc45b6fd5078cc7` | 47,092 |
| `review/wp43-wp45-delivery-2026-09-27/self-checks.json` | `307d1ff0d54d9c1ddbcf8ee10f6161e6eff044cb5d486352b3acab643313004d` | 56,423 |
| `review/wp43-wp45-delivery-2026-09-27/boundary-checks.json` | `21abfe14138ed5e2fcd5ba3d3f0b499d192326e970c4495a905fcafa0098ac4e` | 6,629 |

上述三件被审v1身份保留：

| 材料 | 被审v1完整SHA-256 | 字节 |
| --- | --- | ---: |
| `planning/feature-matrix.md` | `bf77403c9b402f55830a0db482006465d9b74e0e798ab758c80f204e33ab1661` | 47,030 |
| `review/wp43-wp45-delivery-2026-09-27/delivery-summary.md` | `96b9abf484d4eafa958b81f41c4755ff250e19c240804577a74236eed3027619` | 8,597 |
| `review/wp43-wp45-delivery-2026-09-27/self-checks.json` | `3c1259dd3f8966282b7880de4bee02b8c7a5bcd8640ed6dae8e729dc6b841113` | 40,415 |
| `review/wp43-wp45-delivery-2026-09-27/boundary-checks.json` | `c20c3cbcf1e0488f899ab8ff389635543efc49a5499f58741456ad481200687a` | 4,122 |

本摘要、manifest／TSV不自哈希；摘要由外部清单固定，manifest／TSV最终完整哈希与字节在交付消息报告。修订差异与回应的完整身份登记于新轮次，不覆盖任何reviewer原件。

## 7. 停止点

**仅送WP44-R01/R02、WP45-R01、BATCH-N01、C01与直接传播有限复审后停止**；不重做WP43基础计算首审，不启动下一批或WP22／23／32／37／38／42／46等其它包。WP44主稿／附表与WP45保持ReviewPending。

未向reviewer发消息，未创建其它任务／并行Agent，未提交／推送；未操作真实地图／存档／输入。Demo、宿主、媒体、插件、U01–U10及WP78→WP79→WP80阶段出口保留。
