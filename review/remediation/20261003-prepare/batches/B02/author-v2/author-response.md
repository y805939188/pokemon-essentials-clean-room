# A-B02 author-v2 逐ID后继回应

状态：READY_FOR_REVIEW。父统筹明确批准的六个原文件最小同步已实施；这是写范围授权，新增行为字节仍待独立Ultra。本候选不关闭规范finding。有效原finding/二审/扩展沿用v1完整固定输入，见 [原对象](../author/effective-finding-inputs.json) 和 [验收对象](../author/acceptance-inputs.json)。

原/净化/附表/测试/登记完整映射仍见 [v1逐ID回应](../author/author-response.md)；其中六项“待扩围”是v1历史状态，由 [本次授权](scope-expansion-authorization.json) 与以下原条款同步后继，旧文件原字节未改。

## GIR-FD82-A006（P2；RUN-A-006）

原WP02§6.3末句、设置附表Debug行、原WP08§4同步为作者导出目标语言；现游戏A、选B后取消和成功导出均不换游戏语言。启动/载入真正选择与存档直写保留。

前提：当前游戏语言与消息集A，作者候选A/B；LZ15在core/game问题取消，尚未进入导出器；LZ16默认core消息及材料可用、输出操作成功；真实载入例候选≥2并分别给定已读数据有效非空/为空。

最小反例：选导出目标B后取消，玩家语言与游戏消息仍A，导出文件无变化。

反向对照：真实载入语言菜单选B时会切游戏语言；有效非空存档数据还直接写回，而作者成功导出B仍不切。

| 层次 | 原/净化/附表/测试/登记映射 |
| --- | --- |
| 本次原稿/附表 | `specs/kernel/wp02-rule-configuration-and-data-variants.md` §6.3 玩家选择末句 |
| 本次原稿/附表 | `specs/kernel/wp02-settings-inventory-appendix.md` §7.3 Debug使用点行 |
| 本次原稿/附表 | `specs/kernel/wp08-localization.md` §4 选择机会、§6.3 节识别、§9.2 新增三组节名静态场景 |
| v1净化/测试保持 | `deliverables/final-specification-set/generic-kernel/wp08-localization.md` §4、§6.2、§6.4；字节与1c802783一致 |
| v1净化/测试保持 | `deliverables/final-specification-set/test-catalog/generic-kernel-wp05-06-07-08-09-10.md` LZ13–LZ16；字节与1c802783一致 |
| 最小/反向静态向量 | LZ15, LZ16, LZ13, LZ14；未执行 |
| 本次原表新增 | 无 |
| 登记 | `registry-proposals.json#GIR-FD82-A006`，仅A-REG建议 |

剩余：B01已接受的净化WP02原字节保留；本B02新增原条款及v1净化仍待独立Ultra；原规范ID不因本轮局部同步自行关闭。

## GIR-FD82-A010（P2；RUN-A-010）

本ID的v1局部贡献保持原字节，本轮不新增正式条款。

前提：最高产量配置10，各独立计数初始2；确认采摘、背包可接收全部果实、其他调用无异常；12仅为直接入口静态参数，不断言正常栽培超过上限。

最小反例：单株10个果实只+1到3；不是采摘10株的结果。

反向对照：十株每株10个果实分别成功，从2累加到12；取消/不足回到无增量分支。

| 层次 | 原/净化/附表/测试/登记映射 |
| --- | --- |
| 原稿 | 本轮未改；A010/A014/A015/A018的原正确合同保持 |
| v1净化/测试保持 | `deliverables/final-specification-set/generic-kernel/wp06-stats-directory.md` §3 berry_plants_picked / max_yield_berry_plants；字节与1c802783一致 |
| v1净化/测试保持 | `deliverables/final-specification-set/generic-kernel/wp06-time-random-steps-stats.md` §8向量导航；字节与1c802783一致 |
| v1净化/测试保持 | `deliverables/final-specification-set/test-catalog/generic-kernel-wp05-06-07-08-09-10.md` TM09；字节与1c802783一致 |
| 最小/反向静态向量 | TM09；未执行 |
| 本次原表新增 | 无 |
| 登记 | `registry-proposals.json#GIR-FD82-A010`，仅A-REG建议 |

剩余：原附表及原静态qty向量正确，未改；A-REG后续登记净化恢复及静态目录数量；仍需独立复审。

## GIR-FD82-A011（P2；RUN-A-011）

原stats仅trade_count行改为入口先加1、后校验，失败保留增量；计数7→8失败例与有效入口只增一次仍见TM13。

前提：统计对象存在，trade_count初始7；队伍指定位置有效，目标为未注册物种标识，不是现成生物对象；直接入口静态合同，无插件拦截；不宣称Demo可达。

最小反例：目标物种验证抛错，计数7→8，队伍未替换且交换未完成。

反向对照：有效目标且其余流程成功也只+1；原/最终WP26校验前增加的正确合同保持。

| 层次 | 原/净化/附表/测试/登记映射 |
| --- | --- |
| 本次原稿/附表 | `specs/kernel/wp06-stats-directory.md` §5 trade_count行 |
| v1净化/测试保持 | `deliverables/final-specification-set/generic-kernel/wp06-stats-directory.md` §5 trade_count行；字节与1c802783一致 |
| v1净化/测试保持 | `deliverables/final-specification-set/test-catalog/generic-kernel-wp05-06-07-08-09-10.md` TM13；字节与1c802783一致 |
| 最小/反向静态向量 | TM13；未执行 |
| 本次原表新增 | 无 |
| 登记 | `registry-proposals.json#GIR-FD82-A011`，仅A-REG建议 |

剩余：原/净化WP06统计与既有WP26定点合同一致；未作领域整包或实际演出批准；新增原条款待独立Ultra，公共导航/哈希待A-REG。

## GIR-FD82-A012（P2；RUN-A-012）

原WP07只删除入口及两个新静态根目录对照同步：先文件后目录含根；成功空/单文件D最终根不存在；不捕获异常、不撤回已删除项；翻译覆盖保留目录是反向入口。

前提：普通D及父目录存在、权限允许、无隐藏残留/并发/扩展改写、成功例所有调用成功；IO15额外给定文件列举顺序与第二次删除异常；仅该操作入口，不宣称任意隐藏/链接/宿主输入或Demo调用成功。

最小反例：输入空普通D也最终删除D，不是留下空目录。

反向对照：翻译覆盖成功会保留D及原有子目录；删除f1后f2失败时f1不恢复且D尚在。

| 层次 | 原/净化/附表/测试/登记映射 |
| --- | --- |
| 本次原稿/附表 | `specs/kernel/wp07-diagnostics-files-http.md` §3.1 删除入口、§8.2 新增两个根目录消失静态对照 |
| v1净化/测试保持 | `deliverables/final-specification-set/generic-kernel/wp07-diagnostics-files-http.md` §3.1；字节与1c802783一致 |
| v1净化/测试保持 | `deliverables/final-specification-set/generic-kernel/wp08-localization.md` §6.2、§6.4的邻近入口对照；字节与1c802783一致 |
| v1净化/测试保持 | `deliverables/final-specification-set/test-catalog/generic-kernel-wp05-06-07-08-09-10.md` IO13–IO15、LZ12；字节与1c802783一致 |
| 最小/反向静态向量 | IO13, IO14, IO15, LZ12；未执行 |
| 本次原表新增 | 删除普通空目录、删除含一个文件的目录 |
| 登记 | `registry-proposals.json#GIR-FD82-A012`，仅A-REG建议 |

剩余：隐藏/链接/宿主/并发组合未知，实际目录操作未执行；新增原条款及全部候选待独立Ultra；公共登记仅建议。

## GIR-FD82-A013（P2；RUN-A-013）

原WP08§6.3节名先非零整数前缀，再零结果的常量/Map；1tail→1成功、0拒绝、SPECIES_NAMES→1成功；负编号拒绝，EVENT_TEXTS常量0不等于数字节头0。追加同内容三组静态场景，旧GR-002形态/先截断保持。

前提：非空节、同一A/B两非数字内容行、输入可读、无合并冲突；直接单文件解析不打开输出；完整编译对照给定已成功打开旧输出为覆盖写。

最小反例：同内容1tail归1成功，数字0非法；不是严格全名称数字校验。

反向对照：SPECIES_NAMES也归1成功；内容索引0在SCRIPT_TEXTS三行数组可接受；完整编译失败不恢复已截断旧输出。

| 层次 | 原/净化/附表/测试/登记映射 |
| --- | --- |
| 本次原稿/附表 | `specs/kernel/wp08-localization.md` §4 选择机会、§6.3 节识别、§9.2 新增三组节名静态场景 |
| v1净化/测试保持 | `deliverables/final-specification-set/generic-kernel/wp08-localization.md` §6.3；字节与1c802783一致 |
| v1净化/测试保持 | `deliverables/final-specification-set/test-catalog/generic-kernel-wp05-06-07-08-09-10.md` LZ17，保留LZ07及LZ08–LZ11形态边界；字节与1c802783一致 |
| 最小/反向静态向量 | LZ17, LZ08, LZ10, LZ11, LZ07；未执行 |
| 本次原表新增 | 节名非零整数前缀、节名数字零、节名常量名 |
| 登记 | `registry-proposals.json#GIR-FD82-A013`，仅A-REG建议 |

剩余：仅新增节名条款/三个场景待独立Ultra；旧批准不覆盖新字节；静态编译入口的截断预期不是运行/二进制格式验证。

## GIR-FD82-A014（P2；RUN-A-014）

本ID的v1局部贡献保持原字节，本轮不新增正式条款。

前提：已到达恢复后事件守卫；地图及元数据可用、先前地图操作无失败；成对只变事件集合空值/存在零条目；不把通过守卫推成后续成功。

最小反例：存在的空事件集合不触发损坏异常，旧净化断言错误。

反向对照：相同前提仅改为空值则抛损坏；缺图错误是另一较早分支。

| 层次 | 原/净化/附表/测试/登记映射 |
| --- | --- |
| 原稿 | 本轮未改；A010/A014/A015/A018的原正确合同保持 |
| v1净化/测试保持 | `deliverables/final-specification-set/generic-kernel/wp09-save-startup-continue.md` §4.1、§7；字节与1c802783一致 |
| v1净化/测试保持 | `deliverables/final-specification-set/generic-kernel/wp10-migration-failure-recovery.md` §5.4；字节与1c802783一致 |
| v1净化/测试保持 | `deliverables/final-specification-set/test-catalog/generic-kernel-wp05-06-07-08-09-10.md` SV06、MG12；字节与1c802783一致 |
| 最小/反向静态向量 | SV06, MG12, SV04, SV05, MG11；未执行 |
| 本次原表新增 | 无 |
| 登记 | `registry-proposals.json#GIR-FD82-A014`，仅A-REG建议 |

剩余：原WP09/WP10对应nil合同正确保持；真实地图恢复及完整Demo仍未知，运行观察0。

## GIR-FD82-A015（P2；RUN-A-015/RUN-D-014）

本ID的v1局部贡献保持原字节，本轮不新增正式条款。

前提：debug真、无打包归档、SKIP_CONTINUE_SCREEN真；前序准备成功，独立给已读数据空/有效非空；不把文件存在性与读取后非空有效数据等价。

最小反例：同三门+有效非空数据跳菜单继续，不是新游戏。

反向对照：同三门+空数据跳菜单新游戏；旧数组转空的MG03说明存在文件不能替代数据门。

| 层次 | 原/净化/附表/测试/登记映射 |
| --- | --- |
| 原稿 | 本轮未改；A010/A014/A015/A018的原正确合同保持 |
| v1净化/测试保持 | `deliverables/final-specification-set/generic-kernel/wp09-save-startup-continue.md` §4.1标题/载入菜单行；字节与1c802783一致 |
| v1净化/测试保持 | `deliverables/final-specification-set/test-catalog/generic-kernel-wp05-06-07-08-09-10.md` SV02；MG03边界保持；字节与1c802783一致 |
| 最小/反向静态向量 | SV02, MG03；未执行 |
| 本次原表新增 | 无 |
| 登记 | `registry-proposals.json#GIR-FD82-A015`，仅A-REG建议 |

剩余：主责B16；WP65和NV-T03固定输入局部合同正确保持，不提前消费B16候选；A-REG合并RUN-A-015/RUN-D-014，不重复计根因。

## GIR-FD82-A016（P2；RUN-A-016）

原WP10只v20_add_stats行与§8.2四行数值/反向场景同步：无stats键才建，N缺失/nil/false回退0，浮点N/F，会话1；冷无锚点两时间T，已有锚点T+Δ并刷新，存在nil键也跳过。

前提：已到达本转换、前序转换无异常、可处理保存表；数值例无统计键，F给定固定正数，N可浮点转换；冷例无时间锚点；非冷例给定锚点10与读取时长12.5；已存在键例与前述分开。

最小反例：相同120帧在F40得3.0、F60得2.0，121/F60保留小数，不能固定默认帧率/整数截断。

反向对照：缺失/nil/false/0得0；stats键现有nil跳过；已有锚点T2+Δ2.5得4.5而非2。

| 层次 | 原/净化/附表/测试/登记映射 |
| --- | --- |
| 本次原稿/附表 | `specs/kernel/wp10-migration-failure-recovery.md` §4 v20_add_stats行、§8.2 新增对应数值前提与反向场景 |
| v1净化/测试保持 | `deliverables/final-specification-set/generic-kernel/wp10-migration-failure-recovery.md` §4表行、§4.1；字节与1c802783一致 |
| v1净化/测试保持 | `deliverables/final-specification-set/generic-kernel/wp06-stats-directory.md` §9 play_time迁移引用；字节与1c802783一致 |
| v1净化/测试保持 | `deliverables/final-specification-set/test-catalog/generic-kernel-wp05-06-07-08-09-10.md` MG13–MG16；字节与1c802783一致 |
| 最小/反向静态向量 | MG13, MG14, MG15, MG16；未执行 |
| 本次原表新增 | 旧帧数补统计（冷启动换算）、旧帧数补统计（缺值与零）、旧帧数补统计（已有键）、旧帧数补统计（已有锚点） |
| 登记 | `registry-proposals.json#GIR-FD82-A016`，仅A-REG建议 |

剩余：执行时正帧率是给定前提，不声称宿主默认/实际值；没有运行转换/读取真实存档，单项分支不保证完整链；新增原条款待独立Ultra。

## GIR-FD82-A017（P3；RUN-A-017）

本ID的v1局部贡献保持原字节，本轮不新增正式条款。

前提：固定参考SHA/tree身份已核且clean；完整路径身份核验，不当行为全文审查；清锚点Scene_Map实际定点静态核读；其他未核语义保持未知。

最小反例：旧009_Scenes/002_Scene_Map.rb在固定参考树不存在，清锚点路径无法按该导航复核。

反向对照：正确Data/Scripts/003_Game processing/002_Scene_Map.rb存在，243–246直接核读；其余七处同样只路径定位，不改变证据等级。

| 层次 | 原/净化/附表/测试/登记映射 |
| --- | --- |
| 原稿 | 本轮未改；A010/A014/A015/A018的原正确合同保持 |
| 最小/反向静态向量 | PATH01, PATH02, PATH03, PATH04, PATH05, PATH06, PATH07, PATH08；未执行 |
| 本次原表新增 | 无 |
| 登记 | `registry-proposals.json#GIR-FD82-A017`，仅A-REG建议 |

剩余：全部八处待唯一A-REG实际写公共audit；B21核全局导航/身份与正式后继；本作者无canonical关闭权限。

## GIR-FD82-A018（P3；RUN-A-018）

本ID的v1局部贡献保持原字节，本轮不新增正式条款。

前提：每条独立显式节头与输入可读/非空；SCRIPT_TEXTS非地图域24，不由首行编号推断地图；完整编译输出截断与单文件解析入口分开。

最小反例：同0/原文/译文三行：SCRIPT_TEXTS接受索引0，Map005立即拒绝，省略节头不可重复判定。

反向对照：SCRIPT_TEXTS的A123/编号哈希成功，123/编号数组长度拒绝；Map005不等长度检查。

| 层次 | 原/净化/附表/测试/登记映射 |
| --- | --- |
| 原稿 | 本轮未改；A010/A014/A015/A018的原正确合同保持 |
| v1净化/测试保持 | `deliverables/final-specification-set/generic-kernel/wp08-localization.md` §6.3；字节与1c802783一致 |
| v1净化/测试保持 | `deliverables/final-specification-set/test-catalog/generic-kernel-wp05-06-07-08-09-10.md` LZ08–LZ11；字节与1c802783一致 |
| 最小/反向静态向量 | LZ08, LZ09, LZ10, LZ11；未执行 |
| 本次原表新增 | 无 |
| 登记 | `registry-proposals.json#GIR-FD82-A018`，仅A-REG建议 |

剩余：原表首行SCRIPT_TEXTS及后两行同节继承已足够，不借本修订改历史原稿；只局部GR-002前提修复，静态向量未执行。

## GIR-FD82-C003（P2；RUN-C-003/RUN-D-007/RUN-D-021/RUN-D-022）

本ID的v1局部贡献保持原字节，本轮不新增正式条款。

前提：给定缓存18:00色调，重算记录运行时长100；开关开启，现实18:30；各例运行时长129.999/130，到期门与更新取时均给定130；世界呈现室外/桥/高度等消费者前提未在本贡献更改。

最小反例：现实已18:30但仅过29.999秒，仍读旧缓存，不能无条件断言半小时新色调。

反向对照：满30秒才按18/19时表项各半重算；关闭开关复用缓存且不刷新记录。

| 层次 | 原/净化/附表/测试/登记映射 |
| --- | --- |
| 原稿 | 本轮未改；A010/A014/A015/A018的原正确合同保持 |
| v1净化/测试保持 | `deliverables/final-specification-set/generic-kernel/wp06-time-random-steps-stats.md` §3.2–§3.3；字节与1c802783一致 |
| v1净化/测试保持 | `deliverables/final-specification-set/test-catalog/generic-kernel-wp05-06-07-08-09-10.md` TM14；字节与1c802783一致 |
| 最小/反向静态向量 | TM14；未执行 |
| 本次原表新增 | 无 |
| 登记 | `registry-proposals.json#GIR-FD82-C003`，仅A-REG建议 |

剩余：仅WP06局部贡献；WR12由B04修下游测试；原规范全部root_adjudications及八条extensions.root_review原值附在effective-finding-inputs.json；B03/B04/B07/B08/B14–B21各自有效扩展仍开放，不用旧摘要覆盖；默认数据表、其他UI/地图/遭遇/天气/party/puzzle前提由对应批次处理，不消费其他未接受候选。

## GIR-FD82-C081（P2；RUN-C-081）

本ID的v1局部贡献保持原字节，本轮不新增正式条款。

前提：普通步后入口，无强制路线/解释器运行；旧计数2147483647，排除后续订阅者改写；菜单/事件触发只影响较后的战斗检查；强制提前分流是反向例。

最小反例：旧2147483647普通步写0，不是饱和保持2147483647。

反向对照：旧2147483646写上界；强制路线/解释器上界保持不计数；普通菜单/事件门仍先回绕写入。

| 层次 | 原/净化/附表/测试/登记映射 |
| --- | --- |
| 原稿 | 本轮未改；A010/A014/A015/A018的原正确合同保持 |
| v1净化/测试保持 | `deliverables/final-specification-set/generic-kernel/wp06-time-random-steps-stats.md` §4.1；字节与1c802783一致 |
| v1净化/测试保持 | `deliverables/final-specification-set/test-catalog/generic-kernel-wp05-06-07-08-09-10.md` TM12；字节与1c802783一致 |
| 最小/反向静态向量 | TM12；未执行 |
| 本次原表新增 | 无 |
| 登记 | `registry-proposals.json#GIR-FD82-C081`，仅A-REG建议 |

剩余：主责B08：原/最终WP36钳制文字及遭遇测试仍待该批修订；只提交WP06一致性贡献；canonical ID仍开放。

## 冻结与剩余

完整后继候选是v1七净化文件＋本次六原文件；独立Ultra须冻结最终回复的精确候选SHA及父1c802783，不把v1静态自检当独立批准。旧author材料及七净化文件原字节保护，EP01–EP21整段保护；批准计划、历史review、公有登记、原文件历史Reviewed注记不反写。原历史Reviewed限定于旧固定字节，本轮新增原条款不是旧批准范围。

扩围后与B05三种正式读写交集仍为空；不消费任何其他未批准候选。A017八导航仍给唯一A-REG，C003/C081/A015跨批欠项保持。U01–U10/G01–G12/AX01–AX20及未读未知保留；参考执行0、运行观察0、真实Demo链0、静态向量执行0；模型/Max/Standard实际生效UNVERIFIED。
