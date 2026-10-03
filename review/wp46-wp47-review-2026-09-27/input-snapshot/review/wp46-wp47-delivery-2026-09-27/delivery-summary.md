# WP46 → WP47-A → WP47-B 交付摘要 v1

日期2026-09-27；提取侧规格与静态自检，非独立审查、非WP80 sanitized。三新包均**ReviewPending（各自具名范围）**，本批统一送审后停止。

## 1. 管理回填与范围

[回填回应](backfill-response.md)与[五份回填差异](backfill-diffs/)记录九项预检、WP42／48／49限定Reviewed和完整身份级联。授权为[独立复审报告](../wp42-wp48-wp49-recheck-2026-09-27/report.md)及[执行提示](../wp42-wp48-wp49-recheck-2026-09-27/next-batch-prompt.md)。被审v1／v2与回填后新字节分开；旧reviewer、快照与修订回应不修改。

限定通过集合＝WP01–WP21、WP24–WP31、WP33–WP36、WP39–WP45、WP48–WP49、WP59–WP60。WP46／47-A／47-B不在该集合中，WP47只是两包族简称，不另算第四包。

## 2. 新批完整固定身份

| 文件 | SHA-256 | 字节 | 责任 |
| --- | --- | ---: | --- |
| [wp46-damage-multihit-and-healing](../../specs/pokemon-rules/wp46-damage-multihit-and-healing.md) | `0e5a676e234a71a949602d93a2a6aeb4c26cf09acc894e47eee66eb3c1e8a323` | 47,352 | WP46 A～F伤害/多击/恢复主稿 |
| [wp46-damage-healing-coverage](../../specs/pokemon-rules/wp46-damage-healing-coverage.md) | `170e063faaea4b66b5e8a7fc0b9bba907ff7aba7b4c15d8f435ff50d51f7ce88` | 36,408 | WP46有界覆盖 |
| [wp47-a-move-attributes-targeting-and-calling](../../specs/combat/wp47-a-move-attributes-targeting-and-calling.md) | `ad6a6d6c4d5c90dbf32f5cd0c843a84dad605319ee4a99c1d5d3d04f8f57b49c` | 33,207 | WP47-A A～E属性/目标/调用主稿 |
| [wp47-a-attributes-targeting-calling-data](../../specs/combat/wp47-a-attributes-targeting-calling-data.md) | `1c164a68ed2d35c1dceaa9314038a9fe0f6a011c845a9adf512f740a466a898c` | 18,920 | WP47-A覆盖与完整默认数据 |
| [wp47-b-switching-control-and-item-changes](../../specs/combat/wp47-b-switching-control-and-item-changes.md) | `24185ce4179387c900b11e3505d9309f1869ba8587aa2bd263609f1eec25c0bd` | 37,934 | WP47-B A～F换人/控制/物品/能力主稿 |
| [wp47-b-control-items-coverage-data](../../specs/combat/wp47-b-control-items-coverage-data.md) | `3a092b6653b0d283a47e45aa4ed9b06b04ca62683a14b17b42048829bf00d83c` | 17,454 | WP47-B覆盖与完整默认数据 |

顺序为WP46先自检固定，再WP47-A，再WP47-B；同批引用完整哈希并注明尚未外审，已审输入引用当前管理维护版本。状态与矩阵只按具名范围，未扩大到所有战斗或运行组合。

## 3. 行为与数据交付

WP46闭合逐击资格／伤害／反应顺序、多击分布、两回合／连用、固定伤害／反击、威力／攻防替代、吸取／治疗／反伤／自损、蓄力与誓约。139个主身份，38场景。

WP47-A给当前类型与本次招式类型分层、命中／保护、执行目标与重定向、反射／抢夺、调用候选及真实PP对象、模仿与写生；55个主身份，29场景。附表完整列七调用／复制排除集合（并集63效果）、17石板／17存储碟／4卡带映射及67条自然之恩默认数据。

WP47-B给换人／逃离入口差异、接力保留集、拘束、先行／延后／号令／禁用、物品C/I/R/P/Belch写入、能力抑制／获得后置及浮空变身。60个主身份，35场景；附表完整号令32项／安可6＋6排除、不可移物组合、578项投掷默认威力。物品被动效果全集仍WP50。

## 4. 新具名观察，请随直接交界复核

- **WP47-B-N01**：撤退射击被反射后，外层实计击数可为0，末段仍拒换人；旧WP41反射换出摘要不能当无条件保证。源SwitchingActing:91–118／UseMove:403–505；主稿§8和S07。
- **WP47-B-N02**：号令实际传真实槽、specialUsage=false，前置过后耗PP并受普通状态／服从／命中；旧WP40步骤18“特殊使用”简写存在歧义。源UseMove:521–542；主稿§3.3／C01～C03。
- **BATCH-N03**：野生伤害拖出主效果读当前替身耐久，破替身至0后可置决定3；非野生拖出后段才查本击替身标记。与旧WP41“非替身”概括需定点对照。源SwitchingActing:228–255／UseMove:664–711；WP47-B S03。

三项均在新材料独立登记，旧WP40／41文件未修改；不是提取方推翻旧review结论，也不重开全部旧范围。本批自身合同依实际静态来源给定，请独立review判断旧摘要的后续修订范围。

## 5. 自检、交界与登记

[self-checks.json](self-checks.json)和[boundary-checks.json](boundary-checks.json)：三包102条场景、26项独立常数运算。八个效果文件314身份加内建挣扎1，联合315＝254个本批主身份＋61个已有主合同，无重叠主归属、无本有界集合未归属；已有61为WP43 1、WP44 29、WP45 31。只说明该有界范围，全球覆盖出口WP79未启动。身份／行号与默认字面数据的集合核对不替代具体行为验收。

五组交界覆盖伤害与阶段／数值，属性调用与原行动，换人／物品／持久状态，三包目录接缝，以及版本追踪。32源／数据文件实测哈希／字节与固定commit blob一致，实际阅读区间／仅数据检索各主稿列明，不冒称全文重审引擎。reference未修改，未运行或逐行转译参考处理器生成期望。

矩阵F11-06/07及F12-06为管理回填；F12-02/03只维护WP42状态语境；F12-04/05为新批ReviewPending＋前向Inventoried。manifest第五十二轮、主TSV v27保留旧519／423行并补登本轮reviewer12件与本批材料；实际全量计数／最终哈希在登记后实测报告。manifest不自哈希，TSV不收自身。

| 其它材料 | SHA-256 | 字节 |
| --- | --- | ---: |
| `planning/feature-matrix.md` | `9b0ac4a232ec2df4855f8ad31b32d9ef2d9511185d4384647f57c515b434efc8` | 48,848 |
| `review/wp42-wp48-wp49-delivery-2026-09-27/delivery-summary.md` | `498dde568f7c77c30c35d28e2ab492622b7c985c0243977683b54d184111f695` | 9,388 |
| `review/wp46-wp47-delivery-2026-09-27/backfill-response.md` | `7adff526730ce22e211d33b11849e0914ac035d7699b74f12105d37a26f4bb69` | 4,454 |
| `review/wp46-wp47-delivery-2026-09-27/self-checks.json` | `da4c44a0fbd29ce8d656e98a102d331b8a13c0acd6de4b8c62b511b13c59d57b` | 203,805 |
| `review/wp46-wp47-delivery-2026-09-27/boundary-checks.json` | `b39ff17c64ab09e136b031968ed44d3cfbaf826d81517103bbbb7b27f215503b` | 10,413 |

## 6. 停止点

**只送WP46、WP47-A、WP47-B主稿／附表及五组交界（含上述三条新观察）统一独立review后停止**。没有启动WP50或其它第四包；不发reviewer消息、不创建任务／Agent、不提交／推送。

完整形态／Shadow、AI／设施／其它未审域、真实地图／存档／输入、Demo／宿主／媒体／插件、U01–U10及WP78→79→80阶段出口继续保留。未实现新框架、未设计具体API／类层级、未执行游戏／Ruby／表达式／解释器／生成器／编译器／转换器／真实网络。
