# B19 固定候选 FULL 独立复审

结论：**BLOCKED**。完整24项贡献、19项主责均已逐项复审；18项贡献（16项主责）支持局部修订满足，6项贡献（3项主责）受下述精确阻塞影响。另有WP73-B资源枚举的有界补充阻塞R07。此结论只属于固定candidate FULL，不是PASS_SCOPED、ACT/tree签署、正式C或全局关闭。

审查对象：NEW `dfe8e726669a83c751d02e923cf290bdafc82bd7` / tree `b830a49ad76369d19ebaae227aaf190ca5542069`；发布包 `393ec2680af6e118c1fc959fd0c6290d0cb7c82f` / tree `fa5b613f5296f67dd4ac4eca301b3fe6bcddc118`；B18 C `52f24036d09503144c6ec89960029db4ed370734` / tree `3b20f8f2c0dab0ef3e2867aa2bac0fa98497c44b`。固定参考 `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b` / tree `7589c800b61ba13a13040ed0d686979b80a84fd0`。

先读发布包派发入口、管理包原合同及完整原finding/批准acceptance绑定；完整资格、裁决优先级、根裁决、扩展和C007整套effective_case_constraints参与判断。24对象的独立canonical JSON哈希和精确指针见input-verification.json，逐项行为判断及固定blob/路径/SHA256/范围见contribution-review.json。采用内部只读交叉核验辅助，最终结论由根审者独立复读阻塞来源后负责；这些辅助不构成额外正式门签署。

请求配置gpt-6.1-sol / Ultra / default（Standard）接纳有效。可信后端回显未提供时仍UNVERIFIED，依已接受Plan A；未审计额度/回参，未改CLI。只执行自己新写的Git/JSON/hash/text元数据操作；参考游戏、Ruby、编译/转换/生成/反序列化、旧程序、行为向量均未执行，运行观察0、已证Demo链0。

## 完整差异与保全

独立重建不带路径过滤的全仓C→NEW差异：34个实际变更路径，1,800,341 bytes，SHA256 `cb20d5c007c6ab0496419063c51120d42206247b9def9b8c1258c70365357f31`。命令、完整路径清单、独立第二序列化的核对元数据见input-verification.json和preservation-check.json。全仓流包含旧diff正文，因此只记录固定身份/哈希，不递归发布旧证据。

另独立重建全部七payload的未过滤差异，逐字等于唯一现有流：NEW路径 `review/remediation/20261003-prepare/batches/B19/author-draft-2/full-candidate-1/full-unfiltered-C-to-NEW-payload.diff`，blob `c542891696660d5dac52dd19fed00bc947dc6391`，382,948 bytes，SHA256 `61b58208423530ed62fa4fe7a4868bb7cb06ca03e750914fc22f77f3b573df64`。不复制该流。

72声明输入、20不可变证据身份均独立核对匹配。WP72 17条和WP73-A 16条原稿精确after、WP73-B已完成slice逐字应用匹配；这只证明许可边界，不代表质量。三份B18目录整字节保持。178旧demo ID顺序与重数保持、NEW合计195项，但29旧行内容修改，五条明确旧案例内容缺口构成R05。

120效果项（成员83/阵营22/全场13/席位2）逐条独立检查类型、登记默认、合法范围、ACTION复位、层级与行为，全部参数匹配；41注释排除项及表外禁止仍保留。独立明细见effects-independent-check.json；完整编辑质量仍被E088颜色比较R04阻塞。

## 逐项结果

SUPPORTED_SCOPED表示该B19局部贡献的修订及有界资格获得支持，不登记新接受收据、不继承全局关闭。WP80的ASCII标点局部满足；C002的表达式资格缺口单独阻塞，未混算为标点错误。

| ID | 角色 | 本地结论 | 阻塞 |
| --- | --- | --- | --- |
| GIR-FD82-003 | 共享贡献 | BLOCKED | R03 |
| GIR-FD82-C002 | 主责 | BLOCKED | R01 |
| GIR-FD82-C003 | 共享贡献 | BLOCKED | R01, R05, R06, R08 |
| GIR-FD82-C004 | 主责 | SUPPORTED_SCOPED | — |
| GIR-FD82-C005 | 主责 | BLOCKED | R02 |
| GIR-FD82-C007 | 共享贡献 | BLOCKED | R04 |
| GIR-FD82-C008 | 主责 | SUPPORTED_SCOPED | — |
| GIR-FD82-C009 | 主责 | SUPPORTED_SCOPED | — |
| GIR-FD82-C010 | 主责 | SUPPORTED_SCOPED | — |
| GIR-FD82-C011 | 主责 | SUPPORTED_SCOPED | — |
| GIR-FD82-C012 | 主责 | SUPPORTED_SCOPED | — |
| GIR-FD82-C013 | 主责 | SUPPORTED_SCOPED | — |
| GIR-FD82-C014 | 主责 | BLOCKED | R06 |
| GIR-FD82-C015 | 主责 | SUPPORTED_SCOPED | — |
| GIR-FD82-C016 | 主责 | SUPPORTED_SCOPED | — |
| GIR-FD82-C017 | 主责 | SUPPORTED_SCOPED | — |
| GIR-FD82-C018 | 主责 | SUPPORTED_SCOPED | — |
| GIR-FD82-C019 | 主责 | SUPPORTED_SCOPED | — |
| GIR-FD82-C020 | 共享贡献 | SUPPORTED_SCOPED | — |
| GIR-FD82-C021 | 主责 | SUPPORTED_SCOPED | — |
| GIR-FD82-C022 | 主责 | SUPPORTED_SCOPED | — |
| GIR-FD82-C023 | 主责 | SUPPORTED_SCOPED | — |
| GIR-FD82-D025 | 主责 | SUPPORTED_SCOPED | — |
| WP80-INTAKE-R01 | 共享贡献 | SUPPORTED_SCOPED | — |

## 精确阻塞与再检

### R01 表达式资格没有自足定义，重绘与刷新请求顺序写反

NEW 正式第64行、原稿第82行和 M06 用“既有求值资格门保留”代替完整规则，当前独立实现无法确定何时允许求值；USE 又写成原槽翻转→地图刷新请求→页重算，参考是原槽翻转→页重绘并重新求值→地图刷新请求。首token前处理错误边界也未定义；“求值异常回落空值”不应外推到进入eval前的失败。

静态反例：同一 ASCII s: 前缀下，首 token 为已存在大写常量、不存在大写常量、允许的小写名称、事件解释器/事件方法名称及非字母名称应有不同资格。另设合法非字母表达式只读取初始 false 的地图刷新请求标记，立即重绘读到 false，重绘后标记才 true；正文现顺序会使该观察不同。此外名称仅s:时split结果为空数组，在救援之外对空值调用strip!；s:!时移除!后首token为空，随后字符索引为空而继续索引，局部NoMethodError，不能推为[-]。均为静态条件推导，未求值、未观察宿主结果。

最小修订：用兼容行为类别恢复 token 提取/去空白/移除开头一个 !、大写常量存在门、小写排除事件解释器与事件方法门、非字母许可及eval求值异常显示规则，另列空串/只含!等前处理局部未捕获失败，宿主结果未验证。修正重绘顺序；保留 ASCII U+003A 与全角反例、原槽/显示分离和原有合法/拒绝邻例。源类映射可只留审计证据。

再检：逐字符复查前缀和完整资格正反例；区分前处理局部NoMethodError与eval救援空值，禁止扩大宿主保证；静态比对原槽写→页重绘/求值→地图刷新请求；正文、授权原稿、DG-M06 与新对应案例均自足且一致。

候选证据：`dfe8e726669a83c751d02e923cf290bdafc82bd7:deliverables/final-specification-set/demo-dx/wp72-debug-contexts-and-controls.md` L64–65；`dfe8e726669a83c751d02e923cf290bdafc82bd7:specs/demo/wp72-debug-contexts-and-controls.md` L82–83,338–339；`dfe8e726669a83c751d02e923cf290bdafc82bd7:deliverables/final-specification-set/test-catalog/demo-dx-wp72-73-74-75-76-77.md` L16,244；`52f24036d09503144c6ec89960029db4ed370734:deliverables/final-specification-set/demo-dx/wp72-debug-contexts-and-controls.md` L64–65。固定blob/SHA256在JSON对应记录。

错误边界的辅助语言文本：[String#split](https://docs.ruby-lang.org/en/3.0/String.html#method-i-split)、[Array#[]](https://docs.ruby-lang.org/en/3.0/Array.html#method-i-5B-5D)、[String#[]](https://docs.ruby-lang.org/en/3.0/String.html#method-i-5B-5D)、[NoMethodError](https://docs.ruby-lang.org/en/3.0/NoMethodError.html)。例子未执行，真实读取段见source-reading-log.json。

参考证据：`8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b:Data/Scripts/020_Debug/003_Debug menus/003_Debug_MenuExtraCode.rb` L85–104,183–193。全部静态读取，未执行。

### R02 WP73-A 仍无条件声称保存后所有运行读取方立即生效

正式 WP73-A 142 和原稿158的 .dat 保存后立即用新数据仍是无条件总断言；WP73-B 对遭遇快照/指标布局的详细修订无法使两个相互矛盾的正文同时准确。

静态反例：合法当前地图 Land 快照21，编辑登记/保存0但不切图、不改版本、不显式 setup：直接登记查询读0，当前快照仍21；同值版本赋值也不触发 setup。正常已布局的战斗精灵不会因指标保存向既有布局广播重新定位。

最小修订：收窄总句为按消费者分层：直接登记查询、当前地图遭遇快照、指标预览/下一次布局，以及档案/PBS各自阶段。保留保存与导出前后内存可能不等、版本同值早退和局部失败边界；如需修改原稿158应获得精确 successor scope，不默认旧 scope 质量通过。

再检：两正文/原稿不再互相覆盖矛盾；同版本无 setup 与新版本有 setup 的对照明确；直接查询、已有快照和已有精灵布局可见性均有唯一阶段预期。

候选证据：`dfe8e726669a83c751d02e923cf290bdafc82bd7:deliverables/final-specification-set/demo-dx/wp73-a-content-editors.md` L142；`dfe8e726669a83c751d02e923cf290bdafc82bd7:specs/demo/wp73-a-content-editors.md` L158；`dfe8e726669a83c751d02e923cf290bdafc82bd7:deliverables/final-specification-set/demo-dx/wp73-b-world-editors.md` L101–110,149–163。固定blob/SHA256在JSON对应记录。

参考证据：`8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b:Data/Scripts/012_Overworld/002_Battle triggering/003_Overworld_WildEncounters.rb` L13–22,35–47,110–120；`8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b:Data/Scripts/012_Overworld/002_Overworld_Metadata.rb` L114–119；`8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b:Data/Scripts/020_Debug/001_Editor screens/001_EditorScreens.rb` L114–123；`8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b:Data/Scripts/020_Debug/001_Editor screens/004_EditorScreens_SpritePositioning.rb` L102–106,112–136；`8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b:Data/Scripts/011_Battle/004_Scene/006_Battle_Scene_Objects.rb` L577–635。全部静态读取，未执行。

### R03 净化正文仍要求源语言类别及内部命令结果组织

WP73-A 71 的模块/允许多个/自动排序签名式组织，73 的字符串实例与类对象匹配及 param_type/Integer，123 的 [5]/[1]/[2]/[3]/[4] 内部返回元组及第三列匹配，136 的 write_metadata 仍进入正式行为规范。

静态反例：可独立实现者只需要知道编辑类别、LocationFlag实际0–65535数值限制、确认/取消/去重/换序/插删与保存顺序，却被要求复现 Ruby 类分派、结果元组和列表第三列。独立实现采取另一数据结构仍应兼容观察行为。

最小修订：改为行为类别及可观察顺序，保留真实 LocationFlag 数值门、必要外部PBS/Evolution ID、五槽等可观察数量、键位与取消/共享对象副作用；内部源名称/列号/参数组织移至静态审计引用。未授予新增原稿003清理 scope，不改正确原稿源审计身份。

再检：正式正文无非必要源类/内部方法/元组列号；相同键位、去重、取消、排序和保存副作用仍完整；不得把必要兼容ID或可观察限制一并删除。

候选证据：`dfe8e726669a83c751d02e923cf290bdafc82bd7:deliverables/final-specification-set/demo-dx/wp73-a-content-editors.md` L71–74,123–126,136。固定blob/SHA256在JSON对应记录。

参考证据：`8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b:Data/Scripts/020_Debug/002_Editor_DataTypes.rb` L1040–1055,1340–1378；`8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b:Data/Scripts/020_Debug/001_Editor_Utilities.rb` L1–159；`8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b:Data/Scripts/021_Compiler/003_Compiler_WritePBS.rb` L626–633。全部静态读取，未执行。

### R04 E088 显示颜色比较基准缺失

120 参数行均匹配，但7.5第214行只说非默认值绿色，E088登记默认−2，未指出显示比较把这个默认归一到−1；尾部编辑归一说明不能替代显示基准。

静态反例：E088当前−2时有别于显示基准−1，因此绿色；当前−1则普通颜色。直接按登记默认−2判断会得到相反结果。该项仍是数值−1..99而非成员引用。

最小修订：分别声明登记默认−2、显示比较基准−1、编辑/复位−1，补两状态颜色邻例。其余119项及白名单排除集合保持。

再检：静态检查−2与−1的颜色结果；120行参数与完整83/22/13/2集合仍等价；不把E088升级为成员索引或修改参考。

候选证据：`dfe8e726669a83c751d02e923cf290bdafc82bd7:deliverables/final-specification-set/demo-dx/wp72-debug-contexts-and-controls.md` L214,403,447。固定blob/SHA256在JSON对应记录。

参考证据：`8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b:Data/Scripts/020_Debug/003_Debug menus/006_Debug_BattleExtraCode.rb` L130,215–245。全部静态读取，未执行。

### R05 旧测试 ID 保持，但五条旧用例的具体前提/结果被“保留”代替

DG-M07、DG-M11、DG-M19、DG-M21、CE-M20 的当前完整行有缺失或历史指代；178 ID、顺序、重数保持与29旧行修改的哈希仅证明身份，不能证明测试内容保全。

静态反例：DG-M07低于−99,999,999的USE输入/左右越界夹限；DG-M11队伍满/队伍与盒全满/物种数超盒容量/口袋容量0；DG-M19三种特性操作双层结果；DG-M21天气/期限/Mega/NPC/环境/空文本；CE-M20六编辑器逐个确认/取消，均不能由“旧/其它/原有...保留”唯一构造现行用例。

最小修订：在当前行恢复仍有效的完整旧前提、次序结果、无写入/错误和相邻对照，或精确引用当前正式正文/现行完整用例对应条款。保留新修正；不恢复已判错误的旧教招、进化文本等。五条 before/after 行哈希见 preservation-check.json，不复制旧正文。

再检：逐条当前行无需找旧版本即可唯一复核；保留新增ACTION/Teach/100字/IV-EV零及保存阶段；178旧ID序与重数、三B18整文件锁继续保持。

候选证据：`52f24036d09503144c6ec89960029db4ed370734:deliverables/final-specification-set/test-catalog/demo-dx-wp72-73-74-75-76-77.md` L17,21,29,31,67；`dfe8e726669a83c751d02e923cf290bdafc82bd7:deliverables/final-specification-set/test-catalog/demo-dx-wp72-73-74-75-76-77.md` L17,21,29,31,67。固定blob/SHA256在JSON对应记录。

### R06 EV 目标端点修正后丢失分配算法及个人 ID 显示

正式143、原稿161、DG-M14只说“现有逐项随机增量与夹限”，不足以独立实现；基线已写明增量范围。个人ID基线十六进制显示也被删除；授权原稿161还省略EV默认/取消、IV默认/取消与觉醒力量类型/威力/合计（正式143仍保留这些），需要在精确原稿同步中保全。

静态反例：目标同为510，不同增量范围或一次随机分配可产生不同最终分布。真实每次先随机选六项索引，满项重试，再均匀抽1..floor(252/4)=63增量并依次夹到剩余目标/该项余量，直到剩余目标0；这不是六维均匀分布。个人ID1应显示0x00000001格式而不是任意十进制。

最小修订：在正式/原稿/测试自足恢复选项、满项重试、整数增量1..63、双夹限、累积终止及重算；同时恢复个人ID十六进制显示（0x前缀、8位大写十六进制）及原稿遗漏的EV/IV默认、取消和觉醒力量显示。保留普通目标0..509/最大510与实际随机序列未验证。

再检：战斗/非战斗随机全体源循环静态等价；参数化上限与默认252/510明确；PID显示和两个16位半区构成均保留；不执行随机向量或宣称最终分布均匀。

候选证据：`dfe8e726669a83c751d02e923cf290bdafc82bd7:deliverables/final-specification-set/demo-dx/wp72-debug-contexts-and-controls.md` L143；`dfe8e726669a83c751d02e923cf290bdafc82bd7:specs/demo/wp72-debug-contexts-and-controls.md` L161；`dfe8e726669a83c751d02e923cf290bdafc82bd7:deliverables/final-specification-set/test-catalog/demo-dx-wp72-73-74-75-76-77.md` L24；`52f24036d09503144c6ec89960029db4ed370734:deliverables/final-specification-set/demo-dx/wp72-debug-contexts-and-controls.md` L142。固定blob/SHA256在JSON对应记录。

参考证据：`8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b:Data/Scripts/020_Debug/003_Debug menus/007_Debug_PokemonCommands.rb` L208–218,255–273,310–317；`8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b:Data/Scripts/020_Debug/003_Debug menus/005_Debug_BattlePkmnCommands.rb` L336–350；`8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b:Data/Scripts/014_Pokemon/001_Pokemon.rb` L87–94。全部静态读取，未执行。

### R07 阴影尺寸资源编号探测缺少首个缺口停止边界

WP73-B正式136/原稿154的“按编号递增探测存在的项”未限定首缺即停，允许解释为枚举所有更大存在项；完整质量审查需要区分。此为新有界补充问题，不冒充已登记C016的SAVE-TIME finding。

静态反例：自有阴影不存在，通用编号1、3存在，2不存在：只提供0、1，3从未探测。相邻1/2/3均存在、4缺失才提供0/1/2/3；1缺失时仅0，不论更大编号存在与否。资源是静态假设，未验证真实媒体存在。

最小修订：明示编号从1逐增，首个解析不到的编号终止，只枚举连续前缀；补缺口/连续/首号缺失对照。原稿同步若需新精确许可应先取得，不将既有scope当质量证据。

再检：首缺停止与三组资源前提有唯一列表结果；保留自有阴影拒绝、浏览即时预览和BACK恢复；保留资源解析/宿主真实素材未验证边界。

候选证据：`dfe8e726669a83c751d02e923cf290bdafc82bd7:deliverables/final-specification-set/demo-dx/wp73-b-world-editors.md` L133–136；`dfe8e726669a83c751d02e923cf290bdafc82bd7:specs/demo/wp73-b-world-editors.md` L151–154；`dfe8e726669a83c751d02e923cf290bdafc82bd7:deliverables/final-specification-set/test-catalog/demo-dx-wp72-73-74-75-76-77.md` L91。固定blob/SHA256在JSON对应记录。

参考证据：`8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b:Data/Scripts/020_Debug/001_Editor screens/004_EditorScreens_SpritePositioning.rb` L167–210。全部静态读取，未执行。

### R08 正式类型编辑不再明确五个主槽及空槽可编辑

基线正式201及NEW原稿220的“主类型5槽＋额外类型”在NEW正式202缩成“已有主类型与额外类型”。当前正式规范未保留固定五个可选择主槽，尤其空槽新增能力。

静态反例：合法在场成员只有一个主类型：参考仍显示五个主类型槽，空槽显示空标记，选择第二空槽可写合法类型；按“已有主类型”实现只给一个槽会丢掉此可观察功能。

最小修订：恢复五个主槽、一个额外槽及空槽显示/可写语义；保留同值确认移除、去空及仅战斗层。五是界面可观察数量，可保留，无须规定内部数组布局。

再检：单一当前类型前提仍有五个可选主槽；空槽可增、同值确认可删、额外槽独立；正文与正确原稿一致，未扩大原稿清理scope。

候选证据：`dfe8e726669a83c751d02e923cf290bdafc82bd7:deliverables/final-specification-set/demo-dx/wp72-debug-contexts-and-controls.md` L202；`dfe8e726669a83c751d02e923cf290bdafc82bd7:specs/demo/wp72-debug-contexts-and-controls.md` L220；`52f24036d09503144c6ec89960029db4ed370734:deliverables/final-specification-set/demo-dx/wp72-debug-contexts-and-controls.md` L201。固定blob/SHA256在JSON对应记录。

参考证据：`8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b:Data/Scripts/020_Debug/003_Debug menus/005_Debug_BattlePkmnCommands.rb` L413–455。全部静态读取，未执行。

## 支持的功能边界

逐项JSON保留PC两入口、寄养/遗迹石取消变量副作用、六种示例队伍及教招顺序、Wonder Room页内/重进有效值、普通/战斗Shadow Teach区别、单角色普通Proc局部break失败、100字符与外部超长旧值、预选偏移、同值自删、天气取消、IV/EV六显式零及父/外层保存、旧复数进化字段与真正导出/重编译、空物种失败。C014目标0..509/最大510已修，分配算法保全仍失败。

WP73-B有界检查支持档案→PBS→成功编译Land0恢复21、OldRod0/正率70对照；登记查询/当前遭遇快照/版本标记分层；SAVE-TIME指标后缀路径、懒登记/导出省略、档案先行部分失败；连接预提交/取消不对称、地形未保存与保存后内存继续改、稀疏ID索引门、缺图/全透明自动定位及整数半像素边界。阴影尺寸枚举首缺停止仍缺R07。

shared 003/C003/C007/C020/WP80只评B19 local contribution。相邻accepted-owner路由和三B18整文件保全见preservation-check.json；不把它们重开、重签、自动转为NOT_AFFECTED，亦不把所有历史source read冒充本轮真实读取。

## 限制与输出

U01–U10、G01–G12、AX01–AX20以及全部具名未读/条件界限保留。真实地图事件、二进制与反序列化、媒体/字体/宿主、容量1024/2048条件、插件/动态调用、完整67树果、八杯赛名单、pokemon_metrics样本、backup/gen5–8与Shadow启用、跨系统随机、deprecated别名/EventScene/动态阴影和真实Demo未穷尽；精确身份见limits.json，真实静态范围和每文件哈希见source-reading-log.json。身份匹配不意味着完整72输入都作同等语义阅读。

本分支仅新增自己的本目录报告与元数据；未改正文、main、原稿、参考、旧证据、canonical229 OPEN/0 CLOSED或既有284 scoped receipts。修订及后续候选重新冻结仍由授权作者/唯一registrar处理。所有报告文件的byte/SHA256/git blob见output-manifest.json；普通推送后另从独立空bare仓库按远端固定commit读回全部输出并核对，实际读回结果在最终交付中报告。
