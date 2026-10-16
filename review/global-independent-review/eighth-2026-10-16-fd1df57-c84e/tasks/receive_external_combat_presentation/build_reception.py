"""Serialize explicit reader decisions and exact unresolved populations; never assigns automatic PASS."""
from pathlib import Path
import json,hashlib,datetime,os,subprocess
T=Path(__file__).resolve().parent; ROOT=T.parents[1];P=T/'recovered/18d21310bdc360c87d7ffd886df7d06aef8604a7'
C='18d21310bdc360c87d7ffd886df7d06aef8604a7'; CT='40f45dddcdea5522b4bf7d0fea1a0f74f7d3d232'; R='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'; B='fd1df570cad987dc3852a3b958f03916e317f7fe';reader=os.environ.get('CODEX_THREAD_ID','UNVERIFIED')
def read(n):return json.loads((P/n).read_text())
def dump(n,x):(T/n).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def identity(p):
 b=p.read_bytes();return {'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'blob':hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()}
f=read('forward-mapping.json')['facts']; a=read('atomic-assertions.json')['assertions'];groups={g['id']:g for g in f};refs=json.loads((T/'reference-identities.json').read_text());ref_by={r['path']:r for r in refs}
objects=[]
for r in a:objects.append({'id':r['id'],'population':'manual','group':r['group'],'meaning':r,'origin_file':'atomic-assertions.json','origin_pointer':'/assertions/'+str(a.index(r)),'source':groups[r['group']]['reference'],'source_range':r['source_range']})
for name,pop in [('release-variance-fields.json','release_field'),('capture-variance-fields.json','capture_field'),('ball-color-fields.json','RGB_field')]:
 d=read(name)
 for rowindex,row in enumerate(d['records']):
  for index,r in enumerate(row.get('fields',[row])):
   objects.append({'id':r['id'],'population':pop,'group':d['group'],'meaning':r,'ball':row['ball'],'origin_file':name,'origin_pointer':f'/records/{rowindex}'+(f'/fields/{index}' if 'fields'in row else ''),'source':d['source'],'source_range':[r['source_line'],r['source_line']]})
assert len(objects)==1045 and len({r['id']for r in objects})==1045
reverse=read('reverse-mapping.json')
source_groups={f'EXTCP-F{i:03}'for i in [*range(42,51),*range(55,60)]}
source_checked={o['id']for o in objects if o['group']in source_groups};assert len(source_checked)==680
full={'EXTCP-F042.A01','EXTCP-F042.A02','EXTCP-F042.A03'}
qual={
 'EXTCP-F044.A14':'完成回调登记在5单位zoom动作，默认回调只向显示个体请求play_cry；不得把同刻移动或宿主声音完成混为触发条件。',
 'EXTCP-F046.A17':'五组数是Tone的red/green/blue偏移，允许负数，不是最终RGB像素；专用循环绕过表中ray起终tone。',
 'EXTCP-F049.A02':'(-128,-128,-128)是Tone偏移；球累计时长含既存排期，不把4单位当全演出总长。',
 'EXTCP-F055.A11':'5单位移动与缩放共同排期，intro回调登记在缩放完成；仅请求显示个体叫声，蛋/缺资源/宿主失败不保证实际有声。',
 'EXTCP-F057.A05':'这里普通长度指未按pitch调整的底层getPlayTime秒；cry_length已除0.75，不应再次除。有限1秒前提推出29请求单位。',
 'EXTCP-F058.A21':'失败出现沿缩放回调请求显示个体叫声；原位置是构造时读取的实际sprite坐标，不保证异常后复原。'
}
receptions=[]
base_notes={
 'EXTCP-F042':'BaseAnimation1–64及PictureEx1–548全文；running检查在推进前，完成滞后一轮观察，dispose只遍历tempSprites。WP67-A9.3与WP16§6.3明确对应，pbFaintBattler/throw正常返回后dispose接合。',
 'EXTCP-F043':'Base65–166完整：球资源/裁区、15显式色+默认、手位训练家分支/整数除法/帧与层。派出/收回/捕获失败消费者381–813实际读；未来是否固定全部参数仍OPEN。',
 'EXTCP-F044':'Base167–254完整：每段轨迹、二次纵向、未消费midX、滚动帧/三周、开合压缩/声音开关、出现缩放回调及吸入两阶段。PictureEx零时长/顺序/回调/relative取样已全文核。',
 'EXTCP-F045':'释放表完整16行×14字段独立读；POKEBALL后备；CHERISH的ray两字段仅保留配置值，实际分支专用循环。',
 'EXTCP-F046':'释放consumer347–457完整：上下glare反向索引/层/缩放/淡出，DUSK下层不放大；10射线及15对粒子随机域/整数排期、tone与显隐均核。',
 'EXTCP-F047':'捕获表完整16行×17字段独立读；不与释放表合并；NEST下粒子同刻显后隐但字段仍消费。',
 'EXTCP-F048':'捕获consumer567–725完整：三glare、9组粒子/弧返、MASTER/DIVE/PREMIER/NEST分支、NET web、尾环及球零位移时长标记。',
 'EXTCP-F049':'成功consumer726–762完整：catch click、球tone、三颗星各自起角/高度/缩放/转角/透明度与临时销毁，不臆增隐藏动作。',
 'EXTCP-F050':'收回consumer763–823完整：5粒子15单位角/半径分段和两环；球参数本方法不消费。',
 'EXTCP-F055':'双方派出381–525完整；球取显示个体，canonical和metrics实际位置分列，玩家+4/对手+6及开局额外10分列。场景87–156实际读，缩放回调及影子完整定义到位。',
 'EXTCP-F056':'收回/伤害526–609完整：收回绝对10淡球/6隐藏影子与burst起点分列；伤害四次闪烁及原可见性恢复。场景pbRecall完整；原HP/倒下领域判定未因此接收。',
 'EXTCP-F057':'倒下610–657及Species183–246完整；专用/普通75/无声三路、最少10与旧注释区别、29/22/12为假设1秒静态推导。当前required归属未裁。',
 'EXTCP-F058':'捕获658–813完整：原shake成功门/critical压缩、手位/抛物线、吸入起点声音、弹地/摇动、失败重新出现、成功球移出销毁队列。捕获概率/存储所有权消费者未完整接收。',
 'EXTCP-F059':'挡球814–849完整：固定抛物线后8单位回退/滚动；无吸入与成功保留。正常场景入口完整；不推战斗规则执行。'
}
for o in objects:
 rid=o['id'];checked=rid in source_checked; grp=o['group']; isfield=o['population']!='manual'
 status='COMPLETE_FINITE_RECEPTION'if rid in full else ('SOURCE_CHECKED_FORMAL_RECEPTION_OPEN'if checked else'AVAILABLE_NOT_READ_NOT_RECEIVED')
 reason=base_notes.get(grp,'当前对象正文及完整必要source/formal/consumer尚未由本context实际接收；可得未读，不是材料limit。')
 if isfield:
  m=o['meaning'];field=m.get('field','RGB');val=m.get('value',m.get('rgb'))
  if o['population']=='RGB_field': use='球色通道值，Color alpha由派出/收回/失败重现调用另设；不等同像素观测。'
  elif field.endswith('.resource'):use='资源后缀与固定ballBurst前缀组合为相应上下粒子/glare请求；同字段还可触发尺寸/缩放分支。'
  elif field.endswith('.start_tone'):use='该层初始Tone(red,green,blue)偏移；按实际consumer的反向索引选层，不与Color混同。'
  else:use='该层后续插值的目标Tone(red,green,blue)偏移，按各层完整登记时点/时长消费。'
  if m.get('disposition')=='READ_VALUE_OVERRIDDEN_BY_CHERISH_CYCLE':use='此配置值存在但CHERISH实际ray分支不使用，逐单位专用五Tone循环替代；不能删除配置身份或标成当前请求。'
  if m.get('disposition')=='REQUESTED_FOR_SAME_TICK_HIDDEN_PARTICLE':use+=' NEST下粒子在同刻先显示再隐藏，字段有请求不代表可见像素。'
  reason=f"{o['ball']} / {field} = {json.dumps(val,ensure_ascii=False)}：{use} "+reason
 receptions.append({'id':rid,'population':o['population'],'group':grp,'status':status,'actual_complete_meaning':o['meaning'],'source_identity':o['source'],'source_range':o['source_range'],'target_payload_identity':identity(P/o['origin_file']),'target_pointer':o['origin_pointer'],'reader':reader,'source_read_io':['dfe443','8a2b0d','a71646','89a1b0','80426c','21a5ea','b27eb3','d389ec','7b59b2']if checked else[],'target_read_io':['80426c']if isfield and checked else(['b27eb3'if grp in {f'EXTCP-F{i:03}'for i in range(42,51)}else'd389ec']if checked else[]),'reason':reason,'mandatory_qualification':qual.get(rid),'formal_reception':'WP67-A254–270/WP16 297–311 finite aggregate clauses accepted'if rid in full else'OPEN: must complete formal owner/scope, reverse interfaces and necessary producer/consumer joins','execution':'NOT_EXECUTED'})
dump('frozen-denominator.json',{'schema':'gr8-cp-frozen-denominator/v1','contract_commit':CT,'target_commit':C,'target_checkout_tree':'9c19ea470d59a6b09805ecec52ea187071e94e65','target_task_tree':'927edea2c75316f71c400d555be795960af247ef','fixed_B8':B,'fixed_R':R,'object_count':1045,'manual':533,'variance_fields':496,'RGB_fields':16,'scalar_leaves_not_additional_objects':1248,'primary_groups':f,'objects':objects,'reverse_population':{'legacy_groups':31,'legacy_subassertions':150,'selected_interfaces':20,'objects':reverse},'no_primary_formal_denominator':True,'auxiliary_payloads':json.loads((T/'recovery.json').read_text())['files'],'counting':'Source checks, final reception, reverse interface and transport populations remain separate; overlaps never add credit.'})
dump('reception-ledger.json',{'schema':'gr8-cp-independent-reception/v1','status':'INCOMPLETE','reader':reader,'source_checked':680,'source_available_unread':365,'complete_finite_receptions':3,'remaining_final_receptions':1042,'objects':receptions,'UPDATE_NOT_STARTED':True})
dump('proposal-counters.json',{'schema':'gr8-cp-proposal-counters/v1','status':'INCOMPLETE','records':[{'id':'GR8-EXTCP-002','original':read('proposals.json')['records'][0],'reader_scope':'Full proposal15409B and source faint/PictureEx/cry definitions actually read; finite source vector29/22/12 verified by static derivation only. Full WP67-A/WP74/scope/history counterevidence not yet read.','strongest_no_required_attempt':'WP67-A9.4 says not transcribe frame coordinates/tracks and forwards author format to WP74; this may lawfully allow alternate visual tracks. That does not alone resolve whether ordinary cry pitch75 and pitch-adjusted waiting are sound-request behavior within required coverage. Need complete scope/related clauses, not title inheritance.','ELR_dispatch':'delegation/external-cp002-existing-elr-counter-dispatch.json is READY_PARENT_FOLLOWUP_NOT_EXECUTED_BY_ROOT; it is not an actual counterreview receipt. No successor counterreview was supplied in fixed contract.','counter_status':'OPEN_NOT_INDEPENDENTLY_ADJUDICATED','required_updates_added':0},{'id':'GR8-EXTCP-H001','original':read('proposals.json')['retracted_hypotheses'][0],'status':'WITHDRAWAL_PRESERVED_NOT_NEW_CANDIDATE','independent_source_verification':'OPEN sourceBattleAnimationPlayer572–583 and complete foreground timing consumer not read here; original author withdrawal not independent review.','incorrect_original':'background20→110','author_correction':'foreground100→150; NOT_EXECUTED'}],'required_accepted':0,'UPDATE_NOT_STARTED':True})
interfaces=read('interfaces.json');dump('interfaces.json',{'schema':'gr8-cp-independent-interfaces/v1','original':interfaces,'duplicate_id_disambiguation':'original interfaces/IF09=background/audio; continuation_interfaces/IF09=fixed tracks. Preserve full JSON pointer as stable identity.','status':'INCOMPLETE','full_interfaces_accepted':0,'finite_join':'Base/PictureEx aggregate→scene pbFaintBattler/pbThrow and B8WP67-A9.3/WP16§6.3 only; this is a fact-level receipt, not entire IF07 or IF09.','mandatory_battler_supplement':{'manifest':'delegation/battler-reception-mandatory-supplement.v1.json','specific_target_job':'receive_external_com_battler; current task differs','companion_read_full':'adjudication/root-battler-eight-consumer-facts-reception.v1.json IOeeff69','adopted_qualifiers':'No unqualified inheritance: direct-only refresh, wild initial bitmap vs later sendout, separate shiny/super getter gates, HP writer-before-notification with post-notify records. Source inputs31 are only partially read here; no full Battler receipt.','source_evidence':'adjudication/root-battler-eight-facts-exact-inputs.v1.json; metadata read IO4c8af4; UI source ranges separately reread from fixed R.','full_evidence_adoption':False},'UPDATE_NOT_STARTED':True})
print(json.dumps({'objects':len(objects),'source_checked':len(source_checked),'complete_finite':len(full),'unread':1045-len(source_checked),'status':'INCOMPLETE'}))
