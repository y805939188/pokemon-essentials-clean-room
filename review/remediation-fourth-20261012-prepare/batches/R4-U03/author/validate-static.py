import pathlib, json, subprocess, hashlib, re, os, datetime, sys
repo=pathlib.Path(os.environ.get('R4_U03_WORKTREE', '/workspace/r4-u03-author'))
os.chdir(repo)
root=pathlib.Path('review/remediation-fourth-20261012-prepare')
task=root/'tasks/R4-U03'; out=root/'batches/R4-U03/author'
B='1f36475d22120a0d1175967d5b17d71fe8311d88'; START='08a57fb55118914a74ac1ffaf617647c01df8938'; PUB='2b60c7bd0dce8d972e34a9d86a8f6cf6a3b1dd65'; REVIEW='130452d902530140331c21064a3188b7887f72ae'; R='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
F='deliverables/final-specification-set/'
contract=json.loads((task/'batch-contract.json').read_text());scope=json.loads((task/'read-scope.json').read_text());findings=json.loads((task/'findings-input.json').read_text())
def git(*a,cwd=None):return subprocess.check_output(['git',*a],cwd=cwd)
def show(c,p,source=False):return git('show',c+':'+p,cwd='/tmp/r4-u03-reference.git' if source else None)
def ident(b):return {'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'git_blob':hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()}
def dump(name,x): (out/name).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def loc(path,needle):
 ls=pathlib.Path(path).read_text().splitlines();ns=[i+1 for i,s in enumerate(ls) if needle in s];assert ns,(path,needle);return {'path':path,'lines':ns,'needle':needle}
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
read_records=[]
for typ,es in [('SOURCE_STATIC',scope['source']),('SPEC_STATIC',scope['formal_anchors'])]:
 for e in es:
  b=show(e['commit'],e['path'],typ=='SOURCE_STATIC');assert ident(b)==e['identity'];read_records.append(dict(e,evidence_level=typ,full_bytes_verified=True))
a=findings['authority'];d=json.loads(show(a['commit'],a['path']));selected={x['id']:x for x in d['findings'] if x['id'] in contract['finding_ids']};assert all(e==selected[e['id']] for e in findings['canonical_root_records'])
values=[]
def walk(x):
 values.append(x)
 if isinstance(x,dict):
  for v in x.values():walk(v)
 elif isinstance(x,list):
  for v in x:walk(v)
walk(findings['canonical_root_records'])
handoff=(task/'handoff-findings.md').read_text(); blocks=[json.loads(x) for x in re.findall(r'```json\n(.*?)\n```',handoff,re.S)];assert len(blocks)==46 and all(x in values for x in blocks)
ids=json.loads((root/'task-file-identities.json').read_text())['records'];task_inputs=[]
for e in ids:
 if e['path'].startswith(str(task)+'/') or e['path'] in [str(root/x) for x in ['README.md','input-verification.json','resource-scope.json','dispatch-plan.json']]:
  b=show(START,e['path']);assert ident(b)=={k:e[k] for k in ['bytes','sha256','git_blob']};assert pathlib.Path(e['path']).read_bytes()==b;task_inputs.append(dict(e,full_bytes_verified=True))
prep=json.loads((root/'input-verification.json').read_text());bindings=[]
for e in prep['external_bindings']:
 b=show(e['commit'],e['path']);assert ident(b)=={k:e[k] for k in ['bytes','sha256','git_blob']};bindings.append(dict(e,full_bytes_verified=True))
freeze=json.loads(show(PUB,str(root/'freeze-and-publication.json')));assert freeze['author_start_commit']==START;assert freeze['task_package_tree']==git('rev-parse',START+'^{tree}').decode().strip()
assert git('rev-parse',R+'^{tree}',cwd='/tmp/r4-u03-reference.git').decode().strip()==freeze['reference_tree']
assert git('rev-parse',REVIEW+'^{tree}').decode().strip()==freeze['fixed_review_publication']['tree']
assert not git('diff','--name-only',B,START,'--',F)
main=git('ls-remote','origin','refs/heads/main').decode().split()[0];assert main==B
allowed=set(contract['allowed_formal_write_paths']);changed=set(git('diff','--name-only',START).decode().splitlines());assert {p for p in changed if p.startswith(F)}==allowed;assert all(p in allowed or p.startswith(str(out)+'/') for p in changed)
tracked=git('ls-tree','-r','--name-only',START).decode().splitlines(); applicable=[p for p in tracked if p.endswith('AGENTS.md') and any(w==p[:-9] or w.startswith(p[:-9]) for w in allowed|{str(out)+'/x'})]
assert applicable==['AGENTS.md'];ag=show(START,'AGENTS.md');assert pathlib.Path('AGENTS.md').read_bytes()==ag
sets={k['batch']:[] for k in json.loads((root/'dispatch-plan.json').read_text())['shared_owners']['formal_writers']}
for e in json.loads((root/'dispatch-plan.json').read_text())['shared_owners']['formal_writers']:sets[e['batch']].append(e['path'])
assert sum(map(len,sets.values()))==28 and len({p for xs in sets.values() for p in xs})==28
# Structural checks: compare documented data to fixed source data; no function/model/UI execution.
battle=F+'user-interface/wp67-a-battle-interaction-and-presentation.md';st=show(R,'Data/Scripts/011_Battle/004_Scene/004_Scene_PlayAnimations.rb',True).decode()
source_table={}
for line in st.splitlines():
 m=re.match(r'\s*:([A-Z]+)\s*=> \[(.*?)\],?$',line)
 if m:source_table[m[1]]=[None if x.strip()=='nil' else x.strip().lstrip(':') for x in m[2].split(',')]
spec_table={}
for line in pathlib.Path(battle).read_text().splitlines():
 cells=[x.strip() for x in line.split('|')[1:-1]]
 if len(cells)==7 and cells[0] in source_table:spec_table[cells[0]]=[None if x=='空' else x for x in cells[1:]]
assert len(source_table)==18 and source_table==spec_table and all(len(x)==6 for x in spec_table.values())
cat1=F+'test-catalog/pokemon-rules-wp19-21-22-23-34.md';cat2=F+'test-catalog/pokemon-rules-wp53-60-61-62-69-70.md';catui=F+'test-catalog/user-interface-wp17-63-65-66-67-68-69-70-71.md'
series={'IF':(cat1,6),'IV':(cat1,4),'CM':(catui,4),'NM':(catui,4),'SK':(catui,6),'WR':(catui,6),'AN':(catui,6),'DX':(catui,5),'PD':(cat2,5)};vectors=[]
for prefix,(path,count) in series.items():
 s=pathlib.Path(path).read_text();assert 'NOT_EXECUTED' in s
 for i in range(1,count+1):
  vid=f'R4-{prefix}{i:02}';rows=[(n+1,l) for n,l in enumerate(s.splitlines()) if l.startswith('| '+vid+' |')];assert len(rows)==1
  vectors.append({'id':vid,'path':path,'line':rows[0][0],'full_row':rows[0][1],'evidence_level':'DERIVED_VECTOR','execution_status':'NOT_EXECUTED'})
assert len(vectors)==46
# Retain existing correct clauses in changed test catalogs; BR18 alone is deliberately replaced.
for p in [cat1,cat2,catui]:
 before=show(B,p).decode().splitlines();after=pathlib.Path(p).read_text().splitlines();it=iter(after)
 for l in before:
  if p==cat1 and l.startswith('| BR18 |'):continue
  assert any(z==l for z in it),(p,l)
protected=['creature-rpg/wp35-eggs-and-hatching.md','pokemon-rules/wp34-inheritance-and-offspring.md','test-catalog/creature-rpg-wp35-36-57-64-68.md','creature-rpg/wp20-hp-status-moves-helditem.md','user-interface/wp66-c-bag-item-storage-and-shop-ui.md','user-interface/wp65-title-load-options-pause-and-pc.md','engine-overworld/wp13-interpreter-command-matrix.md','generic-kernel/wp02-rule-configuration-and-data-variants.md','demo-dx/wp74-battle-animation-authoring-and-exchange.md','generic-kernel/wp03-content-identity-and-schema.md']
protection=[]
for p in [F+x for x in protected]+['CURRENT-DELIVERY.md']:
 b=show(B,p);assert pathlib.Path(p).read_bytes()==b;protection.append({'path':p,**ident(b),'same_complete_bytes_as_B':True})
assert not git('diff',START,'--','delivery','reference',str(root/'registration'),str(task),'review/global-independent-review')
subprocess.run(['git','diff','--check',START,'--',F],check=True)
contexts=[
 {'finding':'GR4-M04-001','source_ranges_added':['Pokemon.rb 159–184','Pokedex_Entry.rb 446–475 (shared selector boundary)'],'consumer_read':['WP18 §3.4','WP15 §4.1','WP21 §3.2-R03/§3.4/§4','WP35 §5.2/§9','EG-13/20','U03-SP01–10'],'assessment':'Correct simplified species-data read is distinct from per-creature image form evaluation; hatching and SPINDA controls retain original qualifications.'},
 {'finding':'GR4-M06-001','consumer_read':['WP34 §7','WP20 §6.1–6.3','BR16–19'],'assessment':'Two slots occupied by different Power identities cannot also hold Knot; no change to correct primary rule.'},
 {'finding':'GR4-M10-001','source_ranges_added':['011_Messages.rb 56–160 parameter defaults'],'consumer_read':['WP65 §7 PC','WP13 command103','WP66-C §5.1','MG12–20','B04-M07–09','U05-QN01–04','U05-TX01–04'],'assessment':'Command cancel first and numeric edit/use first are distinct from quantity/shop and cursor-naming controls; event default cancel is initial value.'},
 {'finding':'GR4-M10-002','consumer_read':['WP02 skin list config','WP65 §5.2 options','WP17 §3.1/3.4','WP15 §3.1/5.1'],'assessment':'Cold/default logical result distinct from explicit empty and single-window update; no old-image/failure pixels asserted.'},
 {'finding':'GR4-M10-003','source_ranges_added':['010_DrawText.rb 105–127,206–215,580–610','006_UI_Summary.rb 630–640'],'consumer_read':['WP17 tags §3/§6','WP17 §3.3','WP66-A §5.2','DT04/08','B04-M14'],'assessment':'Word boundary, two measurement units and content gate are explicit; localization substitution is a separate upstream scope.'},
 {'finding':'GR4-M10-004','consumer_read':['WP67-A §9.4','WP74 §15','WP03 non-registry products','K35/36'],'assessment':'All108 cells match fixed identity data; raw category/target, candidate registration and mapping separated from animation collection/media; exact-hit offsets retained.'},
 {'finding':'GR4-M11-001','source_ranges_added':['Pokedex_Entry.rb 446–475 selector','PBS/pokemon_forms.txt 74–90 RATTATA1'],'consumer_read':['WP62 §2/§3/§4/§6','WP66-B §6/§7','WP15 §4.1','PD03–05/19/31–34','B30/33/38','U05-HAB01–04'],'assessment':'Saved shiny is not passed through dex images; normal refresh does not write it. Multi-option independent selector fixture is lawful; legacy habitat contract untouched.'}
]
# Criterion maps retain complete fixed criterion text; all are author assessments pending independent review.
mapping={
'GR4-M04-001': [('creature-rpg/wp18-creature-identity-species-ownership.md','按个体取正面'),('pokemon-rules/wp21-dynamic-forms-and-display.md','t+432001'),('engine-overworld/wp15-resource-matching-and-audio.md','资源未命中不会撤销')],
'GR4-M06-001': [('test-catalog/pokemon-rules-wp19-21-22-23-34.md','| BR18 |'),('test-catalog/pokemon-rules-wp19-21-22-23-34.md','## R4-IV')],
'GR4-M10-001': [('user-interface/wp17-messages-windows-input.md','### 4.1'),('user-interface/wp17-messages-windows-input.md','### 5.4')],
'GR4-M10-002': [('engine-overworld/wp15-resource-matching-and-audio.md','### 3.3'),('user-interface/wp17-messages-windows-input.md','- 皮肤：')],
'GR4-M10-003': [('user-interface/wp17-draw-text-tags.md','### 3.1'),('user-interface/wp17-messages-windows-input.md','自动宽度换行'),('user-interface/wp66-a-party-and-summary-ui.md','宽268')],
'GR4-M10-004': [('user-interface/wp67-a-battle-interaction-and-presentation.md','### 9.4.1'),('user-interface/wp67-a-battle-interaction-and-presentation.md','精确命中编号')],
'GR4-M11-001': [('pokemon-rules/wp62-pokedex-records-regions-and-content.md','**记录与图像请求分开**'),('user-interface/wp66-b-storage-and-pokedex-ui.md','固定请求普通外观')]
}
prefix_map={'GR4-M04-001':['IF'],'GR4-M06-001':['IV'],'GR4-M10-001':['CM','NM'],'GR4-M10-002':['SK'],'GR4-M10-003':['WR'],'GR4-M10-004':['AN'],'GR4-M11-001':['PD','DX']}
rationales={
'GR4-M04-001':['WP18不再把图像统一归简化；显式数值形态入口和个体入口有明确分界。','IF01/02给严格五天差异；IF03/04分别守卫与强制0不提交。','WP15说明求值先于资源；IF06不依赖显示成功且不回滚。','本更新没有参考／宿主执行，任何未来执行须另立回执。','WP35及EG-13/20完整字节保留；IF05限定参数已给定，不推整链纯读。'],
'GR4-M06-001':['BR18仅固定2+随机1；IV01区分值总3。','IV02明确单Knot+单Power且世代8，固定1+随机4。','IV04同Power只计一次；WP20/34未修改。','本更新未执行繁育函数／模型／宿主。'],
'GR4-M10-001':['CM01/02与NM01/03唯一确定可取消／不可取消、合法／越界出口。','CM03/NM01单键，NM02/03编辑和越界同轮例均NOT_EXECUTED。','U05-QN和B04-M07–09原行顺序／完整内容保留。','查询真值夹具不证明物理键；未执行宿主UI。','NM04事件一位初1默认取消1，同轮确认2写变量，单BACK写1。'],
'GR4-M10-002':['SK01–04给选项／系统／两个备用／全缺五分支。','SK02冷Missing得Custom；SK05显式完整Missing后空，均未执行。','SK06与WP17原空标签保留；单窗失败不推统一画面。'],
'GR4-M10-003':['绘制附表用词边界和行首不硬拆的行为文字。','WR01–04明确测量假定、AB/A B/显式/pg各逻辑行，未运行字体。','主文和摘要只消费布局，未保证超宽字形全可见。','附表预留2单位与非行首/内容门，WR05宽22/21，普通起点0。'],
'GR4-M10-004':['18×6表全部108格，包括空格，与固定源数据逐字身份核对。','AN01–04给10→20→30→空及对方11／10，NOT_EXECUTED。','精确映射hitNum与默认不偏移，资格／映射／数据库／媒体分层；AN06不是播放验证。'],
'GR4-M11-001':['DX01–03/PD01–02与主文列出主预览、完整Info/Forms前后/图标、摘要单种、简略Info。','普通刷新保持原true/false，与DX05选择器首轮另写false分开。','PD01/03、DX01/04分别成对与仅异色资格；普通固定输入不归因资源回退。','WP15通用按属性规则原范围保留；图鉴合同不推广到个体外观，新增设计未执行。','无媒体／宿主不阻塞静态修订；未来执行须另有相异素材和输入输出。','DX05/PD05独立RATTATA两项夹具；单项BULBASAUR不证明首轮写入。']}
accept=[]
for e in findings['canonical_root_records']:
 ps=prefix_map[e['id']];vs=[v for v in vectors if any(v['id'].startswith('R4-'+p) for p in ps)];criteria=[]
 assert len(e['acceptance_criteria'])==len(rationales[e['id']])
 for i,(criterion,reason) in enumerate(zip(e['acceptance_criteria'],rationales[e['id']])):
  criteria.append({'criterion_number':i+1,**criterion,'author_assessment':'AUTHOR_STATIC_CHECKED' if 'RUNTIME' not in criterion['kind'].upper() and 'EXECUTED_HOST' not in criterion['kind'].upper() else 'NOT_EXECUTED_THIS_UPDATE_RUNTIME_OPTIONAL','mapping_reason':reason,'formal_locations':[loc(F+p,n) for p,n in mapping[e['id']]],'vector_ids':[v['id'] for v in vs]})
 accept.append({'finding':e['id'],'criterion_count':len(criteria),'preconditions':e['preconditions'],'minimal_counterexample':e['minimal_counterexample'],'normal_case':e['normal_case'],'boundary_case':e['failure_or_boundary_case'],'counterreview_refinements':e['review_resolution']['independent_counterreview']['required_refinements'],'criteria':criteria,'independent_review':'PENDING_PARENT_ASSIGNED_REVIEWER','acceptance_registration':'NOT_PERFORMED','unknowns':e['unknowns']})
reportroot='review/global-independent-review/fourth-2026-10-12-1f36475-c92e/'
old=json.loads(show(REVIEW,reportroot+'regression-third-23.json'));affected_gr3=[e for e in old['records'] if e['id'] in ['GR3-M04-001','GR3-M06-001','GR3-M10-002','GR3-M11-001']]
legacy=json.loads(show(REVIEW,reportroot+'regression-legacy-scope.json'))
execs=json.loads(show(REVIEW,reportroot+'execution-evidence.json'));historical=[]
for e in execs['records']:
 if e.get('evidence_level')=='EXECUTED_REFERENCE':
  y=e['record'];historical.append({'origin_module':e['origin_module'],'artifact':e['artifact'],'pointer':e['pointer'],'command':y.get('command'),'execution_id':y.get('id',y.get('execution_id')),'exit_code':y['exit_code'],'limits':y.get('limits',y.get('limitations')),'aggregation_is_not_a_rerun':True})
assert len(historical)==4
formal_ids=[{'path':p,**ident(pathlib.Path(p).read_bytes()),'whole_file_bytes_read':True} for p in sorted(allowed)]
checks={'status':'TOOL_VALIDATION_COMPLETED','at':now,'command':'python /tmp/r4-u03-build-evidence.py (same complete script preserved as author/validate-static.py; read-only Git/source/document checks; own evidence only)', 'validator_artifact_identity':ident(pathlib.Path(__file__).read_bytes()),'python':sys.version,'formal_paths':12,'changed_path_allowlist':'MATCHES_ALL_12_ALLOWED_FORMAL_PATHS','all108_animation_identity_cells_match_fixed_R':True,'new_derived_vector_ids':46,'all_vectors_NOT_EXECUTED':True,'original_catalog_lines_preserved_except_BR18':True,'protected_complete_file_identity_count':len(protection),'protected_files':protection,'git_diff_check_exit_code':0,'git_diff_check_scope':'formal files; all staged files checked again at publication gate','not_a_behavior_test':True,'source_functions_executed':0,'model_executed':0,'host_or_demo_executed':0,'formal_identities':formal_ids}
dump('input-bindings.json',{'role':'R4-U03-author','task_id':'R4-U03','author_thread_id':os.environ.get('CODEX_THREAD_ID'),'source_thread_id':'01a10d94-84b9-759e-aa1d-edb0d9b6d0e2','requested_model':{'model':'gpt-6.1-sol','reasoning_effort':'xhigh','service_tier':'default','Fast':False},'actual_echo':'UNVERIFIED','skills':'No additional skill applies to this repository-scoped specification task; AGENTS.md governs. Visible fixed context is complete.','applicable_agents':[{'path':'AGENTS.md',**ident(ag)}],'worktree':str(repo),'branch':git('branch','--show-current').decode().strip(),'author_start':{'commit':START,'tree':freeze['author_start_tree']},'publication_receipt_input':{'commit':PUB,'path':str(root/'freeze-and-publication.json'),**ident(show(PUB,str(root/'freeze-and-publication.json')))},'formal_baseline':{'commit':B,'tree':freeze['formal_input_tree']},'reference_baseline':{'commit':R,'tree':freeze['reference_tree'],'object_store':'/tmp/r4-u03-reference.git','working_reference_modified':False},'fixed_review':freeze['fixed_review_publication'],'complete_canonical_records_match':True,'handoff46_json_projections_match':True,'root_files_fully_parsed_and_task_inputs_fully_read':True,'task_inputs':task_inputs,'fixed_external_bindings':bindings,'B_to_author_start_formal_drift':'NONE','remote_main_observed':main,'global_28_write_domains_disjoint_metadata_check':True,'no_global_semantic_review_repeated':True})
dump('source-and-consumer-reading.json',{'evidence_levels':['SOURCE_STATIC','SPEC_STATIC'],'source_records':read_records,'actual_read_contexts':contexts,'read_extra_range_rule':'Only necessary ranges of listed source paths and shared formal consumers; no reference function loaded or called.'})
dump('acceptance-map.json',{'status':'AUTHOR_READY_FOR_INDEPENDENT_CANDIDATE_REVIEW','finding_count':7,'criteria_count':sum(e['criterion_count'] for e in accept),'not_independent_PASS':True,'records':accept})
dump('derived-vectors.json',{'count':len(vectors),'evidence_level':'DERIVED_VECTOR','execution_status':'NOT_EXECUTED_THIS_UPDATE','records':vectors})
dump('affected-regression.json',{'status':'AUTHOR_SCOPED_STATIC_REGRESSION_CHECKED','protected_files':protection,'affected_current_controls':[{'id':'WP35/EG-13/20','result':'Original complete bytes unchanged; core/presentation dynamic form split retained.'},{'id':'WP34 §7/BR16/17/19','result':'Correct3/5 and samePower-once clauses retained; onlyBR18 changed.'},{'id':'U05-QN01–04/B04-M07–09/U05-TX01–04','result':'Original rows preserved in order; numeric command consumer added without unifying priorities.'},{'id':'DT04/08/B04-M14','result':'Explicit alignment/newline/pg/pause contracts retained; new width threshold does not assert host pixels.'},{'id':'K35/36/WP74 §15/WP03','result':'Animation switch/absence, naming compiler and products remain; complete identity data added in playback consumer.'},{'id':'PD03–05/19/31–34/B30/33/38/U05-HAB01–04','result':'Original record, form qualification, selector writes and habitat mask rows unchanged; image request documented separately.'}], 'history_links':contract['regression_scope'],'GR3_fixed_review_records':affected_gr3,'legacy_navigation':json.loads((task/'legacy-navigation.json').read_text()),'original229_A053':[e for e in legacy['original229'] if e['id']=='GIR-FD82-A053'],'exact341_A053':[e for e in legacy['exact341'] if e['record_key']=='B08/GIR-FD82-A053'],'all_other229_341':'historical_qualified_evidence_reused/not_reexecuted; no scope expansion or new signoff','GR3_CLOSED':'Original historical status retained; this author does not register closure or actual acceptance.'})
dump('execution.json',{'status':'NOT_EXECUTED_THIS_UPDATE','new_reference_execution':0,'new_model_execution':0,'new_host_or_demo_execution':0,'static_vectors':46,'tool_validation':'static-validation.json','historical_GR4_reference_execution_receipt':{'commit':REVIEW,'path':reportroot+'execution-evidence.json',**ident(show(REVIEW,reportroot+'execution-evidence.json')),'records':historical},'historical_scope':'Four isolated original-function executions retain true attribution, including caught exceptions. Not this batch, not rerun, not full host/Demo PASS. Prior legacy execution states unchanged.','recoverable_attempts':['Initial local fixed-package path missing: recovered with exact-SHA fetch.','Two apply_patch context/order verification failures changed no files; corrected and reapplied atomically.','Fixed historical report object not materialized initially: recovered with exact review SHA fetch.','Staged diff check exit2 flagged context spaces inside the diff evidence file, not formal files; changed the evidence patch to exact zero-context hunks without optional section labels, then checked patch application in a disposable index.'],'excluded_claims':['Real UI/input/key reachability','Font/graphics/animation/audio playback','Full engine/Demo','New independent/actual acceptance']})
dump('static-validation.json',checks)
raw_patch=git('diff','--binary','--unified=0',START,'--',F)
(out/'formal-diff.patch').write_bytes(re.sub(rb'^(@@.*?@@).*$',rb'\1',raw_patch,flags=re.M))
(out/'shared-file-proposals.md').write_text('''# R4-U03 shared-file proposals (integrator only)

作者没有修改公共审计／台账或其它批文件。以下仅交唯一整合员评估。

- audit/source-traceability.md：如需补追溯，请引用本目录 source-and-consumer-reading.json 的固定R锚点及七项finding，并绑定实际已整合字节；保留现有批次身份，不借历史PASS。
- WP65 §5.2皮肤预览可交叉引用WP15 §3.3，明确缺失候选走显式空结果而不是冷读取默认链；正常预览原事实保留。
- WP65 §7 PC与WP13 command103可引用WP17 §4.1/§5.4；事件默认取消是初值，不是−1；数量与命名入口各保留原优先序。
- WP74 §15的播放前向引用已有WP67-A，现可指向§9.4.1完整数据；命名／编译／旧映射文件规则不变。

任何公共文件实际修改由唯一整合员负责，并冻结新的实际字节、复核受影响消费者；本提案不构成授权扩写或接受登记。
''')
(out/'author-report.md').write_text('''# R4-U03 作者候选说明

状态：AUTHOR_READY_FOR_INDEPENDENT_CANDIDATE_REVIEW。作者没有自签独立PASS，没有登记ACCEPTED_SCOPED/CLOSED，没有自行调度reviewer。

七项事实修订仅修改合同12条正式文件：个体取图动态形态入口；BR18普通双Power仅3属性；普通/帮助命令与逐位数字的不同同轮出口；皮肤冷默认链和显式空结果；词边界与额外2单位阈值；18×6动画默认身份及回退；图鉴固定普通图像请求和异色记录分离。正式精确差异见formal-diff.patch；完整身份见static-validation.json，候选冻结身份由后继candidate-publication.json绑定，避免自嵌。

acceptance-map.json逐条保留7 finding全部30条验收标准、前提、反例、反证增加的精确条件与正文/向量位置。derived-vectors.json列46项条件静态设计，均NOT_EXECUTED_THIS_UPDATE。source-and-consumer-reading.json列32源/28正式锚点完整字节核验及必要消费者实际阅读；108个动画单元格只做静态数据对照。

affected-regression.json只核受影响范围。WP35/EG-13/20与WP34正确主合同完整字节保持；U05件数/商店、命名、文本、栖息地及形态资格原行保留。旧GR3具名状态与A053的229/341精确qualified身份保持；其它历史仅复用/not_reexecuted，不重跑全球review或全部历史。

execution.json保留固定第四review四次隔离原函数历史回执（M01一次、M02两次、M12一次），本批新增参考/模型/宿主/Demo执行均0。媒体、真实字体、输入/物理组合、像素、动画播放、完整地图/Demo、插件均未证，不阻塞事实静态修订。未来兼容政策未代选。

真实作者thread与任务ID见input-bindings.json；模型请求sol/xhigh/default/Fast=false，实际回显UNVERIFIED。父任务负责独立reviewer调度，入口为tasks/R4-U03/reviewer.md。仅唯一整合员能登记实际接受/关闭及应用shared-file-proposals.md。
''')
print(json.dumps({'formal_paths':len(allowed),'criteria':sum(e['criterion_count'] for e in accept),'vectors':len(vectors),'all108_cells_match':True,'author_thread':os.environ.get('CODEX_THREAD_ID'),'not_behavior_execution':True},ensure_ascii=False))
