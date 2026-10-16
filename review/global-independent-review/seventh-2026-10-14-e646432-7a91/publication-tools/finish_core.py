"""Write root report/current task index and the non-recursive core reception."""
import datetime
import hashlib
import json
from pathlib import Path

R=Path(__file__).resolve().parents[1]
def read(p):return json.loads((R/p).read_bytes())
def put(p,d):
    q=R/p
    if q.exists():raise FileExistsError(p)
    q.parent.mkdir(parents=True,exist_ok=True)
    q.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n' if not isinstance(d,str) else d)
def sha(p):return hashlib.sha256((R/p).read_bytes()).hexdigest()
def main():
    coverage=read('coverage/summary.final.json');findings=read('findings.json');canonical=read('canonical-records.json')
    if coverage['canonical_reception']['exact_unreceived_count'] or canonical['pending']:raise ValueError('not closed')
    now=datetime.datetime.now(datetime.timezone.utc).isoformat();contexts=canonical['root_actual_context'];tasks=[]
    old={v['logical_id']:v for v in read('progress.json')['tasks']}
    role_ids={'R7-M01':'01a13d94-ace2-7212-908f-48f56a290fda','R7-M02':'01a13d94-fb64-7d42-ac1d-00537e33823c','R7-M03':'01a13d95-406a-7e42-84d6-410b9499e047','R7-C14':'01a13e0a-7a77-7572-8d38-bfe7d3082fe1'}
    for names,original in [('C01 C07 C10 C12 C17','M02'),('C02 C08','M01'),('C03 C13 C18 J09','M03'),('C19 C20','C14')]:
        for n in names.split():role_ids['R7-'+n]=role_ids['R7-'+original]
    for d in sorted((R/'tasks').glob('R7-*')):
        if not d.is_dir():continue
        logical=d.name;t=read('tasks/'+logical+'/task.json') if (d/'task.json').exists() else {}
        entry={**old.get(logical,{}),'logical_id':logical,'write_directory':'tasks/'+logical,'task_metadata':t,'semantic_status':t.get('status',t.get('state','UNVERIFIED')),'actual_platform_id':role_ids.get(logical,'UNVERIFIED'),'output_entry':'tasks/'+logical+'/report.md','qualification':'Task metadata/process state and final domain reception are different. Earlier personal unread complements remain scoped to that reader; final canonical receiver supplies global exact result.'}
        if (d/'launch.json').exists():
            launch=read('tasks/'+logical+'/launch.json');ids=[]
            with (d/'events.jsonl').open() as inp:
                for line in inp:
                    try:v=json.loads(line)
                    except ValueError:continue
                    if v.get('type')=='thread.started':ids.append(v['thread_id'])
            entry.update(actual_platform_id=ids[0] if len(set(ids))==1 else 'UNVERIFIED',actual_launch=launch,all_observed_thread_ids=sorted(set(ids)),public_log_projection='publication-transport/core/platform-io/tasks__'+logical+'__events.jsonl.jsonl')
        tasks.append(entry)
    descendants=read('startup/actual-descendant-platform-metadata.final.json')
    ids={v['actual_platform_id'] for v in tasks if v['actual_platform_id']!='UNVERIFIED'}|{v['platform_thread_id'] for v in descendants['records']}|{contexts}
    prog={'schema':'r7.final-task-register.v1','at_utc':now,'root_actual_platform_id':contexts,'status':'REVIEW_SEMANTIC_CORE_READY_PUBLICATION_PENDING','tasks':tasks,'logical_task_directories':len(tasks),'actual_CLI_parent_launches':sum('actual_launch' in v for v in tasks),'actual_known_distinct_contexts':len(ids),'descendant_metadata':descendants,'model_configuration':{'requested':'gpt-6.1-sol/ultra/default normal; Fast forbidden','actual_model_effort_tier_speed':'UNVERIFIED; requested argv or local metadata is not backend certification'},'live_status_qualification':'Actual CLI parent start/end/exit in each launch. Child lifecycle unknown where no real completion receipt; no universal all-sessions-stopped claim. Visible own collaboration tree and finite conflict checks are separately retained. No conflicting fixed-input writer found.','task_completion_qualification':'All source/formal/effective material obligations are actually received in C17 exact canonical overlays; task process exit is not semantic closure.','update_started':False}
    put('progress.final.json',prog)
    put('reading-ledger.final.json',{'schema':'r7.root-final-reading-index.v1','status':'BOUNDED_REVIEW_COMPLETE','source_identity_and_axes':'inventory/source.final.json','formal_identity_and_full_literal_axis':'inventory/formal.final.json','current_supplements':'inventory/supplements.final.json','source_units':'tasks/R7-C17/canonical-source-units.json','source_fact_consumer_clause_objects':'tasks/R7-C17/canonical-source-fact-registry.json','formal_clauses':'tasks/R7-C17/canonical-formal-coverage.json','authored_subassertions_and_premises':'tasks/R7-C17/canonical-clause-registry.json','finite_decoded_programs':'tasks/R7-C17/canonical-program-index.json','all_effective_purpose_scopes':'tasks/R7-C17/canonical-supplement-purpose-index.json','raw_physical_display_recovery':'tasks/R7-C12/coverage-reception.json','current_exact_unread':'tasks/R7-C17/final-unreceived-ids.json','exact_readers_receipts_payload_SHA_and_ranges':'tasks/R7-C17/final-input-bindings.json plus original named ledgers. The lossless core payload index binds every raw evidence byte.','counts':coverage,'not_host_execution':True})
    table='\n'.join('| '+v['id']+' | '+v['severity']+' | '+next(c['title_zh'] for c in canonical['records'] if c['id']==v['id'])+' |' for v in findings['records'] if v['classification']=='required')
    report=f'''# 第七轮独立全局审查报告

结论：可得、可安全审读的静态文本和有限结构审查及双向接收已完成，发现 **27项必修（10 P2 / 17 P3，P1为0）**。这不是引擎行为等价或宿主可用性PASS。正式规格、planning/audit、reference、旧报告及接受/关闭回执未修订；**UPDATE_NOT_STARTED**。

固定B为e646432c644dec04d306842cc5a559a29c718fbc，workspace tree为84f79ec6e772aacbf3a464fde68cdc5a280e2950，正式tree为ebbe29f2bc88cd17de7072bf440c6fa8c8c7089c；交付tag delivery/sixth-round-closed-final-20261014保持指向B。R为8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b/tree7589c800b61ba13a13040ed0d686979b80a84fd0。完整origin、绝对路径、历史各阶段、readiness769532字节及其SHA、启动差异在startup/fixed-inputs.json及startup/readiness.md。审查根日期保留初始纽约10月14日标签，所有真实执行UTC为10月15日；不借日期标签改变输入。

启动READY_WITH_LIMITS。已知5049未跟踪分98原保全项和4951既有重新分类项；预核及core前实核原98、ignored4963、R工作文件434全字节/大小/模式变化0，正式131与固定B一致。R tracked432，另两份.DS_Store仅OS元资料身份处置。七其它worktree的HEAD/branch/status与准备一致，不外推为整树字节证明；归档tag与恢复身份保持。活动接口无完整全局停机会话证明，记UNVERIFIED；未发现具体重叠写者。没有reset/清理/更改忽略规则或另换clone掩盖差异。

参考 **432/432路径**、原分块 **2668/2668单元**；正式 **131/131份、29493行、21702/21702结构块**；固定有效补充 **9/9、2643357字节、39434 JSON节点及2424 Markdown行**；另 **323** 个派生/历史资格载荷按实际用途接收。可得可审的真正未读和精确待接收均 **0**。源44906485字节，初始UTF8行计389604；散文字面、PBS/序列化字段结构、资源有限结构和opaque native边界分别记，不能把全部这些行当逐字面审校行数。

源轴323文本/元资料、93 typed data、11资源、5 PE；后者的有限内嵌程序与消费者实际审读，机器码/后端未知另列。正式21702块中20046接实际作者clause scope，1656为具名结构处置（原1381与新增275分开）；这些不是21702或20046个独立需求。当前5732源事实对象指针、25001条款对象指针是可恢复对象索引，不是新增问题或独立断言计数。每个compound条款仍以完整原对象的前提、子断言和反证接收为准；定位交叠不创造事实。

覆盖依据在reading-ledger.final.json、coverage/summary.final.json及C17最终索引。原partial/WAIT/UNREAD保留生成时点；M16数据的D01–15、M17有限程序D06/D09/D12、M18字体/SF2/BMP、M13的J14/J15/J16、M09的J09、C15/C16、H13/H16–18、H19–22均按精确原ID和完整对象/范围接收。D10的86377显式字段/7586记录/52418缺席义务，以及漏分两份encounters的582字段、38记录、130组件省略已补接；D11的15448字段与113合同独立。旧scalar/hash相等从未提升成完整case批准；56项R6当前完整合同及其351个case记录按原分母新读、静态接收，未执行。字面解析/接口/负证据/消费者链保留真实限定。

原提案、异议、缩窄及反证在findings.json；当前规范化完整37项在canonical-records.json，其原引用基准tasks/R7-C19保持。27必修均有实际不同context的非提出者证据，C19核七组有效内容及载荷变更，C13提供完整中文视图。主会话对自身提出的本轮行政/数据接收不借角色名自证；M02/C12/C17同一实际审者，M02自己原事实只机械核并保留C02/C03非作者证据。C14/C19/C20同一实际审者，J16反证最终由root独立接收。请求gpt-6.1-sol/ultra/default普速禁Fast，实际参数回显UNVERIFIED；真实task/context/PID、日志、原始请求/退出分开登记，不查额度或认证。

| 必修ID | 级别 | 最低问题范围 |
| --- | --- | --- |
{table}

其余为7 optional entries（5新根、2沿既有optional根别名）、1 no-required revision、2 policy entries（1新font兼容根、1UTIL-03原policy事实资格facet）。额外H08-OF01/OF02是两个可选导航facet、0新增mandatory；6个条件可选贡献已补图。R6原8 optional/1 FLOAT/7 policy/14 limits/1 no-required分开完整保留，不选择policy或无证据重开旧关闭。撤销/别名/原反证不删除。H08必修只DEBUG001导航，两个optional不并入。

R1–R6准确历史资格、原合同、不同范围和生成时点在history/qualifications.final.json与43份恢复身份。R5唯一激活92关闭、R6的14批56实际接收→实际独立内容审查→最终登记依赖审查→ACCEPTED→CLOSED均保留；旧FAIL与修订PASS不同阶段不混用。53正式改动/78未改不替代131；R6的100依赖节点110边有限流程门不证明运行。

执行完整区分SOURCE_STATIC、DERIVED_VECTOR、TOOL_VALIDATION和实际观察。R7仅固定源69字节数字谓词在本机Ruby2.6隔离进程的 **1过程/10输入** 观察，10结果吻合，含终末LF；不是随附游戏Ruby宿主。另有限常数算术只属算术推导工具，不是完整模型。完整独立行为模型、native游戏宿主、Demo、媒体合成/实际像素、真实存档/回放均0。新命令census15537项是重叠回执/CLI证据项，非唯一进程/成功测试数；498已知非零、63退出未知及91原metadata gap记录保留。61个人工候选均按实际工具/命令资格接收；后续保护/发布命令另留真实日志。R6历史18次Ruby尝试12已知0/4非零/2未知、17进入定义/1未加载，含无效/重复替身，不称18成功测试。

L01–L14在当前limits接收和完整原记录中逐项保留：地图/完整工程、资源与宿主、native、有限内嵌程序与实际GPU、animmaker/extendtext目标依赖、字体/SF2目标宿主、序列化启动、动态扩展/无界配置、外部状态/服务、元资料用途和原执行记录缺口。可读材料已审而宿主未知；opaque supply/startup/ABI不假装已读机器码，也不扩大为无限CFG义务。语言质量未作逐文本翻译审校。

操作偏差也保留：部分子任务忽略协调者的禁止派生局部提示，但人已授权并行，实际子context登记且未接收者不获信用；H12/J01日志double-prefix仍在本轮根内；J16误建并删除本轮INVALID；root一次重复核验覆盖两份生成startup快照，初始精确字节未恢复，实际05:11副本及说明保留，后加唯一suffix禁止覆盖。均未掩盖成原记录成功或源/正式修改。C20还独立指出并促成发布工具的取数/日志/进程/路径/环境问题修复，真实旧版本与有限工具测试另存。

有限后续计划13批、27唯一主责、26作者/审者入口；全部13隔离author无已证作者阻塞入边，镜像写写冲突0，第一波13不是服务slots。50实际/可选目标和共享接收图包含39个同目标批次对；实际写者仅R7-I，实际整合后新独立R7-IR。optional采用另裁，不增加mandatory。作者xhigh、审者ultra/default普速禁Fast。manual_launch.py仅提供未来手动argv/真实PID/stdin/日志包装，本轮26次dry-run没有启动Codex或update。

语义core先冻结，后继交接包含实际core commit/tree；再普通push并完整远端逐文件/解码读回；最后包外publication/final-delivery-binding.json绑定真实发布C1和交接载荷身份。文件不写自身commit/tree。体量较大的任务证据保留为无损gzip内容对象及逐原路径身份索引，可恢复完整真实I/O。原私有平台流仅本地保留，公开tool I/O投影单列完整身份，不能声称原私有流已远端回读。传输与hash不替代本轮新语义阅读。
'''
    put('final-report.md',report)
    put('summary.md',f'''# R7 交付摘要

静态全量双向审查及具名接收完成；可审未读0。参考432、正式131（21702结构块）、有效补充9及323派生用途载荷。27必修=10P2/17P3；另7optional、2额外optional导航facet、1no-required、2policy entries。R6各非必修原分母独立。

后续13批，第一波13隔离author，无作者blocking边；实际共享写者R7-I，整合后新R7-IR。完整中文手动交接位于handoff/，发布身份由publication/final-delivery-binding.json外部绑定。

R7真实参考观察仅本机Ruby谓词1过程/10输入；完整模型/游戏宿主/Demo/native媒体/真实存档回放0，14项限制具名保留。正式规格及参考未修改。**UPDATE_NOT_STARTED**。
''')
    put('README.md','''# 第七轮独立全局审查

当前主入口：final-report.md、summary.md、canonical-records.json、coverage/summary.final.json、reading-ledger.final.json、progress.final.json。旧progress.json及所有中间WAIT/UNREAD保留原时点，以final后继和具名接收为当前结论。

完整中文可复制合同：handoff/cloud-seventh-update-handoff-prompt.md；结构化manifest、三图与26完整入口同目录。发布core/C1及逐载荷bytes/SHA/blob和完整远端回读结果由publication/final-delivery-binding.json固定，最后C2自身身份在交付消息给出。UPDATE_NOT_STARTED。

大量任务证据采用无损对象传输；在项目根运行（destination必须不存在）：

```sh
python3 -B review/global-independent-review/seventh-2026-10-14-e646432-7a91/publication-tools/transport.py restore --package review/global-independent-review/seventh-2026-10-14-e646432-7a91/publication-transport/core --destination /private/tmp/r7-e646432-restored
```

恢复后原tasks/<入口ID>/report.md、task.json、logs/及精确矩阵均可读；如查看R7-M09：

```sh
cat /private/tmp/r7-e646432-restored/tasks/R7-M09/task.json
tail -n 40 review/global-independent-review/seventh-2026-10-14-e646432-7a91/publication-transport/core/platform-io/tasks__R7-M09__events.jsonl.jsonl
```

原私有reasoning流不发布，公开命令I/O投影完整身份单列；不把传输核验称语义审查。原输入B/R、历史恢复43份、旧报告、正式131和全部既有环境只读保护。

未来仅由用户手动委派。一个可复制的请求/状态示例（本轮不得加--launch）：

```sh
python3 -B review/global-independent-review/seventh-2026-10-14-e646432-7a91/publication-tools/manual_launch.py --project . --package review/global-independent-review/seventh-2026-10-14-e646432-7a91/handoff --entry R7-U01-A
python3 -B review/global-independent-review/seventh-2026-10-14-e646432-7a91/publication-tools/manual_launch.py --project . --package review/global-independent-review/seventh-2026-10-14-e646432-7a91/handoff --entry R7-U01-A --status
```

用户在另行update分支授权启动时才显式加--launch；立即记录实际Popen.pid，完整分流events/stderr和wait退出，状态不由进程0推导语义PASS。云端先解析实际project/package路径并保存映射，现有本机绝对路径不冒充未来云端路径。
''')
    sections={'coverage':'coverage/summary.final.json','source_inventory':'inventory/source.final.json','formal_inventory':'inventory/formal.final.json','supplement_inventory':'inventory/supplements.final.json','source_units':'tasks/R7-C17/canonical-source-units.json','source_facts':'tasks/R7-C17/canonical-source-fact-registry.json','formal_units':'tasks/R7-C17/canonical-formal-coverage.json','clause_subassertions':'tasks/R7-C17/canonical-clause-registry.json','finite_programs':'tasks/R7-C17/canonical-program-index.json','supplement_purposes':'tasks/R7-C17/canonical-supplement-purpose-index.json','interfaces':'coverage/current-interface-reception.json','reading_ledger':'reading-ledger.final.json','limits':'tasks/R7-C17/limits-and-alias-reception.json','historical_qualifications':'history/qualifications.final.json','inherited_nonmandatory':'history/inherited-nonmandatory.final.json','history_recovery':'history/recovery-identity-verification.json','aliases_tombstones':'evidence/aliases-and-tombstones.final.json','execution':'execution/phase-summary.final.json','tasks':'progress.final.json','c13_identity_index':'tasks/R7-C13/identity-index.json','independent_record_integrity':'tasks/R7-C19/final-adjudication-integrity.json'}
    required=list(sections.values())+['findings.json','canonical-records.json','tasks/R7-C13/chinese-contracts.json','tasks/R7-C13/chinese-handoff.md','batch-plan.final.json','dependency-graph.json','file-conflict-graph.json','final-report.md','summary.md','startup/fixed-inputs.json','evidence/chinese-contract-view-root-reception.json','evidence/root-h22-counter/counter-review-and-facets.json']
    put('evidence/final-root-reception.json',{'schema':'r7.final-root-reception.v1','status':'FINAL_REVIEW_INPUT_ACCEPTED','at_utc':now,'root_adjudicator':'R7-I','actual_context':contexts,'scope':'Actual full source/formal/supplement and finite unit review with independent finding counters and exact successor receptions; static completed, not behavior/native/Demo PASS.','effective_unread':0,'pending':[],'update_started':False,'json_sections':sections,'accepted_payload_sha256':{p:sha(p) for p in sorted(set(required))},'nonrecursive_rule':'This receipt does not contain its own hash/commit; actual archive/core and later publication binding fix its bytes.','C17_global_pass_false_preserved':True,'final_plan_confirmed':'C18 corrected graphs include six optional contributions without expanding27 required; 13 batches/26 entries; xhigh authors/ultra reviewers/default/noFast.','production_renderer':'Root archive-aware renderer consumes immutable actual core, future cloud paths UNVERIFIED; P01/P03 candidate production guards not misrepresented as successful production validation.'})
    (R/'progress.md').write_text('# R7 当前状态\n\n静态全量语义及双向接收完成，可审未读0；27必修，UPDATE_NOT_STARTED。当前完整任务/真实入口请读progress.final.json，覆盖请读coverage/summary.final.json。语义core/交接发布正在执行，最终实际身份与远端回读由publication/final-delivery-binding.json固定；旧progress.json保留原增量时点。\n')
    print(json.dumps({'core_reports_written':True,'logical_tasks':len(tasks),'actual_CLI_parent_launches':prog['actual_CLI_parent_launches'],'actual_known_contexts':len(ids),'accepted_payloads':len(set(required)),'update_started':False}))
if __name__=='__main__':main()
