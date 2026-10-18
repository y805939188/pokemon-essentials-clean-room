"""Serialize the explicitly read D contribution and required final interfaces.
No partition helper or reviewed program is imported or executed. This tool does
not create primary reading credit; fixed contribution judgments and interfaces
were read before their explicit acceptance. Root/main signature remains pending.
"""
import datetime,json
from pathlib import Path
T=Path(__file__).resolve().parent
P=T/'.work/partition-D'
C='46e512033948fb54071af446d0ffce18dc4efd69'
READER='01a1448b-ab99-7002-850f-b61ed5c1100c'
RECEIVER='01a14465-f204-7783-a526-9b43e91ea005'
READY='READY_FOR_ROOT_TASK_FINAL_ACCEPTANCE'
NOW=datetime.datetime.now(datetime.timezone.utc).isoformat()
def read(p):return json.loads(p.read_text())
def write(p,v):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
def main():
    output=T/'partition-receptions/D'
    remote=read(output/'remote-readback.json');assert remote['commit']==C and remote['file_count']==36 and remote['bytes']==1990551
    checks=read(output/'structural-checks.json');assert checks['all29_exact_original_values_and_disjoint_parent2'] and checks['all15_strata_full_array_hash_rows_and_keysets']
    d=read(P/'reception-ledger.json');rs=d['legacy_text_receipts'];assert len(rs)==29 and d['all_29_assigned_purpose_receptions_complete']
    purposes=read(P/'reading-ledger.json')['purposes'];assert len(purposes)==17
    rec=read(T/'reception-ledger.json');assert len(rec['fully_received_records'])==37 and not rec['necessary_unreceived_records']
    matched={(r['kind'],r['index']):r for r in rs}
    for r in rec['original_nonmandatory']:
        key=(r['kind'],r['index'])
        if key not in matched:continue
        original=matched[key];assert r['id']==original['id']
        r['prior_receiver_checkpoint_status']=r.get('prior_receiver_checkpoint_status',r['status'])
        r.update(status='RECEIVED_COMPLETE_D_PURPOSE_CONTRIBUTION_AND_NECESSARY_INTERFACE',primary_reader=READER,fixed_delivery_commit=C,
          qualification='Complete exact historical/current purpose, strongest counter and necessary named bounded join received; original optional/FLOAT/policy/limit/no-required classification and NOT_EXECUTED retained. No all-domain or referenced-target approval.',
          contribution='partition-receptions/D/accepted-contribution.json',parent_interface_receiver=RECEIVER,parent_primary_reread=False)
    assert len(rec['original_nonmandatory'])==31 and all(r['status'].startswith('RECEIVED') for r in rec['original_nonmandatory'])
    purpose_by_index={p['index']:p for p in purposes}
    for r in rec['purpose_payloads']:
        n=r['file_index']
        if n not in purpose_by_index:
            r['retained_body_credit_boundary']=r.get('retained_body_credit_boundary',r['unreceived'])
            r['unreceived']=[]
            continue
        p=purpose_by_index[n]
        r['prior_receiver_checkpoint']=r.get('prior_receiver_checkpoint',dict(status=r['status'],actual_scopes=r.get('actual_scopes'),unreceived=r.get('unreceived')))
        r.update(status='RECEIVED_COMPLETE_DECLARED_PURPOSE_VIA_D_AND_NAMED_RECORD_READERS',actual_scopes=[p['scope']],unreceived=[],
          primary_purpose_reader=READER,fixed_delivery_commit=C,original_body_credit='Only separately received necessary named facts and purposes. Typed locators/transport rows give target-body credit0; canonical bodies separately direct4+A12+B10+C11.',
          current_scope_resolution='D final continued_current_fact_join supplies complete necessary named joins. Original generic file6 scope says per-item source/consumer open: retain it as non-blanket boundary/checkpoint, not a new whole-domain claim or outstanding named debt.')
    rec.update(status=READY,final_integration_utc=NOW,original_nonmandatory_complete=31,original_nonmandatory_unreceived=0,declared_original_purposes_complete=25,
      root_task_final='READY_FOR_ROOT_TASK_FINAL_ACCEPTANCE; MAIN_REVIEWER_FINAL_SIGNATURE_PENDING',material_unavailable=[],
      full_reception_qualification='37 canonical/259 groups and31 legacy are separate populations. All25 defined purposes complete through direct8 and D17; graph/handoff/shared-root consumer gate joined to actual canonical receivers. No global B8 PASS, policy adoption or runtime certification.')
    write(T/'reception-ledger.json',rec)
    legacy_joins=[]
    for r in rs:
        legacy_joins.append(dict(kind=r['kind'],index=r['index'],id=r['id'],meaning=r['meaning'],strongest_counter=r['strongest_no_required_counter'],
          current_named_join=r['continued_current_fact_join'],original_classification=r['retained_classification'],exact_value_sha256=r['exact_value_sha256'],
          primary_reader=READER,parent_interface_receiver=RECEIVER,parent_primary_reread=False,
          parent_reception='Exact contribution, counter, necessary named bounded facts and stated consumer/purpose received; historic limitations and all-domain target-body exclusion retained.'))
    di=read(P/'interfaces.json')
    graph=read(P/'graph-relations.json');handoff=read(P/'handoff-associations.json');typed=read(P/'typed-reception.json')
    contribution=dict(schema='gr8.partition.fixed-D-contribution-reception/v1',utc=NOW,commit=C,primary_reader=READER,parent_interface_receiver=RECEIVER,
      status='RECEIVED_COMPLETE_D_PURPOSES_AND_NECESSARY_INTERFACES',legacy_records=legacy_joins,complete_legacy_contribution=rs,
      original_purposes=purposes,interfaces=di,proposal_counters=read(P/'proposal-counters.json'),typed_reception=typed,
      graph_summary={k:v for k,v in graph.items() if k not in ['paths','scopes','all_artifact_roles']},graph_full_identity_reference=C+':continuation-results/D/graph-relations.json',
      handoff_associations=handoff,current_facts_qualification=d['qualification'],
      parent_D_I02_gate='All37 canonical bodies and required source/consumer interfaces now received: direct4 + fixed A12 + fixed B10 + fixed C11. D original OPEN_OTHER_RECEIVER_BODY remains true at D delivery, parent gate now satisfied.',
      prior_checkpoint='6220f424/b3580 INCOMPLETE stays historical; current final D contribution supplies new reading, not retroactive PASS.',
      purpose6_wording_resolution='Scope retained from prior text-only phase is bounded by final continued_current_fact_join: necessary named joins complete, all-domain source/native/host certification intentionally false. No requested body remains unread.',
      body_credit_from_typed_or_handoff_alias=0,new_required_proposals=0,actual_configuration='model/effort/tier/speed/Fast UNVERIFIED',
      behavior='NOT_EXECUTED',new_behavior_executions=0,new_root_signature=False,remote_readback='remote-readback.json',structural_checks='structural-checks.json')
    write(output/'accepted-contribution.json',contribution)
    f=read(T/'frozen-denominator.json');f['status']=READY;f['final_integration_utc']=NOW
    for r in f['original_nonmandatory_objects']:
        key=(r['kind'],r['index'])
        if key in matched:r.update(status='RECEIVED_VIA_FIXED_D_CONTRIBUTION',primary_reader=READER,delivery_commit=C)
    f['original_nonmandatory_complete']=31;f['original_nonmandatory_remaining']=0;f['declared_purposes_complete']=25;write(T/'frozen-denominator.json',f)
    reading=read(T/'reading-ledger.json');reading.update(status=READY,final_integration_utc=NOW,original_nonmandatory_complete=31,original_nonmandatory_remaining=0,
      original_nonmandatory_primary_read_by_this_context=2,original_nonmandatory_received_via_D=29,
      full_purpose_payloads=25,partial_purpose_payloads=0,unread_purpose_payloads=0,declared_purpose_dispositions_complete=25,remaining_purpose_interfaces_received_via_D=17,
      direct_full_purpose_payloads=8,purpose_credit_rule='Full25 means complete declared semantic/typed purposes through direct8+D17 and all37 named record-body owners, not this context primary reading. Direct8 retained separately. No113MB lexical reading or approval of all referenced target bodies.')
    reading['accepted_partition_receipts']['D']=dict(commit=C,reader=READER,legacy=29,purposes=17,typed_strata=15,receipt='partition-receptions/D/accepted-contribution.json');write(T/'reading-ledger.json',reading)
    interface=read(T/'interfaces.json');interface['status']=READY
    for r in di['interfaces']:
        interface['records']=[v for v in interface['records'] if v['id']!=r['id']]
        interface['records'].append(dict(id=r['id'],producer=r['producer'],consumer=r['consumer'],original_D_delivery_status=r['status'],
          status='RECEIVED_NECESSARY_INTERFACE; PARENT_CANONICAL_GATE_SATISFIED',facts=r['reason'],primary_reader=READER,
          parent_interface_receiver=RECEIVER,reason='For D-I02 all37 actual fixed canonical receipts and required graph producers are now joined here; other interfaces retain exact typed/historical/request bounds. No source/body approval from metadata.',
          fixed_delivery_commit=C,parent_primary_reread=False))
    interface['other_interfaces']='No necessary assigned interface remains unreceived. Historical/native/host/policy limits retained; main final signature pending.';write(T/'interfaces.json',interface)
    counters=read(T/'proposal-counters.json');counters['status']=READY;counters['received_partition_counters']['D']=dict(commit=C,reader=READER,new_required=0,full_counters='partition-receptions/D/accepted-contribution.json',root_final='PENDING_MAIN_REVIEWER');counters['global_NO_REQUIRED_UPDATE']=False;counters['global_verdict_authority']='No global B8 PASS or root verdict issued by receiver; main reviewer owns final decision.';write(T/'proposal-counters.json',counters)
    progress=read(T/'progress.json');progress.update(status=READY,legacy_received=31,legacy_remaining=0,declared_purposes_received=25,declared_purposes_remaining=0,
      necessary_interfaces_remaining=0,final_integration_utc=NOW,root_final_acceptance='READY_FOR_MAIN_REVIEWER_SIGNATURE_NOT_SELF_ISSUED',
      status_detail='All37 canonical/259groups + all31 inherited records +25 defined purposes and necessary graph/shared-root/typed interfaces received. Original readers/qualifications retained. Main final signature pending.',
      capacity_and_unread='No necessary assigned available-unread body or purpose remains. Preserved historical/material/host limits are not reclassified missing reading.')
    progress['partition_state']['D']=C+' RECEIVED_COMPLETE_PURPOSE_CONTRIBUTION_AND_INTERFACE';write(T/'progress.json',progress)
    validation=read(T/'validation.json');validation.update(status=READY,whole_task_final='READY_FOR_ROOT_TASK_FINAL_ACCEPTANCE; MAIN_SIGNATURE_PENDING',final_integration_utc=NOW,
      legacy_equation='2+29=31',purpose_equation='8+17=25',canonical_equation='4+12+10+11=37',groups_equation='28+84+70+77=259',D_remote='PASS;36files/1990551bytes',
      D_typed_strata_exact_array_row_keyset_checks='PASS;15/15 identity/purpose only',D_I02_required_producer_gate='PASS; all27 graph required IDs have actual received canonical contributions',
      new_behavior_executions=0,update_started=False)
    validation['partition_change_scopes']['D']=dict(files=36,exclusive_write_set=True,base_ancestor=True);write(T/'validation.json',validation)
    write(T/'unread.json',dict(schema='gr8.final-nonauthor-reception-unread/v1',status=READY,canonical_unreceived=[],original_nonmandatory_unreceived=[],declared_purpose_unreceived=[],necessary_interface_unreceived=[],
      missing_materials_for_assigned_reception=[],permission_blockers=[],retained_limits='All original L01–L14 with original generation/execution/restoration conditions; native/host/media/GPU/Demo/real-save and policy unknowns do not become newly certified.',
      root_final='MAIN_REVIEWER_PENDING; not an unreceived task input or new administrative review layer',behavior='NOT_EXECUTED',new_behavior_runs=0,UPDATE_NOT_STARTED=True))
    print(json.dumps(dict(status=READY,canonical=37,groups=259,legacy=31,purposes=25,necessary_unreceived=0,new_required_recommendations=0,new_behavior_runs=0),ensure_ascii=False))
if __name__=='__main__':main()
