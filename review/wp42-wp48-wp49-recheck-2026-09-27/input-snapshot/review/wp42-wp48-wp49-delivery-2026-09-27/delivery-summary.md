# WP42→WP48→WP49交付摘要 v2（首审三项有限修订）

日期2026-09-27；提取侧静态规格，非独立review、非最终sanitized产物。新三包均**ReviewPending（各自具名范围）**，首审修订后仅送原编号及直接传播复审；没有外审通过声明。

**本轮依据**：[首审报告](../wp42-wp48-wp49-review-2026-09-27/report.md)与[有限修订提示](../wp42-wp48-wp49-review-2026-09-27/revision-prompt.md)。REQUEST_CHANGES：WP42-R01、WP48-R01、WP49-R01；C01两处维护。已全部定点回源修订为v2，尚待独立有限复审。

**版本记录**：v1为本批首稿与旧批管理回填，首稿覆盖／自检声明不代替行为验收；v2补拾取默认数据、整数命中边界、存活人数门及C01，保留其它已支持范围。被审v1完整身份和旧错误自检的历史语境保留，reviewer原件／快照不改。

## 1. 管理收尾与输入

[回填回应](backfill-response.md)记录八必检＋两补检、WP44／45限定Reviewed及N01 CLOSED；[8份差异](backfill-diffs/)相对本轮闭合快照，旧报告／checks／快照未改。授权来自[独立闭合报告](../wp43-wp45-recheck-2026-09-27/report.md)和[下一批提示](../wp43-wp45-recheck-2026-09-27/next-batch-prompt.md)。本轮首审已接受上述旧管理回填；旧backfill材料只重建v1时点，不能当v2差异。本轮六件必检＋self／boundary／主TSV三补检全部与本轮快照一致。管理通过集合为WP01–WP21、WP24–WP31、WP33–WP36、WP39–WP41、WP43–WP45、WP59–WP60；不连续包含WP42。

## 2. 串行固定的新三包

| 包／文件 | 完整SHA-256 | 字节 | 自身范围 |
| --- | --- | ---: | --- |
| [wp42-growth-end-of-round-and-battle-outcomes](../../specs/combat/wp42-growth-end-of-round-and-battle-outcomes.md) | `6644c77775b1e02481674079c847652dbbf2c566214d3969f1f333f741c22f7d` | 41,329 | A～E成长触发／场上同步、回合末27阶段／早退、正常结果与世界交接、显式中止／异常 |
| [wp48-ability-calculation-modifiers](../../specs/pokemon-rules/wp48-ability-calculation-modifiers.md) | `87e39127e14eddd10f6e0d10e6d63999e0cb9ff70fa0e2505dc97a195f3b3bb8` | 35,021 | A～E计算／免疫／有效性27族，倍率／分支／副作用；148展开身份 |
| [wp49-ability-phase-triggers](../../specs/combat/wp49-ability-phase-triggers.md) | `7a4ecf931a65931cd8c6255d09b2697f83a5b538da907a016e5712efa32a67d7` | 52,573 | A～F阶段21族与直接生命周期，排序／失能／连锁／物品取得接点；119展开身份 |

WP42→WP48→WP49依次固定v2；WP49绑定前两包当前完整哈希，注明“批内修订稿v2，尚未外审”。完成依赖已审范围按各包版本表引用；包内责任与前向扩展分别记录，没有以目录名称代替参数。


被审首稿v1留史（不冒充当前稿）：

| 文件 | v1完整SHA-256 | 字节 |
| --- | --- | ---: |
| `specs/combat/wp42-growth-end-of-round-and-battle-outcomes.md` | `9bde1314b9b96f36fa243abfd0ca965775dd651c7861e0f20f475d5f83d97161` | 37,859 |
| `specs/pokemon-rules/wp48-ability-calculation-modifiers.md` | `480016af9731a97607300ae84851b6b6286ae624b1452a0193b849295f2b3728` | 34,233 |
| `specs/combat/wp49-ability-phase-triggers.md` | `9286900834514d363d0e15b50aeefdd581c0b86b930c9cfe006421dcc470ca6d` | 50,601 |

## 3. 主要行为与本轮有限修订

WP42区分成长提交、展示等待、场上副本回读；最大经验路径无场上刷新；回合末有缓存速度序／显式早退，火海双递减／青草先恢复保留。正常终局与显式中止、世界善后分别记账，持有物还原记录仍可更新。

WP48逐族给真实消费者资格与P/A/D/F量值；速度和重量的模式破坏者门不同，不可忽略状态／伤害／阶级也不等价。静默吸收免疫不提交升阶／回血，目标无防守保留N01已闭合边界。草之毛皮、硬爪、技术高手与钢之精神按固定快照参数。

WP49给每击／招式后段、能力获得失去、气体结束、濒死两遍、四回合末族和场地重复通知。新有界观察包括吐导弹先改形态再读分支、舞者资格失败不恢复预增暴走、预知梦150后被80覆盖；不是对已审主规则的静默改写。普通换下局部HP0、实际濒死与持久写回分层。

本轮修订：WP42§7.2给普通18／稀有11有序表、重复位置与9＋2权重，E12/E13独立推出等级1／91的98／99输出；WP48 C06命中121／闪避100，整数商96，r95命中、r96／97失败；WP49§5.1／H03仅野生敌方当前同侧存活场上数>1拒，双席布局一活可过此门。C01同步MOODY合法五项阶级和ICEFACE不要求真实入场标志，IMPOSTER仍要求。

详见本轮[revision-response.md](../wp42-wp48-wp49-review-2026-09-27/revision-response.md)与[七份revision-diffs](../wp42-wp48-wp49-review-2026-09-27/revision-diffs/)。

## 4. 提取侧自检与覆盖

[self-checks.json](self-checks.json)：31＋23＋31＝85条具名静态场景；当前17项算术记录，原未受影响部分继承，本轮纠正两个C06项并新增权重和。v1的83场景／16项算术及错误边界以revision_history留史。首稿26源身份范围继承，本轮8个源／数据路径定点回读或身份检索并与固定commit blob一致；身份检查不冒充全文读取。目录共48族、239直接＋24复制语句，展开267个（族，能力）身份；WP48 148、WP49 119，无重叠／重复；两空族明确。两稿263条审计行与v1逐字节一致，原登记／复制／起行集合回归保持。其它未改行为／向量按本轮回应所列直接回归，没有重做首审。

[boundary-checks.json](boundary-checks.json)记录五组交界：WP42×基础与已审战斗、WP48×数值与免疫、WP49×入离场和主阶段、48／49覆盖接缝、追踪／版本／未决。静态自检不替代独立行为审查。新稿链接、JSON、全量清单和快照保护在登记完成后重测，最终值由交付消息报告。

## 5. 登记与材料身份

矩阵F12-01/02/03回填与新批F11-06/07、F12-06增量分开；后者只ReviewPending＋前向Inventoried。本轮只更新F11-06/07、F12-06的具名修订状态；旧F12-01/02/03回填保持。manifest第五十一轮、主TSV v26保留旧499／403行，各新增本轮reviewer12件、revision-response与七份revision-diffs共20条。manifest不自哈希、主TSV不收自身；终值在交付消息实测报告。

| 配套材料 | 完整SHA-256 | 字节 |
| --- | --- | ---: |
| `planning/feature-matrix.md` | `6d9a28754bd2cfb3622a8a6dbf6b624600fd8c45aa34db570dc111f57c455a20` | 48,271 |
| `review/wp43-wp45-delivery-2026-09-27/delivery-summary.md` | `4cc8e434e1a7d1feca37dce2290626055fd41fbc8d3dc8215ddc1ef43960e35d` | 10,636 |
| `review/wp42-wp48-wp49-delivery-2026-09-27/backfill-response.md` | `7b99bc61584becf3e9850a1d16bad684add81899be06c44f94a6d268b976a7e2` | 4,642 |
| `review/wp42-wp48-wp49-delivery-2026-09-27/self-checks.json` | `939f7e366b0c75feb45275e5ee340647715499cde96144b22bb78273925864e3` | 102,908 |
| `review/wp42-wp48-wp49-delivery-2026-09-27/boundary-checks.json` | `9509999c8dadeba83dfeceb39fd4d45d7d0b1494e1837abed8f01163792a309b` | 14,399 |


被审v1交付／追踪材料留史：

| 文件 | v1完整SHA-256 | 字节 |
| --- | --- | ---: |
| `planning/feature-matrix.md` | `4234c91e8b2c3a8153e607709425b7ba89900462d069694e962f21206aa0bed2` | 48,137 |
| `review/wp42-wp48-wp49-delivery-2026-09-27/delivery-summary.md` | `c688fc9d509fa605b69dd4a29bc69e990f98668ed15ae83dd52f913844406f1a` | 5,577 |
| `review/wp42-wp48-wp49-delivery-2026-09-27/self-checks.json` | `d7ffb5cdad8253c7f2b52f7419ece41786febe8984bf621179956bbdfbcf80c7` | 87,252 |
| `review/wp42-wp48-wp49-delivery-2026-09-27/boundary-checks.json` | `d0eef5f44519273d94662ab9f8b1b334804ba8bdf97039af916dcee99c6eae34` | 9,704 |

## 6. 未决责任与停止点

运行、真实地图／事件／存档／输入、宿主媒体、插件和U01–U10未验证；WP22／23／32／37／38／46／47／50、AI／设施等完整域具名前向，WP78→79→80不进入。未运行参考Ruby／表达式／解释器／生成器／编译器／转换器／网络，未实现框架、设计具体API或复制源码进规格。

**只送WP42-R01、WP48-R01、WP49-R01、BATCH-C01与直接传播有限复审，然后停止**。WP44／45和N01旧管理收尾已被接受，不重做已关闭审查；不启动第四包，不创建任务／Agent，不向reviewer发消息，不提交／推送。
