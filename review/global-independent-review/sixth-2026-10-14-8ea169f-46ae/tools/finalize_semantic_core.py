"""Freeze the finite semantic conclusion after all three independent final counters completed."""
import collections,datetime,hashlib,json,pathlib
ROOT=pathlib.Path(__file__).resolve().parents[1]
def get(p):return json.loads((ROOT/p).read_text())
def put(p,x):(ROOT/p).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
records=get('findings/normative-records.json');batch=get('handoff/batch-assignment.json')
assert len(records)==65
assert collections.Counter(x['identity_and_verdict']['classification'] for x in records)=={'required':56,'optional':8,'no_required_revision':1}
assert not get('findings/normalization-validation.json')['required_contract_gaps']
assert not get('coverage/assembly-check.json')['unmapped_blocks']
for p in ['tasks/R6-K/global-coverage-counter/report.md','tasks/R6-C/final-packet-counter/report.md',
          'tasks/R6-O/execution-boundary-counter/report.md','tasks/R6-O/policy-profile-counter/report.md']:
 assert (ROOT/p).is_file(),p
assert len(batch['unique_primary_batch'])==56 and batch['first_wave_count']==14

# Refresh identities of evidence produced during the final counter turn, retaining IDs and raw versions.
evidence=get('findings/evidence-binding-index.json')
for eid,x in evidence.items():
 data=(ROOT/x['path']).read_bytes()
 x.update({'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest(),
           'git_blob':hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest(),
           'final_binding_refreshed_at':now})
put('findings/evidence-binding-index.json',evidence)

aliases=[{'canonical':x['id'],'alias':a,'scope':'same root cause, first allocated domain ID retained',
          'reason':'parent aggregation numbered IDs do not replace the first allocated stable IDs'} for x in records for a in x['aggregation_aliases']]
aliases.append({'canonical':'GR6-F-V001','alias':'R6-C-AF001::additional_consumer',
 'scope':'Arena completed-processing producer/skill settlement only',
 'reason':'no-target reflection general-effect fact remains independently accepted; only its scoring consumer shares this root cause'})
put('findings/aliases-and-tombstones.json',{'aliases':aliases,'withdrawn':[{'id':'R6-UI-PARTY-004','state':'NO_REQUIRED_REVISION',
 'reason':'exact original entry method and corrected Entry0/SpeciesClause fixture refuted stale command; original supporting and opposing reports retained',
 'evidence':['tasks/R6-F/countercheck-ui-entry-stale-command.json','tasks/R6-K/imported-ui-party-storage-bag-facts.json']}],
 'separate_accepted_or_dismissed_hypotheses':[{'id':'R6-C-D01','state':'DISPROVED_NO_REQUIRED','artifact':'tasks/R6-C/dismissed-hypotheses.json'},
 {'id':'R6-C-D02','state':'NO_MATERIAL_FORMAL_CONTRADICTION','artifact':'tasks/R6-C/dismissed-hypotheses.json'},
 {'id':'R6-C-P01','state':'NO_DEFAULT_OBSERVABLE_TARGETING_COUNTEREXAMPLE','artifact':'tasks/R6-CM/counter-C-P01.json','required_scoring_facet':'GR6-F-V001'},
 {'ids':'D bulk C01–C04','state':'EXISTING_CONTRACT_SUPPORTED_NO_REQUIRED','artifact':'tasks/R6-D/pbs-bulk/findings.json'},
 {'id':'O Phone recheck','state':'NO_NEW_O003','artifact':'tasks/R6-O/phone-recheck.json'},
 {'id':'Purify first refresh suspicion','state':'BAD_STUB_REFUTED','artifact':'tasks/R6-UI/tool-evidence-status.json'}],
 'hypotheses_not_added_to_normative_proposal_denominator':True})
execution=get('tasks/R6-O/execution-boundary-counter/counts.json')
execution.update({'schema':'r6.execution.v1','source_counter':'tasks/R6-O/execution-boundary-counter/',
 'historical_separate':{'R4_review_isolated_records':4,'R5_review_isolated_records':4,'R5_update_new_execution':0},
 'current_update_execution':0,'update_started':False,
 'platform_identifier_scope':'source-probe runtime UUIDs are not CLI parent thread.started identifiers; eight verified CLI thread UUIDs are retained in control/task-register-current.json',
 'early_root_tool_provenance_limit':'Some early root read/generation commands retain platform tool echo but no separate local stdout/stderr/UTC capture; final validations now captured. See L14.',
 'source_static_derived_tools_reference_model_host_separate':True})
put('execution-evidence.json',execution)
counter_paths=['tasks/R6-K/global-coverage-counter/report.md','tasks/R6-C/final-packet-counter/report.md',
               'tasks/R6-O/execution-boundary-counter/report.md','tasks/R6-O/policy-profile-counter/report.md']
counter_bindings=[]
for p in counter_paths:
 data=(ROOT/p).read_bytes();counter_bindings.append({'path':p,'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest(),
  'git_blob':hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest(),'reading_scope':'root actual full text reread and explicit adoption','runtime_approval':False})
coverage={'schema':'r6.coverage-final.v1','review_state':'COMPLETE_FINITE_AVAILABLE_STATIC_REVIEW_WITH_REQUIRED_REVISIONS',
 'reference_files':{'denominator':432,'reviewed_or_purpose_disposed':432,'unreviewed_available':0,'text':414,'binary':18,
    'text_physical_line_handreading_not_claimed_files':69,'source_program_files':312,'source_program_lines':140865,
    'text_total_lines':389604,'scope':'full actual text or full finite structured data plus author-rule/consumer semantic review; native opaque regions remain precise limits'},
 'formal':{'files':131,'lines':28851,'whole_text_read':131,'finite_blocks':20379,'blocks_assessed_or_named_disposition':20379,'unread_files':0,'unmapped_blocks':0,
    'finite_block_kind':'includes headings/table headers/separators/history/scope, not 20379 behavior requirements'},
 'supplements':{'paths':116,'secondary_originals':111,'independently_retained':5,'retained_full_text_read':5,'secondary_full_structure_identity_disposed':111,
    'retained_composition':'3 support + WP01 scope baseline + WP02 evidence appendix','current_primary':'formal131','unresolved_current_scope':0},
 'whole_workspace_type_inventory':{'fixed_blob_count':38093,'purpose_dispositions_complete':38093,'historical_registration_payloads':37763,'not_new_game_requirements':True},
 'independent_source_locator_checks':236774,'map_child_artifacts_checked':98,'exact_shared_vectors':116,
 'matrix_catalog_files':48,'excluded_overend_ledger_records':6,'counter_reports':counter_bindings,
 'reference_to_spec_scope':'file→finite unit→manual fact/rule→actual or conditional consumer→primary contract/optional/policy/limit/type disposition',
 'spec_to_source_scope':'every formal finite block→source facts and input premise or explicit structural/history/scope disposition',
 'game_semantic_PASS_for_all_formal':False,'full_native_cfg_or_host_PASS':False,'update_started':False,'frozen_at':now}
put('coverage/final-coverage.json',coverage)
for p in ['coverage/reference-payloads-current.json','coverage/formal-payloads-current.json']:
 x=get(p)
 for item in x:
  item['current_semantic_state']='FINITE_DOMAIN_READING_AND_GLOBAL_COUNTER_COMPLETED_WITH_EXPLICIT_BOUNDARIES'
  item['reading_or_structure_complete']=True
  item['counter_basis']='tasks/R6-K/global-coverage-counter/report.md'
 put(p,x)

reg=get('control/task-register-current.json')
for item in reg['parents']:
 if item['logical_id']=='R6-I':
  item['state']='SEMANTIC_REVIEW_COMPLETE_REPORT_PUBLICATION_HANDOFF_PENDING';item['semantic_completed_at']=now
 else:item['state']='ASSIGNED_REVIEW_COMPLETED_ROOT_ADJUDICATION_RECORDED'
 item['current_scope_verdict']='finite static review completed; no full host/Demo approval'
reg['root_phase']='REPORT_CORE_FREEZE_NEXT';reg['update_started']=False
put('control/task-register-current.json',reg)
put('control/semantic-freeze.json',{'state':'READY_FOR_CORE_COMMIT','at':now,'core_identity':'external successor publication binding required; no self hash',
 'required':56,'optional':8,'no_required_revision':1,'optional_facets_separate':1,'policies':7,'limits':14,
 'all_domain_reviewers_finished':True,'source_and_formal_available_unreviewed':0,'update_started':False,
 'final_counter_reports':counter_bindings})

title_overrides={'GR6-F-V001':'Arena完成处理状态与存活结算门','GR6-F-V002':'录制初始条件在设施准备之后捕获',
 'GR6-F-V003':'Palace自动菜单早退与Mega登记范围','GR6-F-V004':'Arena取消多回合状态仍保留重充','GR6-F-V005':'Palace整数HP百分比为0的最佳后备门',
 'GR6-F-S001':'活动模式普通Quit Game仍可请求保存','GR6-F-G001':'默认设施模板的未知身份丢弃向量',
 'R6-D-LZ-001':'收集换行键与运行查找键不匹配','R6-D-LZ-002':'本地化也参与指定图像资源名请求'}
summary=['# 第六轮独立全局审查摘要','',
 '固定main/R的全量有限静态双向审查已完成。现有正式规格需要56项修订（39 P2／17 P3），本轮只发布报告与交接，没有修改正式规格或启动update。',
 '', '65条规范裁决＝64原完整提案＋1源请求精度潜在项：56 required、8 optional、1 no-required revision；浮点递推可选方面另1。7独立政策＝原六条＋GR6-POL-001；14限制＝原L01–L13刷新＋L14执行元数据。',
 '', '| 分母 | 当前完成范围 |', '| --- | --- |',
 '| R432 | 414文本全文或有限全结构规则审查，18binary有限结构/可读程序，未审可得范围0 |',
 '| formal131 | 28,851行全篇新读，20,379有限块双向映射或具名处置，未读/未映射0 |',
 '| supplements116 | 111旧稿secondary完整结构/身份/primary处置，5独立保留全文；不是116新增游戏合同 |',
 '| main38,093 blobs | 完整类型/阶段用途处置；历史证据不转成当前游戏PASS |',
 '', '69份原始文本未声称逐物理行人工阅读全文；其全部有限记录/字段/语义正文与消费者由本轮结构和作者规则闭合。全部机器码、动态宿主选择、GPU/字体/音频/物理输入、真实存档/网络及完整Demo仍未知。',
 '', '指定探针18次Ruby尝试：已知exit0 12、exit1 4、Ruby独立exit未知2；其中1次未加载R，17次进入原定义。exit0含无效Purifyv2与F重复运行，不能当18个成功场景；各家族向量分母另列。完整宿主/Demo/独立完整玩法模型/真实save/生产服务0。',
 '', 'INC-R6-001：UI/Party曾在仓库根瞬时创建两个新untracked报告文件后移入任务目录；当前保护检查无正式/R/旧62变化，不能改写成从未越界。',
 '', '14候选批次均可基于固定事实独立准备mirror；24文件冲突对、54候选正式路径由R6-I唯一实际写者接收。候选PASS、整合后独立PASS、正式接受、最终CLOSED分开。',
 '', '报告core与发布身份由后继publication回执外部绑定；完整中文handoff和manifest随后绑定实际core/发布对象，不递归自哈希。',
 '', '`UPDATE_NOT_STARTED`。', '', '| ID | 分类 | 级别 | 事项 |', '| --- | --- | --- | --- |']
for x in records:
 v=x['identity_and_verdict'];summary.append('| '+x['id']+' | '+v['classification']+' | '+str(v['severity'] or '—')+' | '+title_overrides.get(x['id'],v['title']).replace('|','／')+' |')
(ROOT/'summary.md').write_text('\n'.join(summary)+'\n')
report=['# 第六轮独立全局审查报告','',
 '结论：可得可审的有限静态范围完整审查、双向接合及独立反证已完成；正式合同存在56项必修。当前正式131与全部旧接受/关闭回执保持原字节。本轮不修正式稿，不实现框架，不启动云端update。',
 '', '## 固定输入与保护','',
 'main `8ea169fbd0f33f378b5d732fd6bea59e854e04a6`；workspace tree `6ab3429170d2762607fbc2237014c3a160449fa1`；formal tree `1046fbb657882e84b3dfc6d017943a9edf7782e5`。delivery lightweight tag仍指同一main。',
 '', 'R commit/tree `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`／`7589c800b61ba13a13040ed0d686979b80a84fd0`，432 tracked；两DS_Store额外文件独立库存。准确本地路径、origin、root、初始dirty/untracked、8当前工作树和原62字节保护见control、inventory及命令原始回显。旧行政10工作树快照不冒充当前8。',
 '', '固定发布core b67f542…六载荷、唯一activation六载荷及R1–R5资格均按用途新读。恢复入口local-sync-and-recovery及具名archive根保留；没有移动main/tag、force、删除分支/tag、重置/覆盖原工作或归档释放环境。',
 '', '## 全量读分母与双向接合','',
 json.dumps(coverage,ensure_ascii=False,indent=2),
 '', '逐材料完整身份见inventory与coverage/*-payloads-current；全结构/实际读区间、字段/方法/unit、手工事实、必要consumer、primary formal与前提恢复在48矩阵目录及domain ledgers。global-reverse-block-index逐20,379块保留实际审者/当前行，module-primary-mapping按正式path/领域记录。索引、hash或完整读取本身不授行为PASS。',
 '', 'source→unit→fact→consumer→spec与clause→source→premise全部具名。无默认caller定义、可变别名/缓存、写内存/编译/导出/存档区别、正常/取消/异常/部分提交及资源请求/最终宿主结果分别保留。BE37/CX42/RM37逐116真实接合，不把委托当本人全文。',
 '', '## 裁决、去重与独立反证','',
 '65规范记录完整七组合同见findings/normative-records.json。56必修39P2/17P3、8可选、1撤销；原64完整提案与原支持/相反counter全部可恢复。R6-C-P02仅请求参数精度optional；AN007的一般浮点递推另facet。',
 '', 'F首次GR6-F-V/S/G IDs为canonical，父聚合数字ID仅alias；R6-C-AF001仅Arena评分consumer facet并FV001，默认无目标反弹事实保留。UI-PARTY-004由精确原入口和正确Entry0/SpeciesClause输入独立反证撤销，不算必修。',
 '', 'C最终packet反证实际读64字段投影、56必修证据/负证据/消费者/失败前缀和修订字段/新C-P02，核982定位。其五意见已修：C001本handler拒绝不等最终拒换；C002速度夹具分列与WP40 primary；AN007精度scope；六D记录缺层字段按静态/未执行补全。原字段/错误阶段保留。',
 '', '7policy独立：历史BAG-04/UTIL-03/05/11/12/13及GR6-POL-001旧剖面范围。准确源缺陷不自动成为未来永久兼容。14limits独立，不作为未读豁免。',
 '', '## 历史资格和当前状态','',
 'R1逐原WP范围不臆造总数；R2 229控制/21批/341精确贡献五元组；R3 23/76且M09 optional/U08历史未启动、M02 NO_REQUIRED；R4当前17/76与B5 16/75区分，Summary后继仅精确残余，不转签整旧ID。',
 '', '第五唯一activation仍精确选择同一已审13fddb…候选的92 proposed，仅当前92CLOSED/OPEN0，51P2/41P3。7optional、7no-required、6原policy、13原limits分别保留；410native、568schema、158extra分列；21shared、18deps、85solewriter；262原贡献（259显式+3镜像）与6admin transfer、3纠正分别计。4606指针/hash核验、612当前span/93formal和537qualification反向span/79path只作资格锚点，不代新全源PASS。',
 '', '旧candidate01 G03/G09 FAIL、U03旧FAIL及定向修复、两advisory MISMATCH、SC-U07-001体内LF原错误与纠正全部保存；本轮按体内LF、外围空白、独立合法整调用行及整字段丢文分别判断。旧OPEN/WAIT保生成时点，不因旧字段重开第五已闭项。',
 '', '## 执行、任务与限制','',
 'execution-evidence.json保指定18次Ruby尝试及各家族实际向量/失败/捕获异常/覆盖重跑。K tee0不冒称Ruby0；Purifyv2捕获错误exit0仍无效；F实际5次而不是3次。纯Fraction/字段/PE/SF2/安全Marshal/字形/COFF工具不是参考、IL、宿主或玩法模型执行。旧R4 review4、R5 review4、update0另列。',
 '', 'requested sol/ultra/default禁Fast；实际model/effort/tier/speed未回显UNVERIFIED。8CLI parent真实thread.started UUID、3collaboration canonical任务、root及子任务可查状态/argv/PID/start/end/stdout/stderr/raw-status均登记；缺UUID/时间/独立stderr照实缺，不查询额度/认证或反复追配置。',
 '', 'INC-R6-001真实流程违规及L14元数据/工具记录缺口保留。部分早期工具仅平台回显，关键最终校验另capture，不能替旧时间。Native/字体/音频/地图/资源/外部服务恢复条件见limits-and-missing-materials.md，有限可读binary缺读0不等全部机器码/宿主通过。',
 '', '## 后续有限交接','',
 '14批、每required恰一主批、54formal候选路径、24冲突对、100节点110边DAG。所有作者只写隔离candidate mirrors；R6-I独占正式共享文件/公共台账；各批非作者验收后接收，共享整篇/跨域/历史回归独立实际复验，再正式接受和CLOSED。可独立准备首波14批；当前协作工具容量4（root占1），CLI/未来云端实际容量需核，不宣称无限。',
 '', '未来author请求gpt-6.1-sol/xhigh、reviewer ultra/default禁Fast。实际可用CLI查询和启动方法、完整逐项中文合同、manifest、作者/审者入口将由后继handoff绑定本core和实际发布对象。该交接准备不启动任务。',
 '', '`UPDATE_NOT_STARTED`。', '']
(ROOT/'final-report.md').write_text('\n'.join(report))
(ROOT/'README.md').write_text('# R6独立审查包\n\n入口：final-report.md、summary.md、coverage/final-coverage.json、findings/normative-records.json、execution-evidence.json、control/task-register-current.json。\n\n后继完整handoff：cloud-sixth-update-handoff-prompt.md / cloud-sixth-update-handoff-manifest.json。core/pub/传输身份由publication后继回执外部绑定，文件不自哈希。UPDATE_NOT_STARTED。\n')
print(json.dumps({'ready':True,'records':65,'required':56,'policies':7,'limits':14,'available_unreviewed':0,'update_started':False}))
