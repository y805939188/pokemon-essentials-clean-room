# WP22 → WP23 → WP32 统一送审材料

2026-09-30；规格提取方，非独立reviewer。先完成WP62限定Reviewed管理回填与C03，再按顺序回源、写稿、自检、固定和矩阵增量。**新三包全部ReviewPending（批内固定版本，尚未外审）**；没有实现新框架。105条静态场景不是运行测试。

## 1. 主稿与附表（最终固定身份）

| 包／文件 | 完整SHA-256 | 字节 | 主稿场景 |
| --- | --- | ---: | ---: |
| WP22 [wp22-mega-and-primal-reversion.md](../../specs/pokemon-rules/wp22-mega-and-primal-reversion.md) | `c3f4130c8a755361426f20e60485d2f76a937abd7fb18d1e8833a677a6091099` | 24,859 | 25 |
| WP22 [wp22-transformation-data.md](../../specs/pokemon-rules/wp22-transformation-data.md) | `e2b3943a4c7d0c0d820171217b5058e7649da55534bd5e5337363e3bbfc3335c` | 6,027 | — |
| WP23 [wp23-shadow-hyper-and-purification.md](../../specs/pokemon-rules/wp23-shadow-hyper-and-purification.md) | `cd8b5e244e181bf8c57e483f0364ac315457b9292c9d003523c9a030e79d1c19` | 34,418 | 42 |
| WP23 [wp23-shadow-data-and-vectors.md](../../specs/pokemon-rules/wp23-shadow-data-and-vectors.md) | `416ac4110b8eac8b0e05858f381144c24ae893cb8ad0303854eda1c323cb5d15` | 12,071 | — |
| WP32 [wp32-contextual-trade-and-post-battle-evolution.md](../../specs/pokemon-rules/wp32-contextual-trade-and-post-battle-evolution.md) | `480879bd8eb777938c301a8241dff4e16f4990378543b47fddb2e9af0a2f76de` | 29,515 | 38 |
| WP32 [wp32-context-inputs-and-scenarios.md](../../specs/pokemon-rules/wp32-context-inputs-and-scenarios.md) | `869cbbaafb6dab2c9bd2da0c2711a7443b2ae88b8007e238f5c156acc53c498d` | 9,798 | — |

- WP22 A～F：Mega个体／战斗分层、所有者与资源、登记取消执行、状态传播、Primal独立规则、换下／濒死／捕获／终局／设施还原；48个默认Mega目标／47石／1招式型，含METAGROSS实际HP差异。
- WP23 A～G：建立、心阶段、Hyper、经验／EV暂存与恢复、招式、各净化入口、9组净化室的成员流转／节奏与流量／领取及失败；25性格数据、可选131配置／18招／4物品／1类型与默认未启用边界。
- WP32 A～F：实时地图／时钟／天气输入、L0／K／D与R、逐击记录和濒死清理、战后条件与取消、捕获队伍移位、交换／事件提交；35个情境身份及57条默认数据。

## 2. 回填与新观察

WP62被审v3 `e38812c8057fd3348c10319c29240ef6e21e72f37c769601f6e1d86bb0d56639`／32,378字节获独立PASS_SCOPED；本次回填后身份与六份最终差异见[backfill-response.md](backfill-response.md)。WP58／WP38原受理范围继承，WP38仅状态／身份／W07历史记法同步；旧报告、两轮回应与所有快照不改。

[new-observations.md](new-observations.md)列9项待审观察。WP32-N01指出WP31第114行“对对方”的要害摘要过窄，旧稿未改；WP32-N02公开交换双收尾及宿主重复释放未决。其余7项是新包范围内的数据或生命周期边界，不是重开旧关闭编号。

## 3. 自检、交界与审计材料

- [self-checks.json](self-checks.json)：逐包静态检查与17项标准映射；`dd680d500319b5497e8652781e2c3f9a48956174c170e19274111e47d5ec6231`，28,327字节。
- [boundary-checks.json](boundary-checks.json)：六组交界及45条完整绑定；`5a3aaf88261f9e5b8daa4216bf725e382163d2d12675ded31fd8a4f14fdfcf0f`，20,497字节。
- [source-identities.json](source-identities.json)：实际来源文件身份、读取范围与固定commit blob核对；`996255fc73d67efd0360b513abc2cc17b99006ec6766bf3926832d0c0c48f823`，42,728字节。
- [diff-bindings.json](diff-bindings.json)：六份差异的基线与最终目标绑定；`cb5a5184ef6fd6fcdba7226b8162060dc741d45d89d0bbb2f8a1a1a64eedbc3c`，4,897字节。
- [preflight-checks.json](preflight-checks.json)：9项／828输入／历史快照固定预检；`804dac16d663488dc90c757884e4b4eeaea6da227a89306f35af48fcf120d6dc`，6,438字节。
- [backfill-response.md](backfill-response.md)：管理回填回应与身份链；`d3abe312a2c897899319e274f9448aa03e3af1626de7e7ea6561f19708a15c11`，5,265字节。

全量登记、JSON／链接、差异重建、固定输入白名单、历史原件／快照及reference只读状态的最终只读检查见[validation-results.json](validation-results.json)。自有检查只做文本、哈希、集合、JSON、差异与固定算术；没有执行或转译参考模型。

## 4. 登记范围与停止点

现有[manifest](../../planning/review-manifest-2026-09-19.md)续第六十三轮、[主TSV](../wp18-wp20-delivery-2026-09-26/current-hashes.tsv)续v38；保留全部历史身份与旧ReviewPending。F06-08分别登记WP22／WP23，F09-04登记WP32，均ReviewPending＋前向Inventoried。批内WP22→WP23／WP32、WP23→WP32引用明确未外审。

既有限定通过集合：WP01–WP21、WP24–WP31、WP33–WP36、WP38–WP52（47=A/B，52=A/B/C）、WP54–WP60、WP62。新三包不加入Reviewed集合。不是整个游戏运行通过，也不是全Feature完成。

本批完成后停止；未启动第四包、未创建Agent／新任务、未发reviewer消息、未提交／推送。Demo、宿主、媒体、插件、U01–U10及WP78→WP79→WP80出口保留；新观察与所有新稿等待用户转交独立审查。
