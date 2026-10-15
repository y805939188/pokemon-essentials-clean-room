"""Append the same independent review's completed findings; never execute a target."""
from pathlib import Path
from collections import defaultdict
import json,hashlib,datetime,os,subprocess,shutil
ROOT=Path('/workspace/r7-ir-R7-U10-wave3'); REPO=ROOT/'result-checkout'
PREFIX='review/remediation-seventh-20261015-prepare/integrated-reviews/R7-U10/r1/'
OUT=REPO/PREFIX; EV=OUT/'evidence'
INITIAL='4188ee2bfb8e4b6f3c5ac2c8e8be24384f93d0f4'
MI='e54f54a2cb32e546eabd46aaf53ed45b30a8af89'; FI='b98fa82f8a08b5630ac568cbe8c34f607f623cfb'
B='e646432c644dec04d306842cc5a559a29c718fbc'
def utc():return datetime.datetime.now(datetime.timezone.utc).isoformat()
def ident(b):return dict(bytes=len(b),sha256=hashlib.sha256(b).hexdigest(),git_blob=hashlib.sha1(f'blob {len(b)}\0'.encode()+b).hexdigest())
def dump(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def git(*a):return subprocess.check_output(['git','-C',str(REPO),*a],stderr=subprocess.PIPE)
assert git('rev-parse','HEAD').decode().strip()==INITIAL
archive=EV/'initial-WAIT';archive.mkdir(exist_ok=True)
for name in ['report.md','per-id.json','review-input-receipt.json','artifact-manifest.json']:
    old=git('show',INITIAL+':'+PREFIX+name)
    dest=archive/name
    if dest.exists():assert dest.read_bytes()==old
    else:dest.write_bytes(old)
shutil.copyfile(ROOT/'final-remote-readback/complete-remote-readback.json',EV/'initial-WAIT-remote-readback.json')
shutil.copyfile(ROOT/'final-remote-readback/git-commands.json',EV/'initial-WAIT-publication-commands.json')
shutil.copyfile(ROOT/'bootstrap/read_current.py',EV/'read-current.py')
pi=json.loads((archive/'per-id.json').read_text())
receipt=json.loads((archive/'review-input-receipt.json').read_text())
audit=json.loads((EV/'byte-audit.json').read_text())
supp=json.loads((EV/'supplemental-checks.json').read_text())
frozen=json.loads((ROOT/'bootstrap/integrated-input.json').read_text())
plan=json.loads((ROOT/'actual-plans/R7-U10.json').read_text())
journal=json.loads((ROOT/'actual-input/integration/applied-clauses.json').read_text())
now=utc()
shared=['audit/source-traceability.md','planning/feature-matrix.md','deliverables/final-specification-set/test-catalog/demo-dx-wp72-73-74-75-76-77.md']
full=shared+['deliverables/final-specification-set/demo-dx/'+p for p in ['wp73-b-world-editors.md','wp74-battle-animation-authoring-and-exchange.md','wp75-project-conversion-and-authoring-tools.md','wp77-demo-evidence-and-capability-coverage.md']]+['deliverables/final-specification-set/pokemon-rules/'+p for p in ['wp34-inheritance-and-offspring.md','wp62-pokedex-records-regions-and-content.md']]
deliveries=[json.loads(l) for l in (EV/'continuation-read-receipts.jsonl').read_text().splitlines()]
coverage=[]
for path in full:
    raw=(ROOT/'actual-input/actual'/path).read_bytes(); lines=raw.splitlines(keepends=True)
    seen=set()
    for d in deliveries:
        if d['path']==path:seen.update(range(d['first_line'],d['last_line']+1))
    missing=sorted(set(range(1,len(lines)+1))-seen)
    assert not missing,(path,missing)
    assert raw==git('show',MI+':'+path)
    coverage.append({'path':path,**ident(raw),'total_lines':len(lines),'complete_line_delivery':True,'missing_lines':missing,'semantic_review':'COMPLETE_BY_THIS_SAME_REVIEWER_IN_CONTINUATION','qualification':'Delivery coverage is mechanical evidence only; substantive findings are separately stated below. Truncated displays were supplemented with narrower reads.'})

# Each contribution in all three shared files is compared with its exact candidate
# and mapped back to its own independent result; no other batch gets a new verdict.
bindings={b['id']:b for b in frozen['prior_source_bindings']+frozen['new_source_bindings']}
notes={
 'R7-U01':'整数身份/序号比较、三类节头别名和指标缺字段默认/整条克隆分层；未改WE行，不消除U10资源绑定例外。追加的旧anchor债务、作者时点和条件同步边界保留。',
 'R7-U02':'手柄15按钮/6轴只为有限解析词汇，注册/宿主桥仍未读；不据此重定义编辑器USE/ACTION/BACK物理输入、尾部刷新或资源重绑。U01后接U02的两EOF段保序。',
 'R7-U10':'WE-M17登记/标志/绑定三状态、AN-M09旧游标和普通对照、TOOL-AN17行及来源/矩阵同一有限静态合同；实际条款自行审读，不继承r2 PASS。',
 'R7-U11':'T-WP75、F18-04及EXT01–12属文字扩展请求，未借用animmaker的图像保存规则。DX同EOF先U11再U10，两工具组及CV-M29原文档资格并存。',
 'R7-U12':'audit/matrix仅当前§5.2→§5.3勘误转引；行为与旧R6身份/状态不变，不把历史原回执改成新字节。',
 'R7-U13':'SF2配置声明/原生消费/合成声音分层，T-WP15与F05-02的有限新增不升级U10媒体/图像库执行资格。'
}
shared_map=[]
for h in audit['journal_hunks']:
    if h['path'] not in shared:continue
    b=bindings[h['batch_id']];assert h['candidate_commit']==b['candidate_commit']
    assert all(h['checks'].values())
    if h['batch_id']=='R7-U10':
        report=ROOT/'actual-input/candidate-review/candidates/R7-U10/evidence/reviewer/r2/report.md'
        per=report.with_name('per-id.json')
    else:
        report=ROOT/'actual-input/shared-candidate-review'/h['batch_id']/'report.md'
        per=report.with_name('per-id.json')
    manifest_row=next(x for x in plan['artifacts'] if ROOT/'actual-input'/x['local_path']==report)
    assert manifest_row['commit']==b['candidate_review_commit']
    pdata=json.loads(per.read_text()); records=pdata['records']
    ids={r.get('id',r.get('record_id',r.get('required_id'))):r.get('verdict',r.get('conclusion',r.get('status'))) for r in records}
    assert all(ids[i]=='PASS_SCOPED_CANDIDATE' for i in h['required_ids']),ids
    actual=(ROOT/'actual-input/actual'/h['path']).read_bytes();ls=actual.splitlines(keepends=True);a,z=h['actual_lines_half_open']
    clause=b''.join(ls[a:z]);assert ident(clause)==h['added_identity']
    shared_map.append({**h,'actual_byte_offsets_half_open':[sum(map(len,ls[:a])),sum(map(len,ls[:z]))],'original_independent_result_commit':b['candidate_review_commit'],'original_independent_reviewer':b['reviewer_context'],'original_report_path':manifest_row['path'],'original_report_identity':ident(report.read_bytes()),'original_verdicts':ids,'current_preservation_and_compatibility':'PASS_SCOPED_PRESERVATION_COMPATIBILITY_ONLY','semantic_basis':notes[h['batch_id']],'no_other_batch_new_semantic_PASS':h['batch_id']!='R7-U10'})
assert len(shared_map)==16
dump(EV/'continuation-shared-contributions.json',{'schema':'r7.u10.full-current-shared-contributions.v1','utc':now,'reviewer':pi['reviewer_thread'],'MI':MI,'FI':FI,'whole_files':coverage[:3],'contributions':shared_map,'root_annotations':{'paths':shared[:2],'range':'last four lines of each whole file','result':'PASS_SCOPED_PHASE_ANNOTATION','basis':'25/27 applied,12/13 batches; actual PASS/ACCEPTED5/27,3/13; CLOSED0. Author-time labels remain time-qualified. No borrowed future signature.'},'strict_journal_exception':supp['prior_navigation_annotation'],'qualification':'Current preservation and U10 compatibility only. Other original verdicts remain bound to their own candidates and MI/FI; no global acceptance.'})

history_contract_raw=git('show',B+':review/remediation-sixth-20261014-prepare/contracts/R6-U07.json')
history_contract=json.loads(history_contract_raw)
hc=history_contract['scope_contracts'][6]
expected=hc['bidirectional_evidence']['source'][0]['payload_identity']
new_source=(ROOT/'supplement/independent-history/AnimEditor_Interpolation.rb').read_bytes()
assert all(ident(new_source)[k]==expected[k] for k in ['bytes','sha256','git_blob'])
historic=[
 {'id':'H-WE-STATE-SAVE','applies_to':['GR7-M15-001'],'actual':'WP73-B §7.1–§7.5; WE-M15–20; B19-C016; DXCOMP-C06–08','finding':'首缺停止/自有阴影拒绝、同值确认不新增标志、既有true保真、USE留项/ACTION前进、普通坐标BACK刷新、Yes先档案后按当时非零后缀选PBS、No/无确认改动重载；失败保已达前缀。尺寸资源绑定例外不撤销这些数据/保存合同。','result':'PASS_SCOPED_STATIC_PRESERVATION'},
 {'id':'H-R6-AN002','applies_to':['GR7-M15-002','GR7-M17-001'],'binding':{'commit':B,'path':'review/remediation-sixth-20261014-prepare/contracts/R6-U07.json','pointer':'/scope_contracts/1','file_identity':ident(history_contract_raw)},'actual':'WP74 §3.2/§7.1/§7.4/§11.1/§16; AN-M09/M12','finding':'有效A删成B后BACK而未Load，Focus Target写B=1、A仍4；新单元读A，保存/单项导出读B；取消与重新Load控制保留。M09另限旧selected2缩3→2后未导航，不能把原0/1也判失败。','result':'PASS_SCOPED_STATIC_PRESERVATION'},
 {'id':'H-R6-AN007','applies_to':['GR7-M15-002','GR7-M17-001'],'binding':{'commit':B,'path':'review/remediation-sixth-20261014-prepare/contracts/R6-U07.json','pointer':'/scope_contracts/6'},'source':{'path':expected['path'],'commit':expected['commit'],**ident(new_source),'read_ranges':[[210,235],[295,335]],'matches_frozen_historical_payload_identity':True},'actual':'WP74 §8.6/§19-8; B20-D024','finding':'自动默认点0.3333/0.6666、约99.99/199.98和宿主量化未知保持；显式0/1/8/11、N5向量原样，1/4可精确表示。一般N浮点端点仍optional，未被U10采纳。','result':'PASS_SCOPED_STATIC_PRESERVATION'},
 {'id':'H-EXCHANGE-CACHE','applies_to':['GR7-M15-002','GR7-M17-001'],'actual':'WP74 §3.1–3.4/§11–16; AN-M01/M09–12/M24–33; DXCOMP-C06–08','finding':'临时/有效/空首槽缓存分支、类型正确不保证帧结构、单项导入的替换前后保护、批量交换部分写入、零有效名不写旧映射、磁盘与预载缓存分开。图像工具没有生成动画对象/.anm或自动关联桥。','result':'PASS_SCOPED_STATIC_PRESERVATION'},
 {'id':'H-TOOL-LIMITS','applies_to':['GR7-M17-001'],'actual':'R6 final-delivery L1433–1447 L06/L07; WP75 §14; WP77 §7/§9/§11','finding':'图像/XML库空矩形、编码、错误格式化、文件失败与宿主运行未知继续有效。文字扩展四目标请求与图像工具分开；工具入口不授Demo事件链，③④仍0。','result':'PASS_SCOPED_STATIC_PRESERVATION'},
 {'id':'H-OLD-PRIMARY','applies_to':['GR7-M17-001'],'actual':'specs/demo/WP74 §18/§20/§22/§23; T-WP74; F18-03','finding':'旧specs为早期受审输入，保持完整B身份及历史未读exe/待审时点；当前净化WP74及dated追溯给新静态证据。不要求回写旧身份，也不把旧文档RMXP/PNG用途句作为当前机器码结果。条件同步未激活。','result':'PASS_SCOPED_HISTORICAL_ROLE_PRESERVATION'}
]
accepted_domains=[
 {'files':['combat-requirements/wp39-battle-context-and-participants.md','combat-requirements/wp41-switching-positioning-and-escape.md','test-catalog/combat-requirements-wp39-40-41-42-45.md'],'read_scopes':['WP39 L116–252','WP41 L45–135','catalog BC26–31/SW30–35'],'prior_records':['GR7-M03-001','GR7-M03-002'],'finding':'席位/业主/开场和实际替换派出后的登记、位置恢复与非致死危害仍为战斗域；U10仅编辑器资源与工具请求，未把编辑器预览重绑推广为普通战斗广播刷新，未改目标补救、决定3消费或异常前缀。'},
 {'files':['pokemon-rules/wp34-inheritance-and-offspring.md','test-catalog/pokemon-rules-wp19-21-22-23-34.md'],'read_scopes':['WP34全文233行','BR27–31/R7-U05-PF01–09/R4-IF01–06 L250–305'],'prior_records':['GR7-M07-002'],'finding':'按个体动态形态读取可先提交、条件登记并在缺图后保前缀；它不同于按显式物种/形态的指标编辑与generic shadow选择。母/子相等门、N0缓存、容量后检和非空last保持，不把预览BACK恢复扩成图鉴/形态事务。'},
 {'files':['pokemon-rules/wp62-pokedex-records-regions-and-content.md','user-interface/wp66-b-storage-and-pokedex-ui.md','test-catalog/pokemon-rules-wp53-60-61-62-69-70.md'],'read_scopes':['WP62全文197行','WP66-B §7/§8 L236–272','catalog L136–180及R4-PD01–05 L241–254'],'prior_records':['GR7-M14-001','GR7-M14-002'],'finding':'内部出场包装与全局形态提交接收者/门不同；完整单条编号与摘要/简略分开，普通图像请求不改记录，Forms多项首轮/移动写false且BACK不回滚另算。资源解析同为nil不证明素材存在。U10不改变这些记录、编号或取消合同。'}
]
for d in accepted_domains:d['result']='PASS_SCOPED_U10_INTERSECTION_COMPATIBILITY';d['no_old_ID_recertification']=True
dump(EV/'continuation-semantic-findings.json',{'schema':'r7.u10.completed-semantic-review.v1','utc':now,'reviewer':pi['reviewer_thread'],'MI':MI,'FI':FI,'current_full_read':coverage,'historical_regressions':historic,'prior_accepted_domain_intersections':accepted_domains,'prior_accepted_byte_preservation':audit['prior_accepted_files'],'historical_independent_reports_read_full':['U04-U05/r1/report.md','R7-U09/r1/report.md'],'root_responsibility_boundary':'本审者完成当前三ID内容、具名静态历史回归和消费者相容性；R7-I尚须实际接收新结果的精确commit/tree，登记语义owner/shared receiver/直接传递领域及历史责任，再分别ACCEPTED/CLOSED。根未登记不是本审者内容WAIT。','input_blockers':[],'review_obligations_remaining':[],'reference_behavior_executed':0,'all_vectors':'DERIVED_VECTOR / NOT_EXECUTED','global_old_56_92_recertification':False})

reasons={
 'GR7-M15-001':'完整MI WP73-B和DX目录及三共享文件、源绑定/刷新消费者独立读毕；登记/确认/资源三状态、普通/取消/确认/重开/保存/异常前缀相符，U01指标与已接受形态/图鉴域相容。',
 'GR7-M15-002':'完整MI WP74与DX目录独立读毕；selected2缩3→2未导航、0/1正常控制、Delete尾添/取消及Load已达前缀准确；AN002画布对象和AN007默认近似/显式N5历史范围保留。',
 'GR7-M17-001':'独立静态解码全部15方法/11EH并审读输入/布局/保存分支；完整WP74/WP75/WP77、TOOL-AN17行与三共享全文相符。.anm、停用转换、关联/缓存、U11和Demo/原生限制不被扩大。'
}
for r in pi['records']:
    r['initial_history']={'commit':INITIAL,'verdict':'WAIT','preserved_exact_file':'evidence/initial-WAIT/per-id.json','reason':'当时内容义务未完成，后续在同一context补完；旧WAIT不改写为历史PASS。'}
    r['verdict']='PASS_SCOPED_ACTUAL_INTEGRATION';r['verdict_reason']=reasons[r['id']]
    for v in r['vectors']:
        v['content_check']='PASS_SCOPED_STATIC_ACTUAL_CONTENT';v['gate_credit']=True
        v['gate_credit_kind']='FINITE_STATIC_CONTENT_REVIEW_ONLY_NOT_EXECUTION'
    for h in r['actual_clause_bindings']:
        lines=(ROOT/'actual-input/actual'/h['path']).read_bytes().splitlines(keepends=True);a,z=h['actual_lines_half_open']
        h['actual_byte_offsets_half_open']=[sum(map(len,lines[:a])),sum(map(len,lines[:z]))]
        h['line_indices_are_zero_based']=True
    r['dependencies']['finite_current_source_domain_history']='SATISFIED_BY_THIS_SAME_INDEPENDENT_REVIEW_AT_FIXED_MI'
    r['dependencies']['global_dependencies']='NOT_ASSERTED_SATISFIED'
    r['unmet_gates']=[{'id':'ROOT-EXACT-RECEPTION-RESPONSIBILITY','owner':'R7-I','state':'PENDING_SEPARATE_ROOT_ACTION_NOT_A_CONTENT_REVIEW_BLOCKER','required_action':'接收本新结果commit/tree并登记semantic owner、CG/shared receiver和具名直接/传递/领域/历史责任；随后分别作正式接受/关闭决定。'}]
    r['completed_review_obligations']=['G-FULL-CURRENT-TEXT','G-SHARED-SEMANTICS','G-DOMAIN-HISTORY']
    r['current_findings']='evidence/continuation-semantic-findings.json'
pi['continuation']={'utc':now,'same_actual_thread_and_context':True,'initial_commit_preserved':INITIAL,'new_AI_contexts':0,'new_auth_or_quota_queries':0,'unresolved_content_blockers':[],'verdict_scope':'Only these three mandatory IDs at the exact MI/FI; no ACCEPTED/CLOSED or runtime/global certification.'}
dump(OUT/'per-id.json',pi)
receipt['utc']=now
receipt['continuation']={'initial_commit':INITIAL,'initial_exact_receipt':'evidence/initial-WAIT/review-input-receipt.json','same_reviewer_context':pi['reviewer_thread'],'full_read_coverage':'evidence/continuation-semantic-findings.json','shared_contribution_mapping':'evidence/continuation-shared-contributions.json','read_receipts':'evidence/continuation-read-receipts.jsonl','text_delivery_is_not_semantic_proof':True,'truncation_handling':'audit窄段810–850/985–1045/1170–1215等补读；三共享全文并已核内容，旧截断不当作完整审读。','historical_source_supplement':json.loads((EV/'history-source-recovery.json').read_text())}
receipt['current_text_semantic_read_scope']={'full_current_files':full,'conditional_consumers_and_history_scoped_read':accepted_domains,'old_primary':'specs/demo/WP74 §17–20/§21–23 scoped historical role; unchanged whole bytes verified, no current primary adoption','R6_limits':'final-delivery L1430–1451 incl L06/L07; C17 L01–L14 retained from initial full reading','AGENTS':'full read in initial phase; no applicable repository .agents/skills found','qualification':'All contract-required current full bodies/shared files and named consumer intersections completed; no claim to re-review unrelated source domains or every historical certificate.'}
receipt['unmet_review_obligations']=[]
receipt['completed_review_obligations']={k:'COMPLETED_CURRENT_SCOPED_STATIC_CONTENT' for k in ['G-FULL-CURRENT-TEXT','G-SHARED-SEMANTICS','G-DOMAIN-HISTORY']}
receipt['remaining_root_actions']='Exact result reception, semantic/shared/dependency/historical responsibility registration and separate formal acceptance/closure; no content WAIT inferred.'
receipt['logging_qualification']+=' Continuation plain readers have actual UTC/PID/path/range/bytes/SHA receipts, not invented separated historical stdout/stderr. Full tool I/O remains in platform record. No private model stream is published.'
dump(OUT/'review-input-receipt.json',receipt)

appendix='''

---

# 同一独立审者续审完成记录（当前有效内容结论）

**GR7-M15-001、GR7-M15-002、GR7-M17-001均为PASS_SCOPED_ACTUAL_INTEGRATION。** 本次已补完原WAIT明确列出的三类内容义务；没有发现本批需退回修订的具体反例或缺失输入。上方原报告与`4188ee2bfb8e4b6f3c5ac2c8e8be24384f93d0f4`中的WAIT描述当时未完成的状态，原四份主文件另完整保存在`evidence/initial-WAIT/`，不将其倒写为历史PASS。

审者仍为实际thread/context `01a1403b-12e8-77dc-87ff-20b21d8e302c`，未创建任何辅助agent、子会话或模型调用，未查询认证或额度。有效model/effort/tier/speed仍逐项UNVERIFIED；SOURCE_STATIC、DERIVED_VECTOR和TOOL_VALIDATION分开，全部行为仍NOT_EXECUTED，新增参考/程序/独立完整模型/宿主/Demo/native媒体/真实存档回放均0。

## 实际冻结与完整内容

结论固定MI `e54f54a2cb32e546eabd46aaf53ed45b30a8af89`，workspace tree `b3b6b166b69d2e4dc513cd8d72950b47306191fd`，正式131子树 `e1dfe28acd4f559b22da505238ef3a899aed4542`；FI `b98fa82f8a08b5630ac568cbe8c34f607f623cfb`，tree `eaf9f0831cea151c8a77ad716ad4c8fc5b71dc66`。没有切换到浮动HEAD。新r2 `d7337be83dae5aa7b848cd6a603c2aa7048ffa0c`只是原候选独立依据，本次不继承其PASS。

完整阅读当前audit 1892行、Feature Matrix 592行、DX目录433行、WP73-B 220行、WP74 521行、WP75 460行及WP77 230行；另全文读WP34 233行与WP62 197行。各次实际范围/身份见`evidence/continuation-read-receipts.jsonl`，少数长显示截断后已用窄段补读。范围覆盖工具仅证明文本送达；下述相容性是本审者内容判断。其余先前已接受文件按本批实际相交的派出/形态/记录/资源/取消/保存段及对应向量核语义，不重审无关战斗、储存或小游戏规则。

## 三项结论及向量

| ID | 实际条款 | 独立内容判断 |
| --- | --- | --- |
| GR7-M15-001 | WP73-B §7.3 L140、§7.5 L165；WE-M17 L139 | 合法无自有阴影，通用1/2不同可加载、3首缺，初始登记1/绑定1/标志假；浏览2后BACK为登记1/绑定2/标志假，主菜单仍刷新位置而不重绑。重开尺寸页才按1重载。不浏览、已有true、USE留项/ACTION前进、坐标BACK刷新、首缺/自有阴影/同值确认及总保存门各按独立前态核，均通过有限静态内容核验。 |
| GR7-M15-002 | AN-M09 L168；WP74 §7.1/§17正确条件保留 | 合法A0/A1/A2、旧selected2，缩3→2后未导航才越界。Load可先绑空、释放旧位图再失败；Rename空名失败。Delete Yes恰尾添成3无洞，No仍2。旧0/1的独立正常Load/Rename/Delete保持2，先导航恢复有效。列表BACK保留内存截尾，外层Save/Exit/cache另判。 |
| GR7-M17-001 | WP74 §18 L460–489及范围/未知转引；TOOL-AN01–17 L417–433；T-WP74 L1476–1479；F18-03 L258 | 自行静态解析并读全部15方法、11个EH及跳转目标。先全部解析XML再输出；首参数/无参/缺路径/I/O门、x缺空/整图、负/零/Format/缺值/溢出分流、缺图路径保原槽与存在但加载失败分开。n0=960×192，n6=960×384，槽5=(0,192)，56×68槽0目标(40,28,112,136)，缺0后槽1仍(232,28,112,136)。alpha/非alpha请求、逐项保存、A确存后B失败前缀/finally只请求逐条相符。 |

`per-id.json`保留34项独立向量的完整前提、预期、源定位和理由（9＋8＋17），本次全部标为有限实际静态内容核验通过；执行一律NOT_EXECUTED。实际全文bytes/SHA256/blob、B/候选对照、每个实际条款零基行区间及UTF-8字节半开区间逐项列明，不把共享整文件等同于U10候选整文件。

## 累计共享内容与精确批准

三共享文件共16处累计贡献逐一绑定journal的B片段、批准候选与原独立审查，全部实际片段精确相等，见`evidence/continuation-shared-contributions.json`。audit/matrix的贡献者为U13/U10/U11/U12/U01/U02，DX为U10/U11；其它批次只作贡献保留及本批相容性核验，不给其新语义PASS。

| 贡献者 | 原独立结果 | 当前有限相容性 |
| --- | --- | --- |
| U01 | 2e1b1fb6dd638757436b7292949b3ba0012cafec | 指标缺字段自身默认/整条缺失克隆、后缀及No/Yes保留；不取消阴影资源绑定例外，旧anchor债务不升级。 |
| U02 | 44276c5ae69ef0970a98464a5a9e6ff7eb1c1f1c | 15按钮/6轴词汇与未读注册桥保持，未据此认证编辑器物理输入或尾部刷新；两EOF均先U01后U02。 |
| U11 | 4467147f9f2e184dba6f61d9fb26eb2c781497f9 | T-WP75邻T-WP74、F18-04邻F18-03各归本工具；EXT01–12先于TOOL-AN01–17，同EOF并存不覆盖WE/AN旧行。四目标窗口请求不借图像保存规则。 |
| U12 | 28335c5d8400b6b64e53ad56ee55c572f5a3cc07 | 当前§5.3勘误转引、旧R6原字节/审批状态与作者时点均保持，不据导航更新重签行为。 |
| U13 | 04886b11531bcedb1b5026718480fb25c49ce04a8 | SF2配置声明、原生消费/声音未知分层，未授U10媒体、库或宿主运行资格。 |

上表完整提交值以同目录结构证据中的FI精确绑定为准；生成时另对五份报告全文及逐ID结论核对。root末段只更新wave3当前接收指针/时点，25/27已应用、12/13批，独立实际PASS和正式接受5/27、3/13批，CLOSED0；没有在本次审查前给U10接受。旧作者pending说明是历史时点，原r1辅助披露/WAIT与U03未整合保持。

严格字节重放仍保留原两个未匹配检查：旧`current-navigation-errata.json`整候选hunk与实际三个接收阶段字符串不同，完整差异只有/status、/reception/candidate_review、/reception/shared_integration，当前文件与前一MI 45c80832逐字相同。它是前期receiver注记，行为字段/原定位未变，不属U10新行为或新贡献；不谎称72处纯候选文本全部匹配。27/28文件严格重建、全部U10十三片段匹配；新U07/U10十六片段与原五十六片段保持，U04/U05更早十一片段另由八已接受文件保留校验保护。

## 领域交叉、历史责任与剩余根动作

AN002按B原R6-U07 `/scope_contracts/1`重读：Delete→BACK→Focus写集合B、新单元读画布A、保存/导出读B，普通同对象、取消和重新Load分别保持；这不是AN-M09旧游标前提。AN007按`/scope_contracts/6`和新定向读取固定R的Interpolation核对，源13121字节/SHA256 58c31f761a5f63e0fa526ab8bfe46e209ac2c677bd9700a0c5e161a5e3014341/blob54bebd98e4520b2d7da38ff62ad65f9b08ea2063与旧冻结身份相同。0.3333/0.6666约99.99/199.98、显式N5及B20-D024原向量、一般N端点optional边界保留。

WE-M15–20、B19-C016的确认/坐标/后缀/路径/档案后PBS失败边界；AN-M01/M09–12/M24–33及DXCOMP-C06–08的对象、类型门、批量前缀、缓存/关联边界均相容。图像工具只请求图像产物；WP74 §11的.anm对象类型门、§14.3停用RMXP转换、§15关联、§16保存/cache未改，无自动桥。WP75 §14明确animmaker归WP74，WP77工具入口与Demo事件链分离。R6 L06/L07及C17 L01–L14继续有效，旧H14局部Ruby执行不回填。

先前U04/U05/U09八文件逐字保持之外，已实际核对领域交叉：WP39席位/伙伴与WP41派出/实际替换仍归战斗域，BC26–31/SW30–35的决定/目标补救/前缀未受编辑器预览例外影响；WP34与BR27–31/PF01–09/R4-IF01–06保留按个体动态形态读取可先提交/登记、缺图不回滚和子代同值规则；WP62与WP66-B及PD/R4-PD/R6-PD对照保留出场包装/全局形态提交的门和接收者、完整单条编号、普通图像刷新不写记录与多项Forms首轮另写false/BACK保留。U10按显式物种/形态编辑指标与generic shadow绑定，不把这些独立消费者归成统一刷新或取消事务。原两组独立实际报告与精确接受决定的责任边界已读；这只是本批交叉相容性，不重签旧五ID或56/92。

本审者已完成三ID内容、共享保留/相容性及具名静态历史回归。原record-to-record直接/传递排程边为空不表示全局依赖满足。**仍需R7-I接收本新结果的精确commit/tree，并登记WP73-B/WE、WP74/AN/TOOL-AN、T-WP74/F18-03以及WP75/WP77/图像消费者的语义owner、共享receiver、直接/传递/领域及历史责任，再分别作ACCEPTED/CLOSED决定。**这些是根的后续动作，不再把本审者已完成的内容判断记为WAIT。无缺失输入或未完成内容义务；运行未知只限制结论范围，不阻塞本次静态PASS。7 optional、2导航facet、1 no-required、2policy未采用，27项/13批、旧56/92不变。

成果仅在唯一原分支`codex/r7-ir-u10-20261015-r1`追加证据；保留4188ee2为普通祖先，不force，不改候选/正式正文/公共台账/main/tag。最终提交及全部文件完整远端bytes/SHA256/blob回读在包外以真实commit/tree绑定，manifest不制造递归自哈希。
'''
# Use the actual frozen bindings rather than transcribing IDs by memory.
for batch,stub in [('R7-U11','4467147f9f2e184dba6f61d9fb26eb2c781497f9'),('R7-U13','04886b11531bcedb1b5026718480fb25c49ce04a8')]:
    appendix=appendix.replace(stub,bindings[batch]['candidate_review_commit'])
lead='当前续审结论：三项均为 **PASS_SCOPED_ACTUAL_INTEGRATION**。下方首段是4188ee2的历史WAIT原报告；续审完成依据与当前责任边界见文末，逐项当前结果见per-id.json。\n\n'
(OUT/'report.md').write_bytes(lead.encode()+(archive/'report.md').read_bytes()+appendix.encode())
shutil.copyfile(Path(__file__),EV/'build-continuation.py')
dump(EV/'continuation-validation.json',{'utc':utc(),'pid':os.getpid(),'classification':'TOOL_VALIDATION_ONLY','initial_commit':INITIAL,'full_current_text_delivery_files':len(coverage),'shared_contributions_checked':len(shared_map),'shared_hunk_identity_failures':0,'history_supplement_matches_B_frozen_R_identity':True,'vector_counts':{r['id']:len(r['vectors']) for r in pi['records']},'new_review_findings_are_human_readable_static_judgment_not_derived_from_exit0':True,'errors':[]})
manifest=json.loads((archive/'artifact-manifest.json').read_text())
manifest['schema']='r7.u10.continued-review-artifact-manifest.v1'
manifest['continuation_parent']=INITIAL
manifest['files']=[{'path':p.relative_to(REPO).as_posix(),**ident(p.read_bytes())} for p in sorted(OUT.rglob('*')) if p.is_file() and p!=OUT/'artifact-manifest.json']
manifest['self_binding']='Manifest itself is bound by the final actual commit/tree and complete remote response body; no recursive self hash.'
manifest['qualification']='Current three-ID static content PASS; prior WAIT and strict journal exception preserved. Not ACCEPTED/CLOSED/runtime/global certification.'
dump(OUT/'artifact-manifest.json',manifest)
print(json.dumps({'utc':utc(),'pid':os.getpid(),'full_read_files':len(coverage),'shared_hunks':len(shared_map),'files':len(manifest['files'])+1,'verdicts':{r['id']:r['verdict'] for r in pi['records']}},ensure_ascii=False))
