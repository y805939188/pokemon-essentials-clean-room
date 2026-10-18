from pathlib import Path
import json,datetime
o=Path(__file__).resolve().parent;ids=json.loads((o/'identities.json').read_text())
def bind(kind,index,ranges,meaning):
 x=next(x for x in ids['files'] if x['kind']==kind and x['index']==index)
 return {k:x[k] for k in ('repo','commit','workspace_tree','path','bytes','sha256','git_blob')}|{'ranges':ranges,'meaning':meaning,'actual_identity_matches_frozen':x['identity_matches_frozen'],'reader':'/root/com_ai'}
main=bind('formal',3,[[211,219]],'§6 retains default User0 bypass but lacks callable target handler once+14 definition')
coverage=bind('formal',2,[[180,199],[209,213]],'F/G identity is correct; registration pointer is not full conditional score definition')
catalog=bind('formal',8,[[168,175]],'AE-T02 currently only default bypass vs unspecified future extension; add explicit current direct-call vectors')
source=bind('reference',13,[[784,830]],'Complete Conversion whole failure and existing target-score handler candidate discovery/usable-type/once+14')
p={
 'id':'GR8-AI-001','classification':'PROPOSED_REQUIRED_ROOT_PENDING','severity':'P3','severity_reason':'Finite readable callable evaluation definition is omitted; ordinary default User0 bypass is correct and no default gameplay misranking is asserted.',
 'module':'COM-AI','primary_wp':'WP52-A','primary_contract':main['path']+' §6','root_cause_key':'conversion-callable-target-score-definition-omitted','canonical':True,'aliases':[],
 'history_relation':{'historical_id':'UNASSIGNED_BY_THIS_TASK','reason':'No prior root asserted; root/history owner must complete dedup. Existing correct User0 explanation retained.'},
 'status':'INDEPENDENT_BOUNDED_COUNTEREVIDENCE_COMPLETE_ROOT_ADJUDICATION_PENDING','proposer':'/root/com_ai',
 'evidence':[source,main,coverage,catalog,bind('reference',0,[[79,116]],'Existing callable target-score wrapper retains prior only for nil; existing dispatcher'),bind('reference',4,[[1,88],[215,324]],'Ordinary num_targets0 route scores without targets, so target registration not consumed'),bind('reference',9,[[285,315]],'Usable move helper skips finite PP0 and tests damaging calculated type')],
 'supplementary_evidence':{'identity_and_read_ranges':'../com_facility/adjudications-ai.json#/evidence','actual_owner_reads':['io/D_CONVTARGET.json','io/D_CONVPBS.json'],'facts':'PBS CONVERSION TargetUser; Target default cardinality0; no source loading/execution performed'},
 'fact_chain':[
  'Frozen PBS function identity and User target feed normal candidate constructor. Target cardinality0 means no individual target-effect invocation on the ordinary route.',
  'The existing target-effect wrapper is independently callable with the same already registered function identity and valid AI state. Its handler does not read the supplied target.',
  'Candidate type discovery examines original raw move types, only first slot at generation>=6 or all slots earlier, excluding pseudo types and types already held by user. Candidate discovery itself does not PPfilter.',
  'For each candidate type in order it asks whether user has a usable damaging move of that calculated type; finite PP0 with positive totalPP is excluded by that helper. First match adds14 once and stops; none preserves incoming score.',
  'The result is an evaluation value only. No HP, party, held item, bag, learned move, display or persistent save is committed by this handler.'
 ],
 'finite_premises':[
  'Direct invocation of the existing apply_move_effect_against_target_score wrapper, valid AI user/move/function key and any valid target, incoming score100. No plugins/custom override or invalid registry entries; all accessed helpers return normally.',
  'User typeNORMAL, generation>=6 unless explicitly changed; first raw slotFIRE damaging move with PP>0, positive totalPP; Conversion in a later slot. Corresponding calculated type remainsFIRE, pseudo flagfalse. No other score handlers are part of this isolated query.',
  'This is a current available callable-definition domain. It is not a claim arbitrary nondefault target configuration is reached by normal CONVERSION gameplay.'
 ],
 'normal_control':'Unchanged default CONVERSION/User0 candidate construction does not invoke this target handler. Do not infer full candidate100 because unrelated general modifiers may apply.',
 'minimal_counterexample':{
  'steps':['Prepare finite valid user and move context stated above.','Call the existing target-effect wrapper for SetUserTypesToUserMoveType with score100.','Observe its returned evaluation value without invoking real move execution.'],
  'reference_derived':'114; one matching candidate contributes14 and stops.',
  'current_formal_difference':'Main §6 states only the correct normal-path nonconsumption, coverage only names G registration, AE-T02 leaves target consumption extension unverified. The finite currently callable candidate/PP/once+14 rule is absent.',
  'negative_controls':['Only change first raw slot to already-owned NORMAL; later usableFIRE exists: no current-generation candidate,100.','Keep FIRE first but its finite PP0 and no other usable FIRE damage: candidate discovered but usable helper false,100.','Change only generation<6 with firstNORMAL and laterusableFIRE: later candidate can contribute14. Multiple qualifying candidates still only14.'],
  'execution':'NOT_EXECUTED','evidence_level':'SOURCE_STATIC; DERIVED_VECTOR'
 },
 'state_paths':{
  'normal':'Direct callable query returns incoming+14 once or incoming. Ordinary User0 route does not enter it.',
  'failure':'Ordinary whole prediction uses canChangeType/candidate discovery separately; direct scoring does not silently run prediction or add a new central eligibility gate.',
  'cancel':'No confirm/cancel transaction exists inside this pure scoring query; command cancellation belongs earlier/later command consumer and no action outcome is claimed.',
  'exception':'Invalid registry/helper input can propagate before return; no new rescue/default/rollback contract is inferred.',
  'partial_commit':'Only local score/candidate list changes; no business-state write or persistent reload result. Exceptions do not justify invented whole-round atomicity.'
 },
 'negative_evidence':{'scope':'All9 primary formal files actually fully read; entire final-specification-set searched for SetUserTypesToUserMoveType/Conversion/纹理; relevant §6, coverage§2.4, AE-T02 and WP47-A runtime clause contrasted.','original_output':'negative-conversion.json','result':'No matching current target-score +14 candidate/PP/once rule located; environment change +14 is a different handler with additional loss term. Runtime WP47-A describes random type mutation rather than evaluation.','limits':'No unseen external specification or future plugin behavior asserted.'},
 'impact':'An implementer preserving ordinary User0 behavior still lacks the complete observable definition of a supported existing evaluation query. Scope is documentation completeness P3.',
 'minimum_revision':{
  'correct_final_rule':'Retain ordinary User0 nonconsumption. Separately specify that when the registered target-score query is actually invoked, gather first raw type at generation>=6 or all older raw types excluding pseudo/already-owned types; first candidate for which a PP-aware usable damaging move has matching calculated type contributes14 once; none retains input. Candidate discovery and usable damage traversal have different PP treatment.',
  'preserve_scope':['Default CONVERSION User0 does not invoke G scoring.','Existing whole failure qualification.','No defensive type-benefit or STAB-loss penalty borrowed from environment change.','No target-score promotion to whole-score family.','WP51 skill flags/thresholds/weights and current real Conversion random choice unchanged.'],
  'read_set':[source['path'],'Data/Scripts/011_Battle/005_AI/001_Battle_AI.rb','Data/Scripts/011_Battle/005_AI/005_AI_ChooseMove.rb','Data/Scripts/011_Battle/005_AI/010_AIBattler.rb','Data/Scripts/010_Data/001_Hardcoded data/017_Target.rb','PBS/moves.txt',main['path'],coverage['path'],catalog['path'],'deliverables/final-specification-set/combat-requirements/wp47-a-move-attributes-targeting-and-calling.md'],
  'required_write_set':[main['path'],catalog['path']],
  'sync_dispositions':[{'path':coverage['path'],'reason':'Existing F/G mapping remains correct; recheck reference, no required text change unless anchors change.'},{'path':'deliverables/final-specification-set/combat-requirements/wp47-a-move-attributes-targeting-and-calling.md','reason':'Runtime type mutation remains correct; read-only consistency check, no new runtime rule.'}],
  'public_index':'Root owns any closure/index/manifest changes; this finite new definition does not imply a new engine framework.'
 },
 'acceptance':[
  'WP52-A§6 explicitly distinguishes ordinary User0 bypass and conditional current target-query definition.',
  'Type discovery uses original raw type, generation first/all selection and pseudo/current-type exclusions; usable damage query uses calculated type and finitePPfilter.',
  'Finite direct100→114, rawfirstalreadyowned100, rawcandidatefinitePP0/noothermatching100, oldgenerationlatercandidate114, multitypeonlyonce vectors are all statically decidable.',
  'Normal CONVERSION User0 target contribution remains NOT_ENTERED, with no assertion full candidate/real action success.',
  'Scoring has no HP/item/learnedmove/save writes and no borrowed Camouflage loss term. All business execution remains NOT_EXECUTED unless separately logged actual run occurs.'
 ],
 'regression_scope':['AE-T01 environment±14 distinct','AE-T02 original ordinary bypass','BE-B62 Geomancy target-only consumption','CE-C46/C57 Imprison target-only consumption','WP51 q/weights and ScoreMoves gate'],
 'independent_review':{'proposer':'/root/com_ai','counter_reviewer':'/root/com_facility','different_actual_context':True,'evidence_path':'../com_facility/adjudications-ai.json','recommendation':'SUSTAIN_NARROW_REQUIRED_P3_IF_OWNER_FULL_PROPOSAL_MATCHES','root_decision':'PENDING_ROOT_CANONICAL_CLASSIFICATION','not_a_new_reviewer_from_resume':True},
 'dependencies':{'direct':['Root final canonical/dedup/classification','Actual independent final review of any later edited WP52-A+catalog contribution'],'transitive':['Root shared catalog integration and retained-correct scope reception'],'blocking':['Root decision and later nonauthor revision acceptance'],'nonblocking':['Full default PBS/compiler/runtime reload chain is not needed to decide this direct current handler definition'],'file_conflicts':[main['path'],catalog['path']],'primary_batch':'ROOT_TO_ASSIGN_EXACTLY_ONCE','author_entry':'Later user-triggered update task; no update author started','independent_reviewer_entry':'A later actual nonauthor context, not proposer role rename','shared_receivers':['COM-MOVE for unchanged runtime contract','COM-AI for handler/default distinction','Root shared catalog owner'],'closure':'Root accepts full record, later user manually starts revision, actual nonauthor accepts final edited contributions and all necessary synchronization.'},
 'limits':['Actual Ruby/game/host execution NOT_EXECUTED; no claim observed114.','Actual model/effort/tier/speed/Fast/platformopaqueID UNVERIFIED.'],
 'excluded_claims':['Default gameplay defect','Wrong AI skill or weight formula','Runtime Conversion implementation change','GlobalCOM-AI or whole-system acceptance'],
 'update_started':False
}
q={
 'id':'GR8-AI-002','classification':'PROPOSED_OPTIONAL_EDITORIAL_ROOT_PENDING','severity':'P4','severity_reason':'Conflicting registration count only; complete behavioral table and coverage identities remain readable and correct.',
 'module':'COM-AI','primary_wp':'WP52-A','root_cause_key':'ability-ranking-registration-count-23-vs25','canonical':True,'aliases':[],
 'status':'INDEPENDENT_BOUNDED_COUNTEREVIDENCE_COMPLETE_ROOT_OPTIONAL_DECISION_PENDING','proposer':'/root/com_ai','history_relation':'No historical root asserted; administrative candidate only.',
 'evidence':[bind('formal',3,[[219,232]],'23 registrations copies extra'),bind('formal',2,[[209,213]],'25 expanded registrations:20adds+5copies'),bind('reference',7,[[231,382]],'All20add definitions and5copy target bindings actually read')],
 'premises':'Fixed R/B8 default handlers, exact same family; count excludes conditional item groups and other families.',
 'normal_control':'Main behavior table and coverage25 list still fully describe all concrete ability modifiers; no missing modifier identified.',
 'minimal_counterexample':'Count20add declarations and5copy targets in AbilityRanking; main23 cannot simultaneously mean20direct or25expanded. This is an administrative consistency check, not a battle vector.',
 'state_paths':'No normal/cancel/failure/exception/partial business transaction applies to a prose census; no gameplay behavior revision authorized.',
 'negative_evidence':'Complete utility file and complete main/coverage files read; no extra3 AbilityRankingadd registrations in fixed source. No future plugin census claim.',
 'impact':'Navigation/census ambiguity; no independently established behavioral implementation error.',
 'minimum_revision':'Optionally say20 direct plus5 copied targets (25expanded), or remove unstable local count and link exact coverage. Preserve every modifier, default, typo literal and semantic gate.',
 'read_set':['Data/Scripts/011_Battle/005_AI/008_AI_Utilities.rb',main['path'],coverage['path']],
 'write_set':[main['path']],
 'acceptance':['Main local count unambiguously agrees with coverage20add+5copy=25, if owner chooses edit.','No behavioral table, copy source, typing, flag or default altered.'],
 'independent_review':{'reviewer':'/root/com_facility','evidence_path':'../com_facility/adjudications-ai.json#/separate_count_candidate','recommendation':'OPTIONAL_EDITORIAL_ONLY','root_decision':'PENDING'},
 'dependencies':{'blocking':'Root decides whether optional revision belongs later batch; not a mandatory behavior blocker.','file_conflicts':[main['path']],'primary_batch':'ROOT_OPTIONAL_TO_ASSIGN_IF_CHOSEN','closure':'No required closure counted from this candidate.'},
 'evidence_levels':['SOURCE_STATIC','FORMAL_TEXT_READ'],'execution':'NOT_EXECUTED','new_behavior_runs':0,'update_started':False,
 'excluded_claims':['Required behavior repair','Missing modifier implementations','AI ranking runtime defect']
}
r={'schema':'gr8-com-ai-proposals/v1','updated_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'B8_commit':ids['B8_commit'],'R_commit':ids['R_commit'],'reader':'/root/com_ai','actual_config':ids['actual_config'],'records':[p,q],'classification_note':'Proposals and independent recommendations are not final root required/optional classification. No automatic repair.','update_started':False}
(o/'proposals.json').write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'records':len(r['records']),'ids':[p['id'],q['id']]}))
