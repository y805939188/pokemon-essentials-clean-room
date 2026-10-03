# WP42／WP48／WP49首审有限修订回应 v2

日期2026-09-27，提取／修订方。依据[独立报告](report.md)和[权威有限修订提示](revision-prompt.md)，已亲自回源核实三个原编号及BATCH-C01并完成有限修订；以下为提取侧静态验收，**三包继续ReviewPending，不自批Reviewed**。旧WP44／45回填和N01 CLOSED已被接受，未重开。

## 1. 固定预检与版本

六件必检与self／boundary／主TSV三件补检均实测完整SHA-256和stat字节，与本轮input-snapshot逐字节一致。被审首稿身份如下，新稿不冒充已审。

| 对象 | 被审v1完整SHA-256 | 字节 | 快照 |
| --- | --- | ---: | --- |
| `specs/combat/wp42-growth-end-of-round-and-battle-outcomes.md` | `9bde1314b9b96f36fa243abfd0ca965775dd651c7861e0f20f475d5f83d97161` | 37,859 | MATCH |
| `specs/pokemon-rules/wp48-ability-calculation-modifiers.md` | `480016af9731a97607300ae84851b6b6286ae624b1452a0193b849295f2b3728` | 34,233 | MATCH |
| `specs/combat/wp49-ability-phase-triggers.md` | `9286900834514d363d0e15b50aeefdd581c0b86b930c9cfe006421dcc470ca6d` | 50,601 | MATCH |
| `planning/feature-matrix.md` | `4234c91e8b2c3a8153e607709425b7ba89900462d069694e962f21206aa0bed2` | 48,137 | MATCH |
| `planning/review-manifest-2026-09-19.md` | `a74f4d0ca2d7259dc5fe21630034cf03a0ea02c1a65c193f69b05a27f951eff6` | 267,338 | MATCH |
| `review/wp42-wp48-wp49-delivery-2026-09-27/delivery-summary.md` | `c688fc9d509fa605b69dd4a29bc69e990f98668ed15ae83dd52f913844406f1a` | 5,577 | MATCH |
| `review/wp42-wp48-wp49-delivery-2026-09-27/self-checks.json` | `d7ffb5cdad8253c7f2b52f7419ece41786febe8984bf621179956bbdfbcf80c7` | 87,252 | MATCH |
| `review/wp42-wp48-wp49-delivery-2026-09-27/boundary-checks.json` | `d0eef5f44519273d94662ab9f8b1b334804ba8bdf97039af916dcee99c6eae34` | 9,704 | MATCH |
| `review/wp18-wp20-delivery-2026-09-26/current-hashes.tsv` | `cddd2914bd41389cc786de8970771e43e84fe87029d48e8f02733cc024103283` | 54,775 | MATCH |

## 2. WP42-R01 — 默认有序拾取数据

**回源结论**：世界开战文件`:654–749`确认普通18项、稀有11项，存在性过滤保序且保留重复后才取等级窗口；稀有DESTINYKNOT第7／9／11位不能去重。默认9普通位置权重合计98、两稀有位置各1。此前把完整内容表留在源码，确实不足以由规格独立推出输出。

**修改位置**：WP42§7.2补两张默认有序标识表、窗口位置／权重／整数区间表，删去“完整内容表见来源”的留白；§9新增E12/E13，§10数据要求同步。E11及原资格／过滤不足放弃、首抽9／10、采蜜独立抽取保持。

**静态验收**：规格表与源有序身份逐位置一致；25个不同身份在PBS章节标识全部存在。所有默认身份存在且首抽通过时，等级1的第二抽98／99为HYPERPOTION／NUGGET；等级91为LEFTOVERS／DESTINYKNOT。只做文本／集合和独立权重加法，不执行拾取函数、随机或转换参考过程。

**保留边界**：仅补自有输出数据，不提取物品使用效果或完整WP50／61；WP42其余成长、27阶段、终局与异常正文直接回归保持。

## 3. WP48-R01 — 整数命中阈值

**回源结论**：能力目录`:1123–1137`两次VICTORYSTAR各乘1.1；命中计算`:109–123`先把命中／闪避分别四舍五入成整数，再以整数q取最终整数商，并严格小于比较。WP43§4.2原主规则正确，不修改。

**修改位置**：WP48§4.2明确整数阈值交界，§9 C06补完整共同前提并替换错误边界；self当前C06向量、倍率算术与阈值算术同步，旧错误声明只留在明确撤销的revision_history。

**静态验收**：独立有理数1.1×1.1=121/100；命中整数121、闪避100，80×121整除100得96。固定r95命中、r96和r97失败；排除亲密、其它修正与提前必中。没有继续用浮点比值验证随机边界。其它22条向量及148身份审计表保持。

**保留边界**：N01、普通／不可忽略能力门、P/A/D/F参数与已正确向量保留；不重提取整族、不改已审WP43公式。

## 4. WP49-R01 — 存活场上人数门

**回源结论**：能力目录`:367–408`野生分支使用同侧场上计数，Battle`:458–460,474–475`以非空、未濒死且同侧集合计数；`:204–206`的名义规模是另一输入。WIMPOUT复制同合同；该额外人数门只针对敌方拥有者，随后仍查能否逃跑。

**修改位置**：WP49§5.1删去多人席规模概括，明确拥有者／其它存活成员计入、已倒下／空位／后备不计、玩家侧不加此门；H03改同一野生双席布局的两活／一活对照。self／boundary退出交界同步；只引用既有WP41，不重写其逃跑主规则。

**静态验收**：拥有者跨半标记和有效能力、无天空摔投、其它逃跑资格过：两名敌方存活场上者返回假；另一名倒下后计数1，人数门不拒，后续决定3并返回真。手工集合与控制流核对，没有执行退出或换人。

**保留边界**：训练家分支、其它逃跑守卫、回合末只离场而后补位、每击和后段时点不变；不能由人数门通过推导无条件必逃。

## 5. BATCH-C01 — 两处维护

**回源结论／修改位置**：能力目录`:2436–2464`确认MOODY先收可升／可降集合；E03改合法阶级攻击0、其余四项＋6，主算法不改。`:2820–2848`和AbilityAndItem`:62–70`确认ICEFACE不查switch_in真、IMPOSTER才查，§3.3改为入场回调并补默认假标志；L02加入气体结束时的ICEFACE对照。

**静态验收**：MOODY预降五项，升攻击＋2后移除攻击，剩四项，固定第二抽选防御使＋6→＋5，其余不变；并非仅防御可降。气体结束回调的ICEFACE拥有者存活非变身、EISCUE形态1、有效冰雹时可1→0；IMPOSTER在假标志时不变身。

**保留边界**：不扩展完整形态域，保留通用形态提交门；首稿其余生命周期与具名快照差异保持。

## 6. 修订后固定与直接回归

按WP42→WP48→WP49逐包写入后立即实测固定；WP49当前引用两上游完整v2身份并注明批内修订稿、尚未外审，旧v1身份留史。

| 文件 | 当前v2完整SHA-256 | 字节 |
| --- | --- | ---: |
| `specs/combat/wp42-growth-end-of-round-and-battle-outcomes.md` | `6644c77775b1e02481674079c847652dbbf2c566214d3969f1f333f741c22f7d` | 41,329 |
| `specs/pokemon-rules/wp48-ability-calculation-modifiers.md` | `87e39127e14eddd10f6e0d10e6d63999e0cb9ff70fa0e2505dc97a195f3b3bb8` | 35,021 |
| `specs/combat/wp49-ability-phase-triggers.md` | `7a4ecf931a65931cd8c6255d09b2697f83a5b538da907a016e5712efa32a67d7` | 52,573 |
| `planning/feature-matrix.md` | `6d9a28754bd2cfb3622a8a6dbf6b624600fd8c45aa34db570dc111f57c455a20` | 48,271 |
| `review/wp42-wp48-wp49-delivery-2026-09-27/self-checks.json` | `939f7e366b0c75feb45275e5ee340647715499cde96144b22bb78273925864e3` | 102,908 |
| `review/wp42-wp48-wp49-delivery-2026-09-27/boundary-checks.json` | `9509999c8dadeba83dfeceb39fd4d45d7d0b1494e1837abed8f01163792a309b` | 14,399 |

直接回归：WP42原29场景及§3～7.1、§8保持；WP48除C06外22向量及§5～8保持；WP49除L02/H03/E03外28向量及§6～9保持；能力263条审计行和267展开身份集合不变。旧已审WP41／43等没有修改。8个源／数据文件仅按上述实际区间回读／身份检索，并与固定commit blob核对；原26源范围是继承证据，未冒称本轮全文重读。

新增[revision-diffs](revision-diffs/)七份，相对本轮input-snapshot（三规格、矩阵、摘要、self、boundary）。旧backfill回应／八差异只表示首稿管理回填历史，不倒写成v2差异。详见[交付摘要v2](../wp42-wp48-wp49-delivery-2026-09-27/delivery-summary.md)；manifest第五十一轮、主TSV v26保留旧行和完整版本链，补登本轮reviewer12件。最终全量身份／集合／链接／JSON／快照与reference检查在登记结束后实测，由交付消息报告；manifest／TSV不自哈希。

## 7. 停止与保留

**只送WP42-R01、WP48-R01、WP49-R01、BATCH-C01及直接传播有限复审，然后停止**。三包及矩阵相应子范围保持ReviewPending＋前向Inventoried。限定通过集合仍为WP01–WP21、WP24–WP31、WP33–WP36、WP39–WP41、WP43–WP45、WP59–WP60。

未运行游戏、参考Ruby／表达式／解释器／生成器／编译器／转换器／插件／真实网络；reference只读、没有实现框架；未操作真实地图／存档／输入。未创建任务／Agent、未发reviewer消息、未提交／推送。未启动第四包；Demo／宿主／媒体／插件／U01–U10与WP78→79→80继续保留。
