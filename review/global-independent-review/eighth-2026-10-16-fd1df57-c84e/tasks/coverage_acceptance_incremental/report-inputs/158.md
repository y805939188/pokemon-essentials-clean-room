# R8 KERNEL 独立审查：限定读集交接

**结论为 INCOMPLETE_NO_PASS / UPDATE_NOT_STARTED。** 本审者已连续完整阅读初始冻结的13个正式文件与77个参考源文件，但尚未完成全部跨域真实消费者、全部PBS记录及逐复合断言的双向接收。不得将77/77定义文件、135条显式事实或2219个机械条款定位项解释为内核全域完成。

固定比较基线为 B8 `fd1df570cad987dc3852a3b958f03916e317f7fe`、tree `751dfde81048c81390f89a65ca1d1a565ba8e1ca`、formal tree `f292698cdd4a8e725525a9be6dc34b75faaf151e`；参考R为 `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`、tree `7589c800b61ba13a13040ed0d686979b80a84fd0`。收口时重新计算冻结163路径的SHA256，全部与初始身份一致；root期间新增报告提交的当前HEAD另在identity-recheck.json记录，不能替代B8。请求配置为gpt-6.1-sol、ultra、default、Fast off；模型/effort/tier/Fast实际回显均UNVERIFIED。

Library合同 `libfile_f8ff592304d081918512f51317a8ecee`（36653字节，声明SHA256 `63944b6f264a8e4ed1415db710443a0673f250b8a248af2274a425a314ea068b`）已通过library_read连续读完1–241行；合并输出截断后拆段补读。c0/library技能和B8 AGENTS.md已全文读。本地Library字节级独立下载校验未取得，不能把提供的SHA256说成独立复算成功。planning/module-map.md全文已读；其他planning/全域材料不由本审者声称已读。

## 已读范围与接受边界

| 分母 | 个人阅读结果 | 尚未成立的结论 |
| --- | --- | --- |
| generic-kernel全部11正文/附表＋2个kernel catalog | 13/13连续全文，含WP06统计附表、WP07弃用附录、全部表格与向量 | 所有复合断言的逐断言source→consumer→primary接收尚未穷尽 |
| 初始参考源文件 | 77/77连续全文 | 不是参考全部432源分母，也不是全部跨域caller已验 |
| 010_Data定义 | GameData＋17硬编码文件＋21 PBS类文件全部全文，所有注册记录/字段/构造/查询/导出定义均读 | 域消费者和对应主规格尚待creature/combat/world具名接收 |
| 技术与核心流程 | Technical14、Save5、Compiler4、事件2、启动/Main、Stats/System/Temp、Overworld/Time、Utilities、Load/Save、FilenameUpdater全篇 | UI/世界/战斗/道具等其余真实调用者仍有可读未读项 |
| PBS文本 | 冻结73路径，个人全文0/73、记录0 | 不能用schema/编译器、机械解析、相同blob或其他人的存在性库存替代逐记录语义阅读 |
| 新增局部阅读 | Phone 1–175/530–565；WP75 290–299/410–415/438–445 | 两文件均PARTIAL_READ，不授全文件或全primary信用 |

精确路径、身份、范围与结构说明分别在read-set.v1.json、read-state.json、reading-ledger.json。source-unit-inventory.json是定义/记录位置的机械定位表，独立全文阅读证据来自ledger；其中结构项不自动获得语义接受。read-set.v1不可变，read-state另同步当前状态。新增局部读路径未混入77全文数。

## 候选及独立反证

候选完整身份、位置、前提、正常/最小反例、取消/失败/部分提交、负证据、保留scope、最小修订、同步集和验收在findings.json。当前required计数为0，仅root可在独立反证后裁决。

| 稳定ID | 当前主张 | 已有正确范围/反证 |
| --- | --- | --- |
| GR8-KER-001 | 主档先删，备份删除失败可留下主档缺失/备份仍在；次次存在性门又会绕过孤立备份。可能缺这一有序前缀的精确合同 | root与counter_kernel_first指出UI65§3.3及:245已有部分失败、不重试/不回滚，故不能指称当前规格原子或完全没有失败覆盖。原提案版本保留，主张已收窄，等待root裁决 |
| GR8-KER-002 | WP09:102及UI65:27的早期启动穷尽表，以“有文件→加载boot”代替实际非空数据条件；既存可读序列档适配成{}仍初始化默认boot并进入语言选择 | 独立审者否定把WP02:241/KC05:13充分正常语言子例当错误。WP08:39/WP09:103/LZ13/14/UI65:36/52/136正确。还纠正本提案后继前提：{}随后在load-screen构造先失败校验并进入备份/删除，拒绝退出，不能直接声称菜单false已到达 |
| GR8-KER-003 | WP04:196声称旧属性改名后会输出Changes made提示；默认源只调用纯格式化函数并丢弃返回值，没有输出请求 | counter_kernel_first独立读定义/调用、全源查覆写后认为固定范围静态成立；保留内容实际改写、固定路径、仅变化时写回与I/O失败边界，等待root最终分类 |

`TRIAGE-KER-MAPSAVE`保存在triage.json：地图局部保存普通异常被吞，后继tileset/system成功时仍可记“已修改并保存”；普通成功、无变化与受控第二结果均具名。补读WP75:295/:414/:444已明确地图保存吞异常、不报告，故当前无新行为缺口，最多待developer_full完整primary接收后判断WP04摘要是否需更明确引用。不能把这条triage升级为required。

另有可读定义待完整接收的观察：HandlerHashEnum、CallbackWrapper、一些低层流/弃用/随机/日历工具的默认caller尚未穷尽；缺caller不移出分母。紧急保存旧档备份消息、新游戏标记失败不回退两个facet经root反证已有正确覆盖，不再作为新发现。WP03:116历史承接措辞已交history_current/root核定，不在本报告擅自重开旧账。

## 双向矩阵与剩余链

file-unit-fact-consumer-spec-matrix.json含135条显式事实边，分别绑定源区间、具名单位、事实、消费者、正式条款、有限前提及未接收范围。clause-source-premise-matrix.json枚举13文档全部段落/表行定位并链接相关显式事实，但机械拆段**不是复合语义断言穷尽**；无边及复合尚未逐断言验收项仍标未完成。不得据矩阵存在或定位数量宣称完整逆向审计。

consumer-census.json给出全部参考Ruby文本对121个显式常量（含3元信息，即118设置）及74个GameStats声明字段的词法引用路径/行、个人文件阅读状态。它包含注释等词法命中，不代表独立行为分支、动态调用完整性或实际语义验收。root可把这些路径逐个接到域读者的本轮ledger；尚未接到真实消费者的项仍pending。

具名交界：creature_review已声明若干010_Data定义全文，本审者又独立读完整39文件，但其真实个体/UI链不由本读定义推出；combat_review的核心战斗片不等于全部数据/世代消费者；preflight_resources可接收Intl823行/WP08全文定义读取，但messages_core的所有key/body语义不由此获得信用；Compiler004全文与WP75正文属于source/primary两端，developer_full须具名crossjoin，不能任一端全文读就说链已验。root已安排firstwave与PBS三组待审任务，因CLI环境失败尚不能把待审prompt当完成报告。

## 可读未读与外部未知

**可审但尚未接收**：73个PBS全部记录；77以外Settings、Stats、Event/Menu/handler、Intl、HTTP/文件/弃用工具真实消费者；对应域primary全篇与所有数据记录条款；所有复合断言和未默认caller定义的最终语义接收。这些是本轮工作未完成，不是材料天然缺失。

**宿主/材料未知**：完整宿主、RMXP/图形/输入映射、HTTP实际请求、文件系统受控失败、地图/公共事件及资源真实Demo表现、真实旧存档/迁移运行。可读源分支与静态有限前缀已审，但不能据此宣称宿主表现或完整运行已证。Library独立下载字节hash与实际模型配置回显也保持UNVERIFIED。

所有行为向量均NOT_EXECUTED；参考行为、独立行为模型与宿主执行计数各0。文件读取、库存/定位、SHA256检查、JSON整理是工具动作，不计行为测试。工具调用完整历史计数无平台导出，UNVERIFIED。仅在本任务独占目录写报告/台账/辅助脚本；无formal/planning/audit/reference修改，无git commit/push，无修订启动。

findings.json附加版本快照时曾因浅复制循环引用发生一次半写；已保留findings.failed-write.txt，恢复001完整原提案并从本轮笔记/身份重建002/003，写明artifact_recovery，后续临时文件校验后原子替换。收口已验证全部JSON可解析。此为报告工具错误，既不是材料缺口，也不是参考行为发现。
