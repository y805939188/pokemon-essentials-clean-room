# Item schema companion 有限资格复核

结论：`FINITE_SCHEMA_QUALIFICATION_RECEIVABLE_WITH_EXPLICIT_MEANING`。完整读取指定 2,807-byte companion；其纠正 `Pocket=v`、价格类 `u`、两类 use 为各自内联枚举的部分与固定 R 定义及活跃通用 parser 一致。原件保留；接收时必须采用下述有效义，不能把 companion 的 `original_complete_group.meaning` 整句重新当作正确的最终断言。新增 formal finding 0，新增 required 0、optional 0；不签全部 Item、全部 PBS、原 producer 整包或全局通过。`UPDATE_NOT_STARTED`。

## 固定身份与读者资格

B8 为 `fd1df570cad987dc3852a3b958f03916e317f7fe`，workspace tree `751dfde81048c81390f89a65ca1d1a565ba8e1ca`，formal tree `f292698cdd4a8e725525a9be6dc34b75faaf151e`。R 为 `/workspace/pokemon-essentials` 的 `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b` / tree `7589c800b61ba13a13040ed0d686979b80a84fd0`；本次只读身份核验一致。具体载荷的 bytes、SHA256、Git blob、行/结构范围和机械固定字节核对见 `read-identity-ledger.json`。

原贡献固定提交为 `70dee4e34d08cf32cfaee41d1fa21cd4e4b8d446`；本机未解析该 Git 对象，但 root 已接收的准确恢复目录可读，本次不把这一点扩成材料阻塞。完整实读其 `review.md`、`progress.json`、`reading-ledger.json`、`interfaces.json`、`evidence/peer-reception.json`。原 producer 是该外部任务的 `/root` 上下文；其主责为 ItemEffects 1–1948、WP50 两正文及两共享 catalog。原记录明确要求 root 独立接收，WP50:179/181 旧资格待另接；这些资格不由本次升级。

原 producer 的 `evidence/read-operations.ndjson` 第8条记录亲读 Item 1–270，第11条记录 CompilePBS 1–85、235–266，第12条记录 Compiler 967–1040，第13/15条记录 GameData 有限定义范围。本次只完整读取这些五条与 schema 有关的读操作对象，不接管其余读操作。其 `identities.json` 只读取 fixed 及四份必要源文件的身份对象；其 `evidence/data-reception.json` 只读取顶层资格、六路径身份/缺席/激活前提及 mandatory companion 对象，未显示、未审读其中 record 数组。

原 producer 的 I-DATA 明确保留 `/root/creature_b`、`/root/pbs_battle` 整记录职责；companion 自报实际源读者 `/root/pbs_creature_current_cloud`，声明 Item 全270行及随后精确 schema 补读。本次没有以这些自报代替当前语义核验，而是另亲读当前 Item 全270行和必要 parser/编译/登记定义。此亲读只承担本报告的有限字段资格。

请求配置为 `gpt-6.1-sol / ultra / default普速 / Fast off`。实际 model、effort、tier、speed、Fast 和平台 task ID 均 `UNVERIFIED`；实际逻辑入口 `/root/item_catalog_schema_final_reception/schema_companion_qualification`。

## 可接收的字段语义

下表限定合法 Item 身份、合法作者词汇和所需注册表已具备的 PBS 输入；“缺省”指属性省略、没有参与该字段转换。它不把直接构造记录与 PBS 文本混同。原始值与本地化结果也分开。

| 字段 / 类型 | 精确输入域或含义 | 省略后的记录值 / 必要消费者前提 |
| --- | --- | --- |
| SectionName / m | 非数字开头的字母、数字、下划线名称，成为 Item 身份 | 该身份来自节名，非另造缺省身份；重复身份在登记前报错 |
| Name、NamePlural / s | 两个独立文本字段 | 各自原名 `Unnamed`；复数不由单数生成；分别进入各自语言域 |
| PortionName、PortionNamePlural / s | 两个独立份名文本字段 | 原字段缺值；各 getter 分别回退普通单数名/复数名。已存空串不等于缺席 |
| Pocket / v | 十进制数字串，转换后必须大于0 | 1；PBS 的0、负值、空值拒绝；无此 parser 上限不等于任何正值都有可用口袋 |
| Price / u | 十进制非负整数，0合法 | 0 |
| SellPrice / u | 十进制非负整数，0合法 | 购买价整数半价，即 floor(Price/2) |
| BPPrice / u | 十进制非负整数，0合法 | 1 |
| FieldUse / e | 精确别名 OnPokemon→1、Direct→2、TM→3、HM→4、TR→5 | 0表示无野外使用；PBS显式数字文本0或1–5不因此合法，别名不折叠大小写 |
| BattleUse / e | 精确别名 OnPokemon→1、OnMove→2、OnBattler→3、OnFoe→4、Direct→5 | 0表示无战斗使用；同样区分合法别名、缺省0与非法数字文本 |
| Flags / *s | CSV文本列表；查询标记时不区分大小写 | 空列表；显式空属性与省略不同，不能一律称为空列表 |
| Consumable / b | 真接受1/true/yes/y，假接受0/false/no/n；字母大小写不限，空/off等拒绝 | 原字段缺值时按重要性取反。重要=KeyItem或TM或HM；TR本身不重要。有效消耗要求非重要且存储值为真 |
| ShowQuantity / b | 与 Consumable 相同的布尔输入词汇；存储真假均保留 | 未给定；数量资格为“显式真，或非重要物品”。普通物品省略/false/true均真；重要物品依次false/false/true。与Consumable独立 |
| Move / e引用Move | 需要已登记的招式身份；不是两类use的内联表 | 缺值；若后继把它当机器招式消费，仍需相应身份及合法引用 |
| Description / q | 取预处理、属性分离后的整段值，不重新拼回井号后缀/已去端空白 | 原字段缺省 `???`；显式空 q 为已存空串 |
| pbs_file_suffix / 编译来源 | 非 Item schema 作者属性；来自选定输入文件相对 items 基名的后缀 | 直接构造未给定时为空文本；编译器提供真实来源后缀 |

`s` 字段显式空属性经分词没有首值，得到缺值；名称各用自身默认，份名各按自身回退。`q` 则取已预处理的属性原值，因此显式空描述保留空串。`Flags=` 经列表转换并不等于省略 Flags，不能仅凭缺省表推断其后继查询安全。这里不重新批准全部文本/翻译或全部标记消费者。

有效 use 数字是初始化后供消费者分类的内部值；字面别名校验发生在此前。直接构造记录不经过 PBS 类型校验，直接数字0在这些字段中不会自动变成非法文本；这不证明该记录可正常入袋、使用或展示。使用家族/旗标的存在也不证明已安装处理器、已获得物品或实际扣物。

## 通用 parser 与编译前提

本次亲读活跃定义：Compiler 的行预处理和 section reader、CSV 分词、`cast_csv_value`、`checkEnumField`、`get_csv_record`；旧 `pbGetCsvRecord` 标为未用/弃用，不拿它的旧分支解释当前 Item 编译。字段省略时通用编译器跳过该转换；出现而空的必需数字、布尔、内联枚举分别会拒绝。整数 `u` 允许0，`v`另拒0；内联Hash按精确文本键查找。类型字母大写的可空语义与这里 Item 的小写字段不能混用。

编译 Item 清空当前表，按选定路径和完整 section 顺序解析，先转换、再校验回调和重复身份检查、再登记；单条 Item 校验回调为空，没有额外把非法数字use变合法的步骤。末尾汇集五个名称/描述语言域，再保存数据。注册构造才应用各字段默认；类型接受、构造默认、后继可用性是三个不同前提。中途错误不保证清空前状态或已登记前缀回滚；本次未作任何编译/游戏执行。

默认输入发现只枚举 PBS 顶层 `*.txt`，按基础名及下划线后缀匹配；备份子目录不会递归加入。可选四条 Shadow 数据的原记录有效性和 scent/TimeFlute 实际使用路径仍保留原实际读者及 root 接收，本次没有重读这四条或全部PBS，也不以 schema 正确证明其已激活。

## 必须附带的证据措辞限定

companion 的 `correction` 正确修正了原组“Pocket/Price/FieldUse/BattleUse unsigned”一概而论的说法；原 producer 的 `mandatory_schema_companion.meaning` 已明确不采用旧 unsigned 概括。

companion 的 `original_complete_group.meaning` 还保存了“ShowQuantity stored nil and predicate derives consumable unless explicit”。这只能作为原话的历史记录：缺省存储为nil的部分正确，谓词不依赖 Consumable，显式false也不覆盖普通物品的显示资格。本次有效义由上表及 Item 189–201限定。静态对照：普通物品 Consumable=false、ShowQuantity省略或false，数量资格均真；重要物品 Consumable=true而ShowQuantity省略，数量资格仍假；重要物品 ShowQuantity=true才通过该资格。它们是手工分支推导，均 `NOT_EXECUTED`。

当前 B8 WP27 §2.1–2.2（45–71行）已正确区分二者并给出三态表；WP03 §5.1–5.1.1（138–173行）已正确区分v/u及use别名。因此本项仅限定原证据的可接收意义，保留原 companion 与本报告的纠正链；不构成新的正式缺陷，也不要求修改 formal。名称、数量资格到真实UI图标遮挡/像素，以及使用资格到实际扣物仍由各原消费者合同承担。

## 实际读取、未读与交付边界

有限必需读集未读0，有限 schema 前提未接0。完整指定companion、根AGENTS、本轮prompt/skill、两份root裁决均已读；首个合并输出发生截断，prompt已由1–150、151–241完整补读，不对截断部分单独授信。完整/有限范围与仅机械解析范围逐载荷分列于台账。

原 producer 的868 raw / 862 selected记录、四条 Shadow原始记录、其语义atoms、全部PBS、全部 ItemEffects、全部formal，以及其余外域源码/消费者，本上下文均未重审、未接管。这些不是本次有限必需读集的缺读，也不被改报成已读或宿主limit。WP50旧资格仍由root/history另接；本报告不能关闭它。

指定plain SHA与文件名完全吻合。companion及producer记录所指 `evidence/compressed/708d62e93db2e05400d442be3da03219250e7ec6f2bac11fa0b0ce5108cfe3a7.gz` 在当前工作树缺席；plain完整可读已足以完成本次语义接收，缺席仅记录为传输入口状态，不声称已核gzip恢复身份。

游戏、Ruby、独立行为模型、宿主、保存/重载均未执行；新增业务执行0。只进行文本/JSON解析、Git固定字节及hash核验；无git index、commit、push，无source/formal修改，无其它写集改动。独立写集只含本 `schema-subreview/`。本报告交root作有限证据接收，原贡献的整体接收与全局收口仍由root处理。
