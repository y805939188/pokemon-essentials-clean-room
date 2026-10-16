"""Write reviewer-authored, explicitly incomplete mappings; grant no acceptance."""
import json
import pathlib
import datetime

ROOT=pathlib.Path(__file__).resolve().parents[1]
UTC=datetime.datetime.now(datetime.timezone.utc).isoformat()

def write(name,obj):
    (ROOT/name).write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n')

def at(identity,first,last):
    return dict(identity_id=identity,lines=[first,last])

facts=[
 dict(id='F01',fact='Ordinary PBS discovery enumerates top-level matching text files and assigns by registered base name; the nested Gen5–8 backup directories are not thereby activated.',
      premises='Unmodified fixed R discovery entry and ordinary filesystem enumeration; explicit caller-supplied backup paths are a separate case.',
      source=[at('D07',967,1037)],primary_context=['P01–P16'],consumers=['D06','D08'],spec=[at('D05',215,245),at('D13',59,65)],
      gap='Not a successful backup promotion/compile or generation compatibility test; all backup base records still incomplete.'),
 dict(id='F02',fact='Species form fields have their own schema. Omitted scalar/collection fields inherit via the form compiler; ordinary lists are cloned, nested moves/evolutions clone their member arrays. Any explicit wild-item pool suppresses inheritance of all three pools.',
      premises='Existing valid base record, current active parser and successful field validation; per-record resolved values require that exact generation base.',
      source=[at('D01',52,111),at('D06',388,541)],primary_context=['P03','P07','P11','P15'],consumers=['D01','D16','D18'],spec=[at('D10',60,102),at('D13',130,147)],
      gap='Gen5 base suffix and all Gen6–8 base records unread; abilities/moves/items references and runtime getters not closed.'),
 dict(id='F03',fact='Species lookup tries species_form and falls back to the registered base. A missing explicit backup form cannot alone establish a missing runtime form capability.',
      premises='Valid registered species, form argument and fixed lookup; dynamic handler/caller behavior still requires separate evidence.',
      source=[at('D01',154,162)],primary_context=['P03','P07','P11','P15'],consumers=['D09','D17','D18'],spec=[at('D10',49,58),at('D14',177,206)],
      gap='Pokemon getters, dynamic handlers, generation gates and battle callers unread.'),
 dict(id='F04',fact='All four metrics files contain 674 explicit sections with four properties; missing valid species/form metrics are lazily registered from base/defaults. Form sprite arrays are cloned. Later-generation absent rows are not proof of graphical failure.',
      premises='Species registered; fixed metrics class; explicit source metrics only in attested full ranges.',
      source=[at('D02',14,68)],primary_context=['P04','P08','P12','P16'],consumers=['D01','D09','D17','D19'],spec=[at('D13',130,147),at('D14',177,206)],
      gap='Main reception pending; complete battle/hatching/trading/resource/persistence consumer chains unread.'),
 dict(id='F05',fact='Metrics sprite offsets multiply by two with player/foe index parity; front altitude applies on foe sprite; shadow offset handling is separate. Pokedex back display applies back vertical times two.',
      premises='Valid sprite and metrics object in the fixed consumers; graphics/host dependencies satisfied only conditionally.',
      source=[at('D02',71,87),at('D17',144,158)],primary_context=['P04','P08','P12','P16'],consumers=['D19','D17'],spec=[at('D14',177,206)],
      gap='No observed pixels; full battle scene consumers and actual media unread.'),
 dict(id='F06',fact='Encounter compiler validates registered type/species and positive weights/levels, fills omitted maximum from minimum, merges equal species/level intervals and sorts by descending weight then species. Section versions default to zero; duplicate sections fail after the preceding section is registered.',
      premises='Explicit compile paths and required registries present; no guarantee all backup references resolve.',
      source=[at('D06',658,763),at('D04',1,178),at('D07',232,249)],primary_context=['P01','P05','P09','P13'],consumers=['D03','D16','D17'],spec=[at('D12',49,82),at('D13',148,162)],
      gap='All source slots read, but species/item/move registry combination and actual compiling NOT_EXECUTED.'),
 dict(id='F07',fact='Direct encounter get prefers the specified version and then version0. Version iterator on normal Symbol-key registry still yields version0 when a nonzero version exists; map5v0/v1 records provide a finite contrast.',
      premises='Normal fixed compiler-produced Symbol keys, current version1 and existing map5v0/v1.',
      source=[at('D03',20,59),at('D06',658,763),at('P01',20,50),at('P05',20,50),at('P09',20,50),at('P13',20,50)],primary_context=['P01','P05','P09','P13'],consumers=['D16','D17'],spec=[at('D12',49,54),at('D11',120,125)],
      gap='Already documented; no new omission proposed. Main independent disproof/reception and runtime observations pending.'),
 dict(id='F08',fact='Current-map encounter setup copies step chances and deep-copies slot tables. Candidate selection reads that snapshot; direct specified-map selection reads registered data. Registration/file changes alone do not refresh the current-map snapshot.',
      premises='Existing PokemonEncounters instance set up successfully; subsequent version setter/map entry not included in this completed source readset.',
      source=[at('D16',1,46),at('D16',271,376)],primary_context=['P01','P05','P09','P13'],consumers=['D16'],spec=[at('D12',69,82)],
      gap='Version setter, entering-map caller and editor command definitions unread.'),
 dict(id='F09',fact='Wild held-item selection treats identical three pools as the first selection branch; otherwise cumulative common/uncommon/rare thresholds depend on lead abilities. Generation then applies shiny/Pokerus/gender/nature/form/event modifications.',
      premises='Successful Pokemon.new and valid live lead/player/bag/settings; this states the read generator body, not all data combinations.',
      source=[at('D16',383,447)],primary_context=['P02:S0037','P02:S0038','P03','P07','P11','P15'],consumers=['D16'],spec=[at('D12',178,206)],
      gap='Pokemon initialization/getters, item definitions and received creature_b evidence absent; generation NOT_EXECUTED.'),
 dict(id='F10',fact='Metrics writer chooses output suffixes from nonzero-form entries, emits base records only in chosen paths, and suppresses form entries equal to their base. Editor save writes binary metrics before PBS text; close without saving reloads binary metrics.',
      premises='Live registry and filesystem write/load success; failure may leave a prefix of operations complete.',
      source=[at('D15',291,352),at('D19',14,41),at('D19',92,106)],primary_context=['P04','P08','P12','P16'],consumers=['D08','D19'],spec=[at('D13',210,258)],
      gap='Already documented conditions; serializer host behavior, debug command caller, recovery and file failures NOT_EXECUTED.'),
 dict(id='F11',fact='Ordinary Pokedex registration resolves the display-form receiver and checks its form name. Recent-seen registration uses current-record form name while storing its display alias. The forms list excludes aliases and unnamed alternate records.',
      premises='Valid registered source/receiver species records and Pokedex instance; Pokemon species_data getter still not source-verified.',
      source=[at('D18',197,236),at('D17',160,214),at('D01',175,240)],primary_context=['P11','P15'],consumers=['D17','D18'],spec=[at('D11',84,108),at('D11',169,183)],
      gap='Per-record base inheritance unclosed; Alcremie source data does not alone prove successful host display or save/reload.'),
 dict(id='F12',fact='Gen5 base prefix includes forty complete species records through WIGGLYTUFF and only ZUBAT header/name. It includes all explicit prefix fields, move lists, text, item/evolution declarations; it gives no evidence for the unread remainder or other generations.',
      premises='Exact P02 bytes and read ranges only.',source=[at('P02',1,1060)],primary_context=['P02'],consumers=['D01','D06'],spec=[at('D10',60,102)],
      gap='Full per-record/per-field semantic forward mapping not completed; three entire base files unread.')]
for f in facts:
    f.update(evidence_level='SOURCE_STATIC',acceptance='PENDING_MAIN_REVIEWER',runtime='NOT_EXECUTED')

ledger=json.loads((ROOT/'reading-ledger.json').read_text())
dispositions=[]
for file in ledger['primary']:
    for s in file['all_sections']:
        dispositions.append([s['id'],s['status'],'COMPLETE_FACT_CONSUMER_SPEC_MAPPING_PENDING'])
write('forward-mapping.json',dict(schema='r8-task-forward-mapping/v1',utc=UTC,
 status='INCOMPLETE',identity_dictionary='identities.json#/payloads',
 section_coordinate_dictionary='reading-ledger.json#/primary',
 unit_disposition_columns=['section_id','reading_status','mapping_status'],units=dispositions,
 fact_notes=facts,section_denominator=6712,accepted_sections=0,
 semantically_complete_per_field_mapping_count=0,
 scope='Twelve finite static fact notes, not twelve accepted units and not an exhaustive mapping of read records. Every section retains an explicit open mapping disposition.'))

assertions=[
 ('RV01','D05',[215,226],'Backup presence alone does not activate it via ordinary discovery.','F01'),
 ('RV02','D05',[227,245],'Configuration/generation switch is distinct from a verified compatible backup dataset.','F01'),
 ('RV03','D13',[59,65],'Top-level discovery and class base-name dispatch.','F01'),
 ('RV04','D13',[66,119],'Current section reader/CSV validation path; not all composite numeric subclaims fully decomposed.','F06'),
 ('RV05','D13',[130,147],'Species then forms/metrics and required registered references; per-field inheritance conditional.','F02'),
 ('RV06','D13',[148,162],'Encounter specialized parsing/merging and partial in-memory state.','F06'),
 ('RV07','D13',[210,237],'Generic and specialized registry-derived PBS export, metrics path-selection condition.','F10'),
 ('RV08','D13',[238,258],'Metrics default/clone and write/recompile state vectors need each precondition separated.','F04'),
 ('RV09','D10',[49,58],'Species/form lookup and base fallback.','F03'),
 ('RV10','D10',[60,102],'Species field/default responsibilities; individual table entries require full base data.','F02'),
 ('RV11','D12',[49,54],'Direct get differs from version iterator; explicit map5v0/v1 contrast.','F07'),
 ('RV12','D12',[56,67],'Encounter slot validity/default maximum/duplicate merging and sort.','F06'),
 ('RV13','D12',[69,82],'Current-map snapshot differs from registry/files.','F08'),
 ('RV14','D12',[84,123],'Encounter types and categories/default probabilities.','F06'),
 ('RV15','D12',[178,206],'Wild generation modifiers and equal held-item pools.','F09'),
 ('RV16','D11',[84,108],'Ordinary display-form registration versus recent-seen source name.','F11'),
 ('RV17','D11',[120,125],'Area uses version iterator with hidden/region/visible-point gates.','F07'),
 ('RV18','D11',[127,167],'Area shape union/visibility algorithm, conditional map data and host.','F07'),
 ('RV19','D11',[169,183],'Available form entries require name, alias and seen/configuration gates.','F11'),
 ('RV20','D14',[177,206],'Sprite/data/display form and metrics/default lookup boundaries; dynamic handlers incomplete.','F03')]
rows=[]
for key,ident,span,claim,fid in assertions:
    fact=next(f for f in facts if f['id']==fid)
    rows.append(dict(id=key,spec=at(ident,*span),subassertion=claim,source_fact_id=fid,
                     source=fact['source'],premises=fact['premises'],
                     local_status='FINITE_STATIC_REVIEW_NOTE; COMPOUND_RANGE_NOT_FULLY_DECOMPOSED',
                     unresolved=fact['gap'],acceptance='PENDING_MAIN_REVIEWER'))
write('reverse-mapping.json',dict(schema='r8-task-reverse-mapping/v1',utc=UTC,status='INCOMPLETE',
 identity_dictionary='identities.json#/payloads',selected_assertion_notes=rows,selected_notes_count=len(rows),
 accepted=0,complete_formal_clause_subassertion_denominator='NOT_ESTABLISHED',
 formal_text_full_read_files=6,formal_physical_line_inventory='reading-ledger.json#/formal_read_decomposition_status',
 remaining='Nonzero undecomposed/unmapped clauses, tables, tests and cross-domain source assertions. Twenty notes cannot be used as the denominator for all clauses.'))

chains=[
 ('IF01','backup input→discovery→compile→binary→load→runtime',['P01–P16','D07','D06','D08'],['F01','F02','F06'],'Backup promotion/compatibility and full base/reference tables, runtime loading context.'),
 ('IF02','base/form→Pokemon getter→dynamic handler→battle data/display',['P02','P03','P06','P07','P10','P11','P14','P15','D01','D06'],['F02','F03'],'Unfinished base files, Pokemon/getForm/MultipleForms and battle callers.'),
 ('IF03','metrics→sprite/cry/resource request→battle/hatching/trading→host',['P04','P08','P12','P16','D02','D09','D17','D19'],['F04','F05'],'Battle/hatching/trading/PokemonSprites and actual resource/media/host.'),
 ('IF04','metrics edit/cancel/save→binary/text→reload→display',['D02','D08','D15','D19'],['F10'],'Debug caller, serialization/load host, write failure prefix and subsequent consumers.'),
 ('IF05','encounter records→registry→snapshot→choice→Pokemon generation→battle',['P01','P05','P09','P13','D03','D04','D06','D16'],['F06','F07','F08','F09'],'Version setter/map entry, Pokemon object, hooks, battle and persistence chain.'),
 ('IF06','encounter version iterator→area points→UI',['P01','P05','P09','P13','D03','D17'],['F07'],'Exact map metadata/TownMap/visibility state, actual pixels; formal already documents finite defect.'),
 ('IF07','form alias→Pokedex seen state→form/entry UI→save/reload',['P03','P07','P11','P15','D01','D18','D17'],['F11'],'Unfinished bases/Pokemon getter/registration caller and persistence conversion.'),
 ('IF08','growth/learning/evolution/breeding fields→runtime inheritance/size→outcome',['P02','P03','P06','P07','P10','P11','P14','P15','D01','D06'],['F02','F12'],'Full data, GrowthRate/EV/stat/evolution/breeding handlers and formal/test catalogs unread.'),
 ('IF09','wild item pools→generator→item assignment/use→persistent object',['D01','D06','D16'],['F02','F09'],'creature_b items contribution not received; item definitions/getter/bag and save chain incomplete.')]
write('interfaces.json',dict(schema='r8-task-interfaces/v1',utc=UTC,
 interfaces=[dict(id=k,chain=c,read_nodes=n,fact_ids=f,open_dependencies=g,receiver='Main reviewer; cross-domain owners not independently received',
                  status='OPEN_NOT_ACCEPTED',blocking='This chain only; not a material-limit exemption.') for k,c,n,f,g in chains],
 full_interface_denominator_closed=False,accepted_interfaces=0,
 contribution_reception=dict(creature_b='NOT_RECEIVED; no inferred repeat reading or acceptance',main='PENDING'),
 no_children=True,parallel_update_batches=[],update_started=False))

proposal=dict(id='GR8-XPCB-001',canonical_id='GR8-XPCB-001',alias_ids=[],
 title='版本迭代同时枚举版本0：现有条款已经明确覆盖',
 root_cause_key='Encounter.each_of_version-array-key-vs-symbol-registry',
 proposer='/root current context',local_disposition='WITHDRAWN_AS_NEW_REQUIRED_PROPOSAL_ALREADY_DOCUMENTED',
 classification='PENDING_INDEPENDENT_MAIN_DECISION',severity='UNDECIDED; no new demonstrated specification omission',
 affected_WP=['WP36','WP62'],history_ids='UNVERIFIED; historical ledgers not restored, no historical closure inferred',
 evidence=dict(source=[at('D03',20,59),at('D06',658,763),at('D16',13,21),at('D17',301,351),at('P01',20,50),at('P05',20,50),at('P09',20,50),at('P13',20,50)],
               spec=[at('D12',49,54),at('D11',120,125)],identity_resolution='identities.json#/payloads; exact repo/commit/tree/path/blob/bytes/SHA256; reading-ledger has byte coordinates for primary sections',
               recovery='git -C <repo> show <commit>:<path>; inspect stated inclusive line range in fixed blob. Private tool output is not claimed publicly replicated.'),
 premise='Fixed R normal compiler Symbol-key registry, map5v0 and v1 exactly as each backup file, registered referenced species and valid version1; no plugin/key replacement. Area consequence additionally requires metadata, no hide flag, matching region, visible point and valid scene/resources.',
 ordinary_control=['get(5,1) resolves v1 only.','each_of_version(0) yields v0 once for map5.','With only v0, each_of_version(1) yields v0.'],
 minimal_counterexample_steps=['In an isolated valid registry compile map5v0/v1 from any assigned encounters file; no run was performed here.',
 'Set version1; enumerate records and compare with direct get(5,1).',
 'Static result: iterator yields map5v0 then map5v1; direct get resolves map5v1.',
 'STARLY is in map5v0 PokeRadar slot and absent from map5v1. Conditional area UI union can therefore include its point even though the selected direct table lacks STARLY.'],
 actual_observation='SOURCE_STATIC reasoning only; behavior/runtime vectors NOT_EXECUTED.',
 current_spec_assertion='WP36 §3.1 already states exact map5 contrast; WP62 §5.3 already states conditional area consequence and preserves visibility/region/hidden gates.',
 demonstrated_difference='NONE against those current clauses. Original suspected omission is withdrawn locally, without final independent classification.',
 normal_failure_cancel_partial=dict(normal='Defined finite query/iterator behavior above.',
 failure='Compiler duplicate-section error occurs after previous section registration and before final save; not necessary to this normal-registry contrast.',
 cancel='No cancellation entry in these read-only query/enumeration methods; UI navigation and visibility remain separate.',
 exception='Bad registry/plugin objects or unavailable scene/media are outside finite premise; not converted to fallback behavior.',
 partial_commit='No writes in queried iterator. Compiler/editor save prefixes are separate IF01/IF04 open chains.'),
 negative_evidence=dict(complete_read_scope=['D03 full','D06 full','D12 full','D11 full','D16 full','D17 full','All four encounters files full'],
                       not_searched_or_unread='Remaining formal/test/historical catalogs, actual map metadata/TownMap, runtime/host. No global absence claim.'),
 impact='Potential extra area point under stated conditions is already specified; no newly justified edit to formal.',
 minimal_revision='None proposed for already covered clauses; retain their exact version/query distinction and UI gates.',
 preserve_scope=['Direct get version priority/fallback','v0/nonzero iterator finite contrast','Area hidden/region/visible-point prerequisites','No runtime PASS or generation-compatibility inference'],
 suggested_read_set=['D03','D06','D12 §3.1','D11 §5.3','D16 setup','D17 pbFindEncounter/pbGetEncounterPoints','P01/P05/P09/P13 map5 sections'],
 suggested_write_set=[],sync='No accepted edit and no remediation batch; main should preserve original candidate/withdrawal and independently decide.',
 acceptance=[dict(id='A01',kind='STATIC',criterion='Actual different reviewer verifies normal Symbol key registration and iterator fallback condition in fixed blobs.'),
             dict(id='A02',kind='STATIC',criterion='Actual different reviewer checks all exact current clauses and decides whether any residual omission exists.'),
             dict(id='A03',kind='STATIC',criterion='Do not generalize iterator defect to direct lookup or unconditional area display.'),
             dict(id='A04',kind='RUNTIME',criterion='Optional isolated scenario, if safely available; report actual execution separately. Currently NOT_EXECUTED.')],
 regression_scope=['map5 v0/v1 lookup and iterator','only-v0 and v0 iterator','STARLY contrast','hidden/missing metadata/wrong region/no visible point prevents area contribution'],
 independent_disproof=dict(reviewer='NOT_ASSIGNED_IN_THIS_CONTEXT',evidence='NOT_RECEIVED',state='PENDING_MAIN_REVIEWER',reason='Same current context cannot create independence by renaming its role.'),
 dependency=dict(direct=['IF05','IF06'],transitive=['IF01','IF02'],blocking='Final classification/reception needs actual independent main review; overall task separately blocked by available-unread work.',
                 batch='NONE',author='NONE: UPDATE_NOT_STARTED',shared_receiver='Main reviewer',closure='Independent disproof and final reception; no final closure asserted.'))
write('proposals.json',dict(schema='r8-task-proposals/v1',utc=UTC,status='PENDING_MAIN_REVIEWER',
 records=[proposal],required_accepted=0,optional_accepted=0,no_required_revision_accepted=0,policy_accepted=0,limit_accepted=0,
 no_required_update=False,reason='Incomplete reading/clauses and absent independent reception prevent a global no-required-update decision.',update_started=False))
write('execution.json',dict(schema='r8-task-execution/v1',utc=UTC,
 behavior_executions=0,behavior_vectors='NOT_EXECUTED',host_observation='NOT_EXECUTED',
 reference_compile='NOT_EXECUTED',reference_writer='NOT_EXECUTED',reference_game_or_save='NOT_EXECUTED',
 actual_configuration=dict(model='UNVERIFIED',effort='UNVERIFIED',tier='UNVERIFIED',fast='UNVERIFIED'),
 requested_configuration=dict(model='gpt-6.1-sol',effort='ultra',tier='default',fast=False),
 public_io='preflight-io.json and publication/check logs only; tool source displays remain private platform stream, not a published raw-source archive.',
 source_read_receipts='semantic-notes.json records known chunk IDs/ranges, not a claim of externally retrievable platform full transcript.',
 complete_raw_platform_transcript_export='UNVERIFIED_NOT_EXPORTED',
 notable_tool_failures=[dict(action='Initial unfiltered fetch of pinned commit',exit_code=143,reason='Explicit SIGTERM after stalled transfer; stderr fatal: early EOF. Filtered depth1 fetch then succeeded; no source modification.'),
 dict(action='Diagnostic cat of nonexistent own report-root path',exit_code=1,reason='No such file; no reading credit or source change.'),
 dict(action='Search supplied nonexistent root test-catalog path alongside actual formal tree',exit_code=2,reason='Correct files located under deliverables/final-specification-set/test-catalog; no read credit from this search.')],
 history='Historical R6/R7 attempts not added to R8 counters. Historical PASS grants no read/acceptance credit.',
 protections='Only dedicated branch and own task directory authorized for report commits/push; no formal/reference remediation.',
 update_started=False))
print(json.dumps(dict(fact_notes=len(facts),reverse_notes=len(rows),interfaces=len(chains),local_questions=1)))
