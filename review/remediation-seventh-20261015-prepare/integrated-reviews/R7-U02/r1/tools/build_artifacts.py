import datetime, hashlib, json, re, shutil, subprocess
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
BASE=Path('/workspace/r7-ir-R7-U02')
INPUT=BASE/'actual-input'
B='e646432c644dec04d306842cc5a559a29c718fbc'
MI='45c80832a41c1b56dcd7e9d93497758cbb7721de'
FI='13d76ba61838b13925ba9d41f58a6b047564d926'
P='review/remediation-seventh-20261015-prepare/'
ME='01a1401b-eec4-72eb-800e-6ff904adc009'
VERDICT='PASS_SCOPED_ACTUAL_INTEGRATION'
WP='deliverables/final-specification-set/user-interface/wp17-messages-windows-input.md'
CAT='deliverables/final-specification-set/test-catalog/user-interface-wp17-63-65-66-67-68-69-70-71.md'
def ident(d):return dict(bytes=len(d),sha256=hashlib.sha256(d).hexdigest(),git_blob=hashlib.sha1(f'blob {len(d)}\0'.encode()+d).hexdigest())
def write(name,obj): (ROOT/name).write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n')
def git(*a):return subprocess.check_output(['git',*a])
def clause(path,start,end):
 d=(INPUT/'actual'/path).read_bytes();s=b''.join(d.splitlines(keepends=True)[start-1:end]);return dict(commit=MI,path=path,whole_file_identity=ident(d),lines_inclusive=[start,end],clause_identity_including_LF=ident(s))
def origin(path):
 d=path.read_bytes();return dict(local_path=str(path),**ident(d))
contract=json.loads((BASE/'original/dispatch/delegation/contracts/R7-U02.json').read_bytes())
author=json.loads((INPUT/'candidate/candidates/R7-U02/evidence/author/per-id.json').read_bytes())
normalized=json.loads((BASE/'original/evidence/tasks/R7-C13/inputs/tasks/R7-P02/normalized-record-candidates.json').read_bytes())
limits=json.loads((BASE/'original/evidence/tasks/R7-C17/limits-and-alias-reception.json').read_bytes())
scope=json.loads((ROOT/'scope-validation.json').read_bytes())
assert len(scope['clause_checks'])==56
journal=json.loads((INPUT/'integration/applied-clauses.json').read_bytes())
wp_lines=(INPUT/'actual'/WP).read_text().splitlines()
cat_lines=(INPUT/'actual'/CAT).read_text().splitlines()
rows={}
for n,line in enumerate(cat_lines,1):
 m=re.match(r'\| (R7-U02-(SS|IN|DB|BT|AX)\d\d) \| (.*) \|$',line)
 if m: rows[m[1]]=dict(line=n,cells=m[3].split(' | '),actual_line_identity=ident((line+'\n').encode()))
assert len(rows)==51
ss_reasons=[
'Utilities L613–623在命名之后检查相对目录；目录已存在则跳过mkdir，主截图正常返回才进入资源条件。没有读取宿主数据目录B。',
'相对目录检查假进入mkdir，随后构造主文件名及截图；三个请求按源顺序，不据正常返回证明文件或像素。',
'截图后的pbResolveAudioFile条件是假则跳过SE调用；该条件不改变已经选择的主截图路径。',
'目录查询或mkdir均位于begin内；捕获后只使用预先形成的同一filename，经pbGetSaveFileName进行一次截图。',
'主截图也位于同一保护区；捕获后进入一次同名fallback。源未撤销主请求可能已经产生的外部前缀。',
'rescue体内文件名解析异常没有被该begin再次捕获；后继fallback截图和完成音均未到。',
'rescue体内截图异常传播；无回跳或第二个fallback。没有恢复已建立目录或外部截图的步骤。',
'墙钟读取与sprintf都位于begin前，二者失败未进入该保护；不能据主阶段捕获推出fallback。',
'名称仅由给定墙钟字段/毫秒形成；没有独立序号或存在性去重，故两次同毫秒允许同名。覆盖与原子性未证明。',
'Input L17–20先执行旧宿主刷新再查F8 trigger；未触发则不调用截图助手。助手无确认/取消交互。',
'完成音的资源检查及SE调用在整个捕获保护之后；任何后项错误不能倒转先前已到截图请求。',
'有限rescue不等于捕获所有退出/重启信号；当前条款明确只限可捕获族，不把它们归一为普通失败。']
in_reasons=[
'ItemStorage L200–216循环先Graphics/Input、yield，再不忙时USE退出，恢复可见后方法结束；无局部额外Input.update。Bag更新块仅更新sprites。',
'同一显示循环只以USE/brief处理不忙出口；BACK不在该出口条件，brief也仍受busy守卫，四态保持。',
'共享确认L240–274的BACK置false，USE取当前选项；释放命令窗、恢复可见后返回，没有同一尾部刷新。',
'Party L535–587与Summary L217–265分别读到各自循环及正常返回；局部没有通用尾部，using的ensure只处置窗口而不自动轮询输入。',
'Messages L655及包装L699有显式刷新；包装嵌套可造成多次，不能据一条静态预期限定总次数或其它专用入口。',
'普通选项L721–755：USE取索引；BACK在取消编码非0时退出；dispose后L753明确Input.update，nil早退独立。',
'带帮助选项L757–801只在commands存在时构建/循环并于L797刷新；保留help更新、取消编码和缺commands分支。',
'自由文本L821–848：RETURN接编辑文本，ESCAPE保原文；循环后关闭文字输入、释放窗口、L847刷新。异常不借正常尾部保证。',
'共享静态帮助ItemStorage L219–238恢复可见后明确Input.update；共享前缀不决定是否有尾部，此反向对照保留。',
'普通选项commands=nil在首门返回0；带帮助commands缺值不进循环，[]仍为真值、会建窗。MG14及四态按其原前提。',
'重新核UI旧MG/B04/U06表与SpriteWindow显示/暂停/等待/resume；不忙正常出口不能覆盖三行自动暂停，业务前缀分别保持。',
'传入块和组件调用先于正常后段，抛错会跳过后继；可见性、dispose和输入开关各自观察，不造统一ensure/业务回滚。',
'Interpreter update局部loop_count在每轮前加1，>100先Graphics.update后归0；终止返回true后还有空列表轮。98/99/100注释得0/终止后1/终止前1；116让出、消息等待与深度>100独立。']
db_reasons=[
'实际DB-0087字节中三字段顺序已独立确认。完整15+6目标指针无misc1；未知分支0x1403b278e请求错误后返回，外层0x1403b2a70/2a79不检查该返回且继续。a:b0成功分配到追加，后继rightshoulder:b5可到达。',
'已识别分配失败路径0x1403b2979会清绑定计数，区别未知目标分支；因此保留前项只对本未知字段路径，不形成所有失败定理。',
'有界字段解析代码没有交互取消请求；逻辑Input::BACK的查询和消费由其它入口定义，不能撤回字段。',
'mkxp L31–47明确bindingNames用于显示，Input L1–31是逻辑别名/宿主查询层；未读CC04桥不能补出原生a到ACTION/USE的等价。',
'全文件hash及既有1923/731结构计数只证身份/结构；本次只读具名字段、21表项及有界解析控制流，没有全字段或优先级语义资格。']
reasons={f'R7-U02-SS{i+1:02}':r for i,r in enumerate(ss_reasons)}
reasons.update({f'R7-U02-IN{i+1:02}':r for i,r in enumerate(in_reasons)})
reasons.update({f'R7-U02-DB{i+1:02}':r for i,r in enumerate(db_reasons)})
binary=json.loads((ROOT/'binary-validation.json').read_bytes())
for kind,table in zip(['BT','AX'],binary['tables']):
 for i,r in enumerate(table,1):
  reasons[f'R7-U02-{kind}{i:02}']=f"逐指针独立追读VA {r['va']} 的NUL结尾名称为 {r['name']}，范围{r['bytes_half_open']}；有界两表扫描及普通{'b0' if kind=='BT' else 'a0'}源解析可到追加路径，仍需已选解析器、成功前序、正常源及分配。名称可识别不证明设备/逻辑查询。"
common={
'GR7-M04-301':'默认输入更新无覆写，宿主输入刷新正常；除独立变化外F8沿真；墙钟2026-10-15 12:34:56.007；A≠B；辅助/资源解析/外部请求按各例正常返回，文件名[2026-10-15] 12_34_56.007.png；资源存在判据独立，返回不等于捕获成功。',
'GR7-M06-002':'默认入口、有效组件，无插件/外层或回调额外刷新；所列逻辑查询为夹具，其余假；正常依赖/恢复/释放返回。共享短文本A、brief=false、无中间暂停、循环更新后不忙；各变化独立。仅统计局部显式请求，不证明宿主内部行为。',
'GR7-D06-001':'DB-0087已通过先前接收阶段，被审随附字段解析器实际被选并物化该记录，普通源与分配正常；未真实加载或接入设备。BT15逐名普通b0，AX6逐名普通a0，均继承相同前提；不证明物理或游戏逻辑输入。'}
clauses={
'GR7-M04-301':[clause(WP,163,173)],
'GR7-M06-002':[clause(WP,167,167),clause(WP,281,285)],
'GR7-D06-001':[clause(WP,175,184),clause('audit/source-traceability.md',1864,1884),clause('planning/feature-matrix.md',582,588)]}
conclusions={
'GR7-M04-301':'实际WP17与SS01–12完整表达工作目录主路径、墙钟名称、必要目录及一次同名fallback。命名前失败、主保护可捕获族、fallback失败传播和正常截图后条件音效正确分层；帮助文案不构成保存目录实测，未承诺唯一或回滚。',
'GR7-M06-002':'实际两处全称已改为按入口区分。共享普通/确认和Party/Summary局部正常返回无统一尾部；普通/带帮助选项、自由文本、通用消息及共享静态帮助的明确正常尾部保持。nil/缺commands与[]、四态和异常前缀未混同，正确GR6-O-002图形链保持。',
'GR7-D06-001':'实际资料/目录/追踪/矩阵仅接收有限21目标名和DB-0087未知字段继续。选中解析器/已成功前序/正常分配条件完整；未知分支与分配失败不同，不接物理输入、注册优先级、全1923字段或76/48语义。'}
phases={
'GR7-M04-301':dict(normal='A/Screenshots/N，必要mkdir，正常截图后条件SE；无B请求的主路径对照。',cancel='助手无交互取消；无F8沿是未触发。',failure='保护前命名失败、主阶段可捕获错误、rescue体再错及非捕获信号分别处理。',partial='目录/外部截图已到前缀保留；SE失败不撤销，真实文件成功未观察。'),
'GR7-M06-002':dict(normal='各入口循环内刷新和正常尾部分别追读；共享短文本USE/brief不是忙暂停反例。',cancel='共享确认BACK为No且无统一尾部；普通选项可取消BACK有尾部；自由文本ESCAPE原文。',failure='回调/组件失败可跳过正常恢复、释放、文字输入关闭和尾部刷新；不认证宿主恢复。',partial='可见恢复/释放与刷新独立，UI返回不等于领域事务撤回；旧Bag/PC业务前缀保持。'),
'GR7-D06-001':dict(normal='a:b0及21目标的普通识别；后继rightshoulder:b5在同记录继续。',cancel='数据字段无交互取消，BACK属逻辑消费者。',failure='misc1错误请求/无追加；allocation失败另可清计数；消息显示/硬件失败未证明。',partial='未知字段不撤早前成功追加；不由外层继续推注册、全局回滚或所有失败保留。')}
history={
'GR7-M04-301':dict(result='本次原合同/原M04提案及C04-SS-A–E新读，与MI帮助/截图条款相容；与紧急保存提示GR7-M04-001不同根因。',remaining='全历史去重/别名接收仍由R7-I；无全项目不存在重复的认证。'),
'GR7-M06-002':dict(result='B独立O-002原13行、完整ledger该记录、MI WP13全文/R6-EV01–06及固定R解释器重新核对，正确101轮图形防冻链保留；旧MG02/03/04/14/27、B04-M14、U06-M10-001-A–E全文条件与busy组件相容。',canonical_candidate=None,remaining='不把原null改成无历史根或新ID；全局去重/旧关闭回签均未作。'),
'GR7-D06-001':dict(result='正确WP17宿主未证和WP65/help范围保留；晚到D06前提仅缩窄，TV01接入DB01，TV02–05宽平台/空字段/重叠/priority未采用，TV06仅保原逻辑消费者。',remaining='CC04 NOT_READ；全1923字段/76字段48记录/priority NOT_SIGNED；全历史去重仍R7-I。')}
records=[]
for a in author['records']:
 rid=a['record_id'];kind='SS' if rid=='GR7-M04-301' else 'IN' if rid=='GR7-M06-002' else 'D'
 selected=[v for v in a['candidate_vectors']]
 vectors=[]
 for old in selected:
  v=rows[old['id']];assert v['cells']==old['catalog_cells']
  vectors.append(dict(id=old['id'],actual_MI=MI,actual_catalog=CAT,actual_line=v['line'],actual_line_identity=v['actual_line_identity'],common_premises=common[rid],actual_input_and_expected_cells=v['cells'],independent_static_reason=reasons[old['id']],documentary_assessment='SUPPORTED_IN_ACTUAL_SCOPED_CONTENT',evidence='SOURCE_STATIC / DERIVED_VECTOR',execution='NOT_EXECUTED',host_result='NOT_OBSERVED'))
 n=next(x for x in normalized['records'] if x['id']==rid)
 records.append(dict(id=rid,verdict=VERDICT,reviewer_thread=ME,MI=MI,MI_tree='6480ffe3df49bd9776c719f3c9be1c13618fdb0a',MI_formal_subtree='8403869aaeb4726518414b409b3808c3c0780e65',FI=FI,actual_clauses=clauses[rid],independent_conclusion=conclusions[rid],original_seven_group_input=dict(commit='f622356f3beb9e84ea8cff9db07c7fb382565d3f',path=P+'delegation/contracts/R7-U02.json',record_id=rid,all_seven_groups_actually_read=True,raw_binding_checks='bindings-and-links.json'),original_vector_mapping=a['original_to_candidate_vector_mapping'],vectors=vectors,normal_cancel_failure_partial=phases[rid],received_counterproof_and_current_resolution=dict(original_reader=a['received_counterproof']['reviewer'],strongest_counterargument=a['received_counterproof']['attempted_refutation'],current_resolution=conclusions[rid],candidate_PASS_not_inherited=True),correct_preservation_and_history=history[rid],original_direct_transitive_dependencies=n['groups']['dependencies'],domain_reception=dict(direct='固定源调用者→助手/局部入口→实际WP17/目录，必要WP65/help及MI领域消费者均新读，有界相容。',transitive='数据目录/音效解析、窗口busy/resume、默认输入包装及解释器101轮链按具名源范围新读；更宽宿主/设备/资源链无自动放行。',receiver='R7-I remains sole formal receiver; this report supplies scoped semantic/shared/history evidence only'),shared_reception='shared-reception.json',remaining_gates=['R7-I实际接收本报告，登记本三项语义责任及CG01/CG06/CG07共享责任','R7-I按精确直接/传递消费者和具名历史回归逐项登记接收；全局去重未认证','其它必修/批次的独立实际门及整体依赖仍各自待满足','ACCEPTED与CLOSED由R7-I按合同分开决定'],runtime_qualification='NOT_EXECUTED; L01–L14 retained; effective model/effort/tier/speed UNVERIFIED',ACCEPTED=False,CLOSED=False))
write('per-id.json',dict(schema='r7.u02.independent.actual-review.v1',reviewer_thread=ME,records=records,scope_only_three_ids=True,all_51_vectors_NOT_EXECUTED=True,other_required_new_semantic_PASS=False))
shared=[]
for f in journal['files']:
 if f['path'] in ['audit/source-traceability.md','planning/feature-matrix.md',CAT,'deliverables/final-specification-set/test-catalog/engine-overworld-wp11-15-59-60.md','deliverables/final-specification-set/test-catalog/demo-dx-wp72-73-74-75-76-77.md']:
  for h in f['hunks']:
   binding=next(x for x in journal['source_bindings'] if x['id']==h['batch_id'])
   shared.append(dict(path=f['path'],batch=h['batch_id'],candidate_commit=binding['candidate_commit'],candidate_review_commit=binding['candidate_review_commit'],candidate_review_tree=binding['candidate_review_tree'],base_indices_half_open=h['base_line_indices_half_open'],actual_indices_half_open=h['actual_final_line_indices_half_open'],added_identity=h['added_identity'],assessment='EXACT_CLAUSE_PRESERVED_AND_COMPATIBLE_WITH_U02_SCOPE',receiver='R7-I',fresh_other_ID_semantic_PASS=False,qualification='审批报告全文及相关per-ID共享/范围字段已读；原candidate PASS/配置/NOT_EXECUTED资格保留。本次不重新批准其它ID。'))
write('shared-reception.json',dict(schema='r7.u02.shared-impact.v1',MI=MI,checks=shared,same_boundary_insertions=journal['same_boundary_insertions'],root_adjustments=journal['root_administrative_reception_adjustments'],semantic_findings=['两共同EOF均按U01→U02接入，文本完整，未整文件覆盖；原时点候选标签由当前指针限定。','engine中U13 S01与U01 J01索引分别保留、旧R6-EV不变；新R7-U03/U10未接入，旧同名U10历史不混同。','UI中U08仅K35后四HP行及其其它批准改动，U02所有51行保持；正常HP显示与输入/截图条款无冲突。','audit中U13有限音色库、U11有限extendtext、U12旧Debug导航勘误、U01和U02追加分别接收；matrix各行及EOF追加保留。','DX只核U11批准新段及B前缀/整文件身份，未对整份DX历史重新语义认证；无U01条件写入或新U10贡献。','errata根调整仅status/reception，无行为或旧R6payload改变；两当前入口链接在固定MI解析，候选证据须按public-reception固定commit读取。'],prior_five_exact=scope['prior_accepted_five'],prior_domain_consumers='WP39、WP41、WP34及三领域目录全文新读，只判U02相容/历史资格保持，不转授旧PASS。',formal_receiver_status='PENDING_R7_I_EXPLICIT_RECEIPT',no_ACCEPTED_or_CLOSED=True))
# Copy authentic original restoration receipts; never reconstruct prior command timing.
for name,folder in [('restore-original.json','original'),('restore-actual.json','actual-input')]:
 files=list((BASE/folder).glob('recovery-receipt-*.json'));assert len(files)==1;shutil.copyfile(files[0],ROOT/name)
plans=[];inputs=[]
for pn,dn in [('original-plans','original'),('actual-plans','actual-input')]:
 planpath=BASE/pn/'R7-U02.json';plan=json.loads(planpath.read_bytes());plans.append(origin(planpath))
 for group in ['artifacts','evidence','fixed_read_inputs']:
  for row in plan[group]:inputs.append(dict(plan=pn,group=group,**row,restored_identity=ident((BASE/dn/row['local_path']).read_bytes())))
actual_read=[]
for p in sorted((INPUT/'actual').rglob('*.md')):
 rel=str(p.relative_to(INPUT/'actual'));actual_read.append(dict(path=rel,commit=MI,**ident(p.read_bytes()),full_text_actually_read=True,total_lines=len(p.read_text().splitlines()),reading_evidence='平台完整分段输出；部分有read-delivery.jsonl，早期直接cat无独立逐命令日志；截断区间已另读补齐。',semantic_scope='U02 exact content/consumer compatibility and preservation only; other IDs not freshly approved'))
source_ranges={
'Data/Scripts/001_Technical/004_Input.rb':[[1,31]],
'Data/Scripts/019_Utilities/001_Utilities.rb':[[600,630]],
'Data/Scripts/001_Technical/002_Files/001_FileTests.rb':[[1,60],[230,275]],
'Data/Scripts/008_Audio/002_Audio_Play.rb':[[190,233]],
'Data/Scripts/016_UI/018_UI_ItemStorage.rb':[[60,75],[110,132],[198,274],[341,376]],
'Data/Scripts/016_UI/007_UI_Bag.rb':[[125,145],[242,256]],
'Data/Scripts/016_UI/005_UI_Party.rb':[[525,590]],
'Data/Scripts/016_UI/006_UI_Summary.rb':[[210,292]],
'Data/Scripts/007_Objects and windows/002_MessageConfig.rb':[[480,512]],
'Data/Scripts/007_Objects and windows/011_Messages.rb':[[160,210],[397,605],[621,801],[821,848]],
'mkxp.json':[[1,159]],
'Data/Scripts/003_Game processing/003_Interpreter.rb':[[1,38],[78,150]],
'Data/Scripts/003_Game processing/004_Interpreter_Commands.rb':[[1,45],[110,137],[500,513]],
'Data/Scripts/007_Objects and windows/005_SpriteWindow_text.rb':[[300,445],[526,735],[855,935],[1056,1280]],
'Data/Scripts/016_UI/022_UI_MoveRelearner.rb':[[1,28]],
'Data/Scripts/016_UI/023_UI_PurifyChamber.rb':[[1060,1078],[1148,1172]],
'Data/Scripts/018_Alternate battle modes/001_Battle Frontier/005_UI_BattleSwap.rb':[[65,89],[155,157]]}
sources=[]
for rel,ranges in source_ranges.items():
 path=BASE/'original/inputs/reference'/rel
 if not path.exists():path=BASE/'supplemental'/rel
 sources.append(dict(repository='Maruno17/pokemon-essentials',commit='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b',path=rel,**ident(path.read_bytes()),actually_read_lines_inclusive=ranges,unread_complement='All other lines not asserted freshly read; bounded snapshots are not complete reference checkout',execution='NOT_EXECUTED'))
write('review-input-receipt.json',dict(schema='r7.u02.actual-input-receipt.v1',generated_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),actual_thread_id=ME,actual_session_id=ME,additional_opaque_task_context='NOT_EXPOSED',parent_source_thread='01a13f49-a154-7054-9b04-ce31f924d01c',identity_source='CODEX_THREAD_ID/CODEX_SESSION_ID whitelist values actually read; not PID or /root role inference',excluded_id_comparison='Distinct from all 19 dispatch exclusions; no child/auxiliary agent/model call created',configuration=dict(requested='gpt-6.1-sol / ultra / service_tier default / normal speed / no Fast',effective_model='UNVERIFIED',effective_effort='UNVERIFIED',effective_tier='UNVERIFIED',effective_speed='UNVERIFIED',credential_or_quota_checks=False),dispatch=dict(commit='c64774c60d91e522cb515ef71e3e9d4ea6b4712c',path=P+'integration/wave2/v1/dispatch/R7-U02-R7IR.md',full_read_before_work=True),fixed=dict(B=B,B_formal_subtree='ebbe29f2bc88cd17de7072bf440c6fa8c8c7089c',MI=MI,MI_tree='6480ffe3df49bd9776c719f3c9be1c13618fdb0a',MI_formal_subtree='8403869aaeb4726518414b409b3808c3c0780e65',FI=FI,FI_tree='6747a584b91c86acd4771c1a6dee93260602106f',R='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b',R_tree='7589c800b61ba13a13040ed0d686979b80a84fd0',reference_tree_recertified=False),restoration=dict(fixed_tool_commit='658488c81f1f3181a488298ab27850c8af951d73',tool_identity=origin(BASE/'bootstrap/restore_container_context.py'),plans=plans,original=dict(files=33,bytes=21406782,receipt='restore-original.json'),actual=dict(files=186,bytes=7112903,receipt='restore-actual.json'),shared_directory_assumed=False,resume_needed=False),all_restored_inputs=inputs,mandatory_actual_full_read=actual_read,fresh_bounded_reference_read=sources,native_read='binary-validation.json; full bounded disassembly read in platform, body remains scratch; PE not executed',original_seven_groups=dict(identity=origin(BASE/'original/dispatch/delegation/contracts/R7-U02.json'),all_three_full_seven_groups_read=True,raw_C04_records=[2,5],raw_C08_challenges=[3],raw_original_proposals=[5,8,28],normalized_verification_dependencies=[5,8,28],late_D06='original late-author-payload-receptions record 2 full original and reception read; narrows only',own_18_binding_check='bindings-and-links.json'),evidence_read_qualification='Author report, own independent candidate report/per-ID/read ledger, root eligibility, five shared candidate reports and relevant per-ID scope/shared/qualification fields read. Remaining restored author tooling/identity evidence mechanically rebound; not every metadata field claimed semantically re-reviewed.',AGENTS='Actual full297 lines read; no tracked .agents in B/dispatch/MI; project .agents/skills absent and workspace .agents empty; no relevant local skill applied',history='B independent-O-002 entire13 lines and exact complete ledger record new read; prior IR report and three decision records read; prior per-ID identity only, no old PASS borrowed',limits=limits['limits'],old_56_92='Original exact qualified closure preserved; no reopening or fresh whole-ID attestation',denominators=dict(required_items=27,batches=13,current_integrated_items=18,current_integrated_batches=8,optional7='NOT_ADOPTED',navigation_facets2='NOT_ADOPTED',no_required1='NOT_ADOPTED',policy2='NOT_ADOPTED'),execution=dict(all_vectors='NOT_EXECUTED',REFERENCE_OBSERVATION=0,reference_program=0,independent_complete_model=0,host=0,Demo=0,native_media=0,real_save_replay=0,historical_Ruby_local='Existing 1 process/10 inputs qualification retained; not credited to this task'),logging_limits='Early reconnaissance/fetch/bootstrap/reads have real platform I/O; native restore receipts preserve HTTP/UTC. No independent per-command PID/UTC/streams for all early actions, never retrofilled. From logs/001 onward only wrapped commands have separate true PID/UTC/exit/streams; interactive reads remain platform I/O. Read-delivery records text output delivery, not semantic PASS.',tool_failures='005/006 candidate Git lookup failed because fixed unrelated candidate objects were not in local ancestry; corrected with verified restored files and fixed-commit raw HTTP, no branch substitution. 007 asserted candidate errata slice before root status/reception adjustment; corrected separate administrative JSON delta; 008 all56/24/3 passed. Original logs retained. One mistyped author-report path and freeze display path failed in platform-only reads; corrected exact files. No failure erased or promoted to behavior evidence.',write_scope=P+'integrated-reviews/R7-U02/r1/',output_branch='codex/r7-ir-u02-20261015-r1',formal_baseline_on_output_branch=B,ACCEPTED=False,CLOSED=False))
print(json.dumps(dict(records=len(records),vectors=sum(len(r['vectors']) for r in records),mandatory_full_files=len(actual_read),shared_clauses=len(shared),restored_members=len(inputs)),ensure_ascii=False))
