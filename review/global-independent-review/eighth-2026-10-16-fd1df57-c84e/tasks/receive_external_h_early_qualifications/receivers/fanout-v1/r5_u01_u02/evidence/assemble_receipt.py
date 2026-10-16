"""Assemble manually adjudicated arguments and immutable locators, never infer PASS.

Inputs are inert JSON, source identities, and exact rendered read ranges. This
script does not execute recovered scripts or reference/game behavior.
"""
from pathlib import Path
import json,gzip,hashlib,subprocess,datetime,re,os,collections
W=Path(__file__).resolve().parents[1];T=W.parents[2];F=T/'delegation/fanout-v1';P=Path('/workspace/pokemon-essentials-clean-room');R=Path('/workspace/pokemon-essentials')
C='9abf7bfc87274fb37f08d9f77a1bcb53f53d3ecd';B8='fd1df570cad987dc3852a3b958f03916e317f7fe';RC='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b';TARGET='11c057d9aed330c16312470f80f13d180f8e1e65';PREV='ab44ee8c5ffd53ded7d5bc37ae6f15e6ed3ba8d8'
def raw(x):return (json.dumps(x,ensure_ascii=False,sort_keys=True,separators=(',',':'))+'\n').encode()
def ident(b):return {'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'git_blob':hashlib.sha1(f'blob {len(b)}\0'.encode()+b).hexdigest()}
def write(n,x): (W/n).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def git(repo,*args):return subprocess.check_output(['git','-C',str(repo),*args])
def loc(repo,commit,path,ranges):
 b=git(repo,'show',commit+':'+path)
 return {'commit':commit,'path':path,'mode':'100644',**ident(b),'actual_ranges':ranges}
readset=json.loads((F/'shards/r5_u01_u02/readset.json').read_text());view=json.loads(gzip.decompress((F/'shards/r5_u01_u02/complete-records.json.gz').read_bytes()));objects=view['owned_complete_objects'];roots=[o for o in objects if o['pointer'].startswith('/R5/current_root/records/')]
args=json.loads((W/'evidence/adjudications.json').read_text());by={x['id']:x for x in args['records']};ids=readset['primary_semantic_population']['R5_ids'];assert set(by)==set(ids) and len(by)==48
assert [o['primary_id']for o in roots]==ids
now=datetime.datetime.now(datetime.timezone.utc).isoformat();context=os.environ.get('CODEX_THREAD_ID','UNVERIFIED');assert context!='01a143b2-fc07-7339-ab2f-055dba6bc023'
fixed={'containing_contract':C,'target':TARGET,'target_checkout_tree':'2fcef25ee9903bd7e28dec21f6fc2d970c221f77','target_task_tree':'bb0cb15506d2abc9e6b84abe1391048776de6997','previous_reception':PREV,'B8':B8,'B8_tree':'751dfde81048c81390f89a65ca1d1a565ba8e1ca','B8_formal_tree':'f292698cdd4a8e725525a9be6dc34b75faaf151e','R':RC,'R_tree':'7589c800b61ba13a13040ed0d686979b80a84fd0'}
source=json.loads((W/'.local/source-range-manifest.json').read_text())+json.loads((W/'.local/source-supplement-manifest.json').read_text())+json.loads((W/'.local/final-consumer-manifest.json').read_text())
# Supplemental direct outputs were actually presented, including definition ends.
for p,rs,output in [
 ('Data/Scripts/016_UI/003_UI_Pokedex_Main.rb',[[771,895]],'502148'),
 ('Data/Scripts/016_UI/003_UI_Pokedex_Main.rb',[[479,765]],'693411'),
 ('Data/Scripts/016_UI/004_UI_Pokedex_Entry.rb',[[221,312]],'450219'),
 ('Data/Scripts/020_Debug/002_Editor_DataTypes.rb',[[1624,1720]],'ef459e'),
 ('Data/Scripts/015_Trainers and player/005_Player_Pokedex.rb',[[345,370]],'f83936'),
 ('Data/Scripts/010_Data/002_PBS data/001_MiscPBSData.rb',[[26,37]],'ea0f22'),
 ('Data/Scripts/016_UI/019_UI_PC.rb',[[150,195]],'065ec5'),
 ('Data/Scripts/012_Overworld/008_Overworld_RandomDungeons.rb',[[330,395]],'0faefd'),
 ('Data/Scripts/012_Overworld/008_Overworld_RandomDungeons.rb',[[1054,1112]],'62b5be'),
 ('Data/Scripts/020_Debug/003_Debug menus/002_Debug_MenuCommands.rb',[[1421,1455]],'c0e3e6'),
 ('Data/Scripts/012_Overworld/008_Overworld_RandomDungeons.rb',[[317,346]],'41dd85')]:
 total=len(git(R,'show',RC+':'+p).decode().splitlines());rs=[[a,min(b,total)]for a,b in rs];source.append({**loc(R,RC,p,rs),'platform_output':output,'actual_presented_only':True})
b8=json.loads((W/'.local/b8-range-manifest.json').read_text())+json.loads((W/'.local/vector-range-manifest.json').read_text())
b8.append({**loc(P,B8,'deliverables/final-specification-set/demo-dx/wp73-a-content-editors.md',[[63,76]]),'platform_output':'7d0842'})
b8.append({**loc(P,B8,'deliverables/final-specification-set/user-interface/wp66-b-storage-and-pokedex-ui.md',[[236,245]]),'platform_output':'21c6a2'})
write('evidence/source-reading.json',{'schema':'gr8.fixed-reading-ranges/v1','R':source,'B8':b8,'definition_rule':'原锚点不是完整定义证明；实际完整方法及必要调用的范围如列。额外上下文范围不增加primary或全文件签名。','behavior_execution':0})
objids=json.loads((W/'.local/object-identities.json').read_text());compressed=gzip.compress(raw(objids),mtime=0);(W/'evidence/object-identities.json.gz').write_bytes(compressed)
pagegroups={
 'read-pages':[],
 'source-pages':[],
 'final-consumers':['8cf8f2','e2538a'],
 'supplement-pages':['d0e8d6','48381b','842b7c','f6eb68'],
 'b8-pages':['1b927b','313833','6bd414','fc930d','9138f1','ce0af1','89ffa4','f66c7c','6a883e','56c492','83c523','2921d8','cc0b23','4ab6de'],
 'vector-pages':['8c9037','a3bc5e','d8f3ca','9e4f88','e95b41'],
 'criterion-pages':['e05dbd','23df38','4e13fb']}
# One output normally contained two pages; the last original-value output had 3.
value_outputs={1:'fa8e3a',2:'ef1e39',3:'ef1e39',4:'65504c',5:'65504c',6:'ebbd22',7:'ebbd22',8:'1eff77',9:'1eff77',10:'295164',11:'295164',12:'23f35d',13:'23f35d',14:'78aecf',15:'78aecf',16:'23018b',17:'23018b',18:'7958b8',19:'7958b8',20:'60a4ca',21:'60a4ca',22:'15e5f4',23:'15e5f4',24:'dffb14',25:'dffb14',26:'60544b',27:'60544b',28:'9d4df3',29:'9d4df3',30:'8b9082',31:'8b9082',32:'0c316d',33:'0c316d',34:'0c316d'}
src_outputs=['f55349','6c5d87','ad8dca','3ff11c','c38d88','460052','b4627f','0e73e6','7bf37d','3ae33e','ac94f4','4f0db7','cbc1e3','31377f','c6d8cb']
pagegroups['source-pages']=src_outputs
presented=[]
for group,outs in pagegroups.items():
 for i,p in enumerate(sorted((W/'.local'/group).glob('*.txt')),1):
  output=value_outputs[i]if group=='read-pages'else outs[i-1]if group=='supplement-pages'else outs[(i-1)//2]if group not in ['criterion-pages']else outs[(i-1)//2]
  b=p.read_bytes();item={'group':group,'page':i,'platform_output':output,**ident(b),'truncated':False}
  if group=='read-pages':
   s=b.decode();item['exact_scalar_indices']=[int(m.group(1))for m in re.finditer(r'^\[(\d+);o\d+;',s,re.M)]
  presented.append(item)
short=(W/'.local/short-facts.txt').read_bytes();presented.append({'group':'short-business-values','ranges':[[1,180],[181,360],[361,540],[541,710]],'platform_outputs':['d60389','1900b4','449e89','d53b18'],**ident(short),'truncated':False})
write('evidence/presentations.json',{'schema':'gr8.actual-presentations/v1','input_object_view':{'path':str((F/'shards/r5_u01_u02/complete-records.json.gz').relative_to(P)),**ident((F/'shards/r5_u01_u02/complete-records.json.gz').read_bytes())},'presentations':presented,'meaning':'value组是无损呈现与精确同值关联；不是语义分母。同值在另一语境的判定由48项独立论证和294项接收分别承担。源/规格副本只在忽略缓存，远端按固定Git字节及本范围可回读。','truncated_attempts_not_credited':['早期GitHub fetch_file大prompt/readset输出','直接大JSON/文件身份清单输出','80b48c完整对象输出','eefe65过大结构输出'],'completed_replacements':'固定prompt/readset已连续全读；所有完整对象按可逆值/上下文+原criterion与业务表补读；B8/源按所列连续范围补至定义结束。'})
object_by_index={x['index']:x for x in objids};packets={o['primary_id']:(i,o)for i,o in enumerate(objects)if o.get('role')=='original_packet_finding'}
criteria=[];records=[];freeze=[]
for oi,o in enumerate(roots):
 x=o['expanded_complete_object'];i=x['id'];a=by[i];assert len(a['checks'])==len(x['schema_units'])
 pidx,packet=packets[i];original=packet['expanded_complete_object']
 ownR=[]
 extraR={
  'GR5-M01-001':['004_UI_Pokedex_Entry.rb','003_UI_Pokedex_Main.rb','002_Editor_DataTypes.rb','pokemon.txt'],
  'GR5-M01-004':['002_Editor_DataTypes.rb','pokemon.txt'],
  'GR5-M01-014':['003_UI_Pokedex_Main.rb','005_Player_Pokedex.rb','001_Utilities.rb','001_MiscPBSData.rb'],
  'GR5-M01-024':['003_UI_Pokedex_Main.rb','004_UI_Pokedex_Entry.rb'],
  'GR5-M01-025':['001_Pokemon.rb'],
  'GR5-M01-026':['007_Overworld_DayCare.rb'],
  'GR5-M01-031':['007_Overworld_DayCare.rb']}.get(i,[])
 for q in source:
  if Path(q['path']).name in extraR or any(z[2]==i for z in q.get('requested_ranges',[])if len(z)>2)or q['path']in {s.get('path')for s in original.get('source_anchors',[])+original.get('actual_source',[])}:
   ownR.append({'path':q['path'],'actual_ranges':q['actual_ranges'],'sha256':q['sha256'],'commit':RC})
 for s,note in zip(x['schema_units'],a['checks']):
  orig=s['original_fields'];criteria.append({'criterion_id':s['criterion_id'],'primary_id':i,'kind':s['kind'],'definition':orig.get('criterion',orig.get('definition')),'original_record':s['original_source'],'original_fields_canonical':ident(raw(orig)),'current_pointer':o['pointer']+'/schema_units/'+str(x['schema_units'].index(s)),'current_stage_claim':{'status':s['current_fields'].get('current_actual_result'),'canonical_identity':ident(raw(s['current_fields'])),'source_pointer':o['pointer']+'/schema_units/'+str(x['schema_units'].index(s))+'/current_fields','receiver_does_not_transfer_verdict':True},'accepted_binding_claim':{'canonical_identity':ident(raw(s['accepted_fields'])),'source_pointer':o['pointer']+'/schema_units/'+str(x['schema_units'].index(s))+'/accepted_fields','receiver_does_not_transfer_verdict':True},'receiver_decision':'RECEIVED_SCOPED_STATIC','independent_reason':note,'argument_record':i,'B8_clause_and_vectors':a['B8'],'source_ranges_ref':'evidence/source-reading.json','whole_file_or_interface_signature':False,'new_behavior_execution':0})
 freeze.append({'id':i,'batch':x['current_scope_qualification']['batch'],'native_static_conditions':x['current_scope_qualification']['native_static_conditions'],'criterion_ids':[s['criterion_id']for s in x['schema_units']],'current_root':object_by_index[oi],'original_packet':object_by_index[pidx],'all_context_object_indices':[j for j,z in enumerate(objects)if z.get('primary_id')==i]})
 records.append({'id':i,'primary_reception':'COMPLETE_SCOPED_STATIC','current_effective_meaning':a['reason'],'complete_original_fact_and_cases':{'source_object_index':pidx,'original_fields':list(original),'normal':original.get('normal_case'),'minimal_counterexample':original.get('minimal_counterexample'),'failure_cancel_partial':original.get('failure_or_boundary_case'),'preconditions':original.get('preconditions'),'unknowns':original.get('unknowns'),'excluded_claims':original.get('excluded_claims')},'independent_consumer_join':a['consumer'],'R_definition_and_consumer_ranges':ownR,'B8_clauses_vectors':a['B8'],'B8_paths':x['current_formal_routes'],'criteria':[s['criterion_id']for s in x['schema_units']],'source_objects_ref':f'frozen-units.json#/records/{len(freeze)-1}','open_interfaces':['IF-EXTERNAL-M05-006']if i in ['GR5-M01-011','GR5-M01-016']else [],'outbound_shared_interface':'IF-SHARED-TAIL-'+i,'new_B8_required_finding':False,'whole_file_signature':False,'formal_acceptance_changed':False,'CLOSED_changed':False})
assert [x['criterion_id']for x in criteria]==readset['primary_semantic_population']['R5_criteria'];assert len(criteria)==294
write('frozen-units.json',{'schema':'gr8.r5-u01-u02.frozen/v1','fixed':fixed,'readset_identity':ident((F/'shards/r5_u01_u02/readset.json').read_bytes()),'population':{'primary':48,'schema_criteria':294,'native_static_conditions':192,'U01_primary':34,'U01_criteria':248,'U02_primary':14,'U02_criteria':46,'complete_objects_presentation_only':784,'dictionary_entries_presentation_only':2571,'dictionary_bindings_presentation_only':12655},'records':freeze,'context_header_indices':[780,781,782,783],'not_denominator':['文件数','hash数','V/N独有值','JSON叶','字典绑定','显示页数'],'UPDATE_NOT_STARTED':True})
write('reception-ledger.json',{'schema':'gr8.r5-u01-u02.reception/v1','fixed':fixed,'actual_reviewer_context':context,'context_echo_source':'environment CODEX_THREAD_ID (0e775b)','target_author_context':'01a143b2-fc07-7339-ab2f-055dba6bc023','independent_of_target_author':context!='UNVERIFIED','records':records,'criterion_results':criteria,'counts':{'complete_primary':48,'criteria_read_and_locally_evaluated':294,'new_required_proposals':0},'qualification':'RECEIVED_SCOPED_STATIC仅本组完整原合同/criterion、必要R/B8定义与消费者；不继承旧PASS、不改原阶段资格、不签未接producer或共享全局状态。','new_behavior_execution':0,'UPDATE_NOT_STARTED':True})
outbound=[{'id':'IF-SHARED-TAIL-'+r['id'],'producer_id':r['id'],'producer_receiver':'r5_u01_u02','consumer_owner':'r5_tail_shared_policy','producer_fact':r['current_effective_meaning'],'producer_argument_ref':'reception-ledger.json#/records/'+str(j),'current_status':'PRODUCER_CONTRIBUTION_COMPLETE_RECEIVER_JOIN_OPEN','consumer_receipt':None,'whole_interface_signature':False}for j,r in enumerate(records)]
interfaces=[{'id':'IF-EXTERNAL-M05-006','status':'OPEN','producer_primary':'GR5-M05-006','producer_owner':'r5_u03_u06_core','consumers':['GR5-M01-011/preserve/01','GR5-M01-016/static/06','GR5-M01-016/preserve/01'],'fact':'Pocket/Price/FieldUse/BattleUse四默认及Flags/数量谓词由道具主责；本组只核引用与自己份名/消费位事实，未重签该producer。','producer_receipt':None,'available_evidence':'B8 WP03 L116的真实主责引用；前接收consumer-review是有限消费条件，不是该producer完整接收。','required_to_close':'原接收者/主审取得真实非作者producer收据后，仅接合这三个criterion的主责引用。','whole_interface_signature':False}, {'id':'IF-GLOBAL-STAGE-SHARED','status':'OPEN','producer_owner':'r5_tail_shared_policy','consumers':ids,'fact':'历史shared21/dependency18及全局scope/candidate/actual/acceptance/activation状态接合；H当前reason中的UI/FURFROU/BACK、六行政镜像属于必要共享上下文，不反签U06/UI整producer。','producer_receipt':None,'available_evidence':'固定目标current/accepted绑定、原完整header、现接收者有限consumer-review及本组48贡献已读；尾组最终事实接合尚未取得。','required_to_close':'尾组逐producer引用本组实质凭据，接合其独占共享状态后由原协调者整合。','whole_interface_signature':False}]
write('interfaces.json',{'schema':'gr8.r5-u01-u02.interfaces/v1','fixed':fixed,'local_joins':[{'primary_id':r['id'],'join':r['independent_consumer_join'],'argument_ref':'reception-ledger.json#/records/'+str(j),'status':'LOCAL_NECESSARY_R_B8_JOIN_COMPLETE','whole_system_signature':False}for j,r in enumerate(records)],'incoming_or_global':interfaces,'outbound_per_producer':outbound,'remote_lookup':{'command':"git ls-remote --heads origin 'codex/r8-final-early-*' 'codex/r8-h-early-*'",'platform_outputs':['ec4a16'],'result':'所查询模式当时返回空；只证明这些模式未返回分支，不证明所有可能分支/未发布工作均不存在。','receipt_available_to_this_context':False},'aggregation_rule':'48项事实各自供尾组接合；不能把四任务状态、角色名或本组294局部接收当共享21/依赖18整签。'})
write('unreceived.json',{'schema':'gr8.r5-u01-u02.unreceived/v1','local_available_required_unread':[],'local_primary_unreceived':[],'local_criterion_unreceived':[],'necessary_interface_unreceived':[{'interface':i['id'],'owner':i['producer_owner'],'missing':i['required_to_close']}for i in interfaces],'not_missing_material':['跨组回执尚未接合是实际依赖缺口，不是宿主limit。','其余44个R5 primary及R1–R4/非必修/policy/limit为其它冻结主责，不在此二次接收。'],'unavailable_observation_limits':[{'id':'LIMIT-HOST-DEMO','scope':'归档原生读取、真实地图/公共事件安排、媒体/UI、实际存档及完整编译/往返','status':'NOT_EXECUTED; 不具备此任务新增运行观察，不外推成功。'},{'id':'LIMIT-RUNTIME-PARAMETERS','scope':'actual model/effort/tier/speed/Fast','status':'UNVERIFIED; UUID仅以单独实际环境回显确认。'}],'no_limit_substitutes_for_unread':True})
write('findings.json',{'schema':'gr8.r5-u01-u02.findings/v1','new_required_proposals':[],'new_optional_or_policy_proposals':[],'bounded_dispositions':[{'id':'LOCAL-NO-NEW-B8-REVISION','primary_ids':ids,'result':'NO_NEW_REQUIRED_PROPOSAL_IN_OWN_SCOPE','basis':'48项逐条手写反向/正常/失败论证及294条criterion理由；B8已有作者输入、状态、调用和有序修复合同，最强无需修改解释成立。','not_global_PASS':True},{'id':'RECEPTION-H-EARLY-EVIDENCE-001','result':'CONTEXT_ONLY_NOT_WHOLE_ADJUDICATED_HERE','basis':'接收旧路由按字段名隐藏业务值的风险；本组完整raw/expanded业务值均读，不使用original_actual_text等键名豁免。全局28值及其它producer由尾组原合同处理。','reopen_historical92':False},{'id':'RECEPTION-H-EARLY-POLICY-002','result':'CONTEXT_ONLY_PENDING_ASSIGNED_NONPROPOSER_DISPOSITION','basis':'强制clarifier全文已读。UTIL-03末尾LF是通用numeric旧policy事实候选，不套PBS的单行f/b/枚举门；本组未裁定未来兼容或升B8 required。','new_B8_required':False}],'history_preserved':['candidate/actual/accepted/CLOSED/activation各按原输入时点；原FAIL/WAIT/MISMATCH不改。','五旧身份的新回读只增加身份信用，原UNVERIFIED保留。','U03消费条件与Summary/Party/Bottle有限先接收不升级整producer。'],'UPDATE_NOT_STARTED':True})
write('reading-ledger.json',{'schema':'gr8.r5-u01-u02.reading/v1','actual_reviewer_context':context,'fixed':fixed,'contract_reads':['prompt.md 1–195/196–389/390–665完整含全局prompt/AGENTS/SKILL','readset.json 1–530/531–1080/1081–1600/1601–2086','fanout README全文、common-premises全文、mandatory-policy-clarifier全文、restore helper全文','适用项目根AGENTS；生成/恢复代码先读懂后只作惰性恢复/静态核验','旧接收findings、historical-five-identities、consumer-review、reception-ledger、interfaces及report全文'],'complete_object_coverage':{'count':784,'identity_manifest':{'path':'evidence/object-identities.json.gz',**ident(compressed),'decoded_canonical_identity':ident(raw(objids))},'group_purposes':[{'indices':[0,47],'purpose':'当前逐ID完整记录、schema original/current/accepted绑定及阶段理由'},{'indices':[48,95],'purpose':'完整旧scope资格与路由说明，旧结论保留原时点'},{'indices':[96,99],'purpose':'首四项完整原scope包括closure、native/schema等字段'},{'indices':[100,143],'purpose':'其余原scope/read_fields/scalar_registry及所有业务值'},{'indices':[144,437],'purpose':'294原检查的完整字段、用途和原限定'},{'indices':[438,779],'purpose':'48完整原packet finding与294完整原criterion'},{'indices':[780,783],'purpose':'原header完整counterchain/evidence pool/context；其中外组主责仅上下文，不授第二primary签名'}],'identity_transport_structure_rule':'纯commit/tree/blob/mode/bytes/SHA及无业务值的结构索引按完整类型/集合/用途机械处理；业务事实/前提/例子/状态/资格全部作实质处理。','same_value_rule':'精确同字节呈现复用不是跨语境自动批准；逐primary及criterion独立论证见reception-ledger。'},'actual_nontruncated_presentations':'evidence/presentations.json','fixed_R_B8_reading':'evidence/source-reading.json','mechanical_credit_zero':'input-validation恢复身份、dictionary raw/expanded、生成view及脚本exit0不授semantic credit。','local_unread':0,'whole_source_file_or_spec_file_signatures':False,'new_reference_model_host_demo_execution':0,'UPDATE_NOT_STARTED':True})
write('progress.json',{'schema':'gr8.r5-u01-u02.progress/v1','utc':now,'task':'early_r5_u01_u02','status':'INCOMPLETE_EXTERNAL_INTERFACES','local_primary_reception':'COMPLETE','complete_primary':48,'criteria_read_evaluated':294,'local_required_unread':0,'necessary_interfaces_open':[i['id']for i in interfaces],'ready_for_coordinator_consolidation':False,'root_task_final_signed':False,'fixed':fixed,'branch':'codex/r8-final-early-r5-u01-u02-20261016','exclusive_write_root':str(W.relative_to(P)),'independence':{'actual_context':context,'echo':'CODEX_THREAD_ID, platform 0e775b','target_author':'01a143b2-fc07-7339-ab2f-055dba6bc023','conflict':False,'new_contexts_spawned_by_this_task':0},'requested_runtime':{'model':'gpt-6.1-sol','effort':'ultra','tier':'default','speed':'normal','Fast':'off'},'actual_runtime':dict.fromkeys(['model','effort','tier','speed','Fast'],'UNVERIFIED'),'behavior_execution':'NOT_EXECUTED','new_behavior_execution':0,'UPDATE_NOT_STARTED':True,'publication':'pending ordinary commit/push and isolated remote complete readback; see publication.json once present'})
print(json.dumps({'primary':len(records),'criteria':len(criteria),'local_unread':0,'external_open':len(interfaces),'semantic_status':'scoped manual arguments only','generated_acceptance_credit':0}))
