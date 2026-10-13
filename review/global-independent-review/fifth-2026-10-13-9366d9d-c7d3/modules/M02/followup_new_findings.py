from pathlib import Path
import json,hashlib
P=Path(__file__).parent
D=json.loads((P/'followup-partial-dispositions.json').read_text())
F='deliverables/final-specification-set/'
RV=D['source_baseline']['commit']; B=D['specification_baseline']['commit']
def src(path,lo,hi,symbol,fact,caller,config='fixed R, no override; bounded premises as stated'):
 return {'path':'Data/Scripts/'+path,'version':RV,'lines':[lo,hi],'symbol_or_data_keys':symbol,'caller':caller,'config':config,'supporting_fact':fact}
def sp(path,lo,hi,sec,txt):
 return {'path':F+path,'version':B,'lines':[lo,hi],'section_or_vector':sec,'current_wording':txt}
T='test-catalog/generic-kernel-wp05-06-07-08-09-10.md'
def make(n,title,srcs,sps,expected,current,gap,pre,counter,normal,boundary,impact,negative,change,accept,deps,cap,shared,root,unknowns,excluded):
 return {'id':f'GR5-M02-{n:03d}','title':title,'module':'M02','severity':'P3','disposition':'unresolved','recommended_disposition_after_independent_review':'required within the bounded facts if confirmed','status':'candidate_pending_independent_counterevidence','reviewer':{'id':'M02 original proposer','model_request':'gpt-6-astra / ultra / service_tier=default / no Fast','actual_parameters':'UNVERIFIED'},'category':'Generic Kernel','source_baseline':dict(D['source_baseline'],root='/Users/dingshinn/Desktop/pokemon-framework-reference/reference/pokemon-essentials'),'specification_baseline':D['specification_baseline'],'source_anchors':srcs,'spec_anchors':sps,'expected_reference_behavior':expected,'current_spec_behavior':current,'gap':gap,'preconditions':pre,'minimal_counterexample':counter,'normal_case':normal,'failure_or_boundary_case':boundary,'impact_on_independent_implementation':impact,'negative_evidence_search':negative,'proposed_spec_change':change,'affected_files':list(dict.fromkeys(x['path'] for x in sps if '/generic-kernel/' in x['path'] or '/test-catalog/generic-kernel-' in x['path'])),'shared_contracts':shared,'acceptance_criteria':{'static':accept,'must_execute':[],'execution_boundary':'Static evidence and specified input/output vectors only. No reference, native-host, model, file-I/O fixture or statistical simulation executed or required to close the specification wording.'},'dependencies':deps,'related_capabilities':[cap],'related_findings':[],'root_cause_group':root,'priority':'P3','batch_owner':'M02 proposal; parent owns non-proposer counterevidence and final integration','history_links':{'finite_input':'followup-partial-triage-input.json','subrange_disposition':'followup-partial-dispositions.json','old_five':'001–005 independently confirmed in parent canonical-findings.json; their complete bounded conclusions reused, original proposer objects preserved','reopens_existing_finding':False,'historical_PASS_used_as_evidence':False},'evidence_level':['SOURCE_STATIC','CURRENT_SPEC_STATIC','DERIVED_VECTOR_NOT_EXECUTED'],'execution_status':'NOT_EXECUTED','confidence':'high for the specified static source transformations; parent must independently assess completeness/requirement scope','unknowns':unknowns+['Parent non-proposer counterevidence and final required/optional decision pending.'],'excluded_claims':excluded+['No default-game reachability is inferred from the helper definition. Absence of a located default caller is not the reason for a missing-capability claim.','No concrete future language API, class structure, source expression translation, implementation or automatic bug-preservation policy is prescribed.'],'user_decision_needed':'No answer needed to finish this finite audit. Future compatibility preservation/correction remains separate from recording fixed source facts.','review_resolution':{'proposer':'M02','local_counterevidence_complete_for_named_scope':True,'independent_reviewer':None,'independent_counterevidence_complete':False,'final_required_revision_signed':False,'decision':'candidate_pending_independent_counterevidence'}}
new=[]
new.append(make(6,'派生游戏时间查询的平均值、保存间隔及读取副作用未进入当前合同',[
 src('004_Game classes/012_Game_Stats.rb',173,192,'play_time; play_time_per_session; time_since_last_save','平均与距保存查询均先读取会刷新锚点的游戏时间；一个除会话数、一个减最近保存时刻；无局部零会话/负结果保护','public statistics queries; no ordinary caller located by bounded exact-name search'),
 src('004_Game classes/012_Game_Stats.rb',59,62,'play_time/play_sessions/time_last_saved','三个值为统计数据，游玩时间允许显式写入、其读取另外更新','statistics record'),
 src('003_Game processing/001_StartGame.rb',48,67,'start_new/load','新游戏/载入设置游戏时间锚点并增加会话数','startup/continue'),
 src('003_Game processing/001_StartGame.rb',111,123,'save','保存前刷新最近保存时刻，IO错误不回退该时间','normal save')],[
 sp('generic-kernel/wp06-time-random-steps-stats.md',25,42,'§3.1–3.2','累计游戏时间/会话数/保存时刻与惰性刷新已定义。'),
 sp('generic-kernel/wp06-stats-directory.md',118,140,'§9–11','三个基础字段及移动和/捕获计数/保存计数派生值，未列平均或距上次保存查询。'),
 sp('generic-kernel/wp09-save-startup-continue.md',109,115,'§5.1','保存时刷新最近保存时刻与失败副作用已有。'),
 sp(T,37,68,'TM01–TM23','有游戏时间锚点、初始化及其它计量向量，无两项派生时间查询。')],
 '先按锚点规则取得当前累计时间T；每会话查询返回T/S，正整数S时结果保持该数值输入的除法语义（正整数T给整数商、浮点T给连续商）；距上次保存查询返回T−L且不夹到0。两项都可能刷新T和临时锚点。',
 '基础T、S、L及T读取副作用已有合同，但两个公开派生查询的存在、组合规则、数值前提和负间隔结果没有当前条款或向量。原稿只在消费者列中出现time_since_last_save名字，未定义结果。',
 '这是统计查询输出的限定缺漏，而非要求把两项增加为持久字段或复刻getter API。',
 ['固定R，无查询覆写；有效统计对象、会话数S为给定正整数，T/L为给定普通数值。','无锚点例不累加；有锚点例明确给出运行时长，避免以真实时钟验证静态预期。','零会话/任意错误类型不承诺统一数值回退；不要求本轮执行原生除法。'],
 {'input':'无锚点，累计时间5.0秒、会话数2、最近保存时间7秒；分别查询平均与距保存。','reference':'平均2.5秒，距保存−2.0秒；没有把负间隔归零。','counterevidence_limit':'累计时间/会话字段存在并不能唯一决定提供何种派生查询或其负值处理。'},
 'T=9.0，锚点10、给定现在13，S=2：平均6.0；累计T变12.0、锚点13。独立同输入且L=5：距保存7.0，同样更新T/锚点。',
 '无锚点且整数T=5/S=2得到整数商2；改T=5.0得到2.5。S=0没有本地保护，精确除零/非有限表现依数值类型与原生运行时保留，不写成总返回0。',
 '独立实现可能漏掉两项可查询度量，使用墙钟差、返回缓存时间、不刷新锚点，或把间隔夹零；这些会使相同统计输入得到不同值和后续累计状态。',
 {'record':'followup-partial-negative-search.json#derived_play_time','current_contracts_read_or_reused':[{'path':F+'generic-kernel/wp06-time-random-steps-stats.md','ranges':'full current B5 text reused; §3/4/5 and TM sections focused'},{'path':F+'generic-kernel/wp06-stats-directory.md','ranges':'full current B5 directory reused;118–140 focused'},{'path':F+'generic-kernel/wp09-save-startup-continue.md','ranges':'§5.1 reused'},{'path':'specs/kernel/wp06-time-random-steps-stats.md','ranges':'§3.1 and prior full read reused'},{'path':F+T,'ranges':'TM01–TM23 reused'}],'result':'全正式文本的精确名与平均会话/距保存同义搜索未命中新合同；已述T锚点/保存值是必要依赖而非这两项输出。','caller_check':'精确源搜索只定位三个相关getter定义；不以此否定作者可调用能力。'},
 '在WP06及派生统计附表补两项数学/状态查询，说明读取先刷新、整数/浮点正常前提、正S条件及无统一零会话/负结果保护；添加有限静态向量，不规定API或新保存字段。',
 ['无锚点T5.0/S2/L7的两个输出可唯一推导。','有锚点的T更新和锚点推进必须随两查询说明。','整数T5与浮点T5.0、负保存间隔作独立对照。','已有累计时间/默认会话1/保存副作用合同保持；异常数值输入另列而不模拟宿主。'],
 ['game-time lazy update','play_sessions','time_last_saved','startup/continue and save'], 'M02-STATS-DERIVED',['KERNEL-TIME','KERNEL-STATS','KERNEL-PERSISTENT-VALUES'],'M02-derived-play-time-query-contract',
 ['Zero-denominator exact native result by numeric type, nonfinite values and host clock behavior were not executed.','No runtime/demo use of these queries is claimed.'],
 ['Does not reopen001–005 or previously accepted old-frame migration/anchor rules.','Does not assert all average queries must use floating arithmetic or all failed saves leave the old saved timestamp.']))
new.append(make(7,'普通随机作者输入的双数值闭区间与参数回退未形成明确合同',[
 src('001_Technical/002_RubyUtilities.rb',366,388,'rand forwarding and Kernel.rand normalization','区间优先、两数值给闭区间、空首参委托次参、其它首参回无参；本包装不创建独立随机状态','author/public random input; existing phone/fishing range consumers'),
 src('013_Items/004_Item_Phone.rb',118,134,'refresh_ready_trainers','20...40领域实例已有正确20–39结果','phone timer'),
 src('012_Overworld/005_Overworld_Fishing.rb',30,51,'pbFishing','整数5..10的领域消费已有','fishing')],[
 sp('generic-kernel/wp06-time-random-steps-stats.md',15,21,'§2','普通随机被概括为标准库调用，范围由参数确定。'),
 sp('generic-kernel/wp06-time-random-steps-stats.md',101,129,'§5.1–5.3','普通调用、播种和记录，缺参数归一分层。'),
 sp(T,37,68,'TM01–TM23','存在种子/状态随机/电话区间等向量，未给双数值/空首参/其它首参对照。')],
 '给定原整数随机源按上界产生合法偏移时，两个有序整数a≤b选择a至b的闭区间；区间首参以自身有效最小/最大成员决定整数域并忽略次参；数值首参配非数值次参沿单上界委托；空首参委托次参；其它类型首参回无参抽样且忽略次参，不将文本解析为数值。',
 '已有电话/钓鱼的具体区间与种子/记录合同；通用“标准库/参数决定”未解释参考层扩充与回退，无法唯一确定作者输入5,7或空,7或文本“5”,1的请求。',
 '缺的是限定参数输入到抽样域/底层请求形态的归一规则。并非所有随机源统一可注入、也不是重开已有AntiRandom/seed规则。',
 ['固定R包装，无扩展覆写；正常两数值用有限整数a≤b，单上界用正整数。','在整数例给定底层合法偏移或普通均匀整数抽样前提；不进行统计测试。','浮点、反向/空/无界/非数值区间的原生接受与异常另列，不用标准库习惯补未证输入行为。'],
 {'input':'作者给定下界5、上界7；底层合法偏移分别0/1/2。','reference':'返回5/6/7，包括上界7；等端点5/5只可返回5。','contract_gap':'普通标准随机上界描述不能确定这是两个数值参数的闭区间扩充。'},
 '既有整数5...8与5..7都选择5/6/7；20...40保持20–39，不改变当前电话合同。',
 '空首参加次参7委托为原单上界7；文本“5”加次参1转无参请求，而非解析5或按上界1强制得到0。区间首参配次参不改变其域。',
 '直接移用通常单上界随机API、忽略第二数字、将上界排除或拒绝/解析文本参数，会改变作者输入的合法结果集和错误/回退方式。',
 {'record':'followup-partial-negative-search.json#random_author_inputs','current_contracts_read_or_reused':[{'path':F+'generic-kernel/wp06-time-random-steps-stats.md','ranges':'full B5 prior reading reused; §2/5.1–5.4 focused'},{'path':'specs/kernel/wp06-time-random-steps-stats.md','ranges':'§5 and prior full read'},{'path':F+'user-interface/wp63-pokegear-map-music-and-phone.md','ranges':'§4.4 positive counterexample already covered'},{'path':F+T,'ranges':'TM01–TM23'}],'result':'精确作者输入/双参数/归一名称搜索无新承接；领域给定区间只反证既有20–39/5–10结果，不能提供通用参数分派。','caller_check':'未定位固定核心双数值调用；这是可暴露作者能力的使用范围限定，不用作无需合同的依据。'},
 '在WP06增加语言中立的整数抽样输入表、两端包含规则及空/非数值首参的参考回退；保持普通源、seed、录像与有状态选择分开。非常规Numeric和区间的原生细节具名保留。',
 ['5/7和5/5闭区间结果与单上界对照明确。','区间优先/忽略次参、数值+非数值次参、空首参、文本首参的请求区别明确。','不宣称默认全游戏采用双参数，也不补造统一拒绝非法输入。','按给定底层偏移作静态向量即可，不要求跨语言随机序列或统计执行。'],
 ['ordinary native random source','phone/fishing domain input ranges','existing seed and recorded-random boundaries'], 'M02-RANDOM-BASE',['KERNEL-RANDOM'],'M02-random-author-input-normalization',
 ['Native behavior for floating Numeric, empty/reversed/unbounded/non-numeric Range and invalid bound objects not executed.','Actual arbitrary plugin usage and underlying RNG distribution/seeding portability not certified.'],
 ['Existing domain-range rules are not missing and are not proposed for replacement.','No global service architecture, literal two-argument API or bug-preservation decision is required.']))
new.append(make(8,'定宽小整数与索引字节协议的读取、写出和短输入规则未提取',[
 src('001_Technical/002_Files/002_FileMixins.rb',1,38,'fgetb/fgetw/fgetdw/fgetsb','整数byte提供方下小端8/16/32位组合，短读保留低位，无数据0，有符号8位折返','exposed file input helpers; conditional integer-byte provider'),
 src('001_Technical/002_Files/002_FileMixins.rb',41,85,'absolute-offset reads/getOffset/getLength/readName','绝对定位改变流位置；8字节偏移/长度条目，首偏移除8为条目数；越界0/空串，零长度不读内容','indexed record compatibility input'),
 src('001_Technical/002_Files/002_FileMixins.rb',88,109,'fputb/fputw/fputdw','低位定宽小端逐byte写入，未本地捕获写错误','integer-to-byte sink'),
 src('001_Technical/002_Files/002_FileMixins.rb',111,149,'File/StringInput/StringOutput binding','绑定形态不证明所有宿主均提供整数byte或可用write；内存each_byte透传getc','host/material boundary')],[
 sp('generic-kernel/wp07-diagnostics-files-http.md',21,52,'§3','文件/归档读取与写入面，未给此定宽与索引协议。'),
 sp('generic-kernel/wp07-diagnostics-files-http.md',136,143,'§10','归档/写入宿主未知，不能代替给定整数byte接口下的源码数学。'),
 sp(T,70,109,'IO/DP','现有IO向量未含小整数编码/短读/索引查找。')],
 '在明确提供整数byte的读取接口下，按小端读取1/2/4byte，无数据0、部分数据保留已有低位，signed8将128..255映为−128..−1。索引格式每条8byte，偏移和长度各32位小端；首偏移除8的整数商给条目数。整数输出保留低8/16/32位，小端依序写；底层失败前缀不自动撤回。',
 '当前合同覆盖整个文件内容/路径/归档流，但没有这类byte→数值、数值→byte或索引数据的兼容合同；不能以泛称读取文件或003流定位合同代替字节协议。',
 '可得源码规定一种对外数据内容及查找结果；若独立实现选择大端、溢出拒绝、短读抛错或另一种索引头，给定输入的可观察结果不同。归档宿主未知是另一层。',
 ['只给普通整数byte0..255提供方和成功定位/写入接口；不真实打开文件或加载归档。','正常索引i非负，数据头/位置可用；不据此承诺任意损坏文件或负索引都有统一结果。','输出输入为整数；写入失败例指定哪一次底层byte写失败且其前次已成功。','StringInput字符提供方、实际File/native StringOutput接合另列，不自动满足整数byte前提。'],
 {'input':'给定byte序列十六进制34 12，调用16位读取；独立对照只有34与无byte。','reference':'4660、52、0。给整数0x123456作16位写出→56 34。','contract_gap':'全文文件读写和归档EOF没有约束端序、低位截断或短输入数值。'},
 '给索引表首记录(偏移16,长度3)、第二记录(偏移19,长度0)，偏移16起内容ABC：条目数2，第一项内容ABC，第二项空串。',
 '索引2等于条目数返回0/空串；零内容长度不再定位读内容。signed8的FF→−1。逐byte写第二次失败时首byte已交付，无自动撤回；负索引与本地/native定位差异不作普遍保证。',
 '独立读取者可能解释出错误长度/偏移/有符号值，或者把同一不完整输入从数值结果改成错误；独立写出者可能改变外部byte和失败前缀。',
 {'record':'followup-partial-negative-search.json#binary_helpers','current_contracts_read_or_reused':[{'path':F+'generic-kernel/wp07-diagnostics-files-http.md','ranges':'full B5 text reused; §3/10 focused'},{'path':'specs/kernel/wp07-diagnostics-files-http.md','ranges':'prior full reading; file/HTTP/diagnostic portions'},{'path':F+'engine-overworld/wp15-resource-matching-and-audio.md','ranges':'§3.1/§6.4.1 earlier source/contract comparison; WAV recognition is a different concrete media format'},{'path':F+T,'ranges':'IO01–IO20'}],'result':'全正式文本的小端/byte顺序/辅助名称/8byte索引等精确与同义入口未给承接；已确认003仅为内存流状态机，不含本byte编码根因。','caller_check':'固定脚本扫描仅定义/混入，未定位核心直接调用；记录为作者兼容可用范围，不据此否定能力或宣布无需规格。'},
 '在WP07补语言中立的定宽byte与索引记录条件式合同，明确提供方必须产整数byte、输出宽度/截断/端序、短读、索引返回及写失败前缀；实际宿主适配另列，不要求File混入或某一StringInput实现。',
 ['8/16/32小端及signed8规则可从数据表独立推算。','34 12/34/空输入，以及超宽/负整数低位输出明确。','首偏移/8、每项偏移和长度、越界与零长度给完整静态向量。','绝对定位与输出失败的已提交前缀分层；整数byte前提不得移给未知字符/native接口。','不扩张或重开003；不要求实际文件、归档或参考执行。'],
 ['file read/write/position substrate','integer-byte interpretation','known reference indexed-record data format'], 'M02-BINARY-IO',['KERNEL-FILE-ACCESS'],'M02-fixed-width-indexed-byte-contract',
 ['Actual native File/StringInput/StringOutput byte and write interfaces, Unicode/encoding units and archive source not executed.','Arbitrary malformed/negative indices or broken native positions not exhaustively characterized.','Whether future target promises old authored-file/helper compatibility is a separate adoption policy; candidate requests accurate bounded reference facts.'],
 ['Does not allege existing Game.rxdata/PluginScripts serialization uses this 8byte index format.','Does not infer all sources called each_byte return numeric bytes, or that these helpers are interchangeable with archive stream operations.']))
# Append only the new three objects. Original five are immutable proposer evidence.
p=P/'findings.json';d=json.loads(p.read_text())
protected=json.loads((P/'followup-partial-progress.json').read_text())['protected_original_finding_objects']
for x in d['findings']:
 if x['id'] in protected:
  assert hashlib.sha256(json.dumps(x,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode()).hexdigest()==protected[x['id']],x['id']
d['findings']=[x for x in d['findings'] if x['id'] not in {y['id'] for y in new}]+new
d['followup_scope']={'input':'followup-partial-triage-input.json','dispositions':'followup-partial-dispositions.json','new_candidates':[x['id'] for x in new],'original_five_objects_preserved':True,'parent_confirmed_originals':D['parent_canonical_reuse'],'execution_status':'NOT_EXECUTED'}
p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
(P/'followup-new-findings.json').write_text(json.dumps({'schema_version':'gr5.review.v1','findings':new,'status':'candidate_pending_independent_counterevidence','note':'Convenience subset; canonical proposer objects are appended in findings.json. No independent acceptance claimed.'},ensure_ascii=False,indent=2)+'\n')
print('Appended new candidates:',[x['id'] for x in new])
