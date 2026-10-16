"""Serialize this auditor's manually assessed bounded task qualifications; never run target code."""
from pathlib import Path
import json, hashlib, datetime
from collections import defaultdict

OWN = Path(__file__).resolve().parent
BASE = OWN.parent.parent
CAP = OWN / 'delta-inputs/exited35-0743/capture.json'
EXTRA = OWN / 'delta-inputs/exited35-0753-extra/capture.json'

# These are manual judgments after actual report/contract reading, not generated semantic atoms.
# Tuple: finite deliverable supported by received report, exact residual obligation, bounded assessment.
DETAILS = {
'inventory_denominator': (
 '432R/131F/980 scoped paths fixed; four planning texts read by provider;87WP/113Feature/395 declared edges routed. Identity/routing evidence received here.',
 'Real semantic unit/fact/clause/premise/interface denominator remains UNFROZEN. Old manifest type disposition cannot discharge1413 lines of current-purpose review. Initial dedicated platform prompt NOT_LOCATED_IN_CAPTURE; root task-wide receipt pending.',
 'MECHANICAL_SCOPE_SUPPORTED_SEMANTIC_DENOMINATOR_OPEN'),
'history_current': (
 'Current nonmandatory fields, recovered exact history inputs and six of twelve actual R7 context reports received as the provider bounded scope; old WAIT/FAIL and continuations preserved.',
 'C2 37current records/original evidence+manifest purposes;R6 nine retained/56contracts351cases110edges;R1–R5 full qualifications; complete R7 candidate/final receipts. New H-R7 delivery exists but not retroactively received by this exited provider. contract.md is global prompt copy, not proof of original dedicated dispatch.',
 'PROVIDER_EXPLICITLY_PARTIAL'),
'kernel_review': (
 '135 finite source-fact fields and primary reading claims received; three original KER proposals/counters/root finite decisions remain qualified.',
 '2219 old clause locators are not a complete atom census;771 no-fact links/generic premises and all transitive consumers require actual qualification. New kernel_atomic_reception is running; no whole successor receipt received. Current old clause-source-premise matrix remains unread here.',
 'SOURCE_READING_CLAIM_RECEIVED_ATOMIC_COMPLETION_OPEN'),
'combat_review': (
 '63 bounded CORE facts and finite original COM classifications received; F054 current meaning limited by mandatory straighten clarification, ordinary victory audio limited by later correction.',
 '994 old locators incl165 unlinked/251 definition locators do not close clauses; generic premises and all consumers remain. New CORE actual audit is running. Original clause-to-source payload not fully received here; later COM006 summary is not full reception.',
 'SOURCE_READING_CLAIM_RECEIVED_ATOMIC_COMPLETION_OPEN'),
'creature_review': (
 '102 source-fact fields/108 boundary objects and nine forwarded CORE facts actually received as exact old cut; old source reading26full15partial51unread and formal8full4partial4unread remain historical.',
 '1430 old reverse locators incl1307 unlinked,100 empty consumer fields, Storage/Dex joins and compound clauses remain. Actual CRE-A successor and C scope in same context do not themselves close A or add an independent vote. Original reverse-matrix.pending not fully received here.',
 'EXPLICIT_OLD_PARTIAL_SCOPE_SUCCESSOR_RUNNING'),
'counter_kernel_first': (
 'All three bounded counterproof results received:KER001 ordered deletion prefix;KER002 read-result emptiness with sufficient examples preserved;KER003 discarded formatter return. Root finite classifications already separately received.',
 'No task-wide final receipt. Original dedicated platform prompt NOT_LOCATED; exact assignment-wide clauses beyond named three cannot be reconstructed. Full historical nonduplication/shared-domain acceptance stays with named root/history owners, not inferred from this finite counter.',
 'FINITE_COUNTERPROOF_CONTENT_SUPPORTED_TASK_FINAL_OPEN'),
'preflight_resources': (
 'Binary/resource inventory, original751facts and reported readable659C/55shader/5prelude/3Ruby contribution qualifications received; structural parsing remains separate from semantics.',
 'Original forward-map and controller-readset bodies not fully received here. Later controller/remaining-text/Ruby/media/font deliveries require actual complete finite reception; availability/type parsing does not close readable programs or native consumers. Named opaque/native and host observations remain separately bounded.',
 'FINITE_PREFLIGHT_DELIVERED_FULL_READABLE_CONTENT_RECEPTION_OPEN'),
'counter_combat_first': (
 'COM001 and COM002 ZERO_ABLE/MIXED_ORDER complete bounded counterproofs received; distinct causal facets and source failure prefixes retained; canonical root COM001/002/003 binding separate.',
 'No task-wide receipt; original dedicated prompt NOT_LOCATED. Preserve historical NPC overlap and exact later root canonical keys, shared formal scope and strongest successful rebuttals; finite counterproof does not approve entire combat/AI/scene domain.',
 'FINITE_COUNTERPROOF_CONTENT_SUPPORTED_TASK_FINAL_OPEN'),
'coverage_acceptance_audit': (
 '03:20:52 snapshot report/gaps/qualification fields received. Historical R175/43/196 and F46/14/71 are declared range coverage only.',
 'Seven COV-denominator/kernel/CORE/CRE/resource/history/late obligations were not closed at that cut. New later readers cannot be backfilled into old audit. Original dedicated prompt NOT_LOCATED; task-wide receipt and current whole coverage qualification absent.',
 'FINITE_HISTORICAL_CUT_SUPPORTED_GLOBAL_COMPLETION_OPEN'),
'world_topology_audit': (
 'WP11 89clause groups/304 assertions/31source facts/7interfaces bounded contribution received; two WORLD counters and UI001/PBSW002 finite rebuttals retained.',
 '1245 structural locators are not atoms;533 shared-catalog rows excluded from reverse source audit, WP12/13 accepted only named crossings. Root/world later aggregate receipt is separate. Initial dedicated prompt NOT_LOCATED; full transitive history/source package final reception open.',
 'WP11_FINITE_CONTENT_SUPPORTED_OTHER_DOMAIN_APPROVAL_EXCLUDED'),
'ui_navigation_audit': (
 '37Rfull/24partial and four formal text-read claims;320manual assertions/52vectors bounded contribution metadata received. UI001 strongest No-branch scope rebuttal retained optional.',
 '1127 reverse line locators with183 bounded links are not final compound atom closure. Shared UI catalog other series, remaining partial-source ranges, history and final consumers need qualification. Original forward/reverse bodies pending here; initial dedicated prompt NOT_LOCATED.',
 'FINITE_SOURCE_CONTRIBUTION_COMPOUND_REVERSE_OPEN'),
'pbs_world_record_audit': (
 '18path/15unique raw bytes,2400records/24980field locators reported by actual provider; ten field contracts and finite GEN/source facts received. Default/backup samebytes attribution retained.',
 'Original6.5MB forward and reverse bodies not fully received here. Every Cup TrainerNos/rules/team/session join, Ribbon award/purify/save, Phone callers/localization, Berry time/bag/migration and map/Flag consumers remain explicit residuals. Initial platform prompt not located; field-contracts is evidence, not original dispatch.',
 'ALL_RECORDS_PROVIDER_CLAIM_RECEIVED_BOUNDED_JOINS_PARTIAL'),
'counter_world_first': (
 'Two complete nonproposer counterproofs received; WORLD001 requires explicit outer catch/continue, WORLD002 speed0 once-cycle and26-grid control retained. Root bounded P3 reception separate.',
 'No task-wide receiving receipt; initial dedicated prompt NOT_LOCATED. Preserve root/history dedup qualification and exact source/read scope; no full-domain or actual map/save/native execution acceptance follows.',
 'FINITE_COUNTERPROOF_CONTENT_SUPPORTED_TASK_FINAL_OPEN'),
'binary_controller_strings_review': (
 'Controller1666 records, finite native table requests,1187fragment-view contribution and exact dictionary/numeric type qualifications received as limited scope.',
 'Original14MB semantic-text-readset still unread here.57948 literal occurrences later have separate actual readers and parent reception; this does not retroactively read all controller/native/CFG content or close18166 Game type/consumer residuals. next-context-prompt is successor contract, not initial dispatch.',
 'FINITE_CONTROLLER_CONTRIBUTION_REMAINDER_HAS_DISTINCT_READERS'),
'com_facility': (
 'Provider22R/8F full-read and22natural fact-group claim received;13finite interfaces and original source/rule/session failure-prefix evidence retained.',
 '633/1156/3082 are locator/punctuation candidate counts, final semantic clause census open. SixTrainerNos/Tower/traits data now has later providers, but actual receiver-side complete joining must be evidenced.202 foreign shared rows, all attack exits/ability/item producers, conversion/migration and WP76 tails/history remain; three original payloads pending here.',
 'LOCAL_REVIEW_COMPLETE_JOINS_AND_ATOM_CENSUS_OPEN'),
'com_move': (
 'Team15R/11F full reading,331vector and actual nested2R/2F125structures/1432assertions/114stage contribution receiver claims received; own13R/9F stays distinct.',
 'Two whole formal-domain receptions COM-BATTLER/COM-ABILITY-ITEM remain; CRE-B final receipt binding remains. Original forward/reverse/Fling/vector bodies pending here, child reverse7.5MB pending separately. No inferred global history or all data approval.',
 'FIXED_PRIMARY_PROVIDER_COMPLETE_FINAL_CROSSDOMAIN_RECEPTION_OPEN'),
'com_ai': (
 'Provider20R/9F full,65groups196facts,72body groups273assertions and285vectors reported;14finite interfaces and AI001/002 bounded root decisions received.',
 'IF-COMAI-DEFAULT-PBS-RELOAD is open across default/backup moves/abilities/types/species/forms/trainers→schema/parser/register/compile/export/load/cache/reload→AI query.62path union is not62unread files. Original forward/reverse full bodies pending here.',
 'FIXED_PRIMARY_PROVIDER_COMPLETE_ONE_NAMED_DATA_JOIN_OPEN'),
'creature_b': (
 'Provider6R/4F primary,46own+one exact samebyte path association in47initial payloads;3154item path records and15/20finite interfaces bounded contribution received.',
 'Five finite open surfaces:field transfer,EOR complete composite vectors,other shared-catalog primary scopes,other item consumers,history/binary/host. Wrong Mail source path and PC-Mail ordering must use later exact receiver source evidence, not old summary. No whole-domain final receipt.',
 'FIXED_PRIMARY_PROVIDER_COMPLETE_FIVE_FINITE_SURFACES_OPEN'),
'com_ability_item': (
 'FourF/two whole catalogs read by provider;80families463pairs source contribution accepted by provider from MOVE;116finite vectors plus bounded116vector package fields actually received here.',
 'IF-AI-ABILITY-PBS-AND-RELOAD and IF-AI-HISTORY-STATUS remain. Source facts/forward/reverse original full2MB bodies pending here. Default+Gen5–8 abilities1122path record claim at old cut does not become current full reader by naming later data tasks.',
 'PRIMARY_LOCAL_COMPLETED_TWO_RECEPTIONS_OPEN'),
'pbs_creature_facility': (
 'Seven primaryR, Tower882 templates/sixTrainerNos1600trainer rows provider claim;96Factory domain certificate current fields and911literal identities actually read here; nested trait contribution separate.',
 'Original forward/reverse full bodies pending here; my96 scalar witness consistency is not an independent full graph/maximality/source proof. Complete parser/default normalization(STICK→nil,VICEGRIP filtered),rule×species/form/item/ability/creation/teams/session/restore and whole combat/media consumers need actual final receiver proof.',
 'FINITE_RECORD_DOMAIN_PROVIDER_COMPLETE_WHOLE_CONSUMERS_OPEN'),
'h_r7_final_receptions': (
 'Provider claims243 exact payloads all effective current semantics,32report versions/42IDs/12actual contexts/27unique responsibility and27dependency/shared7 fields; received bounded report and32version metadata here.',
 'Original7.6MB reading-ledger remains PARTIAL here despite exact lossless view generation. All243 payload-body semantics, MI/FI scope/current closure and original WAIT/FAIL/continuations must be actually qualified at final receiver. No root task-wide acceptance and no new independent vote from U06/U10/U12 continuations.',
 'PROVIDER_DELIVERED_ROOT_FINAL_PAYLOAD_RECEPTION_OPEN'),
'pbs_battle': (
 'Provider21primaryR7704path records58056fields;15additionalR+5F full and two whole methods;20forward fact fields/current literal contracts received here.',
 '62union paths include28full-path semantics not received by provider; default/backup source population and producer/compiler/load/cache/reload consumers still need complete joining. Original alternative-semantics/catalog/reverse bodies pending here. Identity/literal existence does not prove eligibility/active profile.',
 'PRIMARY_RECORD_PROVIDER_COMPLETE_FULL_DOMAIN_JOIN_OPEN'),
'world_interpreter': (
 'Provider7R/3F,136units469facts/330reverse1007assertions/169vectors reported; actual parent finite reception claims read; MR17 and later4units30facts separately retained.',
 'Original reverse body946734B and parent-forward/reverse snapshots pending here. Outside actual finite method/window input/PBS/media/native/history scope stays named OPEN; parent receipt cannot turn my metadata reading into full source or all atomic reception. No task-wide signed receipt.',
 'PRIMARY_PROVIDER_COMPLETE_PARENT_FINITE_RECEPTION_REPORTED'),
'binary_ruby_zlib_remaining': (
 'Provider20907occurrences13574literal texts and16YARB654objects171ISEQ1002instructions; actual parent independent finite receipt reported. Auditor independently redecoded and read exact16program projection and builtin binding.',
 'Auditor has not read20907 original literals.115native leaf/compiler CFG, independent zlib native bodies, actual loader/VM/host execution remain separate. Parent bounded16program receipt does not discharge all native or whole original57948 denominator. No task-wide final receipt.',
 'LITERAL_PROVIDER_COMPLETE_16PROGRAMS_FINITE_INDEPENDENT_RECEPTION'),
'world_resources_rendering': (
 'Provider28R/4F and full742line catalog;69units1282facts(including176weather),693body atoms+288data,205vectors822assertions+41supplement reported and parent finite received. All176weather current fields read here and Weather165line source independently read.',
 'Original body/forward/reverse snapshots remain unread here; old snapshots are earlier than final frozen3. Native/resource and font/SF2/messages receptor residuals not retroactively closed by later media report without actual receiving delta. Provider34partial+4unread extras keep their exact cut ranges; requested410 corrected actual406.',
 'PRIMARY_PROVIDER_COMPLETE_FINITE_PARENT_RECEPTION_WITH_RESIDUALS'),
'ui_minigames': (
 'Provider7R/6F+4foreignF full,65units407facts/26dependency units/70groups684atoms/179data rows/164vectors reported; UI parent finite actual reception claim read.',
 '13historical approval claims and six finite interfaces remain in frozen provider cut:fullspecies/PBS,wholeWP72,history,media/binary/font,Demo/external rewards,parent reception. Later UI confirms parent receipt but other finite surfaces need exact current packet qualification. Auditor full forward/reverse bodies not received.',
 'PRIMARY_PROVIDER_COMPLETE_HISTORY_AND_FOREIGN_INTERFACES_OPEN'),
'binary_remaining_texts': (
 'Provider57948occurrences41849different texts content-received or exactly typed; Game37041 own/Ruby20907actual child received.194SHDR+218Aon9/257controller/4401names and five complete discovery proposals reported.',
 '18166Game full type/native consumer candidates still explicit OPEN. Original five readsets inclINVALID historical version require exact purpose/content audit here; all five discovery counterreviews/media final packet still not fully received here. Literal0unread does not prove native/full formal PASS.',
 'FINITE_LITERAL_PROVIDER_COMPLETE_NATIVE_CONSUMER_SEMANTICS_OPEN'),
'world_catalog_remaining': (
 'Provider main742lines full/416assigned lines322vectors1551assertions17contexts;92+3source units/31topology/GEN10/weather176 and ninefinite interfaces reported. Parent frozen+final finite reception reported.',
 'Auditor has not received full2.54MBreverse/545808Bsource/36491Bsupplement. Provider15full13partial49unread sourcepool accurately preserved;62available files with some unread extent not hostlimit. Surf1–94 request only1–91 actual; no nonexistent lines credit. No all56R13F/self whole catalog approval.',
 'ASSIGNED_CATALOG_PROVIDER_COMPLETE_ACTUAL_ROOT_RECEPTION_OPEN'),
'world_full': (
 'Provider personal24Rfull1partial31unread/F13full; team56R13F named readers and complete finite mappings received by WORLD; catalog558rows/742lines claimed fully received, source103units447facts reported.',
 'Five named whole-domain interfaces/history/dedup/native/media/migration/foreignformal residuals remain. Auditor original four reverse bodies and interpreter snapshots not received; later final source/receiver corrections require exact separate reception. Fishing WP60 reverse86records105assertions is not Berry; no105Berry credit.',
 'TEAM_PRIMARY_RECEPTION_REPORTED_WHOLE_WORLD_QUALIFICATION_OPEN'),
'ui_wp66': (
 'Provider10R9385lines/3F790lines full;113units446facts/60groups342atoms/232vectors508expectations; current report plus parent UI actual finite reception claim read.',
 'Frozen four interfaces/three explicit atoms:facility composition,form/item composition,Area producer/history/shared. UI later claims limited source closure of three; auditor has not read full final WP66 source/reverse/cat packets and exact closing units, so remains OPEN here. Four-step U06-M11-002-B is oneUP thenUSE/ACTION/USE, not fourUP.',
 'PRIMARY_PROVIDER_COMPLETE_PARENT_FINITE_RECEPTION_CLAIM_REQUIRES_AUDIT'),
'ui_full': (
 'Provider44R/12F own+7R/6F actual minigame reception;WP66 overlap adds0primary;146units1933facts+178overlapping finite supplement facts/2762ownreverse/746catalog2082selectedatoms reported. Original99unit and638reverse current fields fully read here, exact range/Screen correction qualifications retained.',
 'Original platform stdout/opIDs/chunkUTC and independent EOF/truncation UNVERIFIED;28partialdependency paths42747available lines,13minigamehistory,fullPBS population,wholeWP72,outsideformal/reward/NPC/plugin/native/query bridge remain. Current full1933/2762/catalog and final atomic denominator packets not received here. ItemSprites requested164 actualEOF157, no158–164credit; old Scene-no-pbUpdate corrected actualScreen receiver.',
 'TEAM_FINITE_PRIMARY_REPORTED_COMPLETE_EXTERNAL_HISTORY_IO_OPEN'),
'media_font_programs': (
 'Provider13tables2587glyphs2349complete programs71FDEF/52297instructions and allGDEF/GPOS/GSUB/kern full semantics reported; actual parent finite whole contribution receipt claimed. Exact13table task contract fully read here.',
 'Auditor only current review/progress/task contract received; full program/function/structure/push/control/layout payloads and parent exact counterreceipt not received here. Native active class/service/callback/glyphloader/VM source remains named OPEN, L08 actual font/width/hinting/raster NOT_EXECUTED. These do not erase readable program review requirement.',
 'PROGRAM_PROVIDER_COMPLETE_PARENT_RECEPTION_REPORTED_AUDITOR_BODY_OPEN'),
'resource_media_serialized_cloud': (
 'Provider all13R+16Gameunits complete readable content/types;messages10697pairs21216strings178links/Main49/SF2/8fonts/BMP/DXBC/controller/dictionary/HRTF and five eight-section nonproposer counters reported. Actual font child13table content receipt claimed.',
 'Auditor has not received complete media/font/messages/SF2/type-use/counterreview/source consumer packets. Source OPEN:fontactiveclass+SFNTservice callbacks+glyphVM;HRTF15143Bouterfunction;shaderselector/checksum/Aon9header;controllerlowerI/O/device→game;dictionarycallers;SF2backend. Distinct host Font/GPU/audio/hearing results NOT_EXECUTED. Report-only receipt not whole13R semantic approval.',
 'FINITE_CONTENT_PROVIDER_COMPLETE_ROOT_AND_AUDITOR_PACKAGE_RECEPTION_OPEN'),
'attributes_calling': (
 'Nested actual context2R/2F125structures/1432subassertions/52exclusive vectors and114stage definitions,441blacklist/38heldtype/67NaturalGift mappings provider complete; parent finite exact reception reported.',
 'COM-CORE/COM-BATTLER/COM-ABILITY-ITEM final formal-domain receptions remain. Auditor original344678Bforward/7.53MBreverse/493602Bstage bodies pending; PBS selected fields do not grant all4781raw records/fullpopulation. Original nested platform prompt not located; report/parent bounded contract basis retained.',
 'NESTED_FINITE_PRIMARY_PROVIDER_COMPLETE_THREE_DOMAIN_RECEPTIONS_OPEN'),
'trait_eligibility': (
 'Nested trait/source/finite qualification and independent matching/normalization proof provider report received; actual assignment full prompt+five subsequent parent directives actually read here as exact root-field projection.',
 'Full assignment frozen_inputs/actual_precise_readset arrays not read here; original graph/traits source semantics not inferred from96scalar checks. Preserve cold cache vs arbitrarycanEvolve/babycache predicates,defaultcreation forms,STICK→nil/VICEGRIPdrop and nil privateendpoint equivalence. Parent exact independent whole graph/source receipt and task-wide receipt must be verified, not asserted from matching success.',
 'NESTED_FINITE_TRAIT_PROVIDER_COMPLETE_FULL_GRAPH_SOURCE_RECEPTION_QUALIFIED')
}

def dump(path, value):
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')

def main():
    now = datetime.datetime.now(datetime.timezone.utc).isoformat()
    cap=json.loads(CAP.read_text());extra=json.loads(EXTRA.read_text())
    entries=cap['entries']+extra['entries']
    registry=json.loads((OWN/'delta-inputs/exited35-0743/028-task-registry.current.json').read_text())
    ledger=json.loads((OWN/'reading-ledger.json').read_text())
    sha_groups=defaultdict(list)
    for e in ledger['snapshot_payloads']: sha_groups[e['sha256']].append(e)
    pending=[v[0] for v in sha_groups.values() if not any(e['read_state'].startswith(('FULL_','SAME_BYTES_LINK')) for e in v)]
    assert len(DETAILS)==len(registry['exited'])==35
    rows=[]
    for n,item in enumerate(registry['exited'],1):
        context=item['logical_context'];key=context.split('/')[-1]
        supported,residual,assessment=DETAILS[key]
        prefix=item['outputs'].rstrip('/')+'/'
        refs=[e for e in entries if e['original_path'].startswith(prefix)]
        bodypending=[e for e in pending if e['original_path'].startswith(prefix)]
        rows.append({
          'ordinal':n,'actual_context':context,'process_at_registry_cut':'EXITED',
          'process_evidence':'registry frozen07:41:23.098839+00:00; platform current list only exposed seven active contexts, not independent cumulative exit replay',
          'delivery_exists':True,'delivery_existence_evidence_only':refs,
          'main_progress_and_report_actual_receipt':'FULL_CURRENT_FIELDS_RECEIVED_OR_EXACT_SAMEBYTES_TO_THIS_AUDITOR_PRIOR_FULL_RECEPTION; reports are provider claims, not all underlying bodies',
          'all_effective_delivery_payloads_full_received_by_this_auditor':False,
          'own_source_or_formal_full_read_credit_from_delivery':0,
          'finite_supported_contribution':supported,
          'finite_assignment_completion_assessment':assessment,
          'remaining_assignment_clauses_and_receiver_checks':residual,
          'original289_frozen_unique_payloads_still_not_fully_received_here':[{k:e[k] for k in ['original_path','snapshot','bytes','sha256','git_blob','read_state']} for e in bodypending],
          'pending_payload_qualification':'Exact original289 subset only; current late effective deliveries may add additional unread bodies. Parent/nested prefix overlap is explicit; do not sum these per-task values into a new unique denominator.',
          'source_semantic_acceptance':'ONLY_NAMED_FINITE_RECEPTION_PROOFS_IN_EXISTING_ACCEPTANCE_REGISTER; source全文 does not imply every clause/consumer accepted',
          'task_contract_final_acceptance':'OPEN_NOT_SIGNED',
          'task_final_accepted':False,
          'scope_limits':'Do not transfer whole-global completion clauses to a limited counterproof; only its concrete frozen assignment can be completed. Missing original dedicated prompt is a named provenance gap, not hostlimit.',
          'global_contract_references':{'reading_and_bidirectional':'inputs/eighth-global-review-prompt.md:80–113','process_vs_semantics':'151','independent_receipt':'145–157','completed_review_gate':'239'},
          'business_execution':'NOT_EXECUTED','update':'UPDATE_NOT_STARTED'
        })
    result={'schema':'gr8-exited35-contract-qualification/v1','auditor':'/root/coverage_acceptance_incremental',
       'written_utc':now,'registry_cut_utc':registry['as_of_utc'],'capture':str(CAP.relative_to(OWN)),
       'extra_capture':str(EXTRA.relative_to(OWN)), 'original289_current_qualification':{'qualified_current_field_or_strict_typed_purpose':len(sha_groups)-len(pending),'pending_unique_sha':len(pending),'pending_unique_bytes':sum(e['bytes'] for e in pending)},
       'contexts_parent_registry_reported':{'total':42,'active':7,'exited':35,'task_final_accepted':0,'logical_primary_no_local_start':9,'original_parent_routes_without_external_receipt':17,'local_alternate_groups':8},
       'late_not_backfilled':[{'event':'parent new authorization for independent report branches; old auto-review denial preserved','status':'AUTHORIZATION_PARENT_REPORTED; zero new external start receipts received at writing'}, {'event':'COM00687003B SHA5a5a48d773e45c7f624ccad3f547655aa5baaab6e0f73da20cb2c245c5751e68','status':'AVAILABLE_NOT_FULLY_RECEIVED; parent26/22required+4optional classification not independently accepted here'}, {'event':'KERNELHash missing-key default15183B candidate','status':'PENDING_COUNTERPROOF_NOT_FINDING'}],
       'publication16':'Parent reported30cfed0996003b6ebf4b5c51cc04f31ca9255440/RRtree4c64a3df8908b9ee43eaf69e31d3d0409fe335c7/files7663 bytes691064703/114gzip original1196142655; exact receipt not fully read here, no new independent transport or semantic credit',
       'qualification':'35 exact exited contexts,33top-level+2nested; per-task no global pass. Scope qualification is based on actually read main reports/contracts and prior finite receptions; not a claim that all current effective payloads or all source/clauses have been received.',
       'original_prompt_gap_root_confirmation':'Parent confirmed initial dedicated platform prompts were not exported locally; history contract.md is global copy; controller next-context prompt is successor; PBS field contracts are evidence. NOT_LOCATED_IN_CAPTURE, no reconstruction.',
       'rows':rows,'task_final_accepted_count':0,'global_pass':False,'audit_contract_complete':False,'behavior':'NOT_EXECUTED','update':'UPDATE_NOT_STARTED'}
    dump(OWN/'exited35-contract-qualification.v1.json',result)
    lines=['# 35 个已退出任务的接收与合同资格切点','',f'实际审者 `/root/coverage_acceptance_incremental`；写入UTC `{now}`；registry切点 `{registry["as_of_utc"]}`。35是实际退出交付，不是35任务验收。TASK_FINAL_ACCEPTED=0。','',
    '102份初捕获与9份追加身份快照保留完整字节；main progress/report当前字段实际全读或关联本人此前同字节完整接收。两份UI子prompt只新读专属1–22行，嵌入global精确字节另关联此前全文；附录尚未收。trait assignment只完整接收专属原prompt/后续5指令等root字段，两组大读集未收。报告作者称全文不转成本审者源码全文；全部有效交付正文尚未全收。','',
    '| # | 实际context | 有限交付资格 | 剩余合同与接收 |','|---:|---|---|---|']
    for r in rows: lines.append(f'|{r["ordinal"]}|`{r["actual_context"]}`|{r["finite_assignment_completion_assessment"]}|{r["remaining_assignment_clauses_and_receiver_checks"]}|')
    lines += ['', '初始专属平台prompt未导出项保持NOT_LOCATED_IN_CAPTURE；不能用角色名、后继合同或全局合同复制冒原派发。有限反证不承担整个领域全文的虚构新义务，但没有实际task-wide收据时不标最终验收。', '',
    '本表不覆盖后来活跃输出；COM006、KERNELHash候选和新外部授权另列待接收，不倒填原切点。原始289仍243已限定用途接收/46未完整接收；106749148B未收不是宿主限制。所有业务NOT_EXECUTED，UPDATE_NOT_STARTED。']
    (OWN/'exited35-contract-qualification.v1.md').write_text('\n'.join(lines)+'\n')
    print(json.dumps({'rows':len(rows),'task_final_accepted':0,'pending_original_unique_sha':len(pending),'report':'exited35-contract-qualification.v1.json','utc':now},ensure_ascii=False))

if __name__=='__main__': main()
