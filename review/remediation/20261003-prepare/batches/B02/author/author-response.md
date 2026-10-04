# A-B02 逐ID作者回应

状态：READY_FOR_REVIEW；下列为局部候选贡献，全部未经本作者批准。原规范finding的当前限定、有效二审和扩展完整保存在 [effective-finding-inputs.json](effective-finding-inputs.json)，批准方案输入见 [acceptance-inputs.json](acceptance-inputs.json)。

输入交接 `0a12de641542f9a59909d2a950c1de8df17ca09d`；本批七份正式路径之外保持只读。最小原稿同步建议见 [scope-conflicts.md](scope-conflicts.md)，公共修改只交 [registry-proposals.json](registry-proposals.json) 的 A-REG 串行处理。

## GIR-FD82-A006（P2；RUN-A-006）

角色：B02主责及贡献。

原问题：WP08把调试作者提取目标语言误计为游戏语言切换；旧原WP02/附表/WP08的错误不能当已接受前提。

候选修订：启动/载入实际切换与作者导出参数分开；选B后取消及成功导出均不写玩家语言/不换当前游戏消息；已有有效存档的真实载入切换保留直写。

前提：当前游戏语言与消息集A，作者候选A/B；LZ15在core/game问题取消，尚未进入导出器；LZ16默认core消息及材料可用、输出操作成功；真实载入例候选≥2并分别给定已读数据有效非空/为空。

最小反例：选导出目标B后取消，玩家语言与游戏消息仍A，导出文件无变化。

反向对照：真实载入语言菜单选B时会切游戏语言；有效非空存档数据还直接写回，而作者成功导出B仍不切。

| 层次 | 路径/条款与处理 |
| --- | --- |
| 原finding固定证据定位 | `deliverables/final-specification-set/generic-kernel/wp02-rule-configuration-and-data-variants.md`；历史证据未改，固定SHA/行范围见完整对象；现行路径处理见下行 |
| 原finding固定证据定位 | `deliverables/final-specification-set/generic-kernel/wp08-localization.md`；历史证据未改，固定SHA/行范围见完整对象；现行路径处理见下行 |
| 原finding固定证据定位 | `specs/kernel/wp02-rule-configuration-and-data-variants.md`；历史证据未改，固定SHA/行范围见完整对象；现行路径处理见下行 |
| 原finding固定证据定位 | `specs/kernel/wp02-settings-inventory-appendix.md`；历史证据未改，固定SHA/行范围见完整对象；现行路径处理见下行 |
| 原finding固定证据定位 | `specs/kernel/wp08-localization.md`；历史证据未改，固定SHA/行范围见完整对象；现行路径处理见下行 |
| 净化/测试候选 | `deliverables/final-specification-set/generic-kernel/wp08-localization.md` §4、§6.2、§6.4 |
| 净化/测试候选 | `deliverables/final-specification-set/test-catalog/generic-kernel-wp05-06-07-08-09-10.md` LZ13–LZ16 |
| 附表/登记交界 | `specs/kernel/wp02-settings-inventory-appendix.md` §7.3 Debug使用点：待父统筹精确扩围 |
| 测试/身份对照 | LZ15, LZ16, LZ13, LZ14；静态未执行 |
| 登记 | `registry-proposals.json#GIR-FD82-A006`；不请求CLOSED |

剩余：B01最终WP02局部贡献已接受且原字节保护；原WP02、设置附表、原WP08仍是错误目标；六路径范围建议之一，未获扩围未改；原ID的全部贡献/最终Ultra门尚未满足，不关闭根因。

## GIR-FD82-A010（P2；RUN-A-010）

角色：B02主责及贡献。

原问题：TM09把一次采摘的8/10/12个果实写成8/10/12株。

候选修订：各例从计数2独立复位；单株果实8/10/12给2/3/3；十株各10个给12；成功单株采摘总次数各+1，取消/容量不足两计数不增。

前提：最高产量配置10，各独立计数初始2；确认采摘、背包可接收全部果实、其他调用无异常；12仅为直接入口静态参数，不断言正常栽培超过上限。

最小反例：单株10个果实只+1到3；不是采摘10株的结果。

反向对照：十株每株10个果实分别成功，从2累加到12；取消/不足回到无增量分支。

| 层次 | 路径/条款与处理 |
| --- | --- |
| 原finding固定证据定位 | `deliverables/final-specification-set/generic-kernel/wp06-stats-directory.md`；历史证据未改，固定SHA/行范围见完整对象；现行路径处理见下行 |
| 原finding固定证据定位 | `deliverables/final-specification-set/test-catalog/generic-kernel-wp05-06-07-08-09-10.md`；历史证据未改，固定SHA/行范围见完整对象；现行路径处理见下行 |
| 原finding固定证据定位 | `specs/kernel/wp06-stats-directory.md`；历史证据未改，固定SHA/行范围见完整对象；现行路径处理见下行 |
| 原finding固定证据定位 | `specs/kernel/wp06-time-random-steps-stats.md`；历史证据未改，固定SHA/行范围见完整对象；现行路径处理见下行 |
| 净化/测试候选 | `deliverables/final-specification-set/generic-kernel/wp06-stats-directory.md` §3 berry_plants_picked / max_yield_berry_plants |
| 净化/测试候选 | `deliverables/final-specification-set/generic-kernel/wp06-time-random-steps-stats.md` §8向量导航 |
| 净化/测试候选 | `deliverables/final-specification-set/test-catalog/generic-kernel-wp05-06-07-08-09-10.md` TM09 |
| 附表/登记交界 | `specs/kernel/wp06-stats-directory.md` max_yield_berry_plants行正确，保持原字节 |
| 测试/身份对照 | TM09；静态未执行 |
| 登记 | `registry-proposals.json#GIR-FD82-A010`；不请求CLOSED |

剩余：原附表及原静态qty向量正确，未改；A-REG后续登记净化恢复及静态目录数量；仍需独立复审。

## GIR-FD82-A011（P2；RUN-A-011）

角色：B02主责及贡献。

原问题：trade_count被称为交换完成累加。

候选修订：进入交换入口先+1，再读送出成员/验目标物种；失败仍留增量，不把它理想化为成功计数。

前提：统计对象存在，trade_count初始7；队伍指定位置有效，目标为未注册物种标识，不是现成生物对象；直接入口静态合同，无插件拦截；不宣称Demo可达。

最小反例：目标物种验证抛错，计数7→8，队伍未替换且交换未完成。

反向对照：有效目标且其余流程成功也只+1；原/最终WP26校验前增加的正确合同保持。

| 层次 | 路径/条款与处理 |
| --- | --- |
| 原finding固定证据定位 | `deliverables/final-specification-set/generic-kernel/wp06-stats-directory.md`；历史证据未改，固定SHA/行范围见完整对象；现行路径处理见下行 |
| 原finding固定证据定位 | `specs/kernel/wp06-stats-directory.md`；历史证据未改，固定SHA/行范围见完整对象；现行路径处理见下行 |
| 净化/测试候选 | `deliverables/final-specification-set/generic-kernel/wp06-stats-directory.md` §5 trade_count行 |
| 净化/测试候选 | `deliverables/final-specification-set/test-catalog/generic-kernel-wp05-06-07-08-09-10.md` TM13 |
| 附表/登记交界 | `specs/kernel/wp06-stats-directory.md` trade_count行错误：待精确扩围 |
| 测试/身份对照 | TM13；静态未执行 |
| 登记 | `registry-proposals.json#GIR-FD82-A011`；不请求CLOSED |

剩余：原stats目录trade_count行待父统筹扩围；WP26交界只定点核读，无整域批准；A-REG登记其与WP06一致性。

## GIR-FD82-A012（P2；RUN-A-012）

角色：B02主责及贡献。

原问题：删除目录全部内容遗漏目标目录自身。

候选修订：删除列举文件→由内向外目录→目标根；普通空目录和仅一文件目录成功时根不存在，父目录仍在；失败传播且可部分删除；翻译覆盖只删文件保留目录。

前提：普通D及父目录存在、权限允许、无隐藏残留/并发/扩展改写、成功例所有调用成功；IO15额外给定文件列举顺序与第二次删除异常；仅该操作入口，不宣称任意隐藏/链接/宿主输入或Demo调用成功。

最小反例：输入空普通D也最终删除D，不是留下空目录。

反向对照：翻译覆盖成功会保留D及原有子目录；删除f1后f2失败时f1不恢复且D尚在。

| 层次 | 路径/条款与处理 |
| --- | --- |
| 原finding固定证据定位 | `deliverables/final-specification-set/generic-kernel/wp07-diagnostics-files-http.md`；历史证据未改，固定SHA/行范围见完整对象；现行路径处理见下行 |
| 原finding固定证据定位 | `specs/kernel/wp07-diagnostics-files-http.md`；历史证据未改，固定SHA/行范围见完整对象；现行路径处理见下行 |
| 净化/测试候选 | `deliverables/final-specification-set/generic-kernel/wp07-diagnostics-files-http.md` §3.1 |
| 净化/测试候选 | `deliverables/final-specification-set/generic-kernel/wp08-localization.md` §6.2、§6.4的邻近入口对照 |
| 净化/测试候选 | `deliverables/final-specification-set/test-catalog/generic-kernel-wp05-06-07-08-09-10.md` IO13–IO15、LZ12 |
| 测试/身份对照 | IO13, IO14, IO15, LZ12；静态未执行 |
| 登记 | `registry-proposals.json#GIR-FD82-A012`；不请求CLOSED |

剩余：原WP07同条款错误：待精确扩围；未验证宿主文件系统/链接/隐藏/并发组合；A-REG串行记录。

## GIR-FD82-A013（P2；RUN-A-013）

角色：B02主责及贡献。

原问题：翻译节名概括为数字节号，遗漏非零整数前缀先行及数字0拒绝。

候选修订：非空节先整数前缀，非零即编号；零结果再常量/Map纯数字；负编号拒绝。1tail接受为1、数字0拒绝、SPECIES_NAMES常量为1；EVENT_TEXTS常量0可接受。内容形态仍看首内容行，不混同。

前提：非空节、同一A/B两非数字内容行、输入可读、无合并冲突；直接单文件解析不打开输出；完整编译对照给定已成功打开旧输出为覆盖写。

最小反例：同内容1tail归1成功，数字0非法；不是严格全名称数字校验。

反向对照：SPECIES_NAMES也归1成功；内容索引0在SCRIPT_TEXTS三行数组可接受；完整编译失败不恢复已截断旧输出。

| 层次 | 路径/条款与处理 |
| --- | --- |
| 原finding固定证据定位 | `deliverables/final-specification-set/generic-kernel/wp08-localization.md`；历史证据未改，固定SHA/行范围见完整对象；现行路径处理见下行 |
| 原finding固定证据定位 | `specs/kernel/wp08-localization.md`；历史证据未改，固定SHA/行范围见完整对象；现行路径处理见下行 |
| 净化/测试候选 | `deliverables/final-specification-set/generic-kernel/wp08-localization.md` §6.3 |
| 净化/测试候选 | `deliverables/final-specification-set/test-catalog/generic-kernel-wp05-06-07-08-09-10.md` LZ17，保留LZ07及LZ08–LZ11形态边界 |
| 附表/登记交界 | `deliverables/final-specification-set/generic-kernel/wp08-localization.md` §3域目录0–30仅定位，不升级为严格数字节头范围 |
| 测试/身份对照 | LZ17, LZ08, LZ10, LZ11, LZ07；静态未执行 |
| 登记 | `registry-proposals.json#GIR-FD82-A013`；不请求CLOSED |

剩余：原WP08§6.3需精确同步，未改；GR-002原批准与新增候选区别保留；目录导航只向A-REG提议。

## GIR-FD82-A014（P2；RUN-A-014）

角色：B02主责及贡献。

原问题：缺失事件集合被净化成零条目集合也损坏。

候选修订：只在已到达守卫且先前地图操作成功时，缺失/空值触发损坏错误；存在零条目不触发。缺图调试/非调试分流保持。

前提：已到达恢复后事件守卫；地图及元数据可用、先前地图操作无失败；成对只变事件集合空值/存在零条目；不把通过守卫推成后续成功。

最小反例：存在的空事件集合不触发损坏异常，旧净化断言错误。

反向对照：相同前提仅改为空值则抛损坏；缺图错误是另一较早分支。

| 层次 | 路径/条款与处理 |
| --- | --- |
| 原finding固定证据定位 | `deliverables/final-specification-set/generic-kernel/wp09-save-startup-continue.md`；历史证据未改，固定SHA/行范围见完整对象；现行路径处理见下行 |
| 原finding固定证据定位 | `deliverables/final-specification-set/generic-kernel/wp10-migration-failure-recovery.md`；历史证据未改，固定SHA/行范围见完整对象；现行路径处理见下行 |
| 原finding固定证据定位 | `deliverables/final-specification-set/test-catalog/generic-kernel-wp05-06-07-08-09-10.md`；历史证据未改，固定SHA/行范围见完整对象；现行路径处理见下行 |
| 原finding固定证据定位 | `specs/kernel/wp09-save-startup-continue.md`；历史证据未改，固定SHA/行范围见完整对象；现行路径处理见下行 |
| 原finding固定证据定位 | `specs/kernel/wp10-migration-failure-recovery.md`；历史证据未改，固定SHA/行范围见完整对象；现行路径处理见下行 |
| 净化/测试候选 | `deliverables/final-specification-set/generic-kernel/wp09-save-startup-continue.md` §4.1、§7 |
| 净化/测试候选 | `deliverables/final-specification-set/generic-kernel/wp10-migration-failure-recovery.md` §5.4 |
| 净化/测试候选 | `deliverables/final-specification-set/test-catalog/generic-kernel-wp05-06-07-08-09-10.md` SV06、MG12 |
| 测试/身份对照 | SV06, MG12, SV04, SV05, MG11；静态未执行 |
| 登记 | `registry-proposals.json#GIR-FD82-A014`；不请求CLOSED |

剩余：原WP09/WP10对应nil合同正确保持；真实地图恢复及完整Demo仍未知，运行观察0。

## GIR-FD82-A015（P2；RUN-A-015/RUN-D-014）

角色：B02局部贡献；其他批次主责。

原问题：SV02丢失无存档/空已读数据前提，三门被误作新游戏充分条件。

候选修订：三门只跳菜单；空数据新游戏，有效非空继续；文件存在性与读取/旧数组转换后数据形态分开。

前提：debug真、无打包归档、SKIP_CONTINUE_SCREEN真；前序准备成功，独立给已读数据空/有效非空；不把文件存在性与读取后非空有效数据等价。

最小反例：同三门+有效非空数据跳菜单继续，不是新游戏。

反向对照：同三门+空数据跳菜单新游戏；旧数组转空的MG03说明存在文件不能替代数据门。

| 层次 | 路径/条款与处理 |
| --- | --- |
| 原finding固定证据定位 | `deliverables/final-specification-set/generic-kernel/wp09-save-startup-continue.md`；历史证据未改，固定SHA/行范围见完整对象；现行路径处理见下行 |
| 原finding固定证据定位 | `deliverables/final-specification-set/test-catalog/generic-kernel-wp05-06-07-08-09-10.md`；历史证据未改，固定SHA/行范围见完整对象；现行路径处理见下行 |
| 原finding固定证据定位 | `deliverables/final-specification-set/test-catalog/user-interface-wp17-63-65-66-67-68-69-70-71.md`；历史证据未改，固定SHA/行范围见完整对象；现行路径处理见下行 |
| 原finding固定证据定位 | `deliverables/final-specification-set/user-interface/wp65-title-load-options-pause-and-pc.md`；历史证据未改，固定SHA/行范围见完整对象；现行路径处理见下行 |
| 原finding固定证据定位 | `specs/kernel/wp09-save-startup-continue.md`；历史证据未改，固定SHA/行范围见完整对象；现行路径处理见下行 |
| 净化/测试候选 | `deliverables/final-specification-set/generic-kernel/wp09-save-startup-continue.md` §4.1标题/载入菜单行 |
| 净化/测试候选 | `deliverables/final-specification-set/test-catalog/generic-kernel-wp05-06-07-08-09-10.md` SV02；MG03边界保持 |
| 测试/身份对照 | SV02, MG03；静态未执行 |
| 登记 | `registry-proposals.json#GIR-FD82-A015`；不请求CLOSED |

剩余：主责B16；WP65和NV-T03固定输入局部合同正确保持，不提前消费B16候选；A-REG合并RUN-A-015/RUN-D-014，不重复计根因。

## GIR-FD82-A016（P2；RUN-A-016）

角色：B02主责及贡献。

原问题：旧帧数补统计概括缺执行时帧率、浮点、零值回退与存在键门。

候选修订：仅无统计键：N取缺失/空值/假值回退0，浮点N/F（F为给定正执行时帧率）；会话1；最近保存时间经游戏时间读取。冷无锚点两时间N/F，已有锚点两时间再+Δ并刷新锚点；统计键存在即使nil也跳过。

前提：已到达本转换、前序转换无异常、可处理保存表；数值例无统计键，F给定固定正数，N可浮点转换；冷例无时间锚点；非冷例给定锚点10与读取时长12.5；已存在键例与前述分开。

最小反例：相同120帧在F40得3.0、F60得2.0，121/F60保留小数，不能固定默认帧率/整数截断。

反向对照：缺失/nil/false/0得0；stats键现有nil跳过；已有锚点T2+Δ2.5得4.5而非2。

| 层次 | 路径/条款与处理 |
| --- | --- |
| 原finding固定证据定位 | `deliverables/final-specification-set/generic-kernel/wp10-migration-failure-recovery.md`；历史证据未改，固定SHA/行范围见完整对象；现行路径处理见下行 |
| 原finding固定证据定位 | `specs/kernel/wp06-stats-directory.md`；历史证据未改，固定SHA/行范围见完整对象；现行路径处理见下行 |
| 原finding固定证据定位 | `specs/kernel/wp10-migration-failure-recovery.md`；历史证据未改，固定SHA/行范围见完整对象；现行路径处理见下行 |
| 净化/测试候选 | `deliverables/final-specification-set/generic-kernel/wp10-migration-failure-recovery.md` §4表行、§4.1 |
| 净化/测试候选 | `deliverables/final-specification-set/generic-kernel/wp06-stats-directory.md` §9 play_time迁移引用 |
| 净化/测试候选 | `deliverables/final-specification-set/test-catalog/generic-kernel-wp05-06-07-08-09-10.md` MG13–MG16 |
| 附表/登记交界 | `specs/kernel/wp06-stats-directory.md` 原play_time迁移引用正确保持 |
| 测试/身份对照 | MG13, MG14, MG15, MG16；静态未执行 |
| 登记 | `registry-proposals.json#GIR-FD82-A016`；不请求CLOSED |

剩余：原WP10表行/数值段需父统筹精确扩围，未改；帧率宿主实际值、实际旧档读取/完整转换链未验证。

## GIR-FD82-A017（P3；RUN-A-017）

角色：B02主责及贡献。

原问题：audit/source-traceability八处真正目录错误；不能误报可唯一匹配后缀缩写/显式省略。

候选修订：作者逐处登记旧路径→固定参考树内正确路径，保留原行范围/原行为/历史批准；无公共写入。

前提：固定参考SHA/tree身份已核且clean；完整路径身份核验，不当行为全文审查；清锚点Scene_Map实际定点静态核读；其他未核语义保持未知。

最小反例：旧009_Scenes/002_Scene_Map.rb在固定参考树不存在，清锚点路径无法按该导航复核。

反向对照：正确Data/Scripts/003_Game processing/002_Scene_Map.rb存在，243–246直接核读；其余七处同样只路径定位，不改变证据等级。

| 层次 | 路径/条款与处理 |
| --- | --- |
| 原finding固定证据定位 | `audit/source-traceability.md`；历史证据未改，固定SHA/行范围见完整对象；现行路径处理见下行 |
| 净化候选 | 无正式写入；该ID正式目标属公共A-REG范围 |
| 附表/登记交界 | `audit/source-traceability.md` 八处路径更正建议，只能A-REG串行应用 |
| 测试/身份对照 | PATH01, PATH02, PATH03, PATH04, PATH05, PATH06, PATH07, PATH08；静态未执行 |
| 登记 | `registry-proposals.json#GIR-FD82-A017`；不请求CLOSED |

剩余：全部八处待唯一A-REG实际写公共audit；B21核全局导航/身份与正式后继；本作者无canonical关闭权限。

## GIR-FD82-A018（P3；RUN-A-018）

角色：B02主责及贡献。

原问题：LZ08–10各独立测试未明示非地图SCRIPT_TEXTS，Map005同内容会更早拒绝。

候选修订：三条逐条写SCRIPT_TEXTS域24；两行数字首行数组长度失败、非数字两行哈希登记、数字三行索引0登记；Map005两/三行均在长度前拒绝。

前提：每条独立显式节头与输入可读/非空；SCRIPT_TEXTS非地图域24，不由首行编号推断地图；完整编译输出截断与单文件解析入口分开。

最小反例：同0/原文/译文三行：SCRIPT_TEXTS接受索引0，Map005立即拒绝，省略节头不可重复判定。

反向对照：SCRIPT_TEXTS的A123/编号哈希成功，123/编号数组长度拒绝；Map005不等长度检查。

| 层次 | 路径/条款与处理 |
| --- | --- |
| 原finding固定证据定位 | `deliverables/final-specification-set/test-catalog/generic-kernel-wp05-06-07-08-09-10.md`；历史证据未改，固定SHA/行范围见完整对象；现行路径处理见下行 |
| 原finding固定证据定位 | `specs/kernel/wp08-localization.md`；历史证据未改，固定SHA/行范围见完整对象；现行路径处理见下行 |
| 净化/测试候选 | `deliverables/final-specification-set/generic-kernel/wp08-localization.md` §6.3 |
| 净化/测试候选 | `deliverables/final-specification-set/test-catalog/generic-kernel-wp05-06-07-08-09-10.md` LZ08–LZ11 |
| 测试/身份对照 | LZ08, LZ09, LZ10, LZ11；静态未执行 |
| 登记 | `registry-proposals.json#GIR-FD82-A018`；不请求CLOSED |

剩余：原表首行SCRIPT_TEXTS及后两行同节继承已足够，不借本修订改历史原稿；只局部GR-002前提修复，静态向量未执行。

## GIR-FD82-C003（P2；RUN-C-003/RUN-D-007/RUN-D-021/RUN-D-022）

角色：B02局部贡献；其他批次主责。

原问题：跨域测试前提漂移；WP06的18:30观察遗漏30秒缓存门会向WR12传播错误。

候选修订：WP06明确用运行时长控制重算：不足30秒复用旧色调，到期/无记录才按现实分钟插值；关闭开关返回缓存且不更新记录。

前提：给定缓存18:00色调，重算记录运行时长100；开关开启，现实18:30；各例运行时长129.999/130，到期门与更新取时均给定130；世界呈现室外/桥/高度等消费者前提未在本贡献更改。

最小反例：现实已18:30但仅过29.999秒，仍读旧缓存，不能无条件断言半小时新色调。

反向对照：满30秒才按18/19时表项各半重算；关闭开关复用缓存且不刷新记录。

| 层次 | 路径/条款与处理 |
| --- | --- |
| 原finding固定证据定位 | `deliverables/final-specification-set/creature-rpg/wp28-item-use-and-training.md`；历史证据未改，固定SHA/行范围见完整对象；现行路径处理见下行 |
| 原finding固定证据定位 | `deliverables/final-specification-set/creature-rpg/wp30-growth-learning-and-friendship.md`；历史证据未改，固定SHA/行范围见完整对象；现行路径处理见下行 |
| 原finding固定证据定位 | `deliverables/final-specification-set/creature-rpg/wp36-wild-encounters-and-modifiers.md`；历史证据未改，固定SHA/行范围见完整对象；现行路径处理见下行 |
| 原finding固定证据定位 | `deliverables/final-specification-set/demo-dx/wp72-debug-contexts-and-controls.md`；历史证据未改，固定SHA/行范围见完整对象；现行路径处理见下行 |
| 原finding固定证据定位 | `deliverables/final-specification-set/demo-dx/wp73-a-content-editors.md`；历史证据未改，固定SHA/行范围见完整对象；现行路径处理见下行 |
| 原finding固定证据定位 | `deliverables/final-specification-set/demo-dx/wp74-battle-animation-authoring-and-exchange.md`；历史证据未改，固定SHA/行范围见完整对象；现行路径处理见下行 |
| 原finding固定证据定位 | `deliverables/final-specification-set/engine-overworld/wp11-map-topology-transfer.md`；历史证据未改，固定SHA/行范围见完整对象；现行路径处理见下行 |
| 原finding固定证据定位 | `deliverables/final-specification-set/test-catalog/creature-rpg-wp35-36-57-64-68.md`；历史证据未改，固定SHA/行范围见完整对象；现行路径处理见下行 |
| 原finding固定证据定位 | `deliverables/final-specification-set/test-catalog/demo-dx-wp72-73-74-75-76-77.md`；历史证据未改，固定SHA/行范围见完整对象；现行路径处理见下行 |
| 原finding固定证据定位 | `deliverables/final-specification-set/test-catalog/engine-overworld-wp11-15-59-60.md`；历史证据未改，固定SHA/行范围见完整对象；现行路径处理见下行 |
| 原finding固定证据定位 | `deliverables/final-specification-set/test-catalog/engine-overworld-wp16.md`；历史证据未改，固定SHA/行范围见完整对象；现行路径处理见下行 |
| 原finding固定证据定位 | `deliverables/final-specification-set/test-catalog/pokemon-rules-wp53-60-61-62-69-70.md`；历史证据未改，固定SHA/行范围见完整对象；现行路径处理见下行 |
| 原finding固定证据定位 | `deliverables/final-specification-set/test-catalog/user-interface-wp17-63-65-66-67-68-69-70-71.md`；历史证据未改，固定SHA/行范围见完整对象；现行路径处理见下行 |
| 原finding固定证据定位 | `deliverables/final-specification-set/user-interface/wp17-messages-windows-input.md`；历史证据未改，固定SHA/行范围见完整对象；现行路径处理见下行 |
| 原finding固定证据定位 | `review/wp80-delivery-2026-10-03/batch-03/clause-disposition.md`；历史证据未改，固定SHA/行范围见完整对象；现行路径处理见下行 |
| 原finding固定证据定位 | `review/wp80-delivery-readiness-review-2026-10-03/input-snapshot/review/wp80-delivery-2026-10-03/batch-14/clause-disposition.md`；历史证据未改，固定SHA/行范围见完整对象；现行路径处理见下行 |
| 原finding固定证据定位 | `specs/demo/wp73-a-content-editors.md`；历史证据未改，固定SHA/行范围见完整对象；现行路径处理见下行 |
| 原finding固定证据定位 | `specs/demo/wp74-battle-animation-authoring-and-exchange.md`；历史证据未改，固定SHA/行范围见完整对象；现行路径处理见下行 |
| 原finding固定证据定位 | `specs/demo/wp75-project-conversion-and-authoring-tools.md`；历史证据未改，固定SHA/行范围见完整对象；现行路径处理见下行 |
| 原finding固定证据定位 | `specs/overworld/wp11-map-topology-transfer.md`；历史证据未改，固定SHA/行范围见完整对象；现行路径处理见下行 |
| 原finding固定证据定位 | `specs/overworld/wp12-terrain-movement-vehicles.md`；历史证据未改，固定SHA/行范围见完整对象；现行路径处理见下行 |
| 原finding固定证据定位 | `specs/overworld/wp59-world-time-weather-field-moves.md`；历史证据未改，固定SHA/行范围见完整对象；现行路径处理见下行 |
| 原finding固定证据定位 | `specs/overworld/wp60-fishing.md`；历史证据未改，固定SHA/行范围见完整对象；现行路径处理见下行 |
| 原finding固定证据定位 | `specs/pokemon-rules/wp61-field-passive-effects-and-blackout.md`；历史证据未改，固定SHA/行范围见完整对象；现行路径处理见下行 |
| 原finding固定证据定位 | `specs/ui/wp17-messages-windows-input.md`；历史证据未改，固定SHA/行范围见完整对象；现行路径处理见下行 |
| 原finding固定证据定位 | `specs/ui/wp66-a-party-and-summary-ui.md`；历史证据未改，固定SHA/行范围见完整对象；现行路径处理见下行 |
| 原finding固定证据定位 | `specs/ui/wp67-b-lifecycle-presentations-and-history.md`；历史证据未改，固定SHA/行范围见完整对象；现行路径处理见下行 |
| 原finding固定证据定位 | `specs/ui/wp71-tile-puzzles.md`；历史证据未改，固定SHA/行范围见完整对象；现行路径处理见下行 |
| 净化/测试候选 | `deliverables/final-specification-set/generic-kernel/wp06-time-random-steps-stats.md` §3.2–§3.3 |
| 净化/测试候选 | `deliverables/final-specification-set/test-catalog/generic-kernel-wp05-06-07-08-09-10.md` TM14 |
| 测试/身份对照 | TM14；静态未执行 |
| 登记 | `registry-proposals.json#GIR-FD82-C003`；不请求CLOSED |

剩余：仅WP06局部贡献；WR12由B04修下游测试；原规范全部root_adjudications及八条extensions.root_review原值附在effective-finding-inputs.json；B03/B04/B07/B08/B14–B21各自有效扩展仍开放，不用旧摘要覆盖；默认数据表、其他UI/地图/遭遇/天气/party/puzzle前提由对应批次处理，不消费其他未接受候选。

## GIR-FD82-C081（P2；RUN-C-081）

角色：B02局部贡献；其他批次主责。

原问题：WP36称31位钳制，和固定WP06低31位回绕合同冲突。

候选修订：WP06行为化为非负模2³¹回绕，普通步上界→0、前一值→上界；通知后门不撤前面的写计数；强制路线/解释器提前分流独立。

前提：普通步后入口，无强制路线/解释器运行；旧计数2147483647，排除后续订阅者改写；菜单/事件触发只影响较后的战斗检查；强制提前分流是反向例。

最小反例：旧2147483647普通步写0，不是饱和保持2147483647。

反向对照：旧2147483646写上界；强制路线/解释器上界保持不计数；普通菜单/事件门仍先回绕写入。

| 层次 | 路径/条款与处理 |
| --- | --- |
| 原finding固定证据定位 | `deliverables/final-specification-set/creature-rpg/wp36-wild-encounters-and-modifiers.md`；历史证据未改，固定SHA/行范围见完整对象；现行路径处理见下行 |
| 原finding固定证据定位 | `deliverables/final-specification-set/generic-kernel/wp06-time-random-steps-stats.md`；历史证据未改，固定SHA/行范围见完整对象；现行路径处理见下行 |
| 原finding固定证据定位 | `specs/creature-rpg/wp36-wild-encounters-and-modifiers.md`；历史证据未改，固定SHA/行范围见完整对象；现行路径处理见下行 |
| 净化/测试候选 | `deliverables/final-specification-set/generic-kernel/wp06-time-random-steps-stats.md` §4.1 |
| 净化/测试候选 | `deliverables/final-specification-set/test-catalog/generic-kernel-wp05-06-07-08-09-10.md` TM12 |
| 测试/身份对照 | TM12；静态未执行 |
| 登记 | `registry-proposals.json#GIR-FD82-C081`；不请求CLOSED |

剩余：主责B08：原/最终WP36钳制文字及遭遇测试仍待该批修订；只提交WP06一致性贡献；canonical ID仍开放。

## 跨批及未知边界

B02/B05在固定B01上三种正式读写交集均为空。共享测试完整保留EP01–EP21；WP05正文、弃用DP及其他批候选未改。C003八条扩展仍按原root_review范围留给相应批次；C081的WP36原/净化钳制文字仍由B08处理。B03/B06/B16/B18/B21须等父统筹安排本批受影响独立Ultra及实际整合后再冻结后继；本作者不释放下游。

U01–U10、G01–G12、AX01–AX20保持；参考静态读不证明未读材料、二进制、宿主帧率/IO、插件组合或Demo可达。运行观察0、真实Demo链0、参考执行0、静态向量执行0。
