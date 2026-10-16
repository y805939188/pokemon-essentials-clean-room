import datetime
import hashlib
import json
import pathlib
import stat
import subprocess

base=pathlib.Path(__file__).resolve().parent
rr=base.parents[2]
repo=rr.parents[2]
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
reader='/root/reference_metadata_completion'
E=rr/'evidence/external-recovered/receive_external_h_early_qualifications/4dd33cacb54cdf1a95a9a6c5ce053082d71b12e7'
H6=rr/'evidence/external-recovered/receive_external_h_r6_effective_contracts/1bbfcae714599d6d4e736c16785ac8b5e5800806'

def read(path):
    return json.loads(pathlib.Path(path).read_text())

def write(name,obj):
    (base/name).write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n')

def digest(path):
    p=pathlib.Path(path);data=p.read_bytes()
    return {'path':str(p),'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest(),
      'computed_git_blob':hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest(),
      'mode':'100755' if p.stat().st_mode&stat.S_IXUSR else '100644'}

old_manifest=base.parent/'completion-manifest.json'
old=read(old_manifest)
old_checks=[]
for row in old['files']:
    p=base.parent/row['path'];actual=digest(p)
    assert actual['bytes']==row['bytes'] and actual['sha256']==row['sha256']
    old_checks.append({'path':row['path'],'bytes':row['bytes'],'sha256':row['sha256'],'unchanged':True})
assert len(old_checks)==89
assert digest(old_manifest)['sha256']=='c5acdd1f8154e72a743ce1ae203ca0fad30f0ac619c863764cfe9208e6c10093'
write('original-89-preservation.json',{'schema':'gr8-slot-join-original89-preservation/v1',
 'utc':now,'original_manifest':digest(old_manifest),'payloads':old_checks,'changed':0,
 'scope':'Only the original89 payloads and their externally bound manifest; new child directory is excluded from that frozen list.'})

current=read(base/'read-io/001-current-contract.stdout')
assert current['id']=='GR8-ELR-001' and current['classification']=='required'
assert current['severity']=='P3'
r7=read(base/'read-io/013-r7-qualified-slot-crosswalk.stdout')
r5main=read(base/'received/r5_u01_u02.json')
r5core=read(base/'received/r5_u03_u06_core.json')
r5tail=read(base/'received/r5_tail_shared_policy.json')
ids5=['GR5-M01-002','GR5-M01-003','GR5-M01-008','GR5-M01-009','GR5-JXN-001']
keys5=['id','primary_reception','current_effective_meaning','complete_original_fact_and_cases','independent_consumer_join','criteria','source_objects_ref','open_interfaces','formal_acceptance_changed','CLOSED_changed']
selected5=[{k:r[k] for k in keys5 if k in r} for r in r5main['records'] if r['id'] in ids5]
selected_criteria=[{k:r[k] for k in ['criterion_id','primary_id','kind','definition','independent_reason','receiver_decision','whole_file_or_interface_signature','new_behavior_execution']} for r in r5main['criterion_results'] if r['primary_id'] in ids5]
r6=read(H6/'continuation/readsets/pack-D.complete.json')['primary_contracts'][9]
c=r6['original']['whole_contract']
r6keys=['id','aggregation_aliases','identity_and_verdict','premises_and_counterexample','minimum_revision_contract','acceptance_and_regression','independent_adjudication','dependencies_and_receivers','original_full_proposal','original_proposal_status_scope','non_proposer_packet_scope_correction']
curkeys=['id','status','premise','facts','normal_cancel_failure_partial_commit','ungranted_scope','execution','remaining_required_semantic_reading']
facts={'schema':'gr8-slot-history-qualified-selected-facts/v1','receiver':reader,
 'received_current_contract':current,
 'R1_qualified_purpose_and_scope_records':read(base/'read-io/004-early-r1-bounded.stdout'),
 'R2_complete_limited_obligations':read(base/'read-io/012-r2-complete-limited-obligations.stdout'),
 'R3_complete_relevant_qualified_meanings':read(base/'read-io/005-early-r3-bounded.stdout'),
 'R4_complete_relevant_qualified_meanings':read(base/'read-io/011-early-r4-complete-meaning.stdout'),
 'R5_qualified_primary_complete_meanings':selected5,
 'R5_qualified_original_criterion_meanings':selected_criteria,
 'R5_qualified_resource_neighbours':read(base/'read-io/015-r5-neighbour-resource-meanings.stdout'),
 'R5_qualified_Slot_complete_meaning_and_nine_obligations':read(base/'read-io/010-r5-slot-complete-meaning.stdout'),
 'R6_localized_image_original_operatives':{k:c[k] for k in r6keys},
 'R6_current_complete_qualified_meaning':{k:r6['current']['whole_record'][k] for k in curkeys},
 'R7_already_qualified_bounded_crosswalk':r7,
 'credit':'Actual selected meaning reception, not a repeat of whole R1–R7 review or source reading; qualified original actual readers retain their full-body credit.',
 'original_R5_reader_contexts':{'r5_u01_u02':r5main['actual_reviewer_context'],
    'r5_u03_u06_core':r5core['reader'],'r5_tail_shared_policy':r5tail['reader_context']},
 'new_contexts':0,'new_independent_votes':0,'business_execution':'NOT_EXECUTED','UPDATE_NOT_STARTED':True}
write('qualified-facts.json',facts)

comparisons=[]
def add(ident,meaning,premise,normal,counter,observation,revision,strongest,relation,status,io):
    comparisons.append({'old_id_or_scope':ident,'complete_old_business_meaning':meaning,
      'premises':premise,'old_normal_control':normal,'old_minimal_counterexample':counter,
      'observation_point':observation,'old_minimum_revision_obligation':revision,
      'strongest_alias_or_no_required_argument':strongest,'substantive_relationship_to_ELR001':relation,
      'old_status_and_qualification':status,'actual_read_io':io,
      'current_ELR_scope_ref':'qualified-facts.json#/received_current_contract',
      'canonical_decider':'root; this row does not alter classifications, IDs, counts, acceptance or closure'})

add('R6-D-LZ-002',
 'Selected-language messages select designated UI image variants. The accepted current meaning explicitly covers controls keys, graphical battle menus, trainer cards and Voltorb basenames; language game→core→original identity, empty hit and consumer-specific load/failure semantics are already correct.',
 'Valid selected-language hash, reached designated screen, graphics mode gate where applicable, A/B nonempty suitable assets and normal prior operations; no overrides.',
 'Missing controls-key translation requests original A.',
 'Only controls-key language mapping A→B changes, A remains available: creation receives B even when A exists.',
 'Identity handed to image creation/loading, before final pixels; exactly the same observation layer as ELR001.',
 'Introduce the selected-image capability and connect designated controls/representative inspected battle/UI consumers, preserve backdrop and load/failure distinctions. Current explicit ungranted scope says the48 material pairs do not certify all48 caller chains.',
 'The old generic minimum rule uses representative UI images; perhaps that was an obligation for all actual translation callers, so Slot would be a duplicate.',
 'EXISTING_PARENT_CAPABILITY_WITH_NEW_SLOT_CONSUMER_PRECISION_FACET. The language algorithm and A→B observation are the same parent root. Exact caller scope is positively limited by old source locations, designated four-family current facts and explicit ungranted scope; adding seven Slot roles is a finite consumer extension, not an identical old controls counterexample or a second generic language-image root. The existing R8 bounded required/P3 can remain as the extension obligation; final alias/canonical encoding is reserved to root.',
 'Original proposal PROPOSAL_NOT_ADJUDICATED/LOW and contract OPEN_NOT_UPDATED are preserved generation-time fields. R6 terminal acceptance/56 CLOSED belongs to the accepted9aa/b7/4df stage; current reception COMPLETE_FINITE_SCOPED_STATIC_RECEPTION does not reopen that closure.',
 ['007-r6-language-resource-obligations','014-r6-original-proposal-consumer-boundary'])

add('GR5-M11-004',
 'Slot update q=floor(v*t/H), commit(i+1+q)%22 only while spinning; stop-request/slip is checked before writing the new index. Preserve22×3 ordered symbols and payout/replay/waits; original two processes include first Rect substitute failure and only five bounded observations in the second.',
 'Two separately reset update histories and exact update times; slip2 is injected state, not a no-slipping function result.',
 'No stop and first late-update controls continue rotating with the stated historical interval premise.',
 'At a boundary with already requested stop and slip0 freeze previous committed index before a new index write; positive slip becoming0 still rotates this boundary.',
 'Index/spinning and named five observations, not chosen localized image identity or all rendering/payment columns.',
 'Nine complete criteria require the math/order/history premises and correct execution qualification. Keep reel table data, payout, replay/random/difficulty and all prior limits.',
 'Same Slot source and H derived from image height could make localization merely a detail of this old timing root.',
 'DISTINCT_BEHAVIORAL_OBLIGATION_WITH_SHARED_SLOT_REGRESSION. Choose suitable same-height A/B: all old timing/stop obligations hold while a fixed-A implementation still violates the new language selection hook. Neither theorem implies the other; preserve all22 positions and the49-line appendix without adding another timing finding.',
 'Original criterion old_result PASS_SCOPED_ACTUAL preserved; new reception is qualified finite static and NOT_EXECUTED. Existing R5 closure is not reopened; R5-REF-004 is not language/image execution.',
 ['010-r5-slot-complete-meaning'])

old5={r['id']:r for r in selected5}
details5={
 'GR5-M01-002':('Default core domain and old game collection are valid; distinguish default collection from current-language runtime data.','core missingB permits collectedB; append retains oldZ.','Replacement of collectedA/B with defaultcoreA leaves onlyB; append retains oldA→Old/Z plusB.','Collected/default set and author export, not runtime image receiver.','Specify filters, append/replace, same-map bucket and export target.','Both mention game/core; could the old collection rule cover resource identity use?','DISTINCT_PRODUCER_STAGE: default set collection/export does not name or wire Slot runtime images.'),
 'GR5-M01-003':('Valid standard text lookup, no overrides; compare before window rendering.','TwoASCII spaces normalize to one while a singleLF key stays distinct.','Query doubleLF against distinguishableT/U keys returnsT rather than global-collapseU; translated doubleLF value is preserved.','Normalized key/returned text, not the image caller invoking lookup.','Describe line-edge normalization priority, three key controls and raw-value preservation.','Slot identities are strings too, so generic lookup might settle the hook.','DISTINCT_ALGORITHM_DETAIL: normalization applies once a caller invokes lookup; it cannot identify seven previously unspecified callers.'),
 'GR5-M01-008':('Readable gated archive/loose/plugin/event source, uniqueK not filtered bycore; no preceding failure.','Eligible double-quoted marker collectsK.','Single-quotedK not recognized; a comment may be collected; looseK scanned only for one-section archive.','Author collection candidates and source selection gates, not execution/reachability.','Specify source gates/order, lexical collection and event-text flush differences, keeping002/003 separate.','The seven Slot keys may already have been collected, so another requirement is redundant.','DISTINCT_COLLECTION_VS_CONSUMPTION: collected material existence does not connect the current Slot receiver to the language layer.'),
 'GR5-M01-009':('DefaultSCRIPT_TEXTS K, successful export/read, correct overwrite-open prefix if fullcompile used.','Column-first[Q] is encoded and reconstructed.','OneASCII space+[Q] withoutcontrols is not encoded; import treats it as a newsection and rejects prior oddK; TAB changes the gate.','Author text parsing/output prefix, not image identity selection.','State conditional encoding, section-before-unescape and standalone/fullcompile truncation distinctions.','Both use language material and empty values, possibly one serialization root.','DISTINCT_SERIALIZATION_STAGE: valid already-loaded A→B in ELR avoids this author-format counterexample entirely.'),
 'GR5-JXN-001':('MutablePN template, ordinaryAlice/Bob, all changed-name lookup keys absent or explicitly covered; no reload/alias rewrite.','NoPN string or no-global-player/no-preview control leaves the source unchanged.','Read mapname asAlice, renameBob, read same material again: consumed template can remainAlice; preview/global-name precedence and explicit content-save are separate.','Selected map-name value and in-memory aliases, later explicit content persistence.','Map naming owns mutation; WP08 lookup and WP65 preview reference it. No auto-content-save or language-reload restoration claim.','Both select game/core values and have later consumer side effects.','DISTINCT_CONSUMER_AND_MUTATION: map-name PN alias state is not Slot image-role selection; no shared minimal revision obligation.')}
for ident,args in details5.items():
    prem,norm,ctr,obs,rev,strong,rel=args
    add(ident,old5[ident]['current_effective_meaning'],prem,norm,ctr,obs,rev,strong,rel,
        'Qualified original scoped/static meaning and complete associated acceptance definitions received; producer CLOSED_changed/formal_acceptance_changed=false. R5 original closed92 population and generation-time original fields are retained; no fresh whole-file or runtime approval.',
        ['008-r5-localization-core-meanings','009-r5-localization-lifecycle-meanings','016-r5-locale-acceptance-obligations'])

small5={r['id']:r for r in facts['R5_qualified_resource_neighbours']}
for ident in ['GR5-M10-006','GR5-M10-008','GR5-M10-011']:
    r=small5[ident]
    add(ident,r['current_effective_meaning'],r['retained_scope_and_nonclaims'],
        'The qualified normal reached input follows its named operation/clock/callback gate.',
        r['ordinary_counterexample_cancel_failure_and_partial_commit'],
        'Callback/page state, frame-reset request or PNG frame phase respectively; none observes selected-language Slot identity.',
        r['independent_reason_and_strongest_no_required_explanation'],
        'Shared controls screen, resource contract or AnimatedBitmap consumer could suggest alias.',
        'DISTINCT_NEIGHBOUR: the complete declared input/observation/revision is different. Existing consumer-specific rendering, timing and failure rules remain applicable after language selection, not replaced by it.',
        'OWNED_COMPLETE_STATIC_QUALIFIED; whole-file signaturefalse/new execution0; original closure and nonclaims retained.',
        ['015-r5-neighbour-resource-meanings'])

early3=facts['R3_complete_relevant_qualified_meanings']
early4=facts['R4_complete_relevant_qualified_meanings']
for row in early3+early4:
    ident=row['id'];m=row['meaning'];s=m['original_effective_scope']
    obs={'GR3-M01-001':'Author line filtering/import rejection/truncated output, separate from runtime empty hit.',
     'GR3-M01-002':'Sparse EVENT_TEXTS export discovery and already-deleted file prefix.',
     'GR4-M01-001':'Same-domain normalized-key import merge and preserved sparse entries.',
     'GR4-M01-002':'Placeholder parameter replacement before any message window.'}[ident]
    ctr={'GR3-M01-001':'An exported empty translation line is filtered, leaving odd hash content; leading# and spaced# differ.',
     'GR3-M01-002':'Emptybucket0/missing1/nonempty5 omits mergedEVENT_TEXTS while per-map can emitMap005; earlier nonemptybucket changes result.',
     'GR4-M01-001':'Same-domain repeated normalized keys choose later values while independent keys and sparse indexes survive.',
     'GR4-M01-002':'X{1}Y with backslash& keeps the placeholder; backslash1 givesXY; ordinaryQ and formatted path differ.'}[ident]
    add(ident,json.dumps({'scope':s,'criteria':m['criteria']},ensure_ascii=False),
      json.dumps(s.get('preconditions',s.get('premises',[])),ensure_ascii=False),
      'The companion valid/noncolliding/ordinary input follows the complete old criterion and preserves its earlier successful branch.',ctr,obs,
      '; '.join(x['criterion'] for x in m['criteria']),
      'A common WP08 domain, empty translation or imported runtime material might appear to be the same issue.',
      'DISTINCT_STAGE_AND_REQUIRED_CHANGE: these exact premises repair import/export/key/placeholder behavior; a valid already-loaded same-heightA→B Slot fixture satisfies all old conditions yet still needs the caller hook.',
      'Original R3/R4 acceptance scope and B5 supported_static status retained. No R7/R8 source/runtime approval transferred; R4 17/76 versus B5 16/75+1partial remain original population scopes.',
      ['005-early-r3-bounded','011-early-r4-complete-meaning'])

for row in facts['R2_complete_limited_obligations']:
    ident=row['id']
    add(ident,json.dumps({'minimum_revision':row['minimum_revision'],'root_adjudications':row['root_adjudications'],'extensions':row.get('extensions',[])},ensure_ascii=False),
      'Use the full old minimum-counterexample premises below, not the original title.',
      'Author/export cancellation, valid section or ordinary registration companion as scoped by the original root adjudication.',
      json.dumps(row['minimum_counterexample'],ensure_ascii=False),
      {'GIR-FD82-A006':'Author export target versus active game language.','GIR-FD82-A013':'Parsed section identity1tail/0/constant.','GIR-FD82-A018':'Explicit SCRIPT_TEXTS versusMap005 test premise.','GIR-FD82-A054':'Ordinary registration displayform7 versus last-seen original-form-name check producing0.'}[ident],
      json.dumps(row['minimum_revision'],ensure_ascii=False),
      'Shared current-language source or language fallback may look broad enough to include all later consumers.',
      'DISTINCT_OLD_CONTROL: active language selection, author input parsing/test premise and Pokedex form registration do not specify Slot image lookup. Valid loadedA→B premise bypasses those failures; no old control reopened.',
      'The original scope record says CONFIRMED_REQUIRED_REVISION/OPEN at its generation. Qualified R2 history separately records originalC/FINAL1 OPEN then CLOSED at closure snapshot; neither text is rewritten or used as fresh semantic approval.',
      ['012-r2-complete-limited-obligations'])

add('R1-WP08-and-WP69-qualified-original-purpose',
 'The five exact original qualification rows retain WP08 original/GR002 scoped input identities and unknown language/empty consumer outcomes; Slot trace retains ReviewPending at the original B-v1 time plus later scoped report/import/management successors. The22×3 table is an ordered-data scope, not localization wiring.',
 'Original report-generation and reviewed-versus-management-byte distinctions; no fresh body equivalence.',
 'Original LZ01–14 and SL16 families are retained as typed case routes only.',
 'No new business counterexample is manufactured from an old approval headline or current hash identity.',
 'Historical approval/input identity and declared scope, not new active language image requests.',
 'Retain exact source/report routes and named unknowns, route later behavior to current formal; no global all-image guarantee is granted by an old WP approval.',
 'Original full WP scope or broad historical PASS might be treated as already certifying every Slot image consumer.',
 'QUALIFICATION_ONLY_NOT_EXACT_ALIAS: positive historical scope and explicit unknowns cannot discharge or refute the current seven-role hook. Original22 ordered positions remain required regression material; no old body is reopened or reapproved.',
 'R1 original ReviewPending/qualified scoped successors remain temporal; H-EARLY completion/root acceptance is an audit reception, not new original business PASS.',
 ['004-early-r1-bounded'])

add('R7-current37-and-R6-retained31-qualified-crosswalk',
 r7['record']['premise_consumer_revision_obligation_comparison'],
 'Reuse already qualified full37 original current contribution comparison; no repeat37 body/source review.',
 'Original font/input/soundfont controls retain their own declared capabilities.',
 'Font fallback, MIDI-bank declaration/audio request and input-tail refresh have different producer/consumer obligations from Slot language-selected images.',
 'The exact already qualified crosswalk observation boundaries.',
 'Preserve old obligations and classifications, receive the missing earlier localized-image parent relation here.',
 'The earlier crosswalk explicitly left an earlier alias possible, so it cannot alone certify novelty.',
 'INHERITED_QUALIFIED_R7_NONIDENTITY_PLUS_EXACT_EARLIER_PARENT_JOIN. Its earlier-alias open facet is answered by R6-D-LZ-002 above; no claim of a new all-history negative from this row.',
 'Existing required/P3 and all original counts remain unchanged; global canonical encoding still belongs to root.',
 ['013-r7-qualified-slot-crosswalk'])

result={'schema':'gr8-slot-history-complete-finite-comparison/v1','utc':now,'reader':reader,
 'current_id':'GR8-ELR-001','current_classification_preserved':'required','severity_preserved':'P3',
 'finite_conclusion':'EXISTING_R6_D_LZ_002_PARENT_CAPABILITY_WITH_NEW_SLOT_CONSUMER_PRECISION_FACET',
 'exact_old_parent':'R6-D-LZ-002','exact_duplicate_old_counterexample':False,
 'same_language_algorithm_parent':True,'new_distinct_caller_obligation':True,
 'recommended_relation_encoding':{'current_id':'GR8-ELR-001','parent_historical_root':'R6-D-LZ-002',
   'kind':'NEW_CONSUMER_EXTENSION_PRECISION_FACET','do_not_create_second_generic_image_localization_root':True,
   'do_not_reopen_old_closed_scope':True,'exact_alias_of_completed_old_consumer_obligation':False},
 'root_reserved':'Final canonical ID/alias/tombstone representation and global counts belong to root; this finite join preserves the existing classification and adds0 findings/votes.',
 'comparisons':comparisons,'comparison_rows':len(comparisons),
 'strongest_opposition_final':'Old minimum rule already allows representative designated images, and the generic algorithm returnsB; therefore all actual_INTL image callers might be implicit. This is defeated by the positively bounded old caller lists/current five facts and explicit48-material noncertification, together with the current full-formal designated-caller restriction. Generic algorithm correctness is retained; only the finite additional caller hook remains.',
 'normal_and_counterexample_preserved':{'normal':'No game/coreA mapping→A at each reached Slot role.',
  'counterexample':'Valid loadedgameA→same-heightnonemptyB, coremissingA, A stillvalid→requestB, notA.',
  'reverse':'gameB beatscoreC; gameabsent/coreC→C; fixedbackground staysfixed; empty hit distinct from missing.',
  'observation':'Resource identity handed to existing wrapper, not renderedpixels, actualassetpresence or defaultlanguage execution.'},
 'regression_preserved':['Seven natural Slot roles only; no arbitrary image-localization rule.',
  'All22 ordered reel positions in the49-line appendix, timing H/slip/order/random/payout/replay/coins/statistics.',
  'EmptyIcon clears versus directemptyreel earlyfailure; ordinary/nonprefix/prefix failures and partial state stay distinct.',
  'No new language prompt/save writer, rollback guarantee, fallback-toA on nonemptyB loadfailure, or native/rendering proof.'],
 'necessary_available_meanings_unread':[],'necessary_incoming_unreceived':[],
 'global_history_absence_proof_claimed':False,'original_whole_history_credit':'Retained with qualified actual original readers and root received scopes, not reread by this context.',
 'new_findings':0,'new_classifications':0,'new_contexts':0,'new_independent_votes':0,
 'business_execution':'NOT_EXECUTED','UPDATE_NOT_STARTED':True}
write('finite-comparison.json',result)

inputs=[rr/'adjudication/root-decisions.partial.json',rr/'adjudication/root-elr001-counter-reception.v1.json',
 rr/'tasks/counter_slot_localization_existing_kernel/counterreview.json',
 rr/'tasks/counter_slot_localization_existing_kernel/reel-table-extent-clarifier.v1.json',
 rr/'adjudication/root-h-early-task-final-acceptance.v1.json',rr/'adjudication/root-h-r6-task-final-acceptance.v1.json',
 rr/'adjudication/root-localization-records-task-final-acceptance.v1.json',
 rr/'tasks/handoff_final_five_root_deltas/effective39/handoff/records-index.json',
 rr/'tasks/r7_current_new38_root_dedup_crosswalk/crosswalk.json',
 rr/'tasks/receive_external_h_early_qualifications/receivers/fanout-v1/early_r1_r4/reception-ledger.json',
 E/'interfaces.json',H6/'continuation/readsets/pack-D.complete.json',repo/'review/remediation-20261003-prepare/finding-acceptance.json']
write('input-identities.json',{'schema':'gr8-slot-history-input-identities/v1','utc':now,
 'fixed_B8':'fd1df570cad987dc3852a3b958f03916e317f7fe','fixed_R':'8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b',
 'local_lookup_containers':[digest(p) for p in inputs],
 'container_credit_boundary':'Container byte identity is navigation; only exact operative projections listed in reading-ledger and qualified-facts were actually received. Root-decisions container can change outside the selected frozenELR object; raw001 binds the actual received selected version.',
 'fixed_remote_R5_ledgers':read(base/'received/recovery.json'),
 'ELR_input_exact_projection':digest(base/'read-io/001-current-contract.stdout')})

ios=[]
for p in sorted((base/'read-io').glob('*.json')):
    d=read(p)
    for stream in ['stdout','stderr']:
        raw=p.with_suffix('.'+stream).read_bytes()
        assert len(raw)==d[stream+'_bytes'] and hashlib.sha256(raw).hexdigest()==d[stream+'_sha256']
    ios.append(d)
write('reading-ledger.json',{'schema':'gr8-slot-history-finite-reading/v1','reader':reader,
 'current_contract':'001 exact wholeELR object received; 002 all8 substantive countersections and all current metadata; producer I/O array only referenced, not reread source.',
 'complete_selected_old_meanings':'004/005/007/008/009/010/011/012/014/015/016 are exact complete operative projections as listed in qualified-facts; imported source ranges and prior-reader qualifications do not become this reader sourceFULL.',
 'already_qualified_R7':'013 exactSlot row and universe application only, no other37-body repetition.',
 'truncation':'003 initial combined nine-row display truncated; entire intended nine meanings actually reread without gaps by004(firstfive),005(nexttwo),011(lasttwo). Initial whole records-index/crosswalk output also truncated and grants no whole-body credit.',
 'navigation_errors':'Initial guessed h_early_qualifications/4dd path was absent; corrected to receive_external_h_early_qualifications/4dd. Initial threegitcat-file lookups absent, not business/read failures; exact immutable raw GitHub retrieval006 succeeded. One navigation loop hit a missing pointer key; no semantic absence conclusion from that failure.',
 'uncaptured_platform_transcripts':['cdc559 rootHearly receipt full','7c4ece rootR6 receipt full and localization receipt partial, actual root qualified scope provided by parent','3ae375 rootELR receipt and22-position clarifier full','c44eaf exactR6 producer/caller wiring boundaries and R2 scope-generation sample','00c82d original89 preservation check'],
 'captured_io':ios,'necessary_available_unread':0,'necessary_unreceived':0,
 'unused_recovered_fields':'The unselected other48/32/12 ledger bodies are not claimed newly read here; their qualified original readers and parent acceptance persist.',
 'new_contexts':0,'new_independent_votes':0,'business_execution':'NOT_EXECUTED','UPDATE_NOT_STARTED':True})

write('progress.json',{'schema':'gr8-slot-history-final-join-progress/v1','utc':now,'reader':reader,
 'same_existing_context':True,'new_contexts':0,'new_independent_votes':0,
 'write_set':'tasks/reference_metadata_completion/slot-history-final-join/',
 'status':'COMPLETE_FINITE_COMPARISON_READY_FOR_ROOT_ACTUAL_RECEPTION',
 'conclusion':result['finite_conclusion'],'existing_required_P3_preserved':True,
 'necessary_available_unread':0,'necessary_incoming_unreceived':0,'original89_changed':0,
 'new_findings':0,'root_global_canonical_decision':'RESERVED_NOT_SELF_GRANTED',
 'requested':{'model':'gpt-6.1-sol','effort':'ultra','tier':'default normal','speed':'normal','Fast':'off'},
 'actual':{k:'UNVERIFIED' for k in ['model','effort','tier','speed','Fast','platform_UUID']},
 'business_execution':'NOT_EXECUTED','UPDATE_NOT_STARTED':True})

report='''已完成 ELR001 的有限 R1–R6 历史接合；必要可得旧意义未读0、必要 incoming 未接收0。结论是既有 R6-D-LZ-002“指定 UI 图像语言选择”父能力之下的 Slot 七角色消费者扩展/精度 facet，不是再次发明 game→core→原身份算法，也不是把已关闭的旧控制帮助反例原样重报。当前 GR8-ELR-001 的既有 required/P3 分类保持；最终 canonical/alias 编码与全局计数仍由 root 决定。本接合新增 finding、分类、context、独立票均0。

最强反方已按完整旧最低修订义务处理：R6原文允许指定 UI 变体并以代表性调用者举证，容易被理解成所有实际_INTL图像已涵盖。但旧完整原合同的具体 producer/consumer、当前五条事实、最低读写集与明确 ungranted_scope 都限定实际指定消费者；“48对材料”明确不授全48调用链认证。当前完整 WP08 指定调用者限制又不把算法对任意字符串可用推广为任意图像必须调用。由此应复用旧语言算法并补 Slot 接点；不能仅因同父能力撤销这个有限覆盖义务，也不宜另计第二个通用语言图像根。

普通与最小反例同层比较：合法当前语言已加载且正常到达角色，无译交 A；仅 game 域把 A 映到有效同高度非空 B、core缺键且 A 仍有效，Slot图像包装应收到 B。game盖core、core单独命中、缺译、空译分别保留；观察点是请求身份，未认证像素或实际资产。七自然角色以现有合同为准。背景等固定资源不扩大，22个有序转轮位置/49行附表、H时间分区、滑移/停止、随机/支付/重玩/币额统计全部保持。

GR5-M11-004 已接收完整 qualified Slot 意义及全部九条 criterion：其根是时间映射、历史区间和先停后提交，另保历史两次进程中首次设施失败、第二次五限定观察及 index/spinning 自动核对边界。选择同高度 A/B 可同时满足旧时序而仍丢失语言接点，因此二者不是同一最小修订义务。既有22位置数据不是语言消费者证明，旧运行也不是本次图像/语言运行。

R2作者导出目标与游戏语言、节名/数组形态前提，R3行过滤/稀疏导出，R4同域归并/占位替换，R5集合收集/键归一/脚本提取/条件编码/地图名别名以及邻近帮助键、帧重置、PNG相位均按完整必要业务意义与 acceptance 比较。它们有具体不同输入、生产阶段、观察点和最低修订；没有由同文件、标题相似或检索无命中直接作全史无alias断言。R1原批准/ReviewPending及后继管理资格、R2 OPEN→原关闭、R5/6候选/接受/关闭的代际状态保持，不回写旧记录。

原 R7 current37 的完整比较继承已qualified crosswalk，仅补读其 ELR001 有限行；其“可能更早语言图像父根”现由 R6-D-LZ-002 精确接合。本结果不重读37/92/56或 Slot 全源码，不复活原 pending 字段为当前缺读。所有原完整阅读信用保留实际非作者 reader；本上下文只对所选完整事实意义及当前契约做有限接收。

deliverables: finite-comparison.json 为逐项前提/普通/反例/最强反方/观察点/修订义务/旧状态完整矩阵；qualified-facts.json 保所接原义；input-identities.json、reading-ledger.json、read-io/、original-89-preservation.json 和 manifest.json 提供身份及真实I/O。三 R5 ledger 从明确固定commit/path直接取回，HTTP200、完整字节/SHA/blob计算均保留；恢复和解析本身不授语义信用。原89载荷及原manifest全未改。

请求 gpt-6.1-sol / ultra / default普速 / Fast off；实际配置各字段及平台UUID无回显，UNVERIFIED。未运行源码、Ruby、语言加载、游戏、媒体、存档或模型；NOT_EXECUTED，UPDATE_NOT_STARTED。全局 canonical 签字与本贡献实际接收留 root。
'''
(base/'report.md').write_text(report)
print(json.dumps({'status':'FINITE_JOIN_ARTIFACTS_WRITTEN','comparison_rows':len(comparisons),
 'relation':result['finite_conclusion'],'old89_changed':0,'necessary_unread':0,'necessary_unreceived':0,
 'new_findings':0,'new_contexts':0,'new_independent_votes':0,'UPDATE_NOT_STARTED':True},ensure_ascii=False))
