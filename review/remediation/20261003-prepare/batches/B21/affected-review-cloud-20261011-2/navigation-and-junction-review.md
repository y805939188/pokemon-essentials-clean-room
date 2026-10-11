# B21 NEW2 独立 affected 导航与资格复审

结论：本委派范围 **PASS**。原 `B21-AFF-NAV-001`、`B21-AFF-NAV-002` 及 `B21-AFF-OBS-001` 在固定 NEW2 上均已真实消除，未发现本范围剩余阻塞。此结论只覆盖独立 affected 导航、资格、批准链及其有界回归；不签 FULL、actual、B21 接受、canonical 关闭或 FINAL。

被审 NEW2 `e58486178e746273fb6fab55df00722807f1dc44`，tree `1dbe28a733bfde428129ed662d7e0d66243978c4`；冻结发布 `9b6d16e34daf59e205f8a3df20e24930175064ed`，tree `11c07f505fc57d62ffd0bf643a1ea0b575a3fd8d`。对比旧 NEW `5c3e19831e1e29450247fa6061f3c2feac2f893e`；正式 C `e9c140dc33de1cb0662521318b051174909e4509`；派发 `eb1885265fcde2a52767077de3193862036c3a71`；精确许可 `aa57e293bf3a0a77fa42f1f42777df88cbd2fbe8`。

先依次读取发布中的 `freeze-2/frozen-NEW2.json`、`review-FULL.md`、`review-affected.md`，再读取上述许可的 `scope-grant.json`。许可只授权两份 WP75 §8.6 各一段及最终 engine 目录 MR18–MR22，许可不是质量结论。完整 C→NEW2 差异只引用已发布固定对象，不复制。

**复核方法与边界**

使用新写的只读 Git/文档元数据审计，并阅读真实改变的条款、案例及旧 scoped 证据。607 个固定目标身份、151 个条款/案例区间及 220 个旧 scoped 回执/trace 对象独立复算零误差。数字描述检查范围，不用作质量通过依据。新审计只读原始文件、JSON/TSV 文档，不执行参考程序、Ruby、编译器、转换器、游戏反序列化器、行为向量或旧脚本；静态案例执行 0。NEW2 子任务只写 `/tmp` 新文件，没有修改仓库或旧报告。

47 批准根/扩展的 ID、scope、对象哈希、precedence 完整不变；14 项 whole original/approved/qualified-fields 与旧 receipt/trace 逐值完全不变。10 个改变映射新读条款，另 37 个映射复用同字节旧独立复审。432 原 source identity/inherited evidence 逐值不变，源语义覆盖复用固定旧证据，不声称本轮重新语义读取全部参考来源；源身份另做原始字节核验。46 未变交界、3 未变链、424 未变 source 行和 17 UI 行逐对象/字节复用。原 96 输入与旧已接受 owner 行为证据未变化者使用固定旧审查，不重复执行。

**NAV-001：真实 owner 导航与资格已修复**

| mapping record（0-based） | 固定批准 scope/object SHA256 | 当前真实 consumer 与旧 scoped owner | 判断 |
|---|---|---|---|
| 4 `GIR-FD82-003` | `root_adjudications/1` / `34431bb6311f2f0b559a13d10fbac253d1504594c1bcc6c772154d80c0e79dfa` | WP72 §2/6.4；WP73-A §2/3.5/6；WP73-B §6.5/7.1/7.5；B19、C trace row285。 | PASS |
| 9 `GIR-FD82-003` | `extension_decisions/4` / `eff4332168b08ac236bcc9449680da1c0ed4a2c0c7fbdad621fb8cee7ffec113` | WP67-A §2/6.1/9.1/9.3/9.4 与 WP76 §3.2/6.1/7.4/11；B17、row265。原 whole 批准中的 WP67-B 本地范围保留。 | PASS |
| 14 `GIR-FD82-003` | `extension_decisions/9` / `560c9558ff0bccf86b358ce7a6185d9977c5b4ccc923ac964ca05603c729314c` | WP60 §2/3/8（B14）与 WP61 §2/3.1（B14）；WP63 §2.2/4.1/4.2/4.5（B15）；WP65 §5.1/5.2/6.2（B16）；rows172/208/241。 | PASS |
| 15 `GIR-FD82-003` | `extension_decisions/10` / `8665f5ef298dc14ed97c8b7d5ea3d197f3e4c05c2e840aec08285dc81bc3abda` | WP66-A §2/3.3/5.2/5.3 与 WP67-B §1/2/6.3/6.4；B16/B17、rows241/265。 | PASS |
| 25 `GIR-FD82-C003` | `extension_decisions/1` / `1d0c4642c1cc2a2c79f8efe7af93abf909b45e8e869f4eec68fe2a947c8479b2` | WP74/75，grant-after WP75 当前身份与保留 ASCII/转换条款分别核对；旧批准不转授新 §8.6。 | PASS |
| 30 `GIR-FD82-C003` | `extension_decisions/6` / `46e59d1c9fa44e5cdf9d3fff4fe85303684ccc8cdb246b05447dee9bf9ffc498` | 收获 A23/A31/A33：WP28 §5.1、WP66-A §4.2/7.3；孵化 L09：WP35 §5.1/5.3 机制、WP67-B §4.1/4.2 UI；B07/B08/B16/B17。 | PASS |
| 34 `GIR-FD82-C007` | `extension_decisions/0` / `771aaa877c4cde02458e7dc65ce34dfd0397d9de464b4169dcfe31f1d373d3fd` | WP75 新 §8.6 与历史 C §8.6 分列；原 current qualified rule 整段保留，再追加 grant-after 仍待复审的精确桥。 | PASS |
| 39 `GIR-FD82-C029` | `root_adjudications/0` / `823ff4cb62475fe59b2fc672c9f5c68711d71e2f0bf6c4e34a129f180ab79f4c` | WP21 §6、WP18 §3 为一般规则；WP77 §6.4 为 B20 真正形态覆盖 owner，B20-C029 case/row318。 | PASS |
| 42 `WP80-INTAKE-R01` | `root_adjudications/0` / `25c07b607d03c3bf1c1ac87e8b6325c007d464c9fd6bc6284e523b0937970def` | ASCII 根 WP72/74/75 新 grant 后 WP75 文件身份/条款刷新，兼容条件原样保留。 | PASS |
| 43 `WP80-INTAKE-R01` | `extension_decisions/0` / `525c884d8e49f95a277b3527b10710ee88d8379d74d581da2790fed62b95d0d2` | ASCII 扩展 WP13/74/75 新 grant 后 WP75 身份刷新；WP13 原接受范围保留。 | PASS |

FD003 是按完整限定批准复核，不是把新增局部导航当成 whole 批准替代。record9 的 B17 精确 receipt `/accepted_contribution_receipts/264` 对象 SHA256 `2ec39acd5cb13e2a5db1ff1f67ad3717175b7cd6831f24811e6ec6d51ac19117`，C data row265 SHA256 `bf4b812f1bce1165d44997261a292b840d1bb78280310a3e440aff92c6dcef5d`。旧 WP67-A/B+WP76 整体 scoped 证据未丢失；新的当前导航补足原误配。WP60/61 的容器中立、各地块独立状态、共享 handled 次序及快照成员条件仍是真实正文约束。

L09 在最终 UI 测试目录固定 C 行405区分直接孵化工具的机制提交、单独 UI 入口、正计数直接工具与调用方归零、UI wrapper true 后回退不可达。WP35 机制和 WP67-B UI 分列，收获 A23/A31/A33 分别链接 WP28/WP66-A；没有再误归 WP70 彩票/挖掘。案例只核静态文字及固定行哈希。

C029 traceability `/records/9` 的 accepted primary/accepted contributors 归 B20，B21 只 pending。WP21/WP18 文档 owner B05 作为通用消费者保留，未据此虚增 C029 已接受贡献。WP77 §6.4 保留 GIRATINA 强制0优先、in-battle/storage存储值、正常动态1/0、提交及 `form_simple` 只取强制/存储的真实区分；OBS 归属错误已消除。

**CFG-25/26 与 SRC-392/393**

原空 consumer 现有具名 current interface，分别绑定 `qualified-navigation-repairs.json#/CFG-25`、`#/CFG-26`；source rows392/393 当前路径与配置行一致，源对象和 inherited evidence 未改。当前机制、真实局部读样本、启用未知分别保留，没有把路径存在或旧批准当作全读/启用证明。

| 配置 | 当前具名机制/数据消费者 | 原已接受 owner |
|---|---|---|
| CFG-25 | `deliverables/final-specification-set/pokemon-rules/wp31-basic-evolution.md` §2 L13–26, §3.1 L31–67, §3.5 L94–102, §9 L229–242 | B07 /dependencies/6 |
| CFG-25 | `deliverables/final-specification-set/creature-rpg/wp33-daycare-and-breeding-session.md` §5.1 L109–123, §5.4 L140–149 | B08 /dependencies/7 |
| CFG-25 | `deliverables/final-specification-set/creature-rpg/wp35-eggs-and-hatching.md` §3.1 L45–53, §3.2 L54–59 | B08 /dependencies/7 |
| CFG-25 | `deliverables/final-specification-set/combat-requirements/wp55-facility-session-and-restoration.md` §2.5 L67–100 | B13 /dependencies/12 |
| CFG-25 | `deliverables/final-specification-set/combat-requirements/wp47-b-control-items-coverage-data.md` §2 L49–65 | B11 /dependencies/10 |
| CFG-25 | `deliverables/final-specification-set/combat-requirements/wp47-b-switching-control-and-item-changes.md` §5.1 L110–117 | B11 /dependencies/10 |
| CFG-25 | `deliverables/final-specification-set/demo-dx/wp76-facility-content-generation-and-simulation.md` §5.5 L94–100, §5.6 L101–111 | B17 /dependencies/16 |
| CFG-26 | `deliverables/final-specification-set/pokemon-rules/wp22-mega-and-primal-reversion.md` §2 L11–24, §3 L25–36, §5 L66–75 | B05 /dependencies/4 |
| CFG-26 | `deliverables/final-specification-set/pokemon-rules/wp22-transformation-data.md` §1 L5–59, §2 L60–68 | B05 /dependencies/4 |
| CFG-26 | `deliverables/final-specification-set/pokemon-rules/wp31-basic-evolution.md` §3.5 L94–102, §9 L229–242 | B07 /dependencies/6 |
| CFG-26 | `deliverables/final-specification-set/pokemon-rules/wp32-contextual-trade-and-post-battle-evolution.md` §2 L11–33, §7 L110–122 | B07 /dependencies/6 |
| CFG-26 | `deliverables/final-specification-set/pokemon-rules/wp32-context-inputs-and-scenarios.md` §2 L47–110 | B07 /dependencies/6 |

CFG25 对应基础进化、培育兼容/招式共享、蛋来源、设施队伍数据、战斗道具数据/切换，以及 WP76 事件调用样本；CFG26 对应 mega/primal 机制与输入数据、事件/contextual 进化及输入集。明确下包与大小写边界，不依赖旧正则命中。其余 34 个 source 空 consumer 不因空字段直接判失败：它们保留 NA/未读/工具或候选输入存在性/宿主与动态启用未证等原有限层边界，原全控制资格通过其它固定机制入口保全；未出现新的真实具名已交付机制被空字段吞掉。

**NAV-002：G9-3 五个当前管理条款与真实批准链**

G9-3 现在从五个当前管理文件定位具体区间，逐项附 B01 GIR001 与 B18 R02/GIR001 的真正旧 scoped receipt/trace。当前文字分开原批准、当前字节、候选/actual 与 canonical 关闭；旧 ReviewPending/datedmanifest 按原时点保留。327 已接受贡献不能推成229关闭；14 B21 仍待独立门。

| 当前固定条款 | 行范围 | 同字节区间 SHA256 |
|---|---|---|
| `planning/feature-matrix.md` | 1–16 | `199856ceab0c6a6d55e62c98c453e6de2febcd01f21a4a216204cb956e3860fb` |
| `planning/review-manifest-2026-09-19.md` | 4115–4127 | `caff5115fb27503be8bf08595aa4c074034385e1e9a2adccbd1424e445ef55b9` |
| `audit/source-traceability.md` | 1–18 | `318f62c9379fb666dbc3bdfd5c1081065cc83d5942d490805013b6276bc4b1fd` |
| `deliverables/final-specification-set/README.md` | 1–16 | `c7fb64de645801993206c0b7153e3db0b0aac24a6299d814c674529d0cc9dc51` |
| `deliverables/final-specification-set/scope-statement.md` | 1–16 | `6c4f03c86c06ed760af924c309c69d8082a56cd1453f19eb38533da1e13814ad` |

| 真正旧 scope | C receipt pointer / 对象 SHA256 | C trace data row / 对象 SHA256 |
|---|---|---|
| B01 GIR-FD82-001 | `/accepted_contribution_receipts/0` / `5fb446c8a83d7fe2ee509346c5aff9ee8948e078f6cb9f28a79ac0eea6567b40` | 1 / `718860b4fd38a621948a96ab462917a47de941f932ad9754553e2e7aa0e4e006` |
| B18 WP80-INTAKE-R02 | `/accepted_contribution_receipts/283` / `da9e324e49fc1999fef0a2016a302b1f93d4d752e4aa6558f6600dd39d7bc43c` | 284 / `7ee18703e9ab690396b5a164d79b4c00b2b9549729957602fa6084ff435478ab` |
| B18 GIR-FD82-001 | `/accepted_contribution_receipts/276` / `e972644594a9a560d160751768b6b473e8afc40055fd705d9883e625383ac530` | 277 / `1b1d0222deebabdd6f186577928ab662507d1e89c82ae0fdd08675149bc3a99f` |

上述三个 scope 的对象哈希从固定 C 全文件逐对象重算，D dependency0/17 也是真实 accepted owner；因此不是泛大同 ID 导航替代。管理层仍声明 AUTHOR_PROPOSAL_PENDING_NOT_ACCEPTED，旧 owner 只承接其原语义范围，不接受新 B21 层字节。

九原输入由原 snapshot 与 REVIEW_BASE 原文件重新直接字节比较：`wp69-voltorb-layouts`、`wp70-mining-data` 完全相同；其余七个文件恰有一次 `delivery/`→`../../review/wp68-wp69-wp70-parallel-b-2026-09-30/` 替换，各增加41字节，没有其它修改。九个当前 original 与 final 共18文件在 C、旧NEW、NEW2逐字节相同；九 snapshot 也同 C→NEW2。旧批准只限定这些原输入身份，不转授当前修改正文或候选后继。九后继原始文件 SHA256 `9c2a34d7ed15738b68d9863c110571d7669ccac0491e1f6c42843bf3e0dca7f7` 全字节未变。

G9-3 的 `audit/source-traceability.md` identity 固定旧NEW、整文件 SHA256 `1826bd66095cf0379a3bb8ed5c95dd05cb17a81b0502e4fe14f911f6d0cda714`，bytes289502；NEW2 同路径整文件 SHA256 `f19850de40c266e4135a829419e624ff2cdbb61258fc34edae1938dabd95fe25`，blob `31aa257d553e84cadae5b668bd80256938697644`，bytes290437。NEW2只在文件末尾增精确 WP75/grant/25输出桥，G9指定1–18行独立比较完全相同，因此固定旧局部条款引用有效；没有把旧 whole 文件身份称为 NEW2 whole 身份。

**54 交界、8链、source/UI 与精确 current 依赖回归**

54 中改变 G1-2/G2-4/G2-8/G4-2/G7-4/G8-2/G8-3/G9-3，共8项；其余46整行不变。G1-2把 Shadow 局部读与 Gen5–8 备份仅存在分开；G2-4保留逐成员独立随机分支、成长基础/Shadow门及循环后reset；G2-8明确旧图存在/不同图/天气类型变化，显式重建duration7与连接后写20、显示guard及名义单位分开；G4-2保留原始快照单写、四个队伍入口、空数组与nil取消、取消恢复与结束写入/refresh/save条件。改变条款阅读与相邻失败条件比对未见此范围新导航/资格回归。具体接口 FULL 质量由父复审另行合并。

8链改变 CHAIN-2/4/5/6/8，3链完整对象不变。source432 改8行：SRC-040/314 指向新 route bridge；SRC-364–367 修 Shadow 局部读/启用资格；SRC-392/393 修 PBS current consumer；424整行不变。35配置变CFG25/26/35，UI17全原始字节不变，SHA256 `926ce5169faf1591875a4df9946541f211e84fd4f11506b7d060bc428cc1f973`。

所有111个当前 consumer identity 在 NEW2 实际路径重新核原始字节，均匹配其固定/显式 pending identity。两个 WP75 §8.6 与 engine目录 actual after 分别为原规格 `0db98a17ecd51cc69e7ccc307a97e103d5211585016902f669e226a5f6e7ec75`、最终规格 `2968e3946a4ab751fcdb3d2dda241b3e94f6c4e49c04fe07b0494a5d6c9631a5`、最终目录 `328093fecfc874cab446a8b969ca8e78889842643fb5859edb2ddea7dcfd17fc`，正是许可 after。新 route bridge先普通完整求值，再按任一行三个精确前缀判门；命中推进后结束该帧，未命中推进后继续，异常不推进，且保留限定注释/空白/多行案例，不推出编译器/转换器自动执行保证。旧 WP75 资格单列历史批准；新字节独立待门。

唯一保留旧 catalog fixed identity 的 WT07 案例：C/旧NEW行326在NEW2移至332，因插入6个物理行含空行；带换行 row SHA256 `da1ddd7561b88f9d1b85bb498e06d8c6736ea0bd9a199a6e388479e521b2c29c` 完全相同。其固定旧案例证据仍有效，当前331不是该案例行。其它 whole历史 scope/current精确指针分层保持。

**九单位原问题对应与剩余门**

读取原 FULL 八对象的最低修订，而不是接受作者“完成9项”的数量断言：R001读样本资格、R002友好度次序/分支、R003跨图天气/显示边界、R004设施四队伍/快照/结束条件、R005原FD003 roots/extensions/资格与C029、R006精确许可后WP75门/案例、R007收获与L09机制/UI、R00835配置 current consumers/有限资格均有原固定 finding 对象绑定，逐对象规范JSON哈希与原 FULL 相同。R005合并NAV001 FD003/C029及OBS，R008合并NAV001 CFG25/26+SRC392/393，第九 G9-3合并NAV002；未漏原问题，未新增canonicalfinding，未改原owner职责。原 minimum revision 由绑定保留；本报告不给八 FULL finding 作整体质量签名。

本范围无剩余导航/资格阻塞。后续验收仍需父任务将同一 NEW2/tree 的 FULL 和各 affected owner 独立结论合并；唯一登记员授权整合后冻结精确 actual SHA/tree；原独立 ACTR-B21 对新实际字节复审；随后 B21接受/C、原FINAL-1、证据支持的canonical关闭与最终冻结、FINAL-2逐门协调。327旧接受与14待B21、229OPEN/0CLOSED、九原输入限定批准不得提前改变。父任务另负责57路径边界、36837受保护路径及327贡献逐对象保全；此处仅给本委派直接核对/不变复用证据，不以父结果冒充本子审新增阅读。

**固定入口、输出容器及唯一完整差异身份**

| 固定 commit/path | SHA256 | bytes |
|---|---|---|
| `9b6d16e34daf59e205f8a3df20e24930175064ed:review/remediation/20261003-prepare/batches/B21/author-draft-1/freeze-2/frozen-NEW2.json` | `df5de53a22718412e7c30857b244a5a20bd1609726d7c1e4d55067f7cdabee9f` | 47846 |
| `9b6d16e34daf59e205f8a3df20e24930175064ed:review/remediation/20261003-prepare/batches/B21/author-draft-1/freeze-2/review-FULL.md` | `26277ca19d2c6cc7145679efe6b61ee223efc1347b7968c67e7e7dd952f199ac` | 6554 |
| `9b6d16e34daf59e205f8a3df20e24930175064ed:review/remediation/20261003-prepare/batches/B21/author-draft-1/freeze-2/review-affected.md` | `bcf5c3c6ef552878f5822deb0e676c8b28f1b31af6f453d01cd35afa5df74f48` | 5561 |
| `aa57e293bf3a0a77fa42f1f42777df88cbd2fbe8:review/remediation/20261003-prepare/batches/B21/original-scope-grant-R-B21-006-1/scope-grant.json` | `a768aff855c04e0be4754270a68500fd7b2d5b715cf90c86657ebbfa9a60b3bd` | 18923 |
| `e58486178e746273fb6fab55df00722807f1dc44:review/remediation/20261003-prepare/batches/B21/author-draft-1/obligation-map.json` | `12a5003ae60e655f1a70cec40a41428cc5a2a89437f5b587a07c23aeaa348d0b` | 332278 |
| `e58486178e746273fb6fab55df00722807f1dc44:review/remediation/20261003-prepare/batches/B21/author-draft-1/traceability.json` | `e59f578efc610473ce72cbfb50e02fa8b0f128a12bda3b35b763964a3986039f` | 784372 |
| `e58486178e746273fb6fab55df00722807f1dc44:review/remediation/20261003-prepare/batches/B21/author-draft-1/navigation-identities.json` | `ebebbe74d2c644f98e2f42b80f47faa524aaf2bc129c9033d8769e6da251fc5d` | 277133 |
| `e58486178e746273fb6fab55df00722807f1dc44:review/remediation/20261003-prepare/batches/B21/author-draft-1/eight-chains.json` | `7035d443bdce2dd158677f086482744f61b46bd90b559a5d08747f4b3c5e7f0d` | 189727 |
| `e58486178e746273fb6fab55df00722807f1dc44:review/remediation/20261003-prepare/batches/B21/author-draft-1/junction-evidence.json` | `0cbeab25b0f51f608b737427f3d57092b79f5e470829044613d45f8121e34882` | 920255 |
| `e58486178e746273fb6fab55df00722807f1dc44:review/remediation/20261003-prepare/batches/B21/author-draft-1/nine-input-approval-successor.json` | `9c2a34d7ed15738b68d9863c110571d7669ccac0491e1f6c42843bf3e0dca7f7` | 30327 |
| `e58486178e746273fb6fab55df00722807f1dc44:review/remediation/20261003-prepare/batches/B21/author-draft-1/candidate-fix-1/qualified-navigation-repairs.json` | `8d53f068b9a8b733be8615e9d234139603006967cf594ffa87a26a998fae0725` | 37786 |
| `e58486178e746273fb6fab55df00722807f1dc44:review/remediation/20261003-prepare/batches/B21/author-draft-1/candidate-fix-1/repair-static-cases.json` | `9033064bd280b30a09efdc63f02311a17ae27e3b29ef28053bf755d8c25441ec` | 4844 |
| `e58486178e746273fb6fab55df00722807f1dc44:review/remediation/20261003-prepare/batches/B21/author-draft-1/candidate-fix-2/nine-unit-repair-map.json` | `790978879fc9b6b63c6de53f4ff62de5a0acb057813eb2d0155947739bcec166` | 19054 |
| `e58486178e746273fb6fab55df00722807f1dc44:review/remediation/20261003-prepare/batches/B21/author-draft-1/candidate-fix-2/dependency-refresh.json` | `1c488b6c0a1b8eb88ab9d5a50fc5174ab91bd83139e58d4c3130bca91605e31b` | 48544 |
| `e58486178e746273fb6fab55df00722807f1dc44:review/remediation/20261003-prepare/wp78-junction-successor.tsv` | `a87413465b6f6e64762287158ae98f4e844724f79a34d2fb868536769e7018dd` | 320527 |
| `e58486178e746273fb6fab55df00722807f1dc44:review/remediation/20261003-prepare/wp79-source-successor.json` | `523f0c50c939a23e5b232e0be0cfe3ee54fc3cd557dba631cd566cd4685a440e` | 631086 |
| `e58486178e746273fb6fab55df00722807f1dc44:review/remediation/20261003-prepare/wp79-config-successor.tsv` | `dc6ac8972bf8351554fc648ae79d5345ea0a65d8e8cc031a83a528118872abd7` | 48923 |
| `e58486178e746273fb6fab55df00722807f1dc44:review/remediation/20261003-prepare/wp79-ui-successor.tsv` | `926ce5169faf1591875a4df9946541f211e84fd4f11506b7d060bc428cc1f973` | 23487 |
| `9b6d16e34daf59e205f8a3df20e24930175064ed:review/remediation/20261003-prepare/batches/B21/author-draft-1/freeze-2/complete-C-to-NEW2.diff` | `0213e85fbe687500343f9e3848b49650bafdb7a726cac8beb54f083ee7e41b15` | 4541616 |

伴随 JSON 为本轮新审计元数据和逐对象结果，包含全部47映射、14 whole资格保全、54交界、8链、九单位绑定、111 current consumer身份、151条款/案例哈希及220 scoped旧对象结果。未发布完整批准controls cache、未复制完整差异、未递归复制历史材料。
