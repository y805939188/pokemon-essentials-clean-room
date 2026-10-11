# B21 CFG-25/26 空消费者导航补充判断

被审 NEW `5c3e19831e1e29450247fa6061f3c2feac2f893e`；基线 C `e9c140dc33de1cb0662521318b051174909e4509`。结论：将 CFG-25/26 及对应 SRC-392/393 并入既有 `B21-NAV-01` 导航返修，资格、样本及启用限定保全仍 PASS。此为同一导航阻塞的补充实例，不另开独立阻塞。

判定依据不是字段空本身：两行 mechanism_scope 正向指定真实消费机制，旧绑定仅指固定 C 的 v4 配置历史对象，而两个新 config 行及两个对应 source 行均没有当前 consumer 路径，source 的 assigned_control_ids 也为空。当前正文确实有下述消费者；具名旧机制文字足以保留原范围，不能替代本次有限交付要求的精确当前关联。小写 wp 机制标识与空结果相符，但未见生成器证据，不声称已证实大小写正则是原因。

合同固定 `eb1885265fcde2a52767077de3193862036c3a71:review/remediation/20261003-prepare/batches/B21/refreeze-after-B20-C-1/global-closing-requirements.json /required_finite_outputs/3` 要求 reconcile432/52 with implementation-neutral current consumers、approved/deferred 状态及 current limits；文件 SHA256 `549599c6639f5222c44d53ad5fd439be1f20a581572b33a3d92154a7cfcc6d8f`。

| 位置 | 原历史对象 SHA256（独立重算相符） | 实际当前消费者条款 |
| --- | --- | --- |
| CFG-25，第25数据行；SRC-392 = source /rows/391 | `0815952c8fe7115b6efd342c450342b1cfe13869f65f733c0aa83e1708493ff6` | WP31 §2 line15/§9 line239；WP33 §5.1 lines115–118/§5.4 lines143–148；WP35 §3.1 line51/§3.2 line56；WP55 §2.5 line99；WP47-B 附表§2 line64与主稿§5.1 line114。WP76 §5.5/5.6属具名样本/调用者范围，须与机制及启用分开。 |
| CFG-26，第26数据行；SRC-393 = source /rows/392 | `77ac5dfe519882ca3db1dd447bb8b5829ff8b22509d32a7e4f6dbefd30141ad3` | WP22 §2 line15/§3 line27/§5 line68及 transformation-data §1 line7/§2 lines64–65；WP31 §9 line239；WP32 §2 lines13–30/§7 line117及附表§2 line108（YAMASK1→RUNERIGUS，EventAfterDamageTaken 2）。 |

SRC-392 固定参考 PBS/pokemon.txt blob `39aa345a49b40ba835abeb3c3d1a29ab67850986`、SHA256 `5f0197ff85ddb82cfb218d4faaee844bbbd1d36eef4d96bc5703856b4865c4d2`、1235856 bytes；SRC-393 PBS/pokemon_forms.txt blob `08ae264e420484e31a81087eb3125d6f0c7fdaf6`、SHA256 `e50496e31f618917501e5d34d7b8d18f17d1354bbaa3683766a77122fe106716`、109322 bytes。参考固定 commit `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`；原始字节身份核验没有宣称全量内容读取或编译启用。

全部52配置/UI行复核：35配置中仅 CFG25/26 空，17 UI没有空。全部432源码行复核：共36空，分为15 FILE_IDENTITY_ONLY、9 OPAQUE_IDENTITY_ONLY、10 INHERITED_NAMED_IMPLEMENTATION_BOUNDARY_ONLY及本次2个正向机制项。前24是文件/opaque身份范围；后10继承旧具名实现边界及固定旧对象，不作新的全文件行为覆盖声明，包括文件混入、RPG sprite、animation sprite、screenpos、tileset/autotile、图片窗口/plane、物品/宝可梦精灵辅助。保持其限定而不据空数组直接判阻塞；也不能把边界解释为动画或资源消费者整体被排除，真实 owner 既有行为资格仍在。各空项独立分类及旧绑定见同名 JSON。

修订验收：明确加入上述 CFG 与 source 的当前文件/条款/trace关联；保留机制、样本、内容、启用四层限定，仍不声称全量数据、当前开关或 Demo 已运行。对全部52/432逐范围检查，避免把 opaque 或真实实现边界升级为新的语义覆盖承诺。重新冻结并复审。

下列当前条款原始字节 C→NEW 均相同；身份足以复现定位，不复制正文：

| C:path | clause | SHA256 |
| --- | --- | --- |
| `e9c140dc33de1cb0662521318b051174909e4509:deliverables/final-specification-set/pokemon-rules/wp31-basic-evolution.md` | §2 line15; §9 line239 | `d1074da2561c8ab5e5db894f3db7072ad116e6c86a4c2d925a57aa15a6f64948` |
| `e9c140dc33de1cb0662521318b051174909e4509:deliverables/final-specification-set/creature-rpg/wp33-daycare-and-breeding-session.md` | §5.1 lines115–118; §5.4 lines143–148 | `eb80057290a702e697f490ea05526b7c6a505fadb90d75e097b7c942997e52cc` |
| `e9c140dc33de1cb0662521318b051174909e4509:deliverables/final-specification-set/creature-rpg/wp35-eggs-and-hatching.md` | §3.1 line51; §3.2 line56 | `6588053937fe96b256ef136793377d47ea2254d2839fa15b3b90c4f170d86608` |
| `e9c140dc33de1cb0662521318b051174909e4509:deliverables/final-specification-set/combat-requirements/wp55-facility-session-and-restoration.md` | §2.5 line99 | `2a6331ff0d96ff579e93b4a19dde0caf877f3eb30f98c5bd514aaa5b03b53be1` |
| `e9c140dc33de1cb0662521318b051174909e4509:deliverables/final-specification-set/combat-requirements/wp47-b-control-items-coverage-data.md` | §2 line64 | `3a4b189f23a82dae95b0750ca6967d168ee85afe6e27594e00e6d183f4a63827` |
| `e9c140dc33de1cb0662521318b051174909e4509:deliverables/final-specification-set/combat-requirements/wp47-b-switching-control-and-item-changes.md` | §5.1 line114 | `a27cb39a6446e724b42bbb2493076e1f69cb7474a6436f8c6253b355829837c5` |
| `e9c140dc33de1cb0662521318b051174909e4509:deliverables/final-specification-set/pokemon-rules/wp22-mega-and-primal-reversion.md` | §2 line15; §3 line27; §5 line68 | `33bf91ba9936aeb7f7fd94087df3796f883b2b75f94eb4994b7b13e22305b8e3` |
| `e9c140dc33de1cb0662521318b051174909e4509:deliverables/final-specification-set/pokemon-rules/wp22-transformation-data.md` | §1 line7; §2 lines64–65 | `022525f7e3899f60b9523147f68ca8d0d06828d55f8d80dc222490dd7a02e20d` |
| `e9c140dc33de1cb0662521318b051174909e4509:deliverables/final-specification-set/pokemon-rules/wp32-contextual-trade-and-post-battle-evolution.md` | §2 lines13–30; §7 line117 | `4ee97f16827c2615e63506f0ca4a231f6b9f4b6fdb09e335c8add7792984f384` |
| `e9c140dc33de1cb0662521318b051174909e4509:deliverables/final-specification-set/pokemon-rules/wp32-context-inputs-and-scenarios.md` | §2 line108 | `3da7f524023bd749a0c515b03e96134a9635e911c7f6c692f7e9a415dce3663b` |
| `e9c140dc33de1cb0662521318b051174909e4509:deliverables/final-specification-set/demo-dx/wp76-facility-content-generation-and-simulation.md` | §5.5/§5.6 lines94–110; sample/caller qualification remains separate | `13a9aabe2ac4a7b3c3c0aa70f44cc45ca00738a7f80d187962b9e8cb0fff0acf` |

## 新输出精确行与旧 v4 上下文

NEW `5c3e19831e1e29450247fa6061f3c2feac2f893e:review/remediation/20261003-prepare/wp79-config-successor.tsv`：CFG-25物理行26、CFG-26物理行27（标题后数据行25/26）。源容器 NEW `5c3e19831e1e29450247fa6061f3c2feac2f893e:review/remediation/20261003-prepare/wp79-source-successor.json`：如下固定行。原 v4 `/rows/24` 与 `/rows/25` 均明确 `已覆盖（机制与数据样本）`，不是 NA 或 deferred；其四个 file/mechanism/sample/activation 字段与当前 TSV 逐字相等。保留这些旧限定不等于完成新的当前消费者关联。

| 新位置 | NEW source row规范对象 SHA256 | NEW source navigation_id行 / 空consumer行 | NEW parsed CFG row规范对象 SHA256 |
| --- | --- | --- | --- |
| CFG-25 / SRC-392 | `4f70705937b9da5493d2103cfe4b6922fc742bc60217f70b3fa346fefbe54dc8` | 10668 / 10679 | `7b6723b2daeec8f031722b756f687a1acf3f5ebf6611e094599f9578d3713743` |
| CFG-26 / SRC-393 | `debb8ccaf1cd375e087b4aadbb6da3ae7740ef5f7bb09ef50c1a1702f2460206` | 10689 / 10700 | `2ac9167cc0fe479b76608b41e807f15e33f1eb3a4067c682202b94cfbc51014b` |

规范 JSON SHA 算法：UTF-8、ensure_ascii=false、sort_keys=true、紧凑 separators=(comma,colon)；CFG hash针对CSV解析后的全部字符串字段，source hash针对原JSON整行对象。

| 固定容器 commit:path | Git blob | SHA256 | bytes |
| --- | --- | --- | ---: |
| `5c3e19831e1e29450247fa6061f3c2feac2f893e:review/remediation/20261003-prepare/wp79-config-successor.tsv` | `8c5929f12aa085bd88aa7df2bec902e17ac87718` | `e631bcf69236db493ed10754fe55afe1d518dfd4389e65f68d2f965b3aadd944` | 46883 |
| `5c3e19831e1e29450247fa6061f3c2feac2f893e:review/remediation/20261003-prepare/wp79-source-successor.json` | `d5ed465adfe37c0cdde6e060a2f84248facd8dbb` | `ab5b39f35cfbdbdce75d08b69df1b2734a8a9de4c61f99ff43c368ed624496e0` | 601928 |
| `e9c140dc33de1cb0662521318b051174909e4509:review/wp79-coverage-review-2026-10-03/revision-v4/config-details.json` | `972ecbd9790d5e9129d572ac473d2f9250149b0e` | `28ff127f1fcaf52c9a9410416db13a432f1c6c4f3338fd5f45c24c96a91af577` | 17936 |
