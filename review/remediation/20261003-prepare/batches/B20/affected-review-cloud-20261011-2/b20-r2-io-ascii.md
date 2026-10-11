# B20 NEW2：C024 阶段 IO 与四前缀 ASCII 的独立有界 affected 再审

结论：**BOUNDED_STATIC_REPAIR_PASS_IO_AND_FOUR_PREFIX_ASCII**。固定 NEW2 `3f521e6dea0b442e4bb174a9715c458416386b37` / tree `49f406a6de8ca2786e5dda27abada19780fdfa05` 已在本报告负责的两个修复组内解决旧 FULL 的 `B20-FULL-CLOUD-F01` 和 `B20-FULL-CLOUD-F02`；未发现这两个修复引入的剩余局部阻塞。这是受影响消费者有界再审，不签 FULL、actual、正式接受或全局 WP80 ID 关闭。C003/C028/C029 的质量结论由同次复审的其它专责报告决定。

入口是 `81d3be653e87e6424d0d8cd38dab14a9aafc97a1:review/remediation/20261003-prepare/batches/B20/author-draft-1/candidate-review-2/affected.md` 及同目录 `repair-navigation.json`；活跃案例固定 `bfc6264bf47478bd174412289de2e31f4da2d9a6` 的 `author-draft-1/candidate-fix-1/five-group-static-cases.json#/static_cases/1` 与 `/static_cases/4`，文件在 NEW2 字节相同。入口/作者完成标记、许可及 12/10 子例数量均未用作质量通过依据。原 qualified 合同的完整 C024 根判决/最低修订及 WP80 的已裁决 C02 扩展由 `41fffb540c6483f5296ea0d33b789b75180d27ed:review/remediation-20261003-prepare/finding-acceptance.json` 对应完整对象承接，未用标题代替限定。

## C024：阶段顺序与失败前已经发生的变化

NEW2 formal WP75:48、282，original WP75:304，目录 B20-C024:273 及活跃案例 60–190 行一致：数量门通过后才创建/清空树；逐节生成目录/散文件；全部成功后才写备份；备份完成后才替换装载器。编号仅是目录/文件名布局，没有独立索引文件。正常收尾既有条文保持，新增失败边界未反转原稿正确方向。

独立阅读固定参考 `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b` 的 `scripts_extract.rb:12–66/71–74/154–179/182–183`、`scripts_combine.rb:76–117/182–183` 与 README:23–28，静态核对各门及操作顺序。提取实际活动入口和合并实际活动入口分别保留；提取 9 拒绝、10/11 放行，合并 9/10 放行、11 拒绝。放行只意味着继续后续 IO，合并通过门后从目录重新聚合、丢弃旧归档列表、不备份直接覆盖，没有“同方向重跑必安全”的推论。

逐项评定全部十二个静态子例，结果如下；均 **NOT_EXECUTED**：

- 六个数量对照与真实活动入口、各自守卫一致；11 节合并在聚合/写出之前拒绝。
- 清树成功、首个普通非空节前无目录标记且文件打开未创建该文件的失败：旧树已经删除；备份阶段未到，原 B0 保持原值，原无备份仍无；原归档 A0 尚未替换，无装载器。此例准确重现原 F01 的失败边界，不能提前推出已建新备份。
- 清树中途失败允许旧对象部分删除，后续阶段未到；后续目录/文件失败保留新输出前缀，失败文件本身可有部分写入。没有全局回滚或异常必清理保证。
- 备份阶段失败时新输出树已成，备份可已截断/部分写；装载器阶段未到、原归档尚未替换。装载器写入失败时备份已成，原归档本身可被截断/部分写，不保证形成有效装载器。

formal §12.1/原稿 §12.1 的新增条文与正常收尾并存；合并 §12.2 的内容仍逐字不变（插入行造成位置移动，按节界对齐比对，未误用原行号）。局部验收条件：顺序纠正、没有虚构索引、原失败反例/邻近正常和反向矩阵、部分写入而无回滚承诺，以及正文/目录/活跃 JSON 一致，均已满足。

## 四前缀：码点、识别门与独立登记身份

NEW2 formal WP75:26 的四个正向输入 `item:X`、`hiddenitem:X`、`Battle:`、`Type:` 冒号逐字符核对为 **U+003A**；出现 U+FF1A 的四个例子都被明确称为不匹配负例。original WP75:52/85–94/121 已有准确 ASCII 定义，仍不变。NEW2 目录 B20-INTAKE-R01:287 与活跃 JSON 474–590 行同步给出冒号码点和大小写对照。

参考 `004_Compiler_MapsAndEvents.rb:480–499/520–529/562–580/780–807` 支持四前缀的实际收集/解析边界：道具球前缀与两个训练家前缀大小写不敏感，但合法页、登记资料、有效 Battle 均为独立门。逐项评定全部十个子例，均 **NOT_EXECUTED**：

- POTION 已注册及页合法时，item/ITEM、hiddenitem/HiddenItem 均进入相应前缀识别；仅换为 U+FF1A 则不匹配。注册 ID 本身仍由数据身份合同另判，未凭正则前缀的大小写规则创建自动规范化。
- 独立合法 Type/Name 块存在，且没有其它有效 Battle 块时，ASCII Battle/battle 可满足战斗文本门；全角 Battle 不被该门收集，不能由 Type/Name 替代“至少一 Battle”。这不把满足单门写成整个转换/玩家战斗成功。
- 独立有效 Name/Battle 保留，Type 是唯一类型配置块时，ASCII Type/type 可提供该类型，全角 Type 不提供它。案例谨慎保留其它入选块存在，不误断整个收集为空，也不保证后续类型检查成功。
- Move/OppMove 的冒号后前导空白消费与尾随空白保留，Common 对输入名 Hit 立即精确拼接，Trainer 括号、大小写敏感 SellItem、ASCII 逗号及行首小写 s: 各自独立。四前缀不敏感规则没有扩散至 Common、SellItem 或全部登记身份。

旧 CV-M07:150 的“小写必要”字节按保全要求未改；当前 formal:26、B20-INTAKE:287 与活跃案例明确当前前缀不敏感，并把该旧措辞限定为历史条目，不能用它定义本批门。该处理满足旧 F02 要求的“当前适用解释＋旧字节保留”，不以修正旧接受证据来制造通过。

## 受影响 owner 与有界不变证据

未变语义复用固定旧 affected 报告 `680e3988c4144db269e063971991134b8e0bd678` 下 `affected-review-cloud-20261011-1/` 的 B01–B06、B13–B18 和 B19 报告，未复制旧正文或递归引用包。与旧 NEW `1abaefb1db5818ff9404392143c476979d34c21a` 比较，独立核验 **56 个正式输入对象**的 Git blob 不变，并核验改变文件内的 **10 个未变区间/节**；这些身份/区间只支持复用已审语义，未伪称本轮全文重读。精确 commit/path/blob/hash/bytes 与区间哈希均在本报告 [JSON](b20-r2-io-ascii.json)。

| owner | 两个修复组内的实际交界与限定 |
| --- | --- |
| B01 | 作者工具写出/数据身份/编译阶段受影响；WP04 全量编译、PBS 字段和插件顺序未改。旧正式输入及 WP75 §3.1/§3.2 不变，正常编译顺序与工具独立入口仍分开。 |
| B02 | 文件访问/错误层级受影响；新文字准确保留失败前部分变化。WP07 旧合同与 WP74 资源选择器未改，不从文件保护推目录捕获或宿主恢复。 |
| B03 | 四前缀作者输入、生成 Trainer(3)/s: 与运行页消费者有界交界；生成页条件、末页优先、门副作用、转移/跟随者/路线45段不变，不把全角负例扩成新的运行行为。 |
| B04 | 消息/资源消费者有限交界；工具 IO 写出失败不成为统一音画清理承诺，既有消息码/正常资源匹配不改。C003/CN 由另一修复组独立签，本文不扩为整个 B04 零阻塞结论。 |
| B17 | WP67-A 实际动画播放 reader 仍消费独立 Move/OppMove/Common 合同；WP74 formal/original 与 WP67-A/B 正文不变，三条 PA040 行不变。旧 lookup/cache/生命周期限定复用，不把四前缀规则扩为动画 Common 名称去空白/忽略大小写。 |
| B19 | 调试作者入口、登记身份、编辑取消/落盘/缓存与目录有限交界；五份正文输入与17条 B19 目录行不变，旧全120效果/四类数量、世界快照等原接受范围继续由固定证据支持。CV-M07 只获当前适用解释，旧正反向字节保留；本文不签另组 C003。 |

相邻 B06 的道具登记/库存门、B09 的生成训练家战斗命令与 B15 的电话 CommonEvent reader 保持独立。WP75 的 CommonEvent 无独立白名单、EndSpeech 组合可达及 Battle 吞续行条文不变；ASCII 四前缀修订没有新增 CommonEvent 收集资格或改变电话参数。不签相邻 owner 的完整 contribution，未推 Demo 已运行。

CV-M02–07、CV-M11、CV-M26/27、三条 PA040 与17条 B19 行有精确不变哈希。目录全195旧ID/次序/重复次数及308项旧贡献的总核验由本次根报告负责；本报告提供自己消费者范围的增量证据，不仅靠“未改路径”宣称全部 owner 不受影响。

## 固定证据对象

以下每行身份独立从固定 Git 对象读取；不复制完整差异、旧证据正文或参考源正文。

| 用途 | 固定 commit / path | blob | SHA256 / bytes |
| --- | --- | --- | --- |
| NEW2_FORMAL_WP75 | `3f521e6dea0b442e4bb174a9715c458416386b37` / `deliverables/final-specification-set/demo-dx/wp75-project-conversion-and-authoring-tools.md` | `d29ea4f31cf0b076991bf2cfda391c7703cd3040` | `9778e9a4909b492812034b1c687e27360f18fd96052d87067ddf32d455d6b237` / 67289 |
| NEW2_ORIGINAL_WP75 | `3f521e6dea0b442e4bb174a9715c458416386b37` / `specs/demo/wp75-project-conversion-and-authoring-tools.md` | `3796ec9ff81a2b3d41fc42a952167c2925e0ca46` | `e4c9c56c7ddf3c80d69f2911c25d3bfb5e55510f1f6700dc1cd155ecf70ed820` / 86424 |
| NEW2_CATALOG | `3f521e6dea0b442e4bb174a9715c458416386b37` / `deliverables/final-specification-set/test-catalog/demo-dx-wp72-73-74-75-76-77.md` | `d77a72b65a44f8d91b62dd06f0b324e7bfac774a` | `603ee184ceaed66dc6d5f6010542fb84e6a7f4da5d326e61b1227c6ad8ca9eb1` / 102307 |
| ACTIVE_C024 | `bfc6264bf47478bd174412289de2e31f4da2d9a6` / `review/remediation/20261003-prepare/batches/B20/author-draft-1/candidate-fix-1/five-group-static-cases.json` | `1bcabfa4982655b6ccf971dba508e5ea690efc3b` | `14e51d538294bbbe8bfdd10dfd78b1091a99fa5f5ea39d7771dcfacae7196515` / 34659 |
| PRIOR_FULL_F01 | `df1539b67988d4f161b31935752a7f13aec8556b` / `review/remediation/20261003-prepare/batches/B20/independent-full-candidate-review-cloud-1/findings.json` | `f25b14f64ae4dff51f950c09d440601b47a0917a` | `a73c099e5eb775473335586b2c34c78ae45cc3e0e49bbce2eb3d564be385d3e9` / 17541 |
| PRIOR_AFFECTED_B01_B06 | `680e3988c4144db269e063971991134b8e0bd678` / `review/remediation/20261003-prepare/batches/B20/affected-review-cloud-20261011-1/b20-owners-b01-b06.json` | `4c1c87dfe2b3e73bc2b9edb5e18b1ec97ad4abbe` | `04f06aadbe1ebd87e14f6c120052f54fad2ebd6e834e086bdb56dc8f97e36c36` / 81842 |
| PRIOR_AFFECTED_B13_B18 | `680e3988c4144db269e063971991134b8e0bd678` / `review/remediation/20261003-prepare/batches/B20/affected-review-cloud-20261011-1/b20-owners-b13-b18.json` | `d5717c6fc49dcaa4fd4ba29214f7f4a35bf6a65e` | `448a10f100d8c8cc288dd16e9f27323508753d5a400d5060c78b2bee4b87d703` / 15714 |
| PRIOR_AFFECTED_B19 | `680e3988c4144db269e063971991134b8e0bd678` / `review/remediation/20261003-prepare/batches/B20/affected-review-cloud-20261011-1/b20-owner-b19.json` | `ce1c101e0020880d46da4932aeee34c7418eec42` | `db9dc55e624df856a7eb28f2fa7e71fff065933035da1118940d46c181fba9cc` / 30920 |
| SOURCE_EXTRACT | `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b` / `scripts_extract.rb` | `094c156e87e881d585ba0d326264c13e593d2063` | `4ffa2f449c07d492a248f76247d772e4d0b480c8a2a831a359fbf112cbba7d3f` / 7380 |
| SOURCE_COMBINE | `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b` / `scripts_combine.rb` | `56773c9d99fdfbfd8eb36be70a1fc49121ebcbb4` | `ae85c1e8c8de9ef95a33d5523b2311b63c9e758c607bb2c4878952a46bbc004e` / 7380 |
| SOURCE_PREFIX_GATES | `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b` / `Data/Scripts/021_Compiler/004_Compiler_MapsAndEvents.rb` | `cb302adb0c236984c0b4acc5ea61d31c7048dcca` | `3fd9c8c754f3af9bb6204b2492d266fb252cbcd8771593a6650f70601b9b13cc` / 75159 |

活跃 ASCII 使用与 ACTIVE_C024 同一文件、指针 `/static_cases/4`；原 F02 使用与 PRIOR_FULL_F01 同一文件、指针 `/findings/1`。参考固定 tree `7589c800b61ba13a13040ed0d686979b80a84fd0` 且工作树干净；所有程序只按静态文字阅读。完整 C→NEW2 差异重建/发布身份由根报告统一核验及引用，本报告不重复复制该流。

所有22子例均未执行；运行观察和已证明 Demo 链为0。只写本报告与新 Git/JSON/hash/text 元数据到 `/tmp`，没有修改正文、原稿、参考、main、旧报告或接受记录，没有 commit/push 操作。不执行 Ruby、编译器、转换器、反序列化器、行为向量或旧脚本；无 actual/正式接受自签。没有剩余工具/输入阻塞，此两组未发现剩余质量问题。
