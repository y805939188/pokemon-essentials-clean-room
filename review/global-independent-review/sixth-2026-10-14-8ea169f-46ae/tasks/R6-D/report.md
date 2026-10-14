# R6-D PBS／本地化／序列化及资源独立双向复核

**本域有限静态审查完成，提案待global root终裁；不是正式集整体或运行PASS。** 本域104份固定材料：PBS73、Text_english_core18、序列化2、字体8、BMP2、mkxp配置1。规定的结构、作者数据规则、全部核心文本正文与必要消费者阅读已闭合，域内必读缺口为0；原生/完整hostDemo边界保持未知。

## 固定输入及权限

main `8ea169fbd0f33f378b5d732fd6bea59e854e04a6`／workspace tree `6ab3429170d2762607fbc2237014c3a160449fa1`；正式集 `deliverables/final-specification-set` tree `1046fbb657882e84b3dfc6d017943a9edf7782e5`（131文件）；R commit `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`／tree `7589c800b61ba13a13040ed0d686979b80a84fd0`。本轮重新核对身份与材料SHA，`inventory.json`不沿用旧PASS。AGENTS.md297行首先全文读取；用户仅写本tasks目录的约束优先于更新全局Feature Matrix的一般工作流，因此矩阵/同步建议只落本目录，未改全局规格。

仅写`tasks/R6-D/`及其子目录。未切换、提交、push，未启动update，未修改reference、formal、specs、planning、audit、旧报告；未下载、安装、使用外部服务、修改安全配置或真实存档。自写Python只用于惰性数据/字体/BMP审计，非框架实现；未执行未知脚本。旧工具仅在全文理解后独立适配或作解析边界阅读，未继承旧结果。

请求gpt-6.1-sol／ultra／default普速，禁Fast；实际model、effort、tier、speed、UUID均无回显，记**UNVERIFIED**，未检查认证或额度配置。

## 已完成部分与清楚的分母

| 部分 | 本轮覆盖 | 语义范围和限制 |
| --- | --- | --- |
| 专用及较小PBS |29文件；1955分节记录＋2789非分节行；10592分节字段；28278条记录/字段映射 |15类人工规则分别对照schema、必要消费者、formal及相关向量；`special-coverage.json`。不以散文文学质量评价代替作者文本消费；设施姓名/台词全部做分隔/控制形态检查。 |
| 大型及备份PBS |44文件；16732记录；全部字段/值域/382294引用原子 |104实际字段规则＋12省略专属规则、9节头规则已完成作者合同/必要消费接线阅读；全部记录作有前提规则映射。字段定义/必读上下文缺口0；战斗等下游完整算法按领域交接，不将其词法命中当已审算法。 |
| 英文核心文本 |18文件、10697条键/正文；本轮语义未读0 |逐条消费者/规范键/正文/控制候选及placeholder；结构与真实阅读分列。身份译文副本按证明去重，5对非身份值显式读取。 |
| messages_core.dat |31外域、18文本域10697记录与文本逐条相同；事件域76位置 |55实际空桶＋21缺席位置；无未读事件正文。primitive白名单，不用Marshal.load。 |
| Scripts.rxdata |1个Main压缩字符串，解压49行已全读 |归档恰一节支持外部脚本采集数量门；解压不是执行，不证明宿主启动。 |
| 字体 |8文件，104表，2326glyph/度量，24编码记录／16不重复cmap，全部glyf轮廓和边界 |60954简单点、33空glyph；编码→glyph→度量关联完整。原生发现/测宽/字形呈现没有执行。 |
| BMP |2×64像素全部重解析 |8×8、24位BGR，无alpha；knownpoint灰28/白36，selpoint红32/白32。不是浏览器呈现实测。 |
| mkxp.json |159行全部读取，9个活跃顶层属性；33个活跃/注释属性位置映射 |注释值不是宿主有效默认；声明与原生有效消费分离。屏幕512×384与Settings一致，SoundFont指向现有字节，但MIDI/PCM/GPU仍未知。 |

## 正向与反向证据

父级`manual-rule-catalog.json`和`semantic-notes.md`记录人工消费规则及其前提；`source-to-spec-matrix.jsonl`逐记录字段接事实、消费者、formal精确行和根clause ID；`spec-to-source-matrix.json`有334条本域反向行。它们只覆盖本域数据合同部分，不对同文件里无关算法盖章。配置另有`config-forward-matrix.json`／`config-reverse-matrix.json`。全集导航为`forward-matrix-index.json`、`reverse-matrix-index.json`，较大bulk矩阵用JSON压缩收据定位，所有字节长度/SHA均重新验证。

大型PBS全字段矩阵在`pbs-bulk/`；本地化逐10697记录矩阵为`localization/source-to-formal.json`，68行反向矩阵为`localization/formal-to-source.json`；字体/BMP逐表、glyph、像素矩阵及条款联系在`fonts/source-unit-matrix.json`、`fonts/traceability.json`。`data-contract-counter/`已独立全文读WP03/WP04及测试目录788行，对135具名向量全部分类，120个作者数据相关向量作反向核对，其中77新增数据字段向量逐项复核；15个具名配置/启动等范围外向量不转签。该任务还独立重新读取104个schema锚点，明确不把结构重绑定转成全部运行算法批准。

各账本保留全文/区间显示、结构解析、人工语义接受及工具校验的区别。父`reading-ledger.jsonl`不把text_presented直接标成语义通过；组件保留自己的ledger及command-log。`combined-reading-ledger.jsonl`保留6个原账本的852条原记录及来源，不提升原状态。早期超长输出的截断不计语义，必要片段已分段重读。父range工具八次越界请求在断言处停止，随后按真实长度重读；失败尝试记`command-log.jsonl`。

## 已核数据事实及疑似项处理

当前设施总表仅引用十个路径，fancy非_single两文件是可得但未选数据。全部候选编号均在配对池内；fancy-single两条名单重复59/97，真实消费者保留重复并有放回抽取。当前/Gen8设施的STICK与VICEGRIP分别变为空持物和跳过的招式，非普通枚举编译错误；Gen5–7身份目录有这两个旧标识。`cross-profile-special-references.json`对每档核16957非空引用原子；存在性不构成启用/编译/跨世代兼容证明。

五份遭遇表每份19记录、52方式、220槽，所有槽按自己的档案引用完整且级别/权重满足当前数据域；方法权重合计100是这批数据事实，不是新增编译不变量。区域图鉴151/256成员有序且无重复；地图几何与实际事件仍缺材料。两地牢图块集都提供Autotile/Tile整组；字段缺组失败、奇数大网格写回失败、密度0除零等既有条款不能由正常样本推掉。模板EV分配可超过普通单项252上限；既有B17-PA040明确保留255/255、重复条目与正常培养区别。

八项待global root终裁的提案，均已由父级非提出者新阅读反证：

- **R6-D-LZ-001（建议MEDIUM遗漏）**：提取键中backslash+LF与普通运行输入backslash+n错配，当前材料有三个精确锚；最小例为普通物品成功提示。仅在语言译文只存在于提取键、运行键无命中等前提下回原文；不是全部翻译失效。父级独立原始字节核对、先后消费者反证已完成。
- **R6-D-LZ-002（建议LOW能力遗漏）**：指定UI图像身份也经当前语言查找；键图、部分战斗/UI图及两个小游戏basename有必要消费者。缺译回原身份，坏译名不承诺再试原图。父级独立对照已完成。
- **R6-D-FONT-C01（LOW精度可选）**：三档默认字体无宿主命中可返回空名；只搜索显式候选，不自动遍历八字体。现有条款没有明确声称错误行为，所以不是已证矛盾，父级建议可选精度项。
- **R6-D-PBS-C05（父级建议缩窄为LOW省略合同）**：Type/Move部分原始默认及Item“显式单数、省略复数”的独立默认仍缺明确作者数据对照。已有WP73-A115及U07-T01/101已写新建道具的Unnamed/???结果，不能把这部分重计成全新缺陷。
- **R6-D-PBS-C06（建议MEDIUM作者合同遗漏）**：显式部分形态指标记录的缺字段取构造默认，不是基础指标继承；只有整条记录缺席的查询才克隆基础。现有缺整条条款正确，需补部分记录对照。
- **R6-D-PBS-C07（建议MEDIUM矛盾）**：物种PBS Happiness256按非负整数接受，普通个体创建直接复制256；WP30无条件“持久0–255”措辞过宽。编辑器255上限不能移作PBS校验；不指称随附数据已有超界值。
- **R6-D-PBS-C08（LOW范围可选）**：ShadowSize0是编辑器None标签，资源选择本身仍可请求通用0。只在人工有效0资源夹具下比较请求/位图选择；当前缺Graphics，不是已证可见阴影缺陷。已有WP15的Shadow/N分支保留。
- **R6-D-DATA-C01（LOW边界补充）**：特性Flags省略为空列表，显式空属性则可能保留一个缺值元素，后续标志查询失败；省略默认和既有重复首组警告本身正确。可选孵化投影限定先减一步、后查询失败的前缀，不推成全部孵化或真实Demo失败。

四项bulk疑似（SHADOWSHED未实现名、TutorMoves重复、EffectChance101、BerryPlant/Item依赖）均经非提出者新阅读反证：三个已有明确formal条款，一个在已核成员查询中没有额外结果。建议不作为新增缺陷；不外推所有重复或未知内容都无害。完整提案的定位、最小反例、取消/异常/部分写入、负搜索、最小修订及同步/验收依赖保留在组件`findings.json`，父级反证在`counter-review.json`，终裁仍属global root。

## 证据级别与剩余

STATIC_READ／DERIVED_DATA_RELATION／TOOL_VALIDATION分别记账。参考程序或函数执行0，独立游戏行为模型执行0，完整host/Demo执行0；Python数值、字节、字体及记录关系检查不升级成行为测试。原生字体、PCM/MIDI、GPU、实际地图/资源、插件/动态覆写与完整变体兼容保持具名未知。

必须显示的范围外缺读：data-contract-counter接触45文件后，所读必要区间之外仍有34524行，分属22个非全文读取文件；逐文件数在其`source-bindings-and-coverage.json`。这些文件的整文件/全源语义批准继续BLOCKED，不能用本域“必读缺口0”掩盖；其下游战斗、引擎、UI全域分别归原主责。本任务未承接这些整文件义务，也不宣布它们已被其他人审完。字体组件同样保留必要消费者外的文件行数和原生运行BLOCKED。所有记录按原范围原状态保留。

`final-artifact-validation.json`校验168个JSON审查件、6个压缩收据全字节、104个本域参考文件及131正式文件SHA，受保护跟踪差异为空；这只属TOOL_VALIDATION。候选8项与非新缺陷候选4项全部有非提出者反证，共12条，见`counter-review.json`。没有替global root终裁，没有启动update；后续若接受提案，同步责任文件与验收回归均在`findings.json`。
