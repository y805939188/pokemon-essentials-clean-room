"""Publish the reader's explicit acknowledgements; no reference program is run.

This script records decisions already made by the named reader after presenting
the exact chunks. Parsing, compression, hashes and counts never confer credit.
"""
from pathlib import Path
from datetime import datetime, timezone
from collections import Counter
import gzip, hashlib, json, subprocess

TASK = Path(__file__).resolve().parent
REPO = TASK.parents[4]
READER = 'external-H-EARLY-QUALIFICATIONS/root'
NOW = datetime.now(timezone.utc).isoformat()

def read(name):
    return json.loads((TASK/name).read_text())

def save(name, data):
    (TASK/name).write_text(json.dumps(data, ensure_ascii=False, indent=2)+'\n')

def ident(data):
    return dict(bytes=len(data), sha256=hashlib.sha256(data).hexdigest(),
                git_blob=hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest())

# Explicitly acknowledged presentations, including retries. The two truncated
# attempts are preserved as process evidence and excluded from reading credit.
excluded = {'007-r3-excluded.receipt.json', 'schema-bindings-001.receipt.json'}
acks = []
for f in sorted((TASK/'read-logs').glob('*.receipt.json')):
    if f.name in excluded:
        continue
    d = json.loads(f.read_text())
    d.update(semantic_status='ACTUALLY_READ_ACKNOWLEDGED_BY_NAMED_READER',
             acknowledgement_utc=NOW, receipt_file=str(f.relative_to(TASK)),
             acknowledgement_scope='exact displayed pointer/continuous lines; repeated values reused only with exact source/pointer and context bindings')
    if f.name.startswith('consumer-'):
        d['publication_of_source_text'] = 'LOCAL_ONLY; source reproduction excluded; exact original identity/ranges and receipt retained'
    acks.append(d)
save('read-acknowledgements.json', dict(reader=READER, recorded_utc=NOW,
     acknowledgements=acks, excluded_truncated_attempts=sorted(excluded),
     early_platform_reads='See original checkpoint ledger; no backfilled UTC or stdout',
     credit_rule='Acknowledgement follows actual reading; parser or script output alone is not credit'))

atlas = read('semantic-atlas/manifest.json')
assert len(atlas['chunks']) == 65
assert all(x['status']=='ACTUALLY_READ' for x in atlas['chunks'])
atlas['credit'] = 'All 65 complete presentations actually read; exact occurrence associations plus complete role/context schema and 568 criterion bindings separately read. Group count is presentation deduplication, not a semantic clause denominator.'
atlas['context_evidence'] = ['semantic-context-schema.txt', 'schema-unit-bindings.txt', 'nested-reason-bindings.txt']
atlas['reader'] = READER
save('semantic-atlas/manifest.json', atlas)

nm = read('nonmandatory-reads/manifest.json')
assert len(nm)==7
for c in nm:
    b=(TASK/'nonmandatory-reads'/c['file']).read_bytes()
    assert ident(b)['sha256']==c['sha256']
    c.update(status='ACTUALLY_READ', reader=READER, acknowledged_utc=NOW)
save('nonmandatory-reads/manifest.json', nm)
ls=read('nonmandatory-reads/limits-source.json')
ls.update(status='FULL_READ', reader=READER, receipt='read-logs/r5-limits-full.receipt.json')
save('nonmandatory-reads/limits-source.json',ls)

consumers=read('consumer-reads/manifest.json')
for c in consumers:
    c.update(semantic_status='ACTUALLY_READ', reader=READER,
             receipt='read-logs/consumer-'+c['name']+'.receipt.json',
             publication='Full original identity and exact ranges only; captured source text remains local and ignored')
save('consumer-reads/manifest.json',consumers)

# Lossless index transport preserves every source/RFC6901 occurrence and all
# routed administrative leaves without publishing an 80 MB JSON Git blob.
association=(TASK/'semantic-atlas/associations.json').read_bytes()
compressed=gzip.compress(association, compresslevel=9, mtime=0)
assert gzip.decompress(compressed)==association
(TASK/'semantic-atlas/associations.json.gz').write_bytes(compressed)
save('semantic-atlas/association-transport.json', dict(
    decoded_path='semantic-atlas/associations.json', decoded_identity=ident(association),
    transport_path='semantic-atlas/associations.json.gz', transport_identity=ident(compressed),
    encoding='gzip; mtime=0; exact UTF8 JSON after decompression',
    restoration='gzip.decompress into a new, non-symlink path within this exclusive task directory; verify bytes/SHA256/Git blob before use; do not execute evidence',
    semantic_credit_from_restore=False))

ignore=(TASK/'.gitignore').read_text().rstrip()+'\n'
for pat in ['semantic-atlas/associations.json','semantic-atlas/role-schema.txt',
            'consumer-reads/*.txt','read-logs/consumer-*.stdout']:
    if pat not in ignore.splitlines(): ignore+=pat+'\n'
(TASK/'.gitignore').write_text(ignore)

denominators = {
 'R1': {'trace_records':100,'per_input_records':113,'original_authority_inventory':83,'global_finding_total':'NOT_INVENTED'},
 'R2': {'controls':229,'batches':21,'contributions':341,'PASS_SCOPED_receipts':308,'PASS_SCOPED_STATIC_ACTUAL_receipts':33},
 'R3': {'required_controls':23,'criteria':76,'separate_excluded_records':2,'GR3-M09-001':'OPTIONAL/DEFERRED_U08_NOT_STARTED','GR3-M02-003':'NO_REQUIRED_REVISION'},
 'R4': {'original_controls':17,'original_criteria':76,'B5_supported_controls':16,'B5_supported_criteria':75,'partial_residue':1,'later_summary_limited_criteria':['C01','C02','C03','C04','C05'],'whole_legacy_ID_new_PASS':False},
 'R5': {'required_CLOSED':92,'OPEN':0,'P2':51,'P3':41,'optional':7,'no_required_revision':7,'policy':6,'material_host_limits':13,'native_static_units':410,'schema_static_units':568,'additional_units':158,'shared_contracts':21,'dependency_edges':18,'solewriter_paths':85,'original_contributions':262,'separate_admin':6,'separate_qualification_corrections':3},
 'units_rule':'Each original unit retained. No sum across rounds, versions, criteria, contributions, clauses, or deduplicated presentations.'}

summary = dict(readset_payloads=10, decoded_bytes=18033524,
 fully_body_read_payloads=4, fully_body_read_bytes=42590,
 purpose_complete_without_whole_body_FULL_READ_payloads=6,
 partially_read_required_semantic_payloads=0,
 unread_required_current_semantic_payloads=0,
 not_fully_body_read_payloads=6,
 parent_received_payloads=0,parent_not_received_payloads=10,
 semantic_scope='H exact original qualifications/current succession; all effective rules, premises, cases, dependencies and exclusions in this bounded readset, plus necessary current consumers',
 semantic_clause_denominator='Original structured units in completion-scope.json; no invented universal clause total',
 current_formal_full_body_read_by_this_task=0,
 necessary_consumer_bundles=20,necessary_source_spec_lines=1083,
 new_behavior_executions=0)

ledger=read('reading-ledger.json')
ledger.update(schema='r8.external-h.reading-ledger.v2',recorded_utc=NOW,summary=summary)
sources=read('semantic-atlas/associations.json')['source_identities']
for e in ledger['entries']:
    logical=e['input']['logical_path']
    e['input']['inherited_history_current_reading_snapshot']=e['input'].pop('reading',None)
    e['checkpoint_structure_counts_not_current']=e.pop('mechanical_structure_status_counts',{})
    e['structure_unit']='Original fields and criteria; raw JSON leaf counts only locate content and are not semantic denominators'
    if logical in sources:
        e['reading_status']='CURRENT_EFFECTIVE_SEMANTIC_READ_ADMIN_ROUTED'
        e['read_ranges_or_pointers'].append(dict(
          exact_source_identity=sources[logical],
          occurrences='semantic-atlas/associations.json.gz decoded /groups/*/occurrences filtered by exact source',
          administrative_dispositions='same decoded index /administrative_leaves filtered by exact source',
          continuous_presentations='semantic-atlas/manifest.json: chunks001..065, actual acknowledgements in read-acknowledgements.json',
          context_and_percheck='semantic-context-schema.txt all632lines; schema-unit-bindings.txt all570lines via nontruncated retries; nested-reason-bindings.txt all206lines',
          status='ALL_CURRENT_EFFECTIVE_SEMANTIC_FIELDS_READ; identity and old-body routing inventory only'))
    elif logical=='tasks/R7-H12/r5-activation-selections.json':
        e['reading_status']='PURPOSE_COMPLETE_IDENTITY_INVENTORY_ONLY'
    elif e['reading_status']!='FULL_READ':
        e['reading_status']='PURPOSE_COMPLETE_COMMON_SEMANTIC_FIELDS_ADMIN_ROUTED'
    e['purpose_complete']=True
    e['raw_body_full_read']=e['reading_status']=='FULL_READ'
    e['parent_reception']='NOT_RECEIVED_BY_PARENT'
ledger['continuation_read_evidence']={'acknowledgements':'read-acknowledgements.json','atlas':'semantic-atlas/manifest.json','occurrences':'semantic-atlas/association-transport.json','nonmandatory14':'nonmandatory-reads/associations.json','limits13':'nonmandatory-reads/limits-source.json','consumers':'consumer-reads/manifest.json'}
ledger['original_denominators']=denominators
ledger['credit_rule']='Exact content/context actually read by named reader; no credit from parsing, prior readers, hashes, restoration, selection, old PASS, or runtime inference. Raw whole-body FULL_READ remains4/10.'
save('reading-ledger.json',ledger)

purpose=read('purpose-dispositions.json')
purpose['recorded_utc']=NOW
for d,e in zip(purpose['payloads'],ledger['entries']):
    assert d['logical_path']==e['input']['logical_path']
    d['status']=e['reading_status'];d['purpose_complete']=True
purpose['continued_semantic_fields']='All remaining current effective fields read in65chunks with exact duplicate occurrence bindings; all current percheck contexts independently read; no blanket whole-body claim'
purpose['additional_finite_dependencies']=['Original R5 nonmandatory14 all semantic records in7chunks; identical values reused only after same-context exact comparison','R5 frozen limits L01-L13 all33lines','20 necessary R/B8 consumer bundles all1083original lines']
purpose['administrative_route_closure']='Original report/body locators, old reader lists, identities and superseded formal routes do not confer body credit or require unbounded recursion. All effective imported qualifications were read separately.'
save('purpose-dispositions.json',purpose)

raw_routes=[{
 'logical_path':e['input']['logical_path'],'bytes':e['input']['bytes'],
 'disposition':e['reading_status'],
 'not_claimed':'Whole raw body FULL_READ; old source/report bodies behind immutable administrative routes; earlier readers do not transfer credit',
 'exact_fields':'reading-ledger.json and purpose-field-associations.json; three large inputs additionally semantic-atlas/associations.json.gz'}
 for e in ledger['entries'] if not e['raw_body_full_read']]
save('unread.json',dict(schema='r8.external-h.unread.v2',reader=READER,recorded_utc=NOW,
 summary=summary,required_current_semantic_unread=[],required_current_semantic_unread_count=0,
 readset_raw_bodies_without_whole_body_credit=raw_routes,
 additional_routing_without_inherited_body_credit=[
  '83 R1 original authority/old reader reports: identity and original-time routing only; effective current qualification fields read',
  'R2 underlying229 owner/341 contribution reports: original IDs/qualified common-stage semantics received; do not claim fresh full bodies',
  'Superseded formal paths, original source locators, prior reader logs and exact duplicate qualification copies: routed by identity; no unlimited administrative recursion',
  'Parent R6/R7 current-nonmandatory and stage-audit cached bodies: inventory only; outside H early qualification semantic authority; no body credit',
  'Whole current formal131 and whole reference inventory: outside this delegated H body; necessary consumer ranges only'],
 unread_is_not_material_limit=True,
 remaining_material_or_permission_blockers=[],
 independent_reception={'parent_received_payloads':0,'pending_payloads':10,'status':'PENDING_PARENT_INDEPENDENT_COUNTERREVIEW_AND_FINAL_RECEPTION'},
 disposition='H_BOUNDED_PURPOSE_COMPLETE_PENDING_PARENT; no global PASS, no runtime certification'))

accept=read('history-current-acceptance-records.json')
accept['schema']='r8.external-h.history-current-acceptance.v2'
accept['status']='H_BOUNDED_SEMANTIC_REVIEW_COMPLETE_PENDING_PARENT'
corrections={
 'EH-HISTORY-01':('All100trace/113input qualification structures,5identity errata,9approval/import corrections and8stage contracts actually read.83original report bodies stay identity/old-reader routes; no R1 global finding total invented.','semantic-atlas/chunk-001.txt..chunk-010.txt; exact all source occurrences and structure schema in semantic-atlas/association-transport.json'),
 'EH-HISTORY-02':('All229 identity/stage associations and complete common qualified closing rules received; underlying229/341 body reports remain routed.308+33 are scoped receipt qualifications, not whole-ID or runtime PASS.','purpose-field-associations.json; semantic-atlas/manifest.json'),
 'EH-HISTORY-03':('All23controls/76criteria plus2excluded exceptions and applicable scope qualifications actually read from exact imported original/current structures. Successful dual messages remain distinct from backup-copy gate. Original U08 NOT_STARTED retained at its original time.','semantic-atlas/manifest.json; schema/context bindings; read-logs/009-r3-excluded-retry.receipt.json'),
 'EH-HISTORY-04':('All17original controls/76criteria and16/75 B5 qualification plus1partial residue read; C01-C05 limited successor independently compared to necessary R/B8 producer/consumer ranges. Strict expiry, guarded dynamic read, state before image request, no arbitrary rollback and explicit-number/hatching boundaries retained. No whole legacy ID new PASS.','semantic-atlas/manifest.json; consumer-reads/manifest.json; consumer-review.json'),
 'EH-HISTORY-05':('All92complete finite original scopes and current qualifications,568schema criterion/current result-signature associations,410native/158extra distinction,21shared receipts,18edges,85writer identity map and6admin/3correction records received.7optional/7no-required original dispositions,6policies and13limits all received separately. No historical signature transferred into a fresh global/behavior approval.','semantic-atlas/manifest.json; semantic-atlas/schema-unit-bindings.txt; semantic-atlas/nested-reason-bindings.txt; nonmandatory-reads/manifest.json; nonmandatory-reads/limits-source.json'),
 'EH-HISTORY-06':('Original erratum full body plus fixed R allsix relevant literal branches and B8 receiver clauses actually read. Plain dot/line anchors, peripheral whitespace and whole-field replacement consequences support the exact correction; wrong captured-body LF assertion excluded.33original standards and92finding denominator unchanged. Static only; vectors NOT_EXECUTED.','originals/sc-u07-001-erratum.json; consumer-reads/manifest.json; consumer-review.json'),
 'EH-HISTORY-07':('Old FAIL and narrow successor reports fully read; all applicable imported original/current criterion reasons read. Current R Item effective-consumption defaults/overrides, bag/party guards, six EV item handlers and helper, B8 receiving clauses/current named vector actually read. Consumable=false counterexample remains historical valid; revised nonimportant/effective-consumed-true row narrows premise.59exact reused static rows and other4exact prior ranges are not full11newly reviewed. No behavior execution.','originals/r5-u03-actual-fail.md; originals/r5-u03-limited.md; semantic-atlas/nested-reason-bindings.txt; consumer-review.json'),
 'EH-HISTORY-08':('Candidate FAIL/actual/final reports and exact current92 criterion/receipt scope joins read; current party/summary dynamic-read, rendering and form/registration dependencies independently read. BACK/cancel prevents requested movement but does not undo earlier display refresh commits; actual limited composite receipt does not become21fresh whole bodies. Parent owns activation and current reception.','originals/r5-u08-candidate-fail.md; originals/r5-u08-actual.md; originals/r5-u08-final.md; consumer-review.json')}
for r in accept['records']:
    if r['id'] in corrections:
        r['qualification']=corrections[r['id']][0]
        r['continuation_evidence']=corrections[r['id']][1]
    r['parent_reception']='NOT_RECEIVED_BY_PARENT'
    r['independent_counterreview']='PENDING_PARENT'
accept['records'] += [
 {'id':'EH-HISTORY-10','subject':'R5 original7optional/7no-required dispositions','facts_actually_read':'14original semantic records fully received with exact value/context reuse and source-pointer associations.7optional remain optional.7no-required include canonical duplicates and M05-005 expanded consumer merged into M12-101, distinct from rebutted M06/M12 claims. M11-0054optional facets do not add canonical IDs.','evidence':['nonmandatory-reads/manifest.json','nonmandatory-reads/associations.json','completion-scope.json'],'excluded_claims':['14new required findings','automatic optional update','fresh reading of each historical source anchor body'],'parent_reception':'NOT_RECEIVED_BY_PARENT','independent_counterreview':'PENDING_PARENT'},
 {'id':'EH-HISTORY-11','subject':'R5 original13limits and6policies','facts_actually_read':'L01-L13 all33lines of B8 frozen original limits copy read; source identity retained. Missing full project/media/native host differs from readable binaries/font/SF2/serialized content whose specific inspection exists. Old isolated runs and nonzero/unknown outcomes retain original scope.6compatibility policies have explicit facts, bounded inputs and future decisions; none automatically required.','evidence':['nonmandatory-reads/limits-source.json','originals/r5-limits-and-missing-materials.md','semantic-atlas/manifest.json'],'excluded_claims':['all current R8 limits individually re-established','readable content reclassified missing','source facts erased by future policy','runtime or native output PASS'],'parent_reception':'NOT_RECEIVED_BY_PARENT','independent_counterreview':'PENDING_PARENT'},
 {'id':'EH-HISTORY-12','subject':'Necessary current B8/R consumer crosscheck','facts_actually_read':'20exact source/spec bundles1083original lines read for SC LF correction, U03 consumption premise, Summary/party display read mutation and bottle nested-form ordering. Source producer to receiver and receiver to producer compared, with guards, normal control, minimal boundary and failure prefix retained. No new concrete current mismatch established within this scope.','evidence':['consumer-reads/manifest.json','consumer-review.json'],'excluded_claims':['all131formal full bodies read','all reference inventory freshly reviewed','global NO_REQUIRED_UPDATE','runtime execution'],'parent_reception':'NOT_RECEIVED_BY_PARENT','independent_counterreview':'PENDING_PARENT'}]
accept['evidence_identity_registers'] += ['semantic-atlas/association-transport.json','nonmandatory-reads/limits-source.json','consumer-reads/manifest.json']
save('history-current-acceptance-records.json',accept)

original=read('originals/r5-quarantined-scope.json')
save('completion-scope.json',dict(schema='r8.external-h.completion.v1',reader=READER,recorded_utc=NOW,
 bounded_semantic_status='COMPLETE_FOR_DELEGATED_H_PURPOSE_PENDING_PARENT',
 original_denominators=denominators,
 presentation_only_statistics={'atlas_groups':6857,'atlas_chunks':65,'atlas_administrative_leaf_occurrences':180833,'nonmandatory_new_value_groups':908,'nonmandatory_chunks':7,'nonmandatory_exact_same_context_reuse_occurrences':773,'nonmandatory_identity_routes':1562,'not_a_semantic_clause_denominator':True},
 nonmandatory_original_dispositions=[dict(id=x['id'],disposition=x['disposition'],status=x['status']) for x in original['findings']],
 raw_body_credit='4/10 full raw bodies; remaining6 purpose-complete with explicit identity/admin routes, never FULL_READ',
 semantic_unread_in_delegated_current_scope=0,
 material_blockers=[],parent_reception='0/10payloads and0/12semantic records final received; pending independent parent review',
 signatures='All historical percheck results/signatures retained at exact identity and limited scope; no fresh runtime or blanket whole-ID approval',
 vector_execution='NOT_EXECUTED',new_behavior_execution=0,final_state='UPDATE_NOT_STARTED'))

process=read('process-evidence.json')
process['continuation']={'recorded_utc':NOW,'exact_chunk_read_acknowledgements':'read-acknowledgements.json','no_reference_or_evidence_execution':True,'atlas':'65continuous chunks actually read plus full context/percheck/nested-reason bindings','nonmandatory':'7continuous chunks plus limits33lines actually read','consumers':'20bundles1083original lines actually read; raw reference source local-only','truncated_attempts_excluded':['007-r3-excluded; retry009 complete','schema-bindings-0011-190; complete retries1-90,91-230,231-400,401-570'],'metadata_output':'Generated role-schema only first110lines viewed; remaining mechanical inventory receives no semantic credit; uncompressed file ignored','own_locator_error':'Initial U03 Item path used007 rather than actual006; failed capture made no evidence execution, corrected before complete reading','index_transport':'Lossless gzip with dual identities; restoration gives no semantic credit'}
save('process-evidence.json',process)
finding=read('findings.json')
finding['interpretation']='No new concrete current mismatch established in completed bounded H qualification/necessary-consumer review.0proposals is not a global NO_REQUIRED_UPDATE/PASS; parent owns independent counterreview and final reception.'
save('findings.json',finding)
progress=read('progress.json')
progress.update(status='H_BOUNDED_SEMANTIC_COMPLETE_PENDING_PARENT',semantic_complete=True,recorded_utc=NOW,summary=summary,remaining_blocker=None,publication='Semantic core ready for ordinary report-only commit/push and complete remote readback; publication.json successor will bind the frozen core')
save('progress.json',progress)
print(json.dumps({'summary':summary,'acknowledgements':len(acks),'denominators':denominators,'association_transport':ident(compressed)},ensure_ascii=False))
