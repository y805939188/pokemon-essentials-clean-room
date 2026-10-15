import datetime, hashlib, json, os, pathlib, shutil, subprocess

ROOT=pathlib.Path('/workspace/r7-ir-R7-U06')
REPO=ROOT/'result'
PREFIX='review/remediation-seventh-20261015-prepare/integrated-reviews/R7-U06/r1'
OUT=REPO/PREFIX
OUT.mkdir(parents=True,exist_ok=True)
E=OUT/'evidence'; E.mkdir(exist_ok=True)
B='e646432c644dec04d306842cc5a559a29c718fbc'
MI='45c80832a41c1b56dcd7e9d93497758cbb7721de'
FI='13d76ba61838b13925ba9d41f58a6b047564d926'
THREAD='01a1401c-1527-75c6-9a36-7bc9b3a00007'
SOURCE='01a13f49-a154-7054-9b04-ce31f924d01c'
BRANCH='codex/r7-ir-u06-20261015-r1'
ACT=ROOT/'actual-input/actual'
FORM='deliverables/final-specification-set/'

def load(path):return json.loads(pathlib.Path(path).read_text())
def write(path,data):
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
def ident(data):return {'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest(),'git_blob':hashlib.sha1(f'blob {len(data)}\0'.encode()+data).hexdigest()}
def copy(src,dest):
    dest.parent.mkdir(parents=True,exist_ok=True)
    shutil.copyfile(src,dest)
def locator(path,start,end):
    data=(ACT/path).read_bytes();lines=data.decode().splitlines(keepends=True)
    a=sum(len(s.encode()) for s in lines[:start-1]);b=sum(len(s.encode()) for s in lines[:end])
    return {'commit':MI,'path':path,'full_file_identity':ident(data),'lines_one_based_inclusive':[start,end],'byte_offsets_zero_based_half_open':[a,b],'slice_identity':ident(data[a:b]),'content':data[a:b].decode()}

audit=load(ROOT/'bootstrap-evidence/actual-byte-audit.json')
meta=load(ROOT/'bootstrap-evidence/cumulative-metadata-audit.json')
contract=load(ROOT/'original/dispatch/delegation/contracts/R7-U06.json')
groups={c['record_id']:c['complete_seven_groups'] for c in contract['original_full_contracts']}
utc=datetime.datetime.now(datetime.timezone.utc).isoformat()
runtime={'all_30_behavior_vectors':'NOT_EXECUTED','REFERENCE_OBSERVATION':'NOT_EXECUTED','independent_complete_behavior_model':0,'reference_program_processes':0,'game_host':0,'Demo':0,'native':0,'media':0,'real_save':0,'replay':0,'behavior_fault_injection':0,'static_tools':'TOOL_VALIDATION only; constants arithmetic is not vector/model execution','historical_H14_UTIL03':'Prior Ruby2.6.10 one isolated reference process/10 inputs belongs only to its original task. Never backfilled here.'}
config={k:'UNVERIFIED' for k in ['model','effort','service_tier','speed']}
config['qualification']='Requested configuration, role /root, shell PID and exit0 do not attest effective configuration. No private model stream published.'
deviation={
 'id':'U06-IR-PROC-001','status':'OPEN_PENDING_ROOT_PROCESS_ASSESSMENT','effect':'Both per-ID primary verdicts WAIT. Content observations below are retained but no PASS_SCOPED_ACTUAL_INTEGRATION is issued.',
 'contract_instruction':'不查额度/认证',
 'action':'Before successfully obtaining the dispatch, a shell command ran command -v gh && gh auth status && git config ... while an initial Git fetch was stalled. The auth-status action was unnecessary and contravened this restriction.',
 'tool_output_chunk':'69eb2e','exit_code':1,
 'observed_output':'/usr/bin/gh\ngithub.com\n  X Failed to log in to github.com using token (GH_TOKEN)\n  - Active account: true\n  - The token in GH_TOKEN is invalid.\n',
 'token_value_exposed':False,'credential_value_inspected_or_published_by_reviewer':False,
 'subagents_or_auxiliary_model_calls_created':0,
 'initial_command_utc_and_pid':'UNAVAILABLE: the initial exec output did not preserve these; later wrapper records must not be retroactively used for this action.',
 'disposition':'Disclosed to parent/user during work. No retry of auth diagnostics, no self-waiver. Root must determine whether a fresh independent review is required. This result does not resolve that gate.'}
write(E/'initial-provenance-and-deviation.json',{'utc_recorded':utc,'reviewer_thread_id':THREAD,'process_deviation':deviation,'bootstrap_events':[{'action':'git show fixed dispatch before object fetched','result':'object/path unavailable; contract then obtained through fixed-commit connector/raw content, later compared against Git blob'},{'action':'initial branch fetch stalled','result':'terminated that fetch; subsequently fixed-SHA shallow filtered Git fetches succeeded with credential helper and extraHeader explicitly empty'},{'action':'read-only urllib GitHub API attempt','result':'proxy CONNECT 403; no sandbox automatic-approval rejection; immutable raw transport and Git used successfully'},{'action':'initial clone/workdir lookup','result':'one wrong-working-directory failure was corrected; never treated as verification'},{'action':'005-cumulative-metadata-audit','result':'exit1 because a journal-added navigation file has no B blob; corrected tool explicitly verifies empty baseline and reran as 006. Both true logs retained.'}],'qualification':'Initial event prose is a truthful transcript-derived receipt, not fabricated raw log/PID/UTC. Raw wrapper logs begin at the actual recorded recovery/audit steps.'})

m09_reasons=[
('C01-M09-BU-ABS','形态吸收在普通基底前返回；参与者消费绑定普通基底求值，而成功计数另增。第一击不消费95那名，第二击首次求值5+floor(95/10)=14，10那名的6不被求值。画皮当代额外H//8与直接hpLost0分开。'),
('C01-M09-BU-CONTROL','仅改起始破皮形态，普通两次求值顺序消费95、10，得到14、6；没有改变名单长度或成功计数。'),
('C01-M09-TK-ABS','初始化0且仅在普通求值时加10。首吸收成功不求值，余两次是10、20；成功数3与求值数2分开，不补第四击。'),
('C01-M09-TK-CONTROL','起始形态1消除形态吸收，三次求值各加10得到10/20/30；独立命中门仍按原SKILLLINK条件。'),
('C01-M09-SUB-BU','替身标志不会变成画皮/结冻头的普通计算早返标志；基底仍求值并消费，14/6序列保留。替身HP与个体HP不是同一损失。'),
('C01-M09-SUB-TK','替身不跳过普通基底求值，累计随三次求值加10，得到10/20/30。'),
('C01-M09-MISS-STOP-FIRST-BU','BEATUP数据命中100在−1/0阶级下阈值75，99失败。该前门在基底之前，成功0，首名未消费；仅保留已经到达的PP/历史。'),
('C01-M09-MISS-STOP-FIRST-TK','TRIPLEKICK数据命中90且无有效SKILLLINK时99失败，在基底前停止，无成功或补击。'),
('C01-M09-MISS-STOP-LATER','首吸收计成功1且切形，后续命中失败早于首次普通基底，因此10/20都未求值；首击状态不倒退。'),
('C01-M09-MISS-STOP-FAINT-U','这是独立后段使U倒下的条件路径，不声称默认无其它反应的夹具自然生成倒下。外层成功返回后的U倒下门终止续击，已到前缀保留。'),
('C01-M09-MISS-STOP-SLEEP','独立反应写入真实睡眠且未治愈后，外层状态停止门终止续击；不重新解释成服从/扣PP门。默认夹具不自发睡眠。'),
('C01-M09-MISS-STOP-FREEZE','独立反应写入真实冰冻且未治愈时，同一续击循环的冰冻门停止；不承诺后续基底或补击。'),
('C01-M09-MISS-STOP-FAINT-T','唯一目标在独立后段倒下使全部目标倒下条件成立，计划剩余不绕过停止门。不是断言吸收本身直接耗尽目标HP。'),
('R7-U06-M09-CANCEL','上游尚未建立使用的取消没有本次计划/消费/新扣PP；进入本招式族后无另设UI取消点。命令与执行消费者分别核。'),
('R7-U06-M09-PREFIX','故障前后两个写点分别判断：求值前不补基底/HP，已求值/扣HP后保留已到写入；没有统一事务回滚或宿主恢复保证，未做故障注入。')]
m10_reasons=[
('R7-U06-SE01','水枪P40、L20、特攻33与特防55给普通基础6，最大非会心、本系与水克岩合成3，伤18至82。PP当前5到4不改变总PP25。尾部中央请求+6后，后继速度查询35*(2+6)/2=140，不改原速度35。仅独立常量核算。'),
('R7-U06-SE02','直接尾部以本次计算类型火/水为入口；火的伤害、相性另算。该尾部在附效/畏缩/减伤果消费之后、后续濒死检查之前。'),
('R7-U06-SE03','同水命中改成合法默认HEATPROOF使STEAMENGINE身份门不成立；耐热只改火，不改变此水伤害前缀。'),
('R7-U06-SE04','入口读取已计算类型；非火水或在类型计算前合法输电得到电均不满足。不能仅据原招式数据火水触发，也不复制原伤害18。'),
('R7-U06-SE05','calcDamage可正与替身标志独立；替身排除门先拒升，替身和本体HP分开，既有PP不退。'),
('R7-U06-SE06','保护或失手造成unaffected，直接尾部跳过该目标；只保留已经到的历史/PP，不补伤害。'),
('R7-U06-SE07','这是已到尾部calcDamage0的守卫反例；不把普通正伤夹具强称为自然0。非零计算伤害守卫独立成立。'),
('R7-U06-SE08','普通当前能力有效性分别拒GastroAcid和有效NeutralizingGas压制。该身份不是特殊不可压制例外。'),
('R7-U06-SE09','此处普通能力有效性拒已倒下拥有者；更早OnBeingHit显式允许倒下的资格不能传给此处。'),
('R7-U06-SE10','中央夹限按增量+6：−4到+2，+5到+6，+6不可再升；+2的后继速度35*4/2=70，不能赋绝对+6。'),
('R7-U06-SE11','每次合法击到尾部重读当前能力/伤害标志/阶级。首击到上限，续击不可再升；条件化的中间合法能力改变/压制决定续击资格，不虚构取得能力链。'),
('R7-U06-SE12','直接尾部没有独立MoldBreaker门，且中央来源是T自身；不能从早先目标能力回调的门推导这里被屏蔽。'),
('R7-U06-SE13','默认DARMANITAN的SHEERFORCE与合法EMBER附效10构成有效对照；其附效及具名整招后段二/三门不包住本直接每击尾部。不构造同时蒸汽机/单纯/唱反调。'),
('R7-U06-SE14','上游取消未建立使用与已进入后更早失败分别按到达位置判断；未到直接尾部不补升阶，也不补扣/退款。'),
('R7-U06-SE15','中央阶级写入先于后续反馈，故障后保留阶级及此前PP/HP；后续濒死/反馈/恢复不因此保证完成。条件静态分析，不是已执行故障实验。')]

def make_vectors(catalog,common_line,start,reasons,source_ranges):
    lines=(ACT/catalog).read_text().splitlines()
    result=[]
    for n,(key,reason) in enumerate(reasons,start):
        cells=[x.strip() for x in lines[n-1].split('|')[1:-1]]
        assert cells[0]==key,(n,cells[0],key)
        result.append({'id':key,'execution':'NOT_EXECUTED','evidence_class':['SOURCE_STATIC','DERIVED_VECTOR'],'common_premises':locator(catalog,common_line,common_line),'input_independent_variation':cells[1],'expected_static':cells[2],'actual_MI_row':locator(catalog,n,n),'independent_review_reason':reason,'source_read_ranges':source_ranges,'result':'STATIC_EXPECTATION_SUPPORTED_IN_LIMITED_SCOPE','primary_record_verdict':'WAIT_PROCESS_GATE'})
    return result

src09=[{'repository':'Maruno17/pokemon-essentials','commit':'8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b','path':p,'lines_one_based':s} for p,s in [
 ('Data/Scripts/011_Battle/003_Move/009_MoveEffects_MultiHit.rb',[[69,86],[155,180]]),('Data/Scripts/011_Battle/003_Move/003_Move_UsageCalculations.rb',[[239,281]]),('Data/Scripts/011_Battle/003_Move/002_Move_Usage.rb',[[163,194],[328,345]]),('Data/Scripts/011_Battle/002_Battler/007_Battler_UseMove.rb',[[290,428],[583,762]])]]
src10=[{'repository':'Maruno17/pokemon-essentials','commit':'8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b','path':p,'lines_one_based':s} for p,s in [
 ('Data/Scripts/011_Battle/002_Battler/007_Battler_UseMove.rb',[[403,425],[583,760]]),('Data/Scripts/011_Battle/002_Battler/010_Battler_UseMoveTriggerEffects.rb',[[5,78]]),('Data/Scripts/011_Battle/002_Battler/005_Battler_StatStages.rb',[[1,114]]),('Data/Scripts/011_Battle/002_Battler/001_Battle_Battler.rb',[[48,53],[248,275]])]]
catalog09=FORM+'test-catalog/pokemon-rules-wp43-44-46-48-50.md'
catalog10=FORM+'test-catalog/combat-requirements-wp49-51-52.md'
vectors09=make_vectors(catalog09,137,141,m09_reasons,src09)
vectors10=make_vectors(catalog10,45,49,m10_reasons,src10)

shared={'own_complete_target_files':[f['path'] for f in audit['own_exact_hunks']],'own_shared_preservation_checks':[],'own_contributors':{f['path']:f['contributors'] for f in audit['own_exact_hunks']},'content_receiver_finding':'All four complete actual files read. Only R7-U06 contributes to these target files; no current other-batch clause overwritten/duplicated/omitted. Own six hunks reconstruct B exactly outside changes. Candidate byte equality is corroboration, not inherited content PASS.','cumulative_metadata':'24 targets/56 hunks reconstructed against fixed B and MI; two shared EOF insertions explicitly U01→U02. Three root adjustments verified, audit/matrix link resolves in fixed MI, errata only status/reception differs. No new semantic PASS for U01/U02 engine/UI, audit/matrix, U11 DX or any other batch.','prior_five':audit['prior_five'],'prior_semantic_finding':'U04/U05 current WP39/WP41/WP34 and their two catalog files were read in full. Parent read semantics, natural-gift prefix failure, JABO/ORAN, BeakBlast and forced/error retry limits remain compatible with U06. Prior PASS/acceptance is not inherited.','formal_receiver':'PENDING_ROOT: record this review, semantic/shared/domain/historical responsibilities separately. This result gives no ACCEPTED/CLOSED.'}
deps_common=[
 {'receiver':'battle context / command / switching','actual_files':['combat-requirements/wp39-battle-context-and-participants.md','combat-requirements/wp41-switching-positioning-and-escape.md','combat-requirements/wp40-commands-obedience-and-action-order.md'],'finding':'Full required WP39/WP41 and named WP40 sections distinguish upstream cancellation, actual target/owner, no new family UI cancellation, fault prefix and conditional full-new-attempt retry; no resume-of-missing-hit guarantee.','root_registration':'PENDING'},
 {'receiver':'damage / status / stats / coverage','actual_files':['pokemon-rules/wp43-types-accuracy-and-damage.md','pokemon-rules/wp44-statuses-stat-stages-and-immunities.md','pokemon-rules/wp44-effect-coverage.md','pokemon-rules/wp48-ability-calculation-modifiers.md'],'finding':'Full required current consumers read: C1 early return and Substitute differ, base and final damage differ, central stage/current ability/ordinary speed retained, registered identities/counts unchanged.','root_registration':'PENDING'},
 {'receiver':'domain and historical C12/D/H/J chain','finding':'No named author scheduling edge is not proof of global/domain dependency satisfaction. J09 finite producer/consumer clause reception and old boundaries retained; U03/U07/U10 remain procedural WAIT and unmerged. Their future/source domains are not assumed absent. Full coverage and formal reception remain root responsibility.','root_registration':'PENDING'}]

records=[]
for record_id,vecs,clauses,mapping,findings,history in [
 ('GR7-M09-001',vectors09,[locator(FORM+'pokemon-rules/wp46-damage-multihit-and-healing.md',54,54),locator(FORM+'pokemon-rules/wp46-damage-multihit-and-healing.md',59,59),locator(catalog09,135,157)],
  {'C01-M09-BU-ABS':['C01-M09-BU-ABS'],'C01-M09-BU-CONTROL':['C01-M09-BU-CONTROL'],'C01-M09-TK-ABS':['C01-M09-TK-ABS'],'C01-M09-TK-CONTROL':['C01-M09-TK-CONTROL'],'C01-M09-SUB':['C01-M09-SUB-BU','C01-M09-SUB-TK'],'C01-M09-MISS-STOP':[x[0] for x in m09_reasons if 'MISS-STOP' in x[0]]},
  ['参与者在实际普通基底求值时消费；计划/成功击计数独立，吸收不补击。', '普通14/6、10/20/30对照，替身推进、命中/睡冻/倒下停止及前缀边界逐项成立。', 'WP43 §6.2原C1早返正确；没有触发条件同步或采用可选修订。TK原求值触发正确，仅限定序号例。', '不改AI、登记身份计数、owner资格、命中规则、当前攻防或固定伤害；不将基底当最终伤害。'],
  [{'id':'GR6-CA-EB-001','evidence':'fixed B R6-CA/nonproposer-rebuttals.md; fixed R AI_MoveEffects_MultiHit 151–184; current WP52-B 81–114; current BEB72–76 catalog','finding':'AI空合格名单、正替身、预测关/评分开之除零是另一消费者与原因；本M09真实多击基底消费修订不关闭或覆盖该历史。旧身份与接收资格保持。','receiver':'C12/D/H/J and root historical chain PENDING separate responsibility'}, {'id':'J09 / M09 alias','finding':'按原C01窄裁决接收，286项原始定位/切片/规范JSON绑定重核；未声称全历史同义根去重或全领域完整覆盖。'}]),
 ('GR7-M10-001',vectors10,[locator(FORM+'combat-requirements/wp49-ability-phase-triggers.md',157,164),locator(FORM+'pokemon-rules/wp46-damage-multihit-and-healing.md',23,23),locator(catalog10,43,65)],
  {'GR7-M10-001-C1':['R7-U06-SE01','R7-U06-SE02'],'GR7-M10-001-C2':['R7-U06-SE04'],'GR7-M10-001-C3':[f'R7-U06-SE{i:02}' for i in range(5,10)],'GR7-M10-001-C4':['R7-U06-SE10'],'GR7-M10-001-C5':['R7-U06-SE11'],'GR7-M10-001-C6':['R7-U06-SE12','R7-U06-SE13'],'GR7-M10-001-C7':['R7-U06-SE14','R7-U06-SE15']},
  ['直接每击尾部位置、计算类型、实际目标列表、unaffected/calcDamage0/替身门及当前普通能力有效性均具名。','中央自身来源请求+6，夹限与后继速度70/140成立；未设同时蒸汽机/唱反调/单纯夹具。','与早先允许濒死OnBeingHit、附效及强行整招后段二/三门分开；无独立模式破坏者/强行屏蔽门。','31条原AB与AI/AE/BE/CE保持；WP49的48族267配对和WP48的27族148配对不增。AI评级与孵化角色不当战斗反应证明。'],
  [{'id':'R7-C05 narrowed reception','finding':'原非作者/challenges/2逐条件窄裁决核对；登记表外直接分支不是新增族。原宽泛指控/宿主运行主张不复活。'}, {'id':'NaturalGift / JABO-ORAN / BeakBlast / fault retry','evidence':'current WP39/WP41/WP46/WP49/catalogs full; WP40 §5.2.3; WP42 §8; WP47-A §3.1.1; WP50 §5.1.1; fixed R trigger 34–78','finding':'旧已提交HP/持物/PP和第二击失败前缀、BeakBlast既有时序保留；新直接尾部不保证到达整招后段。条件重试须完整新尝试，不恢复漏击。原受击物允许濒死不扩大普通能力有效性。','receiver':'Root historical/domain reception PENDING, no global or historical closure.'}])]:
    records.append({'record_id':record_id,'verdict':'WAIT','wait_reason':'U06-IR-PROC-001: pre-dispatch authentication-status diagnostic violated 不查额度/认证; root process eligibility assessment pending. No scoped actual PASS is issued.','content_finding':'SUPPORTED_SCOPED_STATIC_ACTUAL; no new content blocker identified within the explicitly read scope','independent_reviewer_thread_id':THREAD,'actual_MI':MI,'actual_MI_tree':audit['git'][MI],'input_freeze_FI':FI,'actual_clauses':clauses,'seven_group_review':{'original_full_contract_file':'evidence/original-seven-group-contract.json','groups':list(groups[record_id]),'all_groups_read':True,'original_refs_checked':'evidence/actual-byte-audit.json / original_bindings (286 including duplicates across contract and normalized records12/13)','identity':'Exact root record and narrowed required P2 classification retained.','counterproof_and_four_paths':'Actual normal controls, upstream cancel, missed/failed paths and committed prefixes reviewed independently; see each vector.','minimal_correction_and_correct_preservation':findings,'acceptance_vectors_mapping':mapping,'independent_adjudication_and_history':history,'dependency_reception':deps_common,'execution_unknowns':runtime},'vectors':vecs,'original_minimum_and_preserve_scope':groups[record_id]['三_最小修订_正确保留'],'conditional_WP43':{'triggered':False,'actual_fact':'WP43 §6.2 C1/early-return already correctly excludes the remaining ordinary core; optional skipped-base cross-reference not adopted.'} if record_id=='GR7-M09-001' else {'not_applicable':True},'direct_and_transitive_receivers':deps_common,'history_reception':history,'shared_receiver':shared,'blocking_author_dependencies_as_dispatched':contract['blocking_author_dependencies'],'unmet_gates':['U06-IR-PROC-001 root process assessment','Root actual-result reception and registration of semantic/shared/domain/history responsibilities','All behavioral/reference/host/implementation/replay closure gates remain unexecuted','Effective model/effort/tier/speed UNVERIFIED; nonexposed opaque internal identity is not inferred'],'PASS_SCOPED_ACTUAL_INTEGRATION':False,'ACCEPTED':False,'CLOSED':False})

write(OUT/'per-id.json',{'schema':'r7.U06.actual-independent-review.r1','reviewed_at_utc':utc,'reviewer_thread_id':THREAD,'source_thread_id':SOURCE,'fixed_B':B,'actual_MI':MI,'actual_MI_tree':audit['git'][MI],'actual_formal_subtree':audit['formal_subtree'],'input_FI':FI,'input_FI_tree':audit['git'][FI],'records':records,'process_deviation':deviation,'runtime':runtime,'effective_configuration':config,'limits':'L01–L14 byte-preserved in evidence/limits-and-alias-reception.json. Old56/92 closure and27items/13batches remain. No optional/policy adoption.','global_PASS':False,'ACCEPTED':False,'CLOSED':False})

for src,name in [
 ('bootstrap-evidence/dispatch.md','dispatch.md'),('bootstrap-evidence/AGENTS.md','AGENTS.md'),('bootstrap-evidence/independent-containers.md','independent-containers.md'),('bootstrap-evidence/integrated-input.json','integrated-input.json'),('bootstrap-evidence/actual-byte-audit.json','actual-byte-audit.json'),('bootstrap-evidence/cumulative-metadata-audit.json','cumulative-metadata-audit.json'),('bootstrap-evidence/read-ledger.jsonl','read-ledger.jsonl'),('bootstrap-evidence/candidate-git-trees.json','candidate-git-trees.json'),('original-plans/R7-U06.json','plans/original-R7-U06.json'),('actual-plans/R7-U06.json','plans/actual-R7-U06.json'),('supplement-plans/R7-U06.json','plans/supplement-R7-U06.json'),('original/dispatch/delegation/contracts/R7-U06.json','original-seven-group-contract.json'),('original/evidence/tasks/R7-C17/limits-and-alias-reception.json','limits-and-alias-reception.json')]:copy(ROOT/src,E/name)
for typ in ['original','actual-input','supplement']:
    receipts=list((ROOT/typ).glob('recovery-receipt-*.json'));assert len(receipts)==1
    copy(receipts[0],E/(typ+'-recovery-receipt.json'))
for p in (ROOT/'bootstrap-evidence').glob('*.json'):
    if p.name.startswith(('restore-','003-','004-','005-','006-')):copy(p,E/'commands'/p.name)
for p in (ROOT/'bootstrap').glob('*.py'):copy(p,E/'tools'/p.name)

extra=[]
actual_paths=subprocess.check_output(['git','ls-tree','-r','--name-only',MI,'--',FORM],cwd=REPO,text=True).splitlines()
for p in sorted((ROOT/'supplement/actual-consumers').glob('*.md')):
    rel=str(p.relative_to(ROOT/'supplement/actual-consumers'))
    is_old=rel.startswith('R6-CA')
    matches=[path for path in actual_paths if pathlib.Path(path).name==rel]
    if not is_old:assert len(matches)==1,(rel,matches)
    path='review/remediation-sixth-20261014-prepare/inputs/evidence/tasks/R6-CA/nonproposer-rebuttals.md' if is_old else matches[0]
    extra.append({'local_path':str(p),'fixed_commit':B if is_old else MI,'path':path,**ident(p.read_bytes()),'read_scope':'Only named ranges in read-ledger; not a claim to full-file semantic review unless explicitly stated.'})
identity={'actual_thread_id':THREAD,'actual_session_id':THREAD,'caas_session_id':'de96e48584e64a59bd8701174fd98e6b','environment_id':'ccarenv_b64_Y2NhcmVudl81Njc2YmE4MDE3YzA4MTkxYTc2ZWJlNWUzYWU4YmQyNA','source_thread_id':SOURCE,'observed_author_thread':'01a13f7f-5a16-72cd-87a7-6b9fd59a1025','observed_candidate_reviewer_thread':'01a13ff0-6000-748c-a2ed-b6965f662032','exclusion_list_check':'Actual visible thread differs from every listed excluded ID; no subagent/task/model session created.','opaque_internal_task_context_model_PID':'NOT_EXPOSED; never inferred from /root or shell PIDs.','process_eligibility':'WAIT due U06-IR-PROC-001; visible independent identity does not waive it.'}
write(OUT/'review-input-receipt.json',{'schema':'r7.U06.actual-review-input-receipt.r1','utc':utc,'identity':identity,'effective_configuration':config,'dispatch_fixed_commit':'c64774c60d91e522cb515ef71e3e9d4ea6b4712c','fixed_input_git_trees':audit['git'],'candidate_git_trees':load(ROOT/'bootstrap-evidence/candidate-git-trees.json'),'fixed_input_file_crosschecks':meta['fixed_files'],'recovery':[{'plan':x['plan'],'members':x['members'],'bytes':x['bytes'],'destination':str(ROOT/('original' if x['plan']=='original-plans' else 'actual-input' if x['plan']=='actual-plans' else 'supplement')),'status':'BOUNDED_RESTORE_BYTES_VERIFIED','verification_details':'evidence/actual-byte-audit.json / restored'} for x in audit['restored']],'recovery_qualification':'All inputs actually restored in this container; no shared filesystem assumption, no restored candidate/reference program executed. Fixed restore tool, instructions and original plan were read before invocation. Targeted missing source/consumer bindings supplemented at fixed commits.','supplemental_actual_consumers':extra,'actual_required_full_read_trace':meta['complete_required_actual_read_trace'],'reading_qualification':'Read ledger is real read trace; several initially large outputs were followed by smaller missing-range reads. AGENTS also read before restoration; later numbered full reread retained. Full14 actual files read; no semantic claim for all131 bodies. Hash, coverage, audit exit0 and historical PASS are never content evidence by themselves.','formal131_table':'evidence/actual-byte-audit.json / formal131; FI identities cross-checked against Git tree blobs/modes for all131. No claim that all131 file bodies were reread or rehashed.','own_actual_hunks':audit['own_exact_hunks'],'cumulative_scope':audit['journal_scope'],'skills':{'actual_git_tree_scan':audit['skills'],'workspace_dot_agents_scan':'No relevant .agents/skills files present. No project skill applied; no invented skill attestation.'},'original_seven_groups':{'all_read':True,'two_records':[x['record_id'] for x in records],'raw_ref_checks':len(audit['original_bindings']['checked']),'missing_raw_refs':0,'details':'evidence/original-seven-group-contract.json; evidence/actual-byte-audit.json / original_bindings'},'process_deviation':deviation,'author_candidate_review_failure_history':'Author command005 missing raw exit1,009 diff exit1,012 whitespace exit2 and later014 exit0 remain historical facts, not erased or behavior PASS; candidate reviewer provenance/configuration gaps remain. Restored originals and their receipts preserve exact bytes.','publication':{'authorized_branch':BRANCH,'base':B,'allowed_prefix':PREFIX+'/', 'method':'ordinary commits and push; complete per-file remote readback recorded after publication','main_tag_formal_candidate_write':False},'runtime':runtime,'limits_L01_L14':'evidence/limits-and-alias-reception.json (unchanged full original)', 'ACCEPTED':False,'CLOSED':False})

report=f'''# R7-U06 独立实际累计整合复审 r1

本次仅复审 **GR7-M09-001、GR7-M10-001**。两项主结论均为 **WAIT**，未签发 PASS_SCOPED_ACTUAL_INTEGRATION。原因是本审者在成功取得派发合同之前，执行过一次 `gh auth status` 认证状态诊断，违反合同“**不查额度/认证**”。该动作退出1，没有暴露令牌值；初始动作没有可恢复的独立 UTC/PID，不以事后日志补造。详见 [流程偏差](evidence/initial-provenance-and-deviation.json)。根任务须判断该资格偏差及是否需要全新复审；本审者不自行豁免。

在实际读取的限定内容范围内，两项修订及30条新增向量均有静态依据，**未发现新的内容阻断**。这项内容观察与流程 WAIT 分开记录，不能被读取为实际整合 PASS、正式接受或关闭。

## 固定身份与恢复

- 实际 thread/session：`{THREAD}`；父 thread：`{SOURCE}`。可见真实 ID 与派发排除表逐项不同；无任何子任务、辅助 agent 或其它模型调用。内部 opaque task/context/model PID 未暴露，不能由角色名或 shell PID 推断。
- B：`{B}`；B tree：`{audit['git'][B]}`；B正式子树：`ebbe29f2bc88cd17de7072bf440c6fa8c8c7089c`。
- 实际 MI：`{MI}`；tree：`{audit['git'][MI]}`；正式131文件子树：`{audit['formal_subtree']}`。
- FI：`{FI}`；tree：`{audit['git'][FI]}`。固定派发 `c64774c60d91e522cb515ef71e3e9d4ea6b4712c`，原完整七组合同 `f622356f3beb9e84ea8cff9db07c7fb382565d3f`。
- 固定 R：`Maruno17/pokemon-essentials@8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`，派发提供 tree `7589c800b61ba13a13040ed0d686979b80a84fd0`。本次只核指定有界成员及其身份，不声称恢复/校验整个 R tree。
- 冻结 `aa369555b0e8b6c8b077f964b54ed63d3b924f26`；作者 `fd0c1e6f50587331846921d446d893f1c1e84f3d` / tree `113069992c0d13f80c41312c26f2143a9e31c15f`；候选审者 `b920f172da981f364cc591a9e68e84d33e9f7dc8` / tree `ac0fe484ae3f19d277e89f3ae09c4a81cb016b84`。候选 PASS 未继承。
- 在本容器实际恢复 original **36成员/7,536,934字节**、actual-input **123/2,704,432**、具名补充 **11/602,702**；三组再次逐文件 bytes/SHA256/Git blob 校验。FI运输计划63,382字节/SHA256 `f3ef6698fd3c971f5a7debbbd42b4331b8264a27627480b6389a1e7ae9ef94de`。恢复日志含真实工具 PID、UTC、输入输出与退出码，不假设共享目录。

全文读取实际 AGENTS.md，按干净室行为规格要求工作。B/MI 的 `.agents`/`.codex` Git树及相关本地目录无可用项目技能，如实保留；没有实现引擎/TS包，也没有转译或发布参考代码。原工具、恢复说明、原计划在执行前全文读；只运行获准恢复器及自编静态身份/范围/证据工具。

## 逐项实际内容结论

| ID | 主结论 | 限定内容观察 | 实际条款与向量 |
| --- | --- | --- | --- |
| GR7-M09-001 | WAIT（流程资格） | 静态最小修订及正确保留范围有依据 | WP46 L54/L59；pokemon目录 L135–157，15条 |
| GR7-M10-001 | WAIT（流程资格） | 静态直接每击规则及同步有依据 | WP49 L157–164、WP46 L23；combat目录 L43–65，15条 |

**M09：** 首次形态吸收在普通基底前早返，不消费围攻参与者、不推进三连踢累计威力，但仍占计划/成功击。SNEASEL95/MAGIKARP10的围攻吸收后首次求值14、非6；普通对照14/6。三连踢首吸收后10/20，普通对照10/20/30。替身仍普通求值推进。首击失手、续击失手、U倒下/睡/冻、唯一T倒下各停止门分别核；后四项为独立反应条件，不谎称默认无反应夹具会自然发生。上游取消没有本次使用/新扣PP，异常只保留已到写点，不保证完成/回滚/宿主恢复。

WP43 §6.2 原C1早返已正确，未触发条件同步、未采用可选交叉引用；不能把整个核心或TK求值触发写成缺失。基底不是最终伤害或HP损失，AI、计数、资格、当前攻防与固定伤害不被扩大。原6组向量拆为13条，加取消/前缀共15条，逐行前提与静态理由见 [per-id.json](per-id.json)。

**M10：** 直接尾部位于附效、额外畏缩、减伤果消费之后、后续T/U濒死检查之前。按本次计算类型火/水及实际目标顺序，排除 unaffected、calcDamage0、替身，要求当下普通有效STEAMENGINE及中央可升资格，自身来源请求速度+6。普通有效性拒倒下/胃液/有效气体；更早允许倒下的OnBeingHit不扩大此门。无独立模式破坏者/强行屏蔽门，不能套用具名整招后段二/三的强行抑制。

水枪夹具合法当前PP5、总PP25，基础6，经本系/相性合成3为18、T100→82、PP5→4；后继普通速度35→140。−4→+2、+5→+6、+6不再升；+2后继速度70。仅独立常量核算，未跑伤害/战斗模型。每击重查，不构造同时蒸汽机/单纯/唱反调。火、其它计算类型/输电、耐热、替身、失手/保护、条件calcDamage0、压制、倒下、封顶、多击、模式破坏、合法强行EMBER、取消及写阶后故障逐条核。C1–C7映射15行，全部 NOT_EXECUTED。原AB31行与48族267配对、WP48的27族148配对保持。

## 当前范围、消费者与历史责任

131份正式文件表与Git blob/mode对应：26份相对B改变、105份不变。此表核验不等于全文读取131份。派发14个当前实际目标/消费者均全文读，包括批准条件WP43、WP34及四份完整目录；初期大输出被截断的中段已按较小区间补读。四个U06文件的完整身份、六hunk的1基行号/0基半开字节区间及SHA/blob写在 [输入回执](review-input-receipt.json) 和 [字节审计](evidence/actual-byte-audit.json)。原七组、原C01/C05非作者反证、normalized12/13的全部286个原始定位/切片/规范JSON绑定实际核验，无缺项。hash/审计退出0与作者自审都不替代内容判断。

本批4个完整目标各仅有U06贡献，`shared_preservation_checks=[]`；无其它当前批次条款被本批覆盖、重复或漏接。全局journal 24目标/56hunk也由B精确重建到MI：audit/matrix两处EOF为U01→U02，其余无重叠；root三处仅追加当前接收指针或改变errata的status/reception。固定MI链接可读、public-reception的候选固定commit读法与journal一致。该机械检查不给U01/U02 engine/UI、U11 DX或其它批次新的语义PASS；本批不触及这些共享文件。

先前U04/U05接受的5份文件与其已接受MI逐字一致，并已全文读其当前内容。与本批相交的WP34父代动态读取、WP39/WP41命令/换人上下文、自然之恩续击异常与JABO/ORAN已提交前缀保持相容。补读当前WP40 §5.2.3、WP42 §8、WP47-A §3.1.1、WP50 §5.1.1和WP52-B具名段，保留BeakBlast历史时序、错误重试只能条件化完整新尝试，不把缺失后击自动恢复。

GR6-CA-EB-001的AI空名单、正替身、预测关/评分开除零，与M09实际围攻参与者消费属不同消费者/原因；旧有限证据及接收资格保持，本次不关闭。M10旧AI评级3与孵化标记不证明战斗直接尾部。J09的有限生产/消费者及逐clause接收保持，完整全域覆盖、C12/D/H/J与根的历史/领域接收责任未被本次替代。无具名作者排程边不等于这些依赖已经满足。

U03/U07/U10仍流程WAIT、未合入，未来贡献和源领域依赖不能假定不存在。原7 optional、2导航facet、1 no-required、2 policy均未采用；27项/13批、旧56/92边界保持。前三项旧实际PASS/接受不是本次18项的PASS依据。

## 运行、流程及交付边界

30条行为向量、REFERENCE_OBSERVATION、参考程序、独立完整模型、宿主/Demo/native媒体/真实存档回放及行为故障注入本次新增运行均0/NOT_EXECUTED。历史H14/UTIL-03 Ruby2.6.10一进程10输入只保留其原资格，不回填本审查。完整 [L01–L14及别名接收原件](evidence/limits-and-alias-reception.json) 逐字保存。实际 model/effort/tier/speed 全为 **UNVERIFIED**，不用请求、角色、PID或退出0认证。

恢复、补取和验证含真实失败记录：早期缺Git对象、错误工作目录、API代理403及被终止的悬挂fetch均不写成成功；作者既有005缺raw的退出1、009无索引diff的退出1（表示有差异）、012空白检查退出2与后续014退出0仍保持其时点。自编累计元数据审计005因新增文件在B不存在而失败，修正空基线处理后的006通过，两个日志同时保留。原两次恢复有包装器PID/UTC；补充恢复保留原工具UTC/逐文件结果，原进程PID未单独捕获，不事后补造；三组又由有PID的独立字节审计复核。最重要的认证诊断流程偏差U06-IR-PROC-001保持OPEN，两项WAIT等待根任务处理。

成果只写 `{PREFIX}/`，唯一分支 `{BRANCH}` 从固定B建立。普通提交推送后进行固定结果commit的完整远端逐文件 bytes/SHA256/Git blob/mode 回读；首轮回读结果随证据提交，最终发布提交的完整回读保存在本容器并随最终答复返回，避免虚构可自含的未来提交身份。未修改被审候选、MI正文、正式台账、main或tag；本审查不自行宣布ACCEPTED/CLOSED。
'''
(OUT/'report.md').write_text(report)
write(E/'build-receipt.json',{'utc':utc,'pid':os.getpid(),'tool':'build_review.py','kind':'Evidence serialization only; manual review reasons pre-authored by the independent reviewer, no reference/model behavior execution','allowed_prefix':PREFIX+'/', 'records':2,'vectors':30,'primary_verdicts':['WAIT','WAIT']})
print(json.dumps({'output':str(OUT),'records':2,'vectors':30,'verdicts':['WAIT','WAIT'],'status':'EVIDENCE_WRITTEN_NOT_YET_PUBLISHED'},ensure_ascii=False))
