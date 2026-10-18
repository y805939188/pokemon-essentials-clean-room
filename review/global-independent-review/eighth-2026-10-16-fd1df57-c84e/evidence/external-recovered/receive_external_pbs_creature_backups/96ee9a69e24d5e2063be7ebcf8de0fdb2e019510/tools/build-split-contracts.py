"""Freeze four disjoint, independently dispatchable reception contracts. Starts no contexts."""
from pathlib import Path
import collections,datetime,hashlib,json,subprocess
T=Path(__file__).resolve().parents[1]
ROOT=T.parents[1]
REPO=Path.cwd()
OUT=T/'delegation/remaining-v1'
CONTRACT='40f45dddcdea5522b4bf7d0fea1a0f74f7d3d232'
PARENT='bf36d6c3e5b8323d530155fc68ac6a4249336f66'
CORE='7ebc431b1cc47d2c41cba2506512ce20c1f4ca84'
TARGET='b6f12ecfbe006ef0f2ea463d6689d78094915e75'
B8='fd1df570cad987dc3852a3b958f03916e317f7fe'
R='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
UTC=datetime.datetime.now(datetime.timezone.utc).isoformat()
def dump(path,value):path.parent.mkdir(parents=True,exist_ok=True);path.write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n')
def load(path):return json.loads(path.read_text())
def gid(data):return hashlib.sha1(('blob '+str(len(data))+'\0').encode()+data).hexdigest()
def identity(path):
 data=path.read_bytes();return dict(path=str(path.relative_to(REPO)),mode='100644',bytes=len(data),sha256=hashlib.sha256(data).hexdigest(),blob=gid(data))
def gitbytes(commit,path):return subprocess.check_output(['git','show',commit+':'+str(path.relative_to(REPO))])
def repo_identity(repo,commit,path):
 data=subprocess.check_output(['git','-C',str(repo),'show',commit+':'+path])
 mode,kind,blob=subprocess.check_output(['git','-C',str(repo),'ls-tree',commit,'--',path]).decode().split('\t')[0].split()
 return dict(repo=str(repo),commit=commit,path=path,mode=mode,kind=kind,blob=blob,bytes=len(data),sha256=hashlib.sha256(data).hexdigest(),lines=len(data.splitlines()),purpose='完整必要定义/条款及前提；不是外域整文件主责或语义信用')
PREREQ={
 'gen5':['D01','D06','D07','D08','D15','D20','D32','D40','D41','D42','D43'],
 'gen6':['D01','D06','D08','D09','D17','D18','D20','D21','D22','D23','D24','D26','D27','D28','D32','D40','D41','D42','D43'],
 'gen7':['D01','D06','D07','D08','D20','D21','D25','D29','D30','D31','D32','D37'],
 'gen8':['D01','D02','D03','D04','D06','D07','D08','D09','D15','D16','D20','D21','D23','D32','D35','D36','D37','D38','D39','D40','D41','D42','D43','D49','D50','D51']}
EXTRA_R={
 'gen5':['Data/Scripts/001_Technical/003_Intl_Messages.rb'],
 'gen6':[],
 'gen7':['Data/Scripts/012_Overworld/007_Overworld_DayCare.rb'],
 'gen8':['Data/Scripts/012_Overworld/002_Battle triggering/001_Overworld_BattleStarting.rb','Data/Scripts/011_Battle/004_Scene/002_Scene_Initialize.rb']}
EXTRA_FORMAL={
 'gen5':['generic-kernel/wp08-localization.md','generic-kernel/wp09-save-startup-continue.md','test-catalog/generic-kernel-wp05-06-07-08-09-10.md','test-catalog/generic-kernel-wp02-03-04.md'],
 'gen6':['generic-kernel/wp09-save-startup-continue.md','pokemon-rules/wp19-attributes-ability-and-stats.md','user-interface/wp66-b-storage-and-pokedex-ui.md','test-catalog/pokemon-rules-wp19-21-22-23-34.md','test-catalog/pokemon-rules-wp53-60-61-62-69-70.md','test-catalog/generic-kernel-wp05-06-07-08-09-10.md'],
 'gen7':['pokemon-rules/wp19-attributes-ability-and-stats.md','creature-rpg/wp20-hp-status-moves-helditem.md','creature-rpg/wp30-growth-learning-and-friendship.md','creature-rpg/wp33-daycare-and-breeding-session.md','creature-rpg/wp35-eggs-and-hatching.md','pokemon-rules/wp34-inheritance-and-offspring.md','test-catalog/creature-rpg-wp27-28-29-30-33.md','test-catalog/pokemon-rules-wp19-21-22-23-34.md','test-catalog/pokemon-rules-wp31-32-37-38.md'],
 'gen8':['creature-rpg/wp20-hp-status-moves-helditem.md','creature-rpg/wp26-acquisition-gifts-and-script-trade.md','creature-rpg/wp35-eggs-and-hatching.md','combat-requirements/wp39-battle-context-and-participants.md','combat-requirements/wp40-commands-obedience-and-action-order.md','pokemon-rules/wp38-capture-and-receiving.md','test-catalog/creature-rpg-wp18-20-24-25-26.md','test-catalog/creature-rpg-wp35-36-57-64-68.md','test-catalog/combat-requirements-wp39-40-41-42-45.md','test-catalog/demo-dx-wp72-73-74-75-76-77.md']}
frozen=load(T/'frozen-denominator.json');previous=load(T/'reception-ledger.json');target=load(T/'recovered-target/forward-mapping.json')
all_ident=load(T/'recovered-target/identities.json')['payloads']
contracts=load(T/'recovered-target/field-contracts.json')
interfaces=load(T/'recovered-target/interfaces.json')['interfaces']
central=load(T/'recovered-target/central-contract-projection.json')
recovery=load(T/'recovery.json')
prior_g={a['id'] for a in previous['atoms'] if a['receiver_status']=='FINITE_PREDICATE_RECEIVED_FOR_ROOT'}
pending_atoms={a['id'] for a in previous['atoms'] if a['id'] not in prior_g}
unread={r['id'] for r in previous['records'] if r['literal_status']=='AVAILABLE_UNREAD_NOT_RECEIVED'}
common=[]
for name,original in [
 ('project-AGENTS.md',REPO/'AGENTS.md'),
 ('eighth-global-review-prompt.md',ROOT/'inputs/eighth-global-review-prompt.md'),
 ('review-SKILL.md',ROOT/'inputs/review-SKILL.md'),
 ('parent-task-prompt.md',ROOT/'delegation/prompts/receive_external_pbs_creature_backups.md'),
 ('parent-readset.complete.json',ROOT/'delegation/readsets/receive_external_pbs_creature_backups.complete.json')]:
 data=gitbytes(CONTRACT,original);p=OUT/'common'/name;p.write_bytes(data)
 common.append(dict(identity(p),source_commit=CONTRACT,source_path=str(original.relative_to(REPO)),required='FULL_TEXT_READ'))
preserve=dict(schema='r8-pbs-preserved-reception/v1',utc=UTC,parent_publication=PARENT,parent_core=CORE,
 target=TARGET,target_checkout_tree='fd4d9ee5b2abcd583cd9e180c3f0502e7172e58e',target_task_tree='b840da3155ee4ade9414e313061f38a188f5ba3b',
 actual_prior_receiver='01a14465-b40a-7432-ba2a-27fb50ffa001',original_author='01a143b3-2169-7510-89e4-e6e3c9712029',
 preserved_literal_record_ids=[r['id'] for r in previous['records'] if r['literal_status'].startswith('FULL')],
 preserved_literal_record_count=2772,preserved_literal_fields=11872,preserved_omission_instances=2696,
 preserved_finite_G_ids=sorted(prior_g),preserved_finite_interfaces=['IF04','IF06'],
 preserved_XPCB001='NO_REQUIRED_BOUNDED_ALREADY_DOCUMENTED; full original/withdrawal/counter remains at parent fixed publication; no global closure',
 credit_rule='These are prior receiver-scoped facts, not a new read or vote by a shard. Never downgrade or overwrite them; fresh necessary source reads remain separately named. Parent retains task-final.',
 statuses=dict(task_final='OPEN_NOT_SIGNED',update='UPDATE_NOT_STARTED',behavior='NOT_EXECUTED'),
 root_counter_fixed_input=str(ROOT/'adjudication/root-xpcb001-already-documented-counterreview.v1.json'),
 source_ending_clarifiers=dict(compile_encounters=[658,765],pokedex_helpers=[302,352]),
 mandatory_metrics_clarification=dict(current_v2=str(ROOT/'tasks/developer_full_cloud/metrics-complete-contribution.v2.json'),
  old_v1=str(ROOT/'tasks/developer_full_cloud/metrics-complete-contribution.v1.json'),corrected_ids=['MET01','MET04','PBS02'],
  rule='lookup/SectionName/equality guard is form>0; path selection guard is form!=0. Retain v1 errors, v2 mandatory when using this finite provider.'))
dump(OUT/'common/preserved-reception.json',preserve);common.append(dict(identity(OUT/'common/preserved-reception.json'),required='FULL_CURRENT_QUALIFICATION_READ'))
specs=[
 dict(id='gen5',pids=['P02','P03'],fields=[1,30,31,32],gs=['G32'],ifs=['IF01','ELR-I03','CD-I06'],header='HC-BASE',
 title='第五代完整基础与形态；发现／编译／本地化与存档写入边界',
 scope='649基础＋86形态；全部原始有序Moves/TutorMoves/EggMoves/Evolution及完整Pokedex文本；Name/Category/Pokedex/Generation字段合同，发现/激活/编译/导出/本地化生产与完整存档写入前缀。',
 consumers='实际活跃parser/编译/导出与GameData；MessageTypes的set/add/get完整定义及必要调用；全量保存验证→Marshal写入及转换/装载必要定义；当前WP02/WP03/WP04/WP08/WP18及必要保存合同与对应向量。',
 shared='本片IF01/ELR-I03/CD-I06对其它代际原始值的消费，必须接收gen6/gen7/gen8逐字段事实；在未到之前只完成共同定义和本代接合，不等待其它片才开始主读。',
 routes=['KERNEL','DEVELOPER','MEDIA','PBS_CURRENT','PBS_BATTLE','PBS_WORLD']),
 dict(id='gen6',pids=['P06','P07'],fields=[2,3,4,5,6,7,8,10,16,17,25,26,27,28,29,33],gs=['G22','G24','G25','G26','G27','G28','G31'],ifs=['IF02','IF07'],header='HC-FORM',
 title='第六代完整基础与形态；动态形态、Mega、图鉴与保存对象',
 scope='721基础＋188形态；所有显式/继承/独立默认值和完整有序学习列表及文本；自然/隐藏能力、性别、Types、Mega、体型/颜色/栖息地、Flags、图鉴alias与动态读写。',
 consumers='完整Pokemon动态form/form_simple/species_data及setter，MultipleForms分派和每个被采用handler；Mega裸查询与战斗资格分开；PlayerPokedex普通登记/最近见到/浏览写入/保存对象与当前版本装载完整定义；必要资源getFormcaller。当前WP18/WP19/WP21/WP22/WP62及保存formal/向量。',
 shared='IF02/IF07使用其它代际数据时接收gen5/gen7/gen8的完整值贡献；本片拥有这些接口最终有界join，别的片只提供其本代producer值，不能重复签接口。FC29描述性Habitat的待接收facet归本片，不重开已收IF06点集合合同。',
 routes=['CREA_C','KERNEL','UI','PBS_CURRENT','HISTORY']),
 dict(id='gen7',pids=['P10','P11'],fields=[9,11,12,13,15,18,19,20,21,22,23,24,37,38],gs=['G29','G30'],ifs=['IF08','CD-I01'],header='HC-ENCOUNTER',
 title='第七代完整基础与形态；成长、学习、繁殖与进化',
 scope='809基础＋250形态；完整各级招式/教学/蛋招式/进化顺序与重复、文本、尺寸及全部字段；BaseStats/EV/BaseExp/Growth/Happiness/学习/蛋组/孵化/Incense/Offspring/进化合同。',
 consumers='GrowthRate完整六曲线与表/公式分界、Stat主能力顺序；Pokemon学习/重置/兼容/友好、Evolution完整必要方法和参数目录、编译前向合并/反向前身；Species血缘与DayCare/EggGenerator及必要孵化条件/handler。当前WP19/WP20/WP30/WP31/WP33–35及必要测试。',
 shared='IF08/CD-I01使用四代具体值，本片只主读本代，需接收其余三片的完整producer对象；G29/G30与FC37/38共同核查，但唯一所有权只在本片。HC-ENCOUNTER是额外头声明核对，不重复领取已读76遭遇记录。',
 routes=['CREA_C','PBS_CURRENT','HISTORY']),
 dict(id='gen8',pids=['P14','P15'],fields=[14,34,35,36,39,40,41,42,43,44,45],gs=['G11','G21'],ifs=['IF03','IF05','IF09'],header='HC-METRICS',
 title='第八代完整基础与形态；指标显示、遭遇与持物交界',
 scope='898基础＋339形态；完整全部字段/列表/图鉴文字、区域/evolution形态和实际同代基础继承；捕获输入、三野生持物池及metrics/遭遇字段合同的剩余facet。',
 consumers='已有2696metrics/76遭遇原值信用保留，仅补必要consumer/formal；完整shadow gate、动态资源getter、battle/hatch/trade必要消费；遭遇registry→snapshot→selector→Pokemon构造→实际WildBattle receiver，持物setter/identity/can_hold/persistence分开；当前WP15/WP18–20/WP36/WP38/WP39和combatpresentation必要条款/向量。',
 shared='IF03/05/09需其余三代的数据贡献，本片仅负责本代原值和接口共同定义/接合。IF04/06既有有限接收不重开，metrics provider v1→v2强制更正必须全文保留；不把shows_shadow?源码恒真扩成完整shadow已显示。',
 routes=['PBS_CURRENT','CREA_C','CREB','PBS_BATTLE','WORLD','UI','DEVELOPER'])]
all_records={r['section_id']:r for r in target['records']}
all_frozen={r['id']:r for r in frozen['records']}
artifacts=[];assignments=[]
for spec in specs:
 sid=spec['id'];d=OUT/sid;d.mkdir(parents=True,exist_ok=True)
 write=str(T.relative_to(REPO)/('shards/'+sid))+'/'
 wanted_fc={f'FC{i:02}' for i in spec['fields']}
 atoms=[a for a in frozen['atoms'] if a['id'].split('.')[0] in wanted_fc or a['id'] in spec['gs']]
 records=[r for r in target['records'] if r['identity_id'] in spec['pids']]
 node_ids={p for a in atoms for side in ['source','spec'] for p in [z['identity_id'] for z in a.get(side,[])]} | set(PREREQ[sid])
 necessary=[dict(id=k,**all_ident[k]) for k in sorted(node_ids)]
 additional=[dict(id='X-R-%02d'%(i+1),**repo_identity(Path('/workspace/pokemon-essentials'),R,path)) for i,path in enumerate(EXTRA_R[sid])]
 additional += [dict(id='X-B8-%02d'%(i+1),**repo_identity(REPO,B8,'deliverables/final-specification-set/'+path)) for i,path in enumerate(EXTRA_FORMAL[sid])]
 providers=[]
 for route in spec['routes']:
  for loc in central['providers'].get(route,[]):
   rel=loc['path'];path=ROOT/rel
   cp=subprocess.run(['git','show',CONTRACT+':'+str(path.relative_to(REPO))],capture_output=True)
   row=dict(route=route,logical_entrypoint=rel,prior_projection_locator=loc,
       purpose='定位与身份，不授整文件语义；采用的必要完整事实/条款/例子/字段和强制clarifier必须实际全文接收。无关外域原值不移交本片主责。')
   if cp.returncode==0:
    data=cp.stdout;row.update(commit=CONTRACT,path=str(path.relative_to(REPO)),mode='100644',bytes=len(data),sha256=hashlib.sha256(data).hexdigest(),blob=gid(data),availability='AVAILABLE_AT_FIXED_CONTRACT')
   else:row.update(availability='THIS_SPELLING_NOT_TRACKED_AT_FIXED_CONTRACT',credit=0,action='不能把缺导航当材料limit；按固定合同已恢复来源、源定义及实际后继locator继续，缺必要内容才具名OPEN。')
   providers.append(row)
 req=[]
 for row in recovery['files']:
  name=row['relative_to_target_task']
  if name in ['review.md','interfaces.json','proposals.json','gaps.json','execution.json']:usage='FULL_CURRENT_OPERATIVE_TEXT'
  elif name=='field-contracts.json':usage='OWNED_CONTRACTS_COMPLETE_OBJECTS; other contracts needed as complete prerequisites when used'
  elif name=='forward-mapping.json':usage='OWNED_RECORDS_COMPLETE_FIELDS_AND_OMISSIONS_PLUS_ASSIGNED_GLOBAL_ASSERTIONS; all raw literal values must separately be read at fixed R, hashes not values'
  elif name=='reverse-mapping.json':usage='OWNED_ATOMS_COMPLETE_ASSERTIONS_AND_EVIDENCE; exact duplicate assertion aliases one read'
  elif name=='central-contract-projection.json':usage='OWNED_INTERFACES_COMPLETE_ORIGINAL_OBJECTS_AND_ALL_NECESSARY_FIELD/PREMISE/PROVIDER_QUALIFICATIONS'
  elif name=='semantic-notes.json':usage='OWNED_TWO_PRIMARY_NOTES_AND_NECESSARY_DEPENDENCY_NOTES; note summaries do not grant original record reading'
  elif name=='reading-ledger.json':usage='EXACT_OWNED_RECORD_LOCATORS_AND_DECLARATION_QUALIFICATIONS; author FULL_READ is not receiver credit'
  elif name.startswith('tools/'):usage='INERT_REPORT_TOOL_IDENTITY; never execute recovered tools or accept generated PASS'
  else:usage='EXACT_IDENTITY/TRANSPORT/ADMINISTRATIVE_PURPOSE; business fields encountered are not exempt'
  req.append(dict(row,required_purpose=usage,parent_recovered_alias_commit=PARENT,parent_recovered_alias_path=str((T/'recovered-target'/name).relative_to(REPO))))
 rs=dict(schema='r8-disjoint-pbs-reception-readset/v1',utc=UTC,id='receive_pbs_remaining_'+sid,status='READY_FOR_PARENT_DISPATCH_NOT_STARTED',
 title=spec['title'],exclusive_write_set=write,branch='codex/r8-receive-pbs-'+sid+'-20261016',
 B8=dict(commit=B8,tree='751dfde81048c81390f89a65ca1d1a565ba8e1ca',formal_tree='f292698cdd4a8e725525a9be6dc34b75faaf151e'),
 R=dict(commit=R,tree='7589c800b61ba13a13040ed0d686979b80a84fd0',observed_cloud_origin='https://github.com/y805939188/pokemon-essentials.git'),
 parent_contract_commit=CONTRACT,parent_reception_publication=PARENT,parent_reception_core=CORE,target_commit=TARGET,
 target_checkout_tree='fd4d9ee5b2abcd583cd9e180c3f0502e7172e58e',target_task_tree='b840da3155ee4ade9414e313061f38a188f5ba3b',
 normative_inputs=common,original_target_inputs=req,owned_primary_files=[dict(id=k,**all_ident[k]) for k in spec['pids']],
 owned_records=[dict(frozen=all_frozen[r['section_id']],complete_target_forward_object=r,
   source_unit_sha256=hashlib.sha256((Path(all_ident[r['identity_id']]['repo'])/all_ident[r['identity_id']]['path']).read_bytes()[all_frozen[r['section_id']]['byte_offsets_half_open'][0]:all_frozen[r['section_id']]['byte_offsets_half_open'][1]]).hexdigest()) for r in records],
 owned_field_contracts=[c for c in contracts['contracts'] if c['id'] in wanted_fc],owned_atoms=atoms,
 owned_header=[h for h in frozen['headers'] if h['id']==spec['header']],
 owned_interfaces=[x for x in interfaces if x['id'] in spec['ifs']],
 complete_original_central_interfaces=[x for x in central['interfaces'] if x['id'] in spec['ifs']],
 source_and_formal_identities=necessary,additional_necessary_source_and_formal_identities=additional,
 prerequisite_scope_rule='各完整必要定义/调用/条款/向量按实际所用事实全文；不把本列表扩成外域全文件主责。新发现必要输入须冻结同等完整身份并补读，不能以本表封闭依赖。',
 all_identity_dictionary=dict(commit=TARGET,path=req[[x['relative_to_target_task'] for x in req].index('identities.json')]['remote_path_at_target_commit']),
 bounded_consumer_work=spec['consumers'],incoming_peer_contract=spec['shared'],provider_entrypoints=providers,
 object_ownership_rule='Record IDs, atom IDs, header declaration IDs and interface IDs are exclusively assigned. Source/formal definitions may be read by multiple shards; those are prerequisites, not duplicated votes/mandatory roots.',
 complete_definition_rule='Old numeric ranges are locators. Read every necessary definition through its real end, plus all actual necessary callers/receivers/clauses/premises. Compiler658–765 and UI302–352 clarifiers mandatory when those definitions used. No full foreign giant-file reassignment.',
 transport_rule='Reuse exact fixed-target recovered identities/bytes when already available; generation/hash/view/exit0 adds reading0. If absent restore only fixed C paths into own inert subdirectory, verify collection/mode/blob/bytes/SHA; never root cache/another author directory.',
 record_semantics_rule='Each source literal including complete ordered lists/repeats/prose and all explicit/omitted/default/inherited meanings must actually be displayed and understood. Lossless reversible views allowed; producing a view gives0 credit; truncation requires repair.',
 independence=dict(original_target_author='01a143b3-2169-7510-89e4-e6e3c9712029',parent_receiver='01a14465-b40a-7432-ba2a-27fb50ffa001',actual_shard_context='NOT_STARTED_NOT_ASSIGNED',requested=dict(model='gpt-6.1-sol',effort='ultra',tier='default',speed='normal',Fast='off'),actual='UNVERIFIED until authoritative echoes; never infer from request',no_self_spawn=True),
 outputs=['progress.json','identities.json','reading-ledger.json','record-reception-ledger.json','atomic-reception.json','interfaces.json','proposal-counters.json','report.md','lossless literal views as necessary','publication/readback receipts if authorized publication'],
 closure=dict(local='All owned record values/fields/defaults and all owned atomic/header/interface facts fully received with necessary source/current formal and actual nonauthor evidence, or exact INCOMPLETE remainder.',
 shared='Incoming peers only gate corresponding cross-generation full-interface closure; finish independent own primary work without waiting. Parent reads exact complete receipts and performs cumulative joins.',
 root='Only main thread signs canonical/task-final. No shard global PASS, no automatic aggregation to acceptance.',update_started=False,behavior_execution='NOT_EXECUTED unless actually observed safely and separately recorded'),
 counts=dict(records=len(records),fields=sum(len(r['fields']) for r in records),omissions=sum(len(r['omitted']) for r in records),atoms=len(atoms),headers=1,interfaces=len(spec['ifs'])))
 dump(d/'readset.complete.json',rs)
 prompt=f'''# 第八轮剩余完整接收：{sid} — {spec['title']}

这是主审可直接复制派发的完整有限审读合同；当前只是冻结派发材料，尚未实际启动任何 context。用户授权独立review专用报告证据普通提交/推送，不整改、不合并main。本包准确仓库相对根为 `{str(OUT.relative_to(REPO))}/`；本片完整readset为 `{str((d/'readset.complete.json').relative_to(REPO))}`；下文common均相对此包根，不相对prompt所在子目录。你必须是真实不同于目标作者 `01a143b3-2169-7510-89e4-e6e3c9712029` 的上下文；若冲突立即报告，不自验。当前实际 ID 未回显则 UNVERIFIED，不改角色名造独立性。不自行spawn。

先完整读取本包 `common/project-AGENTS.md`、`common/eighth-global-review-prompt.md`（36653 bytes，SHA256 63944b6f264a8e4ed1415db710443a0673f250b8a248af2274a425a314ea068b）、`common/review-SKILL.md`、`common/parent-task-prompt.md`、`common/parent-readset.complete.json`、`common/preserved-reception.json`，再完整读本片 `readset.complete.json` 及其引用的完整当前有效目标对象。各准确身份都在readset，不能只读本prompt摘要。全局prompt规定完整审查方法；本合同只把本片精确人口委派给你，不要求重审全系统。

父合同固定 `{CONTRACT}`，既有接收固定发布 `{PARENT}`、语义core `{CORE}`。唯一原目标 `{TARGET}`，checkout tree `fd4d9ee5b2abcd583cd9e180c3f0502e7172e58e`，原任务tree `b840da3155ee4ade9414e313061f38a188f5ba3b`。B8固定 `{B8}`、tree `751dfde81048c81390f89a65ca1d1a565ba8e1ca`、formal tree `f292698cdd4a8e725525a9be6dc34b75faaf151e`；R固定 `{R}`、tree `7589c800b61ba13a13040ed0d686979b80a84fd0`。自行映射实际checkout；不假定Mac路径或父会话/tmp缓存存在，不用同名分支未来HEAD替代固定提交。输入已在固定父发布完整恢复，可复用精确相同身份材料；缺本地材料时按固定原目标路径惰性恢复到自有目录并核全身份，禁止执行恢复旧脚本或游戏。

本片唯一写集 `{write}`，独立分支 `codex/r8-receive-pbs-{sid}-20261016`。父公共账本、dispatch合同、原目标、其它三片、正式规格、R、planning/audit、旧报告均只读。只写自身目录，不能修改其它贡献或替root签字。请求gpt-6.1-sol/ultra/default普速/Fast off；实际model/effort/tier/speed/Fast/UUID逐项无回显UNVERIFIED。实际开始/更新/结束UTC、平台context/执行入口及真实进程状态单列；派发计划不算已启动context。

你主读：{spec['scope']} 精确人口是 {len(records)} 条记录、{rs['counts']['fields']} 个显式字段绑定、{rs['counts']['omissions']} 个省略/继承处置；另有 {len(atoms)} 个独占待接收原子断言、1个头合同、接口 {', '.join(spec['ifs'])}。readset内是全部逐项ID和完整原始forward对象、字段合同、原子断言及原接口对象，不是摘要或抽样。不同人口不可相加为PASS分母。每个形态都必须结合**同代基础记录**接收所有具体继承值；不能用默认同内容、字段schema、名字、parser成功、同blob、旧PASS或原作者FULL_READ批量通过。

必须实际呈现并读懂所有有序列表、重复项、完整图鉴文字、字段参数/default/枚举、激活前提和正常/取消/失败/部分提交语义。可生成无损可逆分片，生成本身reading0；每片有源身份/行或字节首尾/结构ID/完整性和实际读取凭证，截断必须补读。不能把可得业务文字删成locator或typed-purpose。纯身份、重复定位、行政/传输JSON按精确对象/字段说明完整用途；原作者声明与本接收者实际读取严格分开。

必要消费者与当前条款：{spec['consumers']} readset数值范围是旧locator，必须读完整真实定义至结束行和全部必要caller/receiver；不把末尾恰有end当函数完整。若用Encounter编译或图鉴点计算，必须包括658–765与302–352后继clarifier。所有被采用provider贡献必须完整读其事实/七组八节/例子预期/反向条款及强制更正，未读producer不能签consumer。其它外域大文件不被整篇移交，但必要部分可得未读须具名OPEN，不能改标材料/宿主limit。

{spec['shared']} 四片的原始记录、192待接收断言、4头声明和10接口独占且无重叠；共享源定义/参考条款允许重复必要读取，不能重复增加主责/票数。已有2772字面记录、20个有限命题、IF04/IF06及XPCB001有限NO_REQUIRED原接收保留，别把重复别名算新阅读，也不降级原资格。你只补本片缺口；已有接受不替代你新采用事实的必要完整上下文。

每个对象交：完整当前有效意义、固定R/正式定位与原字节身份、实际读片/输出凭证、消费者接合、判定理由、未决及依赖。疑似缺口给最强NO_REQUIRED/当前跨篇覆盖/合理out-of-scope反证；新提案须完整双向证据、普通对照、最小反例、取消/失败/异常/部分提交、影响、最小修正规则/正确保留scope、同步/验收/回归/历史关系。提案作者不能兼作该新提案唯一独立反证者，交主审派发真正不同context。不要把原作者撤回当独立反证。历史optional/FLOAT/policy/limit/no-required分别保留，不选择用户批准、不重开第七轮27。

先完成所有独立可做工作，不因尚未收到其它片而停主读。每个跨代接口清晰分开共同定义/本代producer已收/其它代producer待收/消费者formal未收；有任何必要欠项时INCOMPLETE，不能签完整接口。不得以阶段检查点代替持续工作。若容量仍不足，给父精确未接对象与完整可直接派发材料，不伪造全部通过。

输出本片readset列举的实质中文报告与逐对象ledger，以及每条可恢复的完整字面视图/身份。正常运行、参考编译/导出/游戏/存档/宿主/媒体与行为向量未实际运行则NOT_EXECUTED，工具/传输与行为信用分开。现有源I/O和失败、旧错误及强制后继更正保留；不要倒填未知输出/exit。UPDATE_NOT_STARTED。

本片全部必要内容完备后，最多给 `READY_FOR_PARENT_FINITE_SHARD_RECEPTION`，主审累计读到所有贡献和跨代接口后才决定整个任务的 `READY_FOR_ROOT_TASK_FINAL_ACCEPTANCE`。你不签root canonical/task-final、不宣称B8全局PASS。用户已授权独立review专用报告证据普通commit/push；只普通发布自己的指定分支，不强推/main/tag/合并别人。完整远端逐文件mode/blob/bytes/SHA/集合/tree回读；精确不变输入可复用身份/传输缓存，但传输完成不替代实质接收。返回准确C/tree/任务tree、证据路径、精确已收/必要未收/不可得限制与实际配置。当前包的启动/授权来源为主线程实际派发，不由本文件虚构已启动context。
'''
 (d/'prompt.md').write_text(prompt)
 artifacts.extend([identity(d/'prompt.md'),identity(d/'readset.complete.json')])
 assignments.append(dict(id=sid,title=spec['title'],counts=rs['counts'],exclusive_write_set=write,branch=rs['branch'],
   prompt=identity(d/'prompt.md'),readset=identity(d/'readset.complete.json'),record_ids=[r['section_id'] for r in records],
   atom_ids=[a['id'] for a in atoms],header_ids=[spec['header']],interface_ids=spec['ifs'],status='FROZEN_NOT_STARTED',actual_context=None))
record_groups=[set(s['record_ids']) for s in assignments];atom_groups=[set(s['atom_ids']) for s in assignments];if_groups=[set(s['interface_ids']) for s in assignments]
assert set.union(*record_groups)==unread and sum(map(len,record_groups))==len(unread)==3940
assert set.union(*atom_groups)==pending_atoms and sum(map(len,atom_groups))==len(pending_atoms)==192
assert set.union(*if_groups)=={x['id'] for x in interfaces}-{'IF04','IF06'} and sum(map(len,if_groups))==10
assert sum(a['counts']['fields'] for a in assignments)==77195
assert sum(a['counts']['omissions'] for a in assignments)==72617
assert len({x for a in assignments for x in a['header_ids']})==4
for i,a in enumerate(assignments):
 for b in assignments[i+1:]:
  assert not a['exclusive_write_set'].startswith(b['exclusive_write_set']) and not b['exclusive_write_set'].startswith(a['exclusive_write_set'])
index=dict(schema='r8-four-disjoint-reception-contracts/v1',utc=UTC,status='READY_FOR_PARENT_DISPATCH_NOT_STARTED',
 original_contract=CONTRACT,parent_publication=PARENT,target=TARGET,
 preserved=dict(records_literal_read=2772,finite_G=20,finite_interfaces=['IF04','IF06']),
 remaining=dict(records=3940,source_bytes=4380019,explicit_fields=77195,omission_instances=72617,atoms=192,headers=4,interfaces=10),
 common_inputs=common,assignments=assignments,
 aggregate_rules=['逐项合并4个互斥record-ID集合，保留原2772/20G/IF04/IF06接收与真实原读者；不能加为不同语义分母或新票。',
 '192原子断言和4头声明各有唯一主责；共享源定义只计实际必要读，不重建canonical根因。',
 '每个接口只有一个join-owner，但四代producer值由四片提供；join-owner/父主审必须实际接收完整producer事实，不以路径/状态/哈希签consumer。',
 '先独立完成本片主读及共同定义，不因其它片未交付无限等待；仅对应全接口关闭受incoming阻塞。',
 '任何子片欠记录/字段用途/必要完整方法/当前clause/独立性/接口，父保持精确INCOMPLETE；全满足后父独占task-final。',
 '按真实不同context记录审者；本包只冻结合同，没有spawn、没有新增context、没有新投票、没有执行行为。'],
 pending_root_only=['实际启动和真实context分配','接收四片完整结果与所有incoming joins','root canonical / task-final decision'],
 new_contexts_started_by_this_task=0,behavior_execution='NOT_EXECUTED',update_started=False,
 publication_rule='This index and all prompt/readset/common identities are bound by the actual ordinary publication commit in the final dispatch receipt; no self-hash future commit embedded.')
dump(OUT/'index.json',index)
validation=dict(schema='r8-disjoint-split-contract-validation/v1',utc=UTC,status='PASS_CONTRACT_SET_INTEGRITY_ONLY',
 record_union_exact=True,records_pairwise_disjoint=True,atom_union_exact=True,atoms_pairwise_disjoint=True,interface_union_exact=True,interfaces_pairwise_disjoint=True,
 exclusive_writesets_nonoverlapping=True,preserved_reception_untouched=True,counts=[dict(id=a['id'],**a['counts']) for a in assignments],
 semantic_credit=0,new_contexts=0)
dump(OUT/'validation.json',validation)
# Manifest excludes only itself, including every complete prompt, readset, and common input.
files=[identity(p) for p in sorted(OUT.rglob('*')) if p.is_file() and p!=OUT/'payload-manifest.json']
dump(OUT/'payload-manifest.json',dict(schema='r8-dispatch-payload-manifest/v1',files=files,count=len(files),bytes=sum(r['bytes'] for r in files),excluded_self='Bound by final commit/tree and remote readback',semantic_credit=0))
print(json.dumps(dict(status=index['status'],assignments=validation['counts'],total_records=3940,total_atoms=192,total_interfaces=10,contexts_started=0),ensure_ascii=False))
