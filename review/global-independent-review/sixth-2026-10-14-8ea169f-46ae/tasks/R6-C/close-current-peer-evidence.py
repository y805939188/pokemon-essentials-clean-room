import json,hashlib
from pathlib import Path
b=Path(__file__).parent;cm=b.parent/'R6-CM';vectors=[json.loads(x)for x in(b/'test-vector-map.jsonl').read_text().splitlines()];quant=[json.loads(x)for x in(cm/'quantitative/numerical-vectors.jsonl').read_text().splitlines()];qi={x['id']:x for x in quant};co=[json.loads(x)for x in(cm/'coordinator-test-vector-matrix.jsonl').read_text().splitlines()];ci={x['vector_id']:x for x in co};units=[json.loads(x)for x in(cm/'forward-unit-matrix.jsonl').read_text().splitlines()]
selected=[]
for i,u in enumerate(units,1):
 if any(x in u.get('unit','')for x in ['SwitchOut','FleeFromBattle','StartGravity','StartTrickRoom','StartWonderRoom','StartMagicRoom','SwapSideEffects','ProtectUserSide','EchoedVoice','PledgeMove','UserFaintsExplosive']):
  selected.append({'artifact':str(cm/'forward-unit-matrix.jsonl'),'record':i,'source':u['source'],'new_review_evidence':u['new_review_evidence'],'semantic_status':u['semantic_status']})
# These CM derivations were explicitly read in the tool output. Keep reader source ownership and no-reference-execution labels.
for v in vectors:
 if v['status']=='MOVE_PRODUCER_JOIN_PENDING'and v['id']in qi:
  q=qi[v['id']];c=ci.get(v['id']);v['peer_receipt']={'artifact':str(cm/'quantitative/numerical-vectors.jsonl'),'id':v['id'],'record':quant.index(q)+1,'prerequisites':q['prerequisites'],'independent_derivation':q['independent_derivation'],'source_evidence':q['source_evidence'],'semantic_status':q['semantic_status'],'coordinator_extra':c};v['status']='CM_PRODUCER_REVIEW_RECEIVED_C_CORE_CONSUMER_JOINED';v['assessment']='完整fixture与CM逐向量推导相接，C已全读ordinary/PP/target/protect/perhit/item/phase消费者；不把源指针、算术或收到报告当完整host PASS。';v['source_pipeline'] += [{'path':s['path'],'start':s['lines'][0],'end':s['lines'][1],'read_owner':'R6-CM'}for s in q['source_evidence']]
 elif v['status']in['MOVE_PRODUCER_JOIN_PENDING','FIELD_PRODUCER_JOIN_PENDING']:
  v['peer_receipt']={'artifact':str(cm/'forward-unit-matrix.jsonl'),'selected_actual_producer_records':selected,'receipt_report':str(cm/'report.md')};v['status']='CM_NAMED_CONTROL_FIELD_PRODUCERS_RECEIVED_C_CONSUMERS_JOINED';v['assessment']='CM真实控制/场域定义单位和逐body事实已接收，具体族与C实际执行/替补/调度消费者相合；各门/末尾读取保持本fixture，不统一全部替换或异常恢复。'
# Shared BE/CX/RM remain explicitly K/O-owned, not a C-owned-source semantic claim.
(b/'test-vector-map.jsonl').write_text(''.join(json.dumps(v,ensure_ascii=False)+'\n'for v in vectors))
(b/'received-CM-control-field-units.json').write_text(json.dumps({'selected':selected,'receipt_level':'CURRENT_FRESH_SOURCE_REVIEW_OF_DELEGATE; C owncore fullsource already read','reference_execution_here':0},ensure_ascii=False,indent=2)+'\n')
# Producer joins for repeated WP41/45 clauses.
p=b/'manual-clause-joins.jsonl';manual=[json.loads(x)for x in p.read_text().splitlines()]
for j in manual:
 if j['disposition']=='CROSS_DOMAIN_MOVE_PRODUCER_JOIN_PENDING':j['disposition']='CM_NAMED_PRODUCER_FACTS_RECEIVED_C_CONSUMERS_JOINED';j['peer_receipt_artifact']=str(b/'received-CM-control-field-units.json');j['semantic_assessment']+=' CM final源逐族事实现已接收，保留同一species/function family、wild/trainer、实际hit/Substitute/前置能力和PP前提。'
p.write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n'for x in manual))
print('CM joined vector statuses, unchanged K/O shared-context owner rows',sum(v['status']=='SHARED_CONTEXT_VECTOR_JOIN_PENDING'for v in vectors))
