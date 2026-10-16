"""Serialize explicit bounded reviewer decisions; never promote an enumerated object to PASS."""
from pathlib import Path
import collections,datetime,hashlib,json,os,subprocess
T=Path(__file__).resolve().parents[1]
ROOT=T.parents[1]
def read(name):return json.loads((T/'recovered-target'/name).read_text())
def dump(name,x):(T/name).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
utc=datetime.datetime.now(datetime.timezone.utc).isoformat()
context=os.environ.get('CODEX_THREAD_ID','UNVERIFIED')
ident=read('identities.json')['payloads']
frozen=json.loads((T/'frozen-denominator.json').read_text())
forward=read('forward-mapping.json')
# These are actual displayed ranges in this receiver context, not the author's ranges.
ranges={
'D01':[[1,455]],'D02':[[1,101]],'D03':[[1,71]],'D04':[[1,178]],'D05':[[215,245]],
'D06':[[1,120],[283,581],[658,765]],'D07':[[72,152],[217,293],[360,530],[690,737],[742,842],[961,1117]],
'D08':[[1,283]],'D09':[[1,246]],'D10':[[1,105]],'D11':[[1,32],[105,197]],'D12':[[1,288]],
'D13':[[59,68],[130,162]],'D15':[[174,358],[403,473]],'D16':[[1,469]],'D17':[[139,152],[302,352]],
'D19':[[1,411]],'D22':[[1,83]],'D29':[[1,119]],'D32':[[1,27]],'D37':[[1,268]],'D38':[[1,243]],
'D39':[[513,698]],'D45':[[1,43]],'D49':[[480,494],[1220,1252]],'D50':[[1,125]],'D51':[[224,239]],
'D52':[[100,199]],'D59':[[18,29],[108,168],[201,213]],'D63':[[32,69]]}
io={
'D01':['8ec8ec','1b9519'],'D02':['577034'],'D03':['254aed'],'D04':['577034'],'D05':['0e957b'],
'D06':['dfc880','799702','254aed'],'D07':['877be9','68f3d6','e14ef3','3aeda0','2295e3','c275f8'],
'D08':['5c9ab4'],'D09':['a3626a'],'D10':['336ac2'],'D11':['a3856d','235eda'],'D12':['a3856d','bf9403','5859b4'],
'D13':['430eb0','fad684','75ce42'],'D15':['bf28ac','eae3eb','843dee'],'D16':['1548c8'],'D17':['403271','254aed'],
'D19':['804a4f'],'D22':['bb4215'],'D29':['bb4215'],'D32':['a41afc'],'D37':['914a93'],'D38':['914a93'],
'D39':['65266e'],'D45':['c95c2d'],'D49':['d4afcc','c33448'],'D50':['ec05dc'],'D51':['33b1e0'],
'D52':['048ef1','9be71b'],'D59':['7749fe','7b059e','b0e00f','075ba6'],'D63':['d270f3']}
# Per-fact judgments authored after the full necessary definitions and current clauses were displayed.
g_reason={
'G01':'顶层 glob、最长基名先匹配及 GameData 基名枚举均完整读取；WP02§6.1/WP04§4.1 相同；不外推专用入口。',
'G02':'设置常量8与顶层发现是不同输入；当前候选变体条款仍未保证整代兼容，未执行任何提升或编译。',
'G03':'严格符号节名与形态正数位、基础登记门、复合身份及重复拒绝已完整回源；WP18§3.1相符。',
'G04':'标量拷贝、集合克隆和 moves/evolution 空表逐成员继承分别可见；WP18对应条款不提供实例阅读替代。',
'G05':'三持物池都缺值才继承整组三池；正常显式非空任一池阻止整组继承；未把 raw 空属性归本实例。',
'G06':'FormName没有基础继承分支；pokedex_form自身默认与 category/entry 标量继承分开，WP18完整默认表支持。',
'G07':'完整查找方法只有命中形态或回基础／空的结果，不会创建 Species；当前WP18身份条款支持。',
'G08':'完整metrics getter/constructor与当前WP03§4.3.2、WP73§7三组例子支持缺条克隆／已有缺字段自身默认。',
'G09':'正形态惰性登记不带来源后缀，两坐标数组clone；WP73§7.5明确空后缀及保存路径后果。',
'G10':'完整apply方法和直接显示消费者支持敌我、阴影、倍率2及高度只作用敌方正面；不证明像素。',
'G12':'完整writer先按form!=0收后缀，后按form>0比较当前基础五组；只在正常正形态PBS域使用原nonzero简写。',
'G13':'完整close/save、registry load/save及调试入口显示Yes先档案后PBS，No重载；普通战斗update不重定位；WP73§7.5相符。',
'G14':'完整writer直接wb逐文件写，无跨文件回滚；档案成功后PBS失败的当前静态条款已读，不预测失败文件具体前缀。',
'G15':'完整Encounter.get/exists方法及WP36§3.1支持精确存在性与版本优先回退的分层。',
'G16':'完整登记和迭代器确认键形态差异；当前WP36/62已记同图v0+v1反例；不传播到直取。',
'G17':'完整compile_encounters到save/end，缺最大级、同物种同区间合并及排序与WP36§3.2一致。',
'G18':'完整编译方法确认重复类型重建槽且省略概率保留；新头重复检查前已登记前条；WP04§4.4完整表已读。',
'G19':'完整initialize/setup/reset分列，setup不写累加器；WP36§3.2.1和WP73对照支持。',
'G20':'完整整数校验／同值早退／先写异值再条件setup、调试取消和进图callback已读；当前WP36与WP73对照支持。',
'G23':'完整pbFindEncounter和pbGetEncounterPoints及TownMap/MapMetadata/registry定义已读；WP62§5.3完整门与交集相符。'}
atoms=[]
for a in frozen['atoms']:
 isg=a['id'].startswith('G')
 atoms.append(dict(a,receiver=context,receiver_status='FINITE_PREDICATE_RECEIVED_FOR_ROOT' if a['id'] in g_reason else 'DECLARATION_FULLY_READ_NECESSARY_RECEPTION_OPEN',
  reason=g_reason.get(a['id'],'完整声明已读；字段定义／已读消费者仅是部分接收。其未读实例、必要源方法、当前formal／向量维度不得由模板或来源元数据升级为完整通过。'),
  actual_source_read_evidence=[dict(identity_id=s['identity_id'],actual_ranges=ranges.get(s['identity_id'],[]),io=io.get(s['identity_id'],[])) for s in a.get('source',[])],
  behavior='NOT_EXECUTED'))
records=[]
for f in forward['records']:
 literal=f['kind'] in ['METRICS','ENCOUNTER']
 records.append(dict(id=f['section_id'],identity_id=f['identity_id'],kind=f['kind'],source_lines=f['source_lines'],
  raw_identity_pointer='dependency-identities.json#/files/'+str(list(ident).index(f['identity_id'])),
  literal_status='FULL_LITERAL_READ_FINITE_MAPPING_RECEIVED' if literal else 'AVAILABLE_UNREAD_NOT_RECEIVED',
  content_meaning=('完整备选遭遇段：类型／概率与各槽权重、物种、最低／最高等级；只有显式激活及引用合法时才进入已读编译和选择链。' if f['kind']=='ENCOUNTER' else '完整备选指标段：BackSprite/FrontSprite二元值、ShadowX/ShadowSize；高度省略按已读构造默认0，既有记录不逐字段继承基础。' if f['kind']=='METRICS' else '未实读完整记录；目标值、列表、完整业务文字和具体默认／继承尚未接收，不以源定位代替。'),
  forward_pointer='recovered-target/forward-mapping.json#/records/'+str(len(records)),
  field_count=len(f['fields']),omission_count=len(f['omitted']),
  actual_display_io=(['3f3d63'] if f['kind']=='ENCOUNTER' else ['d64ab1','3efd5f','9e9242'] if literal else []),
  alias_credit=('source-identities.json: exact blobs; one actual content reading per byte-identical file' if literal else None),
  final_task_acceptance='OPEN_NOT_SIGNED'))
assert len([r for r in records if r['literal_status'].startswith('FULL')])==2772
assert len(g_reason)==20
unread=[r['id'] for r in records if r['literal_status'].startswith('AVAILABLE')]
dump('reception-ledger.json',dict(schema='r8-independent-reception-ledger/v1',utc=utc,receiver=context,status='INCOMPLETE',
 records=records,atoms=atoms,headers=[dict(h,receiver_status='DECLARATION_READ_DEFINITION_CHECKED_NOT_RECORD_ACCEPTANCE') for h in frozen['headers']],
 counts=dict(records=6712,full_literal_records=2772,available_unread_records=3940,final_task_accepted_records=0,
 explicit_literal_fields_read=11872,explicit_fields_unread=77195,omission_instances_read=2696,omission_instances_unreceived=72617,
 finite_G_predicates_received=20,remaining_G_ids=[g['id'] for g in forward['global_assertions'] if g['id'] not in g_reason],
 field_contract_declarations_read=45,field_atoms_declarations_read=180,all_fully_received_atoms_not_claimed=True),
 global_pass=False,update_started=False))
source_rows=[]
for k,v in ident.items():
 if k.startswith('D'):
  rs=ranges.get(k,[])
  source_rows.append(dict(identity_id=k,path=v['path'],identity=v,actual_ranges=rs,actual_io=io.get(k,[]),
    receiver_status='SOURCE_OR_FORMAL_FULL_TEXT_READ' if rs==[[1,v['lines']]] else 'PARTIAL_ACTUAL_READ' if rs else 'AVAILABLE_UNREAD_BY_THIS_RECEIVER',
    rule='Range is display coverage; incidental fragments do not claim complete functions. Only report-named complete definitions used.'))
file_rows=[]
for row in json.loads((T/'recovery.json').read_text())['files']:
 name=row['relative_to_target_task']
 if name in ['review.md','proposals.json','gaps.json','execution.json','interfaces.json','coverage.json','publication.json'] or name.startswith('inputs/'):
  use='完整声明／合同业务文字已读；作者状态与接收者实际读量分开；字节相同输入仅授一次阅读。'
 elif name in ['field-contracts.json','reverse-mapping.json']:
  use='全部45字段的180声明／32链声明／4头已读；重复源／formal定位字段作精确身份用途；完整实例接收仍OPEN。'
 elif name=='forward-mapping.json':
  use='records[].{section_id,identity_id,kind,source_lines,header_contract,base_section,fields,omitted}逐对象冻结并机械绑定，全部hash/arity核验。记录字面内容只接收本ledger明确的2772，其余3940未读；metadata/status不授批准。global_assertions全文已读。'
 elif name=='reading-ledger.json':
  use='counts、当前语义分母／范围资格等完整声明已读；primary[].all_sections[].{id,section,lines,byte_offsets_half_open,fields_line_key}及依赖范围为定位身份，逐对象结构解析，不转借原作者FULL_READ。'
 elif name=='semantic-notes.json':
  use='16 primary及64依赖的全部observation/continuation文字和final_state_note已读。是作者声明，底层记录未据此接收。早期未读／旧错误保留；完整观察不能替代原始长列表和文本。'
 elif name=='central-contract-projection.json':
  use='12完整有限接口、8完整PBS归属对象及provider资格已读；provider路径/bytes/hash是导航；仅显式接收的metrics伴件获得本次有限内容信用。13接口计数笔误另记。'
 elif name=='dependency-routing.json':
  use='40 entries的owner_metadata/路径/范围仅责任与定位；完整共同用途文字已读；owner_credit=ROUTED_NOT_RECEIVED不升级。'
 elif name.startswith('tools/'):
  use='惰性原报告生成/校验/传输程序，保持原字节，不执行、不作为行为或阅读/接收真值。build-report前200行及finalize中118–160等范围为工具理解部分阅读，余代码未全文审计；本次使用自行编写的恢复和校验程序。'
 else:
  use='完整结构机械解析；身份/导航/原工具I/O/行政发布状态用途；不采用其中的旧PASS或读取声明认证本次内容。'
 file_rows.append(dict(path=name,bytes=row['bytes'],sha256=row['sha256'],blob=row['git_blob'],mode=row['mode'],purpose=use,
  target_semantic_approval_inherited=False))
dump('reading-ledger.json',dict(schema='r8-actual-receiver-reading/v1',utc=utc,receiver=context,
 source_and_formal=source_rows,payload_dispositions=file_rows,full_private_transcript_export='UNVERIFIED_NOT_EXPORTED',
 declaration_display_io=['7443aa','f1961e','51654d','a330ad','7360c1','209d47','7a10c4','8d724c','40864c','519627','58644f','83400b','0d9565','9128e5'],
 literal_readings=[dict(ids=['P01','P05','P09','P13'],range=[1,311],io=['3f3d63'],status='FULL_LITERAL_READ_EXACT_FILE_ALIASES_DEDUPED'),
 dict(ids=['P04','P08','P12','P16'],range=[1,4045],rows=[1,674],io=['d64ab1','3efd5f','9e9242'],representation='All four raw semantic fields per ordered row; exact source lines in metrics-literal-view.json',status='FULL_LITERAL_READ_EXACT_FILE_ALIASES_DEDUPED')],
 unread_primary_ids=['P02','P03','P06','P07','P10','P11','P14','P15'],all_primary_full_read=False))
inter=[]
rem={
'IF01':'基础/形态完整值未接；完整存档／迁移G31/G32、所依provider必要事实未接。',
'IF02':'全部3940基础/形态值未读；Pokemon动态getter/setter与处理器及Mega许可的完整消费者和formal未接。',
'IF03':'完整metrics值和直接倍率/资源/孵化/交换方法已读；动态形态getter、完整shadow gate及combat presentation对应formal/provider仍OPEN；不签整链。',
'IF05':'76完整遭遇记录、compiler/registry/snapshot/selector/生成请求已读；Pokemon构造/实际battle receiver及更远持久化未接。',
'IF07':'基础/形态值、PlayerPokedex登记/alias/UI选择及保存转换的完整接收未完成；G31保持源前提未接。',
'IF08':'基础/形态完整值、GrowthRate/Evolution全定义、Pokemon学习/繁殖必要消费者和当前formal/向量未接。',
'IF09':'具体持物池值未读；生成请求已读不等于item setter/can-hold/save；CREB/PBS_BATTLE producer贡献未接。',
'ELR-I03':'8个基础/形态路径完整值均未读；原本地化producer报告/当前域消费者未接，不能凭schema或消息语料数量签收。',
'CD-I01':'具体祖先/Incense/Egg/Offspring实例值及繁殖消费者未接。',
'CD-I06':'parser/compile/export必要子集已读，但备份基础/形态完整值与所有必要当前consumer/formal维度未接。'}
for x in read('interfaces.json')['interfaces']:
 y=dict(x);i=x['id'];y['original_status']=y.pop('status');y['receiver']=context
 y['status']='FINITE_STATIC_INTERFACE_RECEIVED_FOR_ROOT' if i in ['IF04','IF06'] else 'INCOMPLETE_NOT_SIGNED'
 y['reception_reason']=('完整editor/metrics/writer/registry/debug入口、开发者24事实及更正、当前WP73§7/WE-M15–20/B19-C016已接；限定正常合法输入与源请求，不证明原生I/O或实际像素。' if i=='IF04' else '完整版本登记/直取/枚举、76备份段、完整图鉴点计算和TownMap/MapMetadata必要定义及WP36/62精确条件已接；不要求实际媒体点亮，不接全图鉴界面。' if i=='IF06' else rem[i])
 y['remaining']=None if i in ['IF04','IF06'] else rem[i];y['task_final_acceptance']='ROOT_ONLY_OPEN';inter.append(y)
dump('interfaces.json',dict(schema='r8-receiver-finite-interfaces/v1',utc=utc,interfaces=inter,finite_received=2,remaining=10,
 primary_complete=False,final_receiver='source_thread01a13f49-a154-7054-9b04-ce31f924d01c',producer_rule='未实读producer内容不签consumer；仅metrics伴件明确逐事实接收，其余导航不升级。'))
# Bind supplementary reports without writing another owner's directory.
supp=[]
for rel in ['adjudication/root-xpcb001-already-documented-counterreview.v1.json','adjudication/root-backup-version-exact-inputs.v1.json',
'evidence/proposal-snapshots/external_pbs_creature_backups-5566e32e562f06698490282d074ade30432a7cddf7d0e2cfb404b89dddb7a2e8.json',
 'tasks/developer_full_cloud/metrics-complete-contribution.v1.json','tasks/developer_full_cloud/metrics-complete-contribution.v2.json']:
 path=ROOT/rel;b=path.read_bytes()
 # The worktree is on the frozen contract plus our own exclusive changes.
 fixed=subprocess.check_output(['git','show','40f45dddcdea5522b4bf7d0fea1a0f74f7d3d232:'+str(path.relative_to(Path.cwd()))])
 assert b==fixed
 supp.append(dict(contract_commit='40f45dddcdea5522b4bf7d0fea1a0f74f7d3d232',path=str(path.relative_to(Path.cwd())),bytes=len(b),sha256=hashlib.sha256(b).hexdigest(),blob=subprocess.check_output(['git','hash-object','--stdin'],input=b).decode().strip(),purpose='Bounded counter/proposal history or complete metrics provider with mandatory correction; exact raw input kept in fixed contract.'))
dump('supplemental-inputs.json',supp)
dump('proposal-counters.json',dict(schema='r8-independent-proposal-counter/v1',utc=utc,receiver=context,author='01a143b3-2169-7510-89e4-e6e3c9712029',
 records=[dict(id='GR8-XPCB-001',classification='NO_REQUIRED_BOUNDED_ALREADY_DOCUMENTED',scope='正常Symbol登记、四备份map5、直取与枚举差异及有条件图鉴贡献',
 full_proposal='recovered-target/proposals.json',earlier_available_withdrawn_snapshot=supp[2],existing_root_counter=supp[0],
 complete_definition_clarifiers=dict(compiler=[658,765],pokedex_helpers=[302,352]),
 actual_read_io=['f1961e','bfd8cc','049772','254aed','3f3d63','a3856d','a66c6f','c95c2d'],
 strongest_counter='当前WP36§3.1/62§5.3已明确覆盖；无已证新正规遗漏。',
 ordinary_controls=['v0枚举一次','仅v0时请求v1回退','map5同时0/1时直取1而枚举0再1'],
 failure_cancel_partial='查询无取消和写入；compiler前条已登记后才查重复，未到尾部save；UI缺metadata/隐藏/错区域/无可见格不贡献；异常宿主不承诺回滚。',
 formal_write_set=[],new_required=0,new_optional=0,history='canonical relation UNVERIFIED; no old closure reopened',
 final_global_acceptance='ROOT_ONLY_OPEN',business='NOT_EXECUTED')],
 audit_corrections=[dict(id='RECEPTION-AUDIT-COUNT-01',object='review.md / central-contract-projection.actual_read',claimed_interfaces=13,
 actual_interface_ids=[x['id'] for x in inter],actual_interfaces=12,provider_route_groups=13,formal_required_added=False,
 disposition='原件不改；接收使用实际12-ID集合，不增加必修根因。')],global_no_required_update=False,update_started=False))
dump('continuation.json',dict(schema='r8-exact-reception-continuation/v1',status='INCOMPLETE',contract_commit='40f45dddcdea5522b4bf7d0fea1a0f74f7d3d232',
 target_commit='b6f12ecfbe006ef0f2ea463d6689d78094915e75',branch='codex/r8-receive-pbs-creature-backups-20261016',
 full_prompt=str(ROOT/'delegation/prompts/receive_external_pbs_creature_backups.md'),full_readset=str(ROOT/'delegation/readsets/receive_external_pbs_creature_backups.complete.json'),
 normative_reading='必须重新取得并完整读固定全局prompt/skill/AGENTS和完整任务合同，不能仅凭本continuation摘要；原作者上下文冲突规则仍适用。',
 exact_unread_record_ids=unread,remaining_interfaces=[x['id'] for x in inter if x['status']=='INCOMPLETE_NOT_SIGNED'],
 remaining_G_ids=[x for x in [g['id'] for g in forward['global_assertions']] if x not in g_reason],
 remaining_field_consumer_facets=[c['id']+'.consumer' for c in read('field-contracts.json')['contracts']],
 rule='已读字段声明/源定义不自动完成实例和consumer；沿现台账精确继续，所有192个非20G对象保持必要接收未完，不用清单生成声明全部人工通过。',
 material_missing=[],host_claims='NOT_EXECUTED，不把可得未读变limit',new_contexts_spawned=0,update_started=False))
failed=[
 dict(action='Initial git show/tree before exact contract fetch',exit=128,credit=0,resolution='普通fetch固定合同后重读成功'),
 dict(action='Initial tools metadata discovery oversized',result='TRUNCATED_NOT_SEMANTIC_INPUT',credit=0),
 dict(action='Root recovery transport receipt display',result='TRUNCATED_IDENTITY_ONLY_NOT_ADOPTED',credit=0),
 dict(action='Root exact-input inventory display accidentally included exact_text',result='TRUNCATED',credit=0,resolution='必要完整source/formal重新从固定Git读取254aed/a3856d等'),
 dict(action='Sample primary reading-ledger display',result='TRUNCATED',credit=0,resolution='全对象定位结构机械冻结；不声称该显示读完9MB文件'),
 dict(action='Primary semantic-notes combined view',result='TRUNCATED',resolution='Gen5/6在7a10c4，Gen7在8d724c补读；未把notes替代原始长列表'),
 dict(action='Central projection compact view',result='TRUNCATED',resolution='12接口此前段完整，缺失localized_paths在9128e5全部补读；provider路径仅导航'),
 dict(action='Metrics provider v2 combined embedded source display',result='TRUNCATED',resolution='source文本与已完整实读固定R逐段精确别名核验938418；剩余12facts完整显示；v1更正214819'),
 dict(action='Stat/Mega reader process creation',result='exec-server transport disconnected',exit='NO_PROCESS_CREATED',credit=0,resolution='pwd成功后同一读取bb4215/2295e3重试成功'),
 dict(action='WE15/B19C016 loose locator spellings',exit=1,credit=0,resolution='准确WE-M15–20和B19-C016定位后8d9128/025bfa实际读取')]
dump('execution.json',dict(schema='r8-receiver-execution/v1',utc=utc,behavior_executions=0,reference_compile='NOT_EXECUTED',reference_writer='NOT_EXECUTED',
 game_save_ui_host_media='NOT_EXECUTED',tools_only=['exact Git fetch/blob recovery','identity/hash/arity/collection verification','lossless metrics view','explicit ledger serialization','remote report readback'],
 semantic_credit_from_tools=0,restored_scripts_executed=False,failures_and_truncations=failed,private_transcript_export='UNVERIFIED_NOT_EXPORTED',
 requested=dict(model='gpt-6.1-sol',effort='ultra',tier='default',speed='normal',Fast='off'),actual={k:'UNVERIFIED' for k in ['model','effort','tier','speed','Fast']},actual_context=context,
 original_author_failures='完整保留recovered-target/execution.json，不转入本次执行计数',material_blockers=[],update_started=False))
dump('progress.json',dict(schema='r8-receiver-progress/v1',utc=utc,task='receive_external_pbs_creature_backups',context=context,
 status='INCOMPLETE',process_state='BOUNDED_CONTENT_DELIVERY_PREPARED',full_literal_records=2772,unread_records=3940,
 finite_interfaces_received=['IF04','IF06'],remaining_interfaces=10,material_or_permission_blocker=False,
 actual_remaining='本接收上下文未完成全部基础/形态原文及后继必要消费者；明确可得未读，不能task-final。',update_started=False))
print(json.dumps(dict(records=6712,literal_read=2772,unread=3940,G_finite_received=20,finite_interfaces=2,status='INCOMPLETE')))
