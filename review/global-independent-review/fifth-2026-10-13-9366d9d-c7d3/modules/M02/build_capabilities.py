from record import *
from build_maps import anchors
C=[
('M02-PERSISTENT-REGISTRATION','持久值登记、校验、加载门及重复身份','supported','values default_values','wp09 §3.1–3.2; SV07–09,12–17','17默认值及动态重复登记分别成立；同键最终保存值不代替逐登记加载/验证。'),
('M02-PERSISTENT-STORES','开关、变量、自开关与便利访问','partial','switches variables selfswitches varhelpers default_values','wp09 §3.2; wp72 §4.2; wp70 §2/5; GR5-M02-001','持久性、5000上界、nil→0、直接/包装刷新已有；false/普通开关原值/自开关严格true差异为P3候选。'),
('M02-TEMPORARY-STATE','临时与持久系统状态分界','supported','temp system default_values','wp09 §3.2/4.2; wp65 §5.4; wp13 matrix','临时状态不经17注册保存；系统对象启动加载不强制新游戏重置；各字段业务规则归消费者。'),
('M02-STARTUP','启动装配、起点验证、选项生效','supported','main start load_ui default_values','wp09 §4.1; wp65 §3/5; SV01–02','启动/旧档转换发生在标题恢复UI之前，默认新游戏/continue三门与读数据空表分开。起点为0或缺图失败已分析。'),
('M02-NEW-CONTINUE','新游戏与继续状态提交','supported','values default_values start scene_title','wp09 §4.1–4.2; wp06 §3.1; SV03–07','加载标记、新游戏重置stats、锚点和会话+1、返回标题卸载门逐项对照。'),
('M02-MAP-RESTORE','存档恢复对世界生命周期的投影','supported','start metadata world_entry mapfactory mapnotify','wp09 §4.1; wp11 §6.1–6.2; U02-SV-WORLD01–02','只签进入/离开、清记录、恢复辅助及失败前缀；完整世界模块归其owner。'),
('M02-SAVE-WRITE','保存取值、覆盖写入与失败副作用','supported','save savefile playtime values save_ui','wp09 §5.1–5.2; SV10–11,17; wp65 §4','前置写入在捕获前，IO/系统错误只回退save_count，错型不回退；UI失败不恢复先清的新游戏标志。'),
('M02-SAVE-READ','读取格式、旧序列适配、回写/删除','supported','savefile values default_values','wp09 §5.2; wp10 §3.3–3.5; MG03,05','只读源码分析；原文件或bak、自定义路径和固定备份不同；旧序列默认无适配为空表。'),
('M02-MIGRATION-MECHANISM','迁移登记、版本选择与执行框架','supported','convert plugin_reg savefile','wp10 §3/6; MG01–05','两族先后、阈值字符比较与同阈值登记次序；先备份后转换版本回写；单对象只执行匹配逐值，不执行全表回调/备份。supported_static仅已述公开机制，不承诺任意旧档成功。'),
('M02-MIGRATION-BERRY','旧种植身份与字段迁移','partial','conversion_data berry_init','wp10 §4; wp60 §3; GR5-M02-004','两个转换的存在、顺序和替换时点已有；完整身份表/输入布局/长度门是候选缺口。'),
('M02-MIGRATION-FOLLOWER','旧跟随状态迁移','supported','conversion_data','wp10 §4 follower row','旧队列非空重建，旧字段清空在条件之外；坐标/外观/公共事件映射源码已审；真实旧对象样本不在证明内。'),
('M02-MIGRATION-DAYCARE','旧寄养迁移','supported','conversion_data daycare','wp10 §4; wp33 §3.4; MG09','首旧对象填所有空新槽及已有槽保留，与清旧字段区分；空旧槽占位与标记转换已分析，未理想化一对一。'),
('M02-MIGRATION-BAG','背包旧字段迁移','partial','conversion_data','wp10 §4; wp27 §5; wp65 §8.4','四字段有名称级合同；浅复制与lastpocket/lastPocket残留源码差异已记录，未被证明影响默认一次迁移，未单列必修。'),
('M02-MIGRATION-PLAYER-DEX','角色编号、图鉴与选项/天气迁移','supported','conversion_data','wp10 §4 rows6–9','角色加1；仅nil计数表/选项补值，既有图鉴形态跳过；天气0变None。仅局部已到达分支，不保证前序链。'),
('M02-MIGRATION-STATS','旧帧数补统计及碰撞字段补值','supported','conversion_data playtime','wp10 §4.1; stats play_time; MG13–16','浮点换算按给定当前帧率；存在stats键含nil跳过；读取保存时刻可能累加全局锚点；bump nil/false补0。'),
('M02-MIGRATION-MARKINGS','整数标记跨存储点迁移','supported','conversion_data','wp10 §4 marking row; wp21 §5.1','6低位0/1；队伍/盒/伙伴/漫游/净化/名人堂/变量0..5000及一层数组。当前合同列表与成员领域结合；不称深层任意对象递归。'),
('M02-MIGRATION-PHONE-FLUTE','电话与笛子旧状态迁移','partial','conversion_data phone_add metadata','wp10 §4 phone/flute rows; wp63 §4.5–4.6','电话冷启动global错误已覆盖；global已存在后的缺Phone.get也由WP63公开查询缺陷承接，迁移消费者投影保留。笛子按当前配置且非nil旧布尔含false迁移。'),
('M02-RECOVERY','坏档递归备份、删除与紧急保存','supported','load_ui emergency main errors savefile','wp10 §5; MG06–12; wp65 §3.3/4.2','无效返回才备份，异常不自动备份；递归bak但删除仅默认主档一级bak；紧急备份与无旧档恒提示已由WP65反证覆盖，GR3-M02-003不重开。'),
('M02-NOTIFICATIONS','事件订阅、参数分配与失败前缀','supported','events collections steps','wp05 §3; EP01–04,22–27','按回调arity规则分配；同键覆盖与列表去重不同；未定义命名事件无效果；异常无隔离/回滚。'),
('M02-CONDITIONAL-HANDLERS','内容处理器解析、复制与移除','partial','handlers condition','wp05 §3.1; wp28 §3.1; wp21 §6.9; GR5-M02-002','查找/参数归一/复制已有；条件组移除与clear差别为候选。Enum定义全文分析但实际消费者未定位，不按Unused注释宣称不存在。'),
('M02-MENU-EXTENSION','菜单排序、条件、动态名与效果','supported','menus','wp05 §4; wp65 §5.1/6/7','order缺失用登记序；条件收args，动态名无参；缺菜单枚举无项；call缺整个菜单可失败，正常菜单前提不扩成全输入容错。'),
('M02-PLUGIN-METADATA','插件元数据发现与脚本候选','supported','plugin_reg plugin_meta directories','wp05 §5.1; EP06–07,13–15,18–21','缺meta忽略、缺键与空键分层；.rb完整路径子串入选；显式顺序在前且文本去重；预处理来源跟读。'),
('M02-PLUGIN-DEPENDENCIES','插件依赖、冲突和版本比较','supported','plugin_reg plugin_meta','wp05 §5.2; EP08–12; MG01','字符hex值比较并非通常版本；可选精确实际可表达；循环/必需缺失中止；双向冲突核对。'),
('M02-PLUGIN-LIFECYCLE','发现、编译、产物消费与诊断','supported','plugin_load plugin_error main','wp05 §6–7; EP16–21; wp07 §5','三个阶段门不同；发布仍读产物；版本列表缺失警告；解压/注册在eval捕获外，脚本任何异常进插件诊断/退出。'),
('M02-CLOCK-CALENDAR','墙钟、时段、日历和色调输入','supported','calendar phone_time phone_frame','wp06 §3.1–3.3; wp59 §3; TM01–03,14','时间类别不可统一离线扣减；时段完整边界与色调缓存由world有效补充承接；只签核心输入算法不签显示。'),
('M02-PLAYTIME','累计游玩时间与保存/标题锚点','supported','playtime start scene_title','wp06 §3.1/4.2; TM04,08,11; MG13–16','惰性累加、无锚点不加、load重设、新游戏stats重建会话1；未执行宿主钟或存档往返。'),
('M02-STATS-DERIVED','派生统计与时间读取辅助','partial','stats playtime','wp06 stats §10; wp09 save_count; WP13 command122','移动和、捕获汇总、系统保存次数已有；每会话平均及距上次保存的局部辅助源码可读，但未独立列完整合同，未自动要求未来保留同名辅助API。'),
('M02-WALLCLOCK-TIMER','游戏变量墙钟计时','supported','timers variables default_values','wp06 §3.4; TM15–19','GR4-M02-001范围静态复核；严格大于/提前清0/天数反直觉公式不修改；历史探针不转为本轮执行。'),
('M02-GAME-TIMER','系统累计游戏时间计时器','supported','timer playtime system','wp13 command124; wp06 §3.1','无起点或无stats为0、可负余量、起点0有效；与墙钟计时不同，存于game_system持久值。'),
('M02-STEPS','普通/强制计步与距离统计','supported','steps movement_stats','wp06 §4.1; TM12; wp05 §3.3','普通2^31回绕且先于通知/战斗门；强制/解释器只generic step不累计；距离不等于该步计数。'),
('M02-STATS','74字段目录、初值及更新点','supported','stats default_values','wp06 §4.2; stats directory all74 rows; TM08–13','全部字段声明/默认与每个可得直接写入者的有限控制段均已审；8个事件写入缺失、BP赢来源待查保留，supported_static不包含这些未知写入者。'),
('M02-RANDOM-BASE','普通随机参数归一与算法边界','partial','rand','wp06 §5.1; phone/fishing consumers','具体域的整数区间已支持；两数闭区间、nil第二参数及非法类型回退等作者辅助输入未独立形成完整合同，未发现默认双参数调用，不据此宣称不可调用。'),
('M02-STATEFUL-RANDOM','偏向未出现值的状态选择','supported','anti rand','wp06 §5.4; TM20–23','GR4-M02-003正n条件分布与轮次重开静态复核；不是无放回/固定n次覆盖；非法规模无验收结论。'),
('M02-SEED-STATE','地牢/彩票全局播种副作用','supported','dungeon lottery metadata default_values','wp06 §5.1–5.2; TM05–06; WP14/WP70','种子优先与待播清空；彩票重播不是恢复前随机状态；不验证跨宿主相同序列。'),
('M02-RANDOM-RECORD','战斗随机记录/回放投影','supported','record','wp06 §5.3; TM07; WP58 §5','只签记录与取用机制；完整布局、AI未记录随机与回放实现归战斗owner。'),
('M02-DIRECTORIES','目录列举、递归、创建、删除','supported','directories','wp07 §3.1; IO13–15; wp05 script order','当前默认路径模式明确文件先于子树、先文件后目录删除含根；safeGlob缺目录入门与块错误不同；隐藏/链接/宿主行为未证。'),
('M02-FILE-WRAPPERS','路径解析、存在性、读取捕获集合','supported','resources file','wp07 §3.2–3.3; WP15 §3.1; IO06–07','非归档exists查文件系统，归档经数据读取；first/full目录错误集合不同；归档open与普通open路径规范化不同。'),
('M02-ARCHIVE-STREAM','归档内存读取状态机','partial','file stream','wp07 §3.2/10; GR5-M02-003','源码全部读完；归档材料与宿主neverload/load_data实现不可得/未执行；条件流语义尚缺合同。'),
('M02-BINARY-IO','小整数及索引内容读写辅助','unresolved','binary','wp07 broad file scope','读取/写入小端、短读补零、索引偏移长度及字符流接合已逐段分析；未定位核心直接消费者，宿主字符接口与未来兼容范围不明，不能把原语定义自动当生产API要求。'),
('M02-COPY-MOVE','文件复制/移动与部分失败','supported','copy_move','wp75 §11/17; wp07 §3.4 shared I/O','全读后删目标再写、成功复制后删源；wp75当前合同反证已覆盖，不重复立必修。'),
('M02-HTTP','网络薄包装与POST构造边界','supported','http','wp07 §4/6; IO01–05,16–20','GET/POST和基础/便利错误边界逐条核对；GR4-M02-002历史Ruby2.6精确异常仅历史隔离回执，不是本轮执行或真实请求。'),
('M02-ERROR-PRESENTATION','异常格式、日志、复制与信号','supported','errors plugin_error main','wp07 §5; IO08–12; wp10 §5.3','事件错误格式例外，普通10/内部25回溯；日志失败会阻断后继；重启/退出/超时按各调用边界。'),
('M02-CRITICAL-COMPLETION','关键段与主入口异常后的完成控制','partial','critical main','wp07 §5; wp09 §4.1; GR5-M02-005','信号/诊断已有，失败返回与主入口结束关系作为候选，不推宿主进程结局。'),
('M02-DEBUG-LOGGING','普通异常包装、即时日志与转储','supported','debug console','wp07 §5.2; wp72 §8.1; WP42 §8/WP51 §2','已有有效跨域合同反证：普通异常报告后不重抛，双标志只管常规日志，不管异常报告；各调用点后继依自身控制。'),
('M02-DEPRECATION','直接弃用警告与别名机制','supported','deprecation validation console','wp07 deprecation full; DP01–05; wp63 §4.6','每次告警/可选版本建议、类型/目标存在门、不显式转发block；31直接warn调用点已定位并跟读告警处，完整业务仅具名投影。'),
('M02-GENERAL-UTILITIES','通用集合、文本、常量和数学辅助','unresolved','rand copy_move console validation','WP54 combination; WP65 card number formatting; other helpers have no independent current clauses','完整源码已分析：组合枚举由WP54反证覆盖；Array交换/Hash合并/上下文回调/温度换算等内部或可选作者便利入口未形成独立规格。清洁实现可用任意方法达已述业务行为；未因方法存在而要求照抄API。')
]
for cid,title,status,src,doc,comp in C:
 cap(cid,title,status,anchors(src),[{'version':B,'contract':doc}],comp, ['Actual runtime, plugin combinations, binary save/archive round trips and missing demo writers remain unverified.'])
d=json.loads((P/'source-to-spec.json').read_text());d['capability_counting_rule']='Each id denotes one semantic capability. Statistics fields, source occurrences, test vectors and consumer projections are not additional capability counts.'
d['coverage_status_is_not_final_disposition']=True
d['source_index']=[{'path':x['path'],'version':x['version'],'review_extent':x['review_extent'],'material_availability':x['material_availability'],'evidence_level':x['evidence_level'],'semantic_ranges':x['segments'],'unreviewed_intervals':x['unreviewed_intervals'],'reading_coverage_ref':'reading-coverage.json'} for x in json.loads((P/'reading-coverage.json').read_text())['sources']]
(P/'source-to-spec.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
# Canonical shared identities, with consumer projections rather than duplicate capability findings.
shared=[
('KERNEL-PERSISTENT-VALUES',[], 'M02 / WP09','持久单元登记/加载/保存阶段', ['M01 configuration/version and localization boot values','WP11/13 map persistence','WP18–38 creature/player/inventory storage','WP65 save/continue UI'], 'M02-PERSISTENT-REGISTRATION', 'Only 17 defaults and extensible registration/stage behavior signed; field business owners retain responsibility.'),
('KERNEL-VARIABLE-ACCESS',[], 'M02 storage semantics; WP13 command semantics','变量、开关、自开关直接及便利访问', ['WP06 wallclock timers','WP13 event conditions/commands','WP70 lottery','WP72 debug'], 'M02-PERSISTENT-STORES','WP70 already supplies nil→0 and refresh/negative/upper-bound projections; candidate001 only remaining boolean-value distinctions.'),
('KERNEL-NOTIFICATION',[], 'M02 / WP05','命名通知顺序与异常前缀',['WP11 enter/leave/map setup','WP36 encounter selection','combat start/end','WP61 step effects'],'M02-NOTIFICATIONS','Only mechanism and necessary step/map callers; no whole-domain handler effect signoff.'),
('KERNEL-HANDLER-SELECTION',[], 'M02 / WP05','精确/条件处理器选择与生命周期',['WP21 forms','WP28 item use','WP48–52 abilities/items/AI'],'M02-CONDITIONAL-HANDLERS','WP28/WP21 current copy semantics reused only after source comparison; candidate002 confined to remove/clear.'),
('KERNEL-PLUGIN-LIFECYCLE',[], 'M02 / WP05','插件发现/编译/消费及版本比较',['M01 / WP04 compiler startup','WP10 migration comparator','author extensions'],'M02-PLUGIN-LIFECYCLE','No plugin sample, archive or dynamic plugin run; source discovery empty does not prove no compiled plugins.'),
('KERNEL-TIME',[], 'M02 / WP06; WP59 owns world/calendar presentation','现实时间、uptime、游玩时间与计时输入',['WP59 day/night/calendar','WP63 phone','WP60 berry/fishing','WP09/10 startup/save/migration'],'M02-PLAYTIME','Only specified input/state algorithms; no host clock accuracy, suspension or offline-unification guarantee.'),
('KERNEL-STATS',[], 'M02 / WP06 directory','74 persistent statistics declarations and consumer writes',['movement/field actions','item/inventory/shop','battle/outcomes','daycare/hatching/evolution','minigames and missing demo NPC events'],'M02-STATS','74 fields are data rows, not 74 new shared capabilities; known writer prefixes reviewed, 8 U01 and BP won unresolved.'),
('KERNEL-RANDOM',[], 'M02 / WP06','随机参数/状态种子/记录边界',['WP14 dungeon','WP70 lottery','WP58 battle recording','all domain probability consumers'],'M02-SEED-STATE','Separate ordinary draws, explicit seeding and recorded draws; no cross-language sequence guarantee.'),
('KERNEL-FILE-ACCESS',['KERNEL-ARCHIVE-READ'], 'M02 / WP07','路径与文件/归档读取分层',['M01 / WP08 message loading','WP58 replay file read','WP15 media path','WP75 file copy/move tooling'],'M02-ARCHIVE-STREAM','Archive stream is a projection of file access, not an extra shared-count root; candidate003 preserves missing archive/host boundary.'),
('KERNEL-HTTP',[], 'M02 / WP07','网络基础/便利包装与请求前构造',['WP64 gift download and data consumers','author POST extension'],'M02-HTTP','No actual HTTP or file-target POST; historical isolated Ruby results never relabeled GR5 execution.'),
('KERNEL-DIAGNOSTIC-FAILURE',[], 'M02 / WP07','诊断包装捕获/重抛/转换/继续与日志失败',['M01 compiler error cleanup','WP05 plugin exit','WP09/10 main/start/emergency','WP42 battle phases','WP51 AI choice','WP72 debug logs'],'M02-CRITICAL-COMPLETION','PBDebug, critical wrapper, compiler, plugin and main are distinct behavior contracts; candidate005 only critical/main completion.'),
('KERNEL-DEPRECATION',[], 'M02 / WP07 appendix','每次警告与目标转发',['WP63 18 legacy phone entries','WP03 Move data','WP20 Pokemon move','WP17 color wrappers','M01 legacy compiler API'],'M02-DEPRECATION','Warning success does not imply target operation succeeds; full phone semantics remains WP63 ownership.'),
('KERNEL-SAVE-MIGRATION',[], 'M02 / WP10','迁移列表与备份/回写及旧数据兼容',['WP60 plants','WP33 daycare','WP13 followers','WP27 bag','WP62 pokedex','WP63 phone','WP65 options'],'M02-MIGRATION-MECHANISM','One canonical migration mechanism; 14 conversion entries are consumer/data projections. candidate004 limited berry data gap.'),
('CREATURE-PLANT-PERSISTENCE',[], 'WP60 owner; M02 migration projection','当前植物字段与旧输入转换',['WP10 two berry conversions','WP06 berry counters'],'M02-MIGRATION-BERRY','Current plant reset fields read; full growth/UI source not signed by M02. Candidate004 requests compatibility data, not plant implementation.'),
('KERNEL-LOCALIZATION',[], 'M01 / WP08','启动消息加载及文件流消费者',['M02 startup and diagnostic warning text'],'M02-STARTUP','Only boundary source531–545 and startup/load callers read; LZ01–35 and remaining localization source not signed.')]
for sid,aliases,owner,behavior,consumers,cid,limit in shared:
 mutate('shared-interfaces','interfaces',{'id':sid,'aliases':aliases,'canonical_owner':owner,'behavior':behavior,'capability_id':cid,'consumer_projections':[{'consumer':v,'review_extent':'partial','evidence_level':'supported_static_boundary_only'} for v in consumers],'boundary':limit,'source_baseline':RV,'specification_baseline':B,'not_additive_to_capability_count':True,'execution_status':'NOT_EXECUTED_THIS_REVIEW'},'id')
print('Capabilities:',len(C),'canonical shared interfaces:',len(shared))
