"""Finite candidate-author batches from explicitly adjudicated records."""
import collections, json, pathlib
ROOT=pathlib.Path(__file__).resolve().parents[1]
def get(p):return json.loads((ROOT/p).read_text())
def put(p,x):(ROOT/p).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
records=get('findings/normative-records.json')
required=[x for x in records if x['identity_and_verdict']['classification']=='required']
groups=[
('U01','内核、所有权与产蛋副作用',lambda i:i.startswith('GR6-K-')),
('U02','战斗对象与精神香草消费者',lambda i:i.startswith('GR6-C-')),
('U03','钓鱼条件抽样与解释器计数',lambda i:i.startswith('GR6-O-')),
('U04','AI失败门、评分异常与定位',lambda i:'CA-' in i),
('U05','招式行动清理、状态及后期目标',lambda i:i.startswith('R6-CM-')),
('U06','作者内容控件及转换工具',lambda i:i.startswith('R6-B-') or i.startswith('R6-DX-E')),
('U07','动画编辑与播放请求',lambda i:i.startswith('R6-DX-AN-')),
('U08','Debug入口、反馈及日志',lambda i:i.startswith('R6-DX-DEBUG-')),
('U09','编译入口、缓存与注释解析',lambda i:i.startswith('R6-DX-COMP-')),
('U10','捕获、Summary及招式回忆UI',lambda i:i.startswith('R6-UI-')),
('U11','存储导航及图鉴形态选择',lambda i:i.startswith('UI-ST-')),
('U12','背包提示与BP商店',lambda i:i.startswith('GR6-UI-BAG-')),
('U13','设施、竞技场、宫殿及活动模式保存',lambda i:i.startswith('GR6-F-')),
('U14','本地化、默认数据、指标及空Flags',lambda i:i.startswith('R6-D-')),
]
batches=[]
assigned={}
for num,title,pred in groups:
    items=[x for x in required if pred(x['id'])]
    bid='R6-'+num
    for x in items:
        assert x['id'] not in assigned,(x['id'],bid)
        assigned[x['id']]=bid
        x['dependencies_and_receivers']['primary_batch']=bid
        x['dependencies_and_receivers']['author_entry']=bid+'-A'
        x['dependencies_and_receivers']['independent_reviewer_entry']=bid+'-R'
    writes=sorted({p for x in items for p in x['minimum_revision_contract']['candidate_formal_write_set']})
    reads=sorted({p for x in items for p in x['minimum_revision_contract']['read_only_source_set']})
    batches.append({'id':bid,'title':title,'required_ids':[x['id'] for x in items],
                    'frozen_main':'8ea169fbd0f33f378b5d732fd6bea59e854e04a6',
                    'frozen_reference':'8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b',
                    'candidate_only_write_directory':'<update-root>/candidates/'+bid+'/',
                    'candidate_formal_paths':writes,'read_only_reference_paths':reads,
                    'additional_read_set':['本批逐ID原证据/反证全文及当前正式全文','源上下文和必要生产—消费—显示—保存链','本批实际受影响R1–R5资格span、消费者与共享合同'],
                    'author':{'logical_id':bid+'-A','requested_model':'gpt-6.1-sol','effort':'xhigh','tier':'default','speed':'default','fast':False,'platform_task_id':'NOT_STARTED'},
                    'reviewer':{'logical_id':bid+'-R','requested_model':'gpt-6.1-sol','effort':'ultra','tier':'default','speed':'default','fast':False,'independence':'非作者；曾写具体规格者不得唯一终裁','platform_task_id':'NOT_STARTED'},
                    'blocking_author_dependencies':[],
                    'nonblocking_domain_dependencies':{x['id']:x['dependencies_and_receivers']['original_dependencies'] for x in items},
                    'scope_contracts':items,
                    'candidate_pass':'逐ID源事实、前提、反例、正常/取消/失败前缀与保留scope均精确；补正文/附表/向量/消费者；候选不是正式接受。',
                    'integrated_acceptance':'R6-I唯一接收正式文件；每份共享文件收齐所有候选后独立全文回源与接口复验，核实际写入和历史精确回归。',
                    'closure_gate':['candidate_non_author_PASS','unique_writer_actual_integration','shared_full_file_non_author_PASS','direct_and_transitive_interface_acceptance','precise_historical_regression','formal_acceptance','CLOSED_registration'],
                    'policy_limits':'不等源缺陷永久兼容决定、不把宿主未知修成已验证；optional/policy/limit不进本批必修。',
                    'state':'PLANNED_UPDATE_NOT_STARTED'})
assert set(assigned)=={x['id'] for x in required}
conflicts=[]
file_receivers={}
for b in batches:
    for p in b['candidate_formal_paths']:
        file_receivers.setdefault(p,[]).append(b['id'])
for ai,a in enumerate(batches):
    for b in batches[ai+1:]:
        paths=sorted(set(a['candidate_formal_paths'])&set(b['candidate_formal_paths']))
        if paths:conflicts.append({'from':a['id'],'to':b['id'],'paths':paths,'conflict':'would conflict if writing actual formal file','mitigation':'independent candidate mirrors; R6-I sole actual writer; integrated full-file reviewer'})
deps=[]
for b in batches:
    deps.extend([{'from':b['id']+'-A','to':b['id']+'-R','kind':'candidate_review','blocking':True},
                 {'from':b['id']+'-R','to':'R6-I','kind':'candidate_acceptance','blocking':True}])
for p,owners in sorted(file_receivers.items()):
    for b in owners:deps.append({'from':b,'to':'R6-I:FILE:'+p,'kind':'shared_candidate_receive','blocking_closure':True,'blocking_author':False})
deps.extend([{'from':'R6-I','to':'R6-X','kind':'actual_integrated_non_author_global_review','blocking':True},
             {'from':'R6-X','to':'R6-I:ACCEPT','kind':'formal_acceptance','blocking':True},
             {'from':'R6-I:ACCEPT','to':'R6-I:CLOSED','kind':'final_registration_after_all_dependencies','blocking':True}])
put('findings/normative-records.json',records)
put('handoff/batch-assignment.json',{'schema':'r6.batch.v1','required_count':len(required),'batches':batches,'unique_primary_batch':assigned,
 'shared_receivers':file_receivers,'formal_file_solewriter':{p:'R6-I' for p in file_receivers},
 'public_admin_solewriter':'R6-I','first_wave_all_independent_candidate_batches':[b['id'] for b in batches],
 'first_wave_count':len(batches),'known_current_collaboration_capacity':4,'root_active_author_capacity':3,
 'future_cli_parallel_capacity':'UNVERIFIED; start within verified available resources, not an unlimited launcher promise',
 'update_started':False})
put('handoff/dependency-graph.json',{'schema':'r6.dependencies.v1','edges':deps,'author_blocking_interbatch_edges':[],
 'reason':'各批依赖已冻结的本轮事实，可独立产候选；组合、共享接收、非作者验收及历史回归仍阻塞正式关闭。','update_started':False})
put('handoff/file-conflict-graph.json',{'schema':'r6.file-conflicts.v1','edges':conflicts,'file_receivers':file_receivers,
 'no_direct_parallel_formal_writes':True,'unique_actual_formal_writer':'R6-I','candidate_mirrors_are_isolated':True})
print(json.dumps({'required':len(required),'batches':len(batches),'counts':{b['id']:len(b['required_ids']) for b in batches},'formal_candidate_paths':len(file_receivers),'file_conflict_edges':len(conflicts)},ensure_ascii=False))
