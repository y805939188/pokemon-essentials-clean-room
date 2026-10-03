# WP21／WP24／WP25 有限闭合复审

日期：2026-09-26（Asia/Shanghai）。独立 reviewer；Reference/Audit 侧材料，非 WP80 sanitized 产物。S = `reference/pokemon-essentials/Data/Scripts/`。

**结论：WP21 PASS_SCOPED；WP24/WP25 继承 PASS_SCOPED，本轮回填接受。WP21-R03 最后剩余规则 CLOSED，BATCH-C02 CLOSED，未发现直接回归，无剩余修订要求。** 其余11个必修项及C01继承关闭，WP01–WP20既有批准范围保持。

**可以开始下一步：先将WP21管理性回填Reviewed，再执行WP26→WP27→WP30三包，逐包自检、固定版本，批末统一送审。** 配套 [回填与下一批执行提示](next-batch-prompt.md)。本reviewer只交付报告与提示，没有代回填或执行新包。WP22/WP23尚未完成，不应将进度概括成“WP01–WP25全部通过”。

## 1. 本轮实际版本

| 对象 | 完整 SHA-256 | 字节数 |
| --- | --- | ---: |
| WP21 v3 `specs/pokemon-rules/wp21-dynamic-forms-and-display.md` | `4e475505084a01f3c9ab26fbb0f863672a59e38b1ade9788efd445745ecff1af` | 42037 |
| WP24回填后 `specs/creature-rpg/wp24-player-trainers-partners.md` | `325940946f7b120c4e484695dd35c5804c2baf9411798d95c22af2f944a2e7e5` | 29668 |
| WP25回填后 `specs/creature-rpg/wp25-party-and-storage.md` | `46bd905d6ee011b0b2da67db418d06ebcc81309251794bdca3e81ed2fbf83941` | 27081 |
| feature-matrix | `e0762970951548e3f52f38413a1d3939a8b2594afaf4c5f164241ea414bdf448` | 39590 |
| manifest | `435af340811e73a69c7947c1c379b64ee83eb4f38506d5c32fe1e6ba65505958` | 92392 |
| 提取侧交付摘要v3 | `62d8a2c8c96e4250e99ad92b02758cb5efde83618b2dabdc5ecc990a79d96d52` | 12088 |

实测与用户提交一致。149条manifest完整哈希/字节记录、53条交付TSV记录全部匹配，固定158项输入。五份提交diff均可从上轮固定快照在内存中精确重建当前字节；未发现原reviewer报告/提示/检查被覆盖。

输入与差异保存于 `input-manifest.json`、`input-snapshot/`、`current-hashes.tsv`、`changes-from-v2.diff`、`diff-checks.json`。字节匹配仅证明版本身份；下面的通过依据是原问题与直接传播的静态源码核对。提取侧回应不代替独立外审。

## 2. WP21-R03 最后剩余：当前PP钳制 — CLOSED

**被审位置**：WP21 `4e475505084a01f3c9ab26fbb0f863672a59e38b1ade9788efd445745ecff1af`:187、194、247、323–324。

四处均已统一为：同一招式对象直接换标识时保留槽位及PP提升计数，当前PP按新招式总PP钳制，不自动回满；通过WP20 §5.4引用主规则。原错误的“当前PP无条件保留”没有留在这些传播位置。

本轮重新核对：

- `S/014_Pokemon/001_Pokemon-related/001_FormHandlers.rb:237–262`：ROTOM找到旧形态招后的直接换标识入口；同文件:658–668、678–688的战斗专属招直接替换使用相同赋值语义。
- `S/014_Pokemon/004_Pokemon_Move.rb:24–26,44–46`：标识变更后当前PP按新总量钳制，提升计数不重置。
- `reference/pokemon-essentials/PBS/moves.txt:2964–2970,8303–8309`：AIRSLASH基础PP15、HYDROPUMP基础PP5。

正常登记数据、ROTOM唯一旧形态招为AIRSLASH、未掌握HYDROPUMP、提升计数0，直接经过提交处理器设形态2且之后不另行重建招式列表：

| 旧当前PP | 新招式总PP | 静态结果 |
| ---: | ---: | --- |
| 15 | 5 | 当前PP为5；原槽位与提升计数保持 |
| 3 | 5 | 当前PP仍为3；不回满 |

新场景给足上述前提，预期正确。交互替换的新招式状态、放弃不回滚形态、KYUREM删除跳项、CALYREX对照和ROTOM最终保底失败等已接受部分没有被无关改写；不重开这些分支，也不改WP20。

## 3. BATCH-C02与WP24/WP25回填 — 接受

| 维护点 | 当前修改与核对结果 |
| --- | --- |
| WP21球字段 | :222明确重置为普通球POKEBALL而非置空；与`004_UI_Evolution.rb:5–19`一致 |
| WP24伙伴道具再查询 | :165明确实际查询键未命中才为空，另一版本可被命中；与`015_Trainer.rb:79–83`的查询语义一致 |
| WP24元数据/刷新 | :201说明回退记录1后仍无记录才拒绝；:261覆盖跳过/成功/失败三种刷新结果，保持先写入和不保证回滚；与`004_Player.rb:60–64`、`017_PlayerMetadata.rb:45–48`、`008_Game_Player.rb:104–117`一致 |
| WP25目标条件 | :217–218分开空格放下与已占用格交换，保留空目标不构成交换成功的条件；与`017_UI_PokemonStorage.rb:1784–1791,1813–1818`一致 |
| WP25墙纸工具 | :226分开基础pbDelete与全局墙纸工具，明确基础对象没有unlockWallpaper同名方法；与`004_PokemonStorage.rb:96–99,254–259,299–301,367–381`一致 |

**BATCH-C02 CLOSED。** 维护限于上轮允许的条件和场景同步，没有扩大包范围。

WP24/WP25的头尾Reviewed登记、矩阵F07-02～F07-05的对应子范围、相互引用和WP21前向引用均与上轮批准范围一致。真实行为通过版本分别仍是：

- WP24：`8b06ddc4ea038867c10d9e300af240b7222f975f1c379d49e9b10ec354430e12`，28865字节。
- WP25：`98b52717874d7a25f18e06b561022d8c802d7eff71e82389f0d6401deb6cb11d`，26359字节。

本轮接受回填及维护后的字节，不倒称这些新哈希是上轮被审对象。上轮已关闭的其余11个必修项及C01继承，WP01–WP20限定Reviewed不变。

## 4. WP21通过范围与登记

WP21可登记 **Reviewed（限定静态范围）**：已述形态登记/查找/替换/复制机制，固定注册及取值目录；已述创建/读取/提交/战斗触发接口与直接副作用，锁定/限时形态；直接换招、交互学招和删除路径的已述区别；标记、缎带与华丽大赛属性的已述读写/展示/失败边界，以及Beauty和复制接收交界。

该结论由首审已接受部分、上轮关闭项及本轮最后闭合组成，不是本轮重新提取完整领域。Mega/Primal/Shadow完整生命周期、战斗/进化/遗传组合、专门UI、完整华丽大赛、Demo可达性及运行环境仍按具名前向范围和未决保留。

提取方可据此回填WP21头尾与F06-07对应子范围，并同步引用其“尚未外审/ReviewPending”的必要位置。保存本轮完整被审哈希、回填后哈希/字节和管理性diff；纯状态回填无需再等一轮全文复审。

## 5. 下一批：WP26→WP27→WP30

依 `planning/extraction-plan.md` §5及§2.1安排三包，所需已完成输入均有相应限定通过依据：

| 包 | 主题与Feature | 计划依赖 |
| --- | --- | --- |
| WP26 | 赠送/获得与脚本交换；F07-06、F10-05 | WP25、WP08 |
| WP27 | 背包、PC物品与登记；F08-01、F08-02 | WP03、WP24 |
| WP30 | 经验/等级/学习替换与友好；F09-01、F09-02 | WP19、WP20、WP24、WP06 |

三包按该顺序串行自检、固定版本，批末统一外审；顺序不是新增包间硬依赖。WP26补“生物—队伍—储存”的获得入口检查点，WP30定义成长主规则，WP42后续闭合战斗触发/等待/当前参战状态更新。Shadow暂存与恢复按计划保留WP23交界，不能借前向引用隐藏本包正确性必需的输入。

WP22/WP23仍有未闭合战斗/成长依赖；WP28还需要WP30/WP31等输入，留后续。WP29在WP27完成后也可推进，但本批限定三包，不将它另造为被WP30阻塞。完整执行范围与停止点见配套提示。本会话不代执行。

## 6. 基线与执行边界

参考HEAD仍为 `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`，describe `v21.1-23-g8c5911e4`；普通状态为空，ignored为`.DS_Store`、`PBS/.DS_Store`。本轮局部阅读10个相关源/数据路径并与固定commit blob核对；前轮28个已检查路径的字节身份未变。见`source-checks.json`，哈希不代表全文语义或运行覆盖。

只新建本轮review目录；未修改原规格、计划、矩阵、manifest、提取侧材料、旧review或reference。未运行参考代码/表达式、游戏、解释器、编译器、转换器、插件、网络或真实地图/存档/输入，未创建任务/并行Agent。

Demo、宿主、媒体、插件组合、U01–U10及WP78→WP79→WP80阶段出口继续保留；本批通过不等于最终sanitized规格或完整运行兼容。静态验收和收尾稳定性分别见`static-checks.json`、`final-checks.json`。
