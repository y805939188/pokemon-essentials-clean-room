# B14 candidate2：R-B02 独立受影响复核

**PASS_SCOPED**，仅覆盖 B14 对已接受 B02 的受影响接口。无本范围新增缺陷、无阻断项；不重批准 WP59–61 全部业务、不代替 R-B14 或其他所有者 gate，不关闭全局 finding。

被审 candidate2：`af39efbf32549be964cb083bd49bed6d1d5c0d2a`，分支 `remediation/20261003-prepare/batch-B14`，已核远端精确引用。接受前驱 B09-C：`1e6b11a47370f1c7c4659a32443fc1afda597bac`；candidate1：`47f7514765f8569ae9172bb06a2cd615e2b83b8a`。本报告是另一提交，发布后报告 SHA 由外部回执给出，不能当作被审 SHA。只新增本目录，review 分支 `remediation/20261003-prepare/review-B14-affected-B02-1`；未改 main、正式规格、公共登记或历史报告。

## 1. 身份、范围与独立性

读取当前 AGENTS.md；检索未发现适用的本地 .agents/skills/SKILL.md。按 B09-C 的 B14-downstream-contract、两个 whole-catalog 锁及 B02 reverse-impact package 重冻结。72个规划输入的 blob/SHA256/bytes 均按明示身份匹配：70个当前前驱输入、2个固定历史输入。6个原规划写入基线身份也吻合；这些是身份核验，不能称为72份材料全部行为已重审。

完整接受前驱→candidate2 有46路径：12正式修改、34新增 B14准备/作者材料；candidate1→candidate2 有22路径：8正式修改、14新增作者材料。两份**未过滤完整差异**与前后身份见 [diff-manifest.json](diff-manifest.json)、[full-predecessor-candidate2.patch.gz](full-predecessor-candidate2.patch.gz)、[full-candidate1-candidate2.patch.gz](full-candidate1-candidate2.patch.gz)。本判断涵盖累积共享目录变化，未只审 v2 增量。

正式12路径为原/最终 WP16、WP59、钓鱼WP60、树果WP60、WP61以及两共享测试目录。原4份同步补丁的范围批准冻结于 `b37533ef1cfc7808ed41d64215647a78d165ada4`；candidate2 额外原/最终 WP16仅一条水花句及树果§5.2/BP18补訂，符合父任务明示有界授权。范围批准不等于正确性验收，作者局部 traceability 不等于公共 A-REG 登记。

先读正式差异、完整 C003 当前限定/4根裁决/8扩展、B02全部12对象及 acceptance 和固定参考分支，形成 [independent-first-judgment.md](independent-first-judgment.md)，随后读 candidate2 fix-response、revised-identities、application、validation和补丁。作者自检不作为通过依据。作者对应6个既有他审材料的精确身份、12份文档的前驱/candidate1/after身份、5份有界 intended/applied身份及6补丁逆向只检查均经独立核对；结果见 [author-comparison.json](author-comparison.json)。未运行作者或历史验证程序。

参考仅在主 Git 外的 `/tmp/r-b14-b02-reference` 静态读取；origin为 Maruno17/pokemon-essentials，HEAD `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`、tree `7589c800b61ba13a13040ed0d686979b80a84fd0`，detached/clean已核。未把参考目录或源码带入主 Git。精确源文件身份、实际阅读区间及结论限度见 [source-reading.json](source-reading.json)。

请求配置为 **gpt-6.1-sol / Ultra / inherited Standard(default)**。按用户方案A，明确参数和平台接受任务可作为执行依据；实际模型/推理档/速度生效未独立核验，记 **UNVERIFIED**。配置/额度探测0、子任务0；没有降级或加速操作。

## 2. 独立证据与相邻反向对照

### 时间表与 B02 缓存接口

参考 `003_Overworld_Time.rb:12–41,82–124` 同时核24整点四通道、System.uptime≥30门、宿主分钟插值、关闭配置返回既有缓存及非地图应用早退。candidate2 WP59§3.5/WT03/WT37和现有 WP16§4.4不把宿主时间变化当作缓存必更新，不用06:30相同端点证明插值。04:30给不同端点的四通道对照；23:30下一小时mod24但端点相同，单一数值不能证明回绕。

B02 WP06§3.2/TM14仍要求上次运行戳100、读取戳129.999/130各例独立：前者旧缓存/旧戳，后者重算18:30并写130；关闭开关仍旧缓存且不更新时间。它们原/最终以及测试文件字节未改。新增24表和 WT 场景补足领域数据，不扩大 B02 的户外呈现、宿主像素或实际时间保证。

连接天气的新增 WT07/09 与原/最终 WP59§4.3保留局部0及连接调用者随后20的区分。参考 `Overworld.rb:241–252`、`Game_MapFactory.rb:91–113,136–151`、`Spriteset_Global.rb:27–41`核先进入通知后20、后续显示消费；20不是20秒。B02不因此批准整条天气/战斗环境链。

### FLY 正常返回、异常切点与地点窗

参考 `004_Overworld_FieldMoves.rb:471–512`：count+1、落位朝下、地图自动BGM、refresh先于可选回调，.25等待随后；演出正常退出才清E，再把D设nil，最后true。`002_MessageConfig.rb:559–591` 的 ensure正常清理表现资源，没有清E/D或吞异常。`002_Overworld_Overlays.rb:8–44` 的D守卫先于延迟计时重置、窗口更新和消息/换图处置。

candidate2 原/最终 WP59§5.3/5.4/5.7/7、WT28/39/40明确合法D=(M,7,5)、可用个体、非空E、count=N、正常前缀及无其他领域写入。无状态写的回调抛普通异常、演出清理正常时：已提交N+1/位置/BGM/refresh；未请求.25等待，未清E/D，未正常返回true，异常传播。相邻只改无回调或无写正常回调且后续均正常的对照，依序等待/演出清理/清E/清D/true。既有“无可用个体内部正常false、外层忽略而true”仍保留，未把异常伪造成布尔返回。

地点窗结论仅在**另有合法、尚未处置的更新机会**时成立；保留D阻挡，清D后曾延迟者才重设计时并检查后续门。未推出未处理异常后游戏继续。普通命名调用 `PauseMenu.rb:206–235`、FieldMoves511没有传入该回调；直接工具能力与真实菜单/plugin/事件可达分开。WP16§5.5、WT36字节未改，门次序保持。此处支持 B03既有问题的局部修订一致性，不代签 B03复审。

### 水花重置与普通更新

参考 `001_Overworld_Weather.rb:210–225,239–312`：默认雨类别奇数索引选末张水花；活动水花重置选离散.30… .49寿命并置255；update到期调用reset后立即return，普通非重置更新才按剩寿命<.2置255，否则0，且不套雨滴漂移。

原/最终 WP16单句现在与正确 WP59§4.1/WT31相容：合法稳定默认雨类、可见index1且资源/后续正常时，重置寿命.40得255；随后普通.30得0/.19得255。反向index0为雨滴；非活动/不可见/无bitmap、改配置、在途渐变或缺资源不由这个夹具保证。WT31以及正确天气/资源/淡入条款字节保持，WP16其余全部字节保持。此处只审新单句的受影响接口，不重批准 B04整域，也不观察屏幕像素。

### 树果公共时间戳、覆盖物与 A010

参考 `006_Overworld_BerryPlants.rb:97–159`：未种植或取整时间差≤0返回；覆盖物在机制分支前修正参数；重植上限reset/return另列；正常写time_alive→growth_stage（重植另+1）→time_last_updated，再进入新干涸或旧浇水。原/最终§5.2和BP18现在保留此序。旧对象已存GROWTHMULCH、基础3h、首生命周期9h的显式结算给8100秒、time_alive32400、阶段5、戳T，随后处理旧标志/有效Rain水。无覆盖物同9h阶段4；未种植或≤0无公共写；普通旧显示链仍不结算（源272–289）；不推出旧UI施肥、实际事件或故障默认可达。GR-012/BP07舍入、BP13容量失败、重植/清零及两机制区分保留。

A010直接接口另核源437–470与当前 WP60§6.4：确认、容量预检先于 picked+1、单株本次qty≥该果最大产量判定、入包、消息、自开关A及true；外层植物reset与工具分开（源308–329）。WP06统计目录/TM09仍是从2独立给8/10/12果得到2/3/3，十株各10果得到12；12仅直接输入，不声称普通栽培可达。BP14终态列表不是次序列表且字节未改；新增BP18时长不是统计的果实量单位，没有反向破坏已接受A010。

### 步进计数与共同 C003 条件

参考 `001_Overworld.rb:172–185` 回绕先于玩家周期/handled/菜单或事件遭遇门；强制/解释器分支一般通知后早退不加全局计数。角色实际完成移动的通知（Character981–985）先于玩家步后入口（Player543–552），新增实际移动两通知条件要求正常地图、无自动冰瀑布/中断转移、强制路线后续等待仍有效或解释器仍运行。B02 TM12的直接步后入口一次、普通上界2147483647→0及无订阅者再次改写前提保持；不把两次通知变成两次全局加计。

共同C003变更行也核最小条件：FS16有效开始公共事件正常返回时绕过内置开始整体，缺/负ID反向回退（Fishing4–28、Utilities524–539）；鱼竿 count/battle请求层次分开（ItemEffects276–315）；输入先于严格>截止门（Fishing87–110）。FP06补 handled=false、毒伤配置及4步门（Overworld83–112）；FP12/14/35仍先原队伍感染门（含蛋），内层仅非蛋且感染期减期限，已治愈/未感染不减、空扣集合也更新时间（Overworld5–16、Pokemon824–827）。这些与B02缓存子贡献没有矛盾；PT/LC/TP/CE/AN/CV等外部扩展不在此签全局通过。

## 3. 共享目录与既有上游保护

独立整段字节比较覆盖所有非WT/FS/BP/FP章节，不靠条数相等证明语义：engine目录339→357，pokemon目录141→148，合计480→505；全部480旧ID顺序及重数保留。累积旧行变化为 WT03/07/09/14/15/17/18/20/23/25、FS02/03/06及FP01/02/06/12/14/15；新增WT26–40、FS16–18、BP18–20、FP32–35。其他所有者行连同段内文字/表头字节保留。

candidate1→candidate2为503→505，仅WT28、BP18旧行变更，新增WT39/40；正确WT31/32/36、其他行保持。B02全部13正式路径字节未改；B01 EP01–21逐行及其共享generic目录完整文件保持。新WP16只有原/最终各一行变化，树果原/最终除§5.2均保持candidate1字节。全累积正式差异的 `git diff --check` 通过；补丁容器空上下文单空格是合法统一diff内容，不将它冒充正式文本错误。

首次计数脚本漏计28个有连字符B04-R ID，先行记录保留原计数并明确补记纠正；最后审计接收完整ID再复核，采用本节480/503/505。外所有者整段字节比较从首次即通过。纠正源于独立文本检查，未以作者自检替代复核。

## 4. 原 B02 逐 ID 当前结论及剩余责任

原完整对象与有效 acceptance 哈希均核固定 `93e10ba…`/`41fffb5…`，完整12对象保存在 [complete-controls.json.gz](complete-controls.json.gz)；current_qualifications/有效二审/扩展优先于旧措辞。表中 NOT_AFFECTED 只针对本候选的改动接口；依据是身份/实际句子/调用者/条件，非自动沿用旧PASS。

| 原ID／保留severity | 当前受影响结论及证据 | 当前剩余责任 |
| --- | --- | --- |
| A006／P2 | NOT_AFFECTED。WP02设置/原最终WP08/相关测试均未改；新增世界时钟、FLY及树果接口不写玩家语言/消息集。作者导出目标与玩家切换区别保持。 | B01/B02已接受局部贡献不等于全局关闭；外部/plugin入口缺失未证。 |
| A010／P2 | PASS_SCOPED_INTERFACE。源437–470、WP60§6.4/BP14与WP06/TM09核单株果实量、成功每株一次及确认/容量先行；BP18时间单位另列。 | 12果直接输入不证明正常产量可达；真实事件/素材与最终全局gate保留。 |
| A011／P2 | NOT_AFFECTED。交换入口计数/先加后验证条款与TM13、原WP06目录未改；本候选没有新增交换调用。 | 7→8失败前缀/未完成交换保持；不补实际演出保证。 |
| A012／P2 | NOT_AFFECTED。原/最终WP07、IO13–15和LZ12未改；本候选无目录删除/翻译覆写调用。 | 根目录删除、部分失败不回滚与导出保目录区别保持；宿主/链接/并发限度保留。 |
| A013／P2 | NOT_AFFECTED。原/最终WP08及LZ17/07未改；新Weather字段字面不是该翻译节名解析入口。 | 非零整数前缀、常量、Map形状及输出截断次序仍分开；GR002不扩围。 |
| A014／P2 | NOT_AFFECTED。保存/损坏门与SV04–06/MG12未改；合法地图转移是新增夹具前提，不替代读取损坏门。 | 缺集合≠存在空集合；前置读取成功/到达该门与真实图显示保持未证。 |
| A015／P2 | NOT_AFFECTED_B02_PARTIAL。三个跳菜单控制、空已读数据新游戏/非空继续的正文/场景未改。 | B16保存启动整域及最终多贡献gate待续；文件存在不代替已读数据非空。 |
| A016／P2 | NOT_AFFECTED。原/最终WP10与MG13–16未改；世界宿主日历/单调缓存新增没有更改迁移的执行FPS输入。 | 浮点N/F、missing/nil/false→0、已有stats键含nil跳过、已有锚点Δ保持；F>0及到达转换不推出整链成功。 |
| A017／P3 | NOT_AFFECTED_CURRENT_NAVIGATION。audit/source-traceability及当前管理文件前驱→candidate2均未改；8处已应用导航的身份保留。 | A-REG/B21总体审计及全局gate保留；旧candidate提案限定作为历史，不改写成新正式修复。 |
| A018／P3 | NOT_AFFECTED。SCRIPT_TEXTS明确节身份、数字首行与Map对照的LZ条目未改；Weather字段不是该节入口。 | 测试原节/形状前提保留；没有运行解析或扩展未读输入保证。 |
| C003／P2 | PASS_SCOPED_PARTIAL_INTERFACE。完整4根/8扩展对固定原对象/acceptance核同；B02 WP06/TM14保持，新24表/缓存场景及共享目录条件经上文对照。 | 全部13贡献批次、多扩展与B21全局合并gate保持OPEN；本报告不关闭别的所有者缺口。 |
| C081／P2 | PASS_SCOPED_INTERFACE。源172–185、完成移动两调用和当前WP61/FP01–02核回绕/提前分流；WP06/TM12及接受B08的WP36未改。 | B08局部修订已接受，不能沿旧B02记录宣称仍未修；原有效约束及全局多贡献关闭gate仍待。 |

## 5. 他审问题、限制与后续

B14-AFFECTED-B03-001（P2）的回调正常前提/异常切点、R-B14-1-001（P3）的公共戳顺序、B14-B04-R1-01（P2）的重置句，在本受影响接口与独立源码判断一致；不是本次新编号，也不改其candidate1 REQUEST_CHANGES历史或代替各所有者candidate2复审。没有新增 B02缺陷，不静默降级，不关闭任何原ID。

U01–U10/G01–G12/AX01–AX20全保留。具名未读：Data/Scripts.rxdata及全部二进制/序列化数据，实际地图/事件，游戏/执行文件/DLL/mkxp.json及宿主容量，图片/音频/字体/soundfont，八杯赛文件、pokemon_metrics样本、backup/gen，未列源区间、真实plugin组合/动态分派/旧别名/EventScene/动态阴影可达及Demo链。未运行参考游戏、Ruby、编译、转换、生成、反序列化、模拟器、求解器或行为验证器。参考程序执行、运行观察、Demo链、静态行为向量执行均0；仅自写Git/hash/text/JSON账本检查执行。

canonical仍 **229 OPEN / 0 CLOSED**，登记与关闭权归父任务/A-REG。审查已完成并仅向授权review分支普通commit/push。**实际integration尚未交付，本报告不能用于实际SHA验收**；父任务交付新exact actual后，须重新固定完整前驱→actual与candidate2→actual、变化读者/锁及所需所有者gate。当前停等父任务安排，不自行集成。
