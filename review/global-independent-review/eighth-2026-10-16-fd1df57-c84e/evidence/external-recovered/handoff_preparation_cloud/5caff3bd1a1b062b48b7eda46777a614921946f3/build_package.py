from pathlib import Path
import json,hashlib,subprocess,gzip,runpy,re,itertools,datetime
R=Path('review/global-independent-review/eighth-2026-10-16-fd1df57-c84e');T=R/'tasks/handoff_preparation_cloud';H=T/'handoff';H.mkdir(exist_ok=True)
C='40f45dddcdea5522b4bf7d0fea1a0f74f7d3d232';B='fd1df570cad987dc3852a3b958f03916e317f7fe';REF='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b';S='/workspace/pokemon-essentials';ROOT='/workspace/pokemon-essentials-clean-room'
def git(*args,repo=ROOT):return subprocess.check_output(['git','-C',repo,*args])
def jwrite(path,data):path.parent.mkdir(parents=True,exist_ok=True);path.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
def identity(repo,c,p):
 b=git('show',c+':'+p,repo=repo);tree=git('rev-parse',c+'^{tree}',repo=repo).decode().strip();mode,typ,blob,*_=git('ls-tree',c,'--',p,repo=repo).decode().split()
 return dict(repo=repo,commit=c,tree=tree,path=p,mode=mode,blob=blob,bytes=len(b),sha256=hashlib.sha256(b).hexdigest())
d=json.loads((R/'adjudication/root-decisions.partial.json').read_text());author=runpy.run_path(str(T/'contracts_authoring.py'))['CONTRACTS'];assert set(author)=={x['id'] for x in d['records']}
formal=git('ls-tree','-r','--name-only',B,'--','deliverables/final-specification-set').decode().splitlines();assert len(formal)==131
short={}
for p in formal:
 stem=Path(p).name
 # all default simple WP prefixes
 m=re.match(r'(wp\d+)-',stem)
 if m and m[1] not in short:short[m[1]]=p
short.update({'wp60-berry':'deliverables/final-specification-set/pokemon-rules/wp60-berry-plants.md','wp65-main':'deliverables/final-specification-set/user-interface/wp65-title-load-options-pause-and-pc.md','wp52-a-main':'deliverables/final-specification-set/combat-requirements/wp52-a-generic-numerical-and-status-evaluation.md','wp67-a':'deliverables/final-specification-set/user-interface/wp67-a-battle-interaction-and-presentation.md','wp69-slot':'deliverables/final-specification-set/user-interface/wp69-slot-machine.md','wp13-events':'deliverables/final-specification-set/engine-overworld/wp13-map-events-npc-followers.md','wp13-matrix':'deliverables/final-specification-set/engine-overworld/wp13-interpreter-command-matrix.md','tc-world':'deliverables/final-specification-set/test-catalog/engine-overworld-wp11-15-59-60.md','tc-kernel-save':'deliverables/final-specification-set/test-catalog/generic-kernel-wp05-06-07-08-09-10.md','tc-kernel-pbs':'deliverables/final-specification-set/test-catalog/generic-kernel-wp02-03-04.md','tc-creature-growth':'deliverables/final-specification-set/test-catalog/pokemon-rules-wp19-21-22-23-34.md','tc-combat-main':'deliverables/final-specification-set/test-catalog/combat-requirements-wp39-40-41-42-45.md','tc-combat-ai':'deliverables/final-specification-set/test-catalog/combat-requirements-wp49-51-52.md','overlay':'review/remediation-eighth-20261016-prepare/navigation/current-r7-metadata-qualification.json'})
for k,p in short.items():
 if k!='overlay':assert p in formal,(k,p)
# Explicit decisions override source proposals throughout. Raw versions preserved separately.
batches={
 'R8-U01':(['GR8-KER-001','GR8-KER-002'],'存档有序失败与读取结果门'),
 'R8-U02':(['GR8-KER-003'],'PBS旧属性更新的输出边界'),
 'R8-U03':(['GR8-PBSW-001'],'树果显式记录频数'),
 'R8-U04':(['GR8-PBSW-002','GR8-WORLD-001','GR8-WORLD-002','GR8-WORLD-003','GR8-WORLD-INT-001','GR8-WORLD-INT-002'],'地图/跳跃/解释器共享合同'),
 'R8-U05':(['GR8-WORLD-004','GR8-EXT-CD-002'],'遭遇输入与驱虫引用'),
 'R8-U06':(['GR8-CRE-001']+['GR8-COM-'+str(n).zfill(3) for n in range(1,9)]+['GR8-AI-001'],'战斗主合同与成长/AI共享目录'),
 'R8-U07':(['GR8-HIST-001','GR8-HIST-R2-BINDING-001','GR8-HIST-U06-CONTINUATION-001'],'历史资格后继overlay'),
 'R8-U08':(['GR8-ELR-001'],'老虎机语言资源接点'),
 'R8-U09':(['GR8-PBS-EGGGROUP-DOMAIN-001'],'固定蛋群作者接受域')}
byid={i:b for b,(ids,_) in batches.items() for i in ids};assert len(byid)==27
# Gather exact all referenced source/formal file identities; reported locators remain associated.
pat=re.compile(r'(?:deliverables/final-specification-set|Data/Scripts|PBS)/[^\n\"<>]*?\.(?:md|rb|txt)')
cache={};missing={};record_paths={}
def discover(v,out):
 if isinstance(v,dict):
  for field in ['path','identity_path']:
   p=v.get(field)
   if isinstance(p,str):
    p=p.removeprefix(ROOT+'/')
    if p.startswith('review/remediation-seventh-20261015-prepare/') and p.endswith(('.json','.md')):out.add(p)
  for k,x in v.items():
   if k not in ['content','text','complete_unit_text','failed_guess_preserved']:discover(x,out)
 elif isinstance(v,list):
  for x in v:discover(x,out)
 elif isinstance(v,str):
  for m in pat.finditer(v):out.add(m.group(0))
for rec in d['records']:
 ps=set();discover(rec,ps)
 for k in author[rec['id']]['write_keys']:ps.add(short[k])
 record_paths[rec['id']]=[]
 for p in sorted(ps):
  if p==short['overlay']:continue
  repo,c=(ROOT,B) if p.startswith(('deliverables/','review/')) else (S,REF)
  key=(repo,c,p)
  if key not in cache:
   try:cache[key]=identity(repo,c,p)
   except subprocess.CalledProcessError:missing[p]='Cited name not recoverable at fixed commit; no read credit; exact original pointer retained.';continue
  record_paths[rec['id']].append(key)
# Source/F identifiers and exact snapshots can use indirection; full frozen record resolves it.
ids={key:'E'+str(i+1).zfill(4) for i,key in enumerate(sorted(cache))}
jwrite(T/'reading-ledger/source-spec-identities.json',{'schema':'r8-handoff-evidence-identities/v1','files':[dict(evidence_id=ids[k],**cache[k],purpose='Fixed parent identity for received bounded contract; no new whole-source review credit') for k in sorted(cache)],'unresolved_cited_spellings':missing,'global_formal_file_denominator':131,'R_tracked_file_denominator':len(git('ls-tree','-r','--name-only',REF,repo=S).splitlines())})
# Full original root records are audit input, never interpreted as self-adopted/PASS.
with gzip.open(T/'audit/received-root-records.json.gz','wb') as f:f.write(json.dumps(d,ensure_ascii=False,separators=(',',':')).encode())
extra_paths=['AGENTS.md',str(R/'delegation/prompts/handoff_preparation_cloud.md'),str(R/'delegation/readsets/handoff_preparation_cloud.complete.json'),str(R/'delegation/handoff-preparation-mandatory-supplement.v1.json'),str(R/'delegation/handoff-preparation-parent-dispatch.v1.json'),str(R/'adjudication/root-wp30-cancel-dynamic-read-scope-reception.v1.json'),str(R/'findings.json'),str(R/'evidence/adjudication-inputs/d58a4a288922efd32598eac0ac9a2170d53a42da3e2f311c1e1b39fdd3df883d.json')]
extras=[]
for p in extra_paths:extras.append(dict(identity(ROOT,C,p),purpose='Operative instructions / current scope / mandatory companion',content=git('show',C+':'+p).decode()))
with gzip.open(T/'audit/exact-additional-inputs.json.gz','wb') as f:f.write(json.dumps(extras,ensure_ascii=False,separators=(',',':')).encode())
# Keep complete natural semantic values and vectors without source-code reproduction.
select_common={'facts','fact','fact_chain','sustained_fact','required_premise_and_scope','finite_premises','premises','vectors','ordinary_control','normal_control','minimal_counterexample','finite_counterexample','state_paths','normal_failure_cancel_partial_commit','normal_cancel_failure_partial','cancel_exception_partial_commit','counterarguments','counter_arguments','negative_evidence','preserve_scope','correct_preserve_scope','correct_scope_to_preserve','acceptance','acceptance_and_regression','regression_scope','regression','limits','excluded_claims','no_required_rewrite','source_evidence','spec_evidence','bidirectional_evidence','evidence','supplementary_evidence','full_observable_rule','consumer_reception','source_location_correction','identity_and_history','dual_evidence','premises_and_counterexamples','premises_and_vectors','finite_domain','independent_findings','rebuttal_attempts','selected_canonical_facet','independent_variants','complete_fifteen_reference_entries'}
# These are supporting evidence, not additional changes. Root minimum Chinese rule controls writes.
def stripcode(v):
 if isinstance(v,dict):return {k:stripcode(x) for k,x in v.items() if k not in ['content','text','complete_unit_text','whole_line','exact_text','complete_paragraph','original_record','actual_configuration','requested_configuration']}
 if isinstance(v,list):return [stripcode(x) for x in v]
 return v
records=[]
for rec in d['records']:
 i=rec['id'];a=author[i];c=rec['complete_semantic_contract_received'];bid=byid.get(i);ws=[short[k] for k in a['write_keys']]
 norm={k:stripcode(v) for k,v in c.items() if k in select_common}
 for k in ['counterarguments','counter_arguments','rebuttal_attempts']:norm.pop(k,None)
 if rec['classification']=='optional':norm={k:v for k,v in norm.items() if k in ['source_evidence','spec_evidence','evidence']}
 if 'sections' in c:
  norm['necessary_finite_sections']={k:stripcode(v) for k,v in c['sections'].items() if k.startswith(('3_','4_','5_'))}
 if i=='GR8-PBS-EGGGROUP-DOMAIN-001':norm={k:stripcode(c[k]) for k in ['bidirectional_evidence','premises_and_counterexample','acceptance_and_regression']}
 # COM002/003 split: do not re-assign both facets under one canonical.
 if i in ['GR8-COM-002','GR8-COM-003']:norm={k:stripcode(c[k]) for k in ['selected_canonical_facet','independent_variants','correct_preserve_scope','negative_evidence','acceptance_and_regression']}
 proposer=rec.get('proposer',c.get('proposer',c.get('author',rec.get('root_reception',{}).get('proposer','UNVERIFIED'))))
 if i=='GR8-EXT-CD-004':proposer='external_creature_d actual01a143ad-2f84-71dd-885d-3e43b80e8000'
 counter=rec.get('actual_nonproposer_reviewer',rec.get('actual_independent_counterreviewer',c.get('independent_reviewer','UNVERIFIED')))
 key=rec.get('root_cause_key',c.get('root_cause_key',c.get('root_key',c.get('identity_and_conclusion',{}).get('root_cause_key',i))))
 aliases=rec.get('origin_proposal_id',rec.get('origin_id',c.get('aliases',c.get('identity_and_conclusion',{}).get('aliases',[]))))
 records.append({'id':i,'classification':rec['classification'],'severity':rec.get('severity'),'state':'BOUNDED_PREPARATION_COMPLETE_PENDING_ROOT_CORE_FREEZE','primary_batch':bid,'seven_groups':{
  '1_身份与结论':{'primary':a['primary'],'root_cause_key':key,'canonical_status':'PROVISIONAL_GLOBAL_HISTORY_DEDUP_OPEN','aliases_or_origin':aliases,'root_reason':rec['root_reason'],'history':'原根、别名/撤销和历史资格按完整冻结原记录保留；本任务不增改root分类或旧关闭台账。'},
  '2_双向证据':{'fact_chain':a['fact_chain'],'evidence_ids':[ids[k] for k in record_paths[i]],'fixed_R':REF,'fixed_B8':B,'complete_locator_payload':{'commit':C,'path':str(R/'adjudication/root-decisions.partial.json'),'pointer':'/records/'+str(d['records'].index(rec))},'evidence_levels':['SOURCE_STATIC','DERIVED_VECTOR'],'raw_tool_evidence':'原提出者/非提出者完整工具定位和范围保留于精确原记录及audit/typed-input-graph.json；私有流不称已公开重放。'},
  '3_前提反例及全部路径':{'contract':a['premises_controls_and_prefix'],'supporting_facts_and_vectors':norm,'execution':'NOT_EXECUTED'},
  '4_最小修订合同':{'rule':a['minimum_revision'],'required_target_write_set':ws,'preserve':a['preserve'],'conditional_public_sync':{'writer':'R8-INTEGRATOR','paths':['audit/source-traceability.md','planning/feature-matrix.md'],'activation':'仅最终整合实际需要对应追溯/索引变动时按每项精确贡献登记，不整表重写；各批不直接写公共层。'} if rec['classification']=='required' else None,'read_set':[cache[k] for k in record_paths[i]],'optional_not_selected':rec['classification']=='optional'},
  '5_验收回归':{'criteria':a['acceptance'],'preservation_regression':a['preserve'],'gates':['candidate PASS','actual integrated PASS','ACCEPTED','CLOSED'],'no_forced_new_tests':'以各项root最小裁决为准；已有正确目录不因补例有益而强制增加。'},
  '6_独立裁决':{'original_proposer':proposer,'actual_nonproposer':counter,'root_decider':'/root','root_reason':rec['root_reason'],'full_audit_record':'audit/received-root-records.json.gz#/records/'+str(d['records'].index(rec)),'new_independent_votes':0,'later_revision_review':'必须是实际非作者完整候选及实际整合受影响结果接收；本任务不自签。'},
  '7_依赖接收与关闭':{'direct_semantic_required_ids':[],'transitive_semantic_required_ids':[],'reason':'现有限修订事实无另一个必修编辑先完成的语义前提；共享文件是写冲突，事实/历史/发布接收是关闭门，二者分开。','blocking':['PENDING_ROOT_CORE_FREEZE','root全历史canonical/alias及必要接口最终接收','用户另行手动启动update','实际非作者候选与整合验收及唯一正式接收/关闭'] if bid else ['用户另行选择该optional；未选择不阻塞required'],'nonblocking':['宿主/媒体未知不阻止上述有限静态判定','未来是否兼容源缺陷政策只阻塞实际依赖它的实现选择'],'shared_receivers':a['shared_receivers'],'integrator':'R8-INTEGRATOR','author_entry':('R8-A-'+bid if bid else None),'reviewer_entry':('R8-R-'+bid if bid else None),'closure':'候选PASS不等于actual PASS，后者不等于ACCEPTED/CLOSED；实际范围、共享与历史依赖均接收后由主审负责签收。','excluded_claims':['全局review完成','游戏/参考/模型/宿主/编译通过','optional自动采用','main merge','整改已开始']}}})
required=[x for x in records if x['classification']=='required'];optional=[x for x in records if x['classification']=='optional'];assert len(required)==27 and len(optional)==6
# Exact conflict graph at record level and the chosen grouping. Read/receive edges do not grant a write.
conflicts=[]
for a,b in itertools.combinations(required,2):
 overlap=sorted(set(a['seven_groups']['4_最小修订合同']['required_target_write_set'])&set(b['seven_groups']['4_最小修订合同']['required_target_write_set']))
 if overlap:conflicts.append({'from':a['id'],'to':b['id'],'paths':overlap,'resolution':'same primary batch, one candidate writer; R8-INTEGRATOR sole actual target writer'})
paths=sorted({p for x in required for p in x['seven_groups']['4_最小修订合同']['required_target_write_set']})
for e in conflicts:assert byid[e['from']]==byid[e['to']],e
assignment=[]
for b,(rr,title) in batches.items():
 rs=[x for x in records if x['id'] in rr];wps=sorted({p for x in rs for p in x['seven_groups']['4_最小修订合同']['required_target_write_set']});es=sorted({e for x in rs for e in x['seven_groups']['2_双向证据']['evidence_ids']})
 assignment.append({'id':b,'title':title,'required_ids':rr,'input_contract_commit':C,'R8_core':'PENDING_ROOT_CORE_FREEZE','candidate_mirror_prefix':'review/remediation-eighth-20261016-prepare/candidates/'+b+'/mirror/','candidate_write_set':['review/remediation-eighth-20261016-prepare/candidates/'+b+'/mirror/'+p for p in wps],'actual_target_write_set':wps,'evidence_ids':es,'semantic_predecessor_batches':[],'independence':'候选镜像与其它批隔离；本批实际target整合由R8-INTEGRATOR唯一写。','author':{'logical_entry':'R8-A-'+b,'requested_model':'gpt-6.1-sol','effort':'xhigh','tier':'default','speed':'normal','Fast':'off','actual_task_id':'NOT_STARTED'},'reviewer':{'logical_entry':'R8-R-'+b,'requested_model':'gpt-6.1-sol','effort':'ultra','tier':'default','speed':'normal','Fast':'off','actual_task_id':'NOT_STARTED','independence':'必须实际不同于该批作者，不能改角色名自验。'},'shared_receivers':sorted({y for x in rs for y in x['seven_groups']['7_依赖接收与关闭']['shared_receivers']}),'state':'PLANNED_NOT_STARTED','current_launch_blocker':'PENDING_ROOT_CORE_FREEZE; UPDATE_NOT_STARTED'})
file_graph={'schema':'r8-file-conflicts/v1','record_edges':conflicts,'actual_file_writers':[{'path':p,'candidate_batch':next(b['id'] for b in assignment if p in b['actual_target_write_set']),'actual_writer':'R8-INTEGRATOR'} for p in paths],'conditional_public_writers':[{'path':p,'writer':'R8-INTEGRATOR','reason':'仅对应贡献精确同步；不授权各批整表重写'} for p in ['audit/source-traceability.md','planning/feature-matrix.md']],'inter_batch_actual_path_conflicts':[]}
dep_graph={'schema':'r8-dependency-graph/v1','required_nodes':[x['id'] for x in required],'semantic_edit_edges':[],'closure_edges':[{'from':b['id'],'to':'R8-INTEGRATOR','kind':'candidate+retained-correct-scope+shared-reception','blocking':'actual integration acceptance only'} for b in assignment],'first_wave_after_common_release':[b['id'] for b in assignment],'first_wave_after_common_release_count':len(assignment),'currently_startable':[],'currently_startable_count':0,'common_release':'root冻结最终core并外部发布绑定；用户手动另行启动update。','transitive_closure_edit_edges':[],'policy':'源行为记录所需事实修订可独立；未选兼容政策只阻塞实际依赖它的实现范围。'}
jwrite(H/'batch-assignment.json',{'schema':'r8-batches/v1','batches':assignment,'one_required_one_primary':True,'update_started':False});jwrite(H/'dependency-graph.json',dep_graph);jwrite(H/'file-conflict-graph.json',file_graph)
# Preserve no-required and binary negatives as separate populations, never count in 33.
no_sources=['root-hash-default-scope-counterreview.v1.json','root-after-all-hits-reception.v1.json','root-recorded-scalar-reception.v1.json','root-gr8-ecb-001-reception.v1.json','root-gr8-ecb-002-reception.v1.json','root-xpcb001-already-documented-counterreview.v1.json','root-cd001-nonpositive-selector-counterreview.v1.json','root-wp30-cancel-dynamic-read-scope-reception.v1.json']
negative=[{'id':i,'classification':'NO_REQUIRED_BOUNDED_SCOPE','formal_write_set':[],'complete_received_root_receipt':json.loads((R/'adjudication'/p).read_text())} for i,p in zip(['GR8-KAR-001','GR8-CAR-CAND-004','GR8-FAC-001','GR8-ECB-001','GR8-ECB-002','GR8-XPCB-001','GR8-EXT-CD-001','CREC-WP30-CANCEL-DYNAMIC-READ-SCOPE'],no_sources)]
binary=json.loads((R/'adjudication/root-binary-bounded-receptions.json').read_text())['records']
rejected=json.loads((R/'adjudication/root-ui002-reception.json').read_text())
manifest={'schema':'gr8-bounded-handoff-preparation/v1','language':'zh-CN','status':'BOUNDED_PREPARATION_COMPLETE_PENDING_ROOT_CORE_FREEZE','input_contract_commit':C,'original_root_input':'c44afe8bfa10ce91e1d55b88f7064918e5bd2510','original_root_tree':'4c0e8484120d4b6c6cfe7750f1036ba9e9cc0068','B8':{'commit':B,'tree':git('rev-parse',B+'^{tree}').decode().strip(),'formal_tree':git('rev-parse',B+':deliverables/final-specification-set').decode().strip(),'formal_files':131},'R':{'commit':REF,'tree':git('rev-parse',REF+'^{tree}',repo=S).decode().strip(),'tracked_files':len(git('ls-tree','-r','--name-only',REF,repo=S).splitlines())},'R8_core':{'state':'PENDING_ROOT_CORE_FREEZE','commit':None,'tree':None,'publication_binding':'由外部后继固定入口实际绑定，本WIP输入commit不作最终core。'},'local_mapping':{'clean_repo':ROOT,'reference_repo':S,'original_Mac_paths':'输入来源导航；不假定云端具同名路径'},'protection':'仅'+str(T)+'/可写；R/正式/planning/audit/旧报告/main/tag/他人任务目录只读。','records':records,'bounded_counts':{'records':33,'required':27,'P2':2,'P3':25,'optional':6,'separate_no_required':8,'separate_binary_negative':4,'rejected_original_ui002':1},'count_qualification':d['counts_qualification'],'separate_no_required':negative,'separate_binary_negative':binary,'separate_rejected':rejected,'batch_assignment':assignment,'dependency_graph':dep_graph,'file_conflict_graph':file_graph,'input_payloads':json.loads((T/'reading-ledger/input-identities.json').read_text()),'source_spec_payloads':json.loads((T/'reading-ledger/source-spec-identities.json').read_text()),'history':'R1原WP不造总数；R2 229/21/341；R3 23/76；R4当前17/76与B5时16/75分时；R5 92/51P2/41P3与nonmandatory分列；R6 56/14及110边/100节点有限；R7 27/13、13作者17候选12实际=42、33改变98未变仅旧有限资格。全部原alias/撤销/FAIL/WAIT保留，不继承全局PASS。','execution':{'this_context_business_vectors':'NOT_EXECUTED','reference_Ruby_game':'NOT_EXECUTED','host_demo_media':'NOT_EXECUTED','compiler':'NOT_EXECUTED','independent_behavior_model':'NOT_EXECUTED','real_save_replay':'NOT_EXECUTED','received_numeric_increment':json.loads((R/'adjudication/root-growth-numeric-execution-increment-reception.v1.json').read_text()),'global_execution_registry':json.loads((R/'coverage/root-execution-increment-registry.v1.json').read_text()),'tool_validation':'Git完整字节身份、schema/图/ID一致性及报告远端传输；不授语义/行为信用。'},'evidence_corrections':{'shop':json.loads((R/'adjudication/root-shop-fact-corrections-reception.v1.json').read_text()),'COM008':'136–278完整组合，原136–277保留；unit6补件强制','EggGroup':'compile generic4–68；原4–67载荷保留；无新增发现/审者'},'open_parent_receptions':['最终R8语义core未冻结','全历史canonical/alias/等价目录与当前effective qualifications未最终接收','39基础接口+2CP后继facet及同ID IF09按pointer区别；root最终全接口接收未签','原始全域source/formal双向阅读分母及任务最终接收OPEN，不能由318/96机械并集授FULL','额外待决CP002/历史颜色根关系/N01导航等不在本33有限分类内，不自动加为必修','全局执行完整分类总表OPEN；数学新增1不是游戏/模型运行'], 'limits':['L01–L14材料/媒体/宿主/native/backend/动态扩展/外部服务等保原有限边界；实际可审未读/未接另列，不能改作limit。'],'launch_methods':{'logical_entries':'R8-A-<batch>/R8-R-<batch>/R8-INTEGRATOR','CLI':'UNVERIFIED_NOT_TESTED','Desktop':'UNVERIFIED_NOT_TESTED','live_platform_logs':'UNVERIFIED；未启动，无任务ID/实时日志可造。','static_log_method':'对本包JSON可用python解析；后续真实任务须登记平台ID、准确日志位置与进度。'},'qualification':{'requested':{'model':'gpt-6.1-sol','effort':'ultra','tier':'default','speed':'normal','Fast':'off'},'actual':{k:'UNVERIFIED' for k in ['model','effort','tier','speed','Fast','opaque_platform_id']},'new_spawned_agents':0,'new_independent_votes':0,'self_acceptance':False},'update_started':False,'final_marker':'UPDATE_NOT_STARTED'}
manifest['additional_payloads']=[{k:v for k,v in x.items() if k!='content'} for x in extras]
manifest['current_historical_overlay_binding']={'U06_actual_result':'55a843b3ab01d26442f604770f30932e120f923b','same_reviewer':'01a1401c-1527-75c6-9a36-7bc9b3a00007','source':identity(ROOT,B,'review/remediation-seventh-20261015-prepare/ledger.json'),'pointer':'/batches/5/actual_integration_review_commit'}
jwrite(H/'cloud-eighth-update-handoff-manifest.json',manifest)
jwrite(H/'contracts.zh.json',records)
# Human readable standalone prompt: all 33 records + full evidence/vector data; no future self hash.
intro=f'''# 第八轮完整中文整改交接：有限已裁定合同准备版\n\n状态：PENDING_ROOT_CORE_FREEZE。UPDATE_NOT_STARTED，update_started:false。本包具体化当前33项有限分类（27必修：2P2/25P3；6可选），并分别保留8有限不必修、4binary负例与1已驳回原UI002。此数不是全轮最终总数。根最终签收由主审完成。\n\n本提示词只供用户在root最终冻结与后继发布绑定后另行手动委派整改。现在不得以WIP输入冒最终core或开始update。固定合同提交{C}；原root输入c44afe8bfa10ce91e1d55b88f7064918e5bd2510/tree4c0e8484120d4b6c6cfe7750f1036ba9e9cc0068。B8={B}，workspace tree751dfde81048c81390f89a65ca1d1a565ba8e1ca，formal treef292698cdd4a8e725525a9be6dc34b75faaf151e；R={REF}/tree7589c800b61ba13a13040ed0d686979b80a84fd0。云端项目{ROOT}，只读R {S}。原Mac路径仅是输入来源导航。\n\n范围只修改下列每项已裁定最小规格；参考只读、不开发框架、不合并main、不强推。不因补例有益就强制新测试，不自动采用optional或选择缺陷兼容政策。使用clean-document-revision：错误原位替换、必要缺项补齐、保留正确范围；正文只保正确行为，原提案/反证/撤销留审计。不得把Ruby类/方法组织或源码搬入未来规格。\n\n作者请求gpt-6.1-sol/xhigh，实际非作者reviewer请求gpt-6.1-sol/ultra，均default普速/Fast off；实际model/effort/tier/speed/Fast/UUID无权威回显逐项UNVERIFIED。逻辑入口、候选镜像和最终target在每批合同内；CLI/Desktop未实际测试，均UNVERIFIED，不编造可用命令/任务ID。\n\n全部业务/参考游戏/宿主/编译/独立行为模型/向量在本准备context均NOT_EXECUTED。已接收的PC-EXEC-GROWTH-MATH-01新增1为Python数值表达式替身过程，600表值+2断言、exit0；不是Ruby/API/游戏/状态模型、也不重跑。全局执行分类总表仍OPEN。L01–L14保持材料/宿主边界，真实未读/未接不得转为limit。\n\n候选PASS、actual整合PASS、ACCEPTED、CLOSED是四个门。全部正式target及公共audit/planning索引由R8-INTEGRATOR唯一写者逐贡献整合；候选作者只写隔离mirror，不写共享target。非作者须实读最终整合受影响全文与累计保留；依赖/policy仅阻对应范围。各项source/spec父身份及行/字段/工具定位随附，哈希、库存、旧PASS不替语义实读。\n\n发布门：root先冻结最终语义core commit/tree；外部后继入口绑定真实core及本包载荷。本文与manifest不含自身未来commit/tree；普通push后完整隔离远端逐文件核mode/blob/bytes/SHA/集合/tree。当前root历史/接口/全域最终接收仍OPEN，不能把本有限准备或传输成功称全局PASS。\n\n## 第一波与唯一主批次\n\n共同release满足后，以下9批候选镜像可彼此独立准备；9为逻辑数量，不是服务slots或已启动数。当前release未满足，实际可启动0、已启动0。批内共享文件归同一候选writer；正式整合另由R8-INTEGRATOR顺序接收。\n\n'''
for b in assignment:intro+=f"- {b['id']}：{b['title']}；"+'、'.join(b['required_ids'])+'。\n'

def render(rec):
 g=rec['seven_groups'];s=f"\n## {rec['id']} — {rec['classification']} / {rec['severity'] or '无必修级别'}\n\n"
 for key,val in g.items():s+='### '+key+'\n\n'+json.dumps(val,ensure_ascii=False,indent=2)+'\n\n'
 return s
prompt=intro+'\n## 全部有限规范记录\n'+''.join(render(x) for x in records)
# Full separate dispositions remain semantically recoverable rather than link-only.
prompt+='\n## 八项有限不必修及四项binary负例\n\n这些记录正式写集均为空，不进入27必修；不把“可补联合例”当作缺必要规则。\n\n'+json.dumps(stripcode({'no_required':negative,'binary_negative':binary}),ensure_ascii=False,indent=2)+'\n\n## 原UI002驳回\n\n标准Ruby3.1的nil &值为false，原NoMethodError构造/换肤反例及其衍生取消/清理结论撤回；不计required/optional，不自动换成其它显示缺项。\n\n## 仍待root最终接收\n\n'+'\n'.join('- '+x for x in manifest['open_parent_receptions'])+'\n\nUPDATE_NOT_STARTED\n'
(H/'cloud-eighth-update-handoff-prompt.md').write_text(prompt)
for b in assignment:
 p=H/'batches'/b['id'];p.mkdir(parents=True,exist_ok=True)
 es=[e for e in manifest['source_spec_payloads']['files'] if e['evidence_id'] in b['evidence_ids']]
 # Complete batch text, frozen readset, and no missing linked normative records.
 (p/'prompt.md').write_text(intro+'\n## 本批独占合同\n\n'+json.dumps(b,ensure_ascii=False,indent=2)+'\n'+''.join(render(x) for x in records if x['id'] in b['required_ids'])+'\nUPDATE_NOT_STARTED\n')
 jwrite(p/'readset.json',{'schema':'r8-batch-complete-readset/v1','contract_commit':C,'B8':B,'R':REF,'report_root':str(R),'R8_core':'PENDING_ROOT_CORE_FREEZE','source_spec_files':es,'mandatory_root_input':manifest['input_payloads'],'additional_mandatory_companions':manifest['additional_payloads'],'records':[x for x in records if x['id'] in b['required_ids']],'read_requirement':'每个当前有效唯一语义值实读；重复精确payload可typed-purpose去重。先核identity不授FULL；必要所有当前/历史接口closure仍待root。','update_started':False})
# External input evidence reading does not claim parent authorship or task-wide acceptance.
ledger=json.loads((T/'reading-ledger/input-identities.json').read_text())
for x in ledger:x['semantic_status']='RECEIVED_FOR_BOUNDED_HANDOFF';x['reading_method']='完整JSON结构、当前33合同七组及反证语义接收；重复值按typed graph去重；身份/导航字段机械核验；原source FULL归原实际reader，不授新全系统审读。'
jwrite(T/'reading-ledger/input-identities.json',ledger)
jwrite(T/'qualification.json',{'schema':'r8-handoff-preparer-qualification/v1','contract_commit':C,'requested':manifest['qualification']['requested'],'actual':manifest['qualification']['actual'],'user_prohibited_spawn':True,'new_agents':0,'new_votes':0,'independent_revision_acceptance':'NOT_EXECUTED','source_formal_main_changed':False,'update_started':False,'core':'PENDING_ROOT_CORE_FREEZE'})
# Intermediate reading projections are evidence of typed reading, archived without proliferating code copies.
archive=T/'audit/reading-projections.json.gz'
projections=json.loads(gzip.decompress(archive.read_bytes())) if archive.exists() else {}
projections.update({p.name:p.read_text() for p in (T/'reading-ledger').iterdir() if p.suffix=='.txt' or (p.name.startswith('record-') and p.suffix=='.json')})
with gzip.open(T/'audit/reading-projections.json.gz','wb') as f:f.write(json.dumps(projections,ensure_ascii=False,separators=(',',':')).encode())
for p in (T/'reading-ledger').iterdir():
 if p.name in projections:p.unlink()
print(json.dumps({'records':33,'required':27,'optional':6,'batches':len(assignment),'source_spec_identities':len(cache),'unresolved_spellings':missing,'formal_targets':len(paths),'conflict_edges':len(conflicts),'prompt_bytes':len(prompt.encode())},ensure_ascii=False))
