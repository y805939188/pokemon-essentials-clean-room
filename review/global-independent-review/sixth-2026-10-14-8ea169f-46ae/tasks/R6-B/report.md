# R6-B 独立双向审查报告

本任务的**指定可读程序与根作者工具静态阅读已完成，剩余可审单元0**。这是下列明确分母的静态完工，不是所有原生机器码、任意可打印字符串或真实宿主/Demo的全量验收。两个现行formal提案已有非提出者独立反证，均等待总root终裁；没有启动update。

固定 main `8ea169fbd0f33f378b5d732fd6bea59e854e04a6` / workspace tree `6ab3429170d2762607fbc2237014c3a160449fa1`；formal tree `1046fbb657882e84b3dfc6d017943a9edf7782e5`（131）；R commit `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b` / tree `7589c800b61ba13a13040ed0d686979b80a84fd0`。开始及收尾只读核验一致，R工作区无改动。AGENTS.md全文先读；旧PASS、旧blob或root阅读标签均未代替本轮源阅读。

请求gpt-6.1-sol/ultra/default普速、禁Fast；actual model/effort/tier/speed/UUID均 **UNVERIFIED**。未查认证、额度或配置。所有写入限定本 `tasks/R6-B` 及其子目录；没有git切换/提交/push，没有改formal/specs/planning/audit/旧报告/参考，没有安装下载、外部服务、安全配置修改、真实存档、环境归档释放或update。

## 1. 指定分母与证据等级

| 对象 | 本轮范围与阅读 | 状态 |
| --- | --- | --- |
| 三个RPG兼容明文 | BIN-0079 968行、0080 1004行、0081 1476行，合计3448；连续全文逐字段/默认/能力/谓词/分派/状态及失败边界 | 静态语义已读；344类/方法索引、988访问器字段索引；当前RGSS选择UNKNOWN |
| shader | 55unit、1297行、66函数及3有限prefix；独立子审逐全文核原字节与root当轮数学 | 静态语义已读；GR5-BIN-001仍optional |
| animmaker CIL | 全15方法、743指令、1670代码bytes、11EH；每方法新`--inspect-il`输出并全文新读，60外部MemberRef/19参数/5字段及签名接合 | 定义/分支已读；CLR/XML/Drawing运行UNKNOWN |
| extendtext native | .text有限1740bytes、入口、callback、mutex、四窗/控件循环、17imports及API参数；回调40129c重新对齐解码 | 有限工作体已审；非完整native CFG或Windows成功证明 |
| help候选 | BIN-0708整条SoundFont load帮助；不是RPG兼容脚本 | 字面量语义已读，未证明游戏开放该命令 |
| controller | BIN-0003全1678行、442647bytes，1666完整身份/未裁剪名、790完整有序pattern及12非数据行无损重复压缩语义阅读 | 未抽样；不是每条重复长行单独重显。物理input及native选择UNKNOWN |
| Game/Ruby/zlib接口 | 全区段/16目录、1114imports、3702exports、27309非辅助COFF核心记录、资源/版本/debug及290已选字面量 | 结构/限定字面量；没有把符号名当行为 |
| 根作者Ruby | 两文件各183行/7380bytes；先181行同字节、末182/183方向差异已证明；两份本轮全文读 | 两向守卫/命名/CR/递归/写出/部分失败已审 |
| 根作者HTML/说明 | townmapgen实际414行，animmaker26行，extendtext实际4行，均读尾部 | 交互/输出/依赖/Cancel/资源与失败前缀静态已审 |
| 单节装载器 | 根工具压缩literal与本轮当前Scripts.rxdata字节身份一致；49行安全数据解码后全文 | 未执行loader或Ruby反序列化代码；文件发现/异常分层已审 |
| 纯meta | README42/LICENSE436/gitignore34/rubocop225/wiki.url5全部全文 | 用途/类型已审，不推法律结论、游戏规则或外站内容 |
| WP75消费者 | Compiler_MapsAndEvents全1751、FilenameUpdater全89；编译主入口/文件copy-move/消息、金币、脚本、接收入口和覆盖模块必要单元 | 活动与停用、异常/部分提交接合 |
| formal反向 | WP75全文438/全部291global clause blocks；demo test全文327，CV与相关新作者向量源回查 | 两提案；其它DG/CE/WE/AN/GN/DM为跨域读，不代签其source全量 |

库存/结构、源码语义、人工推导、工具验证分开。原参考程序执行0、独立行为模型执行0、向量执行0、宿主执行0、运行观察0、完整hostDemo与已证Demo链0。静态全量阅读不以存在宿主为前提；缺宿主限制运行主张，不阻止裁定定义事实。

## 2. 三套兼容定义与实际consumer

本轮逐constructor/default/accessor/method阅读全文的语义事实在 [semantic-notes.md](semantic-notes.md)，精确源行/字段在 [compat-unit-forward.json](compat-unit-forward.json) 和 [compat-field-index.json](compat-field-index.json)。索引工具只定位单元；静态事实来自连续阅读与手写分析，不能用其遍历输出当语义PASS。

三套同名RPG数据不能叠成同一活动系统：一套带四层地图与feature/damage/effect，另一套三层旧数据库，XP套还含Cache/Sprite/Weather。构造默认不保证反序列化旧对象具备同默认；构造/访问/实际数据库值分开。Map的battleback命名差异、Troop未在对应块定义的BattleEventPage、Damage公式捕获范围、UsableItem scope集合差异、BGM/BGS clone与共享last/pos差异都记录为**给定选择下的定义边界**，没有推为当前游戏一定失败。

实际散文件会覆盖XP旧Cache load_bitmap/tile、RPG::Sprite动画/update/位置/effect及Weather活动逻辑。新Weather为symbol/60粒子/time delta，不能让嵌入旧40粒子替代当前合同；资源包装还有引用计数，不能据旧Cache直接对象复用补当前所有生命周期。Audio_Play有Game_System→存在且支持play的RPG子类→Audio fallback的条件链；其存在不证明当前rgss加载哪一套。Game.ini不可得，mkxp.json未设rgssVersion，native selector没有本轮证明。

活动可定位的Map/MapInfo/Event/Page/MoveRoute/Command/Tileset/System/Audio/Animation字段分别接Compiler、Interpreter、散文件音频/动画/资源consumer；其余旧数据库字段以独立可选兼容policy处置，保留native/dynamic消费者未知。没有把全部旧Actor/Skill/Enemy数据库战斗、源类继承或具体API强制给未来框架。

## 3. animmaker与extendtext的新静态事实

[animmaker-method-forward.json](animmaker-method-forward.json)逐15方法绑定token/原文件offset/代码hash/完整IL日志。完整表宽960、五个192格，空集合高192、非空高为192×ceil(n/5)；每图样在其编号格中心两倍放大。不存在图片只打印并跳过绘制，仍保留格编号；Rect.IsEmpty才取整图。x缺失/空串时其它坐标属性不读，x存在则四个属性均解析；所谓positive只拒负而允许0，代码没有96×96钳制。缓存以精确文件名/weak target复用，非alpha图用左上像素作透明色。

全部XML聚合正常返回后才逐animation创建/绘制/Save；前张成功、后张失败没有全局撤回。解析IO救援可返回已聚合前缀，XML错误分支的格式串有{2}却只传两个替换参数，不能补稳定提示/成功返回。Dispose/Close的finally只证明请求发生的控制位置，不保证外部库成功。无参help会等ENTER；没有独立作者取消事务。数值5的InterpolationMode、数值2的GraphicsUnit、Save(string)及DrawImage的确切签名都记录，实际插值/编码/图像结果未执行。

[extendtext-forward.json](extendtext-forward.json)逐有限入口/工作体定位。工具以固定mutex名限制重复启动，但创建失败返回−1而主函数只拒0，不能保证成功持锁。宿主检测是枚举窗口，class包含Afx:且title包含RPG Maker XP；循环分别找Script/Show Text/Comment/Batch Text Entry的#32770窗口和EDIT子控件，请求指定尺寸、批量窗按钮位置，每轮请求Sleep150ms，再重新检查宿主窗口；不是精确150ms周期保证。SetWindowPos及多处读窗返回没有检查成功，实际窗口/控件效果、语言与版本适配未证。

WP74§18和WP75§14本来限定文档证据。上述定义可接**可选新静态附录**，不能仅因新增阅读升级为既有formal行为矛盾或要求未来复刻CLI/.NET/Win32工具。原生能力与实测效果分开。

## 4. 作者工具与K主合同

[script-identity.json](script-identity.json)证明两个根脚本只在182/183改变入口启用。两份有效全文独立新读后关联共同定义，提取<10拒、合并>10拒、10两边允许；提取先清全部旧树、逐节输出、备份、换loader；合并本层rb字母序先于子目录递归，直接覆盖、不备份、ID重随机。9实体/非ASCII按字节重释/空节丢失/CR删除/目录两层计数与合并无深度上限均按源事实，不补往返等价或重跑安全。

loader原归档哈希、literal与解码文本绑定在 [loader-identity.json](loader-identity.json)。49行的新阅读支持WP75§12.4：文件打开/读在局部求值保护外，ScriptError和普通错误分支不同，899/900实际消息长度门、日志写失败前缀与先前加载定义保留。安全数据解码不是执行loader，不保证实际Ruby消息对象改写或启动结果。

townmapgen全文包括所有helpers/事件。文本格尺寸不校验，载入先清数组、逐行修改、badline提示后仍访问失败匹配并中断，已载前缀保留。生成只有textarea/CRLF、原始值未加引号，用户手工复制/加节标题；不是保存文件。Cancel/Refresh/Load清选择但未一致disable Save按钮；无选择时Save业务分支不进。当前“点选才启用”可表示首次启用门，故暂不把这一按钮边界提为formal缺陷。两个标记BMP可得、地区底图/Graphics缺失及浏览器结果仍按root/D原范围。

根工具局部文件异常与Compiler主生命周期/诊断主合同接合：事件转换已有文件前缀不回滚，主编译可后清数据/打印/转一般错误；不能从统一诊断面补每局部错误的坐标、成功日志或原子恢复。File.move实际复制后删除、目标先删除再重建，文件与引用两阶段保留。不使用旧报告当本轮源证据。

## 5. 独立提案与非提出者反证

[findings.json](findings.json)仅两项现行formal提案，精确source/spec/前提/普通对照/最小反例/失败前缀/负搜/必要consumer/影响/最小修订/保留scope/同步/验收/依赖均齐。

| 提案 | 本轮源证据 | 独立反证结果 | 总root |
| --- | --- | --- | --- |
| R6-B-001（low） | 缺图块集对象的表访问失败诊断只带tilesetID/mapID；坐标/一基层号属于随后无效tile的另一分支。WP75 289/392将两者合并 | 非提出者支持字段不准确；收窄到实际抛错并进入局部救援，正常返回nil的表不一概承诺同异常 | PENDING |
| R6-B-002（medium提案） | 免费容量门→售货生成提示→接收；收费金额/容量门→扣款→售货生成提示→接收。收费提示时可已money800而qty0 | 非提出者支持**生产者顺序缺失**；＋可只是集合，不裁为字面明确反序。WP27接收内提示先于add已有，不能套WP29完整商店流程消除本外层顺序 | PENDING |

独立反证在 [shader-counter/counter-B-findings.json](shader-counter/counter-B-findings.json)，绑定未改写候选hash；收窄接纳与证据注意点在 [counter-review-adoption.json](counter-review-adoption.json)。没有由提出者终分类，没有自动mandatory、修formal或启动update。售货无额外取消事务，消息BACK/确认不等于退款；失败例只裁已发生前缀，不补实际窗口/完整Demo。

root shader当轮55条由非提出者逐新源反证，未发现数学或optional/selection边界需要纠正。灰度/色调/覆盖/flash/pattern/反相/灌木次序、合成零alpha、帧表除法在区域门之前、纵门读已偏移横坐标、YUV与alpha变体、核权重归一都保留。二进制偏移不证明prefix拼接先后或实际选择。既有GR5-BIN-001保持optional，不新增canonical/mandatory。

## 6. 双向矩阵、限制与未读口径

[forward-matrix.json](forward-matrix.json)入口汇集109本任务行、344兼容类/方法与988字段、15方法、8native单元，链接55shader及完整controller/PE34219行子矩阵。[reverse-matrix.json](reverse-matrix.json)绑定WP75全部291global clause identity/精确行、demo整篇阅读与CV/new作者源回查；总578条不把跨域阅读标成全源认证。全部矩阵是审计文档，没有复制参考表达式到正式规格或翻译生产实现。

[reading-ledger.jsonl](reading-ledger.jsonl)及子审ledger保存全文区间、hash、模式和语义依据；`logs/`保存本轮真实呈现/CIL/objdump/搜索/安全数据文本。最初两次大输出发生中间截断的WP75/test区间已用小连续区间补读；townmapgen/extendtext按实际splitlines尾部补读，不能凭原newline计数跳过尾行。范围越界及有限Marshal首版不识别I包装的工具失败没有算通过，修正后原byte身份验证成功。

**inventory_only不能计语义通过。** 752可打印候选中692其它项仍按glyph、字典样碎片、诊断/帮助/协议pattern、偶然字节等处置；三大PE另有259625未选字符串未逐条解释。有限源码55shader/3compat/controller/help/CIL/native工作体分母并未藏在这项库存限制内。BIN-0466/0481孤立txt与登记原跨度不符、不属于extracted_path，未签为该ID证据；prefix直接读原字节。COFF静态函数的aux布局视图只作工具标注注意，不推section语义。

[limits.json](limits.json)保留精确L04：Game native `.text` [1024,9738752)、Ruby [1536,4072960)、zlib [1024,82432)完整CFG/dataflow未恢复；原生绑定/后端选择、GPU输入/精度/采样/实际像素、外部XML/Drawing/CLR/Windows成功、物理controller、真实媒体、存档/地图事件和完整hostDemo均UNKNOWN。五份纯meta不变成游戏或法律要求。没有可得指定程序文本缺读；若总root扩大为所有字典/诊断字符串逐字语义或完整native，本状态不能代签该扩大分母，必须另显示实际未读/阻塞。

本任务可交总root：静态阅读与双向审查完工；两个有独立反证的提案等其裁决，所有运行、native和inventory限制保留。
