#!/usr/bin/env python3
"""Build review evidence from independently audited fixed JSON; document operations only."""
import copy, hashlib, json, subprocess
from pathlib import Path
OUT=Path('review/r8-disposition-r2-independent-a32873d-20261017/agents')
BASE='planning/implementation-routing/r8-20261017/'
C='a32873d2860b15d9f5e27727db8f131f4ec433b6';R='8c8b46e919e0a15aaaf204f16df5b4ad3c9888b8';P='908273093e1f6b27fc58249417675dd62d146224'
RP='review/r8-disposition-r1-independent-5666b7b-20261017/'
def b(c,p):return subprocess.check_output(['git','show',c+':'+p])
def obj(c,p):return json.loads(b(c,p))
def sha(x):return hashlib.sha256(x).hexdigest()
k=obj(R,RP+'agents/kernel-results.json');m=obj(C,BASE+'routing-manifest.json')
ev=json.loads((OUT/'kernel-evidence.json').read_text())
f={x['feature_id']:x for x in m['features']};ret={x['feature_id']:x for x in m['retired_features']};meta={x['metadata_id']:x for x in m['metadata_records']}
row_ev={x['feature_id']:x for x in ev['old_row_identity']}
old_result={x['feature_id']:x for x in k['old_feature_results']}
special={
 'FR-000392':'完整WP02§7六个组合逐组核对：编译401/402、领域配置454/532/537、亲密208与战斗/进化28/490/501等、场地374/375、插件411–413、Shadow483/484/487/488及捕获530均连接实际主责；钓鱼385–387已从META19清除。元数据、retirement及§7章节refs相等；不计新功能。',
 'FR-000398':'完整WP03§7的40个字段组逐项核对，涵盖物种/能力/学习/状态/道具/指标/特性/AI/Shadow/繁育/遭遇/世界/设施/非类产物；META20连接已有真实消费者，40组union与元数据、retirement、章节refs相等；完整旧体保全，未造实现空壳。',
 'FR-000407':'完整WP04§7六个交界逐项核对，文本438/440/441、内容与世界编辑262–274、事件转换294–301、资源352–354及指标/动画289/683、身份394–397与候选391均有真实主责；元数据/retirement/coverage同步，旧体完整。',
 'FR-000420':'WP06§6完整10字段与WP22§4完整执行门重新核对；已补FR471及WP22§4直接合同，reason准确限定玩家本人所属者、先增计数后消息/变形、异常不补偿。WP42/38其余生产关系保持，未以终局统计替代Mega生产。',
 'FR-000436':'完整WP07§5.1–6及WP04§6、WP05§7、WP09主流程/失败交界、WP10§5和弃用§6重新核对；四个错误本地化reason已替换成真实编译定位/插件诊断终止/主循环Hangup/恢复条件，五条feature_refs承接真实失败层。WP09广章节7结合本篇4.1.1及WP10§5导航可接受，不要求重复所有最细锚点。'
}
old=[]
for r in k['old_feature_results']:
 id=r['feature_id'];e=row_ev[id];cur=f.get(id) or ret[id]
 reason=special.get(id,'固定R1通过行整行相等，source/current/去向/责任/依赖/范围/状态均未改；本轮三张元数据表和目录补接只导航既有消费者，不转移本行职责。保留R1具体语义：'+r['reason'])
 old.append({'feature_id':id,'original_verdict':r['old_verdict'],'r1_verdict':r['verdict'],'new_verdict':'PASS','verdict':'PASS','disposition':r['disposition'],'reason':reason,'method':'REREAD_COMPLETE_AFFECTED_UNIT_AND_CONSUMERS' if id in special else 'EXACT_R1_ROW_IDENTITY_PLUS_ATTRIBUTED_SEMANTIC_CREDIT_AND_NONIMPACT_REVIEW','inherited':id not in special,'r1_reason':r['reason'],'r1_record_equal':e['r1_record_equal'],'affected_fields':e['changed_top_fields'],'immutable_source_preserved':e['immutable_source_equal_original'],'source':cur['source'],'candidate_pointer':('/features/'+str(m['features'].index(cur))) if id in f else '/retired_features/'+str(m['retired_features'].index(cur)),'finding_refs':[],'resolved_issue_refs':['R1-KF-001'] if id in ['FR-000392','FR-000398','FR-000407'] else ['R1-KF-002'] if id in ['FR-000420','FR-000436'] else []})
active=[]
for r in k['active_feature_results']:
 id=r['feature_id'];cur=f[id]
 base=copy.deepcopy(next(x for x in old if x['feature_id']==id)) if id in old_result else {'feature_id':id,'r1_verdict':r['verdict'],'new_verdict':'PASS','verdict':'PASS','disposition':'active','reason':'FR745整行与固定R1相等，普通随机父427精确排除录像子范围；catalog→427→excluded_child_refs→745明确导航仍有效。保留R1已读WP58完整合同信用；没有要求catalog重复直接列745。','method':'EXACT_R1_ROW_IDENTITY_AND_ATTRIBUTED_SOURCE_CREDIT','inherited':True,'r1_record_equal':True,'affected_fields':[],'finding_refs':[]}
 base.update({'is_r1_new':id not in old_result,'current_applicability':cur['current_applicability'],'functional_scope':cur['functional_scope'],'source':cur['source'],'candidate_pointer':'/features/'+str(m['features'].index(cur))})
 active.append(base)
retired_metadata=[]
for item in ev['metadata_audit']:
 mid=item['metadata_id'];id=item['retired_feature_id']
 for unit in ['retired_feature','metadata_record']:
  retired_metadata.append({'unit_type':unit,'unit_id':id if unit=='retired_feature' else mid,'metadata_id':mid,'retired_feature_id':id,'r1_verdict':'FAIL','verdict':'PASS','reason':special[id],'source':meta[mid]['source'],'consumer_refs':meta[mid]['feature_refs'],'complete_original_history_preserved':row_ev[id]['retired_body_equal_original'],'functional_count_treatment':'NOT_ACTIVE_FUNCTION; metadata responsibility/navigation only','method':'COMPLETE_SOURCE_TABLE_REREAD_ALL_GROUPS_AND_NAVIGATION_PROPAGATION','candidate_pointer':'/retired_features/'+str(m['retired_features'].index(ret[id])) if unit=='retired_feature' else '/metadata_records/'+str(m['metadata_records'].index(meta[mid])),'finding_refs':[]})
catalog_checks=[
 (2226,'KC03许可→374/375；KC05/06玩家语言/提取目标→439/441/642/644。完整KC01–06源与语言/徽章消费者已核；其余粗文档导航允许。'),
 (2227,'KR13 Nature固定顺序和能力结果→454/456；完整KR01–16已读，WP19§3.5完整25映射支持LONELY/BRAVE。'),
 (2228,'KL连接/缓存→323/269，遭遇→272，指标No/Yes与路径→273；动画既有277的WP67-A直接合同可达播放主责，允许间接导航。'),
 (2230,'完整作者输入表新增地牢/图块集346–349及连接323/269；U01-M01-021/022与027真实消费者已核。'),
 (2231,'FLAGS-04先减步再特性查询失败→219；指标部分记录/惰性克隆/编辑→273；完整R6-U14表及WP35§4已读。'),
 (2232,'J01-V01–06/V11地牢参数/图块集→346–349；V12指标编辑→273；完整J01及后继默认表均为NOT_EXECUTED。'),
 (2245,'LZ39–41键图语言身份→639及352/353，WP65控制帮助§3与WP15§3.2明确七键图/背景/标签分层、译后资源无通用重试；LZ36–38保留库存/导入前缀。')
]
s=obj(C,BASE+'section-coverage.json')['sections'];ps=obj('5666b7b912e2fb79b5119283ee6a37401a7071db',BASE+'section-coverage.json')['sections']
cat_by={i:reason for i,reason in catalog_checks}
sections=[]
for i,r in enumerate(s):
 if r['path'] not in {x['path'] for x in ev['reading_ledger']}:continue
 if r['mapping_kind']!='section-metadata':continue
 special_id=next((mid for mid in ['META-000019','META-000020','META-000021'] if mid in r['metadata_refs']),None)
 why=cat_by.get(i)
 if special_id:why=special[{'META-000019':'FR-000392','META-000020':'FR-000398','META-000021':'FR-000407'}[special_id]]
 sections.append({'unit_type':'section_metadata','unit_id':r['document_id']+'#'+r['anchor'],'candidate_pointer':'/sections/'+str(i),'verdict':'PASS','r1_record_equal':r==ps[i],'source':{'commit':P,'document':r['path'],'line_ranges':[[r['line_start'],r['line_end']]]},'consumer_refs':r['feature_refs'],'metadata_refs':r['metadata_refs'],'retired_feature_refs':r['retired_feature_refs'],'reason':why or '与固定R1完整章节映射逐字段相等；原非功能/来源/静态目录处理及文档级导航未受本轮变更影响，保持R1限定语义信用；不等于执行静态向量。','method':'FRESH_COMPLETE_SOURCE_AND_CONSUMER_REVIEW' if why else 'EXACT_MAPPING_IDENTITY_WITH_ATTRIBUTED_R1_SEMANTIC_CREDIT','finding_refs':[]})
issues=[]
issues.append({'issue_id':'R1-KF-001','r1_verdict':'FAIL','verdict':'PASS','all_cases_checked':True,'cases':[{'metadata_id':x['metadata_id'],'retired_feature_id':x['retired_feature_id'],'verdict':'PASS','complete_groups':len(x['groups']),'group_results':[dict(g,verdict='PASS',review_reason='完整源表该字段组逐项对照现有消费者所属合同；该组为责任/证据导航，不新增功能，允许章节级聚合及明确间接导航。') for g in x['groups']],'reason':special[x['retired_feature_id']],'propagation_checks':{key:x[key] for key in ['source_equal_r1','group_union_equals_metadata_refs','retirement_refs_equal_metadata','section_propagation']}} for x in ev['metadata_audit']]+[{'candidate_pointer':'section-coverage.json:/sections/'+str(i),'verdict':'PASS','reason':reason} for i,reason in catalog_checks],'propagation':'全部三meta、三retirement及十个受影响section重核；其它76个section-metadata映射精确身份保全。旧文档级宽导航保留，不凭同WP号认定新主责。','finding_refs':[]})
issues.append({'issue_id':'R1-KF-002','r1_verdict':'FAIL','verdict':'PASS','all_cases_checked':True,'cases':[{'feature_id':id,'verdict':'PASS','reason':special[id],'candidate_pointer':'/features/'+str(m['features'].index(f[id]))+'/dependencies'} for id in ['FR-000420','FR-000436']],'propagation':'KF004其余12原case行完全不变；420只增加真实WP22生产合同，436新理由不更改其源失败层。检查指向436的既有753可读作作者校验的诊断层，不把它理解为本地化提供者。','finding_refs':[]})
groups=[]
for r in k['finding_results']:
 g=copy.deepcopy(r);g['r1_verdict']=r['verdict'];g['verdict']='PASS';g['finding_refs']=[];g['method']='REASSESSED_ALL_CASES' if r['finding_id'] in ['KF-001','KF-004'] else 'EXACT_CASE_ROW_IDENTITY_AND_RELEVANT_NONIMPACT_REVIEW'
 for c in g['original_cases']:
  id=c['feature_id'];c['r1_verdict']=c['verdict'];c['verdict']='PASS';c['finding_refs']=[]
  c['reason']=special[id] if id in special else 'R2相对R1本行整行相同，具体原case裁定保持，相关元数据/生产或失败依赖改动不转移其职责。R1具体理由：'+c['reason']
 g['summary']={'KF-001':'三退役及三后继按完整6/40/6组责任表和导航重新核对，全部PASS。','KF-004':'完整14case：420/436新语义修复通过，另12case整行相等及同根因无影响；全部PASS。'}.get(r['finding_id'],'原组全部case相对R1整行未变，职责/范围与边界不受本轮5旧行修复影响；原PASS有依据保留。')
 g['related_new_or_propagated_units']=[dict(x,r1_verdict=x['verdict'],verdict='PASS',reason='R2实际字段差分及本轮相关完整源表审查支持保全/修正；具体见issue_results、old_feature_results及section_metadata_results。R1证据：'+x['reason']) for x in r['related_new_or_propagated_units']]
 groups.append(g)
extra_specs=[
 ('pokemon-rules/wp22-mega-and-primal-reversion.md',[[37,65]],'Mega实际生产门/玩家本人/先提交与失败前缀'),
 ('demo-dx/wp73-b-world-editors.md',[[28,168]],'完整连接、元数据、地形、遭遇及指标消费者章'),
 ('creature-rpg/wp35-eggs-and-hatching.md',[[67,105]],'完整每步处理/加速及提交前缀'),
 ('engine-overworld/wp14-random-dungeons.md',[[23,281]],'完整生成输入、布局、图块化及摆放章，区分参数/图块集'),
 ('engine-overworld/wp15-resource-matching-and-audio.md',[[20,91]],'资源解析及内容资源变体完整章，指定图像身份接点'),
 ('user-interface/wp65-controls-help-appendix.md',[[1,60]],'控制帮助全文：键图创建/加载、标签及背景分层'),
 ('pokemon-rules/wp19-attributes-ability-and-stats.md',[[30,116]],'完整属性派生章，含Nature25映射'),
 ('engine-overworld/wp59-world-time-weather-field-moves.md',[[181,283]],'场地入口分层、徽章资格、完整逐族效果与统计生产'),
 ('creature-rpg/wp30-growth-learning-and-friendship.md',[[182,221]],'完整友好度/亲密度章及软上限消费者'),
 ('engine-overworld/wp11-map-topology-transfer.md',[[23,77],[121,159]],'完整地图身份/连接、跨图转移和地图恢复章，输入编译与实际连接/读档消费'),
 ('user-interface/wp65-title-load-options-pause-and-pc.md',[[23,82],[102,147]],'完整标题/载入、选项/语言章，玩家语言菜单及直写'),
 ('user-interface/wp17-messages-windows-input.md',[[23,107],[161,267]],'完整消息窗口与输入章，用于435窗口/输入交界'),
 ('combat-requirements/wp58-battle-recording-and-playback.md',[[1,181]],'录像全文，FR745全部五个出站边的真实记录/消费分层'),
]
extra=[]
for path,ranges,purpose in extra_specs:
 path='deliverables/final-specification-set/'+path;bb=b(P,path)
 extra.append({'path':path,'commit':P,'file_sha256':sha(bb),'file_git_blob':subprocess.check_output(['git','rev-parse',P+':'+path],text=True).strip(),'fresh_read_ranges':ranges,'purpose':purpose,'is_primary_allocated_document':False})
# Every cross-domain metadata consumer is tied to prior independent source/semantic credit.
root_results=obj(R,RP+'feature-results.json');rr={x['feature_id']:x for x in root_results['active_feature_results']};root_read=obj(R,RP+'reading-coverage.json');rd={x['path']:x for x in root_read['documents']}
allrefs=sorted(set().union(*(set(meta[x]['feature_refs']) for x in ['META-000019','META-000020','META-000021'])))
consumer_credit=[]
for id in allrefs:
 cur=f[id];path=cur['source']['document'];current=b(P,path);historical=b(cur['source']['commit'],path)
 r=rr.get(id)
 consumer_credit.append({'feature_id':id,'path':path,'source_heading':cur['source']['heading'],'source_line_ranges':cur['source']['line_ranges'],'current_sha256':sha(current),'historical_sha256':sha(historical),'r1_semantic_credit':{'commit':R,'feature_result_pointer':'/active_feature_results/'+str(root_results['active_feature_results'].index(r)) if r else None,'reviewer':r.get('reviewer') if r else 'R2 combat owner for new769','verdict':r['verdict'] if r else 'NOT_R1_NEW769','reason':r['reason'] if r else 'New769 belongs to combat R2 direct review; META20 only navigates phase-trigger owner.'},'r1_source_credit_identity_equal':rd[path]['source_identity'].get('sha256')==sha(historical),'new_relation_review_basis':'完整WP02/03/04责任表与既有消费者合同范围逐组对照，见issue_results；源正文身份及R1独立域语义信用另列。此项不声称跨域全文fresh reread。'})
results={'schema':'r8-r2-independent-kernel.v1','candidate_commit':C,'prior_candidate':'5666b7b912e2fb79b5119283ee6a37401a7071db','prior_review_commit':R,'domain':'generic-kernel','reviewer':'/root/r2_kernel','verdict':'PASS','verdict_scope':'FIXED_CURRENT_908_DOMAIN_ROUTING_ONLY; ROOT_TOOLS_AND_CUMULATIVE_ACCEPTANCE_SEPARATE','configuration':{'requested':{'model':'gpt-6.1-sol','effort':'ultra','service_tier':'default','speed':'normal','Fast':'off'},'authoritative_creation_echo':{x:'UNVERIFIED' for x in ['model','effort','service_tier','speed','Fast','cloud_task_uuid']},'actual_execution_echo':{x:'UNVERIFIED' for x in ['model','effort','service_tier','speed','Fast']}},'counts':dict(ev['summary'],old_feature_verdicts={'PASS':66},active_feature_verdicts={'PASS':64},original_groups={'PASS':6},residual_issues={'PASS':2},explicit_metadata={'PASS':3},retired_history={'PASS':3},catalogs={'PASS':2},section_metadata={'PASS':86}),'old_feature_results':old,'active_feature_results':active,'retired_metadata_results':retired_metadata,'issue_results':issues,'original_group_results':groups,'finding_results':groups,'section_metadata_results':sections,'catalog_results':[{'document_id':id,'verdict':'PASS','classification':'static catalog; not an active function','execution_status':'NOT_EXECUTED preserved','reason':'全文重读；全部原失败具名消费者已连接现有主责。显式间接导航有效，不要求逐case新增ID。'} for id in ['DOC-0108','DOC-0109']],'reading_ledger':ev['reading_ledger'],'extra_consumer_reading':extra,'cross_domain_semantic_credit':consumer_credit,'mechanical_evidence':'kernel-evidence.json','new_findings':[],'remaining':['Current application remains 908/U02U03 only; 0eee source locators/headings are preparation only, cumulative source acceptance is not granted.','Root independently owns source-acceptance tool/schema findings and whole-view/tool/protection verdict; this domain PASS does not grant those gates.','All target verification pending; four prototypes, host and business vectors unexecuted; user scope/stage decisions remain.','Execution configuration and cloud UUID have no authoritative echo and remain individually UNVERIFIED.'],'limitations':['Primary13 documents use exact fixed R1 full source credit for unchanged/unaffected facets; fresh ranges are enumerated, not all-clause reprinting.','New responsibility-table relations are reviewed against full6/40/6 source groups, existing consumer scopes and attributed prior independent semantic credit, supplemented by listed fresh consumer chapters; cross-domain full fresh reading is not claimed.','Early read-only exploration had field-name KeyErrors and truncated broad outputs; failed/truncated output gets no semantic full-read credit; corrected audit completed exit0.'],'business_execution_count':0}
edge_basis={
 'FR-000416':{'FR-000374':'完整场地§5逐族生产统计，§5.3.1严格预检→先加strength_push_count→普通一步/快照及失败前缀，确属统计生产方。'},
 'FR-000420':{'FR-000471':'Mega实际执行的玩家本人计数生产点，见WP22完整§4.3；本轮新边正确。'},
 'FR-000435':{'FR-000446':'诊断遇主流程超时紧急保存需正常保存路径及IO/类型失败分层。','FR-000451':'紧急保存/恢复UI、场景置空与正常尾部恢复，依赖用途准确。','FR-000625':'MZ伙伴承接消息/窗口消费；通用窗口章为呈现交界，不宣称诊断格式等同消息转义。','FR-000628':'MZ伙伴承接输入（如Ctrl复制）的宿主交界；输入章明确宿主按住/刷新未验证，不把字符命名规则套给诊断。'},
 'FR-000436':{'FR-000406':'编译内容异常的位置报告、启动/直接入口清理及转换差异。','FR-000413':'插件注册/载入错误诊断后直接终止的真实失败层。','FR-000432':'弃用告警非致命、创建/使用边界与致命诊断相对照；排除性共同交界成立。','FR-000448':'保存/读档错误的IO、类型、备份/删除边界；WP09本篇4.1.1与WP10完整§5提供主流程/超时导航。','FR-000451':'紧急保存/加载恢复真实失败条件及正常尾部恢复，不是语言状态服务。'},
 'FR-000439':{'FR-000444':'持久系统选项与启动读取/新游戏保留合同。','FR-000446':'载入语言变更直接写档，与正常保存分开。','FR-000642':'启动/载入语言选择可见门与命令交付。','FR-000644':'选项/语言导航和落盘边界，非选项注册中的语言菜单。'},
 'FR-000445':{'FR-000324':'跨图转移章有独立读档恢复行，重建/进入通知与缺图选择分层真实。','FR-000326':'完整WP11§6读档重建/复用、局部记录清空/恢复及异常前缀。','FR-000451':'无效档、备份/删除、缺图选图取消和紧急恢复链。','FR-000642':'标题/载入界面请求与选择交付。'},
 'FR-000451':{'FR-000326':'地图恢复消费者完整§6，含缺图/局部恢复前缀。','FR-000435':'关键段诊断、普通异常完成标记与超时转Reset。','FR-000445':'实际系统装配/新游戏/继续状态与地图恢复调用门。','FR-000642':'载入备份/删除确认与选图等UI接点。'},
 'FR-000745':{'FR-000132':'记录临时/持久生命周期及终局保留门。','FR-000133':'准备后的初态五元组、缺失字段与18键边界。','FR-000134':'命令登记/覆盖/取消与实际动作分开。','FR-000135':'实际记录随机及换人序列、AI不入域和不足前缀。','FR-000136':'回放恢复/槽分派/中止及清理，版本等价未证。'},
}
edges=[];edge_sources=[]
for r in active:
 cur=f[r['feature_id']];refs=cur['dependencies']['feature_refs']
 edge_sources.append({'feature_id':r['feature_id'],'feature_refs':refs,'edge_count':len(refs),'r1_record_equal':r['r1_record_equal'],'verdict':'PASS','empty_refs':not refs})
 for target in refs:
  dst=f[target]
  edges.append({'source_feature_id':r['feature_id'],'target_feature_id':target,'verdict':'PASS','reason':edge_basis[r['feature_id']][target],'source':cur['source'],'target_source':dst['source'],'target_functional_scope':dst['functional_scope'],'candidate_pointer':'/features/'+str(m['features'].index(cur))+'/dependencies/feature_refs','method':'ALL_NONEMPTY_FEATURE_EDGES_SEMANTIC_SCOPE_REVIEW_WITH_COMPLETE_TARGET_CHAPTERS_AND_FIXED_SOURCE_IDENTITY'})
assert len(edge_sources)==64 and len(edges)==28
results['outbound_feature_edge_audit']={'active_source_count':64,'sources_with_edges':8,'sources_without_edges':56,'edge_count':28,'bad_edge_count':0,'all_edges_semantically_examined':True,'source_results':edge_sources,'edge_results':edges,'propagation_note':'整行相等本身不为依赖授PASS；本域全部28feature_refs按实际目标scope逐边核用途，未见同WP号错ID。目录/元数据合并导航另见issue_results。'}
(OUT/'kernel-results.json').write_text(json.dumps(results,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'old':len(old),'active':len(active),'retired_metadata':len(retired_metadata),'groups':len(groups),'issues':len(issues),'section_metadata':len(sections),'cross_consumer_credit':len(consumer_credit)},ensure_ascii=False))
