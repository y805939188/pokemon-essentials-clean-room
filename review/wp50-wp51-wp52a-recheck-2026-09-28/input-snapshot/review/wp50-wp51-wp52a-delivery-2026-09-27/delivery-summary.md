# WP50 → WP51 → WP52-A 交付摘要 v2（首审有限修订）

2026-09-28；提取侧有限修订与管理回填。**WP50／WP52-A继续ReviewPending；WP51按首审PASS_SCOPED限定Reviewed回填**。本摘要不是外审结论或WP80 sanitized产物，不启动下一批。

当前依据：[独立报告](../wp50-wp51-wp52a-review-2026-09-28/report.md)和[有限修订提示](../wp50-wp51-wp52a-review-2026-09-28/revision-prompt.md)。仅WP50-R01、WP52-A-R01、BATCH-C01及直接传播；WP51管理回填获明确授权。版本v1为首稿，v2修果实参数方向、三墙人数口径及C01文字，并级联实际身份；v1在本轮快照与下表留史。

## 1. 旧批已接受与本轮范围

依据[独立首审报告](../wp46-wp47-review-2026-09-27/report.md)及[执行提示](../wp46-wp47-review-2026-09-27/next-batch-prompt.md)，先完成WP47-B-N01/N02、BATCH-N03旧摘要同步并CLOSED，C01三点维护，再回填WP46/47-A/47-B各自限定Reviewed。14固定预检＋7级联补检匹配，旧语义更正与管理状态分列；[回应](backfill-response.md)及[18份差异](backfill-diffs/)保留原身份、来源、静态验收及范围。

限定通过集合＝WP01–WP21、WP24–WP31、WP33–WP36、WP39–WP49（WP47为A/B）、WP59–WP60。本轮另新增WP51限定通过，WP50与WP52-A仍不在该集合；前批运行未决与阶段出口保留。

## 2. 当前固定身份与被审历史

| 文件 | 完整SHA-256 | 字节 | 状态 |
| --- | --- | ---: | --- |
| [wp50-held-item-triggers-and-consumption](../../specs/pokemon-rules/wp50-held-item-triggers-and-consumption.md) | `fcbbca67dafbb1aaa1cfd2560983a6f34830c31c11feccb7688f08b372a395b1` | 31,648 | ReviewPending有限修订v2 |
| [wp50-held-item-effect-coverage](../../specs/pokemon-rules/wp50-held-item-effect-coverage.md) | `4f0f99489f486c8e0dc4cc83689ef56ac73b74c3ecc367cd2a5f7936802ee686` | 13,855 | ReviewPending附表v1（内容未变） |
| [wp51-ai-action-selection-and-skill](../../specs/combat/wp51-ai-action-selection-and-skill.md) | `baebd58a7f4eed635f685f583fa7b4d21785a9ac13a0a1ee4c2ccd6ec7b6bac5` | 26,784 | Reviewed限定管理回填v2 |
| [wp51-ai-decision-defaults](../../specs/combat/wp51-ai-decision-defaults.md) | `5069a3690c6886204ebe9877ff0165e77c4c437fb8273032ac9d6f52bf89c2d0` | 5,472 | Reviewed限定管理回填v2 |
| [wp52-a-generic-numerical-and-status-evaluation](../../specs/combat/wp52-a-generic-numerical-and-status-evaluation.md) | `6c0534fea6d4a18284c1e54a38e413ad010d38291088b0df45d8ac087ca44c9c` | 48,127 | ReviewPending有限修订v2 |
| [wp52-a-evaluation-coverage-and-data](../../specs/combat/wp52-a-evaluation-coverage-and-data.md) | `a5a13acaf8572fa621b91911430b2286b23340618c72d4b5d2e1522aaf4ec5f9` | 58,772 | ReviewPending有限修订v2 |

WP50先修订固定，再WP51维护／回填，再WP52-A修订与级联；WP50引用明确为批内修订v2尚未外审，WP51为已限定通过的回填后版本。附表从属各自包，不新增包。

被审首稿v1完整身份（新字节不冒充这些被审对象）：

| 文件 | v1 SHA-256 | v1字节 |
| --- | --- | ---: |
| `specs/pokemon-rules/wp50-held-item-triggers-and-consumption.md` | `937551e00ec61a8a807bfa197ece1e2f91b6b5f91f620375e6c14ea900e9027a` | 29,336 |
| `specs/pokemon-rules/wp50-held-item-effect-coverage.md` | `4f0f99489f486c8e0dc4cc83689ef56ac73b74c3ecc367cd2a5f7936802ee686` | 13,855 |
| `specs/combat/wp51-ai-action-selection-and-skill.md` | `1174d485f2648682cbd98a446044dfd487bab694d7afdb94e309f3d3fe4a6972` | 25,064 |
| `specs/combat/wp51-ai-decision-defaults.md` | `f3837410a9c41617495d2691e69f2e7baa11e7e5c3d7521f618a0f1472ad6c09` | 4,811 |
| `specs/combat/wp52-a-generic-numerical-and-status-evaluation.md` | `f7f400c642d77f29c5411ac156fe0e49716848b87ed232b02b8d418e1c67126a` | 46,332 |
| `specs/combat/wp52-a-evaluation-coverage-and-data.md` | `b620a868091aff4e1bb519f18e89698688eef279dbb020f828e2a0dfa25739c6` | 58,177 |

## 3. 行为、数据与有限修订验收

- WP50-R01：false表示半血无需贪吃；ORAN H100/HP26无或有效贪吃均至36，HP50至60、51不触发；SITRUS半血至75；五混乱果世代6半血至62，世代8半血无贪吃拒、有效贪吃至83。食果资格、forced、恢复量／RIPEN、Nature和消费次序保留。
- WP52-A-R01：极光幕、物理反射壁、特殊光墙计目标当前同侧存活场上人数。固定名义双席、中等、普通单目标、墙前37：两人25、只剩目标19；空位／倒下／后备不计；预计非会心、未绕墙门及极光幕优先保留。
- BATCH-C01／WP51管理：后备可伤改明确存在一组未被吸收组合；天气到期重估明确CLOUDNINE／AIRLOCK与UTILITYUMBRELLA分列。限定A～E Reviewed及附表数据回填，不改主动治疗估量。

详见[revision-response.md](../wp50-wp51-wp52a-review-2026-09-28/revision-response.md)及相对本轮快照的9份revision-diffs。先前三观察、C01及WP46/47回填已接受，旧回应与18份差异原件不改。


- WP50 A～F：有效性与普通/强制入口、计算槽、触发时序、消费/回收/转移/恢复、共生等连锁；32族、165直接/21复制、展开196（族,物品）身份，两空族具名；33场景、11常数。讲究物P槽、分调用者的半血／四分之一门、红牌先耗等合同已写明；R01更正不改其它量值。
- WP51 A～E：AI控制/技能/标记、换人/主动道具/Mega/招式顺序、候选与目标、阈值权重、资源与回退；15换人处理器、32 X道具默认项；25场景、5常数。高技能仍加权选择，无候选与全零不混同；状态道具方向及SITRUS估量等差异保留。
- WP52-A A～F：失败/合成/22通用修正、粗速度/命中/会心/伤害、阶级与状态/类型/能力偏好，267基础能力评级；164效果身份和334本包登记出现；53场景、12常数。预测与真实规则分开，命中整数96及r96失败保留，负会心级、同速反序、负量评分和方向差异具名。

当前共111静态场景、28独立常数检查；原101场景除V05错误期望已替换外保留，新加10个对照，原21常数另加7项。静态算术与文本对应不等同外审通过。AI全Scripts登记扫描12文件784语句、展开786出现／783不同（族,身份）键：A334、WP51已有15、B247、C190，三重复键全在后续B/C边界显式登记，不冒称无重复。此集合不是完整AI行为已闭合；具体B/C尚未提取，WP79未启动。

## 4. 五组直接交界与未决

[boundary-checks.json](boundary-checks.json)列五组：物品与持久/背包/消费；物品与计算/阶段能力；AI行动与训练家/资源/命令/换人；AI评估与真实规则及后续B/C；历史/当前/批内版本追踪。实际完整身份绑定逐项实测。

本轮没有扩大旧语义同步范围。AI新快照差异是预测合同，不自动改真实WP40/43/44/48。完整形态/Shadow、设施、其它未审效果及动态等价仍前向；预测共享字段、异常回退和宿主交互为运行未决。

## 5. 材料身份与登记

[self-checks.json](self-checks.json)与boundary现为v2，revision_history保留旧结论与完整身份；当前12件预检匹配本轮快照。原覆盖/源身份/默认数据保留，本次只回读两项与C01具名入口并补分支验收；没有参考执行或转译模型。旧self/boundary/摘要v2已维护，旧报告/提示/快照/回应原件不覆盖。

| 配套材料 | SHA-256 | 字节 |
| --- | --- | ---: |
| `planning/feature-matrix.md` | `f2c1a5810dd6fcba6fc7f37f0c0fd5666062f81e8628b70471993cc62d9a1001` | 49,715 |
| `review/wp46-wp47-delivery-2026-09-27/delivery-summary.md` | `73226fe59a5b6036bdabb913f121d5cadd76e23ad2f62c9a54dc686d173697c6` | 6,036 |
| `review/wp46-wp47-delivery-2026-09-27/self-checks.json` | `eda9101ab5b563f5c3b53e53b029a6d0c82ec8e96a7358c3e4e0c6c7be2318c9` | 209,456 |
| `review/wp46-wp47-delivery-2026-09-27/boundary-checks.json` | `2cb48235c7794e4167128a399f04c9cb3465e299c9096da1ecde6e49f9d6dae0` | 23,256 |
| `review/wp50-wp51-wp52a-delivery-2026-09-27/backfill-response.md` | `860bc758987f3ca772ef445fa3051e939aaddd23f76afa6b06275ae85d8f8e05` | 7,731 |
| `review/wp50-wp51-wp52a-delivery-2026-09-27/self-checks.json` | `0960427cb4ce0f2044604a15b1754dc310f47162d1e16ad67999dd753ad4111d` | 416,764 |
| `review/wp50-wp51-wp52a-delivery-2026-09-27/boundary-checks.json` | `82c7c95c75abd44d48213cc470b16ca62c21123eb332d09b36905aeae6b1be90` | 31,428 |

矩阵F12-04/05旧具名范围Reviewed；F08-05分旧状态/物品写入与新WP50；F12-07 WP51限定Reviewed，F12-08仅WP52-A ReviewPending，B/C及运行Inventoried。manifest第五十四轮、主TSV v29保留原587/491行、补登本轮reviewer14件、revision-response及9份差异（新增24行）；登记后全量行数与哈希由交付消息实测报告，不预称外审通过。manifest不自哈希、TSV不收自身。

## 6. 送审与停止

**本次只送WP50-R01、WP52-A-R01、BATCH-C01、WP51管理回填差异及直接传播有限复审，然后停止。** 不启动WP52-B/C、其它第四包或WP22/23/32/37/38；不向reviewer发消息、不创建任务/Agent、不提交/推送。reference只读且基线不切；未运行游戏/Ruby/参考表达式/解释器/事件/生成器/编译器/转换器/插件/真实网络，未操作真实地图/存档/输入。Demo/宿主/媒体/U01–U10与WP78→79→80继续保留。
