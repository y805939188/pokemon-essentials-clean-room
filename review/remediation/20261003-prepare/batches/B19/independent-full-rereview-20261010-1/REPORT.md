# B19 FULL 24/19 独立修复再审

结论：**BLOCKED_SCOPED**。24 项贡献、19 项主责全部逐项覆盖；21 项贡献 / 18 项主责获得本地范围支持，3 项贡献 / 1 项主责仍阻塞。这是固定修复候选的独立质量结论，不代签整合后 actual、ACT、正式 C 接受或全局关闭。R07 仍为补充质量问题，不归入 C016，不新增 canonical finding。

## 固定对象和入口

| 对象 | 完整 commit | tree |
|---|---|---|
| 修复 NEW | `afb97d4dc161594d36b7dcebe35155a206ceb511` | `c5075947e57fb1795c12fc35093c45bfe139314f` |
| 派发发布包 | `69f05c26facc42c3a47c4f0d86b16eb8e0711229` | `9aabcec9292ebaa574fdc27d0be3bf710a904994` |
| 发布包读回证据 | `71090724c21f379dede97b3b8f5ca834f916962a` | `16b72dd28c5547371e3f8092c9db1b6048d2b571` |
| grant3 范围许可 | `d90043962356c3d960daf1a2bc21a7f84086c66b` | `77c12ea44f0b6a3b54fe2b5ad846f76e35e5d414` |
| 原 NEW | `dfe8e726669a83c751d02e923cf290bdafc82bd7` | `b830a49ad76369d19ebaae227aaf190ca5542069` |
| B18 C | `52f24036d09503144c6ec89960029db4ed370734` | `3b20f8f2c0dab0ef3e2867aa2bac0fa98497c44b` |
| 先前本审报告 | `0fb4acd6ce8532436c016ab939532e30a13a3f07` | `07fa69fed79d7087a4302b8bf99a45a5c5a8a373` |
| 静态参考 | `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b` | `7589c800b61ba13a13040ed0d686979b80a84fd0` |

仓库 `y805939188/pokemon-essentials-clean-room`。先读固定入口 `review/remediation/20261003-prepare/batches/B19/author-draft-2/repair-1/complete-candidate-1/publication-1/README.md` 和 FULL 派发 `review/remediation/20261003-prepare/batches/B19/author-draft-2/repair-1/complete-candidate-1/publication-1/FULL-24-19-recheck-dispatch.md`，读取原合同、完整 qualified 控制与 grant3。grant3 仅精确授权原稿范围；其通过不构成质量通过。模型请求接纳有效，未审计额度、参数回参或改用 CLI；无可信后端回参时按 Plan A 标为 UNVERIFIED。

## 完整差异、控制和保全

独立重建两条**全仓未过滤**差异，均使用 `git diff --no-ext-diff --no-textconv --binary --full-index`。没有路径过滤，没有运行旧脚本，没有复制已有完整 diff 到新报告。

| 差异 | bytes | SHA256 | 全部变动路径 |
|---|---:|---|---:|
| 原 NEW → 修复 NEW | 836807 | `840829cfe203bb818f8f553b7c485c849a74884ac5a369bbc5ecbe3ee9934105` | 37（7 payload M + 30 B19 metadata A） |
| B18 C → 修复 NEW | 2566830 | `b3838c64e0aa7014b663059e1b970a071e1ce48f89e293ab93d437da0d554005` | 64（7 payload M + 57 B19 metadata A） |

第一条与发布包 `69f05c26facc42c3a47c4f0d86b16eb8e0711229` 中唯一现有完整流 `review/remediation/20261003-prepare/batches/B19/author-draft-2/repair-1/complete-candidate-1/publication-1/full-unfiltered-OLD-NEW-to-repair-NEW-repository.diff` 字节一致，blob `cbf17ec5ef104a943911f164ecbd99e73e2380b5`。第二条也匹配固定声明的哈希/路径。完整路径和逐文件身份在 [evidence-verification.json](evidence-verification.json)。完整流仅引用，不递归复制。

72 项 before/review 输入身份、23 项不可变证据、7 个 payload 的 blob/SHA256/bytes 均独立核对。完整 findings 与 approved acceptance 的 24 个对象经 canonical SHA 和逐对象相等检查，包含最终优先序、roots、extensions、premises、evidence_limits、以及 C007 effective_case_constraints。当前 45 个正文范围及 65 个目录引用重算哈希一致；身份一致不代替语义质量判断。

grant3 的 9 条原稿修改逐条按声明重建，3 个原稿恰好等于获许可结果，未声明修改为零。178 个基线案例、195 个原/修复候选案例的 ID、顺序和重复度保持。repair 改变原候选 9 行；此前未分配 149 行中仅 WE-M17 属新补充修复，另 148 行字节一致。三份 B18 目录、Tile、35 项跨 owner consumed inputs 完整字节锁通过。R05 的 DG-M07、DG-M11、DG-M19、DG-M21、CE-M20 五条明确前提/结果及反例恢复，且准确的新纠正仍保留。详见 [preservation-check.json](preservation-check.json)。

完整效果白名单重新静态核对 120 项：BATTLER 83 / SIDE 22 / FIELD 13 / POSITION 2，类型、登记默认、范围、重置、层和中性行为含义匹配；41 项注释排除身份和所有表外状态仍不可用。120 完整行与原 NEW 字节一致；E088 登记 −2 与显示比较基准 −1 已分开，当前 −2 为绿色、−1 为普通颜色，范围 −1..99，ACTION 重置 −1。[effects-independent-check.json](effects-independent-check.json) 给出逐项新静态核验；[evidence-reuse.json](evidence-reuse.json) 绑定旧固定证据与当前字节相等，未移植旧结论。

## R01–R08 结果及精确阻塞

R02、R04、R05、R06、R08 和 PC 词误修复在分配的本地范围得到支持。R01 的资格过滤、保留原表达式求值、空 token 局部失败、写槽→立即重绘求值→正常返回后请求地图刷新已修复；R03 的旧签名/类路由/内部元组多数已中性化；R07 第一缺口停止及三组枚举前提已修复。以下残留阻止 PASS_SCOPED，完整判定和最小修订见 [repair-review.json](repair-review.json)。

### R01：求值异常救援范围仍写得过宽

NEW 正文 `deliverables/final-specification-set/demo-dx/wp72-debug-contexts-and-controls.md:64`、原稿 `specs/demo/wp72-debug-contexts-and-controls.md:82`（及原稿 M06 第338行）、目录 `deliverables/final-specification-set/test-catalog/demo-dx-wp72-73-74-75-76-77.md:16` 仍把获准求值的异常统一归为 nil/`[-]`。固定来源 `Data/Scripts/020_Debug/003_Debug menus/003_Debug_MenuExtraCode.rb:85–103` 使用裸 `rescue nil`。

静态最小反例为名称 `s:1+1=2`：首段按 `=` 分割得到 `1+1`，非字母首字符获准；求值仍使用完整原表达式 `1+1=2`。官方 [SyntaxError 文档](https://docs.ruby-lang.org/en/3.0/SyntaxError.html) 将此列为无效语法，[默认 rescue](https://docs.ruby-lang.org/en/3.0/syntax/exceptions_rdoc.html) 仅处理 StandardError 及子类，[ScriptError](https://docs.ruby-lang.org/en/3.0/ScriptError.html) 不在其内。因此局部 SyntaxError 逃逸，不能给出 `[-]`。未执行表达式；宿主异常画面、进程结局和恢复未知。

最小修订：限定可被局部救援的运行时错误范围，并保留未被救援的语法错误传播；增加被捕获错误与该语法反例的静态对照。不得修改参考以扩大救援，原稿若超出 grant3 则需要适用的精确 successor permission。这保持 R01/C002，不另建 WP80 阻塞。

### R03：内部参数残留及允许重复行为遗漏

NEW WP73-A `deliverables/final-specification-set/demo-dx/wp73-a-content-editors.md:105` 仍保留 `includeNew` 内部构造参数；可观察的“列表不含新建项”已经足够。该整行原/修复 NEW 同为 SHA256 `7849087c54e100cadc593858c08f52f30a14eec05b6a762339561f76749c9644`。来源 `003_Editor_Listers.rb:349–395` 与 `001_EditorScreens.rb:926–947` 证实它是源组织参数，无必要外部兼容身份。应仅从净化正文去掉该内部名，保留行为；正确原稿/source audit 不因 003 中性化而清理。

同一正文第71行修复后只保留三种不允许重复的集合，却遗漏通用 **NPC 道具池允许重复、保留顺序、进入时不去重也不自动排序** 的分支。WP72 第225行仍引用此道具集合编辑器。来源 `004_Debug_BattleCommands.rb:157–190` 的道具调用使用默认可重复集合；`002_Editor_DataTypes.rb:1040–1182` 将去重/重复选择拒绝/重复修改删除限定到不允许重复的分支。

静态相邻例：合法池 `[A]` 添加 A、Apply Yes 得 `[A,A]`；`[A,B]` 将 B 改为 A 得 `[A,A]`；原已 `[A,A]` 的池不会在进入或 No 中被无条件去重。应以中性行为恢复允许重复分支，同时保留三种去重池、排序、取消、共享规范化和 Yes/No 的既有准确规则。这里 shared003 和 shared C003 仍阻塞；ReadOnly 英文标签不另扩为阻塞。

### R07：未改变尺寸的确认被错误标为已改

当前目录 WE-M17 第91行写“确认时保留所选指标并标已改”，遗漏差异条件。固定来源 `004_EditorScreens_SpritePositioning.rb:46–97,167–222` 初始 `metricsChanged=false`；USE/ACTION 仅在最终尺寸不同于旧值时新增标记。

静态最小前提：无更早指标修改、旧阴影尺寸0、通用编号1资源缺失，只能选0。USE 确认0后标记仍 false；ACTION 确认0也仍 false，但前进返回独立为 true。已有 true 标记不会被清除。最小修订是将“尺寸实际变化才新增已改，没变化保留之前标记”与 ACTION 前进区分，并保留无变化/变化/原标记已真三个相邻前提。补充问题不归入 C016，也不新增 canonical ID。

## 全部 24 项当前独立结论

| ID | 角色 | 当前结论 | 范围/阻塞 |
|---|---|---|---|
| GIR-FD82-003 | 贡献 | BLOCKED_SCOPED | R03 |
| GIR-FD82-C002 | 主责 | BLOCKED_SCOPED | R01 |
| GIR-FD82-C003 | 贡献 | BLOCKED_SCOPED | R03 |
| GIR-FD82-C004 | 主责 | SUPPORTED_SCOPED | 限定范围支持 |
| GIR-FD82-C005 | 主责 | SUPPORTED_SCOPED | 限定范围支持 |
| GIR-FD82-C007 | 贡献 | SUPPORTED_SCOPED | 限定范围支持 |
| GIR-FD82-C008 | 主责 | SUPPORTED_SCOPED | 限定范围支持 |
| GIR-FD82-C009 | 主责 | SUPPORTED_SCOPED | 限定范围支持 |
| GIR-FD82-C010 | 主责 | SUPPORTED_SCOPED | 限定范围支持 |
| GIR-FD82-C011 | 主责 | SUPPORTED_SCOPED | 限定范围支持 |
| GIR-FD82-C012 | 主责 | SUPPORTED_SCOPED | 限定范围支持 |
| GIR-FD82-C013 | 主责 | SUPPORTED_SCOPED | 限定范围支持 |
| GIR-FD82-C014 | 主责 | SUPPORTED_SCOPED | 限定范围支持 |
| GIR-FD82-C015 | 主责 | SUPPORTED_SCOPED | 限定范围支持 |
| GIR-FD82-C016 | 主责 | SUPPORTED_SCOPED | 限定范围支持 |
| GIR-FD82-C017 | 主责 | SUPPORTED_SCOPED | 限定范围支持 |
| GIR-FD82-C018 | 主责 | SUPPORTED_SCOPED | 限定范围支持 |
| GIR-FD82-C019 | 主责 | SUPPORTED_SCOPED | 限定范围支持 |
| GIR-FD82-C020 | 贡献 | SUPPORTED_SCOPED | 限定范围支持 |
| GIR-FD82-C021 | 主责 | SUPPORTED_SCOPED | 限定范围支持 |
| GIR-FD82-C022 | 主责 | SUPPORTED_SCOPED | 限定范围支持 |
| GIR-FD82-C023 | 主责 | SUPPORTED_SCOPED | 限定范围支持 |
| GIR-FD82-D025 | 主责 | SUPPORTED_SCOPED | 限定范围支持 |
| WP80-INTAKE-R01 | 贡献 | SUPPORTED_SCOPED | 限定范围支持 |

每项当前正文/目录、完整控制对象的固定路径/blob/SHA、限定语义、复用边界及新独立判断在 [contribution-review.json](contribution-review.json)。共享 003/C003/C007/C020/WP80 仅覆盖 B19 的本地贡献，保留其他已接受 owner 和未决 owner，不把完整 ID/字节保全当作全局通过。C016 既有保存后缀/延迟克隆/失败阶段的局部支持不消除独立 R07 补充问题。

## 方法、复用及剩余限制

本审读取参考静态文本、官方语言文档和本次候选，未执行参考游戏、Ruby、编译器、转换器、生成器、反序列化器、行为向量、随机模型、旧执行脚本。仅新写 Git/JSON/hash/text 元数据处理。实际新读取与仅身份复核在 [source-reading-log.json](source-reading-log.json) 分开记录；内部并行只读交叉核验不充当额外正式签门。旧报告 `0fb4acd6ce8532436c016ab939532e30a13a3f07` 原地不改，仅以固定 SHA/路径/哈希复用确实不变的完整控制、来源和正文范围；修复及回归重新判断，不继承旧 PASS/BLOCK。

U01–U10、G01–G12、AX01–AX20 和原有媒体、宿主、插件、67树果、八杯赛、pokemon_metrics 未读样本、Gen5–8/Shadow backups、随机/录像、deprecated/EventScene/动态阴影等界限全部保留。runtime observations=0，proven Demo event chains=0，向量执行=0。canonical OPEN=229 / CLOSED=0，284 旧 scoped receipts 不变。完整限定见 [limits.json](limits.json)。

只添加本新报告目录；不改 main、正文、原稿、参考、旧证据或旧报告，不注册 G/ACT/C，不代签 actual 或正式接受。普通推送后须由空 Git 对象库从远端独立读回完整 commit/tree、分支和本目录每个输出，逐文件校验 manifest、blob、SHA256、bytes、UTF-8/JSON；读回凭据不用于自我授予质量通过。
