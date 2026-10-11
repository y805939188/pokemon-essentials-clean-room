# B20 affected NEW2 独立有界保留核验

结论：`PASS_STATIC_IDENTITY_AND_CATALOG_PRESERVATION`，保留/身份问题 0。此结论只覆盖固定对象、旧接受贡献与目录保留、原稿精确增量边界；不签 B20 整包语义 PASS、FULL、actual、正式接受或 canonical 关闭。作者数量声明、许可与自称完成不作质量通过依据。

## 固定输入和旧独立证据

| 对象 | commit | tree |
| --- | --- | --- |
| C | `de1a1c28a4255ff1cfd59fb6fb96f9be2d6ece1f` | `88a400af08253bea8d97ee2ef2fa6636f0900f92` |
| OLD_NEW | `1abaefb1db5818ff9404392143c476979d34c21a` | `2e40f9ad0e8fa40377d39e5a19eaa74cc2e05e85` |
| repair_BASE | `272885cca76c36cd04dde27b6be2c654759ec4c2` | `46969272b7387645bc97b91d227734e89a5f8a80` |
| NEW2 | `3f521e6dea0b442e4bb174a9715c458416386b37` | `49f406a6de8ca2786e5dda27abada19780fdfa05` |
| entry | `81d3be653e87e6424d0d8cd38dab14a9aafc97a1` | `a9d5db33399fee31780ea6cb6ffa3b5225b927ce` |
| final_author_packet | `dbfa219547690f06eac9180f3ecd9dd1091eb49f` | `59529b00d2a3704251f6622f3b1d7b55a186dfdc` |
| prior_independent_report | `680e3988c4144db269e063971991134b8e0bd678` | `4e2858fe6d52e9b36ede5a54a9ad730c05764108` |
| original_scope | `924c7c3a7a5029b07ad18085cf2dadb594512186` | `3d47ead17dad8bac6775ce49b3ef86513fa594b6` |

入口：`81d3be653e87e6424d0d8cd38dab14a9aafc97a1` 的 `review/remediation/20261003-prepare/batches/B20/author-draft-1/candidate-review-2/affected.md` 与同目录 `repair-navigation.json`。固定最终作者包的这三个入口/路由对象均保持入口 blob。

沿用的独立保留证据为 `680e3988c4144db269e063971991134b8e0bd678` 的 `review/remediation/20261003-prepare/batches/B20/affected-review-cloud-20261011-1/b20-preservation.json`：blob `3f53b569f69097421a1302df3c66d0388cd0eba2`、SHA256 `5612de987509aebf71f432f69fc27a9c30c354adfeec5860a33442265d81da42`、303434 bytes。对应旧保留 Markdown 及四组 owner Markdown/JSON 的固定身份也已逐个绑定；本输出只记录引用和新 metadata，不递归复制旧报告或正文。

原轮已从固定 PLAN、完整 qualified finding/acceptance 对象与 C receipts 独立重建 308 个 `(owner, ID)`、205 个主责、216 个触及 ID。本轮核旧 proof 的固定 blob/哈希、原 PLAN 身份、原对象/批准控制源身份，以及 C 接受容器与各 owner 的旧证据路径/mode/blob：全部保持。因此原轮逐 216 个 whole-qualified 对象、205 个主责哈希、B10–B19 的 158 条本地完整控制哈希仍由相同固定对象支撑；本轮没有用标题或 author map 取代 root/extension、cases、前提、最低修订、确定再检、证据限制及最终全局义务。

## 旧接受贡献与实际增量

| owner | 贡献/主责 | C 旧证据文件数 | NEW2 保留 |
| --- | --- | --- | --- |
| B01 | 14/7 | 46 | 全部旧路径/mode/blob相同 |
| B02 | 12/9 | 66 | 全部旧路径/mode/blob相同 |
| B03 | 27/19 | 106 | 全部旧路径/mode/blob相同 |
| B04 | 35/23 | 121 | 全部旧路径/mode/blob相同 |
| B05 | 16/10 | 76 | 全部旧路径/mode/blob相同 |
| B06 | 10/7 | 130 | 全部旧路径/mode/blob相同 |
| B07 | 19/12 | 98 | 全部旧路径/mode/blob相同 |
| B08 | 17/9 | 187 | 全部旧路径/mode/blob相同 |
| B09 | 20/13 | 298 | 全部旧路径/mode/blob相同 |
| B10 | 7/2 | 95 | 全部旧路径/mode/blob相同 |
| B11 | 6/3 | 142 | 全部旧路径/mode/blob相同 |
| B12 | 9/6 | 155 | 全部旧路径/mode/blob相同 |
| B13 | 8/5 | 249 | 全部旧路径/mode/blob相同 |
| B14 | 24/19 | 247 | 全部旧路径/mode/blob相同 |
| B15 | 16/10 | 222 | 全部旧路径/mode/blob相同 |
| B16 | 24/20 | 252 | 全部旧路径/mode/blob相同 |
| B17 | 12/7 | 83 | 全部旧路径/mode/blob相同 |
| B18 | 8/5 | 94 | 全部旧路径/mode/blob相同 |
| B19 | 24/19 | 90 | 全部旧路径/mode/blob相同 |

合计 **308/205**，**2,757** 个 C 旧 owner 证据对象全部相同；C completion-statistics-successor 的 308 条 receipt 容器在旧 NEW、repair_BASE、NEW2 均为同一 blob。逐 owner 接受绑定、原 PLAN 顺序及正式 write 路径也核验：只 B17/B19 共写的共享目录仍属于既有 C→旧 NEW 变化；其余旧 owner 正式路径 C→NEW2 全同。所有 C 旧路径的变化集合仍严格是原轮七路径，没有新增旧证据删除或修改。

旧 NEW→repair_BASE 独立 name-status 只含 12 个证据追加；repair_BASE→NEW2 全部 name-status 为 33 路径，其中 5 个既存正文/目录变化、28 个新作者证据。旧 NEW→NEW2 的 5 个既存变化如下；其余既存路径全同。完整未过滤差异流的字节核验由本轮 root 单独记录，本分工不存、复制该流。

| 路径 | 旧 NEW blob | NEW2 blob |
| --- | --- | --- |
| `deliverables/final-specification-set/demo-dx/wp75-project-conversion-and-authoring-tools.md` | `8579094c736165428f89b64d2c3a298dc3d0e85c` | `d29ea4f31cf0b076991bf2cfda391c7703cd3040` |
| `deliverables/final-specification-set/demo-dx/wp77-demo-evidence-and-capability-coverage.md` | `3d1ca36c98b662e46d3e9aa257031e71c4f0f123` | `e792348b0a7f35145736f7d595e86ec290b420b8` |
| `deliverables/final-specification-set/test-catalog/demo-dx-wp72-73-74-75-76-77.md` | `a4a5279c9826d87e9663780c6e35a92cc733ffef` | `d77a72b65a44f8d91b62dd06f0b324e7bfac774a` |
| `specs/demo/wp75-project-conversion-and-authoring-tools.md` | `e007c7396d91f99a30b799040e3e030642785604` | `3796ec9ff81a2b3d41fc42a952167c2925e0ca46` |
| `specs/demo/wp77-demo-evidence-and-capability-coverage.md` | `cba9c34c45c31aedb1e3ae58a6b38ecbe39dd3e3` | `64fc5fcf9ace768deaa640cc7f9a4190473785ea` |

两份 WP74（正式及原稿）保持旧 NEW blob。B19 的六个实际输入也按旧独立 owner proof 的固定身份逐一核验：正式 WP72/WP73-A/WP73-B、原稿 WP72/WP73-A 五个正文 C→NEW2 全同，共享目录另核。未变正文只支持保留证据，新增 consumer 条款对 owner 的语义影响仍按实际路由独立判断。

68 个旧作者输出的准确基点是固定作者发布 Q `cd714a3cba8319402ddd81d2bebd8fe1d215003a` / tree `99e32a4bd4d0c1a095216aa5ae515be6a8e335d5`（proposal P 的该子树有 65 文件）。独立枚举 Q 的 author-draft-1 全部 68 个路径，NEW2 全部保持相同 mode/blob；聚合 SHA256 两侧均 `7e385e5b8f13ed7ddb28077709720c6291bdd3a83ce278332b5f94589037900b`。

NEW2→最终作者读回包只增加 13 个作者证据路径，NEW2 全部既存路径/mode/blob 不变。

## 共享目录的旧/新界限

路径 `deliverables/final-specification-set/test-catalog/demo-dx-wp72-73-74-75-76-77.md`：NEW2 blob `d77a72b65a44f8d91b62dd06f0b324e7bfac774a`、SHA256 `603ee184ceaed66dc6d5f6010542fb84e6a7f4da5d326e61b1227c6ad8ca9eb1`、102307 bytes。

直接在内存解析固定 C、旧 NEW、NEW2 的全共享目录：C 的 195 个 ID 等于 NEW2 的前 195 个 ID，原顺序及每项重复次数完全相同；全 214 个 ID 的顺序及重复次数也与旧 NEW 完全一致。原 C 193 行逐字保留；两处原 assigned 修订 AN-M23/CV-M18 沿用旧 NEW 字节，未再扩大。NEW2 的原 261 行前缀与旧 NEW 逐字相同，包括行外文字；只修改追加区的五个 B20 行，不增加、删除或重排案例。

| 旧 assigned 行 | C 行 SHA256，不含LF | NEW2 行 SHA256，不含LF（与旧 NEW 同） |
| --- | --- | --- |
| 126 AN-M23 | `21f86f266d21175a86be08afe2be5376af5fc615ec6c43eabf078148c6a34d4a` | `a69be02b84e60e2df9ad1c16f13cb9b0aac8824d4d468cbfebcc2fe474bb7a63` |
| 161 CV-M18 | `0d56469a3dacab50099d9797f305d562cab0e8ebfbfa5556d59621ec92a438cf` | `0d0104748b1826bb6de583b01dcc8416f65c60e1445be330fe7001e43dbbcf4d` |

本轮只改追加区 B20-C003、B20-C024、B20-C028、B20-C029、B20-INTAKE-R01 五行。B19 的 17 行及 PA040 的三行均保留原 C 的行号和字节。PA040 三行固定行哈希如下：

- 235 `B17-PA040-double`：`44db9b3c35a6aa1792fcea2d4ebcbd4a011e5c7282dac3ff8939bc02884fac0c`。
- 236 `B17-PA040-training`：`56003ac20927c82bae0d3c01e5f0c4715e97e318612e7405c724afc2ae0e5956`。
- 237 `B17-PA040-duplicate`：`1a116b40c05567fc1c1d1370a560bcdbcd7c55a0432ad6efdaefdc9369f4d406`。

全目录唯一显式相对 Markdown 链接按目录路径解析后存在，其 B17 traceability 目标仍是旧 blob。19 个 B20 案例均保留 NOT_EXECUTED。

## 两原稿三 hunk 的独立精确重建

固定许可 `924c7c3a7a5029b07ad18085cf2dadb594512186` 的 `review/remediation/20261003-prepare/batches/B20/candidate-fix-1-original-scope-grant-1/scope-receipt.json`：blob `36ea6e26a6876858cae61b968f2400580dc95709`、SHA256 `3b63ea40281dbe2390180f23c72e513585debc02f44a8b20ad031c20340cdef7`、16978 bytes。许可用于核范围，不用于质量裁决。

分别核固定 repair_BASE/旧 NEW 完整 before、固定 proposal before/after/complete.patch、三组 before/after range 字节及 complete-hunk 哈希。把每组固定 after range 替入独立读取的 before，保留所有 range 外字节，重建结果逐字等于 NEW2 对应原稿的完整对象；实际原稿变化路径恰为许可两文件，无其它 specs 变化。

| 原稿 | NEW2 after blob / SHA256 | hunk |
| --- | --- | --- |
| `specs/demo/wp75-project-conversion-and-authoring-tools.md` | `3796ec9ff81a2b3d41fc42a952167c2925e0ca46` / `e4c9c56c7ddf3c80d69f2911c25d3bfb5e55510f1f6700dc1cd155ecf70ed820` | 1 |
| `specs/demo/wp77-demo-evidence-and-capability-coverage.md` | `64fc5fcf9ace768deaa640cc7f9a4190473785ea` / `46a5e1883baa6c524779f080feb7bec0602f14c3b62b0ff7c2ae41bb4cbb7180` | 2 |

| hunk / 对应贡献 | before→after 范围 | complete-hunk SHA256 |
| --- | --- | --- |
| `wp75-project-conversion-and-authoring-tools-H01` / GIR-FD82-C024 | 301+6→301+7 | `625bb6b752fc4fe6d5e903f817998038b2569b4cc09b99704c1cee976587590c` |
| `wp77-demo-evidence-and-capability-coverage-H01` / GIR-FD82-C028 | 136+7→136+13 | `cb3d0f944044361b55651ab9d2cbede1aa4bb86be7cbc6f5fe7823fe51547bc2` |
| `wp77-demo-evidence-and-capability-coverage-H02` / GIR-FD82-C029 | 162+6→168+12 | `4ae176899e8d8cbbfc273b78f1985370f8fe33778700a0d43d661d2f7542002a` |

WP75 仅追加 C024 分阶段失败边界；WP77 仅改 C028 消费边界并追加 C029 外层门。正确原稿 FormHandlers 局部源审计和全部 range 外内容逐字保持，没有借修复实施旧原稿整体清理。

## 入口与执行界限

repair-navigation 的 39 个记录级固定引用已独立核 commit/path/blob/SHA256/bytes、JSON pointer、NEW2 heading/case 行定位。固定 five-group-static-cases 按案例列表顺序的 3/12/14/12/10 个子例与导航逐贡献对应，已核实际列表长度，合计 51；所有五个 case 及 51 个子例的执行标签均为 NOT_EXECUTED，runtime/Demo 标签均 0。该 metadata 核验不把静态列举当成运行测试，也不采纳作者 quality 字段作为独立结论。

本分工只使用 Git 元数据、有限变更文本和自身新写的 JSON/hash/text 核验代码；未运行参考游戏、Ruby、编译器、转换器、参考反序列化器、行为向量或旧执行脚本。未修改 repository、正文、原稿、main、参考或旧证据，未 commit/push。

保留/身份门无剩余问题；候选质量、实际 B01–B19 路由的五组修复正确性及有界语义回归由本轮独立语义复审合并判定。本分工未自签 actual 或正式接受。全部新逐路径/blob、range/hash、owner 聚合及入口记录见 [b20-r2-preservation.json](b20-r2-preservation.json)。
