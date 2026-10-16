"""Compose the final effective 39-entry handoff from accepted immutable inputs.

Only this effective39 directory is writable. No source execution, new review,
classification vote, remediation, Git/index mutation, or publication is performed.
"""
from pathlib import Path
from collections import Counter
import copy
import hashlib
import json
import subprocess

OUT = Path(__file__).resolve().parent
BASE = OUT.parent
RR = BASE.parent.parent
REPO = RR.parents[2]
STATE = 'READY_PENDING_ROOT_CORE_FREEZE'
F05 = 'GR8-COM-RECORD-DEBUG-RNG-001'
WP58 = 'deliverables/final-specification-set/combat-requirements/wp58-battle-recording-and-playback.md'
ROLE = '/root/handoff_final_five_root_deltas'
ROOT_PATH = RR/'adjudication/root-f05-debug-rng-optional-adjudication.v1.json'
DELTA_PATH = RR/'handoff-supplements/f05-debug-rng-optional-delta.v1.json'
RECEPTION_PATH = RR/'adjudication/root-handoff-38-preparation-reception.v1.json'
COUNT_QUAL_PATH = RR/'adjudication/mandatory-h-r7-task-context-count-qualification.v1.json'
WP39_QUAL_PATH = RR/'adjudication/root-core-c0002-approved-input-provenance-interface.v1.json'
C33 = 'c7fec918d511a0ead8ab325c934e9346d7c43cac'
C33_REPORT_TREE = '030e4d17e5eb6d02b169b1ecd97857e1e1312cf2'
C33_PUSH = RR/'publication/checkpoint-33-root-push-receipt.json'
C33_READBACK = RR/'publication/r8-qualified-primary21-and-recoveries-readback-33.json'
PRIOR = OUT/'prior-freeze-v1'
F06_ROOT_PATH = RR/'adjudication/root-f06-start-order-bounded-counterreview.v1.json'
F06_PROPOSAL_PATH = RR/'tasks/facility_atomic_completion_cloud/parallel_f06_canonical/ordering-candidate.eight-sections.json'
CREB_ROOT_PATH = RR/'adjudication/mandatory-creb-item-false-nil-and-mail-consumer-qualification.v1.json'
CREB_COMPANION_PATH = RR/'tasks/creature_b/final-evidence-corrections.current.json'
CLI_CHECK_PATH = RR/'publication/cli-startup-capability-checks.v1.json'
OLD_CLI_FAILURE_PATH = RR/'tasks/reference_metadata/launcher.stderr'

def read(p): return json.loads(p.read_text())
def rel(p): return str(p.relative_to(RR))
def dump(p, value):
    assert p.is_relative_to(OUT)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(value, ensure_ascii=False, indent=2)+'\n')
def write(p, text):
    assert p.is_relative_to(OUT)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text)
def identity(p, purpose):
    b=p.read_bytes()
    return {'repo':str(REPO),'commit':None,'tree':None,
        'commit_binding':'PENDING_ROOT_CORE_FREEZE; bind actual enclosing publication externally',
        'path':str(p.relative_to(REPO)),'mode':'100644','bytes':len(b),
        'sha256':hashlib.sha256(b).hexdigest(),
        'blob':hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest(),'purpose':purpose}

# Protect all 26 accepted files, including the external delivery manifest itself.
base_delivery=read(BASE/'delivery-manifest.json')
protected=copy.deepcopy(base_delivery['payloads'])
base_manifest_self=identity(BASE/'delivery-manifest.json','原38准备的精确外部manifest；原字节保护')
assert base_manifest_self['bytes']==9306
assert base_manifest_self['sha256']=='ec6a10b6f605540e44056e9aabfb5c05e8ff45da94664441d73b309a11725098'
protected.append({k:base_manifest_self[k] for k in ['path','mode','bytes','sha256','blob']})
def assert_base_unchanged():
    actual=[p for p in BASE.rglob('*') if p.is_file() and not p.is_relative_to(OUT)]
    assert len(actual)==26
    for row in protected:
        p=REPO/row['path'];b=p.read_bytes()
        assert len(b)==row['bytes'] and hashlib.sha256(b).hexdigest()==row['sha256']
        assert hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==row['blob']
assert_base_unchanged()
prior_archive=read(PRIOR/'archive-index.json')
def assert_prior_freeze_unchanged():
    assert prior_archive['preserved_file_count']==24
    for row in prior_archive['files']:
        b=(REPO/row['archived_path']).read_bytes()
        assert len(b)==row['bytes'] and hashlib.sha256(b).hexdigest()==row['sha256']
        assert hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==row['blob']
    archived_delivery=next(x for x in prior_archive['files'] if x['original_path'].endswith('/effective39/delivery-manifest.json'))
    assert archived_delivery['sha256']=='fa07017440aec95ef6ff37cec9d23403376947f681db313135c62f0556d666ce'
assert_prior_freeze_unchanged()

root=read(ROOT_PATH)
delta=read(DELTA_PATH)
current=read(RR/'adjudication/root-decisions.partial.json')
base_index=read(BASE/'handoff/records-index.json')
base_manifest=read(BASE/'handoff/cloud-eighth-update-handoff-manifest.json')
assert identity(ROOT_PATH,'root contract')['sha256']=='3d6a323e8dfac19f9865cd2be00b8ebf922666292898609c438dfcf600bf460c'
assert identity(DELTA_PATH,'delta')['sha256']=='7e5433d80dd79b7407c8b99b5f074cc3ba0b6f506ddccf1f8f84ef7cb7d91958'
assert root['complete_semantic_contract_received']==delta['complete_contract']
assert len(current['records'])==39 and len(base_index['records'])==38
assert current['bounded_counts']=={'required':29,'required_P2':2,'required_P3':27,'optional':10}
assert [(r['id'],r['classification'],r.get('severity')) for r in current['records'][:38]]==[
    (r['id'],r['classification'],r.get('severity')) for r in base_index['records']]
assert current['records'][38]['id']==F05 and current['records'][38]['classification']=='optional'
assert root['selection']=='UNSELECTED' and delta['required_ids_and_nine_batches_changed'] is False

count_qualification=read(COUNT_QUAL_PATH)
wp39_qualification=read(WP39_QUAL_PATH)
assert identity(COUNT_QUAL_PATH,'count qualification')['sha256']=='03e5e34b0b1d70c4dd77c2f6427daa1821656e2ffbb9f6089c3b263aa28fe707'
assert identity(WP39_QUAL_PATH,'WP39 qualification')['sha256']=='479ae920c8bc1b8d9197219960e82d45caa29a8f4b3a32a314c4ad1160ba65fe'
push33=read(C33_PUSH)
readback33=read(C33_READBACK)
assert push33['commit']==readback33['commit']==C33
assert push33['report_tree']==readback33['report_tree']==C33_REPORT_TREE
assert push33['exit']==0 and readback33['status']=='VERIFIED'
qualification_bindings=[]
for p in [COUNT_QUAL_PATH,WP39_QUAL_PATH]:
    local=identity(p,'新增必须保留的历史/来源资格，不新增正式root')
    published=next(x for x in readback33['files'] if x['path']==local['path'])
    assert all(published[k]==local[k] for k in ['mode','blob','bytes','sha256'])
    local.update({'commit':C33,'report_tree':C33_REPORT_TREE,
        'commit_binding':'ACTUAL_SUPPORTING_C33_INPUT_PUBLICATION; NOT_FINAL_R8_CORE',
        'remote_readback':published['readback']})
    qualification_bindings.append(local)
history={
    'schema':'r8-effective39-history-and-provenance-qualifications/v1',
    'task_population':{'complete_root_qualification':count_qualification,
        'effective_fact':'42为唯一任务ID人口，不是42个真实不同context。13作者任务+17候选审查任务+12实际审查context身份；U04/U05共享一个实际context，U06/U10/U12续turn新增context/票0。12实际审者、17候选版本、15实际结果版本分母分别保留。'},
    'WP39_approved_input_provenance':{'complete_root_qualification':wp39_qualification,
        'effective_fact':'批准来源声称有限成立：批准v3=42165B/864dec；管理回填=42697B/9a3a；B8当前原spec=44558B/d4ed，三阶段不相等。B8净化正文另为40296B/7935。历史批准/转写来源成立不等于当前所有metadata hash正确，也不给当前行为或全部manifest PASS。'},
    'exact_qualification_bindings':qualification_bindings,
    'supporting_publication':{'commit':C33,'report_tree':C33_REPORT_TREE,
        'purpose':'已实际发布及远端全byte核验的有限资格输入；不是最终R8语义core',
        'push_receipt':identity(C33_PUSH,'实际普通push、exit0、semantic_credit NONE'),
        'readback_receipt':identity(C33_READBACK,'仅引用10MB原transport载荷，保全本地原件不复制；VERIFIED/相关两文件完整新blob回读'),
        'semantic_credit':'NONE from transport; contract reading recorded separately'},
    'new_formal_roots':0,'new_required':0,'new_optional':0,'new_contexts':0,'new_independent_votes':0,
    'R8_core':{'status':'PENDING_ROOT_CORE_FREEZE','commit':None,'tree':None},'update_started':False}
dump(OUT/'handoff/history-qualifications.json',history)

# Preserve the accepted negative observation separately from the 39 entries.
f06_root=read(F06_ROOT_PATH)
f06_proposal=read(F06_PROPOSAL_PATH)
creb_root=read(CREB_ROOT_PATH)
creb_companion=read(CREB_COMPANION_PATH)
cli_checks=read(CLI_CHECK_PATH)
old_cli_failure=OLD_CLI_FAILURE_PATH.read_text()
assert identity(F06_ROOT_PATH,'F06 negative')['sha256']=='318673295587ed6b959941c1cc9a61a69d05bb7291b5bd90b7127b253ca4f76c'
assert identity(F06_PROPOSAL_PATH,'F06 original')['sha256']=='4755222d874dfbda15223e9b73b889fce7f390403a07738856a6a9f6ace15739'
assert identity(CREB_ROOT_PATH,'CREB mandatory')['sha256']=='5971c3a621d8032f7b4f5dfb5ad739994a2110a003b3aa58884d84c13d0f74ef'
assert identity(CREB_COMPANION_PATH,'CREB full companion')['sha256']=='51aff9b2d877c4fdea9f5ce99f0537d6befe582fa2aefc2341385d15cebb8547'
assert f06_root['classification']=='NO_REQUIRED_BOUNDED_SCOPE'
assert f06_root['5_minimum_write_and_preservation']['formal_write_set']==[]
assert len(creb_companion['complete_source_units'])==12
negatives=copy.deepcopy(read(BASE/'handoff/policy-and-preservation.json'))
negatives['schema']='r8-effective39-policy-and-negative-dispositions/v2'
negatives['current_bounded_no_required_count']=13
negatives['separate_no_required']='13有限NO_REQUIRED：原12项加独立F06-ORDER-START；与39条required/optional分类及4binary负例分列，不是全局NO_REQUIRED_UPDATE。'
negatives['F06_ORDER_START']={
    'id':'F06-ORDER-START','classification':'NO_REQUIRED_BOUNDED_SCOPE',
    'complete_root_contract':f06_root,
    'original_full_proposal':identity(F06_PROPOSAL_PATH,'原完整八节提案，未决旧状态按原字节保留；当前采用root有限NO_REQUIRED'),
    'mandatory_write_set':[],'optional_count_contribution':0,'required_count_contribution':0,
    'preserve':'成功开始所有效果、nil/正越界/负索引区别、SF03/SF31/SF37成功singleton前提和真实失败已写prefix；不把注入rand异常变新增普通失败兼容义务。'}
negatives['mandatory_accepted_fact_companions']=rel(OUT/'handoff/accepted-facts-and-mandatory-companions.json')
negatives['update_started']=False
dump(OUT/'handoff/policy-and-preservation.json',negatives)

accepted_facts={
    'schema':'r8-effective39-accepted-facts-and-mandatory-companions/v1',
    'CREB_ITEM_FALSE_NIL_MAIL':{
        'complete_root_qualification':creb_root,
        'full_source_grounded_companion':identity(CREB_COMPANION_PATH,'完整21730B：旧FITEM1/2、12完整源单位、6控制及8既有强制伴件；必须同用，不回填旧包'),
        'complete_carried_source_unit_identities':[{k:v for k,v in x.items() if k!='complete_text'} for x in creb_companion['complete_source_units']],
        'common_premises':creb_companion['common_premises'],
        'complete_effective_meanings':creb_companion['mandatory_effective_meanings'],
        'operative_parameter_scope':'rawfalse持物时，无参数或check_item=nil走raw非nil判断为true；item getter及check_item非nil的查询才进入typed getter并验证rawfalse抛ArgumentError。合法Item持物配check_item=false则正常比较false。setter输入nil与查询参数nil是不同位置，不混同。',
        'existing_mandatory_companion_bindings':creb_companion['actual_complete_mandatory_companions'],
        'consumer_rule':creb_root['consumer_rule'],
        'no_domain_expansion':'只有采用相同identity/mail/berry facet时适用。普通PBF/AI有效ID或nil不被改成自然注入false，不重审外域、不改旧字节或原状态。',
        'read_requirement':'对应facet实际采用前完整读根6198B、21730B伴件的旧对象/12完整单位/共同前提/六控制/五consumer用途及必要现行强制伴件；身份索引不替代实读。',
        'mandatory_formal_write_set':[],'new_formal_roots':0,'new_required':0,'new_optional':0,
        'business':'NOT_EXECUTED'},
    'status':STATE,'new_contexts':0,'new_independent_votes':0,'new_business_runs':0,'update_started':False}
dump(OUT/'handoff/accepted-facts-and-mandatory-companions.json',accepted_facts)

# The platform API has actually created tasks. CLI help is verified, while a
# model task failed on the precise read-only host boundary; these are distinct.
assert cli_checks['events'][0]['exit']==cli_checks['events'][1]['exit']==0
assert '0.159.0-alpha.3' in cli_checks['events'][0]['stdout']
assert 'failed to initialize in-process app-server client: Read-only file system' in old_cli_failure
cloud_message=f'用户已在未来手动启动本批后执行。逻辑入口R8-A-R8-U06；项目{REPO}、只读R /workspace/pokemon-essentials。完整读取{OUT}/handoff/batches/R8-U06/prompt.md与{OUT}/handoff/cloud-eighth-update-handoff-manifest.json，按其中固定B8/R及用户提供的root真实最终core/enclosing commit核验；未提供真实发布身份时保持发布门，不从本模板伪造hash。完整读取批对象inherited_complete_readset所绑定原读集/完整合同及全部必用伴件；只写本批独占candidate mirror与证据。请求gpt-6.1-sol/xhigh/default normal/Fast off，实际echo逐字段登记UNVERIFIED。F05未选不写WP58。记录返回实际task ID、实读/进度、命令I/O与候选manifest；不自签actual验收。'
cloud_reviewer_message=f'仅用户未来另行启动的真实非作者审查。逻辑入口R8-R-R8-U06；项目{REPO}、只读R /workspace/pokemon-essentials。完整读取{OUT}/handoff/batches/R8-U06/prompt.md与{OUT}/handoff/cloud-eighth-update-handoff-manifest.json、批对象所绑定完整readset/根合同，并另接收作者实际候选输入commit/tree/path身份；实际整合阶段另冻结最终实际输入。root最终core/enclosing或具体候选身份缺失时保持对应门，不猜hash。请求gpt-6.1-sol/ultra/default normal/Fast off，actual无echo逐字段UNVERIFIED。完整读受影响全文/累计保留及CREB对应facet伴件，四门分列，不能以角色改名或作者自验替代独立性。'
cloud_author={'tool':'collaboration.spawn_agent','arguments':{'task_name':'r8_a_u06','fork_turns':'none','model':'gpt-6.1-sol','reasoning_effort':'xhigh','message':cloud_message}}
cloud_reviewer={'tool':'collaboration.spawn_agent','arguments':{'task_name':'r8_r_u06','fork_turns':'none','model':'gpt-6.1-sol','reasoning_effort':'ultra','message':cloud_reviewer_message}}
cli_argv=['codex','exec','-C','/workspace/pokemon-essentials-clean-room','-m','gpt-6.1-sol','-s','workspace-write','--json','-o','review/remediation-eighth-20261016-prepare/tasks/R8-A-R8-U06/last-message.txt','-']
launch={
    'schema':'r8-effective39-evidence-backed-launch-methods/v1',
    'launch_gate':'只给用户未来手动派发方法，本准备不调用、不创建update任务；root final core/enclosing commit与用户选择门仍必须满足。',
    'cloud':{'status':'ACTUALLY_SUCCESSFUL_CURRENT_PLATFORM_ENTRY',
        'actual_supported_entry':'collaboration.spawn_agent',
        'evidence':identity(CLI_CHECK_PATH,'known_platform_entry记录本轮实际成功的gpt-6.1-sol/ultra请求；实际模型/tier无echo'),
        'visible_prior_success_example':'原context已实际返回/root/handoff_final_five_root_deltas/original_contract_mapping；它只承担原handoff只读支援，不是未来整改作者/审者。',
        'author_example':cloud_author,'nonauthor_reviewer_example':cloud_reviewer,
        'configuration_limit':'工具参数可传model/reasoning_effort，default normal/Fast off写入requested与任务登记；无权威echo实际model/effort/tier/speed/Fast逐字段UNVERIFIED。不因请求成功认证实际模型真值。',
        'logical_to_actual_ID':'R8-A-R8-Uxx / R8-R-R8-Uxx是逻辑入口；保存spawn返回实际canonical task name及平台ID（若有），未知不编造。作者与最终审者必须真实不同context。',
        'independent_input':'作者读本批完整prompt/readset；审者另用完整独立审查prompt及实际候选/最终整合输入manifest。fork_turns:none时message必须包含上述固定输入、路径、写集、角色与验收门，不能只给角色名。',
        'continuation':'collaboration.followup_task仅续接已存在实际context，不增加context/独立票，不能把同作者续turn当新非作者审查。',
        'status_queries':[{'tool':'collaboration.list_agents','arguments':{}},
                          {'tool':'collaboration.send_message','arguments':{'target':'<spawn返回的实际task名>','message':'报告当前固定输入、最近实际完成单元、实读/输出路径及具体阻塞；不要新增范围。'}},
                          {'tool':'collaboration.wait_agent','arguments':{'timeout_ms':60000}}],
        'logs':'先用云平台实际任务卡/工具事件和返回task名查看真实进度；list_agents只给可见状态，不冒称能尾读所有私有平台流。每任务在自己目录写progress.json、reading-ledger.json、commands.jsonl及各命令stdout/stderr、候选manifest，实际生成后可用tail -n 50 <独占任务目录>/commands.jsonl查看；未生成记录不得倒填。',
        'future_logical_paths':'review/remediation-eighth-20261016-prepare/tasks/<R8-A-R8-Uxx或R8-R-R8-Uxx>/；候选mirror继续按每批candidate_mirror_prefix。这里只给路径，不创建或写入这些未来目录。'},
    'CLI':{'status':'HELP_AND_VERSION_VERIFIED_MODEL_TASK_NOT_SUCCESSFUL_ON_CURRENT_HOST',
        'version':'codex-cli 0.159.0-alpha.3','version_exit':0,'exec_help_exit':0,
        'capability_receipt':identity(CLI_CHECK_PATH,'实际--version/exec --help命令、stdout/stderr、UTC与exit0'),
        'precise_failed_start':identity(OLD_CLI_FAILURE_PATH,'实际失败为readonly filesystem下in-process app-server client初始化，非flag问题'),
        'failure_text':old_cli_failure,
        'syntax_checked_flags':['-C/--cd','-m/--model','-s/--sandbox workspace-write','--json','-o/--output-last-message','PROMPT - reads stdin','-c/--config key=value is generic syntax only'],
        'example_argv_only':cli_argv,
        'stdin_prompt':rel(OUT/'handoff/batches/R8-U06/prompt.md'),
        'stdout_jsonl':'review/remediation-eighth-20261016-prepare/tasks/R8-A-R8-U06/events.jsonl',
        'stderr':'review/remediation-eighth-20261016-prepare/tasks/R8-A-R8-U06/launcher.stderr',
        'usage':'在用户未来手动启动且宿主允许CLI app-server/会话及输出目录写入后，将完整独立prompt经stdin送入该argv，分别保存JSONL/stdout、stderr、真实底层exit与last-message。必要任务目录由未来已授权任务创建；本准备不执行。',
        'configuration_scope':'help验证这些flag语法，不认证模型授权/网络/任务成功/业务成功，也未证明某具体effort/tier/speed/Fast config key；作者xhigh/审者ultra均在prompt和requested登记，宿主具体配置需按实际可核schema设置，无echo仍UNVERIFIED，不编造配置key。',
        'current_host_limit':'当前只读文件系统阻止in-process app-server client初始化；help exit0及可见flags不能称CLI模型任务已可启动。'},
    'Desktop':{'status':'NOT_AVAILABLE_IN_THIS_CLOUD_EXECUTION_ENVIRONMENT'},
    'new_contexts':0,'future_manual_update_tasks_started':0,'new_business_runs':0,'update_started':False}
dump(OUT/'handoff/launch-methods.json',launch)

new_contract={
    'schema':'r8-effective39-complete-f05-contract/v1','id':F05,'classification':'optional',
    'severity':current['records'][38]['severity'],'selection':'UNSELECTED',
    'root_contract':identity(ROOT_PATH,'完整已有八组根裁决，未新增投票'),
    'complete_contract':copy.deepcopy(delta['complete_contract']),
    'operation':{
        'unique_required_primary_batch':None,'conditional_batch_if_user_selects':'R8-U06',
        'candidate_writer':'R8-A-R8-U06','sole_actual_formal_writer':'R8-INTEGRATOR',
        'mandatory_write_set':[],
        'conditional_candidate_write_set':copy.deepcopy(delta['conditional_batch_append']['conditional_candidate_write_set']),
        'conditional_actual_target':[WP58],
        'read_set':['本完整八组合同与原F05候选65366B（准确身份见bidirectional_evidence/candidate）',
                    '六个固定R完整具名单元，准确repo/commit/tree/path/mode/blob/bytes/SHA及range见bidirectional_evidence/source_units',
                    '固定B8完整WP58全文181行、WP76 §7.1/7.2必要上下文及RC族共同静态前提/RC-W11完整输入与预期',
                    '原38已接收完整合同/本批原prompt/readset的实际相关累计保留'],
        'direct_semantic_required_ids':[],'transitive_semantic_required_ids':[],
        'required_predecessor_batches':[],
        'selection_gate':'当前UNSELECTED，无WP58写入；仅用户后续显式选择且手动启动后纳入U06独占mirror。未选择不阻required关闭。',
        'roles':copy.deepcopy(base_manifest['common_roles']),
        'acceptance_gates':['candidate PASS','actual integrated PASS','ACCEPTED','CLOSED'],
        'independence':'后续真实非作者ultra审者完整读原输入、候选及实际整合受影响全文/累计保留；原作者不得验收本人。',
        'no_automatic_sync':['WP76正文','RC-W11/RC29及QC/WS/PA目录','新测试ID','新debug产品API'],
        'business_execution':'NOT_EXECUTED','status':STATE,'update_started':False,
    },
}
dump(OUT/'handoff/contracts.f05.zh.json',new_contract)
records=copy.deepcopy(base_index['records'])
records.append({'id':F05,'classification':'optional','severity':current['records'][38]['severity'],
    'full_contract':{'path':rel(OUT/'handoff/contracts.f05.zh.json'),'pointer':'/'},
    'root_pointer':'/records/38','required_primary_batch':None,
    'conditional_batch_if_user_selects':'R8-U06','optional_selected':False})
index={'schema':'r8-effective-39-contract-index/v1','status':STATE,
    'classification_authority':identity(RR/'adjudication/root-decisions.partial.json','唯一当前39条分类/严重度；旧38不重新裁决'),
    'records':records,'bounded_counts':current['bounded_counts'],
    'qualification':'39条有限entries：29required（2P2/27P3）+10optional全部UNSELECTED；另1独立视觉政策UNSELECTED。全局core/history/interfaces仍OPEN。',
    'update_started':False}
dump(OUT/'handoff/records-index.json',index)

batches=copy.deepcopy(read(BASE/'handoff/batch-assignment.json')['batches'])
for b in batches:
    bid=b['id']
    b['effective_classification_entries']=39
    b['effective_required_entries']=29
    b['effective_optional_entries']=10
    b['R8_core']='PENDING_ROOT_CORE_FREEZE'
    b['current_launch_blocker']='PENDING_ROOT_CORE_FREEZE; UPDATE_NOT_STARTED'
    b['state']='PLANNED_NOT_STARTED'
    b['inherited_effective38_prompt']=identity(BASE/f'handoff/batches/{bid}/prompt.md','原已合格完整行为合同/保留及读集；当前统计/选择/冻结门由effective39替代')
    b['selected_optional_ids']=[]
    b['current_history_qualifications']=rel(OUT/'handoff/history-qualifications.json')
    b['current_negative_dispositions']=rel(OUT/'handoff/policy-and-preservation.json')
    b['mandatory_accepted_fact_companions']=rel(OUT/'handoff/accepted-facts-and-mandatory-companions.json')
    b['launch_methods']=rel(OUT/'handoff/launch-methods.json')
    if bid=='R8-U06':
        b['optional_ids_if_later_selected'].append(F05)
        b['conditional_target_write_set_by_id'][F05]=[WP58]
        b['conditional_candidate_write_set_by_id']={F05:copy.deepcopy(delta['conditional_batch_append']['conditional_candidate_write_set'])}
        b['conditional_contracts']={F05:rel(OUT/'handoff/contracts.f05.zh.json')}
        b['conditional_writer_by_id']={F05:'R8-A-R8-U06'}
        b['conditional_read_requirement_by_id']={F05:copy.deepcopy(new_contract['operation']['read_set'])}
        b['conditional_scope_by_id']={F05:'仅WP58§5.1 L105相关短语；WP76/RC-W11正确只读，保普通接线、AI主路径、原18初始属性/五元组与RC29全部ID/计数。'}
    b['additional_contract_pointer']=rel(BASE/'handoff/contracts.delta.zh.json')+'#/records'
dump(OUT/'handoff/batch-assignment.json',{'schema':'r8-effective39-nine-batches/v1','status':STATE,
    'batches':batches,'one_required_one_primary':True,'required_ids_changed':False,'batch_count':9,
    'optional_selected_count':0,'update_started':False})

dependency=copy.deepcopy(read(BASE/'handoff/dependency-graph.json'))
dependency['schema']='r8-effective39-dependency-graph/v1'
dependency['effective_classification_entries']=39
dependency['optional_selection'][F05]='UNSELECTED; 未选择不阻required关闭'
dependency['status']=STATE
dependency['R8_core']='PENDING_ROOT_CORE_FREEZE'
dependency['update_started']=False
dump(OUT/'handoff/dependency-graph.json',dependency)
conflicts=copy.deepcopy(read(BASE/'handoff/file-conflict-graph.json'))
conflicts['schema']='r8-effective39-file-conflicts/v1'
conflicts['effective_classification_entries']=39
conflicts['conditional_optional_writers'].append({'id':F05,'candidate_batch':'R8-U06',
    'candidate_writer':'R8-A-R8-U06','actual_writer':'R8-INTEGRATOR','paths':[WP58],
    'conditional_candidate_write_set':copy.deepcopy(delta['conditional_batch_append']['conditional_candidate_write_set']),
    'selection':'UNSELECTED','semantic_predecessor_batches':[]})
conflicts['F05_current_write_state']='WP58未加入当前candidate/actual必修写集；只在用户选择后由U06候选writer/R8-INTEGRATOR正式writer接收。'
conflicts['status']=STATE
conflicts['update_started']=False
dump(OUT/'handoff/file-conflict-graph.json',conflicts)

# Identity-only binding for the new future readset; no inherited source FULL.
future_units=copy.deepcopy(delta['complete_contract']['bidirectional_evidence']['source_units'])
formal_readset=[]
for path,ranges in [
    (WP58,[[1,181]]),
    ('deliverables/final-specification-set/demo-dx/wp76-facility-content-generation-and-simulation.md',[[158,169]]),
    ('deliverables/final-specification-set/test-catalog/combat-requirements-wp54-55-56-58.md','RC共同静态前提/RC族header及RC-W11完整输入预期；保全部RC29 ID/计数')]:
    b=subprocess.check_output(['git','show',base_manifest['B8']['commit']+':'+path],cwd=REPO)
    formal_readset.append({'repo':str(REPO),'commit':base_manifest['B8']['commit'],
        'tree':'751dfde81048c81390f89a65ca1d1a565ba8e1ca','path':path,'mode':'100644',
        'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),
        'blob':hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest(),'required_complete_range_or_units':ranges})
dump(OUT/'handoff/readset.f05.json',{'schema':'r8-effective39-f05-future-readset/v1',
    'id':F05,'source_units':future_units,'formal_units':formal_readset,
    'original_candidate':copy.deepcopy(delta['complete_contract']['bidirectional_evidence']['candidate']),
    'read_requirement':copy.deepcopy(new_contract['operation']['read_set']),
    'credit':'IDENTITY_BINDING_ONLY for this continuation. Prior named root/source reading stays with original readers; future selected author and actual nonauthor must complete the required reading.',
    'business_execution':'NOT_EXECUTED','update_started':False})

common=f'''状态 {STATE}，UPDATE_NOT_STARTED，update_started:false。当前唯一分类依据为 adjudication/root-decisions.partial.json 的39条有限entries：29 required（2P2/27P3）及10 optional，全部optional UNSELECTED；另1独立视觉政策UNSELECTED分列。不是全轮最终验收数。

固定B8={base_manifest['B8']['commit']}；R={base_manifest['R']['commit']}。项目 /workspace/pokemon-essentials-clean-room，R /workspace/pokemon-essentials 只读。先完整读取AGENTS、inputs/eighth-global-review-prompt.md、inputs/review-SKILL.md以及每条对应的完整合同/原prompt/readset。采用clean-document-revision：错误原位修正、必要缺项原位补齐、正确scope保留；审计原字节和旧裁决另存，不复制源码或Ruby组织设计未来框架。

records-index.json逐ID解析全部39条：原33完整合同固定引用5caff3bd1a1b062b48b7eda46777a614921946f3恢复包，新五条完整合同引用已接收的 tasks/handoff_final_five_root_deltas/handoff/contracts.delta.zh.json；F05完整八组合同在本包contracts.f05.zh.json。原38完整事实、前提、反例、最小读写、preserve、验收回归、实际独立反证与历史资格全部保持，不缩成摘要。原已合格prompt/manifest按精确字节引用；其中准备时点的统计/可选选择/冻结状态，以本effective39最终态为准。

真实R8语义core commit/tree尚未冻结，状态PENDING_ROOT_CORE_FREEZE、值为空。执行前须由root后继实际发布入口绑定最终core及真正包含最终报告/本包的enclosing commit，并核path/mode/blob/bytes/SHA和目录tree；当前HEAD和原准备commit不能代替未来身份。原26文件保持字节，本文不填自身未来hash。用户另行手动启动前已启动整改0、当前可启动0；共同release满足后九批隔离候选mirror可独立准备，九是逻辑批数，不代表slots。

作者请求gpt-6.1-sol/xhigh，实际非作者reviewer请求gpt-6.1-sol/ultra；均default普速、normal、Fast off。actual model/effort/tier/speed/Fast无权威echo逐字段UNVERIFIED，未来实际任务ID为NOT_STARTED。当前云平台collaboration.spawn_agent已实际成功创建有限审查任务，是实证可用入口；完整云API参数/逻辑与实际ID映射、独立prompt/readset、状态与日志方法见launch-methods.json。CLI codex0.159.0-alpha.3及exec --help均exit0，flag语法已核；旧模型启动实际因readonly filesystem无法初始化in-process app-server client，并非flag问题，不能称CLI模型任务已可启动。Desktop在本云环境不可用。原作者不得验收本人改动；逻辑角色改名不能创造独立性。

候选作者只写指定独占mirror及证据；所有正式target、共享整文件catalog、公共planning/audit索引和台账仅由R8-INTEGRATOR逐贡献整合。WP67-A由U06唯一候选writer接合旧COM同步、CP002必修及仅另选CP01；WP64由U09的CreatureE子范围接合MG32。共享Creature catalog整文件唯一正式writer接合Factory/Triad/E及EG/EN/FC/TT/MG，保持32条、原ID和别名前缀。

candidate PASS、actual integrated PASS、ACCEPTED、CLOSED四门分列。未来实际非作者须完整接收候选及最终受影响全文/累计保留、直接传递依赖、共享和历史资格；文件冲突不自动产生语义先后边。十个optional及视觉政策未选择不阻无关required关闭。全局core/history/interfaces及全量分母仍由root最终签收，本包不授全域PASS。

历史资格：42是唯一任务ID人口（13作者任务+17候选审查任务+12实际审查context身份），不是42个真实不同context。U04/U05共享一个实际审者，U06/U10/U12续turn不增context/票；12实际审者、17候选版本与15实际结果版本分别计数。WP39批准v3为42165B/864dec，管理回填为42697B/9a3a，B8当前原spec为44558B/d4ed，净化正文为40296B/7935；各阶段不相等。历史批准/转写来源成立，不授当前全部metadata hash或行为PASS。两项完整资格见history-qualifications.json；实际支持输入发布C33=c7fec918d511a0ead8ab325c934e9346d7c43cac、reporttree=030e4d17e5eb6d02b169b1ecd97857e1e1312cf2已远端全byte核验，它仍不是最终R8 core，不新增正式root或改变39条分类。

必用证据资格：采用相同item identity/mail/berry facet时，必须同用accepted-facts-and-mandatory-companions.json内完整CREB根6198B与21730B伴件，保旧FITEM1/2及12源单位/六控制。literal false可原值存入，item_id为false，无参数或check_item=nil的hasItem?为真；item getter及check_item非nil的查询进入typed getter后验证rawfalse并抛ArgumentError。setter输入nil不同；合法Item持物加check_item=false是正常比较false。Mail先赋mail引用，后getter自清再nil.item失败，早于item setter和mailbox删除；匹配持物/取消各自守卫保留。quarter<hp<=half时check_gluttony=false对active/inactive均绕过该谓词，其余独立berry门保留。只纠正采用对应facet的证据，不推false自然进入普通PBS/设施/AI域，不改旧包/状态，不增正式根或targets。

本准备不启动整改、新review、参考/游戏/宿主/编译/行为模型/向量运行或TS开发；新增业务运行0、NOT_EXECUTED。静态、推导、工具身份核验与真实执行分列，旧35项startup-impact保持原分母，不外推39。当前13有限NO_REQUIRED（原12加F06-ORDER-START）、4 binary负例与UI002撤销在本包policy-and-preservation完整分列，不新增39分类entry或整改batch。F06成功开始终态与nil/正越界/负索引保留，完整源采样先于缩队的事实不自动变成新普通异常兼容义务。可得未读不得改标limit。
'''
f05_text='''F05：GR8-COM-RECORD-DEBUG-RNG-001，alias FAC-F05-L105-DEBUG-RANDOM-ATTRIBUTION-CANDIDATE，optional/NOT_REQUIRED_BOUNDARY_PRECISION，UNSELECTED。当前mandatory写集为空，WP58不加入当前实际目标。只有用户后续选择后，才由R8-A-R8-U06在独占mirror改WP58 §5.1 L105相关短语，再由R8-INTEGRATOR唯一正式接收；不增加批次、required或语义依赖。

正常设施和回放使用普通Scene；生成器controlPlayer=true的实际命令先走AI，debug Party也走AI换人。直接调试helper的返回标签和该正常接线分开：菜单静态分支可返1（Bag）、4（Call）、0（Fight），目标无候选−1，换宠无候选nil、否则至多50次yield；Fight单数move访问不能保证成功。它们不经记录pbRandom，不能由局部归因不准推新增debug产品API或普通生成器stub策略。

若选择，最终句为：场景动画相关随机不经记录入口；无视觉调试场景的辅助选择随机也不经该入口，其直接调用的返回值与实际AI主路径分开，见WP76 §7.2。保原18初始属性/五元组、记录先super再append和回放顺序、普通接线及AI路径、失败/取消前缀。WP76和RC-W11现合同正确只读，RC29原ID/计数及QC/WS/PA目录不变；不加测试ID、不重排共享catalog。

完整事实、共同前提、普通/直接helper控制、失败/取消/部分提交、最强NO_REQUIRED与root裁决、read/write/preserve、静态验收、历史/真实独立链见contracts.f05.zh.json八组及readset.f05.json；不得只凭此摘要签收。后续若选择，真实非作者ultra审者完整读原输入与候选/实际整合结果，四门分别登记，运行未知仍NOT_EXECUTED。
'''
master='# 第八轮39条有限裁定完整有效中文人工整改handoff\n\n'+common
master+='\n| ID | 当前分类 | 严重度 | 唯一必修批次／条件批次 |\n| --- | --- | --- | --- |\n'
for r in records:
    batch=r['required_primary_batch'] or r['conditional_batch_if_user_selects']+'（未选）'
    master+=f"| {r['id']} | {r['classification']} | {r['severity'] or '原裁决未赋值'} | {batch} |\n"
master+='\n九批有效入口：\n\n'
for b in batches:
    master+=f"- {b['id']}：{b['title']}；handoff/batches/{b['id']}/prompt.md，完整原合同/读集身份随入口固定。\n"
master+='\n'+f05_text
master+='\n可用云任务启动API（仅供用户未来手动派发，本准备不调用）：\n\n```json\n'+json.dumps(cloud_author,ensure_ascii=False,indent=2)+'\n```\n\n实际非作者reviewer独立入口：\n\n```json\n'+json.dumps(cloud_reviewer,ensure_ascii=False,indent=2)+'\n```\n\n'
master+='保存spawn返回实际task名/平台ID，不用逻辑ID冒实际ID；用collaboration.list_agents({})查看可见状态，send_message给实际task名查询，wait_agent等待真实通知。followup_task续同context不增独立票。按平台任务卡/工具事件查看实际日志；每未来任务在独占tasks/<逻辑ID>/记录progress.json、reading-ledger.json、commands.jsonl及真实stdout/stderr、候选manifest，文件实际存在后可tail -n 50 commands.jsonl。私有平台流没有通用尾读接口，不冒已公开。\n\n'
master+='CLI备用argv语法已由help核验，当前宿主模型任务仍受精确readonly app-server初始化限制；不能把help当授权或任务成功。未来可写且已授权宿主可将本批完整prompt经stdin送入以下argv，独立保存stdout JSONL、stderr、exit和last-message；作者xhigh/审者ultra请求仍须记录，未核具体config key不编造：\n\n```json\n'+json.dumps(cli_argv,ensure_ascii=False,indent=2)+'\n```\n\n完整能力/失败原证据、stdin路径和日志路径见launch-methods.json。Desktop本环境不可用，未来手动启动数仍0。\n\nUPDATE_NOT_STARTED\n'
write(OUT/'handoff/cloud-eighth-update-handoff-prompt.md',master)
for b in batches:
    text=f"# {b['id']} 当前39条计划的完整有效派发入口\n\n"+common
    text+='\n本批必修ID：'+'、'.join(b['required_ids'])+'。\n'
    text+='\n本批条件optional（全部未选）：'+'、'.join(b['optional_ids_if_later_selected'])+'。\n' if b['optional_ids_if_later_selected'] else '\n本批无条件optional写入。\n'
    original=b['inherited_effective38_prompt']
    text+=f"\n完整原行为/保留/验收入口：{original['path']}（{original['bytes']} bytes，SHA256 {original['sha256']}）。必须完整读取其合同和对应原readset，不用本入口缩写替代。当前统计、选择与发布门按本effective39执行；原38条无需新分类或新review。\n"
    if b['id']=='R8-U06': text+='\n'+f05_text
    else: text+='\n本批必修改动、普通/边界/取消/异常/部分提交控制、preserve、读写及验收与已接收完整合同相同。F05仅为U06条件optional，未增加本批目标或依赖。\n'
    text+='\n本批完整调度/写权/读集/角色：\n\n```json\n'+json.dumps(b,ensure_ascii=False,indent=2)+'\n```\n\n'
    text+='输出逐ID候选、精确输入/目标身份、实际实读台账、可判定静态验收与累计保留、共享接收、失败/未知边界；原作者不得自签actual最终结果。UPDATE_NOT_STARTED。\n'
    write(OUT/f"handoff/batches/{b['id']}/prompt.md",text)

payloads=copy.deepcopy(base_manifest['input_payloads'])
classification_path=str((RR/'adjudication/root-decisions.partial.json').relative_to(REPO))
old_classification_identity=next(x for x in payloads if x['path']==classification_path)
payloads=[identity(RR/'adjudication/root-decisions.partial.json','当前39条分类投影的精确载荷；不重审原38') if x['path']==classification_path else x for x in payloads]
for p,purpose in [(ROOT_PATH,'F05完整既有根裁决'),(DELTA_PATH,'完整八组F05派发增量，与根合同逐值相等'),
                  (RECEPTION_PATH,'原38合格准备真实root接收，非全局冻结'),
                  (BASE/'delivery-manifest.json','原26文件完整固定身份'),
                  (BASE/'handoff/cloud-eighth-update-handoff-manifest.json','原38完整规范manifest，不改原字节'),
                  (BASE/'reading-ledger.json','同一实际context的原38真实阅读资格，非新审查'),
                  (COUNT_QUAL_PATH,'42任务ID/真实context分母资格'),
                  (WP39_QUAL_PATH,'批准来源与各阶段身份不等价资格'),
                  (C33_PUSH,'支持输入C33实际普通push，非最终core'),
                  (C33_READBACK,'支持输入C33 transport VERIFIED，相关两资格完整新blob核等，不复制10MB原件'),
                  (F06_ROOT_PATH,'F06完整有限NO_REQUIRED根反证，独立negative第13项'),
                  (F06_PROPOSAL_PATH,'F06完整原八节提案，原字节保留'),
                  (CREB_ROOT_PATH,'完整item false/nil/mail/berry对应facet必用根资格'),
                  (CREB_COMPANION_PATH,'完整21730B旧FITEM/12源单位/6控制及8必用伴件'),
                  (CLI_CHECK_PATH,'真实版本/help exit0和成功云入口/宿主边界'),
                  (OLD_CLI_FAILURE_PATH,'真实in-process app-server readonly初始化失败，不归因flag')]:
    payloads.append(identity(p,purpose))
manifest={
    'schema':'r8-effective39-complete-handoff/v1','language':'zh-CN','status':STATE,
    'B8':copy.deepcopy(base_manifest['B8']),'R':copy.deepcopy(base_manifest['R']),
    'R8_core':{'status':'PENDING_ROOT_CORE_FREEZE','commit':None,'tree':None},
    'enclosing_report_commit':None,
    'enclosing_commit_rule':'root最后以真实语义core及实际后继enclosing commit绑定；不写自身未来hash，不以观察HEAD/旧准备commit替代。',
    'inherited_complete_38_manifest':identity(BASE/'handoff/cloud-eighth-update-handoff-manifest.json','完整复用原38合同/资格/分工，原26文件全保字节'),
    'original_26_file_protection':{'external_manifest':base_manifest_self,'files':protected,'immutable_count':26},
    'classification_source':identity(RR/'adjudication/root-decisions.partial.json','当前唯一39条分类/严重度投影'),
    'superseded_input_identity':{'path':classification_path,'prior_38_sha256':old_classification_identity['sha256'],
       'meaning':'原manifest保持原字节；当前同路径分类载荷以本manifest新的39条身份取代，不要求把可变路径回退为旧38。'},
    'records':records,'bounded_counts':copy.deepcopy(current['bounded_counts']),
    'effective_classification_entries':39,'optional_selected_count':0,'optional_selection':'UNSELECTED_FOR_ALL10',
    'policy_count':1,'policy_selection':'UNSELECTED','bounded_no_required_count':13,
    'policy_and_negative_dispositions':rel(OUT/'handoff/policy-and-preservation.json'),
    'full_contract_resolution':{'inherited_38':rel(BASE/'handoff/records-index.json'),
       'new_39th_complete_eight_groups':rel(OUT/'handoff/contracts.f05.zh.json')},
    'input_payloads':payloads,'new_f05_readset':rel(OUT/'handoff/readset.f05.json'),
    'inherited_source_spec_readset':rel(BASE/'handoff/source-spec-readset.delta.json'),
    'history_qualifications':history,
    'accepted_facts_and_mandatory_companions':rel(OUT/'handoff/accepted-facts-and-mandatory-companions.json'),
    'launch_methods':launch,
    'prior_freeze_v1':{'archive_index':identity(PRIOR/'archive-index.json','前23载荷及其manifest共24文件逐byte保留；原manifest引用原路径，映射由此精确索引提供'),
       'preserved_files':24,'preserved_bytes':prior_archive['preserved_bytes'],
       'old_delivery_manifest_sha256':'fa07017440aec95ef6ff37cec9d23403376947f681db313135c62f0556d666ce',
       'not_recursive':'当前delivery仅枚举当前有效载荷，不递归归档目录；归档索引为外部固定身份。'},
    'batch_assignment':'handoff/batch-assignment.json','dependency_graph':'handoff/dependency-graph.json',
    'file_conflict_graph':'handoff/file-conflict-graph.json','batch_count':9,
    'first_wave_after_release_count':9,'currently_startable_count':0,
    'required_ids_changed':False,'semantic_edit_edges':[],'transitive_semantic_edit_edges':[],
    'common_roles':copy.deepcopy(base_manifest['common_roles']),
    'all_actual_formal_writers':'R8-INTEGRATOR',
    'F05_conditional_operation':copy.deepcopy(new_contract['operation']),
    'shared_catalog':copy.deepcopy(base_manifest['shared_catalog']),
    'execution':copy.deepcopy(base_manifest['execution']),
    'continuation':{'actual_context':ROLE,'new_contexts':0,'new_independent_votes':0,
       'new_global_or_domain_review_layers':0,'new_business_runs':0},
    'protected_scope':'只写tasks/handoff_final_five_root_deltas/effective39/；原26文件/root共享/正式/source/Git/index不改。',
    'remaining':'remaining.md','update_started':False,'final_marker':'UPDATE_NOT_STARTED',
}
dump(OUT/'handoff/cloud-eighth-update-handoff-manifest.json',manifest)
dump(OUT/'reading-ledger.json',{
    'schema':'r8-effective39-same-context-reading-ledger/v1','actual_context':ROLE,
    'new_contexts':0,'new_independent_votes':0,'no_new_review_layer':True,
    'governing_contract':'原实际context已完整读AGENTS、R8完整prompt及inputs/review-SKILL.md，本次按clean-document-revision直接形成最终态；不重审38。',
    'inherited_38_reading':identity(BASE/'reading-ledger.json','原真实阅读台账，原字节不改'),
    'inherited_38_qualified_reception':identity(RECEPTION_PATH,'root完整合格接收，当前已完整读该receipt'),
    'actual_full_reads':[dict(identity(ROOT_PATH,'完整14436B八组根裁决'),reading='FULL_TEXT',reader=ROLE),
                         dict(identity(DELTA_PATH,'完整16006B八组delta/批次条件/精确范围'),reading='FULL_TEXT',reader=ROLE),
                         dict(identity(COUNT_QUAL_PATH,'完整1029B任务ID/context人口资格'),reading='FULL_TEXT',reader=ROLE),
                         dict(identity(WP39_QUAL_PATH,'完整5614B有限批准来源/各阶段身份资格'),reading='FULL_TEXT',reader=ROLE),
                         dict(identity(F06_ROOT_PATH,'完整9873B有限NO_REQUIRED反证'),reading='FULL_TEXT',reader=ROLE),
                         dict(identity(F06_PROPOSAL_PATH,'完整7842B原八节提案'),reading='FULL_TEXT',reader=ROLE),
                         dict(identity(CREB_ROOT_PATH,'完整6198B必用对应facet根资格'),reading='FULL_TEXT',reader=ROLE),
                         dict(identity(CREB_COMPANION_PATH,'完整21730B旧对象/12完整carried源单位/前提/6控制/consumer及伴件；不授whole parent source FULL或外域重审'),reading='FULL_TEXT_WITH_COMPLETE_CARRIED_UNITS',reader=ROLE),
                         dict(identity(CLI_CHECK_PATH,'完整5452B实际CLI能力/云入口资格'),reading='FULL_TEXT',reader=ROLE),
                         dict(identity(OLD_CLI_FAILURE_PATH,'完整197B真实readonly app-server失败'),reading='FULL_TEXT',reader=ROLE)],
    'exact_semantic_dedup':'根complete_semantic_contract_received与delta complete_contract逐值相等；两完整输入已实际阅读。',
    'current_classification_reading':'全部39 id/classification/severity投影；前38与已合格索引逐值核同，不重新审源/投票。',
    'source_spec_credit':'root原六source units/正式输入信用留原读者；本continuation仅身份绑定，不继承source FULL。',
    'C33_transport_reading':'597B push receipt全文；10MB回读receipt只读顶层状态/身份及两资格exact file rows，纯transport/identity处置，不授semantic credit，不重审其22829文件。',
    'assigned_available_operative_unread':0,'assigned_operative_unreceived':0,
    'actual_configuration':{k:'UNVERIFIED' for k in ['model','effort','tier','speed','Fast','platform_session_id']},
    'requested':{'model':'gpt-6.1-sol','effort':'ultra','tier':'default','speed':'normal','Fast':'off'},
    'new_business_runs':0,'business_execution':'NOT_EXECUTED','update_started':False,'status':STATE})
write(OUT/'remaining.md','''# 当前冻结输入准备与后继门

READY_PENDING_ROOT_CORE_FREEZE，UPDATE_NOT_STARTED，update_started:false。

当前39条有限entries为29 required（2P2/27P3）及10 optional，全部optional UNSELECTED；独立视觉政策1条未选。有限NO_REQUIRED当前13（原12+F06）另列，不增加39分类。原38完整合同和九批必修计划保持，F05仅U06的条件WP58 L105短语，未加入当前候选/正式必修写集，不增required、批次或语义依赖。

本续接的完整有效合同未读/未接收0；同一实际context继续，新增context/独立票/审查层/业务运行均0。原26文件全部保字节。源/正式身份绑定不授本context新source FULL，不把历史root实读改成自身重审。

root全局core/history/interfaces与完整分母仍OPEN。真实R8 core commit/tree、最后报告与本包的实际enclosing commit尚未冻结，字段保持PENDING_ROOT_CORE_FREEZE/null；由root单一真实后继绑定，不伪造自身未来hash。用户另行手动启动前当前可启动0/整改已启动0。

两项新增历史资格已完整接收：42为唯一任务ID人口而非42不同context，U04/U05共享与续turn+0保留；WP39批准v3/管理回填/B8当前原spec各阶段身份区分，来源真不等全部当前metadata hash真。支持输入C33及其reporttree是真实已发布/远端核验身份，但不是最终R8 core，不增加正式root或改变39条分类。

CREB对应facet完整根资格/21730B伴件已实读并列为必用acceptedfact入口，旧FITEM1/2、rawfalse/nil/typedgetter、Mail先赋后自清/失败、pinch false精确，普通有效ID或nil域不扩大。CLI版本/help语法实际已核；模型启动曾因readonly app-server初始化失败，Desktop本环境不可用。当前实际可用云入口为collaboration.spawn_agent，方法、真实ID/日志与配置echo边界完整列于launch-methods.json；本准备未调用未来启动。

后续选择F05时仅U06候选writer/R8-INTEGRATOR正式writer接收WP58短语，WP76/RC-W11正确只读，保RC29及其它目录。后续真实非作者ultra审者完整接收原输入、候选和实际整合全文/累计保留，candidatePASS/actualPASS/ACCEPTED/CLOSED分列，原作者不得验收本人。未选optional/policy不阻无关required。
''')
write(OUT/'report.md','''# 39条完整有效人工整改handoff准备

READY_PENDING_ROOT_CORE_FREEZE，UPDATE_NOT_STARTED。

原实际context继续，只在effective39/生成当前最终态完整中文入口、39条规范记录索引/manifest、完整F05八组合同、九批assignment/执行prompt、依赖图及冲突图。原38已合格合同不重审，原26文件全部保字节。当前39=29required（2P2/27P3）+10optional全部UNSELECTED，独立视觉政策仍未选。

F05为GR8-COM-RECORD-DEBUG-RNG-001，severity原值NOT_REQUIRED_BOUNDARY_PRECISION，不提升为P3/required。只在用户后续选择时由U06唯一候选writer精确改WP58 L105相关短语，再由R8-INTEGRATOR唯一正式整合；当前无WP58必修目标，无新批次/依赖。保正常记录/回放普通Scene、生成器AI主路径、直接helper返回和失败区别、原18初始属性/五元组/随机顺序以及RC29原ID/计数；WP76/RC-W11正确只读。

完整交接入口为handoff/cloud-eighth-update-handoff-prompt.md，同规范数据为handoff/cloud-eighth-update-handoff-manifest.json。records-index.json逐ID解析全部39完整合同，contracts.f05.zh.json保F05全部八组，不以路径或摘要替代。九批prompt均给原完整prompt/readset精确身份和当前有效门；只有U06多一个未选条件合同。reading-ledger.json记录本实际continuation完整阅读，verification/validation.json仅为组合/身份工具核验，非新review层或业务证据。

history-qualifications.json完整吸收42唯一任务ID而非42真实不同context的口径，以及WP39批准v3/管理回填/B8当前原spec的阶段身份区分。支持输入C33已实际普通发布及远端全byte核验，相关两资格文件精确匹配；C33不当作最终R8 core，历史来源支持不扩大为当前全部metadatahash或行为批准，不新增正式root。

当前有效稿将13有限NO_REQUIRED（含F06）独立列入policy-and-preservation；完整CREB对应facet acceptedfact及源根伴件入口另存，不新增正式root。launch-methods.json和主prompt给实证成功的云API/逻辑与实际ID/独立prompt-readset/日志方法、已核CLI语法及精确readonly初始化失败，Desktop本云环境不可用。前23载荷及原manifest共24文件原byte存入prior-freeze-v1/，由外部archive-index精确映射；当前manifest不递归self/归档。

仍由root最后绑定真实语义core及报告enclosing commit；当前PENDING_ROOT_CORE_FREEZE/null不伪造hash。新增context、独立票、审查层、业务运行与整改均0。
''')

# Contractual composition checks, not a semantic re-review of the accepted 38.
old_batches=read(BASE/'handoff/batch-assignment.json')['batches']
old_dependency=read(BASE/'handoff/dependency-graph.json')
old_conflicts=read(BASE/'handoff/file-conflict-graph.json')
required=[r['id'] for r in records if r['classification']=='required']
optional=[r['id'] for r in records if r['classification']=='optional']
assigned=[rid for b in batches for rid in b['required_ids']]
assigned_optional=[rid for b in batches for rid in b['optional_ids_if_later_selected']]
checks={
 '39_record_ids_classifications_severities_exact_root':[(r['id'],r['classification'],r['severity']) for r in records]==[(r['id'],r['classification'],r.get('severity')) for r in current['records']],
 'original_38_index_entries_unchanged':records[:38]==base_index['records'],
 '29_required_unique_primary_batches_unchanged':Counter(assigned)==Counter(required) and [b['required_ids'] for b in batches]==[b['required_ids'] for b in old_batches],
 '10_optional_ids_exact_batch_union_all_unselected':Counter(assigned_optional)==Counter(optional) and all(b['selected_optional_ids']==[] for b in batches),
 'nine_batches_unchanged':len(batches)==9 and [b['id'] for b in batches]==[b['id'] for b in old_batches],
 'current_actual_and_candidate_required_targets_unchanged':all(b['actual_target_write_set']==o['actual_target_write_set'] and b['candidate_write_set']==o['candidate_write_set'] for b,o in zip(batches,old_batches)),
 'F05_only_U06_condition_WP58_L105':batches[5]['conditional_target_write_set_by_id'][F05]==[WP58] and new_contract['operation']['mandatory_write_set']==[],
 'no_WP58_actual_writer_while_unselected':all(x['path']!=WP58 for x in conflicts['actual_file_writers']),
 'actual_file_writers_unchanged':conflicts['actual_file_writers']==old_conflicts['actual_file_writers'],
 'no_new_semantic_or_transitive_dependency_edges':dependency['semantic_edit_edges']==old_dependency['semantic_edit_edges']==[] and dependency['transitive_closure_edit_edges']==old_dependency['transitive_closure_edit_edges']==[],
 'complete_F05_eight_group_contract_exact_root':new_contract['complete_contract']==root['complete_semantic_contract_received'] and len(new_contract['complete_contract'])==8,
 'F05_severity_not_promoted':new_contract['severity']=='NOT_REQUIRED_BOUNDARY_PRECISION',
 'independent_policy_still_unselected':manifest['policy_count']==1 and manifest['policy_selection']=='UNSELECTED',
 'core_and_enclosing_hash_not_fabricated':manifest['R8_core']=={'status':'PENDING_ROOT_CORE_FREEZE','commit':None,'tree':None} and manifest['enclosing_report_commit'] is None,
 'two_history_qualifications_exact_and_not_new_formal_roots':history['task_population']['complete_root_qualification']==count_qualification and history['WP39_approved_input_provenance']['complete_root_qualification']==wp39_qualification and history['new_formal_roots']==0,
 'supporting_C33_actual_input_identity_not_final_core':history['supporting_publication']['commit']==C33 and manifest['R8_core']['commit'] is None and all(x['remote_readback']=='FULL_NEW_REMOTE_BLOB_BYTES_VERIFIED' for x in qualification_bindings),
 '13_no_required_separate_from39_and_no_new_F06_targets':manifest['bounded_no_required_count']==13 and negatives['F06_ORDER_START']['mandatory_write_set']==[] and len(records)==39,
 'complete_CREB_root_and12units_mandatory_no_new_formal_root':accepted_facts['CREB_ITEM_FALSE_NIL_MAIL']['complete_root_qualification']==creb_root and len(accepted_facts['CREB_ITEM_FALSE_NIL_MAIL']['complete_carried_source_unit_identities'])==12 and accepted_facts['CREB_ITEM_FALSE_NIL_MAIL']['new_formal_roots']==0,
 'launch_evidence_cloud_success_CLI_help_and_precise_host_limit':launch['cloud']['actual_supported_entry']=='collaboration.spawn_agent' and launch['CLI']['version_exit']==launch['CLI']['exec_help_exit']==0 and 'in-process app-server client: Read-only file system' in launch['CLI']['failure_text'] and launch['future_manual_update_tasks_started']==0,
 'new_contexts_votes_review_layers_business_zero':all(v==0 for k,v in manifest['continuation'].items() if k!='actual_context'),
 'no_update_started':manifest['update_started'] is False,
 'all_39_IDs_in_final_main_prompt':all(r['id'] in master for r in records),
 'all_nine_effective_prompts_match_batch_ID_sets':all(all(rid in (OUT/f"handoff/batches/{b['id']}/prompt.md").read_text() for rid in b['required_ids']+b['optional_ids_if_later_selected']) for b in batches),
}
assert_base_unchanged()
assert_prior_freeze_unchanged()
checks['all_original_26_files_bytes_SHA_blob_unchanged']=True
checks['all_prior23_payloads_plus_manifest_24files_bytes_SHA_blob_unchanged']=True
assert all(checks.values()),checks
dump(OUT/'verification/validation.json',{'schema':'r8-effective39-composition-validation/v1','checks':checks,
    'passed':True,'scope':'TOOL_VALIDATION only; no new semantic review/adjudication/actual remediation acceptance',
    'records':39,'required':29,'optional':10,'policy':1,'bounded_no_required':13,'batch_count':9,
    'new_contexts':0,'new_independent_votes':0,'new_business_runs':0,'update_started':False})

delivery_rows=[]
for p in sorted(OUT.rglob('*')):
    if p.is_file() and p.name!='delivery-manifest.json' and not p.is_relative_to(PRIOR):
        x=identity(p,'effective39独立冻结输入载荷')
        delivery_rows.append({k:x[k] for k in ['path','mode','bytes','sha256','blob']})
dump(OUT/'delivery-manifest.json',{'schema':'r8-effective39-delivery-manifest/v1','status':STATE,
    'payloads':delivery_rows,'payload_file_count':len(delivery_rows),
    'payload_bytes':sum(x['bytes'] for x in delivery_rows),
    'self_binding':'不含自身hash/未来commit/tree；外部root真实后继commit绑定整个目录与本manifest。',
    'original26_preserved':True,'records':39,'required':29,'required_P2':2,'required_P3':27,'optional':10,
    'prior_freeze_v1_archive_index':identity(PRIOR/'archive-index.json','前24文件精确映射，归档整体另行固定，不递归枚举'),
    'prior_freeze_v1_preserved_files':24,'bounded_no_required':13,
    'new_contexts':0,'new_independent_votes':0,'new_business_runs':0,'update_started':False,'final_marker':'UPDATE_NOT_STARTED'})
print(json.dumps({'status':STATE,'records':39,'counts':current['bounded_counts'],'batches':9,
    'composition_checks':len(checks),'all_passed':True,'original26_preserved':True,
    'new_contexts':0,'new_independent_votes':0,'new_business_runs':0,'update_started':False},ensure_ascii=False))
