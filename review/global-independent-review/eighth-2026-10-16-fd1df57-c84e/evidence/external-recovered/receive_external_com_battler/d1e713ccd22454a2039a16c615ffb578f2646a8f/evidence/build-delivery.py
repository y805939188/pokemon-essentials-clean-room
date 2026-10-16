"""Freeze exact unresolved objects and dispatch contracts; grants no semantic credit.

Only writes below this task. Does not import or execute recovered code.
The eight analyses are separately hand-authored in finite-analysis.json.
"""
from pathlib import Path
import collections
import datetime
import hashlib
import json
import subprocess

TASK = Path(__file__).resolve().parent.parent
ROOT = TASK.parent.parent
REPO = ROOT.parents[2]
CONTRACT = '40f45dddcdea5522b4bf7d0fea1a0f74f7d3d232'
TARGET = '5cf9503a99a855c06a8ac9c932e6778b57e71049'
SOURCE = TASK / 'inputs/target-5cf9503a'
NOW = datetime.datetime.now(datetime.timezone.utc).isoformat()

def read(path):
    return json.loads(path.read_text())

def write(path, value):
    assert path.is_relative_to(TASK)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')

def identity(path):
    data = path.read_bytes()
    return {'path': str(path.relative_to(REPO)), 'bytes': len(data),
            'sha256': hashlib.sha256(data).hexdigest(),
            'blob_content_id': hashlib.sha1(f'blob {len(data)}\0'.encode()+data).hexdigest()}

def object_identity(obj):
    data = json.dumps(obj, ensure_ascii=False, separators=(',', ':')).encode()
    return {'canonical_json_bytes': len(data), 'canonical_json_sha256': hashlib.sha256(data).hexdigest(),
            'encoding': 'UTF-8 json.dumps ensure_ascii=False separators=(comma,colon); original field order'}

forward = read(SOURCE/'forward-mapping.json')
reverse = read(SOURCE/'reverse-mapping.json')
interfaces = read(SOURCE/'interfaces.json')
ids = read(SOURCE/'identities.json')
original_readset = read(ROOT/'delegation/readsets/receive_external_com_battler.complete.json')
manual = read(TASK/'evidence/finite-analysis.json')
facts = forward['consumer_facts']
checked = {x['id']: x for x in manual['records']}
compounds = forward['compounds']
children = [c for x in compounds for c in x['children']]
reverse_children = [c for x in reverse['clause_groups'] for c in x['subassertions']]
assert len(compounds)==289 and len(children)==810 and len(reverse_children)==160
assert len({x['semantic_family'] for x in compounds})==92
assert len({x['id'] for x in children})==810
assert len(facts)==24 and len(checked)==8

# Exact workload partition: first file divided only between whole structures.
jobs = []
first = [x for x in compounds if x['file_number']==1]
cut = max(x['source']['ranges'][-1][1] for x in first if x['source']['ranges'][-1][1] <= 400)
next_start = min(x['source']['ranges'][0][0] for x in first if x['source']['ranges'][0][0] > cut)
for label, selection, span in [
    ('P01A', [x for x in first if x['source']['ranges'][-1][1]<=cut], [1,next_start-1]),
    ('P01B', [x for x in first if x['source']['ranges'][0][0]>=next_start], [next_start,777])]:
    jobs.append({'id':label,'kind':'PRIMARY_SOURCE_AND_ASSIGNED_REVERSE', 'compounds':selection,
                 'primary_source_ranges':[span]})
for n in range(2,11):
    cs=[x for x in compounds if x['file_number']==n]
    parent=next(x for x in ids['files'] if x['evidence_id']==cs[0]['source']['evidence_id'])
    jobs.append({'id':f'P{n:02d}','kind':'PRIMARY_SOURCE_AND_ASSIGNED_REVERSE','compounds':cs,
                 'primary_source_ranges':[[1,parent['line_count']]]})
owner={c['id']:j['id'] for j in jobs for c in j['compounds']}
assert len(owner)==289
reverse_owner={}
for c in reverse_children:
    targets=[x['compound_id'] for x in c['primary_facets'] if x['compound_id'] in owner]
    reverse_owner[c['id']]=owner[min(targets)] if targets else 'H01'

core=[x['id'] for x in facts if x['id'].startswith('RX-CORE-') or x['id']=='RX-CLAUSES']
data=['RX-DATA-ID','RX-ABILITY-SCHEMA','RX-ITEM-SCHEMA']
persistent=['RX-POKEMON-SET','RX-POKEMON-PP','RX-SHADOW-HP','RX-SHADOW-BATTLER','RX-PEER']
for label, selected, title in [('R01',core,'CORE必要定义与消费者'),('R02',data,'身份及Ability/Item数据定义'),('R03',persistent,'持久状态、Shadow与Peer接收')]:
    jobs.append({'id':label,'kind':'FINITE_RECEIVER_SOURCE_AND_JOIN','title':title,
                 'consumer_fact_ids':selected, 'compounds':[]})
jobs.append({'id':'H01','kind':'HISTORY_COUNTERS_METADATA_AND_CUMULATIVE_JOIN','compounds':[],
             'consumer_fact_ids':list(checked),
             'work':'两完整独立counter、适用历史资格、184行阅读声称/别名/外壳、四中央接口、展示IF04与prior provider报告全文接收；八事实可复用已读必要定义，仍核全部producer并累计接合。'})
assert len(jobs)==15
fact_owner={f:j['id'] for j in jobs for f in j.get('consumer_fact_ids',[])}
assert set(fact_owner)=={x['id'] for x in facts} and len(fact_owner)==24

catalog=[]
for i,c in enumerate(compounds):
    catalog.append({'id':c['id'],'population':'compound','pointer':f'/compounds/{i}',
                    'file':'forward-mapping.json','identity':object_identity(c),
                    'source':c['source'],'family':c['semantic_family'],
                    'child_ids':[x['id'] for x in c['children']], 'owner':owner[c['id']],
                    'necessary_consumers':c['necessary_consumers'],
                    'formal_clause_ids':[x['clause_id'] for x in c['formal_relations']],
                    'status':'OPEN_FULL_RECEPTION_NOT_COMPLETED'})
for i,g in enumerate(reverse['clause_groups']):
    catalog.append({'id':g['id'],'population':'selected_formal_group','file':'reverse-mapping.json',
                    'pointer':f'/clause_groups/{i}', 'identity':object_identity(g), 'formal':g['formal'],
                    'subassertion_ids':[c['id'] for c in g['subassertions']],
                    'primary_owners':{c['id']:reverse_owner[c['id']] for c in g['subassertions']},
                    'status':'OPEN_FULL_RECEPTION_NOT_COMPLETED'})

field_purposes={
 'forward-mapping.json':{
  '/structures/*':'完整结构身份与原作者阅读声称；kind/name/范围/child关系冻结，原FULL_READ不继承。',
  '/compounds/*/source':'固定源身份/精确范围，身份用途；真正函数完整性另审。',
  '/compounds/*/children/*/assertion':'完整当前业务断言，必须逐值实读与独立比较；本次未完成。',
  '/compounds/*/children/*/premises':'完整适用前提，业务文字，不可改为locator。',
  '/compounds/*/formal_relations/*':'clause定位为追溯；relation/reason/acceptance为语义关系和作者声称，仍OPEN。',
  '/compounds/*/necessary_consumers':'必要关系集合，须逐事实接合，不能由ID存在签收。',
  '/compounds/*/finite_interfaces':'接口归属边，保留全值，不授接收信用。',
  '/compounds/*/pending_counterevidence':'必须保留的反证状态/条件，仍OPEN。',
  '/consumer_facts/*':'24个完整对象文字已读；八个完成有限必要源码比较，其余16的源码支持未独立全文接收。',
  '/legacy_fact_id_crosswalk/*':'精确旧新别名索引保留；reason/后继更正需接收，旧88不能再加计为事实。',
  '/load_envelopes/*':'十外壳处置声称，仍须对照源文件剩余行；不是本次全文通过。',
  'OTHER_FIELDS':'完整原值冻结；schema/ID/hash仅身份，状态/分母/资格为原作者有限声称，不自动采信。'},
 'reverse-mapping.json':{'/clause_groups/*/subassertions/*':'全部160完整业务文字、premise、foreign_facet、primary_facets、disposition、consumer关系必须实读；未接收。',
  'OTHER_FIELDS':'原ID/定位/范围作身份；scope/denominator/warning均已读，不能把160扩成全formal分母。'},
 'interfaces.json':{'/interfaces/*/local_compound_ids':'四个完整ID索引228/80/147/190；精确保留，不含业务正文，不赋新语义阅读信用。',
  'OTHER_FIELDS':'所有非该索引的完整业务值已呈现阅读；接口整体仍未签。'},
 'identities.json':{'/files/*':'184个完整身份记录作身份索引冻结；purpose字段的范围分类仍是作者声称。本次只对31个必要单元所在父文件独立核值。'},
 'reading-ledger.json':{'/files/*':'184条原作者范围/资格声称是待接收材料；没有以其FULL_READ获得本次源码FULL。',
  'OTHER_FIELDS':'gaps/history/counts/acceptance/scope完整已读；log_evidence完整值已呈现，IO原始平台流没有独立完整导出。'},
 'proposals.json':{'/records/*':'两完整对象所有字段已读；完整反证原件及历史资格仍OPEN。'},
 'progress.json':{'ALL':'全文已读，配置/时间/原作者进度声称按行政及资格事实处置，不继承语义信用。'},
 'publication.json':{'ALL':'全文已读；原transport身份和失败/更正保留，只供身份/工具证据。'},
 'validation.json':{'ALL':'全文已读；工具PASS仅完整性及写集，不能证明本次语义PASS。'},
 'review.md':{'ALL':'全文已读；完整本地工作范围、错误后继、更正和未决保留，不继承作者阅读。'} }

write(TASK/'frozen-denominator.json',{
 'schema':'r8-com-battler-frozen-reception-denominators/v1','utc':NOW,
 'fixed_contract_commit':CONTRACT,'target_commit':TARGET,
 'target_checkout_tree':original_readset['target_checkout_tree'],
 'target_task_tree':original_readset['target_task_tree_observed_from_fixed_commit'],
 'inputs':original_readset['files'],'populations_separate_not_additive':forward['denominator'],
 'formal_population':reverse['denominator'],'consumer_fact_ids':[x['id'] for x in facts],
 'central_interface_ids':[x['id'] for x in interfaces['interfaces']],
 'additional_history_join':interfaces['additional_finite_joins'],
 'presentation_interface':interfaces['presentation_contract_object_actually_read'],
 'proposal_ids':[x['id'] for x in read(SOURCE/'proposals.json')['records']],
 'catalog':catalog,'field_purposes':field_purposes,
 'exact_original_payloads_preserved':'inputs/target-5cf9503a; original raw byte identities are not object canonical hashes',
 'credit':'STRUCTURAL_FREEZE_ONLY; no generated object receives semantic credit'})

# Build ready-to-dispatch contracts with complete source object fields, never summaries.
common_text='\n\n'.join((ROOT/x).read_text() for x in [
 'delegation/prompts/receive_external_com_battler.md','inputs/eighth-global-review-prompt.md','inputs/review-SKILL.md'])
agents=(REPO/'AGENTS.md').read_text()
dispatch=[]
for j in jobs:
    jid=j['id']; out=TASK/'splits'/jid
    own_reverse=[c['id'] for c in reverse_children if reverse_owner[c['id']]==jid]
    cs=j['compounds']; needed={f for c in cs for f in c['necessary_consumers']} | set(j.get('consumer_fact_ids',[]))
    selected_groups=[g for g in reverse['clause_groups'] if any(
        c['id'] in own_reverse for c in g['subassertions']) or
        g['id'] in {r['clause_id'] for c in cs for r in c['formal_relations']}]
    subset={
      'schema':'r8-com-battler-exact-split-contract/v1','id':jid,'fixed_contract_commit':CONTRACT,
      'fixed_target_commit':TARGET,'original_complete_readset':original_readset,
      'exclusive_future_write_set':str((out/'result').relative_to(ROOT))+'/',
      'dispatch_status':'PLANNED_CONTEXT_NOT_CREATED','actual_context':'UNVERIFIED_NOT_LAUNCHED',
      'must_not_be_author_context':'01a143b2-64d2-72d2-ae62-0058869a3010',
      'primary_compounds':cs,'primary_child_ids':[c['id'] for x in cs for c in x['children']],
      'assigned_reverse_child_ids':own_reverse,'complete_required_formal_group_objects':selected_groups,
      'primary_source_ranges':j.get('primary_source_ranges',[]),
      'full_required_consumer_fact_objects':[x for x in facts if x['id'] in needed],
      'consumer_primary_ids':j.get('consumer_fact_ids',[]),
      'full_identity_index':ids,'full_interfaces':interfaces,
      'mandatory_supplement':read(ROOT/'delegation/battler-reception-mandatory-supplement.v1.json'),
      'required_companion_paths':['adjudication/root-battler-eight-consumer-facts-reception.v1.json',
        'adjudication/root-battler-eight-facts-exact-inputs.v1.json'],
      'work':j.get('work',j.get('title',j['kind'])),
      'credit_rule':'分片生成reading0；所有原对象业务值完整保留。读完整必要定义/消费者及B8条款，不因未分配主责跳过本片必要上下文。只签自己已实际读的对象。跨片只导航不能继承PASS。',
      'final_owner':'Root coordinator; this split cannot sign global or parent task final',
      'UPDATE_NOT_STARTED':True}
    if jid=='H01':
        subset['additional_complete_inputs']=[
          'tasks/counter_ecb_mode_existing_core/counterreview.json',
          'tasks/counter_ecb_transform_existing_crea/counterreview.json',
          'adjudication/root-gr8-ecb-001-reception.v1.json',
          'adjudication/root-gr8-ecb-002-reception.v1.json',
          'adjudication/root-battler-core-crea-finite-receptions.v1.json',
          'adjudication/root-battler-three-schema-facts-reception.v1.json',
          'adjudication/root-battler-pbs-backup-current-delivery-qualification.v2.json']
        subset['whole_target_metadata_files']=['identities.json','reading-ledger.json','interfaces.json',
                                               'proposals.json','progress.json','publication.json','validation.json','review.md']
        subset['complete_forward_admin_objects']={k:forward[k] for k in ['structures','legacy_fact_id_crosswalk','load_envelopes']}
    write(out/'readset.json',subset)
    prompt=(f'# receive_external_com_battler 容量拆分 {jid}\n\n'
      f'父任务尚为INCOMPLETE。你只负责本片；输入是固定合同{CONTRACT}与固定目标{TARGET}。'
      f'先完整阅读本文件全部合同和同目录readset.json，再执行。唯一写集为{str((out/"result").relative_to(ROOT))}/。'
      '不得spawn，不整改、不合并main，不在公共或他人目录写入。父主审实际派发后才能登记真实上下文；'
      'PLANNED不是启动。完整语义、必要caller/receiver、正式条款、失败/正常/取消/部分提交、历史资格逐对象给证据。'
      '主责分母和完整对象以readset为准；其余必要上下文仍须完整实读，不能只引用locator。'
      '八事实后继强制更正必须全文接收；源码原作者不作自己反证。必要对象未接则INCOMPLETE。'
      '本片子审者只交付result，由父协调者统一commit/push到原指定专用报告分支；不另建发布分支，不自行commit/push，不修改本合同。根最终签收由主审负责。\n\n'
      '以下保留父接收合同、全局合同、skill及AGENTS全文；本片精确写集收窄父写集，其余要求不放宽。\n\n'
      +common_text+'\n\n# 适用AGENTS全文\n\n'+agents)
    (out/'prompt.md').write_text(prompt)
    dispatch.append({'id':jid,'status':'PLANNED_CONTEXT_NOT_CREATED',
      'prompt':identity(out/'prompt.md'),'readset':identity(out/'readset.json'),
      'exclusive_write_set':subset['exclusive_future_write_set'],
      'compound_ids':[c['id'] for c in cs],'source_children':len(subset['primary_child_ids']),
      'reverse_child_ids':own_reverse,'consumer_primary_ids':j.get('consumer_fact_ids',[])})

write(TASK/'split-dispatch.json',{'schema':'r8-com-battler-capacity-split-dispatch/v1',
 'utc':NOW,'status':'INCOMPLETE_CAPACITY_SPLIT_READY_FOR_PARENT_DISPATCH',
 'actual_new_contexts_created_here':0,'spawn_calls':0,
 'reason':'完整主责需要810当前子断言、160反向子断言、各完整源体与必要消费者/历史。单个本次上下文尚未实际完成这些实读；已有31必要单元和八事实有限比较保留。不得以压缩/模板/transport代替。本合同依用户容量不足时给精确拆分合同的授权交父实际派发。',
 'jobs':dispatch,'partition':{'compound_units':len(owner),'source_children':len(children),
 'reverse_children':len(reverse_owner),'foreign_facets':sum('foreign_facet' in c for c in reverse_children),
 'consumer_facts':len(fact_owner),'compound_overlap':0,'reverse_overlap':0,'consumer_primary_overlap':0},
 'completion':'全部片必要对象签收后，实际非作者父协调者核累计接口/历史/冲突与保留，才能给READY_FOR_ROOT_TASK_FINAL_ACCEPTANCE。',
 'UPDATE_NOT_STARTED':True})

reception=[]
for f in facts:
    record={'id':f['id'],'original_complete_object':f,
      'target_file':'forward-mapping.json','pointer':f"/consumer_facts/{facts.index(f)}",
      'raw_identity':next(x for x in original_readset['files'] if x['relative_to_target_task']=='forward-mapping.json'),
      'fact_text':'FULL_OBJECT_READ','final_consumer_join':'OPEN_PRODUCER_CONTRIBUTIONS_NOT_FULLY_RECEIVED',
      'future_primary':fact_owner[f['id']]}
    if f['id'] in checked:
        record['independent_finite_analysis']=checked[f['id']]
        record['source_support']='COMPLETE_NECESSARY_UNITS_ACTUALLY_READ_WITH_QUALIFICATIONS'
    else:
        record['source_support']='OPEN_AVAILABLE_DEFINITIONS_NOT_FULLY_READ_HERE'
        record['reason']='本次已读完整原事实文字，未全文接收其全部必要定义和当前条款；原作者/root有限旧收据不转移FULL信用。'
    reception.append(record)
write(TASK/'reception-ledger.json',{'schema':'r8-com-battler-independent-reception/v1',
 'status':'INCOMPLETE','receiver':'current receive_external_com_battler execution; actual opaque UUID UNVERIFIED',
 'author_actual_context':'01a143b2-64d2-72d2-ae62-0058869a3010',
 'independence':'当前委派接收执行未编写目标报告；来源线程ID不作为自身平台UUID，也不把角色名当新增独立票。',
 'facts':reception,'complete_producer_children_received':0,'complete_selected_formal_children_received':0,
 'source_child_statuses':[{'id':c['id'],'status':'OPEN','future_primary':owner[x['id']],
   'original_pointer':f'/compounds/{i}/children/{k}'} for i,x in enumerate(compounds) for k,c in enumerate(x['children'])],
 'reverse_child_statuses':[{'id':c['id'],'status':'OPEN','future_primary':reverse_owner[c['id']],
   'original_pointer':f'/clause_groups/{i}/subassertions/{k}'} for i,x in enumerate(reverse['clause_groups']) for k,c in enumerate(x['subassertions'])],
 'available_not_received':'所有未接对象均可得；不是材料limit。宿主行为未执行另列。',
 'UPDATE_NOT_STARTED':True})

write(TASK/'interfaces.json',{'schema':'r8-com-battler-interface-reception/v1',
 'four_full_original_interfaces':interfaces['interfaces'],
 'additional_history_join':interfaces['additional_finite_joins'],
 'presentation_IF04':interfaces['presentation_contract_object_actually_read'],
 'status':'OPEN_FULL_PRODUCER_AND_RECEIVER_JOIN_NOT_COMPLETE',
 'qualified_definitions':[x['id'] for x in manual['records']],
 'root_prior_qualified_receipt':'At fixed40f45ddd root has24/24 finite facts joined with mandatory qualifications; that is not this context full810/160 reception.',
 'consumer_primary_partition':fact_owner,'business_execution':'NOT_EXECUTED','UPDATE_NOT_STARTED':True})

root_receipts=[ROOT/f'adjudication/root-gr8-ecb-{n:03d}-reception.v1.json' for n in [1,2]]
write(TASK/'proposal-counters.json',{'schema':'r8-com-battler-proposal-reception/v1',
 'original_proposals':read(SOURCE/'proposals.json'),'original_proposal_read':'ALL_FIELDS_FULL_TEXT_READ',
 'existing_root_receipts':[{'identity':identity(p),'complete_receipt':read(p)} for p in root_receipts],
 'receipt_read':'BOTH_ROOT_BOUNDED_RECEIPTS_FULL_TEXT_READ; complete original counter packages NOT_YET_READ_HERE',
 'independent_assessment':[
  {'id':'GR8-ECB-001','meaning':'正常失败可以保留已经发生的PP/历史/模式标志，EOR无来源Octolock再读当前模式，模式真/假使Contrary分支不同。',
   'strongest_no_required':'若WP40失败分支、WP42无隐含清零、WP44当前模式门组合已完整规定trace，额外联合向量的教学价值不构成必修改稿。root现有有限NO_REQUIRED与原提案自称未证缺口一致。',
   'open':'完整非作者counter八节/源证据/当前历史资格尚未实读，不在本次新增独立裁决。'},
  {'id':'GR8-ECB-002','meaning':'奇妙空间下先读T交换后的100/60写入U原字段，再由U getter交换回60/100；期限结束仅撤读取交换，U保100/60。',
   'strongest_no_required':'已有当前值复制、原字段写入、读取交换、阶级标签不换和无补偿逆写若组合推出结果，无需强制新增组合用例。root有限NO_REQUIRED不能扩成所有变身/UI通过。',
   'open':'完整非作者counter八节/实际copy与damage/UI消费者及历史资格尚未全文实读。'}],
 'new_required':0,'new_optional':0,'new_independent_final_decisions':0,
 'final_state':'OPEN_FOR_FULL_RECEPTION; preserve prior bounded NO_REQUIRED, do not reopenR7_27',
 'future_primary':'H01','execution':'NOT_EXECUTED','UPDATE_NOT_STARTED':True})

units=read(ROOT/'adjudication/root-battler-eight-facts-exact-inputs.v1.json')['complete_necessary_units']
write(TASK/'reading-ledger.json',{'schema':'r8-com-battler-receiver-actual-reading/v1','utc':NOW,
 'control_read':[{'path':p,'status':'FULL_TEXT_READ'} for p in [
 'AGENTS.md','delegation/prompts/receive_external_com_battler.md',
 'delegation/readsets/receive_external_com_battler.complete.json','inputs/eighth-global-review-prompt.md',
 'inputs/review-SKILL.md','delegation/helpers/recover_transport.py',
 'delegation/battler-reception-mandatory-supplement.v1.json']],
 'mandatory_companions':'BOTH_FULL_TEXT_READ_WITH_ALL31UNITS; exact frozen aliases are identity duplicates, no second credit',
 'complete_necessary_units':[{'index':i,'source_identity':u['source_identity'],'range':u['range'],
   'status':'ACTUAL_FULL_SELECTED_UNIT_TEXT_READ','raw_input_pointer':f'/complete_necessary_units/{i}',
   'original_path':'adjudication/root-battler-eight-facts-exact-inputs.v1.json'} for i,u in enumerate(units)],
 'actual_output_sequence':[
  {'query':'global prompt+skill+helper whole','result':'TRUNCATED; omitted global section repaired with numbered lines130–240; skill/helper shown complete'},
  {'query':'mandatory units range(0,6)','result':'COMPLETE'},
  {'query':'mandatory units range(6,15)','result':'COMPLETE'},
  {'query':'mandatory units range(15,31)','result':'TRUNCATED middle; units24–26 separately reread complete; 15–23 and27–30 visible complete'},
  {'query':'mandatory units range(24,27)','result':'COMPLETE_REPAIR'},
  {'query':'schema samples/selected compound objects','result':'TRUNCATED; no full-compound or formal-group credit assigned'},
  {'query':'all24consumer_facts compact JSON','result':'COMPLETE'},
  {'query':'four interfaces excluding local_compound_ids identity indexes','result':'COMPLETE; indexes fully frozen but no semantic credit'},
  {'query':'proposals.json+root receipts001/002+paired receipt','result':'COMPLETE'},
  {'query':'root finite CORE/CREA/schema/backup receipts','result':'COMPLETE receipts; original provider packages not read'},
  {'query':'progress/validation/publication/top metadata','result':'COMPLETE shown scopes; 184 row reading claims remain OPEN'}],
 'platform_raw_transcript_export':'UNVERIFIED; conversation tool responses are actual I/O, no invented external log ID',
 'declared_author_ledger_preserved':'inputs/target-5cf9503a/reading-ledger.json; no transferred source credit',
 'counts':{'mandatory_complete_units':31,'whole_source_parents':2,
   'whole_source_parent_ids':['R4','R5'],'whole_original_fact_texts':24,
   'finite_source_fact_comparisons':8,'complete_primary_child_reception':0,
   'complete_reverse_child_reception':0,'complete_central_interface_reception':0},
 'primary_source_selected_ranges':{
   'E006':{'read':[[107,112],[166,200],[248,288],[344,357],[421,435]],
           'unread':[[1,106],[113,165],[201,247],[289,343],[358,420],[436,777]],
           'read_lines':111,'total_lines':777},
   'E008':{'read':[[1,36]],'unread':[[37,328]],'read_lines':36,'total_lines':328},
   'other_eight_primary_files':'Entire parent ranges unread in this context; original identities.json carries exact line counts. Source schemas/fact text are not source-body credit.',
   'total_primary_read_lines':147,'total_primary_unread_lines':4499,'total_primary_lines':4646},
 'limits':{'L_HOST':'Game/native graphics/audio/real save/Demo NOT_EXECUTED; no pixel/timing/game-result assertion',
   'L_MAC':'Historical Mac worktrees/protected-byte inventory not mounted; cloud identities checked separately',
   'L_CONFIG':'model/effort/tier/speed/Fast/opaque_UUID each UNVERIFIED'},
 'capacity_remaining':'Exact unresolved objects and actual not-started split contracts in split-dispatch.json',
 'UPDATE_NOT_STARTED':True})

print(json.dumps({'jobs':len(jobs),'compounds':len(owner),'children':len(children),
 'reverse_children':len(reverse_owner),'consumer_primary':len(fact_owner),
 'source_units_actually_read':31,'finite_source_comparisons':8,
 'final_status':'INCOMPLETE','mechanical_generation_semantic_credit':0}))
