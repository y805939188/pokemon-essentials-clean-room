import pathlib,json,hashlib,copy,datetime
r=pathlib.Path(__file__).resolve().parent.parent
formal={x['path']:{k:x[k] for k in ['bytes','sha256','git_blob']} for x in json.loads((r/'evidence/formal-identity-check.json').read_text())}
source={x['path']:{k:x[k] for k in ['bytes','sha256','git_blob']} for x in json.loads((r/'evidence/reference-inventory.json').read_text())}
verdicts={}
for task in ['CA','CB']:
 p=r/'modules'/task/'verdicts.json';receipt=r/'tasks'/(task+'-launch.json')
 if p.exists() and json.loads(receipt.read_text())['status']=='PROCESS_COMPLETED':
  for i,v in enumerate(json.loads(p.read_text())['records']):verdicts[v['finding_id']]=(task,i,v)
categories={'GR4-M01-001':'数据或资源契约缺口','GR4-M01-002':'事实错误','GR4-M02-001':'缺能力','GR4-M02-002':'实现信息不足','GR4-M02-003':'缺能力','GR4-M03-001':'缺能力','GR4-M03-002':'状态或时序错误','GR4-M03-003':'实现信息不足'}
def append_criterion(f,text):
 a=f['acceptance_criteria']
 if isinstance(a,dict):a.setdefault('static',[]).append(text)
 else:a.append({'kind':'SPEC_STATIC','criterion':text})
def refine(f):
 id=f['id']
 if id=='GR4-M02-001':
  f['expected_reference_behavior']+=' 一般天数输入在d<0时先取0；若设置时Unix墙钟秒为t，保存持续量D=(t mod 86400)+86400×max(d,0)−t。该量不是下一午夜相对时长。'
  f['preconditions'].append('刷新替身仅计调用；若解释真实地图刷新，假定刷新正常返回且不回写该变量。探针中的刷新次数只指替身调用，不是事件页已执行次数。')
  append_criterion(f,'给出一般天数公式D=(t mod 86400)+86400×max(d,0)−t、默认/负期限和严格大于门；保持无默认caller证据的限定。')
 if id=='GR4-M02-002':
  f['severity']='P3';f['expected_reference_behavior']+=' 源静态事实是构造阶段位于宿主调用的局部捕获之外；FrozenError/ArgumentError等精确异常和返回值只按Ruby2.6隔离回执确认，随附3.1宿主仍未执行。'
  f['impact_on_independent_implementation']+=' 影响限定于已定位的工具输入边界；没有默认业务caller证据，不推断所有默认游戏POST均不可用。'
 if id=='GR4-M02-003':
  f['minimal_counterexample']={'input':'正整数n=2；首次返回0后，已见仅0、未见仅1。','reference_conditional_probabilities':{'next_0':'1/7','next_1':'6/7'},'without_replacement_next_0':'0','independent_uniform_next_0':'1/2','reason':'0,0单条允许序列只排除无放回，不能排除独立均匀随机；差异由条件分布说明。','evidence_level':'DERIVED_VECTOR','execution_status':'NOT_EXECUTED'}
  append_criterion(f,'用首抽0后P(0)=1/7、P(1)=6/7与无放回0、均匀1/2作条件概率对照；不把一条重复序列当统计证明。')
 if id=='GR4-M03-001':
  f['expected_reference_behavior']+=' 对正横界r，左当x>x0−r、右当x<x0+r；对正纵界s，下当y<y0+s、上当y>y0−s。固定参考候选序是左、右、下、上，保留满足门的方向后仅作一次均匀索引选择；此序用于解释固定参考抽样，不规定未来容器或跨语言随机序列。方向选择不预转向，移动成功后的转向沿WP12。'
  append_criterion(f,'写出严格比较式和固定参考候选序，并区分方向过滤/越界钳回；受阻不重抽、不预转向的行为引用已有WP12合同。')
 if id=='GR4-M03-002':
  f['preconditions']+=['玩家through=false，无调试Ctrl穿透；ending_surf初始false。失败跳跃不启动运动计时，初始无未完成运动/步后通知。']
  f['failure_or_boundary_case']='取消游泳参数true只清冲浪/潜水标志，未独立清临时底座/结束字段；后继合格步通知仍可能清理。人为ending_surf=true只用于直接转移与等待门的条件事实：正常事件201会先受解释器等待门阻止，不能用它证明该人工状态可越门，也不宣称默认流程必软锁。'
  append_criterion(f,'反例明确through=false、无Ctrl穿透、ending_surf=false、未启动运动计时；直接转移、正常201与步后清理分层。')
 if id=='GR4-M03-003':
  f['preconditions']+=['主解释器记录的地图与当前地图相同，无消息/移动/冲浪等等待门；116不是终止项，后续全局开关命令之后还有正常终止项。']
  f['gap']+=' 通用“假结果停止当前更新”的调度合同已经存在；只缺116本身选择这一控制结果并在内部推进一项的具名绑定，不另报通用解释器算法缺失。'
  append_criterion(f,'只补116的具名推进/让出结果，复用已有通用调度；后条在下一次解释器更新机会尝试，不硬说下一渲染帧。')
 if id=='GR4-M04-001':
  f['current_spec_behavior']='WP18 §3.4把“图像”列为简化形态读取消费者，属于明确的过宽分类。WP21已有动态读取/提交与守卫；WP35 §5.2/§9及EG-13/20还明确承接孵化演出先读动态形态的副作用。这些是实质反证和已正确部分，但不能消解WP18相反泛称；本项限于入口归属及跨文档一致性。'
  f['proposed_spec_change']='最低修订是纠正WP18的图像泛称，并明确按个体精灵/图标入口继承普通动态读取合同；WP15/21按需要对齐引用，复用已正确的WP21/35提交与守卫。增具名静态对照，不重建动态形态整域，不修改WP35正确规则。'
  f['normal_case']='整数t恰加432000秒不回退。低层按显式物种/形态取图只消费已求值的数值参数；若上游为获得参数先读个体动态形态，调用链仍可能有副作用，孵化即有已承接对照。'
  f['preconditions'].append('时间戳t为整数秒；物种资料、能力重算和图鉴依赖正常。显式参数对照先给定数值，不能以低层纯消费反推整条调用链纯读。')
  f['spec_anchors'] += [{'path':'deliverables/final-specification-set/creature-rpg/wp35-eggs-and-hatching.md','commit':'1f36475d22120a0d1175967d5b17d71fe8311d88','lines_or_symbol':'§5.2/§9；99–122,158–169','fact':'已准确承接孵化核心与演出动态读取，必须保留的强反证。'},{'path':'deliverables/final-specification-set/test-catalog/creature-rpg-wp35-36-57-64-68.md','commit':'1f36475d22120a0d1175967d5b17d71fe8311d88','lines_or_symbol':'EG-13/EG-20；21–32,75','fact':'动态孵化对照已有承接，不重新报缺失。'}]
  append_criterion(f,'保留WP35/EG-13/20已正确的动态孵化合同；显式物种资源接口仅在输入形态已求值时为纯消费，不外推调用者。')
 if id=='GR4-M10-001':
  f['preconditions'].append('无传入块改写值或输入；USE/BACK是给定按下沿，方向是给定repeat查询，不是已实测物理按键。事件103的默认取消值为初值；显式取消−1只是独立通用数字夹具。')
  append_criterion(f,'事件数字消费者另用默认取消等于初值的夹具；例如初1同轮UP+USE+BACK确认2，不能把通用取消−1称为该事件默认。')
 if id=='GR4-M10-002':
  f['expected_reference_behavior']=f['expected_reference_behavior'].replace('System/Window','Graphics/System/Window').replace('Windowskins/001-Blue01','Graphics/Windowskins/001-Blue01')
  f['preconditions'].append('显式设置对照指定完整逻辑资源位置，不假设任意裸名自动加目录；未提供选项对象时从配置首项开始。')
  f['excluded_claims'].append('逻辑空资源名称不等于既有窗口必定清皮肤、保持旧图或必崩溃；这些真实像素与对象失效结果未证。')
 if id=='GR4-M10-003':
  f['expected_reference_behavior']+=' 固定参考的换行宽度判定还预留额外2个同单位的测量量；需非行首词边界及对应内容条件成立才移词，不能概括为裸文字宽大于请求行宽。'
  f['preconditions'].append('普通样式、起点x=0、非斜体、无额外描边，自动与显式换行均开启；高度不限制。<pg>只用于路径对照，比较逻辑行归属，不要求两个路径绝对纵坐标相同。')
  f['failure_or_boundary_case'].append('同一度量A=8、B=8、ASCII空格=4，A B在行宽22保持一行、行宽21时B移下一行；此边界体现额外2单位，不是字体实测或裸宽比较。')
  append_criterion(f,'明确额外2个测量单位及适用的词边界/内容门；补A B宽22不换、21换的独立对照，并限定普通样式和起点0。')
 if id=='GR4-M10-004':
  f['preconditions'].append('映射10/20/30及对方11均为条件夹具中的有效槽，不是默认媒体真实编号；双方映射容器均有效，排除容器异常的局部救援空结果。')
 if id=='GR4-M11-001':
  f['preconditions'].append('最小BULBASAUR夹具先不进入形态选择器；若验证首轮另写异色false，另设>1可列形态的独立夹具，不能用单项个体证明该分支。')
  append_criterion(f,'普通刷新保留true/false原记录与多项Forms选择器首轮写false分开；多项选择器反向例需独立合法多项夹具。')

findings=[];resolutions=[];pending=[]
for m in [f'M{x:02d}' for x in range(1,13)]:
 p=r/'modules'/m/'findings.json';data=json.loads(p.read_text());raw=data['findings'];launch=json.loads((r/'tasks'/(m+'-launch.json')).read_text())
 for i,orig in enumerate(raw):
  f=copy.deepcopy(orig);f['category']=categories.get(f['id'],f['category']);f['classification']=orig.get('classification',{'M01':'Generic Kernel / Demo–Developer Experience','M02':'Generic Kernel','M03':'Engine / Overworld Integration','M04':'Creature-RPG / Pokémon Rules','M05':'Creature-RPG','M06':'Pokémon Rules','M10':'User Interface / Engine Integration','M11':'User Interface / Pokémon Rules','M12':'Demo / Developer Experience'}.get(m,m))
  f['reviewer']={'module':m,'thread_id':launch['thread_id'],'pid':launch['pid'],'role':'fresh independent semantic reviewer','requested':launch['requested'],'actual_echo':'UNVERIFIED'}
  f['artifact_origin']='modules/'+m
  f['original_submission']={'path':str(p.relative_to(r)),'pointer':'/findings/'+str(i),'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'severity':orig['severity'],'category':orig['category'],'status':orig['status'],'reviewer_at_submission':orig['reviewer']}
  f['evidence_level']=list(dict.fromkeys(next((y for y in ['SOURCE_STATIC','SPEC_STATIC','DERIVED_VECTOR','TOOL_VALIDATION','EXECUTED_MODEL','EXECUTED_REFERENCE','EXECUTED_HOST_OR_DEMO'] if str(x).startswith(y)),str(x)) for x in (f['evidence_level'] if isinstance(f['evidence_level'],list) else [f['evidence_level']])))
  if f['id'] in verdicts:
   task,vi,v=verdicts[f['id']];assert v['decision'] in ['CONFIRM','CONFIRM_WITH_REFINEMENT'],(f['id'],v['decision'],'Needs explicit adjudication')
   f['severity']=v['severity'];refine(f);f['status']='CONFIRMED';f['disposition']='REQUIRED'
   counter={'task':task,'thread_id':json.loads((r/'tasks'/(task+'-launch.json')).read_text())['thread_id'],'path':'modules/'+task+'/verdicts.json','pointer':'/records/'+str(vi),'decision':v['decision'],'reason':v['reason'],'required_refinements':v.get('required_refinements',[]),'execution_evidence_assessment':v.get('execution_evidence_assessment'),'historical_relation_assessment':v.get('historical_relation_assessment')}
   f['negative_evidence_search']={'primary_review':f['negative_evidence_search'],'primary_relative_paths_base':f['artifact_origin'],'independent_counterevidence':v['counterevidence_search'],'counter_relative_paths_base':'modules/'+task}
   f['history_links']['independent_scope_assessment']=v.get('historical_relation_assessment')
   f['review_resolution']={'decision':'CONFIRMED_AFTER_INDEPENDENT_CHALLENGE','root_adjudicator':'parent /root; 01a12fc2-e8c0-7e43-a721-ccfe659d75c8','independent_counterreview':counter,'root_judgment':'已阅读完整事实、前提、反证和范围；采纳具名精确化，保持仅事实规格修订，不重开旧CLOSED或冒运行证明。','severity_change':None if f['severity']==orig['severity'] else {'from':orig['severity'],'to':f['severity'],'reason':v['reason']},'formal_revision_applied':False}
   for u in v.get('remaining_unknowns',[]):
    if u not in f['unknowns']:f['unknowns'].append(u)
   resolutions.append({'id':f['id'],'status':f['status'],'severity':f['severity'],'original_severity':orig['severity'],'counterreview':counter,'duplicate_of':v.get('duplicate_of'),'root_decision':'adopt with bounded refinements'})
  else:
   f['status']='PENDING_INDEPENDENT_COUNTERREVIEW';pending.append(f['id']);resolutions.append({'id':f['id'],'status':f['status']})
  for a in f['spec_anchors']:
   if a['path'] in formal:a['identity']=formal[a['path']]
  for a in f['source_anchors']:
   if a['path'] in source:a['identity']=source[a['path']]
  findings.append(f)
assert len({f['id'] for f in findings})==len(findings)
summary={'canonical_ids':len(findings),'required':sum(f['disposition']=='REQUIRED' for f in findings),'optional':sum(f['disposition']=='OPTIONAL' for f in findings),'unresolved':sum(f['disposition']=='UNRESOLVED' for f in findings),'no_required_revision':sum(f['disposition']=='NO_REQUIRED_REVISION' for f in findings),'required_severity':{s:sum(f['disposition']=='REQUIRED' and f['severity']==s for f in findings) for s in ['P1','P2','P3']},'pending_independent_counterreview':pending}
root={'schema_version':'1.0','$schema':'findings.schema.json','status':'FINAL_ADJUDICATED' if not pending else 'DRAFT_PENDING_COUNTERREVIEW','formal_baseline':{'commit':'1f36475d22120a0d1175967d5b17d71fe8311d88','tree':'d696e23ce4a0eae12b0bb2a5e74bf9cd4c74764a'},'reference_baseline':{'commit':'8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b','tree':'7589c800b61ba13a13040ed0d686979b80a84fd0'},'path_resolution':'source/spec paths relative to their fixed repository roots; submission auxiliary paths relative to artifact_origin unless a report-root path is explicit.','summary':summary,'findings':findings}
(r/'findings.json').write_text(json.dumps(root,ensure_ascii=False,indent=2)+'\n')
(r/'counterreview-and-dedup.json').write_text(json.dumps({'schema_version':'1.0','status':root['status'],'records':resolutions,'aliases':[],'rule':'不同根因不因同文件合并；J消费者重复投影仅关联原ID，不重复计问题。所有模块原稿保留原字节。','independent_junction_new_findings':json.loads((r/'modules/J/findings.json').read_text()).get('findings',[])},ensure_ascii=False,indent=2)+'\n')
print(json.dumps(summary,ensure_ascii=False))
