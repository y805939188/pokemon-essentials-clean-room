# WP50 → WP51 → WP52-A 交付摘要 v1

2026-09-27；提取侧规格与静态自检。三个新包均**ReviewPending（各自具名范围）**，批末统一送独立review后停止。本摘要不是外审结论或WP80 sanitized产物。

## 1. 本轮授权与旧批收尾

依据[独立首审报告](../wp46-wp47-review-2026-09-27/report.md)及[执行提示](../wp46-wp47-review-2026-09-27/next-batch-prompt.md)，先完成WP47-B-N01/N02、BATCH-N03旧摘要同步并CLOSED，C01三点维护，再回填WP46/47-A/47-B各自限定Reviewed。14固定预检＋7级联补检匹配，旧语义更正与管理状态分列；[回应](backfill-response.md)及[18份差异](backfill-diffs/)保留原身份、来源、静态验收及范围。

限定通过集合＝WP01–WP21、WP24–WP31、WP33–WP36、WP39–WP49（WP47为A/B）、WP59–WP60。新三包不在该集合；前批运行未决与阶段出口保留。

## 2. 串行固定的六件新稿

| 文件 | 完整SHA-256 | 字节 | 状态 |
| --- | --- | ---: | --- |
| [wp50-held-item-triggers-and-consumption](../../specs/pokemon-rules/wp50-held-item-triggers-and-consumption.md) | `937551e00ec61a8a807bfa197ece1e2f91b6b5f91f620375e6c14ea900e9027a` | 29,336 | ReviewPending首稿v1 |
| [wp50-held-item-effect-coverage](../../specs/pokemon-rules/wp50-held-item-effect-coverage.md) | `4f0f99489f486c8e0dc4cc83689ef56ac73b74c3ecc367cd2a5f7936802ee686` | 13,855 | ReviewPending首稿v1 |
| [wp51-ai-action-selection-and-skill](../../specs/combat/wp51-ai-action-selection-and-skill.md) | `1174d485f2648682cbd98a446044dfd487bab694d7afdb94e309f3d3fe4a6972` | 25,064 | ReviewPending首稿v1 |
| [wp51-ai-decision-defaults](../../specs/combat/wp51-ai-decision-defaults.md) | `f3837410a9c41617495d2691e69f2e7baa11e7e5c3d7521f618a0f1472ad6c09` | 4,811 | ReviewPending首稿v1 |
| [wp52-a-generic-numerical-and-status-evaluation](../../specs/combat/wp52-a-generic-numerical-and-status-evaluation.md) | `f7f400c642d77f29c5411ac156fe0e49716848b87ed232b02b8d418e1c67126a` | 46,332 | ReviewPending首稿v1 |
| [wp52-a-evaluation-coverage-and-data](../../specs/combat/wp52-a-evaluation-coverage-and-data.md) | `b620a868091aff4e1bb519f18e89698688eef279dbb020f828e2a0dfa25739c6` | 58,177 | ReviewPending首稿v1 |

WP50先固定，再WP51，再WP52-A。上游已审依赖取更正／回填后的完整实际身份；同批WP50和WP51引用均注明尚未外审。附表从属各自包，不新造第四包。

## 3. 行为、数据与验收范围

- WP50 A～F：有效性与普通/强制入口、计算槽、触发时序、消费/回收/转移/恢复、共生等连锁；32族、165直接/21复制、展开196（族,物品）身份，两空族具名；28场景、6常数。讲究物P槽、果实四分之一门、红牌先耗等快照区别已写明。
- WP51 A～E：AI控制/技能/标记、换人/主动道具/Mega/招式顺序、候选与目标、阈值权重、资源与回退；15换人处理器、32 X道具默认项；23场景、5常数。高技能仍加权选择，无候选与全零不混同；状态道具方向及SITRUS估量等差异保留。
- WP52-A A～F：失败/合成/22通用修正、粗速度/命中/会心/伤害、阶级与状态/类型/能力偏好，267基础能力评级；164效果身份和334本包登记出现；50场景、10常数。预测与真实规则分开，命中整数96及r96失败保留，负会心级、同速反序、负量评分和方向差异具名。

总101静态场景、21独立常数检查。AI全Scripts登记扫描12文件784语句、展开786出现／783不同（族,身份）键：A334、WP51已有15、B247、C190，三重复键全在后续B/C边界显式登记，不冒称无重复。此集合不是完整AI行为已闭合；具体B/C尚未提取，WP79未启动。

## 4. 五组直接交界与未决

[boundary-checks.json](boundary-checks.json)列五组：物品与持久/背包/消费；物品与计算/阶段能力；AI行动与训练家/资源/命令/换人；AI评估与真实规则及后续B/C；历史/当前/批内版本追踪。实际完整身份绑定逐项实测。

本轮没有扩大旧语义同步范围。AI新快照差异是预测合同，不自动改真实WP40/43/44/48。完整形态/Shadow、设施、其它未审效果及动态等价仍前向；预测共享字段、异常回退和宿主交互为运行未决。

## 5. 材料身份与登记

[self-checks.json](self-checks.json)保存预检、源身份/实际读取范围、字面覆盖、场景、常数结果及历史维护；没有参考执行或转译模型。旧self/boundary/摘要v2已维护，旧报告/提示/快照/回应原件不覆盖。

| 配套材料 | SHA-256 | 字节 |
| --- | --- | ---: |
| `planning/feature-matrix.md` | `35935419cb9648d4bfd60665d7a7719a9d79230b9d7585bf852a9120ef87ab30` | 49,556 |
| `review/wp46-wp47-delivery-2026-09-27/delivery-summary.md` | `73226fe59a5b6036bdabb913f121d5cadd76e23ad2f62c9a54dc686d173697c6` | 6,036 |
| `review/wp46-wp47-delivery-2026-09-27/self-checks.json` | `eda9101ab5b563f5c3b53e53b029a6d0c82ec8e96a7358c3e4e0c6c7be2318c9` | 209,456 |
| `review/wp46-wp47-delivery-2026-09-27/boundary-checks.json` | `2cb48235c7794e4167128a399f04c9cb3465e299c9096da1ecde6e49f9d6dae0` | 23,256 |
| `review/wp50-wp51-wp52a-delivery-2026-09-27/backfill-response.md` | `860bc758987f3ca772ef445fa3051e939aaddd23f76afa6b06275ae85d8f8e05` | 7,731 |
| `review/wp50-wp51-wp52a-delivery-2026-09-27/self-checks.json` | `5faccf42e26c67da07e0d844cc03a0d4c9120246e6823f7bab438691361279fc` | 364,926 |
| `review/wp50-wp51-wp52a-delivery-2026-09-27/boundary-checks.json` | `f5eb0aca474da0ba48adb816b8289b3b4a8e4e5966fe4dbcd18b8a3e69fc914d` | 14,164 |

矩阵F12-04/05旧具名范围Reviewed；F08-05分旧状态/物品写入与新WP50；F12-07 WP51、F12-08仅WP52-A ReviewPending，B/C及运行Inventoried。manifest第五十三轮、主TSV v28保留原546/450行、补登reviewer13件及本批材料；登记后全量行数与哈希由交付消息实测报告，不预称外审通过。manifest不自哈希、TSV不收自身。

## 6. 送审与停止

**本批只送WP50、WP51、WP52-A主稿/附表及上述五组直接回归（含获批同步/C01/回填实际差异）统一独立review。** 不启动WP52-B/C、其它第四包或WP22/23/32/37/38；不向reviewer发消息、不创建任务/Agent、不提交/推送。reference只读且基线不切；未运行游戏/Ruby/参考表达式/解释器/事件/生成器/编译器/转换器/插件/真实网络，未操作真实地图/存档/输入。Demo/宿主/媒体/U01–U10与WP78→79→80继续保留。
