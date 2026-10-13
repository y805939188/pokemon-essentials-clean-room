from pathlib import Path
import json,hashlib
P=Path(__file__).parent
RV='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
B='9366d9d17aaeac3b4414236468affa650fb3dd27'
R=Path('/Users/dingshinn/Desktop/pokemon-framework-reference/reference/pokemon-essentials')
F='deliverables/final-specification-set/'
S='Data/Scripts/'
CAN=Path('review/global-independent-review/fifth-2026-10-13-9366d9d-c7d3/counterevidence/root-M02/canonical-findings.json')
parent=json.loads(CAN.read_text())
def a(path,lo,hi,entry,fact=''):
 return {'path':S+path,'version':RV,'lines':[lo,hi],'entry':entry,'supporting_fact':fact}
def c(path,lo,hi,sec,claim):
 return {'path':F+path,'version':B,'lines':[lo,hi],'section':sec,'current_contract':claim}
def s(id,title,status,src,contracts,facts,reason,controls=None,finding=None,policy=None):
 return {'id':id,'title':title,'complete':True,'status':status,'facts_status':'supported_static','review_extent':'full','review_extent_boundary':'named finite subrange, not entire caller/domain','source_anchors':src,'current_contract_anchors':contracts,'reference_facts':facts,'semantic_reason':reason,'bounded_controls':controls or [],'final_finding':finding,'no_required_revision_reason':None if finding else reason,'policy_boundary':policy,'execution_status':'NOT_EXECUTED','independent_counterevidence_required':bool(finding)}
def rec(id,title,status,subs):
 return {'id':id,'title':title,'complete':True,'status':status,'subranges':subs,'new_findings':list(dict.fromkeys(x['final_finding'] for x in subs if x['final_finding'])),'fact_review_pending':False,'note':'完整处置可包含具名未决兼容政策；不把未决政策写成源码未读或事实矛盾。'}
bag=a('002_Save data/005_Game_SaveConversions.rb',207,230,'v20_rename_bag_variables')
baguse=a('013_Items/008_PokemonBag.rb',4,54,'current bag cursor declarations/defaults/read/write')
bagspec=c('generic-kernel/wp10-migration-failure-recovery.md',84,99,'§4','四个旧字段到新字段的迁移；不存在跳过。')
bagdomain=c('creature-rpg/wp27-bag-and-item-storage.md',33,54,'§2/§3.1','口袋/逐口袋游标为索引；默认1/0及读写门。')
quick=c('user-interface/wp65-title-load-options-pause-and-pc.md',212,228,'§8.2/8.4','快捷游标为三元索引，持久且经迁移填充。')
convert=a('002_Save data/003_SaveData_Conversion.rb',170,223,'conversion version selection/full and single run')
convertsp=c('generic-kernel/wp10-migration-failure-recovery.md',34,76,'§3.2–3.5','旧版本才选中，完整成功更新版本；单项前缀不自动撤回。')
records=[]
records.append(rec('M02-MIGRATION-BAG','背包旧字段迁移','resolved_with_named_policy_boundaries',[
 s('BAG-01','有效旧值的四个目标字段','supported_by_current_contract',[bag,baguse],[bagspec,bagdomain,quick],
 ['旧口袋号写当前口袋号；旧逐口袋索引写当前索引列表；旧登记列表和快捷三元索引分别成为当前字段。nil旧字段不覆盖当前字段。'],
 'WP10已给四个语义迁移，WP27/WP65给消费值形态和保存/游标含义；有效标量索引与列表正常输入不需要另造迁移API。',
 ['旧口袋2、逐口袋索引[0,3]与合法快捷索引[1,2,0]保留对应值；nil对照保持当前字段。']),
 s('BAG-02','lastpocket残留与正常完整链的重复选择门','internal_organization_no_required_revision',[bag,baguse,convert],[bagspec,bagdomain,convertsp],
 ['转换读取lastpocket而清空大小写不同的lastPocket，实际lastpocket仍保留。当前游标读写只取last_viewed_pocket。正常完整转换成功后版本更新为当前，下一次读取不再选择v20转换。'],
 '在明确的有效旧档一次完整迁移及其后正常读取/游标使用范围，残留源字段不改变公开游标值；当前合同未承诺清除每个历史实例字段，也未承诺序列化字节/实例槽布局相同。不要求新实现保留这项内部残留。',
 ['旧lastpocket=2→当前游标2；正常游标后改5，已升级版本的下次读取不自动再次把它改2。'],policy={'id':'BAG-REAPPLY-LEGACY-METADATA','status':'unresolved_policy','known_fact':'若外部保留旧版本元数据，并对同一对象重复请求单对象转换，残留lastpocket可再次覆盖当前游标：2→游标改5→重复转换又2。','decision_required':'是否兼容持有旧版本元数据的重复单对象迁移以及直接检查旧实例字段；不等同正常完整读档必须复刻残留。','if_preserved':'明确不保证幂等、重入可覆盖当前游标；无需保留Ruby字段组织。','if_not_preserved':'记录为超出所选旧档语义导入兼容范围，禁止把该选择写成原源已清理字段。'}),
 s('BAG-03','choices浅复制及注册列表/快捷索引引用','internal_organization_no_required_revision',[bag,baguse],[bagspec,bagdomain,quick],
 ['choices产生新外层列表并清旧字段；若元素为可变对象，内部引用仍共享。registeredItems和registeredIndex移交原列表引用并清旧字段。'],
 '已述正常游标域是平面数值索引；该前提下深复制与浅复制不改变游标值、夹限或导航结果，当前业务合同足以规定输出。无需规定新框架容器复制机制。',
 ['平面[0,3]导入后同值；清掉旧字段不等于撤销其他外部引用。'],policy={'id':'BAG-ALIASED-LEGACY-GRAPH','status':'unresolved_policy','known_fact':'若额外保存或外部对象共享旧登记列表，转换后对当前列表原位修改可被该别名观察；choices外层则已分离，但嵌套可变成员可共享。','decision_required':'是否支持非标准嵌套游标值、旧序列化对象图跨单元别名及作者持有旧列表引用。','if_preserved':'按别名可见性描述结果，不能笼统宣称所有迁移深复制。','if_not_preserved':'仅承诺有效领域值迁移，不追认源无别名副作用。'}),
 s('BAG-04','旧nil与false输入','unresolved_policy',[bag],[bagspec,quick],
 ['nil旧值跳过；registeredItems=false转换为空登记列表，registeredIndex=false转换为[0,0,1]，旧字段均清空。choices非nil会尝试clone；该输入不被额外验证成合法索引列表。'],
 'false旧列表不是已述正常列表/三元索引域，源对它有可判定回退，但当前合同未宣称任意错型旧字段兼容。保留具体事实并给出待选输入域，而非借无默认调用消除该规则。',
 ['旧registeredIndex=nil时不覆盖当前[2,3,0]；旧false时改为[0,0,1]。'],policy={'id':'BAG-FALSE-LEGACY-SENTINELS','status':'unresolved_policy','decision_required':'未来旧档兼容输入域是否包含false作为旧列表哨兵。','if_preserved':'须保留两个false回退及nil跳过的区别。','if_not_preserved':'显式把非列表旧值列为不承诺输入，不能说源把false当nil跳过。'})
]))
phone=a('002_Save data/005_Game_SaveConversions.rb',355,381,'v21_replace_phone_data')
phoneadd=a('013_Items/004_Item_Phone.rb',17,210,'record/class-level add and query')
phonespec=c('generic-kernel/wp10-migration-failure-recovery.md',95,96,'§4 phone/flute','电话转换须区分传入对象和运行全局；全局加载晚于转换，不能无条件成功。')
phonecontract=c('user-interface/wp63-pokegear-map-music-and-phone.md',70,125,'§4.2–4.6','持久电话、静默注册、公开查询缺失及旧入口失败边界。')
flute=a('002_Save data/005_Game_SaveConversions.rb',385,408,'v21_replace_flute_booleans')
records.append(rec('M02-MIGRATION-PHONE-FLUTE','电话与笛子旧状态迁移','supported_static_by_composed_current_contracts',[
 s('PHONE-01','已有电话跳过、创建和旧数据清理时点','supported_by_current_contract',[phone],[phonespec,convertsp],
 ['已有真值电话对象则整项跳过；无电话时先建新电话、清旧phoneTime；只有实际完成旧联系人遍历后才清phoneNumbers。旧联系人nil不进入遍历，空列表可正常清空。'],
 'WP10现行电话行的无对象前提与§3.5先前写入保留/失败中断相组合即可定位创建和失败前缀；不是保证任何旧电话均成功。',
 ['空旧联系人：建空电话并清旧时间/列表；首次注册失败：新电话和旧时间清理已发生，旧列表未清。']),
 s('PHONE-02','冷启动全局未加载的注册失败','supported_by_current_contract',[phone,phoneadd,a('003_Game processing/001_StartGame.rb',21,27,'set_up_system'),a('002_Save data/004_Game_SaveValues.rb',76,81,'global_metadata non-boot')],[phonespec],
 ['静默注册访问运行全局电话；正常冷启动的非启动持久全局尚未装载，旧非空联系人可在该注册入口失败。'],
 '这正是现行WP10电话转换行的具名失败前提，已独立分析过；直接承接，不新增相同根因。'),
 s('PHONE-03','已满足全局前提后的缺公开查询','supported_by_current_contract',[phone,phoneadd],[phonespec,phonecontract,convertsp],
 ['训练家分支静默注册后调用固定环境缺失的Phone.get；合法类型可已新增联系人，随后在旧可见性/再战旗标赋值前失败。此时phoneNumbers未清，后续转换和完整版本提交未到。'],
 'WP63已明确同一个公开查询能力缺失，WP10给出转换调用和对象/中断限制；属于已有共享缺陷的迁移消费者投影，不另造缺失方法根因。',
 ['运行全局恰为迁移对象，训练家类型合法：新增初始可见/旗标0联系人后缺查询失败；非训练家分支不调用该查询。']),
 s('PHONE-04','传入对象与活动全局不同的写入对象','supported_by_current_contract',[phone,phoneadd],[phonespec,phonecontract,convertsp],
 ['若活动全局不同且其电话有效，旧NPC联系人经静默注册进入活动电话；被迁移对象刚建的电话仍可为空。遍历正常结束后被迁移对象旧列表被清。'],
 '当前WP10明确要求追踪传入对象/运行全局，WP63定义持久电话注册写入；相组合已排除“总写入转换目标”的理想化。本条给出有限投影以供父整合，不要求重审电话主文。',
 ['一个合法NPC旧联系人、目标无电话、活动全局另有空电话：活动电话+1，目标新电话0，目标旧列表清空。']),
 s('FLUTE-01','两种配置方向、false/nil与未选字段','supported_by_current_contract',[flute,a('001_Settings.rb',239,242,'FLUTES_CHANGE_WILD_ENCOUNTER_LEVELS'),a('012_Overworld/002_Overworld_Metadata.rb',131,152,'four map-local flags')],[phonespec,c('generic-kernel/wp10-migration-failure-recovery.md',145,146,'§6','配置控制笛子转换方向。')],
 ['等级配置真：黑笛→高等级、白笛→低等级；假：黑笛→低遭遇率、白笛→高遭遇率。每个旧值非nil（含false）才赋所选目标并清旧值；nil跳过。未选中的另一类目标字段不被该转换重置。'],
 '已述“布尔标记存在时按设置转为等级/遭遇率变量”涵盖false值，不应把存在误读成布尔真；四个领域目标与配置已有身份。补成投影表即可，无新必修根因。',
 ['旧黑笛false且目标高等级true、等级配置真→高等级false；旧nil对照保留true；低遭遇率字段不因此清理。'])
]))
def write_partial():
 out={'schema_version':'gr5.review.v1','kind':'finite_partial_dispositions','complete':False,'source_baseline':{'commit':RV,'tree':'7589c800b61ba13a13040ed0d686979b80a84fd0'},'specification_baseline':{'commit':B,'formal_subtree':'d5a462b4c6f8b78c3264a25d6b5495230fa265e2'},'model_request':{'model':'gpt-6-astra','reasoning_effort':'ultra','service_tier':'default','fast':False,'actual_echo':'UNVERIFIED'},'scope_input':'followup-partial-triage-input.json','parent_canonical_reuse':{'path':str(CAN),'sha256':hashlib.sha256(CAN.read_bytes()).hexdigest(),'ids':['GR5-M02-001','GR5-M02-002','GR5-M02-003','GR5-M02-004','GR5-M02-005'],'decision':'all five independently confirmed by parent; original proposer objects preserved; qualifications reused, not reopened'},'records':records,'execution_status':'NOT_EXECUTED','scope_limits':'Only these six records and necessary exact caller/contract projections; no full repository or administrative/history audit.'}
 (P/'followup-partial-dispositions.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
 q=P/'followup-partial-progress.json';d=json.loads(q.read_text());d['completed_records']=[x['id'] for x in records];d['next_scope']='remaining derived stats, random, binary I/O, general utility disposition';q.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
write_partial()
stats=a('004_Game classes/012_Game_Stats.rb',150,192,'derived counters and play-time summaries')
statsmain=c('generic-kernel/wp06-time-random-steps-stats.md',25,42,'§3.1–3.2','有锚点时读取累计时间并刷新；缺锚点不增，载入另设锚点。')
statsdir=c('generic-kernel/wp06-stats-directory.md',108,140,'§8–§11','徽章/名人堂赋值、游戏时间和三类派生统计目录。')
records.append(rec('M02-STATS-DERIVED','派生统计与时间读取辅助','new_candidate_pending_independent_counterevidence',[
 s('STATS-01','移动总量、捕获次数和保存次数','supported_by_current_contract',[stats],[statsdir,c('generic-kernel/wp06-time-random-steps-stats.md',91,99,'§4.2','三类派生读值；统计持久归属另列。')],
 ['移动总量仅步行+骑行+冲浪，不另加已计入步行的冰滑量。没有玩家时捕获总量0，否则逐基础物种累加图鉴捕获次数。保存次数从系统对象读取，缺对象/空假值回0。'],
 '现行派生目录及各领域计数语义已承接这些查询。三个派生量不是新增持久字段，不需要规定源getter结构。'),
 s('STATS-02','徽章、首入名人堂和最近保存时间赋值','supported_by_current_contract',[stats],[statsdir,statsmain],
 ['徽章编号位置写当前游玩时间；名人堂时间只有原值0才赋；最近保存时间每次赋当前游玩时间。每次实际读取play_time沿锚点规则先刷新。'],
 '已有目录明确各赋值门和时间读取副作用；名人堂在时间0写回0后仍可再次赋，属于原值0门的直接推论，不须重新开立“首次只写一次”的相反合同。'),
 s('STATS-03','每会话平均游戏时间','candidate_pending_independent_counterevidence',[stats],[statsmain,statsdir,c('generic-kernel/wp06-time-random-steps-stats.md',159,174,'§8–10','现有TM目录和未知边界，无每会话平均查询。')],
 ['先读取并可能更新游戏时间T，再除以会话数S；没有本地S=0保护。正S时整数T/整数S保留整数商，浮点T保留连续商。'],
 '现行合同包含累计时间和会话数，但没有这项可调用统计查询、数值前提和读取副作用；仅列原始字段不足以唯一确定平均查询结果。候选006记录行为，不要求同名API。',
 ['无锚点T=5.0,S=2→2.5；整数T=5,S=2→2。锚点10、当前13、原T=9.0,S=2→6.0且累计T=12.0、锚点13。'],finding='GR5-M02-006'),
 s('STATS-04','距上次保存的游玩时间及异常输入边界','candidate_pending_independent_counterevidence',[stats],[statsmain,statsdir,c('generic-kernel/wp09-save-startup-continue.md',109,115,'§5.1','保存前刷新最近保存时刻，失败不回滚该时刻。')],
 ['查询先取得刷新后的T，再减最近保存时刻L；不使用墙钟，也不夹到0。T低于L时可负。与平均查询共享惰性刷新，但不是同一次采样的全局原子统计快照。'],
 '保存标记的定义和被保存字段已有，查询输出、负值边界仍缺；与平均查询合并为同根因006。零会话的精确宿主非有限/除零表现与浮点舍入不冒称执行。',
 ['无锚点T=5.0,L=7→−2.0；原T=9.0、锚点10、当前13、L=5→7.0并更新T/锚点。'],finding='GR5-M02-006')
]))
rand=a('001_Technical/002_RubyUtilities.rb',363,388,'global/Kernel random input normalization')
randspec=c('generic-kernel/wp06-time-random-steps-stats.md',19,21,'§2','普通随机表述为标准库随机，参数决定区间；无全局可重放保证。')
randsec=c('generic-kernel/wp06-time-random-steps-stats.md',101,129,'§5.1–5.3','普通调用/种子/记录，各具体域区间已有。')
records.append(rec('M02-RANDOM-BASE','普通随机作者输入','new_candidate_pending_independent_counterevidence',[
 s('RAND-01','正整数单上界与既有领域区间','supported_by_current_contract',[rand,a('013_Items/004_Item_Phone.rb',118,134,'phone integer range'),a('012_Overworld/005_Overworld_Fishing.rb',30,51,'fishing inclusive integer ranges')],[randspec,randsec,c('user-interface/wp63-pokegear-map-music-and-phone.md',87,91,'§4.4','再战随机20–39分钟，40不取。')],
 ['一个数值首参且第二参不是数值时委托原随机上界；正常整数区间通过最小/最大有效成员选择，因此整数排除尾端区间沿其实际最大成员，闭区间含两端。'],
 '电话/钓鱼等已述正常整数域结果已有承接，不重新申报20–39或5–10的既有规则。'),
 s('RAND-02','双数值闭区间与参数分派','candidate_pending_independent_counterevidence',[rand],[randspec,randsec],
 ['两个有序整数a≤b时，按宽b−a+1取得底层整数偏移，再加a，结果可含b。首参为区间时第二参数不参与；首参为数值而次参非数值时次参被忽略。'],
 '现行“标准库调用/由参数确定”不能唯一推出双数值闭区间和参数优先级。合法作者调用本身有可观察输出，不因无默认双参数调用而排除。候选007仅补输入/输出数学合同。',
 ['a=5,b=7，底层偏移0/1/2分别输出5/6/7；a=b=5只输出5。区间5...8加任意第二参仍只取5/6/7。'],finding='GR5-M02-007'),
 s('RAND-03','空首参与其他类型首参','candidate_pending_independent_counterevidence',[rand],[randspec,randsec],
 ['空首参委托第二参数给底层；既非区间、数值也非空的首参回到无参底层抽样，第二参数也不使用。故文本“5”不被解析为数值上界，也不由该包装自行拒绝。'],
 '这是输入归一导致的作者侧观察差异，和默认概率公式/种子记录是不同合同；并入007，不新设随机服务或要求保留语言方法名。',
 ['空首参、正整数7等价向原随机源请求上界7；文本首参“5”、第二参1转无上界抽样，而非确定输出0。'],finding='GR5-M02-007'),
 s('RAND-04','随机来源与非常规数值/区间','named_runtime_boundary',[rand],[randsec],
 ['包装不建立独立随机状态或种子；委托同一原随机入口。浮点Numeric、反向/空/无界/非数值区间仍经过相应取端点/差值或底层调用，未加统一输入校验/错误归一。'],
 '正整数能力事实已可静态给出；其它输入的精确原生接受、分布和异常类取决于底层接口与端点对象，不混入有效整数合同。不是保留“规则未知”，而是列明仍由宿主承担的具体阶段。',
 ['相同输入区间及给定底层偏移可静态推输出；不承诺跨语言seed序列一致。'],policy={'id':'RANDOM-NONINTEGER-NATIVE-PROFILE','status':'unresolved_runtime','boundary':'未执行底层旧随机及Range端点对象；具体浮点/非法区间分布与异常不在本轮新候选正整数验收内。','future_policy':'可另选有效输入域或保留旧输入回退；不能把这种政策选择伪装成源已进行统一校验。'})
]))
binread=a('001_Technical/002_Files/002_FileMixins.rb',1,86,'integer and indexed-entry reading')
binwrite=a('001_Technical/002_Files/002_FileMixins.rb',88,149,'integer writing and File/StringInput/StringOutput integration')
binspec=c('generic-kernel/wp07-diagnostics-files-http.md',21,52,'§3','目录/文件/归档打开与内容读包装；未定义定宽小整数或索引记录格式。')
records.append(rec('M02-BINARY-IO','小整数与索引内容I/O','new_candidate_pending_independent_counterevidence_with_runtime_boundary',[
 s('BIO-01','定宽小端读取与短输入','candidate_pending_independent_counterevidence',[binread],[binspec],
 ['在读取接口提供0..255整数单元的前提下，读1/2/4单元按低字节先行组成无符号值；不足所需单元时返回已读低位值，不额外补读错误，高位等效0；无单元返回0。8位有符号读把最高位1的结果减256。'],
 '该规则决定外部数据字节到数值的兼容结果，具有独立于方法组织的可观察差异。现行全文文件读取或归档流合同不提供字节序/宽度/短读结果；候选008使用条件式数据协议，不要求复刻混入结构。',
 ['字节34 12（十六进制）读16位→4660；只有34→52；空输入→0；有符号FF→−1。'],finding='GR5-M02-008'),
 s('BIO-02','绝对定位读与8字节索引条目','candidate_pending_independent_counterevidence',[binread],[binspec],
 ['绝对定位辅助先改变位置再按宽读取。索引能力每次回到文件开头，以首个32位值除8取整数商推条目数；第i项从8i位置读偏移、从8i+4读长度。i≥条目数时偏移/长度返回0，内容返回空字符串；内容长度0也直接空字符串，否则定位到偏移读指定长度。没有负索引的独立守卫。'],
 '这是可声明的兼容数据格式与返回状态，而非未来容器架构。若误用显式计数头、大端字段或把超界统一抛错，会改变同一给定字节输入；与003流seek/EOF为不同根因。',
 ['首记录偏移16给条目数2；索引2返回0/空字符串。第二项(偏移19,长度0)内容读为空，不请求偏移19处的内容。'],finding='GR5-M02-008'),
 s('BIO-03','定宽写出、截断与失败前缀','candidate_pending_independent_counterevidence',[binwrite],[binspec],
 ['整数输出仅保留低8/16/32位，以低字节先行逐单元交给写入接口；不做溢出拒绝。底层写入异常不被此层捕获；此前已交付字节无撤回步骤。'],
 '输出字节和失败后的已写前缀会影响后续独立读取，不能仅称实现内部组织。与读取/索引同一个定宽字节协议根因，合入008。',
 ['0x123456写16位→56 34；−1写16位→FF FF（整数低位投影前提）。第二单元写入失败时第一单元已交付。'],finding='GR5-M02-008'),
 s('BIO-04','File/内存字符流/输出宿主接合','named_runtime_boundary',[binwrite,a('001_Technical/002_Files/001_FileTests.rb',366,484,'StringInput getc/read/position')],[binspec],
 ['File接入输入和输出辅助；内存流each_byte直接产出getc结果而不强制变整数，binmode为空操作；StringOutput声明仅接入输出辅助，本文件未给写入宿主实现。'],
 'BIO01的整数单元前提不得自动套到返回字符的内存接口：若getc产出字符，单单元读取会透传字符，数值组合不因此获得整数协议保证。实际宿主类型/接合未执行，继承003已确认的原生输入未知边界；不重开或拓宽003。',
 ['整数单元提供方可按BIO01计算；字符提供方和缺write能力的输出对象不宣称成功。'],policy={'id':'BINARY-NATIVE-ADAPTER-PROFILE','status':'unresolved_runtime','known_boundary':'给定整数byte接口与真实File/StringInput/宿主StringOutput不是同一证据层。','future_policy':'若保留此数据协议，可使用独立实现的显式字节接口；是否同时兼容旧字符接口故障另作政策，不要求照抄适配结构。'})
]))
write_partial()
u=lambda lo,hi,name:a('001_Technical/002_RubyUtilities.rb',lo,hi,name)
g=lambda lo,hi,name:a('019_Utilities/001_Utilities.rb',lo,hi,name)
coreio=c('generic-kernel/wp07-diagnostics-files-http.md',85,96,'§5','诊断可见内容、异常报告、控制台分级及着色。')
constsp=c('generic-kernel/wp03-content-identity-and-schema.md',99,117,'§5.1','数据字段模式、枚举/整数输入与逻辑身份，不规定语言类组织。')
records.append(rec('M02-GENERAL-UTILITIES','通用集合、文本、常量和数学辅助','resolved_by_business_abstraction_and_named_compatibility_policies',[
 s('UTIL-01','基础对象显示与类名转身份','internal_organization_no_required_revision',[u(1,19,'Object inspect/full_inspect; Class to_sym')],[coreio,constsp],
 ['基础对象检查显示缩为类标签，原检查入口另存；只影响走该基础实现的对象，不覆盖有自身检查显示的所有子类型。类名可转符号身份。'],
 '前者服务已述诊断类型/消息，后者把源语言类组织适配到身份值。独立实现应满足领域身份与诊断信息，不需要引入源类反射或通用对象方法替换。未承诺字节相同的调试对象转储。'),
 s('UTIL-02','元音首字符与业务冠词','supported_by_current_contract',[u(24,27,'starts_with_vowel?'),a('012_Overworld/006_Overworld_BerryPlants.rb',410,429,'berry naming messages')],[c('pokemon-rules/wp60-berry-plants.md',113,121,'§6.3','种植消息含元音冠词处理。')],
 ['非空文本仅首字符小写化后与a/e/i/o/u匹配；不是语音学发音识别。空字符串首字符为空，随后操作可失败。'],
 '有效物品名的冠词行为已有业务承接；具体函数/字符串扩展方式是内部选择。空名不是本条已述有效名称前提，不能给源补安全空串回退。',policy={'id':'TEXT-EMPTY-NAME-ARTICLE','status':'unresolved_policy','decision_required':'是否对空物品名/作者直接空串查询保留首字符失败，而非改成安全false。','known_fact':'源没有空串守卫；非空普通名字不受该边界影响。'}),
 s('UTIL-03','首尾片段、空白和数值文本判别','unresolved_policy',[u(29,56,'first/last/blank?/numeric?'),a('001_Technical/002_Files/001_FileTests.rb',315,325,'file.last suffix guard')],[c('generic-kernel/wp07-diagnostics-files-http.md',29,39,'§3.2','文件目标与读取捕获集合。'),constsp],
 ['正n时首片段取前n；尾片段n超过长度回原文，n=0也回整串。blank?检查去端部空白后为空。numeric?仅可选正负号+至少一位十进制数字+可选小数点及至少一位小数；不接受指数、仅点、前后空白。'],
 '文件首字节入口只需要默认末字符是否为斜杠，该业务已覆盖；其余完整通用文本helper输入域不应伪称已由PBS数值模式覆盖，二者不是同一解析器。事实在此固定，是否兼容整个旧通用helper输入表单独裁定。',
 ['文本ABC的尾长0/5均ABC；“1.2”为数值，“1e2”/“ 1”不通过该helper；这些不是整个PBS解析的拒绝保证。'],policy={'id':'LEGACY-TEXT-HELPER-INPUTS','status':'unresolved_policy','decision_required':'是否把上述通用首尾/空白/ASCII数值谓词作为作者兼容输入合同。','if_preserved':'声明具体输入输出和0长度特殊情况；无需同名字符串方法。','if_not_preserved':'仅约束各业务解析/路径规则，不能声称源helper行为已不存在。'}),
 s('UTIL-04','金额分组与学习消息中的数词','supported_by_current_contract',[u(62,78,'to_s_formatted/to_word'),a('013_Items/001_Item_Utilities.rb',591,608,'learning count message'),a('011_Battle/001_Battle/003_Battle_ExpAndMoveLearning.rb',237,253,'battle learning count message')],[c('user-interface/wp65-trainer-card-appendix.md',35,37,'text fields','金钱千分位格式。'),c('creature-rpg/wp30-growth-learning-and-friendship.md',154,164,'learning','满槽消息显示已有N招式，随后学习/遗忘选择。')],
 ['整数金额每三位分组；数词列表包含0到20的本地化文字。整数21满足当前边界但取列表外，返回空；其它整数范围外/非整数转普通文本。格式辅助先转文本再从右分组三位，不等同任意小数专用格式器。'],
 '正常整数金额与默认招式数的显示信息已有业务合同，使用数字还是本地化文字的实现组织不需以源Numeric扩展为模板。超出列表的21及任意小数字符串分组不在正常已述显示输入内。',policy={'id':'LEGACY-NUMERIC-PRESENTATION-EXTREMES','status':'unresolved_policy','decision_required':'是否要求兼容直接数词21的空返回和任意小数分组，而非只保证有效业务显示。','known_fact':'不能把源数词列表误写为0..21均有词，或把格式器概括为完整小数格式服务。'}),
 s('UTIL-05','数组对称差','unresolved_policy',[u(81,87,'Array symmetric difference')],[constsp],
 ['结果去重，仅保留恰在一侧出现的值；左侧独有值在前，随后右侧独有值，均按原首次出现次序。'],
 '这是事实已明确的通用集合操作；当前业务身份/队伍/处理器合同没有宣称统一作者集合运算接口。不能仅凭没有默认调用判为不存在，也不能据源扩展自动要求新框架公开数组算符。',
 ['左[A,A,B]、右[B,C,C]→[A,C]。'],policy={'id':'LEGACY-GENERAL-SET-OPERATIONS','status':'unresolved_policy','decision_required':'是否把通用集合对称差（含去重/顺序）纳入作者兼容能力面。','if_preserved':'按集合成员与顺序合同描述即可，不规定运算符/数组类型。'}),
 s('UTIL-06','按值交换辅助与插件依赖排序','internal_organization_no_required_revision',[u(89,94,'Array swap'),a('001_Technical/005_PluginManager.rb',498,550,'dependency ordering')],[c('generic-kernel/wp05-events-extensions-plugins.md',75,80,'§5.2','依赖排序、缺失必需/循环错误。')],
 ['交换的是两值首次位置。插件实际调用前有名称去重与必需依赖存在门，合法输入中的两位置已确定。'],
 '既有插件依赖约束及校验可由任意排序手段实现；按值交换是实现手段，不另规定框架数组API或把内部返回值纳入业务协议。',policy={'id':'LEGACY-SWAP-MALFORMED-INPUT','status':'unresolved_policy','known_fact':'直接对[A,B]请求交换A与不存在的C时，第一位置可先被写C，随后缺第二位置失败，未撤回；正常插件前门排除该输入。','decision_required':'是否保留直接非法交换的部分写入兼容性；该政策不改变缺依赖已在排序前拒绝的现行业务合同。'}),
 s('UTIL-07','递归合并与控制台平面样式','internal_organization_no_required_revision',[u(100,118,'deep_merge/deep_merge!'),a('001_Technical/001_Debugging/002_DebugConsole.rb',191,231,'markup style accumulation')],[coreio],
 ['控制台该调用合并平面颜色/样式键，值为颜色身份或布尔标志，正常路径不要求嵌套递归。通用原位合并遇左值为映射时只递归：右值非映射则该递归无操作；非原位入口只复制外层，嵌套映射仍可写穿原输入。'],
 '当前可见着色/标志组合不需要规定递归容器库。上述嵌套别名特征没有被当前正常样式输入触发，业务可用独立样式模型达同样输出；未把通用helper的别名事实抹除。',
 ['左k→{x:1}，右k→{y:2}：非原位入口所得外层不同，但原左k仍被加y；右k→5时左嵌套映射不被5替换。'],policy={'id':'LEGACY-NESTED-MERGE-ALIASING','status':'unresolved_policy','decision_required':'是否保留作者直接深合并时的写穿别名和映射/标量冲突规则。','if_preserved':'须记录上述两组结果，不能把它写成通用深复制合并；不必采用同样容器。'}),
 s('UTIL-08','逐项映射与设施持物快照','internal_organization_no_required_revision',[u(123,129,'Enumerable transform'),a('018_Alternate battle modes/001_Battle Frontier/004_Challenge_Battles.rb',54,82,'held-item snapshot and restoration')],[c('combat-requirements/wp55-facility-session-and-restoration.md',114,118,'§3','按两侧位置保存物品身份并按当前位置恢复。')],
 ['枚举每项调用给定转换并把各结果按次序放入新列表。设施用它取得双方物品身份序列。'],
 '当前位置/顺序和保存值已被设施合同充分抽象；无需新的通用transform接口、容器或回调组织。普通回调异常仍按调用栈传播，不从新列表生成推事务回滚。'),
 s('UTIL-09','组合枚举和暂用输出对象','supported_by_current_contract',[g(1,47,'combination iteration'),a('018_Alternate battle modes/002_Battle Frontier rules/002_Challenge_Rulesets.rb',135,189,'existence checks')],[c('combat-requirements/wp54-entry-eligibility-level-adjustment-and-clauses.md',29,41,'§2.2','指定正k的索引组合，短列表零枚举、顺序及首成功停止。')],
 ['成员选择按索引，不按值去重；通用分支反复填同一个暂用输出列表，等长分支直接产原输入列表，k=1产单项列表。'],
 '可报名/参赛存在性查询在每次回调内同步判断，不把暂用列表作为独立历史快照保存；当前布尔业务已完整承接组合内容/顺序。',policy={'id':'COMBINATION-YIELD-IDENTITY','status':'unresolved_policy','known_fact':'作者若保留每次收到的列表引用，通用分支可看到多个引用最终同指最后一次组合；不是每次独立快照。','decision_required':'是否兼容作者保留产出对象身份的旧辅助行为；不能以业务组合规则自动承诺此快照性质。'}),
 s('UTIL-10','常量查找在本地化与枚举序列化中的投影','supported_by_current_contract',[g(104,152,'constant queries/reverse queries'),a('001_Technical/003_Intl_Messages.rb',290,311,'text-domain export'),a('001_Technical/003_Intl_Messages.rb',397,425,'text-domain import'),a('021_Compiler/001_Compiler.rb',764,809,'enum output branches')],[c('generic-kernel/wp08-localization.md',110,117,'§6.3','域常量名/Map/整数节头分派。'),constsp,c('generic-kernel/wp04-pbs-lifecycle.md',153,162,'§5.5','写出枚举名称和值转换。')],
 ['hasConst/getConst虽注释Unused，但本地化导入实际调用，分别失败归false/nil。反查首个同值常量名；严格反查无名可抛错，宽松反查无名返回值的检查文本。导出消息未知域可用不抛错查询并跳过。'],
 '常量反射被业务抽象为稳定域身份和枚举名/整数格式；M01拥有这些主合同。此处明确实际调用，不用Unused注释或首次搜索否定能力，不要求未来语言具有模块常量反射。'),
 s('UTIL-11','旧常量便利入口的完整输入/失败域','unresolved_policy',[g(104,152,'isConst/hasConst/getConst/getID/reverse lookup')],[constsp],
 ['isConst的定义存在性阶段异常归false，后续取值阶段不受同一保护；hasConst缺模块/空常量或查询失败false；getConst对应nil。getID缺模块/空输入nil，未知字符串/符号0，其他输入原样。反查重复常量值取枚举先遇的名，不提供稳定别名优先；缺值可选择抛错或空值，另一入口回检查文本。'],
 '有效领域枚举消费已有承接，但这些通用旧输入/错误哨兵和反射别名顺序不能等同当前GameData严格/宽容查询。事实固定，作者兼容此整套旧输入域仍是明确政策选项。',policy={'id':'LEGACY-CONSTANT-HELPER-PROFILE','status':'unresolved_policy','decision_required':'是否保留nil/false/0哨兵、原样返回和重复值别名选择，而非只保留现行域名与枚举文本结果。','if_preserved':'按输入/结果表写兼容规则，不复制常量/类结构；同义别名顺序仍受给定枚举顺序前提。'}),
 s('UTIL-12','带隐式数据上下文的回调执行','unresolved_policy',[u(335,361,'CallbackWrapper initialize/set/execute')],[c('generic-kernel/wp05-events-extensions-plugins.md',24,43,'§3','显式事件参数分配，不包含此隐式上下文包装。')],
 ['set把整份参数集合引用替换到实例；execute优先给定回调，否则存储回调；参数在当次实参数组上下文中可读，返回回调结果。仅构造未set时，实例参数集合未初始化，遍历阶段会在回调体之前失败；没有统一救援或默认空集合保证。'],
 '不能声称事件参数合同覆盖隐式接收者/数据绑定，也不因未见默认消费者判它无用。该能力高度依赖旧脚本的隐式执行上下文；是否要求作者兼容这种上下文，是尚未选择的兼容目标，不是事实错误或强制未来类设计。',
 ['先set键k值7且回调读取该上下文，可得到7；未set且回调准备写状态，会先失败而不进入该回调。'],policy={'id':'LEGACY-IMPLICIT-CALLBACK-CONTEXT','status':'unresolved_policy','decision_required':'是否保留set前置、隐式数据访问、显式回调覆盖与外部参数集合引用共享。','if_preserved':'补行为和失败前置，不要求新的框架对象或instance_eval；若改成显式数据参数须记录兼容差异。','if_not_preserved':'将这种旧脚本上下文兼容排除，保留WP05显式通知参数合同，不宣称二者相同。'}),
 s('UTIL-13','温度转换的舍入位置','unresolved_policy',[g(63,71,'Celsius/Fahrenheit conversions')],[c('generic-kernel/wp06-time-random-steps-stats.md',5,11,'§1','范围是时间/随机/计步/统计，未声明通用物理温度服务。')],
 ['摄氏到华氏先对9C/5舍入，再加32；华氏到摄氏对5(F−32)/9整体舍入。不是都对最终实数温度取整的同一规则。'],
 '数学事实完全可判定，不能标成未知或靠无调用免审；当前世界天气合同没有数字温度量，是否引入并兼容旧温度辅助是独立作者能力政策，不能由源中有方法自动规定新框架物理单位API。',
 ['C=20→68，F=32→0；摄氏方向舍入在加32之前，负半值的结果不能按先加32再舍入替代。'],policy={'id':'LEGACY-TEMPERATURE-CONVERSION','status':'unresolved_policy','decision_required':'是否将该整数温度变换/舍入顺序纳入作者兼容能力。','if_preserved':'提供数学规则和舍入语义（含负半值），不要求两函数或某种数字类。'}),
 s('UTIL-14','线性插值与业务时线','internal_organization_no_required_revision',[u(394,406,'lerp'),a('012_Overworld/004_Overworld_FieldMoves.rb',438,451,'Flash interpolation')],[c('engine-overworld/wp16-world-rendering-and-visual-transitions.md',56,64,'camera timeline','给定时长/位置的线性进度及到时终点。'),c('engine-overworld/wp59-world-time-weather-field-moves.md',198,217,'field action consumers','场地效果各自前置与动作；显示时线另归世界显示。')],
 ['时长≤0直接终值；正时长且已过时间≤0取起值、≥时长取终值，中间按比例线性插值。可用已过时间或当前时间−起点形成该增量。'],
 '业务合同约束可观察的时线和端点，当前辅助只是实现该数学的共用方式；不把两种调用形状或函数身份当作新API。各调用者提前返回门仍独立，不将所有零时长动作统一化。'),
 s('UTIL-15','验证、空字符串检查及复制/移动的去重归属','supported_by_current_contract',[u(390,392,'nil_or_empty?'),a('001_Technical/001_Debugging/004_Validation.rb',1,31,'validate'),u(141,171,'File copy/move')],[c('generic-kernel/wp05-events-extensions-plugins.md',58,73,'metadata','已提供的name/version/link须有效非空文本。'),c('generic-kernel/wp07-deprecation-appendix.md',28,33,'§4','参数类型及目标存在性错误。'),c('demo-dx/wp75-project-conversion-and-authoring-tools.md',266,273,'§11','复制后删除、目标覆盖和失败前缀。')],
 ['空文本判别实际同时拒绝nil、非String、长度0；验证按类/类集合/响应能力，合并错误后抛出；copy全读源后删旧目标再写，move正常复制后才删源。'],
 '这些均有独立M02能力/当前主业务承接，复用已有界结论，不能在General Utilities再次计作新共享能力或新发现。'),
 s('UTIL-16','文字宽度截取、矩形与颜色的既有边界','outside_assigned_generic_subscope',[u(35,52,'String cut rendering helper'),u(134,139,'Rect contains'),u(173,333,'Color helpers')],[c('generic-kernel/wp07-diagnostics-files-http.md',5,11,'§1 scope','资源选择/播放与业务表现归各领域。')],
 ['这些段在原reading-coverage的混合文件owned_ranges之外；已有源码阅读记录，未作M02全显示合同签署。cut按可容纳字符跳过超宽者；矩形命中右/下边界不含；颜色转换/格式属于显示输入。'],
 '本次六项收口不扩大为完整UI/渲染复审；父整合可把确切来源段投影给对应显示所有者。此为既有所有权界限，不是因未见调用免除事实，也不等待其它模块全审结束。')
]))
write_partial()
# Override only this followup progress. Original review and original five finding objects stay unchanged.
out=json.loads((P/'followup-partial-dispositions.json').read_text());out['complete']=True
out['status_definitions']={'supported_by_current_contract':'current bounded contracts already carry the observable behavior','internal_organization_no_required_revision':'normal declared business behavior adequately abstracts this implementation helper; direct legacy edge policies remain explicit if listed','unresolved_policy':'source facts settled; exact compatibility decision named, no factual contradiction alleged','named_runtime_boundary':'static phase/type premises known; named native behavior not executed','candidate_pending_independent_counterevidence':'new concrete observable contract gap; parent non-proposer counterreview required','outside_assigned_generic_subscope':'pre-existing ownership exclusion, precise source interface forwarded without whole-domain signoff'}
out['new_candidate_ids']=['GR5-M02-006','GR5-M02-007','GR5-M02-008']
out['primary_fact_reading_pending']=[]
out['no_wait_for_other_modules']=True
(P/'followup-partial-dispositions.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
q=P/'followup-partial-progress.json';pr=json.loads(q.read_text());pr.update({'complete':False,'completed_records':[x['id'] for x in records],'all_six_semantic_dispositions_written':True,'next_scope':'finish complete new-candidate schema006–008 and integrity check; no further source-domain reading pending','new_candidate_ids':out['new_candidate_ids']});q.write_text(json.dumps(pr,ensure_ascii=False,indent=2)+'\n')
print('Six records and',sum(len(x['subranges']) for x in records),'finite subranges written')
