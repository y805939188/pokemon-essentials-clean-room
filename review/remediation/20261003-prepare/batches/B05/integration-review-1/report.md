# R-B05 实际整合核验：PASS_SCOPED

**PASS_SCOPED**，精确绑定实际被审提交 `cc085d618ce8b5ebda82c28a3a1ac9a09dda9a85`。B05十五正式文件、51历史记录、十个公共改变文件及十个新增整合证据通过本批独立验收；16项B05实际整合贡献通过。新增缺陷 **0**，规范229必修仍 **OPEN**，本reviewer未登记关闭、接受或启动下游。

## 精确输入与完整差异

| 身份 | 固定SHA |
| --- | --- |
| 本轮实际被审integration | `cc085d618ce8b5ebda82c28a3a1ac9a09dda9a85` |
| 实际被审tree | `4363fa50db2042432beaa27894d91e36f4d32877` |
| 已接受B02-C上游 | `9576f00e7d3aeb96f7ca8c42caccfba8f808505e` |
| B02精确被审 / Ultra报告 | `1b1e169faf273e89ad6b7f5e46fd7b60d87d3946` / `361e4e69126559c266a08fdf093082dbbcd83f8d` |
| B05完整候选 / 历史候选报告 | `1914cd379bcb7c8b6feb13dc3e872b7ded27d9a4` / `0da269077aa5a02d5cef08021171acf3719e1b69` |
| B05原起点 / v1 | `0a12de641542f9a59909d2a950c1de8df17ca09d` / `7dc7dd5dfc986788fd6d9ce7b2bdaa6208837b4e` |
| 正常merge | `be9e78e32fd550d5210ab21db0a1868af685f6f5` |
| 公共payload | `b82dde24ae1e0980fe442031e421ea4a709e0981` |

直接Git重建最终对象，接受上游→实际整合 **86路径、8,914,136字节**；B05候选→实际整合 **115路径、11,430,151字节**。全文diff SHA-256分别为 `4f535c5c7d28102546def465c6fe1df2d929e330520f5f5dc98bee3db23f1dca`、`d664b10ec01be648cbefe3c714e4cc0be81674d445f82f8ac534701cf20c6fa2`。包含最终三份证据新增文件；没有仅用payload diff的83/112路径替代。所有路径/旧新blob和全文diff散列见 [完整最终差异清单](complete-diff-manifest.json)。

独立检查merge两父为B02-C上游与B05候选报告，三来源提交父/tree/全部name-status相符；完整66来源路径没有与B02接受链交集。十五正式文件与完整候选、33作者+2授权+16候选复审记录与历史报告逐blob相同。B01/B02既有正式/author/review/接受、PRE0/规划和其他受保护上游路径不回归。

## 逐ID实际整合验收

下列均为 **PASS_SCOPED_B05_ACTUAL_INTEGRATION_CONTRIBUTION**，保持原严重度与原ID。真正证据是实际15文件同一字节、原有效限定/完整源对象/acceptance绑定、公共映射/测试/文件身份的逐项独立核对，以及新公共语义验收；不是仅引用历史候选PASS。每ID的具名前提、反例、测试及剩余内容详见 [整合处置](finding-dispositions.json)和 [独立核对](independent-validation.json)。

| 原ID | 原严重度 | 实际通过的本批范围、关键反例 | 仍待责任 |
| --- | --- | --- | --- |
| GIR-FD82-A020 | P2 | 原/净化25 Nature，20修正/5中性；BULBASAUR中性120/69/69/85/85/65，LONELY防62、BRAVE速58；105修正115/94；ST60–63 | B07/WP28；B01依赖原贡献保留 |
| GIR-FD82-A021 | P3 | 原/净化物种默认；form2继承PokédexForm2、Unnamed/???、unmega/message0、后缀空字符串与空列表不同；CI-25 | 无本批修订待办；父任务接受/最终门 |
| GIR-FD82-A022 | P2 | 基础IV/PID与UNOWN0–27/南瓜族形态抽样分层；withMoves关闭及非零形态不抽；抽0仍可同值提交；缓存/动态读限定；CI-26–28 | 后续生成/遗传按冻结输入；不扩全域随机量词 |
| GIR-FD82-A023 | P2 | 四槽按入口；整表五项、新学只移首一次仍五项、已知移末保PP7/up1、记录/复制保重复；HP-35–37 | 共享整文件锁；不得登记全局四槽 |
| GIR-FD82-A024 | P3 | BULBASAUR L5蛋/教学兼容AMNESIA不自动成为重学候选；首招开关只改候选、不统一改资格；HP-40/41 | B07/WP30一致性贡献 |
| GIR-FD82-A025 | P3 | 两招直接-1/-2删末/首，-3/2不改；调试取消-1在调用者拦；HP-38/39 | 无本批修订待办；最终门 |
| GIR-FD82-A026 | P2 | 六族具名招式/数据门/PP/删除压缩及部分失败；NECROZMA新SUNSTEELSTRIKE PP5/up0、KYUREM缺数据跳过、终战IRONHEAD缺失保原标识；FM36–43及邻近 | B07/WP28完整触发消费者 |
| GIR-FD82-A027 | P2 | ROTOM形态1唯一OVERHEAT裸再写1删为空，无THUNDERSHOCK；CATALOG同值拒绝保原招；FM40/41与PP对照 | 无本批修订待办；保留真实异常 |
| GIR-FD82-A028 | P2 | BANETTITE、48 Mega数据与正确原表；无物/不匹配不触发，METAGROSS异常能力保持；ME26 | 战斗许可/完整退出链、媒体demo限定另保留 |
| GIR-FD82-A029 | P2 | h255/G0工具失败、野外不消费、战斗复检退还；h254可成功至255；G0隐藏Hyper不能绕过；SH47/48/51 | 可选启用/Scent缺旗标/运行未知 |
| GIR-FD82-A030 | P2 | 全131配置；GROWLITHE4000 BLITZ/WAVE、SNORUNT2500 WAVE/SHED；18招/4物品字段与正确原表；SH50 | 可选数据不是默认已启用，实际载入/运行未证 |
| GIR-FD82-A031 | P3 | 存储HARDY2500→2410/H4，LONELY→2370/H3；本次h80不追补、计算覆盖不替代；原W06/SH06/49/52 | 无本批修订待办；最终门 |
| GIR-FD82-A040 | P2 | 设施CATERPIE两项EV255/255总510，能力项floor255/4=63；合法writer局部门保持；ST67与ST56–59 | B07/WP28全称错误、B17/WP76 |
| GIR-FD82-A044 | P2 | TM57实为TR CHARGEBEAM；包内成功追加首招，队伍入口不追加，忘后重学差异；取消/拒绝不记录；HP-42/43 | B07/WP28/WP30、B16/WP66-A |
| GIR-FD82-C124 | P2 | rawIV最高并列按HP/ATK/DEF/SPEED/SPA/SPD轮与PID起点，余5选语义；六31/PID3速度、PID4特攻；最大化不替代原IV；ST64–66 | B16原/净化/UI显示及本地化 |
| GIR-FD82-C126 | P2 | 零招合法：基础MOVES页四空格可显示，USE/事件/遗忘首招详情先失败于BACK，普通零态教TACKLE成功；HP-44/45 | B16原/净化/零招UI及失败测试 |

## 新公共层及证据独立验收

本轮32项主核对全部通过，另直接核三来源提交图和正式/公共读写交集。manifest的144个具名身份与35条current-hashes全匹配；十公共文件各自的新语义及反向对照见 [公共层验收](public-layer-review.md)。原16资格、严重度、owner/contributors、有效case与扩展不收窄；原对象及批准acceptance散列逐ID回算一致，作者建议/测试/原稿与净化路径hash完整保留。

十新增证据文件全部计入；两个完整payload patch逐字节重建一致，最终三个证据后继只新增其自身，无正式或公共payload覆盖。A-REG自检只作为待核材料，本轮未执行其脚本，也未把其121/195作者检查或29登记检查数量充当独立行为通过数。

中央finding-ledger229行原字节保持，全部required/OPEN。approval和trace的旧26行各自完整前缀保持，新增16贡献后各42，finding+candidate唯一，仍OPEN且实际整合待审/下游BLOCKED；42不当规范ID数。两静态目录149/190→164/213，+38，仅FM15/FM20/SH06旧行改动、无删除；PT/PS/AQ/BR全尾段保持，B01/B02目录51/99不变，131最终Markdown/17静态目录数不变。新链接均可解析。

仍存在的WP28“所有EV写入”量词是原A040/B07待办，未在本次引入、未关闭或另开重复ID。原B16/UI、B17/生成器欠项也保留。本轮未建立本批新遗漏、回归或矛盾。

## 有界消费与证据限制

B05的默认/创建、入口容量、Nature/特征/局部EV、六族形态、Mega/Shadow固定数据和部分失败前提已在实际SHA保持，可由父任务串行接受后冻结供B06/B07消费。[依赖建议](dependency-freeze.json) 明确B06须B02+B05接受，B07还须B06；共享目录整文件锁和新输入重冻结仍有效。B03继续既有B02-C冻结，audit/README公共读交集具名保存，未声称其所有输入在本次新SHA都不变。此reviewer没有派发或启动任何下游。

前轮定位勘误原样保留并在公共层引用。本轮以修正后日志及勘误为准，实际回查 `Data/Scripts/019_Utilities/001_Utilities.rb:450–488`；不把冻结首判错写的相邻文件路径当正确。Nature末尾173、Pokemon1227、Move77、Summary1400的有界定位保持。其余固定参考源身份按26个修正后哈希核对，未称本轮全文重读26源文件。十五正式字节和固定参考身份保持，共同规则与数据表继承有界独立证据；源复用说明见 [修正与复用回执](source-reuse-and-corrections.json)。

参考仍在主Git外，固定 `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b` / tree `7589c800b61ba13a13040ed0d686979b80a84fd0`，clean，只读。未执行参考游戏/Ruby/编译/转换/生成/反序列化/模拟/求解；**运行观察0、真实demo链0、行为向量未执行**。U01–U10/G01–G12/AX01–AX20及所有具名未知、可选启用/宿主/素材/插件/事件可达性限制保持。

显式请求 `gpt-6.1-sol / Ultra / Standard(default)`；实际model/effort/speed仍 **UNVERIFIED**，按用户方案A披露，请求值不是实际配置证据。未请求降档、加速、fallback或派生任务。[模型与限制](model-and-limits.json) 另记录一次环境transport断开及正常只读确认恢复，未重登或改权限，当前无环境阻碍。

只新增本 `integration-review-1/`；不改正式/公共登记/历史/main。提交与普通push后由交接提供实际报告SHA及远端核验，报告SHA与上方被审SHA分开，不自引用。完成后停止，等待父任务串行接受登记；本轮报告不自行写CLOSED或替代最终Ultra。
