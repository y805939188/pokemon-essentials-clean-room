"""Record only this context's completed, explicitly enumerated reading windows.

The code serializes audit observations; it neither decides source semantics nor
executes reviewed programs. Duplicate frozen payloads retain association labels.
"""
import datetime
import json
from pathlib import Path

P = Path(__file__).resolve().parent
now = datetime.datetime.now(datetime.timezone.utc).isoformat()
def get(name):
    return json.loads((P/name).read_text())
def put(name, data):
    (P/name).write_text(json.dumps(data, ensure_ascii=False, indent=2)+'\n')

d = get('reading-ledger.json')
rows = d['snapshot_payloads']
for index in (43, 55):
    r = rows[index]
    r.update(read_state='FULL_LEDGER_CURRENT_SEMANTIC_FIELDS_READ_WITH_PRECISE_IDENTITY_ONLY_DISPOSITIONS',
        exact_unread_scope='NONE_FOR_CURRENT_LEDGER_SEMANTIC_FIELDS; SOURCE_IO_AUTHENTICITY_AND_SUPPORT_NOT_YET_RECEIVED',
        semantic_fields_view=f'ledger-views-v2/{index:03d}.semantic-fields.json',
        identity_only_dispositions=f'ledger-views-v2/{index:03d}.identity-dispositions.json')
rows[43]['original_read_io'] = 'Private platform tool chunks e18865 and 848ecb; full continuous view1–650/651–1319. No original read UTC invented.'
rows[55]['original_read_io'] = ['ledger-055-01.receipt.json', 'ledger-055-02.receipt.json']
interface_indices = (3, 41, 52, 75, 109, 164, 174, 184, 229, 245, 253, 265, 277)
for index in interface_indices:
    rows[index].update(read_state='FULL_ARTIFACT_READ',
        exact_unread_scope='NONE_FOR_THIS_INTERFACE_ARTIFACT; UNDERLYING_SOURCE_FACTS_AND_ORIGINAL_IO_REMAIN_SEPARATE',
        original_read_io=([f'interface-{index:03d}-01.receipt.json', f'interface-{index:03d}-02.receipt.json'] if index==41 else f'interface-{index:03d}-full.receipt.json'))
for alias, original in ((243,109),(286,253)):
    assert rows[alias]['sha256']==rows[original]['sha256']
    rows[alias].update(read_state='SAME_BYTES_ASSOCIATION_WITH_PERSONALLY_FULL_READ_INTERFACE_NO_SECOND_DISPLAY',
        exact_unread_scope='NONE_FOR_SAME_BYTE_INTERFACE_PAYLOAD; DISTINCT_RECEPTION_ACTION_NOT_INFERRED_FROM_BYTE_ASSOCIATION',
        associated_original_index=original, original_read_io=rows[original]['original_read_io'])
full_states = {'FULL_ARTIFACT_READ', 'FULL_LEDGER_CURRENT_SEMANTIC_FIELDS_READ_WITH_PRECISE_IDENTITY_ONLY_DISPOSITIONS', 'SAME_BYTES_LINK_TO_PERSONALLY_FULL_READ_CONTRACT_NO_SECOND_READING', 'SAME_BYTES_ASSOCIATION_WITH_PERSONALLY_FULL_READ_INTERFACE_NO_SECOND_DISPLAY'}
read_sha = {r['sha256'] for r in rows if r['read_state'] in full_states}
pending = {r['sha256']:r['bytes'] for r in rows if r['sha256'] not in read_sha}
d.update(updated_utc=now,
    ledger_semantic_full_current_payloads=sum(r['read_state'].startswith('FULL_LEDGER') for r in rows),
    full_frozen_artifact_payloads_personally_read=sum(r['read_state']=='FULL_ARTIFACT_READ' for r in rows),
    current_semantically_read_unique_sha=len(read_sha),
    remaining_not_fully_personally_semantically_read_unique_sha=len(pending),
    remaining_not_fully_personally_semantically_read_unique_bytes=sum(pending.values()),
    full_interface_artifacts_read=18,
    full_interface_paths_with_exact_same_byte_associations=20,
    full_interface_records_read=182,
    full_interface_record_qualification='182 contract records across18 distinct artifact payloads; includes11 WI records twice at two different captured versions. Not182 distinct globally effective interfaces. Topology reception objects and other supplementary records were also read; source/consumer acceptance remains separately pending.')
put('reading-ledger.json',d)

a=get('atomic-and-interface-denominator.json')
for r in a['interface_artifacts']:
    r.update(artifact_full_read_by_auditor=True,
        audit_decision='COMPLETE_CURRENT_ARTIFACT_MEANINGS_READ; NAMED_FINITE_ACCEPTANCES_AND_EACH_OPEN_TAIL_PRESERVED; UNDERLYING_SUPPORT_SOURCE_IO_NOT_AUTOMATICALLY_RECEIVED')
    if r['original_path'].endswith('receptions/creature-b-interfaces.json') or r['original_path'].startswith('tasks/world_topology_audit/'):
        r['same_byte_association_qualification']='Exact snapshot association to personally fullread identical payload; no second original reception or source read inferred.'
a['interface_artifact_reading_summary']={'paths':20,'distinct_payloads':18,'contract_record_instances':182,'globally_effective_distinct_denominator':'NOT_FINAL; DUPLICATE_VERSIONS_FACETS_AND_OPEN_TRANSITIVE_CONSUMERS_REQUIRE_RECONCILIATION','source_acceptance_from_artifact_reading':False}
a['updated_utc']=now
put('atomic-and-interface-denominator.json',a)

p=get('progress.json')
p.update(updated_utc=now, pending_unique_sha=len(pending),pending_unique_bytes=sum(pending.values()),
    personally_current_semantic_full_frozen_artifacts=sum(r['read_state'] in full_states and not r['read_state'].startswith('SAME_BYTES') for r in rows),
    personally_full_read_frozen_artifacts=sum(r['read_state']=='FULL_ARTIFACT_READ' for r in rows)+3,
    ledger_semantic_full_current_payloads=12, full_interface_artifacts=18,interface_records=182,
    cumulative_actual_contexts_parent_reported=38,
    current_actual_live_parent_reported={'running':7,'exited':31,'new_resource_context':'/root/resource_media_serialized_cloud','logical_reserved_primaries_without_actual_local_route_start':16,'original_parent_reserved_routes_without_receipt':17,'CRE_A':'NOT_ACTUALLY_DISPATCHED_AS_LAST_PARENT_MESSAGE'})
pub={'state':'ROOT_REPORTED_COMPLETE_REMOTE_READBACK; NOT_PERSONALLY_PERFORMED_BY_THIS_AUDITOR','commit':'523fb2fc2d86a9a8b3b79d9e595d932201b28c96','report_root_tree':'72be4f67d1960998cc2caab794a5734f6cb97371','files':5813,'published_bytes':488669562,'gzip_objects':99,'restored_original_bytes':1114905184,'receipt':'publication/r8-binary-atomic-contracts-readback-12.json','semantic_credit':False,'later_resource_cloud_contract':'LOCAL_LATER_DELTA_NOT_INCLUDED_IN_THIS_CHECKPOINT'}
p['publication']=pub;p['publication_status']=pub
put('progress.json',p)

e=get('execution-records.json')
e.setdefault('later_reading_tool_failure_events',[]).append({'action':'read_window.py ledger-views-v2/055.semantic-fields.json551–1125','failure':'exec-server transport disconnected before process creation; no process exit code available','failure_utc':'UNVERIFIED_NOT_BACKFILLED','retry':'exit0, toolchunk1d085f; ledger-055-02.receipt.json','not_a_material_or_host_limit':True})
e['later_captured_read_receipts']=[f.name for f in sorted(P.glob('interface-*.receipt.json'))]+['ledger-055-01.receipt.json','ledger-055-02.receipt.json']
e['publication']=pub;e['updated_utc']=now
put('execution-records.json',e)

ar=get('acceptance-register.json')
ar['interface_current_reading_reception']={'artifact_paths':20,'distinct_sha':18,'all_complete_contract_objects_read':True,'meaning_reception':'Named finite receipts, boundaries, evidence requirements and open tails fully read in this audit; original contributing source I/O and all semantic atoms not thereby independently accepted.','current_globally_valid_interface_denominator':'NOT_FINAL','WI_version_rule':'04:40:56 copied receiver snapshot and04:47:46 producer version both actually read; preserve changed status at each captured cut, no backdating.'}
ar['UI_v2_original_IO_author_disclosure']={'source':'actual message from /root/ui_full','own_full_declared':{'R':44,'F':12},'raw_stdout_local':'NOT_CAPTURED','original_operations':'NOT_RETAINED','original_chunk_boundaries':'UNVERIFIED','independent_original_EOF_truncation_qualification':'OPEN','provenance_artifact':'tasks/ui_full/io-provenance.json','provenance_artifact_full_read_by_this_auditor':False,'not_a_material_or_host_limit':True,'not_an_automatic_rejection_of_actual_context_reading':True}
ar['updated_utc']=now
put('acceptance-register.json',ar)
print(json.dumps({'updated_utc':now,'read_current_unique_sha':len(read_sha),'pending_unique_sha':len(pending),'pending_unique_bytes':sum(pending.values()),'all_interface_paths':20,'distinct_interface_payloads':18,'source_full_reads_credit':0,'global_pass':False}))
