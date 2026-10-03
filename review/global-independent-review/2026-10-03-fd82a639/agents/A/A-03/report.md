# A-03 独立复审报告：WP18–WP20

项目输入固定提交：`e1e01bb18d824931e54f182dd61af5a9f908ba85`。参考固定提交：`8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`。结论：**REQUIRES_REVISION_SCOPED**。新增6项（P2=2、P3=4）；另有1个既有捕获/伙伴根因传播到WP20，不重复计数。

## 范围与独立性

三份原稿、三份净化正文全文实读；按readiness映射本批没有额外同名附表。CI24、ST59、HP34共117条适用测试逐项对照。来源69个不同文件有实读或具名复用范围（71条覆盖记录，含1条仅发现记录及同一文件的两种阅读记录）；86条阅读记录；145条原稿—净化—测试映射。数量只说明账本规模，不证明覆盖通过。

核心来源：个体1227行、物种455行、Owner73行、Move77行、性别83行、性格173行、能力项119行、状态76行均全文阅读；另有训练家、特性、Shadow、Mega、遭遇修正全文。其余调用者按reading-log逐段限定。设置/查找/编译/保存仅具名复用本代理A-01/A-02同基线实读；捕获收尾复用本代理X独立复核。没有把依赖定点读取当作WP21–WP76整包完成。

先保存独立首判，再形成报告；未读B/C/D新发现或未授权root结论。先前X交叉复核已完成并公开，不伪称本批对该已知问题再次盲审。原始模型请求为Astra/Ultra，工具接受了明确参数；子代理无独立运行型号回显，speed仍未核验且未改设置。

## 工作包处置

| WP | 处置 | 主要理由 |
| --- | --- | --- |
| WP18 | REQUIRES_REVISION_SCOPED | 记录默认值概括与创建随机来源全称需收窄；所有者/缓存/复制已述边界限定确认。 |
| WP19 | REQUIRES_REVISION_SCOPED | 公式/取整/缓存与GR-016已述向量支持；缺少具名性格增减项，不能独立算出由性格决定的能力。 |
| WP20 | REQUIRES_REVISION_SCOPED | 四槽保证、负索引与重学配置边界需明确；既有伙伴捕获换员还原根因传播。 |

## 发现目录

| ID | 级别 | 主题 |
| --- | --- | --- |
| RUN-A-020 | P2 | 缺少性格身份到增减能力项的固定映射 |
| RUN-A-021 | P3 | 物种记录的其余默认值并非全为空 |
| RUN-A-022 | P3 | 创建仅两类随机来源未排除创建形态回调 |
| RUN-A-023 | P2 | 四槽容量未区分学习工具与直接整表写入 |
| RUN-A-024 | P3 | 重学配置的蛋招式表述应限定为已记录的最初招式 |
| RUN-A-025 | P3 | 按索引遗忘遗漏负索引从末尾计数的边界 |

全部发现类型、状态、置信度、功能ID、固定提交/相对路径/精确行、前提/最小静态向量、影响和确定复审条件见 findings.json。下列摘要与该结构化记录同源；没有复制参考源码。

### RUN-A-020 缺少性格身份到增减能力项的固定映射

原稿与净化稿列出25种性格的派生顺序、5种中性性格和其余一升一降的一般规则，但未给出20种非中性身份各自提升、降低哪个能力项；公式却需要按性格求出逐项修正。

固定注册含全部具名映射。LONELY提升攻击并降低防御；BRAVE提升攻击并降低速度。能力重算实际读取这些逐项变化。最终131个Markdown文件的定向检索、WP19全文及WP28相关条款核对，没有找到承接这些能力映射的表；净化室/Palace/形态的性格表有不同用途，不能补足此输入。

最小静态对照：固定数据已按参考规则装载；非蛋、非Shadow的BULBASAUR，形态0，等级50，六IV均31、六EV均0，无IV上限覆盖、无禁用配置。；分别显式采用LONELY和BRAVE作为计算用性格，无其他能力修正；基础攻击49、防御49、速度45来自固定数据。 LONELY：攻击75、防御62、速度65；BRAVE：攻击75、防御69、速度58。；两种不同的具名增减项安排都能满足当前正文的一升一降描述；仅凭最终交付无法唯一推出上述结果。

影响：独立实现即使照搬现有数学公式和全部ST算术向量，也无法从性格身份确定逐项能力，薄荷、生成与设施消费者同受影响。

最小改正：补入独立数据表：25个性格身份、派生次序、提升项/降低项或中性；交付正文明确引用。不要复制注册源码；保持现有取整与缓存规则。

定位：`specs/pokemon-rules/wp19-attributes-ability-and-stats.md:102–108`；`specs/pokemon-rules/wp19-attributes-ability-and-stats.md:173–173`；`deliverables/final-specification-set/pokemon-rules/wp19-attributes-ability-and-stats.md:77–83`；`deliverables/final-specification-set/pokemon-rules/wp19-attributes-ability-and-stats.md:147–147`；`deliverables/final-specification-set/test-catalog/pokemon-rules-wp19-21-22-23-34.md:17–25`；`deliverables/final-specification-set/test-catalog/pokemon-rules-wp19-21-22-23-34.md:37–37`；`deliverables/final-specification-set/creature-rpg/wp28-item-use-and-training.md:154–161`。参考：`Data/Scripts/010_Data/001_Hardcoded data/009_Nature.rb:30–173`；`Data/Scripts/014_Pokemon/001_Pokemon.rb:496–503`；`Data/Scripts/014_Pokemon/001_Pokemon.rb:1099–1117`；`PBS/pokemon.txt:3–17`。

### RUN-A-021 物种记录的其余默认值并非全为空

默认值目录列完若干字段后称其余空数组/空值，范围覆盖了同节列出的名字、分类、图鉴文本、图鉴形态、变身数值等字段。

记录构造会为原始名字提供Unnamed，分类和图鉴文本提供???；图鉴形态缺省取该记录的形态号；unmega_form和mega_message缺省为0；来源尾注为空字符串。它们不是统一的空值。

最小静态对照：人工的直接物种记录构造输入：有效身份S、形态2；标准六主能力登记存在；省略其余可选字段。；只核对记录构造与原始字段；不声称同样缺省输入必能通过PBS编译器，也不读取缺失翻译素材。 原始名字=Unnamed、原始分类=???、原始图鉴文本=???、pokedex_form=2、unmega_form=0、mega_message=0。；其余字段全置空的实现会在上述字段与参考不同。

影响：默认数据合同不完整，直接记录创建、图鉴形态归类和后续消费者可能得到空值而非已定义默认值。

最小改正：将默认目录补齐或把其余概括限定到明确列出的集合/可选空值字段；区分空数组、空字符串、空值、数值0与继承形态。

定位：`specs/creature-rpg/wp18-creature-identity-species-ownership.md:59–81`；`deliverables/final-specification-set/creature-rpg/wp18-creature-identity-species-ownership.md:58–80`。参考：`Data/Scripts/010_Data/002_PBS data/008_Species.rb:175–220`。

### RUN-A-022 创建仅两类随机来源未排除创建形态回调

创建时只有personalID与六项IV两类随机来源；该句未限定为基础初始化阶段。

默认启用的创建形态复检位于返回之前。UNOWN额外抽取0–27，PUMPKABOO等也有独立形态抽样。WP21净化正文已准确给出这些规则，因此问题是WP18全称与跨包范围衔接。

最小静态对照：无插件；UNOWN基形态0、合法等级；启用创建复检；所需数据和玩家/图鉴依赖有效，所有回调正常返回。；两次静态对照的六IV与personalID随机结果相同，环境和其它输入相同；仅创建处理器的后续随机结果分别为0和1。 两次创建返回形态分别为0和1；还存在第三类生成期随机输入。；关闭复检或不存在额外随机回调时，基础初始化仍只有所列IV与personalID两类。

影响：照全称句设计确定性生成或随机输入清单，会遗漏创建回调；与同套WP21正确数据冲突。

最小改正：把两类限定为个体基础初始化自身，明确创建回调可增加随机输入并引用WP21；不删去WP21现有形态规则。

定位：`specs/creature-rpg/wp18-creature-identity-species-ownership.md:164–168`；`deliverables/final-specification-set/creature-rpg/wp18-creature-identity-species-ownership.md:168–172`；`deliverables/final-specification-set/pokemon-rules/wp21-dynamic-forms-and-display.md:60–73`。参考：`Data/Scripts/014_Pokemon/001_Pokemon.rb:1194–1197`；`Data/Scripts/014_Pokemon/001_Pokemon.rb:1215–1224`；`Data/Scripts/014_Pokemon/001_Pokemon-related/001_FormHandlers.rb:146–150`；`Data/Scripts/014_Pokemon/001_Pokemon-related/001_FormHandlers.rb:448–458`；`PBS/pokemon.txt:5299–5322`。

### RUN-A-023 四槽容量未区分学习工具与直接整表写入

正文把招式槽上限4列作状态不变量，同时只说可直接替换整表，未说明整表写入和外露列表没有四项校验，也未限定学习入口仅保持原先有效的容量。

直接整表写入原样保存；计数读取真实长度。静默学习已知招只移动该对象，新招仅移除首项一次，不把任意超长列表修复为四项。重置默认招式才重新取最多四项。

最小静态对照：人工字段入口向一个有效个体写入五个独立合法招式对象，顺序TACKLE、GROWL、POUND、SCRATCH、TAILWHIP；各招式存在，初始PP合法。；不主张普通教学UI会产生五槽；无额外插件或列表规范化步骤。随后直接调用静默学习LEER。 写入后计数为5；学习LEER后依次为GROWL、POUND、SCRATCH、TAILWHIP、LEER，计数仍5。；对照从四槽开始学习新招仍为四槽；默认招式重置输出至多四槽。

影响：独立实现可能增加来源不存在的校验或截断；超长状态在复制、计数和学习上的结果无法按当前不变量实现。

最小改正：将4项保证限定到正常初始化/学习的有效起点，明确直接整表写入不校验，静默学习只删除首项一次；保留人工边界，不推广为常规游戏可达。

定位：`specs/creature-rpg/wp20-hp-status-moves-helditem.md:121–131`；`specs/creature-rpg/wp20-hp-status-moves-helditem.md:203–203`；`deliverables/final-specification-set/creature-rpg/wp20-hp-status-moves-helditem.md:123–133`；`deliverables/final-specification-set/creature-rpg/wp20-hp-status-moves-helditem.md:209–209`。参考：`Data/Scripts/014_Pokemon/001_Pokemon.rb:29–32`；`Data/Scripts/014_Pokemon/001_Pokemon.rb:605–615`；`Data/Scripts/014_Pokemon/001_Pokemon.rb:625–660`；`Data/Scripts/014_Pokemon/001_Pokemon.rb:1145–1147`；`PBS/moves.txt:5289–5300`；`PBS/moves.txt:5314–5337`；`PBS/moves.txt:5961–5971`；`PBS/moves.txt:6055–6064`；`PBS/moves.txt:6552–6562`。

### RUN-A-024 重学配置的蛋招式表述应限定为已记录的最初招式

配置表概括为决定记录/蛋招式是否成为重学候选，未限定蛋招式必须已进入个体的最初招式记录，容易与兼容判定的整个物种蛋招式表混合。

界面只读取当前等级可达表，再按开关合并最初招式记录；没有直接合并物种蛋招式表。配置注释也限定为孵化时已经会的蛋招式。WP30已有正确的两来源描述。

最小静态对照：固定数据的BULBASAUR，等级5、非蛋非Shadow、默认已知TACKLE/GROWL/VINEWHIP、first_moves为空；默认世代8开关开启。；AMNESIA已登记、在物种蛋招式表，但不在等级可达表或当前列表；其它依赖正常。 开启开关不会使AMNESIA出现在重学列表。；将AMNESIA逐项加入最初记录后，开关开启才把它加入界面候选；关闭开关则不加入，个体可重学判定与界面列表仍是不同入口。

影响：将物种蛋招式表作为额外候选来源会开放未曾掌握的招式，造成跨WP20/WP30不一致。

最小改正：配置行改为最初招式记录中的额外招式（可含已记录的蛋招式），引用WP30；明确不直接枚举整个物种蛋招式表。

定位：`specs/creature-rpg/wp20-hp-status-moves-helditem.md:138–145`；`specs/creature-rpg/wp20-hp-status-moves-helditem.md:225–225`；`deliverables/final-specification-set/creature-rpg/wp20-hp-status-moves-helditem.md:140–147`；`deliverables/final-specification-set/creature-rpg/wp20-hp-status-moves-helditem.md:231–231`；`deliverables/final-specification-set/creature-rpg/wp30-growth-learning-and-friendship.md:163–169`。参考：`Data/Scripts/016_UI/022_UI_MoveRelearner.rb:150–165`；`Data/Scripts/014_Pokemon/001_Pokemon.rb:717–723`；`Data/Scripts/001_Settings.rb:147–151`；`PBS/pokemon.txt:3–18`；`PBS/moves.txt:7324–7332`。

### RUN-A-025 按索引遗忘遗漏负索引从末尾计数的边界

净化稿只称按索引删除越界无效果；原稿附有参考语言容器语义提示，但两者均未用独立规则说明负索引。

直接删除入口采用支持负索引的列表删除语义：长度n时，-1删除末项、-n删除首项，小于-n或大于等于n才无效果。已读调试调用者先拒绝负的取消值，不应把该UI守卫移到通用入口。

最小静态对照：直接字段工具入口；当前两个合法招式对象依次TACKLE/GROWL；每个对照独立从相同列表开始。；不经已检查的调试菜单取消守卫，不声称正常菜单取消会删除招式。 索引-1→仅余TACKLE；索引-2→仅余GROWL；索引-3或2→列表不变。

影响：实现者把所有负索引当越界会改变直接调用行为；删除语言提示后，独立规格无法确定有效负区间。

最小改正：以长度n和等效位置n+i描述有效负索引，给出两端边界；保持正常菜单取消守卫属于调用者。

定位：`specs/creature-rpg/wp20-hp-status-moves-helditem.md:129–129`；`deliverables/final-specification-set/creature-rpg/wp20-hp-status-moves-helditem.md:131–131`。参考：`Data/Scripts/014_Pokemon/001_Pokemon.rb:670–674`；`Data/Scripts/020_Debug/003_Debug menus/007_Debug_PokemonCommands.rb:473–483`。

## 既有根因传播与非发现边界

- X-A-CAPTURE-PARTNER（自有已发布记录c5705d39763ff3540bbab011f3d7bd64f5548325）传播至WP20原稿185–195、净化189–199：有伙伴时参战序列与当前玩家队伍分离，送箱成员仍可被结束还原访问；不能概括为送箱就退出循环。保持已验证的无临时移除主向量；A当前空的暂时移除版本仍须给出合法前史，不能让野生敌人使用受禁止的Knock Off。由root绑定已有规范发现ID，新增计数0。
- HP-30在伙伴场景可能仍保留捕获个体持物，但原因是该新个体不在旧参战还原序列；不能由结果碰巧一致证明原稿原因正确。
- 克隆检查区分独立对象、共享内部对象与字段重新绑定：普通克隆保留markings引用；进化复制入口重新绑定空markings。Owner复制只确证新Owner对象，未把内部可变名字字符串保证为递归深拷贝；Shadow暂存EV共享风险留在WP23范围，本批不把已声明未穷尽的部分包装为新已闭合保证。
- 保留参考现状：HP上限增加可使濒死个体恢复；负PP计数先提交后钳制失败；隐藏特性缺槽后仍可报告隐藏索引；两个异色缓存可以不同步；GR-008整表首招记录保留重复；GR-016设施EV255及四项508。没有把这些准确记录当成规格错误。
- 附加审计定位：audit/source-traceability.md:668中的`012_Overworld/003_Overworld_WildEncounters.rb`缺少`002_Battle triggering/`。真实文件已实读370–460；应修路径。该附加定位与A-02 RUN-A-017的审计路径问题同类，留给root合并，不另增发现数量。

## 测试与覆盖限制

117条测试均有单独等价账。CI-01还需固定命运开关关闭；CI-07需目标基身份不同；HP-12需排除随后完整治疗；ST38只是派生向量摘要，实际fixture须控制随机输入/Owner/比例/缓存。HP-28限合法暂时移除且成员映射不变。上述前提提示不另立重复发现；任何复审不得以缺前提的简写向量覆盖已发现反例。

主入口、固定注册、数据样本、直接赋值与工具、别名叠加、主要调用者、失败阶段和默认配置已经有界核对。未逐一验证全部物种/PBS数据、全部动态形态/战斗效果、所有插件和事件直接写入、完整配置交叉积、资源图标和宿主运行。搜索未命中不等于功能不存在。

未运行参考、游戏、编译器、生成器、反序列化器或行为模拟器；运行观察0，已证明demo链0。保留U01–U10、G01–G12与既有20条AX，不升级、不代填。仅新增A-03复审产物；不改正式规格、中央Feature Matrix、参考源或任何框架实现。

## 复审与交接

先补齐具名Nature映射，再逐项复核原稿/净化/具名向量；校正范围全称和入口边界；对WP20链接既有伙伴捕获根因。发布前检查所有证据行与JSON/TSV结构、输出卫生和A目录白名单。普通推送A分支并核验远端精确提交后，按父代理授权进入A-04[WP21–23]，每次仅一个批次活动。
