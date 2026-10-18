"""Assemble the actually reviewed finite handoff; arithmetic creates no reading credit."""
import datetime
import json
from pathlib import Path

T = Path(__file__).resolve().parent
NOW = datetime.datetime.now(datetime.timezone.utc).isoformat()
READY = 'READY_FOR_ROOT_TASK_FINAL_ACCEPTANCE'
def load(p): return json.loads((T/p).read_text())
def save(p,d): (T/p).write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')

a=load('continuation/received-parts/parent-acceptance.json')
rd=load('reading-ledger.json'); f=load('frozen-denominator.json'); q=load('reception-ledger.json')
it=load('interfaces.json'); pc=load('proposal-counters.json')
own={r['id'] for r in rd['literal_record_reads']}; named={r['id']:r for r in a['records']}
assert len(own)==433 and len(named)==10264 and not own&set(named)
assert own|set(named)=={r['id'] for r in f['primary_objects'] if r['kind']=='record'}
pbs=load('continuation/pbs-field-binding/actual-reader-bindings.json')
assert len(pbs['rows'])==11647 and pbs['counts']=={'new_literal_occurrences':150,'absent':3330,'corpus_literals_resolved':8167}
assert not any(r['status'].startswith('PENDING') for r in pbs['rows'])
purpose=load('continuation/target-payload-purpose.json')
assert len(purpose['entries'])==213 and not any(r.get('necessary_pending_reader_ids') for r in purpose['entries'])

for r in a['records']:
    r['interfaces_final']=True
    r['signature_scope']='receiver finite target interfaces only; root/global final is separate'
a.update(parent_seven_interfaces_complete=True,root_final_signed=False,status=READY,
    distinct_primary_pairs_with_parent=10697,distinct_primary_fields_with_parent=21394,
    remaining_necessary_record_ids=[],semantic_credit_from_mechanical_checks=0)
save('continuation/received-parts/parent-acceptance.json',a)

for r in f['primary_objects']:
    r.setdefault('initial_full_chain_reception',r.get('full_chain_reception'))
    r.setdefault('initial_reason',r.get('reason'))
    r['reason']='Current finite producer/default/consumer/formal scope received; personal literal reading and named-reader ownership stay distinct. Root/global final is separate.'
    if r['kind']=='record':
        if r['id'] in named:
            n=named[r['id']]
            r['named_reader_reception']={'part':n['part'],'context':n['reader_context'],'status':n['reception'],'parent_literal_reread':False}
        r['full_chain_reception']='COMPLETE_VALID_FINITE_TARGET_RECEPTION'
        r['current_reception_evidence']='continuation/received-parts/parent-acceptance.json + interfaces.json'
    else:
        r['full_chain_reception']='COMPLETE_HEADER_FORMAT_PURPOSE_RECEPTION'
    r['root_global_final_signed']=False
for r in f['fact_groups']:
    r.setdefault('initial_status',r['status'])
    r['status']='COMPLETE_VALID_FINITE_FACT_GROUP_RECEIVED'
    r['evidence']='continuation/original-primary-semantics.factored.json + continuation/received-parts/parent-acceptance.json + interfaces.json'
for r in f['pbs35']:
    r['current_necessary_field_reception']='COMPLETE_FINITE_FIELDS_AND_ACTIVATION_ONLY'
    r['current_evidence']='continuation/pbs-field-binding/actual-reader-bindings.json'
f['pbs_value_bundle'].setdefault('initial_status',f['pbs_value_bundle']['status'])
f['pbs_value_bundle']['status']='COMPLETE_VALID_FINITE_LOCALIZATION_PROJECTION_RECEIVED'
f['pbs_value_bundle']['current_scope']='All eight original finite projections, envelopes and necessary field meanings received; full unrelated PBS record bodies are outside this scope.'
f['continuation_2']['historical_snapshot']=True
f['final_reception']={'status':READY,'primary_pairs':10697,'primary_fields':21394,'headers':18,
    'necessary_field_combinations':3324,'PBS_necessary_field_slots':11647,'necessary_unreceived':0,
    'actual_named_readers':{r['part']:r['reader_context'] for r in a['receipts']},
    'root_final_signed':False,'UPDATE_NOT_STARTED':True}
f['updated_utc']=NOW
save('frozen-denominator.json',f)

for r in rd['literal_record_reads']:
    r.setdefault('initial_disposition',r['disposition'])
    r['disposition']='COMPLETE_PERSONAL_LITERAL_READ_AND_FINITE_TARGET_CHAIN_RECEIVED'
rd['status']=READY; rd['updated_utc']=NOW
rd['named_record_reader_receptions'].update(pairs=10264,fields=20528,
    actual_contexts_from_coordinator={r['part']:r['reader_context'] for r in a['receipts']})
rd['counts'].update(primary_distinct_pairs_actually_read_or_received=10697,
    primary_distinct_fields_actually_read_or_received=21394,primary_pairs_still_unreceived=0,
    primary_fields_still_unreceived=0,primary_files_with_complete_literal_reader_coverage=18,
    primary_files_with_partial_literal_reader_coverage=0,primary_files_without_literal_reader_coverage=0,
    headers_read_or_received=18,headers_still_unreceived=0,complete_primary_chains_accepted=10697,
    reverse_mapping_objects_not_received=0)
rd['counts_qualification']='Personal literal fields remain433 pairs/866 fields. Named10264 pairs/20528 fields are actual other-reader receipts. Complete chains mean the target finite handoff, never global B8 approval.'
for r in rd['target_file_states']:
    e=next(x for x in purpose['entries'] if x['path']==r['path'])
    r['reception']=e['purpose'];r['necessary_pending_reader_ids']=[]
rd['independence']['global_context_count_delta']='ROOT_COORDINATOR_OWNED; no self-spawn or added ELR001 vote here'
rd['D_recovery']={'actual_reader':'01a144fc-df1d-7133-97ce-5d218016402d','commit':'477fb3ce438fe5462ee6901908cccc59977d4ba1',
    'receipt':'continuation/received-parts/recovery-D-validation.json','logical_D_count':1,
    'original_D_later_results':'same-ID dedup; conflicting ID freezes; no second record/vote',
    'definition_extent_correction':'D ledger1–64 is not complete generic4–68; parent prior actual1–108 supplies65–68, no retroactive D credit.'}
rd['final_qualification']='All adopted valid finite meanings actually received; broad peer bodies/tools not adopted retain explicit per-path reading scope. Original source/old statuses never converted into this receiver personal FULL.'
rd['continuation']['final_state']=READY
correction={'kind':'D recovery generic extent correction','proof':'D reading-ledger definition1–64 versus exact complete method4–68; parent prior actual1–108 reused, original D claim preserved.'}
if correction not in rd['failures_and_truncations']: rd['failures_and_truncations'].append(correction)
rd['continuation'].setdefault('initial_literal_record_counts_unchanged',rd['continuation']['literal_record_counts_unchanged'])
rd['continuation']['literal_record_counts_unchanged']='Parent personal433 unchanged; actual named A/B/C/D10264 received; union10697, no remaining record.'
rd['continuation']['latest_final_integration']='continuation/final-integration.md'
save('reading-ledger.json',rd)

scopes=[
 ('ELR-I01','当前语言/作者工具/125反向',
  '完整Intl823、KER-F102–112、WP08全文/LZ41及125条款398子断言接收；game→core→原输入、地图共享桶、空译、键/值分层、替换/格式异常和作者取消/覆盖/截断完整保留。',
  ['evidence/necessary-source/R-003_Intl_Messages.rb','continuation/kernel-localization-11.complete.json','continuation/links-and-reverse-validation.json']),
 ('ELR-I02','15生产者与编译阶段',
  '完整15消息生产者+3共同合同+TrainerType、WP04及必要编译定义接收；注册→终检/消息→保存/缓存前缀、set/add/default core过滤、当前语言独立性完整。D所列generic到64的缺口由父此前读至68的完整定义补足。',
  ['continuation/received/media-compiler-message-producers-contribution.json','continuation/reading-and-reception.addendum.json','continuation/received-parts/recovery-D-validation.json']),
 ('ELR-I03','35PBS必要字段与数据getter',
  '八数据源九事实/六家族schema-default-inheritance-getter和35上下文必要字段完成；13051原记录仅投影必要字段，3324不同组合11647字段槽：8167语料别名+150新字面槽+3330缺席，全有实际读者。8原包2339记录字段位置/有效RAW-BASE-DEFAULT引用吻合；备份激活和原始值/运行域分开。',
  ['continuation/pbs-envelope-and-family-fields.full.json','continuation/pbs-field-binding/provider-comparison.json','continuation/pbs-field-binding/actual-reader-bindings.json']),
 ('ELR-I04','全部记录/序列化有限接合',
  '18域10697对21394字段与18头完整读或接收；Parent433+A2756+B1620+C1061+恢复D4827严格无重叠。messages固定字节结构、5不等对及178字符串链接全文和原始字节接合；归档Main49与R Main60分列，未运行Marshal/宿主，不以默认英文材料推当前语言已加载。',
  ['continuation/received-parts/parent-acceptance.json','continuation/links-and-reverse-validation.json','continuation/target-view-reuse.json']),
 ('ELR-I05','36方法/63图像调用及UI消费者',
  '36完整方法63调用、UI36/Dex7/Core4、原四图像家族与Slot七角色有界接合；PictureSprite/EventScene、Mart先统计后余额、NearAlly对象参数/存活枚举以及ItemSprites157 EOF更正完成。名称/描述不是玩法证据，实际像素/字体/媒体未证。',
  ['reception-ledger.json#/image_callers','continuation/substantive-reception-2.md','continuation/direct-source-reception-2.json']),
 ('ELR-I06','保存/地图名/物品提示/语言入口',
  'SaveData/Value/SaveValues/StartGame/Load/SaveUI/Main和必要地图/物品完整方法、WP09及WP11/WP65/WP17相关有限条款接收。顺序回调、有限回退、语言整对象直写、可变地图字符串与add/message顺序保留；运行时选语言默认cancel0，和作者负取消码分开。',
  ['continuation/direct-source-reception-2.json','continuation/runtime-language-command-default.json','continuation/substantive-reception-2.md']),
 ('ELR-I07','目标历史资格与主审保留',
  '完整接收ELR-C07实际限定：L01–14、四历史范围报告、37-title/canonical/alias导航及已采用的optional/Float/policy/no-required后继；R6/C2原INCOMPLETE和未收原56/37正文不改写。标题无负证资格，R7的27不重开；ELR001完整独立反证/有限requiredP3支持保留，最终canonical/alias及根task-final仍由主审。',
  ['continuation/substantive-reception-2.md','proposal-counters.json','continuation/target-payload-purpose.json'])]
interfaces=[]
for ident,title,meaning,evidence in scopes:
    interfaces.append({'id':ident,'title':title,'status':'COMPLETE_VALID_FINITE_TARGET_RECEPTION',
        'current_complete_meaning':meaning,'actually_received':meaning,'evidence':evidence,
        'finite_reception_status':'COMPLETE_FOR_TARGET_VALID_FINITE_CONTRIBUTION','necessary_unreceived':[],
        'receiver_finite_reception_complete':True,'full_final_acceptance':False,
        'full_final_acceptance_scope':'Root/global final approval is exclusive to coordinator; this receiver signs only the declared finite target scope.',
        'root_final_signed':False,'UPDATE_NOT_STARTED':True})
it.update(status=READY,updated_utc=NOW,interfaces=interfaces,complete=7,partial=0,not_received=0,
    finite_contributions_complete=7,finite_contributions_pending=0,root_final_signature_transferred=False,
    complete_count_scope='Seven valid finite target contributions, including I07 historical qualifications; no global primary/body/canonical approval.')
save('interfaces.json',it)

q.update(status=READY,updated_utc=NOW,literal_primary_fields=rd['literal_record_reads'],
    named_reader_primary_fields={'receipt':'continuation/received-parts/parent-acceptance.json','pairs':10264,'fields':20528,'parent_personal_reading_transferred':False},
    primary_coverage={'personal':433,'received_from_named_readers':10264,'distinct_total':10697,'remaining':0},
    complete_primary_chain_count=10697,complete_primary_chain_count_qualification='Complete valid finite receiver chains; no root/global final signature.',
    finite_primary_record_contributions_read_or_received=10697,full_task_final_ready=True,root_final_signed=False,
    necessary_unread=0,necessary_unreceived=0,
    remaining_exact_objects={'primary_records':[],'primary_headers':[],'PBS_necessary_field_slots':[],
        'reverse_objects':[],'target_valid_semantic_purposes':[],'interfaces':[]},
    outside_adopted_finite_scope={'historical_case_bodies':'Original complete R6 effective56/R7 original37 case bodies not adopted/read by this receiver; original target C07 expressly retained these for history/root. No title-based negative or old PASS transfer.',
        'PBS_and_other_domains':'Non-localization PBS fields/whole compiled populations and wider UI/combat/world/native bodies are not approved by finite ELR receipt; exact named peer scope retained.',
        'tool_source':'Unexecuted original report helper bodies not promoted to reference/business authority; exact adopted output purposes in target-payload-purpose.json.'},
    unavailable_or_unverified_material={'private_IO':'Full private platform event stream/individual old per-read UTC not exported; UNVERIFIED rather than reconstructed.',
        'runtime':'Reference/model/game/Demo/native/media/save-replay NOT_EXECUTED; actual host/font/pixel/loaded class data outcomes remain unverified.'},
    capacity_boundary='No capacity/environment blocker remains for the finite target. Recovery D received; original D later output same-ID dedup only. Root final remains exclusive.')
q['pbs_literal_reader_binding'].update(corpus_literal_slots_resolved=8167,corpus_literal_slots_pending_D=0)
q['continuation']['final_state']=READY
q['continuation'].setdefault('initial_status',q['continuation']['status'])
q['continuation']['status']=READY
q['continuation']['latest_final_integration']='continuation/final-integration.md'
q['continuation']['workers_started']='Coordinator dispatched original four and a replacement D recovery; credited logical groups A/B/C/D only. This receiver spawned0.'
packet_current={
    'GR8-ELR-001':'Necessary finite interfaces now received. Final global canonical/alias/history adjudication remains root-owned; no additional finding/vote.',
    'ELR-I04-ENC01–04':'All10697 pairs and178 complete link targets received. Native loader/encoding/media behavior NOT_EXECUTED; no finite textual debt remains.',
    'L01–L14-current-copy':'All adopted historical qualifications received. Original complete56/37 case bodies were not adopted as this finite receiver authority; no title-negative or transferred PASS.',
    'PBS-mandatory-clarifiers':'All35 necessary localization projections/definitions now received; broader combat/whole PBS fields remain outside adopted scope.'}
for row in q['complete_finite_packets']:
    row.setdefault('initial_unresolved',row['unresolved'])
    row['unresolved']=packet_current[row['id']]
save('reception-ledger.json',q)
pc.update(updated_utc=NOW,receiver_task_status=READY,root_task_final_signed=False,
    history='Target historical qualification fully received within C07; broader original56/37 bodies/canonical remain root/history-owned, no false FULL/PASS or title-negative.',
    D_recovery='4827 stable IDs received once from01a144fc-df1d-7133-97ce-5d218016402d; original D future result dedup, no extra independent vote.')
save('proposal-counters.json',pc)

generation=load('continuation/pbs-field-binding/generation.json')
generation.setdefault('initial_corpus_reference_credit_state',generation['corpus_references_credit'])
generation['corpus_references_credit']='All8167 references now bound to actually read/received literals; see actual-reader-bindings.json. This generator still grants0 credit.'
save('continuation/pbs-field-binding/generation.json',generation)
provider=load('continuation/pbs-field-binding/provider-comparison.json')
provider.setdefault('initial_corpus_dictionary_references',provider['corpus_dictionary_references'])
provider['corpus_dictionary_references']='Exact string aliases only; runtime domains determined by family/field/producer. All8167 slots now bound to actual readers; no extra primary denominator.'
save('continuation/pbs-field-binding/provider-comparison.json',provider)
reverse=load('continuation/links-and-reverse-validation.json')
reverse['reverse125']['lossless_status_groups_scope']='Preserved original target clause statuses; PENDING wording is original history, not current receiver debt.'
reverse['reverse125']['current_receiver_status']='All125 complete finite clauses/398 subassertions and their necessary producer/consumer interfaces received; no native execution or global acceptance.'
save('continuation/links-and-reverse-validation.json',reverse)
print(json.dumps({'status':READY,'pairs':10697,'fields':21394,'interfaces':7,'necessary_unreceived':0,
    'PBS_field_slots':11647,'self_spawn':0,'new_proposals':0,'new_independent_votes':0,'root_final_signed':False},ensure_ascii=False))
