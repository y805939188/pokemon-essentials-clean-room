"""Package the root reviewer's explicit judgments, not automated battle verdicts."""
import datetime, hashlib, json, platform, subprocess, sys
from pathlib import Path
D=Path(__file__).resolve().parent; ROOT=D.parents[3]; PRE=D.parents[1]
def load(p): return json.loads(p.read_bytes())
def write(name,x): (D/name).write_text(json.dumps(x,ensure_ascii=False,indent=2)+"\n")
def ident(b): return {"bytes":len(b),"sha256":hashlib.sha256(b).hexdigest(),"git_blob":hashlib.sha1(b"blob "+str(len(b)).encode()+b"\0"+b).hexdigest()}
def canon(x): return hashlib.sha256(json.dumps(x,ensure_ascii=False,sort_keys=True,separators=(",",":")).encode()).hexdigest()
utc=datetime.datetime.now(datetime.timezone.utc).isoformat()
contract=load(PRE/'contracts/R6-U05.json'); bindings=load(D/'input-bindings.json'); checks=load(D/'independent-checks.json')
assert checks['failed']==0
common=load(D/'common-context.json'); vectors=load(D/'new-vectors.json')
M=contract['frozen_main']; A=bindings['author_commit']; R=contract['frozen_reference']
statusfile='deliverables/final-specification-set/pokemon-rules/wp44-statuses-stat-stages-and-immunities.md'
coverage='deliverables/final-specification-set/pokemon-rules/wp44-effect-coverage.md'
pcat='deliverables/final-specification-set/test-catalog/pokemon-rules-wp43-44-46-48-50.md'
ccat='deliverables/final-specification-set/test-catalog/combat-requirements-wp47-ab.md'
wp40='deliverables/final-specification-set/combat-requirements/wp40-commands-obedience-and-action-order.md'
wp47a='deliverables/final-specification-set/combat-requirements/wp47-a-move-attributes-targeting-and-calling.md'
wp47b='deliverables/final-specification-set/combat-requirements/wp47-b-switching-control-and-item-changes.md'
wp49='deliverables/final-specification-set/combat-requirements/wp49-ability-phase-triggers.md'
candidate_prefix=str((PRE/'candidates/R6-U05/mirror').relative_to(ROOT))+'/'
def clause(p,a,z):
 b=(PRE/'candidates/R6-U05/mirror'/p).read_bytes()
 return {'path':candidate_prefix+p,'commit':A,'lines':[a,z],'identity':ident(b),'complete_text':'\n'.join(b.decode().splitlines()[a-1:z])}
reviewer={'logical_id':'R6-U05-R','active_agent':'/root','role':'independent non-author reviewer',
 'author_logical_id':'R6-U05-A','authored_this_candidate':False,'authored_any_specification_in_this_review':False,
 'direct_semantic_reviewer':'/root','read_only_mechanical_assistant':'/root/provenance',
 'requested_configuration':{'model':'gpt-6.1-sol','effort':'ultra','service_tier':'default','speed':'default'},
 'actual_configuration':{k:'UNVERIFIED' for k in ['model','effort','service_tier','speed','platform_UUID']},
 'source_thread_id_supplied_by_user':'01a10d94-84b9-759e-aa1d-edb0d9b6d0e2',
 'UUID_boundary':'The supplied source thread identifies the parent delegation; it is not an observed current reviewer thread.started UUID.',
 'configuration_obstacle':'This delegated tool session exposes no effective model/effort/tier/speed or thread.started echo. No separate Codex CLI probe, config/credential access, installation, service start or safety-setting change was performed.'}
counter_dispositions=[
 {'id':'EV-4a01ea04bbfad749','disposition':'PRESERVE_ADJACENT_SCOPE','reason':'失去绑定与同名已有不可构造类是不同入口；原 fallback/call-control qualification 不转成这四个 ID 的新通过，也未扩修调用框架。'},
 {'id':'EV-6c715cbfbe689c97','disposition':'PRESERVE_OTHER_PRIMARY_BATCH','reason':'精神香草的 Disable 身份读取在其原生产局部成立；属于 U02 精确根因。U05 不重裁它，不借该反证取消 Charge/状态/Curse 的 required。'},
 {'id':'EV-42d8a9414199b4cb','disposition':'PRESERVE_OPTIONAL_BOUNDARY','reason':'默认选择范围未显示反射的可观察差异；仍是原 optional 范围，无新增强制修订。'},
 {'id':'EV-287952ed0a020e33','disposition':'INDEPENDENTLY_CONFIRM_BOUNDED_SE001','reason':'WP40 原有未定量清理名不能提供恰1清除和号令重复观察；Instruct 实际消费者可满足。新建2保留、非电/失手仍清与故障前缀均已独立回源。'},
 {'id':'EV-cbbcc85f98ee09e7','disposition':'INDEPENDENTLY_CONFIRM_BOUNDED_SE002','reason':'异常资格在内部随机抽取之前，纯电免疫跳过抽取；精神力在畏缩抽取之后拒提交。外层101与内层10及替身/强行/鳞粉入口分别保留。'},
 {'id':'EV-a71710b37eb3df21','disposition':'INDEPENDENTLY_CONFIRM_BOUNDED_SE003','reason':'精神转移直接查通用异常资格；梦话的普通外壳及特殊内层有实链。专用条款旁路不取消其它免疫门，也不证明普通冰冻者可发招。'},
 {'id':'EV-5029527e28d9a87a','disposition':'INDEPENDENTLY_CONFIRM_BOUNDED_CALL01','reason':'原 WP40/WP49 已承认重选；遗漏的是后期仅构造、不第二次重定向。保留初始幽灵的正常重定向和类型稳定 MA-T07–T10，不泛化为所有晚期目标。'}]
manual={
'R6-CM-SE-001':{
 'mechanism':'CHARGE 的效果先写计数2再请求特防变化；完整回合尾正计数递减。已到达的行动结束只清恰1，先于更晚 Instruct/Dancer；正计数是伤害威力因子的消费者。',
 'chain':'Charge 建立2 → 同行动末仍2 → 完整尾1 → 次轮普通 Thunderbolt 读1、威力因子2 → 行动末0 → 更晚合法 Instruct 沿真实槽重复读0、威力因子1。最近使用/普通历史与存活、可重复资格必须保留。',
 'normal':'SS43/44 保留新2和完整尾递减；SS45 首次与重复的2/1是威力因子，最终实际损失不必精确二倍。',
 'counterexample':'仅按回合计时会让同回合 Instruct 再读1；候选已修此差异。将清理改为电招成功消耗会错误保留非电/失手行动的1，或错误消耗新2。',
 'failure':'正常到清理点的非电招或失手仍1→0；此前故障不补清理，清后故障不回滚0。先前 PP、历史、伤害分别保留。完整尾未达不补递减。',
 'minimum':'WP44 §4、§8/K02 与效果覆盖、WP40 第18步写明恰1及其相位；添加 SS43–47。保留 WP43 正计数倍率和 WP42 完整尾递减，不引入额外电招耗时规则。',
 'clauses':[(statusfile,78,78),(statusfile,156,156),(statusfile,185,185),(coverage,112,112),(wp40,171,171)],
 'vector_ids':['SS'+str(i) for i in range(43,48)],
 'rebuttals':['尝试以 WP40 已有“蓄力残段清理”否定遗漏：未给恰1、2保留或重复结果，不足。','尝试认定号令无法形成消费者：固定 Instruct 排除与调用链允许给定普通 Thunderbolt；按最近普通/使用记录及真实槽进行，前提合法。','尝试以使用电招或伤害成功为清理门：行动结束写点没有这种条件。'],
 'limits':['Dancer 仅确认清理先于其阶段，不新增该链的可达具体用例；Instruct 为本最小可观察消费者。','无实际参考程序、模型或宿主执行；异常点只按已到达前缀推导。']},
'R6-CM-SE-002':{
 'mechanism':'三个牙类在具名附效回调内先检查状态资格，资格真才取状态随机值，再独立取畏缩值并交提交门。内部10经概率修正；默认外层数据101仍走其独立随机消费者。',
 'chain':'普通命中且计算伤害正 → 外层强行/鳞粉/概率门 → 回调替身和内部概率门 → 状态资格 → 条件状态抽取与提交/即时反应 → 畏缩抽取 → 精神力等提交拒绝。',
 'normal':'非电合格目标、内部5/99：麻痹提交及反应，畏缩失败，两次内部抽取。只改纯电：状态资格拒绝，5成为畏缩值，99保留，一次内部抽取。',
 'counterexample':'错误地无条件先抽状态会使纯电目标消费5、畏缩读99，后继随机流和畏缩状态均错；候选已明确短路。',
 'failure':'精神力拒畏缩不取消已消耗5；替身、内部概率0与普通外层强行/鳞粉抑制分别拒在各自入口。Lum 即治即耗后仍抽畏缩，最终无状态不抹此前提交。已做伤害/PP/历史不回滚。',
 'minimum':'修改 WP44 §6 牙类行及覆盖附表相应族；SS48–52 明确共同夹具与条件化内部0对照。保留 WP43 外层概率101/抽取与鳞粉、强行等门，不扩成所有复合附效的顺序。',
 'clauses':[(statusfile,122,122),(coverage,165,165)],
 'vector_ids':['SS'+str(i) for i in range(48,53)],
 'rebuttals':['尝试把概率101理解为无随机调用：外层仍先取值且101大于普通结果；与内部抽取分开。','尝试把异常免疫理解为先取随机再拒：固定短路资格检查在随机调用左侧，消费者实际不同。','尝试把精神力拒绝也计为未抽取：精神力处于畏缩提交门，已经抽取。','尝试以普通鳞粉穿过外层证明内部0：不能；候选把该用例限定为已到达内部的条件化对照。'],
 'limits':['随机5/99为固定可控输入的静态推导，不是实测随机日志。','未执行消息/动画或真实物品反应；只确认具名源链在假定正常返回时的提交顺序。']},
'R6-CM-SE-003':{
 'mechanism':'精神转移先要求用户原始异常存在，对目标直接使用通用异常资格。Sleep/Modified Sleep/Freeze Clause 附加队伍扫描只覆写专用睡眠/瞌睡/冰冻入口，不接该通用查询。',
 'chain':'普通梦话外壳先睡眠2→1且仍睡，PP5→4 → 唯一合法 Psycho Shift 候选，不在排除名单 → 特殊内层不扣原槽PP10且跳后段状态门（保留其它早期门） → 通用目标资格 → 新睡眠3提交及反应 → 用户治愈为NONE/计数0。最近使用可变内层，最近普通仍梦话。',
 'normal':'同队已有非蛋睡眠：普通专用睡眠拒，精神转移仍可到通用资格。无其它同队睡眠时两入口均可通过。目标新3不复制用户剩余1。',
 'counterexample':'若把专用条款队伍扫描普遍施于通用转移，则合法梦话链的目标拒绝、用户不治愈，和固定源不同；候选修正文与调用桥。',
 'failure':'目标受电场时通用门仍拒，用户已睡眠递减和PP保持且不自动治愈。Chesto 对目标即治即耗完成后再治用户。目标状态已写但提交反应未返回的故障不补用户治疗；晚于治疗的故障保留治疗。',
 'minimum':'WP44 §3.2 专用条款作用域与 §6 转移行；覆盖附表及 WP47-A 梦话入口补有界桥；SS53–59。保留其余状态、场地、目标成功门和原梦话候选限制；冻条款仅结构入口，不造普通冰冻发动保证。',
 'clauses':[(statusfile,54,54),(statusfile,124,124),(coverage,166,166),(wp47a,183,183)],
 'vector_ids':['SS'+str(i) for i in range(53,60)],
 'rebuttals':['尝试以睡眠用户不能普通发招否定可达性：普通梦话为合法外壳，内层特殊入口可到转移；原槽PP不减。','尝试以 clause 模块统一拦截状态否定旁路：只专用包装器扫描队伍；通用入口没有该扫描。','尝试把特殊使用写成跳全部守卫：睡眠外壳与内层早期/目标门不同，候选明示其余门保留。','尝试从最终两个NONE否定目标曾提交：目标提交、Chesto消费后才用户治疗，顺序可观察。'],
 'limits':['冻用例只假定已到达带真冰冻来源的精神转移目标入口，不认定普通冰冻者能选择或发动。','未实际执行条款/梦话/治疗回调或兼容宿主；主夹具的合法性和结果按固定链静态判定。']},
'R6-CM-CALL-01':{
 'mechanism':'初始非幽灵 Curse 为 User/空目标，通常重定向前门返回。普通PP/历史与初始整招门之后，Protean/Libero 改成幽灵会清预选并只重新构造 RandomNearFoe 列表；该晚分支没有第二次重定向，后续目标成功门仍执行。',
 'chain':'L 夹具纯Water U0/有效Protean/CursePP5/HP101 → 初次空目标 → PP4/历史 → 非幽灵三阶级整招资格真 → Ghost提交 → 随机重建席3 → 目标门通过 → 席3咒真 → 自己扣 floor(101/2)=50，HP51；席1Follow Me未二次消费。',
 'normal':'起始Ghost控制仍初次随机3后Follow Me到1；去Protean的Water控制只速度−1/攻击+1/防御+1且无HP代价。MA-T07–T10 类型稳定原行字节保留。',
 'counterexample':'将初始构造+重定向规则再次套在晚重建会咒席1，和固定晚分支的席3不同。WP40/WP49 已有重选事实，所以本项是有界澄清和覆盖，不夸成原规格全局矛盾。',
 'failure':'三请求都饱和不可变时初始整招门先拒，PP4/历史仍存且尚无Ghost。晚席3已咒则目标门拒，Ghost/PP4已写，HP101且不重新去席1。施咒写后、HP写前故障只保留咒/类型/PP/历史，不补HP51；HP写后故障保留51。',
 'minimum':'WP47-A §5.1新增有界晚路径；WP47-B Curse、WP40 第14步、WP49 Protean/Libero 行同步；MA-T11–16。保留初始幽灵重定向、非幽灵阶级门、独立目标成功门，不禁止所有晚期目标重定向。',
 'clauses':[(wp47a,157,158),(wp47b,61,61),(wp40,167,167),(wp49,239,239)],
 'vector_ids':['MA-T'+str(i) for i in range(11,17)],
 'rebuttals':['尝试以 Curse 初始动态目标已明示取消本项：原初次路径正确；候选仅补晚分支不再重定向。','尝试把初始整招检查移到Protean之后：固定顺序先整招资格后改型，所以饱和控制不会Ghost。','尝试把“仅重建”理解为跳目标成功门：固定后继仍检查；晚席3已有咒时不会付HP。','尝试质疑纯Water+Protean+Curse输入：固定Gengar可用Curse及Skill Swap，既有浸水/允许交换可构成指定状态；不把获取链当已执行。'],
 'limits':['合法状态取得链仅作输入域证据，未运行完整获取过程。','Libero 按固定同分支源确认；本正常可观察夹具为Protean，不声称另一个实测Libero向量。','没有宿主消息/动画或异常恢复实测。']}}
vector_reason={
'SS43':'建立2在行动末恰1清理门不命中；特防请求在计数写后。',
'SS44':'完整尾到达才对正2减为1，与行动结束分期。',
'SS45':'初次伤害前1为正，清理写0先于更晚真实槽号令；倍率读值分别2/1，PP与历史有实入口。',
'SS46':'清理门只检查恰1，非电与失手没有额外排除；无需号令。',
'SS47':'限制故障前尚未有计数改写，不能倒补未达写点；后故障保留0。',
'SS48':'资格真后5进入麻痹及即时反应，再99畏缩失败；内部2次。',
'SS49':'更多类型效果真且纯电令资格假，状态抽取短路，5成为畏缩，99未用。',
'SS50':'精神力位于畏缩提交门；5仍已消费，最终畏缩假。',
'SS51':'替身和内部0是内部回调返回，强行/有效鳞粉为普通外层门；三入口不能合并消费计数。',
'SS52':'Lum 消费在状态提交之后的即时治疗链，仍在畏缩99之前，最终NONE不抹前缀。',
'SS53':'专用睡眠包装器在原查询前扫同侧非蛋真睡眠；前PP/历史不回补。',
'SS54':'外壳真睡眠2→1仍可梦话，PP5→4；合法内层无原槽PP扣除，目标新3先提交，之后U治愈。',
'SS55':'通用门仍查询阻睡电场；目标拒绝在用户治疗之前，既有外壳计数/PP/历史不回滚。',
'SS56':'Chesto 即时治目标并消费，目标提交正常返回后仍执行用户治疗，两个NONE含前缀。',
'SS57':'目标提交已发生而回调未返回，用户治疗在后未达；不同故障点分别保留已经治疗的前缀。',
'SS58':'清同队已有睡眠后专用条款不拒，通用入口仍受相同其它资格，双方新时长从提交取。',
'SS59':'专用冻结条款与通用冻资格的入口结构差异成立；未宣称普通冰冻发动可达。',
'MA-T11':'初空目标导致初次重定向前门返回；PP/整招资格后改Ghost，晚重建只构造3，先咒再扣50。',
'MA-T12':'初Ghost已经单敌目标，正常Follow Me在初次重定向将3改1；晚例外不适用。',
'MA-T13':'无有效Protean则不改型或晚重建；非Ghost全局三阶级按原顺序请求，无HP代价。',
'MA-T14':'三请求全不能变化先在整招门失败，PP4已写，Protean尚未到。',
'MA-T15':'晚目标成功门读席3已有Curse而拒；不存在第二次Follow Me或正常HP扣除，Ghost保留。',
'MA-T16':'目标咒先于HP扣除；故障按实际达到的写点限制，不补后继完成或恢复。'}
fixtures={'C':clause(pcat,251,253),'F':clause(pcat,263,263),'P':clause(pcat,273,273),'L':clause(ccat,156,156)}
for v in vectors:
 v.update({'static_result':'PASS_STATIC_DERIVATION','independent_reason':vector_reason[v['id']],
           'fixture_key':'L' if v['id'].startswith('MA-') else 'C' if int(v['id'][2:])<48 else 'F' if int(v['id'][2:])<53 else 'P',
           'actual_reference_result':'NOT_EXECUTED','actual_model_result':'NOT_EXECUTED','actual_host_result':'NOT_EXECUTED'})
write('vector-review.json',{'utc':utc,'level':'DERIVED_VECTOR','fixtures':fixtures,'vectors':vectors,'count':23,'executed':0})
per_id=[]
for n,s in enumerate(contract['scope_contracts']):
 id=s['id'];v=manual[id]
 relevant=[x for x in bindings['candidate_files'] if x['formal_path'] in s['minimum_revision_contract']['candidate_formal_write_set'] or any(x['formal_path']==p for p,_,_ in v['clauses'])]
 g={
 'identity_and_verdict':{'canonical_id':id,'aggregation_aliases':s['aggregation_aliases'],'classification':'required','severity':'P2','root_cause_key':s['identity_and_verdict']['root_cause_key'],'result':'PASS','event':'CANDIDATE_PASS','verdict_scope':'Exact frozen U05 candidate only; SOURCE_STATIC and unexecuted derived vectors.','minimal_necessary_revision':[],'new_task_requirements':[]},
 'bidirectional_evidence':{'mechanism':v['mechanism'],'producer_to_consumer_chain':v['chain'],'source_locators':[x for x in bindings['contract_sources'] if x['id']==id],'candidate_clauses':[clause(p,a,z) for p,a,z in v['clauses']], 'negative_evidence_scope':'The eight complete formal baseline bodies/catalogs and their complete candidate differences, plus explicitly bounded necessary consumer reads in reading-ledger.jsonl. No universal negative over other formal/source files.','counter_dispositions':counter_dispositions,'candidate_payloads':relevant},
 'premises_and_counterexample':{'legal_input_and_common_fixtures':fixtures,'required_vector_ids':v['vector_ids'],'ordinary_control':v['normal'],'minimal_counterexample':v['counterexample'],'failure_cancel_partial_commit':v['failure'],'level':'SOURCE_STATIC/DERIVED_VECTOR','executed':False},
 'minimum_revision_contract':{'assessment':v['minimum'],'correct_scope_preserved':'All original SS01–42 and MA-T01–10 rows remain exact bytes; unchanged surrounding formal rules reconstructed from full baseline plus complete diff.','additional_fix_required':[],'candidate_differences':'candidate-diff.patch','formal_files_modified_by_reviewer':False,'compatibility_decision':'Accurate fixed-R behavior; no future permanent defect-profile choice.'},
 'acceptance_and_regression':{'result':'PASS_STATIC','vectors':[x for x in vectors if x['id'] in v['vector_ids']],'historical_current_spans':'historical-span-checks.json: 33 qualified associations, 32 exact contiguous spans and one Sleep Talk sentence-preserving addition.','older_qualifications':'41 full selected qualification objects read and independently matched to fixed source containers/JSON pointers; no whole-ID historical verdict transfer.','activation_qualified_selection':'activation-qualified.json: six affected exact R5 selections; 92 CLOSED/OPEN0 is fifth-round state only.','necessary_consumers':s['dependencies_and_receivers']['original_dependencies'],'unexecuted_layers':v['limits']},
 'independent_adjudication':{'reviewer':reviewer,'counterattempts':v['rebuttals'],'adjudication':'支持本固定候选 PASS；未发现需改作者镜像的实质问题。原反证及其历史状态不覆盖当前根裁决。','author_429_checks':'Author-only tool validation, not behavior execution and not inherited as review PASS.','independent_tool_validation':{'checks':checks['count'],'passed':checks['passed'],'failed':checks['failed'],'level':'TOOL_VALIDATION','semantic_verdict_source':'This root reviewer, not the checker or mechanical assistant.'},'execution_limits':v['limits']},
 'dependencies_and_receivers':{'primary_batch':'R6-U05','candidate_root':str((PRE/'candidates/R6-U05').relative_to(ROOT)),'blocking_author_dependencies':[], 'nonblocking_domain_dependencies':contract['nonblocking_domain_dependencies'][id], 'formal_receiver_and_sole_writer':'R6-I, parent /root supplied in prompt; this reviewer is not formal writer.', 'all_file_receivers':common['file-conflict-graph.json']['data']['file_receivers'],'shared_conflicts':common['file-conflict-graph.json']['data']['edges'],'integration_requirements':'Receive necessary differences serially; WP40 combines U02/U05/U13 and pokemon catalog combines U02/U05. Independent actual integrated full-file and interface/history review remains pending.','closure_gate':contract['closure_gate'],'integrated_PASS':'NOT_PERFORMED','formal_acceptance':'NOT_PERFORMED','CLOSED':'NOT_REGISTERED'}}
 per_id.append({'id':id,'original_scope_contract_binding':{'commit':bindings['prepare'],'path':bindings['contract']['path'],'payload_identity':{k:bindings['contract'][k] for k in ['bytes','sha256','git_blob']},'pointer':'/scope_contracts/'+str(n),'canonical_record_sha256':canon(s)},'frozen_complete_contract':s,'seven_groups':g})
verdict={'schema':'r6.u05.independent-candidate-review.v1','utc':utc,'reviewer':reviewer,'candidate_binding':{'prepare':bindings['prepare'],'author_commit':A,'author_workspace_tree':bindings['author_workspace_tree'],'candidate_directory_tree':'6b8fbad358e45857d572d6f0924041b3bf17b3e2','mirror_tree':bindings['mirror_tree'],'author_branch':'codex/remediation-sixth-r6-u05-author-20261014','formal_main':M,'formal_tree':'1046fbb657882e84b3dfc6d017943a9edf7782e5','reference_R':R,'reference_tree':'7589c800b61ba13a13040ed0d686979b80a84fd0','complete_input_bindings':'input-bindings.json'},'result':'PASS','candidate_event':'CANDIDATE_PASS','required_count':4,'passed':4,'failed':0,'minimum_necessary_revisions':[],'integrated_PASS':'NOT_PERFORMED','formal_acceptance':'NOT_PERFORMED','CLOSED':'NOT_REGISTERED','per_id':per_id,'execution':'execution.json','publication':'Semantic core and final publication identities will be bound externally after ordinary commit/push and complete pinned remote readback. No prefilled self identity.'}
write('verdict.json',verdict)
reading=[json.loads(x) for x in (D/'reading-ledger.jsonl').read_text().splitlines()]
structured=[json.loads(x) for x in (D/'structured-reading.jsonl').read_text().splitlines()]
write('reading-completion.json',{'utc':utc,'prompt':{**bindings['prompt'],'lines':4290,'semantic_read':'Complete: preamble/tail read as prose; both complete JSON blocks read in lossless compact representations, with all four full scope contracts and all 115 recovery bindings. Whitespace is not semantic content.','preamble_relogged_lines':[1,153],'early_body_and_tail_command_UTC':'NOT_CAPTURED; retained platform tool echo, not retroactively invented.'},'contract':{**bindings['contract'],'semantic_read':'FULL_ALL_FIELDS including original_full_proposal and non_proposer_packet_scope_correction; embedded equality independently checked.'},'formal_full_reads':[{k:r[k] for k in ['formal_path','formal_commit','formal','formal_full_semantic_read','candidate_read']} for r in bindings['candidate_files']],'candidate_difference':'Complete eight-file candidate-diff.patch; all modifications read. Later SS43–59 and MA-T11–16 full fixture blocks independently re-read and logged.','source_read_ranges':[{k:r[k] for k in ['utc_start','utc_end','kind','path','commit','identity','read_range','line_count']} for r in reading if r.get('exit')==0 and r['kind']=='source'],'related_formal_boundary':'WP42 tail, WP43 Charge/probability and WP50 immediate cures read as bounded necessary consumers, not a claim that all their unrelated text was read.','counter_evidence':bindings['counter_evidence'],'historical_scope':'41 complete selected qualification containers; 6 selected R5 required scopes; 33 current association spans; exact closure records 59–61/63–65 and selected activation/exclusions metadata. Large original container full bytes fetched/hash-checked; unselected records not semantically certified.','structured_read_ranges':[{k:r[k] for k in ['utc','path','bytes','sha256','character_range','representation_characters','exit']} for r in structured],'first_logged_read_UTC':min(r['utc_start'] for r in reading),'stdout_truncation_recovery':'Oversized early displays did truncate; affected contract/counter/source/qualification/diff parts were re-read in smaller complete slices. Stored whole stdout and hashes alone are not claimed semantic reading. Common-context receiver projection initially treated a dict as a list; corrected own projection to all eight exact dict entries and re-read complete resulting representation.'})
write('execution.json',{'schema':'r6.u05.independent-review-execution.v1','utc':utc,'cwd':str(ROOT),'review_branch':subprocess.check_output(['git','branch','--show-current'],cwd=ROOT).decode().strip(),'reviewer':reviewer,'tool_python_runtime':sys.version,'runtime_platform':platform.platform(),'reference_object_store_expected':'/workspace/pokemon-essentials-reference-r6','reference_object_store_actual':'ABSENT','author_temp_cache_expected':'/tmp/r6-u05-frozen','author_temp_cache_actual':'ABSENT','source_recovery':'Full pinned raw GitHub payloads, checked bytes/SHA256/Git blob against frozen inputs before range reading. Source mode/type/tree carried from fixed identity index; supplementary GitHub API tree retrieval was blocked by proxy 403 and is not claimed successful.','new_execution_counts':{'reference_or_isolated_original_definitions':0,'reference_observation_with_surrogates':0,'independent_full_behavior_model':0,'full_host_Demo':0,'real_save':0,'production_service':0,'derived_vectors_executed':0,'derived_vectors_reviewed':23},'tool_validation':{'latest':checks['count'],'passed':checks['passed'],'failed':checks['failed'],'boundary':'Finite identity, byte preservation, coverage and qualified JSON pointer checks; never a battle execution.'},'retained_attempts':[{'attempt':'independent-check-01','independent_exit':1,'result':'238/241 checks passed; three reviewer descriptor failures','reason':'Wrong recovery-dictionary expectation116 (actual115); exact old-line matching rejected the sentence-preserving middle insertion in Sleep Talk and its aggregate. Candidate bytes unchanged; fixed descriptors, retained independent-checks-attempt-01.json and raw commands.'},{'attempt':'independent-check-02','independent_exit':1,'result':'Supplemental GitHub API tree request failed with proxy tunnel403','reason':'Original raw error retained in commands/independent-check-02.json; did not affect available pinned source raw payloads. No security/credential/network configuration changed.'},{'attempt':'independent-check-03','independent_exit':0,'result':'261/261 finite tool checks pass after descriptor/fetch-boundary correction.'},{'attempt':'late WP43 lookup','independent_exit':1,'result':'Wrong guessed basename; git show exited128','recovery':'Resolved actual wp43-types-accuracy-and-damage.md via rg --files, re-read needed153–168; ledger preserves failed attempt.'},{'attempt':'activation projection reader missing range arguments','independent_exit':1,'result':'IndexError before record write','recovery':'platform tool stdout/stderr retained; no false completion.'},{'attempt':'activation projection reader upper bound14000','independent_exit':1,'result':'AssertionError actual compact length3343','recovery':'Successful full0–3343 read in structured-reading.jsonl; no candidate change.'}],'author_failures':'Author wrong-ref source attempt, descriptor/selector validation failures and orchestration/path lookup failures retained in frozen author evidence; not repeated as our execution.','early_root_command_provenance':'Some initial read/projection commands have platform tool outputs but no separate local UTC/stdout/stderr/exit record. NOT_CAPTURED; do not reconstruct from mtime or later regeneration. Logged readers and run-owned.py retain actual UTC/argv/cwd/stdout/stderr/independent exit thereafter.','assistant_boundary':'Read-only provenance checks only; no scripts from author executed, no candidate/formal/report write or git mutation by assistant. Root performed all semantic judgments directly.','future_host_recovery_conditions':'A specifically authorized compatible battle host and required project resources, controlled state/random inputs, exact reference identity and safe isolation would be needed to establish runtime behavior. This is an execution limit, not a new mandatory revision.','write_boundary':str(D),'actual_formal_public_ledger_author_mirror_edits':False,'reference_edits':False,'main_merge_force_delete_Mac_operations':False})
write('historical-review.json',{'utc':utc,'level':'SOURCE_STATIC/TOOL_VALIDATION','current_associations':'historical-span-checks.json','assessment':'32 continuous old spans retain exact bytes; Sleep Talk old sentences remain in order with one bounded transfer-entry addition. Direct overlapping prior move-calling guards and variable target controls manually reviewed against new rules. No source/domain-wide prior PASS is reused.','R5_selected':load(D/'activation-qualified.json'),'qualified_41':'Complete selected-historical-scopes.json was read; independent-checks.json compares every frozen record and qualification hash/pointer and exact partial fields.','qualified_relations':{'GR4-M04/05/06':'WP40 old REG97–110/navigation overlap only; unrelated dynamic-form, fainted Ether and power-item claims stay in original scope.','GR3_related':'SPINDA, size, hidden-item and EXP-display links are navigation; action refund/NG first-error old behavior remains unchanged.','legacy_controls':'Specific original controls for guard exceptions, literal clauses, early prerequisites/obedience, weight, direct items, U-turn/Ice Face, stat/PainSplit/count/Curse behavior and clean-room ownership retain exact qualifications.','legacy_contributions':'B09/B10/B11/B21 partial contribution bindings remain distinct id+record_key+owner+qualified-scope tuples; no whole-ID transfer.'},'global_historical_boundaries':{'R1':'original WP ranges only; no invented total','R2':'229 controls /21 batches /341 exact contributions retained separately','R3':'23/76; M09 optional, historical U08 not started, M02 NO_REQUIRED remain scoped','R4':'current17/76 differs from B5 original16/75; Summary residue qualification only','R5':'unique selected92 CLOSED/OPEN0,51P2/41P3; 410native/568schema/158extra and21shared/18edges/85sole;262original,6admin,3correction distinct','failure_history':'candidate01 G03/G09 FAIL, oldU03 FAIL/repair, two advisory MISMATCH and SC-U07-001 LF error/correction retained; oldOPEN/WAIT snapshots do not reopen activated states','R6':'65=56required/8optional/1no-required; Float recurrence extra facet,7policy and14limits separate. No additional U05 tasks.'},'policies_and_limits':'Common-context preserves compatibility boundary and all14 limits; no policy/profile selected and no native execution claimed.'})
report='''R6-U05-R 独立候选复审：PASS（4/4）

本结论只适用于冻结作者发布 `64c77cf1733ab7db300e9f5ac7c79a2886c8ac68` 的八份镜像。作者 workspace tree 为 `1cf207996da85adaa677a5a3bcb2c7cf47fd8859`，候选目录 tree 为 `6b8fbad358e45857d572d6f0924041b3bf17b3e2`，mirror tree 为 `ecc24a2e991ba0eaaf1964ceaa076af551846778`。准备基准为 `469a268b92daed7b4d28d7fd0da75520cbb7228f`；正式输入仍是 `8ea169fbd0f33f378b5d732fd6bea59e854e04a6`，R 仍是 `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`。逐载荷 bytes/SHA256/blob/path/mode 见 [input-bindings.json](input-bindings.json)。没有需退回作者的最小必要修订。

`/root` 是本次直接语义审者，未撰写候选或正式规格；`/root/provenance` 仅协助只读机械身份核验。已先读适用根 AGENTS，写入仅在本审查目录。完整审者提示词268511 bytes、SHA256 `3896335f207f8a52a722b2830692b4479acea9b569e1c0224f2e4aca5ab4c49e`、blob `829e21d41537cc0dd9e3e612e3233675583a2a15`；完整合同及原提案、反证、四 ID 七组、115 个恢复绑定均按完整字段审读。八份相关正式正文/目录全文与全部候选差异已读；必要源上下文及后继消费者独立回源。详细读区间与早期未捕获元数据见 [reading-completion.json](reading-completion.json) 及两份原始阅读台账。报告没有以搜索、hash、作者摘要或作者429项静态检查代替语义审核。

| canonical ID | 裁决 | 新向量 | 关键复审结果 |
| --- | --- | --- | --- |
| R6-CM-SE-001 | PASS / required P2 | SS43–47 | Charge 新建2、完整尾减1；已到达行动末仅清恰1，先于号令重复消费，非电和失手也清 |
| R6-CM-SE-002 | PASS / required P2 | SS48–52 | 异常资格拒绝会跳过状态内部抽取；随后独立畏缩抽取，精神力拒提交仍消费随机值 |
| R6-CM-SE-003 | PASS / required P2 | SS53–59 | 精神转移通用资格不接专用睡眠/冰冻条款扫描；合法梦话实链保留外壳PP、状态门与目标先提交顺序 |
| R6-CM-CALL-01 | PASS / required P2 | MA-T11–16 | Protean/Libero 后期 Curse 仅重新构造目标，不再重定向；独立目标成功门仍执行 |

Charge：固定 Stats 203–214、UseMove 97–112/519–540、UsageCalculations 350–352、EndOfRound 713–727 及 Instruct 563–646 共同支持规则。合法夹具中首次 Thunderbolt 读1、威力因子2，行动末清0后更晚号令读0、因子1；不把最终损失说成恰两倍。已尝试以 WP40 原“蓄力残段清理”否定遗漏，它未给恰1/保留2/重复结果。候选在 WP44 §4/§8、覆盖附表与 WP40 第18步补正文及向量；原 WP43 倍率、WP42 完整尾正确范围保留。清理前故障不补清除，清理后故障不回滚已写0，先行PP/历史/伤害保留。

牙类：三个具名回调与通用状态/畏缩门、UseMove 外层和概率消费者均已读。更多类型效果开启、内部值5/99时，合格普通目标先麻痹后畏缩失败，内部2次；只改纯电免疫便跳异常抽取，5用于畏缩，99留给后继，内部1次。精神力在畏缩提交门拒绝，已取5不退回。默认外层101仍有自己的抽取，内部10仍经概率修正；替身/内部0与强行/有效鳞粉外层抑制分属不同入口，未拿“内部0”虚构普通穿过同一鳞粉。Lum的即时治愈/消耗先于后续畏缩值，最终无异常不抹提交。正文、附表及SS48–52一致，不推广为所有附效顺序。

精神转移：固定 BattlerOther 339–379、Statuses通用查询、Clauses专用包装器、SleepTalk 1136–1200、UseMove调用与SuccessChecks睡眠门组成实链。用户真睡眠2经普通梦话外壳减为1且PP5→4，合法唯一转移候选的特殊内层不再减睡眠/不扣原槽PP10；目标通用资格不扫描同队条款，新睡眠3先提交并完成反应，之后用户治愈NONE/计数0。专用睡眠对照因同队非蛋真睡眠拒绝，通用电场/其它免疫仍可拒绝转移。Chesto即治即耗后仍治用户；目标提交回调未返回时故障不补用户治愈。冻结来源对照只证明假定已到达入口的结构差异，未承诺普通冰冻者可发动。WP44 §3.2/§6、覆盖和WP47-A梦话桥与SS53–59一致，没有写成所有特殊调用免除全部守卫。

Curse：UseMove初次构造/重定向、PP/整招检查、347–363后期分支，Targeting全文件和Curse/Protean具名源已独立读。Water+有效Protean的普通双打夹具初次空目标，初门后改Ghost，只重建随机席3；席1Follow Me未再消费，席3先咒，HP101扣50至51。初始Ghost控制仍正常重定向至席1；无Protean控制只有三阶级变化。三请求饱和则初门拒在改型前；席3已咒则晚目标拒，PP4/Ghost已写、HP仍101。施咒后HP前故障只保留已到前缀。原WP40/WP49已有重选事实，所以本项是有界澄清与覆盖；WP47-A/B、WP40第14步、WP49行及MA-T11–16一致，MA-T07–10类型稳定范围不扩大。

七份原反证逐份全文读、核固定身份并保留处置。四项对应反证的条件和局部资格由本审者重新回源确认；另外三份分别保留 fallback/collision 的邻接范围、U02精神香草根因及反射 optional 边界，不产生新U05任务。每项新反证尝试、源→消费者→候选正文反向定位、正常/反例/故障及最小规则在 [verdict.json](verdict.json) 的独立七组中展开；完整原合同也逐项封装，没有只填PASS字段。

23个向量均为未执行的独立静态推导，完整共同夹具、逐行输入和独立推理见 [vector-review.json](vector-review.json)。独立工具最后261/261检查只核载荷、覆盖、旧字节及JSON资格；作者429项检查也只属工具层。第一次独立工具的3个失败为审者描述器问题（115误记116、梦话中间加句误判连续整行及其汇总），第二次补充API树元数据请求受代理403阻止，原失败和修正记录均保留；没有改候选以使检查通过。

历史回归限定到实际受影响范围：33条第五轮当前span关联（含重叠范围）中32个连续原文不变，梦话一个span原句依序保留并追加有界入口。41个较早完整资格投影已读，三份固定大容器全文载荷与41组 record/qualification 指针、hash、owner和局部贡献对象逐一核验。原SS01–42与MA-T01–10测试行字节全保留。R1原WP范围、R2 229/21/341、R3 23/76、R4当前17/76与B5 16/75、第五唯一92 CLOSED/OPEN0与原失败/optional/policy/limit都保留精确资格；不把旧整ID、整文件或PASS移交为新行为证据。六个受影响第五条目的精确选择及排除范围见 [activation-qualified.json](activation-qualified.json)；其余历史限定见 [historical-review.json](historical-review.json)。

正式共享写者仍为R6-I。WP40须组合U02/U05/U13，pokemon测试目录须组合U02/U05；其余六份本批镜像也须按实际接收差异绑定。候选准备无跨批阻塞，不消除整合后的共享全文、接口、历史资格复审。此报告没有修改实际正式稿、作者镜像或公共台账，没有合并main、force、删除或操作Mac。CANDIDATE_PASS 不代表 INTEGRATED_PASS、正式接受或 CLOSED，后三项本次均未执行。

执行限制：要求gpt-6.1-sol/ultra/default/default，实际model/effort/tier/speed/platform UUID没有有效回显，均UNVERIFIED；没有另开CLI补探。预期参考对象库与作者临时缓存在本环境缺失，固定raw源全文可得且核bytes/SHA/blob；源mode/type/tree取冻结索引，补充API树读取未成功，不伪称独立API确认。原参考定义执行、替身观测、独立完整行为模型、完整宿主/Demo、真实save与生产服务均0。缺宿主不阻断本次有限静态验收；真实运行、媒体与宿主恢复仍未知。完整实际/缺失元数据和失败账见 [execution.json](execution.json)。报告固定core及最终发布身份由真实提交和完整远端回读后的外部回执绑定。
'''
(D/'review.md').write_text(report)
print(json.dumps({'utc':utc,'result':'PASS','required':4,'derived_vector_count':23,'tool_checks':checks['count'],'reference_execution':0,'actual_configuration':'UNVERIFIED'},ensure_ascii=False))
