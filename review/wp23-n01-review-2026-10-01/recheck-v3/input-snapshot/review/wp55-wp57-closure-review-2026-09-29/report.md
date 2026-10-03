# WP55／WP56／WP57 闭合短复审报告

2026-09-29；独立 reviewer。reference固定commit `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`，只读静态取证。

**结论：PASS_SCOPED。WP55-R02、WP56-R04剩余点及C03全部CLOSED；WP57管理性回填接受。原13项必修至此全部关闭，可以回填WP55／56限定Reviewed，再执行WP58→WP62→WP38三包。**

本轮没有重做首审、重开已关闭11项或重复数值测试；只检查两处剩余、C03、WP57回填和直接传播。提取侧回应是提交声明，本结论来自本轮实际固定字节、差异及定点源码复核。未运行参考或游戏，未代执行回填／下一批。

## 1. 本轮固定版本

| 对象 | 完整SHA-256 | 字节 |
| --- | --- | ---: |
| WP55主稿v3 | `b0c2c8b6a28238adff0f76d94dd3e9a1be2e2231999d981a3cf4915a37375b80` | 28,625 |
| WP56主稿v3 | `700e478823ba123af65176d3d29378327000206d6f11c1250aec933ab09f8b4d` | 22,011 |
| WP57主稿，回填后 | `7280bc3061aef6af62b69b09e81a094f21f172be0222bb905bac01cee6aaeefc` | 15,610 |
| feature-matrix | `e5eeb446f2c3c91557cbdd96cbc93d88bb419389dabf7de6dc822464c5601ff9` | 51,922 |
| manifest | `4f965681f9a1800504cb0904fe36a0d318c2a3d1e55371efae107ba199eae60e` | 400,252 |
| 本批摘要v3 | `98637c38d0e7dc4b3a41ace945cdd602d1398573d78daadb3992da3a500009f0` | 7,648 |
| 本批self v3 | `4c739cb0836dbc67adb1e1d026caa56d1c9004ef1e2487694f1fd37733152e17` | 20,980 |
| 本批boundary v3 | `30bebc0ead4b8c4fd9ac518388d3d58de0520cc90d151f064759d09b351ddd44` | 8,923 |
| 主TSV v34 | `c6904ac3f5d94c3eb3423e0dfc20da56f302b2769f84bd5b9117cd7232a64b0a` | 90,335 |

固定755项输入，全部路径与完整身份在 [current-hashes.tsv](current-hashes.tsv)、[input-manifest.json](input-manifest.json)，副本在 [input-snapshot/](input-snapshot/)。manifest753条可核身份与TSV657条匹配；两个“见原件”占位不计作完整身份。相对上轮734项，只有9个原有文件变化（七个diff目标及manifest／TSV），见 [changes-from-v2.diff](changes-from-v2.diff)。

## 2. 剩余点与维护闭合

### WP55-R02 — CLOSED

被审WP55为上表完整哈希。第46行已准确列出进行中提交、开始有报名时替换、取消有原队伍时恢复、结束无条件写字段值四入口及守卫，原排他保证已经删除。

本轮回读 `018_Alternate battle modes/001_Battle Frontier/001_Challenge_BattleChallenge.rb:200–203,225–229,270–282`，与该总述及已正确的§2.3一致。静态对照原队伍P、报名Q且P≠Q：开始写Q，取消恢复P；总述允许两次赋值。空列表／nil、未开始结束置nil、保存分层等已接受范围未改。

### WP56-R04 — CLOSED

被审WP56为上表完整哈希。第121行现在区分共用成功状态与Arena专用裁判累计：普通战斗建立／更新／结算；Palace沿同一路径；Arena额外将当前skill槽用于裁判。

本轮回读（均相对`reference/pokemon-essentials/Data/Scripts/`）：

- `011_Battle/008_Other battle types/003_BattlePalaceBattle.rb:4–5,61–65,160–164`；
- `011_Battle/001_Battle/002_Battle_StartAndEnd.rb:109–118`；
- `011_Battle/001_Battle/010_Battle_AttackPhase.rb:176–184`；
- `011_Battle/002_Battler/007_Battler_UseMove.rb:239–252,431–438,512–520`；
- `011_Battle/008_Other battle types/004_BattleArenaBattle.rb:127–133`。

正常Palace合法招式、无提前返回且到达共用结算入口，确实会更新／结算SuccessState；没有Arena裁判技分累计。未用“无力−2”个案否定整个模式。覆盖赋值、protected保持、早返与既有评分向量保持不变。

### BATCH-C03 — CLOSED

- WP55 W28（第192行）现在具名“报名包装接收到ret=[]”，false来自`002_Challenge_Data.rb:38–49`包装转换，不再与直接setParty返回混同；不声称普通多选UI可达。
- WP57第63行把异常退出与整体校验持续重试未返回分开，与ChooseFoes:144–164一致；临时人数未还原边界、881端点与数据表未变。
- 新提取侧回应已更正旧回应的setParty来源为`001_Challenge_BattleChallenge.rb:200–203`；旧回应原件保留。

上一轮关闭的11项、C01及继承C02继续关闭，不重复审查。原13项行为必修现在无剩余。

## 3. 回填及独立检查

**WP57管理性回填ACCEPTED。** 头尾和F13-05仅登记其已批准A～F子范围；C03维护及对WP55实际v3身份的更新符合授权；被审v2 `7e69ccdccb422d1b04799990041a3745d747ebab3a765b8f7d686ad4f270ef8b`／14,776字节留史，当前回填后字节没有伪称为上轮被审对象。WP57的17条场景未变。

| 独立核对 | 结果 |
| --- | --- |
| 清单身份 | manifest753／TSV657完整哈希、字节、短标签一致；无缺失／重复；原路径顺序保留，新增21项集合一致 |
| 提交差异 | 七份diff均可从本轮前一快照逐块在内存重建到当前字节 |
| 场景 | 34／27／17保持；仅W28按C03更正入口／返回记法，其他77行原样 |
| 当前依赖 | boundary13条、三稿内嵌13条完整身份匹配；当前self的38条声明身份匹配 |
| 旧C02 | artifacts／packages与向量继续一致，无残留回归 |
| 文本完整性 | 201份已登记JSON可解析；当前specs＋矩阵384条相对链接存在。范围与提取侧355份／119条不同，不混用计数 |
| 旧件保护 | 734／707／677／644／613／589／548／521八轮快照及各自已列reviewer artifacts匹配 |
| reference | 33个相关源／数据文件与固定commit和上轮字节一致；本轮新读8个路径；HEAD正确，普通Git状态为空 |

证据在 [diff-checks.json](diff-checks.json)、[propagation-checks.json](propagation-checks.json)、[current-self-checks.json](current-self-checks.json)、[identity-checks.json](identity-checks.json)、[source-checks.json](source-checks.json)、[static-checks.json](static-checks.json)。工具只做自有文本／字节／集合检查；未调用提取侧检查脚本，未执行参考表达式、解释器、生成器、编译器或真实运行。已闭合且无变化的数值向量不重复扩大测试。

## 4. WP55／56管理回填授权

允许提取方先按本报告将两主稿头部／尾部及F13-04对应子范围管理回填 **Reviewed（限定静态范围，2026-09-29闭合短复审PASS_SCOPED；管理性回填）**。

- **WP55范围**：A～F挑战身份／即时注册与记录查询、会话状态与显式推进、对手与内容／个体创建、队伍引用替换／恢复、暂停／继续／取消／结束、保存返回／异常／不终止及具名边界，及已述单场交界。
- **WP56范围**：A～F Palace原始数据与实际抽样门、菜单分流／自动选招、Pinch与AI换人；Arena心分／成功状态／技槽／体分／2/0评判、HP提交／顺序补位、差异及已述裁判显示接点。

保留本轮被审WP55 v3、WP56 v3完整哈希和差异，回填后新身份另列，不冒充本轮被审字节。只同步必要上游状态／身份、WP57引用和活动材料，不改已接受行为。历史“待审／仅剩两项”留在明确历史语境。WP57回填已接受，不需重做其行为。

回填后限定通过集合：**WP01–WP21、WP24–WP31、WP33–WP36、WP39–WP52（WP47=A/B、WP52=A/B/C）、WP54–WP57、WP59–WP60**。WP53、WP58等未完成；F13-04／05仍保留设施完整演出、接待事件、运行和其它前向范围。

## 5. 下一批：WP58→WP62→WP38

按当前`planning/extraction-plan.md`第134、143、106行的依赖安排三包。WP58承接本轮设施与变体；WP62先建立图鉴主合同，再供捕获WP38使用，避免跳过其明确依赖。

| 顺序 | 包与Feature | 计划依赖及当前适用性 |
| --- | --- | --- |
| 1 | WP58 记录／回放，F13-06 | WP06、WP42、WP55、WP56；本轮回填后均有可引用的限定通过范围 |
| 2 | WP62 图鉴记录与内容规则，F15-01 | WP18、WP21、WP24、WP03、WP11、WP36；均已有相关限定通过范围 |
| 3 | WP38 捕获判定与接收策略，F10-06 | WP20、WP25、WP27、WP30、WP39、WP42已有；WP62先自检固定，按“批内固定版本，尚未外审”引用 |

本顺序不代表编号必须连续，也不改变计划依赖。WP62记录写入与WP38捕获流程各自保留唯一主规则和清晰调用顺序；跨包读取不制造反向硬依赖。新三包均保持ReviewPending，串行自检、固定身份，批末统一外审，不自动执行第四包。

可直接转交的文本见 [next-batch-prompt.md](next-batch-prompt.md)。本报告不预批WP58／62／38的内容；此reviewer会话只交报告和提示，不代执行新批次。

## 6. 保留与停止

本轮新证据只支持固定快照的静态范围，旧审查与提取侧声明分别记账。Demo、宿主、媒体、插件、U01–U10、真实地图／存档／输入／网络、随机重放与跨版本等价、WP78→WP79→WP80全部保留。未因设施三包闭合宣称可运行或全局覆盖完成。

本会话仅在本新review目录创建报告、检查、快照和提示；未改规格／矩阵／manifest／reference，未回填、未启动新包、未创建任务／Agent、未发消息、未提交／推送。
