"""Bounded same-context continuation; never run reference code or old builders."""
from pathlib import Path
import json,hashlib,datetime,subprocess,collections

TASK=Path(__file__).resolve().parent
RR=TASK.parent.parent
ROOT=RR.parents[2]
REF=Path('/workspace/pokemon-essentials')
RC='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
BC='fd1df570cad987dc3852a3b958f03916e317f7fe'
EXT=RR/'evidence/external-recovered/receive_external_pbs_creature_backups/96ee9a69e24d5e2063be7ebcf8de0fdb2e019510'
PCR=RR/'tasks/pbs_creature_current_cloud'
NOW=datetime.datetime.now(datetime.timezone.utc).isoformat()
HIST=TASK/'continuation-v1';HIST.mkdir(exist_ok=True)
def rj(p):return json.loads(p.read_text())
def put(p,v):p.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
def sha(raw):return hashlib.sha256(raw).hexdigest()
def identity(p):
 raw=p.read_bytes();return {'path':str(p.relative_to(RR)) if p.is_relative_to(RR) else str(p),'bytes':len(raw),'sha256':sha(raw),'blob':hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()}
def archive(name):
 dest=HIST/('prior-'+name)
 if not dest.exists():dest.write_bytes((TASK/name).read_bytes())
for n in ['review.md','interfaces.json','progress.json','external-data-62.json','reverse-mapping.json','reading-ledger.json','artifact-manifest.json']:
 archive(n)

full_read=[
 RR/'adjudication/root-kernel-task-final-acceptance.v1.json',
 RR/'adjudication/root-developer-task-final-acceptance.v1.json',
 RR/'adjudication/root-pbs-current-task-final-acceptance.v1.json',
 RR/'adjudication/root-pbs-backups-task-final-acceptance.v1.json',
 RR/'adjudication/root-item-task-final-acceptance.v1.json',
 RR/'adjudication/mandatory-item-showquantity-schema-meaning-qualification.v1.json',
 RR/'adjudication/mandatory-item-pinch-false-gluttony-meaning-qualification.v1.json',
 EXT/'report.md',EXT/'interfaces.json',EXT/'necessary-provider-reception.json',EXT/'proposal-counters.json',
 PCR/'review.md',PCR/'owned-scope-handoff.v1.json',PCR/'remaining-necessary-interfaces.v1.json']
receptions=[{'identity':identity(p),'actual_receiver':'/root/pbs_battle','status':'ACTUAL_COMPLETE_OPERATIVE_READ_THIS_CONTINUATION',
 'qualification':'Semantic meanings and complete common premises read. Source/raw records credit stays actual named reader; root signature is bounded scope evidence, not a new root/source re-read or whole-domain PASS.'} for p in full_read]
selected=[
 (EXT/'received/gen8/1f4504d849caa15e25decb49640e1e66fbcc4932/provider-receptions.json',
  ['fixed_packets/0/adopted_complete_objects/common_premises',
   'fixed_packets/0/adopted_complete_objects/manual_groups/species.identity',
   'fixed_packets/0/adopted_complete_objects/manual_groups/species.types',
   'fixed_packets/0/adopted_complete_objects/manual_groups/species.ability',
   'fixed_packets/0/adopted_complete_objects/manual_groups/species.moves',
   'fixed_packets/0/adopted_complete_objects/manual_groups/species.items',
   'fixed_packets/0/adopted_complete_objects/manual_groups/species.stats',
   'fixed_packets/4/adopted_complete_objects: SAVE01–SAVE07 and entire common/failure/open predicates',
   'fixed_packets/9/adopted_complete_objects: all11 PC facts and premises; mandatory3 exclusions applied',
   'fixed_packets/3/adopted_complete_objects/units/WFS-085: complete5 wild-constructor assertions; other truncated unselected units not credited']),
 (PCR/'typed-record-facts.v1.json',['paths/1 entire18 Move raw fields/order/omission values','paths/3 entire1 Type raw fields/order/omission values']),
 (PCR/'mandatory-primary-token-type-clarification.v1.json',['all8 complete original field objects and corrected compiled scalar values','complete scope/qualification/transitive-copy meanings; repeated reference source bodies not credited here as whole artifact read']),
 (PCR/'shadow18-shared-success-interface.complete.v1.json',['common_premises/all12 SSI facts and precise ranges/formal binding/remaining meaning','18 original Move fields separately completely received; no personal14source-body raw FULL']),
 (PCR/'shadow18-four-target-consumer-finite.v1.json',['all5 common premises and optional activation extra premise','all14 TG facts/precise formal-source bindings/open qualifications; full source body array not re-read here'])]
receptions += [{'identity':identity(p),'actual_receiver':'/root/pbs_battle','status':'ACTUAL_COMPLETE_SELECTED_OBJECT_MEANINGS_RECEIVED',
 'selected_objects':s,'unselected_artifact_bytes':'NOT_CLAIMED_PERSONALLY_READ','not_new_full_raw_source_reader':True} for p,s in selected]

readers=[
 {'generation':5,'commit':'77c68ef907bece03291accccf7c8d3f3f3bc7753','actual_reader':'01a144a2-cdca-74e0-a8b6-5f8e90d95021','records':735},
 {'generation':6,'commit':'4d9fdaacc42cb061917d92578d3b247c03ca9739','actual_reader':'01a144a2-f115-7357-815c-37ff4bb71008','records':909},
 {'generation':7,'commit':'aa765be41e1a9ad978faeb6706f673364a0a3a75','actual_reader':'01a144a3-0dee-733e-a9a4-e379313fc01f','records':1059,'child_UUID_self_echo':'UNVERIFIED','binding':'actual original parent dispatch retained'},
 {'generation':8,'commit':'1f4504d849caa15e25decb49640e1e66fbcc4932','actual_reader':'01a144a3-2a91-70f0-af3a-b232b52c602f','records':1237}]
qualifications=[
 'FixedR/B8, no plugin/redefinition/concurrent mutation; all normal branches require valid registered dependencies and earlier calls returning normally.',
 'Default and Gen5–8 and Shadow remain separate activation domains. Directory existence, mechanics-generation setting or identical bytes never automatically activate/merge alternatives.',
 'All3077base/863form values and concrete same-generation inheritance stay original qualified complete readers, not new personal3940raw reads. Name/Gender/Growth/Incense inherit despite no form-author schema; FormName/PokedexForm own defaults and triple wilditem inheritance only all3 absent retained.',
 'Complete actual wildconstructor383–449: one rand100 before equal-array branch; equal three arrays chooses common.sample, all empty givesnil; ordinary50/5/1 versus CompoundEyes/configuredSuperLuck60/20/5. It uses lead raw ability_id and direct item=, not generalactive/can_hold predicate. Later PID/virus/gender/nature/form/callback failures preserve prior reached prefixes.',
 'MAIL source is006_Item_Mail.rb125L (4997B/cfbecae348f4644cde518f77b41daae00ad721527914ebc5634cd2e9395098bd), never005. Immutable oldwrongobjects use complete5113B/677644 mandatory companion.',
 'ShowQuantity is rawtrue OR nonimportant, independent Consumable. Ordinary explicitfalse stillshows; important omitted/false false, explicittrue true. Important=KeyItem/TM/HM; TR alone notimportant.',
 'Berry modefalse does not require Gluttony, including activeGluttony; it never requires Gluttony absent. Berry permission/HP<=half/ordinaryactive and caller eligibility remain distinct.',
 'Reject any-held-MegaStone exclusion: matchingstone OR knownMegaMove remains; bareRAYQUAZA knowsDRAGONASCENT canselectform1 holding anotherstone. No generalbattlepermission inferred.',
 'Reject successful Encounter predicate alwaysreset: returntrue and explicitreset/latercallers differ. Reject general TutorMoves uniq: Speciescompile onlyTypes uniq; authored Tutor repeats remain; reset_moves separately keeps latest eligible levelMove occurrences thenlast4.',
 'Shadow metadata actually received18moves/1type, not personally rawFULL. SHADOW IsSpecialType=true, IconPosition compiledInteger19; earlier tokenstring19 is qualified by8field companion. All18PP0, fourTargets, CanProtect; onlyShadowPanicSound; noBomb. SharedSuccess/gates canrefuse, Accuracy100 not universalhit.',
 'ShadowShed exactRemoveAllScreens lawfulmissingimplementation fallsbackStatusfailure, distinctRemoveAllScreensAndSafeguard. BothSides emptylist doesnot override localfailure. ExistingWP43alreadydocuments; no newproposal.',
 'All save facts preserve whole top-level values and sequential callback/classcheck/partial assignment/write prefixes; no inner objectgraph/nativealias/cycle/binary/readback guarantee.',
 'Root kernel4732 semantics/4792work and existing31 scopegroups do not transfer personal raw/source/fullformal reading here. Original primaryformal0 and own5supplemental fulltext qualification unchanged.',
 'CURRENT math+1/602 is its original separate audit; this context ran no new numeric/behavior model and doesnot recount it.',
 'Historic rootdecisions/optional/required handoffs are bounded existing state references, not proof of currentsource or new canonical count; globalhistory/dedup remains root scope without blocking this already-proven necessary chain.'
]
dispositions=[
 {'id':'PB-O01','prior':'62union external record or source semantics not received here','current':'CLOSED_FOR_THIS_NECESSARY_SCOPE',
  'actual_join':'Qualified complete CURRENT11/2178 and backup16/6712 original reader contributions now received for exact referenced identity/schema/compile/form/item/AI data-family inputs and common activation/failure premises. IF01/02/05/07/08/09/CD-I06 and the full12-interface operatives bind local ownCompiler/PokemonMove/BattleMove/AIMove. Own newly read wild/item/form units resolve the concrete pool→assignment consumer.',
  'necessary_missing':[],'personal_raw_qualification':'Original external28not-own-fullread remains; original primary21reading/receipt statuses unchanged. Broad62union is not re-assigned primary or a request for allforeign callbacks.'},
 {'id':'PB-O02','prior':'Supplemental kernel residual atomics/foreign consumers pending','current':'CLOSED_FOR_THIS_NECESSARY_SCOPE',
  'actual_join':'This task owncompleteRegistry/Compiler1117/4schemas/Targets/startup/objectquery units already prove all stated PBS predicates. Rootqualified currentkernel signature and exact mandatory corrections received. No additional particular local predicate or caller remains missing; wholekernel approval was an overbroad blocker.',
  'necessary_missing':[],'retained':'Five supplemental formal own全文 and21finite manualreverse units stay as read. Old2219/771snapshot not rewritten into own4732review.'},
 {'id':'PB-O03','prior':'WholeMove/AbilityItem/AI/Facility formal and all dependency tails pending','current':'CLOSED_FOR_THIS_NECESSARY_SCOPE',
  'actual_join':'All20localfacts, full named source-family meanings,331Movevectors/31AIsharedAB/14AIinterfaces/13Facility/PBF8boundedfacts were already actually received. CURRENT SSI12/TG14 and19optionalmetadata records now finitely join same gates; rootItem46catalog/schema mandatory qualifiers received. No concrete producer/consumer premise within stated21primary is missing.',
  'necessary_missing':[],'retained':'Allforeign domains keep their final approval/history/native/runtime scope; receiving them doesnot make thiscontext anotherrawreader or new independent vote.'},
 {'id':'PB-O04','prior':'Root/history current finalglobaladjudication pending','current':'DISPOSED_AS_RETAINED_ROOT_GLOBAL_QUALIFICATION_NOT_LOCAL_BLOCKER',
  'actual_join':'Currentroot task-final objects read with currentdecisionmandatory qualifiers; no oldPASS/closedstatus supplies semanticproof. No newproposal requires counterreview. Originalroot globalhistory/equivalent-directory/actualmodel/nativecompletion remains separate.',
  'necessary_missing':[],'retained':'UNVERIFIED historicalexecution and wholehistory/globalreview remain explicit, not hidden as finished or calledhostlimit.'}]
put(TASK/'necessary-reception.v2.json',{'schema':'gr8-pbs-battle-necessary-reception/v2','utc':NOW,'actual_receiver':'/root/pbs_battle',
 'continuation':'Same original context; newcontexts0,newvotes0; no second full globalreview layer',
 'fixed_R':RC,'fixed_B8':BC,'backup_qualified_commit':'96ee9a69e24d5e2063be7ebcf8de0fdb2e019510','original_generation_readers':readers,
 'actual_receptions':receptions,'mandatory_qualifications':qualifications,'four_interface_dispositions':dispositions,
 'necessary_available_unread':0,'necessary_consumer_unreceived':0,'business':'NOT_EXECUTED','new_business_runs':0,'UPDATE_NOT_STARTED':True})

previous=rj(HIST/'prior-interfaces.json')
previous['schema']='gr8-pbs-battle-interfaces/v2'
previous['utc']=NOW
previous['open_before_same_context_continuation']=previous.pop('open')
previous['open']=[]
previous['dispositions']=dispositions
previous['current_necessary_available_unread']=0
previous['current_necessary_consumer_unreceived']=0
previous['status']='REVIEW_COMPLETE_WITH_RETAINED_SCOPE_QUALIFICATIONS_READY_FOR_ROOT_TASK_FINAL'
previous['actual_receipt']='necessary-reception.v2.json'
previous['retained_qualifications']=qualifications
previous['original_primary_reading_credit_unchanged']={'own_full':11,'own_then_exact_byte_association':5,'namedraw':4,'namedassociation':1,'records':7704}
previous['not_current_blockers']='Wholeforeignprimaryapproval/personalrawunread/globalhistory/nativeexecution are retained scope qualifications; none is silently zeroed or made a new unbounded primary readset.'
previous['root_task_final']='ROOT_ONLY_NOT_SELF_SIGNED'
put(TASK/'interfaces.json',previous)

remaining={'schema':'gr8-pbs-battle-remaining/v2','utc':NOW,'status':'NO_CURRENT_NECESSARY_AVAILABLE_UNREAD_OR_UNRECEIVED',
 'primary_paths':21,'primary_path_records':7704,'primary_unread':0,'primary_record_field_semantics_unreceived':0,
 'current_necessary_available_unread':[],'current_necessary_consumer_unreceived':[],'current_necessary_readable_missing_count':0,
 'four_prior_interfaces':dispositions,'retained_foreign_personal_raw_unread':'Original28outerpaths not personally read in full; exact prior classifications remain external-data-62 and continuation-v1/prior-external-data-62.json. Qualifiedowner contribution receipt is not personalrawFULL.',
 'fullforeignapproval_not_granted':True,'globalhistory_and_rootfinal_not_self_granted':True,
 'execution_qualifications':['reference/engine/game/native NOT_EXECUTED','no independent business model or numeric run added','real save/load/serialized objects/pixels/audio not executed','actual model/effort/tier/Fast/platform opaqueID UNVERIFIED'],
 'new_candidates':0,'new_required':0,'new_optional':0,'new_contexts':0,'new_votes':0,'UPDATE_NOT_STARTED':True}
put(TASK/'remaining.v2.json',remaining)

ext=rj(HIST/'prior-external-data-62.json')
for row in ext['records']:
 row['personal_raw_status_preserved']=row['this_receiver_status']
 row['current_necessary_missing_predicate']=None
 row['qualified_owner_contribution']='THIS21_ORIGINAL_READER' if row['is_this_primary'] else 'Qualified original CURRENT/BACKUP and finite source facts received only for identified data-family/common premises; wholeexternalraw/formal is not personalFULL'
 row['whole_foreign_domain_approved_by_this_task']=False
ext.update(schema='gr8-pbs-battle-ai-outer-readset-disposition/v2',updated_utc=NOW,
 status='EXACT_OUTER_UNION_NAVIGATION_NOT_NEW_PRIMARY_OR_NECESSARY_BLOCKER',necessary_missing_count=0,
 prior_personal_status_counts=ext.pop('status_counts'),
 interpretation='Originalstatus counts preserve personalrawqualification. Currentqualified necessaryreceipt and producer semantic scope is explicit; neither untouchedsourcebytes nor everyforeignformalpredicate are newlyread or approved.')
put(TASK/'external-data-62.json',ext)

# Append only actually new complete finite source readings, preserving old raw IO
# credit and the primary21 qualification without rerunning any earlier builder.
ledger=rj(HIST/'prior-reading-ledger.json')
newio=[json.loads(l) for l in (TASK/'read-io/index.jsonl').read_text().splitlines() if '2026-10-16T14:' in l]
for z in newio:
 z['semantic_status']='OWN_ACTUAL_COMPLETE_RELEVANT_UNITS_READ'
 z['unit_scope']='Wildconstructor383–449; Pokemonitem552–583 only plus visible context fragment; Formscompile388–485. No whole-file FULL promotion.'
ledger['same_context_continuation']={'utc':NOW,'new_contexts':0,'new_votes':0,'own_new_finite_read_operations':newio,
 'qualified_necessary_receipts':'necessary-reception.v2.json','not_personal_raw_record_rereads':'Original21primaryqualificationunchanged; optional19records named rawreader remainsPCR; backup6712 originalreaders retained.'}
ledger['current_necessary_available_unread']=0;ledger['current_necessary_consumer_unreceived']=0
put(TASK/'reading-ledger.json',ledger)

reverse=rj(HIST/'prior-reverse-mapping.json')
reverse['same_context_necessary_scope_reconciliation']={'utc':NOW,'actual_receipt':'necessary-reception.v2.json',
 'current_necessary_missing_predicates':0,'prior_broad_unaccepted_remainder_disposition':'Only original foreign scope/globalhistoricalqualification retained. Not a concrete missing prerequisite for local finite21primary chain.',
 'supplemental_manual_units_and_own_read_credit_unchanged':True,'root_kernel_final_not_personal_atomic_denominator':True}
put(TASK/'reverse-mapping.json',reverse)

progress=rj(HIST/'prior-progress.json')
progress.update(updated_utc=NOW,status='REVIEW_COMPLETE_WITH_RETAINED_SCOPE_QUALIFICATIONS_READY_FOR_ROOT_TASK_FINAL',
 same_context_continuation=True,new_contexts=0,new_votes=0,open_ids=[],necessary_available_unread=0,necessary_consumer_unreceived=0,
 retained_qualifications='remaining.v2.json',root_task_final='ROOT_ONLY_NOT_SELF_SIGNED',delivery_snapshot_utc=NOW,
 actual_process_end_utc='UNVERIFIED_UNTIL_PLATFORM_TURN_END',execution='NOT_EXECUTED',update='UPDATE_NOT_STARTED')
put(TASK/'progress.json',progress)

report=(HIST/'prior-review.md').read_text()
report=report.replace('外域可读记录、完整正式条款接收及历史资格仍开放，不能将本结果升级为全局 `NO_REQUIRED_UPDATE`。','同上下文必要接口续审已逐一完成，当前必要可得未读／消费者未接收均为 0；外域个人原文未读、整域批准、历史及执行资格仍保原范围，不能将本结果升级为全局 `NO_REQUIRED_UPDATE`。')
report=report.replace('`PRIMARY_COMPLETE_FINITE_JOINS_COMPLETE_GLOBAL_EXTERNAL_JOINS_OPEN`','`REVIEW_COMPLETE_WITH_RETAINED_SCOPE_QUALIFICATIONS_READY_FOR_ROOT_TASK_FINAL`')
start=report.index('精确开放处置见 [interfaces.json]')
end=report.index('本上下文只写 `tasks/pbs_battle/`',start)
report=report[:start]+'''同一实际上下文续审后的处置见 [interfaces.json](interfaces.json)、[necessary-reception.v2.json](necessary-reception.v2.json) 与 [remaining.v2.json](remaining.v2.json)。**本方当前必要可得未读 0、必要消费者未接收 0**；原 21 路径的 11／5／4／1 阅读资格和 7704 记录分母不变，没有新增上下文或独立票。续审前原字节保留在 `continuation-v1/`。

`PB-O01` 已按本方所需数据族收口。CURRENT 原实际读者的 11 路径／2178 完整记录贡献及 Gen5–8 独立读者的 6712 记录贡献，按各自当前有限接口和共同前提接收；不是本人再读 3940 基础／形态原文。固定备份贡献为 `96ee9a69e24d5e2063be7ebcf8de0fdb2e019510`，其 report、12 接口、necessary-provider 和 counter 完整实际读入，root task-final 的现行资格也完整读入。四代真实 reader 与 Gen7 UUID 自回显 UNVERIFIED 均保留。62 路径只是外域导航 union，原 28 个非本人完整原文路径仍逐个保留个人资格；它们的整域最终批准不构成本方已完成必要链的新阻塞。

具体再接合了三持物池的同代具体继承、引用字段、保存值及实际生成。本人补读野生生成完整383–449、Pokemon 持物552–583和形态编译388–485：rarity 的一次 rand100 在三数组相等分支之前；三数组相等选 common.sample，全空得 nil；直接 item= 验证身份但不调用 can_hold?。normal50/5/1 与首成员 COMPOUNDEYES／配置 SUPERLUCK 的60/20/5分别保留；后继 PID／病毒／性别／性格／形态／callback 与已有前缀不合成全流程成功保证。

`PB-O02` 的本方必要 schema／编译／加载／反写事实已由原亲读完整定义和上述限定贡献证明，没有再发现本方具体缺失的断言前提。已完整读 root 对 KERNEL 与 Developer 的 task-final；4732 个 kernel 意义原子仍属于真实 kernel reader，不借此更换本人 formal 分母或继承其原 2219 定位为通过。原五份补读 formal 和21个有限手写反向单元保原资格，其它 kernel 原属域条款不是新增本方无界欠项。

`PB-O03` 的完整外域批准已从本方必要缺口中分离。原 Move／Battler／AbilityItem／AI／Facility 的有限贡献、331／31 向量和相应共同前提照常保留；此次另实际完整接收 Shadow18 招式和 Type1 的每个作者值／省略意义，以及 SSI01–12／TG01–14 的有限成功、目标、保护、免疫与失败前缀。实际原文读者仍为 PBS_CURRENT；SHADOW 的 IsSpecialType=true、IconPosition 编译为 Integer19，早期 JSON token 表示与8项强制标量伴件同用。四种 Target、TotalPP0、仅 SHADOWPANIC 带 Sound、SHADOWSHED exact RemoveAllScreens 缺实现与相近类不同，均与既有 factory／目标和正式范围接合。没有把所有740回调、267能力或任意插件的整域批准补成前提。

所有必要强制伴件一并采用：Mail 正确源是006而非005；ShowQuantity 是 stored true OR nonimportant，独立于 Consumable；pinch mode false 是不要求 GLUTTONY，包含有效 GLUTTONY，并非要求其缺席。任意 Mega 石阻止 MegaMove、Encounter 成功谓词必 reset、TutorMoves 通用 uniq 三种过强旧句均明确不采用。原件不回填，当前正确条款不重复造提案。

`PB-O04` 处置为保留 root 全局资格，不再冒充当前源缺读。root 的当前 task-final／已裁决 handoff 已按精确必要范围接收；全史等价目录、全局去重、真实配置和历史执行 UNVERIFIED 等仍由原 owner 保留。没有新 proposal，因此没有新增非提出者反证票。CURRENT 的既有 +1／602 数学审计也没有在本上下文重跑或另计。

全部参考 Ruby／游戏／native／真实 `.dat`、保存重载、像素音频与业务状态模型依旧 NOT_EXECUTED。新工具操作只是读完整必要事实、字段和源方法，以及身份／JSON／现有载荷关联验证；没有把未执行变成“源材料不可得”。超长显示的截断处已按完整对象紧凑重显，未给截断部分信用。本方必要余项为零不等于整外国域、全史或全系统 PASS。

''' + report[end:]
(TASK/'review.md').write_text(report)

# Verify frozen primarybytes again only as integrity, never reading credit.
ids=rj(TASK/'identities.json')
for z in ids['primary']:
 raw=(REF/z['path']).read_bytes()
 assert sha(raw)==z['sha256']
 assert subprocess.check_output(['git','show',f"{RC}:{z['path']}"],cwd=REF)==raw
ids['same_context_continuation_qualified_receptions']=receptions
ids['continuation_identity_checks']={'utc':NOW,'all21_fixedbytes_match':True,'semantic_credit_from_hash_check':0}
put(TASK/'identities.json',ids)
validation=rj(TASK/'validation.json')
validation['same_context_necessary_continuation']={'utc':NOW,'all21_frozen_primary_match':True,'required_eight_present':True,
 'prior_four_interfaces_current_necessary_missing':0,'new_contexts':0,'new_votes':0,'reference_engine_model_runs':0,'scope':'Staticidentity/serializationchecks only'}
put(TASK/'validation.json',validation)

manifest=[]
for p in sorted(TASK.rglob('*')):
 if p.is_file() and p.name not in ['delivery-manifest.v2.json']:
  x=identity(p);x['path']=str(p.relative_to(TASK));manifest.append(x)
put(TASK/'delivery-manifest.v2.json',{'schema':'gr8-pbs-battle-delivery-manifest/v2','utc':NOW,
 'status':'READY_FOR_ROOT_TASK_FINAL_ACCEPTANCE_WITH_RETAINED_SCOPE_QUALIFICATIONS','actual_context':'/root/pbs_battle',
 'original_primary_qualification':{'ownfull11':11,'ownbyteassoc5':5,'namedraw4':4,'namedassoc1':1,'pathrecords':7704},
 'current_necessary_available_unread':0,'current_necessary_consumer_unreceived':0,'new_contexts':0,'new_votes':0,
 'new_candidates':0,'new_required':0,'new_optional':0,'behavior':'NOT_EXECUTED','update':'UPDATE_NOT_STARTED',
 'actual_model_effort_tier_fast_opaque':'UNVERIFIED','artifacts':manifest,'manifest_self_excluded':True})
print(json.dumps({'utc':NOW,'files':len(manifest),'necessary_missing':0,'primary':21,'path_records':7704,'new_contexts':0,'new_votes':0},ensure_ascii=False))
