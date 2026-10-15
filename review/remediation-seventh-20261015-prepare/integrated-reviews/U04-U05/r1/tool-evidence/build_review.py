"""Serialize this reviewer's content judgments and exact input/reading anchors."""
from pathlib import Path
import datetime,hashlib,json,os,subprocess
OUT=Path(__file__).parent.parent
TOOLS=OUT/'tool-evidence'
P='review/remediation-seventh-20261015-prepare/'
B='e646432c644dec04d306842cc5a559a29c718fbc';MI='b0eea808887a688d52d28390ac8886fed9c10bcf';FI='d9021aa2d704476f644ef15f1a3b8291653ff8f1';D='95c260d8f3fb4a171675dde877137fcd4c2f1c8d';R='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
def get(c,p):return subprocess.check_output(['git','show',f'{c}:{p}'])
def identity(data):return {'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest(),'git_blob':hashlib.sha1(f'blob {len(data)}\0'.encode()+data).hexdigest()}
def dump(p,v):p.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
def anchor(path,lo,hi=None):
 hi=hi or lo;data=get(MI,path);lines=data.splitlines(True);start=sum(map(len,lines[:lo-1]));end=sum(map(len,lines[:hi]))
 return {'commit':MI,'path':path,'lines_inclusive':[lo,hi],'byte_offsets_half_open':[start,end],'file_identity':identity(data),'span_identity':identity(data[start:end])}
def source(path,ranges):return {'commit':R,'path':path,'lines_inclusive':ranges,'evidence':'SOURCE_STATIC','execution':'NOT_EXECUTED'}
F='deliverables/final-specification-set/'
combat=F+'test-catalog/combat-requirements-wp39-40-41-42-45.md';forms=F+'test-catalog/pokemon-rules-wp19-21-22-23-34.md'
wp39=F+'combat-requirements/wp39-battle-context-and-participants.md';wp41=F+'combat-requirements/wp41-switching-positioning-and-escape.md';wp34=F+'pokemon-rules/wp34-inheritance-and-offspring.md'
thread=os.environ.get('CODEX_THREAD_ID');assert thread=='01a13fef-cc3c-730e-a5ba-a59a61501034'
frozen=json.loads((TOOLS/'frozen-integrated-input.json').read_bytes());audit=json.loads((TOOLS/'input-audit.json').read_bytes())
context={'actual_context':thread,'context_provenance':'Selected environment CODEX_THREAD_ID; direct tool observation','actual_platform_task_id':'NOT_EXPOSED_UNVERIFIED','agent_role':'/root independent actual-integration reviewer','parent_source_thread':'01a13f49-a154-7054-9b04-ce31f924d01c','environment_id':os.environ.get('CODEX_ENVIRONMENT_ID'),'different_from_excluded_contexts':thread not in frozen['excluded_contexts_for_fresh_R7_IR'],'U04_author_internal_context':'NOT_EXPOSED_UNVERIFIED retained; no fabricated match','subtasks_created':0}
configuration={'requested':{'model':'gpt-6.1-sol','effort':'ultra','service_tier':'default','speed':'ordinary; Fast forbidden'},'effective':{k:'UNVERIFIED' for k in ['model','effort','service_tier','speed']},'reason':'No effective configuration return; request text/thread/exit codes are not authentication.'}
exec_state={'content_evidence':['SOURCE_STATIC','DERIVED_VECTOR'],'mechanical_evidence':'TOOL_VALIDATION','all_behavior_vectors':'NOT_EXECUTED','reference_programs':0,'independent_behavior_model':0,'full_model':0,'UI_host':0,'Demo':0,'native_media':0,'real_save_replay':0,'new_reference_observation':0,'old_H14_UTIL03':'Prior isolated Ruby1process/10inputs remains historical, no credit to this task.'}
reasons={
 'SW-30':'逐读源后确认合法2v1保留；P令全队非全灭，首席原始100>50使替补逃跑成功，只跳过本席。后席合法P绑定2并交换顺序为[0,2,1]；位置恢复60→120先于一层撒菱15，至105。排除其它触发且无后备，调用正常返回3，外层阶段22才退出。',
 'SW-31':'唯一待补席No成功，本轮换入集合空；没有第二提示或入场调用，不消费位置2标志或对P扣HP。',
 'SW-32':'首席Yes不调用逃跑，P绑定0；唯一后备已在场，后席无合法可换者，非致死无其它改写时决定0。',
 'SW-33':'普通替补入口正决定3在裁判与扫描前早退；不等于扫描内部才写3。',
 'SW-34':'No是启动逃跑；后席默认必选界面取消输入只继续选择，不能撤回反馈或决定；其它可取消界面仍独立。',
 'SW-35':'显示/选择、绑定/顺序、位置标志/HP各有独立写点。故障只按已到前缀判断；WP42诊断正常返回可能继续外层，不恢复内层余段，不保证最终3或宿主成功。',
 'BC-26':'有效1v3顺序[3,5,1]中既存濒死3阻断偏好扫描，回退从首个既存3返回；只读无写入，不是筛选到5。',
 'BC-27':'仅使3存活，第一既存项正常返回3；这不建立普遍存活保证。',
 'BC-28':'仅使3不存在，跳过缺席后正常返回5，区别于既存濒死。',
 'BC-29':'直接己侧0投球请求先得3，再按全局席序的活同伴集合得1。仅接收捕获计算前目标1，不认证菜单可达、摇晃数或捕获成败。',
 'BC-30':'显式对侧5直接交给投球解析，绕过己侧对位查询；WP38普通菜单许可仍独立，不能据此准许向两个活敌投球。',
 'BC-31':'无活同伴得到空补救，后续状态查询先失败，未到无目标反馈。保持WP38既有消耗/异常边界，不重开旧必修或新增退款。',
 'R7-U05-PF01':'合法作者数据先命中母系旗标；此前物种数据为简化读取，不消耗季节差。二月返回1，母0→1/清特性缓存/重算/条件登记先于子显式1。重算不保证数值变化或返回时缓存仍空。',
 'R7-U05-PF02':'一月动态0与母存储0相等，无本次亲本提交；子显式同值0没有该短路，仍执行已有提交副作用。',
 'R7-U05-PF03':'强制母0优先返回，母存储不动态提交；子显式0的副作用保持。',
 'R7-U05-PF04':'仓库与独立战斗守卫返回母存储0；不取消子显式提交，也不证明这些界面能产蛋。',
 'R7-U05-PF05':'恢复默认DEERLING无母系旗标，且共同前提排除永石资格，故不因该链读母形态；其它入口的读取不能据此概括为纯读。',
 'R7-U05-PF06':'默认SHELLOS有母系旗标，固定处理器完整注册表无其动态/创建/提交注册或复制目标；BR27–31同值子提交、N0和首个合格永石顺序均保持。',
 'R7-U05-PF07':'实际领取先生成、后队满拒绝，故未入队/未复位，但已到母提交和登记不撤销；生成链无交互取消。',
 'R7-U05-PF08':'母重算失败前形态/清缓存已到，登记与遗传子赋值未到；母刷新失败保留已写记录，子赋值未到；子后段失败保留母完成前缀。全部为未注入的条件故障，不保证统一恢复。',
 'R7-U05-PF09':'无玩家/无图鉴分别跳过登记，母提交重算与随后子显式1仍成立；已核创建的空owner默认分支和DEERLING无创建处理器。只审正常生成，不调用需玩家的领取。'
}
def vectors(path,ids):
 lines=get(MI,path).decode().splitlines();out=[]
 for v in ids:
  ln=next(i+1 for i,l in enumerate(lines) if l.startswith('| '+v+' |'));cells=lines[ln-1].split('|')
  out.append({'id':v,'actual_anchor':anchor(path,ln),'premise':cells[2].strip(),'independent_reason':reasons[v],'result':'PASS_CONDITIONAL_STATIC','execution':'NOT_EXECUTED'})
 return out
sw=vectors(combat,[f'SW-{n}' for n in range(30,36)]);bc=vectors(combat,[f'BC-{n}' for n in range(26,32)]);pf=vectors(forms,[f'R7-U05-PF{n:02}' for n in range(1,10)])
common={'verdict':'PASS_SCOPED_ACTUAL_INTEGRATION','scope':'Frozen MI only, narrowed required contract; finite static review, no runtime equivalence certification','findings_requiring_revision':[],'missing_input_or_independence_blockers':[],'effective_configuration':'UNVERIFIED','execution':exec_state,'old_global_PASS_used':False,'optional_policy_adopted':False,'formal_ACCEPTED':False,'CLOSED':False,'L01_L14':'RETAINED'}
records=[]
for rid,b,clauses,vs,counter,checks in [
 ('GR7-M03-001','R7-U04',[anchor(wp41,123),anchor(wp41,127,128),anchor(wp41,237)],sw,'R7-M01 / p02-64f59f549be82df4101e',[
 '最小合同限定非致死继续扫描，未采用原作者危害致死终局扩张。',
 '布局/业主/可战后备/原始速度与正常入场前提逐项满足；不以两席濒死推出全队已负。',
 'WP42 §3.2 L51及§5.1阶段21/22、L135正确延迟消费合同语义相容。',
 'SW01–29、R06/R07/E04及普通逃跑/训练家/伙伴/取消门保持原字节和原资格。']),
 ('GR7-M03-002','R7-U04',[anchor(wp39,190),anchor(wp39,322)],bc,'R7-M02 / p02-7c5bfd2d8a1dc5f59b7a',[
 '只改保证式括注与对应BC辅助查询向量；[3,5,1]表、邻近和其它目标族未改。',
 '原始3、活同伴补救1、显式目标5分层，未宣称普通菜单必选错或捕获必失败。',
 'WP38 §2 L21–25的菜单/登记/专用球/补救/空对象失败逐条件保留。',
 '换人消息、梦话、变身者的false/默认调用已读；WP47-A §5目标资格与随机回退独立保留。']),
 ('GR7-M07-002','R7-U05',[anchor(wp34,188),anchor(forms,263,280)],pf,'R7-C05 / p02-87af89fdf6ad554de858 /challenges/1',[
 'WP34仅§9.10一行修订；§5.2可选交叉引用未采用，亲本不额外直接改遗传字段保留。',
 '合法作者旗标、月份2/母0、先前未动态读取、非战斗/仓库/强制、无合格永石等前提均具名。',
 'WP21动态读取与裸提交的相等门不同；WP33生成→容量→入队→复位语义相容。',
 '母系→首个合格永石、子同值、BR07/27–31、N0、EG-13/20、R4-IF01–06逐条件保留。',
 '默认DEERLING无该旗标，SHELLOS无季节处理器；没有所有读取、任意插件或统一回滚政策扩张。'])]:
 binding=next(x for x in frozen['source_bindings'] if x['batch_id']==b)
 records.append({**common,'id':rid,'batch':b,'actual_clauses':clauses,'vectors':vs,'original_counterproof':counter,'independent_content_checks':[{'condition':s,'result':'PASS_SCOPED_STATIC'} for s in checks],'candidate_evidence_binding':binding,'actual_receiver':{'MI':MI,'FI':FI,'actual_bytes_not_author_mirror_used':True,'applied_hunk_journal':P+'integration/U04-U05/v1/applied-clauses.json','root_candidate_reception':P+f'review-receptions/{b}/r1/reception.json','candidate_PASS_not_inherited':True},'dependencies':{'named_direct_record_edges':[],'named_transitive_record_edges':[],'edge_basis':f'f622356f contract + original normalized record {rid}, groups/dependencies; empty scheduling edges do not remove domain obligations','finite_source_and_consumer_compatibility':'SATISFIED_BY_THIS_NEW_STATIC_REVIEW','formal_reception':'WAIT_R7-I actual reception of this result and semantic/shared-catalog responsibility registration','closure':'WAIT_R7-I exact dependency/historical gate reception; OPEN until actual decision','global_dependencies':'NOT_ASSERTED_SATISFIED'},'unmet_later_gates':['R7-I receive this actual integrated result','R7-I formal acceptance, separately','R7-I closure after exact direct/transitive/domain and historical reception; no automatic close']})
dump(OUT/'per-id.json',{'schema':'r7.ir-u04-u05.per-id.v1','reviewer':context,'configuration':configuration,'dispatch_commit':D,'MI':MI,'MI_tree':frozen['actual_integration_tree'],'MI_formal_subtree':frozen['actual_formal_subtree'],'FI':FI,'FI_tree':'7efe118d11965ea842b5522cfa9dd7a8c7842d2d','fixed_B':B,'fixed_R':R,'records':records,'denominators':{'required':27,'batches':13},'uncovered_required':24,'other_batches_approved':False})
# Honest reading ledger: identity restoration is separate from semantic reading.
reads=[]
for b in ['U04','U05']:
 c=json.loads((Path('/workspace/r7-ir-context')/b/f'dispatch/delegation/contracts/R7-{b}.json').read_bytes())
 for r in c['original_full_contracts']:
  for k,g in r['complete_seven_groups'].items():
   if k.startswith('六_'):
    for x in g['读取义务']['items']:
     if x['path'].startswith(('Data/','PBS/')) and x['scope'].get('lines'):
      item=source(x['path'],[x['scope']['lines']]);
      if item not in reads:reads.append(item)
extras=[('Data/Scripts/011_Battle/001_Battle/005_Battle_ActionSwitching.rb',[[1,140],[142,285],[316,469]]),('Data/Scripts/011_Battle/001_Battle/011_Battle_EndOfRoundPhase.rb',[[690,740]]),('Data/Scripts/011_Battle/002_Battler/001_Battle_Battler.rb',[[690,777]]),('Data/Scripts/011_Battle/004_Scene/003_Scene_ChooseCommands.rb',[[290,310]]),('Data/Scripts/011_Battle/002_Battler/002_Battler_Initialize.rb',[[60,310]]),('Data/Scripts/012_Overworld/007_Overworld_DayCare.rb',[[1,90],[239,360],[450,530]]),('Data/Scripts/014_Pokemon/001_Pokemon.rb',[[90,210],[420,545],[1098,1227]]),('Data/Scripts/014_Pokemon/001_Pokemon-related/001_FormHandlers.rb',[[1,792]]),('Data/Scripts/012_Overworld/003_Overworld_Time.rb',[[1,5],[187,208]]),('Data/Scripts/010_Data/002_PBS data/008_Species.rb',[[80,110],[250,270]]),('Data/Scripts/015_Trainers and player/005_Player_Pokedex.rb',[[185,270]]),('PBS/pokemon.txt',[[11113,11140],[15229,15255]]),('Data/Scripts/021_Compiler/001_Compiler.rb',[[410,440]]),('Data/Scripts/016_UI/001_Non-interactive UI/003_UI_EggHatching.rb',[[1,131],[190,268]]),('Data/Scripts/010_Data/002_PBS data/009_Species_files.rb',[[1,190]])]
reads.extend(source(p,rs) for p,rs in extras)
consumers=[('pokemon-rules/wp38-capture-and-receiving.md',[[1,45]],'原始/补救/显式目标、许可与失败的分层'),('combat-requirements/wp42-growth-end-of-round-and-battle-outcomes.md',[[40,60],[100,145],[251,260]],'延迟决定消费、回合末阶段与异常前缀'),('combat-requirements/wp47-a-move-attributes-targeting-and-calling.md',[[110,205]],'独立目标构造/随机回退与梦话入口'),('pokemon-rules/wp21-dynamic-forms-and-display.md',[[35,85],[145,230],[265,310]],'动态门/提交/同值与历史取图'),('creature-rpg/wp33-daycare-and-breeding-session.md',[[113,145]],'生成/领取/容量守卫'),('creature-rpg/wp35-eggs-and-hatching.md',[[100,122],[165,165]],'孵化接点与动态读取'),('test-catalog/creature-rpg-wp35-36-57-64-68.md',[[23,23],[30,30]],'EG-13/20具名前提')]
consumer_rows=[]
for p,rs,purpose in consumers:
 p=F+p;data=get(MI,p);assert data==get(B,p)
 consumer_rows.append({'commit':MI,'path':p,'lines_inclusive':rs,'purpose':purpose,'identity':identity(data),'baseline_equal':True,'semantic_result':'PASS_STATIC_COMPATIBILITY','execution':'NOT_EXECUTED'})
dump(TOOLS/'reading-ledger.json',{'schema':'r7.ir-reading-ledger.v1','reader':thread,'full_actual_documents':[{'path':x['path'],'commit':MI,'read':'FULL_TEXT','baseline_method':'Full B equivalent complement and removed old lines separately read; complete Git byte comparison','candidate_method':'Complete exact byte comparison; no semantic verdict inherited'} for x in frozen['actual_integrated_files']],'full_dispatch':{'commit':D,'path':P+'integration/U04-U05/v1/R7-IR-dispatch.md'},'original_contracts':'f622356f both batches, seven groups, original normalized verification/dependencies/stages and cited proposer/counterproof members','source_reads':reads,'unchanged_consumer_reads':consumer_rows,'prior_evidence':'All 17+14 author and 20+24 candidate-review files independently restored, whole-byte compared to real fixed Git blobs; report/per-ID content read, input/manifests/transport/commands checked for identity, scope and stage. Downloaded author/reviewer tools were not executed. No inherited broad source-tree negative-proof credit.','limits':'L01-L14 full text read and retained','unread_rule':'Other restored/source complements are UNREAD, not converted to a material limit or full-source certification.','history':'BR07/27-31, EG-13/20, R4-IF01-06 read individually; old56/92 bytes/status preserved, no corpus recertification.'})
bootstrap=[]
for path in sorted(Path('/workspace/r7-ir-bootstrap').rglob('*')):
 if path.is_file():bootstrap.append({'local_path':str(path),**identity(path.read_bytes())})
receipt={'schema':'r7.ir-input-receipt.v1','created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'reviewer':context,'configuration':configuration,'dispatch':{'commit':D,'tree':subprocess.check_output(['git','rev-parse',D+'^{tree}']).decode().strip(),'path':P+'integration/U04-U05/v1/R7-IR-dispatch.md','identity':identity(get(D,P+'integration/U04-U05/v1/R7-IR-dispatch.md'))},'FI':{'commit':FI,'tree':'7efe118d11965ea842b5522cfa9dd7a8c7842d2d','path':P+'integration/U04-U05/v1/integrated-input.json','identity':identity((TOOLS/'frozen-integrated-input.json').read_bytes())},'MI':{'commit':MI,'tree':frozen['actual_integration_tree'],'formal_subtree':frozen['actual_formal_subtree'],'formal_files':131,'actual_file_identities':audit['actual_file_identities']},'B':{'commit':B,'workspace_tree':'84f79ec6e772aacbf3a464fde68cdc5a280e2950','formal_subtree':'ebbe29f2bc88cd17de7072bf440c6fa8c8c7089c'},'R':{'commit':R,'expected_historical_tree':'7589c800b61ba13a13040ed0d686979b80a84fd0','whole_tree_independently_verified':False},'bootstrap_inputs':bootstrap,'restoration':audit['restoration'],'independent_original_binding_checks':16,'independent_byte_audit':'tool-evidence/input-audit.json','supplement':'tool-evidence/supplemental-receipt.json','skills':'Actual AGENTS read. No .agents/.codex paths in B/MI/dispatch Git trees; /workspace/.agents empty and no relevant .agents/skills found in this environment. No nonexistent skill claimed.','source_separation':'Restored reference, candidate, freeze and actual inputs are named read-only snapshots; no downloaded author/reference/native program executed. No shared directory assumed.','execution':exec_state,'remaining':'No blocker to finite static MI judgment; root reception/acceptance/closure and runtime qualifications remain separate.','early_io_qualification':'Initial reconnaissance/reading I/O remains in platform tool record; no retrospective independent UTC/stdout/stderr logs fabricated.'}
dump(OUT/'review-input-receipt.json',receipt)
dump(TOOLS/'session-observations.json',{'actual_thread':thread,'initial_result_branch_remote_check':'ls-remote exact result branch returned empty before own worktree creation; existing unpublished work absent.','result_branch':'codex/r7-ir-u04-u05-20261015-r1','base':B,'initial_tool_failures_retained':'Platform I/O includes initial /workspace non-repo probe, a contract-key lookup KeyError, an exploratory manifest-shape KeyError, and text truncations subsequently covered by exact segmented reads.','audit_first_attempt':{'exit_code':1,'reason':'Auditor allowed only preparation/candidate additions; incorrectly flagged new original R7 publication additions outside those prefixes as historical modifications.','corrective_change':'Added exact original seventh publication prefix, separately asserted every pre-existing path is unchanged except five formal paths.','subsequent_logged_result':'tool-evidence/audit-command.json, exit0. No domain behavior executed or FAIL erased.'},'prior_author_failure':'U04 staged audit patch whitespace check exit2 is retained in immutable author command log; absent-branch ls-remote exit2 is a lookup result. U05 earlier API403/locator errors retain original qualification.','initial_logs':'Available platform records only; no invented timing/stdout/stderr reconstruction.','subtasks_created':0,'other_refs_written':False})
print(json.dumps({'records':len(records),'new_vector_rows':len(sw+bc+pf),'verdicts':{r['id']:r['verdict'] for r in records},'formal_acceptance':False,'closed':False}))
