from pathlib import Path
import json,hashlib,subprocess,datetime
ROOT=Path(__file__).resolve().parent
BASE='fd1df570cad987dc3852a3b958f03916e317f7fe'
REF='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
BROOT='/workspace/pokemon-essentials-clean-room'
RROOT='/workspace/pokemon-essentials'
NOW=datetime.datetime.now(datetime.timezone.utc).isoformat()
TASK='/root/counter_combat_first'
S='deliverables/final-specification-set/'
paths={
 'WP39':S+'combat-requirements/wp39-battle-context-and-participants.md',
 'WP40':S+'combat-requirements/wp40-commands-obedience-and-action-order.md',
 'WP48':S+'pokemon-rules/wp48-ability-calculation-modifiers.md',
 'WP49':S+'combat-requirements/wp49-ability-phase-triggers.md',
 'WP42':S+'combat-requirements/wp42-growth-end-of-round-and-battle-outcomes.md',
 'WP51':S+'combat-requirements/wp51-ai-action-selection-and-skill.md',
 'WP67A':S+'user-interface/wp67-a-battle-interaction-and-presentation.md',
 'BC_CM':S+'test-catalog/combat-requirements-wp39-40-41-42-45.md',
 'AB':S+'test-catalog/pokemon-rules-wp43-44-46-48-50.md',
 'AI_TEST':S+'test-catalog/combat-requirements-wp49-51-52.md',
 'BATTLE':'Data/Scripts/011_Battle/001_Battle/001_Battle.rb',
 'START':'Data/Scripts/011_Battle/001_Battle/002_Battle_StartAndEnd.rb',
 'PRIORITY':'Data/Scripts/011_Battle/001_Battle/004_Battle_ActionAttacksPriority.rb',
 'COMMAND':'Data/Scripts/011_Battle/001_Battle/009_Battle_CommandPhase.rb',
 'ATTACK':'Data/Scripts/011_Battle/001_Battle/010_Battle_AttackPhase.rb',
 'ABILITY':'Data/Scripts/011_Battle/007_Other battle code/008_Battle_AbilityEffects.rb',
 'SUCCESS':'Data/Scripts/011_Battle/002_Battler/009_Battler_UseMoveSuccessChecks.rb',
 'CREATE':'Data/Scripts/012_Overworld/002_Battle triggering/001_Overworld_BattleStarting.rb',
 'OUTER':'Data/Scripts/012_Overworld/002_Battle triggering/002_Overworld_BattleIntroAnim.rb',
 'AI':'Data/Scripts/011_Battle/005_AI/001_Battle_AI.rb',
 'AITRAINER':'Data/Scripts/011_Battle/005_AI/009_AITrainer.rb',
 'AIBATTLER':'Data/Scripts/011_Battle/005_AI/010_AIBattler.rb',
 'AIMOVE':'Data/Scripts/011_Battle/005_AI/005_AI_ChooseMove.rb',
 'PEER':'Data/Scripts/011_Battle/007_Other battle code/004_Battle_Peers.rb',
 'SWITCH':'Data/Scripts/011_Battle/001_Battle/005_Battle_ActionSwitching.rb',
 'INITIALIZE':'Data/Scripts/011_Battle/002_Battler/002_Battler_Initialize.rb',
 'BATTLER':'Data/Scripts/011_Battle/002_Battler/001_Battle_Battler.rb',
 'POKEMON':'Data/Scripts/014_Pokemon/001_Pokemon.rb',
 'TRAINER':'Data/Scripts/015_Trainers and player/001_Trainer.rb',
 'SCENEINIT':'Data/Scripts/011_Battle/004_Scene/002_Scene_Initialize.rb',
 'SCENEPOS':'Data/Scripts/011_Battle/004_Scene/001_Battle_Scene.rb',
 'SCENEBOX':'Data/Scripts/011_Battle/004_Scene/006_Battle_Scene_Objects.rb',
 'SCENEMENU':'Data/Scripts/011_Battle/004_Scene/005_Battle_Scene_Menus.rb',
 'SCENEPLAY':'Data/Scripts/011_Battle/004_Scene/004_Scene_PlayAnimations.rb',
 'SCENEANIM':'Data/Scripts/011_Battle/004_Scene/008_Battle_Scene_Animations.rb',
 'HANDLER':'Data/Scripts/003_Game processing/005_Event_Handlers.rb',
 'FORM':'Data/Scripts/014_Pokemon/001_Pokemon-related/001_FormHandlers.rb',
 'FORMCHECK':'Data/Scripts/011_Battle/002_Battler/003_Battler_ChangeSelf.rb',
 'SETTINGS':'Data/Scripts/001_Settings.rb',
 'BSETTINGS':'Data/Scripts/002_BattleSettings.rb',
 'PBS_ABILITY':'PBS/abilities.txt',
 'PBS_SPECIES':'PBS/pokemon.txt',
 'PBS_MOVES':'PBS/moves.txt',
 'OLD_B002':'review/remediation/20261003-prepare/batches/B09/candidate-1/contribution-dispositions.json'
}
def dump(name,d):
 (ROOT/name).write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
def git(repo,*a):
 return subprocess.check_output(['git','-C',repo,*a]).decode().strip()
def identity(repo,commit,path):
 data=subprocess.check_output(['git','-C',repo,'show',commit+':'+path])
 mode=git(repo,'ls-tree',commit,'--',path).split()[0]
 return {'repo':repo,'commit':commit,'tree':git(repo,'rev-parse',commit+'^{tree}'),'path':path,'mode':mode,'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest(),'blob':git(repo,'rev-parse',commit+':'+path)}
ops=[];groups={}
for p in sorted((ROOT/'io').glob('*.json')):
 d=json.loads(p.read_text()); d['io_record']=str(p.relative_to(ROOT)); ops.append(d)
 if 'path' not in d: continue
 key=(d['repo'],d['commit'],d['path'],d['sha256'])
 x=groups.setdefault(key,{k:d.get(k) for k in ['repo','commit','path','bytes','sha256','blob','total_lines']})
 x.setdefault('ranges',[]).append(d['range']);x.setdefault('io_records',[]).append(str(p.relative_to(ROOT)))
for (repo,c,path,sha),d in groups.items():
 rs=sorted(d['ranges']);merged=[]
 for a,b in rs:
  if merged and a<=merged[-1][1]+1: merged[-1][1]=max(merged[-1][1],b)
  else: merged.append([a,b])
 d['ranges']=merged;d['reading_status']='FULL_READ' if merged==[[1,d['total_lines']]] else 'BOUNDED_UNITS_READ'
 d['outside_ranges']='UNREAD_IN_THIS_TASK; no whole-file semantic completion claimed' if d['reading_status']!='FULL_READ' else []
 d['reviewer']=TASK;d['evidence_level']='SOURCE_STATIC';d['behavior_execution']='NOT_EXECUTED'
 if c!='WORKTREE':
  d['tree']=git(repo,'rev-parse',c+'^{tree}')
  d['mode']=git(repo,'ls-tree',c,'--',path).split()[0]
 else:
  d['tree']=None
  current=(Path(repo)/path).read_bytes()
  d['blob']=hashlib.sha1(b'blob '+str(len(current)).encode()+b'\0'+current).hexdigest() if hashlib.sha256(current).hexdigest()==sha else 'UNVERIFIED_CURRENT_WORKTREE_CHANGED'
  d['mode']='WORKTREE_FILE';d['qualification']='Working report/input bytes at recorded UTC; not B8 normative payload. Blob is computed only when current bytes still match the recorded read SHA.'
ledger={'schema':'r8.counter-review.read-ledger.v1','reviewer':TASK,'scope':['GR8-COM-001','GR8-COM-002'],'updated_utc':NOW,'read_policy':'Only human semantic reading of returned ranges grants credit. Searches and hash matches grant location/identity credit only. Partial documents retain exact ranges.','prerequisites':[{'path':'AGENTS.md','bytes':6328,'sha256':'41cea9c6aa439dc70eaca2c26ce1f7967a887538c1aef25b9297c07b0437ff40','status':'FULL_READ','platform_io':'ff4053'},{'path':'inputs/eighth-global-review-prompt.md','bytes':36653,'sha256':'63944b6f264a8e4ed1415db710443a0673f250b8a248af2274a425a314ea068b','status':'FULL_READ_BY_CONTINUOUS_REREAD','platform_io':['49120e (1–140)','4e71cd (141–end)','io/0046.json (126–141 overlap)'],'initial_truncation_not_used_as_credit':True},{'path':'inputs/review-SKILL.md','bytes':3598,'sha256':'ac3c8560f38192269b65b061673896a77f5eb794b90e90644e3c445b2c3be1f8','status':'FULL_READ','platform_io':'a91afb','applicability':'Explicitly excludes audit reports; final-state document revisions are not performed by this counter-review.'}],'payloads':list(groups.values()),'tool_operations':[{'io_record':d['io_record'],'kind':d['kind'],'started_utc':d['started_utc'],'ended_utc':d['ended_utc'],'argv':d['argv'],'exit_code':d['exit_code']} for d in ops],'mechanical_validation':{'source_worktree_equals_fixed_R':'432 tracked files, mismatches0; io/0100.json','formal_worktree_equals_B8':'131 formal files, mismatches0; io/0100.json','interpretation':'Neither count nor hash match grants semantic reading of unlisted material.'},'source_static_execution_count':0,'behavior_execution_count':0,'update_started':False}
dump('read-ledger.json',ledger)
# Complete reusable evidence identities, with semantic positions separately below.
ev={}
for label,path in paths.items():
 c='d15259042aa6665b3fa75786a4d3650d702cab5c' if label=='OLD_B002' else (BASE if path.startswith('deliverables/') else REF)
 repo=BROOT if path.startswith(('deliverables/','review/')) else RROOT
 ev[label]=identity(repo,c,path)
ev['B7_WP39']=identity(BROOT,'e646432c644dec04d306842cc5a559a29c718fbc',paths['WP39'])
# Audit payload identities are not normative/source claims.
for name in ['findings.json','negative-evidence.json','progress.json']:
 p=ROOT.parent/'combat_review'/name;b=p.read_bytes()
 ev['PROPOSER_'+name]={'repo':BROOT,'commit':'WORKTREE_AUDIT_SNAPSHOT_AT_DELIVERY','tree':None,'path':str(p.relative_to(Path(BROOT))),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'blob':hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest(),'mode':'WORKTREE_FILE','qualification':'Proposer audit snapshot at result preparation is evidence under review, not accepted B8 content. Actual earlier read identities are separately in read-ledger.json.'}
dump('evidence-bindings.json',{'schema':'r8.counter-review.evidence-bindings.v1','updated_utc':NOW,'bindings':ev})
def loc(k,lines,meaning):return {'evidence_id':k,'lines':lines,'meaning':meaning,'identity':'evidence-bindings.json#/bindings/'+k}
common={'reviewer':TASK,'proposer':'/root/combat_review','reviewer_is_distinct_actual_context':True,'reviewer_was_not_proposer':True,'reviewer_authorship':'This context made no formal-specification edits and has not authored the reviewed B8 clauses. Historical unseen authorship cannot be inferred.','requested_configuration':{'model':'gpt-6.1-sol','effort':'ultra','tier':'default','fast':False},'actual_configuration':{'model':'UNVERIFIED','effort':'UNVERIFIED','tier':'UNVERIFIED','fast':'UNVERIFIED','platform_id':'UNVERIFIED'},'actual_logical_task_entry':TASK,'evidence_levels':['SOURCE_STATIC','DERIVED_VECTOR'],'execution':'NOT_EXECUTED','reference_observations':0,'independent_model_executions':0,'full_host_executions':0}
first={
 'id':'GR8-COM-001','recommendation':'SUSTAINED_REQUIRED','classification_recommendation':'required','severity_recommendation':'P3','primary_wp':'WP40','root_cause_key':'priority-bracket-ability-misidentification','status':'INDEPENDENT_COUNTER_REVIEW_COMPLETE_ROOT_ADJUDICATION_PENDING',
 'finding_narrowing':'The actual defect is an inconsistent ability example/name, not an explicit numeric clause assigning TRUANT -1. WP48 already gives the correct complete identity table. Do not characterize the linked specification as wholly lacking the sorting rule or claim a runtime defect.',
 'decision_reason':'WP40 §5.4 and §5.2.1 consistently use 懒惰 for the alternating refusal ability; WP49 expressly pairs TRUANT with 懒惰. WP40 §6.1 then uses 如懒惰类 as a bracket-changing example. The same document therefore invites a different identity from the correct WP48 table. Required correction can be one in-place identifier substitution; no new combat rule is needed.',
 'counter_arguments':[
 {'attempt':'Read full linked WP48 and WP40 instead of isolating one sentence.','result':'PARTLY_SUCCESSFUL_NARROWING','reason':'WP48 §3/§9 uniquely names QUICKDRAW/STALL for bracket changes and states their values. An informed integrated reader can resolve the intended ability to STALL. This prevents a claim of missing global mechanics and limits severity to P3, but does not make the same-document reused name correct.'},
 {'attempt':'Treat 懒惰类 as a generic description of slow behavior rather than TRUANT.','result':'REJECTED_AS_COMPLETE_REBUTTAL','reason':'Within WP40 the exact Chinese name already labels the alternate-turn action gate, so that reading requires silently changing the local terminology. A data identity STALL removes ambiguity without translation research.'},
 {'attempt':'TRUANT may alter order indirectly through skip/priority.','result':'REJECTED_FOR_BRACKET','reason':'The real receiver queries the current effective ability during full sorting. Missing registration returns0; direct TRUANT refusal occurs later after status/obedience. Such refusal is not bracket -1.'}
 ],
 'bidirectional_evidence':[
 loc('WP40',[[174,188],[218,235],[253,270]],'Current failure/action gate names and the disputed bracket example; complete file read io/0005–0006.'),
 loc('WP48',[[13,17],[36,52],[202,213]],'Complete linked mapping: QUICKDRAW30%+1, STALL−1; local recalculation does not re-draw.'),
 loc('WP49',[[19,38]],'Current formal terminology explicitly pairs TRUANT with 懒惰; not inferred from an outside translation dictionary.'),
 loc('ABILITY',[[69,72],[140,149],[844,858]],'Missing bracket result defaults0; concrete handlers only QUICKDRAW and STALL.'),
 loc('HANDLER',[[148,197],[288,292]],'Actual ability handler resolver, conditional fallback and trigger semantics; no TRUANT bracket fallback found in fixed Scripts.'),
 loc('PRIORITY',[[136,176],[217,260],[264,278]],'Effective ability receiver; merge and comparator; living consumer excludes fainted objects.'),
 loc('SUCCESS',[[183,248]],'Execution order and direct TRUANT gate after obedience; separate recharge branch.'),
 loc('INITIALIZE',[[128,149],[273,279]],'Normal initial Truant flagfalse supplies an acting first-turn control.'),
 loc('BATTLER',[[344,355]],'Living/uncompressed effective-ability premise.'),
 loc('PBS_ABILITY',[[217,220],[401,404]],'Different data identities; descriptions alone are not behavior evidence.'),
 loc('BC_CM',[[45,77]],'CM07/08 correct merging and Trick Room controls.'),
 loc('AB',[[159,187]],'AB04 full versus incremental QUICKDRAW behavior remains valid.')
 ],
 'finite_premises':['Ordinary living battlers, default registered handlers, no plugin/override, no Gastro Acid/Neutralizing Gas or other suppression.','Both have a usable ordinary priority0 move; no item bracket, no Trick Room, no competing forced/Quash scheduling, no status/obedience rejection.','A effective speed100, B50; B no bracket effect; A TRUANT acting flag initiallyfalse or otherwise its actual next action is permitted. These are finite current battlefield states, not a claim naturally generated species share the two abilities.'],
 'vectors':[
 {'id':'CC1_STALL','kind':'ordinary_control','input':'A effective STALL speed100, B neutral speed50, same priority0 and no items.','derived_result':'A bracket−1/B0, B precedes A.','execution':'NOT_EXECUTED'},
 {'id':'CC1_TRUANT','kind':'minimal_identity_contrast','input':'Only replace A current effective identity by TRUANT; its next action permitted.','derived_result':'A bracket0/B0, A precedes B by speed. A later may alternate refusal; no bracket effect arises from that.','execution':'NOT_EXECUTED'},
 {'id':'CC1_TRUANT_REFUSAL','kind':'negative_boundary','input':'Same order but A actual Truant state causes this action to loaf.','derived_result':'Ordering remains neutral bracket; later action rejection has separate failed flag and no PP deduction at the gate.','execution':'NOT_EXECUTED'}
 ],
 'state_paths':{'normal':'Correct linked bracket/merge/comparator unchanged.','failure':'Later TRUANT refusal cannot establish slower bracket. Missing ability registration is neutral at this endpoint only.','cancel':'Command cancellation before attack sorting does not produce a completed round/order result; already established full entry sorting is a different call.','exception_partial_commit':'No new exception rollback contract. These ordinary vectors require handlers, logging and diagnostics to return normally.'},
 'negative_evidence':{'scope':'Full fixed Scripts literal searches for PriorityBracketChange plus all actual add/addIf/copy hits, full resolver and relevant dispatcher/handlers; full WP40/WP48 primary contracts, relevant BC/CM and AB units.','io_records':['io/0073.json','io/0082.json','io/0035.json'],'found':'Only QUICKDRAW/STALL bracket registrations. Existing Chinese name assignments consistently refer to alternate-turn behavior elsewhere.','limits':'No universal plugin/translation dictionary assertion; no full runtime or arbitrary custom-handler exploration.'},
 'minimum_revision':{'required':'In-place replace the misleading bracket example with explicit STALL (optionally QUICKDRAW alongside it). Preserve TRUANT action refusal under §5.4; a parenthetical TRUANT there may improve internal identity clarity.','required_write_set':[paths['WP40']],'sync_if_catalog_updated':[paths['BC_CM']],'correct_preserve_scope':['WP48 correct table and AB04','CM07 fast item overrides slow ability; CM08 higher priority/bracket before Trick Room speed','TRUANT recharge and alternating action gates','Full versus incremental tie/bracket behavior','Effective ability and default generation/configuration gates'],'no_new_requirement':'No new sorting algorithm, no species ability restriction, no engine implementation, no mandatory extra full-host test for a naming correction.'},
 'acceptance':['WP40 bracket example unambiguously identifies STALL and does not assign TRUANT a bracket.','Cross-read WP40/WP48 yields identical identities, bracket values and stage separation.','Static CC1_STALL/CC1_TRUANT contrasted with CM07/CM08/AB04; labels remain NOT_EXECUTED unless a separately logged real run occurs.'],
 'history_relation':{'historical_id':'UNASSIGNED_BY_THIS_TASK','scope':'No historical root asserted. Existing qualified R7 closure cannot certify this inconsistent phrase; root/history owner retains final dedup.'},
 'dependencies':{'blocking_final_acceptance':['Root canonical/classification decision and shared WP40 reception'],'nonblocking':['Optional text explanation or extra static regression row'],'file_conflicts':[paths['WP40'],paths['BC_CM']],'batch':'ROOT_TO_ASSIGN'},
 'unresolved':['Final root disposition and any historical alias; actual runtime configuration/host unverified.'],
 'excluded_claims':['Source/runtime sorting bug','Explicit current specification numeric TRUANT−1 assignment','All combat/AI reviewed or globally passed']
}
zero={
 'facet_id':'ZERO_ABLE','recommendation':'SUSTAINED_REQUIRED','severity_recommendation':'P2','root_cause_key':'wild-sparse-absent-able-count-propagates-into-layout','mechanical_root_relation':'Shares sparse absent-count production with historical GIR-FD82-B002, but the wild synchronization consumes the absent first count before owner-range checking. It is a new missing wild facet, not a new claim that old NPC clauses are wrong.',
 'ordinary_control':{'input':'Direct ordinary wild core, player one healthy non-egg, no partner/debug/rules/override, one preexisting ordinary CATERPIE P HP1.','derived':'Nonempty construction, wild able count1, default1v1 remains valid; participant check can return normally.'},
 'minimal_counterexample':{'input':'Change only P HP1→0 using supported persistent HP setter; P remains a nonempty legal Pokemon object, not egg.','derived':['Player skip guard remainsfalse. Existing P reference reused. Start-party level/critical/direct-damage records have been created, battle constructed/prepared, creation rules cleared.','Wild team count has no first item, not numeric0. Equal initial sides1/1 are both replaced by the absent value.','First player-side enumeration on the now-absent side size raises a general exception, earlier than owner-range/has-no-able checks, starting-form hooks, seat creation, battle-scene pbStartBattle, or the dedicated abort catch.','No ordinary outcome/boolean/result-variable write from this failed core is reached.'],'execution':'NOT_EXECUTED'},
 'partial_commit':{'known_local_prefix':'At ordinary outer animation entry in_battle=true; completed BGM/BGS pause and transition, fade push and applicable map-spriteset disposal/cache clear/frame reset precede pbStartBattle. Start-party records and rule-clear persist in the local control flow.','known_unreached_local_cleanup':'On exception propagation, these wrappers have no local rescue/ensure: post-yield spriteset recreation, fade pop/audio resume, memorized/next-battle clears, encounter-step reset, viewport disposal/in_battle=false, after_battle, input update and set_outcome are not reached locally.','unknown':'Actual resource/host behavior and any farther enclosing recovery; no proof of process crash or permanent global state.'},
 'counter_arguments':[{'attempt':'Player no-able skip or empty-party construction rejects it first.','result':'REJECTED','reason':'Skip checks player only; fixed player is healthy. P2 length1 passes construction despite HP0.'},{'attempt':'Use existing NPC invalid-owner/has-no-able behavior.','result':'REJECTED_FOR_THIS_ORDER','reason':'Wild count synchronizes sides before those owner checks, so the default equal-layout failure occurs earlier.'},{'attempt':'Treat absent count as0.','result':'REJECTED','reason':'Actual sparse producer does not initialize a zero item; this idealizes source behavior.'},{'attempt':'All layouts fail first in the same enumeration.','result':'SUCCESSFUL_NARROWING','reason':'For explicitly unequal2v1 with one healthy player, only wild side becomes absent; player enumeration can complete and later layout consumers fail. Do not universalize the default first error.'}],
 'state_paths':{'normal':'Single healthy existing object produces normal eligibility count; all-healthy1/2/3 rules remain.','failure':'Default equal1v1 general pre-core exception, not a controlled skip, empty-party error or dedicated abort0.','cancel':'Default wrapper can_override=false, so override cancellation excluded; explicit override and player-no-able/debug skips are independent earlier paths. No input menu cancellation occurs inside this failing participant check.','exception_partial_commit':'Prefix retained locally; later standard cleanup unreachable as described, farther host recovery unknown.'},
 'minimum_revision':'Add a named existing-wild zero-able boundary to WP39 §3.3/§4.3/§9: absent count and pre-owner-check first failure for equal default layout; distinguish player skip and existing-NPC failure. Record committed records/rule-clear and local skipped cleanup, preserve host limits.',
 'acceptance':['HP1/HP0 isolated contrast identifies exact first stage and no numeric0 normalization.','Keep BC19 NPC invalid-owner and BC20 sparse intermediate-owner comparison as different preconditions.','Explicit unequal layout is not mislabeled as the same first failure.','Keep no-player-able and debug skip guards; all vectors NOT_EXECUTED.']
}
mixed={
 'facet_id':'MIXED_ORDER','recommendation':'SUSTAINED_REQUIRED','severity_recommendation':'P2','root_cause_key':'wild-positive-able-count-layout-versus-all-input-slot-order','mechanical_root_relation':'Distinct from the absent-count root: positive count exists and participant checking completes; the mismatch is filtering/counting eligibility for layout while constructing every input in original order.',
 'finite_fixture':'Ordinary direct wild core or default wrapper; player one healthy non-egg, no active partner/noPartner, DEBUG false, no variant/override/plugin; P/Q ordinary existing non-egg CATERPIE, SHIELDDUST/no item, P HP0, Q healthy, ordinary nonempty valid moves (TACKLE/STRINGSHOT). No form handler or external write alters HP/order. Prior resources/scenes/logging return normally; this is author-provided existing-object input, not a claim generated encounters routinely contain fainted members.',
 'ordinary_control':{'input':'All healthy [P,Q]','derived':'Default2v2 reduces to1v2 for one healthy player; seats1/3 both fall in max3 and both living wilds are in full priority.'},
 'minimal_counterexample':{'input':'Existing ordered [P HP0,Q healthy]','derived':['Initial2v2 synchronizes to1v1 from positive able count1, participant check completes.','Player seat0; wild P seat1 and Q seat3, because wild creation does not filter able or truncate by synchronized side size. Both wild identities receive explicit wild entering hook/seen/used-prefix processing.','AI wrappers are built for all existing seats0/1/3. The command phase scans all existing slots, skips faintedP, and reaches default enemy command for Q3. Wild ownership resolves trainer0; ordinary CATERPIE remains skill0, rejects switching, has no trainer items/Mega, and has valid positive move candidate weights.','Full priority construction only considers configured indices0..1; its stored entries0/1 omitQ3. Living normal priority yields only0, while allBattlers yields0/3. Ordinary and forced/Quash move scans and incremental priority never insert the omittedQ.','Conditional on normal command/scene returns and Q remaining healthy with UseMove, it is eligible for command but omitted from this ordinary action scan. No assertion of completed fight, final target outcome or eventual victory.'],'execution':'NOT_EXECUTED'},
 'order_only_control':{'input':'Reverse only input order to [Q healthy,P HP0], preserving all identities/state.','derived':'Still synchronized1v1 and two wild slots. Q at1 is now inside0..1 and living priority; faintedP at3 is outside but not a pending normal mover. This is an order-only active-scheduling control, not a promise the entire atypical scene is normal.'},
 'consumer_reception':{'entry_effects':'pbOnAllBattlersEnteringBattle builds living index requests from allBattlers but actual per-member entry effects iterate speed priority; Q3 is therefore omitted there, despite earlier explicit wild peer hook/seen and later allBattlers form checks.','ai':'Actual real receiver initializes AIBattler at3 and chooses ordinary move using the actual current battle; skill0 path/owner resolution read, not inferred merely from a method definition.','scene':'Scene creates boxes/sprites for all existing slots and wild sprite changes for the full wild input. Single-side position/box functions have no offset lookup for sideSize1, so index3 is not intrinsically rejected there; target buttons and later intro data-box/cry passes use configured side sizes. This proves inconsistent static request sets, not pixels, visible overlap, sound or real animation success.','judgment':'No immediate initial judge gate before commands. Normal later judgment uses participant-party able count, so livingQ in party prevents claiming an automatic victory merely because priority omits it.'},
 'counter_arguments':[{'attempt':'Wild seat construction filters fainted members or checks side size.','result':'REJECTED','reason':'The complete wild branch iterates every party item and uses original input position; trainer/player branch alone uses able filtering/required seats.'},{'attempt':'AI and command loops use the same configured range as priority.','result':'REJECTED','reason':'They scan actual battlers; allBattlers also sees livingQ3. Their object existence does not prove Q acts, so action consumers were independently read.'},{'attempt':'Incremental order/entry processing repairs missingQ.','result':'REJECTED','reason':'Incremental recalculation only revisits existing priority entries; entry core also uses that priority. Separate form checks are not an insertion.'},{'attempt':'Ordinary scene must fail on index3 before commands.','result':'REJECTED_AS_UNCONDITIONAL','reason':'Real initialization creates index3 objects; size1 geometry/boxes use parity/base rather than out-of-range offsets. All media/host callbacks are still assumed normal for the conditional command observation; real execution remains unverified.'},{'attempt':'Any explicit layout or partner produces the same exclusion.','result':'SUCCESSFUL_NARROWING','reason':'3v1 with three healthy player members yields max4 and includesQ3. Active healthy partner in default two-input battle can instead fail player-owner-position checking after synchronization to1v1. These are not counterexamples to the bounded no-partner/default fixture.'}],
 'state_paths':{'normal':'All healthy1/2/3 counts/seat identities consistent, ordinary player shortage reduction retained.','failure':'Main mixed non-egg example has no inherent participant exception; it creates an extra living object beyond the configured action range. Egg input fails earlier at active-creature initialization.','cancel':'Earlier override/player skip or an actual command ending battle can prevent the observation; the conditional vector excludes them. Ordinary command cancellation keeps existing command semantics and does not repair the participant mismatch.','exception_partial_commit':'If seat creation, form hook, seen registration or media later fails, previously created seats/hooks/records remain locally committed; no rollback/complete-host exit promise. Main vector requires those relevant callbacks to finish.'},
 'minimum_revision':'WP39 must separately describe the positive-able-count/full-input-order boundary and bounded identity trace. WP40 §6.1 current unqualified existing-seat participant set must refer to the configured range and link this boundary. Synchronize BC/CM vector identity sets. Read-receive WP51 and WP67A, qualify their start-chain summaries where needed; do not change correct AI formulas or claim visual observations.',
 'acceptance':['Both input permutations give equal1v1 layout but different living included identity; record built slots and ordinary-priority members separately.','Explicit3v1 player3-alive contrast includesQ3 and blocks universal exclusion claims.','Egg mixed input distinguishes its construction failure from non-egg HP0; record partial seat creation if asserted.','No automatic victory, no guaranteed UI appearance and no claim all command-enumerated members act.','Retain CM07/08 and ordinary all-healthy1/2/3/no-partner player-shortage cases; vectors NOT_EXECUTED.']
}
second={
 'id':'GR8-COM-002','recommendation':'SUSTAINED_REQUIRED_WITH_TWO_DISTINCT_FACETS','classification_recommendation':'required','severity_recommendation':'P2','primary_wp':'WP39','status':'INDEPENDENT_COUNTER_REVIEW_COMPLETE_ROOT_CANONICAL_SPLIT_PENDING','canonical_recommendation':{'retain_proposal_id':True,'do_not_renumber_in_this_task':True,'recommend_distinct_root_keys':True,'reason':'A nonzero/non-sparse count can still trigger MIXED_ORDER, and fixing zero-count semantics alone would leave it. Conversely filtering positive mixed construction does not determine the all-zero first failure. Root may assign a successor stable ID or preserve linked facets but must not count the same historical NPC correction twice.','old_root':'GIR-FD82-B002 / raw RUN-B-002','historical_reopening':False,'new_canonical_ids':'ROOT_TO_ASSIGN'},
 'bidirectional_evidence':[
 loc('WP39',[[49,74],[86,120],[127,140],[159,180],[184,211],[279,302]],'Full main contract permits existing objects and sparse count yet lacks the named wild-zero and mixed-order contracts.'),
 loc('WP40',[[51,64],[124,142],[253,270]],'Command and action stages; participant set at §6.1 unqualified existing seats is overbroad for mixed fixture.'),
 loc('BC_CM',[[5,39],[41,77]],'BC02/09/14/16/19/20 and CM controls distinguish current correct scope; no mixed-order identity vector.'),
 loc('WP42',[[25,55],[251,257]],'Party-based outcome guard and separate exception/abort boundaries; not evidence every construction error is caught.'),
 loc('WP51',[[13,27],[132,148]],'Actual-seat choice, skill0/weighted-selection semantics retained; not an action scheduling guarantee.'),
 loc('WP67A',[[30,43],[315,334]],'Start and failure summaries need bounded reference to the corrected participant contract; host/media unknown.'),
 loc('CREATE',[[110,123],[141,201],[209,304],[354,441]],'Only-player skip, identity reuse, partner entry, rules/defaults and complete ordinary wild core.'),
 loc('TRAINER',[[57,78]],'Actual player eligibility receiver counts non-eggs that are not fainted.'),
 loc('POKEMON',[[214,217],[244,283]],'Egg identity, HP0 setter and strict able predicate; persistent HP0 is valid.'),
 loc('BATTLE',[[98,174],[179,239],[329,380],[400,411],[448,479]],'Nonempty construction, mode/max index, sparse count, ownership and living actual-seat sets.'),
 loc('START',[[16,165],[170,276],[279,347]],'Full ensure, actual wild seat creation, dedicated abort scope and no pre-command initial judging.'),
 loc('INITIALIZE',[[1,280]],'Actual seat receiver rejects egg, copies HP without generic heal and creates normal flags; full relevant unit read.'),
 loc('PEER',[[39,58]],'Starting/entering form callback stages do not constitute generic heal/filter.'),
 loc('FORM',[[4,35]],'Default species callback lookup and absent callback result; no CATERPIE registration/copy/conditional fallback located in Scripts.'),
 loc('FORMCHECK',[[189,295]],'CATERPIE avoids listed weather/entry form branches.'),
 loc('PBS_SPECIES',[[237,261]],'Ordinary finite CATERPIE identity, moves and no legendary flags.'),
 loc('PBS_MOVES',[[327,336],[5326,5336]],'Default STRINGSHOT/TACKLE PP, target and effect fields support the finite ordinary AI candidate path.'),
 loc('SWITCH',[[303,363]],'Entry request living sets versus priority-consumed effects; separate later form checking.'),
 loc('PRIORITY',[[136,278]],'Configured max-index full construction, incremental retained membership, living versus speed-only consumers.'),
 loc('COMMAND',[[35,40],[174,264]],'Actual battler-length scans and AI invocation at healthy slot3.'),
 loc('ATTACK',[[1,202]],'All ordinary attack action and completion scans consume priority; no insertion of index3.'),
 loc('AI',[[10,69]],'Actual all-seat AI wrappers, owner and default command receiver.'),
 loc('AITRAINER',[[28,99]],'Wild skill applies using initial wild member, nonlegendary skill0 flags.'),
 loc('AIBATTLER',[[8,47]],'Index3 wrapper and refresh use actual index, not configured maximum.'),
 loc('AIMOVE',[[23,171],[232,324],[330,392]],'Choice path examines current legal targets and adds weights/registration; skill0 avoids prediction handlers.'),
 loc('SCENEINIT',[[14,92],[183,190]],'Real ordinary scene uses actual existing slots and full wild input for sprites.'),
 loc('SCENEPOS',[[33,53]],'Single-side geometry uses base positions for index3 without double/triple array offset.'),
 loc('SCENEBOX',[[28,103],[286,333]],'Single-side box selects by parity, not a fixed single-slot index bound.'),
 loc('SCENEMENU',[[459,485]],'Target window uses configured maximum; unequal zero-able variant can fail on absent side size here if earlier callbacks finish.'),
 loc('SCENEPLAY',[[5,55]],'Wild data-box/cry/shiny initialization passes use configured side size.'),
 loc('SCENEANIM',[[4,79]],'First wild slide uses full party; later normal-tone/cry pass uses configured wild size.'),
 loc('OUTER',[[51,152]],'Normal-return-only map/audio/fade/in_battle cleanup, no local recovery around yield.'),
 loc('BSETTINGS',[[8,19],[135,139]],'Generation-dependent recalculation default and ordinary wild skill setting.'),
 loc('OLD_B002',[[840,930]],'Recovered original qualified NPC root and original case IDs; candidate status retained as historical.'),
 loc('B7_WP39',[[159,165]],'Existing NPC sparse clauses already in R7 baseline, unchanged at B8 in these lines.')
 ],
 'facets':[zero,mixed],
 'independent_variants':[
 {'id':'CC2_SKIP_PLAYER','change':'Player no able member, any existing wild HP state, no debug overriding other guard.','derived':'Direct core returns skip result before start records/parse; wrapper may already have parsed objects. Does not establish the zero-wild failure.','execution':'NOT_EXECUTED'},
 {'id':'CC2_EGG_ZERO','change':'Single existing egg, positive HP, healthy player/default equal1v1.','derived':'No able first count; earlier absent-layout failure precedes the active-egg guard. Egg is excluded from able count independently of HP.','execution':'NOT_EXECUTED'},
 {'id':'CC2_EGG_MIXED','change':'One healthy non-egg plus egg in either order.','derived':'Positive count permits participant phase; unfiltered wild setup later hits explicit active-egg rejection. An egg-first input has blank/partially created slot before initialization rejection; alive-first preserves its completed earlier slot/hooks. Not the non-egg mixed action vector.','execution':'NOT_EXECUTED'},
 {'id':'CC2_UNEQUAL_ZERO','change':'One healthy player, single HP0 wild, explicit2v1 and no partner.','derived':'Player count check lowers player2→1 while wild side absent is skipped by that checker. First default nil enumeration claim no longer applies; after subsequent normal hooks/setup, target-menu layout comparison may fail on absent side. No full downstream or host guarantee.','execution':'NOT_EXECUTED'},
 {'id':'CC2_TRIPLE_POSITIVE','change':'Mixed[P HP0,Q healthy], explicit3v1, player3healthy, no partner.','derived':'Sides remain3/1, max index4 includes Q3. Refutes any all-layout exclusion statement while retaining eligibility/layout mismatch.','execution':'NOT_EXECUTED'},
 {'id':'CC2_PARTNER','change':'Mixed two-input fixture, one healthy player and one healthy active partner, no explicit size/no noPartner.','derived':'Partner initially supplies two owner segments; wild count1 changes equal2v2→1v1. Required player positions cover owner0 only while owner1 has positive count: player-side no-battler-position error before seat construction. Parent default no-partner premise is necessary.','execution':'NOT_EXECUTED'},
 {'id':'CC2_THREE_HEALTHY','change':'All-healthy three wilds with one healthy player/no partner.','derived':'Default3v3 then player-side shortage reduces to1v3; wild slots1/3/5 fit max5 and are in priority. This preserves supported ordinary3-wild behavior.','execution':'NOT_EXECUTED'}
 ],
 'negative_evidence':{'scope':'Own fixed-Scripts searches plus full WP39/WP40/WP48/WP51 and explicitly bounded related tests/WP42/WP67A; all131 formal Markdown searched for identities/named wild states after byte-equality check.','io_records':['io/0035.json','io/0073.json','io/0082.json','io/0100.json'],'semantic_conclusion':'No matching complete wild-zero or mixed-order contract in the read primary units. NPC paragraph and BC19/20 cover a different first-consumer/order. Searches alone do not prove absence of arbitrary paraphrases in unread clauses.','not_claimed':'Full all131 semantic read, all AI/scene combinations, absent arbitrary dynamic plugin behavior.'},
 'correct_preserve_scope':['Existing-object identity reuse and exactly-once species/level construction','Player-only no-able/debug guard and distinct wrapper/direct-core order','All-healthy1/2/3 and explicit BC16 synchronization (which may increase a prior rule size); only the later shortage loop merely reduces player side','NPC BC19/20 exact first failures and historical closure','Egg rejection, command registration/execution split and actual-seat versus priority-set distinction','WP42 party-based judgment and ordinary exception/abort separation','No future data representation/engine or mandatory defect-compatibility decision'],
 'minimum_revision_contract':{'required_write_set':[paths['WP39'],paths['WP40'],paths['BC_CM']],'shared_sync_review_set':[paths['WP51'],paths['WP67A'],paths['WP42'],paths['AI_TEST']],'necessary_sync':'WP40 §6.1 must qualify the existing-seat ordering set for the mixed edge. WP67A §3.2/§12 should use the primary participant contract for atypical input and not imply that all failures are numeric reduction-to0. WP51 requires receiver reception rather than changing its correct weighted AI rules. WP42 current exception/party guards are correct; add a reference only if integration makes it necessary. Public index/test counts are a unique integrator responsibility.','compatibility_policy':'Document reference defect first. Whether a future implementation rejects, normalizes or reproduces it is a separate user compatibility policy; it does not block correcting reference facts and cannot silently prescribe idealized source results.','architecture':'No Ruby arrays/nil operations required in future framework; state identities, first failure and finite observation sets suffice.'},
 'acceptance_and_regression':['CC2 ordinary healthy/singleHP0 and mixed permutations independently preserve exact prefix and observation identity.','BC02 identity reuse; BC09 player-no-able; BC11/12 partner eligibility; BC13/14 shortage; BC15 trainer rejection; BC16 explicit synchronization; BC19/20 sparse NPC boundaries remain valid.','CM07/08 sorting controls, AB04 incremental bracket retention, AI A01/M02/M03 skill0 and ordinary phase scan semantics remain.','Record no reference/model/host execution; never relabel derived vectors as observed.','Independent non-author review of final shared WP39/WP40/test result plus AI/UI receiving review; explicit root canonical split/dedup.'],
 'dependencies':{'blocking_final_acceptance':['Root canonical split/dedup/classification','Shared WP39/WP40 and BC/CM integrator','AI/UI receiving owners for scoped summaries'],'nonblocking':['Exact farther host recovery','Future compatibility policy for defect reproduction'],'direct_ids':['GR8-COM-001 shares WP40/tests only; not a semantic prerequisite'],'file_conflicts':[paths['WP39'],paths['WP40'],paths['BC_CM'],paths['WP67A']],'batch':'ROOT_TO_ASSIGN'},
 'unresolved':['Actual full host/media outcome and farther recovery are unverified.','Full independent coverage/reception of all combat/AI domains is outside this task.','Canonical stable successor ID for the two source roots is reserved to root; no old ID is reopened.'],
 'excluded_claims':['All generated wild encounters can be fainted','Any egg/non-able input has same first failure','All layouts exclude the living later wild','All existing seats participate in ordinary action priority','Guaranteed final target/UI/AI strategy/battle outcome','Required future replication of source arrays or flaws']
}
adj={'schema':'r8.counter-review.adjudications.v1','created_utc':NOW,**common,'fixed_baseline':{'commit':BASE,'tree':'751dfde81048c81390f89a65ca1d1a565ba8e1ca','formal_tree':'f292698cdd4a8e725525a9be6dc34b75faaf151e'},'reference':{'repo':RROOT,'commit':REF,'tree':'7589c800b61ba13a13040ed0d686979b80a84fd0'},'records':[first,second],'counts':{'reviewed_proposals':2,'sustained_required_proposals':2,'proposed_root_keys':3,'final_canonical_required_count':'ROOT_PENDING','optional_records_created':0,'policy_records_created':0,'limit_records_created':0},'io_index':'read-ledger.json#/tool_operations','evidence_binding':'evidence-bindings.json','semantic_completion':'Only the two delegated findings and explicitly bounded prerequisite/consumer units. No full-combat or whole-round PASS.','update_started':False,'update_state':'UPDATE_NOT_STARTED'}
dump('adjudications.json',adj)
report='''# R8 独立反证：GR8-COM-001／GR8-COM-002

实际任务入口 `/root/counter_combat_first`，原提出者 `/root/combat_review`；本任务是不同上下文中的非提出者。开始/结束及原始工具 I/O 见 `progress.json` 和 `io/`。请求 gpt-6.1-sol／ultra／default 普速／Fast off；实际 model、effort、tier、speed、平台 UUID 均未回显，记 `UNVERIFIED`。本任务未修改正式规格、未 commit/push、未安装软件、未自行分派。

B8 固定 `fd1df570cad987dc3852a3b958f03916e317f7fe`，workspace tree `751dfde81048c81390f89a65ca1d1a565ba8e1ca`，formal tree `f292698cdd4a8e725525a9be6dc34b75faaf151e`；R 固定 `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`／`7589c800b61ba13a13040ed0d686979b80a84fd0`。实查当前项目 HEAD 为合法报告后继 `7478d8daf357d569ac12bea211b4b5f257861930`，受审仍是 B8。源432个 tracked 文件及131个正式文件的当前字节与固定对象一致只用于检索身份，绝不作为全量语义阅读。交付 tag 在此本地克隆无法解析，精确失败保留 `io/0083.json`；不据此阻塞固定 commit 的本任务审读，远端/全局追溯由 root 处理。

## 裁决建议

| 提案 | 建议 | 限定范围 |
| --- | --- | --- |
| GR8-COM-001 | SUSTAINED_REQUIRED，P3 | 修正 WP40 档内特性例子的身份措辞；不宣称当前全文明确赋 TRUANT −1，亦不宣称参考运行排序错误 |
| GR8-COM-002 ZERO_ABLE | SUSTAINED_REQUIRED，P2 | 默认相等布局、健康玩家、既有非蛋 HP0 野生对象：缺项计数先进入布局，早于 NPC 业主失败与专用中止捕获 |
| GR8-COM-002 MIXED_ORDER | SUSTAINED_REQUIRED，P2 | 正计数但按全部输入建席；默认 [HP0,健康] 的活对象在席3、配置上界1，命令可达而普通行动优先序遗漏 |

这是两项提案的局部独立裁决，最终 canonical 数量待 root。002 两 facet 有不同源机械根因，建议拆分 root key 或以明确关联的独立合同保留；本任务不改稳定 ID，也不重开旧关闭项。

## 001：最强反证和保留结论

全文读取 WP40/WP48 后，确有重要反证：WP48 §3 和 §9 已完整、正确且唯一列出 QUICKDRAW／STALL，因此完整关联阅读可以恢复正确意图。本轮不能把局部措辞缺陷升级成全局缺失规则或已发生的错误运行。

但 WP40 §5.4 的“懒惰”指交替不能行动，§5.2.1 也把它归入动作拒绝；同文 §6.1 又以“如懒惰类”举档内排序例。实际排序 receiver 先查询有效能力的档处理器，未登记返回0；STALL 为−1，TRUANT 在状态/服从之后才切换动作门。用明确 STALL 原位替代可消除身份冲突，保留全部正确合并、空间、平局及重算规则。

有限对照为同优先级/无物品/无空间，A速100、B速50：A有效STALL则B先，只有A身份改为本次可动的TRUANT则A先。此对照说明错误身份解释的影响，不是对错误文本强行赋予一个未写出的数值规范。最小必写是 WP40；新增一条具名测试可选，已有CM07/08、AB04应保留并静态回归。

## 002：创建、首次失败与消费者

完整读取普通野生创建入口、玩家准入守卫、构造/计数/参与校验/建席、真实 Battler 接收者、默认 AI 创建与选择、命令与攻击扫描，以及相关场景/过渡消费者。既有个体直接复用；玩家可战数守卫只问玩家，非空构造不检查对手HP；HP0非蛋是有效持久个体输入。这是作者已有对象夹具，不声称自然生成遭遇常产生濒死野生。

ZERO_ABLE 正常对照是单既有对象HP1，只改HP0：玩家仍健康而不 skip，开战等级/会心/直伤记录及创建规则清空已提交。可战计数没有第一项；默认1v1的两尺寸因此成为缺项；首次玩家侧枚举先一般异常，未到业主范围/无可战消息、开战形态处理、建席、场景开战或专用中止catch。零值不能替代缺项。此路径不返回普通决定码或包装布尔。

外层过渡与地图待机包装已完整读取：本地没有包围 yield 的 rescue/ensure。若异常向外传播，已发生的 in_battle=true、暂停/过渡/fade及适用地图spriteset销毁保持，本地 yield 后的重建、恢复音频、清备忘/下一战、重置遭遇步数、销毁视口和 in_battle=false 均未到达。更外层异常处理与真实宿主恢复未知；不能说必崩溃或全局永不恢复。

MIXED_ORDER 使用 P=HP0/Q=健康的普通非蛋CATERPIE、单健康玩家、无伙伴/覆写/变体：默认2v2按正可战数1同步1v1，却仍建立P席1、Q席3。真实AI对象按全部既存席位建立，命令按对象长度扫描、能到健康Q3；所有权在野生侧归默认决策档，CATERPIE技能0、无主动道具/换人/Mega阻断，并有普通正权重招式候选。全量优先序只构造配置0..1，增量也只重访已有条目；普通行动与其完成判定均读该序。故在相关场景和命令正常返回、Q仍健康且选择UseMove的有限观察点，Q可有命令而没有本次普通行动候选。仅反转输入为[Q健康,P HP0]，同样1v1下Q变席1而被纳入。这一反序只证明动作纳入对照，不保证整个异常场景是普通正常呈现。

入场请求也不能混同：显式野生peer入场、已见/已用前缀已覆盖全输入，后续统一入场效果实际按速度优先序消费，Q3可被遗漏；最后另有全存活对象形态检查。场景创建按全部既存席建图，但目标按钮和后续野生数据框/叫声等按配置尺寸遍历。单席几何及数据框的索引3不会仅因下标自动越界；仍不把静态请求集合当最终像素、声音或完整动画证明。普通裁判按参与队伍可战数，并无开场后、命令前统一裁判，因此不能由优先序无敌方推出自动胜利。

## 独立反证成功的限制

- 玩家无可战成员，直接核心先skip；包装可能此前已解析对象。此门不能替代健康玩家主例。
- 单蛋的默认零可战路径先走缺项布局错误，未到蛋拒绝；混合蛋+健康非蛋则可过正计数但在未筛建席时走显式蛋拒绝。顺序影响此前已完成的建席/钩子前缀，与HP0非蛋主例不同。
- 显式不对称2v1且单健康玩家时，零可战只污染野生侧；玩家校验可先降为1，默认同一首次枚举错误不再成立。其后无新改写且相关创建正常时，场景目标窗口等布局消费者可先失败，不普遍指定同一异常点。
- 显式3v1并有3名健康玩家成员时，上界4包含Q席3，反驳“所有布局都遗漏”。默认两输入同步1v1主例保持。
- 默认两输入加健康有效伙伴时，玩家侧两个正计数业主在同步1v1后先遇无席位错误，早于混合建席；noPartner/无伙伴主例的前提不可删除。
- 全部健康1/2/3野生及玩家缺员1v2规则保留。既有BC16的同步本身可将规则1v1改为2v2；只删减应继续限定后续缺员缩减循环，不能用它改写源同步数学。

## 历史与最小接收范围

旧NPC项准确ID为 `GIR-FD82-B002`（raw `RUN-B-002`），历史候选证据位于 `d15259042aa6665b3fa75786a4d3650d702cab5c:review/remediation/20261003-prepare/batches/B09/candidate-1/contribution-dispositions.json` 840–930。它明确接收已有NPC全濒死与中间业主空计数，当前BC19/20保留。B7的WP39 159–165已含同一现行稀疏合同；并非R7刚新增。历史候选当时OPEN/待审状态不倒填成关闭，当前资格由root历史接收链确认。

ZERO_ABLE与旧根共享缺项计数生产，新增野生同步先消费的缺口。MIXED_ORDER则计数为正而正常存在；只修缺项无法解决它，不能因为都叫野生输入而丢一个反例。建议root将两个机械root分别跟踪，既保留新facet也不重复计旧NPC已修事实。

最小必写WP39、WP40 §6.1及BC/CM目录；WP40目前“现有席位”总括需与配置排序范围一致。WP67-A开战/失败摘要应接收主合同边界，WP51正确AI主体与权重规则只需接收验证；WP42现有按参与队伍裁判、普通异常与专用中止分层正确，按整合需要加引用即可。正式公共文件由唯一整合者修改，本任务仅产审计资料。是否在未来复刻该缺陷是独立兼容政策，不阻塞记录参考事实，也不能暗改为理想拒绝/自动过滤行为。

完整逐项定位、bytes/SHA256/blob/commit/tree、普通/最小/失败/取消/部分提交、反证、验收/回归、保留范围与未决见 `adjudications.json` 和 `evidence-bindings.json`。连续读集/片段边界及原工具I/O见 `read-ledger.json`。这里不宣称全部combat、全部AI或整轮PASS。

所有行为向量 `NOT_EXECUTED`；参考观察0、独立行为模型0、真实宿主0。`UPDATE_NOT_STARTED`。
'''
(ROOT/'review.md').write_text(report)
p=ROOT/'progress.json';pr=json.loads(p.read_text());pr.update(updated_utc=NOW,ended_utc=NOW,started_utc_semantics='First persisted local registration after prerequisite reads; true platform task start UTC not returned',actual_platform_task_start_utc='UNVERIFIED',ended_utc_semantics='Scoped semantic result prepared; true platform turn exit occurs after handoff and is not observed here',actual_platform_exit_utc='UNVERIFIED',status='COMPLETED',platform_process_status='RESULT_PREPARED_TURN_HANDOFF',semantic_reception='PENDING_ROOT_CLASSIFICATION_AND_DEDUP',stage='Scoped independent counter-review complete',outputs=['progress.json','read-ledger.json','adjudications.json','review.md','evidence-bindings.json','io/'],completed=['Full assigned proposals and exact B8 WP39/WP40/WP48/WP51 read','Bounded prerequisite creation/default/real receiver and consumer chains independently read','Two proposal recommendations and two distinct COM002 facet roots retained','Historical NPC sparse root and B7 clause scope recovered','All derived vectors NOT_EXECUTED; no source/spec edits'],remaining=['Root canonical split/dedup/classification','Shared AI/UI/formal integration reception','Unverified actual host/configuration and farther recovery'],limits=['This is only GR8-COM-001/002 counter-review; not all combat/AI or entire R8 PASS.','Actual model/effort/tier/speed/platform UUID unverified.','No reference/model/host behavior execution.','Local delivery tag unresolved; fixed commit/tree remains readable; global remote qualification remains root-owned.'],update_started=False,update_state='UPDATE_NOT_STARTED');dump('progress.json',pr)
print(json.dumps({'status':'WRITTEN','outputs':pr['outputs'],'io_records':len(ops),'payload_read_identities':len(groups),'behavior_execution_count':0,'update_state':'UPDATE_NOT_STARTED'},ensure_ascii=False,indent=2))
