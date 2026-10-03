# WP46 → WP47-A → WP47-B 交付摘要 v2（限定回填与批准同步）

2026-09-27；提取侧管理维护，非独立review、非WP80 sanitized。三主稿及三附表均**Reviewed（限定静态范围，首审PASS_SCOPED；管理性回填）**，依据[独立报告](../wp46-wp47-review-2026-09-27/report.md)§2–4与[执行提示](../wp46-wp47-review-2026-09-27/next-batch-prompt.md)。新字节不冒充被审首稿。

## 1. 版本与范围

v1首稿和当时102场景／26常数、三观察待判定的结论保留在本轮input-snapshot；v2先同步获批三观察，再做C01三处维护与限定Reviewed回填、必要身份级联。旧backfill-response／五份diff、前批reviewer及快照不改。本次实际差异与逐项验收见[当前批回填回应](../wp50-wp51-wp52a-delivery-2026-09-27/backfill-response.md)及其backfill-diffs。

WP46 A～F139主身份；WP47-A A～E55；WP47-B A～F60。8效果文件314＋内建挣扎1＝315，有界本批254＋已有61（WP43 1／WP44 29／WP45 31），不扩为全战斗。完整运行、形态、设施与阶段出口保留。限定通过集合＝WP01–WP21、WP24–WP31、WP33–WP36、WP39–WP49（WP47为A/B）、WP59–WP60。

## 2. 当前回填身份与被审历史

| 文件 | 当前SHA-256 | 字节 | 被审首稿SHA-256 | 首稿字节 |
| --- | --- | ---: | --- | ---: |
| [wp46-damage-multihit-and-healing](../../specs/pokemon-rules/wp46-damage-multihit-and-healing.md) | `aa9a7f1e206275ce934a1bc3cf860813bafac852795a5d939316c6f5d9e8bf4c` | 47,646 | `0e5a676e234a71a949602d93a2a6aeb4c26cf09acc894e47eee66eb3c1e8a323` | 47,352 |
| [wp46-damage-healing-coverage](../../specs/pokemon-rules/wp46-damage-healing-coverage.md) | `549cd587095df207bf359c34fd66f14f2dda0c93ce1dcaec6bf4f63fc4d084c1` | 36,824 | `170e063faaea4b66b5e8a7fc0b9bba907ff7aba7b4c15d8f435ff50d51f7ce88` | 36,408 |
| [wp47-a-move-attributes-targeting-and-calling](../../specs/combat/wp47-a-move-attributes-targeting-and-calling.md) | `1b1dea7cee12b38d867f81122718e328857bc8f17096632e9178bf07b5ff6675` | 33,611 | `ad6a6d6c4d5c90dbf32f5cd0c843a84dad605319ee4a99c1d5d3d04f8f57b49c` | 33,207 |
| [wp47-a-attributes-targeting-calling-data](../../specs/combat/wp47-a-attributes-targeting-calling-data.md) | `49e343003be7c22653cad121f3c037b915212da18b6240cda12e653d07c91a17` | 19,340 | `1c164a68ed2d35c1dceaa9314038a9fe0f6a011c845a9adf512f740a466a898c` | 18,920 |
| [wp47-b-switching-control-and-item-changes](../../specs/combat/wp47-b-switching-control-and-item-changes.md) | `0287e0b2ea569d24330933ae06498e61237eb0dc9d4116efa9783cc72f739317` | 38,558 | `24185ce4179387c900b11e3505d9309f1869ba8587aa2bd263609f1eec25c0bd` | 37,934 |
| [wp47-b-control-items-coverage-data](../../specs/combat/wp47-b-control-items-coverage-data.md) | `0736044d556367392e2a0204a4a934a903d3472c9cb28435b4765798d915d13a` | 17,922 | `3a092b6653b0d283a47e45aa4ed9b06b04ca62683a14b17b42048829bf00d83c` | 17,454 |

## 3. 三观察与C01的实际收尾

- WP47-B-N01 CLOSED：WP41普通单目标撤退射击反射可降阶，但原路径外层0击，后段仍拒换出；保留普通成功路径与原换人分层。
- WP47-B-N02 CLOSED：WP40号令按消费时最近招找真实槽，以specialUsage=false普通入口再次用，前置过PP2→1；睡眠前拒仍2，恢复已行动轮不代表PP和记录不变。
- BATCH-N03 CLOSED：WP41野生拖出读主要效果时当前替身耐久0或绕过；替身5被打破可决定3，未破不置3；非野生仍因本击吸收标记拒拖出。

C01：WP46来源粘连区间拆开；鸟嘴加热明确HP提交后的每击反应，首击不重算；神秘守护归WP45建立／期限、WP44免疫查询，61项分布1/29/31不改。以上为独立报告批准的限定同步，不是提取方自动推翻其它旧review。

## 4. 保留的规格与自检范围

WP46逐击、固定伤害、威力与输入替代、吸取／治疗／反伤、两回合／连用／誓约合同；WP47-A类型／保护／目标／反射／调用与默认数据；WP47-B换人／控制／物品C/I/R/P/Belch、能力／浮空／变身操作；均按原独立批准范围。102场景、26独立常数、67自然之恩、578投掷、各排除集合维持原证据，未宣称再做动态验证。

self与boundary现为v2，revision_history保留旧身份／观察语境，活动身份级联到当前规格。前批WP42/48/49回填已接受，本次其必要上游身份更新不重写行为。

## 5. 登记与当前配套材料

F12-04/05具名回填，WP50/51/52-A为新批ReviewPending；manifest第五十三轮、主TSV v28登记当前回填及新三包。各旧被审值由历史链与本轮快照保留，不将历史报告当当前哈希表。

| 材料 | 当前SHA-256 | 字节 |
| --- | --- | ---: |
| `planning/feature-matrix.md` | `35935419cb9648d4bfd60665d7a7719a9d79230b9d7585bf852a9120ef87ab30` | 49,556 |
| `review/wp46-wp47-delivery-2026-09-27/self-checks.json` | `eda9101ab5b563f5c3b53e53b029a6d0c82ec8e96a7358c3e4e0c6c7be2318c9` | 209,456 |
| `review/wp46-wp47-delivery-2026-09-27/boundary-checks.json` | `2cb48235c7794e4167128a399f04c9cb3465e299c9096da1ecde6e49f9d6dae0` | 23,256 |

旧摘要／checks历史完整身份：

| 材料 | 被审v1 SHA-256 | 字节 |
| --- | --- | ---: |
| `review/wp46-wp47-delivery-2026-09-27/delivery-summary.md` | `85f4df02f5592cca3d91fbbb46aec7d86ea5378f83012661455f04910beb0554` | 6,945 |
| `review/wp46-wp47-delivery-2026-09-27/self-checks.json` | `da4c44a0fbd29ce8d656e98a102d331b8a13c0acd6de4b8c62b511b13c59d57b` | 203,805 |
| `review/wp46-wp47-delivery-2026-09-27/boundary-checks.json` | `b39ff17c64ab09e136b031968ed44d3cfbaf826d81517103bbbb7b27f215503b` | 10,413 |

## 6. 后续与停止

已按授权串行完成[WP50→WP51→WP52-A首稿](../wp50-wp51-wp52a-delivery-2026-09-27/delivery-summary.md)，批末只送这三个新包与直接交界。WP52-B/C及其它第四包未启动；运行、Demo／宿主／媒体／插件、U01–U10及WP78→79→80保留；不发reviewer消息、不创建任务／Agent、不提交／推送。
