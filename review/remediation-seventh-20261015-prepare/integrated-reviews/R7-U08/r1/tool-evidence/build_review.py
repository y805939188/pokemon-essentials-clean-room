"""Serialize the reviewer's independently authored static findings, not a behavior test."""
import json,hashlib,datetime,os,subprocess
from pathlib import Path
ROOT=Path('/workspace/r7-ir-R7-U08');OUT=Path(__file__).parent.parent;EV=OUT/'tool-evidence'
B='e646432c644dec04d306842cc5a559a29c718fbc';MI='45c80832a41c1b56dcd7e9d93497758cbb7721de';FI='13d76ba61838b13925ba9d41f58a6b047564d926';R='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
P='deliverables/final-specification-set/';A=P+'user-interface/wp67-a-battle-interaction-and-presentation.md';H=P+'user-interface/wp67-b-lifecycle-presentations-and-history.md';UI=P+'test-catalog/user-interface-wp17-63-65-66-67-68-69-70-71.md'
def load(p):return json.loads(p.read_text())
def put(p,j):p.write_text(json.dumps(j,ensure_ascii=False,indent=2)+'\n')
def ident(b):return {'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'git_blob':hashlib.sha1(f'blob {len(b)}\0'.encode()+b).hexdigest()}
def git(*a):return subprocess.check_output(['git',*a])
def clause(p,first,last):
 b=(ROOT/'actual-input/actual'/p).read_bytes();ls=b.splitlines(keepends=True);start=sum(map(len,ls[:first-1]));end=sum(map(len,ls[:last]));return {'commit':MI,'path':p,'whole_file_identity':ident(b),'lines_inclusive':[first,last],'byte_offsets_half_open':[start,end],'clause_identity':ident(b[start:end]),'actual_text':b[start:end].decode()}
ctx=load(EV/'context.json');check=load(EV/'input-byte-validation.json');journal=load(ROOT/'actual-input/integration/applied-clauses.json');contract=load(ROOT/'original/dispatch/delegation/contracts/R7-U08.json')
phase={'SOURCE_STATIC':'INDEPENDENT_CURRENT_BOUNDED_READ','DERIVED_VECTOR':'STATIC_REASONING_ONLY; ALL_NOT_EXECUTED','TOOL_VALIDATION':'BYTE_TREE_SCOPE_TRANSPORT_ONLY','REFERENCE_OBSERVATION':0,'reference_program':0,'independent_complete_behavior_model':0,'game_host':0,'Demo':0,'native_media':0,'real_save_replay':0,'behavioral_vectors_executed':0,'prior_UTIL03':'Historical isolated Ruby2.6 process/10-input fact retained separately; neither erased nor credited to U08.'}
gates=['R7-I must receive this exact independent result and separately register semantic/shared/consumer/history responsibilities.','Formal ACCEPTED is reserved to R7-I; no acceptance is granted here.','Precise historic alias/root reception and remaining direct/transitive responsibilities must be discharged before a separate CLOSED decision.','Effective model/effort/tier/speed remain UNVERIFIED; no effective backend echo is exposed.','Behavioral/runtime/host/Demo/media/real-save equivalence is not established; L01–L14 remain in force.']
def vec(i,premise,why,origin):return {'id':i,'premises':premise,'independent_static_reason_and_expected_prefix':why,'origin':origin,'static_content_assessment':'SUPPORTED_WITH_EXPLICIT_PREMISES','execution':'NOT_EXECUTED','evidence_phase':'SOURCE_STATIC + DERIVED_VECTOR; not REFERENCE_OBSERVATION'}
c04='original/evidence/tasks/R7-C13/inputs/tasks/R7-P02/evidence/inputs/88d6ae6fb2e073916f1802ca4ce2e365707beffaa9a58aa82a25f7a66b60d4d9.raw#/records/6/acceptance_and_regression'
c14='original/evidence/tasks/R7-C13/inputs/delta-j16/tasks/R7-C14/counter-review.json#/decisions/'
hp_common='正常已建立非蛋战斗数据框，有效正整数总HP；无插件、覆写、外层中止或中途变更，前序资源/数字/时钟更新正常；只观察给定经过时间的逻辑颜色请求。默认Pikachu基础HP35、L50、HP IV12/EV0；固定R的IV/EV禁用配置均false，HP=floor((70+12)*50/100)+50+10=101。'
hall_common='直接普通登记入口（非PC浏览）；初始历史[]、累计编号0；一只合法健康非蛋Pikachu，默认ALLOW_EGGS真、上限50；无插件或竞争修改。基础显示准备和物种查询正常；只观察外层逻辑BGM请求及内存记录，后续成功另以逐步正常返回为条件。'
exp_common='普通交互战斗玩家侧单席位、已建立且可见的经验条；合法非蛋Pikachu Medium L10，区间1000到1331、正宽331、实际经验先写入；无已有满槽闪光计时，无插件、中止或并发覆写。正常组要求前序对象/资源/时钟/SE返回；只判请求参数。'
pur_common='默认净化室包装，无插件补充更新方法、无竞争修改；唯一合格非Lugia组的中心为合法健康非蛋Pikachu L10/E1000、Shadow真/Hyper假、心量G0、暂存S500、有效六项V0和合法已知招/首招，外圈一只普通有效个体；其他组空。前序资格/资源/消息/招式/EV/统计正常，通常队伍或盒有位。合法已保存状态夹具，不声称默认Demo自然产生此状态。Medium表L11下限1331、L12下限1728，恢复floor(4*500/5)=400，目标1400。'
records=[]
def record(id,scope,clauses,counter,normal,cancel,failure,preserve,direct,transitive,history,vectors):
 return {'record_id':id,'verdict':'PASS_SCOPED_ACTUAL_INTEGRATION','scope':scope,'actual_MI':MI,'actual_MI_tree':'6480ffe3df49bd9776c719f3c9be1c13618fdb0a','actual_formal_subtree':'8403869aaeb4726518414b409b3808c3c0780e65','actual_clauses':clauses,'seven_group_independent_review':{'identity_and_precise_claim':'REVIEWED against original fixed full contract and nonauthor counterproof','evidence_and_premises':'REVIEWED; bounded current source and normal/control/failure/partial-state cases below','minimum_revision_and_preserved_scope':'SATISFIED only as scoped below','verification_vectors':'ALL_ORIGINAL_VECTORS_REVIEWED_STATICALLY; NOT_EXECUTED','paths_and_shared_reception':'Exact MI full files read; U02 shared UI independently aligned where applicable','dependencies_and_history':'Explicitly assessed below; empty scheduling lists do not discharge domain obligations','stages_and_gates':'No runtime/configuration/global/acceptance/closure upgrade'},'counterproof_and_response':counter,'paths':{'normal':normal,'cancel_or_rejection':cancel,'failure_and_partial_commit':failure},'preserved_scope':preserve,'dependencies':{'author_record_scheduling_edges':{'direct':[],'transitive':[],'qualification':'Original accepted contract contains no named record-to-record scheduling edge. This does not mean no domain dependencies.'},'direct_consumers':direct,'transitive_consumers':transitive,'current_review_disposition':'Named bounded consumers have no conflict with this precise MI correction; no unread broader consumer is automatically approved.','remaining_gates':gates},'historical_reception':history,'vectors':vectors,'blocking_content_findings':[],'phases':phase,'formal_ACCEPTED':False,'CLOSED':False}
records.append(record('GR7-M13-001','仅战斗数据框HP颜色阈值及四条具名静态目录向量；不扩到队伍/摘要静态条或个体图标。',[clause(A,247,247),clause(UI,399,402)],
 '已重读C04原反证和M13原提案。真实HP整数不能反证显示补间小数；数字绘制中的临时取整不写回动画h。T101也不是非法数值：固定Pikachu基础HP/等级/IV/EV及默认设置支持101。MI明确先红后黄、只对T取floor，不把h、最终HP或精确T/2、T/4代入。',
 '实际HP先提交；数据框从旧值补间到新值，目标1秒，正常场景等待其结束；端点回到真实整数HP。',
 '数据框没有独立玩家取消出口；外层可中止战斗的BACK属于另一入口。',
 '前序数字/资源/时钟/宿主失败可阻断呈现；已提交实际HP不因此撤回，不保证补画或统一恢复。',
 ['宽度继续按比例与偶数像素舍入，数字独立临时取整。','1秒目标、正常等待、Battle Effects Off仍有HP动画；K35原义保留。','整数端点、队伍/摘要静态条、状态/个体图标与战果不扩修。'],
 ['R: DataBox hp getter L163–187、数字L206–216、refresh/update L301–347/L403–413；lerp L394–406。','R: Battler_ChangeSelf L5–34实际HP先写；Scene_PlayAnimations L219–232等待；Battle_Scene L79–119推进数据框。','MI: WP67-A §9.2及UI K35/HP01–04。'],
 ['MI完整WP39参与者/数据框边界及WP41换人/位置/逃走前提已读，不能把外层中止套成HP事务回滚。','固定Pokemon HP公式L1085–1127、PBS Pikachu L629–655及Settings L141–151支持合法夹具。'],
 {'bounded_result':'保留B17/U05/R4既有正确控制；本次读取未把它们当作奇数HP补间色请求的证明。','not_granted':'全历史同根/别名穷尽UNVERIFIED，旧整域PASS不继承。','receiver':'R7-I最终历史去重和关闭登记。'},
 [vec('C04-HP-A',hp_common+'独立观察51→50的t=.5和t=1。','h50.5大于floor(101/2)=50，绿；到端50为黄。实际HP已经50不能替代显示h。',c04),vec('C04-HP-B',hp_common+'改为26→25，t=.75和t=1。','h25.25大于floor(101/4)=25且≤50，为黄；到端25为红。',c04),vec('C04-HP-C','正常无干扰静止框，独立T100时h50/25、T101时h51/50/26/25。','依次黄/红；绿/黄/黄/红，静止整数颜色不改变。',c04),vec('C04-HP-D',hp_common+'分别开启/关闭数字，并独立设Battle Effects Off。','数字临时整数不改变h和选色；Off仍请求1秒HP补间并等待。比例宽度/偶数舍入和先提交HP保持，异常不承诺回滚。',c04)]))
records.append(record('GR7-J16-001','只校正WP67-B登记相对非空BGM逻辑请求和逐成员视觉的次序。',[clause(H,141,141)],
 '重读C14最强反证“演出只指成员视觉”：全文L17明确包含音乐，L143的首项又是BGM，不能默默排除。MI L141现以逐成员视觉为参照，并明确非空BGM请求正常返回后才登记；正确L22继续保留。媒体未实测只限制发声结论，不能抹去逻辑调用顺序。',
 '基础准备→非空BGM逻辑请求→正常返回后克隆/追加/编号/按上限裁剪→成员创建及淡入→视觉动画循环；空音乐跳过该请求。',
 '登记段没有玩家取消分支；PC浏览BACK另属独立入口。空音乐是跳过请求，不拒绝登记。',
 'BGM请求抛错不返回时尚未调用记录登记；此前资源与音频消费者的逻辑状态可已改变，不保证回滚、清理或保存。',
 ['克隆、默认蛋收录、正/负/0上限及每次仅删一届、累计编号不回退保持。','上限0仍追加并编号后裁空；PC可见门与空记录成员创建失败边界保留。','无自动存档、片尾或取消；记录先于成员视觉保持。'],
 ['R完整HallOfFame L1–494：准备L67–74、登记L120–131、创建L178–211、动画L310–318/L347–401、包装L436–440、PC L452–460及查询L471–478。','R Audio_Play L1–115及Game_System L1–100：逻辑状态/资源判断/底层Audio请求并非实际发声认证。','MI完整WP67-B §2/§7与UI LC-L22/23/24/33。'],
 ['UI生命周期历史消费者和PC编号/数组位置相互独立；表中空记录边界没有因次序修订消失。','原作者时点候选标签通过root当前接收入口解释，不能当本次正式接收。'],
 {'bounded_result':'L22记录先于滑入原本正确；L33上限0及编号/PC边界保留，不合并成新根。','not_granted':'C14有限标题搜索不能证明全历史无同义根；根最终全局别名核对仍待。','receiver':'R7-I实际接收及历史责任登记。'},
 [vec('C14-HOF-A',hall_common+'默认非空音乐，观察首逻辑请求入口。','历史仍[]、编号仍0；登记调用尚未发生。',c14+'0/acceptance_and_regression'),vec('C14-HOF-B',hall_common+'该BGM请求和克隆/后续构造均正常返回。','登记产生一届克隆和编号1，再进入逐成员视觉链；不等同落盘。',c14+'0/acceptance_and_regression'),vec('C14-HOF-C',hall_common+'独立仅改为空音乐配置，登记及后续正常返回。','跳过BGM请求，仍登记并先于成员视觉。',c14+'0/acceptance_and_regression'),vec('C14-HOF-D',hall_common+'条件化BGM请求内部异常且未返回。','尚未到登记；资源或音频侧状态可能已有前缀，不保证清理/回滚。',c14+'0/acceptance_and_regression')]))
records.append(record('GR7-J16-002','WP67-A L196和L248仅由“闪白”改为“闪光”；不采用可选RGBA正文/像素断言。',[clause(A,196,196),clause(A,248,248)],
 '重读C14关于“闪白只是亮闪近似/像素未知”的反证：规格两处无近似限定，源只支持蓝青RGBA请求，不能要求白色。中性闪光撤回无证色相，且不把未执行像素改成蓝青色。旧J16经验driver L234–254实为伤害动画；本次独立实读并使用实际L283–293，旧错定位原字节保留。',
 '实际经验先写→显示补间→首次满槽设置闪光计时→停旧SE/满槽SE→框及逐个未释放子精灵的闪光请求→后续更新到期结束。',
 '组件无独立玩家取消；外层BACK另论。无条/无变化/零宽区间不启动，不能据成功夹具推所有入口都会请求闪光。',
 'SE失败可发生在首闪光前；某子精灵请求失败可只留下已交付前缀，已写经验及显示推进不自动回滚，不保证全部子精灵或宿主像素。',
 ['经验补间按1.75秒比例、满槽名义.2秒、音效和等待门保持。','实际经验先提交、逐级升级/学招顺序、无经验条立即完成、Effects Off仍播放保持。','K22/K35无白色断言且保留；GR7-M13-001 HP颜色与M13-002可选Shadow消息范围独立。'],
 ['R DataBox L1–413，尤其经验启动门L191–204、满槽L350–386、update L403–413。','R实际经验driver Scene_PlayAnimations L283–293，Battle_ExpAndMoveLearning L162–224（L194写经验/L195请求场景），Battle_Scene L79–119及lerp L394–406。','MI WP67-A升级与HP/经验段、UI K22/K35。'],
 ['Pokemon/Shadow经验消费者及完整WP23/经验目录已读；本次文字修订不改经验公式、Shadow暂存、逐级学招或净化恢复。','同一WP67-A的HP阈值修订与本项两处中性色词并存，各自原范围不互代。'],
 {'bounded_result':'不复活白色请求；旧错误driver留作失败史而非支持；K22/K35及M13原可选关系保留。','not_granted':'旧全文PASS/标题检索不形成全历史唯一根证明。','receiver':'R7-I全局别名及准确历史接收。'},
 [vec('C14-EXP-A',exp_common+'显示从0/331增到331/331，首次满槽。','先有满槽SE，再给框及正常未释放子精灵RGBA64/200/248/192、名义.2×帧率请求；仅请求参数，不认证像素。',c14+'1/acceptance_and_regression'),vec('C14-EXP-B',exp_common+'仅增100/331至E1100。','未到满槽，故无满槽闪光；既有增益声音及结束门保留。',c14+'1/acceptance_and_regression'),vec('C14-EXP-C','独立多席位或对方数据框无经验条，其他场景入口前提有效。','无条门直接完成，不产生本项满槽请求。',c14+'1/acceptance_and_regression'),vec('C14-EXP-D',exp_common+'条件化满槽SE或某个闪光请求内失败。','SE异常可阻断所有闪光；框/某子精灵已收到时只保留该前缀，后续子精灵不保证；不回滚已写经验。',c14+'1/acceptance_and_regression')]))
records.append(record('GR7-J16-003','仅UI LC-L13的入口与条件后续；沿既有跨级失败边界，不新增净化根因/领域规则。',[clause(UI,444,444)],
 '重读C14“全文WP23/L16/L17已足以继承成功前提”的反证。目录每行为输入→预期，存在合格组既不保证统一净化正常返回，也不保证有下一组；一组合格且全正常仍无下一组询问。MI现在显式引用L16/L17并逐段要求正常返回，同时保留双满提示返回亦清中心。',
 '入口见过标志→建立场景→合格组快照→开组/刷新→统一净化；只有净化正常返回才通用存放，存放正常返回才清中心；列表仍有下一组合格才询问。',
 '开场不先取消；选择器取消另属L15。跨级默认失败早于学招/进化/昵称取消；同级拒昵称不撤回已提交前缀；拒下一组只停止将来组。',
 '默认跨级在首能力窗更新调用缺失处失败，早于USE确认。Shadow/Hyper清除、缎带/已执行招式/首招、V恢复并清V/清S、L11下限经验/能力/亲密度等前缀保留；未精确写1400、未命名/存放/清中心，中心仍同对象。更早资源失败可更早停止；不承诺宿主错误呈现/退出/回滚。',
 ['WP23主文/附表、WP67-B §6.3和LC-L16–19原义保持。','SH38/39/43/44/45保持各自到达前提；旧RATTATA S416→目标1332对照不被Pikachu S500→1400替代。','双满存放正常返回仍清中心，不偷换为存放成功；正常UI选择链/特殊负位置/直接调用三层不混同。','不决定未来兼容缺更新错误的政策，不猜造更早canonical GR-ID。'],
 ['R PurifyChamber完整包装L348–628及到L648，资格L218–263，开场L1115–1135/包装L1277–1308。完整类有显示/确认/刷新而缺所需更新转发。','R统一净化ShadowPokemon_Other L17–58，成长Item_Utilities L132–221（等级先写、首窗口L206–221更新先于确认），Pokemon等级setter L173–218，GrowthRate L1–93及PBS合法个体。','R通用存放Utilities_Pokemon L1–77（双满L17–31正常返回），调用者存放后清中心L583–584；遗迹石包装L106–141提供空更新回调。','MI完整WP23两篇、WP67-B、pokemon目录与UI LC-L13/16–19。'],
 ['Shadow字段/暂存V/S和经验增长的共享对象消费者已核；不能把阶段前缀包装成统一事务。','同一UI目录U02消息/输入贡献没有给L13新增全局正常返回前提；其51条追加仍按各自入口和异常边界。','完整scope-statement及WP34/既有孵化继承消费者未因本目录后缀修订得到新的整域PASS。'],
 {'bounded_result':'沿WP23 §6/§8.3、WP23-data L54–55、SH43–45、WP67-B L23/L125–128及LC-L16/L17原边界；SH38/39与LC-L18/L19正常后续相容。','earlier_root':'现有有限材料未解析更早canonical编号；不造ID、不新增一个跨级缺方法领域根因。','not_granted':'原资格、政策和旧全域审查不重开；更早别名接收仍由R7-I登记。'},
 [vec('C14-PURIFY-A',pur_common,'目标1400属L11；等级setter先置L11下限1331、重算/亲密度前缀，首能力窗口缺更新失败，精确1400/命名/存放/清中心未到，中心同对象部分修改。',c14+'2/acceptance_and_regression'),vec('C14-PURIFY-B',pur_common+'独立只改S0，前序和存放正常返回，拒昵称，一组。','同级经验保持1000而重算，不进缺方法等级窗；可存放/清中心；列表无下一项故不询问。',c14+'2/acceptance_and_regression'),vec('C14-PURIFY-C',pur_common+'独立给两组合格S0，第一组前序/存放正常返回，随后拒switch sets。','第一组已经清中心；第二组保持待净化，关闭停止；不回滚第一组。',c14+'2/acceptance_and_regression'),vec('C14-PURIFY-D',pur_common+'改S0且确实到达通用存放，独立队伍和盒双满，提示正常返回。','通用存放没有成功入队/盒，但调用者随后仍清中心。MI的条件是正常返回，未误收紧为成功。',c14+'2/acceptance_and_regression'),vec('C14-PURIFY-E',pur_common+'同跨级数值改遗迹石包装，资格和窗口后续正常。','该Screen有空更新回调，不在同一缺方法点失败；只有等级辅助正常返回后才写精确1400，后续取消/命名依实际门。',c14+'2/acceptance_and_regression')]))
assert len(records)==4 and sum(len(x['vectors']) for x in records)==17
shared=[]
for f in journal['files']:
 if 'R7-U08' in f['contributors']:
  shared.append({'path':f['path'],'contributors':f['contributors'],'actual_full_file_read':True,'identity':ident((ROOT/'actual-input/actual'/f['path']).read_bytes()),'hunks':[h for h in f['hunks'] if h['batch_id'] in ['R7-U08','R7-U02']]})
shared_assessment={'U02':{'fixed_candidate':'84e2cca132ada38405657f19cbbd3d6891d4794f','fixed_independent_approval':'44276c5ae69ef0970a98464a5a9e6ff7eb1c1f1c','read':'Full actual UI catalog L1–1111; exact U02 report/per-id and eligibility; candidate spans and full identities checked.','contribution':'51 SS/IN/DB/BT/AX rows at EOF; U08 contributes four HP rows after K35 plus one LC-L13 replacement. All present once; disjoint B positions.','compatibility_reason':'U02 entry-specific input/message exit and exception boundaries do not supply an unstated global successful-purification premise. Screenshot/native mapping append is independent of HP/experience/Hall semantics; no row overwritten, duplicated or lost.','receiver':'R7-I CG06 exact shared reception; this review supports U08 compatibility/preservation only.','limits':'No fresh semantic PASS for U02 IDs. Its CC04 actual registration/host-query bridge NOT_READ, devices/backend NOT_EXECUTED, complete1923-record/76field48record/priority semantics NOT_SIGNED remain.'},'all_current_journal':'All56 hunks across24 targets replayed from B and their exact candidate spans. Audit/matrix same-EOF U01→U02 order checked; engine U01/U13 and DX U11 spans preserved mechanically, no new out-of-scope semantic PASS.','administration':'Two827-byte audit/matrix appends link to actual public-reception.json at MI. Errata modifies only status and two reception subfields; no ACCEPTED/CLOSED. Candidate stage labels remain time-qualified and exact frozen candidate paths are used.','previous_five':'Five exact accepted-MI files are byte-identical at current MI; full mandatory contents and relevant U08 consumers separately read. Mechanical preservation is not a new semantic PASS for those older IDs.','procedural_waits':'U03/U07/U10 remain WAIT, not integrated. This does not imply no source-domain dependencies.','future':'No assumed future U03/U10 contribution; optional7/facets2/no-required1/policy2 not adopted; 27items/13batches and old56/92 retained.'}
result={'schema':'r7.u08.independent-actual-integration-per-id.v1','batch':'R7-U08','round':'r1','reviewer':ctx,'fixed_dispatch':'c64774c60d91e522cb515ef71e3e9d4ea6b4712c','fixed_B':B,'fixed_R':R,'actual_MI':MI,'actual_MI_tree':check['git_trees'][MI],'actual_formal_subtree':check['formal_subtrees'][MI],'input_freeze_FI':FI,'FI_tree':check['git_trees'][FI],'records':records,'shared_files':shared,'shared_assessment':shared_assessment,'overall':'FOUR_PASS_SCOPED_ACTUAL_INTEGRATION_ONLY','behavioral_vectors':17,'all_behavioral_vectors':'NOT_EXECUTED','formal_ACCEPTED':False,'CLOSED':False,'configuration':ctx['effective_configuration'],'L01_L14':'RETAINED_FULLY: tool-evidence/retained-L01-L14.json','denominators':{'required_items':27,'batches':13},'nonmandatory_adoption':'NONE','phases':phase}
put(OUT/'per-id.json',result)
ledger=[json.loads(x) for x in (EV/'reading-ledger.jsonl').read_text().splitlines()];full=[]
for p in sorted((ROOT/'actual-input/actual').rglob('*')):
 if p.is_file():
  rel=p.relative_to(ROOT/'actual-input/actual').as_posix();matches=[x for x in ledger if x['path']==str(p) and 'lines' in x];n=len(p.read_bytes().splitlines());covered=set()
  for m in matches:covered.update(range(m['lines'][0],m['lines'][1]+1))
  assert set(range(1,n+1))<=covered,(rel,n)
  full.append({'commit':MI,'path':rel,**ident(p.read_bytes()),'total_lines':n,'recorded_ranges':[m['lines'] for m in matches],'reading_tool_pids':[m['tool_pid'] for m in matches],'reviewer_attestation':'Full emitted content reviewed, with truncated gaps specifically re-read; not inferred merely from hashes.'})
assert len(full)==12
source_scopes=[{k:v for k,v in x.items() if k in ['path','file_bytes','file_sha256','git_blob','lines','tool_pid','utc']} for x in ledger if '/original/inputs/reference/' in x['path'] or x['path'].endswith('/bootstrap/001_Settings.rb')]
receipt={'schema':'r7.u08.actual-review-input-receipt.v1','serialized_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'serializer_tool_pid':os.getpid(),'reviewer_context':ctx,'fixed_inputs':{'dispatch':{'commit':'c64774c60d91e522cb515ef71e3e9d4ea6b4712c','path':'review/remediation-seventh-20261015-prepare/integration/wave2/v1/dispatch/R7-U08-R7IR.md',**ident((ROOT/'bootstrap/R7-U08-R7IR.md').read_bytes())},'original_full_contract':{'commit':'f622356f3beb9e84ea8cff9db07c7fb382565d3f','path':'review/remediation-seventh-20261015-prepare/delegation/contracts/R7-U08.json',**ident((ROOT/'original/dispatch/delegation/contracts/R7-U08.json').read_bytes()),'full_four_seven_group_contracts':'READ before review; bootstrap direct tool outputs are platform-only, not retroactively assigned local PID receipts.'},'FI':{'commit':FI,'tree':check['git_trees'][FI],**check['FI_identity']},'MI':{'commit':MI,'tree':check['git_trees'][MI],'formal_tree':check['formal_subtrees'][MI]},'B':{'commit':B,'tree':check['git_trees'][B],'formal_tree':check['formal_subtrees'][B]},'R':{'commit':R,'tree':check['reference_tree']},'candidate_author':{'commit':'d6e07340aa14eb8b45728020cad018a22d7559b2','tree':check['git_trees']['d6e07340aa14eb8b45728020cad018a22d7559b2']},'candidate_reviewer':{'commit':'d86d1db844c4f8ad0ed92b6a811b971e5057c967','tree':check['git_trees']['d86d1db844c4f8ad0ed92b6a811b971e5057c967']}},'restoration':{'root':str(ROOT),'original':{'members':39,'bytes':7698787},'actual':{'members':204,'bytes':3837793},'receipt_files':[p.name for p in EV.glob('*recovery-receipt-*.json')],'qualification':'Actual restored and independently hash/blob/tree checked in this container; no assumed shared directories; bounded snapshots not runnable checkouts.','plans':'tool-evidence/{original,actual}-restore-plan.json'},'full_actual_reads':full,'bounded_reference_reads':source_scopes,'original_non_author_evidence':{'C04':'Raw /records/6 fully read using derived diagnostic with exact raw-member byte binding retained; no author-only substitution.','C14':'Full counter-review.json27323bytes/SHAf912ce3080054f9f436d516b3ae00154f7ecbd94c116a29a40111ce23eb5a5e2 and all3 decisions/13vectors read.','M13_original':'Original proposal read independently from fixed raw /records/15/original_proposal, plus accepted seven groups.','J16_original':'Three original proposal files retain same91439-byte/SHA9740561f... payload. C14 earlier89933-byte/SHA801a6f78... freeze is a different preserved time; wrong234–254 locator is not used as experience evidence.'},'candidate_and_shared_receivers':shared_assessment,'byte_and_tree_validation':'tool-evidence/input-byte-validation.json (all243 restored members,131 formal identities,26/105 counts,5prior files,56hunks/24targets,3root administration adjustments)','source_extra':'tool-evidence/extra-fixed-source-input.json; fixed Settings plus read-only R Git metadata fetch','AGENTS_and_skills':{'AGENTS':'MI full297lines read; clean-room functional/logic/behavior specification only, source readonly, no implementation/translation.','git_dot_agents':'No .agents paths at fixed B/MI/dispatch; tree checks recorded.','workspace_dot_agents':'Inspected /workspace/.agents; no applicable readable skill files were present.','applied_local_skills':[]},'tool_history_and_provenance':{'001_002':'Successful exact --resume restorations; original initial HTTP restoration receipts preserved too.','005':'Mechanical validator first failed because disconnected candidate commits were not fetched.','006':'Exact readonly candidate commit fetch succeeded.','007':'Validator initially treated declared root errata metadata rewrite as a verbatim candidate hunk; failed as recorded.','008':'After separating admin JSON, validator expected wrong metadata key name reception_phase; actual field is reception. Failure retained.','009':'Final validator verifies only status and candidate_review/shared_integration reception changes; all fixed identities/spans pass. No semantic PASS derives from this exit0.','010':'Current real environment identity, fresh fixed Settings HTTP receipt and evidence copies captured.','bootstrap_gaps':'Initial dispatch/guide/tool/contract reads, initial fetch/worktree setup and some diagnostic commands have platform-visible I/O without full local UTC/PID/stdout/stderr records. Not backfilled. Original author/reviewer bootstrap/read-truncation/failed-pointer/build/fetch logs remain in the restored204-member input; no claim of gap-free historical provenance.','earlier_API_failure':'Fixed-R GitHub metadata API CONNECT403 retained as limitation; read-only Git exact-R fetch/tree check resolved identity.','model_configuration':'All effective values UNVERIFIED; no auth/quota probing.'},'phases':phase,'L01_L14':'Full exact retained-L01-L14.json preserved; no limitation silently closed.','unmet_gates':gates,'write_scope':{'branch':'codex/r7-ir-u08-20261015-r1','base':B,'only_directory':'review/remediation-seventh-20261015-prepare/integrated-reviews/R7-U08/r1/','formal_candidate_main_tag_writes':0},'delivery_protocol':'Ordinary commit/push only. First complete remote readback recorded inside evidence, followed by evidence seal commit and final complete immutable-commit remote readback outside the committed tree to avoid recursive self-hashing. Final seal commit/tree comes from actual Git output, never guessed.'}
put(OUT/'review-input-receipt.json',receipt)
report=f'''# R7-U08 r1 独立实际整合复审

本次仅对下列四项在固定 MI 的实际累计字节签发 **PASS_SCOPED_ACTUAL_INTEGRATION**。未发现本限定范围的内容阻断项；不授予其它 ID、完整领域、运行等价、正式 ACCEPTED 或 CLOSED。

| ID | 本次结论 | 实际条款 |
| --- | --- | --- |
| GR7-M13-001 | PASS_SCOPED_ACTUAL_INTEGRATION | WP67-A L247；UI HP01–04 L399–402 |
| GR7-J16-001 | PASS_SCOPED_ACTUAL_INTEGRATION | WP67-B L141 |
| GR7-J16-002 | PASS_SCOPED_ACTUAL_INTEGRATION | WP67-A L196、L248 |
| GR7-J16-003 | PASS_SCOPED_ACTUAL_INTEGRATION | UI LC-L13 L444 |

真实可见 thread/context：`{ctx['visible_thread_id']}`，由当前 CODEX_THREAD_ID/CODEX_SESSION_ID 实读，与派发排除的19个可见标识及本批作者、候选审者不同。未创建子任务、agent、子会话或辅助模型调用。内部 opaque ID 未暴露的资格继续保留；角色名不作身份凭据。本报告不是创建 API 回执。请求配置 gpt-6.1-sol / ultra / default 普通速度、禁 Fast；实际 model/effort/tier/speed 全部 **UNVERIFIED**。

## 固定输入与实际恢复

- 派发：c64774c60d91e522cb515ef71e3e9d4ea6b4712c，已先全文读取；原完整七组合同 f622356f3beb9e84ea8cff9db07c7fb382565d3f。
- B：{B}；正式子树 ebbe29f2bc88cd17de7072bf440c6fa8c8c7089c。
- R：{R}；tree 7589c800b61ba13a13040ed0d686979b80a84fd0，只读。
- MI：**{MI}**；workspace tree **6480ffe3df49bd9776c719f3c9be1c13618fdb0a**；正式子树 **8403869aaeb4726518414b409b3808c3c0780e65**。
- FI：**{FI}**；tree **6747a584b91c86acd4771c1a6dee93260602106f**；integrated-input.json 93252bytes / SHA256 2e7ca9336bae51edc9d63ea7e8a1a411497071a6a4294bca24d3a05b3ae4ee7d。
- 作者候选 d6e07340aa14eb8b45728020cad018a22d7559b2 / tree ed37cf1d27414f8f7411f079f1f717e55f3213a3；候选审查 d86d1db844c4f8ad0ed92b6a811b971e5057c967 / tree 1fa39ad8dc2a17165c90e943e7601626d17197eb，仅为对照和准入证据。

本容器按已全文读过的固定恢复工具/指南实际恢复原输入39文件/7698787字节、实际输入204文件/3837793字节，并独立重算全部文件身份。实际计划105567字节/SHA256 c459dd53046aa97a3c9ef66e925838c4ae50e741d02f0eeb249a1fb3302c78b4。没有假设跨容器共享目录；actual/是MI，candidate/和baseline/各自仅作对照。完整读取合同列出的12份实际文件（含完整1111行共享UI目录），源码只作具名有界新读。AGENTS全文已读，固定B/MI/派发无.agents条目，本地未发现适用技能。未运行候选/审者脚本、参考程序或native程序；仅执行审计工具和事先完整读过的指定恢复工具。

## 逐项独立内容判断

**M13-001。** 当前h可为补间小数，T是正整数。MI按h≤floor(T/4)红，否则h≤floor(T/2)黄，其余绿；没有先把h取整或用已提交最终HP。Pikachu L50、基础HP35、HP IV12/EV0在固定默认设置下合法得到101。51→50在.5秒h50.5为绿，到端50黄；26→25在.75秒h25.25黄，到端25红。整数控制保持。数字绘制临时整数没有写回h，Off仍播放和等待，宽度比例/偶数舍入、1秒目标和领域HP提交不改。C04关于真实HP整数、数字取整和夹具合法性的最强反证均已按源逐层核。无组件取消；前序呈现异常不回滚HP。B17/U05/R4不作本次全域PASS或全历史去重依据。

**J16-001。** 完整Hall、音乐包装和Game_System消费者支持基础准备后先交付非空BGM逻辑请求，正常返回才克隆/登记/编号，再成员创建和视觉。WP67-B L17将音乐纳入演出、L143首项BGM，因此原“先于演出”不能默认为排除音乐。MI明确“先于逐成员视觉”和请求返回门，空音乐跳过请求仍可登记。C14四向量分别保留请求入口[]/0、正常返回后一届/1、空音乐、请求异常未到登记的状态。默认蛋收录、正负0上限/每次只删一届、编号不回退、PC可见与空记录失败、无取消/自动存档/片尾边界保持；正确L22无需改写。逻辑请求不等于实际发声。

**J16-002。** 两处仅“闪白→闪光”，不强制可选RGBA写入或最终像素。实际满槽在SE请求之后向框及未释放子精灵交付RGBA64/200/248/192和名义.2秒参数，足以撤回白色色相要求；宿主混色未知不支持把白色反向认证。已独立读实际经验driver283–293，原作者错引234–254（伤害）保留为失败史。1.75秒比例目标、满槽音效/等待、经验先写/逐级顺序、无条直接完成、Off和K22/K35保持。SE或子精灵异常只保留到达前缀，不承诺全部交付或经验回滚。

**J16-003。** L13现在只陈述入口和条件后续：合格快照→开组/刷新→统一净化；依L16/L17，净化正常返回才存放、存放正常返回才清中心；双满提示正常返回仍清，尚有下一项才问、拒绝只停后续。存在合格组不能单独推出完整后缀。一组S0且全正常也无下一组询问。默认合法Pikachu L10/E1000/G0/S500目标1400/L11；默认包装首能力窗更新缺操作，先写L11下限1331及已到达的Shadow/缎带/招式/EV/清V清S/能力亲密度前缀，尚未精确写1400或命名/存放/清中心。同级S0和遗迹石空更新回调作为正常对照。WP23两篇、WP67-B §6.3、LC-L16–19、SH38/39/43–45保持；旧RATTATA416→1332向量也保留。这是测试精度修订，不新增净化领域根因，不决定未来兼容政策，不猜造旧canonical编号。

17条原向量的完整前提、原反证定位、当前独立静态理由与阶段逐条见[per-id.json](per-id.json)：C04-HP-A–D四条、C14-HOF-A–D四条、C14-EXP-A–D四条、C14-PURIFY-A–E五条。**全部NOT_EXECUTED**；没有用hash、旧PASS、作者自审或审计退出0代替上述内容判断。

## 共享、依赖与历史接收

本批三个完整实际目标的字节身份如下；各ID的精确条款字节offset、长度/SHA/blob另列于per-id.json。

| 实际文件 | 字节 | SHA256 | Git blob |
| --- | ---: | --- | --- |
| WP67-A | 78445 | f746751b7be6ce908ac374ae3f12baa6c1eadff102f6c1c2b294f8c79e996e44 | b4d64fb7048aba62bef186195f4e3c588037b41d |
| WP67-B | 43347 | 07d62e44f455fc04ebb9df64aefc323525d40354c3c69de2acb3f60cf6988eca | 41814321f0202dfdde6a15fda3442bb2eae33b82 |
| 共享UI目录 | 181927 | c558911e2a4eabd4c98e58a6975016db2d975b0f50c08e8668780f865b034f24 | 0c2a3f4689f0c41aa422d738c1089e5cc2c62d76 |

U02固定候选84e2cca132ada38405657f19cbbd3d6891d4794f、原独立批准44276c5ae69ef0970a98464a5a9e6ff7eb1c1f1c的report/per-id/资格已读，51条SS/IN/DB/BT/AX追加与候选精确片段对齐。U08四条HP插入和L13替换在不同B位置，全部只出现一次，没有覆盖/漏接。U02逐入口消息/异常边界不为L13补出隐含全局成功前提；其CC04未读、设备/backend未运行、全1923记录/76字段48记录/优先级未签等限制不变。本次不另签U02的实际语义PASS。

全journal56片段/24目标已从B按各固定候选重放，与MI字节一致；两处共同EOF明确U01→U02，engine的U01/U13和DX的U11等共享片段机械保留。三处root管理变化仅为audit/matrix各827字节当前接收入口及errata的status/两项reception字段：链接在MI存在、作者证据按精确候选提交/路径读取，ACCEPTED/CLOSED不因此成立。对本批以外条目只给机械保留，未读的其它领域不获语义PASS。

131正式文件完整身份核对为26改/105不变；先前已接受的WP39、WP41、WP34和combat/pokemon两份目录在当前MI逐字保持。此机械事实不代替内容审查：本次另完整读它们及WP23/scope，核HP领域先提交与外层战斗中止、经验逐级、净化成长/容量/共享引用等具名直接和传递消费者。无具名作者排程边仅表示原合同未规定record→record先后，绝不表示领域依赖已全满足。

历史接收保留各自资格：M13 B17/U05/R4旧PASS不继承；J16-001的L22/L33不重开；J16-002不与HP颜色或Shadow经验消息可选项合根；J16-003沿既有WP23/SH43根，不新增缺方法根。全历史同义别名穷尽及更早canonical编号仍由R7-I精确接收。U03/U07/U10流程WAIT且未整合，不据此说源领域无依赖；7optional/2facet/1no-required/2policy未采用，27项/13批及旧56/92保持。

## 运行、配置、工具史与尚未满足的门

新增REFERENCE_OBSERVATION、参考程序、独立完整模型、游戏/宿主/Demo/native媒体/真实存档回放均0；17行为向量未执行。历史UTIL-03独立Ruby2.6一进程/10输入的旧事实分期保留，不清零、不移算本次。完整L01–L14原字节在[retained-L01-L14.json](tool-evidence/retained-L01-L14.json)，没有关闭其中任何限制。有效配置均UNVERIFIED。

本次保留005缺Git对象、007未区分root errata管理改写、008误期望reception_phase键名的机械校验失败；006补取精确对象，009按实际status/reception字段及不改变接受/关闭门重验成功。固定R metadata API CONNECT403后只读Git固定提交/tree核对成功；Settings另有新鲜HTTP200回读。早期bootstrap直接工具输出和部分诊断没有完整本地PID/UTC/I/O收据，明确保留此缺口，不倒填；后续run.py日志含真实子进程PID/UTC/argv/退出码/stdout/stderr身份。候选作者/审者原失败、截断重读和引导缺口也保留在204成员输入中。

R7-I仍须实际接收本结果，分别登记本批语义、CG06共享、直接/传递消费者和历史责任，然后才可另行正式ACCEPTED、再另行CLOSED。未读的全历史/宿主/媒体或未来贡献不自动放行。本次四个静态PASS不免除这些门。

交付仅在从B建立的`codex/r7-ir-u08-20261015-r1`普通提交/推送本目录证据。正式正文、被审候选、公共台账、main/tag均未修改。先将完整载荷普通推送并逐文件远端回读，再封存该回读证据并普通提交推送；最后完整回读的commit/tree和本地收据由实际工具输出报告，避免对自己的commit/hash作递归猜造。详见[输入收据](review-input-receipt.json)、[全量机械证据](tool-evidence/input-byte-validation.json)、[成果清单](artifact-manifest.json)及首轮remote-readback收据。
'''
(OUT/'report.md').write_text(report)
print(json.dumps({'records':len(records),'behavior_vectors':17,'verdicts':[x['verdict'] for x in records],'full_actual_files':len(full),'report_bytes':len(report.encode()),'tool_pid':os.getpid(),'behavior_execution':0,'configuration':'UNVERIFIED'},ensure_ascii=False))
