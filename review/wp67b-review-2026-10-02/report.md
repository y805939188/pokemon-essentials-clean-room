# WP67-B 首版独立审查

2026-10-02；仅静态审查。

**结论：REQUEST_CHANGES。当前不能进入 WP37。** 共16项待关闭：15项P2行为／来源分离问题，1项P3覆盖计数问题。登记通过不等于行为规格通过。

被审主稿：`specs/ui/wp67-b-lifecycle-presentations-and-history.md`，SHA-256 `03b7146c697c8b6bf4196a9245f557446fa68c2c9c4f8de8c8bc8d62d0e4f051`，45,009字节。固定副本见[input-snapshot](input-snapshot/specs/ui/wp67-b-lifecycle-presentations-and-history.md)；全部输入身份见[inputs.json](inputs.json)。

## 1. 已通过的检查与保留边界

manifest §1的1,153条完整身份及2条旧无哈希记录、主TSV v71的1,058行已独立核验；完整身份／字节均与磁盘一致，无重复路径。登记末检的当前身份一致；旧§2／§3／§4和主要标题完整保留，变更仅插入本轮内容。相对于上轮批准交接，既有文件仅矩阵F16-06、manifest和主TSV发生允许的登记变化。L01–L28定义唯一。详见[registration-checks.json](registration-checks.json)。

26份依赖规格和37份起始来源身份保持；reference固定提交为`8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`且Git清洁。六份主来源已全文审阅；共同输入／命名、调用者、容量工具等另行定点取证，见[source-checks.json](source-checks.json)。所有反例均为静态推导，未运行游戏、UI、演出或行为模型。

WP67-A累计17项、WP65八项、GR-001～016、WP23-N01和其余既有批准范围保持关闭；WP23跨级净化失败、同等级／遗迹石对照与WP32-N02宿主未决继续有效。下列冲突要求修正新WP67-B的摘要和传播，并非重开或修改上游。

## 2. 待修订项

### WP67B-R01 · P2 · 满级稀有糖默认开启，且是无升级的独立演出入口

位置：[specs/ui/wp67-b-lifecycle-presentations-and-history.md:52](</Users/dingshinn/Desktop/pokemon-framework-reference/specs/ui/wp67-b-lifecycle-presentations-and-history.md:52>)；[specs/ui/wp67-b-lifecycle-presentations-and-history.md:169](</Users/dingshinn/Desktop/pokemon-framework-reference/specs/ui/wp67-b-lifecycle-presentations-and-history.md:169>)；[review/wp67b-delivery-2026-10-01/entry-coverage-table.md:9](</Users/dingshinn/Desktop/pokemon-framework-reference/review/wp67b-delivery-2026-10-01/entry-coverage-table.md:9>)。

§9把满级稀有糖配置写成默认假；§3.1与附表又把糖果全部并到等级变化后的成长工具。固定基线的规则世代为8，该配置默认开启。满级分支直接检查目标并调用可取消演出，不经过等级变化辅助；因此这不是默认关闭的潜在分支。取消后处理器仍报用物成功，外层正常消费，不能以“没有进化”推断退回糖果。

**有限修订**：改正默认值；正文和附表补独立的满级糖入口、取消权限、无等级变化、处理器返回与消耗时点，沿用WP31/WP28合同，不重做进化条件目录。

**最小对照**：
- 默认世代8、满级、合法进化目标、库存1、动画中BACK：物种和等级不变，取消统计增加，正常返回后糖果消费。
- 配置关闭或无目标：无效提示、不进入演出、不消费。

**来源**：[001_Settings.rb:17–17](</Users/dingshinn/Desktop/pokemon-framework-reference/reference/pokemon-essentials/Data/Scripts/001_Settings.rb:17>)；[001_Settings.rb:243–245](</Users/dingshinn/Desktop/pokemon-framework-reference/reference/pokemon-essentials/Data/Scripts/001_Settings.rb:243>)；[013_Items/002_Item_Effects.rb:917–947](</Users/dingshinn/Desktop/pokemon-framework-reference/reference/pokemon-essentials/Data/Scripts/013_Items/002_Item_Effects.rb:917>)；[013_Items/001_Item_Utilities.rb:661–694](</Users/dingshinn/Desktop/pokemon-framework-reference/reference/pokemon-essentials/Data/Scripts/013_Items/001_Item_Utilities.rb:661>)。

### WP67B-R02 · P2 · 图鉴页内收尾必须按进化、交换、孵化分别限定

位置：[specs/ui/wp67-b-lifecycle-presentations-and-history.md:73](</Users/dingshinn/Desktop/pokemon-framework-reference/specs/ui/wp67-b-lifecycle-presentations-and-history.md:73>)；[review/wp67b-delivery-2026-10-01/entry-coverage-table.md:14](</Users/dingshinn/Desktop/pokemon-framework-reference/review/wp67b-delivery-2026-10-01/entry-coverage-table.md:14>)。

§3.3将进化的图鉴条件页概括为同样在页内收尾，遗漏“待学招式列表为空”条件；附表把三类图鉴入口合成一行并共同挂WP32-N02，进一步把交换的两处收尾风险传播到孵化。进化列表非空时页内只清消息，随后学招，再由调用者收尾；列表为空时才在页内提前收尾。孵化的图鉴页没有对应提前结束原场景的调用。

**有限修订**：分开三类条件页的后续：交换保留WP32-N02；进化补空/非空列表门与外层收尾（按等级条目收集的候选列表，不是最终实际学到的新招数量）；孵化返回后继续命名并正常结束。宿主重复释放保持未证，不称安全、必定重复进化或统一幂等。

**最小对照**：
- 进化图鉴门全真且待学列表非空：条目页后仍可进入学招，页内不结束原进化画面。
- 进化同门且待学列表空：页内提前收尾加外层收尾两处调用，宿主结果未证；交换、孵化作对照。

**来源**：[016_UI/001_Non-interactive UI/004_UI_Evolution.rb:232–253](</Users/dingshinn/Desktop/pokemon-framework-reference/reference/pokemon-essentials/Data/Scripts/016_UI/001_Non-interactive UI/004_UI_Evolution.rb:232>)；[016_UI/001_Non-interactive UI/005_UI_Trading.rb:157–169](</Users/dingshinn/Desktop/pokemon-framework-reference/reference/pokemon-essentials/Data/Scripts/016_UI/001_Non-interactive UI/005_UI_Trading.rb:157>)；[016_UI/001_Non-interactive UI/005_UI_Trading.rb:197–210](</Users/dingshinn/Desktop/pokemon-framework-reference/reference/pokemon-essentials/Data/Scripts/016_UI/001_Non-interactive UI/005_UI_Trading.rb:197>)；[016_UI/001_Non-interactive UI/003_UI_EggHatching.rb:110–133](</Users/dingshinn/Desktop/pokemon-framework-reference/reference/pokemon-essentials/Data/Scripts/016_UI/001_Non-interactive UI/003_UI_EggHatching.rb:110>)。

### WP67B-R03 · P2 · 命名取消要区分输入模式，并区分返回空文本与清除昵称

位置：[specs/ui/wp67-b-lifecycle-presentations-and-history.md:89](</Users/dingshinn/Desktop/pokemon-framework-reference/specs/ui/wp67-b-lifecycle-presentations-and-history.md:89>)；[specs/ui/wp67-b-lifecycle-presentations-and-history.md:217](</Users/dingshinn/Desktop/pokemon-framework-reference/specs/ui/wp67-b-lifecycle-presentations-and-history.md:217>)；[review/wp67b-delivery-2026-10-01/entry-coverage-table.md:24](</Users/dingshinn/Desktop/pokemon-framework-reference/review/wp67b-delivery-2026-10-01/entry-coverage-table.md:24>)。

“文字输入的取消返回空串”未限定键盘模式，L07又把直接取消作为普遍可执行操作。默认光标模式的BACK是删除字符，不退出；该模式需选OK提交（最小长度为0时可提交空文本）。键盘模式Esc才返回空文本。此外，空文本交给名称写入后会清除昵称；不是把昵称字段保留为空串再仅在显示时回退。

**有限修订**：按WP17/WP18分列拒绝命名确认、键盘Esc、光标BACK和空文本OK。写明输入返回值用途及昵称清除、物种名显示；保持图鉴与前序领域提交不回滚。必要时把命名完成分支描述为“进入输入且返回”，不等同于最终确有昵称。

**最小对照**：
- 默认光标模式输入AB后BACK：成为A、仍停留；删空后OK才返回。
- 键盘模式Esc：返回空文本，调用者清昵称、显示物种名；命名确认No则不进入输入。

**来源**：[016_UI/025_UI_TextEntry.rb:180–198](</Users/dingshinn/Desktop/pokemon-framework-reference/reference/pokemon-essentials/Data/Scripts/016_UI/025_UI_TextEntry.rb:180>)；[016_UI/025_UI_TextEntry.rb:666–721](</Users/dingshinn/Desktop/pokemon-framework-reference/reference/pokemon-essentials/Data/Scripts/016_UI/025_UI_TextEntry.rb:666>)；[016_UI/025_UI_TextEntry.rb:754–777](</Users/dingshinn/Desktop/pokemon-framework-reference/reference/pokemon-essentials/Data/Scripts/016_UI/025_UI_TextEntry.rb:754>)；[016_UI/015_UI_Options.rb:24–34](</Users/dingshinn/Desktop/pokemon-framework-reference/reference/pokemon-essentials/Data/Scripts/016_UI/015_UI_Options.rb:24>)；[014_Pokemon/001_Pokemon.rb:877–890](</Users/dingshinn/Desktop/pokemon-framework-reference/reference/pokemon-essentials/Data/Scripts/014_Pokemon/001_Pokemon.rb:877>)；[016_UI/001_Non-interactive UI/003_UI_EggHatching.rb:123–143](</Users/dingshinn/Desktop/pokemon-framework-reference/reference/pokemon-essentials/Data/Scripts/016_UI/001_Non-interactive UI/003_UI_EggHatching.rb:123>)。

### WP67B-R04 · P2 · 直接孵化与仅播放演出不能共用领域写入一栏

位置：[specs/ui/wp67-b-lifecycle-presentations-and-history.md:80](</Users/dingshinn/Desktop/pokemon-framework-reference/specs/ui/wp67-b-lifecycle-presentations-and-history.md:80>)；[review/wp67b-delivery-2026-10-01/entry-coverage-table.md:22](</Users/dingshinn/Desktop/pokemon-framework-reference/review/wp67b-delivery-2026-10-01/entry-coverage-table.md:22>)。

附表把pbHatch与pbHatchAnimation合并后，在状态写入栏写“同上”，从而让仅播放演出的入口也继承孵化统计、拥有者、亲密度、时间、来源、地图、首招等前序写入。实际这些写入在pbHatch中；直接调用演出包装不会先执行它们。演出本身仍会清昵称、登记图鉴和按选项命名，不能反过来写成完全无状态影响。

**有限修订**：分列两个直接入口以及正常迈步入口：分别登记前序领域字段、演出内写入、计数归零的归属和返回。只有演出包装在正常返回时明确返回真；纯消息回退不可达结论保持。不要给直接调用补蛋态或防重门。

**最小对照**：
- 人工入口对照：同一组初值分别直接孵化与仅调用演出；仅演出不增加孵化统计、不重写拥有者/亲密度/孵化来源等，但仍可能清昵称和更新图鉴。
- 目标尚有正孵化计数时，直接入口本身不负责归零；与迈步先归零再孵化分开。

**来源**：[016_UI/001_Non-interactive UI/003_UI_EggHatching.rb:102–143](</Users/dingshinn/Desktop/pokemon-framework-reference/reference/pokemon-essentials/Data/Scripts/016_UI/001_Non-interactive UI/003_UI_EggHatching.rb:102>)；[016_UI/001_Non-interactive UI/003_UI_EggHatching.rb:202–249](</Users/dingshinn/Desktop/pokemon-framework-reference/reference/pokemon-essentials/Data/Scripts/016_UI/001_Non-interactive UI/003_UI_EggHatching.rb:202>)；[016_UI/001_Non-interactive UI/003_UI_EggHatching.rb:252–268](</Users/dingshinn/Desktop/pokemon-framework-reference/reference/pokemon-essentials/Data/Scripts/016_UI/001_Non-interactive UI/003_UI_EggHatching.rb:252>)。

### WP67B-R05 · P2 · 交换首张信息卡是可按键提前结束的2.5秒等待

位置：[specs/ui/wp67-b-lifecycle-presentations-and-history.md:102](</Users/dingshinn/Desktop/pokemon-framework-reference/specs/ui/wp67-b-lifecycle-presentations-and-history.md:102>)；[review/wp67b-delivery-2026-10-01/entry-coverage-table.md:30](</Users/dingshinn/Desktop/pokemon-framework-reference/review/wp67b-delivery-2026-10-01/entry-coverage-table.md:30>)。

首张送出者信息卡被写成“等待输入/等输入”，会导出不按键就一直停留的交互。实际调用共享等待时给50个逻辑时间单位，按20单位/秒换算为2.5秒；USE或BACK可提前结束这次等待。BACK在此处是推进信息卡，不是取消交换，后续消息仍有各自等待规则。

**有限修订**：将首卡等待与随后告别/接收消息区分，写明2.5秒自然推进及USE/BACK提前推进；保持交换不可取消的领域结论。

**最小对照**：
- 首卡不输入：2.5秒期限后进入送出段；首卡按BACK：提前进入送出段而非撤销交换。

**来源**：[016_UI/001_Non-interactive UI/005_UI_Trading.rb:180–190](</Users/dingshinn/Desktop/pokemon-framework-reference/reference/pokemon-essentials/Data/Scripts/016_UI/001_Non-interactive UI/005_UI_Trading.rb:180>)；[007_Objects and windows/011_Messages.rb:805–819](</Users/dingshinn/Desktop/pokemon-framework-reference/reference/pokemon-essentials/Data/Scripts/007_Objects and windows/011_Messages.rb:805>)。

### WP67B-R06 · P2 · 净化室命令CANCEL与总览BACK不是同一退出层

位置：[specs/ui/wp67-b-lifecycle-presentations-and-history.md:122](</Users/dingshinn/Desktop/pokemon-framework-reference/specs/ui/wp67-b-lifecycle-presentations-and-history.md:122>)；[review/wp67b-delivery-2026-10-01/entry-coverage-table.md:38](</Users/dingshinn/Desktop/pokemon-framework-reference/review/wp67b-delivery-2026-10-01/entry-coverage-table.md:38>)。

正文把选组后的EDIT/SWITCH/CANCEL菜单中的CANCEL直接连接到“Continue viewing holograms?”。实际CANCEL或该命令菜单的BACK只返回总览选组循环；在总览选组层按BACK才弹该确认。SWITCH目标选择取消则返回原组，执行同组交换而不弹退出确认。详细组里的命令菜单取消也只回位置选择，不能与详细组BACK的持握/继续编辑判断合并。

**有限修订**：用小表分清总览选组、选组后命令、换组目标、详细位置选择、详细操作菜单五层；确认的Yes/No/BACK结果继承共享UI。保留持握成员阻止退出与编辑结束后合格检查。

**最小对照**：
- 选组→CANCEL：回总览、无继续查看确认；总览BACK：确认Yes继续、No或确认BACK退出。
- SWITCH→目标BACK：组内容不变；详细操作菜单BACK回位置选择，详细位置BACK才做持握门/继续编辑确认。

**来源**：[016_UI/023_UI_PurifyChamber.rb:421–455](</Users/dingshinn/Desktop/pokemon-framework-reference/reference/pokemon-essentials/Data/Scripts/016_UI/023_UI_PurifyChamber.rb:421>)；[016_UI/023_UI_PurifyChamber.rb:525–545](</Users/dingshinn/Desktop/pokemon-framework-reference/reference/pokemon-essentials/Data/Scripts/016_UI/023_UI_PurifyChamber.rb:525>)；[016_UI/023_UI_PurifyChamber.rb:596–627](</Users/dingshinn/Desktop/pokemon-framework-reference/reference/pokemon-essentials/Data/Scripts/016_UI/023_UI_PurifyChamber.rb:596>)；[016_UI/023_UI_PurifyChamber.rb:1168–1229](</Users/dingshinn/Desktop/pokemon-framework-reference/reference/pokemon-essentials/Data/Scripts/016_UI/023_UI_PurifyChamber.rb:1168>)；[016_UI/018_UI_ItemStorage.rb:240–274](</Users/dingshinn/Desktop/pokemon-framework-reference/reference/pokemon-essentials/Data/Scripts/016_UI/018_UI_ItemStorage.rb:240>)；[016_UI/018_UI_ItemStorage.rb:341–374](</Users/dingshinn/Desktop/pokemon-framework-reference/reference/pokemon-essentials/Data/Scripts/016_UI/018_UI_ItemStorage.rb:341>)。

### WP67B-R07 · P2 · REPLACE沿用原始Shadow结果相等门，且有蛋例外

位置：[specs/ui/wp67-b-lifecycle-presentations-and-history.md:123](</Users/dingshinn/Desktop/pokemon-framework-reference/specs/ui/wp67-b-lifecycle-presentations-and-history.md:123>)；[specs/ui/wp67-b-lifecycle-presentations-and-history.md:124](</Users/dingshinn/Desktop/pokemon-framework-reference/specs/ui/wp67-b-lifecycle-presentations-and-history.md:124>)；[review/wp67b-delivery-2026-10-01/entry-coverage-table.md:39](</Users/dingshinn/Desktop/pokemon-framework-reference/review/wp67b-delivery-2026-10-01/entry-coverage-table.md:39>)。

“同Shadow属性才替换”与紧邻的统一放置门省掉了WP23已通过的两个关键区别。替换比较的是原始查询结果：新普通个体的空值与已净化个体的假值不相等，不能先归一成“都非Shadow”。REPLACE也不调用普通放置的拒蛋门，双方原始结果相等时，普通蛋可替换外圈成员。

**有限修订**：把普通PLACE与REPLACE各自守卫和提交分开写，直接引用WP23 §8.1的三组原始值对照及蛋例外；不重开WP23，不给参考补守卫。

**最小对照**：
- 新普通/新普通的空值对照通过；新普通/已净化的空值与假值对照拒绝；两只已净化的假值对照通过此门。
- 同一未设Shadow标志普通蛋：空位普通放置拒绝；替换同原始结果的外圈成员可通过替换门。

**来源**：[016_UI/023_UI_PurifyChamber.rb:361–407](</Users/dingshinn/Desktop/pokemon-framework-reference/reference/pokemon-essentials/Data/Scripts/016_UI/023_UI_PurifyChamber.rb:361>)；[016_UI/023_UI_PurifyChamber.rb:497–510](</Users/dingshinn/Desktop/pokemon-framework-reference/reference/pokemon-essentials/Data/Scripts/016_UI/023_UI_PurifyChamber.rb:497>)；[014_Pokemon/003_Pokemon_ShadowPokemon.rb:100–102](</Users/dingshinn/Desktop/pokemon-framework-reference/reference/pokemon-essentials/Data/Scripts/014_Pokemon/003_Pokemon_ShadowPokemon.rb:100>)。

### WP67B-R08 · P2 · WITHDRAW使用双满门，入盒失败后仍清源

位置：[specs/ui/wp67-b-lifecycle-presentations-and-history.md:123](</Users/dingshinn/Desktop/pokemon-framework-reference/specs/ui/wp67-b-lifecycle-presentations-and-history.md:123>)；[review/wp67b-delivery-2026-10-01/entry-coverage-table.md:39](</Users/dingshinn/Desktop/pokemon-framework-reference/review/wp67b-delivery-2026-10-01/entry-coverage-table.md:39>)。

“盒子满就拒绝取出”与WP23已批准合同冲突。此处拒绝门要求队伍满且全部盒满；通过后却只尝试入盒，不优先入队，也不检查入盒返回值。全部盒满、队伍有空位时会通过拒绝门，入盒失败后仍清当前位置或持握引用。不能把该输入写成保留源成员的拒绝，也不能与净化后通用领取混为一条容量规则。

**有限修订**：沿用WP23的WITHDRAW三分支：双满拒绝、盒有位成功入盒、盒满但队伍有位时失败仍清源。与§6.3净化后通用存放单独列明。

**最小对照**：
- 净化室中非自动净化状态、所有盒满、队伍有空位，选WITHDRAW：不显示双满拒绝，入盒失败，源被清，不保证成员仍被任一容器持有。
- 队伍也满则拒绝且源保留；盒有位时存盒，不以队伍空位改成入队。

**来源**：[016_UI/023_UI_PurifyChamber.rb:474–488](</Users/dingshinn/Desktop/pokemon-framework-reference/reference/pokemon-essentials/Data/Scripts/016_UI/023_UI_PurifyChamber.rb:474>)；[019_Utilities/002_Utilities_Pokemon.rb:4–6](</Users/dingshinn/Desktop/pokemon-framework-reference/reference/pokemon-essentials/Data/Scripts/019_Utilities/002_Utilities_Pokemon.rb:4>)；[014_Pokemon/001_Pokemon-related/004_PokemonStorage.rb:231–252](</Users/dingshinn/Desktop/pokemon-framework-reference/reference/pokemon-essentials/Data/Scripts/014_Pokemon/001_Pokemon-related/004_PokemonStorage.rb:231>)。

### WP67B-R09 · P2 · 迈步准备提示只在正心量下降到合格时触发

位置：[specs/ui/wp67-b-lifecycle-presentations-and-history.md:115](</Users/dingshinn/Desktop/pokemon-framework-reference/specs/ui/wp67-b-lifecycle-presentations-and-history.md:115>)。

正文把“合格时在迈步处提示”写成状态条件，漏了每步入口先跳过心量已为0的中心。心量已0的后续每步不会重复提示；通过编成变化让一个原本心量0的组新变合格，也不会靠下一步补提示，应由打开/编辑结束检查发现。该区别已经明确在WP23中，本包不能用概括句改掉它。

**有限修订**：将步进提示改成有入口前提的状态转移：本步开始心量为正，经本步减量后满足资格才提示；已0跳过。继续把自动净化放在打开与结束编辑的检查点。

**最小对照**：
- 本步由正心量降为0且合格：提示一次；下一步仍0：不提示。
- 原先心量0、无外圈，后来加普通成员：不要推断下一步自动补提示或直接净化。

**来源**：[016_UI/023_UI_PurifyChamber.rb:234–262](</Users/dingshinn/Desktop/pokemon-framework-reference/reference/pokemon-essentials/Data/Scripts/016_UI/023_UI_PurifyChamber.rb:234>)。

### WP67B-R10 · P2 · 遗迹石外层不要求可战斗，选择界面也不会隐藏不合格成员

位置：[specs/ui/wp67-b-lifecycle-presentations-and-history.md:138](</Users/dingshinn/Desktop/pokemon-framework-reference/specs/ui/wp67-b-lifecycle-presentations-and-history.md:138>)；[review/wp67b-delivery-2026-10-01/entry-coverage-table.md:49](</Users/dingshinn/Desktop/pokemon-framework-reference/review/wp67b-delivery-2026-10-01/entry-coverage-table.md:49>)。

外层开放资格被写成“可战斗Shadow且心量0”，但外层只调用一般可净化查询，包含非Lugia门而没有HP/可战斗门。可战斗门在后续选人谓词才出现。选择画面使用整个队伍并标可选/不可选，不是“只列”合格成员。只有一只濒死、非蛋、非Lugia、心量0的Shadow时，外层仍会显示可打开心灵消息并进入队伍画面，该成员随后被标不可选。

**有限修订**：分开外层开放、队伍显示与选中许可、最终统一净化三层；保留已通过的Lugia选择例外。取消可不写净化状态，但选人包装仍会按WP66-A写选择结果变量，不泛称完全无状态写入。

**最小对照**：
- 队伍只有上述濒死非Lugia：入口开放、该成员不可选，可取消退出。
- 另有允许外层开放的非Lugia时，存活零心量Lugia仍可选择；不合格成员仍显示并拒选。

**来源**：[014_Pokemon/001_Pokemon-related/002_ShadowPokemon_Other.rb:147–160](</Users/dingshinn/Desktop/pokemon-framework-reference/reference/pokemon-essentials/Data/Scripts/014_Pokemon/001_Pokemon-related/002_ShadowPokemon_Other.rb:147>)；[014_Pokemon/003_Pokemon_ShadowPokemon.rb:188–192](</Users/dingshinn/Desktop/pokemon-framework-reference/reference/pokemon-essentials/Data/Scripts/014_Pokemon/003_Pokemon_ShadowPokemon.rb:188>)；[016_UI/005_UI_Party.rb:1141–1169](</Users/dingshinn/Desktop/pokemon-framework-reference/reference/pokemon-essentials/Data/Scripts/016_UI/005_UI_Party.rb:1141>)；[016_UI/005_UI_Party.rb:1504–1523](</Users/dingshinn/Desktop/pokemon-framework-reference/reference/pokemon-essentials/Data/Scripts/016_UI/005_UI_Party.rb:1504>)。

### WP67B-R11 · P2 · 遗迹石画面包装没有恒真业务返回合同

位置：[specs/ui/wp67-b-lifecycle-presentations-and-history.md:139](</Users/dingshinn/Desktop/pokemon-framework-reference/specs/ui/wp67-b-lifecycle-presentations-and-history.md:139>)。

正文末尾宣称“返回true（包装恒真）”。实际包装虽然先给返回容器真值，但进入淡入淡出块后将它覆盖为Screen调用的返回；Screen尾部是场景结束调用，结束调用尾部是视口释放。脚本没有重新写一个表示净化成功的真值。它与孵化演出包装的明确恒真返回不同。

**有限修订**：删除恒真断言，说明返回透传场景收尾结果，不能作净化成功标志。只在参考脚本能证明的范围陈述；底层释放具体返回值未取证时不要改猜恒假、空值或另一固定值。

**最小对照**：
- 静态返回链对照：孵化演出正常返回明确真值；遗迹石包装转交Screen/收尾返回，无独立成功布尔保证。

**来源**：[014_Pokemon/001_Pokemon-related/002_ShadowPokemon_Other.rb:70–74](</Users/dingshinn/Desktop/pokemon-framework-reference/reference/pokemon-essentials/Data/Scripts/014_Pokemon/001_Pokemon-related/002_ShadowPokemon_Other.rb:70>)；[014_Pokemon/001_Pokemon-related/002_ShadowPokemon_Other.rb:123–142](</Users/dingshinn/Desktop/pokemon-framework-reference/reference/pokemon-essentials/Data/Scripts/014_Pokemon/001_Pokemon-related/002_ShadowPokemon_Other.rb:123>)；[016_UI/001_Non-interactive UI/003_UI_EggHatching.rb:202–210](</Users/dingshinn/Desktop/pokemon-framework-reference/reference/pokemon-essentials/Data/Scripts/016_UI/001_Non-interactive UI/003_UI_EggHatching.rb:202>)。

### WP67B-R12 · P2 · TIMEFLUTE无净化提交；香类消息要依实际变化分支

位置：[specs/ui/wp67-b-lifecycle-presentations-and-history.md:140](</Users/dingshinn/Desktop/pokemon-framework-reference/specs/ui/wp67-b-lifecycle-presentations-and-history.md:140>)；[specs/ui/wp67-b-lifecycle-presentations-and-history.md:231](</Users/dingshinn/Desktop/pokemon-framework-reference/specs/ui/wp67-b-lifecycle-presentations-and-history.md:231>)；[review/wp67b-delivery-2026-10-01/entry-coverage-table.md:51](</Users/dingshinn/Desktop/pokemon-framework-reference/review/wp67b-delivery-2026-10-01/entry-coverage-table.md:51>)；[review/wp67b-delivery-2026-10-01/entry-coverage-table.md:52](</Users/dingshinn/Desktop/pokemon-framework-reference/review/wp67b-delivery-2026-10-01/entry-coverage-table.md:52>)。

TIMEFLUTE通过自身门时心量必非0，统一净化却只收心量0，因此立即早退，既不清Shadow，也不出现§6.3所列净化消息；道具处理器仍报成功，可按外层规则消费。这是WP23已批准事实。香类的概括也过度：心量本次不变时只显示友好消息，不进入“心门稍开”或准备检查；有效Shadow已零心量但亲密度未满就是正常反例。

**有限修订**：正文、L21与附表沿用WP23的TIMEFLUTE门错配、无领域写入和成功消费；限定普通使用门通过（非蛋、非Hyper等）。香类补三种实际变化消息：心量未变；心量改变而亲密度未变；两者改变。Hyper恢复仍按处理器先行步骤，不以简化条件掩盖已发生变化。

**最小对照**：
- 非蛋、非Hyper、非Lugia Shadow，心量100，库存1，普通使用门通过：TIMEFLUTE成功消费，心量/Shadow不变，无净化成功消息。
- TIMEFLUTE对零心量/Lugia/非Shadow拒绝不消费。
- 非Hyper Shadow心量0、亲密度低于255，香类使用：友好消息，不请求心门稍开或准备提示；正心量发生下降时另列消息分支。

**来源**：[014_Pokemon/001_Pokemon-related/002_ShadowPokemon_Other.rb:17–23](</Users/dingshinn/Desktop/pokemon-framework-reference/reference/pokemon-essentials/Data/Scripts/014_Pokemon/001_Pokemon-related/002_ShadowPokemon_Other.rb:17>)；[014_Pokemon/001_Pokemon-related/002_ShadowPokemon_Other.rb:226–284](</Users/dingshinn/Desktop/pokemon-framework-reference/reference/pokemon-essentials/Data/Scripts/014_Pokemon/001_Pokemon-related/002_ShadowPokemon_Other.rb:226>)；[013_Items/001_Item_Utilities.rb:661–694](</Users/dingshinn/Desktop/pokemon-framework-reference/reference/pokemon-essentials/Data/Scripts/013_Items/001_Item_Utilities.rb:661>)。

### WP67B-R13 · P2 · 净化室只有中心成员时，SUMMARY不会打开摘要

位置：[specs/ui/wp67-b-lifecycle-presentations-and-history.md:123](</Users/dingshinn/Desktop/pokemon-framework-reference/specs/ui/wp67-b-lifecycle-presentations-and-history.md:123>)；[review/wp67b-delivery-2026-10-01/entry-coverage-table.md:39](</Users/dingshinn/Desktop/pokemon-framework-reference/review/wp67b-delivery-2026-10-01/entry-coverage-table.md:39>)。

详细操作把SUMMARY概括成组内成员摘要，未说明正常可达的例外：中心有心量大于0的Shadow、外圈为0、无持握成员时，中心菜单仍显示SUMMARY，但摘要候选扫描由外圈数量决定，得到空候选后直接返回。因而不会打开摘要。持握成员摘要是独立的单成员分支；不能用它覆盖此例外。

**有限修订**：补无持握时摘要候选及空候选返回、摘要选择返回后游标位置，以及持握成员单独摘要的边界；最小修订不需重做WP66-A摘要叶子。

**最小对照**：
- 中心正心量Shadow、外圈0、未持握：选SUMMARY原地返回，不开摘要、不改状态。
- 给同组加1个外圈成员：候选包含中心与该成员；返回时游标跟随摘要最终成员。

**来源**：[016_UI/023_UI_PurifyChamber.rb:432–454](</Users/dingshinn/Desktop/pokemon-framework-reference/reference/pokemon-essentials/Data/Scripts/016_UI/023_UI_PurifyChamber.rb:432>)；[016_UI/023_UI_PurifyChamber.rb:472–473](</Users/dingshinn/Desktop/pokemon-framework-reference/reference/pokemon-essentials/Data/Scripts/016_UI/023_UI_PurifyChamber.rb:472>)；[016_UI/023_UI_PurifyChamber.rb:1232–1258](</Users/dingshinn/Desktop/pokemon-framework-reference/reference/pokemon-essentials/Data/Scripts/016_UI/023_UI_PurifyChamber.rb:1232>)。

### WP67B-R14 · P2 · 名人堂上限0仍增编号，PC可见后会遇到空记录失败

位置：[specs/ui/wp67-b-lifecycle-presentations-and-history.md:146](</Users/dingshinn/Desktop/pokemon-framework-reference/specs/ui/wp67-b-lifecycle-presentations-and-history.md:146>)；[specs/ui/wp67-b-lifecycle-presentations-and-history.md:154](</Users/dingshinn/Desktop/pokemon-framework-reference/specs/ui/wp67-b-lifecycle-presentations-and-history.md:154>)；[specs/ui/wp67-b-lifecycle-presentations-and-history.md:173](</Users/dingshinn/Desktop/pokemon-framework-reference/specs/ui/wp67-b-lifecycle-presentations-and-history.md:173>)；[specs/ui/wp67-b-lifecycle-presentations-and-history.md:186](</Users/dingshinn/Desktop/pokemon-framework-reference/specs/ui/wp67-b-lifecycle-presentations-and-history.md:186>)。

§9把上限0仅写成“不保存”，§10又把“无记录”等同于编号0、PC不可见，遗漏提示要求核对的有界配置行为。从空记录/编号0开始，上限0时登记先追加克隆记录并增编号，再只删最早一届；内存历史仍空而编号变1。PC门只看编号，因此可见；进入后取不到最新届，成员创建对空值请求记录长度处失败，不能正常浏览或静默隐藏。

**有限修订**：区分历史数组、累计编号与PC门，补上限0从空状态的完整结果和静态失败点；正上限每次超限只删一届，负值不裁剪。保留宿主错误呈现未证、不运行UI、不改参考修复。

**最小对照**：
- 显式配置变体：上限0、原数组空、编号0、非空正常队伍、资源正常，登记后数组空/编号1；PC项可见，进入时在创建成员处失败。
- 默认50的裁剪与编号递增、负上限不裁剪作对照；不把“无记录”统一视为PC不可见。

**来源**：[016_UI/001_Non-interactive UI/006_UI_HallOfFame.rb:67–84](</Users/dingshinn/Desktop/pokemon-framework-reference/reference/pokemon-essentials/Data/Scripts/016_UI/001_Non-interactive UI/006_UI_HallOfFame.rb:67>)；[016_UI/001_Non-interactive UI/006_UI_HallOfFame.rb:120–131](</Users/dingshinn/Desktop/pokemon-framework-reference/reference/pokemon-essentials/Data/Scripts/016_UI/001_Non-interactive UI/006_UI_HallOfFame.rb:120>)；[016_UI/001_Non-interactive UI/006_UI_HallOfFame.rb:178–185](</Users/dingshinn/Desktop/pokemon-framework-reference/reference/pokemon-essentials/Data/Scripts/016_UI/001_Non-interactive UI/006_UI_HallOfFame.rb:178>)；[016_UI/001_Non-interactive UI/006_UI_HallOfFame.rb:452–460](</Users/dingshinn/Desktop/pokemon-framework-reference/reference/pokemon-essentials/Data/Scripts/016_UI/001_Non-interactive UI/006_UI_HallOfFame.rb:452>)。

### WP67B-R15 · P2 · 新规格仍有源码赋值，clean-room自检结论不成立

位置：[specs/ui/wp67-b-lifecycle-presentations-and-history.md:87](</Users/dingshinn/Desktop/pokemon-framework-reference/specs/ui/wp67-b-lifecycle-presentations-and-history.md:87>)；[specs/ui/wp67-b-lifecycle-presentations-and-history.md:160](</Users/dingshinn/Desktop/pokemon-framework-reference/specs/ui/wp67-b-lifecycle-presentations-and-history.md:160>)；[specs/ui/wp67-b-lifecycle-presentations-and-history.md:164](</Users/dingshinn/Desktop/pokemon-framework-reference/specs/ui/wp67-b-lifecycle-presentations-and-history.md:164>)；[review/wp67b-delivery-2026-10-01/checks.json:48](</Users/dingshinn/Desktop/pokemon-framework-reference/review/wp67b-delivery-2026-10-01/checks.json:48>)。

正文在清昵称、创建片尾场景、写完成标记处直接嵌入参考赋值/创建语句，而本包执行提示第4节明确禁止新增规格及附表包含源码赋值。自检却声称没有复制Ruby语句。这里只要求清理本轮新产物，不据此重开上游历史。标识符、数据默认值、必要引用位置可以保留；不要将源码换个语言或逐行伪代码。

**有限修订**：改成独立行为句，如清除昵称、进入片尾显示、标记已播放。复扫正文、场景、附表、回应和自检，修正不真实的合规声明；历史首版材料冻结留审计，不覆盖删改。

**最小对照**：
- 文本核查：新交付不再含这三处赋值/创建语句或实质性条件链；仍保留对应字段语义、提交时点和来源路径。

**依据**：根目录AGENTS.md来源分离规则；已批准交接的WP67-B执行提示§4；本轮被审文本与自检。

### WP67B-C01 · P3 · 覆盖表行数为28，摘要错误登记为24

位置：[review/wp67b-delivery-2026-10-01/delivery-summary.md:9](</Users/dingshinn/Desktop/pokemon-framework-reference/review/wp67b-delivery-2026-10-01/delivery-summary.md:9>)。

实际七组数据行分别为7、4、3、6、4、2、2，共28行；首版摘要与用户交付说明称24行。该计数不影响现有文件哈希核验通过，但影响覆盖报告的可信度；不能把已核对的场景28条拿来代替附表行数核验。

**有限修订**：修订版摘要与自检按最终附表独立统计；入口分拆后数目允许变化。首版旧材料保留原样，在v2回应说明纠正，不重写历史。

**最小对照**：
- 程序化分别核对附表各组数据行总数、案例定义ID唯一性与所有引用；不得仅检查硬编码预期数。

**依据**：本轮覆盖附表逐组计数，见registration-checks.json。

## 3. 修订范围与下一步

由原提取方按[next-task-prompt.md](next-task-prompt.md)只做WP67-B修订v2，并在`review/wp67b-delivery-2026-10-01/revision-v2/`保留冻结稿、修订附表、逐项回应、精确差分、来源核对和最终登记检查。旧首版交付材料不可覆盖。主稿、案例、摘要、附表、自检必须同步，不只在回应中更正。

完成后保持ReviewPending并送复审。16项闭环前不启动WP37、WP53、WP61或整体double review；不集中回填旧批准头部，不做B批整合。此reviewer只写本审查目录，未修改主稿、上游或reference；未创建任务／Agent、未发跨会话消息、未提交／推送。
