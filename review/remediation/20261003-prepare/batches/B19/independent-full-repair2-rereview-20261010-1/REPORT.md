# B19 repair-2 FULL 24/19 独立有界再审

结论：**PASS_SCOPED**，仅绑定下列 repair-2 完整 NEW 的 candidate FULL 门。24 项贡献、19 项主责全部给出当前独立限定判定，24/19 均支持，剩余本地阻塞为零。R07 补充问题也已修复，仍不归入 C016，不新增 canonical finding。此结论不代签整合后 actual、ACT、正式 C 接受或其他 owner。

## 固定对象

| 对象 | 完整 commit | tree |
|---|---|---|
| repair-2 NEW | `7be976f821a49aa22dadec52cf6165c4e1d0887b` | `ae9e3e9930fe1cf704b74ddf4b616fce480adc62` |
| 发布及读回包 | `537de126c2671368caa26988cd1aebce89ea4de4` | `face0a662d2a5b26fc005b3123c260e31ea79d69` |
| grant4 | `84cd4bc4c054aa9799532f79f94a237956bacee7` | `726cf9ebeb66149dfd60023537044760b4fa4ebd` |
| 旧 repair-1 NEW | `afb97d4dc161594d36b7dcebe35155a206ceb511` | `c5075947e57fb1795c12fc35093c45bfe139314f` |
| B18 C | `52f24036d09503144c6ec89960029db4ed370734` | `3b20f8f2c0dab0ef3e2867aa2bac0fa98497c44b` |
| 本审上一份固定报告 | `eead55aab54d0dc2df2dbc53490aa901f1b0cd73` | `17f51e26f95bfbdc69bf90729a30cdd6bb0f649c` |
| 静态参考 | `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b` | `7589c800b61ba13a13040ed0d686979b80a84fd0` |

先读取固定入口 `review/remediation/20261003-prepare/batches/B19/author-draft-2/repair-2/complete-candidate-1/publication-1/README.md`、FULL 派发 `review/remediation/20261003-prepare/batches/B19/author-draft-2/repair-2/complete-candidate-1/publication-1/FULL-24-19-recheck-dispatch.md`、grant4 报告及精确三条声明，再核完整 qualified 控制和四 topic/12 正式条款/三原稿修改。发布包和许可的身份核对只是输入证据，不能授予质量通过。模型请求 gpt-6.1-sol / Ultra / default（Standard）接纳有效，无可信后端回参则 UNVERIFIED，沿既有 Plan A；未探针额度/回参或使用 CLI fallback。

## 完整差异、许可和保全

本审重新构造 OLD NEW→repair-2 NEW 与 B18 C→repair-2 NEW 的**完整未过滤全仓差异**，均用 `git diff --no-ext-diff --no-textconv --binary --full-index`。完整流保存在本次临时工作区，仅在报告引用已发布唯一完整流，没有在新报告复制历史流、旧报告或完整控制正文。

| 差异 | bytes | SHA256 | 路径 |
|---|---:|---|---:|
| repair-1 NEW→repair-2 NEW | 1436191 | `94e2886ec016df3cdacb09ba883a13f825f740e793cfef1008dbd902cac4eb30` | 30（4 M / 26 A） |
| B18 C→repair-2 NEW | 3945512 | `c1c491920f9d55730619cb50df1548cf718bc1604dfe7184c6341427f91bb257` | 90（7 M / 83 A） |

第一条与发布包 `537de126c2671368caa26988cd1aebce89ea4de4` 的唯一流 `review/remediation/20261003-prepare/batches/B19/author-draft-2/repair-2/complete-candidate-1/publication-1/full-unfiltered-OLD-NEW-to-repair2-NEW-repository.diff` 字节相同，blob `893715dd951ce1a3c43b42ebcb8bae052632a053`。30 路径中的 26 项新增是 B19 author metadata，包含先前发布证据自然进入差异的路径；完整无过滤不意味着递归读取或复制其历史内容。第二条的全部路径、大小、哈希也独立匹配。[evidence-verification.json](evidence-verification.json) 记录完整路径与固定身份。

72 项输入的 before/review 身份、32 项不可变引用、7 payload 和发布 manifest 均核对。24 个完整原 finding/approved acceptance 对象的 canonical SHA 与本审先前完整 qualified 控制相等，保持所有 roots、extensions、current_decision、current_qualifications、adjudication_precedence、premises、effective_case_constraints 和 evidence_limits。当前49正文范围及67目录引用重算哈希一致；31个正文范围、58个目录引用与先前绑定完全相同，其余是重新判断的修改或新增定位。没有把身份核对称为72文全文语义阅读，也没有把旧21/18支持或旧 affected PASS 转签本候选。

grant4 独立重建 WP72 原稿第82/306/338三条：整个当前原稿恰好等于固定proposal `985114bc8bf4164e15d6e2c7996776d41c5e4003` 的允许 complete-after，blob `a5b71ae5addc7a098aa17b3144dd0366fe6b2148`，SHA256 `6b50e82e43035f0eeba573a6004bee5a3fb021aaa5c4ee43131f21483a1733a9`，99280 bytes；三条外字节不变。WP73-A/B原稿及正式B等于旧NEW，正确原稿003源审计未清理。许可仍不等于质量通过。

195个当前案例只有 DG-M06、DG-M21、CE-M15、WE-M17四行改变，另外191行与旧NEW相同；178个基线ID及当前195个ID的顺序、重数保持。旧候选中与C相等148行仅CE-M15成为本轮有界补项，余147行仍相同。三B18目录、Tile、WP74/WP75、35项跨owner consumed inputs及284旧accepted receipts锁保持。连接/地形部分提交、取消不对称、稀疏ID、缺失/透明资源、SAVE-TIME后缀/懒登记/部分写出以固定字节及限定证据复用。[preservation-check.json](preservation-check.json) 给出逐锁、逐行和精确许可证明。

## 原剩余阻塞的当前判断

**R01 支持。** 正式WP72第64/288、原稿第82/306/338、DG-M06第16行全部区分捕获范围。固定 `003_Debug_MenuExtraCode.rb:85–111,183–193` 的首片段资格和完整原表达式求值顺序保持；静态 `s:1/0` 获准且整数除零属于可救援错误、回落 `[-]`，`s:1+1=2` 同样获准但完整表达式产生范围外 SyntaxError、局部传播。资格前处理的空token错误另列；若发生在USE重绘，原槽已经翻转，正常返回后的地图请求尚未到达。官方 [默认 rescue](https://docs.ruby-lang.org/en/3.0/syntax/exceptions_rdoc.html)、[整数除零](https://docs.ruby-lang.org/en/3.0/ZeroDivisionError.html)、[语法错误](https://docs.ruby-lang.org/en/3.0/SyntaxError.html)、[ScriptError](https://docs.ruby-lang.org/en/3.0/ScriptError.html) 支持该静态分类。没有执行表达式，宿主画面/恢复/进程结局未知。WP80只保持原ASCII前缀局部贡献，不扩为全局兼容关闭。

**R03 支持。** 正式A105移除includeNew，同时不含新建项/新物种不支持保持，正确原稿保留源审计。A66/67/71/138、WP72-225、DG-M21与CE-M15明确NPC允许重复池：`[A]`添加A后Yes为`[A,A]`，`[A,B]`将B改A后Yes为`[A,A]`，`[B,A,A]`只打开No仍保持内容与顺序；入口无去重/自动排序，No返回进入的原序列，调用方仍赋返回值，Cancel继续。三类不重复池分别保留重复添加定位、重复修改删除本项、入口去重、蛋招入口ID排序与刷新显示名排序、No不撤销原地规范化。ACTION+UP与后一项、DOWN与前一项交换，添加哨兵不交换。同值/选择器取消/删除/Yes与父保存门及无NPC/合法空池邻例准确。定点来源为 `002_Editor_DataTypes.rb:1040–1182`、`004_Debug_BattleCommands.rb:143–190`，列表无新增入口另核 `003_Editor_Listers.rb:349–395` 与 `001_EditorScreens.rb:926–947`；[wp73a-independent-check.json](wp73a-independent-check.json) 含完整限定与邻例。

**R07 补充支持。** WE-M17第91行保留首缺停止和三枚举夹具，并正确补入：旧0且仅0可选、初始dirty=false，USE同0不置真；ACTION同0也不置真但独立前进；已有true不清除，BACK恢复旧值且不写标记；真实0→1确认才新增dirty。没有其他已确认改动时正常退出不询问保存，走档案重载；有标记时保存Yes先档案再PBS，输出路径仍由实际保存时后缀集合决定，不保证某个PBS文件必产生。静态来源 `004_EditorScreens_SpritePositioning.rb:46–111,167–222` 及既有保存后缀证据与现行文本一致。媒体未验证、夹具未执行；R07不挂C016、不新增canonical ID。

R02/R04/R05/R06/R08及PC笔误的旧有效修复在准确当前NEW上保留并重新给限定判断。120效果完整行、83/22/13/2、41禁止项、表外不可用、E088 −2绿色/−1普通及重置范围，在固定来源与完整参数证明下逐行复用字节不变证据；不重复整源读取或执行参数向量。完整EV/PID/IV诊断、五主类型槽和独立extra槽、容量/HP/PP/三能力/天气/Mega/六编辑器保存取消、共享C003/C007/C020全部限定和相邻条件保留。详细逐项入口为 [contribution-review.json](contribution-review.json) 和 [repair-review.json](repair-review.json)。

## 当前全部24/19独立限定结论

| ID | 角色 | 当前结论 |
|---|---|---|
| GIR-FD82-003 | 贡献 | PASS_SCOPED |
| GIR-FD82-C002 | 主责 | PASS_SCOPED |
| GIR-FD82-C003 | 贡献 | PASS_SCOPED |
| GIR-FD82-C004 | 主责 | PASS_SCOPED |
| GIR-FD82-C005 | 主责 | PASS_SCOPED |
| GIR-FD82-C007 | 贡献 | PASS_SCOPED |
| GIR-FD82-C008 | 主责 | PASS_SCOPED |
| GIR-FD82-C009 | 主责 | PASS_SCOPED |
| GIR-FD82-C010 | 主责 | PASS_SCOPED |
| GIR-FD82-C011 | 主责 | PASS_SCOPED |
| GIR-FD82-C012 | 主责 | PASS_SCOPED |
| GIR-FD82-C013 | 主责 | PASS_SCOPED |
| GIR-FD82-C014 | 主责 | PASS_SCOPED |
| GIR-FD82-C015 | 主责 | PASS_SCOPED |
| GIR-FD82-C016 | 主责 | PASS_SCOPED |
| GIR-FD82-C017 | 主责 | PASS_SCOPED |
| GIR-FD82-C018 | 主责 | PASS_SCOPED |
| GIR-FD82-C019 | 主责 | PASS_SCOPED |
| GIR-FD82-C020 | 贡献 | PASS_SCOPED |
| GIR-FD82-C021 | 主责 | PASS_SCOPED |
| GIR-FD82-C022 | 主责 | PASS_SCOPED |
| GIR-FD82-C023 | 主责 | PASS_SCOPED |
| GIR-FD82-D025 | 主责 | PASS_SCOPED |
| WP80-INTAKE-R01 | 贡献 | PASS_SCOPED |

共享003/C003/C007/C020/WP80的PASS_SCOPED仅指本门B19分配贡献，保留完整 qualified 控制中的已接受owner成果及未决owner界限；不关闭这些全局ID，也不代签相邻WP63/WP74等贡献。

## 证据复用、限制及发布边界

[source-evidence-reuse.json](source-evidence-reuse.json) 区分本轮定点静态新读与32个旧reference文件身份复核；[wp72-independent-check.json](wp72-independent-check.json)、[wp73a-independent-check.json](wp73a-independent-check.json) 记录24项内部只读交叉核验、固定控制/正文/目录/源码范围的精确复用。它们是支撑本审当前独立判断的证据，不是额外正式签门。旧报告只引用固定commit/path/blob/SHA/范围，不改写、不递归复制、不运行旧metadata脚本。新写Git/JSON/hash/text处理仅用于本次身份和结构检查，作者断言未替代源码/静态语言/保全证据。

U01–U10、G01–G12、AX01–AX20和媒体/宿主/插件/berry67/八杯赛/pokemon_metrics未读样本/Gen5–8及Shadow备份/随机与录像/deprecated/EventScene/动态阴影等全部具名边界保持。runtime observations=0、proven Demo event chains=0；参考游戏、Ruby、编译器、转换器、生成器、反序列化器、行为向量、随机模型、旧脚本执行均为0。canonical229 OPEN/0 CLOSED和284旧接受回执不改。[limits.json](limits.json) 保存完整限制和配置。

只新增本独立报告目录；只签本轮固定NEW candidate FULL，不自签G/ACT/actual/C或正式接受。普通推送后从新建空Git对象库独立远端读取报告完整commit/tree与本目录每个输出，核blob/SHA256/bytes及UTF-8/JSON。输出manifest对自身自排除，manifest自身由完整报告commit/tree及读回哈希绑定。
