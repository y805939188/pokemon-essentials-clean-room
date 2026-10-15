import datetime,hashlib,json,pathlib,shutil,subprocess
R=pathlib.Path('/workspace/r7-ir-R7-U01');C=R/'checkout';PREFIX='review/remediation-seventh-20261015-prepare/integrated-reviews/R7-U01/r1';D=C/PREFIX
MI='45c80832a41c1b56dcd7e9d93497758cbb7721de';FI='13d76ba61838b13925ba9d41f58a6b047564d926';B='e646432c644dec04d306842cc5a559a29c718fbc'
def ident(b):return {'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'git_blob':hashlib.sha1(f'blob {len(b)}\0'.encode()+b).hexdigest()}
def write(p,x):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def copy(p,q):q.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(p,q)
identity=json.loads((R/'tool-evidence/identity-observation.json').read_text())
audit=json.loads((R/'tool-evidence/mechanical-audit.json').read_text());supp=json.loads((R/'tool-evidence/supplemental-audit.json').read_text());journal=json.loads((R/'actual-input/integration/applied-clauses.json').read_text())
rows=[json.loads(x) for x in (R/'tool-evidence/read-io.jsonl').read_text().splitlines()]
actual=[]
for p in sorted((R/'actual-input/actual').rglob('*')):
 if not p.is_file():continue
 rel=str(p.relative_to(R/'actual-input/actual'));b=p.read_bytes();n=len(b.decode().splitlines());spans=[(x['start_line'],x['end_line']) for x in rows if x['path']==str(p)]
 covered=set(i for a,z in spans for i in range(a,z+1));assert set(range(1,n+1))<=covered,(rel,n,spans)
 actual.append({'path':rel,'commit':MI,**ident(b),'lines':n,'semantic_read':'FULL_ACTUAL_DOCUMENT; scoped conclusions only','printed_ranges':spans})
assert len(actual)==16
formal='deliverables/final-specification-set/'
wp03=formal+'generic-kernel/wp03-content-identity-and-schema.md';wp04=formal+'generic-kernel/wp04-pbs-lifecycle.md';generic=formal+'test-catalog/generic-kernel-wp02-03-04.md';engine=formal+'test-catalog/engine-overworld-wp11-15-59-60.md'
facts={x['path']:x for x in actual}
def clause(path,a,z):
 b=(R/'actual-input/actual'/path).read_bytes();span=b''.join(b.splitlines(keepends=True)[a-1:z]);return {'path':path,'commit':MI,'lines_inclusive':[a,z],'file_identity':{k:facts[path][k] for k in ['bytes','sha256','git_blob']},'span_identity':ident(span)}
common={'reference':'8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b','baseline':B,'no_schema_query_equality_overrides':True,'independent_reset_per_subcase':True,'legal_registered_inputs_and_normal_prior_steps':'Required unless the individual negative/failure fixture explicitly changes them','behavior_execution':'NOT_EXECUTED'}
premises=[
 '合法TownMap主身份1已登记，无另加数值序号；直接查找及比较。',
 '同类两个合法TownMap主身份均1；无比较覆写。',
 '合法Grass双身份记录具有序号2；合法EXPSHARE记录；无比较覆写。',
 '可读DungeonParameters输入；仅[cave]或独立[cave,]；尺寸6×4，其余合法省略；正常终检/I/O只在声明保存时要求。',
 '[cave]5×4及[cave,1]6×4合法且共存；分别查询1、2。',
 '仅合法[cave_1]6×4；不附加[cave,1]，记录元数据与查询输入分开。',
 '同一输入两节其它属性合法；cave_1→cave,1及逆序独立复位；观察第二节拒绝点。',
 '合法[cave]5×4与[cave_0]6×4同时存在，无显式次位；查询cave/0。',
 '三类输入分别复位并显式次位0；未知Species另作独立拒绝对照；不能要求这些拒绝例成功转换。',
 'Species已登记RATTATA和RATTATA_1；Metrics仅[RATTATA_1]背面7,8；查询RATTATA/1及0。',
 '同V07物种门；Shadow输入明确存在且启用，仅[RATTATA_1]且GaugeSize5000；合法个体形态1。',
 'Metrics与启用Shadow分别复位；两合法首分量预登记；两种节头顺序分别观察第二节。',
 'Species首分量预登记；Metrics/启用Shadow省略或空次位与正1对照，基础及正1可同时存在。',
 '新整数Tileset7、23各至少一个合法Autotile与Tile；重复7另复位；缺组作为独立构造拒绝例。',
 'PBS编译无交互；独立正常指标编辑会话具有已确认变动，No重载正常；Yes档案成功、后PBS失败单列。',
 'V04或V09的直接与启动入口独立；先前类保存正常；删除/诊断I/O各按具名阶段到达，Reset/SystemExit另列。',
 '固定R，无覆写；Species RATTATA存在，Shadow启用；仅合法[RATTATA]省略GaugeSize且无RATTATA_0；合法形态0个体。',
 '同DEFAULT-01，仅显式GaugeSize4000；合法正整数，不改记录存在性。',
 '同DEFAULT-01，仅显式GaugeSize5000；别名5000向量仍另行保留。',
 'Shadow启用，合法RATTATA/形态0；RATTATA_0及RATTATA均无命中，无额外查询覆写。'
]
reasons=[
 '整数键查找使用主身份；实例对整数比较使用另一数值序号，纯整数类不因此命中。假是正常结果，没有领域写入。',
 '同类比较读主身份而非另一序号，所以同1为真。五类声明和构造均已全文读；Metadata默认0、PlayerMetadata回1、DungeonTileset非空回首条只改变查询。',
 'TerrainTag确有另一序号；Item为符号身份并继承符号/字符串比较。经验分享消费者用符号，不能把纯整数反例扩大为普通游戏故障。',
 '可选正整数位省略或空时先得到缺值，再归为语义0；合法输入可登记/查询6×4。后续终检、保存与生成成功各有自己的前提。',
 '基础身份和正版本身份不同；先查指定版本，未命中版本2再查基础，故6×4及5×4分别成立。',
 '外部cave_1/0及cave/1可指向同一登记身份；查询因此命中已有6×4，但记录自身仍cave_1/0；未执行生成器。',
 '地牢专用重复校验先于通用登记探测；第二节当时的区域/版本分别用于诊断。首条已登记，第二条、终检及本表save未到，不承诺回滚。',
 '零版本查询仍先试cave_0身份，命中6×4；可共存的基础cave没有被删除，也不是无条件优先。',
 '非空可选次位走正整数转换，0在身份归一前拒绝；Species枚举另先确认首分量。省略/空位0属于另一个合法路径。',
 '正形态查询先试RATTATA_1，已有别名命中故不新克隆；0不走该正形态门。缺基础时可创建基础、正形态真正缺席才克隆五组，后缀空等旧规则保持。',
 'Shadow对所有整数先试指定身份，然后基础；已命中记录时最大量表读取其字段5000。本例不证明默认Shadow启用或实际显示。',
 '两类在转换后通用存在性探测拒绝第二节；反序也碰撞，首条自身species/form元数据由实际先条决定。没有本表终检或保存，也不扩成直接register统一拒绝。',
 '省略/空0及正形态均在接受域；正数位只要求正整数，并未再检查基础物种是否登记同号形态；两个不同登记身份不互拒。',
 '单整数身份不采用复合节头规则；两整组齐全才抵达正常登记/重复门。缺组先在构造时失败，缺用途映射返回0又属成功构造后的查询。',
 '指标关闭链No正常加载档案；Yes先档案save再PBS，PBS失败没有撤销先存档案的步骤。编译不借用该编辑器取消语义；现有布局也不自动重定位。',
 '直接入口中首条内存及其它类已存档案可保留，本表旧dat未必被触碰；启动检查的预删及诊断后删除仅为尝试，不能保证全盘删除。退出/重启信号原样重抛。',
 '存在基础记录且省略字段时构造默认4000；消费者读取存在记录的字段。4000的结果不足以推断缺记录。',
 '4000符合正整数域；有记录读取显式4000，与省略字段默认或缺记录回退是不同来源。',
 '已有记录读取显式5000；原V08合法别名消费者不受修订影响，未增加UI或保存步骤。',
 '指定身份和基础都未命中，才进入缺记录回退4000；不能把这一分支的条件泛化为所有4000输出。'
]
source_basis=[
 'GameData1–283;TownMap1–43', 'GameData1–283;五整数类全文;Metadata/PlayerMetadata/DungeonTileset查询覆写', 'TerrainTag1–204;Item1–100,112–140;GameData217–233;Exp1–48',
 'Compiler384–459,690–737;CompilePBS1–90,1196–1232;DungeonParameters1–135', 'DungeonParameters58–96;CompilePBS1211–1232', '同V02;RandomDungeons1063–1106', 'CompilePBS1–90,1211–1232', 'DungeonParameters58–96;CompilePBS1211–1232', 'Compiler384–459,690–737;三类schema全文', 'SpeciesMetrics1–101;CompilePBS543–588;Species267–274', 'ShadowPokemon1–70;CompilePBS543–588;PokemonShadow1–65', 'CompilePBS1–90,543–588', 'Compiler384–459,690–737;CompilePBS543–588', 'DungeonTileset1–222;CompilePBS1–90,1196–1232', 'SpritePositioning1–125;WritePBS23–65,291–359', 'Compiler967–1117;CompilePBS1–90', 'ShadowPokemon16–54;PokemonShadow32–39', 'ShadowPokemon16–54;Compiler正整数门;PokemonShadow32–39', 'ShadowPokemon16–54;PokemonShadow32–39', 'ShadowPokemon35–54;PokemonShadow32–39'
]
author=json.loads((R/'actual-input/candidate/candidates/R7-U01/evidence/author/per-id.json').read_text())
original_vectors=author['records'][0]['vectors']+author['records'][1]['vectors']+author['records'][1]['r1_correction']['additional_vectors']
assert len(original_vectors)==20
vectors=[]
for i,v in enumerate(original_vectors):
 line=(206+i) if i<16 else (231+i-16)
 vectors.append({'id':v['id'],'premises':premises[i],'input_from_fixed_original_or_repaired_candidate':v['input'],'expected_from_fixed_input':v.get('expected',v.get('expected_consumer_result')),'actual_catalog':clause(generic,line,line),'independent_actual_reason':reasons[i],'source_basis':source_basis[i],'static_assessment':'SATISFIES_NARROW_CONTRACT_AT_MI','evidence_level':['SOURCE_STATIC','DERIVED_VECTOR'],'behavior_execution':'NOT_EXECUTED'})
remaining=['R7-I must receive this new exact-result commit/tree and register semantic/shared/consumer/historical responsibilities for these two IDs.','Historical root-cause/dedup reception including M20/M22 and C03 E009/E010 mapping debt remains root-owned at its exact scope; no global completion is inferred.','R7-I alone may make separate scoped ACCEPTED and CLOSED decisions after the applicable original gates; neither state is set here.']
history=[
 {'ids':'KR03–08,KR12,KR14–16','assessment':'全文核对查找类型/未知身份/实例/直接登记/phone默认特例；整数比较补充不改变查询覆写或直接覆盖。','status':'STATICALLY_COMPATIBLE_AND_PRESERVED','execution':'NOT_EXECUTED'},
 {'ids':'KL02–06,KL15–16,KL23–26,KL36–39,R6-U14-C06-01–03','assessment':'启动与直接、可选缺席、重复/引用、部分记录自字段默认与整条缺席克隆、后缀及保存时路径分层保持；新增header条款没有提供统一事务。','status':'STATICALLY_COMPATIBLE_AND_PRESERVED','execution':'NOT_EXECUTED'},
 {'ids':'DG01,DG17–27,GR3-DQ01–09,U01-M01-021/022-01–03','assessment':'默认5×5与cave5×4、非空图块集回首条/空表失败、完整组、构造/播种/生成/摆放及暂存写入前缀均逐前提核对；外部输入别名没有承诺后段生成成功。','status':'STATICALLY_COMPATIBLE_AND_PRESERVED','execution':'NOT_EXECUTED'},
 {'ids':'WE-M15/16/17/19/20,B19-C016;WP73-B§7/7.5;WP23data§3','assessment':'仅成功登记后的指标查询/编辑；同值/取消/改动标记、克隆五组及空后缀、非0后缀选路径先于等值省节、No重载/Yes先dat后PBS、既有布局不广播重定位保持；Shadow字段默认4000与现有记录合法4000均保持。','status':'CONDITIONAL_SYNC_NOT_TRIGGERED','execution':'NOT_EXECUTED'}
]
shared_eval=[
 {'group':'CG01','path':'audit/source-traceability.md','actual_contributors':['R7-U13','R7-U11','R7-U12','R7-U01','R7-U02'],'judgment':'全文读实际1888行；按B坐标接收MIDI三行、extendtext有限静态补充、H08导航单行、U01及U02 EOF段。U01先U02；原批准/未读桥/运行限制保留，root当前接收入口分开作者时点标签。'},
 {'group':'CG02','path':formal+'demo-dx/wp73-b-world-editors.md','actual_contributors':[],'judgment':'U01条件同步未触发，实际全文与B相同。§7已有成功登记/查询、§7.5保存前缀与producer补充相容；U10流程WAIT，未假定其未来内容已合入。'},
 {'group':'CG03','path':formal+'test-catalog/demo-dx-wp72-73-74-75-76-77.md','actual_contributors':['R7-U11'],'judgment':'全文409行；U11只在原B完整前缀后追加EXT01–12，未覆盖WE指标行；窗口请求/native未知与U01静态读取门相容，U10未合入。'},
 {'group':'CG04','path':engine,'actual_contributors':['R7-U13','R7-U01'],'judgment':'全文725行；U13在B04资源之后的独立S01与U01 EOF J01索引均精确保留。MIDI声明的L04/L09未知与地牢producer无冲突，U03流程WAIT未合入。'},
 {'group':'CG06 INCIDENTAL','path':formal+'test-catalog/user-interface-wp17-63-65-66-67-68-69-70-71.md','actual_contributors':['R7-U08','R7-U02'],'judgment':'完整文件字节重组核验；语义只读实际390–452及1025–1111。U08 HP四行/LC13与U02 EOF81行在不同B坐标，原批准报告均读，内容与U01没有互相否定。此处不声明UI全文新审或另项PASS。'},
 {'group':'CG07','path':'planning/feature-matrix.md','actual_contributors':['R7-U13','R7-U11','R7-U12','R7-U01','R7-U02'],'judgment':'全文592行；F05-02 MIDI pending、F18-04有限静态、R6导航单行及U01先U02 EOF分别保留；旧状态/56/92/27/13未升级。'},
 {'group':'ROOT ADMIN','path':'audit/matrix current reception + current-navigation-errata.json','judgment':'两个同文当前登记入口指向MI中真实public-reception；八个固定candidate-input和candidate_commit均核同。errata仅status及reception阶段变化，行为/旧R6载荷/标签其余字段相同，ACCEPTED/CLOSED仍false。'}
]
write(D/'tool-evidence/shared-semantic-evaluation.json',{'MI':MI,'checks':shared_eval,'scope':'Compatibility and preservation of U01 in accumulated bytes; no new verdict for other required IDs.','receiver':'R7-I sole actual integrator; this result still requires root receipt'})
records=[]
for id_,vs,clauses_ in [('GR7-M01-001',vectors[:3],[clause(wp03,41,42),clause(generic,206,208)]),('GR7-J01-001',vectors[3:],[clause(wp03,56,58),clause(wp03,175,209),clause(wp03,379,379),clause(wp04,113,116),clause(wp04,307,307),clause(generic,209,221),clause(generic,224,236),clause(engine,709,725),clause('audit/source-traceability.md',1850,1862),clause('planning/feature-matrix.md',570,580)])]:
 records.append({'id':id_,'conclusion':'PASS_SCOPED_ACTUAL_INTEGRATION','actual_MI':MI,'actual_tree':'6480ffe3df49bd9776c719f3c9be1c13618fdb0a','actual_formal_subtree':'8403869aaeb4726518414b409b3808c3c0780e65','actual_clauses':clauses_,'common_premises':common,'vectors':vs,'findings':[],'seven_groups_assessment':{'identity':'Exact original root and actual MI/FI identities verified; fresh visible context, no agents.','original_counter':'Full original seven groups and narrow non-author counter reviewed; earlier read/execute qualifications retained.','minimum_preserve':'Current actual behavior clauses satisfy narrow revision and correct controls, without architecture/policy expansion.','vectors_regression':'Every named original and repair vector assessed statically; complete mandatory documents read; no behavior execution.','independent_history':'Old r1 FAIL stays bound to de550bb9; r2 candidate approval allows entry only, not inherited.','consumers_shared_dependencies':'Finite direct/transitive consumers and shared bytes compatible; root receipt remains separate.','execution_unknowns':'SOURCE_STATIC and DERIVED_VECTOR only; TOOL_VALIDATION not semantic evidence; effective config UNVERIFIED; L01–L14 retained.'},'normal_cancel_failure_partial_commit':{'normal':'All normal examples retain legal prerequisites and observation points; no default gameplay or host success inference.','cancel':'M01 comparison/query has no interaction; PBS has no cancellation; independent editor No/Yes belongs to J01-V12.','failure':'M01 false is normal; invalid header/unknown Species/duplicate and incomplete Tileset group fail at separate gates.','partial_commit':'M01 comparison no write; J01 first registration, other saved tables, direct olddat and startup delete-attempt prefixes separate, no blanket rollback.'},'historical_and_conditional_reviews':history if id_.startswith('GR7-J') else history[:1],'dependencies':{'named_record_direct_edges':[],'named_record_transitive_edges':[],'edge_qualification':'Original normalized M01 and J01/root narrowed contracts give no named author scheduling edge; this does not remove domain/shared/history obligations.','finite_static_source_consumer_compatibility':'SATISFIED_FOR_THIS_REVIEW_SCOPE','direct_domain':'五整数类/双身份/Item比较与lookup覆写' if id_.startswith('GR7-M') else '三producer接受/转换/登记、各query门、Species枚举及可选Shadow前提','transitive_domain':'EXPSHARE符号消费者保留；不增加普通玩法故障' if id_.startswith('GR7-M') else 'Species.metrics→指标布局/编辑/反写；Shadow查询→最大量表/领域默认；Dungeon查询→生成前输入及失败前缀；直接编译/启动分派；相关目录/追溯/matrix','remaining_root_gates':remaining},'shared_receiver':'R7-I; shared-semantic-evaluation.json and supplemental-audit.json bind exact contributions and original candidate approvals','ACCEPTED':False,'CLOSED':False})
records[1]['r1_finding']={'id':'R7-U01-R1-J01-01','old_candidate':'de550bb9fe5d2b80312b1a4f6f166d2a6aa5fc67','old_review':'1a479cf49386a0aabe2ccd96aef92abb16620143','old_verdict':'FAIL_SCOPED_CANDIDATE_RETAINED','current_assessment':'MINIMUM_REPAIR_SATISFIED_AT_ACTUAL_MI','reason':'Actual WP03:58 separates present-record field default/explicit4000 from missing-record fallback; four additional legal controls read against fixed source and actual catalog.','no_inherited_candidate_pass':True}
write(D/'per-id.json',{'schema':'r7.u01.independent-actual-review.v1','reviewer_identity':identity,'actual_MI':MI,'actual_FI':FI,'records':records,'execution':{'source_static':'PERFORMED','derived_vectors':'ALL_NOT_EXECUTED','tool_validation':'IDENTITY_SCOPE_ASSEMBLY_TRANSPORT_ONLY','REFERENCE_OBSERVATION':'NOT_EXECUTED','reference_program':0,'independent_complete_model':0,'host':0,'Demo':0,'native_media':0,'real_save_replay':0},'limits':'L01–L14 retained in full original file copied under tool-evidence; no runtime/global certificate','denominator':{'issues':27,'batches':13},'nonmandatory_adoption':'NONE'})
source_reads=[]
for path in sorted(set(x['path'] for x in rows if '/inputs/reference/' in x['path'] or '/extra-input/' in x['path'])):
 p=pathlib.Path(path);source_reads.append({'local_path':path,'reference_commit':common['reference'],**ident(p.read_bytes()),'read_ranges':[[x['start_line'],x['end_line']] for x in rows if x['path']==path],'use':'Static source only, never executed; unlisted lines not claimed read.'})
input_receipt={'schema':'r7.u01.actual-input-receipt.v1','created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'identity':identity,'dispatch':{'commit':'c64774c60d91e522cb515ef71e3e9d4ea6b4712c','tree':'a1ca6722bfeb35fa8ad53074fa29658b32ac154e','path':'review/remediation-seventh-20261015-prepare/integration/wave2/v1/dispatch/R7-U01-R7IR.md',**ident((R/'bootstrap/R7-U01-R7IR.md').read_bytes()),'read':'FULL before any delegation; no delegation performed'},'MI':{'commit':MI,'tree':'6480ffe3df49bd9776c719f3c9be1c13618fdb0a','formal131_subtree':'8403869aaeb4726518414b409b3808c3c0780e65'},'FI':{'commit':FI,'tree':'6747a584b91c86acd4771c1a6dee93260602106f','path':'review/remediation-seventh-20261015-prepare/integration/wave2/v1/integrated-input.json',**ident((R/'bootstrap/integrated-input.json').read_bytes())},'B':{'commit':B,'tree':'84f79ec6e772aacbf3a464fde68cdc5a280e2950','formal_subtree':'ebbe29f2bc88cd17de7072bf440c6fa8c8c7089c'},'reference':{'commit':common['reference'],'declared_tree':'7589c800b61ba13a13040ed0d686979b80a84fd0','qualification':'Selected exact reference files restored and independently hashed; no new complete reference checkout/tree or execution certification.'},'original_contract':{'commit':'f622356f3beb9e84ea8cff9db07c7fb382565d3f','path':'review/remediation-seventh-20261015-prepare/delegation/contracts/R7-U01.json',**ident((R/'original/dispatch/delegation/contracts/R7-U01.json').read_bytes()),'read':'Both complete seven groups; original M03 counter, M01 root/normalized verification and dependencies, J01 original record31 and full counter V01–13; full L01–L14'},'candidate_history':{'author_commit':'a3938bbb8f8c2294465b75363a39fd4598b82a15','author_tree':'9a53dcb2abdedbf4246e3e9d93c42080f92939ec','review_commit':'2e1b1fb6dd638757436b7292949b3ba0012cafec','review_tree':'04d0b3861ee1e96650c9982a237120df8cb8701d','old_failed_candidate':'de550bb9fe5d2b80312b1a4f6f166d2a6aa5fc67','old_failed_review':'1a479cf49386a0aabe2ccd96aef92abb16620143','read':'Author report/per-ID/contributions/correction, r1 and r2 review findings, reports/per-ID/qualification; all bounded members mechanically verified, received scripts not executed. Shared original approval reports and root eligibility read.'},'restoration':{'tool_fixed_commit':'658488c81f1f3181a488298ab27850c8af951d73','original':{'files':40,'bytes':7539352,'destination':str(R/'original')},'actual':{'files':186,'bytes':8168283,'destination':str(R/'actual-input')},'all226_independently_reverified':True,'both_native_status':'BOUNDED_RESTORE_BYTES_VERIFIED','no_resume_needed':True,'read_only_snapshots':True,'qualification':'Bounded fresh local restores, not shared directories, not full repository/runtime certification'},'mandatory_full_actual_documents':actual,'source_reads':source_reads,'mechanical_evidence':{'formal':audit['formal_counts'],'journal_hunks':56,'journal_targets':24,'U01_hunks':11,'same_boundary_EOF':'U01 then U02 on audit and matrix','shared_fixed_checks':9,'prior_accepted_files':5,'root_adjustments':3,'all_identities':'tool-evidence/mechanical-audit.json','r1_repair_and_original_bindings':'tool-evidence/supplemental-audit.json'},'instructions':{'AGENTS':'Full actual B/MI AGENTS read; exact unchanged; clean-room behavior only','skills':'No tracked .agents at B/MI; project .agents/skills absent; workspace .agents no files returned; no related local skill applied'},'supplemental_UI':{'actual_identity':supp['UI_full_file'],'semantic_ranges':[[390,452],[1025,1111]],'U08_fixed_approval':'tool-evidence/ui-approval-identity.json','qualification':'Outside-U01 preservation/compatibility only, not full UI semantic review'},'prior_five':{'identities':audit['prior_five'],'semantic_scope':'Full actual WP39/WP41/WP34 and two catalogs read. U04 raw target3/rescue1/explicit5 and nonfatal continuation, U05 parent dynamic read vs explicit child same-value submit remain compatible with identity/header changes. No fresh verdict for their three IDs.'},'provenance_qualifications':['Early reconnaissance/fetch/bootstrap/direct reads have platform I/O but not separate complete local per-command UTC/stdout/stderr/PID; do not reconstruct times or private model streams.','read-io.jsonl logs actual printed ranges and hashes, not independent semantic proof. Oversized output truncations were followed by bounded rereads of required missing segments. JSON projections omit repetitive identity/reference fields explicitly, not new reading credit.','Mechanical audit initial missing Git objects; second compared decompressed bytes to compressed transport Git blob; third attempted nonexistent B errata. Corrected independent audit passes; real failed logs preserved. These are tool defects, not behavioral runs.','Supplemental audit initially assumed only one changed top-level errata phase field. Actual diff has status and reception; corrected exact allowlist verifies all behavior/other fields unchanged and ACCEPTED/CLOSED false; failed log retained.','One read-only cat-file probe for U08 original approval returned128 (object absent); exact read-only fetch succeeded, then report read; early probe platform I/O only.','Candidate r2 early gh auth diagnostic deviation and incomplete early command logs remain disclosed in its received evidence/root eligibility; not promoted to perfect compliance. This review did not query authentication/quota.','Internal opaque identities/effective configuration unexposed remain so; visible distinct identifiers do not certify those hidden fields.','M03 historical unread WP03 96–EOF, DungeonTileset126–EOF, TerrainTag111–EOF stay historical unread; this task new reads do not retroactively fill them.'],'execution_and_limits':{'all_behavior_vectors':'NOT_EXECUTED','reference_observation':0,'reference_program':0,'independent_complete_model':0,'host':0,'Demo':0,'native_media':0,'real_save_replay':0,'L01_L14':'FULL_RETAINED','old56_92':'UNCHANGED_NO_REISSUE','denominator':'27 items/13 batches','nonmandatory_adoption':'NONE','procedural_WAIT_batches':['R7-U03','R7-U07','R7-U10']},'unmet_root_gates':remaining,'publication':{'branch':'codex/r7-ir-u01-20261015-r1','checkout':str(C),'base':B,'only_write_prefix':PREFIX+'/','normal_push_only':True,'self_identity':'Result commit/tree and final remote readback bound externally after real commit; no circular manifest self-hash'}}
write(D/'review-input-receipt.json',input_receipt)
write(D/'tool-evidence/source-and-reading-ledger.json',{'mandatory_actual_full':actual,'source_reads':source_reads,'qualification':'Full mandatory documents read, conclusions limited to U01 and named preservation. Raw reference/source output remains only local/platform; no source text published.'})
for p in (R/'tool-evidence').iterdir():
 if p.is_file():copy(p,D/'tool-evidence'/p.name)
for name in ['restore_container_context.py','run_recorded.py','read_static.py','audit_actual.py','audit_supplement.py','fetch_extra.py','build_deliverables.py']:
 copy(R/'bootstrap'/name,D/'tool-evidence/tools'/name)
for name in ['R7-U01-R7IR.md','independent-containers.md']:
 copy(R/'bootstrap'/name,D/'tool-evidence/bootstrap'/name)
for name in ['original','actual']:
 copy(R/(name+'-plans/R7-U01.json'),D/f'tool-evidence/{name}-restore-plan.json')
 source=R/('original' if name=='original' else 'actual-input')
 receipts=list(source.glob('recovery-receipt-*.json'));assert len(receipts)==1
 copy(receipts[0],D/f'tool-evidence/{name}-restoration.json')
copy(R/'original/evidence/tasks/R7-C17/limits-and-alias-reception.json',D/'tool-evidence/original-L01-L14-and-aliases.json')
report='''# R7-U01 r1 独立实际整合复审

GR7-M01-001、GR7-J01-001 均为 **PASS_SCOPED_ACTUAL_INTEGRATION**。仅限固定 MI 的两项缩窄静态行为合同及具名消费者、回归和共享保留；没有发现阻塞本次有限判断的缺项或内容缺陷。所有行为向量 **NOT_EXECUTED**，本报告不登记 ACCEPTED 或 CLOSED。

审者实际 CODEX_THREAD_ID/CODEX_SESSION_ID 为 `01a1401b-c532-76db-a584-3d378debb00f`，与合同全部可见排除标识及旧 r1 审者不同；来自本容器实际环境回读。未创建子任务、辅助 agent 或模型调用。平台 opaque context/task ID、模型进程 PID 未暴露，不用 /root 或 shell PID 推断身份。请求 gpt-6.1-sol / ultra / default 普速禁 Fast；有效 model/effort/tier/speed 四项均 UNVERIFIED。

| 固定角色 | 完整提交 | tree／子树 |
| --- | --- | --- |
| 全文派发 | c64774c60d91e522cb515ef71e3e9d4ea6b4712c | a1ca6722bfeb35fa8ad53074fa29658b32ac154e |
| 实际 MI | 45c80832a41c1b56dcd7e9d93497758cbb7721de | 6480ffe3df49bd9776c719f3c9be1c13618fdb0a |
| MI 正式131份 | 同 MI | 8403869aaeb4726518414b409b3808c3c0780e65 |
| 实际 FI | 13d76ba61838b13925ba9d41f58a6b047564d926 | 6747a584b91c86acd4771c1a6dee93260602106f |
| B | e646432c644dec04d306842cc5a559a29c718fbc | 84f79ec6e772aacbf3a464fde68cdc5a280e2950；正式 ebbe29f2bc88cd17de7072bf440c6fa8c8c7089c |
| R 具名只读源 | 8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b | 声明7589c800b61ba13a13040ed0d686979b80a84fd0；本次核选定文件，不认证完整参考树 |

完整合同、实际 AGENTS 和固定恢复工具/说明/两清单先读后用；B/MI无 tracked .agents，工作区 .agents 无文件、项目 .agents/skills 不存在，未套用不存在的技能。本成果只分析独立行为，不实现框架或复制参考源码。

本容器按批准命令分别实际恢复原40文件／7,539,352字节和实际输入186文件／8,168,283字节；两次 BOUNDED_RESTORE_BYTES_VERIFIED，无中断续传。全部226成员重新独立核 bytes/SHA256/blob，项目载荷与固定 Git 对象匹配；gzip运输先核编码再核解码，快照已只读。另从固定R精确补取指标编辑器13,377字节和Item12,359字节，均核完整身份，没有把可读依赖伪标限制。

FI全131文件表、实际路径宇宙、B/MI身份及改动标志已核：26改变／105不变。56处B相对批准片段重新从各候选提取并逐段重建24目标；两处同边界EOF为U01→U02，其余不相交。三处root调整是audit/matrix当前入口和errata阶段元数据。前序U04/U05五份已接受文件与其接受时MI逐字相同。此处机械通过仅为TOOL_VALIDATION，以下判断来自内容审读。

合同指定16份实际目标／消费者全部全文读，包括audit1888行、matrix592行和各完整目录；截断输出的缺段已分段补读。原f622356f两项完整七组、M03反证、M01原成员/规范化验收及依赖、J01原record31及非作者V01–13、L01–L14实际读到。五个去重原始区间／JSON pointer／canonical绑定另核相同。旧候选和r1失败史、当前作者及r2候选结果均按固定身份接收，没有继承其PASS。完整字节表、实际跨度和读取范围见[输入回执](review-input-receipt.json)及[独立机械审计](tool-evidence/mechanical-audit.json)。

| ID | 实际条款与本次判断 | 结论 |
| --- | --- | --- |
| GR7-M01-001 | WP03:41–42，generic:206–208。合法TownMap1查找命中而记录对整数1正常为假，同类同主身份为真。五整数类全文声明/构造与查询覆写逐一核；Grass另一序号2及Item符号/字符串EXPSHARE控制保持。比较无交互取消、领域写入、保存或部分提交，不推出普通游戏故障。 | PASS_SCOPED_ACTUAL_INTEGRATION |
| GR7-J01-001 | WP03:56–58、175–209、379；WP04:113–116、307；generic:209–221、224–236及engine:709–725。三生产者接受域、Species先登记/Shadow本例启用、可选省略/空位0与显式0拒绝、外部别名及第二节拒绝逐条件成立。登记元数据、查询、消费者和保存前缀分别描述，不要求未来采用源键/类/架构。 | PASS_SCOPED_ACTUAL_INTEGRATION |

M01重新核查GameData全文、TownMap/Metadata/PlayerMetadata/MapMetadata/DungeonTileset全文、TerrainTag全文以及Item符号声明/构造和经验分享消费者。Metadata默认0、PlayerMetadata回1、DungeonTileset非空回首条仍属各自查询合同；不从数字查询成功推出整数比较真。原M03的未读WP03 96–EOF、DungeonTileset126–EOF、TerrainTag111–EOF保持其历史资格，本次补读不倒填原审者。

J01三query门不同：Metrics只有正形态先试形态身份，Shadow/地牢对所有整数先试指定身份；命中别名不再新建克隆。地牢专用重复诊断在通用门前，两个顺序分别用第二节cave/1、cave_1/0；Metrics/Shadow走通用第二节拒绝。Tileset7/23须各有合法Autotile与Tile完整组，缺组构造失败不能充当重复门反例。直接登记覆盖与PBS转换后拒绝仍是不同入口。

旧r1 `R7-U01-R1-J01-01` 的FAIL仍只绑定 de550bb9fe5d2b80312b1a4f6f166d2a6aa5fc67／审查1a479cf49386a0aabe2ccd96aef92abb16620143。当前r2对旧镜像仅WP03第58行一句修订、generic原223行后追加13行，原16向量对象及另四镜像保持。实际MI已接收这一修订：有记录读取GaugeSize，字段省略默认4000、显式4000也合法；无指定/基础记录才回退4000。四个修订对照分别为省略4000、显式4000、显式5000、双无命中回退4000。同结果4000不能证明缺记录。原5000别名、WP23正确默认及可选前提没有排除。

全部20向量在[逐ID记录](per-id.json)逐条给前提、输入、观察点、固定源静态理由及实际目录跨度身份；3个M01、13个J01原例、4个r1修订例均静态满足。V01/02/10/11正常成功仍须终检/I/O及后续依赖正常；PBS没有取消。V12独立指标No正常重载，Yes先dat后PBS，后PBS失败不回滚先存档案。V04/06/09失败不登记第二节或非法条目。V13保留首条内存、直接旧dat、其它先存表及启动删除尝试；Reset/SystemExit原样重抛，不承诺全盘清空、总回滚或宿主恢复。

具名历史回归已按完整目录重新判读：KR03–08/12/14–16；KL02–06/15–16/23–26/36–39、R6-U14-C06-01–03；DG01/17–27、GR3-DQ01–09、U01-M01-021/022-01–03；WE-M15/16/17/19/20及B19-C016。正确类型/未知身份、可选输入缺席不清表、部分记录自字段默认与整条缺席克隆、后缀/保存时路径、默认5×5/cave5×4、非空图块集回首条/空表失败、构造/播种/生成/摆放失败前缀均保持相容。没有执行历史向量或重授旧全局PASS。

WP14 §3.2/3.3已有输入查询与生命周期转交；WP23data §3正确保留字段默认；WP73-B §7/7.5和DX指标行建立在成功登记后。其非0后缀先选路径、等值省节不取消路径、No/Yes、克隆五组/空后缀及既有布局不自动重定位与本次producer补充无具体矛盾，因此U01四条件目标不触发写入。完整WP39/WP41/WP34和两个前序目录读到：U04原始目标3／捕获补救1／显式5及非致死继续扫描，U05亲本动态读与子代显式同值提交，都未被本批身份/节头规则扩大或否定。五文件相同只是保留证明；这里另作相容判断，不为三个前项新签PASS。

共享接收逐条对照B、候选和原独立批准，详见[内容相容记录](tool-evidence/shared-semantic-evaluation.json)及[精确保留审计](tool-evidence/supplemental-audit.json)。CG01 audit全文保留U13 MIDI、U11 extendtext、U12导航及U01/U02尾段；CG04 engine全文保留U13独立S01及U01 J01索引；CG03 DX全文只接U11尾附，不覆盖WE；CG07 matrix全文保留各批备注/导航及U01先U02。CG06 UI只审390–452、1025–1111实际内容并核完整字节重建，U08两个片段与U02尾附互不覆盖；原U02/U08批准报告均读，不宣称UI全文新语义审查。U03/U07/U10流程WAIT、未合入，不能当其领域无依赖或未来贡献已接收。

root当前入口把作者制作时点候选标签与当前接收分开；两处链接在MI中存在，八份固定freeze/input均绑定正确候选。errata仅status及reception阶段更新，其余字段完整相同，ACCEPTED/CLOSED仍false；不是行为或正式状态升级。公共登记21候选项／3前序实际PASS／3前序ACCEPTED／0CLOSED只是固定输入的旧快照，本报告不修改它。

原合同没有具名record→record直接/传递作者排程边，不能据此推全局依赖满足。有限静态源→producer/query→领域消费者→目录/共享文件相容义务在本次范围已满足；R7-I仍需接收本新结果，并登记语义、共享、直接/传递消费者及具名历史责任。M01历史M20/M22排重、J01 C03 E009/E010错误anchor债务按原资格交根接收；没有改冻结M01/C03或恢复完整SUPPORTED。正式ACCEPTED及CLOSED须根分别决定，不能由本报告自动放行。

SOURCE_STATIC、DERIVED_VECTOR与TOOL_VALIDATION分别记录。REFERENCE_OBSERVATION、参考程序、独立完整行为模型、宿主、Demo、native媒体、真实存档回放新增均0；历史H14/UTIL-03局部观察不移植为本任务执行。L01–L14全文保留于[原限制](tool-evidence/original-L01-L14-and-aliases.json)，model/effort/tier/speed均UNVERIFIED，旧56/92与27项/13批保持，7optional／2导航facet／1no-required／2policy未采用。

工具失败和日志缺口没有抹去：前三次机械审计分别遇缺Git对象、gzip编码/解码对象比较及B不存在新errata的工具错误，修正后实际重核成功；补充审计误假设errata只一顶层字段，实为status/reception两阶段字段，按真实差异修正后成功。失败回参均保留。早期侦察/读取/fetch/bootstrap有平台I/O，未另存逐命令完整UTC/PID/分离流，不回填；read-io只记实印范围/哈希，截断后有补读。候选r2早期认证诊断偏差及原日志限制照旧披露，本次未查认证/额度、不发私有模型流。详细资格见输入回执。

成果仅在从B创建的隔离checkout、唯一分支 `codex/r7-ir-u01-20261015-r1`，只写本r1目录；不携带候选/MI正文、不改公共台账/main/tag。普通提交/推送及最终不可变URL逐文件完整bytes/SHA256/blob/mode回读，由真实外层commit/tree与末次回执绑定；manifest不伪造递归自哈希。先行运输回执若由后继提交封存，只证明其明确前一提交，最终后继另作全量读回。
'''
(D/'report.md').write_text(report)
write(D/'artifact-manifest.json',{'schema':'r7.u01.actual-artifact-manifest.v1','MI':MI,'FI':FI,'branch':'codex/r7-ir-u01-20261015-r1','base':B,'write_prefix':PREFIX+'/','files':[{'path':str(p.relative_to(D)),**ident(p.read_bytes())} for p in sorted(D.rglob('*')) if p.is_file() and p.name!='artifact-manifest.json'],'self_binding':'Manifest itself is bound by final immutable result commit/tree and exhaustive remote readback; no circular self-hash.','qualification':'Only review evidence; no source, candidate mirror, formal content or public-ledger edit.'})
print(json.dumps({'result_directory':str(D),'files':len([p for p in D.rglob('*') if p.is_file()]),'mandatory_full_documents':len(actual),'vectors':len(vectors),'conclusions':{x['id']:x['conclusion'] for x in records}},ensure_ascii=False,indent=2))
