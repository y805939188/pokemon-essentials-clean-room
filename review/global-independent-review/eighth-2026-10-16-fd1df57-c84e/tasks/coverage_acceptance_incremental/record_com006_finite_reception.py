import json,datetime,hashlib
from pathlib import Path
b=Path(__file__).resolve().parent
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
raw=(b/'delta-inputs/root-COM006-developer-0807/00-root-com006-counterreview.json').read_bytes()
check=json.loads((b/'com006-own-fixed-git-selected-units.json').read_text())
assert len(raw)==87003 and hashlib.sha256(raw).hexdigest()=='5a5a48d773e45c7f624ccad3f547655aa5baaab6e0f73da20cb2c245c5751e68'
assert check['exit']==0 and len(check['checks'])==18
receipts=[f'late-com006-expanded-{i:02}.receipt.json' for i in range(1,6)]
p={
 'schema':'r8-coverage-COM006-finite-current-reception-v1','utc':now,'auditor':'/root/coverage_acceptance_incremental',
 'source':{'path':'adjudication/root-com006-counterreview.json','snapshot':'delta-inputs/root-COM006-developer-0807/00-root-com006-counterreview.json','bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()},
 'actual_body_receipt':'FULL_CURRENT_FIELDS_AND_ALL_EMBEDDED_UNITS_READ_IN_LOSSLESS_VIEW',
 'lossless_view':{'path':'late-com006-complete-expanded-view.json','lines':1595,'sha256':'43de2a5a874bb4fa04f4ff750e237324428fcf525df59df332b3ea0e3f237c5d','ranges':[[1,350],[351,700],[701,1050],[1051,1400],[1401,1595]],'receipts':receipts,'all_original_values_preserved':True},
 'original_truncated_attempt':{'receipt':'late-COM006-counter-01.receipt.json','range':[1,130],'qualification':'TRUNCATED_NOT_SOLE_FULL_READING_EVIDENCE; repaired by all1595L lossless-view windows'},
 'own_fixed_Git_check':'com006-own-fixed-git-selected-units.json','selected_units_verified':18,'selected_unique_paths':11,
 'manual_semantic_reception':[
  'Complete producer class writes target Powder after target guard; it is not the HP writer. DefaultPOWDER maps function, defaultEMBER supplies ordinary FIRE example.',
  'At reached pbUseMove Powder+FIRE branch animation/display then lastMoveFailed=true precede the damage-only condition; !Rain/HeavyRain of user.effectiveWeather AND takesIndirectDamage? gate pbTakeEffectDamage and enclosed gainExp. Cancellation/endturn/return remain on both branches.',
  'Ordinary effectiveRain legal counterexample suppresses Powder HP writer while preserving failure. StoredRain plus active UtilityUmbrella may produce effectiveNone; therefore stored/battle/member-effective weather cannot be substituted. Active MagicGuard qualification stipulated; complete dispatcher not received.',
  'Master425L unit proves actual position before primordial Fire suppression and earlier PP/history prefix; complete reducer/TakeEffectDamage units show HP write before item/ability/faint consumers with no exact finalHP or rollback claim.',
  'Complete EOR main184L plus begin/cancel/endturn units qualify Powder tail reset: only reached normal tail/current living members, explicit earlier decision returns remain. WP42 already states this.',
  'Strongest optional interpretation actually considered: WP40 scope excludes effect families and step14 is an overview. Bounded required conclusion remains supported because this explicit sufficient damage implication is owned/routed to WP40 and differs on ordinaryRain; no general obligation to enumerate every immunity inferred.',
  'Accept GR8-COM-006 requiredP3 only exact WP40§5.2 step14 Powder parenthesis; preserve all same-line other ordering and correct WP47-A/WP45/WP42. No mandatory new test or automatic remediation.'
 ],
 'bounded_root_classification_received':{'canonical_id':'GR8-COM-006','classification':'required','severity':'P3','new_independent_vote_created':False,'additional_context_created':0,'whole_current_root_aggregate_packet_read':False,'registry_reported_totals':{'records':26,'required':22,'P2':2,'P3':20,'optional':4},'totals_qualification':'Prior25 bounded records received plus this finite counter; no whole-review required count or full latest aggregate packet claim.'},
 'still_open':['All global historical dedup and complete historical reopen qualifications','Complete activeMagicGuard dispatcher and every actual source/formal consumer','All11 source/formal paths as whole-file reading: only selectedunits received','All primary/domain/global task contract completion; no final acceptance signed'],
 'own_full_source_credit_added':0,'own_source_partial_ranges':'Actual embedded units read and independent fixedGit checked as listed in proof; not yet merged into global file-coverage partial count. Current conservative ownpartial9R/2F counts retained.',
 'original289_count_unchanged':{'qualified':248,'pending':41,'pending_original_unique_bytes':106120006},
 'business':'NOT_EXECUTED','update':'UPDATE_NOT_STARTED','global_pass':False}
(b/'COM006-complete-finite-reception.v1.json').write_text(json.dumps(p,ensure_ascii=False,indent=2)+'\n')
for name in ['progress.json','reading-ledger.json','acceptance-register.json','execution-records.json','coverage-gaps.json','next-dispatch.json']:
 path=b/name;j=json.loads(path.read_text());j['COM006_complete_finite_reception']=p;j['updated_utc']=now
 path.write_text(json.dumps(j,ensure_ascii=False,indent=2)+'\n')
with (b/'review.md').open('a') as f:f.write('\n'+now+'：COM00687003B固定late包已全文接收，1595行无损展开五段完整读，18嵌入单元/11路径另经本context固定Git字节核验。接受唯一WP40§5.2step14粉尘自损effectiveWeather/indirect-damage门限定requiredP3；失败仍成立。原25有界分类加本条，不新增独立票，不授最新aggregate整包或全史去重/全域/完成信用。原289读集仍248已按目的接收/41未完整接收106120006B，源码全文仍R1/F0。\n')
print(json.dumps({'utc':now,'proof':'COM006-complete-finite-reception.v1.json','exit':0,'original289_counts_unchanged':'248/41','full_file_source_credit_added':0},ensure_ascii=False))
