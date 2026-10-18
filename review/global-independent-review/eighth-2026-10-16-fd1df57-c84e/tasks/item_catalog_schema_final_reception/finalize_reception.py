"""Finalize evidence metadata only; no reference execution or business tests."""
from pathlib import Path
import datetime, hashlib, json, subprocess

OUT=Path(__file__).resolve().parent
ROOT=OUT.parent.parent
REPO=ROOT.parent.parent.parent
NOW=datetime.datetime.now(datetime.timezone.utc).isoformat()

def ident(p):
    b=p.read_bytes()
    return dict(path=str(p),bytes=len(b),sha256=hashlib.sha256(b).hexdigest(),
        git_blob_from_bytes=hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest(),mode=oct(p.stat().st_mode&0o777))
def dump(name,x):
    (OUT/name).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')

cat=json.loads((OUT/'catalog-operative-complete-mapping.v1.json').read_text())
view=['有限Item catalog实际完整操作接收。46条主向量，非669行whole catalog重审；业务执行0。','共同前提：']
for p in cat['common_premises']:
    view += [p['id']+' '+p['meaning'],json.dumps(p['locations'],ensure_ascii=False)]
for n,v in enumerate(cat['vectors'],1):
    view += ['',f"{n}/46 {v['id']} {v['catalog_path']}:{v['line']}",
             '完整输入/预期：'+v['complete_current_clause'],
             '实收操作意义：'+v['accepted_operation'],
             '取消/失败/已写前缀：'+v['cancellation_failure_and_reached_prefix'],
             '全部适用共同前提：'+','.join(v['common_premises']),
             '当前WP50行：'+','.join(map(str,v['current_formal']['lines'])),
             '原已接source组：'+','.join(v['already_root_received_producer_groups']),
             '原已接handler：'+','.join(v['already_root_received_handler_bindings'])]
view += ['', '历史资格：WP50:179/181只保留原限定输入/阶段，root全局历史接合另收；本任务不继承当前合规票。',
         '有限未读0/未接0。whole Item/global未签；全部业务执行NOT_EXECUTED。UPDATE_NOT_STARTED。']
(OUT/'catalog-complete-operative-reception.view.txt').write_text('\n'.join(view)+'\n')

sub=OUT/'schema-subreview'
q=json.loads((sub/'qualification.json').read_text())
raw=ROOT/'evidence/adjudication-inputs/708d62e93db2e05400d442be3da03219250e7ec6f2bac11fa0b0ce5108cfe3a7.json'
assert ident(raw)['sha256']==q['original_companion']['sha256']
dump('schema-qualified-reception.v1.json',dict(schema='gr8-item-schema-tail-operative-reception/v1',utc=NOW,
    received_by='/root/item_catalog_schema_final_reception',
    actual_source_reader='/root/item_catalog_schema_final_reception/schema_companion_qualification',
    complete_original_companion=ident(raw),original_bytes_preserved=True,
    full_semantic_payload=ident(sub/'report.md'),full_structured_qualification=ident(sub/'qualification.json'),
    source_and_formal_qualification=ident(sub/'read-identity-ledger.json'),
    original_producer_qualification='Original70dee4 source/selected-data reader ownership retained; this subreview newly reads only finite Item/schema/parser definitions, not868raw/862selected/PBS4 record semantics.',
    parent_actual_full_receipt=['original2807-byte companion all fields','schema-subreview/report.md whole','schema-subreview/qualification.json whole','schema-subreview/read-identity-ledger.json whole'],
    parent_additional_finite_read=[dict(repo='/workspace/pokemon-essentials',path='Data/Scripts/010_Data/002_PBS data/006_Item.rb',ranges=[[25,44],[119,202]]),dict(repo=str(REPO),path='deliverables/final-specification-set/creature-rpg/wp27-bag-and-item-storage.md',ranges=[[45,71]]),dict(repo=str(REPO),path='deliverables/final-specification-set/generic-kernel/wp03-content-identity-and-schema.md',ranges=[[138,173]])],
    complete_field_default_and_input_contract='Whole table and parser/compilation paragraphs in bound report.md; all17 field/source entries actually received. No keyword-only or hash-only credit.',
    effective_schema=q['effective_schema'],ShowQuantity_qualification=q['ShowQuantity_qualification'],
    mandatory_effective_meaning='Original unsigned overgeneralization and derives-consumable ShowQuantity sentence are preserved only as history. Adopt correctedv/u/exact-inline-alias meanings and stored ShowQuantity true OR non-important, independent of Consumable. Current formal correct.',
    transport=dict(gzip_path=str(ROOT/'evidence/compressed/708d62e93db2e05400d442be3da03219250e7ec6f2bac11fa0b0ce5108cfe3a7.gz'),gzip_present=False,gzip_recovery_claimed=False,complete_plain_sha_verified=True,semantic_blocker=False),
    finite_unread=0,finite_unreceived=0,new_formal_findings=0,new_required=0,new_optional=0,business_executions=0,
    no_whole_item_signoff=True,no_global_signoff=True,UPDATE_NOT_STARTED=True))

ledger=json.loads((OUT/'identity-read-ledger.v1.json').read_text())
ledger.update(utc=NOW,state='FINITE_CATALOG_SCHEMA_TAIL_RECEIVED_ROOT_CONSOLIDATION_READY',
    schema_semantic_receipt=ident(OUT/'schema-qualified-reception.v1.json'),
    schema_subreview_actual_reader='/root/item_catalog_schema_final_reception/schema_companion_qualification',
    schema_subreview_identity_ledger=ident(sub/'read-identity-ledger.json'))
dump('identity-read-ledger.v1.json',ledger)
dump('remaining.v1.json',dict(schema='gr8-item-catalog-schema-tail-remaining/v1',utc=NOW,
    finite_necessary=dict(catalog_vectors=46,catalog_received=46,catalog_unread=0,catalog_unreceived=0,schema_necessary_unread=0,schema_necessary_unreceived=0),
    root_remaining=[dict(path='deliverables/final-specification-set/pokemon-rules/wp50-held-item-triggers-and-consumption.md',lines=[179,181],kind='ROOT_GLOBAL_HISTORY_JOIN',meaning='Historical limitedPASS/CLOSED only within original fixed inputs/stages; this task does not grant R8 current source/full-system approval.')],
    known_nonblocking_transport=['Named708d62 gzip absent in current tree; exact complete2807-byte plain SHA received. No gzip recovery verification claimed.','Original producer commit object not locally parseable by schema subreview; exact root-recovered31-file store used, no additional material blocker.'],
    not_repeated_or_upgraded=['Root-received698 meanings/247 controls/166 reverse','All6peer and10finite joins','862selected five-field records/224unique tuples','868raw or whole foreign PBS','Whole foreign primary source/formal/catalog units outside actual listed ranges','Full Item or root global final signoff'],
    findings=dict(new_formal=0,new_required=0,new_optional=0),business_executions=0,UPDATE_NOT_STARTED=True))

# Verification checks identity/referential consistency only. It is not a
# reference test, simulated behavior execution, or a new source semantic read.
preserved=[]
for old in ledger['producer_originals_preservation']:
    cur=ident(Path(old['path']))
    assert cur['sha256']==old['sha256'] and cur['bytes']==old['bytes'],old['path']
    preserved.append(cur)
assert len(cat['vectors'])==46 and len({x['id'] for x in cat['vectors']})==46
assert all(v['complete_current_clause'] and v['accepted_operation'] and v['cancellation_failure_and_reached_prefix'] for v in cat['vectors'])
assert sum(v['bytes'] for v in preserved)==1269073 and len(preserved)==31
manifest_paths=[p for p in sorted(OUT.rglob('*')) if p.is_file() and p.name!='delivery-manifest.v1.json']
dump('delivery-manifest.v1.json',dict(schema='gr8-item-catalog-schema-tail-delivery/v1',utc=NOW,
    state='FINITE_TAIL_COMPLETE_ROOT_CAN_DIRECTLY_RECEIVE',files=[ident(p) for p in manifest_paths],
    original_producer_files_verified_unchanged=31,original_producer_bytes=1269073,
    companion_verified_unchanged=ident(raw),mechanical_validation='All structured JSON readable;46 unique applicable IDs/nonempty operative inputs/meanings/prefixes; original31 files and2807-byte companion unchanged. No business tests.',
    remaining='remaining.v1.json',business_executions=0,UPDATE_NOT_STARTED=True))
print(json.dumps([ident(OUT/n) for n in ['review.md','catalog-operative-complete-mapping.v1.json','catalog-complete-operative-reception.view.txt','schema-qualified-reception.v1.json','identity-read-ledger.v1.json','remaining.v1.json','delivery-manifest.v1.json']],ensure_ascii=False,indent=2))
