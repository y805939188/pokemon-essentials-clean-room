"""Consolidate actual exact-value reading and purpose strata, never infer PASS."""
from pathlib import Path
import json, hashlib, gzip, datetime, collections
import semantic_reader as sr

T=Path(__file__).parent; W=T/'.publication-work'; NOW=sr.now()
state=json.loads(sr.STATE.read_text())
superseded=state.setdefault('superseded_displays',[])
for old,new in [('c1','c1v2'),('mtask','mtasks_v3'),('mtasks_v2','mtasks_v3')]:
    if old in state['pending']:
        row=state['pending'].pop(old)
        row.update(status='SUPERSEDED_DISPLAY_NO_SEPARATE_READ_CREDIT',successor_display=new)
        superseded.append(row)
assert not state['pending'], list(state['pending'])
assert any(x['file']==10 and x['pointer']=='/coverage_and_qualification_sections/tasks' for x in state['acks'])
assert all(any(x['file']==n and x['pointer']=='' for x in state['acks']) for n in (0,1,5,6,12,13,14,15,16,19))
sr.STATE.write_text(json.dumps(state,ensure_ascii=False,indent=1)+'\n')

def save(name,x):
    (T/name).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def ident(p):
    b=Path(p).read_bytes()
    return dict(bytes=len(b),sha256=hashlib.sha256(b).hexdigest(),git_blob=hashlib.sha1(f'blob {len(b)}\0'.encode()+b).hexdigest())

inv=json.loads((T/'material-inventory.json').read_text())
for row in inv:
    assert ident(row['materialized_path'])=={k:row[k] for k in ('bytes','sha256','git_blob')}
canon=sr.load_doc(0)['records'];orig=sr.load_doc(1)['records'];zh=sr.load_doc(15)['records']
assert len(canon)==len(orig)==len(zh)==37
assert {r['id'] for r in canon}=={r['id'] for r in orig}=={r['id'] for r in zh}
view=json.loads((T/'handoff-view-comparison.json').read_text());assert view['complete_37_rendered_body_equal']
view.update(embedded_values_pending_display=False,embedded_values_read='All9 exact original values read or associated to this-context acknowledged complete objects; first object immutable core tuple explicitly read.',
    control_ranges_pending_display=[],control_ranges_read=view['control_ranges_pending_display'],after_read_utc=NOW,
    no_lexical_whole_payload_claim=True)
save('handoff-view-comparison.json',view)

counts=dict(readset_payloads=25,readset_decoded_bytes=113396087,original_C2_identities_verified=25,material_missing=0,
    whole_original_payloads_lexically_read=8,whole_original_payload_bytes_lexically_read=84295,
    additional_complete_semantic_value_payloads_with_identity_atoms_separate=11,
    purpose_stratified_payloads=6,readset_payload_purposes_disposed=25,
    assigned_record_or_current_qualification_text_unread=0,canonical_records=37,canonical_records_fully_value_read=37,
    original_proposal_and_counter_records_fully_value_read=37,C13_records_read_or_exact_complete_value_associated=37,
    C13_seven_groups=259,alias_rows_read=37,C19_integrity_rows_read=37,inherited_nonmandatory_records=31,
    inherited_optional=8,inherited_FLOAT=1,inherited_policy=7,inherited_limits=14,inherited_no_required=1,
    additional_optional_navigation_facets=2,required=27,required_P2=10,required_P3=17,optional_entries=7,no_required_entries=1,policy_entries=2,
    task_register_main_entries=87,task_register_preserved_logical_entries=31,
    source_fact_pointer_index_rows=5732,authored_clause_pointer_index_rows=25001,program_pointer_index_rows=736,
    source_unit_location_rows=2668,formal_structure_location_rows=21702,source_inventory=432,formal_inventory=131,fixed_supplements=9,
    transport_logical_paths=34251,transport_unique_objects=21449,transport_local_private_stream_locators=74,
    R8_final_root_received_records=0,R8_final_root_not_received_records=37,
    new_behavior_runs=0,findings_submitted=1,findings_accepted=0)
full={2,3,4,7,8,17,23,24}; semantic={0,1,5,6,12,13,14,15,16,18,19};stratified={9,10,11,20,21,22}
assert full|semantic|stratified==set(range(25)) and not full&semantic
entries=[]; purposes=[]
for row in inv:
    n=row['index']; e=dict(row)
    e.update(reader='external /root continuing actual context; own platform ID UNVERIFIED',recorded_after_read_utc=NOW,
        final_root_reception='NOT_RECEIVED',behavior_execution='NOT_EXECUTED',prior_reader_semantic_credit_imported=False)
    e['materialization_read_status_not_current']=e.pop('semantic_status',None)
    if n in full:
        status='WHOLE_ORIGINAL_PAYLOAD_READ';scope=['entire payload']
        receipt='Initial actual full display in same continuing platform conversation; no invented per-command UTC.'
    elif n in semantic:
        status='COMPLETE_SEMANTIC_VALUES_READ_IDENTITY_ATOMS_INVENTORIED';scope=['entire JSON semantic field structure']
        receipt='continued-reading-ledger.json exact original pointers/whole-subtree ACKs; exact repeated values linked, not summaries'
        if n==18:
            scope=['all top-level semantic fields and all37 integrity records','/inputs/0..59 exactly bytes,path,sha256,snapshot: identity inventory only']
            receipt='Prior actual complete integrity-field display; input identity inventory separately preserved.'
    else:
        status='COMPLETE_ASSIGNED_PURPOSE_STRATA_READ_NOT_WHOLE_LEXICAL_FULL_READ'
        receipt='typed-purpose-strata.json + purpose-reading-receipts.json; no target-body or source approval'
        scope={9:['all control prose ranges','complete37 C13 bodies exact-rendering association','all9 embedded JSON values associated to complete this-context reads'],
          10:['all top-level fields by true structure; complete current semantic/qualification/task objects','coverage/location/transport identities and pointer purposes typed separately'],
          11:['all publication/binding/qualification claims','all33 and21824 member identities typed; no member-body credit'],
          20:['all root/shared exact qualifier values','all5732 typed target pointers and15 metadata-overlay associations inventoried; no fact-body credit'],
          21:['all root/shared exact qualifier values, DL-F015 no-formal-range disposition','all25001 typed clause target pointers and1072 exact-receiver status pointers inventoried; no assertion-body credit'],
          22:['all root/shared exact kind/status/premise/evidence values','all736 program target locators typed; no program-body or execution credit']}[n]
    e.update(read_status=status,exact_read_scope=scope,receipt=receipt,
        independent_B8_R_source_approval='Only named bounded scopes in record0-supporting-reading.json and continued-observations.json; no whole-source or whole-formal approval')
    entries.append(e)
    purposes.append(dict(file_index=n,path=row['path'],original_purpose=row['purpose'],read_status=status,
        exact_scope=scope,underlying_target_reading_credit_from_inventory=0,current_source_global_PASS=False,
        generation_time_scope_preserved=True,root_final_reception='NOT_RECEIVED'))

strata=json.loads((T/'typed-purpose-strata.json').read_text())
purpose_receipts=dict(schema='r8.external-h-c2.purpose-reading-receipts.v1',recorded_after_read_utc=NOW,
    original_input_identities='material-inventory.json',reader='external /root continuing actual context',
    exact_value_displays_read=['source_pointer_purposes.0','clause_pointer_purposes.0','program_pointer_purposes.0','binding_strata.0','manifest_strata parts0..6',
                               'handoff_embedded.0','handoff_control all recorded ranges'],
    regenerated_strata_note='Later exact regeneration incorporates already-ACKed aliases as =read references; original immutable input identities unchanged; no new source/body credit.',
    source_metadata_overlay_purpose='All18 C03 errata IDs/explicit overlay pointers/mandatory qualification read; underlying overlay bodies not substituted or approved.',
    structural_dispositions_read=['TABLE_SEPARATOR','HORIZONTAL_SEPARATOR','HEADING_NAVIGATION_TO_BOUNDED_BODY_ONLY','HEADING_LABEL_NO_INDEPENDENT_BEHAVIOR_ASSERTION','TABLE_SEPARATOR_NO_BEHAVIOR','TABLE_COLUMN_HEADER_EXPLICITLY_READ_IN_C12_039'],
    typed_purpose_inventory='typed-purpose-strata.json',target_body_approval=False,behavior_execution='NOT_EXECUTED',final_root_reception='NOT_RECEIVED')
save('purpose-reading-receipts.json',purpose_receipts)
save('reading-ledger.json',dict(schema='r8.external-h-c2.reading-ledger.v2',recorded_utc=NOW,counts=counts,entries=entries,
    continued_exact_reading='continued-reading-ledger.json',recoverable_exact_display_bundle='exact-reading-evidence.json.gz',
    whole113MB_lexical_FULL_READ_claim=False,
    reading_rule='Every assigned record/current qualification value actually read. Exact complete duplicates may associate only to this continuing context readings. Typed pure pointer inventories confer zero target-body credit.',
    initial_read_time='Exact independent per-command start UTC for earlier platform-only reads UNVERIFIED; no backfilling',
    raw_command_stream='Original platform conversation only; no exported private stream or fabricated split stdout/stderr/exit receipts',
    current_global_acceptance='NOT_RECEIVED; source/formal claims not reapproved through historical PASS or pointer inventory'))
save('purpose-dispositions.json',dict(schema='r8.external-h-c2.purpose.v2',entries=purposes,
    typed_strata='typed-purpose-strata.json',target_bodies_are_not_summaries=True,no_blanket_administrative_exclusion=True))
save('semantic-units.json',dict(schema='r8.external-h-c2.units.v2',unit_definition='Record/group/purpose scopes, not independent requirement counts',
    canonical_records=[dict(id=r['id'],canonical_root_id=r['canonical_root_id'],original_C2_status=r['status'],classification=r['classification'],
      primary_batch=r['primary_batch'],C2_pointer=f'/records/{j}',complete_seven_groups_read=7,original_proposal_counter_read=True,
      B8_current_source_global_approval='NOT_GRANTED_BY_C2_TEXT_READING',final_root_reception='NOT_RECEIVED') for j,r in enumerate(canon)],
    purpose_strata=[{k:v for k,v in x.items() if k!='groups'} for x in strata['strata']]))

accept=json.loads((T/'history-current-acceptance.json').read_text())
accept.update(schema='r8.external-h-c2.acceptance.v2',recorded_utc=NOW,
    assigned_C2_record_purpose_reading='COMPLETE_EXACT_VALUE_AND_PURPOSE_STRATA',root_final_acceptance='NOT_RECEIVED',global_pass=False,
    complete_record_register='semantic-units.json',full_proposals_and_counters_read=37,full_Chinese_groups_read=259,
    nonmandatory_original_fields_read=31,qualified_history_reception='Full C2 qualification objects read; their source/runtime/other original target bodies are not blanket reapproved.',
    suspected_history_relation='GR8-HIST-C2-001; independent non-proposer counter-review and root final decision pending')
accept['record0']['not_proved']=[x for x in accept['record0']['not_proved'] if x!='remaining36 full contracts']
accept['classification_and_limits']['limits']='All31 full inherited records and all14 C17 successor qualifications read. Original host/source execution and referenced target-body claims remain individually scoped, not newly certified.'
save('history-current-acceptance.json',accept)
find=json.loads((T/'continued-observations.json').read_text())
save('findings.json',dict(schema='r8.external-h-c2.findings.v2',recorded_utc=NOW,records=find['records'],new_findings=1,
    accepted_findings=0,required_classification_by_this_task=0,independent_counter_requests=['GR8-HIST-C2-001'],
    final_adjudicator='Main reviewer different actual context; NOT_RECEIVED',update_started=False,
    conclusion='One historical relation/classification qualification suspected; no demand to reopen old27/56/92 or modify already-neutral B8 wording. No global PASS or NO_REQUIRED_UPDATE.'))
save('unread.json',dict(schema='r8.external-h-c2.unread.v2',recorded_utc=NOW,
    status='ASSIGNED_C2_RECORD_AND_PURPOSE_TEXT_READ_COMPLETE_MAIN_RECEPTION_PENDING',counts=counts,
    assigned_record_and_current_qualification_value_unread=[],material_missing=[],material_or_permission_blocker=False,
    indexed_target_bodies=[dict(file_index=20,pointer='/facts',targets=5732,status='TARGET_OBJECTS_NOT_READ_OR_APPROVED_BY_PURPOSE_INDEXING'),
      dict(file_index=21,pointer='/records',targets=25001,status='TARGET_ASSERTION_OBJECTS_NOT_READ_OR_APPROVED_BY_PURPOSE_INDEXING'),
      dict(file_index=22,pointer='/units',targets=736,status='TARGET_PROGRAM_OBJECTS_NOT_READ_OR_APPROVED_BY_PURPOSE_INDEXING')],
    transport_index=dict(pointer='file10#/all_core_logical_payloads',logical_paths=34251,body_reading_credit=0,
      qualification='Pure frozen identity/recovery index; original bodies have their own scopes. This is not a new34251-body reading obligation or an approval.'),
    R8_root_reception=dict(records=37,received=0,not_received=37,suspected_finding_nonproposer_counter='NOT_RECEIVED'),
    independently_unverified_current_claim_scope='C2 text/purpose completion is not new approval of every source fact or B8 clause. Only explicit bounded fresh checks are receivable; source/formal global reception belongs to main review.',
    prior_external_receipts=dict(current_nonmandatory_semantic_records='NOT_RECEIVED_IN_FULL; no credit imported',R7_stage_identity_audit='NOT_RECEIVED_IN_FULL; no credit imported'),
    new_behavior_execution='NOT_EXECUTED',actual_model_effort_tier_speed_Fast_own_platform_id='UNVERIFIED',update_status='UPDATE_NOT_STARTED'))

progress=json.loads((T/'progress.json').read_text())
progress.update(state='C2_RECORD_PURPOSE_REVIEW_COMPLETE_PENDING_MAIN_RECEPTION',updated_utc=NOW,counts=counts,
    status_detail='All25 prescribed payload purposes and37 complete records read; no blanket source/body/global acceptance;1 proposed historical qualification awaits independent counter-review.',
    semantic_reception='NOT_ACCEPTED_BY_MAIN',publication_state='FINAL_EVIDENCE_PREPARED_PENDING_OWN_BRANCH_PUSH_AND_FULL_REMOTE_READBACK',
    global_pass=False,behavior_execution='NOT_EXECUTED',new_behavior_runs=0)
save('progress.json',progress)

# Bundle exact ACK displays and original pointer bindings for reproducibility.
displays={}
for row in state['acks']:
    for p in row['parts']:
        q=Path(p)
        if q.exists():displays[q.name]=q.read_text()
for p in (W/'strata').glob('*.txt'):
    if p.name!='view-differences.txt':displays['strata/'+p.name]=p.read_text()
bundle=dict(schema='r8.external-h-c2.exact-reading-evidence.v1',pool=state['pool'],metadata=state['metadata'],
    acknowledgments=state['acks'],superseded_displays=superseded,exact_displays=displays,
    rule='Exact values and pointer metadata, not source/behavior approval. Only explicit complete ACKs plus purpose-reading receipts count. Superseded/truncated displays confer no unique credit.')
b=json.dumps(bundle,ensure_ascii=False,separators=(',',':')).encode()
(T/'exact-reading-evidence.json.gz').write_bytes(gzip.compress(b,mtime=0))
save('exact-reading-evidence.identity.json',dict(encoded=ident(T/'exact-reading-evidence.json.gz'),decoded_bytes=len(b),decoded_sha256=hashlib.sha256(b).hexdigest(),
    purpose='Recoverable own exact display/pointer ledger; no reference program execution or private platform stream'))
save('continued-reading-ledger.json',dict(schema='r8.external-h-c2.continued-reading.v2',recorded_utc=NOW,acks=state['acks'],pending={},superseded_displays=superseded,
    evidence_bundle='exact-reading-evidence.json.gz',rule='Only complete actual displays count. Exact repeated values linked to named same-context actual read scopes. Identity/command atoms inventoried separately.'))

report=f'''# H-C2-CURRENT-RECORDS 第八轮外部审读报告

已完成本任务25份指定载荷的记录／当前资格／用途分层审读，37条canonical与37条原提案及反证、259组中文合同均有完整值阅读或本context完整同值关联。**不将113,396,087字节称作逐字全文已读，也不据历史PASS、索引或解析批准全部B8/R行为。** 主审接收0/37；UPDATE_NOT_STARTED。

固定任务提交30cfed0996003b6ebf4b5c51cc04f31ca9255440；B8 fd1df570cad987dc3852a3b958f03916e317f7fe／workspace tree751dfde81048c81390f89a65ca1d1a565ba8e1ca／formal treef292698cdd4a8e725525a9be6dc34b75faaf151e；C2 4580645dfbfec4a3c7ccbad56ae293cc619b0d25／tree1f4375e2a51801ed62bc143c1d51f70296fa52f3；R 8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b／tree7589c800b61ba13a13040ed0d686979b80a84fd0。

实际项目/workspace/pokemon-essentials-clean-room，参考/workspace/pokemon-essentials。唯一写集为本目录，唯一分支codex/r8-external-h-c2-current-records-20261016。本次用户授权仅自身目录commit及普通push，覆盖旧共享容器禁止提交条款；未spawn、整改、改main/tag／正式规格／参考／公共台账／他人目录。

25/25原载荷mode/blob/bytes/SHA及重复版本身份已核，解码分母113,396,087字节。8份原载荷全文实读84,295字节；另11份完整语义值审读，身份原子分列；6份按真实结构分层处置。完整同值按实际已读对象关联，未用摘要代替。`reading-ledger.json`、`continued-reading-ledger.json`、`purpose-reading-receipts.json`及可恢复的`exact-reading-evidence.json.gz`给出逐载荷／pointer／连续显示和实际读者、UTC边界。早期独立每命令UTC未回显处仍UNVERIFIED，不倒填日志。

37条仍为27 required（10 P2／17 P3）、7 optional entries、1 no-required、2 policy entries；2个导航optional facets另列，UTIL-03是旧policy资格facet。R6原31项（8 optional／1 FLOAT／7 policy／14 limits／1 no-required）全文有效字段已读。原作者较宽提案、普通对照、取消／失败／部分提交、反证缩窄、原null、PROPOSED／WAIT／OPEN的生成时点保留，未据此重开原27／56／92。C2旧UPDATE_NOT_STARTED与B8当前关闭／条款分开。

handoff正文211–11033行的全部37条259组，与本context已读C13完整对象重建视图逐行相等；9个内嵌JSON完整值与已读对象关联，所有额外控制文字另实读。批次13、无author blocking入边、R7-I公共整合、R7-IR新非作者核实际字节、可选采用门均保留；旧NOT_STARTED不当B8当前未整改事实。任务登记87条及31保留逻辑条目的结果／scope／状态／依赖／资格均已读，历史argv／时间／日志路径按具名元数据处置。

manifest约80MB未一概标行政：全部当前记录／规则／案例／依赖／接收／限制和任务资格按结构实读；34,251逻辑路径、21,449对象及74本地私有流定位只是传输身份。5732事实、25001条款、736程序、2668源分块和21702正式结构块是具名历史定位／用途索引，所有精确共用资格及例外已读，原目标pointer可恢复；这些索引不授目标事实、条款或程序正文的新阅读／运行信用。18个C03勘误overlay和6类结构处置也保留原定位限定，未把被撤销anchor原样当支持。

提交疑点 **GR8-HIST-C2-001**（建议P3，未裁决）：R6-C-P02已将满经验槽RGBA颜色与“闪白”的同一差异记为optional，R7-J16-002则以required新根接收两处中性用词。所读canonical／原提案反证／aliases／manifest及B8该项三个关闭对象未具名连接两者及重分类差异。最强反证是R7独立审者可将未限定颜色词视为规范承诺，且第二处表述范围与R6可不同；因此本任务不自裁重复根、optional或required。B8两处均已是中性“闪光”，不要求改回正文或重开关闭。完整前提／普通对照／最小实例／负证据边界／最小资格修订／正确保留／主审反证请求见`findings.json`。

新读R八个完整源文件及经验消费者完整方法、EXPSHARE实际节，B8 WP03完整393行与目录236行，支持GR7-M01-001具名有界反核；另新读颜色源350–387和B8相关连续条款、完整三个关闭对象支撑上述历史资格疑点。其它事实不因C2正文或历史receiver状态被新批准；完整源／正式全局接收仍交主审。索引指向的目标正文不以已读索引冒读，也不把可得缺读伪装为L01–L14。

本任务行为／参考／模型／宿主／Demo／native／保存回放新增执行均0，全部新增向量NOT_EXECUTED。R7既有Ruby单定义1过程10输入和R6历史18尝试的原资格保留，未冒本任务执行。请求gpt-6.1-sol／ultra／default普速／Fast关闭；实际model／effort／tier／speed／Fast／自身平台ID均UNVERIFIED。调用方source_thread_id不作自身平台ID。

指定记录／当前资格文字未读0；材料缺失0；主审未接收37／37，疑点独立反证未接收1／1；索引目标正文及全部当前source／formal行为没有本任务全量PASS。无材料或权限阻塞。发布仅本目录；核心冻结与后继发布绑定分开，最后commit/tree及完整远端回读由外部交付回显，避免自指回执循环。旧中断检查点与已披露失败／截断仍留Git历史及原平台记录，不作为当前完成状态。
'''
(T/'report.md').write_text(report)
print(json.dumps(dict(status=progress['state'],counts=counts,evidence_bundle_encoded_bytes=(T/'exact-reading-evidence.json.gz').stat().st_size),ensure_ascii=False))
