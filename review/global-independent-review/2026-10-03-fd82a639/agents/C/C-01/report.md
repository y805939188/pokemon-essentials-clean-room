# C-01 独立首轮审查报告

结论：**NEEDS_REVISION_SCOPED**。本轮仅审 WP72、WP73-A、WP73-B，不签发整个工作包、D18、WP80 或全局完成结论。

项目固定提交 `e1e01bb18d824931e54f182dd61af5a9f908ba85`；参考独立只读克隆固定提交 `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`。分支 `review/2026-10-03-fd82a639/C`。

## 独立性与方法

首判形成时间：2026-10-03 12:36:24 UTC；独立首判于 12:39:09 UTC 落盘。形成前未阅读其他本轮 agent 的发现；已读就绪报告和交接仅用于范围、基线及入口，不据作者自检或旧 PASS 得出结论。全部主项目输入从 C 自有固定基线 worktree 读取。参考只作静态文本阅读/搜索；未运行游戏、编译器、转换器、生成器、反序列化器或行为模拟器。

三份原规格、三份净化正文、四份现行补充表，以及测试族 DG 30／CE 20／WE 22 条已全文逐项阅读。参考源码按 reading-log.tsv 精确登记，含完整菜单框架、效果白名单编辑器、三份世界编辑器及定点调用/保存/编译/缓存消费者；**未全文读完全部 WP72/WP73 主源文件**，不继承旧阅读统计。source-coverage.tsv 列出定点范围和未读部分；equivalence.tsv 区分文本承接与已做源码反核。

## 首判问题

### RUN-C-001 · P2 · 表达式开关的 ASCII s: 前缀在净化时被改成全角冒号

类型：compatibility_literal_changed；状态：OPEN；置信度：HIGH；工作包：WP72。

净化稿 §4.2 指名以 s：为前缀的表达式开关；测试 DG-M06 又只说“表达式前缀”，没有保留字符对照。

参考识别小写 s 后紧跟 ASCII 冒号（U+003A）；全角冒号（U+FF1A）不匹配，按普通开关原始值显示。原规格保留了正确字面。

最小对照：两份开关名仅冒号不同：ASCII s: 版本显示 ON；全角 s：版本显示 OFF。无需执行求值程序即可从识别分支判定。

影响：后续实现或测试若按净化字面识别，会接受错误输入并拒绝兼容输入。

最低更正：净化稿明确 ASCII s:（小写 s、U+003A），测试加入全角冒号不被识别的反例；不要为净化改写输入字符。

项目定位：`deliverables/final-specification-set/demo-dx/wp72-debug-contexts-and-controls.md:64`；`specs/demo/wp72-debug-contexts-and-controls.md:82;337`；`deliverables/final-specification-set/test-catalog/demo-dx-wp72-73-74-75-76-77.md:16`。

参考定位（固定参考提交）：`Data/Scripts/020_Debug/003_Debug menus/003_Debug_MenuExtraCode.rb:79-107`。

### RUN-C-002 · P2 · 表达式开关“翻转后显示不变”缺少表达式独立于该开关的前提

类型：semantic_overgeneralization；状态：OPEN；置信度：HIGH；工作包：WP72。

原稿、净化稿及 DG-M06 无条件声称翻转底层值不会改变求值结果或显示。

USE 先翻转该 ID 的原始值，再刷新显示；显示时重新求值。若表达式读取同一原始开关，结果随翻转变化。原始值与显示机制分离不等于数据依赖分离。

最小对照：打开显示 OFF；对该行 USE 后原始值变真，刷新求值得真，显示 ON。对照常量表达式或不依赖该 ID 的表达式才可保持显示不变。

影响：错误不变量会要求未来 UI 不重新求值或错误冻结显示；目前测试无法区分写入目标和表达式依赖。

最低更正：改为“USE 写原始值、不改表达式文本；刷新时按表达式重新求值，结果是否变化取决于依赖”；DG-M06 分出独立表达式与自引用原始值两种前提。

项目定位：`specs/demo/wp72-debug-contexts-and-controls.md:82;337`；`deliverables/final-specification-set/demo-dx/wp72-debug-contexts-and-controls.md:64`；`deliverables/final-specification-set/test-catalog/demo-dx-wp72-73-74-75-76-77.md:16`；`review/wp72-delivery-2026-10-02/revision-v3/entry-coverage-table.md:26`。

参考定位（固定参考提交）：`Data/Scripts/020_Debug/003_Debug menus/003_Debug_MenuExtraCode.rb:79-107;188-194`；`Data/Scripts/004_Game classes/001_Switches and Variables/002_Game_Switches.rb:14-23`。

### RUN-C-003 · P2 · CE-M02 净化丢失数值和布尔子型，取消预期不再唯一

类型：test_precondition_loss；状态：OPEN；置信度：HIGH；工作包：WP73-A。

CE-M02 把原来的 LimitProperty2 与 BooleanProperty2 简写成“数值类数值取消／布尔类取消”，统一预期返回空。

同稿列出多个数值/布尔行为：普通有界数值 BACK 返回钳制旧默认值；可空数值显式取消才返回空。确认式布尔与可空三态选择也不同。原测试指名的两个子型是必要前提。

最小对照：前者返回 7，后者返回空；二者都符合 CE-M02 当前“数值类数值取消”描述却要求不同预期。

影响：测试设计会把合法保留旧值实现误判失败，或将所有数值取消错误实现成清空。

最低更正：使用行为名称恢复区分，例如“可空有界数值（取消哨兵 −1）”和“可空三态布尔选择”；不必恢复源类名。补普通数值取消保留旧值对照。

项目定位：`deliverables/final-specification-set/test-catalog/demo-dx-wp72-73-74-75-76-77.md:49`；`specs/demo/wp73-a-content-editors.md:198`；`deliverables/final-specification-set/demo-dx/wp73-a-content-editors.md:40-49`。

参考定位（固定参考提交）：`Data/Scripts/020_Debug/002_Editor_DataTypes.rb:32-160`；`Data/Scripts/007_Objects and windows/011_Messages.rb:93-111;166-205`。

### RUN-C-004 · P2 · 遭遇步数率 0 在反写后重编译变回默认值的语义损失未登记

类型：lifecycle_coverage_gap；状态：OPEN；置信度：HIGH；工作包：WP73-B / WP04 / WP36。

世界编辑规格允许步数率 0–255 并描述保存数据档案和反写 PBS；WE-M13 只检查即时内存写入，未说明零值不能保真往返。

遭遇反写只在步数率大于 0 时写第二字段；等于 0 时仅输出类型名。编译对缺失第二字段补该类型缺省触发率，Land 默认 21；这是可证的参考异常，缺陷是规格未记录，而非要求修参考。

最小对照：保存后注册数据及 encounters.dat 的步数率为 0；反写 Land 行不含第二字段；再编译后注册数据及 encounters.dat 为 21。不要将当前地图快照混入该文件往返向量。

影响：未来实现可能合理地保留 0，却与参考往返行为不等价；开发者可能误以为禁用步进遭遇的设置跨编译保持。

最低更正：在 WP73-B 保存/兼容边界列出 0 值的四阶段结果并交叉引用 WP04/WP36；测试增具名往返向量。保留异常事实，不更改参考或自动修成保真。

项目定位：`specs/demo/wp73-b-world-editors.md:92;102;105;183-185`；`deliverables/final-specification-set/demo-dx/wp73-b-world-editors.md:74;84-87`；`deliverables/final-specification-set/test-catalog/demo-dx-wp72-73-74-75-76-77.md:86-88`；`deliverables/final-specification-set/generic-kernel/wp04-pbs-lifecycle.md:136-138`；`deliverables/final-specification-set/creature-rpg/wp36-wild-encounters-and-modifiers.md:55-74`。

参考定位（固定参考提交）：`Data/Scripts/020_Debug/001_Editor screens/001_EditorScreens.rb:115-120;280-287`；`Data/Scripts/021_Compiler/003_Compiler_WritePBS.rb:403-442`；`Data/Scripts/021_Compiler/002_Compiler_CompilePBS.rb:730-737;743-765`；`Data/Scripts/010_Data/001_Hardcoded data/013_EncounterType.rb:29-33`。

### RUN-C-005 · P2 · 遭遇编辑/编译后的注册数据与当前地图快照未在生效合同中分层

类型：consumer_state_coverage_gap；状态：OPEN；置信度：HIGH；工作包：WP73-B / WP72 / WP36。

WP73-B 将编辑落点概括为内存、数据档案、PBS 三层，保存/取消表不说明当前地图步进仍消费旧快照；WP73-A 的通用“保存后读取方立即用新数据”也未限定直接查询方。

当前地图装载时复制步数率并深复制遭遇槽。编辑和保存更改注册数据，普通退出与调试全量编译入口均没有重建当前地图遭遇快照。当前步进/选择从旧快照取值；进入地图或实际变更遭遇版本等具名装载入口才刷新。

最小对照：注册数据和数据档案已为 0，当前步进仍读取旧的 21；实际改变版本触发装载后才可读取新快照。把版本重新设为相同值不会刷新（写入器早退）。这不等于本向量保证某步必定开战。

影响：生效时机无法由交付规格唯一决定，容易误实现为保存即热更新或把改后仍有遭遇当作运行故障。

最低更正：为遭遇编辑加入“注册/文件/当前地图快照”状态表；列出保存、取消、调试编译、同值版本写入与真正重装的区别；将直接数据查询和快照消费者分开。

项目定位：`deliverables/final-specification-set/demo-dx/wp73-b-world-editors.md:17;74;84-87;129`；`deliverables/final-specification-set/demo-dx/wp73-a-content-editors.md:139`；`deliverables/final-specification-set/demo-dx/wp72-debug-contexts-and-controls.md:90;264`。

参考定位（固定参考提交）：`Data/Scripts/012_Overworld/002_Battle triggering/003_Overworld_WildEncounters.rb:13-22;104-116;271-276`；`Data/Scripts/020_Debug/001_Editor screens/001_EditorScreens.rb:115-124`；`Data/Scripts/020_Debug/003_Debug menus/002_Debug_MenuCommands.rb:1163-1170;1335-1345`；`Data/Scripts/007_Objects and windows/002_MessageConfig.rb:559-591`；`Data/Scripts/021_Compiler/001_Compiler.rb:993-1037`；`Data/Scripts/012_Overworld/002_Overworld_Metadata.rb:114-119`；`Data/Scripts/012_Overworld/001_Overworld.rb:224-238`。

### RUN-C-006 · P2 · 净化正文仍以源属性类、子类关系、方法与内部容器组织合同

类型：sanitization_architecture_residue；状态：OPEN；置信度：HIGH；工作包：WP72 / WP73-A / WP73-B。

三篇前言声明不含脚本入口名与类名，全集净化纪律要求这些标识和宿主对象关系留在审计。

WP73-A 保留整组源 Property/Lister 类名、GameDataPoolProperty 的子类关系、Compiler.write_pokemon/write_metadata/write_regional_dexes 等调用名，以及“各数据访问层常量哈希”；WP72 保留方法名 form_simple 和内部用途符号全角化；WP73-B 保留 metricsChanged 等内部字段。这些不是必须保真的外部输入语法。

最小对照：仅阅读 WP73-A §3.5 就收到池属性及三个源子类的组织关系；这超出“不许重复/是否排序/取消是否规范化”的行为需求。源文件对应关系已可单独审计。

影响：交付仍携带参考架构模板，且与自身净化承诺冲突；简单全角化或改名没有完成行为重述。

最低更正：把属性类型改成行为类别并保留范围、取消、别名副作用；把源类/方法/子类映射移至审计，删除内部容器及调用签名式要求。保留真正的兼容输入字符和来源异常结果。

项目定位：`deliverables/final-specification-set/scope-statement.md:31-35`；`deliverables/final-specification-set/demo-dx/wp73-a-content-editors.md:5;17;40-73;79-123;149`；`deliverables/final-specification-set/demo-dx/wp72-debug-contexts-and-controls.md:18-21;128;196;205`；`deliverables/final-specification-set/demo-dx/wp73-b-world-editors.md:23;96;100;109`。

参考定位（固定参考提交）：`Data/Scripts/020_Debug/002_Editor_DataTypes.rb:1040-1068;1160-1182`；`Data/Scripts/020_Debug/001_Editor screens/001_EditorScreens.rb:926-987`；`Data/Scripts/020_Debug/003_Debug menus/005_Debug_BattlePkmnCommands.rb:776-787`。

### RUN-C-007 · P2 · 120 项战斗效果白名单的具体合同仍留在历史交付附件

类型：sanitized_coverage_gap；状态：OPEN；置信度：HIGH；工作包：WP72。

净化稿 §7.5 只给 83/22/13/2 总数，并要求读 review 目录的旧 battle-effects-catalog；全集 README 声明行为正文可独立阅读、追溯仅作审计。

成员/阵营/全场/席位哪些效果可编辑、各自类型/默认/上下界是行为合同。现行附件有逐项120条；净化正文和DG目录未承接这些条目，只有数量和通用交互。审计追溯只提旧目录沿用，未提供净化后的行为附表。

最小对照：实现者从 §7.5 无法确定哪个整数效果上限为4、5、999或金钱上限，也无法确定表外不可编辑集合；两套不同白名单都满足当前总数和通用规则。

影响：可编辑功能范围与数值边界未进入独立交付，不能仅凭路径存在或120计数认定覆盖。

最低更正：把现行目录的行为含义、层、输入类型、默认、范围/哨兵净化为最终集内附表并明确引用；旧审计名映射另留审计。无需复制源哈希或源显示字符串。

项目定位：`deliverables/final-specification-set/demo-dx/wp72-debug-contexts-and-controls.md:210-215`；`review/wp72-delivery-2026-10-02/revision-v2/battle-effects-catalog.md:1-145`；`deliverables/final-specification-set/README.md:20-25`；`audit/source-traceability.md:1262-1274`。

参考定位（固定参考提交）：`Data/Scripts/020_Debug/003_Debug menus/006_Debug_BattleExtraCode.rb:4-177;327-350`。

## 已核实的有限一致项

- 菜单受限模式只排除显式假；描述在进入时收集一次；地图传送与个体菜单的关闭语义不同。
- 战斗 HP、状态、状态计数、道具、等级和形态写回原个体；仅战斗特性不会写回；战斗形态拒绝覆盖前已有清除旧强制值的副作用。
- 训练家类型嵌套创建立即保存并反写两份 PBS，外层训练家取消只重载其数据档案，不撤销已写 PBS；删除/改键无事务回滚保证。
- 地区图鉴子页 No 仍压空洞、空表保存非终止；数据池打开可规范化共享原数组；以上来源异常在本轮定点链上与文本一致，不作为规格缺陷重报。
- 连接少于两图保留旧数据、单轴邻接和逐孤点回退；连接取消重载遭遇而保留地图元数据；地形首次保存后文件 B/运行内存 C；自动定位缺图与透明图分开；无效图块逐图保存。

这些确认只适用于 reading-log.tsv 与 equivalence.tsv 的具名范围，不能扩成完整源码通过。

## 保留与未读

U01–U10、G01–G12、原 20 项 AX 及已登记未验证组合均继续有效。本轮未更改 AX 清单；RUN-C-004 的参考零值往返现象应按新静态证据补登记，问题是规格遗漏，不是让未来审查修参考。已证 demo 事件链仍为 0，运行观察仍为 0；缺失地图/素材/宿主数据/真实插件组合未补造。

未读/未穷尽：WP72 全部世界与玩家命令、普通个体全部数值分支、训练家高级测试与全部战斗数值菜单；WP73-A 全部属性设置实现、所有选择器/预览/试听与完整 schema 参数；跨域运行消费者全集；全部地图事件与素材实际使用；失败注入和实际 I/O。WP74–WP77 测试族未纳入 C-01。现有来源异常未展开的条目原样保留，不能视为已独立复证。

## 执行元数据与交付

父任务已确认成功的 spawn 调用显式设置 gpt-6-astra / ultra，工具返回本 agent 名 /root/review_c；这是启动配置证据，未冒充独立运行时 introspection。子会话无法读取服务 speed；**Standard / Fast / Ultrafast 均未自行改变，speed＝UNVERIFIED**。

只在 `review/global-independent-review/2026-10-03-fd82a639/agents/C/` 写审查输出；原规格、净化稿、附表、计划、审计、旧记录、reference 不修改。提交/推送按本轮人类明确授权执行，范围检查、远程 URL 与精确提交结果见 checkpoint.json；旧交接的禁推送句已由当前授权覆盖。

固定算术复核：高 32／底部行 24 的背面与正面偏移为 3／7；全透明高 32 为 15／19；寄养取消例 256−5＝251；公开 ID 12 复制到两个 16 位半区为 786,444。仅独立常数运算，未执行行为模型。
